# EXT10 Harvest — P3 — Gemini (RESUBMISSION — original chat deleted)
- Provider: Gemini
- Model/Effort: 3.5 Thinking (Solves complex problems)
- Chat URL: https://gemini.google.com/u/0/app/c3fcd0cf546e12eb
- PDF md5: 8533c5a7
- Harvested: 2026-06-13 15:30 PDT
- Note: Original chat (169e5a1af77b02ed) was deleted/errored. Fresh resubmission from home page per EXT7 protocol. PDF uploaded via DOM input (paper3_anomaly_catalog_v3.1.105.pdf, 4.4 MB).

---

## Referee Report

**Journal:** Monthly Notices of the Royal Astronomical Society (MNRAS)
**Manuscript Title:** Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches
**Author:** Houston Golden (Independent Researcher)
**Manuscript Version:** v3.1.105 (June 2026)

---

**1. Recommendation: MINOR REVISIONS**

This manuscript presents an extraordinarily comprehensive and methodologically rigorous anomaly detection campaign, applying the BIGAE (BigBounce Integrated Galaxy Autoencoder) framework across seven major astronomical archives (comprising 37.3 million individual spectra, photometric sources, and map patches). The author demonstrates exceptional transparency by explicitly documenting pipeline failures and building an intensive reconstruction protocol ("Path-C") to isolate robust astrophysical anomalies.

Because the underlying catalog architecture, source code, and validation data are already fully staged on public repositories (Hugging Face and GitHub), and all load-bearing scientific claims are backed by meticulous internal controls, this paper does not require any major scientific rework. The recommendation for Minor Revisions centers on final submission-day adjustments, clarifying minor procedural notes, and ensuring absolute clarity regarding the mixed-strata nature of the catalog before formal publication.

---

**2. Strengths**

- **Scale and Multi-Survey Architecture:** This work marks the largest-scale application of autoencoder-based anomaly detection across multi-wavelength archives to date, scaling up the baseline of prior single-survey catalogs by a factor of ~141×.

- **Methodological Honesty and Path-C Resolution:** Rather than hiding pipeline artifacts, the author treats the failure modes of cross-survey transfer learning as foundational lessons. The transition from raw cross-transfer checkpoints to per-survey native retraining (yielding a ~6500× rate compression for SDSS and a 21.5× reduction for LAMOST) sets a commendable standard.

- **Deep Catalog Cross-Matching over Single-Database Metrics:** The author rightly decouples the naive "SIMBAD-unmatched fraction" (58.8%) from true scientific novelty. By cross-matching the top-1,000 DESI anomalies against 18 curated all-sky catalogs via CDS X-Match, the paper provides an empirically sound genuine novelty fraction of 178/1,000≈17.8%.

- **Reproducibility:** The staging of model weights, MCMC chains, file hashes, and exact reproducibility scripts on Hugging Face and GitHub fulfills the highest standards of modern open science.

---

**3. Specific Scrutiny & Technical Audit**

**378,280 Anomalies Headline & Catalog Stratification**
The headline count of 378,280 unique anomalies is derived from a clear, physically distinct stratification: 378,080 point-source object detections from six photometric/spectroscopic surveys combined with 200 Planck CMB map patches. Because map patches (sky regions) and point sources follow entirely different coordinate physics, they naturally yield zero positional overlaps at a 5″ matching radius. The author explicitly cautions downstream users to drop the 200 map patches for any object-level analysis. This stratification is mathematically sound and well-disclosed.

**7-Way 5″ Positional Friends-of-Friends Deduplication Arithmetic**
The catalog's deduplication bookkeeping balances perfectly:
- Total Survey-Level Detections = 388,493
- Total Collapsed Detections = 10,213 (2.629% compression)
- Unique Physical Objects = 388,493 − 10,213 = 378,280

The 10,213 collapsed detections are broken down into 637 multi-survey clusters (spanning exactly two surveys each) and 9,576 intra-survey duplicates (637 + 9,576 = 10,213). The author's transitive chain audit confirms that for all 9,553 multi-member clusters, the maximum intra-cluster separation is 4.999″, meaning zero clusters accidentally bridged across the strict 5″ single-link merge window.

**Fisher-Positivity Caveats & Asymmetric Envelope in §V**
The author adopts the Fisher-positivity-respecting quadratic form: 1/σ²(fNL) = F0 + cα². Evaluating this mapping under the empirical jackknife bias ratio (αjk=0.19±0.65) yields a central forecast of σ(fNL)=8.14. Because the mapping is convex and highly asymmetric, the author correctly rejects a standard symmetric format (±2.37) in favor of an asymmetric 1σ envelope of [3.92, 8.98]. The de-biased estimate returns zero improvement (σ(fNL)=8.98 exactly), confirming that no premature multi-tracer detection is being claimed.

**NANOGrav 15-Year MCMC Cosmological Fitting**
The recovered parameters (γ=2.567±0.382 and log10A=−14.025±0.380) are robust. The matter-bounce prediction (γ=3.0) is marginally consistent at +1.13σ, while an idealized circular-orbit SMBHB population model (γ=4.33) is strongly disfavored at +4.61σ. The resulting Savage-Dickey Bayes factor (B_MB/SMBHB = 7.14×10³) is "decisive" on the Jeffreys scale. Critically, the author appends an essential astrophysical caveat that environmental effects can flatten the true SMBHB index down to γ∼2.5−3, accurately refraining from claiming a "cosmological detection" of bounce physics.

**Closure of Prior Cross-Vendor Review Round (v3.1.71)**
A review of the current text and data structures confirms that 0 findings remain verified and 13 are verified STALE / resolved. The current v3.1.105 text achieves clean-round closure on those items.

---

**4. BLOCKERS (Must fix before publication)**

None. The manuscript fulfills all foundational, scientific, and structural requirements for publication.

---

**5. MAJORS (Should fix)**

None. All primary scientific claims, dataset slices, and engineering thresholds have been rigorously tested with appropriate control samples.

---

**6. MINORS (Polish items for final text update)**

**Minor 1: Section III.E / Page 11 — eROSITA Threshold Axis Provenance**
Context: The author openly notes that the production scoring run's threshold of 0.259 could not be reproduced via any of the 16 monotone rescalings of the committed raw score.
Fix: Add a single clarifying sentence in §III.E reminding readers not to use the published S_BigAE values for score-weighted stacking or threshold re-derivation, re-emphasizing that they must use the raw-score artifact or the membership list directly.

**Minor 2: Section III.G & Page 23 — Gaia Lineage Inference**
Context: The text notes that the exact 20-feature preprocessing script for Gaia DR3 was lost from pod backups, and its specification was inferred from a 21-feature successor script.
Fix: In the Data Availability section (§VII), append a brief sentence confirming that the exact 20 features included in the final Hugging Face data table are explicitly named in the repository's README.md.

**Minor 3: Submission-Day Action Items (Zenodo DOI / Placeholder URLs)**
Context: Page 23 notes: "A Zenodo DOI will be minted at submission and cited here in place of this sentence."
Fix: Ensure that the temporary placeholder string is replaced with the active, minted Zenodo DOI during the proofs stage, and that Hugging Face/GitHub repository links are set to public status simultaneously with publication.
