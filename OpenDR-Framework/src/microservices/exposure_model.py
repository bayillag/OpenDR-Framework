import geopandas as gpd
import pandas as pd

def calculate_population_exposure(hazard_geom, building_gdf):
    """Spatial join between hazard and Google Open Buildings."""
    exposed_buildings = building_gdf[building_gdf.intersects(hazard_geom)]
    # Apply population weighting
    impact_score = len(exposed_buildings) * 1.25 # Sample weighting
    return impact_score


def calculate_impact_metrics(hazard_gdf, buildings_gdf, population_raster):
    """
    Calculates population-weighted exposure for a detected hazard.
    1. Intersects hazard extents with Open Buildings.
    2. Weights the impact by the local population density.
    """
    # Spatial Join: Buildings within the hazard zone
    impacted_buildings = gpd.sjoin(buildings_gdf, hazard_gdf, predicate='within')
    
    # Calculate weighted metric: Impact = sum(Building_Area * Local_Pop_Weight)
    # This ensures that a flood in a high-density informal settlement 
    # results in a higher alert priority than an empty warehouse district.
    impacted_buildings['impact_score'] = impacted_buildings['area'] * impacted_buildings['pop_density']
    
    summary = {
        "total_buildings_affected": len(impacted_buildings),
        "estimated_displaced_persons": impacted_buildings['pop_density'].sum(),
        "high_priority_infrastructure": impacted_buildings[impacted_buildings['type'] == 'hospital'].count()
    }
    
    return summary
