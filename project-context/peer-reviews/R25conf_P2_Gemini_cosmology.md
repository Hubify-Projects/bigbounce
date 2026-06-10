# P2 R25conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.47.pdf` md5=a6ea2ee9 pages=24
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (17376 chars)
**Wall time**: 185.0s

---

**Referee Report on "Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREX Forecasts, with a MegaMapper Outlook" by Houston Golden**

**Manuscript ID:** [Internal ID]
**Journal:** Physical Review D

This paper presents a detailed forecast for testing the matter-bounce cosmological scenario using measurements of primordial non-Gaussianity from the upcoming SPHEREx survey, with an outlook for the proposed MegaMapper survey. The central prediction of the matter-bounce model is a local-type non-Gaussianity parameter f_NL = -35/8. The author performs a comprehensive analysis, including a re-evaluation of the theoretical prediction, a quantification of the template mismatch with the standard local shape, a systematic budget for observational effects, and a Bayesian model comparison against inflationary alternatives. The paper also provides a critical clarification of a factor-of-two discrepancy in the theoretical literature regarding the predicted f_NL value.

The work is thorough, computationally detailed, and addresses a well-motivated question in fundamental cosmology. The analysis is of high quality, and the author demonstrates a strong command of both the theoretical underpinnings and the observational realities of large-scale structure surveys. The clarification of the Cai et al. vs. Li et al. normalization issue in Appendix A is particularly valuable and essential for the field. However, the paper's length and density, along with several points requiring clarification and correction, necessitate significant revisions before it can be considered for publication in Physical Review D.

---
### **Detailed Findings**

#### **ESSENTIAL**

*   **P2-E1:** **Section IX.D (p. 18), Joint (f_NL, n_fNL) Forecast.** The paper presents two distinct Fisher forecasts: (i) the headline bispectrum-only forecast from Heinrich et al. [4] (σ(f_NL) ≈ 0.7), and (ii) a separate, newly computed joint (f_NL, n_fNL) forecast using scale-dependent bias (SDB) over a different redshift range. The text correctly distinguishes them, but the juxtaposition is confusing and potentially misleading. The SDB-only marginalized constraint σ_marg(f_NL) = 3.08 (or 7.06 with bias marginalization) is much weaker than the bispectrum-only constraint. The abstract and introduction should more clearly state that the headline 3-5σ result is *bispectrum-only* and that the joint (f_NL, n_fNL) analysis from SDB is a separate, sub-dominant channel used only to constrain the running, not to improve the f_NL constraint itself.
    *   **Problem:** The paper's main results are based on the bispectrum, but a significant portion of the discussion is dedicated to a much weaker SDB-based forecast for n_fNL. This could lead readers to incorrectly conflate the two analyses or their respective sensitivities. The abstract does not mention the (f_NL, n_fNL) forecast at all, which is good, but the main text needs to better frame its secondary role.
    *   **Required Fix:** Restructure Section IX.D. State upfront that the SDB channel is significantly less sensitive for f_NL itself compared to the bispectrum channel, as evidenced by comparing σ_unmarg(f_NL) = 1.53 (SDB) with σ(f_NL) = 0.7 (bispectrum). Frame the section as a forecast for the *running* (n_fNL) using the SDB channel, and explicitly state that this channel provides a poor constraint on f_NL itself. Remove any language that could imply the SDB analysis is a competitor to the bispectrum analysis for measuring f_NL.

