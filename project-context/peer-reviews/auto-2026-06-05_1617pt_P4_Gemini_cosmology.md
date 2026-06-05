# P4 auto-2026-06-05_1617pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 157.5s

---

## Referee Report for PRD Submission

**Paper ID:** P4
**Title:** Survey-Scale Galaxy Chirality with Equivariant TTA: A -0.122σ Subsample-Mask l=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)
**Author:** Houston Golden

This paper presents a detailed analysis of galaxy chirality using a large catalog of 3.2 million spiral galaxies from the DESI Legacy Surveys. The primary scientific result is a null detection of a cosmological dipole (l=1) in the chirality asymmetry map. The authors present two primary estimators that both yield null results: a real-space dipole fit (+0.43σ) and a MASTER-deconvolved spherical harmonic amplitude (-0.122σ).

A significant portion of the paper is dedicated to a rigorous investigation of systematic effects. The authors identify a +3.64σ residual on a specific "canonical" survey mask and convincingly demonstrate that this is not a cosmological signal but rather an artifact arising from the coupling of a small, uniform classifier monopole bias with the patchy survey geometry. This systematic analysis is exemplary and serves as a valuable case study for large-scale structure analyses. The paper is well-structured, the methodology is transparent, and the public release of data, code, and models is commendable.

The paper correctly distinguishes between the parity-even l=1 dipole (an isotropy test) and parity-odd observables (a parity test), a subtlety often missed in the literature. The analysis is thorough, and the conclusions are well-supported by the evidence presented.

While the paper is of high quality, several revisions are required to meet the standards of Physical Review D, primarily concerning the clarity and numerical consistency of the tables.

---
### Detailed Findings

#### ESSENTIAL

*   **P4-E1 | Section: IV, Page 5, Table III**
    *   **Problem:** Table III, which presents the angular power spectrum results, is difficult to interpret and appears to be missing information. The "Significance (σ)" column cannot be verified from the other columns provided. Assuming the standard definition `z = (C_l - <C_l^null>) / σ_null`, the mean of the null distribution, `<C_l^null>`, is required but absent. Furthermore, applying this formula to the bandpower results (rows 2-5) by back-calculation yields unphysical (negative) values for `<C_l^null>`, suggesting the significance is defined differently for these rows.
    *   **Required Fix:** Add a column for `<C_l^null>` to Table III. In the caption, provide an explicit mathematical definition for how "Significance (σ)" is calculated for all rows. Ensure that all values in the significance column can be reproduced using the numbers provided in the table.

#### MAJOR

*   **P4-M1 | Section: IV, Page 4, Table II**
    *   **Problem:** The values in the "Dev. (σ)" column of Table II are not reproducible from the other data in the table. For example, for Tier C, the CW fraction `p = 0.4974` and `N = 3,201,160` give a binomial standard deviation of `σ_p ≈ 0.000279`. The deviation from 0.5 is then `(0.4974 - 0.5) / 0.000279 ≈ -9.31σ`, not -9.5σ as reported. Similar small discrepancies exist for Tiers A and B. While minor, this inconsistency undermines confidence in the numerical precision of the analysis.
    *   **Required Fix:** Recompute the "Dev. (σ)" column using un-rounded intermediate values and ensure the results are accurate. Alternatively, provide a footnote explaining the precise calculation if it differs from the standard `(p - 0.5) / sqrt(p(1-p)/N)`.

*   **P4-M2 | Section: IV D, Page 4**
    *   **Problem:** The text contains the sentence: "...were interpreted in earlier paper versions as mask-geometric leakage...". This phrasing refers to the internal revision history of the manuscript, which is inappropriate for a formal journal publication.
    *   **Required Fix:** Rephrase this sentence to remove the reference to past drafts. For example: "The +3.64σ value on the canonical mask and the 3.05σ local hemisphere maximum are consistent with an interpretation as mask-geometric leakage of the global 9.5σ monopole. We formalize this interpretation with a generative null..."

#### MINOR

*   **P4-m1 | Section: Title block, Page 1**
    *   **Problem:** The paper is dated "June 2026", a future date.
    *   **Required Fix:** Correct the date to the submission date.

*   **P4-m2 | Section: IV, Page 5, Table IV**
    *   **Problem:** The z-score for the "Pre-MASTER pseudo-C(l=1)" statistic is reported as +1.68. However, a direct calculation from the provided data and null values gives `(1.696 - 1.685) / 0.007 ≈ 1.57`. This discrepancy should be resolved.
    *   **Required Fix:** Please verify the calculation and update the z-score in Table IV to be consistent with the data and null values, or use higher-precision numbers in the calculation and note this in the caption.

#### NIT (Nitpicks)

*   **P4-N1 | Section: Abstract, Page 1**
    *   **Problem:** The phrasing "...empirical rank p_mc = 0.030, i.e. ≈1.9σ Gaussian-equivalent..." could be clearer. The "i.e." implies a direct definition, whereas it is an approximate correspondence.
    *   **Required Fix:** Suggest rephrasing for precision, for example: "...empirical rank p_mc = 0.030 (corresponding to a one-sided significance of ≈1.9σ for a Gaussian distribution)...".

*   **P4-N2 | Section: VII. Conclusions, Page 6**
    *   **Problem:** Item (c) states that MASTER deconvolution "collapses the pseudo-C_l to the canonical -0.122σ null." This appears to be a typo. The -0.122σ result is for the *subsample mask*, while the *canonical mask* result is the +3.64σ systematic residual. This is a critical distinction that the paper correctly makes elsewhere.
    *   **Required Fix:** Correct the text to read "...collapses the pseudo-C_l to the -0.122σ null on the subsample mask." or similar, to maintain consistency with Table I and the main text.

---
## Summary recommendation

**MAJOR REVISIONS**

The paper represents a substantial and high-quality contribution to the field. The core analysis is sound, and the systematic checks are exceptionally rigorous. The primary recommendation for major revisions stems from the need to correct and clarify numerical results presented in the tables (P4-E1, P4-M1). Without these corrections, the key quantitative results of the paper cannot be independently verified by the reader, which is an essential requirement for publication. The other required changes, while less critical, will improve the professionalism and clarity of the manuscript. I am confident that the authors can address these points, and I look forward to reviewing a revised version of this promising paper.