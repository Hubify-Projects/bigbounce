# P1A v1A.0.118 PDF audit

## Build

- Command: `tectonic -b /tmp/tectonic-p1a-bundle -k --keep-logs -r 2 paper1a_ech_nogo.tex`
- Pages: 7
- Page geometry: US Letter, 612 x 792 pt
- PDF bytes: 151,772
- Source SHA-256: `7cfe09cfb6cd136d6b1e8804be5ac7f7cfd181390ae6e9353c8b321287915dd2`
- PDF SHA-256: `9a5d9216df983858acda1e993a4372fcb92822abebed05163ce1e51463e59844`

## Seven-step audit

1. Compile completed successfully with three TeX passes and BibTeX.
2. Log scan found zero overfull boxes, undefined references/citations, fatal
   errors, or emergency stops; 12 underfull boxes are cosmetic.
3. All seven exact-PDF pages were rendered at 120 dpi and inspected at original
   detail: no clipping, overlap, gutter collision, malformed glyph, table spill,
   or media-box overflow.
4. Page 1 visibly shows `July 14, 2026`; the date and title do not overflow.
5. Raw `texttt` filesystem-path count is zero in source and rendered text.
6. The PDF contains 35 URL annotations (21 unique). Live checks returned HTTP
   200 for 16 unique repository/arXiv/journal links; five syntactically valid DOI
   resolver links returned the resolver's bot-gated HTTP 403 response.
7. The frozen proof TeX/PDF are byte-identical to the live files; their hashes
   and every rendered-page hash are recorded in `SHA256SUMS.txt`.

The pre-existing xdvipdfmx `Object @table.1 already defined` warning is
visually harmless: the table renders once, references resolve, and no duplicate
page object is visible.
