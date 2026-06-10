# P1A auto-2026-06-08_1144pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (5022 chars)
**Wall time**: 138.0s

---

Here is a referee report for the provided paper.

---

## Referee Report: P1A

**Paper ID:** P1A
**Title:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Journal:** Physical Review D

This paper investigates four potential channels for generating late-time dark energy from Einstein-Cartan-Holst (ECH) gravity in the context of a bouncing cosmology. The authors conclude that these channels are closed at the amplitude level under a set of stated assumptions. The central theoretical result is a "perturbation-transparency theorem," which states that for canonical scalar matter, the Holst sector decouples from all scalar and tensor perturbation equations of motion. The paper also highlights a structural tension between the number of e-folds required for the dark energy mechanism and the number allowed for preserving a testable matter-bounce non-Gaussianity signature (`fNL = -35/8`).

The paper's strength lies in the perturbation-transparency theorem, which appears to be a robust and useful result, clarifying the observable consequences of minimal ECH with scalar matter. However, the main framing of the paper—the "closure" of dark energy routes—is based on a phenomenological ansatz involving a non-standard, dimension +1 operator. This foundation is speculative and significantly weakens the conclusions about dark energy. The paper requires substantial revision to clarify the scope and solidity of its claims and to correct several technical errors.

### Summary recommendation
**MAJOR REVISIONS**

The paper presents a valuable result in the perturbation-transparency theorem. However, the primary claims regarding the closure of dark-energy routes are contingent on a speculative and poorly justified theoretical ansatz. The manuscript must be significantly restructured to reflect this, re-framing the dark energy analysis as a test of a specific ansatz rather than a general channel closure. Additionally, several essential and major technical issues must be addressed before the paper can be considered for publication.

---

### Detailed Findings

#### ESSENTIAL

*   **P1A-E1 | Page 1, Title Block | Incorrect Date**
    *   **Problem:** The paper is dated "June 2, 2026 PDT," which is a future date.
    *   **Fix:** Replace the future date with the correct submission date.

*   **P1A-E2 | Page 9, Sec. IV B | Incorrect Dimensional Analysis in Route 2 Closure**
    *   **Problem:** The derivation of the amplitude suppression for Route 2, presented in and around Eq. (15), is dimensionally inconsistent. The ratio `Δθ_one-loop / Δθ_obs` must be dimensionless. The expression given is:
        `Alone-loop / Aθobs ~ (αem / 4π) * (Ho/MPl) / (MPl * (α/M) * βobs)`
        The term `MPl * (α/M)` is dimensionless (as stated in the text, `~10^-2`). `βobs` is dimensionless. `αem` is dimensionless. However, `Ho/MPl` is also dimensionless. The equation as written has an extra `MPl` in the denominator of the second term, making the expression dimensionally incorrect. The entire derivation of the numerical suppression factor `~10^-58` to `10^-60` rests on this flawed equation.
    *   **Fix:** Re-derive the expression for the ratio of the one-loop effect to the observed birefringence, ensuring it is dimensionally correct. The argument should be constructed from properly normalized, dimensionless quantities. The final numerical estimate must be re-calculated based on the corrected derivation.

#### MAJOR

*   **P1A-M1 | Throughout (esp. Abstract, Sec. II C, Appendix B) | Reliance on a Speculative Dimension +1 Operator Ansatz**
    *   **Problem:** The entire dark energy analysis rests on a "phenomenological on-shell scaling ansatz" where a parity-odd operator with off-shell mass dimension +1 (Eq. 6) is assumed to source the observed dark energy density. As acknowledged in Appendix B, this is not a controlled EFT operator. The "fix" of assuming it acquires the correct dimension via on-shell evaluation at Planck-scale densities is a very strong, unjustified assumption. This fundamentally undermines the claim that the paper achieves a "closure" of dark energy routes; rather, it closes routes based on one specific, speculative ansatz. The title, abstract, and main narrative overstate the generality of this negative result.
    *   **Fix:** The paper must be substantially re-framed.
        1.  The title and abstract must be revised to state clearly that the dark energy analysis is a test of a *specific phenomenological ansatz*, not a general closure of ECH dark-energy channels.
        2.  The introduction and conclusions must be rewritten to soften the claims. The result should be presented as: "Under the specific assumption that dark energy arises from the on-shell evaluation of a dimension +1 operator, we find the mechanism is non-viable due to..."
        3.  The discussion in Appendix B should be moved to the main text (e.g., Section II) to ensure every reader understands the speculative nature of the underlying assumption from the outset.

