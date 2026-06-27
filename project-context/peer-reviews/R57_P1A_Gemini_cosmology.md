# P1A R57 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R57_P1A/paper1a_ech_nogo.pdf` md5=? pages=?
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 93.2s

---

## Referee Report: P1A

**To the editor:**

This manuscript, "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter," presents an ambitious and wide-ranging analysis of the potential for Einstein-Cartan-Holst (ECH) gravity to explain late-time dark energy. The paper contains several valuable contributions, most notably a "perturbation transparency" theorem for scalar matter and a compelling "structural tension" argument between the requirements for a dark-energy mechanism and the preservation of a matter-bounce signature.

However, the manuscript suffers from several critical flaws that preclude its publication in Physical Review D in its current form. The most severe issue is a fundamental error in the dimensional analysis of the core parity-odd operator proposed to source dark energy. This error invalidates the central dark-energy mapping, the calculation of the required e-folds of inflation (`N_tot ≈ 92`), and the associated fine-tuning arguments. Additionally, the paper relies heavily on load-bearing results from companion papers that are "in preparation" and thus not available for review, which violates the standard of a self-contained, verifiable scientific article.

While the perturbation-transparency and structural-tension results appear sound and are of significant interest, they are currently entangled with a dark-energy framework that is not demonstrably consistent. The paper requires a complete overhaul of its central dark-energy claim.

Below is a detailed list of required revisions.

---

### ESSENTIAL Revisions

**P1A-E1: Section: Title page (p. 1)**
*   **Problem:** The paper is dated "June 26, 2026," which is in the future.
*   **Fix:** The date must be corrected to the date of submission.

**P1A-E2: Section: II.A.2, Appendix B (p. 7, 26)**
*   **Problem:** The dimensional analysis of the parity-odd operator, which is the foundation of the entire dark-energy mapping, is incorrect. Equation (6) and Appendix B claim the operator `L_odd = (α/M) εμνρσ e_μ^I e_ν^J F_IJρσ` has off-shell mass dimension `[L_odd] = +1`. This is incorrect. In the component formalism used, the tetrads `e_μ^I` are dimensionless, the spin-connection curvature `F_IJρσ` has mass dimension `[F] = +2`, and the Levi-Civita symbol `εμνρσ` is a tensor density, not a tensor, and its contribution depends on the convention. However, the integral `∫d⁴x √-g L_odd` must be dimensionless. With `[d⁴x] = -4` and `[√-g] = 0`, the Lagrangian density `√-g L_odd` must have dimension `+4`. The paper claims `[L_odd] = +1`, which would give the action a dimension of `-3`.
    In form language (Eq. 5), `e^I` is a 1-form (`[e] = -1`) and `F^IJ` is a 2-form (`[F] = +2`), so the 4-form `e^I ∧ e^J ∧ F^IJ` has dimension `(-1) + (-1) + (+2) = 0`. The integral of this 4-form is dimensionless. For the action `S_eff = ∫ (α/M) e∧e∧F` to be dimensionless, the coupling `α/M` must also be dimensionless.
    The paper's framework is built on `[α/M] = -1` (GeV⁻¹), which is inconsistent with a dimensionless action. This error invalidates the mapping in Eq. (B2) `ρ_bounce ~ (α/M) M_Pl⁴`, the subsequent calculation `N_tot ≈ 92`, and the entire fine-tuning discussion that "reparameterizes" the CC problem.
*   **Fix:** The author must provide a complete and correct dimensional analysis for a parity-odd operator that can source dark energy. This will require rewriting the operator, the coupling, and re-deriving the entire dark-energy mapping. If a consistent operator cannot be constructed, the dark-energy claims must be retracted, and the paper refocused on its other, more robust results.

**P1A-E3: Section: Abstract, I, XIII, XIV.D (p. 1, 4, 23, 24)**
*   **Problem:** The paper makes multiple quantitative claims based on a "detailed multi-tracer SPHEREX Fisher forecast" which is cited as being "in preparation, [2]". A published paper cannot base its core testable predictions on unpublished, unreviewable work. The quoted `2.6-5σ` significance for testing `f_NL = -35/8` is a load-bearing claim that lacks verifiable support within this manuscript.
*   **Fix:** The paper must either (a) include a self-contained derivation of the SPHEREX forecast, including the relevant Fisher matrix formalism, assumptions, and system-atics, sufficient for a referee to verify the result, or (b) remove the quantitative significance claims and state that such a forecast is the subject of future work.

**P1A-E4: Section: Abstract, IV.B, XV (p. 1, 10, 25)**
*   **Problem:** The paper relies on a companion paper "[6], in preparation" for MCMC verification, cosmological parameter fits (`H₀`, `ΔN_eff`), and ALP parameter fitting. The text on p. 4 explicitly states these are "documented internally rather than as externally citable arXiv-posted numbers." This is unacceptable for a peer-reviewed publication.
*   **Fix:** All cosmological parameters used to support the paper's arguments must be derived from publicly available data and analyses, or the analysis (datasets, priors, likelihoods, MCMC setup) must be fully documented within this paper or its appendices. The reliance on "in preparation" companion papers for such fundamental inputs must be removed.

