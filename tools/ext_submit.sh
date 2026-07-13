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

echo "=== ext_submit :: $PAPER $REVIEWER round=$ROUND ==="
echo "    pdf: $STAGE"

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
  # chip check: innerText match on the staged filename (or an attachment chip)
  local i chip=0 base; base="$(basename "$STAGE")"
  for i in 1 2 3 4 5 6; do
    bcall 45 js 'document.body.innerText.includes("'"$base"'") || !!document.querySelector("[class*=attachment],[class*=file-chip],[class*=preview]")' || true
    printf '%s' "$BOUT" | grep -qi true && { chip=1; break; }
    sleep 6
  done
  [ "$chip" = 1 ] || echo "    WARN grok chip not confirmed — continuing"
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
  # chip poll 6 x 6s
  local i chip=0 base; base="$(basename "$STAGE")"
  for i in 1 2 3 4 5 6; do
    bcall 45 js '!!document.querySelector("[class*=attachment],[class*=file],[data-testid*=attachment]") || document.body.innerText.includes("'"$base"'")' || true
    printf '%s' "$BOUT" | grep -qi true && { chip=1; break; }
    sleep 6
  done
  [ "$chip" = 1 ] || echo "    WARN chatgpt chip not confirmed — continuing"
  # type (ChatGPT #prompt-textarea — atomic insertText, verify ordered)
  type_prompt '#prompt-textarea' || die "chatgpt type failed: $BOUT"
  # JS-click send: testid first, aria fallback
  bcall 45 js '(function(){var b=document.querySelector("button[data-testid=send-button]");if(b){b.click();return "sent-testid"}var a=document.querySelector("button[aria-label*=Send i]");if(a){a.click();return "sent-aria"}return "no-send-btn"})()' || die "chatgpt send failed: $BOUT"
  echo "    chatgpt send: $BOUT"
  # ChatGPT redirects the project page to /c/<uuid> AFTER send completes —
  # capturing too early records the project URL and orphans the leg
  # (2026-07-11: two legs lost this way). Poll for the /c/ URL.
  SUBMIT_URL=""
  for _i in 1 2 3 4 5 6; do
    sleep 5
    bcall 45 url || true
    SUBMIT_URL="$(printf '%s' "$BOUT" | tr -d '\r' | tail -1)"
    case "$SUBMIT_URL" in */c/*) break ;; esac
  done
  case "$SUBMIT_URL" in
    */c/*) : ;;
    *) echo "    WARN: no /c/ redirect after 30s — URL may be the project page" ;;
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

case "$REVIEWER" in
  grok)    submit_grok ;;
  chatgpt) submit_chatgpt ;;
  gemini)  submit_gemini ;;
esac

# sanity on captured URL
case "${SUBMIT_URL:-}" in
  http*) ;;
  *) SUBMIT_URL="" ; echo "    WARN no http URL captured" ;;
esac

STATUS="submitted"
[ "$REVIEWER" = gemini ] && STATUS="submitted-verified"
append_manifest "$SUBMIT_URL" "$STATUS" ""
echo "OK: $PAPER $REVIEWER round=$ROUND status=$STATUS url=${SUBMIT_URL:-<none>}"
