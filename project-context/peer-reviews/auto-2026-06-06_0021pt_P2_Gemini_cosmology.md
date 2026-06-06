# P2 auto-2026-06-06_0021pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 130.7s

---

**Referee Report: PRD Manuscript [Cosmic Birefringence from a Planck-Scale Axion-Like Particle]**

This paper presents a model of cosmic birefringence from a spectator axion-like particle (ALP) with a Planck-scale decay constant and Hubble-scale mass. The author claims this model naturally predicts a birefringence angle `β` consistent with recent observations from Planck and ACT. The paper includes a summary-likelihood analysis, MCMC parameter estimation, and forecasts for LiteBIRD.

While the topic is timely and of significant interest to the cosmology community, the manuscript in its current form contains several critical flaws that preclude its publication in Physical Review D. The central theoretical claim appears to be based on a flawed calculation, and the paper relies on non-public references, rendering its results unverifiable.

## Detailed Findings

### ESSENTIAL

**P2-E1 | Section 2.2, Page 2 | Contradictory and incorrect theoretical prediction**
*   **Problem:** The paper's central claim is that the proposed ALP model "naturally" predicts `β ≈ 0.27°`. This value requires the dimensionless field displacement `Δφ/f_a` to be `~ 10^-2`. The author states on page 2: "the cosmological field evolution gives `Δφ/fa ~ 10^-2`". However, Equation (1) on the same page, which purports to describe this displacement, gives `Δφ/f_a ≈ θ_i (1 - J_0(m/H_0))`. For the model's "natural" inputs (`θ_i ~ 1`, `m/H_0 ~ 1`), this evaluates to `Δφ/f_a ≈ 1 * (1 - 0.765) ≈ 0.24`. This result is 24 times larger than the value required to match observations and stated in the text. This fundamental contradiction invalidates the paper's primary claim of a natural prediction. The entire analysis rests on this incorrect premise.
*   **Required Fix:** The author must provide a correct, self-consistent derivation for `Δφ/f_a`. If the model with `O(1)` inputs indeed predicts `β ≈ 6-7°`, as the current equations suggest, then the paper's conclusion is incorrect and the model is strongly disfavored. If a different calculation yields `Δφ/f_a ~ 10^-2`, that calculation must be presented in full. Without this, the paper's core scientific contribution is unsubstantiated.

**P2-E2 | Section References, Page 6 | Use of non-public and future-dated references**
*   **Problem:** The manuscript cites several papers that are not publicly available.
    *   The ACT DR6 data is from "[Diego-Palazuelos and Komatsu, 2025]".
    *   The ALP mass constraints are compared to "[Namikawa et al., 2025. In preparation]".
    *   Two companion papers by the author are cited as "[Golden, 2026a]" and "[Golden, 2026b]", both "submitted simultaneously".
    Scientific claims must be supported by verifiable, publicly accessible sources. Citing "in preparation" or future-dated preprints is not acceptable in a peer-reviewed journal.
*   **Required Fix:** All references must be updated to point to publicly available preprints (e.g., on arXiv) or published papers. If the sources are not available, all claims and data relying on them must be removed from the manuscript. The results from the companion papers must be derived within this manuscript if they are essential to its argument.

### MAJOR

**P2-M1 | Section 3.3 & Figure 1, Page 3-4 | Misleading MCMC results and contradiction with "naturalness" claim**
*   **Problem:** The MCMC results for the extended model (Run 2) are presented in a misleading way that obscures a failure of the "naturalness" argument. Figure 1 reports a 1D marginalized posterior mean for the coupling `C_aγ` as `13.4 ± 11.6`. This is not an "order-unity" parameter. The text claims the result is "consistent with O(1) values for both parameters individually," which is contradicted by the figure's own summary statistic. Furthermore, the product of the reported 1D means (`θ_i * C_aγ = 1.33 * 13.4 ≈ 17.8`) is inconsistent with the directly constrained product reported in Eq. (8) (`C_aγ × θ_i = 3.4 ± 1.1`). This indicates that reporting the mean for the highly skewed, prior-dominated posterior of `C_aγ` is inappropriate and obscures the true nature of the constraint.
*   **Required Fix:** The author must provide a more careful and transparent discussion of the MCMC posteriors. For skewed distributions like `C_aγ`, the mode and a credible interval should be reported instead of the mean. The tension between the large mean value of `C_aγ` and the paper's "naturalness" claim must be explicitly addressed. The inconsistency between the product of means and the mean of the product must be resolved and explained.

