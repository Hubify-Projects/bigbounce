#!/usr/bin/env bash
# loop_watchdog.sh — OS-level watchdog for the bigbounce drive-to-100 loop.
#
# ⚠️ DEPLOYMENT (2026-07-11): the launchd agent has NO ~/Desktop TCC grant, so it
# cannot read/exec a script that lives under ~/Desktop (getcwd + exec both EPERM).
# The plist therefore runs a DEPLOYED COPY at
#   ~/Library/Application Support/bigbounce/loop_watchdog.sh
# THIS repo file is the CANONICAL SOURCE. After editing it, re-deploy:
#   cp tools/loop_watchdog.sh "$HOME/Library/Application Support/bigbounce/loop_watchdog.sh"
# Authoritative runtime heartbeat + log live in that same App Support dir (the
# repo copies under project-context/ are best-effort human-visible mirrors only).
#
# THE PROBLEM this fixes: an in-session cron is SESSION-ONLY. It dies
# when the app closes, skips ticks while the session is busy, and expires after
# 7 days. When it silently died, Houston had to NOTICE the loop was down. That is
# unacceptable — the watchdog is the thing that notices, outside any agent, in
# launchd (~/Library/LaunchAgents/com.bigbounce.loopwatchdog.plist, every 15min).
#
# What it does each run:
#   - reads project-context/LOOP_HEARTBEAT.json (lastTickUTC)
#   - if the heartbeat is FRESH (<45min): log one PASS line, exit 0 (silent).
#   - if the heartbeat is STALE (>=45min), the loop is considered DOWN:
#       (a) macOS notification: "bigbounce loop DOWN — last tick <age>"
#       (b) POST a Convex activityFeed:add alert row so the live site shows it
#       (c) RECOVERY: launch ONE lease-free, read-only `codex exec` diagnostic.
#           It runs site_freshness_check read-only and reports pending raw harvests
#           without harvesting, adjudicating, editing, browsing, or writing state.
#       RECOVERY CAP: if a recovery ran <60min ago, only notify+alert (don't stack).
#       => a closed session gets ~hourly headless recovery ticks.
#   - every run logs exactly one line to project-context/LOOP_WATCHDOG_LOG.md.
#
# See canonical spec: ~/.claude/scistack/astrostack/bigbounce-r-round/SKILL.md
#   §"Loop watchdog".

set -uo pipefail

export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
REPO="/Users/houstongolden/Desktop/CODE_YOU/bigbounce"
# Authoritative runtime state lives in the launchd-owned dir (NOT the git tree):
# a launchd agent can CREATE files under ~/Desktop but EPERMs when overwriting an
# EXISTING git-tracked file (macOS App-Management/TCC). Repo paths are kept only
# as best-effort human-visible mirrors.
RUNTIME_DIR="$HOME/Library/Application Support/bigbounce"
HEARTBEAT_RUNTIME="$RUNTIME_DIR/LOOP_HEARTBEAT.json"
HEARTBEAT="$REPO/project-context/LOOP_HEARTBEAT.json"          # repo mirror
WATCHDOG_LOG_RUNTIME="$RUNTIME_DIR/LOOP_WATCHDOG_LOG.md"
WATCHDOG_LOG="$REPO/project-context/LOOP_WATCHDOG_LOG.md"      # repo mirror
CONVEX_MUTATION_URL="https://brilliant-panther-471.convex.cloud/api/mutation"
STALE_SECONDS=$((45 * 60))          # 45 minutes
RECOVERY_COOLDOWN_SECONDS=$((60 * 60))  # 60 minutes — a closed session gets ~hourly
                                         # headless recovery ticks (each writes the
                                         # heartbeat, runs the freshness gate, harvests
                                         # pending EXT rounds). Tightened from 2h
                                         # 2026-07-11 so the loop never idles >1h.
