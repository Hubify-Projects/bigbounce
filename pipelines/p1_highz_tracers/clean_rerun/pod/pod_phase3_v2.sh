#!/bin/bash
# AUG-011 phase 3 v2: SCIENCE-TARGET-ONLY rerun.
#
# Supersedes pod_phase3.sh's S>8 chain, which was found (2026-09-03,
# project-context/ANOMALY_SAMPLE_CONTAMINATION_2026-09-03.md) to be 84.8%
# sky fibers because it never joined to the zcatalog OBJTYPE/FIBERSTATUS
# columns. This script builds the sample with
# `build_flagship_sample.py --science-targets-only --zcatalog ...`,
# re-checks it with `gates/check_sample_provenance.py` (abort on FAIL), and
# only then runs the same enrichment -> SIMBAD/NED -> WISE -> taxonomy chain
# as pod_phase3.sh, entirely under its own /workspace/phase3_v2/ tree so it
# never touches the v1 (SAMPLE-V1-CONTAMINATED, already landed) outputs.
#
# Unattended + idempotent: every stage writes a marker file
# /workspace/phase3_v2/STAGE_<N>_<NAME>_DONE on success and is skipped on
# rerun if its marker already exists. Every stage transition is appended to
# /workspace/phase3_v2/phase3_v2.log as "== <UTC> <stage>" lines (same style
# as phase3.log). On any failure: /workspace/PHASE3_V2_FAILED is written
# with the failing stage name and the script exits non-zero. On full
# success: /workspace/PHASE3_V2_DONE is written.
#
# Threshold-choice rule (pre-declared, encoded here, never eyeballed):
#   From the grid {3,4,5,6,8,10} sigma, take the LARGEST threshold whose
#   science-only post-dedup count is >= 300. If that count exceeds 1,500,
#   step to the NEXT-LARGER grid point instead, unless doing so would drop
#   the count below 300 (in which case keep the >=300 pick). This is
#   implemented in choose_threshold.py below (deterministic, no manual
#   judgment call at run time) and the full rule text + counts + choice are
#   written into science_target_summary.json.

set -uo pipefail

cd /workspace
R=/workspace/bigbounce/pipelines/p1_highz_tracers
V2=/workspace/phase3_v2
LOG="$V2/phase3_v2.log"
FAILMARK=/workspace/PHASE3_V2_FAILED
DONEMARK=/workspace/PHASE3_V2_DONE

CONTRACT=/workspace/run-contract.json
SHARD_DIR=/workspace/shards
RECEIPT_DIR=/workspace/receipts
SUMMARY=/workspace/summary.json
ZCATALOG=/workspace/zall-pix-iron.fits

mkdir -p "$V2"

mark() { echo "== $(date -u +%FT%TZ) $1" | tee -a "$LOG"; }

fail() {
  local stage="$1"
  mark "FAILED at stage: $stage"
  echo "$stage" > "$FAILMARK"
  echo "$(date -u +%FT%TZ) $stage" >> "$FAILMARK"
  exit 1
}

marker_path() { echo "$V2/STAGE_$1_DONE"; }

stage_done() {
  [ -f "$(marker_path "$1")" ]
}

mark_stage_done() {
  touch "$(marker_path "$1")"
  mark "STAGE $1 DONE"
}

# ---------------------------------------------------------------------
# Stage 1: wait for / (re-)run the science-only --describe pass
# ---------------------------------------------------------------------
STAGE=01_DESCRIBE
if stage_done "$STAGE"; then
  mark "skip $STAGE (marker exists)"
else
  mark "start $STAGE: science-only describe pass"
  DESCRIBE_LOG="$V2/describe_science.log"

  # If a describe process is already running (launched before this script,
  # e.g. PID 79216 per PHASE3_V2_PROGRESS_2026-09-03.md), wait for it.
  EXISTING_PID="$(pgrep -f 'build_flagship_sample.py.*--describe.*--science-targets-only' | head -1 || true)"
  if [ -n "${EXISTING_PID:-}" ]; then
    mark "$STAGE: found running describe PID $EXISTING_PID, waiting"
    while kill -0 "$EXISTING_PID" 2>/dev/null; do
      sleep 30
    done
    mark "$STAGE: existing describe PID $EXISTING_PID exited"
  fi

  # If no usable output yet (describe writes to stdout only — capture it),
  # or the log is empty/missing, (re-)run it ourselves, foreground, output
  # captured to DESCRIBE_LOG.
  if [ ! -s "$DESCRIBE_LOG" ]; then
    mark "$STAGE: (re-)running describe pass to $DESCRIBE_LOG"
    python3 "$R/clean_rerun/build_flagship_sample.py" \
      --contract "$CONTRACT" --shard-dir "$SHARD_DIR" --receipt-dir "$RECEIPT_DIR" \
      --summary "$SUMMARY" --describe --science-targets-only --zcatalog "$ZCATALOG" \
      > "$DESCRIBE_LOG" 2>&1
    RC=$?
    if [ $RC -ne 0 ]; then
      tail -20 "$DESCRIBE_LOG" | tee -a "$LOG"
      fail "$STAGE"
    fi
  fi

  if ! grep -qiE 'traceback|error' "$DESCRIBE_LOG"; then
    python3 - "$DESCRIBE_LOG" "$V2/science_target_summary.json" <<'PYEOF'
