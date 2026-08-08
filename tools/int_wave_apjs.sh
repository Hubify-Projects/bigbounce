#!/usr/bin/env bash
# Compatibility entry point for the P3 ApJS review wave.
#
# P3's canonical paper_registry entry already selects paper3_apjs.tex/.pdf,
# The Astrophysical Journal Supplement Series, and the APJS-CATALOG profile.
# Keep one dispatch implementation so Codex subscription, Grok, and Gemini all
# inherit the same six-paper preflight, immutable packet, receipt, and policy
# gates from int_wave.sh.

set -euo pipefail

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
REPO="$(cd "$SCRIPT_DIR/.." && pwd)"
DATESTAMP="$(date +%Y-%m-%d)"

export INT_OUTDIR="${INT_OUTDIR:-$REPO/project-context/peer-reviews/INT_apjs/$DATESTAMP}"
export INT_SUBSCRIPTION_OUTDIR="${INT_SUBSCRIPTION_OUTDIR:-$INT_OUTDIR}"

exec "$REPO/tools/int_wave.sh" P3 "${1:-}"
