from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from src.ingestion.stac_handler import search_stac
from src.microservices.flood_otsu import compute_flood_mask
from src.microservices.exposure_model import calculate_population_exposure

default_args = {'start_date': datetime(2026, 3, 16)}

with DAG('OpenDR_Disaster_Logic', default_args=default_args, schedule_interval='@hourly') as dag:

    def check_new_data():
        # Tier 1: Search STAC for Sentinel-1 acquisitions in Ethiopia
        items = search_stac(bbox=[33.0, 3.0, 48.0, 15.0], datetime_range="2026-03-16/2026-03-17")
        return items[0].assets['vh'].href if items else None

    def run_geoai_analysis(ds_path):
        # Tier 3: Compute Otsu Flood Mask
        mask = compute_flood_mask(ds_path)
        # Tier 3: Run Exposure Join with Google Open Buildings
        impact = calculate_population_exposure(mask, 'data/sample/buildings.parquet')
        return impact

    ingest_task = PythonOperator(task_id='stac_ingest', python_callable=check_new_data)
    compute_task = PythonOperator(task_id='geoai_compute', python_callable=run_geoai_analysis)

    ingest_task >> compute_task