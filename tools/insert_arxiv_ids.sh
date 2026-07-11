#!/usr/bin/env bash
# ============================================================================
# insert_arxiv_ids.sh — wave-2 arXiv-ID insertion automation (bigbounce)
# ----------------------------------------------------------------------------
# ############################################################################
# # ⚠ MERGED-LAYOUT NOTE (2026-07-09 — READ BEFORE RUNNING) ################### #
# ############################################################################
# WAVE-2 IS NOW:  P5 v0.1.118 (45pp)  +  the UNIFIED Paper 1 (P1U, v1U.0.11, 60pp,
#                 bundle submissions/P1A/arxiv_p1_unified_v1U.0.11.tar.gz).
# WAVE-1 IS:      P4 v1.0.235 (35pp) -> P3 v3.1.152 (37pp) -> P2 v1.7.111 (38pp).
#
# P1B is MERGED into P1U — there is NO standalone P1B submission and NO
# reciprocal P1B_V2 note. The Step-1 P5 \paperIVarxiv leg below is still
# CORRECT. The Step-2/3 legs (P1A bib fill + P1B reciprocal) are STALE: they
# target arxiv/paper1a_ech_nogo.tex, which is the pre-merge P1A, not P1U.
#
# For P1U, the wave-2 ID insertion is done in arxiv/references.bib (the shared
# bib P1U compiles against). Grep of arxiv/paper1_unified.tex + references.bib
# (2026-07-09) — the ONLY live wave-2 placeholders are the TODO-SUBMISSION
# companion bib entries in arxiv/references.bib:
#     Golden2026P1a  -> [arXiv:XXXX.XXXXX --- ID inserted at coordinated submission]
#                       *** P1U's OWN forward-ref — LEAVE AS-IS (P1U's ID does
#                           not exist until P1U itself is assigned in wave-2) ***
#     Golden2026P1b  -> "posted concurrently on arXiv"  (companion, now folded;
#                        harmless — fill with the P1U ID at v2 or leave)
#     Golden2026P2   -> fill with the real P2 wave-1 ID
#     Golden2026P3   -> fill with the real P3 wave-1 ID
#     Golden2026P4   -> fill with the real P4 wave-1 ID
#   (Golden2026P2's bib TITLE still reads "-35/8"; the P1U BODY uses -35/16 —
#    the title string is cosmetic bib metadata, not a rendered science claim,
#    but tidy it to -35/16 if editing anyway.)
# The paper1_unified.tex body carries only PROSE "coordinated submission /
# posted concurrently" wording (lines ~1372, ~1602) — no XXXX ID markers to
# substitute in the .tex itself; the IDs render through the .bbl once the bib
# notes are filled and paper1_unified is recompiled (pdflatex + bibtex + x3).
# ############################################################################
#
# On submission day, once wave-1 arXiv IDs (P4, P3, P2) are assigned,
# this script performs the ID insertions the SUBMISSION_NOTE files describe,
# recompiles the touched papers, mirrors the served PDFs, rebuilds the
# arXiv tarballs (standalone-verified), prints the Convex bump commands, and
# updates the checklist rows — one command, all gates.
#
# NOTE (2026-07-10): REPO path constant corrected to CODE_YOU/bigbounce (was the
# stale CODE_2025/bigbounce). Repo now lives at CODE_YOU/bigbounce.
#
# It NEVER changes a scientific number. It only substitutes the clearly-marked
# arXiv-ID placeholders with the real IDs the caller supplies.
#
# USAGE:
#   tools/insert_arxiv_ids.sh --p4 2507.NNNNN --p1b 2507.NNNNN \
#       --p3 2507.NNNNN --p2 2507.NNNNN [--dry-run]
#
# The four IDs are the WAVE-1 IDs (already assigned when this runs):
#   --p4   -> Paper IV (galaxy chirality)      => P5 \paperIVarxiv + P1A bib
#   --p1b  -> Paper I(b) (MCMC companion)      => P1A bib
#   --p3   -> Paper III (anomaly catalog)      => P1A bib
#   --p2   -> Paper II (f_NL forecast)         => P1A bib
#
# WHAT IT DOES (per SUBMISSION_NOTE.txt / SUBMISSION_NOTE.md):
#   1. P5  : set \paperIVarxiv macro to the real P4 ID.
#   2. P1A : fill the TODO-SUBMISSION companion bib entries (P1B/P2/P3/P4)
#            with their real IDs, regenerate the .bbl, so the rendered PDF
#            shows the live IDs.
#   3. P1B : STAGE (do NOT apply) the reciprocal P1A-ID insertion into a
#            P1B_V2_NOTE — P1B submits BEFORE P1A's ID exists, so its v2
#            replacement carries P1A's ID. (P1A's own ID is not known here.)
#   4. For each TOUCHED paper (P5, P1A): recompile (0-undef gate), bump patch
#            version + date, mirror served paths, rebuild + standalone-verify
#            bundle, print the Convex bump command, update checklist rows.
#   5. --dry-run: do everything in a temp copy, verify all gates, touch
#            NOTHING in the repo.
#
# Fails loudly on any gate. Exit 0 = all gates green.
# ============================================================================
set -euo pipefail