import json, re, sys, datetime

describe_log, out_path = sys.argv[1], sys.argv[2]
text = open(describe_log).read()

payload = {
    "generated_utc": datetime.datetime.utcnow().isoformat() + "Z",
    "source_log": describe_log,
    "raw_describe_output": text,
}
with open(out_path, "w") as f:
    json.dump(payload, f, indent=2)
print(f"wrote {out_path}")
PYEOF
    RC=$?
    [ $RC -eq 0 ] || fail "$STAGE"
    mark_stage_done "$STAGE"
  else
    tail -20 "$DESCRIBE_LOG" | tee -a "$LOG"
    fail "$STAGE"
  fi
fi

# ---------------------------------------------------------------------
# Stage 2: sky-fraction-by-score diagnostic
# ---------------------------------------------------------------------
STAGE=02_SKY_FRACTION
if stage_done "$STAGE"; then
  mark "skip $STAGE (marker exists)"
else
  mark "start $STAGE: sky_fraction_by_score.py"
  python3 "$R/clean_rerun/sky_fraction_by_score.py" \
    --contract "$CONTRACT" --shard-dir "$SHARD_DIR" --receipt-dir "$RECEIPT_DIR" \
    --summary "$SUMMARY" --zcatalog "$ZCATALOG" \
    --output-json "$V2/sky_fraction_by_score.json" \
    --output-png "$V2/sky_fraction_by_score.png" 2>&1 | tail -20 | tee -a "$LOG"
  RC=${PIPESTATUS[0]}
  [ "$RC" -eq 0 ] && [ -s "$V2/sky_fraction_by_score.json" ] || fail "$STAGE"
  mark_stage_done "$STAGE"
fi

# ---------------------------------------------------------------------
# Stage 3: choose threshold by the pre-declared rule + build the sample
# ---------------------------------------------------------------------
STAGE=03_CHOOSE_THRESHOLD_AND_BUILD
CHOICE_JSON="$V2/threshold_choice.json"
if stage_done "$STAGE"; then
  mark "skip $STAGE (marker exists)"
else
  mark "start $STAGE: threshold choice + science-only sample build"

  # Get per-threshold science-only counts for the grid by running
  # build_flagship_sample.py --describe's structured counts. The --describe
  # pass already reports fractions/counts above 3/4/5/6/8/10 in its stdout;
  # parse science_target_summary.json's raw text for those counts.
  python3 - "$V2/science_target_summary.json" "$CHOICE_JSON" <<'PYEOF'
import json, re, sys

summary_path, out_path = sys.argv[1], sys.argv[2]
raw = json.load(open(summary_path))["raw_describe_output"]

GRID = [3, 4, 5, 6, 8, 10]
counts = {}
for g in GRID:
    # Accept a few common describe-output phrasings:
    #   ">= 8.0: 1234 (12.3%)" / "score>=8: 1234" / "threshold 8.0 -> count=1234"
    patterns = [
        rf">=\s*{g}\.0[^0-9]*?(\d[\d,]*)",
        rf">=\s*{g}[^0-9]*?(\d[\d,]*)",
        rf"threshold\s*{g}\.0.*?count[=:\s]+(\d[\d,]*)",
    ]
    n = None
    for p in patterns:
        m = re.search(p, raw, re.IGNORECASE)
        if m:
            n = int(m.group(1).replace(",", ""))
            break
    counts[str(g)] = n

rule_text = (
    "From grid {3,4,5,6,8,10}: take the LARGEST threshold whose science-only "
    "count is >= 300. If that count exceeds 1500, step to the NEXT-LARGER "
    "grid point unless that would drop the count below 300 (then keep the "
    ">=300 pick)."
)

# Apply the rule over the grid points we could parse counts for.
valid = [(g, c) for g, c in counts.items() if c is not None]
valid.sort(key=lambda gc: int(gc[0]))

