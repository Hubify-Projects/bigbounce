# P2 RP2-INT-v82 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=db185208 pages=30
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (10294 chars)
**Wall time**: 153.2s

---

An official referee report for Physical Review D follows.

**Paper:** Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook
**Author:** Houston Golden
**Manuscript ID:** [Assigned by journal]

## Referee Report

This manuscript presents a detailed sensitivity forecast for testing the matter-bounce cosmological scenario using upcoming measurements of primordial non-Gaussianity from the SPHEREx survey. The paper is framed as a "sensitivity recast" of a published SPHEREx forecast by Heinrich et al. (2024), but it includes several significant original contributions: a thorough audit of the theoretical prediction `f_NL = -35/8`, including a resolution of a factor-of-two discrepancy in the literature and a novel analysis of a polynomial null-space uncertainty; a detailed calculation of the template-mismatch factor between the bounce bispectrum and the standard local template; a transparent, itemized budget for systematic uncertainties; a comprehensive Bayesian model comparison; and a new, independent Fisher forecast for the running of the non-Gaussianity parameter, `n_fNL`.

The paper is exceptionally well-researched, methodologically transparent, and rigorous in its claims. The author is careful to distinguish between established results, recast sensitivities, and heuristic projections. The clarification of the normalization conventions and the in-in commutator calculation for the bounce bispectrum (Appendix A) is a valuable service to the community. The systematic budget presented in Table IV is a model of clarity for this type of forecast paper.

While the scientific content is of high quality and suitable for publication in Physical Review D, I recommend **Major Revisions** before acceptance. The primary issues are structural and relate to the paper's framing and organization, which currently undersell its most significant original contributions and detract from its readability.

---

### ESSENTIAL Findings

None. The paper is free of critical scientific errors and the abstract accurately reflects the body's findings.

### MAJOR Findings

**P2-M1: Restructuring to Highlight Original Contributions**
*   **Section/Page:** Primarily Section IX.D (page 23), but affects the overall paper structure.
*   **Problem:** The paper's most significant piece of new, independent data analysis—the joint Fisher forecast for `(f_NL, n_fNL)` from the scale-dependent bias (SDB)—is buried deep in the Discussion section (Sec. IX.D). The abstract correctly identifies this as a key result, but its placement in the manuscript makes it seem like an afterthought. This is not a "recast" but a new calculation, and its results (e.g., the 2.0-4.6x degradation of the `f_NL` constraint due to degeneracies) are important.
*   **Required Fix:** The joint `(f_NL, n_fNL)` SDB forecast should be moved into its own dedicated section in the main body of the paper. A logical placement would be after the introduction to the SDB channel (Section III) or after the main bispectrum forecast (Section IV). This section should clearly state its distinct methodology (a new Fisher matrix calculation), its inputs (the SPHEREx low-redshift sample), and its key results. This restructuring will improve the logical flow and give this important original work the prominence it deserves.

**P2-M2: Mismatch Between Framing, Length, and Contribution**
*   **Section/Page:** Overall paper.
*   **Problem:** The paper is 30 pages long, a length typically associated with a major new theoretical calculation or a comprehensive, from-scratch analysis of a new dataset. However, the title and abstract frame the work as a "sensitivity recast of a single externally published forecast." While the paper's deep audit and supplementary analyses are extensive and valuable, this framing creates a mismatch that may confuse the reader about the paper's primary purpose and contribution.
*   **Required Fix:** The author should re-frame the paper to better align its title, abstract, and length with its key original contributions. I suggest two possible paths:
    1.  **Shorten:** Move significant portions of the detailed methodological derivations (e.g., the step-by-step null-space analysis, the detailed cross-checks of the overlap factor `r`) into appendices. The main text would then focus on presenting the results of the audit and recast, resulting in a more focused paper of ~15-18 pages, which is more appropriate for the "recast" framing.
    2.  **Re-frame:** Change the title and abstract to emphasize the original work. For example, a title like "An Audit and Systematic Analysis of the Matter Bounce `f_NL` Prediction for SPHEREx" would be more fitting. The abstract and introduction should then lead with the normalization audit, the null-space analysis, and the new SDB forecast as the primary contributions, with the bispectrum recast presented as the main application of these findings. This path seems preferable as it accurately reflects the significant effort and novelty of the work performed.

