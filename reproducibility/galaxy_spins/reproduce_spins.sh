#!/bin/bash
# reproduce_spins.sh — Reproduce galaxy spin hierarchical Bayesian fit
#
# Prerequisites:
#   pip install cmdstanpy arviz pandas numpy matplotlib
#   install_cmdstan  # downloads and compiles Stan
#
# Expected runtime: ~10-30 minutes on a modern laptop
# Expected output: posteriors for A0, p, q + null test results
#
# NOTE: This script fits the phenomenological A(z) model to published
# galaxy spin data. It does NOT train a CNN classifier — the CW/CCW
# labels are taken from published catalogs (Shamir 2012, 2022).

set -euo pipefail

echo "=== Reproducing Golden (2026) Galaxy Spin Fit ==="
echo ""

# Check prerequisites
if ! python3 -c "import cmdstanpy" 2>/dev/null; then
    echo "ERROR: cmdstanpy not found. Install with:"
    echo "  pip install cmdstanpy && install_cmdstan"
    exit 1
fi

echo "Running hierarchical Bayesian fit..."
python3 spin_fit_stan.py --data galaxy_spin_data.csv --output results/

echo ""
echo "=== Fit complete ==="
echo "Results saved in results/"
echo "  - A0_p_q_posteriors.csv"
echo "  - dipole_axis_estimate.txt"
echo "  - null_test_results.txt"
