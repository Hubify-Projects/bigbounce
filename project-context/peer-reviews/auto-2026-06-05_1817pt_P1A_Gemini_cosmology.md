# P1A auto-2026-06-05_1817pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (13533 chars)
**Wall time**: 152.3s

---

**Referee Report for PRD Manuscript**

**Manuscript ID:** [Fictional ID]
**Title:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Author:** Houston Golden

This paper investigates four potential channels through which Einstein-Cartan-Holst (ECH) gravity could source late-time dark energy. The author concludes that all four channels are closed at the amplitude level under a set of stated assumptions. The main contributions are a "perturbation-transparency theorem," which shows that the Holst sector decouples from scalar and tensor perturbations for canonical scalar matter, and a "structural tension" argument, which posits an incompatibility between the number of inflationary e-folds required for the dark energy mechanism and the number required to preserve a testable matter-bounce signature (`f_NL`).

The perturbation-transparency theorem is a clear, well-derived, and useful result. The structural tension argument is also physically compelling. However, the paper suffers from several fundamental issues that preclude its publication in Physical Review D in its current form. The central dark-energy mechanism is built upon a phenomenologically-motivated but dimensionally inconsistent operator, and the paper's key observational claims are not self-contained, relying heavily on results from multiple companion papers cited as "in preparation."

The following is a detailed list of required revisions.

---

### ESSENTIAL Revisions

**P1A-E1: Fundamentally Unsound Dark-Energy Operator (Abstract; Sec. I; Sec. II C; Appendix B, p. 1, 3, 6, 19)**
The entire dark-energy mechanism proposed in the paper rests on a parity-odd operator (Eq. 6) which the author admits has an off-shell mass dimension of +1, not the +4 required for a valid Lagrangian density. Appendix B explicitly states: "We acknowledge openly that this operator, as written, is not a controlled dimension-+4 EFT operator." The proposed "fix" is an "on-shell scaling ansatz," which is explicitly labeled "a phenomenological dimensional assignment, not a derivation."
*   **Problem:** A physical theory cannot be built upon a dimensionally inconsistent operator, and an "ansatz" is not a substitute for a derivation from a valid effective field theory. This invalidates the central claim that the paper connects ECH to dark energy. While the author is commendably transparent about this issue, transparency does not resolve the fundamental flaw in the physics.
*   **Required Fix:** The author must either (a) provide a rigorous derivation of a dimension-+4 operator from the fundamental ECH action that can source dark energy, or (b) completely re-scope the paper to remove the dark-energy claims. The paper could be reframed to focus solely on the robust results: the perturbation-transparency theorem and the constraints this places on any potential ECH phenomenology. The "closure" of dark-energy routes cannot be claimed if the routes themselves are not well-defined.

**P1A-E2: Unverifiable Claims from Unpublished Companion Papers (Throughout)**
The paper repeatedly cites companion works as "in preparation" to support its core observational and phenomenological claims. This includes:
*   The `f_NL = -35/8` SPHEREx forecast ([2]).
*   All MCMC parameter values (`H_0`, `ΔN_eff`, etc.), pipeline validation, and ALP parameter fitting ([6]).
*   The galaxy spin null result ([23]).
*   The multi-survey anomaly catalog ([46]).
*   **Problem:** A manuscript submitted for peer review must be self-contained. It is impossible for a referee to verify claims, check calculations, or assess the validity of results that are presented in unavailable manuscripts. This practice violates the standards of reproducibility and verifiability required for publication.
*   **Required Fix:** All claims and results that depend on these "in preparation" papers must be removed. Alternatively, the author must incorporate the full analysis and derivations for these results into the present manuscript (e.g., in appendices) or submit the companion papers for review simultaneously. The paper must be evaluable on its own merits.

### MAJOR Revisions

**P1A-M1: Non-Rigorous Derivation of Inflationary Dilution (Sec. II C 1; Sec. XII A, p. 6-7, 15)**
The inflationary suppression factor `D_inf` in Eq. (11) includes a prefactor `(T_reh/M_GUT)^(3/2)`. The derivation of this term is described as "dimensional-analysis aesthetic at this level rather than calculated from a thermal partition function" (p. 6) and an "aesthetic estimate" (p. 15).
*   **Problem:** This level of justification is insufficient for a quantitative claim in PRD. A hand-waving argument based on "aesthetics" is not a physical derivation. This weakens the subsequent calculation of `N_tot ≈ 92`, which depends on this factor.
*   **Required Fix:** The author must provide a rigorous first-principles derivation of this prefactor from a phase-space or partition-function calculation. If this is not possible, the entire quantitative argument for `N_tot ≈ 92` must be presented as purely schematic and illustrative, and all claims of precision (e.g., the "2% offset" discussion in Appendix B) must be removed.

