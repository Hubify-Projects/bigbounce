# P2 auto-2026-06-05_1817pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (5675 chars)
**Wall time**: 120.7s

---

Referee Report for PRD Manuscript
==================================

**Manuscript ID:** [Assigned by system]
**Title:** Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts
**Author:** Houston Golden

This paper presents a model of cosmic birefringence from a spectator axion-like particle (ALP) with a Planck-scale decay constant (`f_a ~ M_Pl`) and a Hubble-scale mass (`m ~ H_0`). The author claims this setup "naturally" predicts a birefringence angle `β ≈ 0.27°`, consistent with current observations. The paper provides a statistical analysis combining Planck and ACT data and forecasts the sensitivity of the LiteBIRD satellite.

While the topic is timely and the statistical analysis appears sound, the central theoretical claim of the paper is based on a flawed and contradictory derivation. This fundamental issue invalidates the paper's main conclusion regarding a "natural" prediction. Therefore, I cannot recommend publication in Physical Review D in its current form.

## Detailed Findings

### ESSENTIAL

**P2-E1: Fatal Contradiction in the Core Theoretical Prediction**
*   **Location:** Section 2.1 & 2.2, Page 1-2, Equations (1) & (2)
*   **Problem:** The paper's central claim is that the proposed ALP model naturally predicts `β ≈ 0.27°`. This prediction hinges on the value of the field displacement `Δφ`. The paper presents two contradictory values for this quantity.
    1.  **Equation (1) implies a large displacement:** The paper gives `Δφ ≈ f_a θ_i (1 - J_0(m/H_0))`. For the model's "natural" inputs (`θ_i ~ 1`, `m/H_0 ~ 1`), the text correctly evaluates `1 - J_0(1) ≈ 0.24`. This leads to a dimensionless displacement `Δφ/f_a ≈ 0.24`.
    2.  **Section 2.2 requires a small displacement:** To arrive at the `β ≈ 0.27°` prediction, the text in Section 2.2 explicitly states: "the cosmological field evolution gives Δφ/fₐ ~ 10⁻²". This value is then used to calculate `β ≈ C₀ θᵢ × 5 × 10⁻³ rad ≈ 0.27°`.

    There is a discrepancy of a factor of ~24 between the value of `Δφ/f_a` implied by Equation (1) and the value required in Section 2.2. If one uses the result from Eq. (1), the predicted birefringence angle would be `β = (C_0 θ_i / 2) * (Δφ/f_a) ≈ (1*1/2) * 0.24 ≈ 0.12` radians, which is `~6.8°`. This is grossly inconsistent with the observed value of `~0.3°`. The paper's central claim of a natural prediction matching observation is therefore unsubstantiated by its own equations.
*   **Required Fix:** The paper cannot be published with this contradiction. The author must provide a complete, step-by-step, and verifiable derivation for `Δφ` that resolves this discrepancy. If the correct result is indeed `Δφ/f_a ≈ 0.24`, then the claim of a natural prediction matching data must be retracted, which would remove the paper's primary motivation.

**P2-E2: Unsubstantiated Physical Model for Field Dynamics**
*   **Location:** Section 2.1, Page 2, Equation (1)
*   **Problem:** Equation (1) presents the field displacement in terms of a Bessel function, `J_0(m/H_0)`. This is not a standard result for the evolution of a scalar field in the late universe. The dynamics are governed by the Klein-Gordon equation in an expanding background, which for `z ~ O(1)` involves a complicated evolution through the matter-dark energy transition. A simple analytical form involving a Bessel function is highly non-trivial and requires a rigorous derivation or, at minimum, a citation to a paper where it is derived. The paper provides neither.
*   **Required Fix:** The author must provide a full derivation of Equation (1) from the Klein-Gordon equation in a ΛCDM background, or cite a source where this specific result is derived. Without this, the equation is an unsubstantiated assertion.

### MAJOR

