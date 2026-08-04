# P3 final package receipt — v3.2.0-r16

Audited 2026-08-03. This release closes the exact-final evidence findings without
changing catalog membership: the accepted-versus-warning-bearing comparison is
stated descriptively; the unsupported causal explanation of the annular deficit
is withdrawn and replaced by an exact core-conditioned audit; the named r2
release directory now contains its manifest-bound Parquet payload; and viewer
capture wording distinguishes 20/20 machine retrievals from 18/20 visible PNGs.

| Item | Binding |
|---|---|
| Source | `paper3_apjs.tex` · SHA-256 `2c23eb15ab9e66320b4afed56f7863033b028614eae7a12939fb64158f7b5423` |
| Canonical / served PDF | pdfTeX build · SHA-256 `c39f080b07c96b0b8db916330219db37afcefccb809659b0ae7de35cfa3fa753` · MD5 `5f1d26eeb0cc7b06fca69bb0707edeb2` · 496,128 bytes · 17 pages |
| Flat-package compile | Tectonic/xdvipdfmx · SHA-256 `934affb51cec38be6744d4d5d9e39179b12e4068d3b4d27486eb6780305ef02f` · MD5 `08185881c9176d7465a2d228a1f765bb` · 268,667 bytes · 17 pages |
| Official class | `aastex702.cls` (AASTeX 7.0.2) · SHA-256 `0ee51ff72a4d0b608a1885e87cddad4bcb41efacb852889de97637671c74d8ad` |
| Exact source tar | `paper3_apjs_arxiv_v3.2.0-r16.tar.gz` · SHA-256 `d1a520437f762c9e5724a5679629e982eda5202721e7a12ffe140e61b266ea58` |
| Flat portal staging package | `apjs_portal_submission_v3.2.0-r16/` · `SHA256SUMS` SHA-256 `a05b50193c173dd7cb89546e8331f6d8be51c50e452ce261e0846a26db62680d` |

## Release verification

`tools/directive_g.sh P3 v3.2.0-r16` passed all gates: source version/date,
served-content leak gate, pdfTeX compilation, retention-before-mirror, six
byte-identical mirrors, and the live Convex version/MD5 bump (row
`k57521s9mvqm2vw25j2f1ef6x18btrz2`). The canonical PDF and all served paths
have the same SHA-256 above:

- `public/papers/paper3_apjs.pdf`
- `public/papers/paper3_apjs_v3.2.0-r16.pdf`
- `site/public/papers/paper3_apjs.pdf`
- `site/public/papers/paper3_apjs_v3.2.0-r16.pdf`
- `site/out/papers/paper3_apjs.pdf`

The source tar contains `paper3_apjs.tex`, `aastex702.cls`, and the three
referenced PDF figures. The flat portal copy contains the manuscript,
class, those figures, `tab3.tsv`, `ReadMe`, and
`AAS_DIGITAL_ASSET_MANIFEST.json` at one directory level; every listed checksum
passes. It was independently compiled to 17 pages.

## LaTeX and visual audit

The canonical pdfTeX release log has **0** fatal errors, **0** undefined
references/citations, and **0** overfull hboxes (including over 50 pt). All 8
declared `\\artifact{}` targets exist. There are no raw filesystem paths in
`\\texttt{}` and no date-overflow risk. Every rendered page (1–17) was inspected:
title/author metadata, line numbers, dense text, all tables, figures, captions,
appendices, and the audit matrix are legible with no clipping, overlap, or
column intrusion.

Independent Tectonic builds issue the pre-existing 1.82327 pt non-table hbox
warning in the long identifier paragraph and a `lineno.sty` UTF-8 replacement
warning. The rendered pages pass; the canonical pdfTeX artifact has zero
overfull boxes.

The r16 core-conditioned all-neighbor control verifies the frozen FITS SHA-256,
streams all 28,425,963 rows, and reproduces 18,134,821 strict rows. For the 170 core clusters it finds 170
observed sub-0.1-arcsec seed recoveries, zero additional 0.1--1-arcsec targets,
zero matches hidden by nearest-seed assignment, and zero annular matches in each
of the 16 shifted core controls. The aggregate 11-versus-75.56 comparison is
therefore retained only as a descriptive diagnostic, not a causal or purity
null. The restored r2 Parquet is 58,038 bytes with SHA-256
`25f06752e0f1e9c0ddcde32e74fc0a82e8c2518a8fb24bf910c21e10ce988b03`,
exactly matching its manifest and the tracked r7 bundle copy. The viewer audit
records 20/20 successful data retrievals and 18/20 visible spectrum/marker PNGs;
the blank captures for `P3-DESI-000004` and `P3-DESI-000047` are disclosed.

The P3 r7 digital-asset validator also passes: 181 rows × 43 columns; 170 core
plus 11 lower-confidence rows; 2,267 warned auxiliary rows; coordinate lineage
PASS; manifest SHA-256
`e59710a1c4f88fc816257d1441ae3eb69d954828c180a8541a1aa8f1c855007a`.
The journal digital-asset DOI remains `pending`.

This is package evidence only, not a submission or a readiness-status change.
