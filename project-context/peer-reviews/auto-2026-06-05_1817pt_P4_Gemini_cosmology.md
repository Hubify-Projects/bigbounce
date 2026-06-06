# P4 auto-2026-06-05_1817pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (3011 chars)
**Wall time**: 140.5s

---

Here is a complete referee report for the submitted manuscript.

***

## Referee Report: P4

**Manuscript ID:** P4
**Title:** Survey-Scale Galaxy Chirality with Equivariant TTA: A -0.122σ Subsample-Mask l=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)
**Author:** Houston Golden

This paper presents an analysis of galaxy chirality using a catalog of 3.2 million spiral galaxies from the DESI Legacy Surveys. The primary scientific result is a null detection of a cosmological dipole (l=1) in the chirality asymmetry map. The authors perform a detailed and rigorous analysis of potential systematic effects, identifying a specific leakage channel where a global monopole asymmetry couples with the survey mask to create a spurious dipole-like signal in naive estimators. They demonstrate that this channel can explain previous claims of a detection in the literature. The headline result is derived from estimators designed to be insensitive to this leakage and is robustly null (-0.122σ).

The scientific methodology, particularly the deep dive into systematics, is a significant strength of this work. The use of a declared analysis hierarchy, a bias-hardening suite for the classifier, and multiple cross-checking null tests is commendable and sets a high standard for this type of analysis. The distinction between the parity-even dipole and parity-odd monopole/even-l multipoles is correctly handled.

However, the manuscript in its current form contains several essential and major errors, inconsistencies, and points of confusion that must be addressed before it can be considered for publication in Physical Review D. The core analysis appears sound, but the numerical reporting and clarity of presentation do not meet the required standards.

### ESSENTIAL Revisions

These issues must be fixed for the paper to be reconsidered.

*   **P4-E1 | Title Page | Future Publication Date:** The paper is dated "June 2026". This is a future date and must be corrected to the date of submission.
*   **P4-E2 | Sec II.B, p. 2 | Training Set Size Discrepancy:** The text states the training set is assembled from three sources: "6,637 galaxies" (GZ1), "17,153 galaxies" (CE-ResNet), and "2,000 artificial images" (Synthetic). The sum of these is 6,637 + 17,153 + 2,000 = 25,790. However, the paper claims "The combined training set contains 26,636 images". This discrepancy of 846 images must be resolved.
*   **P4-E3 | Table II & Sec IV.B, p. 4 | Sign Error in Monopole Significance:** In Table II, for Catalog C (equivariant), the CW fraction is 0.4974, which is less than 0.5. The "Excess (%)" is correctly listed as -0.26. However, the "Dev. (σ)" is listed as 9.5. This should be negative. A direct calculation gives (0.4974 - 0.5) / 0.000279 ≈ -9.3. This sign error is critical as it misrepresents the nature of the residual monopole. The error is repeated in the text of Section IV.B, which states "The Catalog C residual (9.5σ from 0.5000, Table II)". This must be corrected to -9.5σ (or the correctly calculated value) in both the table and the text.

### MAJOR Revisions

These issues represent significant flaws in the presentation that require substantial changes.

*   **P4-M1 | Abstract, p. 1 | Conflicting Significance of Canonical-Mask Residual:** The abstract presents two different significance values for the same quantity, which is highly confusing. It states: "The post-MASTER canonical-mask direct-MC residual is +3.64σ (z = Δ/σ_null moment-ratio; empirical rank p_mc = 0.030, i.e. ≈1.9σ Gaussian-equivalent...)". A p-value of 0.030 corresponds to a one-sided significance of ~1.88σ. Presenting both +3.64σ and ≈1.9σ for the same residual without a clear, immediate explanation of why two different metrics are used and what they mean is unacceptable in an abstract. The abstract must be rewritten to present this diagnostic result clearly, perhaps by choosing one metric or by carefully phrasing the sentence to avoid the apparent contradiction.
*   **P4-M2 | Sec IV.B, p. 4 | Inconsistent Asymmetry Values:** The text in Section IV.B claims: "The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant -0.53% demonstrates the dominance of the equivariant TTA processing." These percentage values do not match those in Table II. Table II reports a raw excess (Catalog A) of +0.79% and an equivariant excess (Catalog C) of -0.26%. The source of the +2.05% and -0.53% values must be clarified, or the text must be corrected to use the values from Table II, with the suppression factor recalculated accordingly.
*   **P4-M3 | Table III, p. 5 | Unverifiable Significance Values:** The significance values reported in Table III for the bandpowers (rows 2-7) cannot be verified from the information given. The significance of a power spectrum measurement is typically calculated as `(C_l - <C_null>) / σ_null`, where `σ_null` is the standard deviation of the null simulations. The table provides `C_l` and `σ_null` but omits `<C_null>`. Without the mean of the nulls, the calculation is impossible. For example, for l_eff=4, `C_l=3.210` and `σ_null=0.804`. The reported significance of +6.097 implies `<C_null>` is negative, which is unphysical for a power spectrum. The table must be amended to include the mean of the null power spectra for each bin, and the significance values must be verifiable from the provided numbers.

