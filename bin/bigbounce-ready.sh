#!/usr/bin/env bash
# bigbounce-ready — one-shot readiness check for the INT/EXT paper-review +
# self-improvement loop. READ-ONLY: verifies the loop skills, review engine,
# secrets, python vendor SDKs, and LaTeX/PDF toolchain, then prints the current
# SSOT state. Exit 0 = ready to run the loop; exit 1 = gaps (with fix commands).
#
# Usage:  bash bin/bigbounce-ready.sh      (or: ./bin/bigbounce-ready.sh)
# Skill:  /bigbounce-ready                 (scistack/astrostack)
set -uo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS="$HOME/.claude/skills"
ok=0; bad=0
chk() { if eval "$2" >/dev/null 2>&1; then printf "  \033[32m✓\033[0m %s\n" "$1"; ok=$((ok+1)); else printf "  \033[31m✗\033[0m %s\n" "$1"; bad=$((bad+1)); fi; }

echo ""
echo "  bigbounce readiness — $REPO"
echo ""
echo "  loop skills (scistack synced):"
for s in cross-vendor-r-round peer-review-truth-audit bigbounce-truth-audit bigbounce-close \
         r-round-finding-archive r-round-pattern-mine paper-pre-review-check \
         external-review-browser-loop cascaded-r-rounds bigbounce-status; do
  chk "$s" "[ -e '$SKILLS/$s' ]"
done
echo "  review engine + secrets:"
chk "tools/v3_native_pdf_review.py" "[ -f '$REPO/tools/v3_native_pdf_review.py' ]"
chk ".env.local present"            "[ -f '$REPO/.env.local' ]"
chk "requirements.txt"             "[ -f '$REPO/requirements.txt' ]"
echo "  python vendor SDKs:"
chk "anthropic"                    "python3 -c 'import anthropic'"
chk "openai"                       "python3 -c 'import openai'"
chk "google.generativeai"          "python3 -c 'import google.generativeai'"
echo "  latex/pdf toolchain:"
chk "pdflatex"                     "command -v pdflatex"
chk "pdftoppm (poppler)"           "command -v pdftoppm"
chk "SSOT/index.md"                "[ -f '$REPO/project-context/SSOT/index.md' ]"

echo ""
if [ -f "$REPO/project-context/SSOT/index.md" ]; then
  echo "  ── current state (SSOT/index.md) ──"
  sed -n '1,12p' "$REPO/project-context/SSOT/index.md" | sed 's/^/  /'
fi
echo ""
if [ "$bad" -eq 0 ]; then
  printf "  \033[32mREADY\033[0m — %s checks passed. In Claude Code (this repo) say: START EVERYTHING UP\n\n" "$ok"
  exit 0
fi
printf "  \033[31mNOT READY\033[0m — %s gap(s). Fixes:\n" "$bad"
echo "    skills missing  → git -C ~/.claude/scistack pull --ff-only && ~/.claude/scistack/bin/sync-to-claude.sh"
echo "    .env.local      → you env vault pull --restore --root \"$(dirname "$REPO")\" --map-existing --existing-only --skip-agent-auth"
echo "    python SDKs     → pip install -r \"$REPO/requirements.txt\" openai google-generativeai"
echo "    toolchain       → brew install --cask mactex-no-gui && brew install poppler"
echo ""
exit 1
