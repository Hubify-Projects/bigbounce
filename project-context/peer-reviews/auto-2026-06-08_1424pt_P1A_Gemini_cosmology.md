# P1A auto-2026-06-08_1424pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (13397 chars)
**Wall time**: 148.2s

---

Here is a complete referee report for the paper "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter".

***

## Referee Report

**Paper ID:** P1A
**Title:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Journal:** Physical Review D

This paper presents a systematic, channel-level investigation into whether minimal Einstein-Cartan-Holst (ECH) gravity can serve as a source for late-time dark energy. The authors assess four specific mechanisms and conclude that all fail at the amplitude or naturalness level under a set of clearly stated assumptions. The central results are a "perturbation-transparency theorem" for canonical scalar matter, which demonstrates that the Holst sector decouples from standard cosmological perturbations, and a catalog of 13 logically-independent "barriers" that constrain such ECH-to-dark-energy routes. The paper also identifies a structural tension between the number of e-folds required for the dark energy mechanism and the preservation of a testable matter-bounce signature in the non-Gaussianity parameter `fNL`.

The work is comprehensive, rigorous, and commendably transparent about its scope and limitations. The negative result is well-supported and of significant value to the cosmology and modified gravity communities. The distinction between a "channel-level closure" and a full "operator-level theorem" is crucial and handled correctly. The analysis of surviving, mechanism-independent observables (`fNL` and cosmic birefringence) and the associated forecasts is sophisticated.

While the paper is of high quality and suitable in principle for publication in Physical Review D, several revisions are required to address issues of internal consistency, clarity in theoretical derivations, and presentation. I recommend **Major Revisions** before the paper can be accepted for publication.

---

### ESSENTIAL Revisions

**P1A-E1: Internal Inconsistency in PTA Spectral Index Value**
*   **Location:** Page 4, Figure 1; Page 15, Sec. XI.G; Page 20, Table IV.
*   **Problem:** The paper uses two different values for the NANOGrav 15-yr PTA spectral index `γ`. Figure 1 quotes `γ = 3.20 ± 0.42 (P3 §6)`. However, the main text on page 15 states, "This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20±0.42 used in pre-real-KDE drafts," and provides the updated value `γ = 2.567 ± 0.382`. This updated value is also used in Table IV. The use of a superseded value in a key summary figure is confusing and unacceptable.
*   **Fix:** The paper must be made internally consistent. Replace the value in Figure 1 with the final adopted value (`γ = 2.567 ± 0.382`) and update the corresponding caption text. Remove any language about "superseded" values or "earlier drafts" from the main text; simply state the final value and its source (the companion paper).

### MAJOR Revisions

**P1A-M1: Ambiguity and Potential Error in Four-Fermion Interaction Lagrangian**
*   **Location:** Page 5, Eq. (4).
*   **Problem:** The four-fermion contact interaction Lagrangian is given as `Lint = (3GN/2) * (γ² / (γ² + 1)) * J_5μ J^5_μ`.
    1.  The symbol `N` in the prefactor `3GN/2` is undefined and appears to be a typo, possibly for `π`.
    2.  The coefficient itself is non-standard. The classic Hehl-Datta result for the axial-axial interaction from integrating out torsion in Einstein-Cartan theory is `L_int = -(3/16) * κ * (J_5μ J^5_μ)`, where `κ = 8πG`. This gives a prefactor of `-3πG/2`. The Holst extension modifies the coupling, but the presented form with `γ² / (γ² + 1)` is not immediately recognizable and requires a clear derivation or citation to a specific result that produces this factor. As written, the equation is unsubstantiated.
*   **Fix:** The authors must clarify Eq. (4). Correct the apparent typo `N`. Provide a derivation or a precise citation for the `γ² / (γ² + 1)` dependence. If this is a known result from Freidel et al. [15] or Shapiro & Teixeira [20] as hinted in Step 4, the connection should be made explicit. If it is a novel derivation, it must be shown in an appendix.

