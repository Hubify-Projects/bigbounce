#!/usr/bin/env bash
# ext_harvest.sh — harvest EXT (browser) referee responses for a round.
#
# Reads manifest rows for <round-label> whose status starts with "submitted",
# visits each chat URL, extracts the reviewer's response with the reviewer's
# proven selectors, and (if a real verdict is present) saves raw .md + .png into
# EXT_real/H17_2026-07-10/<round>/ and flips the manifest row to "harvested".
# Prints a verdict matrix at the end.
#
# Status transitions:
#   real verdict found  -> harvested   (raw .md + .png saved)
#   dead chat            -> FAILED-dead (no verdict, no thinking indicator, no msg)
#   still generating     -> left as-is, printed "cooking"
#
# Usage: tools/ext_harvest.sh <round-label>
#
# Proven-recipe source: ~/.claude/scistack/astrostack/bigbounce-r-round/SKILL.md

set -euo pipefail

REPO="/Users/houstongolden/Desktop/CODE_YOU/bigbounce"
B="$HOME/.claude/skills/gstack/browse/dist/browse"
ROUND_DIR_BASE="$REPO/project-context/peer-reviews/EXT_real/H17_2026-07-10"
MANIFEST="$ROUND_DIR_BASE/manifest.jsonl"

# Grok free-forms ("Recommendation" heading, verdict on the NEXT line) instead of
# ChatGPT's "(1) VERDICT: X" one-liner. grep is line-oriented and cannot match a
# keyword+verdict split across a newline, so the gate is a python check that,
# like the extractor JS, treats the whole blob as one string (DOTALL).
die() { echo "FAIL: $*" >&2; exit 1; }

# has_verdict: read text on stdin -> exit 0 if a verdict is present, else 1.
has_verdict() {
  python3 -c '
import sys, re
t=sys.stdin.read()
sys.exit(0 if re.search(r"(VERDICT|Recommendation)[^A-Za-z]{0,40}(ACCEPT|MINOR|MAJOR|REJECT)", t, re.I|re.S) else 1)
'
}

BOUT=""
bcall() {
  local to="$1"; shift
  local out rc
  out="$(timeout "$to" "$B" "$@" 2>&1)" && { BOUT="$out"; return 0; }
  rc=$?
  if printf '%s' "$out" | grep -qiE "Run '/open-gstack-browser'|not connected"; then
    echo "    [auto-recover] browser not connected — reconnecting headed" >&2
    timeout 90 "$B" connect >/dev/null 2>&1 || true
    out="$(timeout "$to" "$B" "$@" 2>&1)" && { BOUT="$out"; return 0; }
    rc=$?
  fi
  BOUT="$out"
  return $rc
}

[ $# -eq 1 ] || die "usage: tools/ext_harvest.sh <round-label>"
ROUND="$1"
OUTDIR="$ROUND_DIR_BASE/$ROUND"
mkdir -p "$OUTDIR"
[ -f "$MANIFEST" ] || die "manifest not found: $MANIFEST"

# ---- collect rows for this round with a submitted* status + a url ----
ROWS_FILE="$(mktemp)"
trap 'rm -f "$ROWS_FILE"' EXIT
python3 - "$MANIFEST" "$ROUND" > "$ROWS_FILE" <<'PY'
import sys, json
manifest, rnd = sys.argv[1], sys.argv[2]
for line in open(manifest):
    line = line.strip()
    if not line:
        continue
    try:
        r = json.loads(line)
    except Exception:
        continue
    if r.get("round") != rnd:
        continue
    st = r.get("status", "")
    if not st.startswith("submitted"):
        continue
    url = r.get("url", "")
    if not url:
        continue
    print("\t".join([r.get("paper", "?"), r.get("reviewer", "?"), url]))
PY

if [ ! -s "$ROWS_FILE" ]; then
  echo "no submitted* rows with URLs for round '$ROUND' — nothing to harvest"
  exit 0
fi

echo "=== ext_harvest :: round=$ROUND ==="

# extraction JS per reviewer -> prints the response text (or empty)
extract_js() {
  case "$1" in
    grok) cat <<'JS'
(function(){
  var sels=["[class*=message-bubble]","[class*=response-content]",".markdown"];
  var nodes=[];
  sels.forEach(function(s){[].push.apply(nodes,[...document.querySelectorAll(s)]);});
  if(!nodes.length) return "";
  var last=nodes[nodes.length-1];
  var t=(last.innerText||"").trim();
  return /(VERDICT|Recommendation)[^A-Za-z]{0,40}(ACCEPT|MINOR|MAJOR|REJECT)/i.test(t)?t:"";
})()
JS
      ;;
    chatgpt) cat <<'JS'