# --- TeX toolchain (per Houston's standing env) -----------------------------
export PATH="$PATH:$HOME/Library/TinyTeX/bin/universal-darwin:/opt/homebrew/bin"

REPO="/Users/houstongolden/Desktop/CODE_YOU/bigbounce"

# md5 helper (macos: md5sum or gmd5sum or md5)
md5of() {
  if command -v md5sum >/dev/null 2>&1; then md5sum "$1" | awk '{print $1}';
  elif command -v gmd5sum >/dev/null 2>&1; then gmd5sum "$1" | awk '{print $1}';
  else md5 -q "$1"; fi
}

# --- arg parse --------------------------------------------------------------
P4_ID=""; P1B_ID=""; P3_ID=""; P2_ID=""; DRYRUN=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --p4)  P4_ID="$2"; shift 2;;
    --p1b) P1B_ID="$2"; shift 2;;
    --p3)  P3_ID="$2"; shift 2;;
    --p2)  P2_ID="$2"; shift 2;;
    --dry-run) DRYRUN=1; shift;;
    -h|--help) grep '^#' "$0" | sed 's/^# \{0,1\}//'; exit 0;;
    *) echo "FATAL: unknown arg '$1'"; exit 2;;
  esac
done

for pair in "P4:$P4_ID" "P1B:$P1B_ID" "P3:$P3_ID" "P2:$P2_ID"; do
  name="${pair%%:*}"; val="${pair#*:}"
  [[ -n "$val" ]] || { echo "FATAL: missing --${name,,} arXiv ID"; exit 2; }
  # arXiv new-scheme ID sanity: YYMM.NNNNN (4-5 digit suffix), tolerate vN
  if ! [[ "$val" =~ ^[0-9]{4}\.[0-9]{4,5}(v[0-9]+)?$ ]]; then
    echo "FATAL: '$val' for $name is not a valid arXiv ID (expected YYMM.NNNNN)"; exit 2
  fi
done

TODAY="$(date +%Y-%m-%d)"
TODAY_LONG="$(date '+%B %-d, %Y' 2>/dev/null || date '+%B %d, %Y')"
MODE_LABEL=$([[ $DRYRUN -eq 1 ]] && echo "DRY-RUN (temp copy, repo untouched)" || echo "LIVE (repo will be modified)")

echo "============================================================"
echo " insert_arxiv_ids.sh  —  $MODE_LABEL"
echo "   P4=$P4_ID  P1B=$P1B_ID  P3=$P3_ID  P2=$P2_ID"
echo "   date=$TODAY"
echo "============================================================"

