#!/bin/bash
# Bootstrap a fresh pod for AUG-011 phase 3 from committed inputs + the B2 corpus.
# Expects the repo subtree at /workspace/bigbounce and env: B2_APPLICATION_KEY_ID,
# B2_APPLICATION_KEY, B2_BUCKET, HF_TOKEN. Fails closed on any hash mismatch.
set -euo pipefail
cd /workspace
R=/workspace/bigbounce/pipelines/p1_highz_tracers
LOG=/workspace/bootstrap.log
mark() { echo "== $(date -u +%FT%TZ) $1" | tee -a "$LOG"; }

mark "deps"
pip install -q astropy pyarrow scipy umap-learn astroquery scikit-learn b2 huggingface_hub 2>&1 | tail -1

mark "model + inference-code hash gate"
[ "$(sha256sum /workspace/bigbounce/best_model_47k.pt | cut -c1-64)" = "f5266ba48f476bca2f1b12610e0e81322caaa955af70ab83f0b05bf763885f07" ] || { mark "FATAL model sha"; exit 1; }
[ "$(sha256sum $R/outputs/enhanced_18M/enhanced_18M_inference.py | cut -c1-64)" = "3e7efb243fa5cc4e7e06c5ce8e13f011e1173d2cc44aecd8df47e0c67c0ab996" ] || { mark "FATAL inference-code sha"; exit 1; }

mark "sealed inputs -> /workspace"
cp "$R/clean_rerun/sealed_2026-08-05/"{input_manifest.json,calibration.json,run-contract.json,locator_inventory.jsonl} /workspace/
cp "$R/clean_rerun/results_2026-08-07/summary.json" /workspace/summary.json

mark "zcatalog download + SHA gate"
[ -f /workspace/zall-pix-iron.fits ] || curl -sSO https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/zall-pix-iron.fits
[ "$(sha256sum /workspace/zall-pix-iron.fits | cut -c1-64)" = "2d95ad99361039b556c402b49e0e7c84df5f00106dc5731d44476a58b128b49b" ] || { mark "FATAL zcatalog sha"; exit 1; }

mark "corpus restore from B2 (shards + receipts)"
b2 account authorize "$B2_APPLICATION_KEY_ID" "$B2_APPLICATION_KEY" >/dev/null 2>&1 || b2 authorize-account "$B2_APPLICATION_KEY_ID" "$B2_APPLICATION_KEY" >/dev/null
mkdir -p /workspace/shards /workspace/receipts
b2 sync "b2://${B2_BUCKET}/aug-011-clean-rerun/shards"   /workspace/shards   >>"$LOG" 2>&1
b2 sync "b2://${B2_BUCKET}/aug-011-clean-rerun/receipts" /workspace/receipts >>"$LOG" 2>&1
mark "shards=$(ls /workspace/shards | wc -l) receipts=$(ls /workspace/receipts | wc -l)"

mark "full-corpus verify-receipts (contract gate)"
python3 "$R/clean_rerun_contract.py" verify-receipts --contract /workspace/run-contract.json \
  --shard-dir /workspace/shards --receipt-dir /workspace/receipts 2>&1 | tail -2 | tee -a "$LOG"

mark "launch phase 3 (detached)"
setsid nohup "$R/clean_rerun/pod/pod_phase3.sh" > /workspace/phase3_stdout.log 2>&1 < /dev/null &
mark "BOOTSTRAP-DONE (phase3 running; marker /workspace/PHASE3_DONE)"
touch /workspace/BOOTSTRAP_DONE
