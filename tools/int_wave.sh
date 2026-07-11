#!/usr/bin/env bash
# int_wave.sh — run the INT legs (OpenAI API, Grok API, Claude subscription, and
# Gemini API when GEMINI_API_KEY is set) in parallel, block until all finish, then
# print the verdict matrix.
#
# Legs:
#   (a) OpenAI: native-PDF API via tools/int_api_review_2026-07-08.py <paper> openai
#   (b) Grok:   native-PDF API via tools/int_api_review_2026-07-08.py <paper> grok
#   (d) Gemini: native-PDF API via tools/int_api_review_2026-07-08.py <paper> gemini
#               (7th reviewer leg, keyed 2026-07-11 — only runs when GEMINI_API_KEY
#               is present in .env.local; skipped-as-ABSENT otherwise, never fails
#               the wave on a missing key).
#   (c) Claude subscription: `claude -p` with the canonical PRD-referee prompt,
#       run with ANTHROPIC_API_KEY UNSET (2026-07-10 lesson: a sourced
#       ANTHROPIC_API_KEY takes precedence over the claude.ai login and fails /
#       silently bills the API). Its raw output is SAVED (mandatory, per the
#       every-leg-saves-its-raw rule) to
#       INT_api/H17_2026-07-10/intwave_<paper>_claude_HHMM.md.
#
# At the end it prints the verdict triple parsed from:
#   - the two newest API_<paper>_{openai,grok}.md PARSED VERDICT lines in
#     INT_v3/ROUND_2026-07-09/
#   - the VERDICT line of the just-written claude file
# and appends a run.log line to INT_api/H17_2026-07-10/run.log.
#
# Usage: tools/int_wave.sh <P1U|P1A|P1B|P2|P3|P4|P5> ["optional context-note"]
#
# See canonical spec: ~/.claude/scistack/astrostack/bigbounce-r-round/SKILL.md §1 (INT).

set -uo pipefail   # NOT -e: individual legs may fail; we want the triple regardless.

REPO="/Users/houstongolden/Desktop/CODE_YOU/bigbounce"
PY_REVIEW="$REPO/tools/int_api_review_2026-07-08.py"
API_OUTDIR="$REPO/project-context/peer-reviews/INT_v3/ROUND_2026-07-09"
CLAUDE_OUTDIR="$REPO/project-context/peer-reviews/INT_api/H17_2026-07-10"
RUNLOG="$CLAUDE_OUTDIR/run.log"

# tex path per paper (same map as the python script + directive_g.sh).
tex_for_paper() {
  case "$1" in
    P1A) echo "arxiv/paper1a_ech_nogo.tex" ;;
    P1B) echo "arxiv/paper1b_mcmc_companion.tex" ;;
    P1U) echo "arxiv/paper1_unified.tex" ;;
    P2)  echo "research/focused_paper_source_integration/02_full_draft.tex" ;;
    P3)  echo "pipelines/p3_anomaly_engine/paper3_draft.tex" ;;
    P4)  echo "pipelines/p2_chirality/chirality_catalog_paper.tex" ;;
    P5)  echo "pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex" ;;
    *)   echo "" ;;
  esac
}

die() { echo "FAIL: $*" >&2; exit 1; }

