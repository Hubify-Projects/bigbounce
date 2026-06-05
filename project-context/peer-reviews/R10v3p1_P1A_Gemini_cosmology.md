# P1A R10v3p1 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (5508 chars)
**Wall time**: 156.6s

---

## Referee Report: PRD Submission [Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes...]

This paper investigates four potential channels through which minimal Einstein-Cartan-Holst (ECH) theory could source late-time dark energy or other cosmological signatures. The authors present a "channel-level closure" of these routes, arguing that they fail at the amplitude level under a set of stated assumptions. The main contributions are a "perturbation-transparency theorem" for canonical scalar matter, and the identification of a structural tension between the inflationary e-folds needed for a dark energy mechanism and the survival of a matter-bounce bispectrum signature.

The paper contains several valuable and well-argued points, particularly the perturbation-transparency theorem and the structural tension analysis. However, it suffers from several essential flaws in its foundational arguments, reliance on unpublished work, and structure that preclude its publication in Physical Review D in its current form. A significant revision is required.

### ESSENTIAL Revisions

**P1A-E1: Foundational Flaw in Dimensional Analysis and the Dark-Energy Ansatz**
*   **Location:** Section II C, p. 6; Appendix B, p. 19.
*   **Problem:** The entire dark-energy mapping of the paper rests on a "phenomenological on-shell scaling ansatz" that connects a parity-odd operator to the dark energy density. This operator, given in Eq. (6), is claimed in Appendix B (Eq. B1) to have an off-shell mass dimension of +1, based on the assertion that the field strength `F` has a mass dimension `[F]=+1`. This is highly non-standard. The Riemann curvature 2-form `R` has `[R]=+2`, as does a standard gauge field strength `F=dA` (with `[A]=+1`). The authors provide no justification for `[F]=+1`. Consequently, the dimensional analysis for the action appears incorrect, and the operator is not a valid dimension-4 term for a Lagrangian density. The "fix" of adding powers of `M_Pl` to the coupling constant (Appendix B) is an ad-hoc procedure that does not solve the fundamental problem with the operator itself.
*   **Required Fix:** The authors must provide a rigorous derivation and justification for the dimensionality of the operator in Eq. (6). If no such justification exists, the operator must be treated as a toy model. In this case, all claims of a fundamental "closure" of dark-energy routes from ECH must be significantly walked back. The paper's claims must be re-scoped to reflect that it is ruling out a specific, non-standard, and dimensionally-problematic toy model, not the fundamental theory itself.

**P1A-E2: Reliance on Unpublished, Non-citable Results**
*   **Location:** Section II A, p. 5; throughout the paper.
*   **Problem:** The paper explicitly states that key cosmological parameter values (`H_0`, `ΔN_eff`, etc.) are "drawn from the companion internal MCMC analysis (Paper I(b) [6], in preparation); they are documented internally rather than as externally citable arXiv-posted numbers". This is unacceptable for a peer-reviewed publication. All numerical results used to support the paper's arguments must be reproducible, either from publicly available data and methods described in the paper itself or from citable, peer-reviewed publications.
*   **Required Fix:** The authors must replace all results from "in preparation" works with either: (a) results from published literature (e.g., Planck 2018, DESI 2024), clearly stating the source, or (b) results from their own analysis, with the full details of the MCMC analysis (datasets, priors, convergence statistics) included in the present manuscript, perhaps in an appendix.

**P1A-E3: Reporting on In-Progress Computations**
*   **Location:** Table III, footnote `†`, p. 16.
*   **Problem:** The footnote to Table III discusses the status of an MCMC chain that is currently running: "At the time of this writing the chain has accumulated ~3.8×10⁴ accepted samples... descending monotonically toward the standard publication-quality convergence target". A research paper must report on completed, final results. Reporting on work-in-progress is not appropriate for a formal publication.
*   **Required Fix:** This footnote and any related discussion of in-progress work must be removed. The paper should only report final, converged results. If the results are not yet ready, they should not be mentioned.

### MAJOR Revisions

**P1A-M1: Contradictory Arguments for Dark Energy Signal Suppression**
*   **Location:** Section VII, p. 7 ("Reheating thermal-reset barrier") and Section XII A, p. 15.
*   **Problem:** The paper presents two distinct, and seemingly contradictory, arguments for why a bounce-era torsion signal cannot source late-time dark energy. The first is a dilution calculation based on an `exp[-3N_tot]` factor (Eq. 11), which presumes a signal survives the post-bounce era and is merely redshifted. The second is a "reheating thermal-reset barrier," which argues that because torsion is algebraically sourced by the fermion axial current, any coherent bounce-era signal is completely erased by thermalization during reheating. The second argument is physically more robust and, if correct, makes the first argument (and its associated hand-wavy `(T_reh/M_GUT)^(3/2)` prefactor) obsolete and irrelevant. The authors acknowledge this in Sec. XII, calling the dilution factor "mathematical scaffolding," but the contradictory framing remains throughout the paper.
*   **Required Fix:** The authors should restructure their argument. They should lead with the stronger thermal-reset argument as the primary physical reason for closure. The `exp[-3N_tot]` calculation should be either removed or presented clearly as a less rigorous, order-of-magnitude cross-check that is superseded by the thermalization argument.

