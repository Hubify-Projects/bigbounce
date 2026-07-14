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
REQUIRED_KEYS=(HF_TOKEN OPENROUTER_API_KEY XAI_API_KEY RUNPOD_API_KEY)

pass=0; fail=0; warn=0
ROWS=()
row() { # row <STATUS> <check> <detail/fix>
  ROWS+=("$1"$'\t'"$2"$'\t'"$3")
  case "$1" in PASS) pass=$((pass+1));; FAIL) fail=$((fail+1));; WARN) warn=$((warn+1));; esac
}
have() { command -v "$1" >/dev/null 2>&1; }

# Return a TeX executable without evaluating shell text or changing the caller's
# PATH. TinyTeX can be installed outside the system PATH on macOS.
find_tex_tool() { # find_tex_tool <name>
  local tool="$1" found="" root=""
  if have "$tool"; then
    command -v "$tool"
    return 0
  fi
  for root in \
    "/Library/TeX/texbin" \
    "$HOME/Library/TinyTeX/bin/universal-darwin" \
    "$HOME/Library/TinyTeX/bin/arm64-darwin" \
    "$HOME/Library/TinyTeX/bin/x86_64-darwin" \
    "$HOME/.TinyTeX/bin/universal-darwin" \
    "$HOME/.TinyTeX/bin/arm64-darwin" \
    "$HOME/.TinyTeX/bin/x86_64-darwin"; do
    [ -x "$root/$tool" ] && { printf '%s\n' "$root/$tool"; return 0; }
  done
  for root in "$HOME/Library/TinyTeX/bin" "$HOME/.TinyTeX/bin"; do
    [ -d "$root" ] || continue
    found="$(find "$root" -maxdepth 2 -type f -name "$tool" -perm -u+x -print -quit 2>/dev/null)"
    [ -n "$found" ] && { printf '%s\n' "$found"; return 0; }
  done
  return 1
}

sanitized_origin() {
  if ! have python3; then
    printf '%s\n' '[configured; hidden until python3 is available]'
    return 0
  fi
  git -C "$REPO_ROOT" remote get-url origin 2>/dev/null | python3 -c '
import sys
from urllib.parse import urlsplit, urlunsplit
raw = sys.stdin.read().strip()
try:
    p = urlsplit(raw)
    if p.scheme in {"http", "https", "ssh"}:
        host = p.hostname or "unknown-host"
        if p.port:
            host += f":{p.port}"
        print(urlunsplit((p.scheme, host, p.path, "", "")))
    elif "@" in raw:
        print("[credentials]@" + raw.rsplit("@", 1)[1])
    else:
        print(raw)
except Exception:
    print("[configured; display unavailable]")
'
}

env_key_is_nonblank() { # env_key_is_nonblank <file> <key>; never prints values
  python3 - "$1" "$2" <<'PY' >/dev/null 2>&1
import re, shlex, sys
path, wanted = sys.argv[1:3]
assignment = re.compile(r"^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)$")
with open(path, encoding="utf-8") as fh:
    for line in fh:
        match = assignment.match(line.rstrip("\r\n"))
        if not match or match.group(1) != wanted:
            continue
        raw = match.group(2).strip()
        if not raw or raw.startswith("#"):
            continue
        try:
            lexer = shlex.shlex(raw, posix=True)
            lexer.whitespace_split = True
            lexer.commenters = "#"
            value = " ".join(list(lexer)).strip()
        except ValueError:
            value = ""
        if value:
            raise SystemExit(0)
raise SystemExit(1)
PY
}

# 1. git remote reachable ----------------------------------------------------
if git -C "$REPO_ROOT" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  if git -C "$REPO_ROOT" ls-remote --exit-code origin >/dev/null 2>&1; then
    row PASS "git remote reachable" "$(sanitized_origin)"
  else
    row FAIL "git remote reachable" "origin unreachable — check network / 'gh auth login'"
  fi
else
  row FAIL "git repo" "not a git work tree at $REPO_ROOT — clone first (see BOOTSTRAP_PROMPT.md)"
fi

# 2. TinyTeX / pdflatex ------------------------------------------------------
PDFLATEX_BIN="$(find_tex_tool pdflatex 2>/dev/null || true)"
LATEXMK_BIN="$(find_tex_tool latexmk 2>/dev/null || true)"
if [ -n "$PDFLATEX_BIN" ]; then
  row PASS "pdflatex (LaTeX)" "$("$PDFLATEX_BIN" --version 2>/dev/null | head -1) [$PDFLATEX_BIN]"
else
  row FAIL "pdflatex (LaTeX)" "install: brew install --cask mactex-no-gui  (or basictex/TinyTeX)"
fi
[ -n "$LATEXMK_BIN" ] && row PASS "latexmk" "present [$LATEXMK_BIN]" || row WARN "latexmk" "install with TinyTeX/tlmgr or brew (used by /paper-compile-revtex)"
have pdftoppm && row PASS "poppler (pdftoppm)" "present" || row FAIL "poppler (pdftoppm)" "brew install poppler (Grok raster + /latex-audit)"

