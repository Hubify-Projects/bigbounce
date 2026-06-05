# P2 R10v3 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API)
**Wall time**: 54.5s

---

**Referee Report on "Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts"**

This manuscript presents a model of cosmic birefringence from a spectator axion-like particle (ALP) with a Planck-scale decay constant and a Hubble-scale mass. The author claims this setup naturally produces a birefringence angle consistent with recent measurements from Planck and ACT, and provides forecasts for the LiteBIRD satellite. The paper combines a theoretical prediction with a summary-likelihood and MCMC analysis of current data.

The topic is timely and of significant interest to the cosmology community. The paper is well-structured, concise, and presents its data analysis and future forecasts clearly. The discussion of systematic uncertainties and the acknowledgment of prior work are commendable. However, there are several critical issues, primarily concerning the derivation of the central theoretical prediction, that must be addressed before the paper can be considered for publication.

**ESSENTIAL Revisions**

*   **P2-E1:** Section 2.2, Page 2. The derivation of the main prediction, `β ≈ 0.27°`, is critically flawed or at least insufficiently explained. The text states that the field displacement is `Δφ/f_a ≈ θ_i (1 - J_0(m/H_0))`, and that for `m/H_0 ~ 1` and `θ_i ~ 1`, this gives `Δφ/f_a ≈ 0.24`. This is correct. However, the text then immediately claims that "the cosmological field evolution gives `Δφ/f_a ~ 10^-2`" and uses this much smaller value to derive `β ≈ 0.27°`. This is a direct contradiction. The factor of `~24` difference between the analytical estimate and the value used for the final prediction is not explained.
    *   **Required Fix:** The author must provide a complete and transparent derivation for the value of `Δφ/f_a` used in the prediction. If this value comes from a numerical integration of the field's equation of motion, the setup and results of that integration must be presented (e.g., in an appendix). The discrepancy with the analytical `J_0` approximation must be explained. Without this, the central claim of a "natural" prediction is unsubstantiated.

**MAJOR Revisions**

*   **P2-M1:** Section 3.2, Page 2, Equation (5). The paper introduces and provides a constraint on an "effective photon coupling parameter" `f_photon × C_0 = 1.73 ± 0.44`. The parameter `f_photon` is not defined anywhere in the text. The standard ALP-photon coupling is `g_aγ = C_0 / f_a`. It is unclear how `f_photon` relates to the model parameters (`f_a`, `m`, `θ_i`, `C_0`).
    *   **Required Fix:** The author must define `f_photon` explicitly in terms of the fundamental ALP model parameters. The derivation of Eq. (5) from the measurement of `β` must be shown. If `f_photon` is simply a reparameterization, this should be stated and justified. As it stands, Eq. (5) is not interpretable.

**MINOR Revisions**

*   **P2-m1:** Throughout the paper. The manuscript is dated "March 20, 2026", and several key references are cited for future years (2025, 2026a, 2026b). While placeholder dates are common in drafts, for a journal submission this is inappropriate.
    *   **Required Fix:** The date of submission should be corrected. All cited works, especially those that are central to the paper's context (e.g., the ACT DR6 data and the companion papers), must be publicly available, at least as preprints on a service like arXiv. The references should be updated with the correct dates and identifiers (e.g., arXiv numbers).

*   **P2-m2:** Section 2.2, Page 2. The text leading to the final prediction `β ≈ 0.27°` is confusing. It states that `Δφ/f_a ~ 10^-2` is "from the ratio of field displacement to decay constant over the Hubble time". This phrasing is tautological and uninformative.
    *   **Required Fix:** This sentence should be rewritten to be physically precise. It should explain *why* the dimensionless field displacement takes the value it does, connecting it to the underlying dynamics (this is related to point P2-E1).

**NIT (Cosmetic)**

*   **P2-N1:** Section 2.2, Page 2, Equation (2). The final part of the equation, `β ≈ C_0 θ_i / 2 × O(1)`, is imprecise. While technically correct, it obscures the physics. The `O(1)` factor is the result of a specific cosmological evolution.
    *   **Required Fix:** It would be clearer to write the expression explicitly in terms of the physical parameters, for example, `β = (C_0 θ_i / 2) * f(m/H_0)`, where `f(m/H_0)` is the function resulting from the cosmological integration (e.g., `1 - J_0(m/H_0)` in the approximation, or the numerically-derived factor of `~10^-2 / θ_i`).

## Summary recommendation
**MAJOR REVISIONS**

The paper presents a potentially interesting and natural explanation for the observed cosmic birefringence signal. The data analysis is presented clearly, and the future forecast for LiteBIRD correctly highlights the model's falsifiability. However, the paper's central theoretical claim rests on a numerical value (`Δφ/f_a ~ 10^-2`) that is not derived and contradicts the analytical approximation provided in the same section. This is a critical omission that undermines the entire argument for the model's "naturalness". Furthermore, a key result is presented in terms of an undefined parameter. If the author can provide a rigorous and transparent derivation for the predicted birefringence angle and clarify the parameter definitions, the manuscript could become a valuable contribution. As it stands, it does not meet the standards for publication.