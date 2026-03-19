# Reproducibility Audit Checklist

## 1. Data Ingestion (Tier 1)
- [ ] STAC API Endpoint verified
- [ ] COG Range Requests successful
- [ ] Daymet/CHIRPS temporal alignment confirmed

## 2. GeoAI Processing (Tier 3)
- [ ] Dask worker count recorded
- [ ] PyTorch model hash (SHA-256) logged
- [ ] Harmonic coefficients loaded from `harmonic_coefficients.csv`

## 3. Decision Support (Tier 5)
- [ ] OGC API Feature delivery verified in QGIS
- [ ] Field validation loopback tested via KoboToolbox
- [ ] Notebooks executed with zero errors