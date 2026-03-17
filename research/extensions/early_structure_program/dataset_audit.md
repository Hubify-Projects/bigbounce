# Early Structure Program — Dataset Audit

**Date:** 2026-03-13
**Scope:** All candidate data sources for Tracks A, B, and C
**Companion file:** `dataset_registry.csv` (machine-readable version)

---

## A. High-z SMBH / Quasar Data

### A1. Fan et al. 2023 — SDSS High-z Quasar Compilation

- **Source:** Fan, Bram, Carilli, Banados, et al. 2023
- **arXiv:** 2212.06907
- **What it measures:** Catalog of ~300 quasars at z > 5.7, with BH masses from single-epoch virial estimators (Mg II, C IV lines)
- **Public:** Yes (published in ARA&A review)
- **Machine-readable:** Partially. Table is published but not in a standard catalog format. Individual columns extractable from published tables.
- **License:** Journal copyright (ARA&A). Data points are factual and can be used.
- **Recommended role:** Primary catalog for Track A seed mass survey. Extract (M_BH, z, M_BH_err) for each object.
- **Quality notes:** Virial mass estimates carry ~0.3-0.5 dex systematic uncertainty. This is the most comprehensive high-z quasar compilation available.

### A2. Bogdan et al. 2024 — UHZ-1 (z = 10.1)

- **Source:** Bogdan, Goulding, Natarajan, et al. 2024
- **arXiv:** 2305.15458
- **What it measures:** X-ray detected AGN at z = 10.1 behind galaxy cluster Abell 2744. M_BH ~ 4 x 10^7 M_sun estimated from X-ray luminosity.
- **Public:** Yes (published in Nature Astronomy)
- **Machine-readable:** Single object — extract values from paper text.
- **License:** Journal copyright. Single data point is factual.
- **Recommended role:** Key high-z constraint for Track A. One of the most distant AGN known, with an exceptionally high M_BH/M_star ratio suggesting a heavy seed.
- **Quality notes:** BH mass estimate is indirect (X-ray luminosity, not virial). Magnified by cluster lensing (mu ~ 4-8). Systematic uncertainty is large but the object is remarkable regardless.

### A3. Maiolino et al. 2024 — GN-z11 AGN (z = 10.6)

- **Source:** Maiolino, Scholtz, Witstok, et al. 2024
- **arXiv:** 2305.12492
- **What it measures:** JWST NIRSpec detection of broad H-alpha in GN-z11, indicating AGN with M_BH ~ 1.6 x 10^6 M_sun.
- **Public:** Yes (published in Nature)
- **Machine-readable:** Single object — extract from paper.
- **License:** Journal copyright.
- **Recommended role:** Key high-z constraint for Track A. Highest-redshift spectroscopically confirmed AGN.
- **Quality notes:** BH mass from broad-line virial estimate. The broad-line identification is debated by some groups but has been confirmed by multiple analyses.

### A4. Larson et al. 2023 — CEERS AGN Candidates

- **Source:** Larson, Finkelstein, Kocevski, et al. 2023
- **arXiv:** 2303.08918
- **What it measures:** JWST CEERS survey AGN candidates at z ~ 4-8, with photometric and spectroscopic identifications.
- **Public:** Yes (published)
- **Machine-readable:** Table in paper; some objects have spectroscopic confirmation.
- **License:** Journal copyright.
- **Recommended role:** Supplementary sample for Track A at intermediate redshifts (z ~ 4-8).
- **Quality notes:** Some candidates lack spectroscopic confirmation. BH masses where available are virial estimates.

### A5. Harikane et al. 2023 — JWST UV Luminosity Functions (z > 8)

- **Source:** Harikane, Ouchi, Oguri, et al. 2023
- **arXiv:** 2208.01612
- **What it measures:** Galaxy UV luminosity functions at z = 9-17 from JWST early data. Not directly BH masses, but constrains the galaxy population hosting early AGN.
- **Public:** Yes
- **Machine-readable:** Luminosity function data points in tables.
- **License:** Journal copyright.
- **Recommended role:** Background context for Track A — constrains the host galaxy population.
- **Quality notes:** UV luminosity functions have been revised multiple times as JWST calibrations improved. Use latest calibration.

