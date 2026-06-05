# P1A auto-2026-06-05_1517pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (11094 chars)
**Wall time**: 160.6s

---

## Referee Report: "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"

This manuscript investigates four potential channels through which Einstein-Cartan-Holst (ECH) gravity could source late-time dark energy. The authors conclude that all four channels fail at the amplitude level under a set of stated assumptions. The central positive result is a "perturbation-transparency theorem," which demonstrates that for canonical scalar matter, the Holst sector decouples from all scalar and tensor perturbation equations of motion. The paper also identifies two surviving, mechanism-independent predictions of the broader bounce-cosmology paradigm: a specific non-Gaussianity signature (`fNL = -35/8`) and a potential spectator-ALP-induced cosmic birefringence.

The perturbation-transparency theorem is a clear and valuable result, providing a sharp criterion for where to look for observational signatures of the Holst term. The systematic cataloging and closure of the four dark-energy routes is also a useful, albeit negative, contribution. However, the manuscript suffers from several critical flaws in its foundational arguments and quantitative expressions that must be addressed before it can be considered for publication in Physical Review D.

### ESSENTIAL Revisions

**P1A-E1: Foundational Weakness of the Dark-Energy Operator Ansatz**
*   **Location:** Abstract (p. 1), Sec. I (p. 3), Sec. II C (p. 6), Appendix B (p. 19).
*   **Problem:** The entire dark-energy analysis rests on a "phenomenological on-shell scaling ansatz" for a parity-odd operator (Eq. 6) which has an off-shell mass dimension of +1, not the required +4 for a Lagrangian density. Appendix B attempts to remedy this by inserting powers of the Planck mass by hand, stating explicitly "we treat this mapping explicitly as an ansatz, not a derivation." This procedure is not a controlled effective field theory (EFT) construction; it is dimensionally incorrect at the fundamental level. The paper's primary claim is the "closure" of dark-energy routes, but these routes are only opened in the first place by this physically unjustified and dimensionally problematic ansatz.
*   **Required Fix:** The authors must significantly reframe the entire dark-energy portion of the paper. The analysis should be presented not as a closure of viable physical routes, but as a demonstration that even when granting a highly speculative, dimensionally-forced ansatz, the resulting phenomenology is inconsistent with observation. The abstract and introduction must state upfront that the dark-energy operator under consideration is not derived from a controlled EFT and has a problematic dimensionality, and that this is the fundamental reason the dark-energy connection fails. The current framing, while honest about the "ansatz" nature, does not sufficiently emphasize how deeply this assumption undermines the premise of the investigation.

**P1A-E2: Incorrect Formulation of Inflationary Scale Mapping**
*   **Location:** Abstract (p. 1), Sec. III A (p. 3), Sec. XIV D (p. 17).
*   **Problem:** The quantitative argument for the erasure of the matter-bounce `fNL` signature is based on a dimensionally incorrect and physically obscure formula: `k_phys_bounce ~ k_SPHEREx * e^(N_tot - N_exit)`. A comoving wavenumber (`k_SPHEREx`) cannot be related to a physical wavenumber (`k_phys_bounce`) by multiplication with a dimensionless exponential factor. The subsequent claim that `k_phys_bounce / k_phys_SPHEREx ~ e^32` is also ill-defined. While the physical principle—that a sufficient number of inflationary e-folds erases pre-inflationary signatures on observable scales—is correct, the mathematical expression used throughout the manuscript is wrong.
*   **Required Fix:** The authors must remove this incorrect formula and replace it with a correct, first-principles derivation. This should involve defining the comoving horizon size at the bounce (`1/(a_b H_b)`) and showing that the comoving scales probed by SPHEREx (`k_SPHEREx`) are much smaller than this scale (`k_SPHEREx \gg a_b H_b`) if the total number of e-folds `N_tot` is large. The derivation should clearly track the evolution of physical scales relative to the Hubble radius through the bounce and inflationary epochs. This correction is essential for the "structural tension" argument to be quantitatively sound.

### MAJOR Revisions

**P1A-M1: Inconsistent Values for the Number of e-Folds (N)**
*   **Location:** Abstract (p. 1), Sec. II C (p. 6), Fig. 2 caption (p. 5), Sec. XII A (p. 15), Sec. XIV D (p. 17).
*   **Problem:** The manuscript uses multiple, inconsistent values for the number of inflationary e-folds. The abstract and main argument for dark energy require `N_tot ≈ 92`. The discussion of parameter naturalness in Sec. II C 3 mentions `~50 e-folds`. The caption for Figure 2 uses `N ≈ 55 e-folds`. These numbers are not interchangeable and their different origins are not clearly explained. `N ≈ 50-60` is the standard value required to solve the horizon and flatness problems, while `N_tot ≈ 92` is presented as the value *fitted* to make the dark energy ansatz work.
*   **Required Fix:** The authors must clarify the meaning and origin of each value of `N` used. The `N_tot ≈ 92` value should be consistently presented as the *required* number of e-folds under their specific ansatz, not a general feature. The potential tension between the `N_tot` required for the DE mechanism and the `N` required to solve standard cosmological problems should be explicitly discussed. All figures and text must be made consistent.

