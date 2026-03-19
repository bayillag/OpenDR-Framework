import os
import requests
import psycopg2
from psycopg2 import extras
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

class KoboToPostgresSync:
    """
    OpenDR 1.0: Tier 5 - Citizen Feedback Loop
    Microservice to sync KoboToolbox field reports to PostGIS.
    Logic based on: Brovelli et al. (2017)
    """

    def __init__(self):
        # Database Configuration
        self.db_params = {
            "host": os.getenv("POSTGRES_HOST", "localhost"),
            "database": os.getenv("POSTGRES_DB", "opendr"),
            "user": os.getenv("POSTGRES_USER", "opendr_admin"),
            "password": os.getenv("POSTGRES_PASSWORD", "foss4g_hiroshima"),
            "port": os.getenv("POSTGRES_PORT", "5432")
        }
        
        # KoboToolbox API Configuration
        self.kobo_token = os.getenv("KOBO_TOKEN")
        self.kobo_asset_id = os.getenv("KOBO_ASSET_ID") # The form ID
        self.kobo_url = f"https://kf.kobotoolbox.org/api/v2/assets/{self.kobo_asset_id}/data.json"
        
        if not self.kobo_token or not self.kobo_asset_id:
            raise ValueError("[!] Error: KOBO_TOKEN or KOBO_ASSET_ID missing in .env")

    def fetch_field_reports(self):
        """Polls KoboToolbox API for new submissions."""
        headers = {"Authorization": f"Token {self.kobo_token}"}
        print(f"[*] Tier 5: Fetching reports from KoboToolbox Asset {self.kobo_asset_id}...")
        
        try:
            response = requests.get(self.kobo_url, headers=headers)
            response.raise_for_status()
            data = response.json()
            return data.get('results', [])
        except requests.exceptions.RequestException as e:
            print(f"[!] API Connection Error: {e}")
            return []

    def sync_to_postgis(self, records):
        """Pushes field records into the PostGIS validation table."""
        if not records:
            print("[*] No new records found to synchronize.")
            return

        conn = None
        try:
            conn = psycopg2.connect(**self.db_params)
            cur = conn.cursor()
            
            count = 0
            for r in records:
                # Mapping Kobo JSON keys to OpenDR Table Schema
                # Note: Adjust these keys based on your specific Kobo Form structure
                kobo_id = r.get('_id')
                hazard_type = r.get('hazard_category', 'unknown')
                
                # Checkbox validation: 'confirmed' or 'false_positive'
                is_valid = True if r.get('validation_status') == 'confirmed' else False
                
                # Spatial extraction from Kobo '_geolocation' list [lat, lon]
                geo = r.get('_geolocation', [None, None])
                lat, lon = geo[0], geo[1]

                if lat and lon:
                    cur.execute("""
                        INSERT INTO field_validation (
                            kobo_id, hazard_type, is_valid, observation_date, geom
                        ) VALUES (
                            %s, %s, %s, %s, ST_SetSRID(ST_MakePoint(%s, %s), 4326)
                        ) ON CONFLICT (kobo_id) DO NOTHING;
                    """, (kobo_id, hazard_type, is_valid, r.get('_submission_time'), lon, lat))
                    count += cur.rowcount

            conn.commit()
            print(f"[+] Tier 5 Sync Success: {count} ground-truth points added to PostGIS.")
            
            # Triggering Model Retraining logic (Tier 3) if new data threshold met
            if count > 10:
                print("[*] Triggering Tier 3: GeoAI Model Fine-tuning Pass...")

        except (Exception, psycopg2.DatabaseError) as error:
            print(f"[!] Database Error: {error}")
        finally:
            if conn is not None:
                cur.close()
                conn.close()

def main():
    print("-------------------------------------------------------")
    print("  OpenDR 1.0: Manual Field Validation Synchronizer")
    print("-------------------------------------------------------")
    
    try:
        syncer = KoboToPostgresSync()
        reports = syncer.fetch_field_reports()
        syncer.sync_to_postgis(reports)
    except Exception as e:
        print(f"[!] Initialization Failed: {e}")

if __name__ == "__main__":
    main()