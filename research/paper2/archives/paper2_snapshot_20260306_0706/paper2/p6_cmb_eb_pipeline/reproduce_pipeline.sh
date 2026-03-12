#!/usr/bin/env bash
# P6 CMB EB Pipeline — Reproducible Pipeline Runner
#
# Runs Tier 1 (always) and optionally Tier 2 (if maps available).
#
# Usage:
#   bash reproduce_pipeline.sh [--tier2]

set -euo pipefail

RUN_ID="run_$(date +%Y%m%d_%H%M%S)"
OUTPUT_DIR="outputs/$RUN_ID"

echo "============================================"
echo "P6 CMB EB Pipeline"
echo "Run ID: $RUN_ID"
echo "Output: $OUTPUT_DIR"
echo "============================================"

mkdir -p "$OUTPUT_DIR"

# --- Tier 1: Literature Beta Registry (always runs) ---
echo ""
echo "--- TIER 1: Literature Beta Registry ---"
python beta_registry.py --output "$OUTPUT_DIR/"
echo "Tier 1 complete."

# --- Tier 2: Map-Level Estimator (optional) ---
if [ "${1:-}" = "--tier2" ]; then
    echo ""
    echo "--- TIER 2: Map-Level EB Estimator ---"
    TIER2_DIR="$OUTPUT_DIR/tier2"
    mkdir -p "$TIER2_DIR"

    # Check if maps exist
    if [ -d "data/planck_pr4" ] && ls data/planck_pr4/*.fits 1>/dev/null 2>&1; then
        python tier2_eb_estimator.py \
            --data_dir data/ \
            --output_dir "$TIER2_DIR/" \
            --freq1 143 \
            --freq2 217 \
            --nside 512
        echo "Tier 2 complete."
    else
        echo "Planck maps not found in data/planck_pr4/."
        echo "Run: bash tier2_download_maps.sh"
        echo "Skipping Tier 2."
    fi
else
    echo ""
    echo "Tier 2 skipped (use --tier2 flag to enable)."
fi

# --- Summary ---
echo ""
echo "============================================"
echo "Pipeline complete."
echo "Outputs in: $OUTPUT_DIR/"
echo ""
ls -la "$OUTPUT_DIR/"
echo "============================================"
