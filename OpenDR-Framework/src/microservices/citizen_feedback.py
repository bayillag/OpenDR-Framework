import requests
import psycopg2

def sync_kobo_to_postgis(kobo_api_url, token, db_config):
    """
    Polls KoboToolbox for field reports and updates the PostGIS validation table.
    """
    headers = {'Authorization': f'Token {token}'}
    response = requests.get(kobo_api_url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()
        
        for record in data['results']:
            # Insert ground-truth point into PostGIS
            cur.execute("""
                INSERT INTO field_validation (kobo_id, hazard_type, is_valid, geom)
                VALUES (%s, %s, %s, ST_SetSRID(ST_MakePoint(%s, %s), 4326))
                ON CONFLICT (kobo_id) DO NOTHING;
            """, (record['_id'], record['hazard'], record['valid'], record['lon'], record['lat']))
            
        conn.commit()
        cur.close()
        conn.close()
        print("Tier 5: Database synchronized with field validation reports.")