# P1B — arXiv submission bundle

**Bundle:** `arxiv_p1b_v1B.0.96.tar.gz`
**Paper version:** v1B.0.96
**Date:** July 3, 2026
**Primary arXiv category:** astro-ph.CO
**Cross-list (suggested):** gr-qc

## Title

Technical Reproducibility and Consistency-Check Companion to the ECH
Spin-Torsion Program: ΛCDM+ΔN_eff MCMC Proxy, NaMaster Pipeline Recovery, and a
Birefringence Consistency Check with a Spectator-ALP Model

**Author:** Houston Golden — houston@hubify.com — Independent Researcher, Los Angeles, California, USA

## Abstract

We report the technical reproducibility and consistency-check material for the
Einstein-Cartan-Holst (ECH) spin-torsion cosmology no-go program of Paper I(a).
Scope, stated up front: none of the three analyses implements or tests a
torsion-modified Boltzmann/theory module, and none verifies the ECH spin-torsion
sector — each is an adjacent numerical cross-check, so the contribution is a
reproducibility and null-consistency note, not independent evidence for the
theory. Three analyses are documented. (1) Stock-CAMB ΛCDM+ΔN_eff MCMC proxy
(Cobaya v3.6.1, 309,189 frozen samples across two converged dataset
combinations): ΔN_eff is consistent with zero (−0.020 ± 0.169 full-tension;
+0.065 ± 0.17 Planck+BAO+SN) and H0 with standard ΛCDM (67.68 ± 1.06;
67.79 ± 1.09 km/s/Mpc); stock CAMB carries no torsion modifications, so this is a
null-consistency test of an extra radiation-like degree of freedom. (2) NaMaster
pseudo-Cl pipeline validation on the Planck Commander polarization map
(Nside=512, 500 MC realizations): injecting β = 0.27° recovers 0.238°
(bias 0.032°); an fsky sweep (0.85, 0.65) shows the recovery bias is
fsky-independent and well below the published σ_β = 0.094°. The test validates
the algebraic E→B deconvolution under MASTER mode coupling, not the physical
separation of the cosmic-rotation angle from instrumental miscalibration —
recovery figures are pipeline validation, not sky measurements. (3) Spectator-ALP
consistency check against the published joint WMAP+Planck β = 0.342 ± 0.094°
(3.6σ): a field with f_a ~ M_Pl, m ~ H0 is consistent, with a continuous-prior
MCMC over the photon coupling C_aγ in [4,60] placing 69% of the posterior mass in
the EOM-required band [9,51] (median 20.7); the spectator label requires
θ_i ≪ 1 (fine-tuned misalignment), and the same birefringence arises in standard
GR with an identical ALP — it is not a distinctive ECH prediction. A
reproducibility manifest is included.

## Bundle contents

- `paper1b_mcmc_companion.tex` — single source (revtex4-2, PRD two-column).
- `paper1b_mcmc_companion.bbl` — **required**: the paper uses
  `\bibliography{references}` (bibtex), so the compiled `.bbl` ships in the
  tarball (arXiv does not re-run bibtex). No `.bib` file is needed.
- 4 figures under `figures/` (the `.tex` references them as `figures/...`, so the
  subdirectory structure is preserved): `paper1_corner_full_tension.pdf`,
  `fig_dneff_viability_two_frozen.pdf`, `fig_namaster_recovery.png`,
  `alp_triangle_plot.png`.

## Verification (2026-07-03)

- **Fresh recompile from clean:** pdflatex → bibtex → pdflatex ×2, 0 LaTeX
  errors, 0 undefined refs/citations, 21 pages, 1,151,239 bytes. (The bibtex
  run emits the standard apsrev4-2 "not the same literal types" / "missing
  journal" chatter for JCAP/JHEP-style abbreviation macros — non-fatal; the
  `.bbl` is produced and all citations resolve.)
- **latex-audit:** 0 overfull hboxes (0 total, 0 >50pt); 0 undefined references.
- **Tarball standalone-compile:** extracted into a pristine temp dir, compiled
  from zero (pdflatex ×2, no bibtex — shipped `.bbl` used) → 0 errors,
  0 undefined refs/citations, 21 pages. Standalone compile confirmed PASSED.

## Convergence status

P1B **CONVERGED** at v1B.0.95 (bundle rebuilt to v1B.0.96 for tarball freshness).
After the exploratory overlap-uncorrected w0wa appendix was surgically removed
(v1B.0.95) — the sole basis of the prior Gemini REJECT — the targeted external
re-check returned **Gemini ACCEPT + Grok MAJOR REVISIONS**, with **0
genuinely-new findings** surviving truth-audit (Grok's MAJOR is a subjective
companion-note venue opinion plus re-flags of already-disclosed, in-scope
content). The core ECH/torsion ΔN_eff + NaMaster + ALP analyses were untouched
by the cut.

## Status

**READY TO SUBMIT** (prep only — Houston submits). Recompile clean, latex-audit
clean, all links resolve, tarball standalone-compiles byte-identical. Submit-ready
alongside P4/P5. Grok's residual MAJOR is a subjective venue/scope opinion the
author can address in the cover letter (frame as a PRD companion / supplementary
to Paper 1A, or an ApJS reproducibility note), not a correctness defect.
