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
# THE PROBLEM this fixes: Claude Code's in-session cron is SESSION-ONLY. It dies
# when the app closes, skips ticks while the session is busy, and expires after
# 7 days. When it silently died, Houston had to NOTICE the loop was down. That is
# unacceptable — the watchdog is the thing that notices, outside Claude, in
# launchd (~/Library/LaunchAgents/com.bigbounce.loopwatchdog.plist, every 15min).
#
# What it does each run:
#   - reads project-context/LOOP_HEARTBEAT.json (lastTickUTC)
#   - if the heartbeat is FRESH (<45min): log one PASS line, exit 0 (silent).
#   - if the heartbeat is STALE (>=45min), the loop is considered DOWN:
#       (a) macOS notification: "bigbounce loop DOWN — last tick <age>"
#       (b) POST a Convex activityFeed:add alert row so the live site shows it
#       (c) RECOVERY: launch ONE lease-free headless `claude -p` tick that writes
#           a machine-attributed heartbeat, runs site_freshness_check read-only,
#           harvests submitted-unharvested EXT raws (no verdict/adjudication), and
#           appends a status line to LOOP_WATCHDOG_LOG.md.
#       RECOVERY CAP: if a recovery ran <60min ago, only notify+alert (don't stack).
#       => a closed session gets ~hourly headless recovery ticks.
#   - every run logs exactly one line to project-context/LOOP_WATCHDOG_LOG.md.
#
# See canonical spec: ~/.claude/scistack/astrostack/bigbounce-r-round/SKILL.md
#   §"Loop watchdog".

set -uo pipefail

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
REPO="/Users/houstongolden/Desktop/CODE_YOU/bigbounce"
# Authoritative runtime state lives in the launchd-owned dir (NOT the git tree):
# a launchd agent can CREATE files under ~/Desktop but EPERMs when overwriting an
# EXISTING git-tracked file (macOS App-Management/TCC). Repo paths are kept only
# as best-effort human-visible mirrors.
RUNTIME_DIR="$HOME/Library/Application Support/bigbounce"
mkdir -p "$RUNTIME_DIR" 2>/dev/null || true
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
CLAUDE_BIN="$(command -v claude || echo "$HOME/.claude/local/claude")"
MACHINE_ID="${BIGBOUNCE_MACHINE_ID:-$(hostname -s 2>/dev/null | tr -d '\n' | tr -c 'A-Za-z0-9._-' '-')}"

NOW_EPOCH="$(date -u +%s)"
NOW_ISO="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

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

RECOVERY_PROMPT="You are the OS-level RECOVERY tick for the bigbounce loop on machine $MACHINE_ID. This is ALWAYS LEASE-FREE recovery: do not claim or renew the lab lease, drive a browser, adjudicate findings, write verdict/ledger/Convex review state, or commit/push review/site changes. Do ONLY these steps, then stop:
1. Write a fresh heartbeat to the AUTHORITATIVE runtime path \"$HOME/Library/Application Support/bigbounce/LOOP_HEARTBEAT.json\" AND best-effort to project-context/LOOP_HEARTBEAT.json with body {\"lastTickUTC\":\"<current UTC ISO8601>\",\"source\":\"watchdog-recovery\",\"machineId\":\"$MACHINE_ID\",\"role\":\"lease-free\",\"note\":\"recovery tick\"}. Repo-write EPERM is expected; runtime is authoritative.
2. Run tools/site_freshness_check.sh --report as a READ-ONLY diagnostic. Report stale surfaces; do not edit them in recovery mode.
3. For submitted-but-unharvested EXT manifests, run tools/ext_harvest.sh <round-label> only to save raw text/screenshots. Do not truth-audit or record any verdict.
4. Append one RECOVERY-TICK status line to project-context/LOOP_WATCHDOG_LOG.md summarizing heartbeat, diagnostics, and raw harvests (best effort; no commit).
Do not start sweeps, open new work, edit paper/site state, commit, or push. Recovery only."

launch_recovery() {
  # fire-and-forget headless recovery tick; the tick itself writes the heartbeat
  # + appends its own RECOVERY-TICK line to the log.
  echo "$NOW_EPOCH" > "$RECOVERY_MARKER"
  ( unset ANTHROPIC_API_KEY
    "$CLAUDE_BIN" -p "$RECOVERY_PROMPT" \
      --model claude-opus-4-8 \
      --dangerously-skip-permissions \
      --add-dir "$REPO" \
      >> /tmp/bigbounce_watchdog_recovery.log 2>&1
  ) &
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
HB_EPOCH="$(heartbeat_epoch)"

if [ -z "$HB_EPOCH" ]; then
  # No parseable heartbeat at all — treat as DOWN.
  log_line "DOWN   heartbeat missing/unparseable — launching recovery"
  notify "bigbounce loop DOWN — no heartbeat"
  convex_alert "bigbounce loop DOWN" "Watchdog found no parseable LOOP_HEARTBEAT.json at $NOW_ISO. Launching recovery tick."
  REC_LAST="$(recovery_last_epoch)"
  if [ "$((NOW_EPOCH - REC_LAST))" -lt "$RECOVERY_COOLDOWN_SECONDS" ]; then
    log_line "RECOVERY skipped — last recovery <1h ago (notify-only)"
  else
    launch_recovery
    log_line "RECOVERY launched (headless claude -p recovery tick)"
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
  launch_recovery
  log_line "DOWN   heartbeat stale (age ${AGE_H}) — notified+alerted; RECOVERY launched (headless claude -p)"
fi
exit 0
