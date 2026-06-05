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
cd /Users/houstongolden/Desktop/CODE_2025/bigbounce

TS=$(date +%Y-%m-%d_%H%Mpt)
ROUND_LABEL="auto-${TS}"
LOG=project-context/peer-reviews/AUTOLOOP_LOG.md

PAPERS="P1A P1B P2 P3 P4 P5"

get_pdf() {
  case "$1" in
    P1A) echo "site/public/paper1a_ech_nogo.pdf" ;;
    P1B) echo "site/public/paper1b_mcmc_companion.pdf" ;;
    P2)  echo "site/public/paper2_alp_birefringence.pdf" ;;
    P3)  echo "site/public/paper3_draft.pdf" ;;
    P4)  echo "site/public/p4-chirality.pdf" ;;
    P5)  echo "site/public/p5-chirality.pdf" ;;
  esac
}

get_ctx() {
  case "$1" in
    P1A) echo "Closed-form no-go for ECH at tree level." ;;
    P1B) echo "MCMC companion paper to P1A." ;;
    P2)  echo "ALP birefringence + f_NL forecast." ;;
    P3)  echo "Multi-survey anomaly catalog v3.1.75." ;;
    P4)  echo "Galaxy chirality catalog v1.0.159." ;;
    P5)  echo "DESI chirality x environment." ;;
  esac
}

echo "[autoloop $TS] starting v3 native-PDF reviews on all 6 papers (parallel)"

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

echo "[autoloop $TS] all 6 v3.1 reviews completed; running meta-reviewer"

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