(function(){
  var nodes=[...document.querySelectorAll("article,[data-message-author-role=assistant]")];
  var hits=nodes.filter(function(n){var t=n.innerText||"";return /central claim|VERDICT|REJECT|ACCEPT|REVISIONS/i.test(t);});
  // exclude the prompt echo: drop nodes that look like the user prompt
  hits=hits.filter(function(n){var t=n.innerText||"";return !/Review this manuscript to the standard/i.test(t);});
  if(!hits.length) return "";
  return (hits[hits.length-1].innerText||"").trim();
})()
JS
      ;;
    gemini) cat <<'JS'
(function(){
  var sels=["model-response","[class*=model-response]","message-content","[class*=message-content]"];
  var nodes=[];
  sels.forEach(function(s){[].push.apply(nodes,[...document.querySelectorAll(s)]);});
  var hits=nodes.filter(function(n){return /VERDICT/i.test(n.innerText||"");});
  if(!hits.length) return "";
  return (hits[hits.length-1].innerText||"").trim();
})()
JS
      ;;
  esac
}

# dead-chat detector JS per reviewer -> prints "DEAD" or "ALIVE"
dead_js() {
  case "$1" in
    grok) cat <<'JS'
(function(){
  var thinking=/Thinking|Reasoning/i.test(document.body.innerText||"");
  return thinking?"ALIVE":"DEAD";
})()
JS
      ;;
    chatgpt) cat <<'JS'
(function(){
  var thinking=/Thinking|Reasoning/i.test(document.body.innerText||"");
  var asst=document.querySelectorAll("[data-message-author-role=assistant],article").length;
  return (thinking||asst>0)?"ALIVE":"DEAD";
})()
JS
      ;;
    gemini) cat <<'JS'
(function(){
  var thinking=/Thinking|Reasoning/i.test(document.body.innerText||"");
  var uq=document.querySelectorAll("user-query,[class*=user-query]").length;
  return (thinking||uq>0)?"ALIVE":"DEAD";
})()
JS
      ;;
  esac
}

# results accumulator for the matrix
MATRIX_FILE="$(mktemp)"
trap 'rm -f "$ROWS_FILE" "$MATRIX_FILE"' EXIT

update_manifest_status() {
  # args: paper reviewer round url newstatus verdict
  python3 - "$MANIFEST" "$1" "$2" "$3" "$4" "$5" "$6" <<'PY'
import sys, json
manifest, paper, reviewer, rnd, url, newstatus, verdict = sys.argv[1:8]
lines=[]
for line in open(manifest):
    s=line.strip()
    if not s:
        lines.append(line); continue
    try:
        r=json.loads(s)
    except Exception:
        lines.append(line); continue
    if r.get("paper")==paper and r.get("reviewer")==reviewer and r.get("round")==rnd and r.get("url")==url:
        r["status"]=newstatus
        if verdict: r["verdict"]=verdict
        line=json.dumps(r)+"\n"
    lines.append(line if line.endswith("\n") else line+"\n")
with open(manifest,"w") as f:
    f.writelines(lines)
PY
}

parse_verdict() {
  # read raw text on stdin -> print normalized verdict token.
  # NOTE: use `python3 -c` (NOT a `<<'PY'` heredoc) — a heredoc consumes the
  # process stdin, so the piped text would never reach sys.stdin.read().
  python3 -c '
import sys, re
t=sys.stdin.read()
for line in t.splitlines():
    if re.search(r"verdict|recommendation", line, re.I):
        seg=line.split(":",1)[-1].upper()
        for v in ("MAJOR REVISIONS","MINOR REVISIONS","MAJOR","MINOR","ACCEPT","REJECT"):
            if v in seg:
                print({"MAJOR":"MAJOR REVISIONS","MINOR":"MINOR REVISIONS"}.get(v,v)); sys.exit()
up=t.upper()
for v in ("MAJOR REVISIONS","MINOR REVISIONS","ACCEPT","REJECT"):
    if v in up: print(v); sys.exit()
print("UNKNOWN")
'
}

