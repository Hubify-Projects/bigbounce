# Master Extension Dataset Audit

**Project:** BigBounce Spin-Torsion Cosmology — Phenomenology Extensions
**Date:** 2026-03-12
**Auditor:** Automated (Claude Code)
**Scope:** Three extension tracks — Early SMBH Seeds (A), PBH-like Relics (B), CMB Birefringence (C)

---

## Executive Summary

This audit identifies all public, machine-readable datasets relevant to three phenomenology extension tracks. The key finding is that **Track C (Birefringence) has the strongest data availability**, with multiple independent Gaussian constraints already compiled in the existing `p6_cmb_eb_pipeline` registry. **Track A (SMBH Seeds) relies almost entirely on literature-extracted values** from individual JWST discovery papers, with no unified public catalog of high-z SMBH masses. **Track B (PBH Constraints) benefits from well-known constraint compilations**, but the most useful machine-readable version is a community-maintained GitHub repository rather than a formal data release.

---

## TRACK A: Early SMBH Seed Abundance

### A.1 Overview

The goal is to compare the spin-torsion bounce model's predictions for early massive seed formation against observed high-z SMBH masses and number densities. The key question is whether the bounce cosmology provides a natural mechanism for producing heavy seeds (10^4 - 10^5 M_sun) that explain the "too massive too early" problem highlighted by JWST observations.

### A.2 Dataset Inventory

#### A.2.1 UHZ-1 X-ray AGN (Bogdan et al. 2024)

- **Source:** Bogdan et al. (2024), Nature Astronomy 8, 126
- **arXiv:** 2305.15458
- **What it measures:** X-ray detection of an AGN at z ~ 10.1 behind galaxy cluster Abell 2744, with inferred BH mass ~ 4 x 10^7 M_sun (from X-ray luminosity scaling)
- **Format:** Single object; mass estimate reported in paper text and Table 1
- **Public:** Yes (published paper)
- **Machine-readable:** No downloadable catalog. This is a single-object detection with mass estimated from X-ray luminosity. The constraint is: M_BH ~ (1-4) x 10^7 M_sun at z ~ 10.1.
- **License:** Journal publication (Nature Astronomy)
- **Appropriate for paper:** Yes, as a literature-extracted data point. It is the highest-redshift X-ray AGN detection and directly tests seed formation models.
- **Quality:** Vetted (peer-reviewed, Nature Astronomy). Mass estimate depends on X-ray luminosity scaling relations and has systematic uncertainty of ~0.5 dex.
- **Usage mode:** Literature-extracted single constraint.

#### A.2.2 GN-z11 AGN (Maiolino et al. 2024)

- **Source:** Maiolino et al. (2024), Nature 627, 59
- **arXiv:** 2305.12492
- **What it measures:** JWST NIRSpec detection of broad H-alpha and other AGN indicators in GN-z11 at z = 10.6, with inferred M_BH ~ 1.6 x 10^6 M_sun from virial estimator
- **Format:** Single object; mass and accretion properties in paper text
- **Public:** Yes (published)
- **Machine-readable:** No catalog. Single object with M_BH = 1.6 (+0.8/-0.5) x 10^6 M_sun.
- **License:** Journal (Nature)
- **Appropriate for paper:** Yes, as literature-extracted constraint
- **Quality:** Vetted. Virial mass estimator has ~0.3-0.5 dex systematic uncertainty.

#### A.2.3 JWST High-z AGN Candidates (Larson et al. 2023)

- **Source:** Larson et al. (2023), ApJ 953, L29
- **arXiv:** 2303.08918
- **What it measures:** CEERS survey photometric identification of AGN candidates at z > 8, including spectroscopic confirmation of some
- **Format:** Candidate list in paper tables
- **Public:** Yes (published). CEERS data products are public via MAST (doi:10.17909/z7p0-8481).
- **Machine-readable:** CEERS photometric catalogs are downloadable from MAST. However, the AGN identification and mass estimates require reading the paper tables directly.
- **License:** Public (NASA MAST)
- **Appropriate for paper:** Partially. The photometric catalogs are available, but mass estimates for individual AGN are literature-extracted.
- **Quality:** Vetted (ApJ), but photometric AGN identification at z > 8 has known contamination issues.

#### A.2.4 Greene et al. (2024) Review — High-z SMBH Census

