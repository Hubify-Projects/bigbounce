# P1A v1A.0.119 seven-step PDF audit

## Result

`arxiv/paper1a_ech_nogo.pdf` passes the required post-compile visual and link
audit.

```text
LATEX AUDIT — paper1a_ech_nogo.pdf
──────────────────────────────────
Compile errors:        0
Undefined references:  0
Overfull hboxes >50pt: 0
All overfull hboxes:   0
Table-row overflows:   0
Underfull hboxes:      8 (cosmetic; pre-existing line-spacing only)
Broken local URLs:     0 / 3
HTTP 2xx:              12 / 17 HTTP(S) targets
Publisher DOI 403:     5 / 17 (resolver bot gates; URLs valid)
Raw texttt paths:      0 active
Date overflow risk:    0
Visual review:         PASS — all pages 1–7 at 120 dpi

Verdict: PASS
```

## Compile

The final compile used the cached Tectonic bundle with two forced reruns.  The
log and BibTeX log are frozen under `proof/`.  The only BibTeX warning is the
APS style control message `jnrlst (dependency: not reversed) set 1`; it is not
a missing reference or metadata error.

PDF SHA-256:
`dfe2a47a3221888477dfa47adb9cddf7ebbe25acc96185c3af9e58a1e7c065d0`.

## Visual inspection

Every page was rendered with `pdftoppm -r 120` and inspected at original
render resolution.  There is no text across a gutter, margin escape, overlap,
clipped equation, or malformed title block.  In particular:

- page 1 shows `July 14, 2026 (v1A.0.119)` and the corrected abstract values;
- page 6 cleanly contains the full Fierz matrix, operator identity, Table I,
  and Eqs. (B1)--(B4) within their columns; and
- page 7 references and the appendix continuation are unobstructed.

The seven frozen renders are under `proof/render/`.

## Links

The PDF contains 35 URI annotations and 21 unique targets.  All three GitHub
artifact links map to existing repository files:

- `arxiv/scripts/fierz_lemma_check.py`;
- `arxiv/scripts/njl_gap_equation_route1.py`; and
- `arxiv/scripts/njl_gap_equation_route1_results.json`.

Twelve non-mail HTTP(S) targets returned 200.  Five DOI targets returned 403
from publisher resolver bot protection (`10.1063/...` and four APS DOIs); they
are valid DOI annotations, not missing local artifacts.  The remaining unique
target is the author `mailto:` link.

## Source pattern checks

The active source has zero raw path-like `\texttt{...}` uses.  The date is a
short macro expansion and page 1 confirms it fits.  `pdfnewwindow=true` is set
for external-link viewers that honor it.
