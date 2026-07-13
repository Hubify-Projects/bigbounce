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

# ---- HEADED-BROWSER PREFLIGHT (2026-07-13, permanent) -----------------------
# HARVEST is the DANGEROUS one on a launched/headless browser: every chat URL
# renders a login/error wall, the extractor finds no verdict, and the dead-chat
# detector marks LIVE legs FAILED-dead (all 6 M42 legs, 2026-07-13 — the reviews
# were alive server-side). assert_headed requires the literal `Mode: headed`
# line from `$B status` before ANY harvest work; NEVER proceed on `launched`.
assert_headed() {
  local out mode
  out="$(timeout 30 "$B" status 2>&1 || true)"
  mode="$(printf '%s\n' "$out" | grep -iE '^Mode:' | head -1 | awk '{print $2}')"
  if [ "$mode" != "headed" ]; then
    echo "FAIL: browser not headed (Mode: ${mode:-unknown}) — run: $B cleanup; kill port 34567 holders; $B connect; verify Mode: headed" >&2
    exit 1
  fi
}

# has_verdict: read text on stdin -> exit 0 if a verdict is present, else 1.
has_verdict() {
  python3 -c '
import sys, re
t=sys.stdin.read()
sys.exit(0 if re.search(r"(VERDICT|Recommendation)[^A-Za-z]{0,40}(ACCEPT|MINOR|MAJOR|REJECT)", t, re.I|re.S) else 1)
'
}

# ---------------------------------------------------------------------------
# HARVEST-TIME GATES (directive I4: a leg with no verifiable output is FAILED,
# NOT a verdict). Four incidents drove these — a 273-byte prompt-echo stub
# recorded MAJOR (P1U M30), a 0-byte raw recorded REJECT (P4 M24), two
# wrong-paper misfiles recorded as P3APJS (M32 byte-identical to a P1U raw;
# M34 a P5 review). Each gate runs AFTER the raw is on disk but BEFORE any
# verdict reaches the manifest/matrix.
# ---------------------------------------------------------------------------

# gate_substance <rawfile> -> 0 pass, 1 fail (too small / no verdict line)
gate_substance() {
  local f="$1"
  local n
  n=$(wc -c < "$f" 2>/dev/null | tr -d ' ')
  [ -n "$n" ] || n=0
  if [ "$n" -lt 1500 ]; then
    echo "    GATE substance: FAIL — raw is ${n} bytes (< 1500-byte floor)" >&2
    return 1
  fi
  if ! grep -iqE "VERDICT|MAJOR REVISIONS|MINOR REVISIONS|ACCEPT|REJECT" "$f"; then
    echo "    GATE substance: FAIL — no verdict line found in raw" >&2
    return 1
  fi
  return 0
}