**P2-M1: Manuscript Date**
*   **Location:** Page 1
*   **Problem:** The manuscript is dated "March 20, 2026", which is a future date. This is unprofessional and should be corrected.
*   **Required Fix:** Change the date to the date of submission.

### MINOR

**P2-m1: Confusing Phrasing in Introduction**
*   **Location:** Section 1, Page 1
*   **Problem:** The abstract presents the paper's combined result `β = 0.242 ± 0.061° (3.9σ)`. The introduction, however, states "Combined, the evidence exceeds 3.5σ." This latter figure refers to the Eskilt et al. (2022) joint analysis (`3.6σ`), not the result derived in this paper. This could confuse the reader about which result is being discussed.
*   **Required Fix:** Clarify the sentence in the introduction. For example: "The joint analysis of Eskilt et al. found evidence exceeding 3.6σ, and our combination of more recent point estimates (see Sec. 3.2) yields a significance of 3.9σ."

**P2-m2: Inconsistent Parameter Notation**
*   **Location:** Section 3.3, Page 3
*   **Problem:** The text refers to "Run 1, C = 8 fixed". However, Table 1 and the priors list the parameter as `C_aγ`. The parameter `C` is not defined. This appears to be a typo.
*   **Required Fix:** Change "C = 8 fixed" to "C_aγ = 8 fixed" for consistency with the rest of the text and tables.

### NIT

**P2-N1: Notation for Planck Mass**
*   **Location:** Throughout the paper (e.g., Abstract, Page 1)
*   **Problem:** The paper uses `MP1`. The standard notation in cosmology is `M_Pl`.
*   **Required Fix:** Use the standard notation `M_Pl` consistently.

**P2-N2: Notation for Gelman-Rubin Statistic**
*   **Location:** Table 1 and Section 3.3, Page 3
*   **Problem:** The table header is `R-1` and the text uses `R - 1`. The standard notation for the Gelman-Rubin diagnostic is `R̂`.
*   **Required Fix:** Use the standard notation `R̂ - 1 < 0.01` for clarity and consistency with the literature.

## Summary recommendation

**REJECT**

The paper addresses a compelling and important topic in modern cosmology. The statistical analysis is presented clearly, and the discussion of systematics and future tests is appropriate. However, the entire premise of the paper—that a simple, natural ALP model predicts the observed birefringence angle—is invalidated by a fatal contradiction at the heart of its theoretical derivation (P2-E1). The calculation presented implies a predicted signal that is more than an order of magnitude larger than what is claimed and what is observed. Furthermore, the key equation for the field's evolution is presented without derivation or citation (P2-E2).

Because these issues undermine the central scientific contribution of the manuscript, it does not meet the standards for publication in Physical Review D. A revision would require a completely new and correct theoretical derivation, which would constitute a new paper that would need to be reviewed from scratch.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from the second, more rigorous review.

================================================================
Referee Report for PRD Manuscript (Additional Findings)
================================================================

**P2-E3: Inconsistency Between Analytical Model and MCMC Results**
*   **Location:** Section 2.2 & Section 3.3, Page 2-3, Eq (1) & Eq (8)
*   **Problem:** There is a severe numerical inconsistency between the analytical prediction of the model and the results of the MCMC fit to the data.
    1.  The analytical model, using Eq (1), predicts a birefringence angle `β [rad] ≈ 0.12 × C_aγ × θ_i`.
    2.  The MCMC fit, which finds the parameter values preferred by the data, reports a posterior for the product `C_aγ × θ_i = 3.4 ± 1.1` (Eq 8).
    3.  Substituting the MCMC result into the analytical formula gives a predicted angle of `β ≈ 0.12 × 3.4 = 0.408` radians, which is `23.4°`. This is nearly two orders of magnitude larger than the observed value of `~0.3°`.
    This demonstrates that the physical model presented in Section 2 is fundamentally incompatible with the data and the parameter constraints derived in Section 3. The paper's claim that the model "reproduces the observed birefringence with no tension" is incorrect.