# 3. python3 + review SDKs ---------------------------------------------------
if have python3; then
  row PASS "python3" "$(python3 --version 2>&1)"
  # The openai Python package remains an SDK dependency for OpenAI-compatible
  # xAI/Perplexity endpoints; no OPENAI_API_KEY is required or used for reviews.
  for spec in "openai:openai" "google.generativeai:google-generativeai"; do
    mod="${spec%%:*}"; package="${spec#*:}"
    if python3 -c "import importlib; importlib.import_module('$mod')" >/dev/null 2>&1; then
      row PASS "py: $mod" "importable"
    else
      row WARN "py: $mod" "pip install $package (review tooling vendor SDK)"
    fi
  done
else
  row FAIL "python3" "install python3 (review tooling + audits require it)"
fi

# 4. legacy claude CLI (not used by the active BigBounce campaign) -----------
if have claude; then
  row PASS "claude CLI" "$(claude --version 2>/dev/null | head -1)"
else
  row WARN "claude CLI" "Claude Code CLI not on PATH (fine if orchestrating in Codex/Cursor)"
fi

# 5. gstack browse tool ------------------------------------------------------
BROWSE="$HOME/.claude/skills/gstack/browse/dist/browse"
if [ -x "$BROWSE" ]; then
  row PASS "gstack browse tool" "$BROWSE"
  # `status` is read-only: it reports the existing server and never connects,
  # cleans up, opens a tab, or changes browser mode.
  browse_status="$($BROWSE status 2>/dev/null || true)"
  browse_health="$(printf '%s\n' "$browse_status" | awk -F': *' '/^Status:/{print $2; exit}')"
  browse_mode="$(printf '%s\n' "$browse_status" | awk -F': *' '/^Mode:/{print $2; exit}')"
  if [ -n "$browse_mode" ]; then
    row PASS "gstack browser mode" "${browse_mode} (status: ${browse_health:-unknown}; read-only probe)"
  else
    row WARN "gstack browser mode" "no active mode reported (read-only status probe only; bootstrap did not connect)"
  fi
else
  row WARN "gstack browse tool" "not found at $BROWSE — needed for HEADED EXT sweeps (/connect-chrome)"
fi

# 5b. BROWSE_HEADED sticky-headed guard (2026-07-13, machine-level root fix) ---
# The gstack browse server auto-launches HEADLESS on any on-demand relaunch when
# BROWSE_HEADED != 1 (server-node useHeadless defaults true). A headed server
# that dies between ticks then silently relaunches headless -> login walls read
# as dead chats -> false FAILED-dead harvests. The EXT tools now each export
# BROWSE_HEADED=1 and the cron tick exports it at the root, so the tools are
# covered. This check is the MACHINE-LEVEL belt-and-suspenders: a persistent
# `export BROWSE_HEADED=1` in the shell profile covers ad-hoc `browse` invocations
# from an interactive shell too.
if grep -qsE '^\s*export\s+BROWSE_HEADED=1' "$HOME/.zshrc" "$HOME/.zprofile" "$HOME/.profile" "$HOME/.bashrc" 2>/dev/null \
   || [ "${BROWSE_HEADED:-}" = "1" ]; then
  row PASS "BROWSE_HEADED sticky" "export BROWSE_HEADED=1 present (tools+cron already export it; this is the shell-profile belt-and-suspenders)"
else
  row WARN "BROWSE_HEADED sticky" "no 'export BROWSE_HEADED=1' in shell profile — tools+cron export it, but add it to ~/.zshrc so ad-hoc 'browse' calls also relaunch HEADED"
fi

# 6. launchd plists installed (durable loop guarantee) -----------------------
for plist in com.bigbounce.loopwatchdog com.bigbounce.cron-tick; do
  repo_copy="$REPO_ROOT/tools/launchd/$plist.plist"
  if [ -f "$LA_DIR/$plist.plist" ]; then
    if launchctl print "gui/$(id -u)/$plist" >/dev/null 2>&1; then
      row PASS "launchd: $plist" "installed + loaded"
    else
      row WARN "launchd: $plist" "installed but NOT loaded — load: launchctl load -w $LA_DIR/$plist.plist"
    fi
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
    # Parse without evaluation. Empty, whitespace-only, quoted-empty, malformed,
    # and comment-only assignments all fail; values are never printed.
    if env_key_is_nonblank "$ENV_FILE" "$k"; then
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

# 9. Hubify CLI (optional to run the paper loop; required for Hubify status) --
if have hubify; then
  if hubify status >/dev/null 2>&1; then
    row PASS "Hubify CLI auth" "authenticated (status query succeeded; output hidden)"
  else
    row WARN "Hubify CLI auth" "installed but unauthenticated — run 'hubify auth login' or restore HUBIFY_TOKEN; paper loop remains runnable"
  fi
else
  row WARN "Hubify CLI" "not installed — Hubify lab/status checks unavailable; paper loop remains runnable"
fi

# 10. lab lease tool + headed-browser note -----------------------------------
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
