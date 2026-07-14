#!/usr/bin/env bash
# int_wave_apjs.sh — the P3 ApJS-framed INT wave (directive M, 2026-07-12).
#
# P3's REJECTs on the PRD variant are PROVEN venue-class (three independent
# referees converged on "catalog paper, wrong venue"; the ApJS-framed Gemini INT
# returned MINOR REVISIONS "strongly supported ... perfectly aligns with the ApJS
# mandate" — submissions/P3_VENUE_DECISION.md). The honest directive-M lever for
# P3 is the venue: an ApJS-framed review IS a legitimate review of the same
# science at the right journal. This wraps the same int_api_review engine as
# tools/int_wave.sh but:
#   * reviews the ApJS variant PDF (P3APJS -> pipelines/p3_anomaly_engine/paper3_apjs.pdf)
#   * with the ApJS referee prompt (INT_VENUE / INT_PROMPT / INT_SYSTEM)
#   * writes raws to a clearly-labeled sibling dir (INT_OUTDIR .../INT_apjs/<date>)
#     so the PRD round dir is never clobbered.
# Three INT legs run: Grok API, Gemini API, and a read-only Codex CLI leg
# authenticated through the local ChatGPT subscription. OpenAI API review
# dispatch is forbidden. Prints the verdict matrix + appends a run.log line.
#
# Usage: tools/int_wave_apjs.sh ["optional context-note"]
set -uo pipefail

REPO="/Users/houstongolden/Desktop/CODE_YOU/bigbounce"
PY_REVIEW="${BIGBOUNCE_INT_API_REVIEW_BIN:-$REPO/tools/int_api_review_2026-07-08.py}"
PAPER="P3APJS"
API_PAPER="P3"
TEX_REL="pipelines/p3_anomaly_engine/paper3_apjs.tex"
PDF_REL="pipelines/p3_anomaly_engine/paper3_apjs.pdf"
DATESTAMP="$(date +%Y-%m-%d)"
export INT_OUTDIR="${INT_OUTDIR:-$REPO/project-context/peer-reviews/INT_apjs/$DATESTAMP}"
RUNLOG="$INT_OUTDIR/run.log"
CODEX_ENABLED="${BIGBOUNCE_CODEX_SUBSCRIPTION_ENABLED:-1}"
CODEX_BIN="${BIGBOUNCE_CODEX_BIN:-$(command -v codex 2>/dev/null || { [ -x /opt/homebrew/bin/codex ] && printf '%s' /opt/homebrew/bin/codex; })}"
CODEX_MODEL="${BIGBOUNCE_CODEX_MODEL:-gpt-5.6-sol}"
CODEX_EFFORT="${BIGBOUNCE_CODEX_EFFORT:-high}"
API_LEGS_ENABLED="${BIGBOUNCE_INT_API_LEGS_ENABLED:-1}"

# ApJS referee framing (same wording as the ApJS Gemini leg that returned MINOR).
export INT_VENUE="${INT_VENUE:-The Astrophysical Journal Supplement Series (ApJS)}"
export INT_SYSTEM="${INT_SYSTEM:-You are an independent expert referee for The Astrophysical Journal Supplement Series (ApJS).}"
export INT_PROMPT="${INT_PROMPT:-You are an independent expert referee for The Astrophysical Journal Supplement Series (ApJS). Assess scientific correctness, reproducibility, data-product completeness, and journal suitability independently; do not presume that the manuscript fits the venue or that its central claim is supported. Review to the standard of a real ApJS submission. Respond with exactly: (1) VERDICT: ACCEPT / MINOR REVISIONS / MAJOR REVISIONS / REJECT. (2) ISSUES: numbered, each prefixed [MAJOR] or [MINOR], naming the specific section/claim and concrete problem. (3) One sentence: is the central claim (the released multi-survey anomaly catalog) supported and appropriate for ApJS?}"

cd "$REPO"
HHMM="$(date +%H%M%S)"
CODEX_OUT="$INT_OUTDIR/API_P3APJS_codex_${HHMM}.md"
CODEX_CLI_LOG="$INT_OUTDIR/.intwave_P3apjs_codex_${HHMM}.log"

live_version() {
  python3 - "$REPO/$TEX_REL" <<'PY'
import re, sys
txt = open(sys.argv[1]).read()
for pattern in (
    r"\\newcommand\{\\paperVersion\}\{([^}]+)\}",
    r"\\date\{[^}]*\}\s*%\s*(v[\w.\-]+)",
    r"^%\s*(v[\w.\-]+)\s*\(",
):
    match = re.search(pattern, txt, re.MULTILINE)
    if match:
        print(match.group(1))
        break
else:
    raise SystemExit("cannot determine P3 ApJS paper version")
PY
}
VER="$(live_version)"

