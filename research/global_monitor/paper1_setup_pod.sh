#!/bin/bash
# Paper-1 Clean Restart — Pod Setup Script
# Run this on the RunPod pod AFTER SSH access is confirmed.
# Usage: bash paper1_setup_pod.sh
set -euo pipefail

echo "=========================================="
echo "Paper-1 Clean Restart — Pod Setup"
echo "=========================================="
echo "Date: $(date -u)"
echo ""

# 1. System info
echo "[1/8] System information"
echo "  CPU cores: $(nproc)"
echo "  RAM: $(free -h | awk '/Mem:/ {print $2}')"
echo "  Disk (workspace): $(df -h /workspace | awk 'NR==2 {print $2, "total,", $4, "avail"}')"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader 2>/dev/null || echo "  GPU: N/A"
echo ""

# 2. Install cosmology stack
echo "[2/8] Installing Cobaya + CAMB + cosmology dependencies..."
pip install -q cobaya camb healpy getdist scipy matplotlib numpy pandas pyyaml 2>&1 | tail -3
echo "  Cobaya version: $(python3 -c 'import cobaya; print(cobaya.__version__)' 2>/dev/null || echo 'FAILED')"
echo "  CAMB version: $(python3 -c 'import camb; print(camb.__version__)' 2>/dev/null || echo 'FAILED')"
echo ""

# 3. Install Planck likelihoods
echo "[3/8] Installing Planck likelihoods (this takes a few minutes)..."
cobaya-install planck_2018_lowl.TT planck_2018_lowl.EE planck_2018_lensing.clik planck_NPIPE_highl_CamSpec.TTTEEE --path /workspace/cobaya_packages 2>&1 | tail -5
echo ""

# 4. Install BAO + SN likelihoods
echo "[4/8] Installing BAO + SN likelihoods..."
cobaya-install bao.sdss_dr16_baoplus_lrg bao.sdss_dr16_baoplus_lyauto bao.sdss_dr16_baoplus_lyxqso bao.sdss_dr16_baoplus_qso bao.sdss_dr7_mgs bao.sixdf_2011_bao sn.pantheonplus --path /workspace/cobaya_packages 2>&1 | tail -5
echo ""

# 5. Create directory structure
echo "[5/8] Creating canonical run directory structure..."
CANONICAL="/workspace/bigbounce/reproducibility/cosmology/canonical_run_001"
mkdir -p "$CANONICAL"/{dneff,lcdm}/{full_tension,planck_only,planck_bao,planck_bao_sn}/{chain_01,chain_02,chain_03,chain_04}
mkdir -p "$CANONICAL"/warm_start_assets/gpu_20260305_covmats
mkdir -p /workspace/backups/{hourly,snapshots,manifests}
mkdir -p /workspace/logs/{cobaya,monitor,backup}
echo "  Directory structure created at $CANONICAL"
echo ""

# 6. Set COBAYA_PACKAGES_PATH
echo "[6/8] Setting environment..."
echo 'export COBAYA_PACKAGES_PATH=/workspace/cobaya_packages' >> ~/.bashrc
export COBAYA_PACKAGES_PATH=/workspace/cobaya_packages
echo "  COBAYA_PACKAGES_PATH=/workspace/cobaya_packages"
echo ""

# 7. Quick CAMB test
echo "[7/8] Running quick CAMB test..."
python3 -c "
import camb
pars = camb.set_params(H0=67.5, ombh2=0.022, omch2=0.12, ns=0.965, As=2.1e-9, tau=0.054)
results = camb.get_results(pars)
print(f'  CAMB test: H0={results.hubble_parameter(0):.1f}, sigma8={results.get_sigma8_0():.4f}')
print('  CAMB: OK')
" 2>&1
echo ""

# 8. Summary
echo "[8/8] Setup Summary"
echo "  Pod ready for chain deployment"
echo "  Next steps:"
echo "    1. Upload covmats from local machine"
echo "    2. Generate Cobaya YAML configs"
echo "    3. Launch chains"
echo ""
echo "=========================================="
echo "Setup complete: $(date -u)"
echo "=========================================="