*   **P2-E2:** **Section VI.C (p. 10), Bayesian Comparison Priors.** The paper's headline Bayes factor (BF ~ 10-17) depends critically on the choice of priors for the inflationary competitor model. The text explores a "broad multifield" prior of [-15, +15] and a "curvaton-natural" prior of [-5, +5]. While the exploration is good, the abstract and main conclusions heavily promote the BF ~ 10-17 range derived from the broad prior. This specific choice, while defensible as an envelope, is not uniquely motivated and has a large impact on the result. A BF > 10 is typically considered "strong" evidence, and the distinction between BF=4 and BF=17 is significant.
    *   **Problem:** The abstract states "Bayes factor BF ≈ 10 ... up to BF ≈ 17", and the headline envelope is "BF ~ 10-17". This gives undue prominence to the result from the widest, most generous prior, which maximizes the "discovery" potential. The more physically motivated curvaton prior gives a much more modest BF ~ 4-7.
    *   **Required Fix:** The abstract and conclusion must be rephrased to lead with the result from the more physically motivated "curvaton-natural" [-5, +5] prior (BF ~ 4-7). The BF ~ 10-17 result from the broader [-15, +15] prior should be presented as an upper limit under a specific, less-motivated prior choice. This provides a more conservative and intellectually honest summary of the results. Table II should be re-ordered or annotated to clearly identify the "recommended" or "physically motivated" prior scenario.

#### **MAJOR**

*   **P2-M1:** **Paper Length and Structure.** At 24 pages, the paper is excessively long for a forecast study. The narrative flow is frequently interrupted by detailed asides, parenthetical qualifications, and forward/backward references. Significant portions of the detailed numerical analysis and systematic discussions could be moved to appendices to improve the readability of the main text.
    *   **Problem:** The core results—the significance of a SPHEREx detection and the Bayesian comparison—are diluted by the sheer volume of text. Key sections like the systematic budget (Sec. VII) and the Bayesian analysis (Sec. VI) are dense and difficult to parse.
    *   **Required Fix:** Restructure the paper.
        1.  The main text should be streamlined to focus on the primary results: the f_NL = -35/8 prediction, the template mismatch `r`, the application to the SPHEREx forecast to get the headline significance, the main Bayesian result (with the re-prioritized priors from P2-E2), and the conclusion. Recommended length for the main text: 10-12 pages.
        2.  Move the detailed derivation of the polynomial underdetermination (part of Sec. II.A), the full discussion of all 10 noise-weighting schemes (part of Sec. III.B), the detailed breakdown of the GR-degradation scenarios (part of Sec. VII.C), and the full joint (f_NL, n_fNL) SDB analysis (Sec. IX.D) to appendices.
        3.  Appendix A on the normalization convention is excellent and should remain as is.

*   **P2-M2:** **Section VII (p. 13), Systematic Budget.** The paper constructs a systematic budget that takes the optimistic 5.2-5.5σ significance and degrades it to a "realistic range" of ~3-5σ. While the individual systematic effects discussed are valid (GR effects, b_φ uncertainty, photo-z errors, etc.), the method of combining them and arriving at the final range is not transparently derived. The abstract claims this is a "combined systematic budget," but the text seems to discuss them mostly in isolation.
    *   **Problem:** The final 3-5σ range is a key result of the paper, but its derivation is qualitative. How are the various percentage degradations combined? Are they added in quadrature? Are correlations accounted for? The paper needs to provide a clear, quantitative path from 5.5σ to the final range.
    *   **Required Fix:** In Section VII, provide a summary table or a clear formula showing how the final systematic degradation is calculated. For example: σ_final = σ_initial × (1 - frac_degrade_GR) × (1 - frac_degrade_bφ) × ... or similar. Justify the combination method (e.g., assuming independent effects). This will make the final headline number much more robust and reproducible.

*   **P2-M3:** **Section II.A (p. 3), Polynomial Underdetermination.** The paper claims that the 6-coefficient polynomial `P` is underdetermined by the 3 published benchmark constraints from Cai et al. This leads to a 3D null space and a ±0.13 scatter in the recovery factor `r`, which is a ~15% systematic uncertainty. This is a significant new claim about a foundational paper. The footnote on page 3 explains that the coefficients in Cai et al. are in a different basis, but the argument needs to be made more explicit in the main text.
    *   **Problem:** The claim of underdetermination is a strong one and is presented as a core part of the theoretical uncertainty. However, the text is slightly ambiguous about whether this is a genuine physical ambiguity or an artifact of the author's choice of a symmetric monomial basis to represent a result originally derived in a single-time-ordering formalism. The sentence "The three-constraint vs. six-coefficient mismatch arises specifically when we recompile the doubled polynomial into our symmetrized monomial basis" is key and should be in the main text.
    *   **Required Fix:** Elevate the core of the argument from the footnote and the "Important scope" paragraph into the main text of Sec. II.A. State clearly that the underdetermination arises in the author's specific, well-motivated symmetrized basis when fitting to the published benchmark values, and that the original derivation in Cai et al. did not encounter this. This clarifies the origin of the uncertainty and properly scopes the claim.

