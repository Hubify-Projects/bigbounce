# P2 auto-2026-06-08_1520pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (3346 chars)
**Wall time**: 115.6s

---

# Referee Report

**Paper:** Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts
**Author:** Houston Golden

This paper presents a model of cosmic birefringence from an axion-like particle (ALP) with a Planck-scale decay constant and a Hubble-scale mass. The author claims this setup "naturally" predicts a birefringence angle `β ≈ 0.27°`, consistent with current observations. The paper provides a statistical analysis combining Planck and ACT data, MCMC parameter estimation for the ALP model, and forecasts for the LiteBIRD satellite.

While the topic is timely and of significant interest to the cosmology community, the manuscript suffers from several fundamental flaws that preclude its publication in Physical Review D. The issues range from the use of non-public and futuristic data/references to a critical failure to derive the central physical prediction of the paper. The statistical analysis also contains major inconsistencies.

Below is a detailed list of required revisions.

---
## Detailed Findings

### ESSENTIAL Revisions (Paper cannot be accepted without these fixes)

**P2-E1: Use of Fictitious/Futuristic Dates, Data, and References**
*   **Section/Page:** Throughout (e.g., Title page, Sec. 3.1 on p. 2, References on p. 6)
*   **Problem:** The paper is dated "March 20, 2026". It cites multiple papers with publication dates of 2025 and 2026 (e.g., [3] Diego-Palazuelos and Komatsu, 2025; [8] Namikawa et al., 2025; [5,6] Golden, 2026a,b). Most critically, the analysis relies on a measurement from "ACT DR6" ([3]), which is not public. A scientific paper must be based on publicly available data and literature at the time of submission. Using hypothetical future results is unacceptable.
*   **Required Fix:** The entire analysis must be redone using only currently available, public data. All futuristic dates and references must be removed or replaced with appropriate citations to existing work. The manuscript date must be corrected to the submission date.

**P2-E2: Central Physical Prediction is Unsubstantiated and Contradictory**
*   **Section/Page:** Sec. 2.2, p. 2
*   **Problem:** The paper's core claim is a "natural prediction" of `β ≈ 0.27°`. This relies on the field displacement `Δφ`. The manuscript provides two contradictory and entirely unsubstantiated claims for this crucial quantity:
    1.  Eq. (1) gives `Δφ ≈ f_a θ_i (1 - J_0(m/H_0))`, which for `m/H_0 ~ 1` and `θ_i ~ 1` implies `Δφ/f_a ≈ 0.24`. The appearance of the Bessel function `J_0` is non-standard for the dynamics of a scalar field with a cosine potential in the late universe and is presented without any derivation or citation.
    2.  The text below Eq. (2) claims "the cosmological field evolution gives `Δφ/f_a ~ 10⁻²`". This value is necessary to obtain the final `β ≈ 0.27°` prediction, but it directly contradicts the result from Eq. (1) and is also presented without derivation.
*   **Required Fix:** The author must provide a complete, first-principles derivation of the ALP field displacement `Δφ` from recombination to today by solving the equation of motion in an expanding universe. This derivation must transparently show how the final numerical value for `β` is obtained from the model's input parameters. Without this, the paper's central physical claim is unsupported.

**P2-E3: Inconsistent MCMC Results**
*   **Section/Page:** Sec. 3.3 (p. 3) and Figure 1 (p. 4)
*   **Problem:** There is a major inconsistency between the results presented in the text and in Figure 1 for the MCMC analysis (Run 2).
    *   Eq. (8) reports the posterior for the product of the coupling and misalignment angle as `C_aγ × θ_i = 3.4 ± 1.1`.
    *   However, the 1D marginalized posteriors in the titles of Figure 1 are `C_aγ = 13.4...` and `θ_i = 1.33...`. The product of these mean values is `~17.8`, which is a factor of 5 larger than the value quoted in Eq. (8).
    *   While `E[XY] ≠ E[X]E[Y]` for correlated variables, this large a discrepancy, combined with the visual evidence of the `C_aγ` posterior being pushed against its prior boundary, indicates that the 1D marginalized constraints are highly misleading and the results are not being presented transparently.
*   **Required Fix:** The author must resolve this inconsistency. The text must clearly explain why the product of the means of the 1D marginalized posteriors is so different from the mean of the posterior of the product. The misleading 1D constraints in the titles of Figure 1 should be removed or properly qualified, as they do not represent the typical values of the parameters due to the strong degeneracy.

**P2-E4: Unverifiable Observational Input**
*   **Section/Page:** Sec. 3.1, p. 2
*   **Problem:** The MCMC analysis is based on the value `β_obs = 0.342 ± 0.094°`. This is attributed to an "Eskilt et al. joint Planck + ACT analysis". However, there is no corresponding reference in the bibliography. The cited Eskilt & Komatsu 2022 paper [2] reports a different value (`0.30 ± 0.11°`) and does not include ACT data. The foundation of the entire inference section (Sec. 3.3, 3.4, Fig. 1, Fig. 2) rests on a data point from an un-cited, and possibly non-existent, analysis.
*   **Required Fix:** Provide a proper, verifiable citation for the `β_obs = 0.342 ± 0.094°` value. If this value is from a private communication or a preliminary analysis that is not public, it cannot be used. The analysis must be based on a published, citable result.

### MAJOR Revisions

**P2-M1: Undefined Parameter in Results**
*   **Section/Page:** Sec. 3.2, p. 2
*   **Problem:** Equation (5) presents a constraint on a parameter combination `f_photon × C_0 = 1.73 ± 0.44`. The parameter `f_photon` is described only as an "effective photon coupling parameter" and is never defined in terms of the model's fundamental parameters (`f_a`, `m`, `θ_i`, `C_0`). This makes the result uninterpretable.
*   **Required Fix:** Provide a precise mathematical definition for `f_photon`. Explain its physical significance and how it is derived from the other model parameters and the data.

