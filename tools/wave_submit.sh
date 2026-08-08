#!/usr/bin/env bash
# wave_submit.sh — place a full EXT review wave with PER-LEG ISOLATION.
#
# Drives tools/ext_submit.sh once per (paper, reviewer) leg. The whole point is
# RESILIENCE: one leg failing NEVER stops the chain, and every leg's full output
# is captured to its own log so nothing is lost silently. Compound
# `cmd | tail -1` chains in the orchestrator lost legs twice (M25 P3APJS
# unknown-paper double-FAIL half-noticed; M34 chain died after leg 2 with three
# legs never attempted). This runner makes both classes impossible: it never
# uses `set -e` across legs, always attempts every leg, and prints a summary
# table so callers see OK/FAIL per leg at a glance.
#
# Usage:
#   tools/wave_submit.sh <round> <PAPER:reviewer> [<PAPER:reviewer> ...]
#   tools/wave_submit.sh --dry-run <round> <PAPER:reviewer> [...]
#
# Example:
#   tools/wave_submit.sh M37 P5:grok P5:chatgpt P2:grok P2:chatgpt
#
# --dry-run   Print the planned legs + summary path WITHOUT driving the browser
#             (arg-parsing / summary path live-test only; no real submissions).
#
# Exit: 0 if ALL legs OK, 1 if ANY leg FAILED (so callers see it at a glance).
#
# NOTE: intentionally NO `set -e` — a failing leg must not abort the chain.
set -uo pipefail

# ROOT FIX (2026-07-13, permanent): make the headed browser STICKY. The gstack
# browse server auto-launches HEADLESS on any on-demand relaunch when
# BROWSE_HEADED != 1 (server-node useHeadless defaults true) -> login walls read
# as dead chats -> false FAILED-dead harvests. Exporting BROWSE_HEADED=1 here (and
# inheriting into every ext_submit.sh child) makes every browse relaunch HEADED.
# ROOT kill; assert_headed is the safety net.
export BROWSE_HEADED=1

REPO="/Users/houstongolden/Desktop/CODE_YOU/bigbounce"
EXT_SUBMIT="$REPO/tools/ext_submit.sh"

DRYRUN=0
ARGS=()
for a in "$@"; do
  case "$a" in
    --dry-run) DRYRUN=1 ;;
    *) ARGS+=("$a") ;;
  esac
done

if [ "${#ARGS[@]}" -lt 2 ]; then
  echo "usage: tools/wave_submit.sh [--dry-run] <round> <PAPER:reviewer> [<PAPER:reviewer> ...]" >&2
  echo "  e.g. tools/wave_submit.sh M37 P5:grok P5:chatgpt P2:grok P2:chatgpt" >&2
  exit 2
fi

ROUND="${ARGS[0]}"
LEGS=("${ARGS[@]:1}")

if [ "${#LEGS[@]}" -lt 1 ]; then
  echo "wave_submit: no legs given after round '$ROUND'" >&2
  exit 2
fi

WAVE_DIR="/tmp/wave_${ROUND}"
mkdir -p "$WAVE_DIR"

echo "=== wave_submit :: round=$ROUND legs=${#LEGS[@]} ==="
echo "    logs: $WAVE_DIR"
[ "$DRYRUN" = 1 ] && echo "    *** DRY RUN — no browser, no real submissions ***"

# Parallel-index arrays hold each leg's result (bash-3.2 safe: no assoc arrays).
R_LEG=()
R_STATUS=()
R_INFO=()

any_fail=0

