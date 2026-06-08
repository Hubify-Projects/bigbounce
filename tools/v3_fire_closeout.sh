#!/bin/bash
# v3 fire-closeout — unified post-fire analysis wrapper.
#
# Runs the full autoloop closeout pipeline:
#   1. content-diff (this fire vs previous)
#   2. closure-verification (against CLOSURE_LEDGER.json)
#   3. v2 persistence tracker (multi-round aggregation)
#   4. pattern-040 cross-section sweep across all 6 papers
#
# Usage:
#   bash tools/v3_fire_closeout.sh <new_round> [<prev_round>]
#
# Example:
#   bash tools/v3_fire_closeout.sh auto-2026-06-08_1620pt auto-2026-06-08_1520pt
#
# If <prev_round> is omitted, it's auto-detected as the second-most-recent
# auto-* round in the META_REVIEW files.

set -eu
cd /Users/houstongolden/Desktop/CODE_2025/bigbounce

NEW_ROUND="${1:-}"
PREV_ROUND="${2:-}"

if [ -z "$NEW_ROUND" ]; then
  echo "Usage: bash $0 <new_round> [<prev_round>]"
  exit 2
fi

if [ -z "$PREV_ROUND" ]; then
  # Auto-detect previous round (2nd most recent META_REVIEW round excluding new)
  PREV_ROUND=$(ls project-context/peer-reviews/auto-*_META_REVIEW.md 2>/dev/null \
    | sed -E 's|.*/(auto-[^_]+_[^_]+_)P.*|\1|' \
    | sort -u \
    | grep -v "${NEW_ROUND}_" \
    | tail -1 \
    | sed 's/_$//')
  echo "Auto-detected previous round: $PREV_ROUND"
fi

echo ""
echo "============================================================"
echo "# Fire closeout: $NEW_ROUND vs $PREV_ROUND"
echo "============================================================"

echo ""
echo "## STEP 1 — content-diff fire $PREV_ROUND -> fire $NEW_ROUND"
echo ""
python3 tools/v3_meta_content_diff.py "$PREV_ROUND" "$NEW_ROUND" 2>&1 | tee /tmp/closeout_step1.log | tail -50 || true
CONTENT_DIFF_EC=$(python3 tools/v3_meta_content_diff.py "$PREV_ROUND" "$NEW_ROUND" >/dev/null 2>&1; echo $?)

echo ""
echo "## STEP 2 — closure verification"
echo ""
python3 tools/v3_closure_verification.py 2>&1 | tee /tmp/closeout_step2.log | tail -50 || true
CLOSURE_EC=$(python3 tools/v3_closure_verification.py >/dev/null 2>&1; echo $?)

echo ""
echo "## STEP 3 — v2 persistence tracker (multi-round aggregation)"
echo ""
python3 tools/v3_persistence_tracker_v2.py 2>&1 | tee /tmp/closeout_step3.log | tail -30 || true
PERSIST_EC=$(python3 tools/v3_persistence_tracker_v2.py >/dev/null 2>&1; echo $?)

echo ""
echo "## STEP 4 — pattern-040 sweep across all 6 papers"
echo ""
bash tools/v3_pattern040_all_papers.sh 2>&1 | grep -E "^# |Flagged contradictions|OVERALL TOTAL" | head -20 || true

echo ""
echo "============================================================"
echo "# Fire closeout summary"
echo "============================================================"
echo "  new_round:               $NEW_ROUND"
echo "  prev_round:              $PREV_ROUND"
echo "  content-diff exit code:  $CONTENT_DIFF_EC (papers with NEW ESS)"
echo "  closure-verif exit code: $CLOSURE_EC (closures RE-FIRED)"
echo "  v2-tracker exit code:    $PERSIST_EC (NEW ESS content-clusters)"
echo ""
echo "Self-terminate criterion (cron rule 8): 3 consecutive fires with"
echo "  CONTENT_DIFF_EC = 0 (no papers with new ESS)"
echo "  AND CLOSURE_EC = 0 (no closures re-fired)"
echo ""
echo "Counter advance recommendation:"
if [ "$CONTENT_DIFF_EC" -eq 0 ] && [ "$CLOSURE_EC" -eq 0 ]; then
  echo "  ADVANCE counter (this fire is clean)"
else
  echo "  RESET / HOLD counter (this fire has NEW ESS or RE-FIRED closures)"
fi
