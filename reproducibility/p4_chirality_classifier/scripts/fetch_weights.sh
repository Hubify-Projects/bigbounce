#!/usr/bin/env bash
# Fetch the chirality_model_v2_best.pt weights from HuggingFace.
#
# The 8.47M-galaxy ViT-Small classifier weights live on HF under
# bamfai/galaxy-chirality-v2 (CC-BY-4.0).
#
# The local repo does NOT bundle the weights (they exceed the 50MB
# git/GitHub-LFS practical limit and HF is the canonical home).
#
# Usage:
#   bash fetch_weights.sh                          # default: ./weights/
#   bash fetch_weights.sh /tmp/chirality           # override target dir
#
# Requires: curl (or huggingface-cli + huggingface_hub Python pkg).

set -euo pipefail

TARGET_DIR="${1:-$(dirname "$0")/../weights}"
mkdir -p "$TARGET_DIR"

REPO="bamfai/galaxy-chirality-v2"
FILES=(
  "chirality_model_v2_best.pt"
)

echo "Fetching v2 chirality classifier weights from $REPO ..."
for f in "${FILES[@]}"; do
  url="https://huggingface.co/$REPO/resolve/main/$f"
  echo "  $url"
  if command -v huggingface-cli >/dev/null 2>&1; then
    huggingface-cli download "$REPO" "$f" --local-dir "$TARGET_DIR" --local-dir-use-symlinks=False
  else
    curl -L --fail-with-body -o "$TARGET_DIR/$f" "$url"
  fi
done

echo
echo "Weights staged at: $TARGET_DIR"
ls -la "$TARGET_DIR"
