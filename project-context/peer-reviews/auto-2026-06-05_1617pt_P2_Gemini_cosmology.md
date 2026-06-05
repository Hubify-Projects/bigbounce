# P2 auto-2026-06-05_1617pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 122.4s

---

**Referee Report for PRD Manuscript**

**Manuscript Title:** Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts
**Author:** Houston Golden

This paper presents a simple axion-like particle (ALP) model with a Planck-scale decay constant and a Hubble-scale mass as a "natural" explanation for the cosmic birefringence signal observed in Planck and ACT data. The author performs a summary-likelihood and MCMC analysis to constrain the model and provides forecasts for the LiteBIRD satellite.

The topic is timely and of interest to the cosmology community. The paper is concise and well-structured. However, I have identified several essential and major issues related to the core theoretical prediction and the interpretation of the statistical results that prevent me from recommending publication in its current form. The issues must be addressed in a major revision.

---
### Detailed Findings

#### ESSENTIAL

**P2-E1: Inconsistent derivation of the central prediction (Section 2.2, Page 2)**
The paper's central claim is a prediction of β ≈ 0.27°. The derivation of this value is opaque and appears to be internally inconsistent.
- **Problem:** Equation (1) gives the field displacement as Δφ ≈ f_a θ_i (1 - J₀(m/H₀)). For m/H₀ ~ 1 and θ_i ~ 1, this implies a dimensionless displacement Δφ/f_a ≈ 1 - J₀(1) ≈ 0.24. However, a few lines later, the text states, "the cosmological field evolution gives Δφ/f_a ~ 10⁻²". This value is then used to derive the final prediction β ≈ 0.27°. There is an unexplained discrepancy of a factor of ~24 between the result implied by Equation (1) and the value used in the subsequent calculation. This invalidates the paper's core quantitative claim.
- **Required Fix:** The author must provide a clear, step-by-step derivation of the field displacement Δφ/f_a. If Equation (1) is an incorrect or misleading approximation, it must be removed or corrected. The origin of the Δφ/f_a ~ 10⁻² value must be explicitly shown, for example, by referencing the specific calculation in the literature (e.g., Fujita et al. 2021) and demonstrating how it applies here. The entire section needs to be rewritten for clarity and correctness.

**P2-E2: Undefined parameter and unexplained result in likelihood analysis (Section 3.2, Page 2)**
Equation (5) presents a constraint on a quantity that is never defined in the paper.
- **Problem:** Equation (5) states: `fphoton × Co = 1.73 ± 0.44`. The parameter `fphoton` is not defined anywhere in the text. It is impossible for the reader to understand what this quantity represents, how it was derived from the data, or what its physical significance is.
- **Required Fix:** This equation and the corresponding text must be removed. If it represents a meaningful physical quantity, the parameter `fphoton` must be rigorously defined, and the derivation of the constraint must be explained in full. Given the lack of context, removal seems most appropriate.

#### MAJOR

**P2-M1: Tension between the "naturalness" claim and MCMC results (Section 3.3, Section 5, Figure 1)**
The paper's central thesis is that a "natural" model with m ~ H₀ and O(1) couplings fits the data. However, the author's own MCMC results contradict this simple picture.
- **Problem:** The MCMC analysis (Figure 1) shows a posterior for the ALP mass peaked at log₁₀(mₐ/eV) = -31.4, which corresponds to mₐ ≈ 30 H₀, significantly larger than the "natural" value of H₀. To compensate for the suppressed field evolution at this higher mass, the fit requires a larger coupling-misalignment product, Cₐᵧ × θᵢ = 3.4 ± 1.1 (Equation 8), which is larger than the O(1) value of ~1.2 implied by the m ~ H₀ scenario. The paper fails to acknowledge or discuss this clear tension. Instead, it repeatedly claims the model is "natural" and "consistent" without qualification.
- **Required Fix:** The author must explicitly discuss the tension between the simple m ~ H₀ prediction and the parameter region preferred by the MCMC fit. The abstract, discussion, and conclusion must be revised to reflect this nuance. The claim of "naturalness" is significantly weakened by the data's preference for mₐ > H₀ and should be toned down accordingly. The paper should discuss why the data might prefer this region of parameter space.

**P2-M2: Misleading caption for Figure 1 (Page 4)**
The caption for the main results plot makes a claim that is not well-supported.
- **Problem:** The caption for Figure 1 states that the posterior for Cₐᵧ × θᵢ is "consistent with order-unity natural values." While 3.4 is technically O(1), it is on the high end, and this statement glosses over the important physical context identified in P2-M1: this value is required because the mass is simultaneously driven away from its "natural" H₀ scale. The statement is therefore misleading.
- **Required Fix:** The caption should be rewritten to be more precise. It should note the value of the product and point out the degeneracy with the mass, which is explored in the main text (once P2-M1 is addressed). For example: "The posterior for the product Cₐᵧ × θᵢ is constrained to 3.4 ± 1.1. The visible degeneracy with the mass mₐ shows that larger masses, which suppress the field's evolution, are compensated by a larger coupling product to fit the observed birefringence angle."

#### MINOR

**P2-m1: Citing a paper "in preparation" (Section 6, Page 6)**
The paper cites a work in preparation to support a claim of superiority.
- **Problem:** The text states that "Namikawa, Murai & Naokawa [Namikawa et al., 2025] provide superior ALP mass constraints using the full Planck EB spectrum." The reference is listed as "In preparation." Citing a non-public work, especially to claim it is "superior," is not best practice.
- **Required Fix:** The author should either remove the claim of superiority or rephrase to state that other methods (like full EB spectrum analysis) are expected to yield stronger constraints, and cite the paper only once it is publicly available on the arXiv.

#### NIT

**P2-N1: Understating the Bayes factor evidence (Abstract, Page 1)**
The abstract describes a Bayes factor of ln B = 5.17 as "indicative."
- **Problem:** On the commonly used Jeffreys scale, ln B > 5 constitutes "very strong" evidence. While being conservative is not a flaw, using standard terminology would be clearer.
- **Required Fix:** Consider changing "indicative" to "strong" or "very strong" evidence, while noting the prior-dependence as is already done in the main text.

**P2-N2: Ambiguous coupling definition (Section 2.2, Page 2)**
The ALP-photon coupling is defined in a non-standard way that could cause confusion.
- **Problem:** The text defines gₐᵧ = C₀/fₐ. The standard definition in the literature is gₐᵧ = (αₑₘ / 2πfₐ) × Cₐᵧ, where Cₐᵧ is the anomaly coefficient. It is unclear how C₀ relates to Cₐᵧ.
- **Required Fix:** The author should briefly clarify the definition of C₀ and its relationship to the standard anomaly coefficient to aid readers familiar with the literature.

---
## Summary recommendation
**MAJOR REVISIONS**

The paper addresses a compelling and topical question: whether a simple, natural ALP model can explain the observed cosmic birefringence. The core idea is appealing. However, the manuscript in its current form suffers from a critical flaw in its central theoretical derivation (P2-E1) and a significant disconnect between its "naturalness" claims and its own statistical results (P2-M1). These issues undermine the paper's primary conclusions.

Before this paper can meet the standards of Physical Review D, the author must provide a correct and transparent derivation of the predicted birefringence angle and thoroughly address the tension between the simple model and the MCMC posteriors. The claims throughout the paper must be revised to accurately reflect what the analysis actually shows. If these substantial issues can be satisfactorily resolved, a revised version of the paper could be a valuable contribution.