**P2-M2: Unacknowledged Prior-Dependence of MCMC Results**
*   **Section/Page:** Figure 1, p. 4
*   **Problem:** The 1D marginalized posterior for the ALP mass, `log10(m_a/eV)`, is clearly pushed against the upper boundary of its prior (`[-35, -30]`). This is a strong indication that the data prefer a higher mass than the prior allows, and that the posterior is heavily dependent on the choice of this upper boundary. This is a significant weakness of the analysis that is not mentioned or discussed in the text.
*   **Required Fix:** The author must acknowledge and discuss the prior-dependence of the mass constraint. The analysis should be repeated with a wider prior on the mass to investigate how the posterior changes. The conclusion that `m ~ H_0` (which corresponds to `log10(m/eV) ≈ -32.7`) may not be robust.

**P2-M3: Overstated Novelty**
*   **Section/Page:** Sec. 6, p. 5
*   **Problem:** The paper acknowledges that "Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces β ~ 0.3°". The author then claims their contribution is "the specific parameter identification (fa ~ MP1, m ~ Ho) ... and the inference framework". Given that the physical derivation for this specific identification is missing (see P2-E2) and the inference framework is standard, the claimed novelty is extremely narrow and, in its current state, unsupported.
*   **Required Fix:** The author must significantly revise the claims of novelty. If the physical derivation can be fixed, the contribution must be framed carefully in the context of prior work. If not, the paper does not contain a sufficient contribution for publication in PRD.

### MINOR Revisions

**P2-m1: Inconsistent Notation for Anomaly Coefficient**
*   **Section/Page:** p. 2 and p. 3
*   **Problem:** The text uses `C_0` for the anomaly coefficient in Section 2.2, but the MCMC analysis in Section 3.3 and Figure 1 uses `C_aγ`. It is not explicitly stated that these are the same parameter.
*   **Required Fix:** Use consistent notation for the anomaly coefficient throughout the paper.

---
## Summary recommendation

**REJECT**

This manuscript in its current form is not suitable for publication in Physical Review D. The work is predicated on a physical "prediction" that is not derived, relies on non-public data from a futuristic, non-existent analysis, and presents MCMC results that are internally inconsistent and misleading. These issues are not cosmetic; they undermine the entire scientific basis of the paper. A complete overhaul, starting from a rigorous first-principles derivation of the physics and using only currently available public data, would be required. This would constitute a new submission.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a second, more rigorous review of the paper.

---
### NEW Findings

**P2-M4: Misleading "Order-Unity" Claim in Figure Caption**
*   **Section/Page:** Figure 1 Caption, p. 4
*   **Problem:** The caption states that the posterior is "consistent with order-unity natural values." This is a misleading hedge. While the product `C_aγ × θ_i` is `3.4 ± 1.1`, the 1D marginalized posterior for the anomaly coefficient `C_aγ` (shown in the figure title as `13.4 ± 11.6`) is clearly not centered on an order-unity value. The data, in the context of this model, prefer a value for `C_aγ` of `~10` or larger. The caption misrepresents the MCMC results and conceals a tension with the paper's central "naturalness" argument, which assumes all dimensionless inputs are `O(1)`.
*   **Required Fix:** The caption must be revised to accurately reflect the posterior distributions. The tension between the "naturalness" assumption and the posterior for `C_aγ` should be acknowledged and discussed in the main text.

**P2-M5: Abstract Misrepresents Data Support for Model's Mass Scale**
*   **Section/Page:** Abstract, p. 1
*   **Problem:** The abstract presents `m ~ H_0` as a key feature of the model, claiming it is a "natural" choice that "ensures the field is rolling today." This implies that this mass scale is consistent with the data. However, the paper's own MCMC analysis (Figure 1) contradicts this. The 1D posterior for `log10(m_a/eV)` is peaked at the upper boundary of the prior (`-30`), far from the value corresponding to `H_0` (`log10(m/eV) ≈ -32.7`). This indicates the data prefer a mass *higher* than `H_0`, and the result is entirely prior-dependent (as noted in P2-M2). The abstract's claim that the data are accommodated by an `m ~ H_0` ALP is not supported by the results presented.
*   **Required Fix:** The abstract must be rewritten to reflect the actual results of the MCMC analysis regarding the mass. The claim that the `m ~ H_0` scale is supported by the data must be removed or substantially weakened and qualified.

**P2-m2: Out-of-Place and Self-Promotional Claim**
*   **Section/Page:** Sec. 6, p. 5
*   **Problem:** The Discussion section abruptly introduces a highly specific prediction for primordial non-Gaussianity, `f_NL = -35/8`, citing only another of the author's (futuristic) papers. This claim is presented without any context, derivation, or connection to the main topic of birefringence. It is extraneous to the paper's argument and appears to be included primarily for self-promotion.
*   **Required Fix:** This sentence should be removed. The discussion should remain focused on the results and implications of the birefringence analysis.

**P2-m3: Inconsistent Parameter Naming in Abstract**
*   **Section/Page:** Abstract, p. 1
*   **Problem:** The abstract introduces the decay constant as `f_a ~ M_Pl` but then presents a constraint on an "effective photon coupling `f_photon`". The relation between `f_a` and `f_photon` is never defined, creating confusion for the reader from the outset. This is an extension of the issue noted in P2-M1.
*   **Required Fix:** Use consistent and well-defined parameters in the abstract. Either define `f_photon` in terms of `f_a` in the abstract itself or, preferably, present the constraint in terms of the fundamental model parameters.