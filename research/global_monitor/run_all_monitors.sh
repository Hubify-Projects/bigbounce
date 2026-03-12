#!/usr/bin/env bash
# ===========================================================================
# BigBounce Global Monitor — Run All
# ===========================================================================
# Single entrypoint that runs status, backup, and artifact index in order.
# Saves combined log to logs/TIMESTAMP.log
#
# Usage:
#   ./run_all_monitors.sh [--timeout SECONDS] [--dry-run] [--pod POD_NAME]
# ===========================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_DIR="${SCRIPT_DIR}/logs"
TIMESTAMP="$(date -u +%Y%m%d_%H%M%S)"
LOG_FILE="${LOG_DIR}/${TIMESTAMP}.log"

# Forward args
EXTRA_ARGS=("${@:+$@}")

# Colors
BOLD="\033[1m"
CYAN="\033[96m"
GREEN="\033[92m"
YELLOW="\033[93m"
RED="\033[91m"
RESET="\033[0m"
SEP="============================================================================"

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------
mkdir -p "${LOG_DIR}"

echo -e "${BOLD}${CYAN}${SEP}${RESET}"
echo -e "${BOLD}${CYAN}  BIGBOUNCE GLOBAL MONITOR — FULL SCAN${RESET}"
echo -e "${BOLD}${CYAN}  $(date -u '+%Y-%m-%d %H:%M:%S UTC')${RESET}"
echo -e "${BOLD}${CYAN}${SEP}${RESET}"
echo ""

START_TIME=$(date +%s)

# ---------------------------------------------------------------------------
# 1. Global Status
# ---------------------------------------------------------------------------
echo -e "${BOLD}[1/4] Running global_status.py ...${RESET}"
echo ""

STATUS_EXIT=0
python3 "${SCRIPT_DIR}/global_status.py" ${EXTRA_ARGS[@]+"${EXTRA_ARGS[@]}"} 2>&1 | tee -a "${LOG_FILE}" || STATUS_EXIT=$?

echo ""
if [ "${STATUS_EXIT}" -eq 0 ]; then
    echo -e "  ${GREEN}Status check completed successfully.${RESET}"
else
    echo -e "  ${YELLOW}Status check completed with warnings (exit ${STATUS_EXIT}).${RESET}"
fi
echo ""

# ---------------------------------------------------------------------------
# 2. GPU Freeze Manager (convergence-only freeze logic)
# ---------------------------------------------------------------------------
echo -e "${BOLD}[2/4] Running gpu_freeze_manager.py ...${RESET}"
echo ""

FREEZE_EXIT=0
python3 "${SCRIPT_DIR}/gpu_freeze_manager.py" ${EXTRA_ARGS[@]+"${EXTRA_ARGS[@]}"} 2>&1 | tee -a "${LOG_FILE}" || FREEZE_EXIT=$?

echo ""
if [ "${FREEZE_EXIT}" -eq 0 ]; then
    echo -e "  ${GREEN}Freeze manager completed successfully.${RESET}"
else
    echo -e "  ${YELLOW}Freeze manager completed with issues (exit ${FREEZE_EXIT}).${RESET}"
fi
echo ""

# ---------------------------------------------------------------------------
# 3. Global Backup
# ---------------------------------------------------------------------------
echo -e "${BOLD}[3/4] Running global_backup.py ...${RESET}"
echo ""

BACKUP_EXIT=0
python3 "${SCRIPT_DIR}/global_backup.py" ${EXTRA_ARGS[@]+"${EXTRA_ARGS[@]}"} 2>&1 | tee -a "${LOG_FILE}" || BACKUP_EXIT=$?

echo ""
if [ "${BACKUP_EXIT}" -eq 0 ]; then
    echo -e "  ${GREEN}Backup completed successfully.${RESET}"
else
    echo -e "  ${RED}Backup had errors (exit ${BACKUP_EXIT}).${RESET}"
fi
echo ""

# ---------------------------------------------------------------------------
# 4. Artifact Index
# ---------------------------------------------------------------------------
echo -e "${BOLD}[4/4] Running global_artifact_index.py ...${RESET}"
echo ""

ARTIFACT_EXIT=0
python3 "${SCRIPT_DIR}/global_artifact_index.py" ${EXTRA_ARGS[@]+"${EXTRA_ARGS[@]}"} 2>&1 | tee -a "${LOG_FILE}" || ARTIFACT_EXIT=$?

echo ""
if [ "${ARTIFACT_EXIT}" -eq 0 ]; then
    echo -e "  ${GREEN}Artifact index completed successfully.${RESET}"
else
    echo -e "  ${RED}Artifact index had errors (exit ${ARTIFACT_EXIT}).${RESET}"
fi
echo ""

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
END_TIME=$(date +%s)
ELAPSED=$(( END_TIME - START_TIME ))

echo -e "${BOLD}${CYAN}${SEP}${RESET}"
echo -e "${BOLD}${CYAN}  MONITOR RUN COMPLETE${RESET}"
echo -e "${BOLD}${CYAN}${SEP}${RESET}"
echo ""
echo -e "  Duration:      ${ELAPSED}s"
echo -e "  Status exit:   ${STATUS_EXIT}"
echo -e "  Freeze exit:   ${FREEZE_EXIT}"
echo -e "  Backup exit:   ${BACKUP_EXIT}"
echo -e "  Artifact exit: ${ARTIFACT_EXIT}"
echo -e "  Log file:      ${LOG_FILE}"
echo ""

# List all output files
echo -e "${BOLD}Output files:${RESET}"
for f in \
    "${SCRIPT_DIR}/global_status_latest.txt" \
    "${SCRIPT_DIR}/global_status_latest.json" \
    "${SCRIPT_DIR}/project_status_latest.txt" \
    "${SCRIPT_DIR}/project_status_latest.json" \
    "${SCRIPT_DIR}/global_backup_latest.txt" \
    "${SCRIPT_DIR}/artifact_index.csv" \
    "${SCRIPT_DIR}/artifact_index_latest.txt"; do
    if [ -f "${f}" ]; then
        SIZE=$(du -sh "${f}" 2>/dev/null | awk '{print $1}')
        echo -e "  ${GREEN}[OK]${RESET}  ${f}  (${SIZE})"
    else
        echo -e "  ${YELLOW}[--]${RESET}  ${f}  (not created)"
    fi
done
echo ""

# Overall exit code
OVERALL_EXIT=0
if [ "${STATUS_EXIT}" -ne 0 ] || [ "${FREEZE_EXIT}" -ne 0 ] || [ "${BACKUP_EXIT}" -ne 0 ] || [ "${ARTIFACT_EXIT}" -ne 0 ]; then
    OVERALL_EXIT=1
fi

exit ${OVERALL_EXIT}