### MINOR Revisions

These issues should be addressed to improve the quality of the manuscript.

*   **P4-m1 | Table III, p. 5 | Missing Value in Table:** In the first row of Table III (l=1 single mode), the value for `C_null` is not provided in the table itself. While it is given in the main text (Sec IV.C.b), for completeness and clarity, it should be included in the table, perhaps by renaming the `σ_null` column to `C_null` and providing values as `mean ± std`.
*   **P4-m2 | Abstract, p. 1 | Typo in Notation:** The abstract states "...471 049 high-confidence per-spiral after pow>0.9". The notation `pow` is likely a typo for `p_cw` or a similar probability/confidence metric. This should be corrected to a consistent notation used in the body of the paper.

### NIT (Cosmetic)

*   **P4-N1 | Title | Excessive Length:** The title is exceptionally long and reads like a summary of the abstract. While descriptive, it is unwieldy. The authors should consider shortening it to focus on the main result, for example: "A Null Measurement of the Galaxy Chirality Dipole at Sub-Percent Sensitivity from 3.2 Million DESI Legacy Spirals".

***

## Summary recommendation

**MAJOR REVISIONS**

The paper presents a valuable and well-executed analysis that provides a stringent null result for the galaxy chirality dipole and, crucially, a convincing explanation for prior conflicting results. The systematic analysis is thorough and of high quality. However, the manuscript is marred by several essential numerical errors and major inconsistencies in the presentation of its results. An incorrect sign on a key >9σ result, discrepancies in the training set size, and an unverifiable results table are unacceptable for a journal of PRD's caliber. While the underlying science appears sound, the paper requires a thorough and careful revision to correct these errors and improve clarity. Once these issues are addressed, the paper will likely be a strong candidate for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the report of new findings from the second, more rigorous review.

***

### NEW FINDINGS (Second Pass)

My initial review identified several critical issues. This second, more detailed pass, focusing on numerical and cross-referential integrity, has uncovered additional major and minor errors that were missed initially. These new findings reinforce the recommendation for major revisions.

### MAJOR Revisions (New)

*   **P4-M4 | Table II, p. 4 | Arithmetic Errors in Significance Calculation:** The "Dev. (σ)" column in Table II contains multiple arithmetic errors.
    *   For Catalog A (raw), the CW fraction is 0.5079 and the uncertainty is 0.000279. The deviation is (0.5079 - 0.5) / 0.000279 ≈ 28.3σ. The table reports 28.8σ, an error of ~2%.
    *   For Catalog B (calibrated), the CW fraction is 0.504 and the uncertainty is 0.000279. The deviation is (0.504 - 0.5) / 0.000279 ≈ 14.3σ. The table reports 14.6σ, an error of ~2%.
    These are significant miscalculations in a primary results table and must be corrected.

*   **P4-M5 | Table IV, p. 5 | Arithmetic Error in z-score:** The z-score for the "Pre-MASTER pseudo-C(l=1)" statistic is reported incorrectly. Given the data value (1.696e-2) and the null distribution (mean=1.685e-2, std=0.007e-2), the z-score is (1.696 - 1.685) / 0.007 ≈ +1.57. The table reports +1.68, an error of over 7%. This calculation is central to the paper's argument about the monopole-mask leakage channel, and its accuracy is paramount.

### MINOR Revisions (New)

*   **P4-m3 | Abstract & Sec IV.C, p. 1 & 4 | Inconsistent p-value and Significance:** The paper reports the real-space dipole significance as +0.43σ with a corresponding p-value of 0.30. For a Gaussian distribution, a significance of +0.43σ corresponds to a one-sided p-value of approximately 0.33. While the bootstrap distribution may not be perfectly Gaussian, this discrepancy should be clarified or corrected for precision.
*   **P4-m4 | Sec I, p. 2 | Weak Justification for Exclusion Factor:** The paper claims its result is inconsistent with Shamir's claimed ~3% signal "by a factor of ~ 6-12". However, the paper's own 3σ sensitivity threshold is 0.75%, which implies an exclusion factor of 3 / 0.75 = 4. The basis for the larger 6-12 factor is not clear from the text and should be explicitly justified or revised.
*   **P4-m5 | Sec III, p. 3 | Incorrect Internal Cross-Reference:** The text refers to "Sec. IV C" for the discussion of the "sub-percent systematic floor". The correct section discussing the global monopole offset and its interpretation as a systematic floor is Section IV.B.
*   **P4-m6 | Sec VII, p. 6 | Unsubstantiated "Largest Catalog" Claim:** The paper claims to have constructed the "largest galaxy chirality catalog to date". While plausible, this claim is not substantiated with a direct numerical comparison to other contemporary large-scale catalogs (e.g., the DESI-based catalog from Shamir 2022). A brief comparison should be added to support this claim.