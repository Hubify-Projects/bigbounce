# P3 final package receipt — v3.2.0-r16

Audited 2026-08-03. This release closes one bounded wording issue: the
accepted-versus-warning-bearing comparison is now stated descriptively, rather
than as a ranked causal/association claim. It adds no metric, numerical result,
or scientific claim.

| Item | Binding |
|---|---|
| Source | `paper3_apjs.tex` · SHA-256 `e54d4b8e307c2ebb62503a5b78e380e6afb00626ae0b4e0ffac7a65556336cdc` |
| Canonical / served PDF | pdfTeX build · SHA-256 `22c76260da4da37d073fe78fcedc993fbaf7e56daca9a29a52a6b39226226c5f` · MD5 `c57ee558b8c1e49dcdb784febcd0eca3` · 495,351 bytes · 17 pages |
| Clean-room canonical compile | Tectonic/xdvipdfmx · SHA-256 `39e9c87fb50bd7f0b9119104dc2556eda1f5ec90b9d0cc6fd6c4cf1ac8a6ed41` · MD5 `af46e80815b7da59efc1c5d1ff1e8560` · 267,829 bytes · 17 pages |
| Official class | `aastex702.cls` (AASTeX 7.0.2) · SHA-256 `0ee51ff72a4d0b608a1885e87cddad4bcb41efacb852889de97637671c74d8ad` |
| Exact source tar | `paper3_apjs_arxiv_v3.2.0-r16.tar.gz` · SHA-256 `83680594c8829d51f17c207e6368c1945c257ed903dbb6365904c24dfa984e66` |
| Flat portal staging package | `apjs_portal_submission_v3.2.0-r16/` · `SHA256SUMS` SHA-256 `729f81f596c65d5eefc704b62949fe31a0d0759fa3b507a60f5860d17221253e` |

## Release verification

`tools/directive_g.sh P3 v3.2.0-r16` passed all gates: source version/date,
served-content leak gate, pdfTeX compilation, retention-before-mirror, six
byte-identical mirrors, and the live Convex version/MD5 bump (row
`k577j5y4zqtmyzgjz5e1ye00j58btng7`). The canonical PDF and all served paths
have the same SHA-256 above:

- `public/papers/paper3_apjs.pdf`
- `public/papers/paper3_apjs_v3.2.0-r16.pdf`
- `site/public/papers/paper3_apjs.pdf`
- `site/public/papers/paper3_apjs_v3.2.0-r16.pdf`
- `site/out/papers/paper3_apjs.pdf`

The source tar contains exactly `paper3_apjs.tex`, `aastex702.cls`, and the
three referenced PDF figures. The flat portal copy contains the manuscript,
class, those figures, `tab3.tsv`, `ReadMe`, and
`AAS_DIGITAL_ASSET_MANIFEST.json` at one directory level; every listed checksum
passes. It was independently compiled to 17 pages.

## LaTeX and visual audit

The canonical pdfTeX release log has **0** fatal errors, **0** undefined
references/citations, and **0** overfull hboxes (including over 50 pt). All 7
declared `\\artifact{}` targets exist. There are no raw filesystem paths in
`\\texttt{}` and no date-overflow risk. Every rendered page (1–17) was inspected:
title/author metadata, line numbers, dense text, all tables, figures, captions,
appendices, and the audit matrix are legible with no clipping, overlap, or
column intrusion.

Independent Tectonic builds issue the pre-existing 1.82327 pt non-table hbox
warning in the long identifier paragraph and a `lineno.sty` UTF-8 replacement
warning. The rendered pages pass; the canonical pdfTeX artifact has zero
overfull boxes.

The P3 r7 digital-asset validator also passes: 181 rows × 43 columns; 170 core
plus 11 lower-confidence rows; 2,267 warned auxiliary rows; coordinate lineage
PASS; manifest SHA-256
`e59710a1c4f88fc816257d1441ae3eb69d954828c180a8541a1aa8f1c855007a`.
The journal digital-asset DOI remains `pending`.

This is package evidence only, not a submission or a readiness-status change.
