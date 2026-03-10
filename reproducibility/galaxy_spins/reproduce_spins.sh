#!/bin/bash
# reproduce_spins.sh — Reproduce galaxy spin hierarchical Bayesian fit
#
# Prerequisites:
#   pip install cmdstanpy arviz pandas numpy matplotlib pyarrow requests tqdm
#   install_cmdstan  # downloads and compiles Stan
#
# Expected runtime: ~10-30 minutes on a modern laptop
# Expected output: posteriors for A0, p, q + null test results
#
# Data sources:
#   1. Galaxy Zoo DECaLS (Walmsley et al. 2022) — spiral galaxy catalog
#      DOI: 10.5281/zenodo.4573248, License: CC-BY-4.0
#   2. Published CW/CCW counts (Shamir 2024, arXiv:2401.09450) — for A(z) fit
#      File: research/paper2/wp5_spin_amplitude/data/galaxy_spin_counts.csv
#
# NOTE: galaxy_spin_data.csv was DEPRECATED on 2026-03-06 (unverified provenance).
# See DEPRECATED.md for details.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

echo "=== Reproducing Golden (2026) Galaxy Spin Analysis ==="
echo ""

# Check prerequisites
if ! python3 -c "import cmdstanpy" 2>/dev/null; then
    echo "ERROR: cmdstanpy not found. Install with:"
    echo "  pip install cmdstanpy && install_cmdstan"
    exit 1
fi

# Step 1: Build Galaxy Zoo DECaLS spiral catalog (if not cached)
SPIRAL_CATALOG="$REPO_ROOT/data/public_mirror/galaxy_zoo_decals_spins.csv"
if [ ! -f "$SPIRAL_CATALOG" ]; then
    echo "Step 1: Building Galaxy Zoo DECaLS spiral catalog..."
    python3 "$REPO_ROOT/research/data_build/build_galaxy_spin_dataset.py"
else
    echo "Step 1: Galaxy Zoo DECaLS spiral catalog already exists."
    echo "  $SPIRAL_CATALOG"
fi

# Step 2: Run hierarchical Bayesian fit on published aggregate counts
DATA_PATH="$REPO_ROOT/research/paper2/wp5_spin_amplitude/data/galaxy_spin_counts.csv"
echo ""
echo "Step 2: Running hierarchical Bayesian fit..."
echo "  Data: $DATA_PATH (Shamir 2024, verified provenance)"
python3 spin_fit_stan.py --data "$DATA_PATH" --output results/

echo ""
echo "=== Analysis complete ==="
echo "Results saved in results/"
echo "  - A0_p_q_posteriors.csv"
echo "  - dipole_axis_estimate.txt"
echo "  - null_test_results.txt"
echo ""
echo "Spiral catalog: $SPIRAL_CATALOG"
echo "Fit data source: $DATA_PATH"
