#!/usr/bin/env bash
# directive_g.sh — one-shot per-paper PDF hygiene chain (bigbounce directive-G).
#
# Runs the FULL directive-G HARD-GATE chain in one command so owner-agents never
# hand-do (and never half-do) the 5-step chain again. Idempotent: rerunning with
# the same version is a safe re-mirror + re-bump-verify (a duplicate Convex bump
# row is acceptable — the site reads the newest matching row).
#
# The owner bumps \paperVersion + \date in the .tex BEFORE calling this. This
# script VERIFIES that (never edits paper content), then:
#   1. verify tex version + date
#   2. leak-gate grep (reviewer/internal terms must not leak into served content)
#   3. compile (TinyTeX pdflatex 2-pass + bibtex if bib present → 2 more passes)
#   4. mirror byte-identical to every served path + create versioned aliases
#   5. Convex paperVersions:bump + read-back verify
#   6. one-line PASS summary
#
# Usage: tools/directive_g.sh <P1U|P2|P3|P4|P5> <new-version> "<changelog>"
#
# See canonical spec: ~/.claude/scistack/astrostack/bigbounce-r-round/SKILL.md
#   §"directive-G one-shot: tools/directive_g.sh".

set -euo pipefail

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
REPO="/Users/houstongolden/Desktop/CODE_YOU/bigbounce"
TINYTEX_BIN="$HOME/Library/TinyTeX/bin/universal-darwin"
CONVEX_URL="https://brilliant-panther-471.convex.cloud/api/mutation"
CONVEX_QUERY_URL="https://brilliant-panther-471.convex.cloud/api/query"

# paper -> tex path + canonical Convex slug. macOS ships bash 3.2 (no
# associative arrays), so these are plain case lookups.
# TEX paths are relative to $REPO; the PDF is the sibling <name>.pdf.
# Slugs are the canonical site slugs (Lesson 2026-07-10: NEVER invent slugs;
# note P1U -> paper-1a, where the unified P1 lives).
tex_for_paper() {
  case "$1" in
    P1U) echo "arxiv/paper1_unified.tex" ;;
    P2)  echo "research/focused_paper_source_integration/02_full_draft.tex" ;;
    P3)  echo "pipelines/p3_anomaly_engine/paper3_draft.tex" ;;
    P4)  echo "pipelines/p2_chirality/chirality_catalog_paper.tex" ;;
    P5)  echo "pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex" ;;
    *)   echo "" ;;
  esac
}
slug_for_paper() {
  case "$1" in
    P1U) echo "paper-1a" ;;
    P2)  echo "paper-2" ;;
    P3)  echo "paper-3" ;;
    P4)  echo "paper-4" ;;
    P5)  echo "paper-5" ;;
    *)   echo "" ;;
  esac
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
die() { echo "FAIL: $*" >&2; exit 1; }

md5of() { md5 -q "$1"; }

pages_of() {
  local pdf="$1" n=""
  if command -v pdfinfo >/dev/null 2>&1; then
    n=$(pdfinfo "$pdf" 2>/dev/null | awk '/^Pages:/ {print $2}')
  fi
  if [ -z "$n" ]; then
    n=$(python3 - "$pdf" <<'PY'
import sys
try:
    from pypdf import PdfReader
except Exception:
    from PyPDF2 import PdfReader
print(len(PdfReader(sys.argv[1]).pages))
PY
)
  fi
  [ -n "$n" ] || die "could not determine page count of $pdf"
  echo "$n"
}