*   **P1A-M2 | Page 6, Sec. II C 1 | Unjustified Prefactor in Dilution Formula**
    *   **Problem:** The inflationary dilution factor in Eq. (11) includes a prefactor `(Treh/MGUT)^(3/2)`. The justification for this term is described as "dimensional-analysis aesthetic" and based on a "phenomenological phase-space ansatz," not a calculation from a thermal partition function or a proper matching calculation. This is a critical part of the numerical argument that leads to `Ntot ≈ 92`, but its foundation is weak.
    *   **Fix:** The authors must either provide a more rigorous derivation for this prefactor or, at minimum, perform a sensitivity analysis. How does the required value of `Ntot` change if this prefactor is O(1) or has a different power-law dependence? The weakness of this assumption must be more prominently acknowledged in the main text.

#### MINOR

*   **P1A-m1 | Abstract & Page 17, Sec. XIV D | Confusing Formulation of Scale Evolution**
    *   **Problem:** The abstract states: "...a contracting-phase quantity mode with `kSPHEREx ~ 10⁻¹ h/Mpc` is pushed to `k_phys(bounce) ~ k_SPHEREx * e^(N_tot-N_exit)`...". This expression is dimensionally inconsistent (`k_phys` vs. `k_comov`) and confusing. The physical argument—that a large number of e-folds pushes observable scales deep into the sub-horizon regime during the pre-bounce phase, erasing the `fNL` signature—is sound, but the mathematical expression used to convey it is incorrect and opaque.
    *   **Fix:** Rephrase this argument clearly in terms of the ratio of the physical wavelength of a mode (`λ_phys = 2πa/k`) to the Hubble radius (`R_H = 1/H`) during the contracting phase. State the conclusion in terms of the number of e-folds of inflation (`N_tot`) required to erase the signature generated when SPHEREx-relevant modes were super-horizon. Avoid the confusing and incorrect formula.

*   **P1A-m2 | Page 13, Sec. IX L | Unjustified Scaling for Gravitational Wave Production**
    *   **Problem:** Barrier 12 states that gravitational wave production from the bounce is bounded by `Ω_GW(bounce) ~ (ρ_crit/ρ_Pl)^2`. The standard scaling for GWs produced by cosmological sources is `Ω_GW ~ (ρ_source/ρ_Pl)`. The squared dependence is non-standard and is presented without derivation or citation.
    *   **Fix:** Provide a reference that derives this `(ρ/ρ_Pl)^2` scaling for GWs from an LQC bounce, or provide a brief derivation. If neither is possible, the standard scaling should be used and the numerical result adjusted accordingly.

*   **P1A-m3 | Page 15, Sec. XII B | Repulsive Channel for Condensate**
    *   **Problem:** The text states: "The condensate route fails because the scalar/pseudoscalar channel is repulsive at γ = 0.274 and subcritical." This statement is too dense. It is not immediately clear what "channel," "repulsive," and "subcritical" refer to in this context without prior expertise in this specific model.
    *   **Fix:** Briefly expand on this point. Explain what interaction becomes repulsive and why this prevents the formation of a condensate that could act as dark energy.

*   **P1A-m4 | Page 16, Table III | Ambiguous Footnote on `wowa` Evidence**
    *   **Problem:** Footnote `†` in Table III provides a very detailed status update on an ongoing MCMC chain for a `wowa` model. While the transparency is commendable, this level of real-time progress reporting is not appropriate for a final publication. The key takeaway is that the analysis is not yet complete.
    *   **Fix:** Condense the footnote to a simple statement, such as: "A dedicated MCMC analysis for the `wowa` model is in progress; at the time of submission, the chains have not yet converged to publication-quality standards. Therefore, we report the Quintom-B model as 'consistent' at the theoretical level, without a quantitative posterior preference."

#### NIT (Nitpicks)

*   **P1A-N1 | Page 1, Abstract | Awkward Phrasing**
    *   **Problem:** The phrase "...whose off-shell mass dimension is +1 rather than +4 (Appendix B); we treat this scaling explicitly as an ansatz, not a derivation." is slightly clunky.
    *   **Fix:** Suggest rephrasing, e.g., "The analysis relies on a phenomenological ansatz that maps a dimension-+1 operator to the dark energy scale; we explicitly treat this as an assumption, not a derivation (Appendix B)."

*   **P1A-N2 | Page 3, Sec. I | Typo/Grammar**
    *   **Problem:** "The surviving phenomenological predictors... are mechanism-independent and shared by other UV completions."
    *   **Fix:** "The surviving phenomenological predictions... are mechanism-independent..."

*   **P1A-N3 | Page 7, Sec. II C 2 | Underprediction Magnitude**
    *   **Problem:** "...underpredicts any plausible spin asymmetry by > 100 orders of magnitude." This is a very large number. While likely correct given the scales involved, it's worth double-checking if this is an exaggeration.
    *   **Fix:** Please confirm the calculation. If correct, it stands.

