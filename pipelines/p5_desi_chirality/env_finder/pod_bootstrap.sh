#!/bin/bash
# P5 Track B pod bootstrap — runs the full Zel'dovich-reconstruction V-Web
# pipeline end-to-end on a RunPod pod with >=96 GB RAM.
#
# Usage (on the pod, after rsyncing the env_finder/ directory and the
# p5_matched_chirality_desi.parquet into /workspace):
#
#   bash pod_bootstrap.sh 2>&1 | tee /workspace/p5_track_b.log
#
# Outputs land in /workspace/p5_track_b_output/ and are pulled back via
# rsync from the local machine.
set -euo pipefail

WORKSPACE=/workspace
SCRIPTS_DIR=$WORKSPACE/env_finder
LSS_DIR=$WORKSPACE/desi_lss_v1p5
RECON_DIR=$WORKSPACE/desi_recon
OUT_DIR=$WORKSPACE/p5_track_b_output
LOG_DIR=$WORKSPACE/p5_track_b_logs
mkdir -p $RECON_DIR $OUT_DIR $LOG_DIR

echo "[$(date -u +%FT%TZ)] === P5 Track B pod bootstrap starting ==="

# 1. System deps (Ubuntu / Debian).
echo "[$(date -u +%FT%TZ)] Phase 0: system deps"
apt-get update -qq
apt-get install -y -qq git build-essential gcc g++ libfftw3-dev python3-pip rsync wget curl

# 2. Python deps. Pin numpy < 2 to keep pyrecon ABI happy.
echo "[$(date -u +%FT%TZ)] Phase 0: python deps"
pip install --quiet --upgrade pip
pip install --quiet 'numpy<2' scipy pandas pyarrow astropy fitsio pyyaml
pip install --quiet 'pyrecon[default] @ git+https://github.com/cosmodesi/pyrecon'

# 3. Phase 1+2: Run the pyrecon driver (downloads LSS catalogs +
# runs pyrecon per tracer + writes combined recon parquet).
echo "[$(date -u +%FT%TZ)] Phase 1+2: pyrecon driver"
python3 $SCRIPTS_DIR/00_pyrecon_driver.py \
    --lss-dir $LSS_DIR \
    --out-dir $RECON_DIR \
    --n-rand-files 4 \
    --tracers BGS_BRIGHT LRG ELG_LOPnotqso QSO \
    2>&1 | tee $LOG_DIR/00_pyrecon.log

# 4. Phase 3: V-Web on reconstructed positions at R_s=8 Mpc/h.
# Override the input path to the pod-side recon parquet.
echo "[$(date -u +%FT%TZ)] Phase 3: V-Web on reconstructed positions"
RECON_CONFIG=/tmp/recon_config_pod.yaml
sed "s|pipelines/p5_desi_chirality/data/desi_recon/desi_recon_combined.parquet|$RECON_DIR/desi_recon_combined.parquet|g; s|pipelines/p5_desi_chirality/data/desi_env/desi_env_vweb_recon_R8_N1024.parquet|$OUT_DIR/desi_env_vweb_recon_R8_N1024.parquet|g; s|pipelines/p5_desi_chirality/env_finder/reports/01b_volume_fractions_recon_R8_N1024.json|$OUT_DIR/01b_volume_fractions_recon_R8_N1024.json|g" \
    $SCRIPTS_DIR/recon_config.yaml > $RECON_CONFIG

python3 $SCRIPTS_DIR/02_compute_vweb_recon.py \
    --config $RECON_CONFIG \
    --repo-root $WORKSPACE \
    2>&1 | tee $LOG_DIR/02_vweb_recon.log

echo "[$(date -u +%FT%TZ)] === P5 Track B pod bootstrap DONE ==="
echo "Outputs in $OUT_DIR:"
ls -lh $OUT_DIR
echo "Logs in $LOG_DIR:"
ls -lh $LOG_DIR
