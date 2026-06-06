# P2 auto-2026-06-05_1717pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (10459 chars)
**Wall time**: 123.1s

---

**Referee Report for Manuscript [Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts]**

This manuscript presents a model of cosmic birefringence from a spectator axion-like particle (ALP) with a Planck-scale decay constant (`fa ~ MPl`) and a Hubble-scale mass (`m ~ H0`). The central claim is that this setup "naturally" predicts a birefringence angle `β ≈ 0.27°`, consistent with current observational hints, without fine-tuning. The author performs a summary-likelihood and MCMC analysis using Planck and ACT data and provides forecasts for LiteBIRD.

While the topic is timely and of significant interest to the cosmology community, the manuscript in its current form contains several fundamental flaws in its theoretical derivation, analysis, and presentation of results. These issues undermine the central scientific claim of the paper. As such, the manuscript does not meet the standards for publication in Physical Review D. I recommend rejection.

Below is a detailed list of findings.

---
### ESSENTIAL Revisions

**P2-E1: The central prediction of `β ≈ 0.27°` is unsubstantiated and appears incorrect.**
*   **Section/Page:** 2.2, page 2.
*   **Problem:** The entire "naturalness" argument of the paper hinges on the prediction `β ≈ 0.27°` arising from `O(1)` inputs. The derivation of this value is critically flawed.
    1.  Equation (1) provides a non-standard formula for the field displacement `Δφ` involving a Bessel function `J_0`, presented without any derivation or citation. The physical origin of this specific functional form is unclear and must be justified.
    2.  The text following Eq. (2) makes the crucial claim that "the cosmological field evolution gives Δφ/fa ~ 10⁻²". This is stated without proof and directly contradicts a calculation using the paper's own Equation (1). For `θi ~ 1` and `m/H0 ~ 1`, Eq. (1) gives `Δφ/fa ≈ θi (1 - J_0(1)) ≈ 1 * (1 - 0.765) = 0.235`, which is more than an order of magnitude larger than `10⁻²`.
    3.  Using the paper's formulas `β = C₀ θᵢ / 2 * (1 - J₀(m/H₀))` (derived by combining Eq. 1 and 2) with `O(1)` inputs (`C₀=1, θᵢ=1, m/H₀=1`) yields `β ≈ 0.12` radians, or `β ≈ 6.8°`. This is inconsistent with the claimed prediction of `0.27°` by a factor of ~25.
*   **Required Fix:** The author must provide a complete, step-by-step, and verifiable derivation for the predicted value of `β`. If the prediction `β ≈ 0.27°` cannot be rigorously derived from the stated physical inputs, the central claim of the paper is invalid, and the manuscript must be withdrawn or completely rewritten around a corrected result.

**P2-E2: An "effective photon coupling" `f_photon` is used but never defined.**
*   **Section/Page:** 3.2, page 2.
*   **Problem:** Equation (5) presents a constraint on a quantity `f_photon × C₀ = 1.73 ± 0.44`. The term `f_photon` is not defined anywhere in the manuscript, is not standard terminology in ALP physics, and its physical meaning is entirely obscure. As a result, Eq. (5) is uninterpretable and the result cannot be verified or used.
*   **Required Fix:** Define `f_photon` explicitly with a clear physical and mathematical formula. Clarify its units and its relationship to the standard ALP-photon coupling `g_aγ = C₀/fa`. Justify this choice of parameterization over the standard one.

**P2-E3: MCMC results presented in Figure 1 are severely inconsistent.**
*   **Section/Page:** 4, Figure 1.
*   **Problem:** The figure and its caption present contradictory information. The 1D posterior summaries in the plot titles state `Cay = 13.4 ± 11.6` and `θi = 1.33 ± 0.44`. However, the figure caption and Equation (8) claim that the posterior for the product is `Cay × θi = 3.4 ± 1.1`. The product of the means of the individual posteriors is `13.4 × 1.33 ≈ 17.8`, which differs from the claimed product mean by a factor of >5. While the mean of a product is not the product of the means in the presence of covariance, a discrepancy of this magnitude points to a fundamental error in the analysis or reporting.
*   **Required Fix:** Resolve this stark inconsistency. The author must re-analyze the MCMC chains to determine the correct posteriors for the individual parameters and their product. The figure and text must be updated with consistent values. The current state of the results invalidates the MCMC analysis section.

