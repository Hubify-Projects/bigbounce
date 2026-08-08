# P3 v3.2.0 structural-recovery closure and disposition

Date: 2026-07-14  
Lane owner: P3-only recovery worker  
Disposition: **LOCAL STRUCTURAL CLOSURE COMPLETE; READINESS HELD FOR INDEPENDENT EXACT-R1 REVIEW**

This report does not mark P3 accepted, publication-ready, or minor-revisions-only. It records the
exact artifacts that an independent panel must review. Shared readiness, SSOT, Convex, site data,
paper-overview state, and version files were intentionally not changed in this lane.

## 1. Structural decision

The rejected heterogeneous product was not defended or cosmetically revised. It was replaced by
one falsifiable deliverable: a DESI DR1 main-survey science-target anomaly-candidate catalog whose
public identifiers, selection gates, source rows, payload hashes, and input provenance can all be
checked independently.

The release is explicitly a follow-up candidate list. It does **not** claim validated detections,
novel object classes, an anomaly occurrence rate, population completeness, or reproduction of the
historical neural-network scores from public spectra.

## 2. Finding disposition

| Structural problem | Disposition | Evidence |
|---|---|---|
| Mixed surveys and incompatible selection functions | Closed by scope reduction | v3.2.0 contains only the DESI product; Gaia, eROSITA, LAMOST, SDSS, Planck, ACT, and aggregate mixed-survey tables are absent. |
| Legacy identifiers were not reliable public DESI keys | Closed for the release cohort | 181 unique public `TARGETID` values are copied from public DR1 rows and rejoined exactly. The legacy mixed/hash ID remains audit metadata only. |
| Large aggregate count could be misread as validated detections | Closed in claims and title/abstract/conclusions | Paper reports 181 candidates and explains why the smaller auditable count is the integrity improvement. |
| Selection function was not reconstructable | Closed | Ordered bitmask, survey, radius, primary, warning, and duplicate rules are executable and documented; the full waterfall is machine-readable. |
| Source provenance could silently drift | Closed for the exact release | Immutable historical-input URLs/tag/commit and SHA-256 values are recorded; the 22 GB DESI input hash matches the current official checksum. |
| Release correction risked moving an immutable tag | Closed additively | Original tag was preserved; metadata-complete correction was issued under a new annotated tag. |
| Paper appendices and floats were out of reading order | Closed | References precede appendices; nonfloating appendix tables eliminate rotated/blank pages and keep headings adjacent to evidence. |

## 3. Exact data result

The memory-bounded scan processed the complete public DESI DR1 pixel zcatalog without
materializing the 22 GB table in memory:

| Stage | Rows |
|---|---:|
| Public FITS rows scanned | 28,425,963 |
| Main-survey rows with any declared LRG/ELG/QSO/BGS_ANY/MWS_ANY bit | 20,299,155 |
| Nearest positional matches within 1 arcsec after deterministic deduplication | 2,468 |
| Global-primary matches | 2,448 |
| Global-primary and `ZWARN == 0` released candidates | **181** |

Independent release checks:

- 181/181 recorded FITS rows reopened.
- 18/18 carried DESI fields agree exactly at zero tolerance.
- Candidate ID, cluster ID, `TARGETID`, and FITS-row keys are unique.
- No null cells.
- Every row is main survey, carries a declared science bit, is global-primary, has `ZWARN == 0`,
  and lies within 1 arcsec.
- Spectral types are descriptive, not selected: 157 GALAXY, 23 QSO, one STAR.
- Programs: 162 dark and 19 bright.
- Match-quality disclosure: 170 rows at or below 0.1 arcsec; 11 in the 0.1--1 arcsec tail;
  maximum 0.9905736 arcsec.
- Full local DESI FITS SHA-256 equals the current official checksum:
  `2d95ad99361039b556c402b49e0e7c84df5f00106dc5731d44476a58b128b49b`.
- Eight independently selected 1 MiB live/local byte ranges matched.

The full scan completed in 97.1 seconds with 200,000-row explicit-column FITS chunks and
checkpointed Parquet match parts. This is a concrete process acceleration: interrupted runs resume
from verified chunks, while full reruns remain short enough to use as a routine integrity gate.

## 4. Immutable inputs and reproduction

Historical inputs are pinned at `p3-v3.1.161`, resolving to commit
`cdaaa03a72c69d86f011be128d93f261dc5b39a8`:

- `https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog/resolve/p3-v3.1.161/pathc_unique_objects.parquet`
  - SHA-256 `b14deb02ddc374cc30a54e6013c0695d1c35cbf18cef9144245e338d6138c643`
- `https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog/resolve/p3-v3.1.161/desi_dr1_anomalies.parquet`
  - SHA-256 `0a36b8d6dfb8086c2c417885c99689d7a75b416dad1b030db56477baf103ec65`

Both URLs returned HTTP 200 on 2026-07-14. Fresh downloads independently matched the recorded
hashes. The public DESI input and checksum URLs also returned HTTP 200. Exact download, build, and
validation commands are present in the release `README.md`, `PROVENANCE.json`, bundled builder,
and manuscript Data Availability section.

## 5. Immutable release evidence

Public dataset: `bamfai/bigbounce-anomaly-catalog`  
Release path: `releases/p3-v3.2.0/`

| Revision | Commit | Disposition |
|---|---|---|
| `p3-v3.2.0` | `f2df8c00284350a7fe84a4ba6eb06468408b1c49` | Preserved original immutable release. |
| `p3-v3.2.0-r1` | `983209ae606be311d9bda9f0258716d56386ee69` | Canonical metadata-complete correction; adds immutable-input URLs and concrete commands. |