# ----------------------------------------------------------------------------
# WORKROOT: in dry-run we copy the whole repo subtree we touch into /tmp.
# In live mode WORKROOT is the repo itself.
# ----------------------------------------------------------------------------
if [[ $DRYRUN -eq 1 ]]; then
  WORKROOT="$(mktemp -d /tmp/insert_arxiv_ids_XXXX)"
  echo "[dry-run] staging temp workroot: $WORKROOT"
  mkdir -p "$WORKROOT/arxiv" \
           "$WORKROOT/pipelines/p5_desi_chirality/paper" \
           "$WORKROOT/submissions/P5" "$WORKROOT/submissions/P1A" \
           "$WORKROOT/public/papers" "$WORKROOT/site/public/papers"
  # P5 source (whole dir for figures + tex)
  cp -R "$REPO/pipelines/p5_desi_chirality/paper/." "$WORKROOT/pipelines/p5_desi_chirality/paper/"
  # P1A source (tex + shared bib + figures)
  cp "$REPO/arxiv/paper1a_ech_nogo.tex" "$WORKROOT/arxiv/"
  cp "$REPO/arxiv/references.bib" "$WORKROOT/arxiv/"
  [[ -f "$REPO/arxiv/paper1a_ech_nogo.bbl" ]] && cp "$REPO/arxiv/paper1a_ech_nogo.bbl" "$WORKROOT/arxiv/" || true
  cp "$REPO/arxiv/fig_theory_map.png" "$WORKROOT/arxiv/" 2>/dev/null || true
  [[ -d "$REPO/arxiv/figures" ]] && cp -R "$REPO/arxiv/figures" "$WORKROOT/arxiv/" || true
  cp "$REPO/submissions/SUBMIT-TODAY-CHECKLIST.md" "$WORKROOT/submissions/" 2>/dev/null || true
else
  WORKROOT="$REPO"
fi

P5_TEX="$WORKROOT/pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex"
P1A_TEX="$WORKROOT/arxiv/paper1a_ech_nogo.tex"
P1A_BIB="$WORKROOT/arxiv/references.bib"
P1B_TEX="$REPO/arxiv/paper1b_mcmc_companion.tex"   # only read for the note; never edited here
CHECKLIST="$WORKROOT/submissions/SUBMIT-TODAY-CHECKLIST.md"

GATE_FAILED=0
gate() {  # gate "<label>" <ok:0|1>
  if [[ "$2" == "0" ]]; then echo "  [GATE OK ] $1"; else echo "  [GATE FAIL] $1"; GATE_FAILED=1; fi
}

# bump the trailing patch number of a v-string:  v0.1.104 -> v0.1.105 ; v1A.0.112 -> v1A.0.113
bump_patch() {  # echoes bumped version
  local v="$1"
  local head="${v%.*}"; local tail="${v##*.}"
  # tail may carry a -DATE suffix (v0.1.104-2026-07-07) — strip it
  tail="${tail%%-*}"
  echo "${head}.$((tail+1))"
}

# ===========================================================================
# STEP 1 — P5: set \paperIVarxiv to the real P4 ID
# ===========================================================================
echo ""
echo ">>> STEP 1 — P5 \\paperIVarxiv := arXiv:$P4_ID"
P5_MACRO_BEFORE='\newcommand{\paperIVarxiv}{arXiv:XXXX.XXXXX}'
P5_MACRO_AFTER='\newcommand{\paperIVarxiv}{arXiv:'"$P4_ID"'}'
if grep -qF "$P5_MACRO_BEFORE" "$P5_TEX"; then
  # literal find/replace via env vars — NO regex/escape interpolation
  BB_FIND="$P5_MACRO_BEFORE" BB_REPL="$P5_MACRO_AFTER" \
    perl -0pi -e 'my ($f,$r)=($ENV{BB_FIND},$ENV{BB_REPL}); s/\Q$f\E/$r/g;' "$P5_TEX"
  gate "P5 \\paperIVarxiv placeholder found + replaced" \
       "$(grep -qF "arXiv:$P4_ID" "$P5_TEX" && ! grep -qF 'arXiv:XXXX.XXXXX' "$P5_TEX" && echo 0 || echo 1)"
