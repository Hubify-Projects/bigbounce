# P3 final package receipt — v3.2.0-r15

Audited 2026-08-03 after a source-only ApJS portal closure. This release adds
current AASTeX 7.0.2, required line numbers, a running title, the verified
ORCID, and an evidence-bounded AI-use acknowledgement. It makes **no** change
to scientific claims, abstract values, catalog contents, figures, or numerical
results.

| Item | Binding |
|---|---|
| Source | `paper3_apjs.tex` · SHA-256 `9e9faff87d268588862b4dc5f52b5a86d694b572bd7bfd2faff28ba49dd97156` |
| Canonical PDF | `paper3_apjs.pdf` · SHA-256 `3cd210767a109c7819fc01e15bda1189ed249ff818ce036813151073386147e0` · MD5 `1bb47a0862c696668140ef7c2e4c7838` · 17 pages |
| Official class | `aastex702.cls` (AASTeX 7.0.2 distribution) · SHA-256 `0ee51ff72a4d0b608a1885e87cddad4bcb41efacb852889de97637671c74d8ad` |
| Exact source tar | `paper3_apjs_arxiv_v3.2.0-r15.tar.gz` · SHA-256 `3358914ebb8ac3f7505142e9664c8ecc410434df8a6db621b9d89b5a22e4002c` |
| Flat portal staging package | `apjs_portal_submission_v3.2.0-r15/` · `SHA256SUMS` SHA-256 `148cd76581c30c0ea0cec3576b2157dafca500792634687e9e21a34fff12d658` |

The source tar contains exactly the source, official class, and its three
referenced PDF figures. The flat staging package places its manuscript source,
class, three figures, `tab3.tsv`, `ReadMe`, and
`AAS_DIGITAL_ASSET_MANIFEST.json` at one directory level; its staged source has
only the three figure paths flattened. The bibliography is inline, so no `.bbl`
is required.

## Compile and LaTeX audit

Fresh Tectonic/xdvipdfmx builds of both the canonical source and flat staging
copy passed with 17 pages, zero fatal errors, and zero undefined references or
citations. Both retain one 1.82327 pt non-table overfull hbox in the long
identifier paragraph, below the 10 pt visual-risk threshold. Tectonic also
reports the existing `lineno.sty` UTF-8 replacement warning; it does not alter
the rendered title, text, figures, or line numbering.

Full audit: errors `0`; undefined references/citations `0`; overfull hboxes over
10 pt `0`; table-row overflow `0`; broken `\\artifact{}` paths `0/7`; raw
filesystem paths inside `\\texttt{}` `0`; date-overflow risk `0`. Rendered
inspection of pages 1, 6, and 8 passed: title/ORCID/line numbers, dense text,
and figures/captions are legible without overlap.

The P3 r7 digital-asset validator also passed: 181 rows × 43 columns; 170 core
plus 11 lower-confidence rows; 2,267 warned auxiliary rows; coordinate lineage
PASS; manifest SHA-256
`e59710a1c4f88fc816257d1441ae3eb69d954828c180a8541a1aa8f1c855007a`.
Its journal digital-asset DOI remains `pending`.

## Remaining human decisions

Houston must still supply final sign-off and bounded final-hash active-leg
confirmation, then complete live portal choices: affiliation postal detail,
topical corridor/UAT terms, review mode, data-asset declaration, funding and
conflict disclosures, originality/exclusive-consideration attestation,
reviewer/conflict information, and financial/account choices. This receipt is
package evidence, not a submission or readiness change.