After tag creation, all 11 files were downloaded from `p3-v3.2.0-r1` and compared with the local
release. Every byte count and SHA-256 matched. The release manifest contains 10 payload entries and
excludes itself to avoid a self-referential hash; a separate shell audit recomputed all 10 hashes
and byte sizes successfully.

Key release hashes:

- `RELEASE_MANIFEST.json`:
  `ec86b06ccc69ff10ea50580302801d8c8df365e9ba8d4adbd67fdd19c5552b5a`
- released Parquet:
  `ae1e992c766a0efd13ccbe7feaa9c3c554b0a97e61c8d632af4a45da1e78c6ca`
- bundled/source builder:
  `2b619995146d7a50e940f396d72f24e068f1de331ffe67ccf94a4523b3eb2ae8`
- bundled/source independent validator:
  `36327825a56b1b4ef18fcfe9d5ac4f966b6198378a63bf01543f3dc82ef28e96`

## 6. Exact manuscript evidence

Canonical source: `pipelines/p3_anomaly_engine/paper3_apjs.tex`  
Compiled PDF: `pipelines/p3_anomaly_engine/paper3_apjs.pdf`

- TeX SHA-256:
  `fad611e9fd3b5e19daaa9db4aac529569e0c2cf4ba6c53c59a89d8d6c1171249`
- PDF SHA-256:
  `3dc9d45862ccaad2ae7c61db991e5a5b7025390876c492905e127bdde3308db8`
- PDF size: 411,679 bytes
- Pages: 11, US letter
- Conservative abstract word count: 239 (below the 250-word AAS limit)
- Selection-waterfall figure SHA-256:
  `e5332de32fa771ccfba11194411ae24debb6c638b91de675ea21c81865c65770`
- Catalog-overview figure SHA-256:
  `8690353505ff025fa19b289416233974f500c5ca7ab9789a45de2f7c5204835c`

Compilation used:

```sh
PATH="$HOME/Library/TinyTeX/bin/universal-darwin:$PATH" \
  latexmk -pdf -interaction=nonstopmode -halt-on-error paper3_apjs.tex
```

Final log audit found:

- zero overfull boxes;
- zero underfull boxes;
- zero unresolved citations or references;
- zero deferred/stuck-float warnings;
- zero placeholder/PENDING markers;
- one `nameref` warning: `The definition of \label has changed!`.

The remaining warning is not caused by this manuscript. A two-pass one-line minimal document using
only `\documentclass[twocolumn]{aastex701}` reproduces it under the installed LaTeX 2026 kernel and
AASTeX 7.0.1. It occurs while the class loads `hyperref/nameref`, before manuscript packages or
content. Suppressing it would hide class/kernel evidence without changing output, so it is recorded
as non-actionable rather than masked.

## 7. Visual and URL audit

All 11 final pages were rendered at 144 dpi and inspected. The final checks found:

- no text, URL, table, figure, or date overflow;
- no clipping or inter-column overlap;
- readable figure labels and captions;
- references before appendices;
- appendix A specification followed by B field tables and C audit matrix;
- no blank pages;
- no rotated pages or tables;
- all 11 raster pages nonblank by byte-size check.

Pages 1--8 of the final render were pixel-identical to the previously inspected render; pages 9--11
were reinspected at original image resolution after the table-layout repair.

Every URL encoded by the manuscript, plus the exact r1 release-tree URL, returned HTTP 200 during
the final audit. This included the two immutable historical inputs, the public DESI directory, the
public dataset, the exact r1 tree, and the repository script path.

## 8. Never-fabricate audit and remaining limitations

Every quantitative manuscript claim in this recovery is traceable to the released Parquet,
`COHORT_COUNTS.json`, `QC_REPORT.json`, `SELECTION_AUDIT.json`, `PROVENANCE.json`, or the public DESI
source row. The paper explicitly retains the following limitations:

1. historical score/residual lineage was preserved, not regenerated;
2. `ZWARN == 0` makes the release a quality-conditioned, incomplete subset;
3. a 1 arcsec positional association is not proof of physical identity in every field;
4. no object-by-object astrophysical novelty or physical-anomaly vetting was performed;
5. the footprint and overlapping target classes are inherited and not completeness-corrected;
6. the public redshift catalog is version-specific and may later be superseded.

Searches for the rejected aggregate counts, placeholders, unsupported detection language, and
unqualified occurrence-rate claims found no live claim that contradicts these limitations. The
phrase “hundreds of thousands of validated detections” remains only in an explicit sentence
rejecting that unsupported implication.

## 9. Readiness hold and independent-review handoff

This lane closes the concrete structural, data-integrity, provenance, release-immutability, and PDF
layout work. It does **not** self-adjudicate scientific readiness. P3 readiness must remain unchanged
until independent reviewers inspect the exact artifacts identified by the hashes above and return
their own finding matrix. The next panel must use the exact `p3-v3.2.0-r1` data tag and the exact PDF
SHA-256 `3dc9d458...3308db8`; any later edit requires a new hash and a fresh review.

Required independent panel questions:

1. Is the structural scope scientifically coherent and appropriately limited for ApJS?
2. Are the selection and duplicate rules defensible and fully described?
3. Does the 0.1--1 arcsec tail require manual object-level adjudication before publication?
4. Are any claims stronger than the released evidence?
5. Does the data package satisfy object-level reuse and reproducibility expectations?
6. Is the paper acceptable/minor-revisions-only, or are further blocker/major changes required?

Only after that exact-artifact panel closes its findings should the director update shared
readiness, SSOT, Convex, site papers/reviews/PDF mirrors, or project-wide versions.
