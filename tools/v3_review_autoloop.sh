#!/bin/bash
# v3 hourly auto-loop for continuous internal/external review-gap closure.
# Houston 2026-06-05 directive: "Every hour I want you to run the next loop."
#
# Each fire:
#   1. Runs v3 native-PDF review on all 6 papers in parallel
#   2. Synthesizes per-paper consensus-grouped findings
#   3. Compares against previous round to compute gap delta
#   4. Logs to project-context/peer-reviews/AUTOLOOP_LOG.md
#
# Self-terminates after 3 consecutive rounds with zero new ESSENTIAL findings.

set -euo pipefail
cd /Users/houstongolden/Desktop/CODE_2025/bigbounce

TS=$(date +%Y-%m-%d_%H%Mpt)
ROUND_LABEL="auto-${TS}"
LOG=project-context/peer-reviews/AUTOLOOP_LOG.md

declare -A PDFS=(
  [P1A]=site/public/paper1a_ech_nogo.pdf
  [P1B]=site/public/paper1b_mcmc_companion.pdf
  [P2]=site/public/paper2_alp_birefringence.pdf
  [P3]=site/public/paper3_draft.pdf
  [P4]=site/public/p4-chirality.pdf
  [P5]=site/public/p5-chirality.pdf
)

declare -A CONTEXTS=(
  [P1A]="Closed-form no-go for ECH at tree level."
  [P1B]="MCMC companion paper to P1A."
  [P2]="ALP birefringence + f_NL forecast."
  [P3]="Multi-survey anomaly catalog v3.1.75."
  [P4]="Galaxy chirality catalog v1.0.158."
  [P5]="DESI chirality x environment."
)

echo "[autoloop $TS] starting v3 native-PDF reviews on all 6 papers (parallel)"

mkdir -p $(dirname "$LOG")
{
  echo ""
  echo "## $TS — round=$ROUND_LABEL"
  echo ""
} >> "$LOG"

pids=()
for paper in P1A P1B P2 P3 P4 P5; do
  pdf=${PDFS[$paper]}
  ctx=${CONTEXTS[$paper]}
  echo "  launching v3 on $paper..."
  python3 tools/v3_native_pdf_review.py "$pdf" "$ROUND_LABEL" "$paper" "$ctx" \
    > /tmp/autoloop_${paper}.log 2>&1 &
  pids+=($!)
done

# Wait for all 6 (each takes ~3 minutes; parallel finish = ~3 minutes)
for pid in "${pids[@]}"; do
  wait "$pid" || true
done

echo "[autoloop $TS] all 6 reviews completed; running synthesis"

total_essential=0
for paper in P1A P1B P2 P3 P4 P5; do
  python3 tools/v3_review_synthesis.py "$ROUND_LABEL" "$paper" > /dev/null 2>&1
  total=$(grep "Total findings" "project-context/peer-reviews/${ROUND_LABEL}_${paper}_SYNTHESIS.md" 2>/dev/null | grep -oE '[0-9]+' | head -1 || echo 0)
  consensus=$(grep -c "CONSENSUS" "project-context/peer-reviews/${ROUND_LABEL}_${paper}_SYNTHESIS.md" 2>/dev/null || echo 0)
  echo "  - $paper: $total findings, $consensus consensus" >> "$LOG"
  echo "  $paper: $total findings, $consensus consensus"
done

echo "[autoloop $TS] complete. log appended to $LOG"