[ $# -ge 1 ] || die "usage: tools/int_wave.sh <PAPER> [\"context-note\"]"
PAPER="$1"
CONTEXT="${2:-}"

TEX_REL="$(tex_for_paper "$PAPER")"
[ -n "$TEX_REL" ] || die "unknown paper key '$PAPER' (want P1A|P1B|P1U|P2|P3|P4|P5)"
TEX="$REPO/$TEX_REL"
[ -f "$TEX" ] || die "tex not found: $TEX"

mkdir -p "$CLAUDE_OUTDIR"
cd "$REPO"

HHMM="$(date +%H%M)"
CLAUDE_OUT="$CLAUDE_OUTDIR/intwave_${PAPER}_claude_${HHMM}.md"

# Live version label (same logic as the python script: paperVersion macro, else
# \date version comment, else changelog comment).
live_version() {
  python3 - "$TEX" <<'PY'
import re, sys
txt = open(sys.argv[1]).read()
for pat in (r"\\newcommand\{\\paperVersion\}\{([^}]+)\}",
            r"\\date\{[^}]*\}\s*%\s*(v[\w.\-]+)",
            r"^%\s*(v[\w.]+)\s*\("):
    m = re.search(pat, txt, re.M)
    if m:
        print(m.group(1)); break
else:
    print("unknown-version")
PY
}
VER="$(live_version)"

echo "=== int_wave :: $PAPER ($VER) ==="
[ -n "$CONTEXT" ] && echo "    context-note: $CONTEXT"
echo "    tex:    $TEX_REL"
echo "    claude: ${CLAUDE_OUT#$REPO/}"

# ---------------------------------------------------------------------------
# Canonical PRD-referee prompt for the Claude subscription leg (full-file
# referee format), plus the optional context-note. The Claude leg reads the
# full paper + source + context (never fabricate — verify against artifacts).
# ---------------------------------------------------------------------------
CLAUDE_PROMPT="You are an expert referee for Physical Review D reviewing the manuscript at $TEX_REL (version $VER) in this repository. Read the FULL .tex file (and any figures/source/data you need to verify claims — you have the full repo). Review to the standard of a real PRD submission. Do NOT fabricate: verify every number you check against the committed artifacts (recompute, don't just read).

Respond in EXACTLY this format:
(1) VERDICT: ACCEPT / MINOR REVISIONS / MAJOR REVISIONS / REJECT
(2) ISSUES: a numbered list, each item prefixed [MAJOR] or [MINOR], naming the specific section/claim with a file:line reference and the concrete problem.
(3) One sentence: is the central claim supported?"
if [ -n "$CONTEXT" ]; then
  CLAUDE_PROMPT="$CLAUDE_PROMPT

CONTEXT NOTE for this review: $CONTEXT"
fi

# ---------------------------------------------------------------------------
# Launch the three legs in parallel subshells; capture PIDs; wait on all.
# ---------------------------------------------------------------------------

# (a) OpenAI leg
(
  set -a; source "$REPO/.env.local"; set +a
  python3 "$PY_REVIEW" "$PAPER" openai
) >"$CLAUDE_OUTDIR/.intwave_${PAPER}_openai_${HHMM}.log" 2>&1 &
PID_OPENAI=$!

# (b) Grok leg
(
  set -a; source "$REPO/.env.local"; set +a
  python3 "$PY_REVIEW" "$PAPER" grok
) >"$CLAUDE_OUTDIR/.intwave_${PAPER}_grok_${HHMM}.log" 2>&1 &
PID_GROK=$!

# (d) Gemini leg — 7th reviewer, only when GEMINI_API_KEY is present (keyed
#     2026-07-11). We source .env.local in a subshell to test the key without
#     leaking it into this shell's env or any log line.
GEMINI_ON=0
if ( set -a; source "$REPO/.env.local" >/dev/null 2>&1; set +a; [ -n "${GEMINI_API_KEY:-}" ] ); then
  GEMINI_ON=1
  (
    set -a; source "$REPO/.env.local"; set +a
    python3 "$PY_REVIEW" "$PAPER" gemini
  ) >"$CLAUDE_OUTDIR/.intwave_${PAPER}_gemini_${HHMM}.log" 2>&1 &
  PID_GEMINI=$!
fi

# (c) Claude subscription leg — ANTHROPIC_API_KEY MUST be unset (never source
#     .env.local in this subshell). Save raw to the mandated path.
(
  unset ANTHROPIC_API_KEY
  {
    echo "# INT Claude-subscription Review — $PAPER $VER — claude-opus-4-8"
    echo "paper: $PAPER  version: $VER  tex: $TEX_REL"
    echo "modality: full-repo Claude Code subscription subagent (claude -p)"
    echo "UTC: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    [ -n "$CONTEXT" ] && echo "context-note: $CONTEXT"
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

if [ "$GEMINI_ON" = 1 ]; then
  echo "    launched: openai(pid $PID_OPENAI) grok(pid $PID_GROK) gemini(pid $PID_GEMINI) claude(pid $PID_CLAUDE) — blocking until all done..."
else
  echo "    launched: openai(pid $PID_OPENAI) grok(pid $PID_GROK) claude(pid $PID_CLAUDE) [gemini: no key] — blocking until all done..."
fi

wait "$PID_OPENAI"; RC_OPENAI=$?
wait "$PID_GROK";   RC_GROK=$?
wait "$PID_CLAUDE"; RC_CLAUDE=$?
RC_GEMINI=0
if [ "$GEMINI_ON" = 1 ]; then wait "$PID_GEMINI"; RC_GEMINI=$?; fi

# ---------------------------------------------------------------------------
# Parse the verdict triple.
# ---------------------------------------------------------------------------
parse_api_verdict() {
  # $1 = vendor (openai|grok). The python script writes/overwrites
  # API_<paper>_<vendor>.md with a "PARSED VERDICT:" line.
  local f="$API_OUTDIR/API_${PAPER}_$1.md"
  if [ -f "$f" ]; then
    grep -m1 '^PARSED VERDICT:' "$f" | sed 's/^PARSED VERDICT:[[:space:]]*//' || true
  fi
}

V_OPENAI="$(parse_api_verdict openai)"; [ -n "$V_OPENAI" ] || V_OPENAI="ABSENT"
V_GROK="$(parse_api_verdict grok)";     [ -n "$V_GROK" ]   || V_GROK="ABSENT"
if [ "$GEMINI_ON" = 1 ]; then
  V_GEMINI="$(parse_api_verdict gemini)"; [ -n "$V_GEMINI" ] || V_GEMINI="ABSENT"
else
  V_GEMINI="NO-KEY"
fi

# Claude verdict: pull the (1) VERDICT line from the just-written raw file, then
# normalize to a bare verdict token (strip markdown **, trailing punctuation, and
# any trailing prose after the verdict word).
V_CLAUDE_RAW="$(grep -m1 -iE 'VERDICT:' "$CLAUDE_OUT" 2>/dev/null \
  | sed -E 's/.*VERDICT:[[:space:]]*//I')"
V_CLAUDE="$(printf '%s' "$V_CLAUDE_RAW" | python3 -c '
import sys, re
s = sys.stdin.read().strip().strip("*").strip()
u = s.upper()
for v in ("MAJOR REVISIONS","MINOR REVISIONS","ACCEPT","REJECT"):
    if v in u:
        print(v); break
else:
    print(re.sub(r"[*_`]+"," ",s).strip() or "ABSENT")
')"
[ -n "$V_CLAUDE" ] || V_CLAUDE="ABSENT"

TS_UTC="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo ""
echo "=== INT WAVE VERDICT MATRIX :: $PAPER $VER ==="
echo "  OpenAI (gpt-5.5):          $V_OPENAI"
echo "  Grok (grok-4.3):           $V_GROK"
echo "  Gemini (gemini-3.1-pro):   $V_GEMINI"
echo "  Claude (opus-4-8):         $V_CLAUDE"
echo "  (rc: openai=$RC_OPENAI grok=$RC_GROK gemini=$RC_GEMINI claude=$RC_CLAUDE)"

# Append to run.log.
LOGLINE="$TS_UTC | $PAPER $VER | openai=$V_OPENAI | grok=$V_GROK | gemini=$V_GEMINI | claude=$V_CLAUDE | claude_raw=${CLAUDE_OUT#$REPO/}"
[ -n "$CONTEXT" ] && LOGLINE="$LOGLINE | ctx=\"$CONTEXT\""
echo "$LOGLINE" >>"$RUNLOG"
echo "  logged -> ${RUNLOG#$REPO/}"