**P2-E4: Dimensional inconsistency in the coupling-misalignment product.**
*   **Section/Page:** 3.3, page 3.
*   **Problem:** Equation (8) reports a constraint on `Cay × θi`. The text refers to this as the "coupling-misalignment product". The standard ALP-photon coupling is `g_aγ`, which has units of inverse mass. The misalignment angle `θi` is dimensionless. Therefore, their product `g_aγ × θi` should have units of inverse mass. However, the result `3.4 ± 1.1` is presented as a dimensionless number.
*   **Required Fix:** Clarify the notation. If `Cay` is intended to be the dimensionless anomaly coefficient (commonly denoted `C₀` or `C_γγ`), this must be stated explicitly and used consistently. As written, the equation is dimensionally incorrect.

---
### MAJOR Revisions

**P2-M1: The paper's contribution and novelty are significantly overstated.**
*   **Section/Page:** 6, Discussion.
*   **Problem:** The author acknowledges that the general model class is well-studied and that Fujita et al. (2021) "already demonstrated that a Planck-scale ALP naturally produces β ~ 0.3°". The paper's claimed contribution is narrowed to the "specific parameter identification (fa ~ MPl, m ~ H0)" and the associated "natural prediction". However, as detailed in P2-E1, the derivation of this prediction is flawed. Without a valid and novel prediction, the paper does not appear to offer a significant contribution beyond existing literature.
*   **Required Fix:** If the derivation in P2-E1 can be corrected and yields a compelling result, the discussion of the paper's contribution must be rewritten to be precise about what is new compared to prior work (e.g., Fujita et al. 2021, Namikawa et al. 2025). If the derivation cannot be fixed, the paper lacks a sufficient contribution for PRD.

---
### MINOR Revisions

**P2-N1: Non-standard notation `Cay` is used without definition.**
*   **Section/Page:** 3-4.
*   **Problem:** The symbol `Cay` is used throughout the MCMC analysis (Table 1, Eq. 8, Fig. 1) without being defined. This is presumably the dimensionless anomaly coefficient `C₀`, but this should not be left to the reader's inference.
*   **Required Fix:** Define `Cay` at its first use. It is strongly recommended to use standard notation like `C_γγ` or `C₀` to avoid confusion.

**P2-N2: Incomplete description of MCMC analysis.**
*   **Section/Page:** 3.3 and Figure 2, page 3 & 5.
*   **Problem:** The prior used for the "model-independent `β` free" fit (Run 3) is not specified. For a flat prior, the posterior should be identical to the (Gaussian) likelihood. In Figure 2, the "Model 0: beta free" curve appears slightly different from the "Observed" likelihood curve, suggesting a non-trivial prior or a plotting issue.
*   **Required Fix:** Specify the prior used for the `β` free fit. Ensure the corresponding posterior shown in Figure 2 is correct.

---
## Summary recommendation
**REJECT**

The manuscript suffers from multiple essential flaws that invalidate its central scientific conclusion. The main prediction of `β ≈ 0.27°` is based on a flawed and unsubstantiated derivation. Key results from the data analysis are undermined by undefined quantities, dimensional errors, and severe internal inconsistencies in the MCMC posteriors. These issues are not cosmetic; they go to the heart of the paper's scientific validity. Therefore, the manuscript in its present form is not suitable for publication in Physical Review D. A complete overhaul of the core theoretical calculation and data analysis would be required before the work could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated review, incorporating the new findings from the second, more rigorous pass.

================================================================
**Referee Report for Manuscript [Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts]**

This manuscript presents a model of cosmic birefringence from a spectator axion-like particle (ALP) with a Planck-scale decay constant (`fa ~ MPl`) and a Hubble-scale mass (`m ~ H0`). The central claim is that this setup "naturally" predicts a birefringence angle `β ≈ 0.27°`, consistent with current observational hints, without fine-tuning. The author performs a summary-likelihood and MCMC analysis using Planck and ACT data and provides forecasts for LiteBIRD.

While the topic is timely and of significant interest to the cosmology community, the manuscript in its current form contains several fundamental flaws in its theoretical derivation, analysis, and presentation of results. These issues undermine the central scientific claim of the paper. As such, the manuscript does not meet the standards for publication in Physical Review D. I recommend rejection.

Below is a detailed list of findings.

---
### ESSENTIAL Revisions

