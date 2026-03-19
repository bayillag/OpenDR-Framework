# Open Disaster Response (OpenDR) 1.0

**A Multidimensional Cloud-Native Framework for Real-Time GeoAI, Multi-Sensor Fusion, and Humanitarian Intelligence.**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![FOSS4G 2026](https://img.shields.io/badge/Conference-FOSS4G%20Hiroshima%202026-green)](https://2026.foss4g.org/)
[![Status: Academic Prototype](https://img.shields.io/badge/Status-Academic%20Prototype-orange)]()

---

## 📖 Overview
**OpenDR 1.0** is an event-driven, cloud-native geospatial ecosystem designed to close the "latency gap" in disaster response. Developed for the **FOSS4G 2026 Academic Track**, this framework moves beyond traditional monolithic Spatial Data Infrastructures (SDIs) to provide real-time actionable intelligence within the critical "golden hours" of a crisis.

By leveraging **Cloud-Native Geospatial (CNG)** formats (COGs, GeoParquet) and distributed computing, OpenDR 1.0 integrates GeoAI hazard detection with building-level humanitarian exposure modeling. This framework ensures **Geospatial Sovereignty** for regional agencies in the Global South by providing an entirely open-source, platform-independent pipeline.

## 🏗️ System Architecture
The framework is organized into five functional tiers to ensure modularity and scalability:

1.  **Tier 1: Data Ingestion & Discovery ("The Sensor Web")** – Automated monitoring of **STAC** endpoints for Sentinel-1/2, Landsat 8/9, GOES-16, and GRACE.
2.  **Tier 2: Orchestration ("The Brain")** – Managed via **Apache Airflow**, triggering specialized analytical DAGs upon new data detection.
3.  **Tier 3: Distributed Compute ("The Engine")** – Parallelized imagery analysis using **Dask-Geo** on Kubernetes, executing PyTorch U-Net models.
4.  **Tier 4: Mediation & Standards ("The Standardized Interface")** – Data persistence in **PostGIS 3.4** and exposure via **pygeoapi** (OGC API - Features/Processes).
5.  **Tier 5: Client & Feedback ("The Decision Support")** – Expert visualization in **QGIS** and field validation via **KoboToolbox**, completing the "Loop-in-the-Citizen" refinement cycle.

## 🔬 Scientific Foundation
OpenDR 1.0 operationalizes and ports complex scientific logic originally developed in platform-locked environments (e.g., GEE) into independent Python microservices:

*   **Hydrology:** Adaptive Otsu Thresholding and Canny Edge Detection for SAR-based flood extraction (*Markert et al., 2024*).
*   **Subsurface Intelligence:** Gravimetric anomaly analysis for flood pre-cursor detection (*Purdy & Famiglietti, 2024*).
*   **Vegetation Resilience:** Second-Order Harmonic Regression for phenological detrending in rangelands (*Wang & Azzari, 2024*).
*   **Humanitarian Exposure:** Population-weighted risk modeling using the **Google Open Buildings** dataset (*Van Den Hoek & Friedrich, 2024*).

## 🚀 Getting Started

### Prerequisites
- Docker and Docker-Compose
- Python 3.11+
- [Optional] Kubernetes Cluster (for Tier 3 scaling)

### Quick Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/bayillag/OpenDR-Framework.git
   cd OpenDR-Framework
   ```

2. **Initialize Environment:**
   ```bash
   make setup
   ```

3. **Generate Sample Case Study Data:**
   ```bash
   make data
   ```

4. **Deploy the FOSS4G Stack:**
   ```bash
   make deploy
   ```

## 🧪 Case Studies
The repository includes **Technical Reproducibility** notebooks for our cross-continental validation sites:
*   [**Tokyo, Japan**](notebooks/01_case_study_japan.ipynb): 3D Digital Twin integration with Project PLATEAU CityGML.
*   [**East Africa**](notebooks/01_hydrology_ethiopia.ipynb): Transboundary flood and malaria early warning in the Baro-Akobo-Sobat Basin.
*   [**Regional Watch**](notebooks/02_wildfire_tactical_watch.ipynb): Tactical wildfire watch using 15-minute GOES-16 updates.

## 📂 Repository Structure
*   `src/microservices/`: Core scientific Python modules.
*   `src/geoai/`: PyTorch models and retraining logic.
*   `data/metadata/`: STAC Catalog and Collection definitions.
*   `deploy/`: Docker-Compose and Kubernetes manifests.
*   `scripts/`: Utilities for data generation and setup.

## 📄 License
Distributed under the **GPLv3 License**. See `LICENSE` for more information.

## 🤝 Contact & Affiliation
**Bayilla Geda**  
Jinka Regional Veterinary Laboratory, South Ethiopia Regional State, Ethiopia.  
Email: [bayillag@gmail.com](mailto:bayillag@gmail.com)  

---
*Developed for FOSS4G Hiroshima 2026. Building multi-hazard resilience through the power of Open Source.*
