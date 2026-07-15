#!/usr/bin/env bash
# int_wave.sh — run the INT legs (Grok API, Gemini API, and Codex subscription)
# Gemini API when GEMINI_API_KEY is set) in parallel, block until all finish, then
# print the verdict matrix.
#
# Legs:
#   (a) OpenAI: Codex CLI authenticated by the local ChatGPT subscription.
#               OpenAI API dispatch is forbidden; OPENAI_API_KEY is always unset.
#   (b) Grok:   native-PDF API via tools/int_api_review_2026-07-08.py <paper> grok
#   (d) Gemini: native-PDF API via tools/int_api_review_2026-07-08.py <paper> gemini
#               (7th reviewer leg, keyed 2026-07-11 — only runs when GEMINI_API_KEY
#               is present in .env.local; skipped-as-ABSENT otherwise, never fails
#               the wave on a missing key).
#   (c) Codex subscription: `codex exec` with the canonical PRD-referee prompt,
#       authenticated by the local ChatGPT login (not OPENAI_API_KEY). Its raw
#       output is SAVED (mandatory, per the
#       every-leg-saves-its-raw rule) to
#       INT_api/H17_2026-07-10/intwave_<paper>_codex_HHMM.md.
#
# At the end it prints the verdict matrix parsed from:
#   - the newest API_<paper>_{grok,gemini}.md PARSED VERDICT lines in
#     INT_v3/ROUND_2026-07-09/
#   - the VERDICT line of the just-written Codex file
# and appends a run.log line to INT_api/H17_2026-07-10/run.log.
#
# Usage: tools/int_wave.sh <P1A|P1B|P2|P3|P4|P5> ["optional context-note"]
#
# See canonical spec: ~/.claude/scistack/astrostack/bigbounce-r-round/SKILL.md §1 (INT).

set -uo pipefail   # NOT -e: individual legs may fail; we want the triple regardless.

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
REPO="$(cd "$SCRIPT_DIR/.." && pwd)"
REGISTRY="$REPO/tools/paper_registry.py"
PY_REVIEW="$REPO/tools/int_api_review_2026-07-08.py"
# Match the Python review dispatcher's INT_OUTDIR override.  Exact-PDF
# confirmation waves must be able to write to a content-addressed round
# directory instead of overwriting the legacy rolling files.
API_OUTDIR="${INT_OUTDIR:-$REPO/project-context/peer-reviews/INT_v3/ROUND_2026-07-09}"
SUBSCRIPTION_OUTDIR="$REPO/project-context/peer-reviews/INT_api/H17_2026-07-10"
RUNLOG="$SUBSCRIPTION_OUTDIR/run.log"
CODEX_ENABLED="${BIGBOUNCE_CODEX_SUBSCRIPTION_ENABLED:-1}"
CODEX_BIN="${BIGBOUNCE_CODEX_BIN:-$(command -v codex 2>/dev/null || { [ -x /opt/homebrew/bin/codex ] && printf '%s' /opt/homebrew/bin/codex; })}"
CODEX_MODEL="${BIGBOUNCE_CODEX_MODEL:-gpt-5.6-sol}"
CODEX_EFFORT="${BIGBOUNCE_CODEX_EFFORT:-high}"
REVIEW_COMMIT="${INT_REVIEW_COMMIT:-$(git -C "$REPO" rev-parse HEAD)}"

die() { echo "FAIL: $*" >&2; exit 1; }

