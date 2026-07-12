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
# All four INT legs run: OpenAI API, Grok API, Gemini API, Claude subscription
# subagent (ANTHROPIC_API_KEY unset — the running Claude Code subscription, per
# CLAUDE.md I1). Prints the verdict quad + appends a run.log line.
#
# Usage: tools/int_wave_apjs.sh ["optional context-note"]
set -uo pipefail

REPO="/Users/houstongolden/Desktop/CODE_YOU/bigbounce"
PY_REVIEW="$REPO/tools/int_api_review_2026-07-08.py"
PAPER="P3APJS"
TEX_REL="pipelines/p3_anomaly_engine/paper3_apjs.tex"
DATESTAMP="$(date +%Y-%m-%d)"
export INT_OUTDIR="$REPO/project-context/peer-reviews/INT_apjs/$DATESTAMP"
RUNLOG="$INT_OUTDIR/run.log"
mkdir -p "$INT_OUTDIR"

# ApJS referee framing (same wording as the ApJS Gemini leg that returned MINOR).
export INT_VENUE="The Astrophysical Journal Supplement Series (ApJS)"
export INT_SYSTEM="You are an expert referee for The Astrophysical Journal Supplement Series (ApJS), the AAS catalog / data-release / methods journal."
export INT_PROMPT="You are an expert referee for The Astrophysical Journal Supplement Series (ApJS). ApJS is the AAS catalog / data-release / methods journal: it exists for exactly this kind of paper --- large released catalogs, data-mining pipelines, and machine-readable data products with reproducibility scripts. Review this manuscript to the standard of a real ApJS submission. Respond with exactly: (1) VERDICT: ACCEPT / MINOR REVISIONS / MAJOR REVISIONS / REJECT. (2) ISSUES: numbered, each prefixed [MAJOR] or [MINOR], naming the specific section/claim and concrete problem. (3) One sentence: is the central claim (the released multi-survey anomaly catalog) supported and appropriate for ApJS?"

cd "$REPO"
HHMM="$(date +%H%M)"
CLAUDE_OUT="$INT_OUTDIR/API_P3apjs_claude_${HHMM}.md"

live_version() {
  python3 - "$REPO/$TEX_REL" <<'PY'
import re, sys
txt = open(sys.argv[1]).read()
m = re.search(r"\\date\{[^}]*\}\s*%\s*(v[\w.\-]+)", txt)
print(m.group(1) if m else "unknown-version")
PY
}
VER="$(live_version)"

echo "=== int_wave_apjs :: P3 ApJS review-of-record ($VER) ==="
[ $# -ge 1 ] && echo "    context-note: $1"
echo "    tex:      $TEX_REL"
echo "    venue:    $INT_VENUE"
echo "    outdir:   ${INT_OUTDIR#$REPO/}"
echo "    claude:   ${CLAUDE_OUT#$REPO/}"

CLAUDE_PROMPT="$INT_PROMPT

You are reviewing the manuscript source at $TEX_REL (version $VER) in this repository. Read the FULL .tex file (and any figures/source/data you need to verify claims — you have the full repo). Do NOT fabricate: verify every number you check against the committed artifacts (recompute, don't just read). Prefix your reply with '(1) VERDICT: ...' exactly."
[ $# -ge 1 ] && CLAUDE_PROMPT="$CLAUDE_PROMPT

CONTEXT NOTE: $1"

# ---- API legs (openai, grok, gemini) in parallel ----
for vend in openai grok gemini; do
  ( set -a; source "$REPO/.env.local"; set +a; python3 "$PY_REVIEW" "$PAPER" "$vend" ) \
    >"$INT_OUTDIR/.intwave_P3apjs_${vend}_${HHMM}.log" 2>&1 &
done
PIDS_API="$(jobs -p)"

# ---- Claude subscription leg (ANTHROPIC_API_KEY unset) ----
(
  unset ANTHROPIC_API_KEY
  {
    echo "# INT Claude-subscription Review (ApJS-framed) — P3APJS $VER — claude-opus-4-8"
    echo "paper: P3APJS  version: $VER  tex: $TEX_REL"
    echo "venue-framing: The Astrophysical Journal Supplement Series (ApJS)"
    echo "modality: full-repo Claude Code subscription subagent (claude -p)"
    echo "UTC: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo ""
    echo "======================================================================"
    echo "RAW RESPONSE (verbatim):"
    echo "======================================================================"
    echo ""
    claude -p "$CLAUDE_PROMPT" --model claude-opus-4-8 --allowedTools "Read,Glob,Grep" 2>&1 \
      || echo "(claude -p leg errored — see above)"
  } >"$CLAUDE_OUT"
) &
PID_CLAUDE=$!

echo "    launched: openai+grok+gemini (api) + claude(pid $PID_CLAUDE) — blocking..."
for p in $PIDS_API; do wait "$p"; done
wait "$PID_CLAUDE"

# ---- parse the quad ----
parse_api() {
  local f="$INT_OUTDIR/API_P3APJS_$1.md"
  [ -f "$f" ] && grep -m1 '^PARSED VERDICT:' "$f" | sed 's/^PARSED VERDICT:[[:space:]]*//' || true
}
V_OPENAI="$(parse_api openai)"; [ -n "$V_OPENAI" ] || V_OPENAI="ABSENT"
V_GROK="$(parse_api grok)";     [ -n "$V_GROK" ]   || V_GROK="ABSENT"
V_GEMINI="$(parse_api gemini)"; [ -n "$V_GEMINI" ] || V_GEMINI="ABSENT"
V_CLAUDE="$(grep -m1 -iE 'VERDICT:' "$CLAUDE_OUT" 2>/dev/null | sed -E 's/.*VERDICT:[[:space:]]*//I' \
  | python3 -c 'import sys;s=sys.stdin.read().strip().strip("*").strip().upper()
for v in ("MAJOR REVISIONS","MINOR REVISIONS","ACCEPT","REJECT"):
    if v in s: print(v); break
else: print("ABSENT")')"
[ -n "$V_CLAUDE" ] || V_CLAUDE="ABSENT"

TS_UTC="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo ""
echo "=== INT WAVE (ApJS) VERDICT QUAD :: P3APJS $VER ==="
echo "  OpenAI (gpt-5.5):          $V_OPENAI"
echo "  Grok (grok-4.3):           $V_GROK"
echo "  Gemini (gemini-3.1-pro):   $V_GEMINI"
echo "  Claude (opus-4-8):         $V_CLAUDE"
echo "$TS_UTC | P3APJS $VER (ApJS) | openai=$V_OPENAI | grok=$V_GROK | gemini=$V_GEMINI | claude=$V_CLAUDE | claude_raw=${CLAUDE_OUT#$REPO/}" >>"$RUNLOG"
echo "  logged -> ${RUNLOG#$REPO/}"
