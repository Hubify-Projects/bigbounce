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

export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$HOME/Library/TinyTeX/bin/universal-darwin:$PATH"
REPO="${BIGBOUNCE_REPO:-$HOME/Desktop/CODE_YOU/bigbounce}"
LOGDIR="${BIGBOUNCE_LOGDIR:-$REPO/project-context/cron-logs}"
RUNTIME_DIR="${BIGBOUNCE_RUNTIME_DIR:-$HOME/Library/Application Support/bigbounce}"
LOCK="${BIGBOUNCE_CRON_LOCK:-/tmp/bigbounce-cron.lock}"
CODEX_ENABLED="${BIGBOUNCE_CODEX_SUBSCRIPTION_ENABLED:-1}"
CODEX_BIN="${BIGBOUNCE_CODEX_BIN:-$(command -v codex 2>/dev/null || { [ -x /opt/homebrew/bin/codex ] && printf '%s' /opt/homebrew/bin/codex; })}"
# BIGBOUNCE_CRON_MODEL remains a compatibility alias; new deployments should
# use the shared BIGBOUNCE_CODEX_MODEL / BIGBOUNCE_CODEX_EFFORT knobs.
MODEL="${BIGBOUNCE_CODEX_MODEL:-${BIGBOUNCE_CRON_MODEL:-gpt-5.6-sol}}"
EFFORT="${BIGBOUNCE_CODEX_EFFORT:-${BIGBOUNCE_CRON_EFFORT:-high}}"
DRIVER_SANDBOX="${BIGBOUNCE_CRON_DRIVER_SANDBOX:-danger-full-access}"
LEASE_TTL="${BIGBOUNCE_LEASE_TTL_MINUTES:-75}"
MACHINE_ID="${BIGBOUNCE_MACHINE_ID:-$(hostname -s 2>/dev/null | tr -d '\n' | tr -c 'A-Za-z0-9._-' '-')}"
TS="$(date +%Y%m%d-%H%M%S)"

case "$CODEX_ENABLED" in 0|1) ;; *) echo "FAIL: BIGBOUNCE_CODEX_SUBSCRIPTION_ENABLED must be 0 or 1" >&2; exit 1 ;; esac
case "$EFFORT" in minimal|low|medium|high|xhigh|max|ultra) ;; *) echo "FAIL: BIGBOUNCE_CODEX_EFFORT must be minimal|low|medium|high|xhigh|max|ultra" >&2; exit 1 ;; esac
case "$DRIVER_SANDBOX" in workspace-write|danger-full-access) ;; *) echo "FAIL: BIGBOUNCE_CRON_DRIVER_SANDBOX must be workspace-write or danger-full-access" >&2; exit 1 ;; esac

# True no-launch/no-state validation path. It intentionally runs before mkdir,
# mutex, remote lease CAS, and heartbeat writes. Set DRY_RUN_ROLE=driver to
# inspect the authorized driver command; lease-free is the safe default.
if [ "${BIGBOUNCE_CRON_DRY_RUN:-0}" = "1" ]; then
  DRY_ROLE="${BIGBOUNCE_CRON_DRY_RUN_ROLE:-lease-free}"
  case "$DRY_ROLE" in driver) DRY_SANDBOX="$DRIVER_SANDBOX" ;; lease-free) DRY_SANDBOX="read-only" ;; *) echo "FAIL: BIGBOUNCE_CRON_DRY_RUN_ROLE must be driver or lease-free" >&2; exit 1 ;; esac
  LOGIN="unavailable"
  if [ -n "$CODEX_BIN" ]; then LOGIN="$(env -u OPENAI_API_KEY -u CODEX_API_KEY -u ANTHROPIC_API_KEY "$CODEX_BIN" login status 2>&1 || true)"; fi
  printf 'DRY_RUN role=%s codex_enabled=%s model=%s effort=%s sandbox=%s auth=%s no_state=1\n' \
    "$DRY_ROLE" "$CODEX_ENABLED" "$MODEL" "$EFFORT" "$DRY_SANDBOX" "$LOGIN"
  exit 0
fi

# Fail before mutex/lease/heartbeat state if the subscription runtime is
# disabled or unavailable. Never acquire the driver lease without an agent that
# can actually perform the tick.
if [ "$CODEX_ENABLED" = 0 ]; then
  echo "Codex subscription tick disabled by BIGBOUNCE_CODEX_SUBSCRIPTION_ENABLED=0" >&2
  exit 0
