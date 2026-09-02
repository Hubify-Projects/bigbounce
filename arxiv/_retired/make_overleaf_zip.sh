#!/usr/bin/env bash
# make_overleaf_zip.sh — Create an Overleaf-compatible ZIP of the arxiv/ directory
#
# Usage: ./make_overleaf_zip.sh
# Output: ../bigbounce_arxiv_overleaf.zip

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUTPUT_DIR="$(dirname "${SCRIPT_DIR}")"
ZIP_NAME="bigbounce_arxiv_overleaf.zip"

cd "${SCRIPT_DIR}"

echo "=== Creating Overleaf-compatible ZIP ==="

# Remove old zip if present
rm -f "${OUTPUT_DIR}/${ZIP_NAME}"

# Create zip excluding build artifacts and scripts
zip -r "${OUTPUT_DIR}/${ZIP_NAME}" \
  main.tex \
  references.bib \
  figures/ \
  -x "*.aux" "*.bbl" "*.blg" "*.log" "*.out" "*.pdf" "*.synctex*" \
     "*.sh" ".DS_Store"

echo "Created: ${OUTPUT_DIR}/${ZIP_NAME}"
echo "Upload to https://www.overleaf.com/project (New Project > Upload Project)"
echo ""
echo "Note: Overleaf should auto-detect revtex4-2 and all packages."
echo "Set main document to main.tex in Overleaf settings if needed."