else
  # already-inserted? (idempotent) or placeholder moved
  if grep -qF "arXiv:$P4_ID" "$P5_TEX"; then
    echo "  [note] P5 already carries arXiv:$P4_ID (idempotent)"; gate "P5 macro present" 0
  else
    gate "P5 \\paperIVarxiv placeholder present" 1
  fi
fi

# ===========================================================================
# STEP 2 — P1A: fill companion bib TODO-SUBMISSION entries with wave-1 IDs
#   Golden2026P1b -> P1B_ID ; Golden2026P2 -> P2_ID ;
#   Golden2026P3  -> P3_ID  ; Golden2026P4 -> P4_ID
#   (Golden2026P1a is P1A's OWN forward-ref placeholder — P1A's ID is not
#    known at wave-2 time, so it is LEFT as [arXiv:XXXX.XXXXX].)
# The note text is:  note = "Companion paper, posted concurrently on arXiv"
# We append the ID:  ... posted concurrently on arXiv (arXiv:2507.NNNNN)"
# Then regenerate the .bbl so the rendered PDF shows the IDs.
# ===========================================================================
echo ""
echo ">>> STEP 2 — P1A companion bib IDs (P1B/P2/P3/P4)"
# Fill each companion entry's note with " (arXiv:ID)". Operates within the
# specific @article{key,...} block (captures the mid-block so the entry body is
# preserved). Idempotent: skips a note that already carries an arXiv:NNNN.NNNNN.
# Golden2026P1a (P1A's own forward-ref) is deliberately NOT in the map.
BB_P1B="$P1B_ID" BB_P2="$P2_ID" BB_P3="$P3_ID" BB_P4="$P4_ID" \
perl -0777 -pi -e '
  my %ids = ("Golden2026P1b",$ENV{BB_P1B},"Golden2026P2",$ENV{BB_P2},
             "Golden2026P3",$ENV{BB_P3},"Golden2026P4",$ENV{BB_P4});
  for my $k (keys %ids) {
    my $id = $ids{$k};
    s/(\@article\{\Q$k\E,)(.*?)(note\s*=\s*")([^"]*?)(")/
      my ($h,$mid,$np,$body,$nq)=($1,$2,$3,$4,$5);
      if ($body =~ m{arXiv:\d{4}\.\d{4,5}}) { "$h$mid$np$body$nq" }
      else { $body =~ s{\s+$}{}; "$h$mid$np$body (arXiv:$id)$nq" }
    /gxse;
  }
' "$P1A_BIB"

for kv in "Golden2026P1b:$P1B_ID" "Golden2026P2:$P2_ID" "Golden2026P3:$P3_ID" "Golden2026P4:$P4_ID"; do
  k="${kv%%:*}"; v="${kv#*:}"
  # verify the ID now sits inside that key's note
  if perl -0ne 'exit(!(/\@article\{\Q'"$k"'\E,.*?note\s*=\s*"[^"]*arXiv:\Q'"$v"'\E/s))' "$P1A_BIB"; then
    gate "P1A bib $k := arXiv:$v" 0
  else
    gate "P1A bib $k := arXiv:$v" 1
  fi
done
# sanity: P1A's own forward-ref placeholder must remain untouched
gate "P1A Golden2026P1a self-placeholder preserved ([arXiv:XXXX.XXXXX])" \
     "$(grep -q 'arXiv:XXXX.XXXXX --- ID inserted at coordinated submission' "$P1A_BIB" && echo 0 || echo 1)"

# ===========================================================================
# STEP 3 — P1B reciprocal: STAGE (do not apply) the P1A-ID insertion.
#   P1B submits before P1A's ID exists, so we only WRITE A NOTE describing
#   exactly what the v2 replacement must do. No P1B source is edited here.
# ===========================================================================
echo ""
echo ">>> STEP 3 — P1B_V2_NOTE (staged reciprocal insertion; not applied)"
P1B_NOTE_DIR="$WORKROOT/submissions/P1B"
P1B_NOTE="$P1B_NOTE_DIR/P1B_V2_NOTE.md"
mkdir -p "$P1B_NOTE_DIR"
cat > "$P1B_NOTE" <<EOF
# P1B_V2_NOTE — reciprocal P1A-arXiv-ID insertion (STAGED, apply at P1B v2)

Generated by \`tools/insert_arxiv_ids.sh\` on $TODAY${DRYRUN:+ }$([[ $DRYRUN -eq 1 ]] && echo "(dry-run preview)").

**Do NOT apply until P1A has an assigned arXiv ID.** P1B posts in wave 1,
BEFORE P1A, so P1A's ID does not exist yet at wave-2 time. When P1A's ID is
assigned, produce the P1B **v2 replacement** by running the two substitutions
below, then recompile + rebuild the bundle (standing Directive-G).

## Substitutions (replace BOTH \`[arXiv:XXXX.XXXXX]\` markers with P1A's real ID)

1. \`arxiv/references.bib\`, bib key \`Golden2026P1a\`, \`note =\` field:
   \`\`\`
   note = "Companion paper, posted concurrently on arXiv [arXiv:XXXX.XXXXX --- ID inserted at coordinated submission]"
   \`\`\`
   -> replace \`[arXiv:XXXX.XXXXX --- ID inserted at coordinated submission]\`
      with \`arXiv:<P1A_ID>\` (P1A's assigned ID).

2. \`arxiv/paper1b_mcmc_companion.tex\`, Introduction coordinated-submission
   paragraph (~line 1468), inline marker:
   \`\`\`
   \mbox{\texttt{[arXiv:XXXX.XXXXX]}}
   \`\`\`
   -> replace \`[arXiv:XXXX.XXXXX]\` with P1A's assigned ID \`arXiv:<P1A_ID>\`.

## Then (Directive-G, on the P1B v2 bundle)
- Recompile P1B: \`pdflatex x4 + bibtex\`, verify 0 undefined refs (22 pp).
- Bump P1B \`\paperVersion\` (patch) + \`\paperTimestamp\`/\`\date\` to the day.
- Re-mirror the new PDF byte-identical to every served path (public/papers/
  versioned+alias, site/public/papers/, source dir).
- Convex \`paperVersions:bump\` for P1B with the REAL new md5/pages.
- Rebuild + standalone-verify the P1B v2 tarball; commit.

## Values captured at generation time (wave-1 IDs, for cross-reference)
- P4  = arXiv:$P4_ID
- P1B = arXiv:$P1B_ID  (P1B's OWN id — informational)
- P3  = arXiv:$P3_ID
- P2  = arXiv:$P2_ID
- P1A = arXiv:<assigned in wave 2 — fill here at P1B v2 time>
EOF
gate "P1B_V2_NOTE staged at submissions/P1B/P1B_V2_NOTE.md" \
     "$([[ -f "$P1B_NOTE" ]] && echo 0 || echo 1)"
# Confirm P1B source itself was NOT touched (staged-only requirement)
gate "P1B source untouched (placeholders intact in repo)" \
     "$(grep -q 'XXXX.XXXXX' "$P1B_TEX" && echo 0 || echo 1)"

# ===========================================================================
# STEP 4 — per touched paper: recompile (0-undef), bump, mirror, bundle,
#          Convex cmd, checklist rows.
# ===========================================================================
# recompile_paper <tex> <label> <uses_bibtex:0|1>  -> sets globals PAGES,PDF
recompile_paper() {
  local tex="$1" label="$2" usebib="$3"
  local dir base; dir="$(cd "$(dirname "$tex")" && pwd)"; base="$(basename "$tex" .tex)"
  echo "    [$label] compiling in $dir"
  ( cd "$dir"
    pdflatex -interaction=nonstopmode "$base.tex" >/dev/null 2>&1 || true
    if [[ "$usebib" == "1" ]]; then bibtex "$base" >/dev/null 2>&1 || true; fi
    pdflatex -interaction=nonstopmode "$base.tex" >/dev/null 2>&1 || true
    pdflatex -interaction=nonstopmode "$base.tex" >/dev/null 2>&1 || true
    pdflatex -interaction=nonstopmode "$base.tex" >/dev/null 2>&1 || true
  )
  local log="$dir/$base.log"
  local errs undef
  if [[ -f "$log" ]]; then
    errs=$({ grep -c '^!' "$log" 2>/dev/null || true; }); errs=${errs:-0}
    undef=$({ grep -c 'Reference.*undefined\|Citation.*undefined' "$log" 2>/dev/null || true; }); undef=${undef:-0}
  else
    errs=99; undef=99
  fi
  PAGES=$(pdfinfo "$dir/$base.pdf" 2>/dev/null | awk '/^Pages/{print $2}')
  PDF="$dir/$base.pdf"
  echo "    [$label] errors=$errs undef=$undef pages=$PAGES"
  gate "$label recompile: 0 errors" "$([[ "$errs" == "0" ]] && echo 0 || echo 1)"
  gate "$label recompile: 0 undefined refs/cites" "$([[ "$undef" == "0" ]] && echo 0 || echo 1)"
  gate "$label PDF produced" "$([[ -f "$PDF" ]] && echo 0 || echo 1)"
}

# --- P5 -----
echo ""
echo ">>> STEP 4a — P5 recompile / bump / mirror / bundle"
P5_VER_CUR=$(grep -oE '\\newcommand\{\\paperVersion\}\{[^}]*\}' "$P5_TEX" | sed 's/.*{\(v[^}]*\)}/\1/')
P5_VER_BASE="${P5_VER_CUR%%-*}"                   # v0.1.104
P5_VER_NEW="$(bump_patch "$P5_VER_BASE")"         # v0.1.105
echo "    P5 version $P5_VER_CUR -> ${P5_VER_NEW}-${TODAY}"
perl -0pi -e "s/\\\\newcommand\{\\\\paperVersion\}\{[^}]*\}/\\\\newcommand{\\\\paperVersion}{${P5_VER_NEW}-${TODAY}}/" "$P5_TEX"
perl -0pi -e "s/\\\\newcommand\{\\\\paperTimestamp\}\{[^}]*\}/\\\\newcommand{\\\\paperTimestamp}{${TODAY_LONG}}/" "$P5_TEX"
perl -0pi -e "s/\\\\date\{[^}]*\}/\\\\date{${TODAY_LONG}}/" "$P5_TEX"
recompile_paper "$P5_TEX" "P5" 0
P5_PDF="$PDF"; P5_PAGES="$PAGES"; P5_MD5="$(md5of "$P5_PDF")"
echo "    P5 pdf md5=$P5_MD5 pages=$P5_PAGES"

# mirror served paths (in live mode -> repo; in dry-run -> temp workroot dirs)
mirror_pdf() {  # <src.pdf> <basename-stem> <newver-with-date>
  local src="$1" stem="$2" verdate="$3"
  local pub="$WORKROOT/public/papers" spub="$WORKROOT/site/public/papers"
  local srcdir; srcdir="$(cd "$(dirname "$src")" && pwd)"
  mkdir -p "$pub" "$spub"
  # cp with self-copy guard (compiled PDF may already BE the source-dir alias)
  local srcabs; srcabs="$srcdir/$(basename "$src")"
  cpq() {  # <src> <dst>
    local dstdir dstabs; dstdir="$(dirname "$2")"; mkdir -p "$dstdir"
    dstabs="$(cd "$dstdir" && pwd)/$(basename "$2")"
    [[ "$srcabs" == "$dstabs" ]] && return 0
    cp "$1" "$2"
  }
  cpq "$src" "$pub/${stem}_${verdate}.pdf"
  cpq "$src" "$pub/${stem}.pdf"                 # canonical alias
  cpq "$src" "$spub/${stem}_${verdate}.pdf"
  cpq "$src" "$srcdir/${stem}_${verdate}.pdf"
  cpq "$src" "$srcdir/${stem}.pdf"             # source-dir alias
  # three-way md5 identity check across served copies
  local m1 m2 m3
  m1="$(md5of "$pub/${stem}_${verdate}.pdf")"
  m2="$(md5of "$spub/${stem}_${verdate}.pdf")"
  m3="$(md5of "$srcdir/${stem}_${verdate}.pdf")"
  gate "$stem served copies byte-identical (public==site==source)" \
       "$([[ "$m1" == "$m2" && "$m2" == "$m3" ]] && echo 0 || echo 1)"
}
mirror_pdf "$P5_PDF" "p5_desi_chirality" "${P5_VER_NEW}-${TODAY}"

# rebuild + standalone-verify bundle
P5_BUNDLE_OUT="arxiv_p5_${P5_VER_NEW}"
echo "    P5 rebuilding bundle $P5_BUNDLE_OUT.tar.gz (standalone-verify)"
if bash "$REPO/tools/build_arxiv_tarball.sh" "$P5_TEX" "$P5_BUNDLE_OUT" >/tmp/p5_bundle.log 2>&1; then
  gate "P5 bundle standalone-compile clean" 0
  # move built tarball to submissions/P5 (live only)
  BUILT="$(dirname "$P5_TEX")/${P5_BUNDLE_OUT}.tar.gz"
  if [[ $DRYRUN -eq 0 && -f "$BUILT" ]]; then mkdir -p "$WORKROOT/submissions/P5"; mv "$BUILT" "$WORKROOT/submissions/P5/"; fi
else
  echo "    ---- P5 bundle log tail ----"; tail -15 /tmp/p5_bundle.log
  gate "P5 bundle standalone-compile clean" 1
fi

# --- P1A -----
echo ""
echo ">>> STEP 4b — P1A recompile / bump / mirror / bundle"
P1A_VER_CUR=$(grep -oE '\\newcommand\{\\paperVersion\}\{[^}]*\}' "$P1A_TEX" | sed 's/.*{\(v[^}]*\)}/\1/')
P1A_VER_BASE="${P1A_VER_CUR%%-*}"
P1A_VER_NEW="$(bump_patch "$P1A_VER_BASE")"       # v1A.0.113
echo "    P1A version $P1A_VER_CUR -> $P1A_VER_NEW"
perl -0pi -e "s/\\\\newcommand\{\\\\paperVersion\}\{[^}]*\}/\\\\newcommand{\\\\paperVersion}{${P1A_VER_NEW}}/" "$P1A_TEX"
perl -0pi -e "s/\\\\newcommand\{\\\\paperTimestamp\}\{[^}]*\}/\\\\newcommand{\\\\paperTimestamp}{${TODAY_LONG}}/" "$P1A_TEX"
recompile_paper "$P1A_TEX" "P1A" 1      # P1A uses bibtex (references.bib) — regenerates .bbl with real IDs
P1A_PDF="$PDF"; P1A_PAGES="$PAGES"; P1A_MD5="$(md5of "$P1A_PDF")"
echo "    P1A pdf md5=$P1A_MD5 pages=$P1A_PAGES"

# verify the real IDs actually landed in the regenerated .bbl (rendered PDF source)
P1A_BBL="$(dirname "$P1A_TEX")/paper1a_ech_nogo.bbl"
if [[ -f "$P1A_BBL" ]]; then
  ok=0
  for v in "$P1B_ID" "$P2_ID" "$P3_ID" "$P4_ID"; do
    grep -qF "arXiv:$v" "$P1A_BBL" || ok=1
  done
  gate "P1A .bbl carries all 4 companion IDs (rendered in PDF)" "$ok"
else
  gate "P1A .bbl regenerated" 1
fi

mirror_pdf "$P1A_PDF" "paper1a_ech_nogo" "$P1A_VER_NEW"

P1A_BUNDLE_OUT="arxiv_p1a_${P1A_VER_NEW}"
echo "    P1A rebuilding bundle $P1A_BUNDLE_OUT.tar.gz (standalone-verify)"
if bash "$REPO/tools/build_arxiv_tarball.sh" "$P1A_TEX" "$P1A_BUNDLE_OUT" >/tmp/p1a_bundle.log 2>&1; then
  gate "P1A bundle standalone-compile clean" 0
  BUILT="$(dirname "$P1A_TEX")/${P1A_BUNDLE_OUT}.tar.gz"
  if [[ $DRYRUN -eq 0 && -f "$BUILT" ]]; then mkdir -p "$WORKROOT/submissions/P1A"; mv "$BUILT" "$WORKROOT/submissions/P1A/"; fi
else
  echo "    ---- P1A bundle log tail ----"; tail -15 /tmp/p1a_bundle.log
  gate "P1A bundle standalone-compile clean" 1
fi

# ===========================================================================
# STEP 4c — Convex bump commands (printed; run manually or wire up)
# ===========================================================================
echo ""
echo ">>> STEP 4c — Convex bump commands (real md5/pages)"
CONVEX_URL="https://brilliant-panther-471.convex.cloud/api/mutation"
cat <<EOF
  # P5:
  curl -s -X POST '$CONVEX_URL' -H 'Content-Type: application/json' -d '{
    "path":"paperVersions:bump",
    "args":{"paperSlug":"p5-desi-chirality","version":"${P5_VER_NEW}-${TODAY}",
            "pdfMd5":"$P5_MD5","pages":${P5_PAGES:-0}},"format":"json"}'
  # P1A:
  curl -s -X POST '$CONVEX_URL' -H 'Content-Type: application/json' -d '{
    "path":"paperVersions:bump",
    "args":{"paperSlug":"p1a-ech-nogo","version":"${P1A_VER_NEW}",
            "pdfMd5":"$P1A_MD5","pages":${P1A_PAGES:-0}},"format":"json"}'
EOF

# ===========================================================================
# STEP 4d — checklist rows
# ===========================================================================
echo ""
echo ">>> STEP 4d — checklist rows (submissions/SUBMIT-TODAY-CHECKLIST.md)"
if [[ -f "$CHECKLIST" ]]; then
  STAMP="<!-- insert_arxiv_ids.sh $TODAY: P5 ${P5_VER_NEW}-${TODAY} (P4 ID $P4_ID); P1A ${P1A_VER_NEW} (P1B/P2/P3/P4 IDs); P1B_V2_NOTE staged -->"
  if ! grep -qF "$STAMP" "$CHECKLIST"; then
    printf '\n%s\n' "$STAMP" >> "$CHECKLIST"
  fi
  gate "checklist stamped" 0
else
  gate "checklist present" 1
fi

# ===========================================================================
# FINALE
# ===========================================================================
echo ""
echo "============================================================"
if [[ "$GATE_FAILED" == "0" ]]; then
  echo " ALL GATES GREEN."
  if [[ $DRYRUN -eq 1 ]]; then
    echo " DRY-RUN complete — repo untouched. Temp workroot: $WORKROOT"
    echo " (inspect it, then rerun WITHOUT --dry-run on submission day)"
  else
    echo " LIVE run complete."
    echo "   P5  -> ${P5_VER_NEW}-${TODAY}  bundle submissions/P5/${P5_BUNDLE_OUT}.tar.gz"
    echo "   P1A -> ${P1A_VER_NEW}          bundle submissions/P1A/${P1A_BUNDLE_OUT}.tar.gz"
    echo "   P1B_V2_NOTE staged; run Convex bumps above; commit the bundle."
  fi
  exit 0
else
  echo " ONE OR MORE GATES FAILED — see [GATE FAIL] lines above."
  [[ $DRYRUN -eq 1 ]] && echo " (dry-run: repo was NOT modified)"
  exit 1
fi
