# P5 v0.1.130 closure audit

## Purpose

This is a structural closure against the exact v0.1.129 PRD and AJ review
boards. It does not represent a new external review, an acceptance decision,
or a readiness uplift.

## Structural changes

- Recast the title and paper around a catalog-native DESIVAST DR1 test.
- Designated one released-parent estimator: DESIVAST GALZONE rows with
  `OUT=0`, analyzed by covariate standardization and coarse-sky
  cluster-sandwich inference.
- Declared the hierarchy change post-review, post-hoc, exploratory, and not
  preregistered.
- Demoted author-defined any-hole/sphere-PIS paths, historical DESIVAST
  variants, T-Web, Tempel, ASTRA, and concurrent-literature overlays to
  sensitivity or secondary-diagnostic status.
- Removed the heterogeneous 0.96 pp quadrature summary from the rendered
  manuscript. Individual perturbations remain separate and are not presented
  as a calibrated uncertainty budget, bound, or exclusion limit.
- Added the standard DESI acknowledgment, DESI DR1 citation, a sourced and
  non-quantitative Rubin/LSST extension, and explicit Paper IV dependency.
- Split and then co-placed the artifact map without blank pages.

## Exact designated result

Source artifact:
`pipelines/p5_desi_chirality/outputs/36_desivast_native_selection_control.json`
([A37] in the manuscript).

- N: 145,766
- non-void-minus-void adjusted contrast: +0.001256361596130571
- coarse HEALPix NSIDE=4 cluster-sandwich SE: 0.0034127443342044377
- 95% CI: [-0.005432494387353252, +0.007945217579614394]
- two-sided p: 0.712770179721297

The abstract, methods hierarchy, designated-results section, conclusion, and
PDF text all reproduce the rounded values N=145,766, +0.00125636,
SE=0.00341274, CI [-0.00543249,+0.00794522], and p=0.71277.

## Build and LaTeX audit

Command:

```sh
PATH="$HOME/Library/TinyTeX/bin/universal-darwin:$PATH" \
  latexmk -pdf -interaction=nonstopmode -halt-on-error p5_desi_chirality.tex
```

- Exit status: 0
- Pages: 38
- PDF bytes: 1,490,643
- Undefined references/control sequences: none
- Overfull boxes: none
- `Float too large`: none
- RevTeX emits deferred-float placement warnings at three internal output
  boundaries. These are retained in the exact log rather than suppressed.
  Every affected table and figure is present in the PDF, and the complete
  visual audit found no clipping, overlap, missing float, or blank page.
- Font warning: the document falls back from one unavailable OMS typewriter
  shape to the standard symbol font; rendered output is intact.

## Full visual audit

The exact frozen PDF was rendered with:

```sh
pdftoppm -png -r 110 P5_v0.1.130_AJ_structural_closure.pdf page
```

All 38 pages were inspected. Outcome: no column overflow, clipping, table or
figure overlap, illegible caption, broken equation, raw path escaping the
column, blank page, or missing bibliography/artifact-map content. Both halves
of the artifact map appear together on page 37; references appear on page 38.

## Link checks on 2026-07-14

- 200: DESI DR1 root
- 200: DESI DR1 Iron zcatalog
- 200: DESIVAST v1.0 VAC
- 200: public HuggingFace chirality catalog
- 200: public GitHub repository
- 200: DESI collaborating-institutions page
- 200: Rubin/LSST paper DOI
- 403 to automated `curl`: APS/PRL DOI landing page. The DOI is syntactically
  valid and the response is an access-control result, not evidence that the
  DOI is absent.

Artifact links A37--A40 are explicitly marked as pending the release-candidate
commit/push; the manuscript does not claim that an immutable tag or Zenodo DOI
already exists.

## Publication gates still open

1. Dispatch an exact-PDF v0.1.130 non-Anthropic review panel and truth-audit
   every finding before any status change.
2. Coordinate Paper IV review/acceptance and independently verifiable final
   label release; P5 explicitly makes acceptance conditional on this.
3. Create and verify the immutable public release tag and archival snapshot.
4. Re-check every A1--A40 link against the committed/tagged release.
5. Update SSOT/site/Convex only from the truth-audited exact-PDF result.

Readiness remains 74. No acceptance, minor-revisions-only, or publication-ready
claim is made by this closure.
