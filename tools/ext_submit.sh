#!/usr/bin/env bash
# ext_submit.sh — submit ONE EXT (browser) referee leg for a bigbounce paper.
#
# One (paper, reviewer) submission per invocation. Uploads the paper PDF into the
# reviewer's project chat (fresh chat), pastes the canonical PRD-referee prompt,
# sends, captures the resulting chat URL, and appends a manifest row so a
# later ext_harvest.sh run can pick up the response even if this agent dies.
#
# Usage: tools/ext_submit.sh <P1U|P2|P3|P4|P5> <grok|chatgpt|gemini> <round-label> [pdf-path]
#
# Proven-recipe source (2026-07-10 H17 wave):
#   ~/.claude/scistack/astrostack/bigbounce-r-round/SKILL.md
#   project-context/peer-reviews/EXT_real/H17_2026-07-10/manifest.jsonl
#
# HARD RULES honored here:
#  - HEADED browser only (auto-recover via `$B connect` on "not connected").
#  - Fresh chat per leg (grok: project chat; chatgpt: project/project new; gemini u/1/app).
#  - Capture chat URL IMMEDIATELY after submit, BEFORE any polling (H16 lesson).
#  - Gemini: in-place send-verify loop, NEVER navigate away after send.

set -euo pipefail

REPO="/Users/houstongolden/Desktop/CODE_YOU/bigbounce"
B="$HOME/.claude/skills/gstack/browse/dist/browse"
ROUND_DIR_BASE="$REPO/project-context/peer-reviews/EXT_real/H17_2026-07-10"
MANIFEST="$ROUND_DIR_BASE/manifest.jsonl"

GROK_PROJECT="https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1"
CHATGPT_PROJECT="https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/project"
GEMINI_APP="https://gemini.google.com/u/1/app"

die() { echo "FAIL: $*" >&2; exit 1; }

# ---- HEADED-BROWSER PREFLIGHT (2026-07-13, permanent) -----------------------
# The gstack browse server silently regresses headed -> `Mode: launched`
# (chrome-headless-shell, temp profile, NO logins). On a launched/headless
# browser SUBMIT fails visibly, but HARVEST fails silently-WRONG: every chat
# renders a login/error wall and the dead-chat detector marks live legs
# FAILED-dead (all 6 M42 legs, 2026-07-13). assert_headed gates ALL browser
# work: require the literal `Mode: headed` line from `$B status` before any
# submit/harvest step, and NEVER proceed on `launched` (or anything else).
assert_headed() {
  local out mode
  out="$(timeout 30 "$B" status 2>&1 || true)"
  mode="$(printf '%s\n' "$out" | grep -iE '^Mode:' | head -1 | awk '{print $2}')"
  if [ "$mode" != "headed" ]; then
    echo "FAIL: browser not headed (Mode: ${mode:-unknown}) — run: $B cleanup; kill port 34567 holders; $B connect; verify Mode: headed" >&2
    exit 1
  fi
}

# ---- paper -> pdf map (mirrors tools/int_api_review_2026-07-08.py) ----
pdf_for_paper() {
  case "$1" in
    P1U) echo "arxiv/paper1_unified.pdf" ;;
    P2)  echo "research/focused_paper_source_integration/02_full_draft.pdf" ;;
    P3)  echo "pipelines/p3_anomaly_engine/paper3_draft.pdf" ;;
    P4)  echo "pipelines/p2_chirality/chirality_catalog_paper.pdf" ;;
    P5)  echo "pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf" ;;
    P3APJS) echo "pipelines/p3_anomaly_engine/paper3_apjs.pdf" ;;
    *)   echo "" ;;
  esac
}

# ---- canonical PRD-referee prompt (exact text used by the working H17 legs) ----
PROMPT='You are an expert referee for Physical Review D. Review this manuscript to the standard of a real submission. Respond with exactly: (1) VERDICT: ACCEPT / MINOR REVISIONS / MAJOR REVISIONS / REJECT. (2) ISSUES: numbered, each prefixed [MAJOR] or [MINOR], naming the specific section/claim and concrete problem. (3) One sentence: is the central claim supported?'