**P1A-M2: Overstated "Structural Constraints" (Sec. IX; Table II, p. 12-13)**
The paper presents a catalog of 14 "mechanism-class constraints" (13 of which are claimed to be logically independent) that purportedly map the minimal ECH parameter space.
*   **Problem:** The rigor and independence of these constraints are questionable. Several "barriers" appear to be philosophical or qualitative rather than quantitative constraints (e.g., B10: "UV→IR Specificity Dilemma," B13: "Gravitational Democracy"). Others seem to be re-statements of the same underlying physical principle (e.g., B1 "Mass-Coupling Lock" and B4 "Planck Suppression"). The claim of "13 logically-independent" barriers is not adequately justified.
*   **Required Fix:** The author should significantly revise this section. The list should be streamlined to include only rigorously derived, quantitative, and demonstrably independent constraints. Philosophical arguments should be removed or clearly separated from physical constraints. The language should be toned down from definitive "barriers" to "qualitative challenges" or "consistency checks" where appropriate.

### MINOR Revisions

**P1A-m1: Inconsistent `f_NL` Forecast Value (Table I; Sec. VII; Footnote 1, p. 4, 11)**
The paper quotes a SPHEREx forecast of `σ(f_NL) ≈ 0.7` in Table I, but Footnote 1 on page 11 reveals this is a "Fisher-ideal" value, and the realistic, degraded value is closer to `σ(f_NL) ≈ 1.0`. The abstract of the cited reference [36] (Heinrich et al. 2024) reports `σ(f_NL^loc) = 1.6`.
*   **Problem:** The most optimistic, "ideal" value is presented in the main summary table, which is misleading. The value also appears inconsistent with the cited literature.
*   **Required Fix:** The main text and tables should use the most realistic, fully-degraded forecast value (`σ(f_NL) ≈ 1.0` or `1.6`). The distinction between ideal and realistic forecasts should be made clear in the main text, not just a footnote. The discrepancy with the cited paper's abstract must be resolved.

**P1A-m2: Paper Length and Structure (Full paper)**
The paper is 21 pages long. The core, defensible contributions are the perturbation-transparency theorem (Sec. X) and the four-route amplitude-level closure arguments (Sec. IV). The lengthy catalog of "barriers" in Sec. IX adds significant length but, as noted in P1A-M2, is of questionable rigor.
*   **Problem:** The paper's length is not justified by the amount of novel, rigorously-derived content.
*   **Required Fix:** The author should consider restructuring the paper. The main text should focus on the key results (Sec. IV and X). The less rigorous "barriers" section (Sec. IX) should be heavily condensed or moved to an appendix.

**P1A-m3: Ambiguous Wording in "Structural Tension" Argument (Abstract; Sec. XIV D, p. 1, 17)**
The abstract states that a mode with `k_SPHEREx` is pushed to `k_phys,bounce ~ k_SPHEREx,phys,exit * e^(N_tot - N_exit)`.
*   **Problem:** The notation and explanation are confusing. It appears to be comparing the physical momentum at the bounce to the physical momentum at horizon exit, but the factor `e^(N_tot - N_exit)` corresponds to the expansion between horizon exit and the end of inflation.
*   **Required Fix:** Clarify the argument and notation. A more standard and clear way to express this is that for `N_tot` e-folds of inflation, any comoving scale `k` observable today was `e^N_tot` times smaller than the Hubble radius at the time of the bounce, placing it deep in the sub-horizon regime where any pre-existing fluctuations would be erased.

### NIT-PICKS

**P1A-N1: Superseded Value Mentioned (Sec. XI G, p. 15)**
The text states: "This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20±0.42 used in pre-real-KDE drafts".
*   **Problem:** Internal draft history and superseded values should not appear in a final manuscript.
*   **Required Fix:** Remove this sentence.

**P1A-N2: Inconsistent Date Formatting in References (p. 19-21)**
Reference [9] is listed as "(2024)" while reference [10] is listed as "(2025)", though both are 2024 preprints. Reference [5] is listed as "(2025)" for a 2025 preprint. The paper itself is dated 2026. This is inconsistent.
*   **Problem:** Inconsistent and potentially incorrect publication years.
*   **Required Fix:** Correct the publication years for all references to reflect their actual status (e.g., for preprints, use the year of submission).

