#!/usr/bin/env bash
# directive_g.sh — one-shot per-paper PDF hygiene chain (bigbounce directive-G).
#
# Runs the FULL directive-G HARD-GATE chain in one command so owner-agents never
# hand-do (and never half-do) the 7-step chain again. Idempotent: rerunning with
# the same version is a safe re-mirror + re-bump-verify (a duplicate Convex bump
# row is acceptable — the site reads the newest matching row).
#
# The owner bumps \paperVersion + \date in the .tex BEFORE calling this. This
# script VERIFIES that (never edits paper content), then:
#   1. verify tex version + date
#   2. leak-gate grep (reviewer/internal terms must not leak into served content)
#   3. compile (TinyTeX pdflatex 2-pass + bibtex if bib present → 2 more passes)
#   4. append-only retention snapshot (normal mode only; fail closed)
#   5. mirror byte-identical to every served path + create versioned aliases
#   6. Convex paperVersions:bump + read-back verify
#   7. one-line PASS summary
#
# Usage: tools/directive_g.sh [--verify-only] <P1A|P1B|P2|P3|P4|P5> <new-version> "<changelog>"
#
#   --verify-only : run the step 1-2-3 checks (tex version+date, leak-gate,
#                   compile) + md5 comparison of the already-served mirrors + the
#                   Convex read-back, WITHOUT writing retention state,
#                   re-mirroring, or re-bumping. Use to
#                   validate current state (2026-07-10 lesson: a full validation
#                   re-run re-inserts the version with a newer createdAt and can
#                   steal "current" under the same-datestamp tie-break — verify-only
#                   never writes Convex, so it never displaces the true current).
#
# See canonical spec: ~/.claude/scistack/astrostack/bigbounce-r-round/SKILL.md
#   §"directive-G one-shot: tools/directive_g.sh".

set -euo pipefail

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
REPO="$(cd "$SCRIPT_DIR/.." && pwd)"
REGISTRY="$REPO/tools/paper_registry.py"
RETENTION="$REPO/tools/pdf_version_retention.py"
TINYTEX_BIN="$HOME/Library/TinyTeX/bin/universal-darwin"
CONVEX_URL="https://brilliant-panther-471.convex.cloud/api/mutation"
CONVEX_QUERY_URL="https://brilliant-panther-471.convex.cloud/api/query"

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
VERIFY_ONLY=0
if [ "${1:-}" = "--verify-only" ]; then
  VERIFY_ONLY=1
  shift
