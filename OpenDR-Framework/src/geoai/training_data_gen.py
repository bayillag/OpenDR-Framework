import geopandas as gpd
import numpy as np
from shapely.geometry import Point

def generate_training_samples(roi_gdf, num_points=1000):
    """
    Implements Ocular Sampling logic (Ch 52) to create 
    Presence/Absence points for hazard training.
    """
    bounds = roi_gdf.total_bounds
    lon_min, lat_min, lon_max, lat_max = bounds
    
    points = []
    while len(points) < num_points:
        p = Point(np.random.uniform(lon_min, lon_max), 
                  np.random.uniform(lat_min, lat_max))
        if roi_gdf.contains(p).any():
            points.append(p)
            
    samples = gpd.GeoDataFrame(geometry=points, crs="EPSG:4326")
    samples['class'] = 0 # Default to 'Absence' (Stable)
    
    return samples