[ $# -ge 1 ] || die "usage: tools/int_wave.sh <PAPER> [\"context-note\"]"
PAPER="$1"
CONTEXT="${2:-}"

TEX_REL="$(python3 "$REGISTRY" "$PAPER" tex_path 2>/dev/null)"
[ -n "$TEX_REL" ] || die "unknown paper key '$PAPER' (want P1A|P1B|P2|P3|P4|P5)"
TARGET_JOURNAL="$(python3 "$REGISTRY" "$PAPER" target_journal)"
ARTICLE_TYPE="$(python3 "$REGISTRY" "$PAPER" article_type)"
REVIEW_PROFILE="$(python3 "$REGISTRY" "$PAPER" review_profile)"
TEX="$REPO/$TEX_REL"
[ -f "$TEX" ] || die "tex not found: $TEX"

cd "$REPO"

HHMM="$(date +%H%M)"
CODEX_OUT="$SUBSCRIPTION_OUTDIR/intwave_${PAPER}_codex_${HHMM}.md"
CODEX_CLI_LOG="$SUBSCRIPTION_OUTDIR/.intwave_${PAPER}_codex_${HHMM}.log"

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
echo "    venue:  $TARGET_JOURNAL ($ARTICLE_TYPE; profile=$REVIEW_PROFILE)"
echo "    codex:  ${CODEX_OUT#$REPO/}"

# ---------------------------------------------------------------------------
# Canonical PRD-referee prompt for the Codex subscription leg (full-file
# referee format), plus the optional context-note. The Codex leg reads the
# full paper + source + context (never fabricate — verify against artifacts).
# ---------------------------------------------------------------------------
CODEX_PROMPT="You are an expert referee for $TARGET_JOURNAL reviewing this $ARTICLE_TYPE manuscript at $TEX_REL (version $VER; canonical review profile $REVIEW_PROFILE) in this repository. This is a strictly READ-ONLY review: do not edit files, write state, use a browser, commit, push, or expose credentials. Never inspect .env.local or other secret-bearing files. Read the FULL .tex file (and non-secret figures/source/data you need to verify claims — you have the full repo). Review to the standard of a real $TARGET_JOURNAL submission. Do NOT fabricate: verify every number you check against committed artifacts (recompute read-only, don't just read).

Respond in EXACTLY this format:
(1) VERDICT: ACCEPT / MINOR REVISIONS / MAJOR REVISIONS / REJECT
(2) ISSUES: a numbered list, each item prefixed [MAJOR] or [MINOR], naming the specific section/claim with a file:line reference and the concrete problem.
(3) One sentence: is the central claim supported?"
if [ -n "$CONTEXT" ]; then
  CODEX_PROMPT="$CODEX_PROMPT

CONTEXT NOTE for this review: $CONTEXT"
fi

# Freeze one content-addressed packet before any provider can launch. The API
# legs independently rebuild the same binding; the Codex subscription leg gets
# this packet's immutable PDF snapshot and a clean detached source tree at the
# packet HEAD. The packet hashes the canonical prompt above plus its allowed
# context; the binding appendix added below is metadata, not unhashed review
# instruction.
PACKET_PROMPT="$(mktemp "${TMPDIR:-/tmp}/bigbounce-int-prompt.XXXXXX")"
PACKET_CONTEXT="$(mktemp "${TMPDIR:-/tmp}/bigbounce-int-context.XXXXXX")"
PACKET_JSON="$(mktemp "${TMPDIR:-/tmp}/bigbounce-int-packet.XXXXXX")"
CODEX_TREE=""
cleanup() {
  if [ -n "$CODEX_TREE" ] && [ -d "$CODEX_TREE" ]; then
    git -C "$REPO" worktree remove --force "$CODEX_TREE" >/dev/null 2>&1 || true
  fi
  rm -f "$PACKET_PROMPT" "$PACKET_CONTEXT" "$PACKET_JSON"
}
trap cleanup EXIT INT TERM
printf '%s\n' "$CODEX_PROMPT" >"$PACKET_PROMPT"
printf '%s' "$CONTEXT" >"$PACKET_CONTEXT"

PACKET_ARGS=("$PAPER" --prompt-file "$PACKET_PROMPT" --context-file "$PACKET_CONTEXT" \
  --model "$CODEX_MODEL" --effort "$CODEX_EFFORT")
[ -n "${INT_EXPECTED_PDF_SHA256:-}" ] && PACKET_ARGS+=(--expected-pdf-sha "$INT_EXPECTED_PDF_SHA256")
python3 "$REPO/tools/review_packet.py" "${PACKET_ARGS[@]}" >"$PACKET_JSON" \
  || die "could not build exact Codex review packet"

IFS=$'\t' read -r PACKET_KEY PROMPT_SHA PDF_SHA PDF_PAGES PACKET_HEAD SOURCE_SHA SNAPSHOT_REL \
  < <(python3 - "$PACKET_JSON" <<'PY'
import json, sys
p = json.load(open(sys.argv[1], encoding="utf-8"))["packet"]
print("\t".join(str(p[k]) for k in (
    "packet_key", "prompt_sha256", "pdf_sha256", "page_count",
    "repository_head", "source_sha256", "pdf_snapshot_path",
)))
PY
)
[ -n "$PACKET_KEY" ] || die "empty review packet binding"
[ "$PACKET_HEAD" = "$REVIEW_COMMIT" ] \
  || die "review commit mismatch: expected $REVIEW_COMMIT, packet binds $PACKET_HEAD"
SNAPSHOT_ABS="$(python3 - "${BIGBOUNCE_REVIEW_CACHE:-$HOME/.cache/bigbounce/review-packets}" "$SNAPSHOT_REL" <<'PY'
import pathlib, sys
print((pathlib.Path(sys.argv[1]).expanduser() / sys.argv[2]).resolve())
PY
)"

