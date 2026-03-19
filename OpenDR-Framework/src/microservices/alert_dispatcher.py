import requests
import psycopg2

def dispatch_humanitarian_alerts(db_config, webhook_url):
    """
    Monitors the 'building_exposure_v1' view and dispatches 
    alerts when high-priority infrastructure is at risk.
    """
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()
    
    # Query high-risk buildings from the spatial view
    cur.execute("""
        SELECT building_id, woreda_name, pct_inundated 
        FROM building_exposure_v1 
        WHERE pct_inundated > 50;
    """)
    
    high_risk_cases = cur.fetchall()
    
    for building in high_risk_cases:
        payload = {
            "alert": "IMMEDIATE EVACUATION",
            "building_id": building[0],
            "location": building[1],
            "hazard_intensity": f"{building[2]}% flooded"
        }
        # Push alert to Responder Dashboard / Telegram / SMS Gateway
        requests.post(webhook_url, json=payload)

    cur.close()
    conn.close()