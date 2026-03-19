# ==============================================================================
# OpenDR 1.0: Real-Time GeoAI Framework
# Author: Bayilla Geda (Jinka Regional Veterinary Laboratory)
# License: GPL-3.0
# ==============================================================================

.PHONY: help setup data deploy stop sync-field retrain test clean

# Default shell
SHELL := /bin/bash
PYTHON := venv/bin/python
PIP := venv/bin/pip

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup: ## Step 1: Install system dependencies and initialize venv
	chmod +x scripts/setup_env.sh
	./scripts/setup_env.sh

data: ## Step 2: Generate sample data for Case Studies A & B
	@echo "[*] Initializing Scientific Sample Data..."
	$(PYTHON) scripts/gen_tokyo_sample.py
	$(PYTHON) scripts/gen_ethiopia_flood_cog.py
	chmod +x scripts/download_weights.sh
	./scripts/download_weights.sh

deploy: ## Step 3: Launch the FOSS4G Stack (PostGIS, pygeoapi, Airflow)
	@echo "[*] Launching Tier 2 & Tier 4 Infrastructure..."
	docker-compose -f deploy/docker/docker-compose.yml up -d
	@echo "[+] OpenDR 1.0 API active at http://localhost:80"

stop: ## Shutdown the framework infrastructure
	docker-compose -f deploy/docker/docker-compose.yml down

sync-field: ## Tier 5: Manually trigger KoboToolbox synchronization
	@echo "[*] Polling Citizen Feedback Loop..."
	$(PYTHON) scripts/sync_kobo_manual.py

retrain: ## Tier 3: Trigger GeoAI model fine-tuning pass from field data
	@echo "[*] Retraining U-Net hazard weights..."
	$(PYTHON) src/geoai/retrain_logic.py --model src/geoai/weights/base_unet.pth

test: ## Run unit tests for Intelligence Modules (Otsu, Harmonic Regr)
	venv/bin/pytest tests/

clean: ## Remove temporary data, pycache, and logs
	rm -rf data/raw/*
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +
	@echo "[+] Workspace cleaned."

all: setup data deploy ## Full initialization (Setup -> Data -> Deploy)