#!/usr/bin/env bash
# post_verdict.sh — record ONE EXT verdict to Convex + recompute the paper's
# readiness cap from the EXT-reviewer formula.
#
#   1. externalReviews:upsertByLabelDate  (real verdict, raw-path in notes)
#   2. query the paper's externalReviews rows -> latest-per-EXT-reviewer
#   3. readiness = 50 + sum over {grok,chatgpt,gemini} of latest score
#          ACCEPT 16.7 / MINOR 12 / MAJOR 6 / REJECT 0  (per reviewer)
#   4. papers:setReadinessCap
#
# Usage:
#   tools/post_verdict.sh <paper> <reviewer-label> <recommendation> \
#                         <majorCount> <minorCount> <raw-path>
#     <paper>          P1U|P2|P3|P4|P5  (or a canonical slug paper-1a..paper-5)
#     <reviewer-label> free label, e.g. "H17H-Grok" (must contain grok|chatgpt|gemini)
#     <recommendation> accept|minor-revisions|major-revisions|reject|pending
#
# Proven-recipe source: ~/.claude/scistack/astrostack/bigbounce-r-round/SKILL.md

set -euo pipefail

CONVEX_MUT="https://brilliant-panther-471.convex.cloud/api/mutation"
CONVEX_QRY="https://brilliant-panther-471.convex.cloud/api/query"

die() { echo "FAIL: $*" >&2; exit 1; }

slug_for_paper() {
  case "$1" in
    P1U) echo "paper-1a" ;;
    P2)  echo "paper-2" ;;
    P3)  echo "paper-3" ;;
    P4)  echo "paper-4" ;;
    P5)  echo "paper-5" ;;
    paper-1a|paper-1b|paper-2|paper-3|paper-4|paper-5) echo "$1" ;;
    *)   echo "" ;;
  esac
}

[ $# -eq 6 ] || die "usage: tools/post_verdict.sh <paper> <reviewer-label> <recommendation> <majorCount> <minorCount> <raw-path>"
PAPER="$1"; RLABEL="$2"; REC="$3"; MAJ="$4"; MIN="$5"; RAW="$6"

SLUG="$(slug_for_paper "$PAPER")"; [ -n "$SLUG" ] || die "unknown paper '$PAPER'"
case "$REC" in accept|minor-revisions|major-revisions|reject|pending) ;; *) die "bad recommendation '$REC'" ;; esac

TODAY_HUMAN="$(date '+%B %-d, %Y')"

# verbatim verdict line from the raw file (first line matching VERDICT), + path
VLINE=""
if [ -f "$RAW" ]; then
  VLINE="$(grep -iE 'VERDICT' "$RAW" | head -1 | tr -d '\r' || true)"
fi
NOTES="$(printf '%s | raw: %s' "${VLINE:-$REC}" "$RAW")"

# ---- step 1: upsert the review row ----
echo "=== post_verdict :: $SLUG / $RLABEL -> $REC (maj=$MAJ min=$MIN) ==="
UPSERT_PAYLOAD="$(python3 - "$SLUG" "$RLABEL" "$TODAY_HUMAN" "$MAJ" "$MIN" "$REC" "$NOTES" "$RAW" <<'PY'
import json, sys
slug, label, when, maj, minc, rec, notes, raw = sys.argv[1:9]
print(json.dumps({
  "path": "externalReviews:upsertByLabelDate",
  "args": {
    "paperSlug": slug,
    "source": "internal-stage3",
    "reviewerLabel": label,
    "receivedAt": when,
    "blockerCount": 0,
    "majorCount": float(maj),
    "minorCount": float(minc),
    "recommendation": rec,
    "notes": notes,
    "pdfUrl": raw,
  },
  "format": "json",
}))
PY
)"
UP_RESP="$(curl -sS -X POST "$CONVEX_MUT" -H 'Content-Type: application/json' -d "$UPSERT_PAYLOAD")"
echo "    upsert: $UP_RESP"
echo "$UP_RESP" | python3 -c 'import sys,json;sys.exit(0 if json.load(sys.stdin).get("status")=="success" else 1)' \
  || die "externalReviews upsert did not succeed"

# ---- step 2: query rows + compute latest-per-EXT-reviewer readiness ----
LIST_PAYLOAD="$(python3 - "$SLUG" <<'PY'
import json,sys
print(json.dumps({"path":"externalReviews:list","args":{"paperSlug":sys.argv[1]},"format":"json"}))
PY
)"
LIST_RESP="$(curl -sS -X POST "$CONVEX_QRY" -H 'Content-Type: application/json' -d "$LIST_PAYLOAD")"