**P1A-E5: Section: Abstract, XV (p. 1, 25)**
*   **Problem:** The abstract and conclusions juxtapose significance values that arise from different null procedures without the required caveat at every instance. For example, the abstract mentions a `~3.6σ` and `~2.9σ` result for birefringence and a `2.6-5σ` forecast for `f_NL`. While a caveat is present, the instruction is to ensure it appears at every juxtaposition to prevent misinterpretation. A similar issue occurs on p. 25, where the `~9σ` test (against `β=0`) is compared with the `~0.73σ` test (model vs. prior).
*   **Fix:** At every point in the text where sigma values from different tests or null hypotheses are mentioned in the same paragraph or context, an explicit statement such as "These significance values test different physical hypotheses and are not directly comparable" must be included.

### MAJOR Revisions

**P1A-M1: Section: IV.B (p. 12)**
*   **Problem:** The one-loop operator in Eq. (14) appears to be dimensionally inconsistent. The action `S = ∫ d⁴x L` must be dimensionless. The integrand is `∂_μ θ_NY J^5μ`. `[J⁵]` is `+3`. If `θ_NY` is a pseudoscalar field, `[∂_μ θ_NY]` is `+2`. The integrand has dimension `+5`. With `[d⁴x] = -4`, the integral has dimension `+1`. The prefactor `β(γ)/M_Pl` has dimension `-1`. The action is dimensionless, but the argument seems ad-hoc. The EFT construction is not clearly derived or justified.
*   **Fix:** Provide a rigorous derivation of this effective operator from a well-defined theory, ensuring it is dimensionally consistent and properly normalized. Justify the form and the prefactor, or treat it as a purely phenomenological ansatz and state the limitations clearly.

**P1A-M2: Section: Overall Structure and Length**
*   **Problem:** The paper is 29 pages long and attempts to cover too much ground: a review of four ECH channels, a "no-go" argument for each, a new perturbation theorem, a new structural tension, and forecasts for future experiments. Given the essential flaw in the dark-energy mechanism (P1A-E2), the paper's focus is diluted.
*   **Fix:** The paper should be substantially restructured and shortened. I recommend focusing the manuscript on the two strongest and most novel contributions: the Perturbation-Transparency Result (Sec. X) and the Structural Tension between dark energy and the matter-bounce `f_NL` signature (Sec. XIV.D). The "Four-Route No-Go" section should be heavily condensed or presented as a consequence of these structural results, especially since the derivation for the primary DE route is flawed. A target length of 10-12 pages for the main body would be more appropriate.

**P1A-M3: Section: VII (p. 15)**
*   **Problem:** The section on falsifiability criteria presents the LiteBIRD and SPHEREx tests. The text correctly notes that for LiteBIRD, the relevant test is a differential measurement against the existing `β_obs` central value, not a naive detection against zero. However, this crucial statistical point is somewhat buried.
*   **Fix:** Elevate this point. The section should more clearly frame the surviving tests not as "predictions of ECH" but as "class-level tests of bounce/ALP models that are not ruled out by the ECH closure arguments." The distinction between a detection (`β ≠ 0`) and model discrimination (`β = 0.27°` vs. `β = 0.342°`) must be made more prominent.

### MINOR Revisions

**P1A-N1: Section: II.A.2 (p. 6)**
*   **Problem:** Footnote 2 is exceptionally long and dense, containing a full derivation that interrupts the flow of the main text.
*   **Fix:** Move the detailed derivation from Footnote 2 into an appendix to improve readability.

**P1A-N2: Section: IV.D (p. 13)**
*   **Problem:** Footnote 4 attempts to clarify the convention for the canonical ALP field `φ` versus the dimensionless angle `θ`. While necessary, the explanation is convoluted and reflects the underlying complexity of the chosen parameterizations.
*   **Fix:** Streamline the main text to use a single, consistent notation for the ALP field throughout the derivation (e.g., consistently use the canonical field `φ` and only introduce `θ` when discussing the potential `V(θ)`). This would make the argument easier to follow and the footnote unnecessary.

**P1A-N3: Section: X.G (p. 21)**
*   **Problem:** The paper quotes a NANOGrav comparison: `γ_PTA = 2.567 ± 0.382` from a "real-KDE GPU MCMC, in preparation [46]". This is another instance of relying on an unpublished result.
*   **Fix:** Replace the citation with a reference to the official NANOGrav 15-year data release paper and use the officially published value and uncertainty for the spectral index, or clearly state that this is a re-analysis and provide the full details and justification for it.

---

## Summary recommendation

**MAJOR REVISIONS**

This paper has the potential for two significant publications. The first is a focused, shorter paper on the perturbation-transparency theorem for ECH and the resulting structural tension that prevents a simple unification of a matter bounce and late-time dark energy within this minimal framework. These results appear robust and are of high interest to the cosmology community.

The second, separate project would be to correctly formulate a viable ECH-based dark energy mechanism, which would first require fixing the fundamental error in the dimensional analysis of the proposed operator.

As it stands, the manuscript's central claim regarding a dark-energy solution is unsubstantiated due to a critical flaw in its theoretical foundation. Furthermore, its reliance on numerous "in preparation" works for load-bearing observational and theoretical claims is not acceptable for PRD. Therefore, the paper must undergo major revisions, including a potential split and a complete re-derivation of its dark-energy-related claims, before it can be reconsidered for publication.