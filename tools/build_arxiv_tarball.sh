#!/usr/bin/env bash
# Build a self-contained arXiv submission tarball for one paper.
# Usage: tools/build_arxiv_tarball.sh <path/to/paper.tex> <output_tarball_basename>
# - copies .tex + .bbl + every \includegraphics target (relative paths preserved)
# - verifies a standalone pdflatex x2 compile in an isolated temp dir
# - writes <texdir>/<output_tarball_basename>.tar.gz
set -euo pipefail

TEX="$1"; OUT="$2"
TINYTEX_BIN="${TINYTEX_BIN:-$HOME/Library/TinyTeX/bin/universal-darwin}"
if command -v pdflatex >/dev/null 2>&1; then
  PDFLATEX="$(command -v pdflatex)"
elif [[ -x "$TINYTEX_BIN/pdflatex" ]]; then
  PDFLATEX="$TINYTEX_BIN/pdflatex"
else
  echo "FAIL: pdflatex not found on PATH or at $TINYTEX_BIN" >&2
  exit 127
fi
TEXDIR="$(cd "$(dirname "$TEX")" && pwd)"
BASE="$(basename "$TEX" .tex)"
STAGE="$(mktemp -d /tmp/arxiv_${OUT}_XXXX)"

cp "$TEXDIR/$BASE.tex" "$STAGE/"
if [[ -f "$TEXDIR/$BASE.bbl" ]]; then cp "$TEXDIR/$BASE.bbl" "$STAGE/"; else echo "WARN: no .bbl"; fi

# figures: extract \includegraphics{...} args
# NOTE: grep exits 1 on zero matches, which under `set -o pipefail` used to abort
# the whole script for a legitimately figure-less paper (e.g. P1B). Collect the
# list first (tolerating the empty case) and iterate WITHOUT a pipeline, so the
# MISSING FIGURE `exit 1` below still aborts the script instead of only a subshell.
FIGS="$(grep -o '\\includegraphics\(\[[^]]*\]\)\?{[^}]*}' "$TEXDIR/$BASE.tex" \
  | sed 's/.*{\([^}]*\)}.*/\1/' | sort -u || true)"
if [[ -z "$FIGS" ]]; then
  echo "INFO: no \\includegraphics in $BASE.tex — figure-less paper, nothing to stage"
else
  while IFS= read -r fig; do
    [[ -n "$fig" ]] || continue
    src="$TEXDIR/$fig"
    if [[ ! -f "$src" ]]; then
      # extension-less \includegraphics — resolve like LaTeX does
      for ext in pdf png jpg jpeg eps; do
        if [[ -f "$TEXDIR/$fig.$ext" ]]; then src="$TEXDIR/$fig.$ext"; fig="$fig.$ext"; break; fi
      done
    fi
    [[ -f "$src" ]] || { echo "MISSING FIGURE: $fig"; exit 1; }
    mkdir -p "$STAGE/$(dirname "$fig")"
    cp "$src" "$STAGE/$fig"
  done <<< "$FIGS"
fi

# any local .sty/.cls next to the tex (globs stay literal when nothing matches)
for f in "$TEXDIR"/*.sty "$TEXDIR"/*.cls; do
  if [[ -f "$f" ]]; then cp "$f" "$STAGE/"; fi
done

# standalone compile test (uses .bbl; no bibtex run)
( cd "$STAGE" \
  && "$PDFLATEX" -interaction=nonstopmode "$BASE.tex" > compile1.log 2>&1 \
  && "$PDFLATEX" -interaction=nonstopmode "$BASE.tex" > compile2.log 2>&1 )
ERRS=$(grep -c '^!' "$STAGE/$BASE.log" || true)
UNDEF=$(grep -c 'LaTeX Warning: Reference.*undefined\|LaTeX Warning: Citation.*undefined' "$STAGE/$BASE.log" || true)
PAGES=$(pdfinfo "$STAGE/$BASE.pdf" | awk '/^Pages/{print $2}')
echo "standalone compile: errors=$ERRS undef=$UNDEF pages=$PAGES"
[[ "$ERRS" == "0" && "$UNDEF" == "0" ]] || { echo "FAIL: standalone compile not clean"; exit 1; }

# tarball excludes compile byproducts
( cd "$STAGE" && rm -f compile1.log compile2.log "$BASE".{aux,log,out,toc,pdf,blg} \
  && tar czf "$TEXDIR/$OUT.tar.gz" . )
SIZE=$(ls -lh "$TEXDIR/$OUT.tar.gz" | awk '{print $5}')
echo "OK: $TEXDIR/$OUT.tar.gz ($SIZE) — contents:"
tar tzf "$TEXDIR/$OUT.tar.gz" | head -40
rm -rf "$STAGE"
