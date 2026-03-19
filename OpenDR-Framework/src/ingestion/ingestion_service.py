import pystac_client

def get_latest_data(bbox, collection="sentinel-1-grd"):
    """Search STAC for the most recent acquisitions in the study area."""
    catalog = pystac_client.Client.open("https://earth-search.aws.element84.com/v1")
    search = catalog.search(
        collections=[collection],
        bbox=bbox,
        max_items=1
    )
    item = next(search.get_items())
    # Return the URL to the Cloud-Optimized GeoTIFF (COG)
    return item.assets['vh'].href