**P1A-M2: Paper Length, Structure, and Repetition**
*   **Location:** Throughout the manuscript.
*   **Problem:** The paper is quite long (21 pages) for its core contributions. This is partly due to significant repetition of key arguments. For example, the "Structural Tension" between `N_tot ≈ 92` and the survival of the `f_NL = -35/8` signal is explained in detail in the Abstract, the Introduction (Sec. I), and again in Limitations (Sec. XIV D). The catalog of 14 "Barriers" in Section IX, while comprehensive, disrupts the main narrative flow from theory to observables and back to closure.
*   **Required Fix:** The manuscript should be significantly condensed. The "Structural Tension" argument should be presented once in full, and subsequent mentions should refer back to that section. The authors should consider moving the entire "Barriers" catalog (Section IX and Table II) to an appendix. This would allow the main text to focus on the core narrative: the four routes, the perturbation-transparency theorem, and the surviving observational tests.

### MINOR Revisions

**P1A-m1: Future Date of Submission**
*   **Location:** Page 1.
*   **Problem:** The paper is dated "June 2, 2026 PDT".
*   **Required Fix:** The date should be corrected to the date of submission.

**P1A-m2: Acknowledgment of AI Research Assistant**
*   **Location:** Acknowledgments, p. 18.
*   **Problem:** The paper acknowledges the use of "Claude (Anthropic) as an AI research assistant". Journal policies on such acknowledgments are still evolving.
*   **Required Fix:** The authors should verify that this form of acknowledgment is compliant with PRD's current editorial policies. This is noted for the editor's attention.

**P1A-m3: Unclear Operator Form in Equation (6)**
*   **Location:** Page 6, Eq. (6).
*   **Problem:** The operator `ε^{μνρσ} F_{μν}^{I} F_{Iρσ}` is non-standard. The indices and the nature of `F` are unclear. If `F` is intended to be the Riemann curvature 2-form `R`, the notation is incorrect.
*   **Required Fix:** The authors must clarify the precise form and definition of this operator. If it is a typo for the Pontryagin density, the equation should be corrected to the standard form involving `R_{μν}^{IJ}`.

### NIT-PICKING

**P1A-N1: Status of Gravitational Wave Constraint (Barrier 12)**
*   **Location:** Section IX L, p. 13.
*   **Problem:** Barrier 12, the "Vacuum Amplification Ceiling," is presented as a constraint. However, the authors correctly note that a quantitative comparison to PTA data requires propagating the signal, which is deferred to a future paper.
*   **Required Fix:** The text should be slightly rephrased to make it clearer that this is a loose, order-of-magnitude bound on the energy density at the source, not a direct constraint from current observational data.

## Summary recommendation

**MAJOR REVISIONS**

This paper presents a mix of strong, valuable results and arguments built on critically flawed foundations. The perturbation-transparency theorem is elegant and provides a clear guide for future phenomenological tests of ECH. The structural tension between dark energy and the matter-bounce `f_NL` signature is a novel and compelling consistency check. However, the central claim of closing dark-energy routes is predicated on a dimensionally-problematic ansatz and is therefore not proven. Furthermore, the reliance on non-citable, "in-preparation" results is a violation of standard scientific practice.

The paper has the potential to be a valuable contribution to the literature if the authors undertake a major revision. They must either provide a rigorous derivation for their dark-energy operator or re-scope the paper to focus on its robust results, treating the dark-energy part as a speculative analysis of a toy model. All numerical inputs must be made citable and reproducible. If these essential issues are addressed, and the paper's structure is streamlined, it could become a solid and impactful publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from the second, more rigorous review pass.

================================================================
### ADDITIONAL FINDINGS (Second Pass)

