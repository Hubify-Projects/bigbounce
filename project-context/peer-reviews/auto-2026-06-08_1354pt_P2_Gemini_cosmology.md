# P2 auto-2026-06-08_1354pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 121.5s

---

## Referee Report: Cosmic Birefringence from a Planck-Scale Axion-Like Particle

**Manuscript ID:** [As provided by journal]
**Title:** Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts
**Author:** Houston Golden

This paper presents a model of an axion-like particle (ALP) with a Planck-scale decay constant and a Hubble-scale mass to explain the tentative evidence for cosmic birefringence in CMB data. The author claims this model "naturally" produces the observed rotation angle without fine-tuning. The paper presents a summary-likelihood analysis, MCMC parameter estimation, and forecasts for the LiteBIRD satellite.

While the topic is timely and of significant interest, the manuscript in its current form suffers from several critical flaws in its core physical derivation and subsequent analysis. The central claims are not substantiated by the details provided, and the numerical results are internally inconsistent. For these reasons, the paper does not meet the standards for publication in Physical Review D.

### ESSENTIAL Revisions

**P2-E1: The central physical prediction is unsubstantiated and appears incorrect.**
*   **Section/Page:** Section 2.2, page 2.
*   **Problem:** The paper's core claim is that an ALP with `m ~ H₀` and `fₐ ~ M_Pl` naturally predicts a birefringence angle `β ≈ 0.27°`. This result hinges on the assertion that "the cosmological field evolution gives `Δφ/fₐ ~ 10⁻²`". This crucial value is stated without any derivation or citation. A simple estimate of the field evolution for `m ~ H₀` suggests a much larger displacement. The equation of motion `d²φ/dt² + 3H dφ/dt + m²fₐ sin(φ/fₐ) = 0` for a field starting to roll today (`H ~ m`) implies `Δφ ~ -∫[V'(φᵢ)/(3H)]dt`, which is dominated by late times. This yields `Δφ/fₐ ~ O(0.1-1)`, not `10⁻²`. This would predict a `β` angle of several degrees, an order of magnitude larger than observed, contradicting the "naturalness" claim. The un-derived Eq. (1), `Δφ ≈ fₐθᵢ(1 - J₀(m/H₀))`, also gives `Δφ/fₐ ≈ 0.24` for `m/H₀ ~ 1` and `θᵢ ~ 1`, which is inconsistent with `10⁻²`.
*   **Required Fix:** The author must provide a complete, step-by-step derivation for the field displacement `Δφ` in the specified cosmological background (matter + dark energy). This derivation must transparently show how the value `Δφ/fₐ ~ 10⁻²` is obtained. If this value is incorrect, the paper's central claim of a natural prediction is invalid, and the manuscript must be completely reframed or withdrawn.

**P2-E2: MCMC results are internally inconsistent.**
*   **Section/Page:** Section 3.3 and Figure 1, pages 3-4.
*   **Problem:** The text and the main figure present contradictory results from the MCMC analysis. Section 3.3 (page 3) reports the constraint on the product of the coupling and misalignment angle as `Cₐᵧ × θᵢ = 3.4 ± 1.1`. However, the triangle plot in Figure 1 (page 4) shows marginalized 1D posteriors of `θᵢ = 1.33 ± 0.44` and `Cₐᵧ = 13.4 ± 1.8`. The product of the means of these two parameters is `1.33 × 13.4 ≈ 17.8`, which is more than five times larger than the value `3.4` quoted in the text. The caption of Figure 1 repeats the incorrect value from the text.
*   **Required Fix:** This is a critical error that undermines the entire parameter estimation section. The author must find the source of this discrepancy, correct the analysis, and ensure that the text, tables, and figures are all mutually consistent. The paper cannot be considered for publication until this is resolved.

**P2-E3: Undefined quantities and opaque derivations.**
*   **Section/Page:** Section 3.2, page 2.
*   **Problem:** Equation (5) presents a constraint on an "effective photon coupling parameter" as `f_photon × C₀ = 1.73 ± 0.44`. The quantity `f_photon` is not defined anywhere in the manuscript, making the expression meaningless to the reader. Furthermore, it is impossible to reproduce this result from the information given. A constraint on a physical coupling can only be derived from the measured angle `β` by assuming a model for the field displacement `Δφ`, but this link is not made explicit.
*   **Required Fix:** The author must define all terms, especially `f_photon`. The derivation of Eq. (5) from the combined `β` value in Eq. (4) must be shown explicitly, including all model assumptions (e.g., the assumed value of `Δφ/fₐ`).

### MAJOR Revisions

**P2-M1: MCMC analysis lacks statistical robustness.**
*   **Section/Page:** Section 3.3 and Table 1, page 3.
*   **Problem:** The author correctly acknowledges that the MCMC sample sizes are "modest by modern standards," with effective sample sizes `N_eff ~ 1,000`. For a paper whose conclusions rely on parameter inference and model comparison (via the Bayes factor), this level of sampling is insufficient to robustly characterize the posterior, especially its tails, or to compute a reliable evidence value.
*   **Required Fix:** The MCMC analysis should be re-run with much longer chains to achieve `N_eff > 10,000` for all relevant parameters. This is the standard in modern cosmological data analysis and is necessary to lend credibility to the parameter constraints and the Bayes factor calculation.

### MINOR Revisions

**P2-m1: Inconsistent labeling in Figure 2.**
*   **Section/Page:** Figure 2, page 5.
*   **Problem:** The legend in Figure 2 uses labels "Model 2", "Model 2b", and "Model 0". The text and Table 1, however, refer to these as Run 1, Run 2, and Run 3.
*   **Required Fix:** Harmonize the labeling between the text, tables, and figures for clarity. Using the descriptive names (e.g., "ALP (C=8 fixed)") consistently would be best.

**P2-m2: Unconventional citation of future work.**
*   **Section/Page:** References, page 6.
*   **Problem:** The bibliography cites several papers with future dates (e.g., "2025", "2026a", "2026b"). For works by other authors not yet on the arXiv, the standard is to cite them as "in preparation" or "private communication". For the author's own work, "submitted" or an arXiv identifier is appropriate.
*   **Required Fix:** Please format all citations according to journal standards. Replace future years with the appropriate status (e.g., arXiv:YYMM.NNNNN, in preparation).

### NIT

**P2-N1: Manuscript date.**
*   **Section/Page:** Page 1.
*   **Problem:** The manuscript is dated "March 20, 2026".
*   **Required Fix:** The date should be corrected to the date of submission.

## Summary recommendation
**REJECT**

The manuscript attempts to connect a simple, "natural" ALP model to the observed hints of cosmic birefringence. While the idea is appealing, the execution is critically flawed. The central physical prediction is not derived and appears to be incorrect by an order of magnitude based on simple estimates (P2-E1). The numerical analysis that forms the bulk of the paper is undermined by a severe internal inconsistency between the text and a key figure (P2-E2). Important physical quantities are left undefined (P2-E3).

These issues are not cosmetic; they strike at the heart of the paper's scientific validity. Correcting them would require a complete re-derivation of the physics and a full re-analysis of the data, which constitutes a new submission. Therefore, I cannot recommend this manuscript for publication in Physical Review D.