#!/usr/bin/env bash
# Build a self-contained arXiv submission tarball for one paper.
# Usage: tools/build_arxiv_tarball.sh <path/to/paper.tex> <output_tarball_basename>
# - copies .tex + .bbl + every \includegraphics target (relative paths preserved)
# - verifies a standalone pdflatex x2 compile in an isolated temp dir
# - writes <texdir>/<output_tarball_basename>.tar.gz
set -euo pipefail

TEX="$1"; OUT="$2"
TEXDIR="$(cd "$(dirname "$TEX")" && pwd)"
BASE="$(basename "$TEX" .tex)"
STAGE="$(mktemp -d /tmp/arxiv_${OUT}_XXXX)"

cp "$TEXDIR/$BASE.tex" "$STAGE/"
if [[ -f "$TEXDIR/$BASE.bbl" ]]; then cp "$TEXDIR/$BASE.bbl" "$STAGE/"; else echo "WARN: no .bbl"; fi

# figures: extract \includegraphics{...} args
grep -o '\\includegraphics\(\[[^]]*\]\)\?{[^}]*}' "$TEXDIR/$BASE.tex" \
  | sed 's/.*{\([^}]*\)}.*/\1/' | sort -u | while read -r fig; do
    src="$TEXDIR/$fig"
    [[ -f "$src" ]] || { echo "MISSING FIGURE: $fig"; exit 1; }
    mkdir -p "$STAGE/$(dirname "$fig")"
    cp "$src" "$STAGE/$fig"
done

# any local .sty/.cls next to the tex
for f in "$TEXDIR"/*.sty "$TEXDIR"/*.cls; do [[ -f "$f" ]] && cp "$f" "$STAGE/"; done

# standalone compile test (uses .bbl; no bibtex run)
( cd "$STAGE" \
  && pdflatex -interaction=nonstopmode "$BASE.tex" > compile1.log 2>&1 \
  && pdflatex -interaction=nonstopmode "$BASE.tex" > compile2.log 2>&1 )
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
