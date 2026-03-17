import pytest
import numpy as np
from src.microservices.flood_otsu import compute_flood_mask
from src.microservices.rangeland_regr import fit_harmonic_model

def test_otsu_logic():
    # Create mock SAR array
    mock_data = np.random.rand(100, 100)
    # Ensure it handles 0-1 range
    mask = compute_flood_mask(mock_data)
    assert mask.shape == (100, 100)
    assert mask.dtype == bool

def test_harmonic_regression():
    t = np.linspace(2020, 2023, 36)
    ndvi = 0.5 + 0.2 * np.sin(2 * np.pi * t) # Pure seasonal signal
    residuals, _ = fit_harmonic_model(ndvi, t)
    # Residuals for pure signal should be near zero
    assert np.mean(residuals) < 1e-10