#!/usr/bin/env bash
# bigbounce_cron_tick.sh — canonical durable loop tick source.
#
# Deploy (do not run from Desktop under launchd; macOS TCC blocks it):
#   cp tools/bigbounce_cron_tick.sh \
#     "$HOME/Library/Application Support/bigbounce/bigbounce-cron-tick.sh"
#
# The lease is checked before work starts. One machine becomes DRIVER and may
# adjudicate/write verdicts or use the headed browser. Every other machine runs
# a lease-free INT/compute lane only. The lease helper never touches this
# checkout's worktree or index.

set -uo pipefail

REPO="${BIGBOUNCE_REPO:-$HOME/Desktop/CODE_YOU/bigbounce}"
LOGDIR="${BIGBOUNCE_LOGDIR:-$REPO/project-context/cron-logs}"
RUNTIME_DIR="${BIGBOUNCE_RUNTIME_DIR:-$HOME/Library/Application Support/bigbounce}"
LOCK="${BIGBOUNCE_CRON_LOCK:-/tmp/bigbounce-cron.lock}"
MODEL="${BIGBOUNCE_CRON_MODEL:-opus}"
LEASE_TTL="${BIGBOUNCE_LEASE_TTL_MINUTES:-75}"
MACHINE_ID="${BIGBOUNCE_MACHINE_ID:-$(hostname -s 2>/dev/null | tr -d '\n' | tr -c 'A-Za-z0-9._-' '-')}"
TS="$(date +%Y%m%d-%H%M%S)"

mkdir -p "$LOGDIR" "$RUNTIME_DIR"
LOG="$LOGDIR/tick-$TS.log"
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$HOME/Library/TinyTeX/bin/universal-darwin:$PATH"

# A local mutex prevents two launchd ticks on this machine from overlapping.
if [ -d "$LOCK" ]; then
  if [ -n "$(find "$LOCK" -maxdepth 0 -mmin +55 2>/dev/null)" ]; then
    echo "[$TS] stale local lock (pid $(cat "$LOCK.pid" 2>/dev/null)) — reclaiming" >> "$LOGDIR/skips.log"
    rm -rf "$LOCK" "$LOCK.pid" 2>/dev/null
  else
    echo "[$TS] previous local tick still running (pid $(cat "$LOCK.pid" 2>/dev/null)) — skipping" >> "$LOGDIR/skips.log"
    exit 0
  fi
fi
if ! mkdir "$LOCK" 2>/dev/null; then
  echo "[$TS] local lock race — skipping" >> "$LOGDIR/skips.log"
  exit 0
fi
echo $$ > "$LOCK.pid"
trap 'rm -rf "$LOCK" "$LOCK.pid" 2>/dev/null' EXIT HUP INT TERM

cd "$REPO" || { echo "[$TS] cannot cd $REPO" >> "$LOG"; exit 1; }
LEASE="$REPO/tools/lab_lease.sh"

# Remote lease CAS. A network/parse failure fails closed into LEASE-FREE mode.
ROLE="lease-free"
LEASE_NOTE="lease unavailable or held by another machine"
if "$LEASE" holds "$MACHINE_ID" >/dev/null 2>&1; then
  if "$LEASE" renew "$MACHINE_ID" "$LEASE_TTL" >> "$LOG" 2>&1; then
    ROLE="driver"; LEASE_NOTE="fresh lease renewed"
  fi
elif "$LEASE" claim "$MACHINE_ID" "$LEASE_TTL" >> "$LOG" 2>&1; then
  ROLE="driver"; LEASE_NOTE="lease claimed"
fi

# Heartbeat records machine identity and whether this tick owns the driver lane.
HEARTBEAT_RUNTIME="$RUNTIME_DIR/LOOP_HEARTBEAT.json"
HEARTBEAT_REPO="$REPO/project-context/LOOP_HEARTBEAT.json"
HB_JSON="$(python3 - "$MACHINE_ID" "$ROLE" "$LEASE_NOTE" <<'PY'
import datetime, json, sys
print(json.dumps({
  "lastTickUTC": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
  "source": "cron-tick",
  "machineId": sys.argv[1],
  "role": sys.argv[2],
  "note": sys.argv[3],
}))
PY
)"
( printf '%s\n' "$HB_JSON" > "$HEARTBEAT_RUNTIME" ) 2>/dev/null || true
( printf '%s\n' "$HB_JSON" > "$HEARTBEAT_REPO" ) 2>/dev/null || true

if [ "$ROLE" = "driver" ]; then
  ROLE_PROMPT="DRIVER MODE: machine $MACHINE_ID holds the fresh lab lease. You may harvest, truth-audit/adjudicate, write verdict/ledger/Convex state, and commit the same-commit site mirror. Drive EXT only if the visible gstack browser is already healthy and reports Mode: headed; never substitute headless. Renew the lease before any additional long driver phase."
else
  ROLE_PROMPT="LEASE-FREE MODE: machine $MACHINE_ID does NOT hold the driver lease. Do not drive any browser, adjudicate findings, write verdict/ledger/Convex review state, or commit/push review/site-surface bundles. Do one bounded lease-free task only: INT API review with raw capture, local/RunPod compute, reproducibility verification, or disjoint docs/tooling. Re-check the lease next tick."
fi

PROMPT="Bigbounce durable loop tick. Repo: $REPO.

$ROLE_PROMPT

Read ops/RUNBOOK.md, CLAUDE.md directives I and J-M, and canonical SSOT first. Perform ONE atomic, idempotent increment in the allowed role. Never fake ACCEPT, fabricate science, or record a verdict without complete raw text and screenshot. All paper changes require directive-G PDF hygiene and same-commit site/SSOT/Convex sync. Report exactly what advanced and stop."

# Test hook: exercises lease + heartbeat routing without launching an agent.
if [ "${BIGBOUNCE_CRON_DRY_RUN:-0}" = "1" ]; then
  printf 'DRY_RUN role=%s machineId=%s note=%s\n' "$ROLE" "$MACHINE_ID" "$LEASE_NOTE"
  exit 0
fi

CLAUDE_BIN="${BIGBOUNCE_CLAUDE_BIN:-$(command -v claude 2>/dev/null || true)}"
[ -n "$CLAUDE_BIN" ] || { echo "[$TS] claude CLI unavailable" >> "$LOG"; exit 1; }
TIMEOUT_BIN="$(command -v timeout 2>/dev/null || command -v gtimeout 2>/dev/null || true)"
[ -n "$TIMEOUT_BIN" ] || { echo "[$TS] timeout/gtimeout unavailable" >> "$LOG"; exit 1; }

unset ANTHROPIC_API_KEY
"$TIMEOUT_BIN" 3000 "$CLAUDE_BIN" -p "$PROMPT" \
  --dangerously-skip-permissions --model "$MODEL" >> "$LOG" 2>&1
rc=$?
echo "[$TS] tick exit $rc role=$ROLE machineId=$MACHINE_ID" >> "$LOG"

ls -t "$LOGDIR"/tick-*.log 2>/dev/null | tail -n +61 | xargs rm -f 2>/dev/null
exit "$rc"
