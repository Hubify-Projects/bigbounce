# P4 auto-2026-06-08_1144pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (11710 chars)
**Wall time**: 159.7s

---

Here is a complete referee report based on the provided paper.

---
## Referee Report: "Survey-Scale Galaxy Chirality with Equivariant TTA..."

**Manuscript ID:** [Assigned by journal]
**Title:** Survey-Scale Galaxy Chirality with Equivariant TTA: A -0.122σ Subsample-Mask l=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)
**Author:** Houston Golden

This paper presents a search for a dipole asymmetry in the chirality of 3.2 million spiral galaxies from the DESI Legacy Imaging Surveys. The primary scientific result is a null detection of a dipole, established using two independent estimators. The analysis is distinguished by its scale, its use of a bias-hardened Vision Transformer classifier, and a detailed investigation of systematic effects. A key part of the work is the identification and explanation of a statistically significant (+3.64σ) signal on a particular survey mask as an artifact arising from the coupling of a small classifier monopole bias with the mask geometry.

The methodology is rigorous, employing a pre-declared analysis hierarchy, equivariant test-time averaging to suppress biases, and an extensive suite of validation tests. The public release of the catalog, model, and analysis code is commendable. The paper provides a valuable contribution to the literature on cosmological isotropy and parity tests, and serves as an important case study on controlling systematics in large-scale survey analyses.

While the overall quality of the work is high, there are several critical issues that must be addressed before the manuscript can be considered for publication. I recommend **MAJOR REVISIONS**.

### ESSENTIAL Revisions

These issues must be resolved for the paper to be acceptable.

*   **P4-E1: Fundamental error in the parity of the observable**
    *   **Section:** VI.B, Page 6
    *   **Problem:** The text states, "The l=1 dipole observable is parity-even (isotropy-breaking axial-vector, not a direct parity-violation test); the parity-odd signal lives in the l=0 monopole and even-l multipoles." This statement is incorrect. The observable is the sky map of a pseudoscalar quantity (2D projected chirality asymmetry, `A_p = (N_CW - N_CCW) / N_total`). A dipole (`l=1`) component in a pseudoscalar field is parity-odd. A test for a dipole is a test for a preferred direction (a polar vector), which violates both isotropy and parity. An axial vector is parity-even, but a correlation of galaxy spins with a background axial vector would not produce a simple dipole in the chirality map.
    *   **Required Fix:** The authors must correct this fundamental physics error. They need to accurately describe the transformation properties of their observable. The search for an `l=1` dipole in the chirality map *is* a direct parity-violation test. The entire section VI.B must be rewritten to reflect the correct physics. This may also require adjustments to the abstract and introduction where this distinction is made.

*   **P4-E2: Inconsistent and unclear data in Table III**
    *   **Section:** IV, Page 5
    *   **Problem:** Table III, which presents the main angular power spectrum results, is critically flawed.
        1.  The column header is `C_null x 10^6 (sr)`, but for the `l=1` single mode (the headline result), the value `0.429` corresponds to `σ_null` from the text on page 4, not `C_null`. Using the numbers as presented in the table, the significance cannot be reproduced.
        2.  The relationship between the columns `C_l`, `C_null`, and `Significance` is not defined, and the significance values for `l_eff > 1` cannot be verified.
        3.  The caption states that rows 2-5 are from a "canonical-N MASTER recompute," which is different from the analysis for the first row. This makes the table a confusing mix of results from two different analyses without sufficient explanation.
    *   **Required Fix:** The table must be completely revised.
        1.  All column headers must be clearly and correctly labeled (e.g., `C_l`, `<C_l>_null`, `σ(C_l)_null`).
        2.  All values must be consistent, allowing for the re-computation of the significance for every row.
        3.  The caption and/or main text must clearly explain the analysis setup for all rows presented in the table. If two different analyses are shown, they should be clearly separated and justified.

*   **P4-E3: Future date on manuscript**
    *   **Section:** Title block, Page 1
    *   **Problem:** The paper is dated "(Dated: June 2026)".
    *   **Required Fix:** This placeholder must be replaced with the actual date of submission.

### MAJOR Revisions

These issues represent significant shortcomings that require substantial changes.

*   **P4-M1: Absence of a formal upper limit on the dipole amplitude**
    *   **Section:** VI.A, VI.B, VII (and Abstract)
    *   **Problem:** The paper claims to disfavor previous detections (e.g., Shamir ~3%) but never computes a formal upper limit on the physical dipole amplitude `A` given their null measurement. The quoted `A ≈ 0.75%` is an empirical 3σ *detection threshold* from signal injection, which is not the same as a 95% or 99% confidence level upper limit on the amplitude given the observed data. Without a proper upper limit, the comparison to previous work is qualitative and lacks statistical rigor.
    *   **Required Fix:** The authors must compute and report a frequentist or Bayesian upper limit on the dipole amplitude `A` based on their `l=1` `C_l` measurement. This upper limit should then be used for a quantitative comparison with previous claims in the literature. This is the correct way to frame the constraining power of a null result.