# marker file records the epoch of the last recovery launch (recovery cap)
RECOVERY_MARKER="/tmp/bigbounce_watchdog_last_recovery"
CODEX_ENABLED="${BIGBOUNCE_CODEX_SUBSCRIPTION_ENABLED:-1}"
CODEX_BIN="${BIGBOUNCE_CODEX_BIN:-$(command -v codex 2>/dev/null || { [ -x /opt/homebrew/bin/codex ] && printf '%s' /opt/homebrew/bin/codex; })}"
CODEX_MODEL="${BIGBOUNCE_CODEX_MODEL:-gpt-5.6-sol}"
CODEX_EFFORT="${BIGBOUNCE_CODEX_EFFORT:-high}"
CODEX_TIMEOUT_SECONDS="${BIGBOUNCE_WATCHDOG_CODEX_TIMEOUT_SECONDS:-900}"
TIMEOUT_BIN="$(command -v timeout 2>/dev/null || command -v gtimeout 2>/dev/null || true)"
MACHINE_ID="${BIGBOUNCE_MACHINE_ID:-$(hostname -s 2>/dev/null | tr -d '\n' | tr -c 'A-Za-z0-9._-' '-')}"

NOW_EPOCH="$(date -u +%s)"
NOW_ISO="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

case "$CODEX_ENABLED" in 0|1) ;; *) echo "FAIL: BIGBOUNCE_CODEX_SUBSCRIPTION_ENABLED must be 0 or 1" >&2; exit 1 ;; esac
case "$CODEX_EFFORT" in minimal|low|medium|high|xhigh|max|ultra) ;; *) echo "FAIL: BIGBOUNCE_CODEX_EFFORT must be minimal|low|medium|high|xhigh|max|ultra" >&2; exit 1 ;; esac
case "$CODEX_TIMEOUT_SECONDS" in ''|*[!0-9]*) echo "FAIL: BIGBOUNCE_WATCHDOG_CODEX_TIMEOUT_SECONDS must be a positive integer" >&2; exit 1 ;; 0) echo "FAIL: BIGBOUNCE_WATCHDOG_CODEX_TIMEOUT_SECONDS must be >0" >&2; exit 1 ;; esac

# True no-launch/no-state validation path: no mkdir, log append, notification,
# Convex mutation, marker write, heartbeat write, or agent session.
if [ "${BIGBOUNCE_WATCHDOG_DRY_RUN:-0}" = "1" ]; then
  LOGIN="unavailable"
  if [ -n "$CODEX_BIN" ]; then LOGIN="$(env -u OPENAI_API_KEY -u CODEX_API_KEY -u ANTHROPIC_API_KEY "$CODEX_BIN" login status 2>&1 || true)"; fi
  printf 'DRY_RUN codex_enabled=%s model=%s effort=%s sandbox=read-only timeout=%ss auth=%s no_state=1\n' \
    "$CODEX_ENABLED" "$CODEX_MODEL" "$CODEX_EFFORT" "$CODEX_TIMEOUT_SECONDS" "$LOGIN"
  exit 0
fi

mkdir -p "$RUNTIME_DIR" 2>/dev/null || true

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
log_line() {
  # Append one line to the AUTHORITATIVE runtime watchdog log (launchd-writable),
  # and best-effort mirror to the repo copy (may EPERM under launchd — non-fatal).
  local hdr='# Loop Watchdog Log\n\nOne line per watchdog run (launchd, ~15min). Recovery lines start with `RECOVERY`.\n\n'
  # Authoritative runtime log (launchd-writable). Subshell wraps the redirect so a
  # failed open never leaks an error to stderr (bash reports redirect-open errors
  # before an inline 2>/dev/null takes effect).
  ( [ -f "$WATCHDOG_LOG_RUNTIME" ] || printf "$hdr" > "$WATCHDOG_LOG_RUNTIME"
    printf '%s  %s\n' "$NOW_ISO" "$1" >> "$WATCHDOG_LOG_RUNTIME" ) 2>/dev/null || true
  # Best-effort repo mirror (EPERMs under launchd — no ~/Desktop grant; expected).
  ( [ -f "$WATCHDOG_LOG" ] || printf "$hdr" > "$WATCHDOG_LOG"
    printf '%s  %s\n' "$NOW_ISO" "$1" >> "$WATCHDOG_LOG" ) 2>/dev/null || true
}

