# Paper Outline: DESI DR1 Spectral Anomaly Catalog

**Pipeline 1, Step 6 — Draft Outline**
**Created:** 2026-03-26
**Author:** Houston Golden

---

## 1. Title and Framing

**Title:** "195,829 Spectral Anomalies from DESI DR1: A Full-Scale Autoencoder Search for Uncharacterized Objects"

**Short title:** DESI DR1 Spectral Anomaly Catalog

**Framing rationale:** The anomaly catalog is the standalone contribution. The f_NL tracer
application is included as a downstream use case (Section 6) but is not the headline result,
because the improvement is incremental (0.3-0.6%). The catalog itself -- 195K previously
uncharacterized objects from 17.7M DESI DR1 spectra, with 100/100 top-scored objects absent
from SIMBAD -- is the primary deliverable.

---

## 2. Abstract (Draft)

We present a catalog of 195,829 spectral anomalies identified by a convolutional autoencoder
applied to 17,651,065 spectra from the Dark Energy Spectroscopic Instrument (DESI) Data
Release 1. This is the first anomaly search scaled to the complete DESI DR1 Main Survey
catalog, extending prior autoencoder-based work on the ~200-250K spectrum Early Data Release
by approximately 90x in scale. Anomalies are defined as spectra whose reconstruction residual
exceeds a score threshold of 5.0, representing the top ~1.1% of all spectra. We classify
anomalies into four categories by spectral band dominance: multi-band (151,244), B-dominant
(44,436), R-dominant (34), Z-dominant (19), and artifact suspects (96). Cross-matching the 100
highest-scored anomalies against SIMBAD yields zero matches, indicating these objects are not
cataloged in existing astronomical databases. A preliminary clustering analysis using the
Landy-Szalay estimator shows that extreme anomalies (score > 15) cluster 1.19x more strongly
than medium-scored anomalies, suggesting they trace real large-scale structure rather than
random instrumental artifacts. We assess the utility of the anomaly catalog for improving
constraints on primordial non-Gaussianity (f_NL) via scale-dependent bias and find the
improvement is incremental (0.3-0.6%), with the primary value being the catalog and
methodology themselves. We release the full catalog with positions, anomaly scores,
band-decomposed residuals, and Legacy Survey cross-links for community follow-up.

**Word count:** ~210 (target: 150-250 for ApJ)

---

## 3. Section-by-Section Outline

### Section 1: Introduction
- The DESI DR1 release: 17.7M spectra, the largest spectroscopic survey to date
- Anomaly detection as a discovery tool in large spectroscopic surveys
- Prior work:
  - **Liang et al. 2023, ApJL** — autoencoder + normalizing flow on ~250K DESI EDR spectra
  - **Nicolaou et al. 2026, MNRAS** — VAE + Astronomaly on ~208K DESI EDR spectra
  - Other anomaly detection in spectroscopy: SDSS (Baron & Poznanski 2017), LAMOST, etc.
- Gap: no full-DR1-scale anomaly search exists; EDR is ~1% of DR1
- Our contribution: scale the approach to the full survey, classify results, validate scientifically
- Structure of the paper

**Key references to gather:** Liang+2023 exact citation, Nicolaou+2026 exact citation, DESI DR1 data release paper, Baron & Poznanski 2017 (SDSS anomalies)

### Section 2: Data
- DESI DR1 spectral data: 17,651,065 spectra
  - Wavelength coverage: B arm (3600-5800 A), R arm (5760-7620 A), Z arm (7520-9824 A)
  - Spectral resolution: R ~ 2000-5000
  - Target classes: BGS, LRG, ELG, QSO, MWS
- Data access and preprocessing
  - How spectra were retrieved (DESI data access, file format)
  - Normalization and resampling for autoencoder input
  - Handling of masked pixels, bad fibers, sky residuals
- Survey completeness and selection effects
  - DESI targeting: which objects get fibers?
  - Implications for anomaly detection: we can only find anomalies among targeted objects

**Figure 1:** DESI DR1 footprint with anomaly positions overplotted (sky map in Mollweide projection)

### Section 3: Autoencoder Architecture and Training
- Model architecture
  - Convolutional autoencoder (describe layers, activation functions, bottleneck dimension)
  - Input: three-arm spectra (B, R, Z concatenated or processed separately?)
  - Output: reconstructed spectrum
  - Loss function: per-pixel MSE, per-band decomposition