**P1A-M2: Weak Justification for the Thermal Prefactor in the Dilution Factor**
*   **Location:** Sec. II C 1 (p. 6), Sec. VII (p. 7).
*   **Problem:** The inflationary dilution factor `D_inf` in Eq. (11) includes a prefactor `(T_reh / M_GUT)^(3/2)`. The justification for this term is described as "dimensional-analysis aesthetic" and a "phenomenological phase-space ansatz," not a calculation from a thermal partition function. This introduces a significant, unquantified uncertainty into the calculation of `N_tot ≈ 92`.
*   **Required Fix:** The authors should either provide a more rigorous derivation for this prefactor or, more appropriately, absorb it into the overall uncertainty of the calculation. They should explicitly state that the precise value of `N_tot` is sensitive to this prefactor, which is not robustly derived, and discuss how this affects their conclusions. This reinforces the finding that the dark-energy mechanism is not predictive.

### MINOR Revisions

**P1A-m1: Contradictory Status of the Ekpyrotic Scenario**
*   **Location:** Figure 1 (p. 4).
*   **Problem:** In Figure 1, the box for the "Ekpyrotic" mechanism has text that says "produces ECH; permitted," but a dashed arrow points from it to a box labeled "structurally closed (this paper)." This is contradictory and confusing.
*   **Required Fix:** Clarify the intended meaning. If the paper closes the ECH-mediated aspects of an ekpyrotic scenario, the diagram and caption should state this clearly. If not, the arrow and "structurally closed" label should be removed for this path.

**P1A-m2: Ambiguous Scope of "Channel-Level Closure"**
*   **Location:** Abstract (p. 1), Sec. IV (p. 8).
*   **Problem:** The paper emphasizes that its closure is at the "channel-level" and not the "operator-level," and lists specific missing operators (e.g., gravitational Chern-Simons `R∧R`). However, the distinction and its implications could be made clearer for the reader.
*   **Required Fix:** Briefly explain in the introduction *why* an operator-level closure is more difficult and what new possibilities it might allow. This would better frame the scope and contribution of the present work.

### NITs (Cosmetic)

**P1A-N1: Future Date**
*   **Location:** p. 1.
*   **Problem:** The paper is dated "June 2, 2026 PDT."
*   **Required Fix:** Change to the current date of submission.

**P1A-N2: Informal Email Address**
*   **Location:** p. 1.
*   **Problem:** The contact email `houston@hubify.com` is unconventional for an academic publication.
*   **Required Fix:** Use a standard institutional or academic email address if available.

## Summary recommendation

**MAJOR REVISIONS**

This paper presents a valuable and rigorous proof of a perturbation-transparency theorem for the Holst action with scalar matter, which is a significant contribution. The systematic analysis of potential dark-energy channels is also thorough. However, the entire dark-energy component of the manuscript is built upon a dimensionally flawed operator ansatz (P1A-E1), and a key quantitative argument about the erasure of primordial signals is based on an incorrect formula (P1A-E2). These are not minor issues; they go to the core of the paper's central claims.

The paper can be made suitable for publication if the authors perform a major revision to correct these foundational flaws. The focus should be shifted to the robust perturbation-transparency theorem, with the dark-energy analysis reframed as a demonstration of the failures that arise from a speculative, non-EFT-controlled starting point. The incorrect scale-mapping equations must be re-derived from scratch. If these essential changes are made, the revised manuscript would represent a solid contribution to the literature on alternative cosmologies and quantum gravity phenomenology.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated referee report, incorporating the findings from the second, more detailed review.

================================================================
## Referee Report: "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"

This manuscript investigates four potential channels through which Einstein-Cartan-Holst (ECH) gravity could source late-time dark energy. The authors conclude that all four channels fail at the amplitude level under a set of stated assumptions. The central positive result is a "perturbation-transparency theorem," which demonstrates that for canonical scalar matter, the Holst sector decouples from all scalar and tensor perturbation equations of motion. The paper also identifies two surviving, mechanism-independent predictions of the broader bounce-cosmology paradigm: a specific non-Gaussianity signature (`fNL = -35/8`) and a potential spectator-ALP-induced cosmic birefringence.