### MINOR Findings

**P2-m1: Inconsistent Symbol for Barbero-Immirzi Parameter**
*   **Section/Page:** Page 3 and Page 6.
*   **Problem:** The Barbero-Immirzi parameter is referred to as `γ_BI` on page 3 ("...the Barbero-Immirzi parameter γ_BI re-enters...") but as `BI` on page 6 ("...reactivate BI in the contracting-phase cubic action...").
*   **Required Fix:** Use a single, consistent symbol for the parameter throughout the manuscript. The standard symbol is `γ`, but `γ_BI` is acceptable for clarity if used consistently.

**P2-m2: Incorrect Formula in Table IV Caption**
*   **Section/Page:** Page 21, Table IV.
*   **Problem:** The caption for Table IV states the combination rule for quadrature addition as `(σeff = √σbase + σsyst)`. This is incorrect. The text in Section VII correctly states the rule is `σeff = √(σ_base^2 + Σ_i σ_i^2)`.
*   **Required Fix:** Correct the formula in the Table IV caption to reflect addition in quadrature, e.g., `σ_eff^2 = σ_base^2 + σ_syst^2`.

**P2-m3: Inconsistent Notation for Slow-Roll `f_NL`**
*   **Section/Page:** Throughout the paper (e.g., pages 1, 2, 12, 25).
*   **Problem:** The `f_NL` value from standard single-field slow-roll inflation is denoted variously as `f_NL^inf`, `f_NL`, and `f_NL^(inf, gauge)`.
*   **Required Fix:** Adopt a single, consistent notation for this quantity (e.g., `f_NL^SR` or `f_NL^inf`) and use it uniformly throughout the paper to avoid ambiguity.

**P2-m4: Awkward Phrasing**
*   **Section/Page:** Page 11, Column 1.
*   **Problem:** The phrase "...Liang et al. [25] methodology..." is slightly awkward.
*   **Required Fix:** Rephrase for better flow, for example: "...using the methodology of Liang et al. [25]...".

### NIT-PICKING / COSMETIC

**P2-N1: Future Date**
*   **Section/Page:** Page 1.
*   **Problem:** The paper is dated "June 30, 2026". This is a future date.
*   **Required Fix:** This is likely a placeholder and can be updated to the submission date upon revision.

**P2-N2: Typo in Computation**
*   **Section/Page:** Page 23, Section IX.D.
*   **Problem:** The word "computation" is misspelled as "compu- tation".
*   **Required Fix:** Correct the typo.

**P2-N3: ACT DR6 Birefringence Result**
*   **Section/Page:** Page 24, Section IX.E.b.
*   **Problem:** The cosmic birefringence result from ACT DR6 is quoted as a significance ("2.9σ from null"), whereas results from other experiments are given as a value with an error bar (`β = X ± Y`).
*   **Required Fix:** For consistency, please provide the measured value and uncertainty for the ACT DR6 result in addition to, or in place of, the significance.

---

## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, thorough, and valuable paper that provides a rigorous assessment of the testability of the matter-bounce scenario. Its original contributions, particularly the audit of the theoretical prediction and the new SDB forecast, are significant. However, the paper's structure and framing do not do justice to this original work, burying key results and creating a mismatch between its length and its stated scope as a "recast". Once the paper is restructured to better highlight its novel contributions, it will be an excellent and impactful addition to the literature. I recommend its publication in Physical Review D after these major revisions are addressed.

---

## PASS 2 — self-critique findings (what initial review missed)

An official referee report for Physical Review D follows.

**Paper:** Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook
**Author:** Houston Golden
**Manuscript ID:** [Assigned by journal]

## Referee Report

This manuscript presents a detailed sensitivity forecast for testing the matter-bounce cosmological scenario using upcoming measurements of primordial non-Gaussianity from the SPHEREx survey. The paper is framed as a "sensitivity recast" of a published SPHEREx forecast by Heinrich et al. (2024), but it includes several significant original contributions: a thorough audit of the theoretical prediction `f_NL = -35/8`, including a resolution of a factor-of-two discrepancy in the literature and a novel analysis of a polynomial null-space uncertainty; a detailed calculation of the template-mismatch factor between the bounce bispectrum and the standard local template; a transparent, itemized budget for systematic uncertainties; a comprehensive Bayesian model comparison; and a new, independent Fisher forecast for the running of the non-Gaussianity parameter, `n_fNL`.