fi
[ $# -eq 3 ] || die "usage: tools/directive_g.sh [--verify-only] <P1A|P1B|P2|P3|P4|P5> <new-version> \"<changelog>\""
PAPER="$1"; NEWVER="$2"; CHANGELOG="$3"

TEX_REL="$(python3 "$REGISTRY" "$PAPER" tex_path 2>/dev/null)"
SLUG="$(python3 "$REGISTRY" "$PAPER" site_slug 2>/dev/null)"
REVIEW_PROFILE="$(python3 "$REGISTRY" "$PAPER" review_profile 2>/dev/null)"
SERVED_ALIASES="$(python3 "$REGISTRY" "$PAPER" served_aliases 2>/dev/null)"
[ -n "$TEX_REL" ] && [ -n "$SLUG" ] && [ -n "$REVIEW_PROFILE" ] \
  || die "unknown paper key '$PAPER' (want P1A|P1B|P2|P3|P4|P5)"

cd "$REPO"
TEX="$REPO/$TEX_REL"
[ -f "$TEX" ] || die "tex not found: $TEX"
TEX_DIR="$(dirname "$TEX")"
TEX_BASE="$(basename "$TEX" .tex)"        # e.g. p5_desi_chirality
SRC_PDF="$TEX_DIR/$TEX_BASE.pdf"

# Current human date "July D, YYYY" derived from `date` (no leading zero on day).
TODAY_HUMAN="$(date '+%B %-d, %Y')"       # e.g. "July 10, 2026"

MODE_LABEL=""
[ "$VERIFY_ONLY" -eq 1 ] && MODE_LABEL=" [VERIFY-ONLY]"
echo "=== directive_g.sh :: $PAPER $NEWVER (slug=$SLUG)$MODE_LABEL ==="
[ "$VERIFY_ONLY" -eq 1 ] && echo "    mode: VERIFY-ONLY (no re-mirror, no Convex bump)"
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
# STEP 4 — append-only PDF retention (normal mode only)
# ---------------------------------------------------------------------------
if [ "$VERIFY_ONLY" -eq 1 ]; then
  echo "--- step 4: append-only retention (verify-only — skipped, no archive writes) ---"
else
  echo "--- step 4: append-only retention ---"
  [ -f "$RETENTION" ] || die "retention tool not found: $RETENTION"
  LATEX_PASSES=2
  [ "$USE_BIB" -eq 1 ] && LATEX_PASSES=4
  RETENTION_BUILD_METADATA="tools/directive_g.sh paper=${PAPER} version=${NEWVER} source=${TEX_REL} pdflatex_passes=${LATEX_PASSES} bibtex=${USE_BIB}"
  RETENTION_REVIEW_METADATA="directive-g/${REVIEW_PROFILE}/${PAPER}/${NEWVER}"
  RETENTION_JSON=""
  if ! RETENTION_JSON="$(python3 "$RETENTION" \
      --paper "$PAPER" \
      --build-command "$RETENTION_BUILD_METADATA" \
      --review-round "$RETENTION_REVIEW_METADATA" 2>&1)"; then
    [ -n "$RETENTION_JSON" ] && echo "$RETENTION_JSON" >&2
    die "append-only retention failed; refusing to mirror or mutate Convex"
  fi
  RETENTION_MANIFEST="$(printf '%s' "$RETENTION_JSON" | python3 -c '
import json, pathlib, sys
paper, version, build, review = sys.argv[1:5]
payload = json.load(sys.stdin)
rows = payload.get("papers") or []
if len(rows) != 1 or rows[0].get("paper_id") != paper or rows[0].get("paper_version") != version:
    raise SystemExit("retention receipt paper/version mismatch")
if payload.get("build_command") != build or payload.get("review_round") != review:
    raise SystemExit("retention receipt metadata mismatch")
manifest = payload.get("manifest_path")
if not isinstance(manifest, str) or not manifest:
    raise SystemExit("retention receipt missing manifest_path")
print(manifest)
' "$PAPER" "$NEWVER" "$RETENTION_BUILD_METADATA" "$RETENTION_REVIEW_METADATA")" \
    || die "append-only retention returned an invalid receipt; refusing to mirror or mutate Convex"
  case "$RETENTION_MANIFEST" in
    /*) RETENTION_MANIFEST_ABS="$RETENTION_MANIFEST" ;;
    *) RETENTION_MANIFEST_ABS="$REPO/$RETENTION_MANIFEST" ;;
  esac
  [ -f "$RETENTION_MANIFEST_ABS" ] \
    || die "retention manifest not found after snapshot: $RETENTION_MANIFEST"
  echo "    manifest: $RETENTION_MANIFEST"
  echo "    ok: compiled PDF retained before any mirror or Convex mutation"
fi

# ---------------------------------------------------------------------------
# STEP 5 — mirror byte-identical to every served path + versioned aliases
# ---------------------------------------------------------------------------
echo "--- step 5: mirror ---"
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

# 2026-07-24: this list is the enforced set, so anything it omits is a place a
# superseded PDF can sit forever without directive G ever looking at it. The
# reverse-direction sweep (tools/verify_pdf_mirror_integrity.py) found 31 such
# orphans across 13 documents -- every one of them outside the roots below. The
# bare "public" root (which serves at /<name>.pdf) and the downloads/ roots are
# added here so a future mirror cannot land outside the enforced set again.
# Missing directories are skipped by the guards below, so listing a root that
# does not exist today is free and keeps the next one from being a blind spot.
SERVED_ROOTS=(
  "site/public"
  "site/public/papers"
  "site/public/downloads"
  "public"
  "public/papers"
  "public/downloads"
  "site/out"
  "site/out/papers"
  "site/out/downloads"
  "$TEX_DIR"
)

declare -a MIRROR_TARGETS=()

# (a) canonical unversioned base copies. The two public papers roots are
# mandatory even when a major restructure introduces a brand-new PDF basename;
# otherwise discovery from pre-existing files creates only versioned aliases.
for root in "site/public/papers" "public/papers"; do
  [ -d "$root" ] || continue
  MIRROR_TARGETS+=("$root/$BASE_PDF_NAME")
done

# Preserve any additional canonical unversioned locations already in use.
for root in "${SERVED_ROOTS[@]}"; do
  if [ -f "$root/$BASE_PDF_NAME" ]; then
    MIRROR_TARGETS+=("$root/$BASE_PDF_NAME")
  fi
done

# (b) registry-owned legacy aliases. Explicit ownership is both faster and safer
# than hashing every PDF in every served directory, and it still repairs an alias
# whose bytes have already drifted from the canonical copy.
while IFS= read -r alias; do
  [ -n "$alias" ] || continue
  for root in "${SERVED_ROOTS[@]}"; do
    [ -f "$root/$alias" ] && MIRROR_TARGETS+=("$root/$alias")
  done
done <<EOF
$SERVED_ALIASES
EOF

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
if [ "$VERIFY_ONLY" -eq 1 ]; then
  # Compare-only: validate the CURRENTLY-SERVED set is internally byte-identical
  # and matches what Convex records — do NOT compare against the fresh recompile
  # (a recompile is non-reproducible: it re-embeds a build /CreationDate, so its
  # md5 differs from a committed PDF even with identical content). The reference
  # is the canonical served copy site/public/<base>.pdf (PREV_MD5). Step 3 still
  # confirms the source COMPILES clean; this step confirms served coherence.
  [ -n "$PREV_MD5" ] || die "verify-only: no canonical served copy at site/public/$BASE_PDF_NAME to reference"
  REFMD5="$PREV_MD5"
  MISMATCH=0
  for tgt in "${MIRROR_TARGETS[@]}"; do
    tgt_abs="$(cd "$(dirname "$tgt")" && pwd)/$(basename "$tgt")"
    if [ "$tgt_abs" = "$SRC_ABS" ]; then
      echo "    (skip freshly compiled canonical source in served compare: ${tgt#$REPO/})"
      continue
    fi
    if [ ! -f "$tgt" ]; then
      # versioned aliases for a not-yet-mirrored version are expected-absent;
      # only flag absence of the unversioned canonical copies.
      case "$(basename "$tgt")" in
        "$TEX_BASE"_*) echo "    (skip absent versioned alias: ${tgt#$REPO/})"; continue ;;
        *) echo "    MISMATCH: served copy missing: $tgt" >&2; MISMATCH=1; continue ;;
      esac
    fi
    got="$(md5of "$tgt")"
    if [ "$got" = "$REFMD5" ]; then
      NCOPIED=$((NCOPIED+1))
    else
      echo "    MISMATCH: $tgt md5=$got != canonical-served $REFMD5" >&2
      MISMATCH=1
    fi
  done
  [ "$MISMATCH" -eq 0 ] || die "verify-only: served mirror(s) not byte-identical to canonical served copy (above)"
  # For the Convex read-back below, the served set (not the recompile) is truth.
  NEWMD5="$REFMD5"
  echo "    ok: $NCOPIED served path(s) byte-identical, md5==$REFMD5 (compare-only, nothing re-mirrored)"
else
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
fi

# ---------------------------------------------------------------------------
# STEP 6 — Convex bump + read-back verify
# ---------------------------------------------------------------------------
if [ "$VERIFY_ONLY" -eq 1 ]; then
  echo "--- step 6: convex read-back (verify-only — no bump) ---"
  ROWID="(verify-only)"
else
  echo "--- step 6: convex bump ---"
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
fi

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
# STEP 7 — PASS summary
# ---------------------------------------------------------------------------
if [ "$VERIFY_ONLY" -eq 1 ]; then
  echo "PASS [verify-only]: $PAPER $NEWVER md5=$NEWMD5 pages=$NEWPAGES served=$NCOPIED convex=current-match (no writes)"
else
  echo "PASS: $PAPER $NEWVER md5=$NEWMD5 pages=$NEWPAGES mirrored=$NCOPIED convexRow=$ROWID"
fi