- **Source:** Greene, Labbe, Goulding et al. (2024), ApJ 964, 39
- **arXiv:** 2309.05714
- **What it measures:** Review and compilation of JWST-discovered AGN at z > 4, including "Little Red Dots" (LRDs). Contains a compilation table of BH mass estimates.
- **Format:** Summary tables in paper (Table 1 typically lists objects, redshifts, mass estimates)
- **Public:** Yes (published)
- **Machine-readable:** Not as a downloadable catalog. Must be extracted from paper tables. This is the closest thing to a "compiled catalog" of high-z SMBH masses from JWST, but it is a review paper, not a data release.
- **License:** AAS journals (open access)
- **Appropriate for paper:** Yes. This is the best single source for a compiled list of high-z SMBH detections. Should be the primary reference for Track A.
- **Quality:** Vetted (ApJ review). Individual mass estimates inherit uncertainties from original papers.

#### A.2.5 Natarajan et al. (2024) — Heavy Seed Models

- **Source:** Natarajan, Pacucci, et al. (2024), ApJL 960, L1
- **arXiv:** 2302.04888
- **What it measures:** Theoretical framework for distinguishing light seeds (~100 M_sun, Pop III remnants) vs heavy seeds (~10^4-10^5 M_sun, direct collapse) using JWST observations. Includes model predictions for BH mass function at z > 5.
- **Format:** Model predictions in paper figures; no downloadable data files
- **Public:** Yes (published)
- **Machine-readable:** No. Model curves must be digitized from figures.
- **License:** AAS journals
- **Appropriate for paper:** Yes, as the theoretical comparison framework. The paper provides the light-vs-heavy seed mass function predictions that spin-torsion bounce seeds would be compared against.
- **Quality:** Vetted. Widely cited theoretical framework.

#### A.2.6 SDSS/BOSS High-z Quasar Catalogs (z > 5)

- **Source:** Various SDSS quasar catalogs, e.g., Wu & Shen (2022), ApJS 263, 42; Yang et al. (2023)
- **What it measures:** Spectroscopically confirmed quasars at z > 5 with virial BH mass estimates from MgII line widths
- **Format:** FITS/CSV catalogs downloadable from SDSS
- **Public:** Yes
- **Machine-readable:** Yes — this is the most machine-readable high-z SMBH dataset
- **URL:** https://www.sdss.org/dr18/
- **License:** Public
- **Appropriate for paper:** Yes, but these are z ~ 5-7 quasars, not z > 8. They constrain the high-mass end of the SMBH mass function at somewhat lower redshift than the JWST frontier.
- **Quality:** Vetted. SDSS quasar catalogs are among the most thoroughly validated in astronomy.

#### A.2.7 Inayoshi, Visbal & Haiman (2020) Review — SMBH Formation Models

- **Source:** Inayoshi, Visbal & Haiman (2020), ARAA 58, 27
- **arXiv:** 1911.05791
- **What it measures:** Comprehensive review of SMBH seed formation channels with predicted mass functions
- **Format:** Review paper, model comparisons in figures
- **Public:** Yes
- **Machine-readable:** No (figures only)
- **Appropriate for paper:** Yes, as theoretical framework reference
- **Quality:** Vetted (ARAA)

### A.3 Track A Assessment

**Overall data availability: POOR for machine-readable catalogs, ADEQUATE for literature-extracted constraints.**

The fundamental problem is that there is no single, unified, machine-readable catalog of high-z (z > 8) SMBH masses from JWST. Each object is reported individually in discovery papers. The Greene et al. (2024) review provides the closest thing to a compiled list but requires manual table extraction.

**Recommended approach:**
1. Manually compile a table of ~10-20 high-z SMBH detections from JWST papers (M_BH, z, method, uncertainty)
2. Use SDSS quasar catalogs for z ~ 5-7 constraints (machine-readable)
3. Compare against Natarajan et al. (2024) seed model predictions (digitized from figures)
4. All constraints should be labeled as "literature-extracted" with appropriate caveats

**Key gap:** No public, community-maintained database of high-z SMBH masses exists. This is an active area where such a compilation would be valuable but does not yet exist as of March 2026.

---

## TRACK B: PBH-like Relic / Compact Seeds

### B.1 Overview

The spin-torsion bounce can potentially produce compact over-dense regions that mimic primordial black holes (PBHs). This track requires comparison against existing PBH abundance constraints across a wide mass range.

### B.2 Dataset Inventory