leg_idx=0
for leg in "${LEGS[@]}"; do
  leg_idx=$((leg_idx + 1))
  # Parse PAPER:reviewer.
  paper="${leg%%:*}"
  reviewer="${leg#*:}"
  if [ "$paper" = "$leg" ] || [ -z "$paper" ] || [ -z "$reviewer" ]; then
    echo "--- leg $leg_idx: '$leg' — BAD FORMAT (expected PAPER:reviewer) ---"
    R_LEG+=("$leg")
    R_STATUS+=("FAIL")
    R_INFO+=("bad leg format (expected PAPER:reviewer)")
    any_fail=1
    continue
  fi

  log="$WAVE_DIR/${paper}_${reviewer}_${ROUND}.log"
  echo "--- leg $leg_idx/${#LEGS[@]}: $paper:$reviewer -> $log ---"

  if [ "$DRYRUN" = 1 ]; then
    # Plan only — record the command that WOULD run, do not execute.
    printf 'DRY-RUN planned leg: %s %s %s %s\n' "$EXT_SUBMIT" "$paper" "$reviewer" "$ROUND" | tee "$log"
    R_LEG+=("$paper:$reviewer")
    R_STATUS+=("OK")
    R_INFO+=("dry-run (planned, not submitted)")
    # Mirror the real chain's chatgpt-spacing so a dry run exercises the path.
    if [ "$reviewer" = "chatgpt" ] && [ "$leg_idx" -lt "${#LEGS[@]}" ]; then
      echo "    [dry-run] would sleep 10 after chatgpt leg"
    fi
    continue
  fi

  # Run the leg in its own subshell so a die()/exit inside ext_submit.sh can
  # NEVER terminate this runner. Capture full stdout+stderr to the per-leg log
  # AND stream it to the console. `set -e` is not active here, so a non-zero rc
  # is simply recorded — the loop always continues to the next leg.
  ( "$EXT_SUBMIT" "$paper" "$reviewer" "$ROUND" ) >"$log" 2>&1
  rc=$?

  if [ "$rc" -eq 0 ]; then
    # Success path: pull the OK line's url= field for the summary.
    okline="$(grep -E '^OK: ' "$log" | tail -1)"
    url="$(printf '%s' "$okline" | sed -n 's/.*url=\([^ ]*\).*/\1/p')"
    [ -n "$url" ] || url="OK (see log)"
    R_LEG+=("$paper:$reviewer")
    R_STATUS+=("OK")
    R_INFO+=("$url")
    echo "    leg OK: $url"
  else
    # Failure path: surface the FAIL: reason (or last log line) for the summary.
    reason="$(grep -E '^FAIL: ' "$log" | tail -1 | sed 's/^FAIL: //')"
    [ -n "$reason" ] || reason="$(tail -1 "$log")"
    [ -n "$reason" ] || reason="rc=$rc (see log)"
    R_LEG+=("$paper:$reviewer")
    R_STATUS+=("FAIL")
    R_INFO+=("$reason")
    any_fail=1
    echo "    leg FAILED (rc=$rc): $reason" >&2
  fi

  # Between chatgpt legs, sleep 10 to reduce composer-state contention — two
  # wrong-PDF misfile incidents happened on back-to-back chatgpt legs. Only
  # sleep when THIS leg was chatgpt and another leg follows.
  if [ "$reviewer" = "chatgpt" ] && [ "$leg_idx" -lt "${#LEGS[@]}" ]; then
    echo "    [spacing] sleeping 10s after chatgpt leg to settle composer state"
    sleep 10
  fi
done

# ---- summary table ----
echo ""
echo "=== wave_submit summary :: round=$ROUND ==="
printf '%-16s %-6s %s\n' "LEG" "RESULT" "URL-OR-REASON"
printf '%-16s %-6s %s\n' "---" "------" "-------------"
i=0
while [ "$i" -lt "${#R_LEG[@]}" ]; do
  printf '%-16s %-6s %s\n' "${R_LEG[$i]}" "${R_STATUS[$i]}" "${R_INFO[$i]}"
  i=$((i + 1))
done
echo "---"
echo "logs: $WAVE_DIR"

if [ "$any_fail" -eq 0 ]; then
  echo "OVERALL: all ${#R_LEG[@]} leg(s) OK"
  exit 0
else
  echo "OVERALL: at least one leg FAILED" >&2
  exit 1
fi