**P2-M2 | Section 3.2, Page 2 | Undefined and underived parameter**
*   **Problem:** Equation (5) introduces an "effective photon coupling parameter" `f_photon × C_0 = 1.73 ± 0.44`. The parameter `f_photon` is never defined, and no derivation is provided for this value. It appears in the "Summary-Likelihood Inference" section, yet does not seem derivable from the summary likelihood combination alone. It is inconsistent with quantities derived in the MCMC section. The introduction of this opaque parameter is confusing and unscientific.
*   **Required Fix:** The parameter `f_photon` must be clearly defined in terms of the model's physical parameters (`f_a`, `m`, `θ_i`, `C_0`). A step-by-step derivation of its value in Eq. (5) from the data must be provided. If it cannot be clearly defined and derived, it should be removed.

### MINOR

**P2-m1 | Section 3.3, Page 3 | Unjustified prior range**
*   **Problem:** The prior for the anomaly coefficient `C_aγ` is taken as flat in `[1, 30]`. For a parameter that is claimed to be "order-unity," this range is very wide and requires justification. The MCMC results, particularly the long tail in the `C_aγ` posterior, are likely sensitive to this choice.
*   **Required Fix:** Justify the choice of the prior range for `C_aγ`.

**P2-m2 | Figure 2, Page 5 | Inconsistent legend labeling**
*   **Problem:** The legend in Figure 2 ("Model 2", "Model 2b", "Model 0") does not match the run identifiers in Table 1 ("Run 1", "Run 2", "Run 3"). This makes the figure difficult to interpret.
*   **Required Fix:** Make the legend labels in Figure 2 consistent with the run descriptions in Table 1.

**P2-m3 | Section 6, Page 5 | Out-of-place claim**
*   **Problem:** The Discussion section mentions a non-Gaussianity prediction `f_NL = -35/8` from a "matter-bounce" scenario. As the paper repeatedly and correctly states that its birefringence prediction is independent of bounce cosmology, this specific value feels like an advertisement for a companion paper and is disconnected from the present work's core argument.
*   **Required Fix:** Remove the specific `f_NL` value or significantly expand on its relevance to the main claims of this paper.

### NIT

**P2-N1 | Abstract, Page 1 | Understated evidence**
*   **Problem:** The Bayes factor `ln B = 5.17` is described as "indicative." On the standard Jeffreys scale, this constitutes "strong" or "very strong" evidence.
*   **Required Fix:** Use standard terminology to describe the strength of the Bayesian evidence, e.g., "strong evidence".

**P2-N2 | Throughout | Future dating**
*   **Problem:** The paper is dated "March 20, 2026".
*   **Required Fix:** The date should be the date of submission.

## Summary recommendation
**REJECT**

The manuscript is not acceptable for publication in Physical Review D. The central theoretical claim, which forms the basis for the entire paper, is invalidated by a significant internal contradiction in its derivation (P2-E1). Without a correct and self-consistent calculation, the paper's primary contribution is unsubstantiated. Furthermore, the reliance on non-public and unverifiable references (P2-E2) violates fundamental principles of scientific publishing. While the topic is important, the execution is critically flawed. A complete overhaul of the theoretical calculation and sourcing of data and literature would be required before this work could be reconsidered for publication.