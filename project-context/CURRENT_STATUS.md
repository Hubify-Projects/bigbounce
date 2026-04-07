# Current Status: BigBounce Research Program

**Last updated: 2026-04-06**

## Papers

| Paper | Version | Pages | Status | Notes |
|-------|---------|-------|--------|-------|
| Paper 1 (Spin-Torsion Cosmology) | v2.2.0 | 24 | Ready for submission | 14 ECH barriers, ALP birefringence, bounce model discrimination table, 63+ refs |
| Paper 2 (f_NL Forecast) | v1.3.0 | 12 | Ready for submission | f_NL = -35/8 (parameter-free), SPHEREx testable, Fisher forecast |
| Paper 3 (DESI DR1 Anomaly Catalog) | v0.1 draft | — | In progress | 195K anomalous objects from 18M spectra, autoencoder-based |
| Paper 4 (Chirality Catalog) | — | — | ~85% ready | 8.47M galaxies, CW/(CW+CCW)=0.4974, dipole=0.43σ (null). Needs confusion matrix, training curves, redshift distribution |

## Multi-Survey Anomaly Sweep

**33.5M sources processed, 328K+ anomalies detected across 8 surveys:**

| Survey | Sources | Anomalies | QC Status |
|--------|---------|-----------|-----------|
| DESI DR1 | 22.5M | 195,829 (0.87%) | PASS — 2,145 SNR-filtered, 1,127 uncataloged |
| SDSS DR18 | 2.3M | 77,905 (3.4%) | PASS — domain shift scores noted |
| LAMOST DR10 | 11.4M | 44,075 (0.39%) | PASS — 98% blue-excess bias (known) |
| eROSITA DR1 | 930K | 9,303 (1%) | PASS — 73% novel |
| Planck CMB | 20K patches | 193 | FIXED — galactic GAL080 mask applied (was QC FAIL) |
| ACT DR6 | 20K patches | 200 | FIXED — 100 epoch proper training (was QC FAIL) |
| NEOWISE | 43.5K | 444 | FIXED — ecliptic mask applied (was QC FAIL) |
| Gaia DR3 | 50K → 500K | 5,000 | FIXED — 10x expansion (was too small) |

## Queue v2 Progress

**Phases 1-3 COMPLETE (17/18 experiments). Phase 4 RUNNING.**

| Phase | Status | Highlights |
|-------|--------|------------|
| 1: Re-run broken | **COMPLETE** | Planck masked, ACT trained, NEOWISE masked, Gaia 10x expanded |
| 2: Validation | **COMPLETE** | SIMBAD cross-match (479 known), injection recovery, spatial clustering, score distributions |
| 3: Cross-survey | **COMPLETE** | SDSS×LAMOST (30 overlap), multi-messenger (40 joint), Planck×ACT (0 — independent) |
| 4: Science | **RUNNING** | f_NL bias validation, LAMOST tracer, threshold sweep, NANOGrav MCMC, combined PTA |
| 5-10 | Pending | New surveys, ML re-runs, full-sky scans, papers |

## Active Compute

- **H200 pod** `o76k3jfzbfh25e`: SSH `root@205.196.19.52 -p 11452`
- **Phase 4** running in tmux session `phase4` (5 experiments chained)
- **Monitor**: `ssh root@205.196.19.52 -p 11452 -i ~/.ssh/id_ed25519 "tail -20 /workspace/bigbounce/phase4_runner.log"`

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
- NANOGrav 15yr: γ = 3.0 (bounce) vs 3.2 ± 0.6 (observed) — 0.33σ consistent

## Website

- **Live:** https://bigbounce.hubify.app
- **Deployment:** Netlify auto-deploys from `main` branch
- 12+ pages: Research, Papers, Explainer, Data Explorer, Figures, Glossary, Articles, Timeline, Visualize, Activity, Dossier, Datasets
