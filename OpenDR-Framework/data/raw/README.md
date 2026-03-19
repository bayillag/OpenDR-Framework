# OpenDR 1.0: Raw Data Landing Zone & Cache

## Overview
This directory serves as the primary local landing zone for **Tier 1 (Data Ingestion & Discovery)** of the Open Disaster Response (OpenDR) 1.0 framework. 

Consistent with the principles of **Cloud-Native Geospatial (CNG)** architectures and the goal of **Geospatial Sovereignty**, this folder is designed to store only temporary data chunks and intermediate climate files. By leveraging **SpatioTemporal Asset Catalogs (STAC)** and **HTTP Range Requests**, OpenDR 1.0 avoids the traditional "download-then-analyze" paradigm, significantly reducing the storage burden on regional research centers.

## Operational Lifecycle

### 1. Ingestion (Tier 1)
When **Apache Airflow** triggers a discovery task, the system identifies relevant assets (Sentinel-1/2, Landsat 8/9, GOES-16/17). Only the specific spatial and spectral windows required for the **Intelligence Modules** are streamed into this directory.

### 2. Processing (Tier 3)
The distributed compute engine (**Dask-Geo**) utilizes this folder as a high-speed local cache for:
*   **SAR FLOAT Chunks:** Raw power-scale data for **Adaptive Otsu Thresholding**.
*   **Thermal Anomalies:** High-cadence (15-min) GOES-16 bands for **Active Wildfire Watch**.
*   **Meteorological Arrays:** CHIRPS and Daymet NetCDF files used for **Phenological Detrending** and **Fire-to-Flood** runoff risk calculation.

### 3. Transformation (Tier 4)
Once the GeoAI processing layer (PyTorch U-Net) has extracted hazard vectors, the raw imagery cached here is processed into **GeoParquet** or discarded, while the resulting intelligence is persisted in the **PostGIS** database.

## Directory Governance

*   **Version Control:** To maintain a lightweight repository, this folder contains a `.gitignore` file that prevents the accidental committing of bulky satellite imagery or binary data.
*   **Geospatial Sovereignty:** Local administrators are encouraged to mount this directory on a high-speed SSD or NVMe drive to optimize the performance of the **Dask** worker nodes.
*   **Data Privacy:** In accordance with **Brovelli et al. (2017)**, raw data remains within the institutional boundary of the regional agency, ensuring complete ownership over the analytical logic and intermediate data artifacts.

## Cleanup Policy
The system is configured to clear files from this directory that are older than **30 days** (configurable in `data/metadata/search_logic.json`). This ensures the framework remains operational in storage-constrained environments.

---
**Contact:** [bayillag@gmail.com](mailto:bayillag@gmail.com)  
**Repository:** [https://github.com/bayillag/OpenDR-Framework](https://github.com/bayillag/OpenDR-Framework)