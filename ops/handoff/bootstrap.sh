#!/usr/bin/env bash
# ops/handoff/bootstrap.sh — idempotent new-machine readiness verifier for the
# bigbounce ONE-LAB-TWO-MACHINES handoff. Safe to run repeatedly; it CHECKS and
# REPORTS, it does not mutate paper state or drive the loop. It prints a
# PASS/FAIL table and, for anything missing, the exact command / skill to fix it.
#
# NEVER prints secret VALUES — only key NAMES and present/absent status.
#
# Companion docs (same dir): BOOTSTRAP_PROMPT.md (the paste-in prompt),
# HANDOFF_SYNC.md (two-machine model), ORCHESTRATOR_PORTABILITY.md (Codex/Cursor/Pi).
# The generic cross-machine restore is the /machine-sync skill; the full
# bigbounce delta is project-context/AGENT_ONBOARDING.md.

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
ENV_FILE="$REPO_ROOT/.env.local"
CONVEX_QUERY_URL="https://brilliant-panther-471.convex.cloud/api/query"
LA_DIR="$HOME/Library/LaunchAgents"

# required .env.local key NAMES (names only — values never printed / never read out)
REQUIRED_KEYS=(HF_TOKEN OPENROUTER_API_KEY OPENAI_API_KEY XAI_API_KEY RUNPOD_API_KEY)

pass=0; fail=0; warn=0
ROWS=()
row() { # row <STATUS> <check> <detail/fix>
  ROWS+=("$1"$'\t'"$2"$'\t'"$3")
  case "$1" in PASS) pass=$((pass+1));; FAIL) fail=$((fail+1));; WARN) warn=$((warn+1));; esac
}
have() { command -v "$1" >/dev/null 2>&1; }

# 1. git remote reachable ----------------------------------------------------
if git -C "$REPO_ROOT" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  if git -C "$REPO_ROOT" ls-remote --exit-code origin >/dev/null 2>&1; then
    row PASS "git remote reachable" "$(git -C "$REPO_ROOT" remote get-url origin 2>/dev/null)"
  else
    row FAIL "git remote reachable" "origin unreachable — check network / 'gh auth login'"
  fi
else
  row FAIL "git repo" "not a git work tree at $REPO_ROOT — clone first (see BOOTSTRAP_PROMPT.md)"
fi

# 2. TinyTeX / pdflatex ------------------------------------------------------
if have pdflatex; then
  row PASS "pdflatex (LaTeX)" "$(pdflatex --version 2>/dev/null | head -1)"
else
  row FAIL "pdflatex (LaTeX)" "install: brew install --cask mactex-no-gui  (or basictex/TinyTeX)"
fi
have latexmk && row PASS "latexmk" "present" || row WARN "latexmk" "brew install latexmk (used by /paper-compile-revtex)"
have pdftoppm && row PASS "poppler (pdftoppm)" "present" || row FAIL "poppler (pdftoppm)" "brew install poppler (Grok raster + /latex-audit)"

# 3. python3 + review SDKs ---------------------------------------------------
if have python3; then
  row PASS "python3" "$(python3 --version 2>&1)"
  for mod in openai google.generativeai anthropic; do
    if python3 -c "import ${mod%%.*}" >/dev/null 2>&1; then
      row PASS "py: $mod" "importable"
    else
      row WARN "py: $mod" "pip install ${mod/./-} (review tooling vendor SDK)"
    fi
  done
else
  row FAIL "python3" "install python3 (review tooling + audits require it)"
fi

# 4. claude CLI --------------------------------------------------------------
if have claude; then
  row PASS "claude CLI" "$(claude --version 2>/dev/null | head -1)"
else
  row WARN "claude CLI" "Claude Code CLI not on PATH (fine if orchestrating in Codex/Cursor)"
fi

# 5. gstack browse tool ------------------------------------------------------
BROWSE="$HOME/.claude/skills/gstack/browse/dist/browse"
if [ -x "$BROWSE" ]; then
  row PASS "gstack browse tool" "$BROWSE"