---

## Summary recommendation

**MAJOR REVISIONS**

This manuscript contains the kernel of a valuable contribution to the literature, namely the perturbation-transparency theorem for minimal ECH gravity and the associated argument that its phenomenology must be sought in non-perturbative channels. The "structural tension" between a hypothetical ECH dark energy mechanism and the survival of matter-bounce signatures is also a compelling point. However, the paper in its current form is unacceptable. The central claim of connecting ECH to dark energy is based on a physically unsound, dimensionally incorrect operator, and the paper's empirical support rests entirely on unverifiable results from unpublished companion works.

For the paper to be reconsidered for publication in Physical Review D, the author must address the ESSENTIAL points. This will likely require a significant re-scoping of the paper away from the dark energy claims and toward the robust, self-contained theoretical results. If the author can provide a rigorous foundation for the dark energy operator and make the paper self-contained, it could become a significant work. Otherwise, it should be revised to a more modest scope.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated referee report, incorporating the new findings from the second, more rigorous review.

================================================================
**Referee Report for PRD Manuscript**

**Manuscript ID:** [Fictional ID]
**Title:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Author:** Houston Golden

This paper investigates four potential channels through which Einstein-Cartan-Holst (ECH) gravity could source late-time dark energy. The author concludes that all four channels are closed at the amplitude level under a set of stated assumptions. The main contributions are a "perturbation-transparency theorem," which shows that the Holst sector decouples from scalar and tensor perturbations for canonical scalar matter, and a "structural tension" argument, which posits an incompatibility between the number of inflationary e-folds required for the dark energy mechanism and the number required to preserve a testable matter-bounce signature (`f_NL`).

The perturbation-transparency theorem is a clear, well-derived, and useful result. The structural tension argument is also physically compelling. However, the paper suffers from several fundamental issues that preclude its publication in Physical Review D in its current form. The central dark-energy mechanism is built upon a phenomenologically-motivated but dimensionally inconsistent operator, the paper contains basic errors in the dimensional analysis of key physical equations, and its core observational claims are not self-contained, relying heavily on results from multiple companion papers cited as "in preparation."

The following is a detailed list of required revisions.

---

### ESSENTIAL Revisions

**P1A-E1: Fundamentally Unsound Dark-Energy Operator (Abstract; Sec. I; Sec. II C; Appendix B, p. 1, 3, 6, 19)**
The entire dark-energy mechanism proposed in the paper rests on a parity-odd operator (Eq. 6) which the author admits has an off-shell mass dimension of +1, not the +4 required for a valid Lagrangian density. Appendix B explicitly states: "We acknowledge openly that this operator, as written, is not a controlled dimension-+4 EFT operator." The proposed "fix" is an "on-shell scaling ansatz," which is explicitly labeled "a phenomenological dimensional assignment, not a derivation."
*   **Problem:** A physical theory cannot be built upon a dimensionally inconsistent operator, and an "ansatz" is not a substitute for a derivation from a valid effective field theory. This invalidates the central claim that the paper connects ECH to dark energy. While the author is commendably transparent about this issue, transparency does not resolve the fundamental flaw in the physics.
*   **Required Fix:** The author must either (a) provide a rigorous derivation of a dimension-+4 operator from the fundamental ECH action that can source dark energy, or (b) completely re-scope the paper to remove the dark-energy claims. The paper could be reframed to focus solely on the robust results: the perturbation-transparency theorem and the constraints this places on any potential ECH phenomenology. The "closure" of dark-energy routes cannot be claimed if the routes themselves are not well-defined.

**P1A-E2: Unverifiable Claims from Unpublished Companion Papers (Throughout)**
The paper repeatedly cites companion works as "in preparation" to support its core observational and phenomenological claims. This includes:
*   The `f_NL = -35/8` SPHEREx forecast ([2]).
*   All MCMC parameter values (`H_0`, `ΔN_eff`, etc.), pipeline validation, and ALP parameter fitting ([6]).
*   The galaxy spin null result ([23]).
*   The multi-survey anomaly catalog ([46]).
*   **Problem:** A manuscript submitted for peer review must be self-contained. It is impossible for a referee to verify claims, check calculations, or assess the validity of results that are presented in unavailable manuscripts. This practice violates the standards of reproducibility and verifiability required for publication.
*   **Required Fix:** All claims and results that depend on these "in preparation" papers must be removed. Alternatively, the author must incorporate the full analysis and derivations for these results into the present manuscript (e.g., in appendices) or submit the companion papers for review simultaneously. The paper must be evaluable on its own merits.

