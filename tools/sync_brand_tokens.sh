#!/usr/bin/env bash
# Re-sync site/src/styles/brand.tokens.css from the canonical hubify token
# file, then re-apply the lab's one allowed divergence (teal --accent).
# Idempotent: a second run with no upstream/local changes is a no-op.
# Fails loudly with a diff (exit 1, no write) if the existing local copy
# has drifted from a fresh rebuild — pass --force to accept the rebuild.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HUBIFY_BRAND="/Users/houstongolden/Desktop/CODE_YOU/hubify/packages/brand/tokens.css"
DEST="$REPO_ROOT/site/src/styles/brand.tokens.css"
FORCE="${1:-}"
SOURCE_COMMIT="$(git -C "$(dirname "$HUBIFY_BRAND")" rev-parse --short=8 HEAD 2>/dev/null || echo unknown)"

[[ -f "$HUBIFY_BRAND" ]] || { echo "FAIL: canonical token file not found at $HUBIFY_BRAND" >&2; exit 1; }

TMP="$(mktemp)"; trap 'rm -f "$TMP"' EXIT
{
  echo "/* ── SYNCED COPY — DO NOT EDIT HERE. ─────────────────────────────────"
  echo "   Source: hubify/packages/brand/tokens.css @ commit ${SOURCE_COMMIT}"
  echo "   Synced: $(date +%F) via bigbounce/tools/sync_brand_tokens.sh"
  echo "   Edit the canonical file in hubify and re-run this script. ── */"
  echo
  cat "$HUBIFY_BRAND"
  echo
  echo "/* ── BigBounce Lab differentiator (the ONE allowed divergence) ── */"
  echo ':root { --accent: #26685f; --accent-ink: #1b4f48; --on-accent: #f8f6f0; }'
  echo '@media (prefers-color-scheme: dark) {'
  echo '  :root:not([data-theme="light"]) { --accent: #5fb0a4; --accent-ink: #84d2c6; --on-accent: #0a0a0a; }'
  echo '}'
  echo ':root[data-theme="dark"] { --accent: #5fb0a4; --accent-ink: #84d2c6; --on-accent: #0a0a0a; }'
} > "$TMP"

if [[ -f "$DEST" ]] && ! diff -q <(tail -n +6 "$DEST") <(tail -n +6 "$TMP") > /dev/null; then
  if [[ "$FORCE" != "--force" ]]; then
    echo "DRIFT DETECTED between $DEST and a fresh rebuild:" >&2
    diff -u <(tail -n +6 "$DEST") <(tail -n +6 "$TMP") >&2 || true
    echo "FAIL: re-run with --force to accept the rebuild, or investigate the hand-edit." >&2
    exit 1
  fi
fi

cp "$TMP" "$DEST"
echo "OK: synced $DEST from $HUBIFY_BRAND (commit ${SOURCE_COMMIT})"
