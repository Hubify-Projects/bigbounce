# P5 — arXiv submission bundle

**Bundle:** `arxiv_p5_v0.1.100.tar.gz`
**Paper version:** v0.1.100-2026-07-01
**Date:** July 1, 2026
**Primary arXiv category:** astro-ph.CO
**Cross-list (suggested):** astro-ph.GA

## Title

Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Void
Null Test on 56,981 DESI DR1 Spirals, with a Secondary Tidal-Tensor
Cross-Check

**Author:** Houston Golden — houston@hubify.com — Independent Researcher, Los Angeles, California, USA

## Abstract

We cross-match the 8,474,531-galaxy chirality catalog of our companion work
with the DESI Data Release 1 redshift catalog to test whether spiral galaxy
handedness is statistically independent of large-scale-structure environment.
The 1-arcsec matched catalog contains 2,232,212 unique galaxies, of which
791,635 carry an unambiguous equivariant CW/CCW label. DESIVAST provides the
primary void anchor (three void-finding algorithms); a tidal-tensor cosmic-web
classification of 14.1 million DR1 galaxies assigns every matched spiral to
{void, wall, filament, cluster}, including 56,981 void spirals. Headline result:
chirality is statistically independent of cosmic-web environment -- no class
deviates from parity after look-elsewhere correction (omnibus chi-squared
p = 0.31 canonical; p = 0.99 after z-shell selection-function correction, under
which class populations migrate massively -- void x10, wall x23 -- yet the
cross-class CW-fraction range tightens from 1.98 to 0.05 percentage points).
The null is robust to a depth- and program-stratified permutation null, a
brightness split, a Tempel-catalog cross-validation, and a logistic regression
with full physical covariates (size, magnitude, morphology, inclination, merger
disturbance; 100% Galaxy Zoo DESI join), in which every environment coefficient
is null after adjustment. These results constrain environment-coupled
parity-violation models at the sub-percent level across the void-to-cluster
density range and complement the all-sky dipole null of the companion catalog
paper.

## Bundle contents

- `p5_desi_chirality.tex` — single self-contained source (revtex4-2, PRD
  two-column). Bibliography is an **inline `\begin{thebibliography}`** — no
  `.bbl`/`.bib` file is required in the tarball (the pre-existing
  `p5_desi_chirality.bbl` in the source dir is a stale bibtex artifact and is
  intentionally NOT shipped).
- 9 figures: `fig_cw_vs_z.png`, `fig_p5_cw_by_env_bar.png`,
  `fig_p5_cw_vs_density.png`, `fig_p5_healpix_skymap_nside32.png`,
  `fig_p5_phase2_sensitivity_heatmap.png`, `fig_p5_voids_vs_chirality_skymap.png`,
  `fig_p5_volume_fractions_pie.png`, `fig_p5_vweb_vs_tempel_overlay.png`,
  `fig_z_histogram.png`.

## Verification (2026-07-01)

- **Fresh recompile from clean:** 3-pass pdflatex, 0 LaTeX errors, 0 undefined
  refs/citations, 36 pages, 1.2 MB.
- **latex-audit:** 0 overfull hboxes >50pt (0 overfull hboxes total); tables use
  `table*`/`ruledtabular`; title block (long title + footnote) clean; page 1 +
  wide-table pages rendered and visually confirmed — no column escape.
- **Tarball standalone-compile:** extracted into a pristine temp dir, compiled
  from zero → 0 errors, 0 undefined refs/citations, 36 pages (matches canonical).
- **Artifact/external links:** all GitHub `\artifact{}` file + directory paths
  resolve on origin/main (directory links use `/blob/` but GitHub auto-resolves
  them to the tree view — HTTP 200, not broken); DESI DR1 public data URLs
  (dr1 root, iron zcatalog, desivast v1.0) all HTTP 200; HuggingFace dataset +
  model HTTP 200; both DOIs (`10.1016/j.physrep.2009.07.002`,
  `10.1103/PhysRevLett.83.1506`) confirmed real via Crossref (the APS DOI returns
  403 to curl only because journals.aps.org bot-blocks non-browser agents; it
  resolves in a browser).
- **Broken links found:** none. No link fix was required for P5.

## Convergence status

Genuine multi-vendor peer-review convergence at the RS11 floor
(Grok + Gemini convergent ACCEPT/silence; 0 genuinely-new findings surviving
truth-audit; P5 earned individual ACCEPTs including an OpenAI leg that
re-derived every scalar). Every genuine scientific and reproducibility defect is
closed, including the Appendix-A parity-EFT operator reformulation.

## Status

**READY TO SUBMIT** (prep only — Houston submits). Tarball standalone-compiles
clean; all links resolve. Submit AFTER P4 — the abstract cites P4 as the
companion catalog paper, so P4's arXiv ID should be minted first and dropped into
the P5 citation if a cross-reference is desired.
