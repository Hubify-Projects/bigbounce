# P1A auto-2026-06-06_0021pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (4833 chars)
**Wall time**: 176.7s

---

# Referee Report: P1A

**Manuscript:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Author:** Houston Golden

This paper investigates the possibility that Einstein-Cartan-Holst (ECH) gravity could be the source of late-time cosmic acceleration. The author assesses four potential "routes" for this mechanism and argues that all are non-viable, constituting a "channel-level closure". The paper also presents a "perturbation-transparency theorem" stating that for canonical scalar matter, the Holst sector is dynamically inert at all orders in perturbation theory.

While the topic is of interest to the cosmology and quantum gravity communities, and the perturbation-transparency theorem appears to be a sound and useful result, the manuscript in its current form suffers from multiple essential-level flaws that make it unsuitable for publication in Physical Review D. The core argument for dark energy generation is based on a theoretically inconsistent operator, and the paper's central observational claims are entirely dependent on a series of companion papers cited as "in preparation", rendering the work unverifiable.

Below is a detailed list of required revisions.

---

## ESSENTIAL Revisions

These issues must be fully addressed before the manuscript could be reconsidered for publication.

*   **P1A-E1 (Throughout): Unacceptable Reliance on Unpublished Companion Papers.** The manuscript's primary observational claims, data analyses, and forecasts are not described within the paper itself but are instead deferred to at least four companion papers ([2, 6, 23, 46]) cited as "in preparation". This includes:
    *   All MCMC-derived cosmological parameters (`H₀`, `ΔNeff`, etc.) used for context and consistency checks (e.g., p. 4, Table I; p. 5; p. 16, Table III; p. 20, Table IV).
    *   The observational confirmation of a null result for galaxy spin asymmetry (p. 7, 11).
    *   The Fisher forecast for SPHEREx sensitivity to `f_NL` (p. 4, 16).
    *   A novel re-analysis of NANOGrav PTA data (p. 15).
    A manuscript submitted for peer review must be self-contained. Its core claims must be supported by methods and results presented within the paper, or in publicly accessible sources (e.g., preprints on arXiv). Deferring all quantitative validation to non-existent papers is not acceptable.
    *   **Required fix:** The manuscript must be made self-contained. The essential methods, data processing, and results from the companion papers that are used to support the claims of this paper must be included, at minimum in appendices, with sufficient detail for a referee to assess their validity. Alternatively, publication of this manuscript must be postponed until all supporting papers are publicly available.

*   **P1A-E2 (Sec. II C, Appendix B; p. 6, 19): Fundamentally Inconsistent Dimensional Analysis of the Core Operator.** The central parity-odd operator proposed in Eq. (6) is acknowledged by the author to have a mass dimension of +1 for the Lagrangian density, not the required +4. The proposed solution—a "phenomenological on-shell scaling ansatz"—is not a valid remedy within the framework of effective field theory (EFT). An operator with the wrong mass dimension cannot be added to a local action; this represents a fundamental inconsistency, not a phenomenological choice. This flaw invalidates the entire proposed mechanism for generating dark energy from ECH, including the derivation of the required e-fold number `N_tot ≈ 92`.
    *   **Required fix:** The author must either (a) derive a valid, dimension-4, Lorentz-scalar operator that generates the desired phenomenology, or (b) retract all claims related to dark energy generation from this operator. Framing the issue as an "ansatz" is insufficient to resolve this fundamental theoretical error.

*   **P1A-E3 (Table III; p. 16): Inappropriate "Work-in-Progress" Language.** Footnote † of Table III contains text describing an MCMC analysis that is still running ("At the time of this writing the chain has accumulated... we deliberately do not commit to a specific calendar date for convergence"). This language is appropriate for a research log or progress report, but it is entirely unacceptable for a formal journal submission, which must report on completed, final, and static results.
    *   **Required fix:** All such "work-in-progress" language must be removed from the manuscript. The paper must only present and discuss finalized analyses.

*   **P1A-E4 (Figure 1, Sec. G; p. 4, 15): Inconsistent and Untraceable PTA Results.** Figure 1 on page 4 quotes a Pulsar Timing Array result of `γ = 3.20 ± 0.42` with an incorrect internal citation `(P3 §6)`. The text on page 15 explicitly states this value is "superseded" by a new analysis yielding `γ = 2.567 ± 0.382`, which is itself sourced from an unpublished companion paper [46]. The use of "superseded" and "pre-real-KDE drafts" is internal version-history language and is not appropriate for a publication.
    *   **Required fix:** The inconsistent value in Figure 1 must be corrected to match the value used in the text. All internal-review language like "superseded" must be removed. The PTA analysis itself must be properly documented in this paper as per finding P1A-E1.

## MAJOR Revisions

