#!/bin/bash
# reproduce_cosmology.sh — Reproduce MCMC cosmological fits from Golden (2026)
#
# Prerequisites:
#   pip install cobaya==3.5.4
#   cobaya-install cosmo -p ./packages
#
# Expected runtime: ~4-12 hours per config on 4 CPU cores
# Expected output: chains/ directory with MCMC samples + convergence diagnostics
#
# NOTE: The model is standard LCDM + Delta_Neff using stock CAMB.
# No custom CAMB modifications are required. The spin-torsion framework
# motivates the nonzero Delta_Neff but the actual MCMC uses standard code.

set -euo pipefail

PACKAGES_PATH="${PACKAGES_PATH:-./packages}"

echo "=== Reproducing Golden (2026) Cosmological Fits ==="
echo "Using Cobaya + stock CAMB with N_eff as free parameter"
echo ""

# Check prerequisites
if ! command -v cobaya-run &> /dev/null; then
    echo "ERROR: cobaya-run not found. Install with: pip install cobaya==3.5.4"
    exit 1
fi

if [ ! -d "$PACKAGES_PATH" ]; then
    echo "Installing cosmology packages to $PACKAGES_PATH..."
    cobaya-install cosmo -p "$PACKAGES_PATH"
fi

export COBAYA_PACKAGES_PATH="$PACKAGES_PATH"

# Run all 4 dataset combinations
for config in cobaya_planck.yaml cobaya_planck_bao.yaml cobaya_planck_bao_sn.yaml cobaya_full_tension.yaml; do
    echo ""
    echo "--- Running: $config ---"
    if [ -f "cosmology/$config" ]; then
        cobaya-run "cosmology/$config" --packages-path "$PACKAGES_PATH"
    else
        echo "WARNING: $config not found, skipping"
    fi
done

echo ""
echo "=== All runs complete ==="
echo "Chains saved in chains/*/"
echo ""
echo "To analyze results:"
echo "  python -c \"import getdist; ...\""
echo "  or use the GetDist GUI: getdist-gui"