REVIEW_COMMIT="${BIGBOUNCE_REVIEW_COMMIT:-worktree}"
EXPECTED_PDF_SHA256="${BIGBOUNCE_EXPECTED_PDF_SHA256:-}"
PDF_SHA256="$(shasum -a 256 "$REPO/$PDF_REL" | awk '{print $1}')"
TEX_SHA256="$(shasum -a 256 "$REPO/$TEX_REL" | awk '{print $1}')"
if [ -n "$EXPECTED_PDF_SHA256" ] && [ "$PDF_SHA256" != "$EXPECTED_PDF_SHA256" ]; then
  echo "FAIL: worktree PDF SHA-256 mismatch: expected $EXPECTED_PDF_SHA256 got $PDF_SHA256" >&2
  exit 1
fi
if [ "$REVIEW_COMMIT" != "worktree" ]; then
  COMMIT_PDF_SHA256="$(git show "$REVIEW_COMMIT:$PDF_REL" | shasum -a 256 | awk '{print $1}')" || exit 1
  COMMIT_TEX_SHA256="$(git show "$REVIEW_COMMIT:$TEX_REL" | shasum -a 256 | awk '{print $1}')" || exit 1
  if [ "$COMMIT_PDF_SHA256" != "$PDF_SHA256" ] || [ "$COMMIT_TEX_SHA256" != "$TEX_SHA256" ]; then
    echo "FAIL: worktree P3 ApJS PDF/source do not match commit $REVIEW_COMMIT" >&2
    exit 1
  fi
fi
export INT_REVIEW_COMMIT="$REVIEW_COMMIT"
export INT_EXPECTED_PDF_SHA256="$PDF_SHA256"

echo "=== int_wave_apjs :: P3 ApJS review-of-record ($VER) ==="
[ $# -ge 1 ] && echo "    context-note: $1"
echo "    tex:      $TEX_REL"
echo "    venue:    $INT_VENUE"
echo "    outdir:   ${INT_OUTDIR#$REPO/}"
echo "    codex:    ${CODEX_OUT#$REPO/}"
echo "    commit:   $REVIEW_COMMIT"
echo "    pdf-sha:  $PDF_SHA256"
echo "    tex-sha:  $TEX_SHA256"

CODEX_PROMPT="$INT_PROMPT

You are reviewing the manuscript source at $TEX_REL (version $VER) in this repository. This is a strictly READ-ONLY review: do not edit files, write state, use a browser, commit, push, or expose credentials. Never inspect .env.local or other secret-bearing files. Read the FULL .tex file (and non-secret figures/source/data you need to verify claims — you have the full repo). Do NOT fabricate: verify every number you check against committed artifacts (recompute read-only, don't just read). Prefix your reply with '(1) VERDICT: ...' exactly."
[ $# -ge 1 ] && CODEX_PROMPT="$CODEX_PROMPT

CONTEXT NOTE: $1"

case "$CODEX_ENABLED" in 0|1) ;; *) echo "FAIL: BIGBOUNCE_CODEX_SUBSCRIPTION_ENABLED must be 0 or 1" >&2; exit 1 ;; esac
case "$API_LEGS_ENABLED" in 0|1) ;; *) echo "FAIL: BIGBOUNCE_INT_API_LEGS_ENABLED must be 0 or 1" >&2; exit 1 ;; esac
case "$CODEX_EFFORT" in minimal|low|medium|high|xhigh|max|ultra) ;; *) echo "FAIL: BIGBOUNCE_CODEX_EFFORT must be minimal|low|medium|high|xhigh|max|ultra" >&2; exit 1 ;; esac

# No-launch validation path: no directories, API calls, or agent sessions.
if [ "${BIGBOUNCE_INT_WAVE_DRY_RUN:-0}" = "1" ]; then
  LOGIN="unavailable"
  if [ -n "$CODEX_BIN" ]; then LOGIN="$(env -u OPENAI_API_KEY -u CODEX_API_KEY -u ANTHROPIC_API_KEY "$CODEX_BIN" login status 2>&1 || true)"; fi
  printf 'DRY_RUN paper=P3APJS version=%s codex_enabled=%s model=%s effort=%s sandbox=read-only auth=%s\n' \
    "$VER" "$CODEX_ENABLED" "$CODEX_MODEL" "$CODEX_EFFORT" "$LOGIN"
  exit 0
fi

mkdir -p "$INT_OUTDIR"

# ---- API legs (grok, gemini) in parallel ----
PIDS_API=""
if [ "$API_LEGS_ENABLED" = 1 ]; then
  for vend in grok gemini; do
    ( set -a; source "$REPO/.env.local"; set +a; python3 "$PY_REVIEW" "$API_PAPER" "$vend" ) \
      >"$INT_OUTDIR/.intwave_P3apjs_${vend}_${HHMM}.log" 2>&1 &
  done
  PIDS_API="$(jobs -p)"
else
  echo "    API legs disabled for this invocation; preserving existing raws"
fi