**P1A-M2: Weak Justification for Prefactor in Inflationary Dilution Formula**
*   **Location:** Page 6, Eq. (11) and surrounding text; Page 7, text.
*   **Problem:** The inflationary dilution factor `D_inf` includes a prefactor `(T_reh / M_GUT)^(3/2)`. The justification for this term is described as "dimensional-analysis aesthetic" and based on a "phenomenological phase-space ansatz," not a first-principles calculation from a thermal partition function. While the authors are transparent about this weakness and correctly argue that the exponential term `exp[-3N_tot]` dominates the fine-tuning, the argument remains physically weak.
*   **Fix:** The authors should further emphasize that their main conclusions are entirely independent of the precise form of this algebraic prefactor. In Section XII.A ("Caveat on the (Treh/MGUT)3/2 prefactor"), they should explicitly state that the structural closure arguments and the 13 barriers of Section IX do not rely on this factor. The argument should be reframed to state that *any* pre-exponential factor of order unity (or that scales polynomially with energy scales) is insufficient to solve the 120-order-of-magnitude cosmological constant problem, which is why the exponential dilution is required in this model. This makes the argument more robust and less dependent on the weakly-justified `(3/2)` power.

### MINOR Revisions

**P1A-m1: Unconventional Formula for Birefringence Angle**
*   **Location:** Page 10, Eq. (17).
*   **Problem:** The formula for the rotation angle `β ~ (α/M) * sqrt(ρ_θ) / m_θ` is a rough estimate. While dimensionally correct, it conflates the total change in the axion field with its instantaneous amplitude. The standard expression relates `β` to the total change in the field, `Δθ`, as `β = (α/M) Δθ`.
*   **Fix:** The authors should briefly clarify how their Eq. (17) is derived from the standard formula, for instance by noting that for an oscillating field, the characteristic field amplitude is `θ_0 ~ sqrt(ρ_θ) / m_θ`, and this amplitude sets the scale for the total change `Δθ`. This would make the connection to standard literature clearer.

**P1A-m2: Future Date on Manuscript**
*   **Location:** Page 1, Abstract.
*   **Problem:** The paper is dated "June 2, 2026". This is a minor artifact but should be corrected to the actual submission date.
*   **Fix:** Update the date to the current date of submission.

**P1A-m3: Citation for `fNL = -35/8`**
*   **Location:** Page 1, Abstract; Page 3, Introduction; throughout.
*   **Problem:** The result `fNL = -35/8` for a matter bounce is a cornerstone of one of the paper's "surviving" predictions. The abstract cites a work in preparation [1] for this. However, this is a classic result.
*   **Fix:** While citing their own companion paper [2] for the SPHEREx forecast is appropriate, the original derivation of `fNL = -35/8` should be cited. The current reference [1] (Cai, Xue, Brandenberger, and Zhang, 2009) is indeed one of the key original papers. The phrasing should be clear that [1] is the origin of the theoretical value and [2] is the new forecast. The current phrasing is acceptable but could be slightly sharpened to give more credit to the original authors.

**P1A-m4: Clarification of `N_tot` Tension**
*   **Location:** Page 19, Appendix B.
*   **Problem:** The appendix shows that two different ways of framing the dark energy problem lead to slightly different required e-fold counts (`N_tot ≈ 92` vs. `N_tot ≈ 94`). The text explains this `~2%` offset arises from the choice of ansatz.
*   **Fix:** This is well-explained, but for maximum clarity, the authors should add a sentence in the main body (e.g., in Sec. XIV.D) explicitly stating that the structural tension argument is robust to O(1) changes in the required `N_tot` and does not depend on this `~2%` ansatz-dependent uncertainty.

### NIT-PICKING / COSMETIC

**P1A-N1: Awkward Phrasing in Abstract**
*   **Location:** Page 1, Abstract.
*   **Problem:** The phrase "The dark-energy mapping rests on a phenomenological on-shell scaling ansatz whose off-shell mass dimension is +1 rather than +4" is slightly dense for an abstract.
*   **Fix:** Consider simplifying to: "The connection to dark energy relies on a phenomenological scaling ansatz, as the relevant parity-odd operator has an off-shell mass dimension of +1, not the +4 required for a standard Lagrangian term."

**P1A-N2: Redundant Phrase**
*   **Location:** Page 17, Sec. XIV.D.
*   **Problem:** The text reads "...the rigorous bounce-vs-SPHEREx scale ratio is the physical scaling above with kbounce/kSPHEREx ~ e32) and the surviving bispectrum signal becomes purely vacuum-inflationary rather than matter-bounce contraction-mode." The parenthetical seems to repeat the main point.
*   **Fix:** Suggest removing the parenthetical or rephrasing for better flow, e.g., "...since the physical wavelength of modes accessible to SPHEREx is stretched by a factor of ~e^32 from the bounce to horizon exit, their surviving bispectrum signal..."