candidates_ge_300 = [gc for gc in valid if gc[1] >= 300]
if not candidates_ge_300:
    chosen = None
    reason = "no grid point met the >=300 science-only floor; manual review required"
else:
    # Largest threshold with count >= 300 (largest g, since count decreases
    # with g in a typical anomaly-score distribution -> the "largest g that
    # still clears 300" is the last entry in candidates_ge_300 sorted by g).
    candidates_ge_300.sort(key=lambda gc: int(gc[0]))
    pick = candidates_ge_300[-1]
    if pick[1] > 1500:
        idx = [i for i, gc in enumerate(valid) if gc[0] == pick[0]][0]
        if idx + 1 < len(valid) and valid[idx + 1][1] >= 300:
            pick = valid[idx + 1]
    chosen = pick[0]
    reason = f"grid={counts}; picked g={pick[0]} count={pick[1]}"

result = {
    "rule": rule_text,
    "grid": GRID,
    "counts_by_threshold": counts,
    "chosen_threshold": chosen,
    "reason": reason,
}
json.dump(result, open(out_path, "w"), indent=2)
print(json.dumps(result, indent=2))
if chosen is None:
    sys.exit(2)
PYEOF
  RC=$?
  [ $RC -eq 0 ] || fail "$STAGE"

  CHOSEN="$(python3 -c "import json; print(json.load(open('$CHOICE_JSON'))['chosen_threshold'])")"
  mark "$STAGE: chosen threshold = $CHOSEN"

  python3 "$R/clean_rerun/build_flagship_sample.py" \
    --contract "$CONTRACT" --shard-dir "$SHARD_DIR" --receipt-dir "$RECEIPT_DIR" \
    --summary "$SUMMARY" --science-targets-only --zcatalog "$ZCATALOG" \
    --score-threshold "$CHOSEN" \
    --output-sample "$V2/flagship_sample_v2.parquet" \
    --output-manifest "$V2/flagship_sample_v2_manifest.json" 2>&1 | tail -10 | tee -a "$LOG"
  RC=${PIPESTATUS[0]}
  [ "$RC" -eq 0 ] && [ -s "$V2/flagship_sample_v2.parquet" ] || fail "$STAGE"

  mark "$STAGE: provenance gate"
  python3 "$R/clean_rerun/gates/check_sample_provenance.py" --sample "$V2/flagship_sample_v2.parquet" 2>&1 | tee -a "$LOG"
  RC=${PIPESTATUS[0]}
  [ "$RC" -eq 0 ] || fail "$STAGE (provenance gate FAIL)"

  mark_stage_done "$STAGE"
fi

CHOSEN="$(python3 -c "import json; print(json.load(open('$CHOICE_JSON'))['chosen_threshold'])" 2>/dev/null || true)"

# ---------------------------------------------------------------------
# Stage 4: enrichment
# ---------------------------------------------------------------------
STAGE=04_ENRICH
if stage_done "$STAGE"; then
  mark "skip $STAGE (marker exists)"
else
  mark "start $STAGE: enrich_flagship_sample.py"
  python3 "$R/clean_rerun/enrich_flagship_sample.py" \
    --sample "$V2/flagship_sample_v2.parquet" \
    --sample-manifest "$V2/flagship_sample_v2_manifest.json" \
    --contract "$CONTRACT" \
    --model /workspace/bigbounce/best_model_47k.pt \
    --zcatalog "$ZCATALOG" \
    --coadd-cache-dir "$V2/enrich_cache" \
    --shard-dir "$V2/enrich_shards" \
    --checkpoint "$V2/enrich_checkpoint.json" \
    --audit-log "$V2/enrich_audit.jsonl" \
    --output "$V2/flagship_sample_v2_enriched.parquet" \
    --manifest-output "$V2/flagship_enriched_v2_manifest.json" 2>&1 | tail -20 | tee -a "$LOG"
  RC=${PIPESTATUS[0]}
  [ "$RC" -eq 0 ] && [ -s "$V2/flagship_sample_v2_enriched.parquet" ] || fail "$STAGE"
  mark_stage_done "$STAGE"
fi

# ---------------------------------------------------------------------
# Stage 5: SIMBAD/NED crossmatch
# ---------------------------------------------------------------------
STAGE=05_CROSSMATCH
if stage_done "$STAGE"; then
  mark "skip $STAGE (marker exists)"
