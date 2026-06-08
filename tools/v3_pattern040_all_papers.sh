#!/bin/bash
# Run v3_pattern040_cross_section_check.py on all 6 papers.
# Designed for pre-bump auditing as part of /paper-pre-review-check.
#
# Usage:
#   bash tools/v3_pattern040_all_papers.sh
#
# Exit code = total flagged across all papers.

set -u
cd /Users/houstongolden/Desktop/CODE_2025/bigbounce

declare -a TEX_FILES=(
  "arxiv/paper1a_ech_nogo.tex"
  "arxiv/paper1b_mcmc_companion.tex"
  "research/focused_paper_source_integration/paper2_alp_birefringence.tex"
  "pipelines/p3_anomaly_engine/paper3_draft.tex"
  "pipelines/p2_chirality/chirality_catalog_paper.tex"
  "pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex"
)

TOTAL=0
for tex in "${TEX_FILES[@]}"; do
  if [ ! -f "$tex" ]; then
    echo "SKIP: $tex not found"
    continue
  fi
  echo "============================================================"
  echo "# $tex"
  echo "============================================================"
  python3 tools/v3_pattern040_cross_section_check.py "$tex"
  EC=$?
  TOTAL=$((TOTAL + EC))
  echo ""
done

echo "============================================================"
echo "# OVERALL TOTAL: $TOTAL flagged cross-section contradictions"
echo "============================================================"
exit $TOTAL