### A6. Greene et al. 2024 — Little Red Dots / High-z AGN Review

- **Source:** Greene, Labbe, Goulding, et al. 2024
- **arXiv:** 2309.05714
- **What it measures:** Review of JWST "little red dots" — compact, red sources at z ~ 4-9 that may be dust-obscured AGN with M_BH ~ 10^6-10^8 M_sun.
- **Public:** Yes
- **Machine-readable:** Review paper with compiled data from multiple surveys.
- **License:** Journal copyright.
- **Recommended role:** Context and additional high-z AGN candidates for Track A.
- **Quality notes:** The nature of little red dots is actively debated. Some may be compact star-forming galaxies rather than AGN. Use with appropriate caveats.

### A7. Inayoshi, Visbal & Haiman 2020 — Seed Formation Review

- **Source:** Inayoshi, Visbal, Haiman 2020
- **arXiv:** 1911.05791
- **What it measures:** Comprehensive review of SMBH seed formation channels with model comparison tables.
- **Public:** Yes (ARA&A review)
- **Machine-readable:** Tables with model parameters and predictions.
- **License:** Journal copyright.
- **Recommended role:** Primary reference for seed formation model parameters in Track A. Their Table 1 is the standard comparison of light/medium/heavy seed channels.
- **Quality notes:** Pre-JWST review. Seed mass requirements should be updated with JWST discoveries.

### Note on JWST Data Availability

Most JWST high-z AGN data consists of individual objects reported in discovery papers, not machine-readable catalogs. For Track A, the approach is:

1. Compile a table of individual (M_BH, z, source, method) entries from the papers above
2. Save as `data/high_z_smbh.csv` with provenance for each entry
3. Update as new JWST discoveries are published

This is standard practice for this field — there is no single authoritative machine-readable catalog.

---

## B. PBH Constraints

### B1. PBHbounds (bradkav/PBHbounds)

- **Source:** Bradley Kavanagh, PBHbounds repository
- **URL:** https://github.com/bradkav/PBHbounds
- **arXiv:** (associated with multiple papers; see repo README)
- **What it measures:** Compiled upper limits on f_PBH(M) from ~30 independent observational channels (microlensing, GW, CMB, evaporation, dynamical).
- **Public:** Yes
- **Machine-readable:** Yes — .dat and .csv files with (M, f_PBH_max) pairs for each constraint
- **License:** MIT
- **Recommended role:** PRIMARY constraint source for Track B. This is the gold standard for PBH constraint compilation.
- **Quality notes:** Actively maintained. Constraints are compiled from published papers with citations provided. Some constraints may be updated or superseded — check repo for latest versions. Use the `bounds/` directory data files directly.

### B2. Carr et al. 2021 — Comprehensive PBH Review

- **Source:** Carr, Kohri, Sendouda, Yokoyama 2021
- **arXiv:** 2002.12778
- **What it measures:** Comprehensive review of PBH constraints across the full mass range, with discussion of caveats and uncertainties.
- **Public:** Yes
- **Machine-readable:** Constraint figures in paper, but numerical data is better sourced from PBHbounds (B1).
- **License:** Journal copyright.
- **Recommended role:** Reference for constraint methodology and caveats. Use PBHbounds for actual data.
- **Quality notes:** Some constraints have been updated since this review. Cross-check with PBHbounds for latest values.

### B3. Green & Kavanagh 2021 — Updated Constraints Review

- **Source:** Green, Kavanagh 2021
- **arXiv:** 2007.10722
- **What it measures:** Updated PBH constraints with emphasis on extended mass functions (non-monochromatic).
- **Public:** Yes
- **Machine-readable:** Via PBHbounds
- **License:** Journal copyright.
- **Recommended role:** Reference for extended mass function methodology. Important for the log-normal mass function used in Track B.
- **Quality notes:** Includes discussion of how constraints weaken for extended mass functions — relevant for realistic PBH scenarios.

---

## C. CMB Spectral Distortion Constraints

### C1. FIRAS (COBE)