else
  row WARN "gstack browse tool" "not found at $BROWSE — needed for HEADED EXT sweeps (/connect-chrome)"
fi

# 6. launchd plists installed (durable loop guarantee) -----------------------
for plist in com.bigbounce.loopwatchdog com.bigbounce.cron-tick; do
  repo_copy="$REPO_ROOT/tools/launchd/$plist.plist"
  if [ -f "$LA_DIR/$plist.plist" ]; then
    row PASS "launchd: $plist" "installed in ~/Library/LaunchAgents"
  elif [ -f "$repo_copy" ]; then
    row WARN "launchd: $plist" "not installed — install: cp $repo_copy $LA_DIR/ && launchctl load -w $LA_DIR/$plist.plist"
  else
    row WARN "launchd: $plist" "repo copy missing at $repo_copy"
  fi
done

# 7. .env.local presence + required key NAMES (NEVER values) -----------------
if [ -f "$ENV_FILE" ]; then
  row PASS ".env.local present" "$ENV_FILE (gitignored)"
  for k in "${REQUIRED_KEYS[@]}"; do
    # match a non-empty assignment; we read only the KEY column, never the value.
    if grep -qE "^[[:space:]]*(export[[:space:]]+)?${k}=[^[:space:]]" "$ENV_FILE" 2>/dev/null; then
      row PASS "key: $k" "set (value hidden)"
    else
      row FAIL "key: $k" "missing/blank — restore via /machine-sync (You.md Secret Vault); do NOT paste values here"
    fi
  done
else
  row FAIL ".env.local present" "missing — restore via /machine-sync skill (You.md Secret Vault); NEVER commit it"
fi

# 8. Convex reachability probe ----------------------------------------------
if have curl; then
  code="$(curl -sS -m 8 -o /dev/null -w '%{http_code}' -X POST "$CONVEX_QUERY_URL" \
           -H 'Content-Type: application/json' \
           -d '{"path":"papers:list","args":{},"format":"json"}' 2>/dev/null || echo 000)"
  if [ "$code" = "200" ]; then
    row PASS "Convex reachable" "brilliant-panther-471 responds 200 (shared live state)"
  else
    row WARN "Convex reachable" "HTTP $code from convex query endpoint — check network (writes are best-effort anyway)"
  fi
else
  row WARN "Convex reachable" "curl missing — cannot probe; install curl"
fi

# 9. lab lease tool + headed-browser note ------------------------------------
if [ -x "$REPO_ROOT/tools/lab_lease.sh" ]; then
  row PASS "lab_lease.sh" "present — acquire the lab lease BEFORE driving (see HANDOFF_SYNC.md)"
else
  row WARN "lab_lease.sh" "missing/not executable at tools/lab_lease.sh"
fi
row WARN "headed browser login" "first run: HEADED Chrome needs Houston's manual reviewer logins (ChatGPT/Grok/Gemini). Run /connect-chrome, sign in, THEN run EXT."

# --- render table -----------------------------------------------------------
echo ""
echo "  bigbounce two-machine handoff — bootstrap readiness ($(date -u +%FT%TZ))"
echo "  machine: $(hostname -s 2>/dev/null || echo unknown)   repo: $REPO_ROOT"
echo ""
printf "  %-6s  %-26s  %s\n" "STATUS" "CHECK" "DETAIL / FIX"
printf "  %-6s  %-26s  %s\n" "------" "--------------------------" "----------------------------------------"
for r in "${ROWS[@]}"; do
  IFS=$'\t' read -r st ck dt <<<"$r"
  printf "  %-6s  %-26s  %s\n" "$st" "$ck" "$dt"
done
echo ""
echo "  SUMMARY: $pass PASS · $warn WARN · $fail FAIL"
if [ "$fail" -gt 0 ]; then
  echo "  → RESULT: NOT READY. Resolve every FAIL above (WARN is degraded-but-runnable), then re-run."
  exit 1
fi
echo "  → RESULT: READY. Next: acquire the lab lease (tools/lab_lease.sh claim <machine-id> <ttl>), then start the loop per ops/RUNBOOK.md."
exit 0
