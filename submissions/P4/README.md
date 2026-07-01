# P4 — arXiv submission bundle

**Bundle:** `arxiv_p4_v1.0.208.tar.gz`
**Paper version:** v1.0.208 (bumped from v1.0.207 for the artifact-link fix below)
**Date:** July 1, 2026
**Primary arXiv category:** astro-ph.CO
**Cross-list (suggested):** astro-ph.GA

## Title

Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space
Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic
Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47
Million DESI Legacy Galaxies (3.2 Million Spirals)

**Author:** Houston Golden — houston@hubify.com — Independent Researcher, Los Angeles, California, USA

## Abstract

We report a multi-survey, equivariance-corrected angular dipole analysis of
3,201,160 DESI Legacy spiral galaxies (8.47M sources). The headline result is a
null real-space chirality dipole: the post-TTA Catalog C dipole fit gives
+0.43 sigma (p=0.30, isotropic-null bootstrap, N_MC=10,000), and a
block-bootstrap WLS template fit disfavors a clean cosmological dipole at the
1.7% reference amplitude at z~-18. This l=1 observable is the isotropy-breaking
axial-vector channel and is parity-EVEN, not a direct parity-violation test.
The MASTER-deconvolved pseudo-Cl channel on the patchy survey footprint is a
systematics diagnostic, not an independent null: a controlled monopole-only
generative null reproduces 99.3% of the observed pre-MASTER pseudo-Cl(l=1)
power -- a small uniform classifier monopole couples through patchy mask
geometry to inflate the raw dipole, explaining prior pre-MASTER detection
claims at the percent level. Post-MASTER residuals (+3.64 sigma canonical;
+7.3 sigma apodized weighted footprint, unchanged under depth-stratified nulls)
are attributed to a coherent depth/sampling-correlated systematic by a
five-anchor battery. A future-survey detection at >5 sigma with amplitude
A >~ A95 ~ 1.5-2% would be in tension with the present null (empirical
50%-recovery-at-3-sigma threshold A50 ~ 0.75%). The catalog (3.2M spirals),
model weights, and all reproducibility scripts are publicly released.

## Bundle contents

- `chirality_catalog_paper.tex` — single self-contained source (revtex4-2, PRD
  two-column). Bibliography is an **inline `\begin{thebibliography}`** — no
  `.bbl`/`.bib` file is required in the tarball (the pre-existing
  `chirality_catalog_paper.bbl` in the source dir is a stale bibtex artifact and
  is intentionally NOT shipped).
- 12 figures: `fig_bootstrap_null.png`, `fig_class_pie.png`,
  `fig_confidence_dist.png`, `fig_equivariance_demo.png`, `fig_gallery_ccw.png`,
  `fig_gallery_cw.png`, `fig_gallery_notspi.png`,
  `fig_harmonic_completeness.pdf`, `fig_multipoles.png`, `fig_raw_vs_eq.png`,
  `fig_sky_map.png`, `fig_spiral_density.png`.

## Verification (2026-07-01)

- **Fresh recompile from clean:** 3-pass pdflatex, 0 LaTeX errors, 0 undefined
  refs/citations, 29 pages, 32 MB.
- **latex-audit:** 0 overfull hboxes >50pt (0 overfull hboxes total); tables use
  `table*`/`ruledtabular`; title block clean; page 1 + table pages rendered and
  visually confirmed — no column escape.
- **Tarball standalone-compile:** extracted into a pristine temp dir, compiled
  from zero → 0 errors, 0 undefined refs/citations, 29 pages (matches canonical).
- **Artifact/external links:** all 24 GitHub `\artifact{}` paths resolve on
  origin/main; HuggingFace dataset (`bamfai/galaxy-chirality-catalog`), model
  (`bamfai/galaxy-chirality-v2`), parent dataset (`Smith42/galaxies`), and
  `rwightman/pytorch-image-models` all return HTTP 200.
- **Link fix applied this bundle:** the `\artifact{...canonical_mask_nside64.npy}`
  link pointed at a binary that was never committed (absent on disk AND on
  origin/main → dead 404). Reverted to plain `\texttt{canonical_mask_nside64.npy}`
  (consistent with how the same file is already cited in the Table caption).
  This is the only change vs v1.0.207.

## Convergence status

Genuine multi-vendor peer-review convergence at the RS11 floor
(Grok + Gemini convergent ACCEPT/silence; 0 genuinely-new findings surviving
truth-audit). P4 was version-frozen through multiple consecutive external ACCEPT
rounds; every genuine scientific and reproducibility defect is closed.

## Status

**READY TO SUBMIT** (prep only — Houston submits). The one broken artifact link
found in packaging is fixed in this bundle; tarball standalone-compiles clean;
all remaining links resolve. Submit before P5 (P5's abstract cites this paper as
its companion catalog paper).
