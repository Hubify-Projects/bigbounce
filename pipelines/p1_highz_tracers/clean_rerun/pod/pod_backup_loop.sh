#!/bin/bash
# AUG-011 backup loop (standing directive E / backup-3plus):
# every 2h mirror receipts+checkpoints+audit (small) and sync shards to B2.
# Requires env: HF_TOKEN, B2_APPLICATION_KEY_ID, B2_APPLICATION_KEY, B2_BUCKET
set -uo pipefail
cd /workspace
LOG=/workspace/backup_loop.log
mark() { echo "== $(date -u +%FT%TZ) $1" | tee -a "$LOG"; }
while :; do
  mark "backup cycle start"
  b2 sync --skip-newer /workspace/shards "b2://${B2_BUCKET}/aug-011-clean-rerun/shards" >>"$LOG" 2>&1 \
    && mark "b2 shards synced" || mark "B2-SHARD-SYNC-FAILED"
  b2 sync --skip-newer /workspace/receipts "b2://${B2_BUCKET}/aug-011-clean-rerun/receipts" >>"$LOG" 2>&1 \
    && mark "b2 receipts synced" || mark "B2-RECEIPT-SYNC-FAILED"
  mkdir -p /workspace/hf_stage
  cp -f /workspace/checkpoint_w*.json /workspace/scan_audit_w*.jsonl /workspace/hf_stage/ 2>/dev/null
  python3 - <<'PY' >>"$LOG" 2>&1 && mark "hf receipts+state uploaded" || mark "HF-UPLOAD-FAILED"
import os
from huggingface_hub import HfApi
api = HfApi(token=os.environ["HF_TOKEN"])
api.upload_folder(folder_path="/workspace/hf_stage", path_in_repo="scan_state",
                  repo_id="bamfai/bigbounce-aug-011-clean-rerun", repo_type="dataset")
api.upload_folder(folder_path="/workspace/receipts", path_in_repo="receipts",
                  repo_id="bamfai/bigbounce-aug-011-clean-rerun", repo_type="dataset")
PY
  done_shards=$(ls /workspace/shards 2>/dev/null | wc -l)
  mark "progress: shards=$done_shards"
  if ! pgrep -f "run_scan.py" >/dev/null; then mark "workers done — backup loop exiting"; break; fi
  sleep 7200
done
touch /workspace/BACKUP_LOOP_DONE
