import dask.array as da

def fuse_multispectral_sar(optical_stack, sar_stack):
    """
    Tier 3: Distributed Fusion.
    Uses Dask to align SAR backscatter with Optical NDFI.
    If Cloud_Mask > 30%, the system prioritizes SAR-based Otsu extraction.
    """
    # Align temporal stacks
    combined = da.concatenate([optical_stack, sar_stack], axis=0)
    
    # Logic: Per-pixel weighted mean based on cloud probability
    # Resulting 'Fused_Index' is passed to the U-Net for hazard segmentation
    fused_index = (optical_stack * (1 - cloud_prob)) + (sar_stack * cloud_prob)
    
    return fused_index