The paper is exceptionally well-researched, methodologically transparent, and rigorous in its claims. The author is careful to distinguish between established results, recast sensitivities, and heuristic projections. The clarification of the normalization conventions and the in-in commutator calculation for the bounce bispectrum (Appendix A) is a valuable service to the community. The systematic budget presented in Table IV is a model of clarity for this type of forecast paper.

While the scientific content is of high quality and suitable for publication in Physical Review D, I recommend **Major Revisions** before acceptance. The primary issues are structural and relate to the paper's framing and organization, which currently undersell its most significant original contributions and detract from its readability.

---

### ESSENTIAL Findings

None. The paper is free of critical scientific errors and the abstract accurately reflects the body's findings.

### MAJOR Findings

**P2-M1: Restructuring to Highlight Original Contributions**
*   **Section/Page:** Primarily Section IX.D (page 23), but affects the overall paper structure.
*   **Problem:** The paper's most significant piece of new, independent data analysis—the joint Fisher forecast for `(f_NL, n_fNL)` from the scale-dependent bias (SDB)—is buried deep in the Discussion section (Sec. IX.D). The abstract correctly identifies this as a key result, but its placement in the manuscript makes it seem like an afterthought. This is not a "recast" but a new calculation, and its results (e.g., the 2.0-4.6x degradation of the `f_NL` constraint due to degeneracies) are important.
*   **Required Fix:** The joint `(f_NL, n_fNL)` SDB forecast should be moved into its own dedicated section in the main body of the paper. A logical placement would be after the introduction to the SDB channel (Section III) or after the main bispectrum forecast (Section IV). This section should clearly state its distinct methodology (a new Fisher matrix calculation), its inputs (the SPHEREx low-redshift sample), and its key results. This restructuring will improve the logical flow and give this important original work the prominence it deserves.

**P2-M2: Mismatch Between Framing, Length, and Contribution**
*   **Section/Page:** Overall paper.
*   **Problem:** The paper is 30 pages long, a length typically associated with a major new theoretical calculation or a comprehensive, from-scratch analysis of a new dataset. However, the title and abstract frame the work as a "sensitivity recast of a single externally published forecast." While the paper's deep audit and supplementary analyses are extensive and valuable, this framing creates a mismatch that may confuse the reader about the paper's primary purpose and contribution.
*   **Required Fix:** The author should re-frame the paper to better align its title, abstract, and length with its key original contributions. I suggest two possible paths:
    1.  **Shorten:** Move significant portions of the detailed methodological derivations (e.g., the step-by-step null-space analysis, the detailed cross-checks of the overlap factor `r`) into appendices. The main text would then focus on presenting the results of the audit and recast, resulting in a more focused paper of ~15-18 pages, which is more appropriate for the "recast" framing.
    2.  **Re-frame:** Change the title and abstract to emphasize the original work. For example, a title like "An Audit and Systematic Analysis of the Matter Bounce `f_NL` Prediction for SPHEREx" would be more fitting. The abstract and introduction should then lead with the normalization audit, the null-space analysis, and the new SDB forecast as the primary contributions, with the bispectrum recast presented as the main application of these findings. This path seems preferable as it accurately reflects the significant effort and novelty of the work performed.

---
*The following findings were identified during a second, more detailed review pass.*

**P2-M3: Dimensional Inconsistency and Ambiguity in Bispectrum Definition**
*   **Section/Page:** Page 3, Section II.A, Equations (1) and (2).
*   **Problem:** Equation (1) defines the bispectrum `A_T` in a way that is dimensionally inconsistent. The right-hand side is dimensionless, while a bispectrum `B_ζ` should have units of `(length)^6`. This likely stems from adopting a convention from the source literature (Cai et al. 2009) where amplitude factors (e.g., two powers of the power spectrum) are suppressed. This is compounded by Equation (2), which defines a dimensionless quantity `B_NL` from `A_T` in a way that is also inconsistent with `A_T` being a standard bispectrum. This lack of clarity on the foundational theoretical equations hinders reproducibility.
*   **Required Fix:** The author must clarify the definitions of `A_T` and `P`.
    1.  State explicitly the units and definition of `A_T`. Is it the full bispectrum `B_ζ`, a dimensionless shape function `S`, or another quantity?
    2.  If factors like `P_ζ(k_i)` are suppressed, this must be stated. The most transparent fix would be to write Eq. (1) in a form analogous to the standard local template, for example: `B_bounce(k1,k2,k3) = C * [P_ζ(k_ref)]^2 * S_bounce(k1,k2,k3)`, and then define the dimensionless shape `S_bounce` which contains the polynomial `P`.
    3.  The definition of `B_NL` in Eq. (2) must be made consistent with the definition of `A_T` in Eq. (1). The text should clarify that `B_NL` is the configuration-dependent amplitude, which becomes the standard `f_NL` only in the squeezed limit.

