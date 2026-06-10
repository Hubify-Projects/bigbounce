# P2 auto-2026-06-08_1144pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 145.1s

---

**Referee Report for Physical Review D**

**Manuscript Title:** Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts
**Author:** Houston Golden
**Date:** June 8, 2026

This paper presents an analysis of an axion-like particle (ALP) model with a Planck-scale decay constant (`f_a ~ M_Pl`) and a Hubble-scale mass (`m ~ H_0`) as an explanation for the tentative signal of cosmic birefringence in CMB data. The author claims this setup "naturally" produces a rotation angle `β ≈ 0.27°`, consistent with observations, without fine-tuning. The paper combines recent Planck and ACT data, performs a parameter inference using MCMC, and provides forecasts for the LiteBIRD satellite.

While the topic is timely and the analysis framework is potentially interesting, the manuscript in its current form suffers from several fundamental flaws, including a contradictory derivation of its central prediction and a significant inconsistency between its main theoretical premise and its own numerical results. The paper cannot be published without addressing the following essential and major issues.

---
### Detailed Findings

#### ESSENTIAL Revisions

**P2-E1: Contradictory and Opaque Derivation of the Birefringence Prediction**
*   **Section/Page:** Sec. 2.2, p. 2
*   **Problem:** The derivation of the paper's central prediction, `β ≈ 0.27°`, is based on a value for the field displacement `Δφ/f_a ~ 10⁻²`. However, this value is in direct contradiction with the analytical approximation provided in Equation (1).
    *   Equation (1) states `Δφ ≈ f_a θ_i (1 - J_0(m/H_0))`. For the model's assumptions (`θ_i ~ 1`, `m/H_0 ~ 1`), this gives `Δφ/f_a ≈ 1 - J_0(1) ≈ 0.24`.
    *   The text immediately following Equation (2) claims "the cosmological field evolution gives `Δφ/f_a ~ 10⁻²`".
    This is a discrepancy of a factor of ~24. The paper's final prediction relies entirely on the `10⁻²` value, but its origin is unexplained, while the only provided equation gives a completely different result. Furthermore, Equation (1) itself is non-standard and presented without citation or derivation.
*   **Required Fix:** The author must provide a clear, correct, and verifiable derivation for the field displacement `Δφ`. If the `10⁻²` value comes from a numerical integration, the setup and results of that integration must be presented, and the incorrect/misleading Equation (1) must be removed or corrected. The central quantitative claim of the paper is currently unsubstantiated.

**P2-E2: MCMC Results Contradict the Paper's Central Premise (`m ~ H_0`)**
*   **Section/Page:** Sec. 3.3, p. 3 and Figure 1, p. 4
*   **Problem:** The core argument of the paper is that an ALP with a "Hubble-scale mass" (`m ~ H_0`) naturally explains the observed birefringence. However, the paper's own MCMC results, shown in Figure 1, decisively falsify this premise.
    *   The posterior for the mass is `log10(m_a/eV) = -31.4 ± 1.2`.
    *   The Hubble scale corresponds to `H_0 ≈ 2.13 h × 10⁻³³ eV ≈ 1.4 × 10⁻³³ eV`, which is `log10(m_a/eV) ≈ -32.85`.
    *   The best-fit mass (`10⁻³¹·⁴ eV ≈ 4 × 10⁻³² eV`) is more than an order of magnitude larger than `H_0`, and the value `m_a = H_0` is excluded at high significance by the data (`~1.2σ` away based on the reported error, but the posterior in Fig 1 shows a sharp cutoff at low mass). The model presented in the text (`m ~ H_0`) is not the model preferred by the data.
*   **Required Fix:** The entire narrative of the paper must be revised to reflect what the results actually show. The central claim that a Hubble-scale mass ALP "naturally accommodates" the signal is incorrect. The paper should be reframed as a constraint on the ALP mass, demonstrating that the data prefers `m_a ≈ 30 H_0`. The abstract, introduction, discussion, and conclusion must be rewritten to remove the unsupported "naturalness" claims related to `m ~ H_0`.

#### MAJOR Revisions