# ---- Codex ChatGPT-subscription leg (fixed read-only sandbox) ----
CODEX_ON=0
CODEX_STATE="DISABLED"
if [ "$CODEX_ENABLED" = 1 ] && [ -n "$CODEX_BIN" ]; then
  CODEX_LOGIN="$(env -u OPENAI_API_KEY -u CODEX_API_KEY -u ANTHROPIC_API_KEY "$CODEX_BIN" login status 2>&1 || true)"
  if printf '%s' "$CODEX_LOGIN" | grep -q 'Logged in using ChatGPT'; then
    CODEX_ON=1
    CODEX_STATE="ENABLED"
  else
    CODEX_STATE="AUTH-UNAVAILABLE"
  fi
elif [ "$CODEX_ENABLED" = 1 ]; then
  CODEX_STATE="CLI-UNAVAILABLE"
fi

if [ "$CODEX_ON" = 1 ]; then
(
  {
    echo "# INT Codex-subscription Review (ApJS-framed) — P3APJS $VER — $CODEX_MODEL ($CODEX_EFFORT)"
    echo "paper: P3APJS  version: $VER  tex: $TEX_REL"
    echo "venue-framing: The Astrophysical Journal Supplement Series (ApJS)"
    echo "modality: full-repo Codex CLI ChatGPT-subscription referee (read-only, ephemeral)"
    echo "provenance: commit=$REVIEW_COMMIT  pdf=$PDF_REL  sha256=$PDF_SHA256"
    echo "source: $TEX_REL  sha256=$TEX_SHA256"
    echo "UTC: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo ""
    echo "======================================================================"
    echo "RAW RESPONSE (verbatim):"
    echo "======================================================================"
    echo ""
    RAW_TMP="$(mktemp "${TMPDIR:-/tmp}/bigbounce-codex-apjs-review.XXXXXX")"
    if printf '%s\n' "$CODEX_PROMPT" | env -u OPENAI_API_KEY -u CODEX_API_KEY -u ANTHROPIC_API_KEY \
      "$CODEX_BIN" --cd "$REPO" --sandbox read-only --ask-for-approval never \
        --model "$CODEX_MODEL" -c "model_reasoning_effort=\"$CODEX_EFFORT\"" \
        exec --ephemeral --ignore-user-config \
        --color never --output-last-message "$RAW_TMP" - \
        >"$CODEX_CLI_LOG" 2>&1; then
      cat "$RAW_TMP"
    else
      echo "(Codex subscription leg errored; diagnostics: ${CODEX_CLI_LOG#$REPO/})"
      cat "$RAW_TMP" 2>/dev/null || true
      rm -f "$RAW_TMP"
      exit 1
    fi
    rm -f "$RAW_TMP"
  } >"$CODEX_OUT"
) &
PID_CODEX=$!
fi

echo "    launched: grok+gemini (api) + openai-via-codex-subscription=${CODEX_STATE}${PID_CODEX:+(pid $PID_CODEX)} — blocking..."
for p in $PIDS_API; do wait "$p"; done
RC_CODEX=0
if [ "$CODEX_ON" = 1 ]; then wait "$PID_CODEX"; RC_CODEX=$?; fi

# ---- parse the matrix ----
parse_api() {
  local f="$INT_OUTDIR/API_${API_PAPER}_$1.md"
  [ -f "$f" ] && grep -m1 '^PARSED VERDICT:' "$f" | sed 's/^PARSED VERDICT:[[:space:]]*//' || true
}
V_GROK="$(parse_api grok)";     [ -n "$V_GROK" ]   || V_GROK="ABSENT"
V_GEMINI="$(parse_api gemini)"; [ -n "$V_GEMINI" ] || V_GEMINI="ABSENT"
V_CODEX="$(grep -m1 -iE 'VERDICT:' "$CODEX_OUT" 2>/dev/null | sed -E 's/.*VERDICT:[[:space:]]*//I' \
  | python3 -c 'import sys;s=sys.stdin.read().strip().strip("*").strip().upper()
for v in ("MAJOR REVISIONS","MINOR REVISIONS","ACCEPT","REJECT"):
    if v in s: print(v); break
else: print("ABSENT")')"
if [ "$CODEX_ON" = 1 ]; then
  [ -n "$V_CODEX" ] || V_CODEX="ABSENT"
else
  V_CODEX="$CODEX_STATE"
fi

TS_UTC="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo ""
echo "=== INT WAVE (ApJS) VERDICT MATRIX :: P3APJS $VER ==="
echo "  Grok (grok-4.3):           $V_GROK"
echo "  Gemini (gemini-3.1-pro):   $V_GEMINI"
echo "  OpenAI via Codex subscription ($CODEX_MODEL/$CODEX_EFFORT): $V_CODEX"
LOGLINE="$TS_UTC | P3APJS $VER (ApJS) | commit=$REVIEW_COMMIT | pdf_sha256=$PDF_SHA256 | grok=$V_GROK | gemini=$V_GEMINI | openai_subscription=$V_CODEX | codex_rc=$RC_CODEX"
[ "$CODEX_ON" = 1 ] && LOGLINE="$LOGLINE | codex_raw=${CODEX_OUT#$REPO/}"
echo "$LOGLINE" >>"$RUNLOG"
echo "  logged -> ${RUNLOG#$REPO/}"
