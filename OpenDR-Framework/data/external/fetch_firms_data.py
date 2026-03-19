import pandas as pd
import requests
from io import StringIO

def fetch_realtime_hotspots(api_key, region="world"):
    """
    Polls NASA FIRMS for 24h active fire hotspots.
    FOSS4G logic: Converts CSV stream to GeoParquet for Tier 3 Joins.
    """
    url = f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{api_key}/MODIS_NRT/world/1"
    
    print("[*] OpenDR Ingestion: Fetching NRT Fire Hotspots (FIRMS)...")
    
    try:
        response = requests.get(url)
        df = pd.read_csv(StringIO(response.text))
        
        # Save as GeoParquet for cloud-native performance
        output_path = "data/external/fire/hotspots_nrt.parquet"
        df.to_parquet(output_path)
        print(f"[+] Success: {len(df)} fire pixels ingested to {output_path}")
    except Exception as e:
        print(f"[!] FIRMS API Error: {e}")

if __name__ == "__main__":
    # In practice, API Key is pulled from Tier 1 .env
    fetch_realtime_hotspots(api_key="YOUR_NASA_API_KEY")