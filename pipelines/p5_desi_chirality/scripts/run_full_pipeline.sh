#!/usr/bin/env bash
# P5 end-to-end orchestrator. Runs every script in order, streams a
# structured progress log to logs/p5_run.log, writes a machine-readable
# state file at logs/progress.json that the watchdog reads.
#
# Usage:
#   ./scripts/run_full_pipeline.sh           # full run
#   FORCE=1 ./scripts/run_full_pipeline.sh   # re-download even if cached
#
# Exit codes:
#   0 = full pipeline completed
#   2 = a step failed; check progress.json["last_error"]
# NOTE: do NOT set -u — macOS bash 3.2 chokes on "${arr[@]}" with empty arrays.
P5_DIR="$(cd "$(dirname "$0")/.." && pwd)"
LOG_DIR="$P5_DIR/logs"
LOG="$LOG_DIR/p5_run.log"
PROG="$LOG_DIR/progress.json"
mkdir -p "$LOG_DIR"

# Load HF_TOKEN from .env.local without echoing it
if [[ -f "$P5_DIR/../../.env.local" ]]; then
  set -a; source "$P5_DIR/../../.env.local"; set +a
fi

ts() { date -u +%Y-%m-%dT%H:%M:%SZ; }

write_progress() {
  python3 - "$@" <<'PY' >>"$LOG" 2>&1
import json, sys, os, time
prog_path = os.environ['PROG']
state = {}
if os.path.exists(prog_path):
    try: state = json.load(open(prog_path))
    except Exception: state = {}
key = sys.argv[1]
val = sys.argv[2] if len(sys.argv) > 2 else ""
state[key] = val
state["last_update_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
json.dump(state, open(prog_path, "w"), indent=2)
PY
}
export PROG

run_step() {
  local name="$1"; shift
  echo "[$(ts)] [run] $name :: $*" | tee -a "$LOG"
  write_progress "current_step" "$name"
  write_progress "${name}_status" "running"
  if "$@" >>"$LOG" 2>&1; then
    write_progress "${name}_status" "done"
    echo "[$(ts)] [ok ] $name" | tee -a "$LOG"
  else
    local rc=$?
    write_progress "${name}_status" "failed_rc${rc}"
    write_progress "last_error" "$name failed rc=$rc"
    echo "[$(ts)] [FAIL] $name (rc=$rc)" | tee -a "$LOG"
    exit 2
  fi
}

cd "$P5_DIR"
write_progress "pipeline_started_utc" "$(ts)"

FORCE_FLAG=""
if [[ "${FORCE:-0}" == "1" ]]; then FORCE_FLAG="--force"; fi

run_step fetch_p4    python3 scripts/01_fetch_p4_catalog.py $FORCE_FLAG
run_step fetch_desi  python3 scripts/02_fetch_desi_dr1.py   $FORCE_FLAG
run_step crossmatch  python3 scripts/03_crossmatch.py
run_step diagnostics python3 scripts/04_diagnostics.py
run_step analysis_z  python3 scripts/05_analysis_redshift.py
run_step analysis_d  python3 scripts/06_analysis_density.py
run_step analysis_hp python3 scripts/07_analysis_healpix.py
run_step analysis_cw python3 scripts/08_analysis_cosmic_web.py
run_step systematics python3 scripts/09_systematics.py
run_step figures     python3 scripts/10_make_figures.py

write_progress "current_step" "complete"
write_progress "pipeline_finished_utc" "$(ts)"
echo "[$(ts)] [done] full pipeline complete" | tee -a "$LOG"