**P2-E1: The central prediction of `β ≈ 0.27°` is unsubstantiated and appears incorrect.**
*   **Section/Page:** 2.2, page 2.
*   **Problem:** The entire "naturalness" argument of the paper hinges on the prediction `β ≈ 0.27°` arising from `O(1)` inputs. The derivation of this value is critically flawed.
    1.  Equation (1) provides a non-standard formula for the field displacement `Δφ` involving a Bessel function `J_0`, presented without any derivation or citation. The physical origin of this specific functional form is unclear and must be justified.
    2.  The text following Eq. (2) makes the crucial claim that "the cosmological field evolution gives Δφ/fa ~ 10⁻²". This is stated without proof and directly contradicts a calculation using the paper's own Equation (1). For `θi ~ 1` and `m/H0 ~ 1`, Eq. (1) gives `Δφ/fa ≈ θi (1 - J_0(1)) ≈ 1 * (1 - 0.765) = 0.235`, which is more than an order of magnitude larger than `10⁻²`.
    3.  Using the paper's formulas `β = C₀ θᵢ / 2 * (1 - J₀(m/H₀))` (derived by combining Eq. 1 and 2) with `O(1)` inputs (`C₀=1, θᵢ=1, m/H₀=1`) yields `β ≈ 0.12` radians, or `β ≈ 6.8°`. This is inconsistent with the claimed prediction of `0.27°` by a factor of ~25.
*   **Required Fix:** The author must provide a complete, step-by-step, and verifiable derivation for the predicted value of `β`. If the prediction `β ≈ 0.27°` cannot be rigorously derived from the stated physical inputs, the central claim of the paper is invalid, and the manuscript must be withdrawn or completely rewritten around a corrected result.

**P2-E2: An "effective photon coupling" `f_photon` is used but never defined.**
*   **Section/Page:** 3.2, page 2.
*   **Problem:** Equation (5) presents a constraint on a quantity `f_photon × C₀ = 1.73 ± 0.44`. The term `f_photon` is not defined anywhere in the manuscript, is not standard terminology in ALP physics, and its physical meaning is entirely obscure. As a result, Eq. (5) is uninterpretable and the result cannot be verified or used.
*   **Required Fix:** Define `f_photon` explicitly with a clear physical and mathematical formula. Clarify its units and its relationship to the standard ALP-photon coupling `g_aγ = C₀/fa`. Justify this choice of parameterization over the standard one.

**P2-E3: MCMC results presented in Figure 1 are severely inconsistent.**
*   **Section/Page:** 4, Figure 1.
*   **Problem:** The figure and its caption present contradictory information. The 1D posterior summaries in the plot titles state `Cay = 13.4 ± 11.6` and `θi = 1.33 ± 0.44`. However, the figure caption and Equation (8) claim that the posterior for the product is `Cay × θi = 3.4 ± 1.1`. The product of the means of the individual posteriors is `13.4 × 1.33 ≈ 17.8`, which differs from the claimed product mean by a factor of >5. While the mean of a product is not the product of the means in the presence of covariance, a discrepancy of this magnitude points to a fundamental error in the analysis or reporting.
*   **Required Fix:** Resolve this stark inconsistency. The author must re-analyze the MCMC chains to determine the correct posteriors for the individual parameters and their product. The figure and text must be updated with consistent values. The current state of the results invalidates the MCMC analysis section.

**P2-E4: Dimensional inconsistency in the coupling-misalignment product.**
*   **Section/Page:** 3.3, page 3.
*   **Problem:** Equation (8) reports a constraint on `Cay × θi`. The text refers to this as the "coupling-misalignment product". The standard ALP-photon coupling is `g_aγ`, which has units of inverse mass. The misalignment angle `θi` is dimensionless. Therefore, their product `g_aγ × θi` should have units of inverse mass. However, the result `3.4 ± 1.1` is presented as a dimensionless number.
*   **Required Fix:** Clarify the notation. If `Cay` is intended to be the dimensionless anomaly coefficient (commonly denoted `C₀` or `C_γγ`), this must be stated explicitly and used consistently. As written, the equation is dimensionally incorrect.

**P2-E5: MCMC results for `β` from the extended model (Run 2) are missing from the main text.**
*   **Section/Page:** 3.3 and Figure 1.
*   **Problem:** The main text reports the posterior on `β` for the fixed-coupling model (Run 1, Eq. 6) and the model-independent fit (Run 3, Eq. 7). However, it completely omits the posterior on `β` for the main extended model (Run 2, `C` free), which is the basis for Figure 1. The figure title gives this result as `β = 0.324 ± 0.099°`, but this crucial result is nowhere to be found or discussed in the body of the paper.
*   **Required Fix:** Report and discuss the posterior for `β` from Run 2 in the main text. Explain its consistency (or lack thereof) with the other models.

