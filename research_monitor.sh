#!/bin/bash
# Research Queue Monitor v3 — Full H200 Watchdog
# Ensures the H200 is NEVER idle while it's running.
# Checks every 15 minutes: GPU utilization, experiment completion, backups, queue advancement.
#
# Run: nohup bash ./research_monitor.sh > monitor.log 2>&1 &
# Or:  bash ./research_monitor.sh  (foreground for debugging)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/.env.local" 2>/dev/null || true

H200_HOST="root@103.196.86.169"
H200_PORT=34546
SSH_KEY="$HOME/.ssh/id_ed25519"
SSH_CMD="ssh -o ConnectTimeout=30 -o StrictHostKeyChecking=no -o BatchMode=yes -i $SSH_KEY -p $H200_PORT $H200_HOST"
SCP_CMD="scp -o ConnectTimeout=30 -o StrictHostKeyChecking=no -i $SSH_KEY -P $H200_PORT"
INTERVAL=900  # 15 minutes
QUEUE_FILE="$SCRIPT_DIR/research_queue.json"
RESULTS_DIR="$SCRIPT_DIR/pipelines/h200_results"
LOG_DIR="$RESULTS_DIR/monitor_logs"

mkdir -p "$LOG_DIR"

# All experiments in priority order — maps session name to script path on H200
# Using indexed arrays for macOS/zsh compatibility (no associative arrays needed)
EXP_NAMES=(lamost planck neowise gaia act cross-survey super-resolution)
EXP_SCRIPTS=(
  "python3 -u /workspace/bigbounce/lamost_scan.py 2>&1 | tee /workspace/bigbounce/lamost_h200.log"
  "python3 -u /workspace/bigbounce/planck_cmb_scan.py 2>&1 | tee /workspace/bigbounce/planck_h200.log"
  "python3 -u /workspace/bigbounce/neowise_variability.py 2>&1 | tee /workspace/bigbounce/neowise_h200.log"
  "python3 -u /workspace/bigbounce/gaia_epoch_scan.py 2>&1 | tee /workspace/bigbounce/gaia_h200.log"
  "python3 -u /workspace/bigbounce/act_dr6_scan.py 2>&1 | tee /workspace/bigbounce/act_h200.log"
  "python3 -u /workspace/bigbounce/sdss_desi_correlation.py 2>&1 | tee /workspace/bigbounce/cross_survey_h200.log"
  "python3 -u /workspace/bigbounce/super_resolution.py 2>&1 | tee /workspace/bigbounce/super_resolution_h200.log"
)
# Queue IDs matching research_queue.json
EXP_QUEUE_IDS=(lamost-dr10 planck-cmb-full neowise-full gaia-epoch act-dr6-cmb sdss-cross-validation super-resolution)

log() {
  local msg="$(date '+%Y-%m-%d %H:%M:%S'): $1"
  echo "$msg"
  echo "$msg" >> "$LOG_DIR/monitor_$(date '+%Y%m%d').log"
}

update_queue_status() {
  # Update research_queue.json status for a given experiment
  local queue_id="$1"
  local new_status="$2"
  if command -v python3 &>/dev/null && [ -f "$QUEUE_FILE" ]; then
    python3 -c "
import json, sys
with open('$QUEUE_FILE') as f:
    q = json.load(f)
for item in q['queue']:
    if item['id'] == '$queue_id':
        item['status'] = '$new_status'
        break
counts = {'complete': 0, 'running': 0}
for item in q['queue']:
    s = item['status']
    if s in counts:
        counts[s] += 1
q['completed'] = counts['complete']
q['running'] = counts['running']
q['last_updated'] = '$(date +%Y-%m-%d)'
with open('$QUEUE_FILE', 'w') as f:
    json.dump(q, f, indent=2)
" 2>/dev/null || true
  fi
}

backup_experiment() {
  local session="$1"
  log "Backing up $session results..."
  mkdir -p "$RESULTS_DIR/$session"

  # Backup output files
  $SCP_CMD "$H200_HOST:/workspace/bigbounce/outputs/$session/*" "$RESULTS_DIR/$session/" 2>/dev/null || true
  # Backup log
  $SCP_CMD "$H200_HOST:/workspace/bigbounce/${session}_h200.log" "$RESULTS_DIR/$session/" 2>/dev/null || true
  # Backup any parquet/json results in workspace
  $SCP_CMD "$H200_HOST:/workspace/bigbounce/${session}_*.parquet" "$RESULTS_DIR/$session/" 2>/dev/null || true
  $SCP_CMD "$H200_HOST:/workspace/bigbounce/${session}_summary.json" "$RESULTS_DIR/$session/" 2>/dev/null || true

  log "Backup complete for $session. Files in $RESULTS_DIR/$session/"
}

print_queue_status() {
  if command -v python3 &>/dev/null && [ -f "$QUEUE_FILE" ]; then
    python3 -c "
import json
with open('$QUEUE_FILE') as f:
    q = json.load(f)
print()
print('  Queue Status:')
for item in q['queue']:
    s = item['status']
    icons = {'complete': 'DONE', 'running': ' RUN', 'queued': 'WAIT', 'ready': 'NEXT'}
    icon = icons.get(s, '  ? ')
    cost = item.get('est_cost', 0)
    hrs = item.get('est_hours', '?')
    print(f'    [{icon}] {item[\"name\"]}: {s} (~\${cost}, ~{hrs}h)')
print(f'  Completed: {q.get(\"completed\", \"?\")} | Running: {q.get(\"running\", \"?\")} | Updated: {q.get(\"last_updated\", \"?\")}')
" 2>/dev/null
  fi
}