#### **MINOR**

*   **P2-m1:** **Section I (p. 2), Bounce vs. Inflation Contrast.** The abstract and introduction quote the gauge-frame contrast |f_NL^bounce|/|f_NL^inf| ≈ 290. The text also mentions the conformal-Fermi physical-frame, where f_NL^inf -> 0, making the contrast formally larger. While the paper correctly states that the gauge-frame value is the relevant one for the survey estimators, the discussion of the physical frame could be confusing.
    *   **Problem:** The dual-frame discussion adds complexity without adding to the forecast. The key point is that in the frame relevant to the measurement, the contrast is large.
    *   **Required Fix:** Shorten the discussion of the conformal-Fermi frame. State that the conventional gauge frame is used by the estimators, the contrast in this frame is ~290, and that other frames exist but are not relevant to the forecast methodology. This keeps the focus on the observable quantity.

*   **P2-m2:** **Figure 2 (p. 9), Caption.** The caption describes the error bars as spanning from the "optimistic endpoint" to the "conservative endpoint". It then lists the components of the full §VII budget. This is good, but it would be clearer to explicitly state what is included in "optimistic" (e.g., template overlap only) vs. "conservative" (e.g., overlap + GR + b_φ + photo-z).
    *   **Problem:** The definition of the error bar endpoints is slightly vague in the caption itself.
    *   **Required Fix:** Revise the caption to be more explicit. E.g., "Error bars span from an optimistic case (including only the template-mismatch correction, r=0.84-0.88) to a conservative case (including the full systematic budget of §VII: template mismatch, e-correction, photometric-z degradation, and marginalization over GR effects and PNG bias b_φ)."

*   **P2-m3:** **Table III (p. 15), Correction Note.** The table includes a correction note: "[Correction note: an earlier version of this table quoted BF values... they are replaced here by the fully documented closed-form computation.]" While transparency is commendable, such version-history notes are not appropriate for a final publication. The same applies to the correction notes in Sec. IX.D (p. 18) and Sec. VI.b (p. 13).
    *   **Problem:** Internal versioning or correction history does not belong in the published article.
    *   **Required Fix:** Remove all such "Correction note" blocks from the manuscript. The final version should simply present the correct, validated numbers.

*   **P2-m4:** **Throughout, Date of Paper.** The date is listed as "(Dated: June 10, 2026)". While arXiv pre-prints can have future dates for release coordination, this is highly unconventional for a journal submission.
    *   **Problem:** The future date is unusual and could be a typo.
    *   **Required Fix:** Change the date to the current date of submission.

#### **NIT**

*   **P2-N1:** **Section II.A (p. 3), Footnote 1.** The footnote refers to an artifact `c9i_epsilon_ratio_check.json`. While the availability of code is excellent, referencing specific filenames from the code repository in the text is unconventional.
    *   **Problem:** Filenames can change, and it makes the text less self-contained.
    *   **Required Fix:** Rephrase to describe the check without naming the file. E.g., "Our numerical checks, included in the supplementary materials, confirm that a direct evaluation..."

*   **P2-N2:** **Section VI.C (p. 10), Realization Count.** The text states "10^5 realizations each (3 × 10^5 aggregate)". The parenthetical is redundant.
    *   **Problem:** Minor redundancy.
    *   **Required Fix:** Simplify to "three independent Monte Carlo ensembles of 10^5 realizations each."

---
### **Summary recommendation**

**MAJOR REVISIONS**

This is a very strong, comprehensive, and valuable paper. The author's careful work, especially in clarifying the theoretical prediction in Appendix A and quantifying the template mismatch, is a significant contribution. The paper is well-suited for publication in Physical Review D after the issues identified above are addressed.