fi
[ -n "$CODEX_BIN" ] || { echo "codex CLI unavailable" >&2; exit 1; }
CODEX_LOGIN="$(env -u OPENAI_API_KEY -u CODEX_API_KEY -u ANTHROPIC_API_KEY "$CODEX_BIN" login status 2>&1 || true)"
printf '%s' "$CODEX_LOGIN" | grep -q 'Logged in using ChatGPT' || { echo "Codex ChatGPT login unavailable: $CODEX_LOGIN" >&2; exit 1; }
TIMEOUT_BIN="$(command -v timeout 2>/dev/null || command -v gtimeout 2>/dev/null || true)"
[ -n "$TIMEOUT_BIN" ] || { echo "timeout/gtimeout unavailable" >&2; exit 1; }

mkdir -p "$LOGDIR" "$RUNTIME_DIR"
LOG="$LOGDIR/tick-$TS.log"
# STICKY HEADED (2026-07-13, permanent): every browse relaunch this tick spawns
# must come back HEADED, not the server-node headless default. The EXT tools
# (ext_submit/ext_harvest/wave_submit) each re-export this, but exporting it at
# the cron root is belt-and-suspenders so any agent-spawned browse inherits it.
export BROWSE_HEADED=1

atomic_write() {
  local path="$1" body="$2" dir tmp
  dir="$(dirname "$path")"
  tmp="$(mktemp "$dir/.heartbeat.XXXXXX")" || return 1
  if ! printf '%s\n' "$body" > "$tmp"; then rm -f "$tmp"; return 1; fi
  chmod 0644 "$tmp" 2>/dev/null || true
  mv -f "$tmp" "$path"
}

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
  "note": sys.argv[3] + "; Codex ChatGPT-subscription tick",
}))
PY
)"
atomic_write "$HEARTBEAT_RUNTIME" "$HB_JSON" 2>/dev/null || true
atomic_write "$HEARTBEAT_REPO" "$HB_JSON" 2>/dev/null || true

if [ "$ROLE" = "driver" ]; then
  ROLE_PROMPT="DRIVER MODE: machine $MACHINE_ID holds the fresh lab lease. You may harvest, truth-audit/adjudicate, write verdict/ledger/Convex state, and commit the same-commit site mirror. Drive EXT only if the visible gstack browser is already healthy and reports Mode: headed; never substitute headless. Renew the lease before any additional long driver phase."
else
  ROLE_PROMPT="LEASE-FREE MODE: machine $MACHINE_ID does NOT hold the driver lease. This Codex run is READ-ONLY. Do not drive any browser, launch reviews or compute, adjudicate findings, edit files, write verdict/ledger/Convex/review state, or commit/push anything. Inspect current status and report exactly one bounded recommended next action for the lease holder. Re-check the lease next tick."
fi

PROMPT="Bigbounce durable loop tick. Repo: $REPO.

$ROLE_PROMPT

Read ops/RUNBOOK.md, CLAUDE.md directives I and J-M, and canonical SSOT first. Perform ONE atomic, idempotent increment in the allowed role. Never fake ACCEPT, fabricate science, or record a verdict without complete raw text and screenshot. All paper changes require directive-G PDF hygiene and same-commit site/SSOT/Convex sync. Report exactly what advanced and stop."

if [ "$ROLE" = "driver" ]; then
  SANDBOX="$DRIVER_SANDBOX"
else
  SANDBOX="read-only"
fi

printf '%s\n' "$PROMPT" | env -u OPENAI_API_KEY -u CODEX_API_KEY -u ANTHROPIC_API_KEY \
  "$TIMEOUT_BIN" 3000 "$CODEX_BIN" --cd "$REPO" --sandbox "$SANDBOX" \
    --ask-for-approval never --model "$MODEL" \
    -c "model_reasoning_effort=\"$EFFORT\"" exec --ephemeral --color never - \
    >> "$LOG" 2>&1
rc=$?
echo "[$TS] tick exit $rc role=$ROLE machineId=$MACHINE_ID model=$MODEL effort=$EFFORT sandbox=$SANDBOX auth=ChatGPT" >> "$LOG"

ls -t "$LOGDIR"/tick-*.log 2>/dev/null | tail -n +61 | xargs rm -f 2>/dev/null
exit "$rc"