**P1A-E3: Typo and Dimensional Error in Core LQC Equation (p. 6, Eq. 9)**
The equation for the LQC critical density, `ρ_crit`, is presented as `3 / (32π²γ³ ρ_Pl)`.
*   **Problem:** This equation is dimensionally incorrect. The left side, `ρ_crit`, has units of energy density (Mass⁴), while the right side is dimensionless. The source literature formula involves `G²ħ` or `l_Pl²`, not `ρ_Pl`, in the denominator. This is a fundamental error in a core equation of the theoretical framework.
*   **Required Fix:** The author must correct this equation to be dimensionally and physically sound, ensuring it matches the cited literature. This error undermines confidence in the paper's theoretical rigor.

**P1A-E4: Dimensionally Inconsistent Equation for Birefringence (p. 10, Eq. 17)**
The equation for the induced birefringence angle is given as `β ~ (α/M) √(ρ_θ) / m_θ²`.
*   **Problem:** This equation is dimensionally inconsistent. The angle `β` on the left is dimensionless, while the expression on the right has units of `Mass⁻¹`. A correct derivation would likely yield a denominator proportional to a single power of mass (e.g., `H_0` or `m_θ`), not `m_θ²`.
*   **Required Fix:** The author must derive and present the correct, dimensionally consistent equation for the birefringence angle. This error invalidates the quantitative claims made in Section IV D regarding the spectator ALP route.

### MAJOR Revisions

**P1A-M1: Non-Rigorous Derivation of Inflationary Dilution (Sec. II C 1; Sec. XII A, p. 6-7, 15)**
The inflationary suppression factor `D_inf` in Eq. (11) includes a prefactor `(T_reh/M_GUT)^(3/2)`. The derivation of this term is described as "dimensional-analysis aesthetic at this level rather than calculated from a thermal partition function" (p. 6) and an "aesthetic estimate" (p. 15).
*   **Problem:** This level of justification is insufficient for a quantitative claim in PRD. A hand-waving argument based on "aesthetics" is not a physical derivation. This weakens the subsequent calculation of `N_tot ≈ 92`, which depends on this factor.
*   **Required Fix:** The author must provide a rigorous first-principles derivation of this prefactor from a phase-space or partition-function calculation. If this is not possible, the entire quantitative argument for `N_tot ≈ 92` must be presented as purely schematic and illustrative, and all claims of precision (e.g., the "2% offset" discussion in Appendix B) must be removed.

**P1A-M2: Overstated "Structural Constraints" (Sec. IX; Table II, p. 12-13)**
The paper presents a catalog of 14 "mechanism-class constraints" (13 of which are claimed to be logically independent) that purportedly map the minimal ECH parameter space.
*   **Problem:** The rigor and independence of these constraints are questionable. Several "barriers" appear to be philosophical or qualitative rather than quantitative constraints (e.g., B10: "UV→IR Specificity Dilemma," B13: "Gravitational Democracy"). Others seem to be re-statements of the same underlying physical principle (e.g., B1 "Mass-Coupling Lock" and B4 "Planck Suppression"). The claim of "13 logically-independent" barriers is not adequately justified.
*   **Required Fix:** The author should significantly revise this section. The list should be streamlined to include only rigorously derived, quantitative, and demonstrably independent constraints. Philosophical arguments should be removed or clearly separated from physical constraints. The language should be toned down from definitive "barriers" to "qualitative challenges" or "consistency checks" where appropriate.

**P1A-M3: Incorrect Internal Cross-Reference (Abstract)**
The abstract states that missing operators are acknowledged "explicitly in Sec. IV and Sec. XI."
*   **Problem:** Section XI, "The Hybrid Dark-Energy Loophole," does not appear to discuss these missing operators. This reference is incorrect.
*   **Required Fix:** Correct all internal cross-references. This particular error suggests a lack of careful proofreading.