#### B.2.1 PBH Constraint Compilation — Green & Kavanagh (2021)

- **Source:** Green & Kavanagh (2021), J. Phys. G 48, 043001
- **arXiv:** 2007.10722
- **What it measures:** Comprehensive compilation of observational upper limits on the PBH abundance f_PBH = Omega_PBH / Omega_DM as a function of PBH mass, from ~10^15 g to ~10^10 M_sun
- **Format:** The paper itself contains summary plots. Crucially, an associated **machine-readable dataset is maintained on GitHub**: https://github.com/bradkav/PBHbounds
- **Public:** Yes
- **Machine-readable:** **Yes** — the `PBHbounds` GitHub repository contains digitized constraint curves as plain-text data files (mass, f_PBH columns). This is the gold-standard machine-readable PBH constraint compilation.
- **License:** MIT license on the GitHub repository
- **Appropriate for paper:** Yes. This is the standard reference for PBH constraints and is directly usable.
- **Quality:** Vetted. Widely cited (>500 citations). Regularly updated by the community.
- **URL:** https://github.com/bradkav/PBHbounds

#### B.2.2 Carr, Kohri, Sendouda & Yokoyama (2021)

- **Source:** Carr et al. (2021), Rep. Prog. Phys. 84, 116902
- **arXiv:** 2002.12778
- **What it measures:** Comprehensive review of PBH constraints and formation mechanisms. Includes extensive constraint summary figures.
- **Format:** Review paper with constraint summary plots
- **Public:** Yes
- **Machine-readable:** No standalone data release. The constraint curves in figures must be digitized. However, many of the same constraints are available in machine-readable form via PBHbounds (B.2.1).
- **License:** Journal (IoP)
- **Appropriate for paper:** Yes, as review reference. For actual constraint data, use PBHbounds.
- **Quality:** Vetted (RPP review, >1000 citations)

#### B.2.3 Microlensing Constraints — EROS-2

- **Source:** EROS-2 Collaboration, Tisserand et al. (2007), A&A 469, 387
- **arXiv:** astro-ph/0607207
- **What it measures:** Upper limits on compact halo object abundance from microlensing of LMC/SMC stars. Constrains f_PBH for M ~ 10^-7 to 10 M_sun.
- **Format:** Constraint curves in paper; digitized versions available in PBHbounds
- **Public:** Yes
- **Machine-readable:** Via PBHbounds (digitized)
- **Appropriate for paper:** Yes
- **Quality:** Vetted. Foundational microlensing constraint.

#### B.2.4 Microlensing Constraints — OGLE

- **Source:** Mroz et al. (2024), ApJS 273, 4; Niikura et al. (2019), Nature Astronomy 3, 524
- **arXiv:** 2403.02398 (Mroz), 1701.02151 (Niikura)
- **What it measures:** Microlensing constraints on compact objects. Niikura et al. (2019) used Subaru/HSC to probe ultra-short timescale events, constraining PBHs in the 10^-11 to 10^-6 M_sun range (the "asteroid mass" window).
- **Format:** Constraint curves in papers; digitized in PBHbounds
- **Public:** Yes
- **Machine-readable:** Via PBHbounds
- **Appropriate for paper:** Yes
- **Quality:** Vetted

#### B.2.5 CMB Accretion Constraints — Planck

- **Source:** Serpico et al. (2020), based on Planck CMB anisotropy data
- **arXiv:** Various; compiled in Carr et al. (2021)
- **What it measures:** PBH accretion onto CMB photons modifies the CMB spectrum and anisotropies, constraining f_PBH for M > ~1 M_sun
- **Format:** Constraint curves; available in PBHbounds
- **Public:** Yes (Planck data public; derived constraints in literature)
- **Machine-readable:** Via PBHbounds
- **Appropriate for paper:** Yes
- **Quality:** Vetted. Depends on accretion model assumptions (spherical vs disk).

#### B.2.6 Gravitational Wave Constraints — LIGO/Virgo/KAGRA