The recommendation for **MAJOR REVISIONS** is driven by three key requirements:
1.  **Clarity and Focus:** The paper must be substantially shortened and restructured (P2-M1) to present its important findings more clearly and concisely. The main narrative should not be encumbered by excessive detail that can be moved to appendices.
2.  **Rigor in Interpretation:** The presentation of the Bayesian results must be revised to lead with the more conservative, physically motivated priors (P2-E2), ensuring the headline claims are not inflated. The derivation of the final systematic budget must be made quantitative and transparent (P2-M2).
3.  **Scoping of Forecasts:** The distinction between the primary bispectrum forecast and the secondary SDB forecast for the running must be sharpened to avoid any potential for confusion (P2-E1).

Addressing these points will elevate the manuscript to the high standards of the journal and ensure its significant contributions are communicated effectively to the community. I look forward to reviewing a revised version of this manuscript.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated referee report, incorporating the findings from the "fresh eyes" review. New findings are added to the end of each section.

================================================================
**Referee Report on "Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREX Forecasts, with a MegaMapper Outlook" by Houston Golden**

**Manuscript ID:** [Internal ID]
**Journal:** Physical Review D

This paper presents a detailed forecast for testing the matter-bounce cosmological scenario using measurements of primordial non-Gaussianity from the upcoming SPHEREx survey, with an outlook for the proposed MegaMapper survey. The central prediction of the matter-bounce model is a local-type non-Gaussianity parameter f_NL = -35/8. The author performs a comprehensive analysis, including a re-evaluation of the theoretical prediction, a quantification of the template mismatch with the standard local shape, a systematic budget for observational effects, and a Bayesian model comparison against inflationary alternatives. The paper also provides a critical clarification of a factor-of-two discrepancy in the theoretical literature regarding the predicted f_NL value.

The work is thorough, computationally detailed, and addresses a well-motivated question in fundamental cosmology. The analysis is of high quality, and the author demonstrates a strong command of both the theoretical underpinnings and the observational realities of large-scale structure surveys. The clarification of the Cai et al. vs. Li et al. normalization issue in Appendix A is particularly valuable and essential for the field. However, the paper's length and density, along with several points requiring clarification and correction, necessitate significant revisions before it can be considered for publication in Physical Review D.

---
### **Detailed Findings**

#### **ESSENTIAL**

*   **P2-E1:** **Section IX.D (p. 18), Joint (f_NL, n_fNL) Forecast.** The paper presents two distinct Fisher forecasts: (i) the headline bispectrum-only forecast from Heinrich et al. [4] (σ(f_NL) ≈ 0.7), and (ii) a separate, newly computed joint (f_NL, n_fNL) forecast using scale-dependent bias (SDB) over a different redshift range. The text correctly distinguishes them, but the juxtaposition is confusing and potentially misleading. The SDB-only marginalized constraint σ_marg(f_NL) = 3.08 (or 7.06 with bias marginalization) is much weaker than the bispectrum-only constraint. The abstract and introduction should more clearly state that the headline 3-5σ result is *bispectrum-only* and that the joint (f_NL, n_fNL) analysis from SDB is a separate, sub-dominant channel used only to constrain the running, not to improve the f_NL constraint itself.
    *   **Problem:** The paper's main results are based on the bispectrum, but a significant portion of the discussion is dedicated to a much weaker SDB-based forecast for n_fNL. This could lead readers to incorrectly conflate the two analyses or their respective sensitivities. The abstract does not mention the (f_NL, n_fNL) forecast at all, which is good, but the main text needs to better frame its secondary role.
    *   **Required Fix:** Restructure Section IX.D. State upfront that the SDB channel is significantly less sensitive for f_NL itself compared to the bispectrum channel, as evidenced by comparing σ_unmarg(f_NL) = 1.53 (SDB) with σ(f_NL) = 0.7 (bispectrum). Frame the section as a forecast for the *running* (n_fNL) using the SDB channel, and explicitly state that this channel provides a poor constraint on f_NL itself. Remove any language that could imply the SDB analysis is a competitor to the bispectrum analysis for measuring f_NL.