**P1A-M4: Weakening of MCMC Results (p. 17, Sec. XIV A)**
The paper admits in Section XIV that the MCMC analysis uses a "phenomenological proxy" (stock CAMB with `ΔN_eff`) and not a "bespoke spin-torsion Boltzmann module."
*   **Problem:** This is a critical caveat that is not given sufficient prominence. It implies that the cosmological parameter values quoted throughout the paper are not direct constraints on the ECH model but rather on a proxy model.
*   **Required Fix:** This limitation must be stated clearly in the abstract and introduction, not just buried in the "Limitations" section. The author must be more circumspect when presenting the MCMC results as evidence for or against the ECH framework.

### MINOR Revisions

**P1A-m1: Inconsistent `f_NL` Forecast Value (Table I; Sec. VII; Footnote 1, p. 4, 11)**
The paper quotes a SPHEREx forecast of `σ(f_NL) ≈ 0.7` in Table I, but Footnote 1 on page 11 reveals this is a "Fisher-ideal" value, and the realistic, degraded value is closer to `σ(f_NL) ≈ 1.0`. The abstract of the cited reference [36] (Heinrich et al. 2024) reports `σ(f_NL^loc) = 1.6`.
*   **Problem:** The most optimistic, "ideal" value is presented in the main summary table, which is misleading. The value also appears inconsistent with the cited literature.
*   **Required Fix:** The main text and tables should use the most realistic, fully-degraded forecast value (`σ(f_NL) ≈ 1.0` or `1.6`). The distinction between ideal and realistic forecasts should be made clear in the main text, not just a footnote. The discrepancy with the cited paper's abstract must be resolved.

**P1A-m2: Paper Length and Structure (Full paper)**
The paper is 21 pages long. The core, defensible contributions are the perturbation-transparency theorem (Sec. X) and the four-route amplitude-level closure arguments (Sec. IV). The lengthy catalog of "barriers" in Sec. IX adds significant length but, as noted in P1A-M2, is of questionable rigor.
*   **Problem:** The paper's length is not justified by the amount of novel, rigorously-derived content.
*   **Required Fix:** The author should consider restructuring the paper. The main text should focus on the key results (Sec. IV and X). The less rigorous "barriers" section (Sec. IX) should be heavily condensed or moved to an appendix.

**P1A-m3: Ambiguous Wording in "Structural Tension" Argument (Abstract; Sec. XIV D, p. 1, 17)**
The abstract states that a mode with `k_SPHEREx` is pushed to `k_phys,bounce ~ k_SPHEREx,phys,exit * e^(N_tot - N_exit)`.
*   **Problem:** The notation and explanation are confusing.
*   **Required Fix:** Clarify the argument and notation. A more standard and clear way to express this is that for `N_tot` e-folds of inflation, any comoving scale `k` observable today was `e^N_tot` times smaller than the Hubble radius at the time of the bounce, placing it deep in the sub-horizon regime where any pre-existing fluctuations would be erased.

### NIT-PICKS

**P1A-N1: Superseded Value Mentioned (Sec. XI G, p. 15)**
The text states: "This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20±0.42 used in pre-real-KDE drafts".
*   **Problem:** Internal draft history and superseded values should not appear in a final manuscript.
*   **Required Fix:** Remove this sentence.

**P1A-N2: Inconsistent Date Formatting in References (p. 19-21)**
Reference [9] is listed as "(2024)" while reference [10] is listed as "(2025)", though both are 2024 preprints. Reference [5] is listed as "(2025)" for a 2025 preprint. The paper itself is dated 2026. This is inconsistent.
*   **Problem:** Inconsistent and potentially incorrect publication years.
*   **Required Fix:** Correct the publication years for all references to reflect their actual status (e.g., for preprints, use the year of submission).

---

## Summary recommendation

**MAJOR REVISIONS**

This manuscript contains the kernel of a valuable contribution to the literature, namely the perturbation-transparency theorem for minimal ECH gravity and the associated argument that its phenomenology must be sought in non-perturbative channels. The "structural tension" between a hypothetical ECH dark energy mechanism and the survival of matter-bounce signatures is also a compelling point. However, the paper in its current form is unacceptable. It is marred by fundamental errors, including the use of a physically unsound dark-energy operator, multiple dimensionally incorrect equations, and an empirical framework that rests entirely on unverifiable results from unpublished companion works.

For the paper to be reconsidered for publication in Physical Review D, the author must address the ESSENTIAL points. This will likely require a significant re-scoping of the paper away from the dark energy claims and toward the robust, self-contained theoretical results. If the author can provide a rigorous foundation for the dark energy operator, correct the numerous theoretical errors, and make the paper self-contained, it could become a significant work. Otherwise, it should be revised to a more modest scope.