---

## Summary recommendation

**MAJOR REVISIONS**

This is a substantial and valuable contribution that performs a rigorous and systematic closure of several proposed dark energy mechanisms within the ECH framework. The perturbation-transparency theorem is an elegant and important result, and the identification of the structural tension with `fNL` is a novel insight. The paper is well-written, well-structured, and its conclusions are well-supported by the presented arguments. However, the identified issues, particularly the internal inconsistency of a key observational number (P1A-E1) and the lack of clarity in a fundamental theoretical equation (P1A-M1), are significant enough to require major revisions. Once these points are thoroughly addressed, the paper will be an excellent candidate for publication in Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is a complete referee report for the paper "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter".

***

## Referee Report

**Paper ID:** P1A
**Title:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Journal:** Physical Review D

This paper presents a systematic, channel-level investigation into whether minimal Einstein-Cartan-Holst (ECH) gravity can serve as a source for late-time dark energy. The authors assess four specific mechanisms and conclude that all fail at the amplitude or naturalness level under a set of clearly stated assumptions. The central results are a "perturbation-transparency theorem" for canonical scalar matter, which demonstrates that the Holst sector decouples from standard cosmological perturbations, and a catalog of 13 logically-independent "barriers" that constrain such ECH-to-dark-energy routes. The paper also identifies a structural tension between the number of e-folds required for the dark energy mechanism and the preservation of a testable matter-bounce signature in the non-Gaussianity parameter `fNL`.

The work is comprehensive, rigorous, and commendably transparent about its scope and limitations. The negative result is well-supported and of significant value to the cosmology and modified gravity communities. The distinction between a "channel-level closure" and a full "operator-level theorem" is crucial and handled correctly. The analysis of surviving, mechanism-independent observables (`fNL` and cosmic birefringence) and the associated forecasts is sophisticated.

While the paper is of high quality and suitable in principle for publication in Physical Review D, several revisions are required to address issues of internal consistency, clarity in theoretical derivations, and significant errors in the dimensional analysis of key equations. I recommend **Major Revisions** before the paper can be accepted for publication.

---

### ESSENTIAL Revisions

**P1A-E1: Internal Inconsistency in PTA Spectral Index Value**
*   **Location:** Page 4, Figure 1; Page 15, Sec. XI.G; Page 20, Table IV.
*   **Problem:** The paper uses two different values for the NANOGrav 15-yr PTA spectral index `γ`. Figure 1 quotes `γ = 3.20 ± 0.42 (P3 §6)`. However, the main text on page 15 states, "This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20±0.42 used in pre-real-KDE drafts," and provides the updated value `γ = 2.567 ± 0.382`. This updated value is also used in Table IV. The use of a superseded value in a key summary figure is confusing and unacceptable.
*   **Fix:** The paper must be made internally consistent. Replace the value in Figure 1 with the final adopted value (`γ = 2.567 ± 0.382`) and update the corresponding caption text. Remove any language about "superseded" values or "earlier drafts" from the main text; simply state the final value and its source (the companion paper).

**P1A-E2: Dimensional Error in Dark Energy Parameterization**
*   **Location:** Page 6, Eq. (10).
*   **Problem:** The central equation parameterizing the effective cosmological constant, `Λ_eff = (α/M) M_Pl D_inf`, is dimensionally incorrect. The left-hand side, `Λ_eff`, is an energy density with mass dimension +4. The right-hand side is a product of a dimensionless coupling `(α/M) M_Pl` and a dimensionless dilution factor `D_inf`, resulting in a dimensionless quantity. This fundamental error invalidates the quantitative connection between the parity-odd sector and the dark energy scale as formulated.
*   **Fix:** The authors must correct this equation. This likely requires reformulating the definition of `Ξ` or the structure of the equation to ensure the right-hand side has units of (mass)⁴. This correction will propagate through several other calculations in the paper (e.g., the required value of `N_tot`) and must be handled with care.

### MAJOR Revisions

**P1A-M1: Ambiguity and Potential Error in Four-Fermion Interaction Lagrangian**
*   **Location:** Page 5, Eq. (4).
*   **Problem:** The four-fermion contact interaction Lagrangian is given as `Lint = (3GN/2) * (γ² / (γ² + 1)) * J_5μ J^5_μ`.
    1.  The symbol `N` in the prefactor `3GN/2` is undefined and appears to be a typo, possibly for `π`.
    2.  The coefficient itself is non-standard. The classic Hehl-Datta result for the axial-axial interaction from integrating out torsion in Einstein-Cartan theory is `L_int = -(3/16) * κ * (J_5μ J^5_μ)`, where `κ = 8πG`. This gives a prefactor of `-3πG/2`. The Holst extension modifies the coupling, but the presented form with `γ² / (γ² + 1)` is not immediately recognizable and requires a clear derivation or citation to a specific result that produces this factor. As written, the equation is unsubstantiated.
