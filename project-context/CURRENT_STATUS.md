# Current Status: BigBounce Research Program

**Last updated: 2026-04-02**

## Papers

| Paper | Version | Pages | Status | Notes |
|-------|---------|-------|--------|-------|
| Paper 1 (Spin-Torsion Cosmology) | v2.2.0 | 24 | Ready for submission | 14 ECH barriers, ALP birefringence, bounce model discrimination table, 63+ refs |
| Paper 2 (f_NL Forecast) | v1.3.0 | 12 | Ready for submission | f_NL = -35/8 (parameter-free), SPHEREx testable, Fisher forecast |
| Paper 3 (DESI DR1 Anomaly Catalog) | v0.1 draft | — | In progress | 195K anomalous objects from 18M spectra, autoencoder-based |
| Paper 4 (Chirality Catalog) | — | — | ~85% ready | 8.47M galaxies, CW/(CW+CCW)=0.4974, dipole=0.43σ (null). Needs confusion matrix, training curves, redshift distribution |

## Multi-Survey Anomaly Sweep

**32.3M spectra processed, 327K anomalies detected across 4 surveys:**

| Survey | Spectra | Anomalies | Status |
|--------|---------|-----------|--------|
| DESI DR1 | 18M | 196K | Complete |
| SDSS | 3.9M | 78K | Complete |
| LAMOST | 11.4M | 44K | Complete |
| eROSITA | — | 9.3K | Complete |

## Active Compute

- **H200 pod** running full research queue: Planck CMB → ACT DR6 → NEOWISE → Gaia → cross-match → super-res
- Monitor with `research_monitor.sh`

## MCMC Results

- 424,181+ posterior samples across 3 frozen dataset combinations
- w0-wa quintom converged: P(quintom-B) = 98.6%, favored at 2.3σ
- NANOGrav 15yr: matter bounce γ = 3.0 vs observed 3.2 +/- 0.6 (0.33σ consistent)
- ΔNeff ≈ 0 in all datasets; H0 = 67.68 (standard ΛCDM)

## Key Scientific Results

- 14 structural barriers close all ECH-specific routes from bounce to dark energy
- ALP birefringence prediction β = 0.27° matches 3.6σ observed signal (0.342 +/- 0.094°)
- Branch V matter bounce: f_NL = -35/8 = -4.375 (parameter-free, mechanism-independent)
- f_NL triple role: galaxy bispectrum + PBH abundance regulator + induced GW spectral shape
- Bounce model discrimination table: matter bounce vs Cuscuton vs ekpyrotic vs quintom vs inflation

## Website

- **Live:** https://bigbounce.hubify.app
- **Deployment:** Netlify auto-deploys from `main` branch
- 12+ pages: Research, Papers, Explainer, Data Explorer, Figures, Glossary, Articles, Timeline, Visualize, Activity, Dossier, Datasets

## Key Next Steps

1. **Pipeline 1 tracer purification** — steps 2-6 (cross-match, classify, validate bias, re-measure σ(f_NL), paper) after H200 queue finishes
2. **Finish chirality paper** — add confusion matrix, training curves, redshift distribution to Paper 4
3. **Back up H200 results** — download all outputs after queue completes before pod termination