---
### MAJOR Revisions

**P2-M1: The paper's contribution and novelty are significantly overstated.**
*   **Section/Page:** 6, Discussion.
*   **Problem:** The author acknowledges that the general model class is well-studied and that Fujita et al. (2021) "already demonstrated that a Planck-scale ALP naturally produces β ~ 0.3°". The paper's claimed contribution is narrowed to the "specific parameter identification (fa ~ MPl, m ~ H0)" and the associated "natural prediction". However, as detailed in P2-E1, the derivation of this prediction is flawed. Without a valid and novel prediction, the paper does not appear to offer a significant contribution beyond existing literature.
*   **Required Fix:** If the derivation in P2-E1 can be corrected and yields a compelling result, the discussion of the paper's contribution must be rewritten to be precise about what is new compared to prior work (e.g., Fujita et al. 2021, Namikawa et al. 2025). If the derivation cannot be fixed, the paper lacks a sufficient contribution for PRD.

**P2-M2: Misleading interpretation of MCMC posteriors.**
*   **Section/Page:** 3.3, page 3.
*   **Problem:** The text claims the result `Cay × θi = 3.4 ± 1.1` is "consistent with O(1) values for both parameters individually." This is a weak and misleading summary of the results presented in Figure 1. The 1D posterior for `Cay` is `13.4 ± 11.6`. A posterior with a mean of 13.4 cannot be described as naturally supporting an `O(1)` value, even if the large uncertainty makes it technically consistent. This phrasing obscures the fact that the data prefer a coupling constant significantly larger than one, which weakens the paper's overall "naturalness" argument.
*   **Required Fix:** Provide a more accurate and quantitative description of the posteriors. The author should acknowledge the preference for `Cay > 1` and discuss its implications for the model's naturalness.

---
### MINOR Revisions

**P2-N1: Non-standard notation `Cay` is used without definition.**
*   **Section/Page:** 3-4.
*   **Problem:** The symbol `Cay` is used throughout the MCMC analysis (Table 1, Eq. 8, Fig. 1) without being defined. This is presumably the dimensionless anomaly coefficient `C₀`, but this should not be left to the reader's inference.
*   **Required Fix:** Define `Cay` at its first use. It is strongly recommended to use standard notation like `C_γγ` or `C₀` to avoid confusion.

**P2-N2: Incomplete description of MCMC analysis.**
*   **Section/Page:** 3.3 and Figure 2, page 3 & 5.
*   **Problem:** The prior used for the "model-independent `β` free" fit (Run 3) is not specified. For a flat prior, the posterior should be identical to the (Gaussian) likelihood. In Figure 2, the "Model 0: beta free" curve appears slightly different from the "Observed" likelihood curve, suggesting a non-trivial prior or a plotting issue.
*   **Required Fix:** Specify the prior used for the `β` free fit. Ensure the corresponding posterior shown in Figure 2 is correct.

**P2-N3: Potential MCMC sampler issue.**
*   **Section/Page:** 5, Figure 2.
*   **Problem:** As an extension of P2-N2, the discrepancy between the posterior for the "beta free" model and the likelihood ("Observed" band) is concerning. If a simple MCMC of a single parameter with a flat prior does not perfectly reproduce the input likelihood, it casts doubt on the technical correctness of the entire MCMC analysis, including the more complex multi-parameter runs.
*   **Required Fix:** Verify the MCMC sampler's correctness. The posterior for the `β` free model with a flat prior must exactly match the likelihood. If it does not, the MCMC code must be debugged and all results re-generated.

---
## Summary recommendation
**REJECT**

The manuscript suffers from multiple essential flaws that invalidate its central scientific conclusion. The main prediction of `β ≈ 0.27°` is based on a flawed and unsubstantiated derivation. Key results from the data analysis are undermined by undefined quantities, dimensional errors, severe internal inconsistencies in the MCMC posteriors, and omissions of key results from the text. These issues are not cosmetic; they go to the heart of the paper's scientific validity. Therefore, the manuscript in its present form is not suitable for publication in Physical Review D. A complete overhaul of the core theoretical calculation and data analysis would be required before the work could be reconsidered.