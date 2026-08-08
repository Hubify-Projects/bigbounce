# P5 v0.1.131 LaTeX audit

Status: **PASS**

- Compile: `latexmk -pdf -interaction=nonstopmode -halt-on-error p5_desi_chirality.tex` (TinyTeX 2026), exit 0.
- Exact PDF: 39 pages, 1,510,954 bytes, SHA-256 `4f545606e290e0295b4284e8ba441f04155aa601100b213c1e3cfdb894d803a0`.
- Log scan: 0 fatal errors, 0 undefined references/citations, 0 multiply-defined labels, and 0 overfull boxes.
- Visual audit: all 39 rendered pages inspected; no margin, gutter, table, figure, equation, title, date, or path collision.
- Page 39: the segmented rule above references is the intentional APS REVTeX `\bib@device`, verified directly in `aps4-2.rtx`; it is not a stray float/table rule.
- Version/date: `v0.1.131-2026-07-14` is present in the PDF release-candidate material; the title page date is July 14, 2026. The version is not printed on page 1.
- Static URLs: 8/9 returned HTTP 200. The Phys. Rev. Lett. DOI resolver returned HTTP 403 to the automated client; recorded as bot denial, not as proof of a broken DOI.
- Render checksums: `SHA256SUMS` covers every page image.