# ---- browse wrapper: run a browse call with timeout + one auto-recover retry ----
# usage: bcall <timeout-secs> <browse-args...>   (stdout captured, returns exit)
BOUT=""
bcall() {
  local to="$1"; shift
  local out rc
  out="$(timeout "$to" "$B" "$@" 2>&1)" && { BOUT="$out"; return 0; }
  rc=$?
  if printf '%s' "$out" | grep -qiE "Run '/open-gstack-browser'|not connected"; then
    echo "    [auto-recover] browser not connected — reconnecting headed" >&2
    timeout 90 "$B" connect >/dev/null 2>&1 || true
    # After reconnect, re-verify headed — NEVER proceed on a launched/headless
    # relaunch (the exact regression assert_headed exists to catch).
    assert_headed
    out="$(timeout "$to" "$B" "$@" 2>&1)" && { BOUT="$out"; return 0; }
    rc=$?
  fi
  BOUT="$out"
  return $rc
}

# ---- type helper. `type` fires keystrokes that (a) HANG on a post-type settle
# wait, and worse (b) land OUT OF ORDER in ProseMirror/tiptap while the editor is
# still hydrating (observed: 343/386 chars, scrambled). Instead set the prompt
# ATOMICALLY: focus the composer, select-all, then execCommand("insertText").
# This is ordered, single-shot, and works for both contenteditable (Grok tiptap)
# and textarea (ChatGPT #prompt-textarea). Verify head+tail before returning.
# usage: type_prompt <single-composer-selector>
composer_has_prompt() {   # 0 if composer holds prompt head AND tail, in order
  local sel="$1"
  bcall 20 js '(function(){var t=document.querySelector("'"$sel"'");var v=t?(t.innerText||t.value||""):"";var ok=v.indexOf("You are an expert referee")===0 && v.includes("central claim supported");return ok?"FULL":("BAD len="+v.length+" head="+JSON.stringify(v.slice(0,25)))})()' || true
  printf '%s' "$BOUT" | grep -q FULL
}
type_prompt() {
  local sel="$1"
  local pjson; pjson="$(python3 -c 'import json,sys;print(json.dumps(sys.argv[1]))' "$PROMPT")"
  # atomic set via execCommand insertText after select-all
  bcall 30 js '(function(){var t=document.querySelector("'"$sel"'");if(!t)return "no-composer";t.focus();var s=window.getSelection();if(t.value!==undefined){t.select();document.execCommand("insertText",false,'"$pjson"');}else{s.selectAllChildren(t);document.execCommand("insertText",false,'"$pjson"');}t.dispatchEvent(new InputEvent("input",{bubbles:true}));return "set len="+((t.innerText||t.value||"").length)})()' || true
  echo "    [insertText] $BOUT"
  if composer_has_prompt "$sel"; then return 0; fi
  # fallback: keystroke type, then verify ordered content
  bcall 20 js '(function(){var t=document.querySelector("'"$sel"'");if(!t)return;t.focus();if(t.value!==undefined){t.value="";}else{t.innerHTML="<p></p>";}t.dispatchEvent(new InputEvent("input",{bubbles:true}));})()' || true
  bcall 60 type "$PROMPT" || true
  if composer_has_prompt "$sel"; then echo "    [type-fallback] prompt set via keystrokes"; return 0; fi
  echo "    type_prompt FAILED — composer state: $BOUT"
  return 1
}

# ---- args ----
[ $# -ge 3 ] || die "usage: tools/ext_submit.sh <P1U|P2|P3|P4|P5|P3APJS> <grok|chatgpt|gemini> <round-label> [pdf-path]"
PAPER="$1"; REVIEWER="$2"; ROUND="$3"; PDF_ARG="${4:-}"

case "$PAPER" in P1U|P2|P3|P4|P5|P3APJS) ;; *) die "unknown paper '$PAPER'" ;; esac

# P3APJS = the ApJS venue variant (review-of-record for P3): same science,
# ApJS-framed referee prompt. Head/tail sentinels unchanged so
# composer_has_prompt verification still holds.
if [ "$PAPER" = "P3APJS" ]; then
  PROMPT="${PROMPT/Physical Review D/The Astrophysical Journal Supplement Series (ApJS)}"