*   **P4-M2: Confusing and potentially misleading significance reporting**
    *   **Section:** Abstract, Page 1; Section IV.D, Page 4
    *   **Problem:** The canonical-mask residual is prominently reported as "+3.64σ" but immediately followed by the qualification "≈1.9σ Gaussian-equivalent" based on its empirical rank `p_mc = 0.030`. Reporting the much larger, non-Gaussian significance first is confusing. The physical meaning of a significance derived from a "moment-ratio" is not well-justified, whereas the empirical p-value is unambiguous.
    *   **Required Fix:** The authors should prioritize the empirical rank (`p_mc`) and its Gaussian-equivalent significance (`≈1.9σ`) when reporting this result. The `+3.64σ` value, if reported at all, must be clearly defined and justified as a useful metric, and it should not be the headline number for this diagnostic test as it could be misinterpreted as a standard Gaussian significance.

### MINOR Revisions

These issues should be addressed to improve the clarity and accuracy of the paper.

*   **P4-m1: Numerical discrepancy in Table II**
    *   **Section:** IV, Page 4
    *   **Problem:** The values in the "Dev. (σ)" column of Table II are not fully consistent with a re-computation from the `cw/(cw+ccw)` and uncertainty columns. For Catalog C, the deviation is re-calculated as -9.3σ, whereas the table lists 9.5σ.
    *   **Required Fix:** Please check the calculations for Table II and correct any inconsistencies.

*   **P4-m2: Numerical discrepancy in Table IV**
    *   **Section:** IV, Page 5
    *   **Problem:** The `z` value for the "Pre-MASTER pseudo-C(l=1)" statistic in Table IV re-computes to `z=1.57`, while the table lists `z=1.68`.
    *   **Required Fix:** Please check the calculation and correct the value in the table.

*   **P4-m3: Overly long and technical title**
    *   **Section:** Title, Page 1
    *   **Problem:** The title is exceptionally long and reads like a summary of the abstract. It is packed with technical jargon and specific numerical results that are not ideal for a title.
    *   **Required Fix:** The authors should consider a more concise and accessible title that captures the main contribution. For example: "A Null Search for a Chirality Dipole on 3.2 Million DESI Legacy Spiral Galaxies" or "A Survey-Scale Null Test of Galaxy Chirality Asymmetry with the DESI Legacy Surveys".

### NIT (Cosmetic)

*   **P4-N1: Inconsistent notation for confidence score**
    *   **Section:** Abstract and throughout
    *   **Problem:** The abstract uses `pcw` for the confidence score cut (`pcw>0.9`), while the body and appendices frequently use `p_eq` (e.g., `p_eq > 0.6` on page 5).
    *   **Required Fix:** Use consistent notation for the classifier's probability/confidence score throughout the manuscript.

## Summary recommendation

**MAJOR REVISIONS**

This paper presents a methodologically strong and important null result on galaxy chirality. The analysis is thorough, and the investigation into systematic effects is a model of good practice. However, the manuscript is marred by a fundamental error in its description of the parity of the observable, a critically flawed results table (Table III), and the omission of a formal upper limit on the dipole amplitude, which is necessary to properly contextualize the result. These issues must be fully addressed. Given the high quality of the underlying analysis, I am confident that the authors can correct these points, and I would be willing to review a revised version of the manuscript.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the second, more rigorous review, incorporating new findings.

---
## Referee Report: "Survey-Scale Galaxy Chirality with Equivariant TTA..." (Second Pass)

**Manuscript ID:** [Assigned by journal]
**Title:** Survey-Scale Galaxy Chirality with Equivariant TTA: A -0.122σ Subsample-Mask l=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)
**Author:** Houston Golden

This paper presents a search for a dipole asymmetry in the chirality of 3.2 million spiral galaxies from the DESI Legacy Imaging Surveys. The primary scientific result is a null detection of a dipole, established using two independent estimators. The analysis is distinguished by its scale, its use of a bias-hardened Vision Transformer classifier, and a detailed investigation of systematic effects. A key part of the work is the identification and explanation of a statistically significant (+3.64σ) signal on a particular survey mask as an artifact arising from the coupling of a small classifier monopole bias with the mask geometry.

The methodology is rigorous, employing a pre-declared analysis hierarchy, equivariant test-time averaging to suppress biases, and an extensive suite of validation tests. The public release of the catalog, model, and analysis code is commendable. The paper provides a valuable contribution to the literature on cosmological isotropy and parity tests, and serves as an important case study on controlling systematics in large-scale survey analyses.

