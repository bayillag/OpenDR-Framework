import xarray as xr

def calculate_saturation_threshold(grace_nc_path, region_geom):
    """
    Calculates the Total Water Storage (TWS) anomaly 
    to determine if the 'subsurface sponge' is full.
    """
    ds = xr.open_dataset(grace_nc_path)
    
    # Clip to Baro-Akobo-Sobat Basin
    regional_tws = ds.rio.clip([region_geom], ds.rio.crs)
    
    # Calculate anomaly relative to baseline
    tws_anomaly = regional_tws['lwe_thickness'].mean().values
    
    # Saturation threshold: If anomaly > 2 standard deviations
    is_saturated = tws_anomaly > (regional_tws.std() * 2)
    
    return {
        "tws_anomaly_cm": float(tws_anomaly),
        "flood_precursor_alert": bool(is_saturated)
    }