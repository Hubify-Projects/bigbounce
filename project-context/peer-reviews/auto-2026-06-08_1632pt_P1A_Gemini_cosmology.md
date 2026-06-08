# P1A auto-2026-06-08_1632pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (4864 chars)
**Wall time**: 148.4s

---

Here is a complete referee report for the submitted manuscript.

***

**Referee Report for Manuscript P1A**

**Title:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Author:** Houston Golden

## General Comments

This manuscript investigates the possibility of sourcing late-time dark energy from minimal Einstein-Cartan-Holst (ECH) gravity, in the context of a quantum bounce cosmology. The author(s) assess four potential "routes" for this mechanism and conclude that all fail at the amplitude level under a set of stated assumptions. The central theoretical result is a "perturbation-transparency theorem," which states that for canonical scalar matter, the Holst sector of ECH gravity decouples from scalar and tensor perturbations, leaving them identical to those in standard General Relativity.

The paper contains a solid and valuable theoretical result in the perturbation-transparency theorem. The proof is straightforward and the implications are clearly articulated. However, the manuscript in its current form has several fatal flaws that prevent its publication in Physical Review D. The most critical issue is that the paper is not self-contained; its observational claims and constraints rely entirely on a suite of companion papers that are cited as "in preparation." Furthermore, the manuscript is excessively long for its core contribution, with the bulk of the paper dedicated to analyzing a speculative dark-energy mechanism based on a phenomenological ansatz. Finally, the paper contains several internal review comments, typos, and dimensionally inconsistent equations that undermine its quality.

For these reasons, I must recommend rejection. A significantly revised and refocused manuscript, centered on the publishable theoretical result, could be reconsidered in the future.

## Detailed Findings

### ESSENTIAL Revisions

**P1A-E1: Reliance on Unpublished Companion Papers**
*   **Location:** Throughout the paper, especially Abstract, Sec. I, Table I, Sec. III, Sec. V, Sec. XI, Sec. XIII, Table III, Table IV, and References [2, 6, 23, 46].
*   **Problem:** The manuscript's key observational claims and quantitative results are not derived within the paper itself but are imported from at least four companion papers cited as "in preparation." This includes:
    *   All cosmological parameter values from MCMC analysis (`H_0`, `Ω_m`, `σ_8`, `ΔN_eff`) (Ref [6]).
    *   The `f_NL = -35/8` Fisher forecast for SPHEREx (Ref [2]).
    *   The confirmed null result for galaxy spin asymmetry (Ref [23]).
    *   The PTA spectral index analysis vs. NANOGrav data (Ref [46]).
    A paper submitted to PRD must be self-contained and its results verifiable. Basing the core arguments of a paper on unpublished work is unacceptable.
*   **Fix:** The paper must be made self-contained. Either (a) the analyses from the companion papers must be incorporated into this manuscript (likely in appendices), or (b) all claims and numerical values derived from these unpublished sources must be removed. The latter would require a fundamental restructuring of the paper. The manuscript cannot be published until its companion papers are publicly available on a preprint server or a journal.

**P1A-E2: Presence of Internal Review Artifacts**
*   **Location:** Page 1 (footnote a), Page 2 (footnote), Page 15 (footnote 2).
*   **Problem:** The manuscript contains several notes that appear to be remnants of an internal review process.
    *   Page 2 footnote: "Earlier versions of this manuscript erroneously identified the two; the correction preserves the headline conclusion..."
    *   Page 15 footnote 2: "An earlier version of this manuscript misidentified the Holst dual contraction with the Pontryagin density. The correction..."
    These comments are unprofessional, undermine confidence in the final state of the manuscript, and must be removed.
*   **Fix:** Remove all such internal-facing comments and version-history notes from the manuscript.

**P1A-E3: Speculative Nature of the Core Dark-Energy Mechanism**
*   **Location:** Abstract, Sec. I, Sec. II C, Sec. VI, Appendix B.
*   **Problem:** The entire dark-energy analysis rests on a "phenomenological on-shell scaling ansatz" that maps a mass-dimension +1 operator to a mass-dimension +4 energy density. The paper is commendably transparent about this being an ansatz and not a derivation (see Appendix B). However, this means that the bulk of the paper (the "four-route no-go" and the "14 barriers") is an analysis of a speculative, non-derived model. While such phenomenological explorations can be valuable, the 21-page length is not justified for what amounts to closing channels for a model that was not derived from first principles in the first place.
*   **Fix:** The paper should be significantly restructured and shortened to focus on its main, solid contribution: the perturbation-transparency theorem (Sec. X). The phenomenological dark-energy analysis should be heavily condensed and presented as a brief, speculative application of the broader ECH framework, rather than as the central result of the paper.

