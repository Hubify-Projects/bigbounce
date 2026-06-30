#!/bin/bash
# bigbounce-cron-tick.sh — durable 24/7 paper-driving loop tick.
#
# Fires hourly via the system crontab (survives session exit + reboot, unlike the
# in-session CronCreate job). Runs the bigbounce review/drive loop headless via
# `claude -p`. Idempotent: an atomic mkdir lock prevents overlapping ticks (a tick
# can run 30+ min; hourly firing must not pile up).
#
# Model is configurable: BIGBOUNCE_CRON_MODEL (default opus). Cost note: most ticks
# are cheap (state-check + harvest); full rounds spawn 6 subagents only when idle.
set -u

REPO="$HOME/Desktop/CODE_2025/bigbounce"
LOGDIR="$REPO/project-context/cron-logs"
LOCK="/tmp/bigbounce-cron.lock"
MODEL="${BIGBOUNCE_CRON_MODEL:-opus}"
TS="$(date +%Y%m%d-%H%M%S)"
mkdir -p "$LOGDIR"
LOG="$LOGDIR/tick-$TS.log"

# cron runs with a minimal PATH — restore what the loop + its tools need.
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$HOME/Library/TinyTeX/bin/universal-darwin:$PATH"

# Stale-lock reclaim: if the lock dir is older than 90 min, a prior tick crashed.
if [ -d "$LOCK" ]; then
  if [ -n "$(find "$LOCK" -maxdepth 0 -mmin +90 2>/dev/null)" ]; then
    rmdir "$LOCK" 2>/dev/null
  else
    echo "[$TS] previous tick still running (pid $(cat "$LOCK/pid" 2>/dev/null)) — skipping" >> "$LOGDIR/skips.log"
    exit 0
  fi
fi
# Atomic lock (mkdir is atomic on POSIX).
if ! mkdir "$LOCK" 2>/dev/null; then
  echo "[$TS] lock race — skipping" >> "$LOGDIR/skips.log"; exit 0
fi
echo $$ > "$LOCK/pid"
trap 'rmdir "$LOCK" 2>/dev/null' EXIT

cd "$REPO" || { echo "[$TS] cannot cd $REPO" >> "$LOG"; exit 1; }

read -r -d '' PROMPT <<'EOF'
Bigbounce paper-driving loop tick (hourly system cron). Repo: ~/Desktop/CODE_2025/bigbounce. GOAL: drive ALL 6 papers (P1A/P1B/P2/P3/P4/P5) to REAL external ACCEPT from ChatGPT+Grok+Gemini with 0 MAJOR and 0 minor. The bar is the reviewer actually returning ACCEPT, NOT a truth-audit dismissing their finding. NEVER fake an ACCEPT; never fabricate math/data (patterns 061-064 + calibration apply).

ONE atomic increment per tick (idempotent; guard against overlap):
1) STATE CHECK: if review agents / an EXT browser sweep are running or there are fresh un-harvested EXT*/RREXT*/R* results, do NOT start a new round — harvest the completed legs, record REAL verdicts to Convex (externalReviews:upsertByLabelDate, source internal-stage3), re-cap readiness (papers:setReadinessCap) to match the real verdicts, then stop.
2) IF un-harvested results exist: per-paper, INTAKE every external MAJOR/minor and SUBSTANTIVELY address it (fix the science/consistency/clarity, run a calculation where a finding points to a real gap, or make the in-paper treatment bulletproof so the next reviewer can't re-flag). For compute-gated items see project-context/SSOT/compute-to-accept-queue.md — those need real pod runs, not edits; do NOT fake them. Recompile (TinyTeX; 0 undef-refs) + /latex-audit. Bump version+date, mirror PDFs to all served paths, Convex paperVersions:bump, papers.ts + reviewTimeline same-commit (pattern-065). Commit+push.
3) IF idle (no round running, last harvested): spawn one Opus paper-owner agent per paper to drive its weakest external verdicts up by addressing the specific reasons; recompile; then run a de-biased browser EXT sweep IF the logged-in gstack browser is available (headless cron may not have it — if unavailable, do the INT/paper-improvement side this tick and note EXT is browser-gated). Commit+push.
4) ALWAYS keep the site honest: readiness reflects external acceptance (caps 86-92 until reviewers ACCEPT; 96 only at all-3-ACCEPT R-converged), never a false high %.
EXIT GATE: only when a FULL fresh external sweep returns ACCEPT from all 3 reviewers on all 6 papers, 0 MAJOR 0 minor, INT/EXT gap 0. Until then CONTINUE every hour. The point is to genuinely FIX + advance the papers (run new science when a finding needs it), not game the gate. Report what advanced this tick. Read project-context/AGENT_ONBOARDING.md + CLAUDE.md if context is thin.
EOF

# 50-minute cap so a tick can never overlap the next hour.
timeout 3000 claude -p "$PROMPT" --dangerously-skip-permissions --model "$MODEL" >> "$LOG" 2>&1
echo "[$TS] tick exit $?" >> "$LOG"

# Keep only the last 60 tick logs.
ls -t "$LOGDIR"/tick-*.log 2>/dev/null | tail -n +61 | xargs rm -f 2>/dev/null
