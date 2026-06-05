# P4 auto-2026-06-05_1517pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 136.8s

---

## Referee Report for PRD

**Manuscript Title:** Survey-Scale Galaxy Chirality with Equivariant TTA: A -0.122σ Subsample-Mask l=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)
**Author:** Houston Golden
**Journal:** Physical Review D

This paper presents a comprehensive analysis of the large-scale angular distribution of spiral galaxy chirality using a new catalog of 3.2 million spiral galaxies derived from the DESI Legacy Imaging Surveys. The primary scientific result is a null detection of a chirality dipole (l=1 mode), which is a parity-even, isotropy-breaking observable. The authors employ a Vision Transformer (ViT) classifier with Test-Time Equivariant Averaging (TTA) to create the catalog and perform a rigorous set of systematic checks. A key part of the analysis is the identification and quantification of a "monopole-mask leakage" channel, where a small global monopole in the classified sample couples with the survey mask to create a spurious dipole signal. The paper convincingly demonstrates that this systematic effect can explain previous claims of detection and that, after proper mitigation, no significant dipole remains.

The methodology is generally sound and represents a significant advance in the rigor applied to this type of measurement. The public release of the catalog, model, and analysis code is commendable. The distinction between the parity-even dipole and parity-odd monopole/even-l modes is correctly and clearly maintained.

However, the manuscript contains several significant numerical errors, inconsistencies, and presentation issues that must be addressed before it can be accepted for publication. These issues undermine confidence in the otherwise careful analysis.

### Findings

#### ESSENTIAL

*   **P4-E1:** Section IV, Table III (p. 5). The table of angular power spectrum results is unverifiable and potentially inconsistent. The `Significance (σ)` column cannot be recomputed from the provided `C_l` and `σ_null` columns, as the null mean `<C_l_null>` is not given. For the `leff=4` bandpower, the reported significance of +6.097σ with C_l = 3.210e-6 and σ_null = 0.804e-6 would imply a large negative null mean, which is highly unusual for a power spectrum (a positive-definite quantity).
    *   **Required Fix:** The table must be corrected and clarified. Add a column for the null mean `<C_l_null>`. Ensure that the significance is calculated as `(C_l - <C_l_null>) / σ_null` and that all values are consistent. Provide a brief explanation for any non-obvious features, such as a potentially non-zero null mean.

#### MAJOR

*   **P4-M1:** Section II.B (p. 2) & Section III (p. 3). The description of the training dataset contains numerical errors. The text states the set contains 26,636 images from three sources: 6,637 (GZ1), 17,153 (CE-ResNet), and 2,000 (Synthetic). The sum is 6637 + 17153 + 2000 = 25,790, not 26,636. This discrepancy of 846 images must be resolved. Consequently, the derived percentage of labels from CE-ResNet ("67.6%") is also incorrect.
    *   **Required Fix:** Correct the total number of training images and all dependent calculations. Verify all numbers in this section for self-consistency.

*   **P4-M2:** Section IV.B, Table II (p. 4). The deviation from a 50/50 split for the equivariant Catalog C is reported with a sign error. With fcw = 0.4974, the deviation is negative. The table correctly shows an excess of -0.26%, but the deviation is listed as `9.5` σ. It should be `-9.5` σ. This error is propagated into the main text on p. 4, which refers to "the global 9.5σ monopole".
    *   **Required Fix:** Correct the sign of the deviation in Table II and in all corresponding mentions in the text.

*   **P4-M3:** Section IV.B (p. 4). The text claims a "3.86x asymmetry-suppression factor from raw +2.05% to equivariant -0.53%". These percentages are inconsistent with the values reported in Table II for the raw (Tier A) and equivariant (Tier C) catalogs, which are +0.79% and -0.26% respectively.
    *   **Required Fix:** Reconcile the numbers in the text with those in Table II. If the numbers in the text refer to a different quantity (e.g., a different definition of asymmetry), this must be explicitly defined and justified. Otherwise, correct the text to match the table.

*   **P4-M4:** Section VI.B (p. 6). The paper claims its null result disfavors the "Shamir ~3% amplitude class by a factor of ~6–12". This factor is not justified. The paper's own empirical 50%-recovery-at-3σ threshold is A ≈ 0.75%. A simple comparison gives a factor of 3% / 0.75% = 4.
    *   **Required Fix:** Provide a clear and explicit calculation to justify the factor of 6–12. Specify precisely which "3% amplitude" from Shamir's work is being used for the comparison (e.g., overall dipole amplitude, peak regional asymmetry) and explain how it maps to the full-amplitude `A` defined in this work.

#### MINOR

*   **P4-m1:** Title (p. 1). The title is exceptionally long and dense with technical jargon. While accurate, it functions more as a one-sentence abstract, reducing its immediate impact and readability.
    *   **Required Fix:** Shorten the title to focus on the main scientific result. A suggestion would be: "A Null Measurement of the Galaxy Chirality Dipole from 3.2 Million DESI Legacy Spirals". The details about the leakage channel and systematic residuals are better placed in the abstract.

*   **P4-m2:** Metadata (p. 1). The paper is dated "June 2026".
    *   **Required Fix:** Change the date to the date of submission.

#### NIT

*   **P4-N1:** Section IV, Table I caption (p. 4). The description of `N_map_weighted` states it is used as a "survey-depth weight". The choice to use the total number of galaxies (spirals + non-spirals) as the weight, rather than just the number of spiral galaxies, is reasonable but could be briefly justified (e.g., as a more robust proxy for imaging depth and quality, less susceptible to morphological classification variations).
    *   **Required Fix:** Consider adding a short sentence of justification for this choice of weight map.

## Summary recommendation

**MAJOR REVISIONS**

The paper presents a valuable and methodologically robust null result for the galaxy chirality dipole. The analysis of systematic effects, particularly the monopole-mask leakage, is thorough and convincing. This work has the potential to be a definitive statement on this topic at the current survey scale. However, the manuscript is compromised by several numerical errors and inconsistencies in key tables and text, including a basic arithmetic error in the training set size, a sign error in a key result, and an unsubstantiated factor in the comparison to previous work. An essential table containing the main power spectrum results is unverifiable as presented. These issues must be thoroughly addressed to ensure the paper meets the high standards of rigor and accuracy expected for publication in Physical Review D. I recommend that the paper be reconsidered after major revisions have been made to correct these flaws.