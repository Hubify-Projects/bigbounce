#!/bin/bash
# Row12 SSL pilot: self-supervised spectral model on 1M DESI DR1 science-
# target spectra, evaluated via the known-object recovery benchmark against
# the sealed v2 catalogue (1,244 objects). Modelled on
# pipelines/p1_highz_tracers/clean_rerun/pod/pod_phase3_v2.sh's stage-marker
# + idempotent + fail-closed pattern, extended with a mandatory self-stop
# (this script's LAST action stops its own pod) and a background watchdog
# started at launch as the absolute cost-runaway fallback.
#
# Unattended + idempotent: every stage writes /workspace/row12/STAGE_<N>_DONE
# on success and is skipped on rerun if the marker exists. On any failure:
# /workspace/ROW12_FAILED is written with the failing stage + the script
# exits non-zero (the caller reads the log, fixes, and relaunches -- the
# script resumes from markers). On full success: /workspace/ROW12_DONE.
#
# Required env vars (passed at launch, never hardcoded):
#   HF_TOKEN, RUNPOD_API_KEY, RUNPOD_POD_ID
# Optional: B2_APPLICATION_KEY_ID, B2_APPLICATION_KEY, B2_BUCKET (backup)

set -uo pipefail

R=/workspace/bigbounce/pipelines/p3_anomaly_engine/ssl_pilot
W=/workspace/row12
LOG="$W/row12.log"
FAILMARK=/workspace/ROW12_FAILED
DONEMARK=/workspace/ROW12_DONE

mkdir -p "$W" "$W/shards"

mark() { echo "== $(date -u +%FT%TZ) $1" | tee -a "$LOG"; }
fail() {
  mark "FAILED at stage: $1"
  { echo "$1"; echo "$(date -u +%FT%TZ) $1"; } > "$FAILMARK"
  exit 1
}
marker_path() { echo "$W/STAGE_$1_DONE"; }
stage_done() { [ -f "$(marker_path "$1")" ]; }
mark_stage_done() { touch "$(marker_path "$1")"; mark "STAGE $1 DONE"; }

cd /workspace/bigbounce || fail "00_REPO_MISSING"

# ---------------------------------------------------------------------
# Stage 01: stage 1M science-target coadd spectra (fresh stream, per
# PREFLIGHT_2026-09-04.md -- no raw-spectrum mirror exists to reuse)
# ---------------------------------------------------------------------
STAGE=01_STAGE_SPECTRA
if stage_done "$STAGE"; then
  mark "skip $STAGE"
