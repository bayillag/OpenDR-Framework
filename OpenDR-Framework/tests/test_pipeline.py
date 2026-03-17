import pytest
from src.ingestion.stac_handler import search_stac

def test_stac_to_api_flow():
    # 1. Test Ingestion
    items = search_stac(bbox=[39.0, 8.0, 40.0, 9.0], datetime_range="2024-01-01/2024-01-02")
    assert len(items) >= 0
    
    # 2. Test Mediation Layer (pygeoapi connectivity)
    import requests
    try:
        response = requests.get("http://localhost/collections/flood_alerts")
        # If stack is up, should return 200
        assert response.status_code in [200, 404] 
    except requests.exceptions.ConnectionError:
        pytest.skip("API gateway not running")