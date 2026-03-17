def calculate_population_exposure(hazard_geom, building_gdf):
    """Spatial join between hazard and Google Open Buildings."""
    exposed_buildings = building_gdf[building_gdf.intersects(hazard_geom)]
    # Apply population weighting
    impact_score = len(exposed_buildings) * 1.25 # Sample weighting
    return impact_score