CODEX_PROMPT="$CODEX_PROMPT

IMMUTABLE REVIEW BINDING (mandatory):
- packet_key: $PACKET_KEY
- prompt_sha256: $PROMPT_SHA
- repository_head: $PACKET_HEAD
- source_sha256: $SOURCE_SHA
- exact_pdf_snapshot: $SNAPSHOT_ABS
- pdf_sha256: $PDF_SHA
- pdf_pages: $PDF_PAGES
- target_journal: $TARGET_JOURNAL
- article_type: $ARTICLE_TYPE
Treat the exact PDF snapshot above as the manuscript of record. Use the clean
detached source tree only to inspect source and committed supporting artifacts.
Do not substitute a working-tree PDF or any differently hashed manuscript."

case "$CODEX_ENABLED" in 0|1) ;; *) die "BIGBOUNCE_CODEX_SUBSCRIPTION_ENABLED must be 0 or 1" ;; esac
case "$CODEX_EFFORT" in minimal|low|medium|high|xhigh|max|ultra) ;; *) die "BIGBOUNCE_CODEX_EFFORT must be minimal|low|medium|high|xhigh|max|ultra" ;; esac

# No-launch validation path: packet creation/hash verification is allowed, but
# there are no API calls, agent sessions, output reviews, or detached worktrees.
if [ "${BIGBOUNCE_INT_WAVE_DRY_RUN:-0}" = "1" ]; then
  LOGIN="unavailable"
  if [ -n "$CODEX_BIN" ]; then LOGIN="$(env -u OPENAI_API_KEY -u CODEX_API_KEY -u ANTHROPIC_API_KEY "$CODEX_BIN" login status 2>&1 || true)"; fi
  printf 'DRY_RUN paper=%s version=%s dispatch=false codex_enabled=%s model=%s effort=%s sandbox=read-only auth=%s\n' \
    "$PAPER" "$VER" "$CODEX_ENABLED" "$CODEX_MODEL" "$CODEX_EFFORT" "$LOGIN"
  printf 'BINDING packet_key=%s prompt_sha256=%s commit=%s source_sha256=%s pdf_sha256=%s pages=%s venue=%s article_type=%s source_tree=detached-clean\n' \
    "$PACKET_KEY" "$PROMPT_SHA" "$PACKET_HEAD" "$SOURCE_SHA" "$PDF_SHA" "$PDF_PAGES" \
    "$TARGET_JOURNAL" "$ARTICLE_TYPE"
  exit 0