*   **P2-E2:** **Section VI.C (p. 10), Bayesian Comparison Priors.** The paper's headline Bayes factor (BF ~ 10-17) depends critically on the choice of priors for the inflationary competitor model. The text explores a "broad multifield" prior of [-15, +15] and a "curvaton-natural" prior of [-5, +5]. While the exploration is good, the abstract and main conclusions heavily promote the BF ~ 10-17 range derived from the broad prior. This specific choice, while defensible as an envelope, is not uniquely motivated and has a large impact on the result. A BF > 10 is typically considered "strong" evidence, and the distinction between BF=4 and BF=17 is significant.
    *   **Problem:** The abstract states "Bayes factor BF ≈ 10 ... up to BF ≈ 17", and the headline envelope is "BF ~ 10-17". This gives undue prominence to the result from the widest, most generous prior, which maximizes the "discovery" potential. The more physically motivated curvaton prior gives a much more modest BF ~ 4-7.
    *   **Required Fix:** The abstract and conclusion must be rephrased to lead with the result from the more physically motivated "curvaton-natural" [-5, +5] prior (BF ~ 4-7). The BF ~ 10-17 result from the broader [-15, +15] prior should be presented as an upper limit under a specific, less-motivated prior choice. This provides a more conservative and intellectually honest summary of the results. Table II should be re-ordered or annotated to clearly identify the "recommended" or "physically motivated" prior scenario.

*   **P2-E3 (NEW):** **Section II.A (p. 3), Dimensional Inconsistency in Core Prediction Definition.** Equations (1) and (2), which define the central quantity `B_NL` that is identified with `f_NL`, are dimensionally inconsistent. As written, `A_T` in Eq. (1) is dimensionless (a degree-9 polynomial in `k` divided by `k^9`), while the denominator `Σk_i^3` in Eq. (2) has units of `(wavenumber)^3`. This makes the resulting `B_NL` have units of `(wavenumber)^-3`, which contradicts its identification with the dimensionless parameter `f_NL`.
    *   **Problem:** This is a fundamental error in the presentation of the model's core prediction. The equations that form the basis of the entire analysis are not physically correct as written.
    *   **Required Fix:** The author must correct Equations (1) and (2) and the surrounding descriptive text to be dimensionally consistent. This will likely involve revisiting the original definitions in Cai et al. [8] and correctly defining a dimensionless shape function that can be identified with `f_NL` in the squeezed limit. This correction is essential for the physical and mathematical validity of the paper.

#### **MAJOR**

*   **P2-M1:** **Paper Length and Structure.** At 24 pages, the paper is excessively long for a forecast study. The narrative flow is frequently interrupted by detailed asides, parenthetical qualifications, and forward/backward references. Significant portions of the detailed numerical analysis and systematic discussions could be moved to appendices to improve the readability of the main text.
    *   **Problem:** The core results—the significance of a SPHEREx detection and the Bayesian comparison—are diluted by the sheer volume of text. Key sections like the systematic budget (Sec. VII) and the Bayesian analysis (Sec. VI) are dense and difficult to parse.
    *   **Required Fix:** Restructure the paper.
        1.  The main text should be streamlined to focus on the primary results: the f_NL = -35/8 prediction, the template mismatch `r`, the application to the SPHEREx forecast to get the headline significance, the main Bayesian result (with the re-prioritized priors from P2-E2), and the conclusion. Recommended length for the main text: 10-12 pages.
        2.  Move the detailed derivation of the polynomial underdetermination (part of Sec. II.A), the full discussion of all 10 noise-weighting schemes (part of Sec. III.B), the detailed breakdown of the GR-degradation scenarios (part of Sec. VII.C), and the full joint (f_NL, n_fNL) SDB analysis (Sec. IX.D) to appendices.
        3.  Appendix A on the normalization convention is excellent and should remain as is.