**P1A-E4: Essential Flaw in Birefringence Calculation**
*   **Location:** Page 10, Eq. (17).
*   **Problem:** The equation for the rotation angle `β` is dimensionally inconsistent. The left side (`β`) is dimensionless, while the right side has units of `mass²`. The equation appears to be a non-standard or incorrect transcription of the standard result for birefringence from a pseudoscalar coupling (e.g., from the cited Ref. [28]).
*   **Required Fix:** The authors must derive or cite the correct, dimensionally consistent equation for the rotation angle `β` within their framework. All subsequent numerical estimates based on this equation must be re-evaluated. This error, combined with the dimensional issues in the core dark-energy ansatz (P1A-E1), casts serious doubt on the quantitative reliability of the paper's phenomenological calculations.

**P1A-E5: Use of Stale/Superseded Data**
*   **Location:** Table I, p. 4 vs. Section XI.G, p. 15.
*   **Problem:** Table I, the "Executive summary," quotes a PTA data value of `γ = 3.20 ± 0.42`. However, the main body text in Section XI.G explicitly states: "This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20±0.42 used in pre-real-KDE drafts; the migration is documented in Paper III § 6." The new, correct value is given as `γ = 2.567 ± 0.382`. The summary table, which is a primary entry point for readers, contains a value that the authors themselves identify as obsolete.
*   **Required Fix:** All instances of the stale data value must be updated to the current one. The significance calculation in Table I must be re-done with the correct numbers.

**P1A-M3: Inconsistent and Misleading Figure**
*   **Location:** Figure 2, p. 5.
*   **Problem:** This figure, which illustrates the core energy-scale argument, is internally inconsistent. The y-axis shows a hierarchy starting from a "Parity-odd vacuum energy" `ρ_vac = M_Pl⁴`, which is the standard (and unsolved) cosmological constant problem. This is then shown to be diluted by inflation. However, the caption and the main text (Sec. II A 2) describe a completely different mechanism based on the paper's specific ansatz, `ρ_bounce ~ (α/M) M_Pl³`. The figure depicts the problem the paper claims to address, not the solution it actually proposes. This is highly misleading.
*   **Required Fix:** The figure must be redrawn to be consistent with the model actually being tested in the paper. It should clearly illustrate the energy scales derived from the paper's ansatz, not the generic cosmological constant problem. The caption and figure must be mutually consistent.

**P1A-m4: Typo in Critical Density Equation**
*   **Location:** Page 6, Eq. (9).
*   **Problem:** The expression for the LQC critical bounce density, `ρ_crit`, is inconsistent with the cited source (Ashtekar & Singh [11]). The formula in the paper is missing a factor of `√3`. A simple numerical check confirms that the paper's formula yields `~0.71 ρ_Pl`, while the formula from the literature yields `~0.41 ρ_Pl`, which is the value the authors quote in the text.
*   **Required Fix:** Correct the formula in Equation (9) to match the cited literature and the numerical values used.

**P1A-m5: Unclear Claim in Summary Figure**
*   **Location:** Figure 1, p. 4.
*   **Problem:** The flowchart in Figure 1 claims that the Ekpyrotic scenario is "structurally closed (this paper)". However, the main body of the paper does not contain a dedicated analysis or argument for closing the Ekpyrotic scenario. The focus is on the four minimal-ECH routes.
*   **Required Fix:** The claim regarding the Ekpyrotic scenario should be removed from the figure unless a clear argument for its closure is added to the main text.

**P1A-m6: Incorrect Internal Cross-Reference**
*   **Location:** Abstract, p. 1.
*   **Problem:** The abstract states that missing operators are acknowledged "explicitly in Sec. IV and Sec. XI". While Section IV does contain this acknowledgment, Section XI does not.
*   **Required Fix:** Remove the incorrect reference to Section XI.

**P1A-m7: Overstated Claim in Abstract**
*   **Location:** Abstract, p. 1.
*   **Problem:** The abstract claims that all four channels "fail at the amplitude level". However, the body of the paper (Sec. IV.D) makes clear that the closure of Route 4 (spectator ALP) is a "naturalness objection rather than an amplitude no-go".
*   **Required Fix:** The abstract should be rephrased to accurately reflect the different nature of the closure arguments for the four routes.

**P1A-m8: Confusing Paper Structure (Appendix)**
*   **Location:** Page 19-20.
*   **Problem:** The paper's table of contents and main text refer to an "Appendix A: Complete Parameter Summary". However, there is no labeled Appendix A. Instead, Table IV, which contains this summary, appears unlabeled after the reference list.
*   **Required Fix:** The parameter summary table should be clearly labeled as Appendix A and placed either before or after the references, according to the journal's style guide.

**P1A-m9: Future-Dated Reference**
*   **Location:** References [5], p. 19.
*   **Problem:** The reference for the ACT DR6 result is dated "(2025)", which is in the future. The corresponding arXiv preprint appeared in 2024.
*   **Required Fix:** Correct the year in the reference.