else
  mark "start $STAGE"
  if [ ! -s "$W/locator_inventory.jsonl" ]; then
    curl -sf -H "Authorization: Bearer $HF_TOKEN" -L -o "$W/locator_inventory.jsonl" \
      "https://huggingface.co/datasets/bamfai/bigbounce-aug-011-clean-rerun/resolve/main/sealed_2026-08-05/locator_inventory.jsonl" \
      || fail "$STAGE (locator inventory pull)"
  fi
  python3 "$R/select_row12_groups.py" \
    --locator-inventory "$W/locator_inventory.jsonl" \
    --output "$W/row12_group_selection.json" 2>&1 | tee -a "$LOG"
  [ -s "$W/row12_group_selection.json" ] || fail "$STAGE (selection)"

  python3 "$R/stage_row12_flux.py" \
    --selection "$W/row12_group_selection.json" \
    --shard-dir "$W/shards" \
    --audit-log "$W/stage_audit.jsonl" 2>&1 | tee -a "$W/stage_spectra.log"
  RC=${PIPESTATUS[0]}
  N_SHARDS=$(ls "$W/shards"/*.parquet 2>/dev/null | wc -l | tr -d ' ')
  [ "$RC" -eq 0 ] && [ "$N_SHARDS" -gt 0 ] || fail "$STAGE (staging, rc=$RC, shards=$N_SHARDS)"
  mark_stage_done "$STAGE"
fi

# ---------------------------------------------------------------------
# Stage 02: provenance gate on the staged sample
# ---------------------------------------------------------------------
STAGE=02_PROVENANCE_GATE
if stage_done "$STAGE"; then
  mark "skip $STAGE"
else
  mark "start $STAGE"
  python3 "$R/gates/check_sample_provenance.py" --shard-glob "$W/shards/*.parquet" 2>&1 | tee -a "$LOG"
  RC=${PIPESTATUS[0]}
  [ "$RC" -eq 0 ] || fail "$STAGE (provenance gate FAIL -- abort per contract)"
  mark_stage_done "$STAGE"
fi

# ---------------------------------------------------------------------
# Stage 03: train the masked-spectrum transformer (hard 2h wall-clock cap)
# ---------------------------------------------------------------------
STAGE=03_TRAIN
if stage_done "$STAGE"; then
  mark "skip $STAGE"
else
  mark "start $STAGE (max 7200s)"
  timeout 7500 python3 "$R/train_ssl_model.py" \
    --shard-glob "$W/shards/*.parquet" \
    --output-checkpoint "$W/model.pt" \
    --config-output "$W/train_config.json" \
    --max-seconds 7200 2>&1 | tee -a "$W/train.log"
  RC=${PIPESTATUS[0]}
  [ "$RC" -eq 0 ] && [ -s "$W/model.pt" ] || fail "$STAGE (training, rc=$RC)"
  mark_stage_done "$STAGE"
fi

# ---------------------------------------------------------------------
# Stage 04: embed + score the 1M pilot + the 1,244 v2 objects
# ---------------------------------------------------------------------
STAGE=04_EMBED_SCORE
if stage_done "$STAGE"; then
  mark "skip $STAGE"
else
  mark "start $STAGE: fetch v2 flux"
  python3 "$R/fetch_v2_flux.py" \
    --v2-sample "$W/flagship_sample_v2.parquet" \
    --output "$W/v2_flux.parquet" \
    --audit-log "$W/v2_fetch_audit.jsonl" 2>&1 | tee -a "$W/v2_fetch.log"
  RC=${PIPESTATUS[0]}
  [ "$RC" -eq 0 ] && [ -s "$W/v2_flux.parquet" ] || fail "$STAGE (v2 flux fetch)"

  mark "$STAGE: embed + score"
  python3 "$R/embed_and_score.py" \
    --checkpoint "$W/model.pt" \
    --pilot-shard-glob "$W/shards/*.parquet" \
    --v2-flux "$W/v2_flux.parquet" \
    --output-pilot-scores "$W/pilot_scores_full.parquet" \
    --output-v2-scores "$W/v2_scores.parquet" 2>&1 | tee -a "$W/embed_score.log"
  RC=${PIPESTATUS[0]}
  [ "$RC" -eq 0 ] && [ -s "$W/pilot_scores_full.parquet" ] && [ -s "$W/v2_scores.parquet" ] || fail "$STAGE (embed/score)"

  python3 - "$W/pilot_scores_full.parquet" "$W/pilot_scores_slim.parquet" <<'PYEOF'
import sys, pyarrow.parquet as pq, pyarrow as pa
src, dst = sys.argv[1], sys.argv[2]
t = pq.read_table(src)
cols = [c for c in t.column_names if c != "ssl_embedding"]
pq.write_table(t.select(cols), dst)
print(f"slim: {t.num_rows} rows, cols={cols}")
PYEOF
  [ -s "$W/pilot_scores_slim.parquet" ] || fail "$STAGE (slim scores)"
  mark_stage_done "$STAGE"
fi

# ---------------------------------------------------------------------
# Stage 05: recovery benchmark vs the cached VizieR reference classes
# ---------------------------------------------------------------------
STAGE=05_RECOVERY_BENCHMARK
if stage_done "$STAGE"; then
  mark "skip $STAGE"
else
  mark "start $STAGE"
  python3 - "$W/pilot_scores_slim.parquet" "$W/row12_group_selection.json" \
    "$W/row12_footprint_locator_inventory.jsonl" "$W/catalogs_config.json" <<'PYEOF'
import json, sys
import pyarrow.parquet as pq
import numpy as np

scores_path, selection_path, footprint_out, config_out = sys.argv[1:5]

sel = json.load(open(selection_path))
with open(footprint_out, "w") as fh:
    for g in sel["groups"]:
        fh.write(json.dumps({"survey": g["survey"], "program": g["program"], "healpix": g["healpix"]}) + "\n")

t = pq.read_table(scores_path)
scores = np.asarray(t.column("ssl_anomaly_score").to_pylist())
parent_total = t.num_rows

GRID = [1, 2, 3, 4, 5]
counts = {g: int((scores > (scores.mean() + g * scores.std())).sum()) for g in GRID}
candidates = [(g, c) for g, c in counts.items() if c >= 30]
chosen_sigma, chosen_count = (candidates[0] if candidates else (GRID[0], counts[GRID[0]]))
threshold = float(scores.mean() + chosen_sigma * scores.std())

config = [{
    "name": "row12_ssl_pilot",
    "path": scores_path,
    "id_col": "targetid",
    "ra_col": "target_ra",
    "dec_col": "target_dec",
    "score_col": "ssl_anomaly_score",
    "z_col": None,
    "threshold": threshold,
    "parent_total": parent_total,
    "catalog_total_at_threshold": chosen_count,
    "catalog_total_note": (
        f"row12 SSL pilot: mean+{chosen_sigma}sigma of the masked-spectrum "
        f"transformer's reconstruction-MSE score over {parent_total} staged "
        f"science-target spectra (grid={counts}, first sigma with count>=30 chosen)."
    ),
    "is_partial_preview": True,
}]
json.dump(config, open(config_out, "w"), indent=2)
print(json.dumps({"threshold_sigma": chosen_sigma, "threshold": threshold, "counts_grid": counts}, indent=2))
PYEOF
  RC=$?
  [ "$RC" -eq 0 ] && [ -s "$W/catalogs_config.json" ] || fail "$STAGE (threshold/config build)"

  python3 "/workspace/bigbounce/pipelines/p1_highz_tracers/clean_rerun/benchmark_known_object_recovery.py" \
    --crossmatch \
    --catalogs-config "$W/catalogs_config.json" \
    --locator-inventory "$W/row12_footprint_locator_inventory.jsonl" \
    --reference-cache-dir "$W/recovery_refs" \
    --reference-manifest "$W/recovery_refs/reference_manifest.json" \
    --out-dir "$W" 2>&1 | tee -a "$W/recovery_benchmark.log"
  RC=${PIPESTATUS[0]}
  [ "$RC" -eq 0 ] && [ -s "$W/recovery_benchmark.json" ] || fail "$STAGE (recovery benchmark, rc=$RC)"
  mark_stage_done "$STAGE"
fi

# ---------------------------------------------------------------------
# Stage 06: backup-3plus (HF + B2 + local tar) with sha256 manifest
# ---------------------------------------------------------------------
STAGE=06_BACKUP
if stage_done "$STAGE"; then
  mark "skip $STAGE"
else
  mark "start $STAGE"
  PACK="$W/pack_2026-09-04"
  mkdir -p "$PACK"
  for f in model.pt train_config.json pilot_scores_full.parquet pilot_scores_slim.parquet \
           v2_scores.parquet recovery_benchmark.json recovery_benchmark.md \
           catalogs_config.json row12_group_selection.json stage_audit.jsonl \
           v2_fetch_audit.jsonl row12.log stage_spectra.log train.log embed_score.log \
           recovery_benchmark.log; do
    [ -f "$W/$f" ] && cp "$W/$f" "$PACK/$f"
  done
  tar -C "$W" -czf "$W/row12_pilot_2026-09-04.tar.gz" "$(basename "$PACK")"
  python3 - "$W/row12_pilot_2026-09-04.tar.gz" "$W/SHA256SUMS.txt" <<'PYEOF'
import hashlib, sys
path, out = sys.argv[1], sys.argv[2]
h = hashlib.sha256()
with open(path, "rb") as fh:
    for block in iter(lambda: fh.read(1 << 20), b""):
        h.update(block)
open(out, "w").write(f"{h.hexdigest()}  {path}\n")
print(h.hexdigest())
PYEOF
  [ -s "$W/SHA256SUMS.txt" ] || fail "$STAGE (sha256)"

  python3 -c "
from huggingface_hub import HfApi
api = HfApi(token='$HF_TOKEN')
api.upload_folder(folder_path='$PACK', repo_id='bamfai/bigbounce-aug-011-clean-rerun',
                   repo_type='dataset', path_in_repo='row12_ssl_pilot/2026-09-04')
api.upload_file(path_or_fileobj='$W/row12_pilot_2026-09-04.tar.gz', repo_id='bamfai/bigbounce-aug-011-clean-rerun',
                 repo_type='dataset', path_in_repo='row12_ssl_pilot/2026-09-04/row12_pilot_2026-09-04.tar.gz')
print('HF upload OK')
" 2>&1 | tee -a "$LOG"
  RC=${PIPESTATUS[0]}
  [ "$RC" -eq 0 ] || fail "$STAGE (HF upload)"

  if [ -n "${B2_APPLICATION_KEY_ID:-}" ] && [ -n "${B2_APPLICATION_KEY:-}" ]; then
    b2 account authorize "$B2_APPLICATION_KEY_ID" "$B2_APPLICATION_KEY" >>"$LOG" 2>&1
    b2 file upload "${B2_BUCKET:-bigbounce}" "$W/row12_pilot_2026-09-04.tar.gz" \
      "row12_ssl_pilot/2026-09-04/row12_pilot_2026-09-04.tar.gz" 2>&1 | tee -a "$LOG"
    RC=${PIPESTATUS[0]}
    [ "$RC" -eq 0 ] || fail "$STAGE (B2 upload)"
  else
    mark "$STAGE: B2 credentials absent, skipping B2 leg (2/3 backups only -- recorded, not silent)"
  fi
  mark_stage_done "$STAGE"
fi

mark "ROW12-DONE"
touch "$DONEMARK"

# ---------------------------------------------------------------------
# Stage 07: self-stop (absolute last action)
# ---------------------------------------------------------------------
mark "self-stop: podStop $RUNPOD_POD_ID"
# NOTE (2026-09-04 3rd attempt): Authorization:Bearer returns HTTP 403 on the
# current RunPod API; ?api_key= query param is the confirmed-working auth.
curl -sf -X POST "https://api.runpod.io/graphql?api_key=$RUNPOD_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"query\": \"mutation { podStop(input: {podId: \\\"$RUNPOD_POD_ID\\\"}) { id desiredStatus } }\"}" \
  2>&1 | tee -a "$LOG"

exit 0