*   **P2-M2:** **Section VII (p. 13), Systematic Budget.** The paper constructs a systematic budget that takes the optimistic 5.2-5.5σ significance and degrades it to a "realistic range" of ~3-5σ. While the individual systematic effects discussed are valid (GR effects, b_φ uncertainty, photo-z errors, etc.), the method of combining them and arriving at the final range is not transparently derived. The abstract claims this is a "combined systematic budget," but the text seems to discuss them mostly in isolation.
    *   **Problem:** The final 3-5σ range is a key result of the paper, but its derivation is qualitative. How are the various percentage degradations combined? Are they added in quadrature? Are correlations accounted for? The paper needs to provide a clear, quantitative path from 5.5σ to the final range.
    *   **Required Fix:** In Section VII, provide a summary table or a clear formula showing how the final systematic degradation is calculated. For example: σ_final = σ_initial × (1 - frac_degrade_GR) × (1 - frac_degrade_bφ) × ... or similar. Justify the combination method (e.g., assuming independent effects). This will make the final headline number much more robust and reproducible.

*   **P2-M3:** **Section II.A (p. 3), Polynomial Underdetermination.** The paper claims that the 6-coefficient polynomial `P` is underdetermined by the 3 published benchmark constraints from Cai et al. This leads to a 3D null space and a ±0.13 scatter in the recovery factor `r`, which is a ~15% systematic uncertainty. This is a significant new claim about a foundational paper. The footnote on page 3 explains that the coefficients in Cai et al. are in a different basis, but the argument needs to be made more explicit in the main text.
    *   **Problem:** The claim of underdetermination is a strong one and is presented as a core part of the theoretical uncertainty. However, the text is slightly ambiguous about whether this is a genuine physical ambiguity or an artifact of the author's choice of a symmetric monomial basis to represent a result originally derived in a single-time-ordering formalism. The sentence "The three-constraint vs. six-coefficient mismatch arises specifically when we recompile the doubled polynomial into our symmetrized monomial basis" is key and should be in the main text.
    *   **Required Fix:** Elevate the core of the argument from the footnote and the "Important scope" paragraph into the main text of Sec. II.A. State clearly that the underdetermination arises in the author's specific, well-motivated symmetrized basis when fitting to the published benchmark values, and that the original derivation in Cai et al. did not encounter this. This clarifies the origin of the uncertainty and properly scopes the claim.

#### **MINOR**

*   **P2-m1:** **Section I (p. 2), Bounce vs. Inflation Contrast.** The abstract and introduction quote the gauge-frame contrast |f_NL^bounce|/|f_NL^inf| ≈ 290. The text also mentions the conformal-Fermi physical-frame, where f_NL^inf -> 0, making the contrast formally larger. While the paper correctly states that the gauge-frame value is the relevant one for the survey estimators, the discussion of the physical frame could be confusing.
    *   **Problem:** The dual-frame discussion adds complexity without adding to the forecast. The key point is that in the frame relevant to the measurement, the contrast is large.
    *   **Required Fix:** Shorten the discussion of the conformal-Fermi frame. State that the conventional gauge frame is used by the estimators, the contrast in this frame is ~290, and that other frames exist but are not relevant to the forecast methodology. This keeps the focus on the observable quantity.

*   **P2-m2:** **Figure 2 (p. 9), Caption.** The caption describes the error bars as spanning from the "optimistic endpoint" to the "conservative endpoint". It then lists the components of the full §VII budget. This is good, but it would be clearer to explicitly state what is included in "optimistic" (e.g., template overlap only) vs. "conservative" (e.g., overlap + GR + b_φ + photo-z).
    *   **Problem:** The definition of the error bar endpoints is slightly vague in the caption itself.
    *   **Required Fix:** Revise the caption to be more explicit. E.g., "Error bars span from an optimistic case (including only the template-mismatch correction, r=0.84-0.88) to a conservative case (including the full systematic budget of §VII: template mismatch, e-correction, photometric-z degradation, and marginalization over GR effects and PNG bias b_φ)."

