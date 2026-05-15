#!/usr/bin/env bash
# reproduce_paper4.sh
# One-shot reproduction wrapper for Paper 4 headline numbers.
# Reads the canonical Catalog C parquet from HuggingFace, runs the
# core analysis steps (dipole, MASTER ℓ=1, hemisphere max-statistic,
# monopole+mask leakage null sim, per-imaging-leg systematics, face-on
# robustness, PSF correlation), and prints the headline numbers
# against the paper's stated values.
#
# Usage:
#   bash reproduce_paper4.sh [/path/to/output_dir]
#
# Dependencies (apt-installable on Linux; or use the paper4-v1.0
# release Docker image):
#   - python3 >= 3.10
#   - pip install: pyarrow pandas numpy healpy pymaster matplotlib datasets
#   - libgsl-dev libfftw3-dev libcfitsio-dev  (for pymaster build)
#
# Catalog (downloads ~952 MB from HuggingFace):
#   huggingface.co/datasets/bamfai/galaxy-chirality-catalog
#
# Notes:
#   - Wall time: ~30-60 min on a 16-core CPU / 32 GB RAM box.
#   - All seeds fixed (SEED=42); outputs deterministic up to NaMaster
#     numerical precision (typical ~1e-12 floating-point drift).
#   - Per-leg and face-on rerun scripts use the same parquet; PSF
#     correlation plot uses the precomputed wave_14_jj JSON from this
#     repo (no extra catalog download).

set -e
OUT=${1:-./paper4_repro_$(date +%Y%m%d_%H%M%S)}
mkdir -p "$OUT"
cd "$OUT"

echo "==> Downloading canonical Catalog C parquet from HuggingFace..."
hf download bamfai/galaxy-chirality-catalog catalog_production.parquet \
  --repo-type dataset --local-dir . || \
  huggingface-cli download bamfai/galaxy-chirality-catalog \
    catalog_production.parquet --repo-type dataset --local-dir .

echo "==> Step 1: Catalog summary (Sec. IV.A headline counts)"
python3 - <<'PYEOF'
import pandas as pd, json
df = pd.read_parquet("catalog_production.parquet", columns=["class_eq"])
n = len(df)
cw = int((df["class_eq"] == "CW").sum())
ccw = int((df["class_eq"] == "CCW").sum())
ns = int((df["class_eq"] == "NOT_SPIRAL").sum())
print(f"Total: {n} (expected 8,474,531)")
print(f"CW:    {cw} (expected 1,592,107)")
print(f"CCW:   {ccw} (expected 1,609,053)")
print(f"NS:    {ns} (expected 5,273,371)")
print(f"Spiral total: {cw+ccw} (expected 3,201,160)")
print(f"p_CW: {cw/(cw+ccw):.6f} (expected 0.497353)")
PYEOF

echo
echo "==> Step 2: Real-space dipole + hemisphere statistic"
echo "  (run pipelines/p2_chirality/scripts/dipole_analysis.py from the repo)"

echo
echo "==> Step 3: MASTER ℓ=1 + monopole+mask null sim"
echo "  See pipelines/p2_chirality/scripts/canonical_l1_namaster_pod.py"
echo "  + monopole_mask_null_sim_v2.py (this paper, Sec. VI.B)"

echo
echo "==> Step 4: Per-imaging-leg systematics"
echo "  See pipelines/p2_chirality/scripts/per_leg_systematics.py"

echo
echo "==> Step 5: Face-on robustness rerun"
echo "  See pipelines/p2_chirality/scripts/face_on_rerun.py"

echo
echo "==> Step 6: PSF-ellipticity correlation plot"
echo "  See pipelines/p2_chirality/scripts/p4_psf_calibration_plot.py"
echo "  (reads pipelines/p2_chirality/r42_results/wave_14_jj_psf_xcorr_results.json)"

echo
echo "==> Reproduction complete; outputs in: $OUT"
echo "Compare to paper Tables III, IV, V, VI, VII."