# human-readable age string from a number of seconds
age_str() {
  local s="$1" m h
  if [ "$s" -lt 60 ]; then echo "${s}s"; return; fi
  m=$((s / 60)); h=$((m / 60))
  if [ "$h" -ge 1 ]; then echo "${h}h$((m % 60))m"; else echo "${m}m"; fi
}

# parse the FRESHEST lastTickUTC epoch across the runtime + repo heartbeats
# (runtime is authoritative; repo is a best-effort mirror that may be stale).
heartbeat_epoch() {
  python3 - "$HEARTBEAT_RUNTIME" "$HEARTBEAT" <<'PY' 2>/dev/null
import sys, json
from datetime import datetime, timezone
best = None
for path in sys.argv[1:]:
    try:
        s = json.load(open(path)).get("lastTickUTC", "").strip()
        if not s:
            continue
        if s.endswith("Z"):
            s = s[:-1] + "+00:00"
        dt = datetime.fromisoformat(s)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        e = int(dt.timestamp())
        if best is None or e > best:
            best = e
    except Exception:
        continue
print("" if best is None else best)
PY
}

notify() {
  # macOS user notification (best-effort; never fail the run on it)
  /usr/bin/osascript -e "display notification \"$1\" with title \"bigbounce watchdog\"" >/dev/null 2>&1 || true
}

convex_alert() {
  # POST an activityFeed:add alert row so the live site surfaces the outage.
  # Best-effort — a network failure must not abort the watchdog.
  local body_title="$1" body_text="$2"
  local payload
  payload="$(python3 - "$body_title" "$body_text" "$NOW_ISO" <<'PY' 2>/dev/null
import sys, json
title, body, iso = sys.argv[1], sys.argv[2], sys.argv[3]
print(json.dumps({
  "path": "activityFeed:add",
  "args": {
    "type": "alert",
    "date": iso,
    "title": title,
    "body": body,
    "tags": [
      {"label": "watchdog", "kind": "alert"},
      {"label": "loop-down", "kind": "alert"},
    ],
  },
  "format": "json",
}))
PY
)"
  [ -z "$payload" ] && return 0
  curl -sS -X POST "$CONVEX_MUTATION_URL" \
    -H "Content-Type: application/json" \
    -d "$payload" >/dev/null 2>&1 || true
}

recovery_last_epoch() {
  [ -f "$RECOVERY_MARKER" ] || { echo 0; return; }
  cat "$RECOVERY_MARKER" 2>/dev/null | tr -dc '0-9' || echo 0
}

atomic_write() {
  local path="$1" body="$2" dir tmp
  dir="$(dirname "$path")"
  tmp="$(mktemp "$dir/.heartbeat.XXXXXX")" || return 1
  if ! printf '%s\n' "$body" > "$tmp"; then rm -f "$tmp"; return 1; fi
  chmod 0644 "$tmp" 2>/dev/null || true
  mv -f "$tmp" "$path"
}

RECOVERY_PROMPT="You are the OS-level RECOVERY diagnostic for the bigbounce loop on machine $MACHINE_ID. This is ALWAYS LEASE-FREE and strictly READ-ONLY. Do not claim or renew the lab lease, drive a browser, launch reviews or compute, harvest raws, adjudicate findings, inspect secrets, edit any file, write heartbeat/verdict/ledger/Convex/review/site state, or commit/push anything. Do ONLY these steps, then stop:
1. Run tools/site_freshness_check.sh --report as a READ-ONLY diagnostic. Report stale surfaces; do not edit them.
2. Inspect submitted EXT manifests read-only and list submitted-but-unharvested round labels. Do not run ext_harvest.sh and do not open a browser.
3. Return one concise RECOVERY-DIAGNOSTIC status report in your final response.
The watchdog wrapper, not you, records runtime health only after a successful diagnostic. Do not start sweeps or open new work."

