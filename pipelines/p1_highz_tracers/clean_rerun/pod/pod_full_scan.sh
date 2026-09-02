#!/bin/bash
# AUG-011 full scan: N parallel workers over the 36,634-group inventory.
set -euo pipefail
cd /workspace
R=/workspace/bigbounce/pipelines/p1_highz_tracers
N_WORKERS=${N_WORKERS:-12}
TOTAL=$(wc -l < /workspace/locator_inventory.jsonl)
LOG=/workspace/full_scan.log
mark() { echo "== $(date -u +%FT%TZ) $1" | tee -a "$LOG"; }
mkdir -p /workspace/shards /workspace/receipts
mark "full-scan launch: $TOTAL groups, $N_WORKERS workers"
step=$(( (TOTAL + N_WORKERS - 1) / N_WORKERS ))
for w in $(seq 0 $((N_WORKERS - 1))); do
  start=$((w * step)); end=$(((w + 1) * step)); [ "$end" -gt "$TOTAL" ] && end=$TOTAL
  nohup python3 "$R/clean_rerun/run_scan.py" \
    --inventory /workspace/locator_inventory.jsonl --contract /workspace/run-contract.json \
    --model /workspace/bigbounce/best_model_47k.pt --group-targetids /workspace/group_targetids.parquet \
    --audit-log /workspace/scan_audit_w${w}.jsonl --shard-dir /workspace/shards --receipt-dir /workspace/receipts \
    --checkpoint /workspace/checkpoint_w${w}.json --coadd-cache-dir /workspace/coadd_cache_w${w} \
    --start "$start" --end "$end" > /workspace/worker_w${w}.log 2>&1 &
  mark "worker $w launched pid=$! range=$start-$end"
done
mark "all workers launched"
