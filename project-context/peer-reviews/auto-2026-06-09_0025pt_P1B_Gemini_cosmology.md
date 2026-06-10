# P1B auto-2026-06-09_0025pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 718.2s

---

## Referee Report: Technical Verification Companion to the ECH Spin-Torsion Program

This manuscript presents technical verification material for a separate work (Paper I(a)) on Einstein-Cartan-Holst (ECH) cosmology. It documents three distinct numerical analyses: (1) a `ΛCDM+ΔNeff` MCMC analysis as a null-consistency test, (2) a `NaMaster` pipeline validation for cosmic birefringence measurements, and (3) a spectator-ALP model consistency check for observed cosmic birefringence.

The paper is commendable for its transparency regarding the scope and limitations of each analysis. The authors clearly state what is *not* being claimed (e.g., this is not a direct test of the ECH theory, not a competitive sky detection of birefringence) and provide excellent reproducibility materials. However, the paper suffers from a significant numerical error in a key table and a confusing structure that mixes results from different analyses, which must be addressed before publication.

### ESSENTIAL

*   **P1B-E1: Incorrect variance calculation in Table II.**
    *   **Section:** Table II, footnote b (Page 4)
    *   **Problem:** The footnote attempts to reproduce the uncertainty on `w_pivot` (±0.0301) from the uncertainties on `w_0` and `w_a`. The provided formula, `σ_wpivot^2 = σ_w0^2 + (1-ap)^2 σ_wa^2`, is only valid if `w_0` and `w_a` are uncorrelated, which they are not. Furthermore, the numerical evaluation of this incorrect formula is also wrong: `(0.0436)^2 + (0.3320)^2 * (0.1864)^2 = 0.00190 + 0.00382 = 0.00572`, whereas `(0.0301)^2 = 0.000906`. The calculation is off by a factor of ~6.
    *   **Required Fix:** The authors must provide the correct formula for the propagation of errors for correlated variables: `σ_wpivot^2 = σ_w0^2 + (1-ap)^2 σ_wa^2 + 2(1-ap)Cov(w_0, w_a)`. They should then use the actual covariance `Cov(w_0, w_a)` from their MCMC chain to demonstrate that the calculation correctly reproduces the quoted `σ_wpivot = 0.0301`. Alternatively, if the provided `a_p` is indeed the value that decorrelates the parameters, the definition and resulting variance calculation must be clarified and corrected. This is a critical error in a central results table and must be fixed.

### MAJOR

*   **P1B-M1: Confusing paper structure mixing unrelated analyses.**
    *   **Section:** III and V (Pages 3-4, 6)
    *   **Problem:** Section III is titled "Stock-CAMB ΛCDM+ΔNeff MCMC". However, midway through the section, under "Physics interpretation (Table II)", it abruptly switches to discussing results from a completely different `w_0w_a` model run using different datasets (DESI DR2). This makes the paper extremely difficult to follow. The `w_0w_a` analysis is a significant piece of work in its own right and should not be buried without context inside the `ΔNeff` section.
    *   **Required Fix:** The paper needs significant restructuring for clarity. The `w_0w_a` analysis should be presented in its own dedicated section with a proper introduction explaining its motivation and connection to the overall program. The current Section III should focus exclusively on the `ΔNeff` proxy test and Table I. The current Section V ("Cosmological Fits and Model Comparison") is too generic and should be broken up or rewritten to clearly delineate the different analyses being discussed.

*   **P1B-M2: Missing `θ_i^2` dependence in backreaction scaling relation.**
    *   **Section:** VI, footnote 5 (Page 7)
    *   **Problem:** The footnote discusses the ALP backreaction, stating the scaling `Ω_a ~ ρ_a/ρ_crit ~ (m^2 f_a^2 / H_0^2 M_Pl^2)`. This is incorrect. The energy density of a coherently oscillating scalar field scales as `ρ_a ~ m^2 φ^2 ~ m^2 (f_a θ_i)^2`. The expression is missing the crucial `θ_i^2` dependence. While the subsequent text correctly uses this dependence to calculate the 25x fine-tuning factor, the formula itself is wrong.
    *   **Required Fix:** Correct the formula to `Ω_a ~ (m^2 f_a^2 θ_i^2) / (H_0^2 M_Pl^2)` or a similar expression that correctly reflects the dependence on the initial misalignment angle.

### MINOR

*   **P1B-m1: Ambiguous sign on pipeline bias.**
    *   **Section:** IV and V (Pages 1, 6)
    *   **Problem:** The abstract states the pipeline bias is `0.032°`. The text in Section V (page 6) also states the bias is `0.032°`. However, the actual calculation is `β_rec - β_inj = 0.238° - 0.27° = -0.032°`. The sign is omitted. For the second case, the bias is `0.302° - 0.342° = -0.040°`.
    *   **Required Fix:** State the bias with the correct sign (e.g., `-0.032°`) or explicitly report the absolute value of the bias, e.g., `|β_rec - β_inj| = 0.032°`. Consistency is needed.

*   **P1B-m2: Typo in significance notation.**
    *   **Section:** VI (Page 7)
    *   **Problem:** The significance of the combined birefringence measurement in Eq. (4) is given as `(3.9)`. This is likely a typo.
    *   **Required Fix:** Change `(3.9)` to `3.9σ` for clarity and consistency with standard notation used elsewhere in the paper (e.g., `3.6σ`).

*   **P1B-m3: Internal-sounding language in conclusion.**
    *   **Section:** VIII (Page 8)
    *   **Problem:** The final sentence of the Spectator-ALP consistency summary reads: "...§VI for the explicit numerical derivation correcting the earlier Caγθi product)." This sounds like a note from a previous draft or a response to a previous review.
    *   **Required Fix:** Rephrase this to be more formal and self-contained for a published paper. For example: "...as shown by the explicit numerical derivation in §VI."

### NIT

*   **P1B-N1: Future date on manuscript.**
    *   **Section:** Title block (Page 1)
    *   **Problem:** The paper is dated "2026-06-08 PDT". This is a date in the future.
    *   **Required Fix:** Change this to the current submission date.

*   **P1B-N2: Inconsistent sample counts in Figure 2 caption.**
    *   **Section:** Figure 2 caption (Page 5)
    *   **Problem:** The caption lists "Full tension (175 545 samples)" and "Planck+BAO+SN (132 949 samples)". The full-tension sample count (175,545) does not match the value given in Table I (176,240). The difference is small (~0.4%) but should be consistent.
    *   **Required Fix:** Ensure all quoted sample counts for a given chain are consistent across all tables and figure captions.

## Summary recommendation
**MAJOR REVISIONS**

This manuscript provides a valuable and transparent technical summary of three numerical analyses supporting a larger research program. The commitment to reproducibility is a significant strength. However, the paper is marred by a critical numerical and formulaic error in Table II and a confusing structure that hinders readability. These issues must be thoroughly addressed. Once the calculation in Table II is corrected and the paper is restructured to present the `ΔNeff` and `w_0w_a` analyses in separate, clear sections, the manuscript will be much closer to the high standard expected for Physical Review D.