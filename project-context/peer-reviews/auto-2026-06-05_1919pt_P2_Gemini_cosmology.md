# P2 auto-2026-06-05_1919pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 1328.8s

---

Here is the referee report.

---
## Referee Report for PRD Manuscript

**Manuscript ID:** [Assigned by system]
**Title:** Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts
**Author:** Houston Golden

This paper presents a theoretical model and statistical analysis of cosmic birefringence, attributing the observed signal to a spectator axion-like particle (ALP) with a Planck-scale decay constant and a Hubble-scale mass. The author argues that this model "naturally" predicts a rotation angle consistent with current data from Planck and ACT, and provides forecasts for the LiteBIRD satellite.

While the topic is timely and of significant interest to the cosmology community, the manuscript in its current form contains several fundamental errors, internal contradictions, and a lack of rigor that prevent it from meeting the publication standards of Physical Review D. The core claims of the paper are not substantiated by the analysis presented. I recommend rejection, but the author may consider a full rewrite and resubmission after addressing the critical issues outlined below.

### ESSENTIAL Revisions

**P2-E1: Section 2.2 (p. 2) — Fatal Contradiction in the Central Prediction**
The paper's central claim is a "natural" prediction of β ≈ 0.27°. The derivation of this value is critically flawed and internally contradictory.
*   **Problem:** The text in Section 2.2 states, "the cosmological field evolution gives Δφ/fa ~ 10⁻²". This value is used to derive β ≈ 0.27°. However, Equation (1) on the same page gives the field displacement as Δφ ≈ f_a θ_i (1 - J₀(m/H₀)). For the model's parameters (θ_i ~ 1, m/H₀ ~ 1), this yields Δφ/f_a ≈ 1 - J₀(1) ≈ 0.24. This value is more than 20 times larger than the 10⁻² value used in the subsequent derivation. This contradiction invalidates the entire quantitative argument for the β ≈ 0.27° prediction and collapses the "naturalness" claim.
*   **Required Fix:** The author must provide a complete, correct, and self-consistent derivation for the predicted value of β. This will require a thorough revision of Section 2. The current argument is incorrect. The author should carefully follow and cite established literature on this calculation (e.g., Fujita et al. 2021, which the paper cites elsewhere).

**P2-E2: Abstract (p. 1) & Section 3.2 (p. 2) — Undefined Parameter and Opaque Result**
The paper presents a constraint on an "effective photon coupling parameter" that is never defined.
*   **Problem:** The abstract and Equation (5) state a result: "fphoton × C₀ = 1.73 ± 0.44". The parameter `fphoton` is not defined anywhere in the manuscript, making this statement and its claimed "order-unity" nature completely meaningless. It is impossible for the reader to understand what has been constrained or how it was derived from the birefringence angle β.
*   **Required Fix:** This result must be removed entirely. Alternatively, the author must provide a precise definition for `fphoton`, show a full derivation of how the combination `fphoton × C₀` is related to β, and justify its physical importance.

**P2-E3: Section 3.3 (p. 3) & Figure 1 (p. 4) — Gross Inconsistency in MCMC Results**
The reported results from the MCMC analysis are mutually exclusive.
*   **Problem:** Equation (8) reports the posterior for the product of the coupling and misalignment angle as "C_aγ × θ_i = 3.4 ± 1.1", based on "Run 2, C free". However, Figure 1, which the caption states is from the *same run*, shows marginalized posteriors of θ_i = 1.33 ± 0.44 and C_aγ = 13.4 ± 11.6. The product of these central values is 1.33 × 13.4 ≈ 17.8, which is completely inconsistent with 3.4. This indicates a profound error in either the analysis code, the post-processing, or the reporting of results.
*   **Required Fix:** The author must find and correct this error. The text, equations, and figures reporting on the MCMC results must be made fully consistent. The current discrepancy invalidates the entire inference part of the paper.

**P2-E4: Abstract (p. 1) & Section 3.1 (p. 2) — Unverifiable Source for Primary Data**
The paper's main observational constraint relies on a data point whose source is not clearly and correctly cited.
*   **Problem:** The paper uses β_obs = 0.342 ± 0.094° for its MCMC analysis and as the primary point of comparison. This value is attributed to an "Eskilt et al. joint Planck + ACT analysis". However, the cited paper, Eskilt and Komatsu (2022), contains a Planck+WMAP analysis and reports a different value (β = 0.30 ± 0.11°). A verifiable and correct citation for the 0.342 ± 0.094° value must be provided. Without it, the paper's main observational input is unsubstantiated.
*   **Required Fix:** Provide a precise and correct citation (journal reference or public arXiv link) for the joint analysis value β_obs = 0.342 ± 0.094°. If this value is a custom combination performed by the author, the methodology must be described and justified in detail.