fi
case "$REVIEWER" in grok|chatgpt|gemini) ;; *) die "unknown reviewer '$REVIEWER'" ;; esac

if [ -n "$PDF_ARG" ]; then
  SRC_PDF="$PDF_ARG"
else
  REL="$(pdf_for_paper "$PAPER")"; [ -n "$REL" ] || die "no pdf map for $PAPER"
  SRC_PDF="$REPO/$REL"
fi
[ -f "$SRC_PDF" ] || die "pdf not found: $SRC_PDF"

# ---- stage to /tmp with the round label; gs-compress if >8MB ----
STAGE="/tmp/ext_${PAPER}_${ROUND}.pdf"
SZ="$(stat -f%z "$SRC_PDF")"
if [ "$SZ" -gt 8388608 ]; then
  echo "    pdf ${SZ}B >8MB — gs-compressing to $STAGE"
  if command -v gs >/dev/null 2>&1; then
    gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/ebook \
       -dNOPAUSE -dQUIET -dBATCH -sOutputFile="$STAGE" "$SRC_PDF" \
       || { cp -f "$SRC_PDF" "$STAGE"; echo "    WARN gs failed — using raw"; }
    NEWSZ="$(stat -f%z "$STAGE")"
    echo "    compressed -> ${NEWSZ}B"
  else
    cp -f "$SRC_PDF" "$STAGE"; echo "    WARN no gs — using raw"
  fi
else
  cp -f "$SRC_PDF" "$STAGE"
fi

mkdir -p "$ROUND_DIR_BASE"

# ---- manifest append helper (single JSON line) ----
append_manifest() {
  python3 - "$MANIFEST" "$PAPER" "$REVIEWER" "$ROUND" "$1" "$2" "$3" <<'PY'
import sys, json, datetime
manifest, paper, reviewer, rnd, url, status, note = sys.argv[1:8]
row = {"paper": paper, "reviewer": reviewer, "round": rnd,
       "status": status, "ts": datetime.datetime.now().astimezone().isoformat(timespec="seconds")}
if url: row["url"] = url
if note: row["note"] = note
with open(manifest, "a") as f:
    f.write(json.dumps(row) + "\n")
PY
}

# HEADED preflight BEFORE any submission work (2026-07-13).
assert_headed

echo "=== ext_submit :: $PAPER $REVIEWER round=$ROUND ==="
echo "    pdf: $STAGE"

# Initialized so the post-dispatch `${SUBMIT_URL:-}` sanity block is robust even
# if a submit_* function returned (via `|| true`) before assigning it.
SUBMIT_URL=""

