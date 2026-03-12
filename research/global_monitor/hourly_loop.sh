#!/usr/bin/env bash
# ===========================================================================
# BigBounce Global Monitor — Hourly Loop
# ===========================================================================
# Runs run_all_monitors.sh every hour in the background.
# Logs to logs/hourly_TIMESTAMP.log
#
# Usage:
#   ./hourly_loop.sh &          # run in background
#   ./hourly_loop.sh --once     # single run (for testing)
#
# To stop:
#   kill $(cat /tmp/bigbounce_hourly_monitor.pid)
# ===========================================================================

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PID_FILE="/tmp/bigbounce_hourly_monitor.pid"
INTERVAL=3600  # 1 hour

# Check for --once flag
ONCE=false
if [[ "${1:-}" == "--once" ]]; then
    ONCE=true
fi

# Write PID file
echo $$ > "${PID_FILE}"
echo "[$(date -u '+%Y-%m-%d %H:%M:%S UTC')] Hourly monitor started (PID $$)"
echo "[$(date -u '+%Y-%m-%d %H:%M:%S UTC')] PID file: ${PID_FILE}"
echo "[$(date -u '+%Y-%m-%d %H:%M:%S UTC')] Interval: ${INTERVAL}s"
echo ""

cleanup() {
    echo "[$(date -u '+%Y-%m-%d %H:%M:%S UTC')] Hourly monitor stopping (PID $$)"
    rm -f "${PID_FILE}"
    exit 0
}
trap cleanup SIGTERM SIGINT

while true; do
    echo "============================================================"
    echo "[$(date -u '+%Y-%m-%d %H:%M:%S UTC')] Starting monitor run..."
    echo "============================================================"

    bash "${SCRIPT_DIR}/run_all_monitors.sh" 2>&1 | \
        tee "${SCRIPT_DIR}/logs/hourly_$(date -u +%Y%m%d_%H%M%S).log"

    EXIT_CODE=$?
    echo ""
    echo "[$(date -u '+%Y-%m-%d %H:%M:%S UTC')] Monitor run finished (exit ${EXIT_CODE})"

    if [ "${ONCE}" = true ]; then
        echo "[$(date -u '+%Y-%m-%d %H:%M:%S UTC')] --once flag set, exiting."
        rm -f "${PID_FILE}"
        exit ${EXIT_CODE}
    fi

    echo "[$(date -u '+%Y-%m-%d %H:%M:%S UTC')] Next run in ${INTERVAL}s ($(date -u -v+${INTERVAL}S '+%H:%M:%S UTC' 2>/dev/null || date -u -d "+${INTERVAL} seconds" '+%H:%M:%S UTC' 2>/dev/null || echo 'in 1 hour'))"
    echo ""

    sleep ${INTERVAL} &
    wait $!
done
