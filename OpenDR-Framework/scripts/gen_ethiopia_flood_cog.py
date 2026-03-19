import os
import numpy as np
import rasterio
from rasterio.transform import from_origin
from pathlib import Path

def generate_flood_cog():
    """
    OpenDR 1.0 Data Generation Utility
    Pillar: Hydrology & Subsurface Extraction
    Logic: Markert et al. (2024) - SAR Flood Extraction Proxy
    """
    print("[*] OpenDR 1.0: Generating Ethiopia Flood Sample (SAR COG)...")

    # 1. Setup target directory
    output_dir = Path("data/sample")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "flood_mask_cog.tif"

    # 2. Define Image Dimensions and Spatial Metadata
    # Location: Machar Marshes/Gambella Region (Case Study B)
    width, height = 512, 512
    # Upper left corner (Lon, Lat) and pixel resolution (approx 10m in degrees)
    lon_ul, lat_ul = 34.12, 8.45
    res = 0.0001 
    transform = from_origin(lon_ul, lat_ul, res, res)
    crs = 'EPSG:4326'

    # 3. Create Synthetic SAR Backscatter (FLOAT Power Scale)
    # Background "Land" noise (higher backscatter: 0.15 - 0.40)
    data = np.random.normal(0.25, 0.05, (height, width)).astype('float32')

    # Insert "Flood" anomaly (specular reflectance = very low backscatter: < 0.05)
    # We simulate a river/wetland feature
    flood_zone = np.zeros((height, width), dtype=bool)
    # Draw a diagonal 'river'
    for i in range(height):
        center = int(width/2 + np.sin(i/50)*40)
        flood_zone[i, center-15:center+15] = True
    
    # Draw a localized 'marsh' expansion
    flood_zone[200:350, 100:250] = True
    
    # Apply low backscatter values to the flood zone
    data[flood_zone] = np.random.uniform(0.01, 0.04, size=data[flood_zone].shape)

    # 4. Write as Cloud-Optimized GeoTIFF (COG)
    # Requirements: Tiled, Blocked, Internal Overviews
    with rasterio.open(
        output_path, 'w',
        driver='GTiff',
        height=height,
        width=width,
        count=1,
        dtype='float32',
        crs=crs,
        transform=transform,
        tiled=True,
        blockxsize=256,
        blockysize=256,
        compress='deflate',
        interleave='pixel'
    ) as dst:
        dst.write(data, 1)
        
        # Build overviews (Pyramids) - Essential for CNG Tier 1 performance
        overviews = [2, 4, 8, 16]
        dst.build_overviews(overviews, rasterio.enums.Resampling.average)
        dst.update_tags(ns='rio_overview', resampling='average')

    print(f"[+] Success: Created Cloud-Native SAR sample at {output_path}")
    print(f"[*] Scientific Context: FLOAT Power scale initialized for Otsu Module.")

if __name__ == "__main__":
    generate_flood_cog()