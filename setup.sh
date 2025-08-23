#!/bin/bash

# Setup script for ai_driver
# Usage: bash setup.sh

echo "[*] Setting up ai_driver..."

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "[*] Creating virtual environment..."
    python3 -m venv venv
fi

# Activate and install dependencies
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "[✓] Setup complete. Activate with: source venv/bin/activate"