### MINOR Findings

**P2-m1: Inconsistent Symbol for Barbero-Immirzi Parameter**
*   **Section/Page:** Page 3 and Page 6.
*   **Problem:** The Barbero-Immirzi parameter is referred to as `γ_BI` on page 3 ("...the Barbero-Immirzi parameter γ_BI re-enters...") but as `BI` on page 6 ("...reactivate BI in the contracting-phase cubic action...").
*   **Required Fix:** Use a single, consistent symbol for the parameter throughout the manuscript. The standard symbol is `γ`, but `γ_BI` is acceptable for clarity if used consistently.

**P2-m2: Incorrect Formula in Table IV Caption**
*   **Section/Page:** Page 21, Table IV.
*   **Problem:** The caption for Table IV states the combination rule for quadrature addition as `(σeff = √σbase + σsyst)`. This is incorrect. The text in Section VII correctly states the rule is `σeff = √(σ_base^2 + Σ_i σ_i^2)`.
*   **Required Fix:** Correct the formula in the Table IV caption to reflect addition in quadrature, e.g., `σ_eff^2 = σ_base^2 + σ_syst^2`.

**P2-m3: Inconsistent Notation for Slow-Roll `f_NL`**
*   **Section/Page:** Throughout the paper (e.g., pages 1, 2, 12, 25).
*   **Problem:** The `f_NL` value from standard single-field slow-roll inflation is denoted variously as `f_NL^inf`, `f_NL`, and `f_NL^(inf, gauge)`.
*   **Required Fix:** Adopt a single, consistent notation for this quantity (e.g., `f_NL^SR` or `f_NL^inf`) and use it uniformly throughout the paper to avoid ambiguity.

**P2-m4: Awkward Phrasing**
*   **Section/Page:** Page 11, Column 1.
*   **Problem:** The phrase "...Liang et al. [25] methodology..." is slightly awkward.
*   **Required Fix:** Rephrase for better flow, for example: "...using the methodology of Liang et al. [25]...".

### NIT-PICKING / COSMETIC

**P2-N1: Future Date**
*   **Section/Page:** Page 1.
*   **Problem:** The paper is dated "June 30, 2026". This is a future date.
*   **Required Fix:** This is likely a placeholder and can be updated to the submission date upon revision.

**P2-N2: Typo in Computation**
*   **Section/Page:** Page 23, Section IX.D.
*   **Problem:** The word "computation" is misspelled as "compu- tation".
*   **Required Fix:** Correct the typo.

**P2-N3: ACT DR6 Birefringence Result**
*   **Section/Page:** Page 24, Section IX.E.b.
*   **Problem:** The cosmic birefringence result from ACT DR6 is quoted as a significance ("2.9σ from null"), whereas results from other experiments are given as a value with an error bar (`β = X ± Y`).
*   **Required Fix:** For consistency, please provide the measured value and uncertainty for the ACT DR6 result in addition to, or in place of, the significance.

---

## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, thorough, and valuable paper that provides a rigorous assessment of the testability of the matter-bounce scenario. Its original contributions, particularly the audit of the theoretical prediction and the new SDB forecast, are significant. However, the paper's structure and framing do not do justice to this original work, burying key results and creating a mismatch between its length and its stated scope as a "recast". Furthermore, the foundational equations for the bispectrum are presented in a dimensionally inconsistent and ambiguous manner that must be clarified. Once the paper is restructured to better highlight its novel contributions and the theoretical definitions are corrected, it will be an excellent and impactful addition to the literature. I recommend its publication in Physical Review D after these major revisions are addressed.