# Write the response to a temp file and pass its path as argv — a `<<'PY'`
# heredoc consumes stdin, so we must NOT rely on a pipe into sys.stdin here.
LIST_TMP="$(mktemp)"
trap 'rm -f "$LIST_TMP"' EXIT
printf '%s' "$LIST_RESP" > "$LIST_TMP"
CAP="$(python3 - "$LIST_TMP" <<'PY'
import sys, json, re
d=json.load(open(sys.argv[1]))
rows=d.get("value") or []
# score map per reviewer recommendation
SCORE={"accept":16.7,"minor-revisions":12.0,"major-revisions":6.0,"reject":0.0,"pending":0.0}
def canon(label):
    l=(label or "").lower()
    if "chatgpt" in l or "gpt" in l: return "chatgpt"
    if "grok" in l: return "grok"
    if "gemini" in l: return "gemini"
    return None
# latest-per-reviewer by receivedAt (rows already sorted desc by list handler,
# but re-sort to be safe: Date.parse-ish ordering not needed — take first seen).
latest={}
def key(r):
    # sort newest first: rows come pre-sorted desc; keep stable
    return 0
seen=set()
for r in rows:  # already desc by receivedAt
    who=canon(r.get("reviewerLabel"))
    if who and who not in latest:
        latest[who]=r.get("recommendation","pending")
score=50.0
for who in ("grok","chatgpt","gemini"):
    rec=latest.get(who)
    if rec is not None:
        score+=SCORE.get(rec,0.0)
cap=int(round(score))
if cap>100: cap=100
if cap<0: cap=0
sys.stderr.write("    latest-per-reviewer: %s\n" % json.dumps(latest))
print(cap)
PY
)"
echo "    computed readiness cap: $CAP"

# ---- step 3: setReadinessCap ----
CAP_PAYLOAD="$(python3 - "$SLUG" "$CAP" <<'PY'
import json,sys
print(json.dumps({"path":"papers:setReadinessCap","args":{"slug":sys.argv[1],"cap":int(sys.argv[2])},"format":"json"}))
PY
)"
CAP_RESP="$(curl -sS -X POST "$CONVEX_MUT" -H 'Content-Type: application/json' -d "$CAP_PAYLOAD")"
echo "    setReadinessCap: $CAP_RESP"
echo "$CAP_RESP" | python3 -c 'import sys,json;sys.exit(0 if json.load(sys.stdin).get("status")=="success" else 1)' \
  || die "papers:setReadinessCap did not succeed"

echo "PASS: $SLUG $RLABEL=$REC cap=$CAP"

# ---- step 4: mirror this verdict into readinessMetrics (trajectory chart + ETA) ----
# One row per (paper, wave). Reviewer + wave label derived from the reviewer-label.
# Keeps the /reviews Verdict-trajectory chart + the homepage Submission-ready ETA
# live on every harvest with no extra manual step. Non-fatal: a readinessMetrics
# failure must not fail the verdict post.
REVIEWER="Grok"
case "$(printf '%s' "$RLABEL" | tr 'A-Z' 'a-z')" in
  *chatgpt*|*gpt*) REVIEWER="ChatGPT" ;;
  *grok*)          REVIEWER="Grok" ;;
  *gemini*)        REVIEWER="Gemini" ;;
esac
# wave label = reviewer-label with the trailing reviewer token stripped,
# e.g. "H17H-Grok" -> "H17H". Falls back to the full label.
WAVE_LABEL="$(printf '%s' "$RLABEL" | sed -E 's/[-_]?(chatgpt|gpt|grok|gemini)$//I')"
[ -n "$WAVE_LABEL" ] || WAVE_LABEL="$RLABEL"
TODAY_ISO="$(date '+%Y-%m-%d')"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
if [ -x "$SCRIPT_DIR/record_wave.sh" ]; then
  # genuinelyNew/streak/open counts default to 0 here — the orchestrator posts a
  # fuller row via record_wave.sh directly when it knows the audit outcome.
  "$SCRIPT_DIR/record_wave.sh" "$PAPER" "$WAVE_LABEL" "$TODAY_ISO" 0 0 0 0 \
    "$REVIEWER:EXT:$REC" "auto from post_verdict.sh ($RLABEL); raw: $RAW" \
    || echo "WARN: readinessMetrics record_wave failed (non-fatal)" >&2
fi
