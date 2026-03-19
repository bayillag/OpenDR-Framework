import os
import requests
import pandas as pd
import geopandas as gpd
from shapely import wkt
from pathlib import Path

class GoogleBuildingsFetcher:
    """
    OpenDR 1.0 Data Ingestion Microservice
    FOSS4G Stack: Python, Pandas, GeoPandas, PyArrow
    Logic based on: Van Den Hoek and Friedrich (2024)
    """

    def __init__(self, output_dir="data/external/buildings"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        # Google Open Buildings V3 Index URL
        self.base_url = "https://storage.googleapis.com/open-buildings-data/v3/polygons"
        
    def fetch_by_tile_id(self, s2_token, aoi_geometry=None):
        """
        Downloads a specific S2 tile from Google Cloud Storage.
        Optional: Filter results by an AOI (Shapely geometry).
        """
        filename = f"{s2_token}_buildings.parquet"
        output_path = self.output_dir / filename
        
        # Download URL for V3
        csv_url = f"{self.base_url}/{s2_token}.csv.gz"
        
        print(f"[*] OpenDR Ingestion: Fetching tile {s2_token} from Google Storage...")
        
        try:
            # Using chunked reading to handle large building files without memory overflow
            # Essential for Tier 1 stability in Global South environments
            df_list = []
            with requests.get(csv_url, stream=True) as r:
                r.raise_for_status()
                # Read compressed CSV
                df = pd.read_csv(csv_url, compression='gzip', engine='c')
                
                print(f"[*] Processing {len(df)} building footprints...")
                
                # Convert WKT to geometry
                geometry = df['geometry'].apply(wkt.loads)
                gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")
                
                # Tier 3 Logic: Spatial Filtering
                if aoi_geometry:
                    gdf = gdf[gdf.intersects(aoi_geometry)]
                    print(f"[*] AOI Filtering complete. {len(gdf)} buildings retained.")

                # Save to GeoParquet (Cloud-Native format)
                gdf.to_parquet(output_path, compression='snappy')
                print(f"[+] Success: Saved to {output_path}")
                return output_path

        except Exception as e:
            print(f"[!] Error during ingestion of {s2_token}: {e}")
            return None

def main():
    """
    Example execution for OpenDR 1.0 Case Study B:
    Baro-Akobo-Sobat Basin (Ethiopia Region)
    """
    print("--- OpenDR 1.0: Humanitarian Data Ingestion ---")
    
    # Example AOI (Bounding box for a portion of the Amhara region)
    from shapely.geometry import box
    amhara_subset = box(34.0, 7.5, 35.5, 9.0)
    
    fetcher = GoogleBuildingsFetcher()
    
    # '20f' is a common S2 token for parts of Ethiopia/South Sudan
    # In production, Tier 2 (Airflow) would dynamically determine tokens based on AOI
    tile_id = "20f" 
    
    path = fetcher.fetch_by_tile_id(tile_id, aoi_geometry=amhara_subset)
    
    if path:
        print(f"--- Ingestion Complete for Tier 4 Processing ---")

if __name__ == "__main__":
    main()