*   **P2-m3:** **Table III (p. 15), Correction Note.** The table includes a correction note: "[Correction note: an earlier version of this table quoted BF values... they are replaced here by the fully documented closed-form computation.]" While transparency is commendable, such version-history notes are not appropriate for a final publication. The same applies to the correction notes in Sec. IX.D (p. 18) and Sec. VI.b (p. 13).
    *   **Problem:** Internal versioning or correction history does not belong in the published article.
    *   **Required Fix:** Remove all such "Correction note" blocks from the manuscript. The final version should simply present the correct, validated numbers.

*   **P2-m4:** **Throughout, Date of Paper.** The date is listed as "(Dated: June 10, 2026)". While arXiv pre-prints can have future dates for release coordination, this is highly unconventional for a journal submission.
    *   **Problem:** The future date is unusual and could be a typo.
    *   **Required Fix:** Change the date to the current date of submission.

*   **P2-m5 (NEW):** **Section III.A (p. 7), Missing Factor in `M(k,z)` Definition.** Equation (4) for the scale-dependent bias kernel `M(k,z)` is dimensionally inconsistent in standard units. It is likely missing a factor of the scale factor `a=1/(1+z)` in the denominator, or it relies on an unstated unit convention (e.g., setting `c=1` and measuring `k` and `H_0` in inverse length units).
    *   **Problem:** The equation as written is not dimensionally sound, which hinders reproducibility.
    *   **Required Fix:** Clarify the units used or add the missing physical factors to make the equation dimensionally consistent.

*   **P2-m6 (NEW):** **Section V (p. 9), Ambiguity in Figure 2 (MegaMapper bars).** The error bars for the MegaMapper forecasts in Figure 2 are not clearly explained and do not seem to directly map to the optimistic vs. conservative ranges quoted in the text. The text gives a range from ~7.5σ (optimistic) down to 3-5σ (conservative), but the "realistic" bar in the plot seems to span roughly 4-7σ.
    *   **Problem:** The figure, a key summary of the results, is confusing and potentially inconsistent with the text.
    *   **Required Fix:** Revise the figure and/or caption to clarify exactly what scenario each bar ("ideal", "realistic", "conservative") represents and how the error bars are constructed to match the ranges quoted in the text.

*   **P2-m7 (NEW):** **Section VII.B (p. 14), Mismatch between Figure 5 and Text.** The text describing the degradation of the SPHEREx bispectrum significance due to `bφ` uncertainty quotes values (e.g., `4.0-4.2σ` at 30% `bφ` prior) that are quantitatively different from what is shown on the corresponding line in Figure 5 (which appears closer to `4.5σ`). The text attributes this to relaxing the `bφ` universality assumption.
    *   **Problem:** The plot and text present different results for what appears to be the same scenario.
    *   **Required Fix:** The text should clarify the assumptions used to generate the plot, and explicitly state why they differ from the more detailed calculation described in the text. For clarity, the plot should represent the same scenario as the main text, or the difference should be clearly noted in the caption.

---
### **Summary recommendation**

**MAJOR REVISIONS**

This is a very strong, comprehensive, and valuable paper. The author's careful work, especially in clarifying the theoretical prediction in Appendix A and quantifying the template mismatch, is a significant contribution. The paper is well-suited for publication in Physical Review D after the issues identified above are addressed.

The recommendation for **MAJOR REVISIONS** is driven by four key requirements:
1.  **Fundamental Correctness:** The dimensional inconsistency in the core defining equations for the bounce prediction (P2-E3) must be fixed.
2.  **Clarity and Focus:** The paper must be substantially shortened and restructured (P2-M1) to present its important findings more clearly and concisely. The main narrative should not be encumbered by excessive detail that can be moved to appendices.
3.  **Rigor in Interpretation:** The presentation of the Bayesian results must be revised to lead with the more conservative, physically motivated priors (P2-E2), ensuring the headline claims are not inflated. The derivation of the final systematic budget must be made quantitative and transparent (P2-M2).
4.  **Scoping of Forecasts:** The distinction between the primary bispectrum forecast and the secondary SDB forecast for the running must be sharpened to avoid any potential for confusion (P2-E1).

Addressing these points will elevate the manuscript to the high standards of the journal and ensure its significant contributions are communicated effectively to the community. I look forward to reviewing a revised version of this manuscript.