The perturbation-transparency theorem is a clear and valuable result, providing a sharp criterion for where to look for observational signatures of the Holst term. The systematic cataloging and closure of the four dark-energy routes is also a useful, albeit negative, contribution. However, the manuscript suffers from several critical flaws in its foundational arguments, dimensional analysis, and quantitative expressions that must be addressed before it can be considered for publication in Physical Review D.

### ESSENTIAL Revisions

**P1A-E1: Foundational Weakness of the Dark-Energy Operator Ansatz**
*   **Location:** Abstract (p. 1), Sec. I (p. 3), Sec. II C (p. 6), Appendix B (p. 19).
*   **Problem:** The entire dark-energy analysis rests on a "phenomenological on-shell scaling ansatz" for a parity-odd operator (Eq. 6) which has an off-shell mass dimension of +1, not the required +4 for a Lagrangian density. Appendix B attempts to remedy this by inserting powers of the Planck mass by hand, stating explicitly "we treat this mapping explicitly as an ansatz, not a derivation." This procedure is not a controlled effective field theory (EFT) construction; it is dimensionally incorrect at the fundamental level. The paper's primary claim is the "closure" of dark-energy routes, but these routes are only opened in the first place by this physically unjustified and dimensionally problematic ansatz.
*   **Required Fix:** The authors must significantly reframe the entire dark-energy portion of the paper. The analysis should be presented not as a closure of viable physical routes, but as a demonstration that even when granting a highly speculative, dimensionally-forced ansatz, the resulting phenomenology is inconsistent with observation. The abstract and introduction must state upfront that the dark-energy operator under consideration is not derived from a controlled EFT and has a problematic dimensionality, and that this is the fundamental reason the dark-energy connection fails.

**P1A-E2: Incorrect Formulation of Inflationary Scale Mapping**
*   **Location:** Abstract (p. 1), Sec. III A (p. 3), Sec. XIV D (p. 17).
*   **Problem:** The quantitative argument for the erasure of the matter-bounce `fNL` signature is based on a dimensionally incorrect and physically obscure formula: `k_phys_bounce ~ k_SPHEREx * e^(N_tot - N_exit)`. A comoving wavenumber (`k_SPHEREx`) cannot be related to a physical wavenumber (`k_phys_bounce`) by multiplication with a dimensionless exponential factor. While the physical principle—that a sufficient number of inflationary e-folds erases pre-inflationary signatures on observable scales—is correct, the mathematical expression used throughout the manuscript is wrong.
*   **Required Fix:** The authors must remove this incorrect formula and replace it with a correct, first-principles derivation. This should involve defining the comoving horizon size at the bounce (`1/(a_b H_b)`) and showing that the comoving scales probed by SPHEREx (`k_SPHEREx`) are much smaller than this scale (`k_SPHEREx \gg a_b H_b`) if the total number of e-folds `N_tot` is large. The derivation should clearly track the evolution of physical scales relative to the Hubble radius.

**P1A-E3: Dimensionally Incorrect Formula in Figure 2 Caption**
*   **Location:** Figure 2 Caption (p. 5).
*   **Problem:** The caption for Figure 2 presents the scaling ansatz as `ρ_vac ~ [(α/M) M_Pl] M_Pl³`. This expression is dimensionally incorrect: `[α/M]` has units of `Mass⁻¹`, so the right-hand side has units of `Mass³`, not `Mass⁴` as required for an energy density.
*   **Required Fix:** This formula must be corrected to be dimensionally consistent with an energy density. This error, present in a key illustrative figure, compounds the confusion surrounding the central ansatz of the paper.

**P1A-E4: Inconsistent and Dimensionally Incorrect Appendix**
*   **Location:** Appendix B (p. 19).
*   **Problem:** Appendix B, which is supposed to clarify the dimensional status of the parity-odd operator, is itself internally inconsistent and incorrect. Equation (B2), `ρ_Λ^bounce ~ (α/M) M_Pl³`, is dimensionally wrong, yielding units of `Mass²` instead of `Mass⁴`. The subsequent text describes a different modification (`α → α M_Pl³/M`) that *would* yield the correct dimensions, creating a direct contradiction between the appendix's core equation and its explanatory text.
*   **Required Fix:** The entire appendix must be rewritten for clarity and correctness. A single, consistent, and dimensionally-sound (even if phenomenological) expression must be used. As it stands, the appendix undermines the reader's confidence in the paper's technical foundations.

### MAJOR Revisions

**P1A-M1: Inconsistent Values for the Number of e-Folds (N)**
*   **Location:** Abstract (p. 1), Sec. II C (p. 6), Fig. 2 caption (p. 5), Sec. XII A (p. 15), Sec. XIV D (p. 17).
*   **Problem:** The manuscript uses multiple, inconsistent values for the number of inflationary e-folds (`N_tot ≈ 92`, `~50`, `N ≈ 55`). These numbers are not interchangeable and their different origins are not clearly explained.
*   **Required Fix:** Clarify the meaning and origin of each value of `N` used. The `N_tot ≈ 92` value should be consistently presented as the *required* number of e-folds under their specific ansatz, not a general feature. The potential tension between this value and the `N ≈ 50-60` required to solve standard cosmological problems should be explicitly discussed.

