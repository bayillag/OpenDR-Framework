def malaria_risk_forecast(lst_anomaly, precip_total):
    """
    EPIDEMIA Logic: Predicts malaria transmission suitability 
    based on Land Surface Temperature and Rainfall lags.
    """
    # Thresholds based on Amhara region research
    suitability = 0
    if 18 < lst_anomaly < 32: # Optimal mosquito breeding temp
        suitability += 1
    if precip_total > 50:     # Sufficient rainfall for larval habitats
        suitability += 1
        
    risk_level = "High" if suitability == 2 else "Low"
    return {"malaria_suitability_index": suitability, "alert_level": risk_level}