- **Source:** Fixsen et al. 1996
- **arXiv:** (pre-arXiv; ApJ 473, 576)
- **What it measures:** CMB spectral distortions — deviations from a perfect blackbody.
- **Constraint:** $|\mu| < 9 \times 10^{-5}$ (95% CL)
- **P(k) constraint range:** $1 \lesssim k \lesssim 10^4\,\mathrm{Mpc}^{-1}$
- **Public:** Yes
- **Machine-readable:** Single upper limit (not a curve).
- **License:** Public domain (NASA data).
- **Recommended role:** Upper limit on P(k) enhancement in the mu-distortion window. Cross-check for Track B — if the P(k) bump extends to $k < 10^4\,\mathrm{Mpc}^{-1}$, it is constrained by FIRAS.
- **Quality notes:** 30-year-old measurement. Still the best constraint on mu-distortions. The SMBH-seed-relevant scales ($k \sim 10^5\text{--}10^6\,\mathrm{Mpc}^{-1}$) are ABOVE the FIRAS window, so this constraint may not directly apply unless the P(k) bump is very broad.

### C2. PIXIE / PRISTINE Projections

- **Source:** Kogut et al. 2011 (PIXIE); various forecast papers
- **arXiv:** 1105.2044 (PIXIE concept)
- **What it measures:** Projected sensitivity to mu-distortions: $\sigma_\mu \sim 10^{-8}$
- **Public:** Projected sensitivity only (mission not yet flown)
- **Machine-readable:** Forecast sensitivity curves in papers.
- **License:** N/A (projections)
- **Recommended role:** Future constraint projection line on joint constraint figure. Shows how future missions would tighten the P(k) constraints.
- **Quality notes:** PIXIE has not been selected for flight. Use as a projection/motivation only.

---

## D. Halo Mass Function Data

### D1. Press-Schechter / Sheth-Tormen / Tinker Mass Functions

- **Source:** Press & Schechter 1974; Sheth & Tormen 1999; Tinker et al. 2008
- **What it measures:** Analytic and calibrated predictions for the halo mass function $dn/dM$ as a function of $\sigma(M)$ and redshift.
- **Public:** Yes (analytic formulae)
- **Machine-readable:** Analytic — implemented in code (no external data files needed)
- **License:** N/A (published formulae)
- **Recommended role:** Core calculation for Track A halo abundance. Use Sheth-Tormen as default (better fit than Press-Schechter at high masses); Tinker for cross-validation.
- **Quality notes:** Calibrated on N-body simulations at $z < 10$. Extrapolation to $z > 15$ introduces systematic uncertainty of $\mathcal{O}(1)$ at the high-mass tail. This uncertainty should be flagged.

### D2. Planck 2018 Cosmological Parameters

- **Source:** Planck Collaboration 2018
- **arXiv:** 1807.06209
- **What it measures:** Standard cosmological parameters ($H_0$, $\Omega_m$, $\Omega_b$, $\sigma_8$, $n_s$, $A_s$) needed for computing $\sigma(M)$, $D(z)$, $t(z)$.
- **Public:** Yes
- **Machine-readable:** Parameter values in paper; also available via astropy.cosmology
- **License:** Public
- **Recommended role:** Baseline cosmology for all calculations across all tracks.
- **Quality notes:** Use the TT,TE,EE+lowE+lensing best-fit values (Table 2 of Planck 2018 VI).

---

## Summary Table

| Track | Datasets needed | Critical path? | Data quality |
|-------|----------------|----------------|--------------|
| A | Fan+23, Bogdan+24, Maiolino+24, Inayoshi+20, Planck 2018 | Fan+23 for sample; Planck for cosmology | Good but individual-object extraction required |
| B | PBHbounds, Carr+21, FIRAS | PBHbounds is critical (MIT, machine-readable) | Excellent — gold standard |
| C (joint) | All of the above | Both Track A and B outputs | Depends on input track quality |

## Data Acquisition Checklist

- [ ] Clone PBHbounds repository: `git clone https://github.com/bradkav/PBHbounds.git`
- [ ] Compile high_z_smbh.csv from papers A1-A7 (manual extraction)
- [ ] Verify Planck 2018 parameters in astropy match Table 2 values
- [ ] Check PBHbounds for updates since last download
- [ ] Verify FIRAS mu-distortion limit and applicable k range
