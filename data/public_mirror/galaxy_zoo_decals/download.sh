#!/bin/bash
# download.sh — Download Galaxy Zoo DECaLS volunteer classifications from Zenodo
#
# Source: Walmsley et al. (2022), MNRAS 509:3966
# DOI: 10.5281/zenodo.4573248
# License: CC-BY-4.0
#
# This downloads the volunteers_1_and_2 parquet file (~18.7 MB).
# For the full auto-posteriors catalog (~1.6 GB parquet), uncomment the second URL.

set -euo pipefail

ZENODO_RECORD="4573248"
BASE_URL="https://zenodo.org/api/records/${ZENODO_RECORD}/files"

echo "=== Downloading Galaxy Zoo DECaLS from Zenodo ==="
echo "DOI: 10.5281/zenodo.4573248"
echo ""

# Volunteer classifications (campaigns 1+2) — 18.7 MB parquet
curl -L -o gz_decals_volunteers_1_and_2.parquet \
    "${BASE_URL}/gz_decals_volunteers_1_and_2.parquet/content"

echo ""
echo "Computing checksums..."
shasum -a 256 gz_decals_volunteers_1_and_2.parquet | tee CHECKSUMS.txt

echo ""
echo "Download complete. To build the spiral catalog, run:"
echo "  python ../../research/data_build/build_galaxy_spin_dataset.py --skip-download"