else
  mark "start $STAGE: crossmatch_flagship.py"
  python3 "$R/clean_rerun/crossmatch_flagship.py" \
    --input-sample "$V2/flagship_sample_v2.parquet" \
    --input-manifest "$V2/flagship_sample_v2_manifest.json" \
    --zcatalog "$ZCATALOG" \
    --checkpoint-dir "$V2/crossmatch_ckpt" \
    --output-matched "$V2/flagship_crossmatch_v2_matched.parquet" \
    --output-unmatched "$V2/flagship_crossmatch_v2_unmatched.parquet" \
    --output-manifest "$V2/flagship_crossmatch_v2_manifest.json" 2>&1 | tail -20 | tee -a "$LOG"
  RC=${PIPESTATUS[0]}
  [ "$RC" -eq 0 ] && [ -s "$V2/flagship_crossmatch_v2_manifest.json" ] || fail "$STAGE"
  mark_stage_done "$STAGE"
fi

# ---------------------------------------------------------------------
# Stage 6: WISE photometry join
# ---------------------------------------------------------------------
STAGE=06_WISE
if stage_done "$STAGE"; then
  mark "skip $STAGE (marker exists)"
else
  mark "start $STAGE: wise_join_flagship.py"
  python3 "$R/clean_rerun/wise_join_flagship.py" \
    --input-enriched "$V2/flagship_sample_v2_enriched.parquet" \
    --input-enriched-manifest "$V2/flagship_enriched_v2_manifest.json" \
    --checkpoint "$V2/wise_checkpoint.json" \
    --output "$V2/flagship_wise_v2.parquet" \
    --output-manifest "$V2/flagship_wise_v2_manifest.json" 2>&1 | tail -20 | tee -a "$LOG"
  RC=${PIPESTATUS[0]}
  [ "$RC" -eq 0 ] && [ -s "$V2/flagship_wise_v2.parquet" ] || fail "$STAGE"
  mark_stage_done "$STAGE"
fi

# ---------------------------------------------------------------------
# Stage 7: taxonomy
# ---------------------------------------------------------------------
STAGE=07_TAXONOMY
if stage_done "$STAGE"; then
  mark "skip $STAGE (marker exists)"
else
  mark "start $STAGE: taxonomy_flagship.py"
  python3 "$R/clean_rerun/taxonomy_flagship.py" \
    --input-unmatched "$V2/flagship_crossmatch_v2_unmatched.parquet" \
    --input-crossmatch-manifest "$V2/flagship_crossmatch_v2_manifest.json" \
    --output-results "$V2/flagship_taxonomy_v2.json" \
    --output-manifest "$V2/flagship_taxonomy_v2_manifest.json" 2>&1 | tail -20 | tee -a "$LOG"
  RC=${PIPESTATUS[0]}
  [ "$RC" -eq 0 ] && [ -s "$V2/flagship_taxonomy_v2.json" ] || fail "$STAGE"
  mark_stage_done "$STAGE"
fi

# ---------------------------------------------------------------------
# Stage 8: pack enrich shards into tar parts (<= 9000 files each) + SHA manifest
# ---------------------------------------------------------------------
STAGE=08_PACK_SHARDS
if stage_done "$STAGE"; then
  mark "skip $STAGE (marker exists)"
else
  mark "start $STAGE: pack enrich shards"
  PACK_DIR="$V2/packed"
  mkdir -p "$PACK_DIR"
  python3 - "$V2/enrich_shards" "$PACK_DIR" <<'PYEOF'
import hashlib, json, os, sys, tarfile

shard_dir, pack_dir = sys.argv[1], sys.argv[2]
os.makedirs(pack_dir, exist_ok=True)

files = sorted(
    os.path.join(dp, f)
    for dp, _, fs in os.walk(shard_dir)
    for f in fs
)

CHUNK = 9000
parts = [files[i:i + CHUNK] for i in range(0, len(files), CHUNK)] or [[]]

sha_manifest = {}
for idx, chunk in enumerate(parts, start=1):
    part_path = os.path.join(pack_dir, f"enrich_shards_part{idx:03d}.tar")
    with tarfile.open(part_path, "w") as tf:
        for fpath in chunk:
            arcname = os.path.relpath(fpath, shard_dir)
            tf.add(fpath, arcname=arcname)
    with open(part_path, "rb") as fh:
        h = hashlib.sha256()
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    sha_manifest[os.path.basename(part_path)] = {
        "sha256": h.hexdigest(),
        "n_files": len(chunk),
    }

out = os.path.join(pack_dir, "PACKED_SHA256SUMS.json")
json.dump(sha_manifest, open(out, "w"), indent=2)
print(f"packed {len(files)} files into {len(parts)} part(s); manifest={out}")
PYEOF
  RC=$?
  [ $RC -eq 0 ] || fail "$STAGE"
  mark_stage_done "$STAGE"
fi

mark "PHASE3-V2-DONE"
touch "$DONEMARK"
exit 0
