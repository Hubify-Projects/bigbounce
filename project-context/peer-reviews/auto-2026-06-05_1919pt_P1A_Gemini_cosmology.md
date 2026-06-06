# P1A auto-2026-06-05_1919pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 1361.4s

---

**Referee Report for Manuscript [P1A]**
**Title:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Author:** Houston Golden

## General Comments

This manuscript presents a systematic investigation into the viability of generating late-time dark energy from four specific channels within minimal Einstein-Cartan-Holst (ECH) gravity. The author concludes that all four channels fail at the amplitude level under a set of stated assumptions, a result termed "channel-level closure." The paper's primary original contributions are (1) a "perturbation-transparency theorem" demonstrating that the Holst sector decouples from cosmological perturbations for canonical scalar matter, (2) a catalog of 14 structural and observational constraints on ECH-based dark energy, and (3) the identification of a "structural tension" between the number of e-folds required for the dark-energy mechanism and the number required to preserve a testable matter-bounce signature (`f_NL`).

The paper is ambitious and well-structured. The perturbation-transparency theorem is a clear, rigorous, and useful result that clarifies the observable consequences of the Holst term in scalar-driven cosmologies. The systematic catalog of barriers is a valuable contribution that organizes the challenges facing this class of models. The author is also commendably transparent about the limitations of the analysis, particularly the reliance on a phenomenological ansatz to connect the bounce scale to the dark energy scale.

However, the manuscript suffers from a fundamental error in its dimensional analysis of the core parity-odd operator. This error invalidates the central narrative framing that the operator has an incorrect mass dimension, which the author uses to justify the phenomenological scaling ansatz that underpins much of the quantitative analysis. This is an essential flaw that must be corrected and will necessitate a significant revision of several sections. Additionally, some figures are misleading, and the overall "closure" claim should be softened to better reflect its dependence on un-derived assumptions.

The paper has the potential to be a strong contribution to the field, but only after substantial revisions to address these core issues.

## Findings

### ESSENTIAL

*   **ID: P1A-E1**
    *   **Location:** Page 6, Sec. II C, "Step 3"; Page 19, Appendix B
    *   **Problem:** The paper incorrectly states that the parity-odd operator in Eq. (6), `L_odd = (α/M) εμνρσ FμνIJ FρσIJ`, has a mass dimension of +1. This is based on the assertion in Appendix B that `[εμνρσ FμνIJ FρσIJ] = +2`. This is incorrect. The Riemann tensor (or Lorentz connection field strength) `F` has a mass dimension of +2. The product of two such tensors, `F F`, therefore has a mass dimension of +4. Consequently, the Lagrangian density `L_odd` has a mass dimension of `[α/M] + 4`. For `L_odd` to have the correct dimension of a Lagrangian density (+4), the prefactor `α/M` must be dimensionless.
    *   **Impact:** This fundamental error invalidates the entire narrative that the operator is problematic because it has the "wrong" dimension and therefore requires a special "on-shell scaling ansatz" to acquire the missing powers of mass. The subsequent discussion of "fixing" the operator by adding powers of `M_Pl` and the quantitative distinction between `N_tot ≈ 92` (from the ansatz) and `N_tot ≈ 94` (from the "genuine" hierarchy) are all artifacts of this initial mistake.
    *   **Required Fix:** The dimensional analysis must be corrected throughout the manuscript. The author must re-evaluate the motivation for the phenomenological scaling ansatz `ρ_Λ ~ (α/M) M_Pl^4` (Eq. B2). The operator as written in Eq. (6) is a valid dimension-4 operator if `α/M` is dimensionless. The paper's core argument must be reframed. The problem is not one of incorrect dimension, but that a dimensionless coupling `α/M` of order unity would lead to a dark energy density of order `M_Pl^4`. The required smallness of the dark energy density must therefore be encoded in an extremely small dimensionless coupling, which is simply a restatement of the cosmological constant fine-tuning problem. The entire discussion in Appendix B and related sections must be rewritten based on a correct dimensional analysis.

### MAJOR

