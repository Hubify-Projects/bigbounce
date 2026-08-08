#!/usr/bin/env bash
# record_wave.sh — post ONE per-paper per-wave readinessMetrics row to Convex
# after a harvest/audit, so the /reviews Verdict-trajectory chart + the homepage
# Submission-ready ETA stay live with zero manual steps.
#
# Idempotent on (paperSlug, waveLabel): re-running overwrites the row in place.
#
# HONESTY: verdicts come ONLY from the recorded raws you pass in. A leg with no
# output is "<reviewer>:failed" (a chart GAP, never a zero). Never synthesize.
#
# Usage:
#   tools/record_wave.sh <paper> <waveLabel> <dateISO> \
#       <genuinelyNewCount> <cleanWaveStreak> <openComputeCount> <openVenueCount> \
#       "<reviewer:channel:verdict,reviewer:channel:verdict,...>" ["<note>"]
#
#   <paper>       P1A|P1B|P2|P3|P4|P5  (P1U accepted as an alias for P1A)
#   channel       INT|EXT
#   verdict       reject|major-revisions|minor-revisions|accept|failed
#
# Example (H17 EXT harvest for P5 — Grok ACCEPT, ChatGPT MAJOR, Gemini failed):
#   tools/record_wave.sh P5 H17F-final 2026-07-10 0 1 0 0 \
#     "ChatGPT:EXT:major-revisions,Grok:EXT:accept,Gemini:EXT:failed" \
#     "final-wave EXT; 0 genuinely-new; Gemini upload-throttle FAILED"
#
# Proven-recipe source: ~/.claude/scistack/astrostack/bigbounce-r-round/SKILL.md
set -euo pipefail

CONVEX_MUT="https://brilliant-panther-471.convex.cloud/api/mutation"
die() { echo "FAIL: $*" >&2; exit 1; }

[ $# -ge 8 ] || die "usage: tools/record_wave.sh <paper> <waveLabel> <dateISO> <genuinelyNew> <cleanStreak> <openCompute> <openVenue> <verdicts> [note]"
PAPER="$1"; WAVE="$2"; DATE="$3"; GNEW="$4"; STREAK="$5"; OCOMP="$6"; OVEN="$7"; VERDICTS="$8"; NOTE="${9:-}"

case "$PAPER" in
  P1A|P1U) PID="P1A"; SLUG="paper-1a" ;;
  P1B) PID="P1B"; SLUG="paper-1b" ;;
  P2)  PID="P2";  SLUG="paper-2" ;;
  P3)  PID="P3";  SLUG="paper-3" ;;
  P4)  PID="P4";  SLUG="paper-4" ;;
  P5)  PID="P5";  SLUG="paper-5" ;;
  *)   die "unknown paper '$PAPER'" ;;
esac

PAYLOAD="$(python3 - "$SLUG" "$PID" "$WAVE" "$DATE" "$GNEW" "$STREAK" "$OCOMP" "$OVEN" "$VERDICTS" "$NOTE" <<'PY'
import json, sys
slug, pid, wave, date, gnew, streak, ocomp, oven, vstr, note = sys.argv[1:11]
VALID_V = {"reject","major-revisions","minor-revisions","accept","failed"}
verdicts = []
for tok in vstr.split(","):
    tok = tok.strip()
    if not tok:
        continue
    parts = tok.split(":")
    if len(parts) != 3:
        sys.stderr.write("bad verdict token (need reviewer:channel:verdict): %r\n" % tok)
        sys.exit(2)
    reviewer, channel, verdict = parts
    if channel not in ("INT","EXT"):
        sys.stderr.write("bad channel %r (INT|EXT)\n" % channel); sys.exit(2)
    if verdict not in VALID_V:
        sys.stderr.write("bad verdict %r\n" % verdict); sys.exit(2)
    verdicts.append({"reviewer": reviewer, "channel": channel, "verdict": verdict})
if not verdicts:
    sys.stderr.write("no verdicts parsed\n"); sys.exit(2)
args = {
    "paperSlug": slug, "paperId": pid, "waveLabel": wave, "dateISO": date,
    "genuinelyNewCount": int(gnew), "cleanWaveStreak": int(streak),
    "openComputeCount": int(ocomp), "openVenueCount": int(oven),
    "verdicts": verdicts,
}
if note:
    args["note"] = note
print(json.dumps({"path": "readinessMetrics:recordWave", "args": args, "format": "json"}))
PY
)"

echo "=== record_wave :: $PID / $WAVE ($DATE) ==="
RESP="$(curl -sS -X POST "$CONVEX_MUT" -H 'Content-Type: application/json' -d "$PAYLOAD")"
echo "    $RESP"
echo "$RESP" | python3 -c 'import sys,json;sys.exit(0 if json.load(sys.stdin).get("status")=="success" else 1)' \
  || die "readinessMetrics:recordWave did not succeed"
echo "PASS: $PID $WAVE recorded"
