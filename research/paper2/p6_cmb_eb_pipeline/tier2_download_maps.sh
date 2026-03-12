#!/usr/bin/env bash
# P6 Tier 2: Download Planck PR4 (NPIPE) frequency maps from PLA
#
# This script downloads the maps needed for the Tier 2 EB estimator.
# Total download: ~13 GB (HFI frequency maps + masks)
#
# Source: Planck Legacy Archive (https://pla.esac.esa.int/)
# License: ESA-PSL
#
# Usage:
#   bash tier2_download_maps.sh [OUTPUT_DIR]
#   Default OUTPUT_DIR: data/planck_pr4/

set -euo pipefail

OUTPUT_DIR="${1:-data/planck_pr4}"
PLA_BASE="https://pla.esac.esa.int/pla/aio/product-action?MAP.MAP_ID="

mkdir -p "$OUTPUT_DIR"

echo "============================================"
echo "Planck PR4 (NPIPE) Map Downloader"
echo "============================================"
echo "Output: $OUTPUT_DIR"
echo "Estimated total: ~13 GB"
echo ""

# HFI frequency maps (full mission)
HFI_FREQS="100 143 217 353"
for FREQ in $HFI_FREQS; do
    FILE="HFI_SkyMap_${FREQ}_2048_R4.00_full.fits"
    if [ -f "$OUTPUT_DIR/$FILE" ]; then
        echo "[SKIP] $FILE already exists"
    else
        echo "[DOWNLOAD] $FILE ..."
        wget -q --show-progress -O "$OUTPUT_DIR/$FILE" \
            "${PLA_BASE}${FILE}" || {
            echo "[ERROR] Failed to download $FILE"
            echo "  Try manual download from: https://pla.esac.esa.int/#maps"
            continue
        }
    fi
done

# HFI A/B detector splits (for null tests)
for FREQ in $HFI_FREQS; do
    for SPLIT in A B; do
        FILE="HFI_SkyMap_${FREQ}_2048_R4.00_${SPLIT}.fits"
        if [ -f "$OUTPUT_DIR/$FILE" ]; then
            echo "[SKIP] $FILE already exists"
        else
            echo "[DOWNLOAD] $FILE ..."
            wget -q --show-progress -O "$OUTPUT_DIR/$FILE" \
                "${PLA_BASE}${FILE}" || {
                echo "[WARN] Failed to download $FILE (A/B split optional)"
                continue
            }
        fi
    done
done

# LFI 70 GHz (for multi-frequency cross-check)
FILE="LFI_SkyMap_070_1024_R4.00_full.fits"
if [ -f "$OUTPUT_DIR/$FILE" ]; then
    echo "[SKIP] $FILE already exists"
else
    echo "[DOWNLOAD] $FILE ..."
    wget -q --show-progress -O "$OUTPUT_DIR/$FILE" \
        "${PLA_BASE}${FILE}" || {
        echo "[WARN] Failed to download $FILE (LFI 70 GHz optional)"
    }
fi

# Common polarization mask
FILE="common_mask_pol.fits"
if [ -f "$OUTPUT_DIR/$FILE" ]; then
    echo "[SKIP] $FILE already exists"
else
    echo "[DOWNLOAD] $FILE ..."
    wget -q --show-progress -O "$OUTPUT_DIR/$FILE" \
        "${PLA_BASE}${FILE}" || {
        echo "[WARN] No mask downloaded. Estimator will use latitude-based fallback."
    }
fi

echo ""
echo "============================================"
echo "Download complete. Contents:"
ls -lh "$OUTPUT_DIR"/*.fits 2>/dev/null || echo "  (no FITS files found)"
echo "============================================"
