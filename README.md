# **Open Disaster Response (OpenDR) 1.0**

**A Multidimensional Cloud-Native Framework for Real-Time GeoAI, Multi-Sensor Fusion, and Humanitarian Intelligence.**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![FOSS4G 2026](https://img.shields.io/badge/Conference-FOSS4G%20Hiroshima%202026-green)](https://2026.foss4g.org/)
[![Status: Academic Prototype](https://img.shields.io/badge/Status-Academic%20Prototype-orange)]()

---

## 📖 Overview
**OpenDR 1.0** is an event-driven, cloud-native geospatial framework developed to address the latency challenges in disaster response for the **FOSS4G 2026 Academic Track** [1]. By leveraging cloud-native formats (COGs, GeoParquet) and distributed computing, the framework integrates GeoAI hazard detection with building-level exposure modeling. OpenDR 1.0 is designed to support regional agencies in the Global South with a reproducible, open-source pipeline [2, 3].

## 🏗️ System Architecture
The framework is organized into five functional tiers:

1.  **Tier 1: Data Ingestion & Discovery** – Automated monitoring of STAC endpoints (Sentinel-1/2, Landsat 8/9, GOES-16, GRACE) [5].
2.  **Tier 2: Orchestration** – Apache Airflow pipelines triggering analytical DAGs upon new data detection.
3.  **Tier 3: Distributed Compute** – Imagery analysis using Dask-Geo on Kubernetes, executing PyTorch segmentation models.
4.  **Tier 4: Mediation & Standards** – Data persistence in PostGIS and exposure via pygeoapi (OGC API - Features/Processes).
5.  **Tier 5: Client & Feedback** – Visualization in QGIS and field validation via KoboToolbox / OSM [6].

## 🔬 Scientific Foundations
OpenDR 1.0 implements several open-source algorithms for environmental and humanitarian modeling:
*   **Hydrology:** Adaptive Otsu Thresholding and Canny Edge Detection for surface water segmentation.
*   **Subsurface Moisture:** Gravity anomaly analysis using GRACE data for flood precursor detection.
*   **Vegetation Analysis:** Second-Order Harmonic Regression for rangeland monitoring.
*   **Humanitarian Exposure:** Building-level risk estimation using the Google Open Buildings dataset.

## 🧪 Case Studies (Notebooks)
The repository includes reproducible notebooks for the validation sites:
*   [**Tokyo, Japan (Project PLATEAU)**](notebooks/01_case_study_japan.ipynb) – 3D urban resilience modeling [4].
*   [**East Africa (Baro-Akobo-Sobat Basin)**](notebooks/01_hydrology_ethiopia.ipynb) – Flood and health hazard early warning.
*   [**Regional Active Fire Watch**](notebooks/02_wildfire_tactical_watch.ipynb) – Near-real-time wildfire monitoring using GOES-16 data.

## 📄 License
Distributed under the **GPLv3 License**.

## 🤝 Contact & Affiliation
**Bayilla Geda**  
Regional Veterinary and Research Services, South Ethiopia Regional State, Ethiopia.  
Email: [bayillag@gmail.com](mailto:bayillag@gmail.com)  

---
*Developed for FOSS4G Hiroshima 2026. Empowering local communities through open geospatial technologies.*