fi

mkdir -p "$SUBSCRIPTION_OUTDIR"

# ---------------------------------------------------------------------------
# Validate subscription auth and prepare the clean tree before any provider
# launches. This prevents an API leg from escaping if Codex provenance setup
# fails closed.
# ---------------------------------------------------------------------------

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
  CODEX_TREE="$(mktemp -d "${TMPDIR:-/tmp}/bigbounce-codex-tree.XXXXXX")"
  rmdir "$CODEX_TREE"
  git -C "$REPO" worktree add --quiet --detach "$CODEX_TREE" "$PACKET_HEAD" \
    || die "could not create clean detached Codex source tree at $PACKET_HEAD"
  [ -z "$(git -C "$CODEX_TREE" status --porcelain)" ] \
    || die "detached Codex source tree is unexpectedly dirty"
fi

# ---------------------------------------------------------------------------
# Launch the API and subscription legs in parallel; capture PIDs; wait on all.
# ---------------------------------------------------------------------------

# (b) Grok leg
(
  set -a; source "$REPO/.env.local"; set +a
  INT_CONTEXT="$CONTEXT" python3 "$PY_REVIEW" "$PAPER" grok
) >"$SUBSCRIPTION_OUTDIR/.intwave_${PAPER}_grok_${HHMM}.log" 2>&1 &
PID_GROK=$!

# (d) Gemini leg — 7th reviewer, only when GEMINI_API_KEY is present (keyed
#     2026-07-11). We source .env.local in a subshell to test the key without
#     leaking it into this shell's env or any log line.
GEMINI_ON=0
if ( set -a; source "$REPO/.env.local" >/dev/null 2>&1; set +a; [ -n "${GEMINI_API_KEY:-}" ] ); then
  GEMINI_ON=1
  (
    set -a; source "$REPO/.env.local"; set +a
    INT_CONTEXT="$CONTEXT" python3 "$PY_REVIEW" "$PAPER" gemini
  ) >"$SUBSCRIPTION_OUTDIR/.intwave_${PAPER}_gemini_${HHMM}.log" 2>&1 &
  PID_GEMINI=$!
fi