*   **P1A-N4 | Page 18, Sec. XV | Sigma Calculation Phrasing**
    *   **Problem:** The calculation of the `0.73σ` separation for LiteBIRD is correct and an important point. However, the text "NOT at the naive... 2.4σ which would ignore the prior measurement's... uncertainty" is slightly confrontational.
    *   **Fix:** Rephrase to be more neutral, e.g., "A direct comparison of the 0.27° prediction to the 0.342° central value would be misleading. A proper model discrimination test must account for the uncertainty on the existing measurement, resulting in a projected separation of ~0.73σ."

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated referee report, incorporating the new findings from the second, more rigorous review.

---

## Referee Report: P1A (Second Pass)

**Paper ID:** P1A
**Title:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Journal:** Physical Review D

This report contains additional findings from a second, more detailed review of the manuscript. These issues are in addition to those raised in the initial report (P1A-E1, E2; M1, M2; m1-m4; N1-N4). The new findings, particularly the multiple dimensional inconsistencies in fundamental equations, are severe and undermine the paper's central quantitative arguments.

### Summary recommendation
**MAJOR REVISIONS** (Unchanged, but with increased severity)

The new findings reveal fundamental errors in the mathematical formalism used to support the paper's main conclusions about closing dark energy routes. Multiple key equations are dimensionally inconsistent, invalidating the numerical estimates derived from them. While the perturbation-transparency theorem remains a potentially valuable result, the dark energy analysis requires a complete overhaul, starting from correctly formulated physical operators and equations. The paper cannot be published in its current form.

---

### Detailed New Findings

#### ESSENTIAL

*   **P1A-E3 | Page 6, Eq (10) | Incorrect Dimensionality of Effective Cosmological Constant**
    *   **Problem:** Equation (10), `A_eff = Ξ M_Pl + c_ω ω^2`, is dimensionally inconsistent. The effective cosmological constant `A_eff` must have units of energy density (mass⁴). The term `Ξ M_Pl` has units of mass² (since `Ξ` is dimensionless and `M_Pl` is mass¹), and `c_ω ω^2` is also stated to be mass². The equation cannot be correct as written. The associated Figure 2 uses `ρ_vac = Ξ M_Pl^4`, which is dimensionally correct and suggests the equation in the text is a typo.
    *   **Fix:** The authors must correct Equation (10) to be dimensionally consistent, likely by changing `Ξ M_Pl` to `Ξ M_Pl^4`. All subsequent arguments that rely on this equation must be checked for consistency with the corrected form.

*   **P1A-E4 | Page 9, Eq (14) | Incorrect Dimensionality of Parity-Odd Operator**
    *   **Problem:** The one-loop parity-odd operator defined in Equation (14) is dimensionally incorrect. The Lagrangian density (the integrand) must have units of mass⁴. The operator `∂θ J⁵` has dimension 4. However, the prefactor `1/(16π² M_Pl)` has dimension mass⁻¹, making the entire Lagrangian density have dimension mass³. This invalidates the subsequent quantitative analysis in Section IV B.
    *   **Fix:** The authors must re-derive or find a correct expression for this operator from the literature. The prefactor should be dimensionless for the operator as written. The entire amplitude-suppression argument for Route 2 must be re-evaluated based on the corrected operator. This is in addition to the separate dimensional error in Eq (15) identified in the first review (P1A-E2).

#### MAJOR

*   **P1A-M3 | Page 10, Eq (17) | Incorrect Dimensionality of Birefringence Angle**
    *   **Problem:** Equation (17), which relates the birefringence angle `β` to the spectator field properties, is dimensionally inconsistent. The left side (`β`) is dimensionless, while the right side has units of mass⁻¹. This indicates a missing mass scale in the formula. This error undermines the entire argument in Section IV D that `m_e ~ H_0` is required to match observations, as the relationship between the observables is incorrectly stated.
    *   **Fix:** The authors must provide the correct, dimensionally consistent formula for the induced birefringence angle from a spectator field with this coupling. The subsequent analysis of the "naturalness objection" for Route 4 must be completely redone using the correct formula.

#### MINOR

*   **P1A-m5 | Page 1, Abstract & Body | Incorrect Cross-Reference**
    *   **Problem:** The abstract and the introduction (page 1) state that missing operators (like the Jackiw-Pi term) are discussed in "Sec. IV and Sec. XI". While Section IV does mention them, Section XI ("The Hybrid Dark-Energy Loophole") does not. This is a misleading cross-reference.
    *   **Fix:** Remove the incorrect reference to Section XI.

*   **P1A-m6 | Page 6, Eq (5) | Incorrect Dimensionality of Action Term**
    *   **Problem:** The action term in Equation (5) is dimensionally incorrect. The integrand has units of mass¹, which when integrated over `d⁴x` (units of mass⁻⁴) gives a term with units of mass⁻³, not a dimensionless action. This is a precursor to the issue with Eq (6) but should be noted as a separate error in the formalism.
    *   **Fix:** The authors need to correct the formulation of this action term. This is deeply tied to the speculative nature of the dimension +1 operator, but the expression for the action itself should still be dimensionally sound, even if the operator within it is non-standard.