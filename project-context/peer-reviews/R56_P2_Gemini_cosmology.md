# P2 R56 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R56_P2/02_full_draft.pdf` md5=592c7849 pages=28
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (8093 chars)
**Wall time**: 185.4s

---

## Referee Report for "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"

This paper presents a detailed sensitivity forecast for testing the matter bounce cosmological scenario using upcoming measurements of primordial non-Gaussianity (PNG) from the SPHEREx survey, with an outlook towards the proposed MegaMapper experiment. The primary observable is the local-type non-Gaussianity parameter, `f_NL`, for which the quasi-dust matter bounce model predicts a specific value of `f_NL = -35/8`. The paper recasts existing SPHEREx forecasts for the galaxy bispectrum, performs a comprehensive analysis of systematic effects, and conducts a Bayesian model comparison to quantify the discriminating power against inflationary alternatives. A notable contribution is the resolution of a factor-of-two discrepancy in the literature regarding the predicted `f_NL` value.

The paper is well-structured, thorough, and transparent about its assumptions and limitations. The analysis is detailed, with many valuable internal consistency checks. The provision of code and data artifacts for reproducibility is commendable. The paper is a strong candidate for publication in Physical Review D, pending revision to address the following points.

---
### ESSENTIAL Revisions

**P2-E1**
*   **Section/Page**: Sec. II.A, p. 3
*   **Problem**: The definitions of the bispectrum amplitude `A_T` (Eq. 1) and the nonlinearity parameter `B_NL` (Eq. 2) are dimensionally inconsistent.
    *   The text states that `P` is a degree-9 homogeneous polynomial in wavenumbers `k`.
    *   Eq. (1) defines `A_T = (3 / (256 k_1^3 k_2^3 k_3^3)) * P(k_1, k_2, k_3)`. Since `(k_1 k_2 k_3)^3` is degree 9, this makes `A_T` dimensionless.
    *   Eq. (2) defines `B_NL = (10 A_T) / (3 Σk_i^3)`. Since `Σk_i^3` has dimensions of `[wavenumber]^3`, this gives `B_NL` dimensions of `[wavenumber]^-3`.
    *   However, the text explicitly states "BNL is dimensionless by construction". This is a direct contradiction. The quantity `f_NL` is by convention dimensionless. This inconsistency undermines the fundamental theoretical setup of the paper's central observable. While the numerical results presented in Table I and Figure 1 appear to be correct (suggesting the code uses the correct physics, likely taken from the cited Cai et al. paper), the analytic expressions presented are incorrect.
*   **Required Fix**: The author must revise the definitions in Section II.A to be dimensionally correct and consistent with the standard definitions in the literature (e.g., Cai et al. 2009). The text describing the dimensional analysis ("the prefactor of Eq. (1) removes degree 6...") must also be corrected to reflect the revised, correct equations. This is essential for the logical and theoretical integrity of the paper.

---
### MINOR Revisions

**P2-m1**
*   **Section/Page**: p. 1
*   **Problem**: The paper is dated "June 26, 2026". This is unconventional for a manuscript under review and appears to be a placeholder. It also creates a slightly confusing timeline, as the text refers to the SPHEREx launch (March 2025) as a past event.
*   **Required Fix**: The date should be updated to the current submission date or removed as per journal style.

---
### NIT (Cosmetic)

**P2-N1**
*   **Section/Page**: p. 2 (footnote)
*   **Problem**: The contact email address `houston@hubify.com` appears to be non-standard for an academic publication and may be a placeholder.
*   **Required Fix**: The author should verify that this is the intended permanent contact address.

---
### Overall Assessment

The paper's strengths are numerous:
*   **Thoroughness**: The systematic budget is comprehensive, including template mismatch, polynomial basis uncertainty, `ε`-corrections, photometric redshift degradation, PNG bias uncertainty, and GR projection effects.
*   **Transparency**: The author is commendably clear about all assumptions, particularly the crucial unverified assumption of faithful third-order bispectrum transmission through the bounce. The use of a parameterized GR degradation and the discussion of its limitations is honest and appropriate for a forecast.
*   **Reproducibility**: The provision of analysis scripts and named data artifacts is a model of open science and greatly increases confidence in the results. The inclusion of a "worked example" for the Bayes factor calculation is particularly helpful.
*   **Contribution**: The resolution of the factor-of-two discrepancy between the Cai et al. and Li et al. predictions for `f_NL` in Appendix A is a valuable service to the community, clarifying the physical prediction. The symbolic verification of the in-in commutator identity provides a rigorous foundation for this conclusion.
*   **Clarity**: Despite the density of the material, the paper is generally well-written. The summary tables (e.g., Table IV for systematics) and figures are effective at communicating the key results.