*   **Fix:** The authors must clarify Eq. (4). Correct the apparent typo `N`. Provide a derivation or a precise citation for the `γ² / (γ² + 1)` dependence. If this is a known result from Freidel et al. [15] or Shapiro & Teixeira [20] as hinted in Step 4, the connection should be made explicit. If it is a novel derivation, it must be shown in an appendix.

**P1A-M2: Weak Justification for Prefactor in Inflationary Dilution Formula**
*   **Location:** Page 6, Eq. (11) and surrounding text; Page 7, text.
*   **Problem:** The inflationary dilution factor `D_inf` includes a prefactor `(T_reh / M_GUT)^(3/2)`. The justification for this term is described as "dimensional-analysis aesthetic" and based on a "phenomenological phase-space ansatz," not a first-principles calculation from a thermal partition function. While the authors are transparent about this weakness and correctly argue that the exponential term `exp[-3N_tot]` dominates the fine-tuning, the argument remains physically weak.
*   **Fix:** The authors should further emphasize that their main conclusions are entirely independent of the precise form of this algebraic prefactor. In Section XII.A ("Caveat on the (Treh/MGUT)3/2 prefactor"), they should explicitly state that the structural closure arguments and the 13 barriers of Section IX do not rely on this factor. The argument should be reframed to state that *any* pre-exponential factor of order unity (or that scales polynomially with energy scales) is insufficient to solve the 120-order-of-magnitude cosmological constant problem, which is why the exponential dilution is required in this model. This makes the argument more robust and less dependent on the weakly-justified `(3/2)` power.

**P1A-M3: Dimensional Error in LQC Critical Density Formula**
*   **Location:** Page 6, Eq. (9).
*   **Problem:** The equation relating the LQC critical density `ρ_crit` to the Planck density `ρ_Pl` is given as `ρ_crit = ... = 3 / (32π²γ³ ρ_Pl)`. This is dimensionally incorrect. Both `ρ_crit` and `ρ_Pl` are densities with units of (mass)⁴. The equation should have the form `ρ_crit = (dimensionless constant) * ρ_Pl`, not `ρ_crit ∝ 1/ρ_Pl`.
*   **Fix:** Correct the formula for `ρ_crit` in terms of `ρ_Pl`. The correct relation is `ρ_crit = (3 / (32π²γ³)) * ρ_Pl`. This is a significant error in a foundational equation and must be fixed.

**P1A-M4: Dimensionality of Parity-Odd Action**
*   **Location:** Page 6, Eq. (5).
*   **Problem:** The effective action `S_eff` is written as an integral over a 4-form `e ∧ e ∧ F`. In this formalism, the integrand has mass dimension +4, and the integral should also have dimension +4. The prefactor `α/M` has dimension -1, making the total action `S_eff` have dimension +3, which is incorrect for an action. While the authors acknowledge the dimensional problem with the component form (Eq. 6), the 4-form notation should be dimensionally consistent.
*   **Fix:** Clarify the definition of the fields or the structure of the action in Eq. (5) to ensure it is dimensionless. For example, if the action is intended to be `∫ (α/M) * (form)`, the form itself must have dimension +1, which is not standard for `e ∧ e ∧ F`. The presentation is confusing and needs to be corrected or further explained.

### MINOR Revisions

**P1A-m1: Unconventional Formula for Birefringence Angle**
*   **Location:** Page 10, Eq. (17).
*   **Problem:** The formula for the rotation angle `β ~ (α/M) * sqrt(ρ_θ) / m_θ` is a rough estimate. While dimensionally correct, it conflates the total change in the axion field with its instantaneous amplitude. The standard expression relates `β` to the total change in the field, `Δθ`, as `β = (α/M) Δθ`.
*   **Fix:** The authors should briefly clarify how their Eq. (17) is derived from the standard formula, for instance by noting that for an oscillating field, the characteristic field amplitude is `θ_0 ~ sqrt(ρ_θ) / m_θ`, and this amplitude sets the scale for the total change `Δθ`. This would make the connection to standard literature clearer.

