# P4 — arXiv submission bundle

**Bundle:** `arxiv_p4_v1.0.219.tar.gz` (md5 `aa5dca1b611196c0e1dca6d3cc827c0e`, 25MB)
**Paper version:** v1.0.219 (D-round final polish: condensed title + reader-first abstract + expanded AI-methods disclosure; presentation-only, no science number changed)
**Date:** July 6, 2026
**Primary arXiv category:** astro-ph.CO
**Cross-list (suggested):** astro-ph.GA

## Title

A Null Chirality Dipole in 8.5 Million DESI Galaxies from Equivariant Deep Learning

**Author:** Houston Golden — houston@hubify.com — Independent Researcher, Los Angeles, California, USA

## Abstract

We measure the large-scale chirality dipole of spiral galaxies and find it
consistent with null. Our primary estimator --- a real-space dipole fit to the
high-confidence equivariant sample (N ~ 9.5x10^5 spirals) --- gives +0.41 sigma
(moment-z against an isotropic pixel-permutation null; empirical-rank p = 0.31,
10^4 realizations), and a block-bootstrap WLS template fit disfavors a clean
cosmological dipole at the 1.7% reference amplitude (the lower end of Shamir's
reported 1.7%-4.0% range) at z ~ -18. This ell=1 observable is parity-even (an
isotropy-breaking axial-vector channel), not a direct parity-violation test. The
measurement rests on the largest chirality-labeled galaxy catalog to date:
8,474,531 DESI Legacy DR8 galaxies classified by a flip-equivariant Vision
Transformer into clockwise (CW), counter-clockwise (CCW), and non-spiral classes,
with N_spiral = 3,201,160 spirals, released publicly with model weights and
reproducibility scripts. The p_eq > 0.6 confidence cut is pre-specified (not
tuned post-hoc): the null is robust across the high-confidence regime (p_eq in
{0.6,0.7,0.8}) of a full confidence-cut sweep, while the low-confidence tail
(p_eq <= 0.5) carries a systematics-attributed excess (z ~ 4.0-4.3). The
real-space null holds under a per-galaxy label-shuffle test (z = 0.58
same-generator, z = 0.70 independent re-implementation). We are explicit about
two limitations. First, the MASTER pseudo-C_ell harmonic channel on this patchy
footprint is a systematics diagnostic, not an independent cosmological null: a
monopole-only generative null reproduces 99.32% of the raw pre-MASTER ell=1 power
(monopole-mask leakage), and MASTER deconvolution reduces but does not remove it,
leaving systematics-attributed residuals (+3.64 sigma canonical mask, ~1.9 sigma
Gaussian-equivalent; +7.28 sigma apodized footprint) that we attribute to
residual survey systematics via an eight-anchor battery rather than claim as
detections. Second, the various sigma values quoted above come from distinct null
procedures, so they are diagnostic indicators and are not directly comparable to
one another as detection significances. Falsification criterion: a future
real-space dipole detection at >= 5 sigma with amplitude A >~ A_95, where
injection-recovery brackets A_95 in (1.0%, 1.5%] (A_50 ~ 0.75%), would be in
tension with this null.

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
  title block clean (dated July 6, 2026); page 1 (the dense single-column
  abstract) rendered and visually confirmed — no column escape or overflow.
- **Served-PDF integrity:** the versioned served file
  (`chirality_catalog_paper_v1.0.219.pdf`, md5 `e8b4f10a9bcc9545aeb58869395e7d06`)
  and its aliases are byte-identical across all served paths (`site/public/papers/`
  versioned + `chirality_catalog_paper.pdf` + `p4-chirality.pdf`, and the mirrors
  under `site/public/`); content matches a fresh compile of the committed source.
- **Convex:** `paperVersions` current = v1.0.219 (31pp, md5 `e8b4f10a…`,
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
