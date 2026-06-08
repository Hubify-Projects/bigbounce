# P2 auto-2026-06-08_1424pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (2960 chars)
**Wall time**: 128.1s

---

**Referee Report for Physical Review D**

**Manuscript Title:** Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts
**Author:** Houston Golden

This paper presents a model of cosmic birefringence from a spectator axion-like particle (ALP) with a Planck-scale decay constant (f_a ~ M_Pl) and a Hubble-scale mass (m ~ H_0). The author claims this setup naturally predicts a birefringence angle β ≈ 0.27°, consistent with current measurements from Planck and ACT. The paper provides a Bayesian analysis of the model and forecasts the constraining power of the future LiteBIRD satellite.

While the topic is timely and of significant interest to the cosmology community, the manuscript in its current form suffers from several critical flaws that preclude its publication in Physical Review D. The issues range from a fundamental lack of novelty and an opaque, seemingly incorrect central derivation to a misrepresentation of the paper's own statistical results and an unprofessional reliance on hypothetical future references.

A detailed list of required revisions follows.

---
### Detailed Findings

#### ESSENTIAL Revisions

**P2-E1: Lack of Novelty**
*   **Section/Page:** Section 6, page 5.
*   **Problem:** The paper's central physical claim—that an ALP with f_a ~ M_Pl and m ~ H_0 can naturally generate a birefringence angle β ~ 0.3°—appears to have been established in prior work. The manuscript cites Fujita et al. (2021, PRD 103, 043509), whose abstract states: "If the axion has a mass of m_φ ~ 10⁻³³ eV ~ H_0 and a decay constant of f_φ ~ M_Pl, the rotation angle can be of the order of 0.1 degrees". This is the core physical result of the present manuscript. The author's claimed contribution is "the specific parameter identification... and the inference framework." This is not sufficient for a new publication in PRD, especially when the original work is not adequately discussed or built upon in a substantial way. The paper reads as a rediscovery of a known result.
*   **Required Fix:** The author must clearly and prominently state what precisely is new in this work compared to Fujita et al. (2021). The introduction and discussion must be rewritten to place the current work in the proper context of existing literature. If the only contribution is a straightforward Bayesian analysis of a known model, the paper is likely not suitable for PRD and may be better as a shorter letter or comment, if at all.

**P2-E2: Opaque and Inconsistent Derivation of the Main Prediction**
*   **Section/Page:** Section 2.2, page 2.
*   **Problem:** The derivation of the main prediction, β ≈ 0.27°, is critically flawed.
    1.  Equation (1) for the field displacement Δφ includes a Bessel function term, `(1 - J_0(m/H_0))`, without any derivation or citation. This is a non-standard result for axion dynamics and must be rigorously derived from the Klein-Gordon equation in a ΛCDM background.
    2.  The text contains a direct contradiction. The author states that for m/H_0 ~ 1, the factor `1 - J_0(m/H_0) ≈ 0.24`. With θ_i ~ 1, this implies Δφ/f_a ≈ 0.24. However, the text immediately following Equation (2) claims "the cosmological field evolution gives Δφ/f_a ~ 10⁻²". These two values differ by an order of magnitude.
    3.  Using the derived formula β = (C_0 θ_i / 2) * (1 - J_0(m/H_0)) with O(1) inputs and the calculated value of 0.24 for the parenthesis yields β ≈ 0.12 radians ≈ 7°, which is inconsistent with the claimed 0.27°. The entire quantitative basis of the paper is therefore unsubstantiated.
*   **Required Fix:** Provide a complete, step-by-step derivation of the field displacement Δφ from first principles, starting from the equation of motion for the ALP field in an expanding universe. All approximations must be justified. The numerical inconsistency must be resolved, and the final prediction for β must follow transparently from the derived equations and input parameters.

**P2-E3: Misrepresentation of MCMC Results for the ALP Mass**
*   **Section/Page:** Section 5 and Figure 1, page 4.
*   **Problem:** The MCMC results presented in Figure 1 are misrepresented in the text and figure labels. The 1D posterior for the ALP mass, log10(m_a/eV), clearly peaks near -33.2. However, the marginalized constraint is quoted as `log10(m_a/eV) = -31.4 ± 1.2`. This value is far in the tail of the distribution and is a poor summary of the posterior, which is highly non-Gaussian. This misleads the reader into believing the data prefer a mass more than an order of magnitude larger than H_0 (log10(H_0/eV) ≈ -32.6), which undermines the paper's central "m ~ H_0" naturalness argument.
*   **Required Fix:** The summary statistics for non-Gaussian posteriors must be chosen carefully. Report the posterior mode or median in addition to, or instead of, the mean. The text must be revised to accurately reflect what the posterior implies about the preferred value of the ALP mass and its consistency with the H_0 scale. The current presentation is unacceptable.

#### MAJOR Revisions

**P2-M1: Use of Hypothetical and Future-Dated References**
*   **Section/Page:** Throughout, especially Abstract, Sections 3.1, 6, and References.
*   **Problem:** The paper is dated "March 20, 2026". It repeatedly cites papers with publication dates of 2025 and 2026, including the key ACT DR6 data source "[Diego-Palazuelos and Komatsu, 2025]", a work on ALP mass constraints "[Namikawa et al., 2025]", and the author's own companion papers "[Golden, 2026a]" and "[Golden, 2026b]". A scientific paper submitted for peer review cannot be based on data, analyses, or theoretical work that do not yet exist. This practice is unprofessional and invalidates the scientific basis of the claims.
*   **Required Fix:** The paper must be rewritten to rely only on publicly available data and peer-reviewed publications or public preprints (e.g., on arXiv). All future-dated and hypothetical references must be removed. The analysis must be re-run using only existing, citable data. The date of the manuscript must be corrected.

