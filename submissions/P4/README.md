# P4 — arXiv submission bundle

**Bundle:** `arxiv_p4_v1.0.217.tar.gz`
**Paper version:** v1.0.217 (RETEST v215→v217 EXT closure; Grok + Gemini both MINOR REVISIONS, central claim robustly supported; INT ACCEPT)
**Date:** July 5, 2026
**Primary arXiv category:** astro-ph.CO
**Cross-list (suggested):** astro-ph.GA

## Title

Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space
Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic
Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47
Million DESI Legacy Galaxies (3.2 Million Spirals)

**Author:** Houston Golden — houston@hubify.com — Independent Researcher, Los Angeles, California, USA

## Abstract

We present, to our knowledge, the largest chirality-labeled galaxy catalog to
date: 8,474,531 DESI Legacy DR8 galaxies classified by a flip-equivariant Vision
Transformer pipeline (3,201,160 spirals), publicly released with model weights
and reproducibility scripts. The headline result is a null real-space chirality
dipole: the high-confidence (p_eq > 0.6, N ≈ 9.5×10^5) post-TTA Catalog C dipole
fit gives +0.41 sigma (rank-p = 0.31, isotropic pixel-permutation null,
N_MC = 10,000), and a block-bootstrap WLS template fit disfavors a clean
cosmological dipole at the 1.7% reference amplitude at z ≈ -18. This l=1
observable is the isotropy-breaking axial-vector channel and is parity-EVEN, not
a direct parity-violation test. The MASTER-deconvolved pseudo-Cl channel on the
patchy footprint is a systematics diagnostic, not an independent null: a
controlled monopole-only generative null reproduces 99.32% of the observed
pre-MASTER pseudo-Cl(l=1) power. Post-MASTER residuals (+3.64 sigma canonical;
+7.28 sigma apodized weighted footprint, unchanged under depth-stratified nulls)
are attributed to a coherent depth/morphology-correlated systematic by an
eight-anchor battery. A future-survey detection at >5 sigma with amplitude
A ≳ A95 (bracketed in (1.0%, 1.5%]) would be in tension with the present null
(empirical 50%-recovery-at-3-sigma threshold A50 ≈ 0.75%). A fully
model-independent GZ1 human-vote cross-check (N = 46,017, no learned model in the
label chain) recovers the same null (z = -0.54 sigma). The catalog, model
weights, and all reproducibility scripts are publicly released.

## Bundle contents

- `chirality_catalog_paper.tex` — single self-contained source (revtex4-2, PRD
  two-column). Bibliography is an **inline `\begin{thebibliography}`** — no
  `.bbl`/`.bib` file is required in the tarball.
- 12 figure files: `fig_bootstrap_null.png`, `fig_class_pie.png`,
  `fig_confidence_dist.png`, `fig_equivariance_demo.png`, `fig_gallery_ccw.png`,
  `fig_gallery_cw.png`, `fig_gallery_notspi.png`,
  `fig_harmonic_completeness.pdf`, `fig_multipoles.png`, `fig_raw_vs_eq.png`,
  `fig_sky_map.png`, `fig_spiral_density.png`.

## Verification (2026-07-06)

- **Fresh recompile from clean:** 4-pass pdflatex, 0 LaTeX errors, **0 undefined
  refs/citations**, **31 pages**, ~34 MB.
- **latex-audit:** **0 overfull hboxes**; tables use `table*`/`ruledtabular`;
  title block clean (dated July 5, 2026); page 1 (the dense single-column
  abstract) rendered and visually confirmed — no column escape or overflow.
- **Served-PDF integrity:** the versioned served file
  (`chirality_catalog_paper_v1.0.217.pdf`) and its aliases are byte-identical
  (md5 `b62c22be…`, 33,998,415 bytes) across all served paths (`public/papers/`
  versioned + `chirality_catalog_paper.pdf` + `p4-chirality.pdf`, and the mirror
  under `site/public/papers/`); content matches a fresh compile of the committed
  source.
- **Convex:** `paperVersions` current = v1.0.217 (31pp, md5 `b62c22be…`,
  tarball path recorded); live site reflects the true state.
- **Headline-number spot-check vs committed outputs:** real-space dipole
  +0.41σ / p=0.31 / amplitude 4.4×10⁻³ / (l,b)=(293°,12°); label-shuffle z=0.58;
  GZ1 human-vote null z=−0.54 / rank-p=0.67 / CW-fraction 0.4836 — all match the
  manuscript exactly (`outputs/dipole/catalog_c_summary.json`,
  `outputs/gz1only_fullN_dipole_result.json`).
- **Figure/table counts:** 10 figure floats, 14 tables, 31 pages.

## Convergence status

At the recalibrated Grok+Gemini gate (Directive H): Grok + Gemini both return
MINOR REVISIONS with the central null explicitly "robustly supported"; INT
ACCEPT. ChatGPT REJECT is record-only per gate H (structural harsh-referee floor;
its MAJORs are dispositioned in truth-audit). Two pod-gated *strengthening* items
remain honestly deferred (never fabricated): (1) the full per-pixel morphology
*attribution* of the ~47% unmodelled l=1 residual (bounded now: its cosmological
content is < the A_50 real-space floor, so it cannot be a coherent dipole), and
(2) the edge-on-*isolated* tie-break variant (the leg-resolved band statistic
already answers the coherence concern; the population is inside the +0.41σ null).

## Status

**READY TO SUBMIT** (prep only — Houston submits). Tarball is a complete,
self-contained arXiv source bundle (`.tex` v1.0.217 + all 12 figures, inline
bibliography); every `\artifact{}` path resolves on `main`. Submit before P5
(P5's abstract cites this paper as its companion catalog paper).
