# P5 — arXiv submission bundle

**Bundle:** `arxiv_p5_v0.1.102.tar.gz`
**Paper version:** v0.1.102-2026-07-06
**Date:** July 6, 2026
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

## Verification (2026-07-06)

- **Fresh recompile from clean:** 3-pass pdflatex (inline thebibliography, no bibtex needed),
  0 LaTeX errors, 0 undefined refs/citations, 37 pages, 1,315,622 bytes (md5 191d698702a805b4805dded18608f48c).
- **latex-audit:** 0 overfull hboxes (total); 0 undefined references.
- **Tarball standalone-compile:** extracted into a pristine temp dir, compiled
  from zero → 0 errors, 0 undefined refs/citations, 37 pages (matches canonical).
  Standalone compile confirmed PASSED. Tarball md5 822ce2fafd2cbfb0dca0e12f22df3b7c.

## Review status (verified, 2026-07-05/06 round)

Latest verifiable EXT+INT round (raw reviewer text + screenshots in
`project-context/peer-reviews/EXT_real/ROUND_2026-07-05/P5_*` and
`INT_v3/ROUND_2026-07-05/P5_INT_claude.md`): INT (Claude, full-source, verified
every headline number exact) = MINOR; Grok = MINOR REVISIONS; Gemini = MAJOR
REVISIONS; ChatGPT = REJECT. The dominant finding across all four reviewers is
the Paper-IV dependency, which this v0.1.102 addresses via the coordinated-
submission reframe (see below) — converting the structural major into a
citation-timing note. Remaining ChatGPT/Gemini majors (systematics-budget
completeness, RSD/T-Web scope, statistical independence) are disclosed limitations
already in-text; readiness cap is Houston's call, not hand-set here.

## Paper-IV reframe (v0.1.102)

Paper IV = the companion chirality-catalog paper in THIS repo
(`pipelines/p2_chirality/`, at the Grok+Gemini gate, first-wave submission). The
dependency closes by **coordinated submission**: P4 posts to arXiv first, P5
cites its real arXiv ID same-day. In the source, every Paper-IV reference now
routes through the single `\paperIVarxiv` macro (placeholder `arXiv:XXXX.XXXXX`);
the headline Δf_CW is foregrounded as monopole-shift invariant and refereeable
from public GZ1/DESI/DESIVAST data alone; and the catalog's model-free
pseudo-label independence (GZ1-human-only null, z=−0.54σ, N=46,017) is cited.

## Status

**READY TO SUBMIT — same day, AFTER P4** (prep only; Houston submits). Tarball
standalone-compiles clean; all links resolve. **Coordinated submission:** post P4
to arXiv first, then insert P4's real arXiv ID into `\paperIVarxiv` in
`p5_desi_chirality.tex` (single insertion point), recompile, rebuild this tarball,
and submit P5. See `SUBMISSION_NOTE.txt`.