while IFS=$'\t' read -r PAPER REVIEWER URL; do
  [ -n "$PAPER" ] || continue
  echo "--- $PAPER / $REVIEWER ---"
  echo "    url: $URL"
  if ! bcall 45 goto "$URL"; then
    echo "    WARN goto failed: $BOUT — skipping"
    printf '%s\t%s\t%s\n' "$PAPER" "$REVIEWER" "goto-failed" >> "$MATRIX_FILE"
    continue
  fi
  bcall 45 wait --networkidle || true
  sleep 4

  # try extraction — SPA chats can take several seconds to render after goto,
  # so poll the extractor a few times before declaring the chat dead.
  EJS="$(extract_js "$REVIEWER")"
  RESP=""
  for _try in 1 2 3 4 5; do
    bcall 45 js "$EJS" || true
    RESP="$BOUT"
    RESP="$(printf '%s' "$RESP" | sed -e 's/^"//' -e 's/"$//')"
    printf '%s' "$RESP" | has_verdict && break
    sleep 4
  done

  if printf '%s' "$RESP" | has_verdict; then
    # real verdict -> save
    RAW="$OUTDIR/${PAPER}_${REVIEWER}_${ROUND}.md"
    PNG="$OUTDIR/${PAPER}_${REVIEWER}_${ROUND}.png"
    printf '%s\n' "$RESP" > "$RAW"
    bcall 45 screenshot "$PNG" || echo "    WARN screenshot failed"
    VERDICT="$(printf '%s' "$RESP" | parse_verdict)"
    update_manifest_status "$PAPER" "$REVIEWER" "$ROUND" "$URL" "harvested" "$VERDICT"
    echo "    HARVESTED -> $VERDICT  ($RAW)"
    printf '%s\t%s\t%s\n' "$PAPER" "$REVIEWER" "$VERDICT" >> "$MATRIX_FILE"
  else
    # no verdict: dead or cooking?
    DJS="$(dead_js "$REVIEWER")"
    bcall 45 js "$DJS" || true
    if printf '%s' "$BOUT" | grep -q DEAD; then
      update_manifest_status "$PAPER" "$REVIEWER" "$ROUND" "$URL" "FAILED-dead" ""
      echo "    FAILED-dead (no verdict, no thinking indicator, no message)"
      printf '%s\t%s\t%s\n' "$PAPER" "$REVIEWER" "FAILED-dead" >> "$MATRIX_FILE"
    else
      echo "    cooking (still generating — status left submitted)"
      printf '%s\t%s\t%s\n' "$PAPER" "$REVIEWER" "cooking" >> "$MATRIX_FILE"
    fi
  fi
done < "$ROWS_FILE"

echo ""
echo "================ VERDICT MATRIX (round $ROUND) ================"
printf '%-6s %-9s %s\n' "PAPER" "REVIEWER" "VERDICT/STATUS"
printf '%-6s %-9s %s\n' "-----" "--------" "--------------"
if [ -s "$MATRIX_FILE" ]; then
  while IFS=$'\t' read -r P R V; do
    printf '%-6s %-9s %s\n' "$P" "$R" "$V"
  done < "$MATRIX_FILE"
fi
echo "=============================================================="

# --- site-freshness gate (non-fatal warn) --------------------------------
# A harvest just landed new verdicts; the public surfaces (banner/board/skills/
# versions) must reflect them. Warn here so the operator fixes them same-tick;
# the pre-push hook enforces it hard.
FRESH_CHECK="$REPO/tools/site_freshness_check.sh"
if [ -x "$FRESH_CHECK" ]; then
  echo ""
  if ! "$FRESH_CHECK" --report; then
    echo "WARN: site is STALE after this harvest — sync the flagged surface(s) THIS tick (see table above)." >&2
  fi
fi