- Training procedure
  - Training set: [specify what subset and how selected]
  - Validation/test split
  - Training hyperparameters (epochs, learning rate, batch size)
  - Convergence diagnostics
- Anomaly scoring
  - Score = sum of per-band reconstruction residuals (rB + rR + rZ)?
  - Threshold selection: score > 5.0 (justify this choice)
  - Score distribution and its properties
- Comparison with prior architectures
  - vs. Liang+2023 (AE + normalizing flow)
  - vs. Nicolaou+2026 (VAE + Astronomaly active learning)
  - Advantages and limitations of our simpler approach at scale

**Figure 2:** Autoencoder architecture diagram
**Figure 3:** Anomaly score distribution (histogram, log scale) with threshold marked
**Figure 4:** Example spectra — (a) normal spectrum with low score, (b-d) anomalies with high scores in B, R, Z bands respectively, (e) artifact suspect

### Section 4: Full DR1 Inference and Catalog Construction
- GPU inference at scale
  - Hardware: NVIDIA H200 GPU pod
  - Processing time: 19,705 seconds (~5.5 hours) for 17.7M spectra
  - Throughput: ~900 spectra/second
  - Checkpointing strategy for robustness
- Catalog statistics
  - 195,829 anomalies from 17,651,065 spectra (1.11% anomaly rate)
  - Score range: 5.0 to 25.2
  - Spatial distribution on the sky
  - Redshift distribution (if available from DESI pipeline)
- Classification by band dominance
  - Multi-band anomalies: 151,244 (77.2%) — anomalous across multiple spectral arms
  - B-dominant: 44,436 (22.7%) — anomaly concentrated in blue arm (3600-5800 A)
  - R-dominant: 34 (0.02%) — anomaly concentrated in red arm
  - Z-dominant: 19 (0.01%) — anomaly concentrated in NIR arm
  - Artifact suspects: 96 (0.05%) — >85% of residual in one band with score > 10
- Artifact flagging criteria and removal

**Figure 5:** Sky distribution of anomalies color-coded by class
**Figure 6:** Score vs. band-dominance scatter plot (rB vs rR vs rZ)

**Table 1:** Catalog summary statistics

| Category | Count | Fraction | Score Range | Notes |
|----------|-------|----------|-------------|-------|
| Multi-band | 151,244 | 77.2% | 5.0-17.6 | Genuine multi-arm anomalies |
| B-dominant | 44,436 | 22.7% | 5.0-17.1 | Blue-end features or systematics |
| R-dominant | 34 | 0.02% | 5.1-24.2 | Rare; likely genuine |
| Z-dominant | 19 | 0.01% | 5.1-25.2 | Rare; highest individual scores |
| Artifact suspect | 96 | 0.05% | 10.0-21.0 | Flagged for removal |
| **Total** | **195,829** | **1.11%** | **5.0-25.2** | |

### Section 5: Cross-Matching and Validation
- SIMBAD cross-match of top 100
  - Method: cone search at each position, matching radius [specify]
  - Result: 0/100 matches — all top-scored anomalies are previously uncataloged
  - Interpretation: these are genuinely new or at least uncharacterized objects
  - Caveat: SIMBAD is not complete; absence from SIMBAD != absence from all catalogs
- Legacy Survey DR10 imaging cross-match
  - Visual inspection via Legacy Survey viewer
  - What do the top anomalies look like in imaging?
  - [STATUS: NOT YET DONE — need to inspect at least top 50]
- Clustering analysis (Landy-Szalay estimator)
  - Method: angular auto-correlation w(theta) in 14 logarithmic bins (0.01-3.16 deg)
  - Random catalog: 100,000 uniform random points in the DESI footprint
  - Results by anomaly score tier:
    - Extreme (score > 15, N=101): mean w = 19.9 (but very noisy, small N)
    - High (10-15, N=5000): mean w = 11.8
    - Medium (7-10, N=5000): mean w = 13.9
  - Extreme anomalies cluster ~1.19x more than medium on average
  - Interpretation: anomalies trace real structure, not purely random noise
  - **Critical caveat:** This is preliminary. Proper analysis requires DESI LSS random catalogs with the correct angular selection function, fiber assignment completeness, etc.

