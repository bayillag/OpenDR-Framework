import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon
import os

def generate_plateau_sample():
    """
    Generates a mock GeoParquet file representing Project PLATEAU 
    building models for the Tokyo Urban Resilience case study.
    """
    print("[*] Generating Tokyo Building Sample (Project PLATEAU Proxy)...")
    
    # Define a small neighborhood in Tokyo (approx. Minato City area)
    # Coordinates match study_areas.geojson
    data = [
        {
            "building_id": "JP_TYO_001",
            "usage_code": 1, # Residential (from lookup/urban_vulnerability_weights.csv)
            "measured_height": 12.5, # Floor-level flood risk threshold
            "pop_density": 45.2, # Population weight for exposure modeling
            "geometry": Polygon([(139.752, 35.685), (139.753, 35.685), (139.753, 35.686), (139.752, 35.686)])
        },
        {
            "building_id": "JP_TYO_002",
            "usage_code": 4, # Emergency Services (Critical Priority)
            "measured_height": 25.0,
            "pop_density": 120.5,
            "geometry": Polygon([(139.755, 35.687), (139.756, 35.687), (139.756, 35.688), (139.755, 35.688)])
        },
        {
            "building_id": "JP_TYO_003",
            "usage_code": 5, # Transportation Hub
            "measured_height": 8.0,
            "pop_density": 350.0,
            "geometry": Polygon([(139.758, 35.682), (139.759, 35.682), (139.759, 35.683), (139.758, 35.683)])
        }
    ]

    # Create GeoDataFrame
    gdf = gpd.GeoDataFrame(data, crs="EPSG:4326")

    # Define output path
    output_dir = "data/sample"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    output_path = os.path.join(output_dir, "tokyo_buildings_sample.parquet")

    # Save as GeoParquet (CNG Standard)
    gdf.to_parquet(output_path, compression='snappy')
    print(f"[+] Success: Sample created at {output_path}")

if __name__ == "__main__":
    generate_plateau_sample()