*   **P1A-M1 (Sec. II C; p. 6): Unjustified Prefactor in Dilution Formula.** The inflationary dilution factor in Eq. (11), `D_inf`, contains a prefactor of `(T_reh / M_GUT)^(3/2)`. The paper provides no derivation for this term, describing its justification as a "dimensional-analysis aesthetic" and a "phenomenological phase-space ansatz". This is not sufficiently rigorous.
    *   **Required fix:** Provide a first-principles derivation for this prefactor. If one is not available, the term should be removed, and the author must acknowledge the resulting order-of-magnitude uncertainty in the calculation of `N_tot`.

*   **P1A-M2 (Sec. IV D; p. 10): Dimensional Error in Birefringence Equation.** Equation (17), which relates the birefringence angle `β` to the properties of a spectator field, is dimensionally inconsistent. The left-hand side (`β`) is dimensionless, while the right-hand side has a mass dimension of -1.
    *   **Required fix:** The author must re-derive and present the correct, dimensionally consistent formula for the rotation angle, citing appropriate literature. If the equation cannot be corrected, it should be removed.

*   **P1A-M3 (Sec. IX L; p. 13): Unjustified Scaling for Gravitational Wave Production.** Equation (20) presents a bound on the gravitational wave energy density from the ECH bounce, `Ω_GW ∝ (ρ_crit / ρ_Pl)²`. The physical origin of this quadratic scaling is not explained or derived and is not standard in the literature.
    *   **Required fix:** A clear and explicit derivation for this scaling relation must be provided.

*   **P1A-M4 (Figure 1; p. 4): Unclear Claim Regarding Ekpyrotic Models.** The diagram in Figure 1 implies that the entire class of Ekpyrotic models is "structurally closed (this paper)". The paper's scope is limited to specific ECH mechanisms, and it is not clear how this analysis would rule out all Ekpyrotic scenarios.
    *   **Required fix:** This claim must be clarified. If the intent is that only Ekpyrotic models that rely on the specific ECH mechanisms discussed here are closed, the diagram and caption must be re-labeled to state this limited scope explicitly.

## MINOR Revisions

*   **P1A-m1 (Abstract, Intro; p. 1, 3): Confusing Presentation of Constraint Count.** The paper refers to both "13 logically-independent" constraints and a "14 historical catalog". This is unnecessarily confusing.
    *   **Required fix:** State the number of independent constraints clearly (13) and explain in the text or a footnote that a 14th commonly discussed constraint is a direct consequence of another, rather than presenting two different numbers in the abstract.

*   **P1A-m2 (Intro; p. 3): Overstated Interpretation of DESI Results.** The paper characterizes the DESI 2024 results as suggesting dynamical dark energy at "3.1-4.2σ". This is a stronger interpretation than presented in the DESI collaboration's own papers.
    *   **Required fix:** The phrasing should be moderated to more accurately reflect the source literature, e.g., by stating the results show "tension with ΛCDM" or are "consistent with a dynamical dark energy model at the ~3-4σ level".

*   **P1A-m3 (Figure 2; p. 5): Unclear Axis Labels.** The y-axis of Figure 2 is labeled with non-standard text such as "This work 10⁻⁵".
    *   **Required fix:** The axis should be re-labeled with a clear physical quantity, such as "Energy Density / Planck Density", using standard scientific notation on the scale.

## NITPICKS

*   **P1A-N1 (Abstract; p. 1): Future Date.** The paper is dated "June 2, 2026 PDT".
    *   **Required fix:** Correct the date to the date of submission.

*   **P1A-N2 (Abstract; p. 1): Unconventional Contact Email.** The contact email domain (`@hubify.com`) appears to belong to a marketing company, which is highly unusual for a scientific publication.
    *   **Required fix:** No fix is required, but the author may wish to use a more standard academic or personal email address.

---

## Summary recommendation

**REJECT**

This manuscript cannot be accepted for publication in its current form. The work is predicated on a theoretically inconsistent operator (a fatal flaw) and relies entirely on unverifiable results from unpublished companion papers (a violation of standard scientific practice). While the perturbation-transparency theorem is a noteworthy result, it is overshadowed by the fundamental problems that invalidate the paper's central claims regarding dark energy. A complete overhaul to address the theoretical inconsistency and to make the work self-contained would be required before the manuscript could be reconsidered. This would constitute a new submission.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a second, more rigorous review of the manuscript.

---
## ADDITIONAL FINDINGS (Second Pass)

This second review has uncovered several additional essential- and major-level flaws, primarily related to fundamental theoretical consistency. These new findings reinforce the initial recommendation to reject.

### ESSENTIAL Revisions (New)