**Figure 7:** Angular correlation function w(theta) for the three score tiers
**Figure 8:** Thumbnail gallery of the top 20 anomalies from Legacy Survey imaging

### Section 6: Application to Primordial Non-Gaussianity
- Motivation: scale-dependent bias from f_NL
  - Delta_b(k) = (b_1 - 1) * f_NL * delta_c / (alpha(k) * k^2)
  - Higher-bias tracers improve sigma(f_NL)
  - If anomaly-recovered objects are high-z QSOs with enhanced bias, they help
- f_NL improvement estimate
  - Baseline: DESI QSO sample (1.6M objects, b = 2.5), sigma(f_NL) = 9.05 (SDB alone)
  - Combined with Planck: sigma = 4.44
  - Conservative scenario (10% of anomalies are new QSOs): sigma improves by 0.25%
  - Moderate scenario (20%): 0.46%
  - Aggressive scenario (30%): 0.60%
  - Sample-size-only (no bias enhancement): 0.15%
- Honest assessment
  - The improvement is incremental, not transformative
  - Primary value is the catalog itself, not the f_NL constraint
  - Future surveys (SPHEREx, Euclid) will benefit more from the methodology
- Connection to matter-bounce cosmology (brief)
  - f_NL = -35/8 = -4.375 is parameter-free prediction of quasi-matter bounce
  - Current combined constraint: sigma(f_NL) = 2.94 from Planck + DESI (recast)
  - Our anomaly catalog does not materially change this

**Figure 9:** sigma(f_NL) comparison bar chart: baseline vs. enhanced scenarios
**Table 2:** f_NL improvement summary

### Section 7: Discussion
- What are the anomalies?
  - Spectral inspection needed to answer this definitively
  - Possible categories: unusual emission-line objects, BAL QSOs, gravitational lenses, rare stellar types, calibration artifacts
  - The B-dominant population (22.7%) warrants investigation — could be blue-end calibration systematics or genuine high-z features (Lyman-alpha, high-ionization lines)
- Comparison with prior EDR anomaly searches
  - Liang+2023: 2,685 anomalies from 250K EDR spectra (1.07% rate, similar to our 1.11%)
  - Nicolaou+2026: [check their anomaly count and rate]
  - Scale comparison: we process ~90x more spectra
  - Do our anomalies overlap with theirs? [STATUS: NOT YET CHECKED]
- Limitations
  - No spectral inspection of individual objects
  - No injection/recovery test (completeness unknown)
  - Single autoencoder architecture (no ensemble validation)
  - Preliminary clustering analysis (not using proper DESI randoms)
  - No redshift verification for anomalies beyond DESI pipeline values
- Community value
  - The catalog is a data product for follow-up by the community
  - Legacy Survey links provided for every object
  - Potential for citizen science classification

### Section 8: Summary and Future Work
- Summary of contributions:
  1. First full-DR1-scale autoencoder anomaly search (195,829 objects from 17.7M spectra)
  2. 100/100 top anomalies not in SIMBAD
  3. Classification by spectral band dominance
  4. Preliminary clustering validation
  5. Honest assessment of f_NL improvement potential
- Future work:
  - Spectral inspection of top 100-500 anomalies
  - Injection/recovery completeness test
  - Ensemble anomaly detection (VAE + isolation forest)
  - Cross-correlation with CMB lensing for independent bias measurement
  - Application of methodology to DESI DR2 and beyond

### Appendix A: Catalog Format and Access
- Column descriptions for the released catalog
- Data access instructions (Zenodo DOI or similar)
- Example queries

### Appendix B: Artifact Rejection Details
- Detailed criteria for the 96 artifact suspects
- Fiber-number and observation-date correlations (if analyzed)

---

## 4. Figures Summary