# =====================================================================
# GROK
# =====================================================================
submit_grok() {
  # Expert is the session default in this project; clicking the Expert button
  # opens a menu that STEALS composer focus and makes the subsequent type step
  # time out. So: NEVER click Expert — only VERIFY the mode label reads Expert.
  bcall 45 goto "$GROK_PROJECT" || die "grok goto failed: $BOUT"
  sleep 6
  # upload into the file input
  bcall 90 upload 'input[type="file"]' "$STAGE" || die "grok upload failed: $BOUT"
  sleep 8
  # FILENAME-VERIFIED chip check (2026-07-13 M32/M34 parity fix): require a
  # composer-area attachment chip whose visible text contains this leg's exact
  # round token "ext_${PAPER}_${ROUND}" — not merely that SOME chip exists.
  # Same wrong-PDF-attach failure class the chatgpt flow just closed; enforce it
  # here too. On mismatch/absence after ~30s: clear wrong chip(s), re-upload
  # once, re-verify; if still unmatched, DIE — never send an unverified file.
  local base token; base="$(basename "$STAGE")"; token="ext_${PAPER}_${ROUND}"
  local i chipok=0
  for i in 1 2 3 4 5 6; do
    bcall 45 js '(function(){var tok="'"$token"'";
      var scope=document.querySelector("form")||document.body;
      var chips=[].slice.call(scope.querySelectorAll("[class*=attachment],[class*=file-chip],[class*=file],[class*=preview],[class*=chip]"));
      var names=chips.map(function(c){return (c.innerText||c.getAttribute("title")||c.getAttribute("aria-label")||"")});
      var match=names.some(function(n){return n.indexOf(tok)!==-1});
      return match?"MATCH":(chips.length?("MISMATCH names="+JSON.stringify(names.slice(0,4))):"NONE")})()' || true
    printf '%s' "$BOUT" | grep -q MATCH && { chipok=1; break; }
    echo "    grok chip poll $i: $BOUT"
    sleep 6
  done
  if [ "$chipok" != 1 ]; then
    echo "    grok chip: expected token '$token' not found — clearing wrong attachment(s) + re-upload"
    bcall 30 js '(function(){var scope=document.querySelector("form")||document.body;
      var btns=[].slice.call(scope.querySelectorAll("button[aria-label*=Remove i],button[aria-label*=Delete i],button[title*=Remove i],[data-testid*=remove],[class*=remove] button,button[class*=remove]"));
      btns.forEach(function(b){try{b.click()}catch(e){}});return "removed="+btns.length})()' || true
    sleep 3
    bcall 90 upload 'input[type="file"]' "$STAGE" || die "grok re-upload failed: $BOUT"
    for i in 1 2 3 4 5; do
      sleep 6
      bcall 45 js '(function(){var tok="'"$token"'";
        var scope=document.querySelector("form")||document.body;
        var chips=[].slice.call(scope.querySelectorAll("[class*=attachment],[class*=file-chip],[class*=file],[class*=preview],[class*=chip]"));
        return chips.map(function(c){return (c.innerText||c.getAttribute("title")||c.getAttribute("aria-label")||"")}).some(function(n){return n.indexOf(tok)!==-1})?"MATCH":"NOMATCH"})()' || true
      printf '%s' "$BOUT" | grep -q MATCH && { chipok=1; break; }
    done
  fi
  [ "$chipok" = 1 ] || die "grok wrong/missing attachment (expected ${token}.pdf) — never send with an unverified attachment"
  # VERIFY Expert mode is active (read-only) — do NOT click. Just confirm a
  # button's innerText includes Expert (mode label present in the composer bar).
  bcall 45 js '(function(){var b=[...document.querySelectorAll("button,[role=button]")].find(function(e){return /Expert/i.test(e.textContent||e.getAttribute("aria-label")||"")});return b?"expert-present":"expert-not-visible"})()' || true
  echo "    grok mode(verify-only): $BOUT"
  # type the prompt (Grok tiptap/ProseMirror — atomic insertText, verify ordered)
  type_prompt '.tiptap.ProseMirror' || die "grok type failed: $BOUT"
  sleep 2
  # JS-click submit/send (aria)
  bcall 45 js '(function(){var b=document.querySelector("button[aria-label*=Submit i],button[aria-label*=Send i],button[type=submit]");if(b){b.click();return "sent"}var f=[...document.querySelectorAll("button")].find(function(e){return /submit|send/i.test(e.getAttribute("aria-label")||"")});if(f){f.click();return "sent-fallback"}return "no-send-btn"})()' || die "grok send failed: $BOUT"
  echo "    grok send: $BOUT"
  sleep 8
  bcall 45 url || true
  SUBMIT_URL="$(printf '%s' "$BOUT" | tr -d '\r' | tail -1)"
}