The single essential revision concerning the dimensional inconsistency in the bispectrum definition is critical but should be straightforward to fix. Once this is addressed, the paper will represent a robust and valuable contribution to the literature on primordial cosmology. It provides a clear and well-supported target for upcoming observational programs and a compelling science case for the galaxy bispectrum as a probe of the pre-big-bang universe.

## Summary recommendation
**MAJOR REVISIONS**

The paper requires a major revision to correct the essential flaw in the theoretical definitions in Section II.A. Although this is the only major issue, its fundamental nature (a dimensional inconsistency in the definition of the main observable) precludes a more favorable recommendation at this stage. However, the overall quality of the analysis is very high, and I am confident that the author can address this point. Upon successful correction of this issue, the paper will be suitable for publication in Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated referee report, incorporating findings from a more rigorous second pass.

================================================================
## Referee Report for "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"

This paper presents a detailed sensitivity forecast for testing the matter bounce cosmological scenario using upcoming measurements of primordial non-Gaussianity (PNG) from the SPHEREx survey, with an outlook towards the proposed MegaMapper experiment. The primary observable is the local-type non-Gaussianity parameter, `f_NL`, for which the quasi-dust matter bounce model predicts a specific value of `f_NL = -35/8`. The paper recasts existing SPHEREx forecasts for the galaxy bispectrum, performs a comprehensive analysis of systematic effects, and conducts a Bayesian model comparison to quantify the discriminating power against inflationary alternatives. A notable contribution is the resolution of a factor-of-two discrepancy in the literature regarding the predicted `f_NL` value.

The paper is well-structured, thorough, and transparent about its assumptions and limitations. The analysis is detailed, with many valuable internal consistency checks. The provision of code and data artifacts for reproducibility is commendable. The paper is a strong candidate for publication in Physical Review D, pending revision to address the following points.

---
### ESSENTIAL Revisions

**P2-E1**
*   **Section/Page**: Sec. II.A, p. 3
*   **Problem**: The definitions of the bispectrum amplitude `A_T` (Eq. 1) and the nonlinearity parameter `B_NL` (Eq. 2) are dimensionally inconsistent.
    *   The text states that `P` is a degree-9 homogeneous polynomial in wavenumbers `k`.
    *   Eq. (1) defines `A_T = (3 / (256 k_1^3 k_2^3 k_3^3)) * P(k_1, k_2, k_3)`. Since `(k_1 k_2 k_3)^3` is degree 9, this makes `A_T` dimensionless.
    *   Eq. (2) defines `B_NL = (10 A_T) / (3 Σk_i^3)`. Since `Σk_i^3` has dimensions of `[wavenumber]^3`, this gives `B_NL` dimensions of `[wavenumber]^-3`.
    *   However, the text explicitly states "BNL is dimensionless by construction". This is a direct contradiction. The quantity `f_NL` is by convention dimensionless. This inconsistency undermines the fundamental theoretical setup of the paper's central observable. While the numerical results presented in Table I and Figure 1 appear to be correct (suggesting the code uses the correct physics, likely taken from the cited Cai et al. paper), the analytic expressions presented are incorrect.
*   **Required Fix**: The author must revise the definitions in Section II.A to be dimensionally correct and consistent with the standard definitions in the literature (e.g., Cai et al. 2009). The text describing the dimensional analysis ("the prefactor of Eq. (1) removes degree 6...") must also be corrected to reflect the revised, correct equations. This is essential for the logical and theoretical integrity of the paper.