log "Research Monitor v3 started. Interval: ${INTERVAL}s. Watching ${#EXP_NAMES[@]} experiments."

while true; do
  log "============================================="
  log "Checking H200 research queue"
  log "============================================="

  # 1. Check pod reachability
  if ! $SSH_CMD "echo ok" > /dev/null 2>&1; then
    log "H200 pod UNREACHABLE. Pod may be stopped or network issue."
    log "Check: https://www.runpod.io/console/pods or try SSH manually."
    sleep $INTERVAL
    continue
  fi

  # 2. GPU utilization
  GPU_UTIL=$($SSH_CMD "nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits 2>/dev/null" || echo "ERR")
  GPU_MEM=$($SSH_CMD "nvidia-smi --query-gpu=memory.used,memory.total --format=csv,noheader,nounits 2>/dev/null" || echo "ERR")
  log "GPU: ${GPU_UTIL}% utilization | Memory: ${GPU_MEM} MiB"

  # 3. Active tmux sessions
  RUNNING_SESSIONS=$($SSH_CMD "tmux ls 2>/dev/null" || echo "(none)")
  log "Tmux sessions: $RUNNING_SESSIONS"

  # 4. Disk usage
  DISK=$($SSH_CMD "df -h /workspace | tail -1 | awk '{print \$3\"/\"\$2\" (\"\$5\" used)\"}'" 2>/dev/null || echo "ERR")
  log "Disk: $DISK"

  # 5. Check each experiment for completion
  FOUND_RUNNING=false
  for i in "${!EXP_NAMES[@]}"; do
    session="${EXP_NAMES[$i]}"
    queue_id="${EXP_QUEUE_IDS[$i]}"
    LOG_FILE="/workspace/bigbounce/${session}_h200.log"

    # Check if this experiment's log shows COMPLETE
    COMPLETE=$($SSH_CMD "grep -c 'COMPLETE\|ALL DONE\|Finished\|Total anomalies' $LOG_FILE 2>/dev/null" || echo "0")

    if [ "$COMPLETE" -gt "0" ]; then
      # Check if already backed up
      if [ -f "$RESULTS_DIR/$session/${session}_h200.log" ]; then
        continue  # Already handled
      fi

      log "$session COMPLETED! Running backup..."
      backup_experiment "$session"
      update_queue_status "$queue_id" "complete"

      # Kill the completed tmux session
      $SSH_CMD "tmux kill-session -t $session 2>/dev/null" || true
      log "$session: backed up and session cleaned."
    fi

    # Check if currently running in tmux
    if echo "$RUNNING_SESSIONS" | grep -q "$session"; then
      FOUND_RUNNING=true
      LAST_LINE=$($SSH_CMD "tail -1 $LOG_FILE 2>/dev/null" || echo "(no output yet)")
      log "  RUNNING [$session]: $LAST_LINE"
    fi
  done

  # 6. If nothing running, start next experiment
  if [ "$FOUND_RUNNING" = false ]; then
    # Double-check no tmux sessions at all
    ACTIVE=$($SSH_CMD "tmux ls 2>/dev/null | grep -c ':'" || echo "0")
    if [ "$ACTIVE" -eq "0" ]; then
      log "GPU IS IDLE! (\$3.59/hr being wasted)"
      log "Looking for next experiment to start..."

      STARTED=false
      for i in "${!EXP_NAMES[@]}"; do
        session="${EXP_NAMES[$i]}"
        queue_id="${EXP_QUEUE_IDS[$i]}"
        LOG_FILE="/workspace/bigbounce/${session}_h200.log"

        # Skip if already completed
        ALREADY_DONE=$($SSH_CMD "grep -c 'COMPLETE\|ALL DONE\|Finished\|Total anomalies' $LOG_FILE 2>/dev/null" || echo "0")
        if [ "$ALREADY_DONE" -gt "0" ]; then
          continue
        fi

        # Skip if script doesn't exist on pod
        SCRIPT_EXISTS=$($SSH_CMD "ls /workspace/bigbounce/${session}*.py 2>/dev/null | head -1" || echo "")
        if [ -z "$SCRIPT_EXISTS" ]; then
          log "  Skipping $session — script not deployed yet."
          continue
        fi

        log "Starting experiment: $session"
        $SSH_CMD "tmux new-session -d -s $session '${EXP_SCRIPTS[$i]}'" 2>/dev/null
        update_queue_status "$queue_id" "running"
        log "$session LAUNCHED!"
        STARTED=true
        break
      done

      if [ "$STARTED" = false ]; then
        log "All experiments either complete or not yet deployed."
        log "Deploy next script to /workspace/bigbounce/ on H200 to continue."
      fi
    fi
  fi

  # 7. Print full queue status
  print_queue_status

  log "Next check in ${INTERVAL}s ($(date -v+${INTERVAL}S '+%H:%M' 2>/dev/null || date -d "+${INTERVAL} seconds" '+%H:%M' 2>/dev/null || echo '?'))"
  sleep $INTERVAL
done