### MAJOR Revisions

**P1A-M1: Unusual Citation Practice (Future-Dated References)**
*   **Location:** Bibliography (e.g., Refs [5, 10, 35, 41-45]).
*   **Problem:** The paper, dated June 2026, cites numerous preprints with future dates (e.g., `arXiv:2503.14738`, `arXiv:2509.13654`). This is not standard scientific practice. All citations must refer to works that are publicly available at the time of submission.
*   **Fix:** All citations must be updated to point to existing, publicly accessible works. If these works do not yet exist, the citations and any claims based on them must be removed.

**P1A-M2: Dimensionally Inconsistent Equation**
*   **Location:** Page 10, Sec. IV D, Equation (17).
*   **Problem:** Equation (17), `β = Δθ_rec->today ~ (α/M)^2 ρ_θ / m_θ^2`, is dimensionally inconsistent. The left side (`β`) is dimensionless, while the right side has a mass dimension of `[-1]^2 * [+4] / [+1]^2 = +4`.
*   **Fix:** The equation must be corrected. The standard relation is `β = (α/M) Δθ`. The subsequent physical argument, which relies on relating `ρ_θ` and `m_θ`, should be re-evaluated based on the correct formula.

**P1A-M3: Overstated Claim in Figure Caption**
*   **Location:** Page 4, Figure 1.
*   **Problem:** The diagram claims that the "Ekpyrotic" bounce mechanism is "structurally closed (this paper)". However, the paper's analysis focuses exclusively on ECH cosmology. There is no derivation or argument presented in the text to support the closure of the ekpyrotic route.
*   **Fix:** Remove the "structurally closed (this paper)" label from the "Ekpyrotic" box in Figure 1, as this claim is not substantiated in the manuscript.

### MINOR Revisions

**P1A-N1: Incorrect Cross-Reference**
*   **Location:** Page 5, right column.
*   **Problem:** The text states: "...the ~0.020 figure that appears in the parameter-budget table (Appendix B) is the spread between counting prescriptions...". The parameter table is Table IV on page 20, and the parameter summary is Appendix A. Appendix B is about the dimensional status of an operator.
*   **Fix:** Correct the cross-reference to point to the correct table or appendix (likely Table IV or Appendix A).

**P1A-N2: Inconsistent Sigma Value**
*   **Location:** Page 20, Table IV, row for `γ_PTA`.
*   **Problem:** The table notes that for the PTA spectral index, "Bounce γ = 3.0 at +1.2σ". However, the calculation on page 15 gives `+1.13σ`. A re-computation `(3.0 - 2.567) / 0.382 ≈ 1.13` confirms the value on page 15 is correct.
*   **Fix:** Correct the sigma value in Table IV to `+1.13σ`. (Note: this entire result is contingent on the publication of Ref [46] as per P1A-E1).

**P1A-N3: Unclear Figure Axis**
*   **Location:** Page 5, Figure 2.
*   **Problem:** The x-axis of Figure 2 is labeled with "This work 10^5" and "ΛCDM 10^120". This is not a physical axis. It appears to be labeling the magnitude of the fine-tuning problem that each scenario addresses.
*   **Fix:** Clarify the x-axis label. For example, "Hierarchy Problem Magnitude" or "Fine-Tuning Factor".

**P1A-N4: Internal Reference Format**
*   **Location:** Page 4, Figure 1 caption.
*   **Problem:** The caption refers to "PTA γ = 3.0 v.s. data 3.20 ± 0.42 (P3 §6)". The "(P3 §6)" format appears to be an internal reference to a different document (perhaps one of the companion papers).
*   **Fix:** Remove this internal reference or replace it with a proper citation.

### NITs (Cosmetic)

**P1A-T1: Typo in Date**
*   **Location:** Page 1, Date line.
*   **Problem:** The date is given as "June 8, 22026 PDT".
*   **Fix:** Correct the year to 2026.

***

## Summary recommendation

**REJECT**

I recommend that this manuscript be rejected. The paper's primary flaw is its complete dependence on multiple "in preparation" companion papers for all of its quantitative observational results, rendering it unverifiable and not self-contained. This issue alone is sufficient for rejection. Additionally, the manuscript suffers from an excessive length given that its core dark-energy analysis is based on a speculative ansatz, and it contains unprofessional internal review artifacts. While the perturbation-transparency theorem is a sound and interesting result, it is not sufficient to carry a 21-page paper with these fundamental problems. The author should consider resubmitting a much shorter, focused paper on the transparency theorem and its direct implications, ensuring that any phenomenological discussion is self-contained and properly scoped.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the report of additional findings from the second, more rigorous review.