#### MINOR Revisions

**P2-m1: Inconsistent Observational Inputs**
*   **Section/Page:** Section 3.1, page 2.
*   **Problem:** The paper uses two different observational constraints for β. For the summary-likelihood calculation in Eq. (4), it combines the Planck NPIPE and a hypothetical ACT DR6 result. For the MCMC analysis, it uses a different value, "the Eskilt et al. joint analysis value β_obs = 0.342 ± 0.094°". While these values are consistent, the choice to use different inputs for different parts of the analysis is confusing and not well-justified.
*   **Required Fix:** Use a single, consistent, and properly cited observational constraint for β throughout the entire paper. Justify the choice of this constraint.

**P2-m2: Undefined Parameter `f_photon`**
*   **Section/Page:** Section 3.2, page 2.
*   **Problem:** Equation (5) presents a constraint on an "effective photon coupling parameter" `f_photon × C_0`. The parameter `f_photon` is never defined in the text, making the equation and its interpretation impossible to follow.
*   **Required Fix:** Clearly define all parameters used in the paper. If `f_photon` is a new parameter, explain its physical meaning and relation to the model's fundamental parameters (e.g., f_a). If it is a typo, correct it.

**P2-m3: Understated Bayes Factor Interpretation**
*   **Section/Page:** Section 3.4, page 3.
*   **Problem:** The paper reports a Bayes factor of ln B = 5.17 and describes it as "indicative evidence". On the commonly used Jeffreys scale, ln B > 5 constitutes "very strong" evidence. The term "indicative" is an unnecessary and potentially misleading understatement.
*   **Required Fix:** Use standard terminology to describe the strength of the evidence as indicated by the Bayes factor (e.g., "strong" or "very strong" on the Jeffreys scale), while retaining the important caveat about prior dependence.

**P2-m4: Out-of-Place Reference to a Companion Paper**
*   **Section/Page:** Section 6, page 5.
*   **Problem:** The discussion includes the sentence: "The matter-bounce non-Gaussianity f_NL = -35/8 provides a complementary and independent test [Golden, 2026b]." This feels like an advertisement for the author's other work and is not directly relevant to the analysis of birefringence presented in this manuscript.
*   **Required Fix:** Remove this sentence to maintain the focus of the paper.

---
## Summary recommendation

**REJECT**

This manuscript cannot be accepted in its present form. The combination of a fundamental lack of novelty, a missing and self-contradictory derivation for its central claim, and a clear misrepresentation of its own statistical results constitutes a set of fatal flaws. Furthermore, the reliance on non-existent, future-dated references falls far below the professional standards expected for a submission to Physical Review D. A complete overhaul of the paper, starting with a rigorous derivation and a frank assessment of its contribution relative to existing literature, would be required before it could be reconsidered for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a second, more detailed review of the manuscript.

---
### Additional Findings

#### ESSENTIAL Revisions

**P2-E4: Unsubstantiated and Arithmetically Inconsistent Quantitative Results**
*   **Section/Page:** Section 2.2 and 3.2, page 2.
*   **Problem:** The quantitative core of the paper, which connects the ALP model to the predicted and constrained values, appears to be arithmetically broken.
    1.  The text following Eq. (2) claims "the cosmological field evolution gives Δφ/f_a ~ 10⁻²". This is in direct contradiction with the value implied by Eq. (1) for the paper's own inputs (m/H₀ ~ 1, θᵢ ~ 1), which gives Δφ/f_a ≈ 1 - J₀(1) ≈ 0.24. This is a discrepancy of a factor of 24, and it invalidates the subsequent derivation of β ≈ 0.27°.
    2.  The constraint on the "effective photon coupling parameter" in Eq. (5), `f_photon × C_0 = 1.73 ± 0.44`, cannot be reproduced from the other numbers presented in the paper. The parameter `f_photon` is undefined, and the numerical value does not seem to follow from the model relation `β = (C_0 Δφ) / (2 f_a)` combined with the reported MCMC results for β.
*   **Required Fix:** The author must provide a complete and arithmetically self-consistent derivation of all quantitative results. The contradiction in the value of Δφ/f_a must be resolved. The origin and derivation of the constraint in Eq. (5) must be explicitly shown, including a clear definition of all parameters. As it stands, the paper's central claims are not supported by its own calculations.

#### MAJOR Revisions

**P2-M2: Abstract Misrepresents Key Findings**
*   **Section/Page:** Abstract, page 1.
*   **Problem:** The abstract's primary claim is that the proposed ALP model "naturally accommodates a birefringence rotation angle β ≈ 0.27°". This is presented as a solid prediction. However, as detailed in P2-E2 and P2-E4, the derivation of this value in the main text is opaque, self-contradictory, and unsubstantiated. The abstract is therefore not a faithful summary of what has been demonstrated in the paper. It presents a flawed or incomplete calculation as a robust scientific result.
*   **Required Fix:** The abstract must be rewritten to accurately reflect the (corrected) results in the manuscript. If the central prediction cannot be rigorously derived and justified, it cannot be presented as the key finding of the work.

#### MINOR Revisions

**P2-m5: Inconsistent Model/Run Labeling**
*   **Section/Page:** Section 3.3 and Figure 2, pages 3 and 5.
*   **Problem:** The MCMC configurations are referred to as "Run 1", "Run 2", and "Run 3" in the text (Sec. 3.3) and Table 1. However, in the legend of Figure 2, they are labeled "Model 2", "Model 2b", and "Model 0", respectively. This inconsistent labeling is confusing for the reader.
*   **Required Fix:** Use a single, consistent naming scheme for the different analysis configurations throughout the text, tables, and figures.