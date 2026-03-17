import numpy as np
from scipy import optimize

def fit_harmonic_model(ndvi_time_series, time_fractional_years):
    """
    Fits a 2nd-order harmonic regression to detrend seasonal greenness.
    f(t) = a1*cos(2pi*t) + b1*sin(2pi*t) + a2*cos(4pi*t) + b2*sin(4pi*t) + c
    """
    omega = 2.0 * np.pi
    
    def harmonic_func(t, a1, b1, a2, b2, c):
        return (a1 * np.cos(omega * t) + b1 * np.sin(omega * t) +
                a2 * np.cos(2 * omega * t) + b2 * np.sin(2 * omega * t) + c)

    # Initial guess for coefficients
    params, _ = optimize.curve_fit(harmonic_func, time_fractional_years, ndvi_time_series)
    
    # Calculate residuals (Anomalies)
    fitted = harmonic_func(time_fractional_years, *params)
    residuals = ndvi_time_series - fitted
    
    return residuals, params