**P1A-M2: Weak Justification for the Thermal Prefactor in the Dilution Factor**
*   **Location:** Sec. II C 1 (p. 6), Sec. VII (p. 7).
*   **Problem:** The inflationary dilution factor `D_inf` in Eq. (11) includes a prefactor `(T_reh / M_GUT)^(3/2)`. The justification for this term is described as "dimensional-analysis aesthetic" and a "phenomenological phase-space ansatz," not a rigorous calculation. This introduces a significant, unquantified uncertainty into the calculation of `N_tot ≈ 92`.
*   **Required Fix:** The authors should either provide a more rigorous derivation or absorb this prefactor into the overall uncertainty of the calculation. They should explicitly state that the precise value of `N_tot` is sensitive to this non-robust prefactor, reinforcing the conclusion that the dark-energy mechanism is not predictive.

**P1A-M3: Incorrect Labeling of One-Loop Action**
*   **Location:** Eq. (14) (p. 9).
*   **Problem:** Equation (14) is labeled as an energy density (`ρ_parity-odd_one-loop`) but is written as a dimensionless action term (`∫ d⁴x ...`). This is a fundamental dimensional error.
*   **Required Fix:** The equation must be correctly labeled as an action, `S_parity-odd_one-loop`.

**P1A-M4: Dimensionally Inconsistent Coupling**
*   **Location:** Eq. (18) (p. 12).
*   **Problem:** The middle term in the expression for the effective coupling, `g_eff ~ 1 / (M_Pl √τ³) `, is dimensionally inconsistent. If `τ` is a time or length scale, this expression does not yield a dimensionless number.
*   **Required Fix:** The authors must define `τ` and correct this expression to be dimensionally sound.

### MINOR Revisions

**P1A-m1: Contradictory Status of the Ekpyrotic Scenario**
*   **Location:** Figure 1 (p. 4).
*   **Problem:** In Figure 1, the box for the "Ekpyrotic" mechanism has text that says "produces ECH; permitted," but a dashed arrow points from it to a box labeled "structurally closed (this paper)." This is contradictory.
*   **Required Fix:** Clarify the intended meaning. If the paper closes the ECH-mediated aspects of an ekpyrotic scenario, the diagram and caption should state this clearly.

**P1A-m2: Ambiguous Scope of "Channel-Level Closure"**
*   **Location:** Abstract (p. 1), Sec. IV (p. 8).
*   **Problem:** The paper emphasizes that its closure is at the "channel-level" and not the "operator-level." The distinction and its implications could be made clearer.
*   **Required Fix:** Briefly explain in the introduction *why* an operator-level closure is more difficult and what new possibilities it might allow. This would better frame the scope and contribution of the present work.

**P1A-m3: Arithmetic Discrepancy**
*   **Location:** Sec. D (p. 10).
*   **Problem:** The claim that the spectator-ALP route reproduces the dark energy density `ρ_Λ` "to within a factor of unity" is inaccurate. A direct calculation using the paper's own numbers shows a discrepancy of a factor of ~1.4.
*   **Required Fix:** The authors should either correct their input parameters or acknowledge the discrepancy more accurately than with the current hedge.

### NITs (Cosmetic)

**P1A-N1: Future Date:** The paper is dated "June 2, 2026 PDT." This should be corrected.
**P1A-N2: Informal Email Address:** The contact email `houston@hubify.com` is unconventional for an academic publication.
**P1A-N3: Incorrect Cross-Reference:** The abstract's reference to Sec. XI for a discussion of missing operators is incorrect.

## Summary recommendation

**MAJOR REVISIONS**

This paper presents a valuable and rigorous proof of a perturbation-transparency theorem for the Holst action with scalar matter, which is a significant contribution. However, the entire dark-energy component of the manuscript is built upon a dimensionally flawed and internally inconsistent operator ansatz (P1A-E1, E3, E4). Furthermore, several key equations throughout the text suffer from dimensional inconsistencies (P1A-E2, M3, M4). These are not minor issues; they represent a lack of rigor that undermines the paper's central claims about dark energy.

The paper can be made suitable for publication only after a major revision to correct these foundational flaws. The focus should be shifted to the robust perturbation-transparency theorem, with the dark-energy analysis reframed as a demonstration of the failures that arise from a speculative, non-EFT-controlled starting point. All dimensionally incorrect equations must be re-derived and corrected. If these essential changes are made, the revised manuscript would represent a solid contribution to the literature.