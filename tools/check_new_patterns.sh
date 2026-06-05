#!/bin/bash
# Run mechanical detection for patterns 037, 038, 039 on every bigbounce paper.
# 037: future-dated \date{} block
# 038: σ-mixing without per-juxtaposition qualifier
# 039: hardcoded Roman-numeral table reference

set -eu

PAPERS_ROOT=/Users/houstongolden/Desktop/CODE_2025/bigbounce

declare_papers() {
  echo "P1A:arxiv/paper1a_ech_nogo.tex"
  echo "P1B:arxiv/paper1b_mcmc_companion.tex"
  echo "P2:research/focused_paper_source_integration/02_full_draft.tex"
  echo "P3:pipelines/p3_anomaly_engine/paper3_draft.tex"
  echo "P4:pipelines/p2_chirality/chirality_catalog_paper.tex"
  echo "P5:pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex"
}

CUR_YEAR=$(date +%Y)
NEXT_YEAR=$((CUR_YEAR + 1))

declare_papers | while IFS=: read -r tag rel; do
  tex="$PAPERS_ROOT/$rel"
  if [ ! -f "$tex" ]; then
    echo "[$tag] .tex not found at $rel — skip"
    continue
  fi
  echo ""
  echo "=== $tag ($rel) ==="

  # Pattern 037: future date
  date_lines=$(grep -nE "\\\\date\{" "$tex" || true)
  for line in $date_lines; do
    if echo "$line" | grep -qE "20(2[7-9]|[3-9][0-9])\\\b"; then
      echo "  ⚠ p037 future-year date: $line"
    fi
  done
  # Also check \newcommand{\paperTimestamp}
  ts=$(grep -E "newcommand\{\\\\paperTimestamp\}" "$tex" | head -1 || true)
  if [ -n "$ts" ]; then
    if echo "$ts" | grep -qE "20(2[7-9]|[3-9][0-9])"; then
      echo "  ⚠ p037 future paperTimestamp: $ts"
    fi
  fi

  # Pattern 038: σ-mixing in table captions
  # Find all table* captions and check if they list multiple sigma symbols
  sigma_caps=$(awk '/\\caption\{/,/\}/' "$tex" | grep -c "sigma\|σ\|\\$\\\\sigma\|\\\\sigmaunit" || true)
  if [ "$sigma_caps" -gt 1 ]; then
    qual=$(grep -c "not directly comparable\|distinct null" "$tex" || true)
    if [ "$qual" -lt "$sigma_caps" ]; then
      echo "  ⚠ p038 σ in $sigma_caps captions but only $qual qualifier mentions"
    fi
  fi

  # Pattern 039: hardcoded Roman-numeral table reference in prose
  prose_ref=$(grep -nE "Table\s+I+V?I*\\\b" "$tex" | grep -v "\\\\ref" | head -5 || true)
  if [ -n "$prose_ref" ]; then
    echo "  ⚠ p039 hardcoded prose 'Table II/IV' reference(s):"
    echo "$prose_ref" | sed 's/^/    /'
  fi
done
