import xarray as xr
from skimage.filters import threshold_otsu

def compute_flood_mask(sar_image_path):
    """Applies Adaptive Otsu Thresholding to Sentinel-1 SAR COGs."""
    ds = xr.open_rasterio(sar_image_path)
    # Filter and identify threshold
    thresh = threshold_otsu(ds.values)
    flood_mask = ds < thresh
    return flood_mask.rename("flood_extent")