# P2 auto-2026-06-05_1418pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 117.6s

---

## Referee Report for PRD Submission

**Manuscript Title:** Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts
**Author:** Houston Golden

This paper presents a model of an axion-like particle (ALP) with a Planck-scale decay constant (`fa ~ M_Pl`) and a Hubble-scale mass (`m ~ H_0`) as a "natural" explanation for the tentative signal of cosmic birefringence observed in CMB data. The author performs a likelihood analysis using Planck and ACT data, finds consistency, and forecasts a high-significance detection by LiteBIRD.

While the topic is timely and the model is appealing in its simplicity, the paper suffers from several critical flaws that undermine its central claims of "naturalness" and predictive power. The derivation of the main theoretical prediction is opaque and appears to be numerically inconsistent, and the results of the author's own data analysis are in significant tension with the model's core assumptions. For these reasons, I cannot recommend the paper for publication in its current form.

---
### Detailed Findings

#### ESSENTIAL

**P2-E1: Section 2.2, Page 2 — The central prediction for the birefringence angle `β` is not rigorously derived and appears numerically inconsistent.**

The entire "naturalness" argument of the paper hinges on the prediction `β ≈ 0.27°` arising from `O(1)` inputs. This prediction is derived from Eq. (1) and (2). However, this derivation has two fatal problems:

1.  **Unjustified Formula:** Equation (1) for the field displacement, `Δφ ≈ f_a θ_i (1 - J_0(m/H_0))`, is presented without citation or derivation. The solution to the Klein-Gordon equation for an axion rolling in a matter/dark energy-dominated universe is non-trivial and does not typically yield a simple closed-form expression in terms of Bessel functions for the total displacement. This equation is the foundation of the paper's prediction and must be rigorously derived or cited from existing literature.

2.  **Numerical Inconsistency:** The author makes two contradictory claims about the key quantity `Δφ/f_a`.
    *   From Eq. (1), for `m/H_0 ~ 1` and `θ_i ~ 1`, the displacement is `Δφ/f_a ≈ θ_i (1 - J_0(1)) ≈ 0.24 θ_i`. This is a large displacement, `O(0.1)`.
    *   In the text immediately following Eq. (2), the author claims "the cosmological field evolution gives `Δφ/f_a ~ 10^-2`". This value is then used to calculate `β ≈ 0.27°`.

    These two values for `Δφ/f_a` differ by a factor of ~24. This is not an `O(1)` discrepancy; it is a fundamental contradiction. If the `~10^-2` value is correct, its origin must be shown. If the value from Eq. (1) is correct, the predicted angle would be `β ≈ 0.24 * C_0 θ_i / 2` radians, which is `~6.9°` for `C_0, θ_i ~ 1`, grossly inconsistent with the observed value. The central theoretical claim of the paper is therefore unsupported.

**P2-E2: Section 3.3 & Figure 1, Pages 3-4 — The MCMC results contradict the paper's "naturalness" premise of `m ~ H_0`.**

The paper's premise is that an ALP with `m ~ H_0` naturally explains the signal. However, the author's own MCMC fit, shown in Figure 1, yields a posterior for the mass of `log10(m_a/eV) = -31.4 ± 1.2`.

Let's compare this to the Hubble scale. `H_0 ≈ 67.4 km/s/Mpc ≈ 1.44 x 10^-33 eV`. This corresponds to `log10(H_0/eV) ≈ -32.84`. The best-fit mass from the author's analysis is `m_a ≈ 10^-31.4 eV`, while `H_0 ≈ 10^-32.84 eV`. The ratio is `m_a / H_0 ≈ 10^1.44 ≈ 27.5`.

The data, as analyzed by the author, therefore prefers a mass nearly 30 times larger than `H_0`. This result is in strong tension with the foundational claim that the `m ~ H_0` scale is the "natural" one. The paper cannot simultaneously claim the model is natural because `m ~ H_0` and present a fit that decisively disfavors this choice. The abstract, introduction, and discussion must be fundamentally rewritten to acknowledge that the data prefer a mass scale significantly different from `H_0`, which weakens the core "naturalness" argument.

#### MAJOR

**P2-M1: Section 3.2, Page 2 — The "effective photon coupling parameter" `f_photon` is undefined.**

Equation (5) introduces a parameter `f_photon` and constrains the product `f_photon × C_0 = 1.73 ± 0.44`. This parameter is not defined anywhere in the text, nor is its relationship to the fundamental ALP parameters (`f_a`, `m`, `θ_i`, `C_0`) explained. As a result, Eq. (5) is uninterpretable and its significance cannot be assessed. The author must explicitly define this parameter and show how it is derived from the birefringence angle `β`.

**P2-M2: Sections 2 & 3, Pages 2-3 — Inconsistent and ambiguous notation for the ALP-photon coupling.**

The paper uses `C_0` in Section 2.2 to denote the "order-unity coefficient from the ABJ anomaly". However, the MCMC analysis in Section 3.3 and Figure 1 uses the notation `C_aγ`. It is not stated whether these are the same parameter. Furthermore, the standard definition of the ALP-photon coupling is `g_aγ = (α / (2π f_a)) * C_aγ`, where `α` is the fine-structure constant. The paper uses a non-standard convention `g_aγ = C_0 / f_a`. This makes the physical interpretation of `C_0` (or `C_aγ`) ambiguous. Is it the integer-valued anomaly coefficient, or does it absorb other factors like `α/(2π)`? This must be clarified for the results to be reproducible and comparable to the wider literature.

#### MINOR

**P2-m1: Section 6, Page 5 — The discussion of non-Gaussianity is extraneous.**

The Discussion section mentions a non-Gaussianity prediction, `f_NL = -35/8`, and cites a companion paper. As the current paper explicitly states its results are "independent of bounce cosmology" (Section 5), this prediction from a specific bounce model is out of place and serves only to advertise other work. It should be removed from the discussion or confined to Section 5, where the connection to bounce cosmology is briefly motivated.

**P2-m2: Page 1 — The paper is dated for the future.**

The paper is dated "March 20, 2026". This should be corrected to the date of submission.

#### NIT

**P2-N1: Section 3.3, Page 3 — Minor notational inconsistency.**

The text refers to "Run 1, C = 8 fixed". Table 1 labels this "ALP (C = 8 fixed)". For clarity, the text and table should use consistent notation, for example by specifying which parameter is fixed (e.g., `C_aγ = 8`).

---
## Summary recommendation

**REJECT**

The paper in its current form is not suitable for publication in Physical Review D. The central theoretical prediction (P2-E1) is based on an unsubstantiated and numerically inconsistent calculation, which invalidates the claim of a sharp, natural prediction. Furthermore, the author's own analysis (P2-E2) shows that the data prefer a mass scale that is in significant tension with the model's "natural" `m ~ H_0` assumption. These two essential flaws undermine the entire foundation of the paper. Correcting them would require a complete re-derivation of the theoretical prediction and a fundamental reframing of the paper's claims and conclusions, which goes far beyond the scope of major revisions.