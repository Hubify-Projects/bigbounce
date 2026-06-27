# P4 R54 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R54_P4/chirality_catalog_paper.pdf` md5=bda86fa1 pages=23
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 183.9s

---

**Referee Report on "Survey-Scale Galaxy Chirality with Equivariant TTA..."**

**To the Editor of Physical Review D,**

This paper presents a comprehensive analysis of galaxy chirality using a catalog of 8.47 million galaxies from the DESI Legacy Surveys, of which 3.2 million are classified as spirals. The authors employ a Vision Transformer with a Test-Time Averaging (TTA) scheme to enforce flip-equivariance, a crucial step for mitigating systematic biases. The primary scientific result is a null detection of a real-space chirality dipole at a sensitivity level that places strong constraints on previously reported claims. The paper's main contributions are (1) the production of the largest publicly available chirality-labeled galaxy catalog, (2) a robust null result for the chirality dipole, and (3) a detailed methodological investigation into systematics, most notably the quantification of a "monopole-mask leakage" channel that can produce spurious dipole signals.

The analysis is exceptionally rigorous and transparent. The authors pre-declare their analysis hierarchy, carefully distinguish between different estimators and null hypotheses, and provide an extensive suite of robustness checks and systematic-in-characterization diagnostics. The methodological lesson—that a sub-percent classifier bias can be amplified by survey geometry into a highly significant but spurious signal—is a critical contribution to the field. The paper is well-written, self-contained, and provides exemplary documentation for reproducibility.

The work is of high quality and is suitable for publication in Physical Review D. I recommend acceptance after the authors address the following essential and minor points.

---
### **Detailed Findings**

#### **ESSENTIAL**

*   **P4-E1:** **Section: Data Availability (Page 22)**
    *   **Problem:** The commit hash is associated with a future date. The text states: "Repository state for this release: commit 53b41d12 (June 2026)". This is a placeholder that must be updated for the final publication.
    *   **Required Fix:** Replace the placeholder date with the correct date corresponding to the final, version-stamped commit hash for the camera-ready version of the paper. Confirm that the Zenodo DOI for the archival snapshot has been created and is included, as promised in the text.

#### **MAJOR**

*   **P4-M1:** **Section: Abstract (Page 1)**
    *   **Problem:** A key falsification criterion in the abstract is garbled by a typo. The text reads: "a future > 5σ real-space dipole detection ... at amplitude A A95".
    *   **Required Fix:** Correct the typo to "A ≥ A95" or "A > A95" to match the intended meaning, which is that an amplitude greater than or equal to the A95 threshold would be in tension with the null.

#### **MINOR**

*   **P4-m1:** **Section: Abstract (Page 1)**
    *   **Problem:** The abstract states the WLS template fit disfavors a clean cosmological dipole "at z ≈ -18". The corresponding result in Appendix D (Table X, Page 20) is a more precise z = -18.1. Given the strength of this exclusion, the precision is meaningful.
    *   **Required Fix:** Please report the value as z ≈ -18.1 in the abstract to better reflect the precision of the calculation in the main text.

*   **P4-m2:** **Section: IV.C Dipole Analysis (Page 7)**
    *   **Problem:** The definition of the dipole amplitude is missing vector notation. The text reads: "the dipole amplitude is Adip = |a".
    *   **Required Fix:** Correct this to Adip = |**a**| to indicate the magnitude of the dipole vector **a**.

*   **P4-m3:** **Section: IV.C Dipole Analysis (Page 7)**
    *   **Problem:** The text correctly notes that at the low significance of the best-fit dipole, the direction (l, b) = (293°, 12°) is unconstrained.
    *   **Required Fix:** For clarity, I suggest adding a brief parenthetical statement explicitly stating that this direction is the best-fit point but carries no statistical significance, e.g., "(the best-fit direction, which is statistically unconstrained)".

*   **P4-m4:** **Section: IV.D Monopole+Mask Leakage Generative Null (Page 9) & Abstract (Page 1)**
    *   **Problem:** The abstract quotes the canonical-mask residual as "+3.64σ moment-z, ≈1.9σ Gaussian-equivalent". This Gaussian-equivalent value is derived and mentioned on page 15 but is absent from the primary discussion of the +3.64σ result on page 9. The heavy-tailed nature of the null (mentioned in the Table III caption) makes this conversion non-trivial and important context.
    *   **Required Fix:** Please add the "≈1.9σ Gaussian-equivalent" clarification when the +3.64σ result is first introduced on page 9, to provide immediate context on its statistical weight and to directly support the abstract's statement.

*   **P4-m5:** **Section: III.B Training Labels (Page 3)**
    *   **Problem:** The text in the caption of Figure 1 refers to the classifier as "The ViT - Small classifier". This appears to be a typo.
    *   **Required Fix:** Change "ViT - Small" to "ViT-Small" for consistency with the model's standard name (e.g., as used in Appendix B).

#### **NIT (Cosmetic)**

*   **P4-N1:** **Section: III.A Notation and Significance Conventions (Page 3)**
    *   **Problem:** In the "MASTER l=1 moment-z" bullet point, the notation for the null mean is `(C1)null`, whereas the line above introduces the convention `(x)null`.
    *   **Required Fix:** For consistency, consider using `<C1>_null` or `μ_null(C1)` to represent the mean of the null distribution for C1.

*   **P4-N2:** **Section: Appendix A (Page 16)**
    *   **Problem:** Typo in a subheading: "Bandpower US single-l estimator distinction."
    *   **Required Fix:** Change "US" to "vs.".

*   **P4-N3:** **Section: Appendix D (Page 20)**
    *   **Problem:** The caption for Table X defines the z-score as `z = â/σ(â)`. The text makes a critical distinction between the naive WLS errors and the more robust block-bootstrap errors.
    *   **Required Fix:** To improve clarity, I suggest adding a subscript to the sigma in the caption, e.g., `σ_naive(â)`, to remind the reader that these are the naive, pre-bootstrap errors.

---
### **Summary recommendation**

**ACCEPT WITH MINOR CORRECTIONS**

The paper is of outstanding quality, presenting a robust and highly significant result in a methodologically transparent and rigorous manner. The identified issues are minor and easily addressable. The essential fix regarding the placeholder date in the data availability section is a prerequisite for publication but is straightforward. This work represents a substantial advance in the search for cosmic parity violation and provides a valuable public data product and methodological template for future studies. It is well-suited for publication in Physical Review D.