import pystac_client

def search_stac(bbox, datetime_range, collection="sentinel-2-l2a"):
    """Queries STAC endpoints for new acquisitions."""
    catalog = pystac_client.Client.open("https://earth-search.aws.element84.com/v1")
    search = catalog.search(
        collections=[collection],
        bbox=bbox,
        datetime=datetime_range
    )
    return search.item_collection()