# (c) Codex ChatGPT-subscription leg. Never source .env.local here. The fixed
#     read-only sandbox + never-approve policy makes this a referee, not an editor.
if [ "$CODEX_ON" = 1 ]; then
(
  {
    echo "# INT Codex-subscription Review — $PAPER $VER — $CODEX_MODEL ($CODEX_EFFORT)"
    echo "paper: $PAPER  version: $VER  tex: $TEX_REL"
    echo "modality: full-repo Codex CLI ChatGPT-subscription referee (read-only, ephemeral)"
    echo "binding: packet_key=$PACKET_KEY  prompt_sha256=$PROMPT_SHA"
    echo "provenance: commit=$PACKET_HEAD  source_sha256=$SOURCE_SHA"
    echo "pdf: snapshot=$SNAPSHOT_ABS  sha256=$PDF_SHA  pages=$PDF_PAGES"
    echo "venue: $TARGET_JOURNAL  article_type: $ARTICLE_TYPE  profile: $REVIEW_PROFILE"
    echo "source_tree: clean detached worktree at $PACKET_HEAD"
    echo "UTC: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    [ -n "$CONTEXT" ] && echo "context-note: $CONTEXT"
    echo ""
    echo "======================================================================"
    echo "RAW RESPONSE (verbatim):"
    echo "======================================================================"
    echo ""
    RAW_TMP="$(mktemp "${TMPDIR:-/tmp}/bigbounce-codex-review.XXXXXX")"
    if printf '%s\n' "$CODEX_PROMPT" | env -u OPENAI_API_KEY -u CODEX_API_KEY -u ANTHROPIC_API_KEY \
      "$CODEX_BIN" --cd "$CODEX_TREE" --sandbox read-only --ask-for-approval never \
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

if [ "$GEMINI_ON" = 1 ]; then
  echo "    launched: grok(pid $PID_GROK) gemini(pid $PID_GEMINI) codex-subscription=${CODEX_STATE}${PID_CODEX:+(pid $PID_CODEX)} — blocking until all done..."
else
  echo "    launched: grok(pid $PID_GROK) codex-subscription=${CODEX_STATE}${PID_CODEX:+(pid $PID_CODEX)} [gemini: no key] — blocking until all done..."
fi

wait "$PID_GROK";   RC_GROK=$?
RC_CODEX=0
if [ "$CODEX_ON" = 1 ]; then wait "$PID_CODEX"; RC_CODEX=$?; fi
RC_GEMINI=0
if [ "$GEMINI_ON" = 1 ]; then wait "$PID_GEMINI"; RC_GEMINI=$?; fi

# ---------------------------------------------------------------------------
# Parse the verdict triple.
# ---------------------------------------------------------------------------
parse_api_verdict() {
  # $1 = vendor (grok|gemini). The python script writes/overwrites
  # API_<paper>_<vendor>.md with a "PARSED VERDICT:" line.
  local f="$API_OUTDIR/API_${PAPER}_$1.md"
  if [ -f "$f" ]; then
    grep -m1 '^PARSED VERDICT:' "$f" | sed 's/^PARSED VERDICT:[[:space:]]*//' || true
  fi
}

V_GROK="$(parse_api_verdict grok)";     [ -n "$V_GROK" ]   || V_GROK="ABSENT"
if [ "$GEMINI_ON" = 1 ]; then
  V_GEMINI="$(parse_api_verdict gemini)"; [ -n "$V_GEMINI" ] || V_GEMINI="ABSENT"
else
  V_GEMINI="NO-KEY"
fi

# Codex verdict: pull the (1) VERDICT line from the just-written raw file, then
# normalize to a bare verdict token (strip markdown **, trailing punctuation, and
# any trailing prose after the verdict word).
V_CODEX_RAW="$(grep -m1 -iE 'VERDICT:' "$CODEX_OUT" 2>/dev/null \
  | sed -E 's/.*VERDICT:[[:space:]]*//I')"
V_CODEX="$(printf '%s' "$V_CODEX_RAW" | python3 -c '
import sys, re
s = sys.stdin.read().strip().strip("*").strip()
u = s.upper()
for v in ("MAJOR REVISIONS","MINOR REVISIONS","ACCEPT","REJECT"):
    if v in u:
        print(v); break
else:
    print(re.sub(r"[*_`]+"," ",s).strip() or "ABSENT")
')"
if [ "$CODEX_ON" = 1 ]; then
  [ -n "$V_CODEX" ] || V_CODEX="ABSENT"
else
  V_CODEX="$CODEX_STATE"
fi

TS_UTC="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo ""
echo "=== INT WAVE VERDICT MATRIX :: $PAPER $VER ==="
echo "  Grok (grok-4.3):           $V_GROK"
echo "  Gemini (gemini-3.1-pro):   $V_GEMINI"
echo "  OpenAI via Codex subscription ($CODEX_MODEL/$CODEX_EFFORT): $V_CODEX"
echo "  (rc: grok=$RC_GROK gemini=$RC_GEMINI codex_subscription=$RC_CODEX)"

# Append to run.log.
LOGLINE="$TS_UTC | $PAPER $VER | grok=$V_GROK | gemini=$V_GEMINI | openai_subscription=$V_CODEX"
[ "$CODEX_ON" = 1 ] && LOGLINE="$LOGLINE | codex_raw=${CODEX_OUT#$REPO/}"
[ -n "$CONTEXT" ] && LOGLINE="$LOGLINE | ctx=\"$CONTEXT\""
echo "$LOGLINE" >>"$RUNLOG"
echo "  logged -> ${RUNLOG#$REPO/}"