# gate_duplicate <rawfile> <paper> <round> -> 0 pass, 1 fail
# Fails if this raw's md5 matches ANY OTHER paper's raw in the current round
# dir or the previous 2 round dirs (M-numbered scan window).
gate_duplicate() {
  local f="$1" paper="$2" round="$3"
  local mine
  mine=$(md5 -q "$f" 2>/dev/null || md5sum "$f" 2>/dev/null | awk '{print $1}')
  [ -n "$mine" ] || return 0
  # build the scan window: current round + previous 2 M-numbered rounds
  local dirs=("$ROUND_DIR_BASE/$round")
  local num=""
  case "$round" in
    M[0-9]*) num="${round#M}" ;;
  esac
  if [ -n "$num" ] && printf '%s' "$num" | grep -qE '^[0-9]+$'; then
    local p
    for p in 1 2; do
      dirs+=("$ROUND_DIR_BASE/M$((num - p))")
    done
  fi
  local d other omd5
  for d in "${dirs[@]}"; do
    [ -d "$d" ] || continue
    for other in "$d"/*.md; do
      [ -e "$other" ] || continue
      # skip our own file and same-paper files (a paper legitimately shares
      # content across its own legs/rounds; a cross-PAPER match is the tell)
      [ "$other" = "$f" ] && continue
      case "$(basename "$other")" in
        ${paper}_*) continue ;;   # same paper -> not a misfile signal
      esac
      omd5=$(md5 -q "$other" 2>/dev/null || md5sum "$other" 2>/dev/null | awk '{print $1}')
      if [ "$omd5" = "$mine" ]; then
        echo "    GATE duplicate: FAIL — md5 identical to another paper's raw: $other" >&2
        return 1
      fi
    done
  done
  return 0
}

# gate_paper_signature <rawfile> <paper> -> 0 pass, 1 fail
# Each paper has signature tokens that MUST appear (any-of within required
# groups). If the expected paper's signature is ABSENT and another paper's
# signature is strongly present, this is a wrong-paper misfile. Token lists
# live in the case block below so they stay editable.
gate_paper_signature() {
  local f="$1" paper="$2"
  python3 - "$f" "$paper" <<'PY'
import sys, re
f, paper = sys.argv[1], sys.argv[2]
t = open(f, encoding="utf-8", errors="replace").read().lower()

def has(tok):
    return tok.lower() in t

# signature(paper) -> True if the paper's own signature is present.
# Each paper: a list of AND-groups; each group is an any-of list of tokens.
# 2026-07-15 fix (false positive on P1U M40): (a) P1U group-1 was the single
# literal "dark energy" — a genuine P1U review used other phrasings, failing
# the AND while its f_NL mention tripped P2's one-token signature. Broadened
# token lists. (b) partial_own(): if ANY own token appears at all, never rule
# WRONGPAPER — cross-paper mentions are common (P1U discusses f_NL; P4/P5
# both discuss chirality).
SIGS = {
    "P1U":     [["dark energy", "dark-energy", "no-go", "four-route", "vacuum energy", "cosmological constant"], ["fierz", "ech", "channel", "route"]],
    "P2":      [["f_nl", "-35/16", "in-in"], ["forecast", "fisher", "bispectrum", "non-gaussian"]],
    "P3":      [["anomaly"], ["neowise", "erosita", "lamost", "catalog"]],
    "P3APJS":  [["anomaly"], ["neowise", "erosita", "lamost", "catalog"]],
    "P4":      [["chirality"], ["galaxy zoo", "gz1", "spiral"]],
    "P5":      [["desi"], ["void"]],
}

def hit_count(p):
    groups = SIGS.get(p) or []
    return sum(t.count(tok.lower()) for grp in groups for tok in grp)

def sig_present(p):
    groups = SIGS.get(p)
    if not groups:
        return None  # unknown paper -> can't judge, don't block
    return all(any(has(tok) for tok in grp) for grp in groups)

own = sig_present(paper)
if own is None:
    print("UNKNOWN-PAPER"); sys.exit(0)

if own:
    print("OK"); sys.exit(0)

# own signature absent -> is another paper's signature strongly present?
# Count-based dominance (2026-07-15): rule WRONGPAPER only when the other
# paper's FULL signature is present AND its token hit-count clearly dominates
# the expected paper's (>=3x, or own==0). Incidental cross-mentions (P1U
# discussing f_NL; a P5 review saying "catalog") must not flip the ruling.
own_hits = hit_count(paper)
for other, groups in SIGS.items():
    if other == paper:
        continue
    # skip the twin (P3 <-> P3APJS share a signature)
    if {other, paper} == {"P3", "P3APJS"}:
        continue
    if all(any(has(tok) for tok in grp) for grp in groups):
        oh = hit_count(other)
        if own_hits == 0 or oh >= 3 * max(own_hits, 1):
            print("WRONGPAPER:%s" % other); sys.exit(0)

# own absent, no strong other -> ambiguous/weak, don't hard-fail on signature
print("WEAK")
PY
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
    # After reconnect, re-verify headed — NEVER harvest on a launched/headless
    # relaunch (login walls read as dead chats -> false FAILED-dead).
    assert_headed
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

# HEADED preflight BEFORE any harvest work (2026-07-13). This is the gate that
# would have prevented the M42 false-FAILED-dead sweep on a headless browser.
assert_headed

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
    # real verdict candidate -> save raw first, THEN run harvest-time gates
    # before any verdict is written to the manifest/matrix (directive I4).
    RAW="$OUTDIR/${PAPER}_${REVIEWER}_${ROUND}.md"
    PNG="$OUTDIR/${PAPER}_${REVIEWER}_${ROUND}.png"
    printf '%s\n' "$RESP" > "$RAW"

    GATE_FAIL=""
    if ! gate_substance "$RAW"; then
      GATE_FAIL="FAILED-stub"
    elif ! gate_duplicate "$RAW" "$PAPER" "$ROUND"; then
      GATE_FAIL="FAILED-duplicate"
    else
      SIG="$(gate_paper_signature "$RAW" "$PAPER")"
      case "$SIG" in
        WRONGPAPER:*)
          echo "    GATE paper-signature: FAIL — expected $PAPER signature absent, ${SIG#WRONGPAPER:} signature strongly present" >&2
          GATE_FAIL="FAILED-wrongpaper" ;;
        *) : ;;  # OK / WEAK / UNKNOWN-PAPER -> pass
      esac
    fi

    if [ -n "$GATE_FAIL" ]; then
      # a leg with no verifiable output is FAILED, not a verdict. Keep the raw
      # on disk for inspection; record NO verdict.
      update_manifest_status "$PAPER" "$REVIEWER" "$ROUND" "$URL" "$GATE_FAIL" ""
      echo "    $GATE_FAIL — raw kept at $RAW, NO verdict recorded"
      printf '%s\t%s\t%s\n' "$PAPER" "$REVIEWER" "$GATE_FAIL" >> "$MATRIX_FILE"
      continue
    fi

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