launch_recovery() {
  # Fire-and-forget read-only recovery diagnostic. The wrapper records only an
  # atomic runtime-health heartbeat after Codex exits successfully; the model is
  # sandboxed from every repo/review/Convex/browser write.
  [ "$CODEX_ENABLED" = 1 ] || return 1
  [ -n "$CODEX_BIN" ] || return 1
  [ -n "$TIMEOUT_BIN" ] || return 1
  CODEX_LOGIN="$(env -u OPENAI_API_KEY -u CODEX_API_KEY -u ANTHROPIC_API_KEY "$CODEX_BIN" login status 2>&1 || true)"
  printf '%s' "$CODEX_LOGIN" | grep -q 'Logged in using ChatGPT' || return 1
  echo "$NOW_EPOCH" > "$RECOVERY_MARKER"
  ( if printf '%s\n' "$RECOVERY_PROMPT" | env -u OPENAI_API_KEY -u CODEX_API_KEY -u ANTHROPIC_API_KEY \
      "$TIMEOUT_BIN" "$CODEX_TIMEOUT_SECONDS" "$CODEX_BIN" \
        --cd "$REPO" --sandbox read-only --ask-for-approval never \
        --model "$CODEX_MODEL" -c "model_reasoning_effort=\"$CODEX_EFFORT\"" \
        exec --ephemeral --ignore-user-config \
        --color never - >> /tmp/bigbounce_watchdog_recovery.log 2>&1; then
      RECOVERY_HB="$(python3 - "$MACHINE_ID" <<'PY'
import datetime, json, sys
print(json.dumps({
  "lastTickUTC": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
  "source": "watchdog-recovery",
  "machineId": sys.argv[1],
  "role": "lease-free",
  "note": "read-only Codex diagnostic completed; no science/review state written",
}))
PY
)"
      atomic_write "$HEARTBEAT_RUNTIME" "$RECOVERY_HB" 2>/dev/null || true
    fi
  ) &
  return 0
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
HB_EPOCH="$(heartbeat_epoch)"

if [ -z "$HB_EPOCH" ]; then
  # No parseable heartbeat at all — treat as DOWN.
  log_line "DOWN   heartbeat missing/unparseable — recovery requested"
  notify "bigbounce loop DOWN — no heartbeat"
  convex_alert "bigbounce loop DOWN" "Watchdog found no parseable LOOP_HEARTBEAT.json at $NOW_ISO. Launching recovery tick."
  REC_LAST="$(recovery_last_epoch)"
  if [ "$((NOW_EPOCH - REC_LAST))" -lt "$RECOVERY_COOLDOWN_SECONDS" ]; then
    log_line "RECOVERY skipped — last recovery <1h ago (notify-only)"
  else
    if launch_recovery; then
      log_line "RECOVERY launched (read-only Codex ChatGPT-subscription diagnostic)"
    else
      log_line "RECOVERY unavailable (Codex disabled, CLI missing, or ChatGPT login unavailable)"
    fi
  fi
  exit 0
fi

AGE=$((NOW_EPOCH - HB_EPOCH))
AGE_H="$(age_str "$AGE")"

if [ "$AGE" -lt "$STALE_SECONDS" ]; then
  # fresh — silent pass
  log_line "PASS   heartbeat fresh (age ${AGE_H})"
  exit 0
fi

# STALE — the loop is DOWN
notify "bigbounce loop DOWN — last tick ${AGE_H} ago"
convex_alert "bigbounce loop DOWN — last tick ${AGE_H} ago" \
  "The drive-to-100 loop heartbeat is ${AGE_H} old (threshold 45m) as of ${NOW_ISO}. The OS watchdog is attempting a recovery tick."

REC_LAST="$(recovery_last_epoch)"
if [ "$((NOW_EPOCH - REC_LAST))" -lt "$RECOVERY_COOLDOWN_SECONDS" ]; then
  REC_AGE="$(age_str $((NOW_EPOCH - REC_LAST)))"
  log_line "DOWN   heartbeat stale (age ${AGE_H}) — notified+alerted; recovery SKIPPED (last recovery ${REC_AGE} ago, <1h cap)"
else
  if launch_recovery; then
    log_line "DOWN   heartbeat stale (age ${AGE_H}) — notified+alerted; RECOVERY launched (read-only Codex diagnostic)"
  else
    log_line "DOWN   heartbeat stale (age ${AGE_H}) — notified+alerted; RECOVERY unavailable (Codex disabled/CLI/auth)"
  fi
fi
exit 0
