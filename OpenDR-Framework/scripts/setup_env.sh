#!/bin/bash

# ==============================================================================
# OpenDR 1.0: System Environment Setup Utility
# Purpose: Installs FOSS4G system libraries, Python venv, and core directories.
# Affiliation: Jinka Regional Veterinary Laboratory, Ethiopia.
# FOSS4G Stack: GDAL 3.8+, PostGIS Client, Docker, Python 3.11+
# ==============================================================================

# Exit on any error
set -e

# Logging colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}------------------------------------------------------------${NC}"
echo -e "${BLUE}  OpenDR 1.0: Initializing Local Environment${NC}"
echo -e "  Pillar: Geospatial Sovereignty & Technical Reproducibility"
echo -e "${BLUE}------------------------------------------------------------${NC}"

# 1. Update System and Install FOSS4G Core Dependencies
echo -e "[*] ${GREEN}Step 1: Installing System Dependencies (Requires sudo)...${NC}"
sudo apt-get update
sudo apt-get install -y \
    python3-pip \
    python3-venv \
    python3-dev \
    gdal-bin \
    libgdal-dev \
    postgresql-client \
    libspatialindex-dev \
    docker-compose \
    curl \
    git

# Export GDAL environment variables (Critical for 'pip install gdal/rasterio')
export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal

# 2. Initialize Directory Structure
echo -e "[*] ${GREEN}Step 2: Initializing OpenDR Directory Tree...${NC}"
mkdir -p data/raw data/sample data/external data/lookup src/geoai/weights src/api/static
echo "[+] Folders verified."

# 3. Setup Python Virtual Environment
echo -e "[*] ${GREEN}Step 3: Creating Python Virtual Environment (venv)...${NC}"
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "[+] Virtual environment created."
else
    echo "[*] venv already exists. Skipping creation."
fi

# 4. Install Python Dependencies
echo -e "[*] ${GREEN}Step 4: Installing OpenDR Stack via pip...${NC}"
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "[+] Python dependencies installed."

# 5. Handle Environment Variables
echo -e "[*] ${GREEN}Step 5: Configuring Environment Variables...${NC}"
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "[!] Created .env from .env.example. Please update your API keys."
else
    echo "[*] .env file already exists."
fi

# 6. Verify Docker Installation
echo -e "[*] ${GREEN}Step 6: Verifying Docker Engine for Tiers 2 & 4...${NC}"
if command -v docker >/dev/null 2>&1; then
    docker --version
    echo "[+] Docker verified. Ready for containerized deployment."
else
    echo "[!] WARNING: Docker not found. Tiers 2 (Orchestration) and 4 (API) require Docker."
fi

# 7. Download Core Assets (Optional)
echo -e "[*] ${GREEN}Step 7: Initializing Core Data Assets...${NC}"
# Run the data generators created in previous steps
python3 scripts/gen_tokyo_sample.py
python3 scripts/gen_ethiopia_flood_cog.py
chmod +x scripts/download_weights.sh
./scripts/download_weights.sh

echo -e "${BLUE}------------------------------------------------------------${NC}"
echo -e "${GREEN}[SUCCESS] OpenDR 1.0 Environment is ready!${NC}"
echo -e "  To activate the environment: ${BLUE}source venv/bin/activate${NC}"
echo -e "  To launch the full stack:    ${BLUE}make deploy${NC}"
echo -e "${BLUE}------------------------------------------------------------${NC}"