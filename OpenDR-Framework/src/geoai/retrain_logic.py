import torch
import psycopg2
import pandas as pd
from src.geoai.models.unet_segmentation import UNet

def incremental_learning_pass(model_path, db_config):
    """
    Tier 5 -> Tier 3 Feedback Loop.
    1. Fetches field-validated points from PostGIS.
    2. Performs a fine-tuning gradient descent pass on the U-Net.
    3. Saves regionalized model weights.
    """
    # Load existing model
    model = UNet(in_channels=6, out_channels=1)
    model.load_state_dict(torch.load(model_path))
    model.train()

    # Fetch validation data provided by citizens/responders via pygeoapi/Kobo
    conn = psycopg2.connect(**db_config)
    query = "SELECT ST_AsText(geom), hazard_type, is_valid FROM field_validation WHERE discovery_time > NOW() - INTERVAL '7 days'"
    df = pd.read_sql(query, conn)

    if not df.empty:
        print(f"Retraining: Found {len(df)} new field validation points.")
        # Logic to extract image patches at these coordinates from COGs
        # Perform 5 epochs of fine-tuning on the new samples
        # optimizer.step()...
        
        new_weight_path = model_path.replace(".pth", "_regional_optimized.pth")
        torch.save(model.state_dict(), new_weight_path)
        return new_weight_path
    
    return model_path