- **Source:** LIGO-Virgo-KAGRA Collaboration, various; Abbott et al. (2023) GWTC-3
- **arXiv:** 2111.03606 (GWTC-3)
- **What it measures:** Binary black hole merger rates constrain PBH abundance in the ~1-100 M_sun range. The merger rate and mass distribution can be compared to PBH formation models.
- **Format:** GWTC-3 catalog is publicly available via GWOSC (https://gwosc.org/)
- **Public:** Yes — GWOSC provides full posterior samples for all detected events
- **Machine-readable:** Yes — HDF5 and JSON formats
- **License:** CC-BY-4.0
- **Appropriate for paper:** Partially. The raw GW catalog is available, but deriving PBH constraints from merger rates requires population synthesis modeling. The derived PBH constraints are available via PBHbounds.
- **Quality:** Vetted (LVK official data release)

#### B.2.7 Evaporation Constraints — Voyager / INTEGRAL / Fermi

- **Source:** Various; Boudaud & Cirelli (2019), Laha (2019), DeRocco & Graham (2019)
- **arXiv:** 1807.03075, 1906.09994, 1906.07740
- **What it measures:** Hawking evaporation of low-mass PBHs produces gamma rays, positrons, and other particles detectable by Voyager, INTEGRAL, and Fermi. Constrains f_PBH for M < ~10^17 g.
- **Format:** Constraint curves in papers; digitized in PBHbounds
- **Public:** Yes
- **Machine-readable:** Via PBHbounds
- **Appropriate for paper:** Yes, for the low-mass end
- **Quality:** Vetted. Evaporation constraints depend on Hawking radiation assumptions (standard physics).

#### B.2.8 Femtolensing and Millilensing Constraints

- **Source:** Barnacka, Glicenstein & Moderski (2012) — femtolensing of GRBs; Wilkinson et al. (2001) — millilensing of compact radio sources
- **What it measures:** Gravitational lensing at very small (femto) and intermediate (milli) angular scales
- **Format:** Constraint curves; some available in PBHbounds
- **Public:** Yes
- **Machine-readable:** Partially via PBHbounds
- **Appropriate for paper:** Yes
- **Quality:** Vetted, but femtolensing constraints have been questioned by more recent analyses (Katz et al. 2018, arXiv:1807.11495 showed that finite-source effects weaken femtolensing bounds). Flag this caveat.

### B.3 Track B Assessment

**Overall data availability: GOOD, thanks to PBHbounds.**

The `PBHbounds` GitHub repository (https://github.com/bradkav/PBHbounds) is the single most valuable resource for this track. It provides machine-readable constraint curves from dozens of independent observational channels, all in a consistent format (mass vs f_PBH). This repository is MIT-licensed, actively maintained, and widely used in the PBH literature.

**Recommended approach:**
1. Use PBHbounds as the primary data source for all constraint curves
2. Cite original papers for each constraint channel, but use PBHbounds for the actual data
3. Overlay spin-torsion bounce relic predictions on the PBHbounds exclusion plot
4. Note that femtolensing constraints are contested (cite Katz et al. 2018)

**Key strength:** This is the most data-rich track. Machine-readable constraints exist across 30+ orders of magnitude in mass.

---

## TRACK C: Parity / CMB Birefringence

### C.1 Overview

The spin-torsion coupling in the bounce model introduces a parity-violating term that produces cosmic birefringence --- a uniform rotation of CMB polarization by an angle beta. This track compares model predictions against measured beta values.

### C.2 Dataset Inventory

**Note:** This track has already been partially audited in the existing `p6_cmb_eb_pipeline/dataset_registry.csv`. This audit expands and validates that registry.

#### C.2.1 Minami & Komatsu (2020) — First >2-sigma Detection

- **Source:** Minami & Komatsu (2020), PRL 125, 221301
- **arXiv:** 2011.11254
- **What it measures:** Isotropic cosmic birefringence angle beta = 0.35 +/- 0.14 deg (68% CL) from Planck 2018 HFI EB cross-correlations, using the self-calibration method to break the degeneracy with instrument miscalibration angles
- **Format:** Single Gaussian constraint (beta, sigma_beta) reported in paper text
- **Public:** Yes
- **Machine-readable:** Literature-extracted Gaussian constraint. No downloadable likelihood or data file.
- **License:** APS (PRL)
- **Appropriate for paper:** Yes. Foundational measurement. Usable as N(0.35, 0.14^2) Gaussian constraint.
- **Quality:** Vetted. 2.4-sigma significance. Self-calibration method is now standard.
- **Caveat:** Uses Planck 2018 (PR3) data, which has known systematics in polarization that are improved in PR4.

#### C.2.2 Eskilt & Komatsu (2022) — PR3 Frequency Analysis

- **Source:** Eskilt & Komatsu (2022), PRD 106, 063503
- **arXiv:** 2203.04830
- **What it measures:** Frequency-dependent analysis of birefringence from Planck PR3. Confirms beta is frequency-independent (as expected for a cosmological signal, not Galactic dust).
- **Format:** beta per frequency pair reported in paper tables
- **Public:** Yes
- **Machine-readable:** Literature-extracted. No public likelihood code.
- **Appropriate for paper:** Yes, as supporting evidence for frequency-independence
- **Quality:** Vetted (PRD)

#### C.2.3 Eskilt (2022) — PR4 Combined

- **Source:** Eskilt (2022), A&A 662, A10
- **arXiv:** 2205.13962
- **What it measures:** beta = 0.30 +/- 0.11 deg (68% CL) from Planck PR4 (NPIPE) data, frequency-combined analysis
- **Format:** Single Gaussian constraint
- **Public:** Yes
- **Machine-readable:** Literature-extracted Gaussian constraint. N(0.30, 0.11^2).
- **License:** A&A (open access)
- **Appropriate for paper:** Yes. Tightest Planck-only constraint. Directly usable.
- **Quality:** Vetted (A&A). Uses improved PR4/NPIPE maps.

#### C.2.4 Diego-Palazuelos & Komatsu (2025) — ACT DR6

- **Source:** Diego-Palazuelos & Komatsu (2025)
- **arXiv:** 2509.13654
- **What it measures:** beta = 0.215 +/- 0.074 deg (2.9-sigma) from ACT DR6 data, independent of Planck systematics
- **Format:** Single Gaussian constraint
- **Public:** Yes
- **Machine-readable:** Literature-extracted Gaussian. Additionally, there is a **GitHub repository** (pdp79/act_dr6_analysis) that may contain analysis code.
- **License:** Preprint / AAS
- **Appropriate for paper:** Yes. Critical independent confirmation from non-Planck experiment.
- **Quality:** Vetted. ACT is an independent ground-based experiment with different systematics than Planck.

#### C.2.5 Zagatti et al. (2025) — PR4 Map-Space

- **Source:** Zagatti, Trombetti & Natoli (2025)
- **arXiv:** 2502.07654
- **What it measures:** beta = 0.46 +/- 0.04 (stat) +/- 0.28 (syst) deg from Planck PR4 using a map-space estimator (independent cross-check of spectrum-level analyses)
- **Format:** Gaussian constraint with separate stat and syst errors
- **Public:** Yes
- **Machine-readable:** Literature-extracted. When using as constraint, must combine stat + syst in quadrature: sigma_total ~ 0.28 deg.
- **Appropriate for paper:** Yes, but with caveats about the large systematic error
- **Quality:** Vetted. Large systematic uncertainty makes it less constraining than Eskilt (2022).

#### C.2.6 SPIDER Collaboration (2025) — Combined 7-sigma

- **Source:** SPIDER Collaboration (2025)
- **arXiv:** 2510.25489
- **What it measures:** Joint SPIDER + Planck + ACT constraint on cosmic birefringence reaching 7-sigma significance
- **Format:** Combined constraint reported in paper. SPIDER provides independent low-frequency (95/150 GHz) balloon data.
- **Public:** Yes (published)
- **Machine-readable:** Literature-extracted Gaussian constraint
- **License:** Preprint
- **Appropriate for paper:** Yes. The strongest combined significance to date.
- **Quality:** Vetted. SPIDER is a balloon experiment with very different systematics from both Planck and ACT.
- **Note:** The combined beta value and uncertainty from the paper should be used carefully; the 7-sigma comes from the combination, not from SPIDER alone.

#### C.2.7 Planck PR4 (NPIPE) Maps — Raw Data

- **Source:** Planck Legacy Archive (PLA)
- **URL:** https://pla.esac.esa.int/#maps
- **What it measures:** Full-sky CMB polarization maps (Q, U Stokes parameters) at 70-353 GHz
- **Format:** HEALPix FITS files, Nside=2048 (HFI), Nside=1024 (LFI)
- **Public:** Yes
- **Machine-readable:** Yes (FITS format, readable with healpy)
- **Size:** ~12 GB for frequency maps + ~1 GB for masks
- **License:** ESA Planck Science Legacy (free for scientific use)
- **Appropriate for paper:** Only if conducting an independent EB analysis (Tier 2 pipeline). Not needed for literature-level constraints.
- **Quality:** Vetted. Official ESA data release.

#### C.2.8 ACT DR6 Public Data

- **Source:** ACT Collaboration
- **URL:** https://lambda.gsfc.nasa.gov/product/act/actpol_prod_table.html
- **What it measures:** CMB temperature and polarization maps and power spectra from ACT
- **Format:** FITS files
- **Public:** Yes (via LAMBDA)
- **Machine-readable:** Yes
- **Appropriate for paper:** Only for independent re-analysis. For birefringence, the published constraint from Diego-Palazuelos & Komatsu (2025) is sufficient.
- **Quality:** Vetted (official ACT data release)

#### C.2.9 Birefringence Likelihood Code

- **Source:** No single public likelihood code exists for cosmic birefringence that is universally used
- **Partial options:**
  - Diego-Palazuelos GitHub (pdp79/act_dr6_analysis) — may contain ACT analysis code
  - Minami & Komatsu method is well-documented but not released as a standalone public code
  - The self-calibration framework is described in sufficient detail in Minami & Komatsu (2020) and Eskilt (2022) for reimplementation
- **Assessment:** For this paper's purposes, the published Gaussian constraints are sufficient. A full likelihood re-analysis is not needed unless challenging the published values.

### C.3 Track C Assessment

**Overall data availability: GOOD for literature constraints, EXCELLENT for raw data.**

This is the best-served track. Five independent or semi-independent measurements of beta are available as simple Gaussian constraints, directly usable without any data processing:

| Measurement | beta (deg) | sigma (deg) | Significance |
|---|---|---|---|
| Minami & Komatsu (2020) | 0.35 | 0.14 | 2.4-sigma |
| Eskilt (2022, PR4) | 0.30 | 0.11 | 2.7-sigma |
| Diego-Palazuelos & Komatsu (2025, ACT) | 0.215 | 0.074 | 2.9-sigma |
| Zagatti et al. (2025, map-space) | 0.46 | 0.28 | 1.6-sigma |
| SPIDER (2025, combined) | TBD | TBD | 7-sigma |

**Recommended approach:**
1. Use the published Gaussian constraints directly for an inverse-variance weighted average
2. The existing `p6_cmb_eb_pipeline` already implements this approach (Tier 1)
3. Raw Planck/ACT maps are available for independent verification but not required for the paper
4. Note that Minami & Komatsu (2020) and Eskilt (2022) use overlapping Planck data --- they are not fully independent. In a meta-analysis, use Eskilt (2022) as the superseding Planck constraint.

**Important caveat:** The Minami-Komatsu and Eskilt measurements both use Planck data and are not independent. A careful meta-analysis should either use only the most constraining Planck measurement (Eskilt 2022) or properly account for correlations. The ACT and SPIDER measurements are genuinely independent.

---

## Cross-Track Summary

| Track | Machine-readable datasets | Literature-extracted constraints | Overall readiness |
|---|---|---|---|
| A (SMBH Seeds) | 1 (SDSS quasar catalogs) | ~10-20 individual JWST objects | LOW — requires manual compilation |
| B (PBH Relics) | 1 major (PBHbounds, ~30 channels) + GWOSC | Carr et al. (2021) review | HIGH — PBHbounds is ready to use |
| C (Birefringence) | 2 (Planck PR4 maps, ACT DR6 maps) | 5 Gaussian constraints | HIGH — literature constraints directly usable |

### Datasets NOT Found / Flagged

1. **No unified high-z SMBH mass catalog exists** (Track A). This is a known gap in the field. Several groups are working on compilations but nothing public and machine-readable as of March 2026.

2. **No public birefringence likelihood code** (Track C). The self-calibration method is documented well enough for reimplementation, but no plug-and-play likelihood package exists.

3. **SPIDER combined beta value** (Track C) needs verification — the 7-sigma significance is for the combined SPIDER+Planck+ACT analysis; the SPIDER-only constraint is weaker. The exact combined beta and uncertainty should be extracted carefully from the paper.

4. **Femtolensing PBH constraints are contested** (Track B). Katz et al. (2018, arXiv:1807.11495) showed finite-source effects weaken these bounds. PBHbounds includes updated versions but this should be flagged.

5. **PBH constraints from NANOGrav / PTAs** (Track B). Recent pulsar timing array results (NANOGrav 15yr, EPTA, PPTA) have been interpreted as possible PBH signals. These are speculative and should not be used as constraints without careful caveats.
