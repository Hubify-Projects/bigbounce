#!/usr/bin/env bash
# Row 16 step (ii) — N=20,000 pixel-level parity-injection test, full local
# pipeline: sample -> inference (production equivariant TTA forward pass,
# local MPS device) -> analysis (f in {0,0.5,1,2,5}% x 10 seeds) -> figure.
# Idempotent: each stage is skipped if its marker file already exists.
# Designed to be launched detached (nohup ... &) and left to run for hours.
set -e
set -u

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$HERE"

RUN_DIR="$HERE/row16_local"
mkdir -p "$RUN_DIR"
LOG="$RUN_DIR/run.log"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG"
}

PY=python3

fail() {
  log "FAILED at stage: $1"
  touch "$RUN_DIR/ROW16_FAILED"
  exit 1
}

log "=== row16 local run starting (pid $$) ==="

# --- Stage 1: sample (N=20000, sky-uniform, seed=44) ---
if [ -f "$RUN_DIR/STAGE_SAMPLE_DONE" ]; then
  log "stage sample: skip (marker present)"
elif [ -f "$HERE/scale20k_sample.parquet" ]; then
  log "stage sample: skip (scale20k_sample.parquet already present)"
  touch "$RUN_DIR/STAGE_SAMPLE_DONE"
else
  log "stage sample: running fetch_scale20k_sample.py"
  $PY "$HERE/fetch_scale20k_sample.py" >>"$LOG" 2>&1 || fail "sample"
  touch "$RUN_DIR/STAGE_SAMPLE_DONE"
fi

# --- Stage 2: inference (resumable forward-pass pairs, local MPS) ---
if [ -f "$RUN_DIR/STAGE_INFERENCE_DONE" ]; then
  log "stage inference: skip (marker present)"
else
  log "stage inference: running run_injection_scale20k.py (resumes from scale20k_pairs.parquet if present)"
  $PY "$HERE/run_injection_scale20k.py" >>"$LOG" 2>&1 || fail "inference"
  # Verify the full N=20000 target was actually reached (script can exit 0
  # having produced a partial parquet if a wave of failures burns down the
  # remaining rows to nothing left to attempt).
  N_DONE=$($PY -c "import pandas as pd; print(len(pd.read_parquet('$HERE/scale20k_pairs.parquet')))")
  log "stage inference: $N_DONE/20000 pairs on disk"
  if [ "$N_DONE" -lt 20000 ]; then
    fail "inference (only $N_DONE/20000 pairs — rerun script to resume remaining rows)"
  fi
  touch "$RUN_DIR/STAGE_INFERENCE_DONE"
fi

# --- Stage 3: analysis (f in {0,0.5,1,2,5}% x 10 seeds, bootstrap errors) ---
if [ -f "$RUN_DIR/STAGE_ANALYSIS_DONE" ]; then
  log "stage analysis: skip (marker present)"
else
  log "stage analysis: running analyze_injection_scale20k.py"
  $PY "$HERE/analyze_injection_scale20k.py" >>"$LOG" 2>&1 || fail "analysis"
  touch "$RUN_DIR/STAGE_ANALYSIS_DONE"
fi

# --- Stage 4: figure ---
if [ -f "$RUN_DIR/STAGE_FIGURE_DONE" ]; then
  log "stage figure: skip (marker present)"
else
  log "stage figure: running gen_fig_scale20k_injection.py"
  $PY "$HERE/gen_fig_scale20k_injection.py" >>"$LOG" 2>&1 || fail "figure"
  touch "$RUN_DIR/STAGE_FIGURE_DONE"
fi

log "=== row16 local run complete ==="
touch "$RUN_DIR/ROW16_DONE"