### MAJOR Revisions

**P2-M1: Throughout — Unsubstantiated "Naturalness" and "No Fine-Tuning" Claims**
The central narrative of the paper—that the model is "natural" and requires "no fine-tuning"—is not well-supported.
*   **Problem:** This claim hinges on the flawed derivation (E1). Furthermore, the MCMC results in Figure 1 show a posterior for the coupling C_aγ peaking at ~13, with a long tail to the prior boundary at 30. A value of 13 is not "order-unity" in the typical sense used for anomaly coefficients. This suggests the data may prefer a larger coupling than the "natural" O(1) value, which would constitute a form of tuning.
*   **Required Fix:** The author must re-evaluate all claims of "naturalness" and "no fine-tuning" in light of a corrected theoretical derivation and consistent MCMC results. These claims should be significantly tempered or removed unless a much more robust argument can be made.

**P2-M2: Section 2.1 (p. 1) — Missing Derivations and Citations for Key Physics**
The paper presents key physical results without proper context or citation.
*   **Problem:** Equation (1) presents the solution for the ALP field displacement involving a Bessel function (J₀). This is a non-trivial result from solving the equation of motion in an expanding universe. It is presented without any derivation or citation to the original literature where this solution was derived.
*   **Required Fix:** The physical origin of this equation must be explained, and appropriate citations to seminal works (e.g., Carroll 1998, or a modern review like Marsh 2016) must be added.

### MINOR Revisions

**P2-m1: Title Page (p. 1) — Future Date**
*   **Problem:** The paper is dated "March 20, 2026".
*   **Required Fix:** Correct the date to the date of submission.

**P2-m2: References (p. 6) — Reliance on Future/In-Preparation Work**
*   **Problem:** The analysis relies on two preprints dated 2025 and cites another work as "in preparation". This makes the paper's foundations difficult to verify.
*   **Required Fix:** The author should confirm that the 2025 works are publicly available on arXiv. The "in preparation" citation should be replaced with a proper reference or the claim it supports should be removed.

**P2-m3: Throughout — Inconsistent Notation for Coupling Constant**
*   **Problem:** The ALP-photon coupling coefficient is denoted C₀ in Section 2.2 but C_aγ in Section 3.3 and Figure 1.
*   **Required Fix:** Use a single, consistent notation throughout the manuscript.

**P2-m4: Section 3.3 (p. 3) — Arbitrary Parameter Choice**
*   **Problem:** MCMC Run 1 is performed with the coupling fixed to C = 8. No justification is provided for this specific value.
*   **Required Fix:** Explain the motivation for choosing C=8 or remove this run if it is not essential to the argument.

**P2-m5: Section 6 (p. 5) — Irrelevant Mention of Non-Gaussianity**
*   **Problem:** The paragraph discussing matter-bounce non-Gaussianity (f_NL) is disconnected from the rest of the paper's content and reads as an advertisement for a companion paper.
*   **Required Fix:** Remove this paragraph to improve the focus and flow of the Discussion section.

### NITs

**P2-N1: Section 1 (p. 1) — Imprecise Introductory Formula**
*   **Problem:** The introduction gives the formula for the rotation angle as β = Δφ/(2f_a), which omits the dimensionless coupling constant.
*   **Required Fix:** For clarity and precision, write the formula as β = C₀ Δφ/(2f_a) or similar, consistent with the notation used later.

---
## Summary recommendation
**REJECT**

The manuscript addresses an important and exciting topic in modern cosmology. However, it is marred by a fatal contradiction in its central theoretical derivation, severe inconsistencies in the reporting of its analysis results, and a failure to properly cite the primary observational data it relies upon. These essential-level flaws undermine the entirety of the paper's scientific claims. The paper does not meet the standards of rigor and correctness expected for publication in Physical Review D. A complete overhaul of the theoretical calculations and data analysis sections would be necessary before the manuscript could be reconsidered for publication.