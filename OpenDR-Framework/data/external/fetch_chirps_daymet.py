from pystac_client import Client
import planetary_computer

def fetch_met_context(bbox, time_range):
    """
    Uses STAC to discover CHIRPS (Rain) and Daymet (Weather).
    Essential for calculating the Runoff Risk Index.
    """
    catalog = Client.open(
        "https://planetarycomputer.microsoft.com/api/stac/v1",
        modifier=planetary_computer.sign_inplace,
    )

    search = catalog.search(
        collections=["daymet-daily-na", "chirps"],
        bbox=bbox,
        datetime=time_range
    )
    
    items = search.item_collection()
    print(f"[*] OpenDR Ingestion: Found {len(items)} climate records for context.")
    return items

if __name__ == "__main__":
    # Example for transboundary Ethiopia-South Sudan region
    fetch_met_context(bbox=[33.0, 7.0, 36.0, 10.0], time_range="2024-01-01/2024-01-07")