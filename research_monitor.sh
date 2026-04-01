#!/bin/bash
# Research Queue Monitor
# Checks H200 pod status every 15 minutes.
# If the current experiment is done, starts the next one in the queue.
# Run: nohup ./research_monitor.sh > monitor.log 2>&1 &

set -e

source "$(dirname "$0")/.env.local"

H200_HOST="root@103.196.86.169"
H200_PORT=34546
SSH_KEY="$HOME/.ssh/id_ed25519"
SSH="ssh -o ConnectTimeout=30 -o StrictHostKeyChecking=no -i $SSH_KEY -p $H200_PORT $H200_HOST"
INTERVAL=900  # 15 minutes
QUEUE_FILE="$(dirname "$0")/research_queue.json"

echo "$(date): Research monitor started. Interval: ${INTERVAL}s"

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

    # 2. Check if anything is running
    RUNNING=$($SSH "tmux ls 2>/dev/null | grep -c ':'" || echo "0")

    if [ "$RUNNING" -gt "0" ]; then
        # Something is running - check progress
        SESSIONS=$($SSH "tmux ls 2>/dev/null" || echo "none")
        echo "Active sessions: $SESSIONS"

        # Check the log for the latest session
        for SESSION in sdss erosita lamost planck neowise gaia; do
            LOG=$($SSH "tail -3 /workspace/bigbounce/${SESSION}*.log 2>/dev/null" || true)
            if [ -n "$LOG" ]; then
                echo "  $SESSION: $(echo $LOG | tail -1)"
            fi
        done

        # Check for COMPLETE in logs
        COMPLETE=$($SSH "grep -l 'COMPLETE' /workspace/bigbounce/*.log 2>/dev/null" || true)
        if [ -n "$COMPLETE" ]; then
            echo "$(date): EXPERIMENT COMPLETED! Backing up results..."

            # Backup results locally
            scp -o StrictHostKeyChecking=no -i "$SSH_KEY" -P "$H200_PORT" -r "$H200_HOST:/workspace/bigbounce/outputs/" "$(dirname "$0")/pipelines/h200_results/" 2>/dev/null

            echo "$(date): Results backed up. Ready for next experiment."
            # TODO: auto-start next experiment from queue
        fi
    else
        echo "$(date): No experiments running on H200!"
        echo "  GPU is IDLE and costing \$3.59/hr"
        echo "  Check research_queue.json for next experiment"
    fi

    # 3. Show queue status
    if [ -f "$QUEUE_FILE" ]; then
        echo ""
        echo "Queue status:"
        python3 -c "
import json
with open('$QUEUE_FILE') as f:
    q = json.load(f)
for item in q['queue']:
    status = item['status']
    icon = '🟢' if status == 'running' else '⏳' if status == 'queued' else '⏸️'
    print(f'  {icon} {item[\"name\"]}: {status} (~\${item[\"est_cost\"]}, ~{item[\"est_hours\"]}h)')
" 2>/dev/null
    fi

    echo "$(date): Next check in ${INTERVAL}s"
    sleep $INTERVAL
done
