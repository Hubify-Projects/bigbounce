#!/bin/bash
# reproduce_cosmology.sh — Reproduce MCMC cosmological fits from Golden (2026)
#
# Prerequisites:
#   pip install cobaya==3.6.1
#   cobaya-install cosmo -p ./packages
#
# Expected runtime: ~4-12 hours per config on 4 CPU cores
# Expected output: fresh Cobaya chains under each YAML's configured output path.
# This launcher does not reproduce the frozen-chain post-processing products;
# those files and their hashes are retained in the paper artifact manifest.
#
# NOTE: The model is standard LCDM + Delta_Neff using stock CAMB.
# No custom CAMB modifications are required. The spin-torsion framework
# motivates the nonzero Delta_Neff but the actual MCMC uses standard code.

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/../.." && pwd)"
PACKAGES_PATH="${PACKAGES_PATH:-$REPO_ROOT/packages}"
CHECK_ONLY=0

if [[ "${1:-}" == "--check" ]]; then
    CHECK_ONLY=1
elif [[ $# -gt 0 ]]; then
    echo "Usage: $0 [--check]" >&2
    exit 2
fi

echo "=== Reproducing Golden (2026) Cosmological Fits ==="
echo "Using Cobaya + stock CAMB with N_eff as free parameter"
echo ""

CONFIGS=(
    cobaya_planck.yaml
    cobaya_planck_bao.yaml
    cobaya_planck_bao_sn.yaml
    cobaya_full_tension.yaml
)

if [[ "$CHECK_ONLY" -eq 1 ]]; then
    for config in "${CONFIGS[@]}"; do
        config_path="$SCRIPT_DIR/$config"
        [[ -f "$config_path" ]] || {
            echo "ERROR: required configuration missing: $config_path" >&2
            exit 1
        }
        echo "CHECKED: $config_path"
    done
    if python3 -c 'import cobaya' 2>/dev/null; then
        COBAYA_VERSION="$(python3 -c 'import cobaya; print(cobaya.__version__)')"
        [[ "$COBAYA_VERSION" == "3.6.1" ]] || {
            echo "ERROR: Cobaya 3.6.1 required; found $COBAYA_VERSION" >&2
            exit 1
        }
        echo "CHECKED: Cobaya $COBAYA_VERSION"
    else
        echo "NOTE: Cobaya is not installed; configuration paths passed the no-run check."
    fi
    echo "Configuration/path smoke check passed; no chains were run."
    exit 0
fi

# Check prerequisites
if ! command -v cobaya-run &> /dev/null; then
    echo "ERROR: cobaya-run not found. Install with: pip install cobaya==3.6.1"
    exit 1
fi

COBAYA_VERSION="$(python3 -c 'import cobaya; print(cobaya.__version__)')"
if [[ "$COBAYA_VERSION" != "3.6.1" ]]; then
    echo "ERROR: Cobaya 3.6.1 required; found $COBAYA_VERSION" >&2
    exit 1
fi

if [ ! -d "$PACKAGES_PATH" ]; then
    echo "Installing cosmology packages to $PACKAGES_PATH..."
    cobaya-install cosmo -p "$PACKAGES_PATH"
fi

export COBAYA_PACKAGES_PATH="$PACKAGES_PATH"
cd "$SCRIPT_DIR"

# Run all 4 dataset combinations
for config in "${CONFIGS[@]}"; do
    config_path="$SCRIPT_DIR/$config"
    echo ""
    if [[ ! -f "$config_path" ]]; then
        echo "ERROR: required configuration missing: $config_path" >&2
        exit 1
    fi
    echo "--- Running: $config_path ---"
    cobaya-run "$config_path" --packages-path "$PACKAGES_PATH"
done

echo ""
echo "=== All runs complete ==="
echo "Fresh chains were written to the output paths declared by the YAML files."
echo ""
echo "This command does not regenerate the frozen publication summaries or figures."
echo "Compare fresh chains to the frozen artifacts listed in the P1B SHA-256 manifest."