# =====================================================================
# CHATGPT
# =====================================================================
submit_chatgpt() {
  # Unique per-round input id so `upload` NEVER matches multiple elements
  # (the old bare 'input[type=file]' fallback errored "matched multiple").
  local INPID="extUpload_${PAPER}_${ROUND}"
  bcall 45 goto "$CHATGPT_PROJECT" || die "chatgpt goto failed: $BOUT"
  sleep 10
  # JS-tag the first file input with the unique id. If NO-INPUT, the page may
  # not have hydrated yet — sleep 5 and retry the goto+tag ONCE.
  bcall 45 js '(function(){var f=document.querySelector("input[type=file]");if(f){f.id="'"$INPID"'";return "tagged"}return "NO-INPUT"})()' || true
  echo "    chatgpt tag: $BOUT"
  if printf '%s' "$BOUT" | grep -q NO-INPUT; then
    echo "    chatgpt file-input not hydrated — retry goto+tag once"
    sleep 5
    bcall 45 goto "$CHATGPT_PROJECT" || die "chatgpt goto(retry) failed: $BOUT"
    sleep 8
    bcall 45 js '(function(){var f=document.querySelector("input[type=file]");if(f){f.id="'"$INPID"'";return "tagged"}return "NO-INPUT"})()' || true
    echo "    chatgpt tag(retry): $BOUT"
    printf '%s' "$BOUT" | grep -q NO-INPUT && die "chatgpt file input never appeared"
  fi
  # Upload ONLY via the unique id — never a bare multi-match selector.
  bcall 90 upload "#$INPID" "$STAGE" || die "chatgpt upload failed: $BOUT"
  # FILENAME-VERIFIED chip poll (2026-07-13 M32/M34 wrong-PDF-attach fix):
  # Twice a chatgpt leg following another chatgpt leg in a chain uploaded the
  # WRONG pdf — a stale attachment chip from the prior leg was grabbed and the
  # harvested raw reviewed a DIFFERENT paper (byte-identical P1U raw once, a
  # P5-signature review once). The old poll only confirmed that SOME chip
  # existed — never that its filename matched THIS leg's staged file. Now we
  # require a composer-area attachment chip whose visible text contains the
  # exact round token "ext_${PAPER}_${ROUND}" (== basename minus .pdf). Query
  # the DOM chip text in the composer/form region, not the whole body (a prior
  # message could echo the filename). If not present after ~30s, try to remove
  # any wrong attachment; if a wrong/absent state persists, DIE — never send an
  # unverified attachment.
  local base token; base="$(basename "$STAGE")"; token="ext_${PAPER}_${ROUND}"
  local i chipok=0
  for i in 1 2 3 4 5 6; do
    bcall 45 js '(function(){var tok="'"$token"'";
      var scope=document.querySelector("form")||document.querySelector("[data-testid=composer],[class*=composer]")||document.body;
      var chips=[].slice.call(scope.querySelectorAll("[class*=attachment],[class*=file],[data-testid*=attachment],[class*=chip],[class*=preview]"));
      var names=chips.map(function(c){return (c.innerText||c.getAttribute("title")||c.getAttribute("aria-label")||"")});
      var match=names.some(function(n){return n.indexOf(tok)!==-1});
      var any=chips.length>0;
      return match?"MATCH":(any?("MISMATCH names="+JSON.stringify(names.slice(0,4))):"NONE")})()' || true
    printf '%s' "$BOUT" | grep -q MATCH && { chipok=1; break; }
    echo "    chatgpt chip poll $i: $BOUT"
    sleep 6
  done
  if [ "$chipok" != 1 ]; then
    echo "    chatgpt chip: expected token '$token' not found — attempting to clear wrong attachment(s)"
    # Best-effort: click any chip remove/X button in the composer scope.
    bcall 30 js '(function(){var scope=document.querySelector("form")||document.body;
      var btns=[].slice.call(scope.querySelectorAll("button[aria-label*=Remove i],button[aria-label*=Delete i],button[title*=Remove i],[data-testid*=remove],[class*=remove] button,button[class*=remove]"));
      btns.forEach(function(b){try{b.click()}catch(e){}});return "removed="+btns.length})()' || true
    echo "    chatgpt chip clear: $BOUT"
    sleep 3
    # Re-upload the correct file once and re-verify.
    bcall 45 js '(function(){var f=document.querySelector("input[type=file]");if(f){f.id="'"$INPID"'";return "retagged"}return "NO-INPUT"})()' || true
    bcall 90 upload "#$INPID" "$STAGE" || die "chatgpt re-upload failed: $BOUT"
    for i in 1 2 3 4 5; do
      sleep 6
      bcall 45 js '(function(){var tok="'"$token"'";
        var scope=document.querySelector("form")||document.body;
        var chips=[].slice.call(scope.querySelectorAll("[class*=attachment],[class*=file],[data-testid*=attachment],[class*=chip],[class*=preview]"));
        var names=chips.map(function(c){return (c.innerText||c.getAttribute("title")||c.getAttribute("aria-label")||"")});
        return names.some(function(n){return n.indexOf(tok)!==-1})?"MATCH":"NOMATCH"})()' || true
      printf '%s' "$BOUT" | grep -q MATCH && { chipok=1; break; }
    done
  fi
  [ "$chipok" = 1 ] || die "wrong/missing attachment (expected ${token}.pdf) — never send with an unverified attachment"
  # type (ChatGPT #prompt-textarea — atomic insertText, verify ordered)
  # Guard (2026-07-13 M25 lesson): record the tab URL BEFORE send. If the
  # fresh-chat navigation silently failed, the tab still shows the PREVIOUS
  # leg's /c/ chat — the poll below would accept that stale URL instantly and
  # record the wrong chat (observed: P5+P2 M25 chatgpt legs both recorded the
  # P4 M24 chat URL). A post-send /c/ URL must DIFFER from the pre-send one.
  bcall 30 url || true
  PRE_URL="$(printf '%s' "$BOUT" | tr -d '\r' | tail -1)"
  type_prompt '#prompt-textarea' || die "chatgpt type failed: $BOUT"
  # JS-click send: testid first, aria fallback
  bcall 45 js '(function(){var b=document.querySelector("button[data-testid=send-button]");if(b){b.click();return "sent-testid"}var a=document.querySelector("button[aria-label*=Send i]");if(a){a.click();return "sent-aria"}return "no-send-btn"})()' || die "chatgpt send failed: $BOUT"
  echo "    chatgpt send: $BOUT"
  # ChatGPT redirects the project page to /c/<uuid> AFTER send completes —
  # capturing too early records the project URL and orphans the leg
  # (2026-07-11: two legs lost this way). Poll for the /c/ URL.
  # 2026-07-13 (M26/M27 lesson): project->chat redirects now regularly take
  # longer than the old ~30s window, so real completed reviews were dying
  # "FAILED" while landing server-side as orphaned chats. Extend the poll to
  # 24x5s (~120s), keeping the stale-URL guard (accept only a /c/ URL that
  # DIFFERS from PRE_URL). If the poll still yields no new /c/ URL, fall back
  # to the project sidebar: find a chat created in the last ~3 min whose first
  # user message starts with the referee prompt and adopt THAT chat's URL
  # instead of dying.
  SUBMIT_URL=""
  for _i in $(seq 1 24); do
    sleep 5
    bcall 45 url || true
    SUBMIT_URL="$(printf '%s' "$BOUT" | tr -d '\r' | tail -1)"
    case "$SUBMIT_URL" in
      */c/*) [ "$SUBMIT_URL" != "$PRE_URL" ] && break ;;
    esac
    SUBMIT_URL=""
  done
  case "$SUBMIT_URL" in
    */c/*)
      [ "$SUBMIT_URL" = "$PRE_URL" ] && die "chatgpt URL capture returned the pre-send chat URL (stale tab) — leg NOT confirmed, treat as FAILED"
      ;;
    *)
      # Fallback: no new /c/ URL after ~120s. The redirect may simply be slow
      # or the tab never navigated even though the chat was created server-side.
      # Snapshot the project sidebar for a recently-created chat whose first
      # user message starts with the referee prompt and adopt its URL.
      echo "    WARN: no /c/ redirect after ~120s — trying project sidebar fallback"
      local RECOVER=""
      # Collect candidate recent chat hrefs from the sidebar (newest first).
      bcall 45 js '(function(){var seen={},out=[];[].slice.call(document.querySelectorAll("nav a[href*=\"/c/\"],a[href*=\"/c/\"]")).forEach(function(a){var h=a.getAttribute("href")||"";var m=h.match(/\/c\/[0-9a-f-]+/);if(m&&!seen[m[0]]){seen[m[0]]=1;out.push(m[0])}});return out.slice(0,8).join(",")})()' || true
      local CANDS; CANDS="$(printf '%s' "$BOUT" | tr -d '\r' | tail -1)"
      local origin; origin="$(printf '%s' "$PRE_URL" | sed -E 's#^(https?://[^/]+).*#\1#')"
      [ -n "$origin" ] || origin="https://chatgpt.com"
      local cand
      for cand in $(printf '%s' "$CANDS" | tr ',' ' '); do
        case "$cand" in /c/*) : ;; *) continue ;; esac
        local curl="$origin$cand"
        # Skip the pre-send chat outright.
        [ "$curl" = "$PRE_URL" ] && continue
        bcall 45 goto "$curl" || continue
        sleep 4
        # First user message text: first article/message-author=user block.
        bcall 45 js '(function(){var el=document.querySelector("[data-message-author-role=user]");if(!el){var a=document.querySelector("article,[data-testid^=conversation-turn]");el=a}var t=(el&&el.innerText||"").trim();return t.slice(0,120)})()' || true
        local FIRST; FIRST="$(printf '%s' "$BOUT" | tr -d '\r')"
        case "$FIRST" in
          "You are an expert referee"*)
            RECOVER="$curl"; break ;;
        esac
      done
      if [ -n "$RECOVER" ]; then
        SUBMIT_URL="$RECOVER"
        echo "    RECOVERED chatgpt leg from sidebar fallback: $SUBMIT_URL"
      elif [ -n "$PRE_URL" ] && case "$PRE_URL" in */c/*) true ;; *) false ;; esac; then
        die "chatgpt: no NEW /c/ redirect after ~120s, sidebar fallback found no matching recent chat, and tab was on a prior chat ($PRE_URL) — leg NOT confirmed, treat as FAILED"
      else
        echo "    WARN: no /c/ redirect after ~120s and no sidebar match — URL may be the project page"
      fi ;;
  esac
}

# =====================================================================
# GEMINI  (native macOS file dialog; in-place send-verify; NEVER navigate)
# =====================================================================
submit_gemini() {
  bcall 45 goto "$GEMINI_APP" || die "gemini goto failed: $BOUT"
  bcall 45 wait --networkidle || true
  # open "Upload & tools" then "Upload files"
  bcall 45 js '(function(){var b=[...document.querySelectorAll("button,[role=button]")].find(function(e){return /Upload.*tools|Upload files|add files/i.test(e.getAttribute("aria-label")||e.textContent||"")});if(b){b.click();return "opened-uploadmenu"}return "no-upload-btn"})()' || true
  echo "    gemini uploadmenu: $BOUT"
  sleep 2
  bcall 45 js '(function(){var b=[...document.querySelectorAll("button,[role=menuitem],[role=option],span,div")].find(function(e){return /^\s*Upload files\s*$/i.test(e.textContent||"")});if(b){b.click();return "clicked-upload-files"}return "no-upload-files-leaf"})()' || true
  echo "    gemini leaf: $BOUT"
  sleep 2
  # native macOS open-dialog: Cmd+Shift+G, type path, return, return
  osascript <<OSA || echo "    WARN osascript dialog failed"
tell application "System Events"
  keystroke "g" using {command down, shift down}
  delay 0.6
  keystroke "$STAGE"
  delay 0.6
  key code 36
  delay 0.6
  key code 36
end tell
OSA
  # chip wait up to 30s
  local i chip=0
  for i in 1 2 3 4 5; do
    sleep 6
    bcall 45 js '!!document.querySelector("[class*=attachment],[class*=file-preview],[class*=uploaded]") || document.body.innerText.includes("'"$(basename "$STAGE")"'")' || true
    printf '%s' "$BOUT" | grep -qi true && { chip=1; break; }
  done
  [ "$chip" = 1 ] || echo "    WARN gemini chip not confirmed — continuing"
  # type
  bcall 45 js 'var t=document.querySelector("[contenteditable=true],textarea,rich-textarea");if(t){t.focus();}' || true
  bcall 45 type "$PROMPT" || die "gemini type failed: $BOUT"
  # capture the chat URL NOW (before send) so a drop still leaves a harvestable id
  bcall 45 url || true
  SUBMIT_URL="$(printf '%s' "$BOUT" | tr -d '\r' | tail -1)"
  # JS-click send
  bcall 45 js '(function(){var b=document.querySelector("button[aria-label*=Send i],button[mattooltip*=Send i]");if(b&&!b.disabled){b.click();return "sent"}var f=[...document.querySelectorAll("button")].find(function(e){return /send/i.test(e.getAttribute("aria-label")||"")&&!e.disabled});if(f){f.click();return "sent-fallback"}return "no-send-btn"})()' || die "gemini send failed: $BOUT"
  echo "    gemini send: $BOUT"
  # IN-PLACE send-verify loop 3 x 30s: composer emptied AND a user-query exists.
  # NEVER navigate away.
  local verified=0
  for i in 1 2 3; do
    sleep 30
    bcall 45 js '(function(){var c=document.querySelector("[contenteditable=true],textarea,rich-textarea");var empty=!c||!(c.innerText||c.value||"").trim();var uq=document.querySelectorAll("user-query,[class*=user-query],[data-test-id*=user]").length>0;return (empty&&uq)?"VERIFIED":("empty="+empty+" uq="+uq)})()' || true
    if printf '%s' "$BOUT" | grep -q VERIFIED; then verified=1; break; fi
    echo "    gemini verify attempt $i: $BOUT"
  done
  # refresh URL after send (may have minted a chat id)
  bcall 45 url || true
  local u2; u2="$(printf '%s' "$BOUT" | tr -d '\r' | tail -1)"
  case "$u2" in http*) SUBMIT_URL="$u2" ;; esac
  if [ "$verified" != 1 ]; then
    append_manifest "$SUBMIT_URL" "DROPPED" "in-place send-verify failed (upload-throttle?); retry next cycle fresh session"
    die "gemini send NOT verified in place — recorded DROPPED"
  fi
}

# Dispatch the submit function.
#
# CRITICAL (2026-07-13 silent-exit fix): a submit_* function signals a REAL
# failure EXCLUSIVELY by calling die() (explicit non-zero exit + "FAIL:" line).
# Any *return* from the function means "reached the end" — but its incidental
# last-command status can be non-zero (e.g. the success arm's
# `[ "$SUBMIT_URL" = "$PRE_URL" ] && die` short-circuits to rc 1 on the normal
# path, or a fallback `case ... esac` returns 1). Because the dispatch below is
# a top-level statement, that leaked non-zero status made `set -euo pipefail`
# abort the script HERE — silently, BEFORE the manifest-append + OK/FAIL block
# ran. Observed: chatgpt legs printed "chatgpt send: sent-testid" then vanished
# with no poll WARN, no manifest row, no OK, no FAIL. The 02d68a8f patch made
# this reachable on the ordinary success path.
#
# Fix: run the dispatch guarded so a benign trailing status can NEVER trip
# set -e. A genuine failure still `die`s inside the function (subshell inherits
# nothing to swallow the exit — die() calls `exit`, which terminates the whole
# script regardless). This guarantees the flow ALWAYS terminates in exactly one
# of: (a) die -> "FAIL:" + non-zero exit; (b) the OK + manifest block below.
case "$REVIEWER" in
  grok)    submit_grok ;;
  chatgpt) submit_chatgpt ;;
  gemini)  submit_gemini ;;
esac || true

# sanity on captured URL — an OK row without a harvestable URL is a lie
# (2026-07-14: P1U M35 chatgpt recorded OK url=<none>, unharvestable).
case "${SUBMIT_URL:-}" in
  http*) ;;
  *) die "no http URL captured after submit — leg NOT confirmed (message may have landed; recover via project sidebar)" ;;
esac

STATUS="submitted"
[ "$REVIEWER" = gemini ] && STATUS="submitted-verified"
append_manifest "$SUBMIT_URL" "$STATUS" ""
echo "OK: $PAPER $REVIEWER round=$ROUND status=$STATUS url=${SUBMIT_URL:-<none>}"