***

### ADDITIONAL FINDINGS (Second Pass)

My initial review identified several fatal flaws, primarily the reliance on unpublished work and the speculative nature of the central claim. This second, more detailed pass confirms the initial assessment and uncovers additional, fundamental issues in the paper's theoretical construction.

**A. ARITHMETIC**
*   No new arithmetic errors were found. The calculations that could be verified from the text were correct. However, many key inputs rely on unpublished companion papers.

**B. FIGURE-CAPTION VS BODY-CLAIM**
*   **P1A-N5: Stale Data in Figure:** Figure 1 quotes the PTA spectral index data as `3.20 ± 0.42 (P3 §6)`. The main text on page 15 explicitly supersedes this, stating: "This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20±0.42 used in pre-real-KDE drafts". The new value is given as `2.567 ± 0.382`. The figure has not been updated to reflect the final analysis presented in the text, which is misleading.

**C. EQUATION DIMENSIONAL CONSISTENCY**
*   **P1A-E4: Fundamentally Flawed Dimensional Analysis:** The theoretical foundation of the proposed dark-energy mechanism is dimensionally inconsistent, which is a fatal flaw.
    *   **The Operator:** The action term in Eq. (5) and Eq. (6) is claimed to have a Lagrangian density `L_odd` with mass dimension `[L_odd] = +1` (acknowledged in Appendix B). A valid Lagrangian density in 4D spacetime must have mass dimension +4. This means the proposed operator is not a valid, local term in an effective field theory action without introducing additional mass scales, which are absent.
    *   **The "Fix":** The paper attempts to resolve this via a "phenomenological on-shell scaling ansatz" in Appendix B, Eq. (B2): `ρ_bounce ~ (α/M) M_Pl³ ~ 10⁻² M_Pl⁴`. This equation is itself dimensionally inconsistent. The term `(α/M) M_Pl³` has mass dimension `[-1][+1]³ = +2`, while `ρ_bounce` and `M_Pl⁴` have mass dimension +4. An ansatz cannot violate dimensional analysis. This invalidates the entire derivation of the dark energy density and the subsequent constraints (like `N_tot ≈ 92`).

**D. INTERNAL CROSS-REFERENCES**
*   **P1A-N6: Incorrect Cross-Reference to Footnote:** On page 19, in the Conclusions (Sec. XV), the text refers to a decomposition of the curvature: "...see Sec. X footnote for the e^e^R = -NY+T^T decomposition)". There is no footnote in Section X. The relevant footnote explaining this is on page 2.
*   **P1A-N7: Incorrect Cross-Reference to Section XI:** The abstract claims that missing operators are acknowledged in "Sec. IV and Sec. XI". While Section IV does mention them, Section XI ("The Hybrid Dark-Energy Loophole") does not.

**I. APPENDIX VS MAIN-TEXT MISMATCH**
*   **P1A-N8: Missing Appendix Content:** Appendix A is titled "Complete Parameter Summary" but is empty. It appears to be a placeholder that was never filled in.

**J. STALE NUMBERS / INCONSISTENCIES**
*   **P1A-M4: Inconsistent `N_tot` Calculation:** The paper's central "structural tension" argument relies on `N_tot ≈ 92` e-folds of inflation. However, the derivation in Appendix B from the standard cosmological constant hierarchy yields `N_tot ≈ 94` e-folds (`122 ln(10)/3`). The paper notes this `~2%` discrepancy but does not resolve it, stating it depends on the choice of ansatz. This ambiguity undermines the precision of the structural tension claim.

***

### Updated Summary Recommendation

**REJECT**

This second, more rigorous review reinforces my initial recommendation to **reject** the manuscript. The new findings, particularly the **fatal flaw in the dimensional analysis (P1A-E4)** of the core dark-energy operator and its associated "fixing" ansatz, render the entire dark-energy portion of the paper theoretically unsound. An ansatz must be physically and mathematically consistent, and this one is not.

This fundamental problem is compounded by the previously identified issues: the complete reliance on unpublished companion work, the presence of internal review artifacts, stale data in figures, and incorrect cross-references. The paper's only potentially salvageable component is the perturbation-transparency theorem (Sec. X), which appears correct and is a useful result. However, it cannot justify the publication of a 21-page manuscript whose primary focus is a theoretically invalid model.

The manuscript is not suitable for publication in PRD in any recognizable form of its current state. A future submission should be radically different: a short, focused paper on the perturbation-transparency theorem and its immediate, rigorously-derived consequences. The speculative dark-energy model would need to be completely reformulated on a sound theoretical basis before it could be considered for publication.