| # | Description | Status |
|---|-------------|--------|
| 1 | Sky map of anomalies in DESI footprint | **NEED TO MAKE** |
| 2 | Autoencoder architecture diagram | **NEED TO MAKE** |
| 3 | Anomaly score distribution histogram | **NEED TO MAKE** (have data) |
| 4 | Example spectra (normal + anomalous) | **NEED TO MAKE** (requires spectral downloads) |
| 5 | Sky distribution color-coded by class | **NEED TO MAKE** (have positions) |
| 6 | Score vs band-dominance scatter | **NEED TO MAKE** (have data) |
| 7 | Angular correlation function w(theta) | **NEED TO MAKE** (have data in bias_validation.json) |
| 8 | Legacy Survey thumbnails of top 20 | **NEED TO MAKE** (have URLs) |
| 9 | f_NL improvement bar chart | **NEED TO MAKE** (have data) |

---

## 5. What We Have vs. What We Still Need

### HAVE (ready now)
- [x] Full anomaly catalog: 195,829 objects with positions, scores, band residuals
- [x] SIMBAD cross-match of top 100: 0/100 matches
- [x] Classification by band dominance: 4 categories + artifact suspects
- [x] Preliminary clustering analysis (Landy-Szalay, 3 score tiers)
- [x] f_NL improvement estimate (honest: 0.3-0.6%)
- [x] Legacy Survey viewer URLs for top objects
- [x] Processing statistics (17.7M spectra, 5.5 hours on H200)

### NEED (before submission)

**Critical (paper cannot be submitted without these):**
- [ ] **Spectral inspection of top 50-100 anomalies** — download actual DESI spectra, plot with reconstructions, classify what they are. Without this, we are publishing a list of numbers without knowing what we found. This is the single most important gap.
- [ ] **Injection/recovery test** — inject known unusual spectra into the pipeline, measure completeness. Without this, we cannot claim any completeness. Reviewers will demand this.
- [ ] **Artifact investigation for B-dominant population** — 44K objects (22.7%) are B-dominant. Is this a calibration systematic or genuine? Must check correlation with fiber number, observation conditions, airmass, galactic latitude. If systematic, must quantify and potentially remove.
- [ ] **Autoencoder architecture details** — exact layer sizes, activation functions, training data composition, hyperparameters. Need to recover these from the training code/logs on the GPU pod.

**Important (significantly strengthens the paper):**
- [ ] **Overlap check with Liang+2023 and Nicolaou+2026 EDR catalogs** — if available, cross-match our DR1 anomalies against their EDR anomalies. Do we recover the same objects? This validates consistency.
- [ ] **Proper clustering analysis with DESI LSS randoms** — current analysis uses uniform randoms, which does not account for the DESI angular selection function. Must use official DESI random catalogs.
- [ ] **Redshift distribution of anomalies** — plot n(z) from DESI pipeline redshifts. Are anomalies at particular redshift ranges?
- [ ] **Score threshold justification** — why 5.0? Show how results change with threshold (3.0, 4.0, 5.0, 6.0, 7.0). Demonstrate robustness.

**Nice to have (strengthens but not required):**
- [ ] Ensemble anomaly detection (VAE + isolation forest cross-validation)
- [ ] CMB lensing cross-correlation
- [ ] Photometric color analysis (g-r, r-z, W1-W2)
- [ ] Comparison with DESI's internal QSO catalog (how many anomalies are already classified?)

---

## 6. Target Journal

**Recommendation: The Astrophysical Journal Supplement Series (ApJS)**

Rationale:
- ApJS is the standard venue for large catalog papers
- The primary contribution is a data product (195K object catalog), not a single measurement
- ApJS papers can be longer, accommodating the catalog description + validation + application
- Recent precedent: DESI DR1 itself was published across ApJ/ApJS

**Alternatives:**
- **MNRAS** — also publishes catalog papers; Nicolaou+2026 published there
- **A&A** — possible but less natural for a DESI-focused catalog
- **ApJL** — too short for a catalog paper; would only work if we had a dramatic single result

**Format:** Full-length article, estimated 12-18 pages (ApJ format)

---

## 7. Estimated Timeline to Submission

| Phase | Tasks | Duration | Target Date |
|-------|-------|----------|-------------|
| **Phase 1: Critical gaps** | Spectral inspection (top 100), injection/recovery, B-dominant investigation, architecture documentation | 2-3 weeks | 2026-04-15 |
| **Phase 2: Figures** | All 9 figures, score distribution, sky maps, example spectra | 1 week | 2026-04-22 |
| **Phase 3: Writing** | Full draft (all sections) | 2 weeks | 2026-05-06 |
| **Phase 4: Internal review** | Self-review, fix inconsistencies, verify all numbers | 1 week | 2026-05-13 |
| **Phase 5: Submission** | Final formatting, compile, submit to ApJS | 3 days | 2026-05-16 |

