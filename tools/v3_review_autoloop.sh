#!/bin/bash
# v3 hourly auto-loop for continuous internal/external review-gap closure.
# Houston 2026-06-05 directive: "Every hour I want you to run the next loop."
#
# Each fire:
#   1. Runs v3 native-PDF review on all 6 papers in parallel
#   2. Runs v3.2 meta-reviewer on each paper (gpt-5-pro 6th pass)
#   3. Synthesizes per-paper consensus-grouped findings
#   4. Logs to project-context/peer-reviews/AUTOLOOP_LOG.md
#
# Compatible with macOS bash 3.2 (no associative arrays).

set -eu

# Retired 2026-07-15: hourly portfolio-wide rereview is the incremental loop we
# are replacing.  It spent provider calls on unchanged artifacts, included a
# non-canonical seventh manuscript, and used stale mirror paths.  Reviews now
# launch only per changed canonical paper through int_wave.sh after the
# accumulated six-paper prevention gate passes.
echo "ERROR: v3_review_autoloop.sh is retired; use tools/int_wave.sh for one changed canonical paper after preflight" >&2
exit 2

cd /Users/houstongolden/Desktop/CODE_2025/bigbounce

TS=$(date +%Y-%m-%d_%H%Mpt)
ROUND_LABEL="auto-${TS}"
LOG=project-context/peer-reviews/AUTOLOOP_LOG.md

PAPERS="P1A P1B P2 P2ALP P3 P4 P5"

# Canonical paper-local PDF (single source of truth — the compile target).
get_src() {
  case "$1" in
    P1A)   echo "arxiv/paper1a_ech_nogo.pdf" ;;
    P1B)   echo "arxiv/paper1b_mcmc_companion.pdf" ;;
    P2)    echo "research/focused_paper_source_integration/02_full_draft.pdf" ;;
    P2ALP) echo "research/focused_paper_source_integration/paper2_alp_birefringence.pdf" ;;
    P3)    echo "pipelines/p3_anomaly_engine/paper3_draft.pdf" ;;
    P4)    echo "pipelines/p2_chirality/chirality_catalog_paper.pdf" ;;
    P5)    echo "pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf" ;;
  esac
}

# Loop-local mirror the reviewers actually receive (refreshed every fire).
get_pdf() {
  case "$1" in
    P1A)   echo "site/public/paper1a_ech_nogo.pdf" ;;
    P1B)   echo "site/public/paper1b_mcmc_companion.pdf" ;;
    P2)    echo "site/public/papers/paper2_fnl_forecast.pdf" ;;
    P2ALP) echo "site/public/paper2_alp_birefringence.pdf" ;;
    P3)    echo "site/public/paper3_draft.pdf" ;;
    P4)    echo "site/public/p4-chirality.pdf" ;;
    P5)    echo "site/public/p5-chirality.pdf" ;;
  esac
}

get_ctx() {
  case "$1" in
    P1A) echo "Closed-form no-go for ECH at tree level." ;;
    P1B) echo "MCMC companion paper to P1A." ;;
    P2)    echo "f_NL = -35/8 SPHEREx/MegaMapper forecast (02_full_draft; current version per SSOT)." ;;
    P2ALP) echo "Spectator-ALP birefringence side manuscript (paper2_alp_birefringence; tracked separately from P2)." ;;
    P3)  echo "Multi-survey anomaly catalog (current version per SSOT)." ;;
    P4)  echo "Galaxy chirality catalog (current version per SSOT)." ;;
    P5)  echo "DESI chirality x environment (current version per SSOT)." ;;
  esac
}

# Pre-flight: refresh every loop mirror from its canonical paper-local PDF and
# verify md5 equality. Root-cause fix for the 2026-06-09 wrong-PDF round
# (mirror staleness/collision class eliminated — the loop always reviews the
# current compile).
echo "[autoloop $TS] pre-flight mirror refresh + md5 verify"
for paper in $PAPERS; do
  src=$(get_src "$paper"); dst=$(get_pdf "$paper")
  if [ ! -f "$src" ]; then echo "  FATAL: missing canonical PDF $src for $paper"; exit 1; fi
  cp "$src" "$dst"
  m1=$(md5 -q "$src"); m2=$(md5 -q "$dst")
  if [ "$m1" != "$m2" ]; then echo "  FATAL: mirror verify failed for $paper"; exit 1; fi
  echo "  $paper: $(echo "$m1" | cut -c1-8) $(pdfinfo "$dst" | awk '/^Pages/{print $2}')pp OK"
done

echo "[autoloop $TS] starting v3 native-PDF reviews on all 7 papers (parallel)"

mkdir -p "$(dirname "$LOG")"
{
  echo ""
  echo "## $TS — round=$ROUND_LABEL"
  echo ""
} >> "$LOG"

pids=""
for paper in $PAPERS; do
  pdf=$(get_pdf "$paper")
  ctx=$(get_ctx "$paper")
  echo "  launching v3 on $paper..."
  python3 tools/v3_native_pdf_review.py "$pdf" "$ROUND_LABEL" "$paper" "$ctx" \
    > "/tmp/autoloop_${paper}.log" 2>&1 &
  pids="$pids $!"
done

# Wait for all 6
for pid in $pids; do
  wait "$pid" || true
done

echo "[autoloop $TS] all v3.1 reviews completed; running meta-reviewer"

# v3.2 meta-reviewer (parallel)
meta_pids=""
for paper in $PAPERS; do
  pdf=$(get_pdf "$paper")
  python3 tools/v3_meta_review.py "$pdf" "$ROUND_LABEL" "$paper" \
    > "/tmp/autoloop_meta_${paper}.log" 2>&1 &
  meta_pids="$meta_pids $!"
done
for pid in $meta_pids; do
  wait "$pid" || true
done

echo "[autoloop $TS] meta-reviews completed; running synthesis"

for paper in $PAPERS; do
  python3 tools/v3_review_synthesis.py "$ROUND_LABEL" "$paper" > /dev/null 2>&1 || true
  synth="project-context/peer-reviews/${ROUND_LABEL}_${paper}_SYNTHESIS.md"
  meta="project-context/peer-reviews/${ROUND_LABEL}_${paper}_META_REVIEW.md"
  total=$(grep "Total findings" "$synth" 2>/dev/null | grep -oE '[0-9]+' | head -1 || echo 0)
  consensus=$(grep -c "CONSENSUS" "$synth" 2>/dev/null || echo 0)
  meta_exists="no"
  [ -f "$meta" ] && meta_exists="yes ($(wc -c < "$meta") chars)"
  printf -- "  - %s: %s findings, %s consensus, meta=%s\n" "$paper" "$total" "$consensus" "$meta_exists" >> "$LOG"
  printf "  %s: %s findings, %s consensus, meta=%s\n" "$paper" "$total" "$consensus" "$meta_exists"
done

echo "[autoloop $TS] complete. log appended to $LOG"