While the overall quality of the work is high, there are several critical issues that must be addressed before the manuscript can be considered for publication. I recommend **MAJOR REVISIONS**.

### ESSENTIAL Revisions

These issues must be resolved for the paper to be acceptable.

*   **P4-E1: Fundamental error in the parity of the observable**
    *   **Section:** VI.B, Page 6
    *   **Problem:** The text states, "The l=1 dipole observable is parity-even (isotropy-breaking axial-vector, not a direct parity-violation test); the parity-odd signal lives in the l=0 monopole and even-l multipoles." This statement is incorrect. The observable is the sky map of a pseudoscalar quantity (2D projected chirality asymmetry, `A_p = (N_CW - N_CCW) / N_total`). A dipole (`l=1`) component in a pseudoscalar field is parity-odd. A test for a dipole is a test for a preferred direction (a polar vector), which violates both isotropy and parity. An axial vector is parity-even, but a correlation of galaxy spins with a background axial vector would not produce a simple dipole in the chirality map.
    *   **Required Fix:** The authors must correct this fundamental physics error. They need to accurately describe the transformation properties of their observable. The search for an `l=1` dipole in the chirality map *is* a direct parity-violation test. The entire section VI.B must be rewritten to reflect the correct physics. This may also require adjustments to the abstract and introduction where this distinction is made.

*   **P4-E2: Inconsistent and unclear data in Table III**
    *   **Section:** IV, Page 5
    *   **Problem:** Table III, which presents the main angular power spectrum results, is critically flawed.
        1.  The column header is `C_null x 10^6 (sr)`, but for the `l=1` single mode (the headline result), the value `0.429` corresponds to `σ_null` from the text on page 4, not `<C_l>_null`. Using the numbers as presented in the table, the significance cannot be reproduced.
        2.  The relationship between the columns `C_l`, `C_null`, and `Significance` is not defined, and the significance values for `l_eff > 1` cannot be verified as the mean of the null distribution, `<C_l>_null`, is missing.
        3.  The caption states that rows 2-5 are from a "canonical-N MASTER recompute," which is different from the analysis for the first row. This makes the table a confusing mix of results from two different analyses without sufficient explanation.
    *   **Required Fix:** The table must be completely revised.
        1.  All column headers must be clearly and correctly labeled (e.g., `C_l`, `<C_l>_null`, `σ(C_l)_null`).
        2.  All values must be consistent, allowing for the re-computation of the significance for every row.
        3.  The caption and/or main text must clearly explain the analysis setup for all rows presented in the table. If two different analyses are shown, they should be clearly separated and justified.

*   **P4-E3: Future date on manuscript**
    *   **Section:** Title block, Page 1
    *   **Problem:** The paper is dated "(Dated: June 2026)".
    *   **Required Fix:** This placeholder must be replaced with the actual date of submission.

### MAJOR Revisions

These issues represent significant shortcomings that require substantial changes.

*   **P4-M1: Absence of a formal upper limit on the dipole amplitude**
    *   **Section:** VI.A, VI.B, VII (and Abstract)
    *   **Problem:** The paper claims to disfavor previous detections (e.g., Shamir ~3%) but never computes a formal upper limit on the physical dipole amplitude `A` given their null measurement. The quoted `A ≈ 0.75%` is an empirical 3σ *detection threshold* from signal injection, which is not the same as a 95% or 99% confidence level upper limit on the amplitude given the observed data. Without a proper upper limit, the comparison to previous work is qualitative and lacks statistical rigor.
    *   **Required Fix:** The authors must compute and report a frequentist or Bayesian upper limit on the dipole amplitude `A` based on their `l=1` `C_l` measurement. This upper limit should then be used for a quantitative comparison with previous claims in the literature. This is the correct way to frame the constraining power of a null result.

*   **P4-M2: Confusing and potentially misleading significance reporting**
    *   **Section:** Abstract, Page 1; Section IV.D, Page 4
    *   **Problem:** The canonical-mask residual is prominently reported as "+3.64σ" but immediately followed by the qualification "≈1.9σ Gaussian-equivalent" based on its empirical rank `p_mc = 0.030`. Reporting the much larger, non-Gaussian significance first is confusing. The physical meaning of a significance derived from a "moment-ratio" is not well-justified, whereas the empirical p-value is unambiguous.
    *   **Required Fix:** The authors should prioritize the empirical rank (`p_mc`) and its Gaussian-equivalent significance (`≈1.9σ`) when reporting this result. The `+3.64σ` value, if reported at all, must be clearly defined and justified as a useful metric, and it should not be the headline number for this diagnostic test as it could be misinterpreted as a standard Gaussian significance.

