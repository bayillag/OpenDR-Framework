"""
Script to download Google Open Buildings footprints 
for a specific Area of Interest (AOI).
"""
import pandas as pd

def download_by_s2_cell(s2_token):
    url = f"https://storage.googleapis.com/open-buildings-data/v3/polygons/{s2_token}.csv.gz"
    # Logic to fetch and convert to GeoParquet for OpenDR 1.0
    print(f"Fetching data from {url}...")