**P1A-m2: Future Date on Manuscript**
*   **Location:** Page 1, Abstract.
*   **Problem:** The paper is dated "June 2, 2026". This is a minor artifact but should be corrected to the actual submission date.
*   **Fix:** Update the date to the current date of submission.

**P1A-m3: Citation for `fNL = -35/8`**
*   **Location:** Page 1, Abstract; Page 3, Introduction; throughout.
*   **Problem:** The result `fNL = -35/8` for a matter bounce is a cornerstone of one of the paper's "surviving" predictions. The abstract cites a work in preparation [1] for this. However, this is a classic result.
*   **Fix:** While citing their own companion paper [2] for the SPHEREx forecast is appropriate, the original derivation of `fNL = -35/8` should be cited. The current reference [1] (Cai, Xue, Brandenberger, and Zhang, 2009) is indeed one of the key original papers. The phrasing should be clear that [1] is the origin of the theoretical value and [2] is the new forecast. The current phrasing is acceptable but could be slightly sharpened to give more credit to the original authors.

**P1A-m4: Clarification of `N_tot` Tension**
*   **Location:** Page 19, Appendix B.
*   **Problem:** The appendix shows that two different ways of framing the dark energy problem lead to slightly different required e-fold counts (`N_tot ≈ 92` vs. `N_tot ≈ 94`). The text explains this `~2%` offset arises from the choice of ansatz.
*   **Fix:** This is well-explained, but for maximum clarity, the authors should add a sentence in the main body (e.g., in Sec. XIV.D) explicitly stating that the structural tension argument is robust to O(1) changes in the required `N_tot` and does not depend on this `~2%` ansatz-dependent uncertainty.

**P1A-m5: Undefined Symbol in Equation**
*   **Location:** Page 12, Eq. (18).
*   **Problem:** The equation for the effective coupling `g_eff` contains the symbol `τ₃`, which is not defined anywhere in the text. This makes the expression unintelligible.
*   **Fix:** Define `τ₃` or correct what is likely a typo.

**P1A-m6: Incorrect Internal Cross-Reference**
*   **Location:** Page 1, Abstract.
*   **Problem:** The abstract states that missing operators are acknowledged "explicitly in Sec. IV and Sec. XI." While Section IV does contain this acknowledgment, Section XI discusses a hybrid dark-energy loophole and does not appear to mention missing operators.
*   **Fix:** Correct the cross-reference. It should likely point only to Section IV.

### NIT-PICKING / COSMETIC

**P1A-N1: Awkward Phrasing in Abstract**
*   **Location:** Page 1, Abstract.
*   **Problem:** The phrase "The dark-energy mapping rests on a phenomenological on-shell scaling ansatz whose off-shell mass dimension is +1 rather than +4" is slightly dense for an abstract.
*   **Fix:** Consider simplifying to: "The connection to dark energy relies on a phenomenological scaling ansatz, as the relevant parity-odd operator has an off-shell mass dimension of +1, not the +4 required for a standard Lagrangian term."

**P1A-N2: Redundant Phrase**
*   **Location:** Page 17, Sec. XIV.D.
*   **Problem:** The text reads "...the rigorous bounce-vs-SPHEREx scale ratio is the physical scaling above with kbounce/kSPHEREx ~ e32) and the surviving bispectrum signal becomes purely vacuum-inflationary rather than matter-bounce contraction-mode." The parenthetical seems to repeat the main point.
*   **Fix:** Suggest removing the parenthetical or rephrasing for better flow, e.g., "...since the physical wavelength of modes accessible to SPHEREx is stretched by a factor of ~e^32 from the bounce to horizon exit, their surviving bispectrum signal..."

---

## Summary recommendation

**MAJOR REVISIONS**

This is a substantial and valuable contribution that performs a rigorous and systematic closure of several proposed dark energy mechanisms within the ECH framework. The perturbation-transparency theorem is an elegant and important result, and the identification of the structural tension with `fNL` is a novel insight. The paper is well-written, well-structured, and its conclusions are well-supported by the presented arguments. However, the identified issues, particularly the internal inconsistency of a key observational number (P1A-E1) and the fundamental dimensional errors in core theoretical equations (P1A-E2, P1A-M3), are significant enough to require major revisions. Once these points are thoroughly addressed, the paper will be an excellent candidate for publication in Physical Review D.