*   **P4-M3: Inconsistent and incorrect calculation of monopole significance in Table II**
    *   **Section:** IV, Page 4
    *   **Problem:** The "Dev. (σ)" column of Table II contains multiple arithmetic errors. Re-calculation from the provided `cw/(cw+ccw)` fraction and uncertainty yields deviations of 28.3σ (vs 28.8), 14.3σ (vs 14.6), and -9.3σ (vs 9.5) for Tiers A, B, and C respectively. For Tier C, the sign is also incorrect in the table. These errors undermine confidence in the reported values for the global monopole, a key systematic discussed in the paper.
    *   **Required Fix:** The authors must re-calculate and correct all values in the "Dev. (σ)" column of Table II.

### MINOR Revisions

These issues should be addressed to improve the clarity and accuracy of the paper.

*   **P4-m1: Numerical discrepancy in Table II**
    *   *This issue was upgraded to P4-M3.*

*   **P4-m2: Numerical discrepancy in Table IV**
    *   **Section:** IV, Page 5
    *   **Problem:** The `z` value for the "Pre-MASTER pseudo-C(l=1)" statistic in Table IV re-computes to `z = (1.696 - 1.685) / 0.007 = 1.57`, while the table lists `z=1.68`.
    *   **Required Fix:** Please check the calculation and correct the value in the table.

*   **P4-m3: Overly long and technical title**
    *   **Section:** Title, Page 1
    *   **Problem:** The title is exceptionally long and reads like a summary of the abstract. It is packed with technical jargon and specific numerical results that are not ideal for a title.
    *   **Required Fix:** The authors should consider a more concise and accessible title that captures the main contribution. For example: "A Null Search for a Chirality Dipole on 3.2 Million DESI Legacy Spiral Galaxies" or "A Survey-Scale Null Test of Galaxy Chirality Asymmetry with the DESI Legacy Surveys".

*   **P4-m4: Juxtaposition of non-comparable significance values**
    *   **Section:** V.A, Page 5
    *   **Problem:** The text states that "our ... 0.43σ simple dipole is well below the 2-4σ dipoles reported by Shamir". This compares a significance value from this paper's specific null procedure (isotropic bootstrap) with significance values from a completely different analysis pipeline. This violates the paper's own excellent cautionary note on page 1 that "σ values ... are not directly comparable across estimators".
    *   **Required Fix:** Rephrase this comparison to focus on physical amplitudes rather than non-comparable σ values. This will be naturally resolved by addressing P4-M1 and computing a formal upper limit on the amplitude.

*   **P4-m5: Ambiguous definition of dipole amplitude `A`**
    *   **Section:** VI.A and Appendix D.f
    *   **Problem:** The paper uses a dipole amplitude parameter `A` for its injection tests (e.g., `A=0.75%`). It is not explicitly defined whether this `A` refers to the fractional modulation of the CW-fraction map (`f_cw`) or the asymmetry map (`A_p`). Since `A_p = 2f_cw - 1`, the amplitude of a dipole on `A_p` is approximately twice the amplitude on `f_cw`. This factor of two is critical for interpreting the sensitivity and any derived upper limits.
    *   **Required Fix:** Provide a clear, unambiguous mathematical definition of the physical dipole amplitude `A` used in the injection tests and for comparison with other works.

### NIT (Cosmetic)

*   **P4-N1: Inconsistent notation for confidence score**
    *   **Section:** Abstract and throughout
    *   **Problem:** The abstract uses `pcw` for the confidence score cut (`pcw>0.9`), while the body and appendices frequently use `p_eq` (e.g., `p_eq > 0.6` on page 5).
    *   **Required Fix:** Use consistent notation for the classifier's probability/confidence score throughout the manuscript.

*   **P4-N2: Potential typo in contact email**
    *   **Section:** Page 1, footnote
    *   **Problem:** The contact email `houston@hubify.com` appears to belong to a marketing agency, which is unusual for a scientific publication.
    *   **Required Fix:** Please verify that the contact email address is correct.

## Summary recommendation

**MAJOR REVISIONS**

This paper presents a methodologically strong and important null result on galaxy chirality. The analysis is thorough, and the investigation into systematic effects is a model of good practice. However, the manuscript is marred by a fundamental error in its description of the parity of the observable, a critically flawed results table (Table III), and the omission of a formal upper limit on the dipole amplitude, which is necessary to properly contextualize the result. Additional arithmetic errors in other tables further reduce confidence. These issues must be fully addressed. Given the high quality of the underlying analysis, I am confident that the authors can correct these points, and I would be willing to review a revised version of the manuscript.