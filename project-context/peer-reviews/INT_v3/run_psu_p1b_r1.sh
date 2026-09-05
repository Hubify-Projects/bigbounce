#!/usr/bin/env bash
# One-shot mint+dispatch-in-same-line runner for PSU + P1B R1 API legs
# (Grok_brutal, Gemini_cosmology), retrying up to 6x on the
# "portfolio receipt is stale" preflight race with a 20s wait between tries.
set -uo pipefail
REPO="/Users/houstongolden/Desktop/CODE_YOU/bigbounce"
cd "$REPO"
set -a; source .env.local; set +a
unset ANTHROPIC_API_KEY OPENAI_API_KEY CODEX_API_KEY 2>/dev/null || true

run_paper() {
  local pdf="$1" round_label="$2" paper_tag="$3" round_dir="$4" ctx="$5"
  local receipt="$round_dir/preflight_receipt.json"
  local log="$round_dir/api_legs_run.log"
  local pidfile="$round_dir/api_legs_run.pid"
  mkdir -p "$round_dir"
  : > "$log"
  local attempt=1
  local rc=1
  while [ "$attempt" -le 6 ]; do
    {
      echo "=== [$paper_tag] attempt $attempt: mint && dispatch (same shell line) ==="
    } >> "$log"
    ( BIGBOUNCE_PREFLIGHT_RECEIPT="$receipt" V3_REVIEWERS="Grok_brutal,Gemini_cosmology" bash -c '
        python3 tools/bigbounce_preflight.py run --project-root "'"$REPO"'" --receipt "'"$receipt"'" \
        && python3 tools/v3_native_pdf_review.py "'"$pdf"'" "'"$round_label"'" "'"$paper_tag"'" "'"$ctx"'"
      ' ) >> "$log" 2>&1 &
    local pid=$!
    echo "$pid" > "$pidfile"
    wait "$pid"
    rc=$?
    if [ "$rc" -eq 0 ]; then
      echo "=== [$paper_tag] attempt $attempt SUCCEEDED (rc=0) ===" >> "$log"
      return 0
    fi
    if grep -q "portfolio receipt is stale" "$log"; then
      echo "=== [$paper_tag] attempt $attempt: stale receipt race, retrying in 20s ===" >> "$log"
      attempt=$((attempt+1))
      sleep 20
      continue
    else
      echo "=== [$paper_tag] attempt $attempt FAILED rc=$rc (non-stale error) ===" >> "$log"
      return "$rc"
    fi
  done
  echo "=== [$paper_tag] exhausted 6 attempts, still stale ===" >> "$log"
  return 1
}

run_paper \
  "$REPO/arxiv/paper1b_namaster_proof.pdf" \
  "ROUND_2026-09-04-P1B-v2B.0.17-EXACTPDF-0d0c92ab-R1" \
  "P1B" \
  "$REPO/project-context/peer-reviews/INT_v3/ROUND_2026-09-04-P1B-v2B.0.17-EXACTPDF-0d0c92ab-R1" \
  "Methods/software companion; R1 exact-PDF API legs (Grok+Gemini)" &
P1B_PID=$!

wait "$P1B_PID"; P1B_RC=$?

echo "P1B_RC=$P1B_RC"
exit "$P1B_RC"