*   **Required Fix:** This contradiction must be resolved. It likely stems from the incorrect formula for `Δφ` (P2-E1), but it represents a separate, fatal check-sum failure between the theory and data-fitting sections of the paper.

**P2-E4: Opaque and Undefined "Effective Coupling"**
*   **Location:** Abstract & Section 3.2, Page 1-2, Eq (5)
*   **Problem:** The paper presents a constraint on an "effective photon coupling `f_photon × C_0 = 1.73 ± 0.44`". The parameter `f_photon` is never defined anywhere in the paper, nor is the derivation of this constraint from the birefringence angle `β` shown. As presented, this result is entirely opaque and cannot be verified or interpreted. It appears to be a simple rescaling of `β`, but without an explicit definition, it has no physical meaning.
*   **Required Fix:** The parameter `f_photon` must be rigorously defined. The full derivation of its constraint from the measured value of `β` must be provided. If it is simply a linear rescaling of `β`, this should be stated, and its utility justified.

**P2-M2: Contradictory Claims of "Naturalness" and "Order-Unity Inputs"**
*   **Location:** Abstract, Section 1, Figure 1
*   **Problem:** A central claim of the paper is that the observed signal is naturally produced from "order-unity inputs". However, the paper's own MCMC results contradict this. Figure 1 shows the posterior distribution for the coupling constant `C_aγ`, which has a mean of `13.4` (with a large uncertainty of `11.6`). A value of `~13` is not "order-unity". The abstract's claim that the model works for order-unity inputs is therefore falsified by the results presented in the paper.
*   **Required Fix:** The claims of naturalness from order-unity inputs must be retracted or substantially revised to be consistent with the MCMC results. The author must acknowledge that the data prefers a coupling constant significantly larger than one.

**P2-M3: Manuscript Date**
*   **Location:** Page 1
*   **Problem:** The manuscript is dated "March 20, 2026", which is a future date. This is unprofessional and should be corrected.
*   **Required Fix:** Change the date to the date of submission.

**P2-m3: Inconsistent Model/Run Numbering in Figure**
*   **Location:** Section 3.3 and Figure 2, Page 3 & 5
*   **Problem:** The MCMC configurations are referred to as "Run 1", "Run 2", and "Run 3" in the text and Table 1. The legend of Figure 2, which plots the results of these runs, labels them "Model 2", "Model 2b", and "Model 0", respectively. This inconsistent numbering is confusing.
*   **Required Fix:** The numbering/labeling scheme for the MCMC runs must be made consistent between the text, tables, and figures.

**P2-m4: Inconsistent Use of Observational Data**
*   **Location:** Section 3.2 and 3.3, Page 2-3
*   **Problem:** The paper presents two different values for the observational constraint on `β`. In Section 3.2, it derives a combined value of `β = 0.242 ± 0.061°`. However, in Section 3.3, the MCMC analysis uses the literature value `β_obs = 0.342 ± 0.094°`. While using the more rigorous literature value for the MCMC is defensible, the paper does not justify this choice or explain the role of its own derived value, which is presented as a key result in the abstract. This creates ambiguity about which constraint the model is being tested against.
*   **Required Fix:** The author should clarify why two different observational constraints are used. It would be more consistent to use a single, well-justified value throughout the paper, or to explicitly state why different values are appropriate for different parts of the analysis.

**P2-m5: Misleading Hedge on Parameter Consistency**
*   **Location:** Section 3.3, Page 3
*   **Problem:** The paper claims that the MCMC posterior `C_aγ × θ_i = 3.4 ± 1.1` is "consistent with O(1) values for both parameters individually." While technically true due to the enormous error bar on `C_aγ` (`13.4 ± 11.6`), this statement is misleading. It obscures the fact that the posterior *mean* for `C_aγ` is over an order of magnitude larger than one, which contradicts the paper's central "naturalness" argument.
*   **Required Fix:** The phrasing should be made more precise to reflect the actual posterior constraints. For example, by stating that while the posterior is wide, its mean value for `C_aγ` is significantly larger than one.