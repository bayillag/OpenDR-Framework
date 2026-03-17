# System Architecture

OpenDR 1.0 is organized into five functional tiers to ensure scalability and geospatial sovereignty.

## Tier 1: Data Ingestion & Discovery ("The Sensor Web")
- **Inputs:** Sentinel-1 (SAR), Sentinel-2 (MSI), Landsat 8/9, GOES-16/17, GRACE, CHIRPS.
- **Standard:** SpatioTemporal Asset Catalog (STAC).
- **Format:** Cloud-Optimized GeoTIFFs (COGs).

## Tier 2: Orchestration ("The Brain")
- **Engine:** Apache Airflow.
- **Logic:** Disaster Logic Directed Acyclic Graphs (DAGs) trigger specialized processing when new data hits STAC endpoints.

## Tier 3: Distributed Compute ("The Engine")
- **Infrastructure:** Kubernetes Cluster.
- **Parallelization:** Dask-Geo for big data geospatial arrays.
- **AI Models:** PyTorch U-Net for hazard segmentation.

## Tier 4: Mediation & Standards ("The Standardized Interface")
- **Database:** PostGIS 3.4 / PostgreSQL 16.
- **Gateway:** pygeoapi.
- **Protocol:** OGC API - Features.

## Tier 5: Client & Feedback ("The Decision Support")
- **Interface:** QGIS for Command Centers; KoboToolbox for Mobile Teams.
- **Citizen Feedback Loop:** Real-time ground-truth validation to retrain model weights.