# ---------------------------------------------------------------------------
# Args
# ---------------------------------------------------------------------------
[ $# -eq 3 ] || die "usage: tools/directive_g.sh <P1U|P2|P3|P4|P5> <new-version> \"<changelog>\""
PAPER="$1"; NEWVER="$2"; CHANGELOG="$3"

TEX_REL="$(tex_for_paper "$PAPER")"
SLUG="$(slug_for_paper "$PAPER")"
[ -n "$TEX_REL" ] && [ -n "$SLUG" ] || die "unknown paper key '$PAPER' (want P1U|P2|P3|P4|P5)"

cd "$REPO"
TEX="$REPO/$TEX_REL"
[ -f "$TEX" ] || die "tex not found: $TEX"
TEX_DIR="$(dirname "$TEX")"
TEX_BASE="$(basename "$TEX" .tex)"        # e.g. p5_desi_chirality
SRC_PDF="$TEX_DIR/$TEX_BASE.pdf"

# Current human date "July D, YYYY" derived from `date` (no leading zero on day).
TODAY_HUMAN="$(date '+%B %-d, %Y')"       # e.g. "July 10, 2026"

echo "=== directive_g.sh :: $PAPER $NEWVER (slug=$SLUG) ==="
echo "    tex:  $TEX_REL"
echo "    date: $TODAY_HUMAN"

# ---------------------------------------------------------------------------
# STEP 1 — verify tex already carries the new version + today's date
# ---------------------------------------------------------------------------
echo "--- step 1: verify tex version + date ---"
grep -qF "$NEWVER" "$TEX" \
  || die "tex does NOT contain version '$NEWVER' — owner must bump \\paperVersion first (this script never edits content)"
grep -qF "$TODAY_HUMAN" "$TEX" \
  || die "tex \\date does NOT contain today '$TODAY_HUMAN' — owner must bump \\date first"
echo "    ok: version + date present in tex"

# ---------------------------------------------------------------------------
# STEP 2 — leak-gate: no reviewer/internal terms in served (non-comment,
#          non-AI-disclosure) content.
# ---------------------------------------------------------------------------
echo "--- step 2: leak-gate ---"
LEAK_PAT='ChatGPT|Gemini|Grok|referee pass|review round|reviewer noted|truth-audit|pattern-0'
# Exclude: comment lines (^ optional-ws %) AND the legit AI-assisted-methodology
# disclosure/acknowledgment paragraph (which names the cross-checking models).
DISCLOSURE_PAT='AI-assisted methodology|AI assist|adversarial internal-review|cross-checking and adversarial|used as cross-checking'
LEAKS="$(grep -nE "$LEAK_PAT" "$TEX" \
  | grep -vE '^[0-9]+:\s*%' \
  | grep -vE "$DISCLOSURE_PAT" || true)"
if [ -n "$LEAKS" ]; then
  echo "$LEAKS" >&2
  die "leak-gate: reviewer/internal terms found in served content (lines above)"
fi
echo "    ok: no leaks in served content"

# ---------------------------------------------------------------------------
# STEP 3 — compile (TinyTeX)
# ---------------------------------------------------------------------------
echo "--- step 3: compile ---"
[ -x "$TINYTEX_BIN/pdflatex" ] || die "pdflatex not found at $TINYTEX_BIN"
PDFLATEX="$TINYTEX_BIN/pdflatex"
BIBTEX="$TINYTEX_BIN/bibtex"
LOG="$TEX_DIR/$TEX_BASE.log"

# Does the paper use a bib? (external .bib + \bibliography, not inline thebibliography)
USE_BIB=0
if grep -qE '\\bibliography\{' "$TEX" && ls "$TEX_DIR"/*.bib >/dev/null 2>&1; then
  USE_BIB=1
fi

run_pdflatex() {
  ( cd "$TEX_DIR" && "$PDFLATEX" -interaction=nonstopmode -halt-on-error "$TEX_BASE.tex" ) \
    >/dev/null 2>&1 || true   # non-zero exit is inspected via log below, not trusted directly
}

run_pdflatex
run_pdflatex
if [ "$USE_BIB" -eq 1 ]; then
  echo "    (bibtex leg)"
  ( cd "$TEX_DIR" && "$BIBTEX" "$TEX_BASE" ) >/dev/null 2>&1 || true
  run_pdflatex
  run_pdflatex
fi

[ -f "$SRC_PDF" ] || die "compile produced no PDF at $SRC_PDF"

# Hard checks: LaTeX errors ("^!") and undefined references.
# grep -c exits 1 on zero matches; capture the count without tripping set -e.
ERRC=$(grep -c '^!' "$LOG" 2>/dev/null) || ERRC=0
[ "$ERRC" -eq 0 ] || { grep -n '^!' "$LOG" | head; die "compile: $ERRC LaTeX error line(s) in log"; }
UNDEF=$(grep -c 'LaTeX Warning: Reference.*undefined' "$LOG" 2>/dev/null) || UNDEF=0
[ "$UNDEF" -eq 0 ] || { grep -n 'Reference.*undefined' "$LOG" | head; die "compile: $UNDEF undefined reference(s)"; }
CITEUNDEF=$(grep -c 'Citation.*undefined' "$LOG" 2>/dev/null) || CITEUNDEF=0
[ "$CITEUNDEF" -eq 0 ] || echo "    WARN: $CITEUNDEF undefined citation(s) (not a hard fail)"

# Overfull hboxes > 50pt (warn only). Portable (BSD awk): pull the pt value
# out of "Overfull \hbox (NNNpt too wide)" and threshold it.
OVERFULL="$(grep -E 'Overfull \\hbox \([0-9.]+pt' "$LOG" 2>/dev/null \
  | awk '{ if (match($0, /\([0-9.]+pt/)) { v=substr($0, RSTART+1, RLENGTH-3)+0; if (v > 50) print } }' || true)"
if [ -n "$OVERFULL" ]; then
  echo "    WARN overfull >50pt hboxes:"
  echo "$OVERFULL" | sed 's/^/      /'
else
  echo "    ok: no overfull >50pt hboxes"
fi
echo "    ok: 0 errors, 0 undefined refs"

# ---------------------------------------------------------------------------
# STEP 4 — mirror byte-identical to every served path + versioned aliases
# ---------------------------------------------------------------------------
echo "--- step 4: mirror ---"
NEWMD5="$(md5of "$SRC_PDF")"
NEWSIZE="$(stat -f%z "$SRC_PDF")"
NEWPAGES="$(pages_of "$SRC_PDF")"

# Discover the previous served set: every tracked (non-worktree, non-.git) file
# whose basename derives from this paper's PDF basename. This yields the exact
# per-paper allowlist of served locations WITHOUT a broad cross-paper pattern:
# we match ONLY files named "<base>.pdf", "<base>_<ver>.pdf", or short aliases
# that already sit beside a "<base>.pdf" in a served dir.
#
# Served base filenames for this paper (unversioned canonical name + known
# short aliases living next to it):
BASE_PDF_NAME="$TEX_BASE.pdf"

# Collect candidate served files: any *.pdf under the known served roots whose
# name starts with the paper base (covers versioned aliases) OR equals a short
# alias that currently md5-matches the CURRENT source (safe: only touch files
# that were the previous byte-identical mirror).
PREV_MD5=""   # md5 of the previously-served base copy, to find its aliases
if [ -f "site/public/$BASE_PDF_NAME" ]; then PREV_MD5="$(md5of "site/public/$BASE_PDF_NAME")"; fi

SERVED_ROOTS=(
  "site/public"
  "site/public/papers"
  "public/papers"
  "site/out"
  "site/out/papers"
  "$TEX_DIR"
)

declare -a MIRROR_TARGETS=()

# (a) canonical unversioned base copies in each served root that already has one
for root in "${SERVED_ROOTS[@]}"; do
  if [ -f "$root/$BASE_PDF_NAME" ]; then
    MIRROR_TARGETS+=("$root/$BASE_PDF_NAME")
  fi
done

# (b) short aliases that currently md5-match the previous base copy (e.g.
#     p5-chirality.pdf). Only in roots holding the base copy; only if md5==PREV.
if [ -n "$PREV_MD5" ]; then
  for root in "${SERVED_ROOTS[@]}"; do
    [ -d "$root" ] || continue
    while IFS= read -r f; do
      [ -f "$f" ] || continue
      bn="$(basename "$f")"
      # skip the canonical base + any versioned <base>_v...pdf (handled elsewhere)
      case "$bn" in
        "$BASE_PDF_NAME") continue ;;
        "$TEX_BASE"_v*) continue ;;
      esac
      # only adopt a short alias if it was the previous byte-identical mirror
      if [ "$(md5of "$f")" = "$PREV_MD5" ]; then
        MIRROR_TARGETS+=("$f")
      fi
    done < <(find "$root" -maxdepth 1 -type f -name '*.pdf' 2>/dev/null)
  done
fi

# (c) versioned aliases: create/refresh <base>_<version>.pdf in the two papers/
#     dirs that hold versioned aliases (site/public/papers + public/papers),
#     following the existing naming convention.
for aroot in "site/public/papers" "public/papers"; do
  [ -d "$aroot" ] || continue
  MIRROR_TARGETS+=("$aroot/${TEX_BASE}_${NEWVER}.pdf")
done

# de-dup targets (bash 3.2 safe — no readarray)
DEDUP="$(printf '%s\n' "${MIRROR_TARGETS[@]}" | awk 'NF && !seen[$0]++')"
MIRROR_TARGETS=()
while IFS= read -r t; do
  [ -n "$t" ] && MIRROR_TARGETS+=("$t")
done <<EOF
$DEDUP
EOF

NCOPIED=0
SRC_ABS="$(cd "$(dirname "$SRC_PDF")" && pwd)/$(basename "$SRC_PDF")"
for tgt in "${MIRROR_TARGETS[@]}"; do
  mkdir -p "$(dirname "$tgt")"
  tgt_abs="$(cd "$(dirname "$tgt")" && pwd)/$(basename "$tgt")"
  # The source PDF is itself a served path (lives in the tex dir); don't cp onto
  # itself, but still count + md5-verify it as a mirror.
  if [ "$tgt_abs" != "$SRC_ABS" ]; then
    cp -f "$SRC_PDF" "$tgt"
  fi
  got="$(md5of "$tgt")"
  [ "$got" = "$NEWMD5" ] || die "mirror md5 mismatch at $tgt ($got != $NEWMD5)"
  NCOPIED=$((NCOPIED+1))
done
echo "    ok: mirrored to $NCOPIED path(s), all md5==$NEWMD5"

# ---------------------------------------------------------------------------
# STEP 5 — Convex bump + read-back verify
# ---------------------------------------------------------------------------
echo "--- step 5: convex bump ---"
TEXCOMMIT="$(git rev-parse --short HEAD)"
SITE_PDF_PATH="/papers/${TEX_BASE}_${NEWVER}.pdf"

BUMP_PAYLOAD="$(python3 - "$SLUG" "$NEWVER" "$TODAY_HUMAN" "$TEXCOMMIT" "$NEWMD5" "$NEWPAGES" "$NEWSIZE" "$CHANGELOG" "$SITE_PDF_PATH" <<'PY'
import json, sys
slug, ver, datestamp, commit, md5, pages, size, changelog, sitepath = sys.argv[1:10]
print(json.dumps({
  "path": "paperVersions:bump",
  "args": {
    "paperSlug": slug,
    "version": ver,
    "datestamp": datestamp,
    "texCommit": commit,
    "pdfMd5": md5,
    "pdfPages": int(pages),
    "pdfSizeBytes": int(size),
    "changelog": changelog,
    "sitePdfPath": sitepath,
  },
  "format": "json",
}))
PY
)"

BUMP_RESP="$(curl -sS -X POST "$CONVEX_URL" \
  -H 'Content-Type: application/json' \
  -d "$BUMP_PAYLOAD")"
echo "    bump response: $BUMP_RESP"
echo "$BUMP_RESP" | python3 -c 'import sys,json; d=json.load(sys.stdin); sys.exit(0 if d.get("status")=="success" else 1)' \
  || die "convex bump did not return status=success"
ROWID="$(echo "$BUMP_RESP" | python3 -c 'import sys,json; print(json.load(sys.stdin).get("value",""))')"

# read-back verify current row matches version + md5. The query can transiently
# return an empty body immediately after the mutation, so query+verify together
# inside a retry loop and only fail after all attempts are exhausted.
QUERY_BODY="$(python3 - "$SLUG" <<'PY'
import json,sys
print(json.dumps({"path":"paperVersions:current","args":{"paperSlug":sys.argv[1]},"format":"json"}))
PY
)"
# Verifier reads the response body from stdin and want-version/md5 from argv.
VERIFY_PY="$REPO/tools/.directive_g_verify.py"
cat > "$VERIFY_PY" <<'PY'
import sys, json
want_ver, want_md5 = sys.argv[1], sys.argv[2]
raw = sys.stdin.read()
try:
    d = json.loads(raw)
except Exception as e:
    print(f"unparseable: {e}"); sys.exit(1)
if d.get("status") != "success":
    print("query status != success"); sys.exit(1)
v = d.get("value") or {}
if v.get("version") != want_ver or v.get("pdfMd5") != want_md5:
    print(f"mismatch: got {v.get('version')}/{v.get('pdfMd5')} want {want_ver}/{want_md5}"); sys.exit(1)
print("ok")
PY
trap 'rm -f "$VERIFY_PY"' EXIT

VERIFY_OK=0
LAST_ERR=""
for attempt in 1 2 3 4 5 6 7 8; do
  CUR_RESP="$(curl -sS -X POST "$CONVEX_QUERY_URL" -H 'Content-Type: application/json' -d "$QUERY_BODY" 2>/dev/null || true)"
  if [ -z "$CUR_RESP" ]; then LAST_ERR="empty response"; sleep 1; continue; fi
  MSG="$(printf '%s' "$CUR_RESP" | python3 "$VERIFY_PY" "$NEWVER" "$NEWMD5" 2>&1)" && { VERIFY_OK=1; break; }
  LAST_ERR="$MSG"
  sleep 1
done
[ "$VERIFY_OK" -eq 1 ] || die "convex read-back verify failed: $LAST_ERR"
echo "    ok: convex current == $NEWVER / $NEWMD5 (row $ROWID)"

# ---------------------------------------------------------------------------
# STEP 6 — PASS summary
# ---------------------------------------------------------------------------
echo "PASS: $PAPER $NEWVER md5=$NEWMD5 pages=$NEWPAGES mirrored=$NCOPIED convexRow=$ROWID"
