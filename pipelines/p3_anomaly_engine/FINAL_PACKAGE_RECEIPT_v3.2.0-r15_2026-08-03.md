# P3 final package receipt — v3.2.0-r15

Audited 2026-08-03 after a source-only ApJS portal closure. This release adds
current AASTeX 7.0.2, required line numbers, a running title, the verified
ORCID, and an evidence-bounded AI-use acknowledgement. It makes **no** change
to scientific claims, abstract values, catalog contents, figures, or numerical
results.

| Item | Binding |
|---|---|
| Source | `paper3_apjs.tex` · SHA-256 `5ba0f87c6d7782d0fa1ae37cab9411c5460bbc5c429ace0c381f5ce731aa04e4` |
| Canonical / served PDF | `paper3_apjs.pdf` · pdfTeX build · SHA-256 `793575f5705c421a3c75bfa2fe66b9f3c07aed327a2a75e01f835f952aee47ef` · MD5 `6659b909c928488873179ba71af8556d` · 495,346 bytes · 17 pages |
| Clean-room compile record | Tectonic/xdvipdfmx r15 compile · SHA-256 `ecbce4fdc12ff9348b89f0d4679e78d960042b5957d678ed9801579434e4fb49` · MD5 `1622dd1810fb6bc4089f1d67f8d108a9` · 17 pages |
| Official class | `aastex702.cls` (AASTeX 7.0.2 distribution) · SHA-256 `0ee51ff72a4d0b608a1885e87cddad4bcb41efacb852889de97637671c74d8ad` |
| Exact source tar | `paper3_apjs_arxiv_v3.2.0-r15.tar.gz` · SHA-256 `14689637cdd7bb1ec89ab0907bebc382a57c6e9b96b4a3076a2f9b4394ba9fe7` |
| Flat portal staging package | `apjs_portal_submission_v3.2.0-r15/` · `SHA256SUMS` SHA-256 `32652baf6033a45f653e9027a04cc4aee75ea95b3299c7ac148d5666c4254d54` |

The source tar contains exactly the source, official class, and its three
referenced PDF figures. The flat staging package places its manuscript source,
class, three figures, `tab3.tsv`, `ReadMe`, and
`AAS_DIGITAL_ASSET_MANIFEST.json` at one directory level; its staged source has
only the three figure paths flattened. The bibliography is inline, so no `.bbl`
is required.

## Compile and LaTeX audit

Fresh Tectonic/xdvipdfmx builds of both the canonical source and flat staging
copy passed with 17 pages, zero fatal errors, and zero undefined references or
citations; their checksum is retained above as the clean-room compile record.
The currently canonical PDF was then rebuilt with pdfTeX and mirrored byte-for-byte
to `public/papers/` and `site/public/papers/` (unversioned and r15 aliases), plus
`site/out/papers/`; its checksum is the canonical/served binding above. Both builds
retain one 1.82327 pt non-table overfull hbox in the long
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