*   **ID: P1A-M1**
    *   **Location:** Page 5, Figure 2
    *   **Problem:** The figure is misleading. The step from `ρ_Pl` to `ρ_vac = Ξ M_Pl^4` is labeled "Parity-odd vacuum energy (one-loop, Holst term)". This presents the energy scale `Ξ M_Pl^4` as a derived quantity. However, the text correctly identifies this relationship as a phenomenological ansatz, not a derived result from a one-loop calculation. The figure should reflect the ansatz nature of this step. Additionally, the y-axis labels "This work 10⁵" and "ΛCDM 10¹²⁰" are unclear and should be explicitly defined (e.g., "Fine-Tuning Hierarchy ρ_theory/ρ_obs").
    *   **Required Fix:** Relabel the arrow/box for `ρ_vac` to explicitly state that this is a "Phenomenological Scaling Ansatz". Clarify the y-axis label to explain what the numbers `10^5` and `10^120` represent.

*   **ID: P1A-M2**
    *   **Location:** Abstract & Throughout
    *   **Problem:** The paper's central claim is the "channel-level closure" of dark energy routes. However, this closure relies fundamentally on a non-derived, phenomenological ansatz to connect the Planck-scale physics to the observed dark energy density. While the paper is honest about this, the term "closure" implies a more definitive, first-principles refutation than what is actually achieved. The more robust results are the catalog of obstacles and the perturbation-transparency theorem.
    *   **Required Fix:** The author should soften the "closure" language throughout the manuscript. The abstract and conclusions should be rephrased to emphasize that the paper provides a systematic catalog of severe, and likely insurmountable, obstacles for these ECH dark energy routes, with the quantitative closure being conditional on a specific phenomenological scaling. The focus should be shifted to the more rigorous results like the transparency theorem.

### MINOR

*   **ID: P1A-m1**
    *   **Location:** Page 9, Sec. IV A
    *   **Problem:** The text states the energy density for the NJL contact term is "bounded above by `ρ_NJL ~ κ n_f^2 ~ n_f^4 / M_Pl^2`". The operator is dimension-6 with coefficient `κ ~ 1/M_Pl^2`, so the energy density scales as `n_f^2 / M_Pl^2`, not `n_f^4 / M_Pl^2`. This appears to be a typo.
    *   **Required Fix:** Correct the scaling to `ρ_NJL ~ n_f^2 / M_Pl^2`. The ultimate conclusion that the contribution is negligible remains correct.

*   **ID: P1A-m2**
    *   **Location:** Page 4, Figure 1
    *   **Problem:** The diagram shows an arrow from "Ekpyrotic" to "ECH / torsion", which is then marked as "structurally closed". The line from Ekpyrotic itself is labeled "produces ECH; permitted". This is confusing. It seems to imply that Ekpyrotic models are closed by this work, which is not the focus of the paper and likely an overstatement.
    *   **Required Fix:** Clarify the diagram and/or caption. For example, state "Ekpyrotic models relying on ECH torsion..." to make it clear that only a specific subset of models is being constrained.

### NIT

*   **ID: P1A-N1**
    *   **Location:** Page 1
    *   **Problem:** The manuscript is dated "June 2, 2026 PDT", a future date. This is unconventional.
    *   **Required Fix:** Change the date to the date of submission.

*   **ID: P1A-N2**
    *   **Location:** Throughout
    *   **Problem:** The paper makes frequent reference to companion papers "in preparation" (e.g., [2, 6, 23, 46]). While this is sometimes necessary, the sheer number of such references for key inputs (MCMC results, `f_NL` forecasts, galaxy spin data) makes the current manuscript difficult to assess as a self-contained work.
    *   **Required Fix:** No fix is required, but the author should ensure that upon publication, these references are updated to their final, citable versions. This is noted as a minor weakness in the current presentation.

*   **ID: P1A-N3**
    *   **Location:** Page 18, Acknowledgments
    *   **Problem:** The acknowledgment of an AI research assistant ("Claude (Anthropic)") is unusual. While transparency is good, PRD policy on such acknowledgments should be checked. The statement "All scientific claims... were independently verified by the author" is crucial and well-placed.
    *   **Required Fix:** The author should verify this acknowledgment is consistent with the journal's policy.

## Summary recommendation

**MAJOR REVISIONS**

This paper contains the seeds of a valuable contribution to the cosmology literature. The perturbation-transparency theorem is elegant and important, and the systematic barrier analysis is a useful organizational effort. However, the paper is built around a central narrative that is invalidated by a fundamental error in dimensional analysis. Correcting this error is essential and will require a substantial restructuring of the paper's core argument regarding the dark energy connection. Once this foundational issue is fixed and the claims are recalibrated to reflect what has been rigorously proven versus what remains dependent on phenomenological assumptions, the manuscript will be much stronger and potentially acceptable for publication in Physical Review D.