**Total: ~7-8 weeks from today (late May 2026 submission)**

This is aggressive but feasible if the spectral inspection and injection/recovery tests go smoothly. The main risk is the B-dominant investigation — if 22.7% of the catalog turns out to be a calibration artifact, the paper needs significant reframing.

---

## 8. What Makes This Publishable vs. What Are the Gaps

### What makes it publishable NOW (in principle)

1. **Scale.** 17.7M spectra is ~90x the EDR. Nobody else has done this on DR1 yet (as far as we know). First-mover advantage matters.
2. **Clean SIMBAD result.** 100/100 top objects are new. This is a strong headline.
3. **Honest f_NL assessment.** Papers that honestly report incremental results are valued. We don't oversell.
4. **Community data product.** The catalog with Legacy Survey links is immediately useful to others regardless of our interpretation.

### What would get it rejected (the gaps)

1. **No spectral inspection.** A referee will ask: "What are these objects?" If we say "we don't know, we just found high reconstruction errors," that is insufficient. We need to look at at least 50-100 spectra and say: "30% are unusual emission-line galaxies, 25% are BAL QSOs, 20% are blue-end calibration issues, 15% are genuinely unclassifiable, 10% are artifacts." Even rough percentages from manual inspection would satisfy a referee.

2. **No completeness estimate.** Without injection/recovery, we cannot say whether our 1.11% anomaly rate represents 10% or 90% of the true anomalies in DESI. A referee will ask: "What unusual objects did you miss, and why?" We need at least a basic injection test with known anomalous spectra.

3. **B-dominant systematic.** 22.7% of anomalies are B-dominant. If a referee suspects this is a blue-end calibration issue (common in fiber spectrographs), and we haven't investigated, the paper is weakened. We need to either (a) show it correlates with instrumental parameters (and remove those objects) or (b) show it does NOT correlate (and they are genuine blue-end spectral features).

4. **No comparison with existing EDR catalogs.** Liang+2023 and Nicolaou+2026 found anomalies in EDR. If our method finds completely different objects in the overlapping footprint, that is concerning. If it finds the same objects, that is validating. Either way, we need to check.

### Minimum viable paper (if we want to submit fast)

Strip it down to:
- Sections 1-4 (data, method, catalog)
- Section 5 with SIMBAD cross-match only (drop clustering)
- Section 7 discussion with full honesty about limitations
- Drop Section 6 (f_NL) entirely — save for a separate paper

But still need: spectral inspection of top 50 + injection/recovery + B-dominant check. These three are non-negotiable.

---

## 9. Mandatory Prior Art Citations

These papers MUST be cited. Failure to cite direct prior work on DESI anomaly detection would be a serious omission and could lead to desk rejection.

1. **Liang et al. 2023, ApJL** — "Outlier Spectral Analysis of DESI EDR" (or similar title). Autoencoder + normalizing flow on ~250K DESI EDR spectra. The most direct predecessor.

2. **Nicolaou et al. 2026, MNRAS** — "Anomaly Detection in DESI EDR with Astronomaly" (or similar title). VAE-based approach on ~208K DESI EDR spectra. The other direct predecessor.

3. **DESI Collaboration 2024** — DESI DR1 data release paper. Must cite the data source.

4. **Baron & Poznanski 2017** — Anomaly detection in SDSS spectra. Foundational work in spectroscopic anomaly detection.

5. **Reis et al. 2019** — Anomaly detection in astronomical spectra (if applicable to method).

---

## 10. Relationship to Bounce Cosmology Program

This paper is intentionally decoupled from the bounce cosmology claims. The connection is:
- The bounce model predicts f_NL = -4.375
- Better tracers could help constrain f_NL
- But the improvement is incremental (0.3-0.6%), so we don't oversell

The paper stands on its own as an observational/methodological contribution. The bounce connection appears only in Section 6 as one of several motivations for improving f_NL constraints, alongside inflation and curvaton models. This is deliberate: the catalog paper should be publishable regardless of whether bounce cosmology is correct.
