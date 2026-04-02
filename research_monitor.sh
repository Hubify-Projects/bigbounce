#!/bin/bash
# Research Queue Monitor v2
# Checks H200 pod status every 15 minutes.
# When an experiment completes, backs up results and starts the next one.
# Run: nohup ./research_monitor.sh > monitor.log 2>&1 &

set -e

source "$(dirname "$0")/.env.local"

H200_HOST="root@103.196.86.169"
H200_PORT=34546
SSH_KEY="$HOME/.ssh/id_ed25519"
SSH="ssh -o ConnectTimeout=30 -o StrictHostKeyChecking=no -i $SSH_KEY -p $H200_PORT $H200_HOST"
INTERVAL=900  # 15 minutes
QUEUE_FILE="$(dirname "$0")/research_queue.json"
RESULTS_DIR="$(dirname "$0")/pipelines/h200_results"

# Experiment definitions: session_name → script
declare -A EXPERIMENTS
EXPERIMENTS[lamost]="python3 -u /workspace/bigbounce/lamost_scan.py 2>&1 | tee /workspace/bigbounce/lamost_h200.log"
EXPERIMENTS[planck]="python3 -u /workspace/bigbounce/planck_cmb_scan.py 2>&1 | tee /workspace/bigbounce/planck_h200.log"

# Order of experiments
EXPERIMENT_ORDER=(lamost planck)

echo "$(date): Research monitor v2 started. Interval: ${INTERVAL}s"

while true; do
    echo ""
    echo "============================================="
    echo "$(date): Checking research queue"
    echo "============================================="

    # 1. Check if pod is reachable
    if ! $SSH "echo ok" > /dev/null 2>&1; then
        echo "$(date): H200 pod unreachable. Waiting..."
        sleep $INTERVAL
        continue
    fi

    # 2. Check GPU utilization
    GPU_UTIL=$($SSH "nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits" 2>/dev/null || echo "0")
    echo "GPU utilization: ${GPU_UTIL}%"

    # 3. Check what's running
    RUNNING_SESSIONS=$($SSH "tmux ls 2>/dev/null" || echo "none")
    echo "Active tmux sessions: $RUNNING_SESSIONS"

    # 4. Check for COMPLETE in any experiment log
    for session in "${EXPERIMENT_ORDER[@]}"; do
        LOG="/workspace/bigbounce/${session}_h200.log"
        COMPLETE=$($SSH "grep -c 'COMPLETE' $LOG 2>/dev/null" || echo "0")
        if [ "$COMPLETE" -gt "0" ]; then
            echo "$(date): $session COMPLETED! Backing up..."

            # Backup results
            mkdir -p "$RESULTS_DIR/$session"
            scp -o StrictHostKeyChecking=no -i "$SSH_KEY" -P "$H200_PORT" \
                "$H200_HOST:/workspace/bigbounce/outputs/$session/*" \
                "$RESULTS_DIR/$session/" 2>/dev/null || true
            scp -o StrictHostKeyChecking=no -i "$SSH_KEY" -P "$H200_PORT" \
                "$H200_HOST:$LOG" \
                "$RESULTS_DIR/$session/" 2>/dev/null || true

            echo "$(date): $session backed up."

            # Kill the completed session
            $SSH "tmux kill-session -t $session 2>/dev/null" || true
        fi
    done

    # 5. Check if anything is running. If not, start next experiment.
    ACTIVE=$($SSH "tmux ls 2>/dev/null | grep -c ':'" || echo "0")
    if [ "$ACTIVE" -eq "0" ]; then
        echo "$(date): No experiments running. GPU is IDLE (\$3.59/hr)!"

        # Find next experiment to run
        for session in "${EXPERIMENT_ORDER[@]}"; do
            LOG="/workspace/bigbounce/${session}_h200.log"
            ALREADY_DONE=$($SSH "grep -c 'COMPLETE' $LOG 2>/dev/null" || echo "0")
            if [ "$ALREADY_DONE" -eq "0" ]; then
                echo "$(date): Starting next experiment: $session"
                $SSH "tmux new-session -d -s $session '${EXPERIMENTS[$session]}'" 2>/dev/null
                echo "$(date): $session launched!"
                break
            fi
        done
    else
        # Show progress of running experiment
        for session in "${EXPERIMENT_ORDER[@]}"; do
            LOG="/workspace/bigbounce/${session}_h200.log"
            LAST_LINE=$($SSH "tail -1 $LOG 2>/dev/null" || echo "")
            if [ -n "$LAST_LINE" ]; then
                echo "  $session: $LAST_LINE"
            fi
        done
    fi

    # 6. Show queue status
    echo ""
    echo "Queue status:"
    python3 -c "
import json
with open('$QUEUE_FILE') as f:
    q = json.load(f)
for item in q['queue']:
    s = item['status']
    icon = 'DONE' if s == 'complete' else 'RUN' if s == 'running' else 'WAIT'
    print(f'  [{icon}] {item[\"name\"]}: {s} (~\${item[\"est_cost\"]}, ~{item[\"est_hours\"]}h)')
" 2>/dev/null

    echo "$(date): Next check in ${INTERVAL}s"
    sleep $INTERVAL
done