**P2-E2**
*   **Section/Page**: Main text (p.1) vs. Appendix A (p.24)
*   **Problem**: The paper uses inconsistent definitions for the local-type bispectrum.
    *   The abstract and main text (p. 1) correctly state the standard definition: `B_local(k1,k2, k3) = (6f_NL^local/5)[P_s(k1)P_s(k2) + 2 perms]`.
    *   Appendix A, which is crucial for the paper's normalization audit, uses a different, non-standard definition in Eq. (A1): `B_Φ(k1,k2, k3) = c * f_NL [P_Φ(k1)P_Φ(k2) + 2 perms]`, with a convention of `c=2`.
    *   The appendix attempts to reconcile these forms via a non-standard relation between the Bardeen potential `Φ` and the curvature perturbation `ζ`. This is confusing and obscures the core argument. Using inconsistent fundamental definitions in different parts of the paper undermines the rigor of the normalization audit, which is a key contribution.
*   **Required Fix**: The author must use a single, standard, and dimensionally correct definition for the bispectrum throughout the entire manuscript. The arguments in Appendix A should be re-phrased in terms of this single convention to ensure clarity and consistency.

---
### MINOR Revisions

**P2-m1**
*   **Section/Page**: p. 1
*   **Problem**: The paper is dated "June 26, 2026". This is unconventional for a manuscript under review and appears to be a placeholder. It also creates a slightly confusing timeline, as the text refers to the SPHEREx launch (March 2025) as a past event.
*   **Required Fix**: The date should be updated to the current submission date or removed as per journal style.

**P2-m2**
*   **Section/Page**: Sec. V, p. 11
*   **Problem**: The calculation of the MegaMapper conservative significance ("~3.2σ conservative") appears to use a rule for combining systematic errors that is inconsistent with the methodology used elsewhere in the paper. The text describes a calculation `~√[σ_base^2 + σ_syst^2]`, but the main systematics budget in Table IV indicates that the `b_φ` uncertainty *replaces* the baseline uncertainty `σ_base`, not adds to it in quadrature.
*   **Required Fix**: The author should make the systematic error combination for the MegaMapper forecast consistent with the methodology established in Table IV and used for the SPHEREx forecast, and update the resulting significance value.

---
### NIT (Cosmetic)

**P2-N1**
*   **Section/Page**: p. 2 (footnote)
*   **Problem**: The contact email address `houston@hubify.com` appears to be non-standard for an academic publication and may be a placeholder.
*   **Required Fix**: The author should verify that this is the intended permanent contact address.

---
### Overall Assessment

The paper's strengths are numerous:
*   **Thoroughness**: The systematic budget is comprehensive, including template mismatch, polynomial basis uncertainty, `ε`-corrections, photometric redshift degradation, PNG bias uncertainty, and GR projection effects.
*   **Transparency**: The author is commendably clear about all assumptions, particularly the crucial unverified assumption of faithful third-order bispectrum transmission through the bounce. The use of a parameterized GR degradation and the discussion of its limitations is honest and appropriate for a forecast.
*   **Reproducibility**: The provision of analysis scripts and named data artifacts is a model of open science and greatly increases confidence in the results. The inclusion of a "worked example" for the Bayes factor calculation is particularly helpful.
*   **Contribution**: The resolution of the factor-of-two discrepancy between the Cai et al. and Li et al. predictions for `f_NL` in Appendix A is a valuable service to the community, clarifying the physical prediction. The symbolic verification of the in-in commutator identity provides a rigorous foundation for this conclusion.
*   **Clarity**: Despite the density of the material, the paper is generally well-written. The summary tables (e.g., Table IV for systematics) and figures are effective at communicating the key results.

The essential revisions concerning the dimensional and conventional inconsistencies in the bispectrum definition are critical and must be fixed. Once these are addressed, the paper will represent a robust and valuable contribution to the literature on primordial cosmology. It provides a clear and well-supported target for upcoming observational programs and a compelling science case for the galaxy bispectrum as a probe of the pre-big-bang universe.

## Summary recommendation
**MAJOR REVISIONS**

The paper requires a major revision to correct the essential flaws in the theoretical definitions in Section II.A and Appendix A. Although the core analysis appears sound, its fundamental nature (dimensional and conventional inconsistencies in the definition of the main observable) precludes a more favorable recommendation at this stage. However, the overall quality of the analysis is very high, and I am confident that the author can address these points. Upon successful correction of these issues, the paper will be suitable for publication in Physical Review D.