**P2-M1: Misleading Claims of "Order-Unity" Parameters**
*   **Section/Page:** Sec. 3.3, p. 3 and Figure 1, p. 4
*   **Problem:** The paper repeatedly claims that the model works with "order-unity" inputs, which is a key part of its "no fine-tuning" argument. The MCMC results in Figure 1 contradict this. The posterior for the coupling constant `C_aγ` is `13.4 ± 11.6`. The 1D posterior is clearly peaked far from unity, with `C_aγ=1` having very low posterior support. The data prefers a moderately large coupling, which weakens the naturalness argument. Stating that the result is "consistent with O(1) values for both parameters individually" is misleading.
*   **Required Fix:** The author must accurately report that the MCMC fit prefers a value for `C_aγ` of `O(10)`, not `O(1)`. The discussion of naturalness must be revised to account for this preference for a larger-than-unity coupling.

**P2-M2: Undefined Parameters and Inconsistent Notation**
*   **Section/Page:** Sec. 3.2, p. 2
*   **Problem:** Equation (5) presents a constraint on a quantity `f_photon × C_0`. The parameter `f_photon` is never defined in the text, making the equation and its value (`1.73 ± 0.44`) incomprehensible. Additionally, the notation for the coupling constant is inconsistent throughout the paper, alternating between `C_0` (Abstract, Sec 2.2) and `C_aγ` (Sec 3.3, Fig 1) without stating if they are the same quantity.
*   **Required Fix:** Define all parameters clearly. If `f_photon` is a typo, correct it. If it is a new parameter, define it and explain its physical meaning. Unify the notation for the coupling constant (e.g., use `C_aγ` everywhere) and define it explicitly in relation to the Chern-Simons term.

**P2-M3: Overstated Novelty**
*   **Section/Page:** Sec. 6, p. 5
*   **Problem:** The paper claims its contribution is "the specific parameter identification (`f_a ~ M_Pl`, `m ~ H_0`) that produces a natural prediction". However, as the paper itself cites, Fujita et al. (2021, PRD 103, 043509) already identified this exact parameter space as a viable source for `β ~ O(0.1) deg`. The novelty of the paper is therefore not the model itself, but the application of updated data and a specific inference framework.
*   **Required Fix:** The author should moderate the claims of novelty and more clearly situate the work as an updated constraint and test of a previously proposed model class, highlighting that the new data disfavors the simplest `m ~ H_0` scenario.

#### MINOR Revisions

**P2-m1: Understated Statistical Evidence**
*   **Section/Page:** Sec. 3.4, p. 3
*   **Problem:** The Bayes factor `ln B = 5.17` is described as "indicative evidence". On the commonly used Jeffreys scale, `ln B > 5` corresponds to "very strong" or "decisive" evidence. The terminology used is unusually weak and should be clarified.
*   **Required Fix:** Use standard terminology to describe the strength of the Bayesian evidence, for example, by referencing the Jeffreys scale.

**P2-m2: Missing Citation for Key Data Value**
*   **Section/Page:** Sec. 3.1, p. 2
*   **Problem:** The MCMC analysis uses the value `β_obs = 0.342 ± 0.094°`, attributed to an "Eskilt et al. joint Planck + ACT analysis". However, the reference list only contains "Eskilt and Komatsu, 2022", which reports a different value.
*   **Required Fix:** Provide a full citation for the joint analysis from which this value is taken.

**P2-m3: Inconsistent Figure/Table Labeling**
*   **Section/Page:** Figure 2, p. 5 and Table 1, p. 3
*   **Problem:** The legend in Figure 2 refers to "Model 2", "Model 2b", and "Model 0". Table 1 refers to these same configurations as "Run 1", "Run 2", and "Run 3".
*   **Required Fix:** Make the labeling consistent between the table and the figure legend.

#### NITs

**P2-N1: Future Date on Manuscript**
*   **Section/Page:** p. 1
*   **Problem:** The manuscript is dated "March 20, 2026".
*   **Required Fix:** The date should be corrected to the date of submission.

---
## Summary recommendation

**MAJOR REVISIONS**

The paper addresses a compelling and timely topic, but its central scientific claims are undermined by its own results and a flawed theoretical derivation. The discrepancy between the claimed `m ~ H_0` model and the MCMC posterior that strongly prefers a significantly larger mass is a fatal issue that requires a complete reframing of the paper's narrative and conclusions. The derivation of the `β` prediction must be made transparent and correct.

Given the fundamental nature of these problems, the paper requires a thorough and substantial revision. The author must abandon the unsupported "naturalness" argument and instead present the work as a data-driven constraint on this ALP model, one which points to a mass scale an order of magnitude above `H_0`. If these essential and major issues can be satisfactorily addressed, a revised version of the manuscript could be a valuable contribution.