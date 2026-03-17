# Deployment Guide

OpenDR 1.0 is designed for rapid deployment in resource-constrained environments.

## Prerequisites
- Docker and Docker-Compose
- A Kubernetes cluster (for Tier 3 scaling)
- Access to a STAC API (e.g., Microsoft Planetary Computer or AWS)

## Quick Start
1. Clone the repository:
   `git clone https://github.com/bayillag/OpenDR-Framework.git`
2. Configure your environment variables in `.env`.
3. Launch the stack:
   `docker-compose up -d`

## Local Data Sync
Use the provided scripts in `src/ingestion/` to mirror sample COGs from the Baro-Akobo-Sobat study area.