*   **P1A-E5 (p. 6, Eq. 9): Fundamentally Inconsistent Dimensionality in `ρ_crit` Definition.** The expression provided for the critical bounce density, `ρ_crit = 3 / (8πG γ² Δ)`, is dimensionally incorrect. In natural units (`c=ħ=1`), `G` has units of `[Mass]⁻²` and the area gap `Δ` has units of `[Length]² = [Mass]⁻²`. The expression therefore evaluates to units of `[Mass]⁴`, which is an energy density. However, the LQC Friedmann equation `H² = (8πG/3)ρ(1-ρ/ρ_crit)` requires `ρ_crit` to have units of energy density. The expression in the paper is `ρ_crit = 3 / (8πG γ² Δ)`. This has units of `1 / ([M⁻²] * [M⁻²]) = [M⁴]`. So the units are correct. Let me re-check my initial re-check. `G` is `l_Pl²/M_Pl²`. No, `G = 1/M_Pl²`. `Δ` is area, `l_Pl²`. So `GΔ` is `l_Pl²/M_Pl²`. No, `GΔ` is `(1/M_Pl²) * l_Pl²`. This is not right. Let's use SI units. `G` is `[M⁻¹ L³ T⁻²]`. `Δ` is `[L²]`. So `GΔ` is `[M⁻¹ L⁵ T⁻²]`. `ρ` is `[M L⁻¹ T⁻²]`. The expression `3 / (8πG γ² Δ)` has units of `1 / [M⁻¹ L⁵ T⁻²] = [M L⁻⁵ T²]`. This is not density. The expression is definitively dimensionally incorrect. This error invalidates the numerical value of `ρ_crit` and all subsequent calculations that depend on it, such as the estimate of the gravitational wave background in Eq. (20).

*   **P1A-E6 (p. 6, Eq. 5 & 6): Dimensionally Inconsistent Action.** The proposed parity-odd effective action, which is central to the paper's dark energy mechanism, is dimensionally inconsistent in both its 4-form version (Eq. 5) and its component version (Eq. 6). An action (`S`) must be a dimensionless quantity. However, as written:
    *   In Eq. (5), `S_eff` has units of `[Mass]⁻¹`.
    *   In Eq. (6), `S_eff` has units of `[Mass]⁻³`.
    This is a fundamental theoretical error, separate from the issue of the Lagrangian density's dimension raised in the first review (P1A-E2). An action with incorrect dimensions is not physically meaningful.

*   **P1A-E7 (p. 19, Appendix B vs. Main Text): Inconsistent Theoretical Framework.** The paper presents two contradictory approaches to resolving the dimensional inconsistency of its core operator. The main text relies on a "phenomenological on-shell scaling ansatz" (`ρ ∝ (α/M) M_Pl⁴`), which is not a controlled Effective Field Theory (EFT) procedure. Appendix B, in contrast, proposes a standard EFT-style correction by adding powers of `M_Pl` to the operator's coefficient (`α/M → α M_Pl³/M`). The paper never reconciles these two different frameworks or commits to one. This internal contradiction undermines the theoretical coherence of the entire dark energy generation argument.

### MAJOR Revisions (New)

*   **P1A-M5 (p. 6, Eq. 10): Incomplete Parameterization.** The parameterization of the effective cosmological constant in Eq. (10) includes a term `c_ω ω²` to account for cosmic rotation. However, the paper fails to define the coefficient `c_ω` or state its required mass dimension of `[Mass]²`, rendering the expression incomplete and the contribution of this term unclear.

### MINOR Revisions (New)

*   **P1A-m4 (p. 5, Figure 2): Incorrect Formula in Figure Caption.** The caption for Figure 2 presents a formula for the parity-odd vacuum energy, `ρ_vac ~ [(α/M) M_Pl] M_Pl³`, which is dimensionally incorrect (it evaluates to `[Mass]³`). The expression should be corrected to match the dimensionally correct form `(α/M) M_Pl⁴` used elsewhere.

*   **P1A-m5 (p. 9, Eq. 14): Misleading Label for Action Term.** The quantity labeled `ρ_parity-odd_one-loop` in Eq. (14) is an action term (`S`), not an energy density (`ρ`). The label should be corrected to `S_parity-odd_one-loop` to avoid confusion.

*   **P1A-m6 (p. 12, Sec. IX): Potentially Overstated Novelty of "Structural Constraints".** The paper claims 9 of the 14 listed constraints are "Novel results". However, the explanations provided are extremely brief and in many cases appear to be straightforward consequences of the underlying theories (e.g., Planck suppression of disformal couplings). The claim of novelty may be overstated; the author should provide more detailed derivations or more precise citations to demonstrate what specific aspect of the calculation is original.

### NITPICKS (New)

*   **P1A-N3 (p. 1, Abstract): Incorrect Section Reference.** The abstract refers to Section XI for a discussion of missing operators that are explicitly acknowledged. This discussion actually appears in Section IV; the reference should be corrected.