# EXT10 Harvest — P4 — Gemini
- Provider: Gemini
- Model/Effort: 3.5 Thinking (Solves complex problems)
- Chat URL: https://gemini.google.com/u/0/app/3e0efda152a967cb
- PDF md5: 414048af
- Harvested: 2026-06-13 15:16 PDT

---

## Referee Report

**Journal:** MNRAS / Physical Review D / JCAP
**Manuscript Title:** Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)
**Author:** Houston Golden (Independent Researcher)
**Date of Review:** June 13, 2026
**Version:** v1.0.185

---

**1. Recommendation: MINOR REVISIONS**

This manuscript presents an exceptionally thorough, methodologically rigorous, and large-scale study of galaxy morphology chirality utilizing 8.47 million galaxies from the DESI Legacy Imaging Surveys DR8. By implementing a flip-equivariant Vision Transformer architecture paired with Test-Time Augmentation (TTA), the author systematically robustifies the catalog against the artificial network biases that have historically led to spurious claims of cosmic parity violation or directional dipoles. The statistical controls, clear separation of diagnostic vs. primary estimators, and transparent accounting of survey geometry leakage set a high standard for future publications in this field. The science is completely sound, and the paper is nearly ready for publication pending a few administrative updates and minor clarifications.

---

**2. Strengths**

- **Unprecedented Scale:** To our knowledge, this is the largest chirality-labeled galaxy catalog produced to date, spanning over 8.47 million total galaxies and 3.20 million classified spiral galaxies, significantly expanding the statistical volume over prior works.

- **Methodological Rigor via Equivariance:** The implementation of a 2-fold flip-equivariant TTA pipeline forces a flip-swap correlation of exactly 1.000 by construction. This simple but powerful architectural control collapses a raw +28.72σ classifier bias down to a uniform, manageable monopole offset.

- **Definitive Explanation of Systematic Leakage:** The author identifies and quantifies a major pitfall in pseudo-Cℓ estimations on cut skies, proving that a small uniform classifier monopole couples to patchy survey-mask geometries to simulate high-significance dipoles. The generative null model successfully reproduces 99.32% of the pre-MASTER ℓ=1 power from mask leakage alone.

- **Comprehensive Diagnostic Battery:** The paper stands out due to its multi-axis bias-hardening audit suite (incorporating eight distinct stress tests) and an 8-anchor systematic analysis in the appendices that explores boundary conditions, cross-power alignment, and quality-quartile dependencies.

---

**3. Specific Scrutiny**

**Real-Space ℓ=1 Dipole Headline**
The primary real-space high-confidence dipole fit (restricting to galaxies with confidence >0.6; N≈9.5×10^5 spirals) yields a significance of +0.41σ (empirical-rank p=0.31), which is fully consistent with a null isotropic universe. The author correctly distinguishes this rank calculation from standard Gaussian mappings due to the positive-definite nature of the dipole amplitude.

**Joint Nuisance-Marginalized Template Fit**
The manuscript employs a robust 9-template weighted least squares (WLS) linear regression on the canonical-mask field. Using a spatial-coherence-respecting block-bootstrap model at NSIDE=8 (Nboot=1000 iterations over 440 super-pixels), the author establishes that a clean cosmological dipole at a 1.7% reference amplitude is excluded at z ≈ -18.1.

**MASTER Channel as a Systematics Diagnostic**
While the post-MASTER harmonic channel displays an excess of +7.28σ on the apodized footprint, the author provides compelling evidence that this channel serves as a systematic tracer rather than a cosmological detection. The stability of this excess under depth-stratified nulls (+7.13σ) indicates that joint spatial-depth features and morphology-correlated instrument variations dominate the signature.

**ℓ=2 Cross-Spectrum Antialignment**
The cross-correlation between the chirality field Ap and the pixel-density field ntotal(p) yields rℓ=2=−0.65 with a significance of σ=−2.89 at the quadrupole scale. This strong anti-alignment provides unambiguous observational proof that the large-scale harmonic residuals are tied to footprint-correlated depth variations rather than primordial cosmic structure.

**Shamir 2020 vs. 2022 Literature Breakdown**
The comparison with previous claims is factual and properly caveated. The author carefully reviews the legacy literature, citing Shamir (2012), Shamir (2020), Shamir (2022a), and Shamir (2022b). The report appropriately underscores that the current pipeline excludes the previously claimed ~3% signal amplitude by a factor of 6 to 12.

---

**4. Blockers (Must fix before publication)**

**Section VI.A / Page 13 — In-Computation Placeholder:** The text states that "a finer-grid, higher-Ninj recovery curve is in computation". For final journal publication, the author must conclude this calculation, update the text to reflect the finalized output, and explicitly confirm whether the updated grid introduces any shifts to the bracketed A95∈(1.0%,1.5%] boundary.

**Data Availability / Page 21 — Zenodo DOI Placement:** The paper notes that "A persistent archival DOI (Zenodo deposit of the versioned release) has not yet been minted". Minting this persistent identifier and updating the manuscript text with the active DOI link is a mandatory requirement for final acceptance.

---

**5. Majors (Should fix)**

None. The scientific conclusions are fully backed by extensive null tests, injection-recovery validation curves, and structural cross-checks. No additional core analysis or scientific rework is required.

---

**6. Minors (Polish)**

- **Section III.A / Page 3 — Notation Invariance:** The author defines three distinct significance metrics (Moment-z, MASTER ℓ=1 moment-z, and Blockbootstrap-z). While the differences are explained well, adding a sentence reminding readers of these distinct conventions in the captions of Table III and Table X would improve the paper's standalone readability.

- **Appendix B.d / Page 18 — Circular Coordinate Wrapping for T5:** The text notes a minor limitation of test T5, which uses a linear Pearson correlation coefficient against the raw Right Ascension (RA) coordinate. Since RA is a circular coordinate (0°≡360°), using a standard linear correlation can artificially damp the apparent azimuthal coupling. The text would benefit from a quick note recommending circular-linear correlation metrics for future iterations of test T5.

- **Section IV.A / Page 5 — Rounding Transparency:** The text states that catalog composition percentages are rounded to maintain a sum-to-one consistency at the second decimal place. It would be helpful to briefly state the unrounded percentage fractions directly alongside the integer counts to maximize transparency for future metadata collectors.
