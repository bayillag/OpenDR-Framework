# OpenDR: Open GIS Framework for Real-Time Disaster Response

[![FOSS4G-2026](https://img.shields.io/badge/FOSS4G-2026_Academic_Track-red)]([https://2026.foss4g.org](https://talks.osgeo.org/fossg4-2026-academic-track/))
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Reproducibility](https://img.shields.io/badge/Reproducibility-Docker_Verified-green)](#-reproducibility-and-quick-start)

## 📌 Project Overview
The **Open Disaster Response (OpenDR)** framework is a cloud-native, event-driven ecosystem designed for low-latency hazard detection and situational awareness. It bridges the gap between **Asian Big Data initiatives** (JAXA, Project PLATEAU) and regional disaster management in **East Africa**.

### Scientific Research Question
*How can a decentralized, event-driven FOSS4G framework semantically fuse high-resolution GeoAI hazard detection with ground-level human intelligence to provide a real-time "Single Source of Truth" for transboundary crisis management?*

## 🚀 Key Scientific Features
- **Cloud-Native Ingestion:** Real-time monitoring of STAC endpoints (Sentinel-1/2 & JAXA ALOS-2).
- **GeoAI Analytics:** Distributed U-Net segmentation for flood mapping using **Dask-Geo**.
- **Real-Time Mediation:** Implementation of **OGC API - Features & Processes** for bidirectional "Loop-in-the-Citizen" workflows.
- **Geospatial Sovereignty:** 100% open-source stack ensuring data privacy and local ownership.

## 🛠️ The FOSS4G Stack
- **Storage:** PostGIS 3.4 (Relational/Spatial), Cloud-Optimized GeoTIFFs (COG), GeoParquet.
- **Service Layer:** `pygeoapi` (OGC API suite) and `GeoServer` (MVT tiling).
- **Analytics:** `PyTorch`, `Dask`, `GDAL`, and `Apache Sedona`.
- **Validation:** Integration with `KoboToolbox` and `OpenStreetMap`.

## 🌏 Case Studies & Synergies
1. **Tokyo, Japan (Project PLATEAU):** 3D urban flood recovery simulation using CityGML models.
2. **Baro-Akobo-Sobat Basin (Ethiopia/South Sudan):** Transboundary "under-canopy" flood detection using **JAXA ALOS-2 SAR (L-band)**.
3. **Mekong Basin (SE Asia):** Cross-continental scaling and interoperability testing of the OpenDR stack.

## 📦 Reproducibility and Quick Start
To instantiate the environment and run the analytical notebooks:

```bash
# Clone the repo
git clone https://github.com/bayillag/OpenDR-Framework.git
cd OpenDR-Framework

# Start the stack
docker-compose up -d
