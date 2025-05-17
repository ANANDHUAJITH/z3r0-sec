# Lightweight Threat Modeling Tool

## Overview
A lightweight web-based tool for performing threat modeling and risk assessments for small applications using the STRIDE framework.

## How to Use
1. Run `app.py` using Python (Flask must be installed).
2. Open your browser and go to `http://127.0.0.1:5000/`.
3. Enter system components and data flows.
4. View generated threat models.

## Requirements
- Python 3.x
- Flask

## Files
- `app.py`: Flask backend
- `templates/index.html`: Frontend UI
- `threat_templates/stride.json`: STRIDE threat definitions
