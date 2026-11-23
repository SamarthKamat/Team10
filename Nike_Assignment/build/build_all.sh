#!/usr/bin/env bash
# Rebuild every deliverable. Run from anywhere: bash Nike_Assignment/build/build_all.sh
set -e
cd "$(dirname "$0")"
python3 charts.py
python3 build_report.py
python3 build_docs.py
python3 build_pptx.py
python3 build_xlsx.py
