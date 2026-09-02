#!/bin/bash
# AUG-011 babysitter v4 — /proc/<pid>/exe-based worker identification.
# v3 fatal flaw: PyTorch renames worker comm to "pt_main_thread", so comm
# filters saw zero workers and relaunched forever. exe symlink is authoritative:
# real workers exec python3.x; bash -c wrappers exec /bin/bash.
set -uo pipefail
cd /workspace
R=/workspace/bigbounce/pipelines/p1_highz_tracers
N_WORKERS=12
TOTAL=$(wc -l < /workspace/locator_inventory.jsonl)
step=$(( (TOTAL + N_WORKERS - 1) / N_WORKERS ))
LOG=/workspace/babysitter.log
mark() { echo "== $(date -u +%FT%TZ) [v4] $1" | tee -a "$LOG"; }
declare -A restarts

pythons_for_range() {  # $1=start -> real python worker pids, oldest first
  for p in $(pgrep -f -- "run_scan\.py.*--start $1 --end"); do
    exe=$(readlink "/proc/$p/exe" 2>/dev/null)
    case "$exe" in *python*) ;; *) continue ;; esac
    et=$(ps -o etimes= -p "$p" 2>/dev/null | tr -d ' ')
    [ -n "$et" ] && printf "%s %s\n" "$et" "$p"
  done | sort -rn | awk '{print $2}'
}

relaunch() {
  local w=$1 start=$2 end=$3
  nohup bash -c "python3 '$R/clean_rerun/run_scan.py' \
    --inventory /workspace/locator_inventory.jsonl \
    --contract /workspace/run-contract.json \
    --model /workspace/bigbounce/best_model_47k.pt \
    --group-targetids /workspace/group_targetids.parquet \
    --audit-log /workspace/scan_audit_w${w}.jsonl \
    --shard-dir /workspace/shards \
    --receipt-dir /workspace/receipts \
    --checkpoint /workspace/checkpoint_w${w}.json \
    --coadd-cache-dir /workspace/coadd_cache_w${w} \
    --start $start --end $end \
    && echo 'range complete'" >> /workspace/worker_w${w}.log 2>&1 &
  mark "relaunched worker $w range=$start-$end (restart #${restarts[$w]:-0})"
}

mark "babysitter v4 online: $N_WORKERS ranges, step=$step"
while :; do
  all_done=1
  for w in $(seq 0 $((N_WORKERS - 1))); do
    start=$((w * step)); end=$(((w + 1) * step)); [ "$end" -gt "$TOTAL" ] && end=$TOTAL
    mapfile -t pids < <(pythons_for_range "$start")
    if [ "${#pids[@]}" -gt 1 ]; then
      for dup in "${pids[@]:1}"; do
        kill "$dup" 2>/dev/null
        mark "killed duplicate worker $dup for range $start (kept ${pids[0]})"
      done
      all_done=0; continue
    fi
    if [ "${#pids[@]}" -eq 1 ]; then all_done=0; continue; fi
    if tail -3 /workspace/worker_w${w}.log 2>/dev/null | grep -aq "range complete"; then
      continue
    fi
    restarts[$w]=$(( ${restarts[$w]:-0} + 1 ))
    if [ "${restarts[$w]}" -gt 400 ]; then
      mark "worker $w exceeded restart budget — leaving down"; continue
    fi
    all_done=0
    sleep $(( (RANDOM % 10) + 3 ))
    relaunch "$w" "$start" "$end"
  done
  [ "$all_done" -eq 1 ] && { mark "all ranges complete — babysitter v4 exiting"; break; }
  sleep 240
done
touch /workspace/SCAN_ALL_DONE
