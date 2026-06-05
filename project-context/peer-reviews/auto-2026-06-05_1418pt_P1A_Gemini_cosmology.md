# P1A auto-2026-06-05_1418pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (3764 chars)
**Wall time**: 121.5s

---

Here is a referee report for the submitted paper.

---
## Referee Report: P1A

**Manuscript:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Author:** Houston Golden
**Journal:** Physical Review D

This paper presents a systematic assessment of four potential channels through which minimal Einstein-Cartan-Holst (ECH) gravity could source late-time dark energy. The author concludes that all four channels are closed at the amplitude level under a set of stated assumptions. The central results are a "perturbation-transparency theorem" for canonical scalar matter and a catalog of 14 structural constraints that map out the minimal-ECH parameter space. The paper also identifies a structural tension between the requirements for an ECH-sourced dark energy mechanism and the survival of a matter-bounce signature in the non-Gaussianity parameter `f_NL`.

The work is ambitious and demonstrates a deep command of the relevant physics, from loop quantum cosmology to observational constraints. The perturbation-transparency theorem is elegant and appears correct, and the systematic cataloging of constraints is a valuable exercise. The distinction between a "channel-level closure" and a full "operator-level theorem" is appropriately and carefully made.

However, the manuscript suffers from several critical flaws that preclude its publication in Physical Review D in its current form. The most significant issues are an over-reliance on unpublished companion works and the use of non-standard, speculative citation practices. While the core theoretical arguments are often sharp, they are built upon a foundation that is not verifiable by the reader.

A recommendation of **MAJOR REVISIONS** is made. The paper contains the core of a potentially important contribution, but it must be made self-contained and adhere to established standards of scientific citation.

---
### Detailed Findings

#### ESSENTIAL REVISIONS

**P1A-E1: Unacceptable Reliance on "In Preparation" Companion Works**
*   **Location:** Throughout the paper, e.g., Abstract (p.1), Sec. I (p.3), Sec. III.B (p.8), Sec. V (p.11), Sec. XV (p.18), and References [2, 6, 23, 46].
*   **Problem:** The paper's key observational and computational claims are not substantiated within the manuscript itself but are instead deferred to a suite of companion papers cited as "in preparation". These include:
    *   The `f_NL = -35/8` SPHEREx forecast [2].
    *   The entire MCMC analysis, including `H_0` and `ΔN_eff` values, NaMaster pipeline validation, and ALP parameter fitting [6].
    *   The galaxy spin chirality null result [23].
    *   The multi-survey anomaly catalog and PTA analysis [46].
*   **Required Fix:** A manuscript submitted for peer review must be self-contained. The author must integrate the essential methods and results from these companion papers into the present manuscript, for example in appendices. At a minimum, this must include: (1) a summary of the MCMC setup, datasets, and posteriors for the cosmological parameters used; (2) a description of the galaxy spin classifier and a table/figure showing the null dipole result; (3) a summary of the Fisher forecast methodology for `f_NL`. Without this, the central claims of the paper are unverifiable.

**P1A-E2: Foundational Dark-Energy Mapping is an Uncontrolled Ansatz**
*   **Location:** Abstract (p.1), Sec. II.C (p.6), Appendix B (p.19).
*   **Problem:** The entire premise of connecting ECH to dark energy rests on a "phenomenological on-shell scaling ansatz" for a parity-odd operator that has an off-shell mass dimension of +1, not the required +4 for a Lagrangian density term. The paper is commendably transparent about this, particularly in Appendix B. However, this is such a profound weakness that it undermines the central claim of "closure". The paper is closing channels that were never rigorously opened from a controlled effective field theory perspective.
*   **Required Fix:** The language in the title, abstract, and introduction must be softened to reflect this reality. The term "Channel-Level Closure" is too strong. A title like "Channel-Level Constraints on..." or "A Critical Assessment of..." would be more appropriate. The abstract must state upfront that the analysis assesses phenomenological routes built upon a dimensionally-incomplete operator ansatz, rather than routes derived from a complete EFT.

**P1A-E3: Use of Fictional and Future-Dated Citations**
*   **Location:** Throughout the bibliography, e.g., [5], [10], [41], [42], [43], [44], [45]. The paper is dated "June 2, 2026".
*   **Problem:** The manuscript cites several papers with future dates (e.g., 2025, 2026) and arXiv IDs that are either placeholders or correspond to unrelated work. For example, reference [10] is cited for DESI DR2 results, but the arXiv ID is fictional. This is not an acceptable practice in a scientific paper. All claims must be supported by existing, publicly accessible, and correctly cited literature.
*   **Required Fix:** All fictional, placeholder, and future-dated citations must be removed. The claims supported by these citations must either be removed or rephrased as general future prospects (e.g., "Future data from DESI may provide...") without a specific, non-existent reference. The date of the manuscript should be changed to the date of submission.

#### MAJOR REVISIONS

**P1A-M1: Hand-Waving Justification for Dilution Prefactor**
*   **Location:** Sec. II.C.1 (p.6) and Sec. XII.A (p.15).
*   **Problem:** The crucial `(T_reh / M_GUT)^(3/2)` prefactor in the inflationary dilution formula (Eq. 11) is justified on grounds of "dimensional-analysis aesthetic" and a "phenomenological phase-space ansatz". The author admits this is not a rigorous derivation. This lack of rigor undermines the quantitative claim of `N_tot ≈ 92` and the sharpness of the "structural tension" argument.
*   **Required Fix:** The author should be more explicit in the main text (not just in the discussion) that the `N_tot ≈ 92` value is an order-of-magnitude estimate whose precision is limited by the un-derived prefactor. The structural tension should be framed as a strong qualitative inconsistency rather than a precise numerical conflict.

**P1A-M2: Inconsistent Energy Density in Figure 2**
*   **Location:** Figure 2 (p.5).
*   **Problem:** The figure caption states the figure illustrates the scaling ansatz `ρ_vac ~ [(α/M) M_Pl] M_Pl^3`. However, the label in the figure itself reads `ρ_vac = M_Pl^4`. These are different quantities. The former is the dimensionally-corrected ansatz value at the bounce, while the latter is the natural Planck-scale energy density. This is confusing.
*   **Required Fix:** The label in the figure should be changed to be consistent with the text and caption, for example, by labeling it `ρ_bounce` or `ρ_ECH` and clarifying its relation to the Planck density `ρ_Pl`.

#### MINOR REVISIONS

**P1A-m1: Typo in `f_NL` Forecast Significance**
*   **Location:** Table I, footnote `a` (p.4).
*   **Problem:** The text reads "63-50 realistic after full systematic budget". This appears to be a typo.
*   **Required Fix:** This should likely read "3-5σ realistic". Please correct.

**P1A-m2: Ambiguous Language on LiteBIRD Test**
*   **Location:** Conclusions, Sec. XV, point 2 (p.18).
*   **Problem:** The text states that the LiteBIRD test at `~9σ` "will not by itself separate the spectator-ALP class from generic-ALP fits to the observed signal." This is a subtle but crucial point, but the initial `~9σ` figure (from `0.27°/0.03°`) is misleading if quoted without immediate context.
*   **Required Fix:** The author has correctly performed the more rigorous calculation (`~0.73σ` differential test). It would be clearer to lead with the correct test and its interpretation, and perhaps relegate the naive `9σ` calculation to a parenthetical comment explaining what it represents (a test against `β=0`, not against the current central value) to avoid confusion.

**P1A-m3: Overly Aggressive Claim on DESI Data**
*   **Location:** Introduction, Sec. I (p.3).
*   **Problem:** The paper claims "DESI 2024-2025 BAO results suggest dynamical dark energy at 3.1-4.2σ (dataset-dependent) [9, 10]". While reference [9] (the real DESI 2024 paper) does show a preference for dynamical models (up to 3.9σ for a specific model), the range quoted here seems to be an aggressive interpretation, and reference [10] is fictional.
*   **Required Fix:** The statement should be rephrased to more accurately reflect the findings of the cited paper [9], e.g., "up to 3.9σ preference for specific thawing models". The fictional citation [10] must be removed.

#### NIT-PICKS (Cosmetic)

**P1A-N1: Awkward Phrasing in Abstract**
*   **Location:** Abstract (p.1).
*   **Problem:** The phrase "The dark-energy mapping rests on a phenomenological on-shell scaling ansatz whose off-shell mass dimension is +1 rather than +4" is slightly awkward.
*   **Required Fix:** Suggest rephrasing for clarity, e.g., "The mapping of ECH to dark energy relies on a phenomenological scaling ansatz for an operator with an off-shell mass dimension of +1, rather than the +4 required for a standard Lagrangian term."

**P1A-N2: Inconsistent Sigma Notation**
*   **Location:** Abstract (p.1).
*   **Problem:** The text uses both `3.60` and `~2.90` (with a trailing zero) for sigma values.
*   **Required Fix:** Use a consistent number of significant figures for sigma values, e.g., `3.6σ` and `2.9σ`.

---
## Summary recommendation

**MAJOR REVISIONS**

This manuscript presents a thorough and insightful theoretical investigation into the viability of minimal ECH as a source for dark energy. The perturbation-transparency theorem is a highlight, and the systematic approach to cataloging constraints is valuable. However, the paper in its current form is not suitable for publication. The heavy and unacceptable reliance on unpublished work makes its central claims unverifiable, and the use of fictional citations falls well below the standards of a professional physics journal. If the author can make the paper self-contained by incorporating the necessary supporting results and adhere to standard citation practices, it has the potential to be a strong and impactful contribution to the literature.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the addendum to the referee report, based on a more rigorous second review.

---
### Addendum to Referee Report: P1A (Second Pass)

Following a more detailed re-examination of the manuscript, several additional critical issues have been identified. These findings reinforce the initial recommendation for **MAJOR REVISIONS** and highlight fundamental problems with the paper's theoretical formalism.

#### NEW ESSENTIAL REVISIONS

**P1A-E4: Critical Dimensional Inconsistencies in Key Equations**
*   **Location:** Sec. II.A.2 (Eq. 6), Sec. II.C (Eq. 10), Sec. IV.D (Eq. 17).
*   **Problem:** Several of the paper's foundational equations are dimensionally inconsistent, indicating fundamental errors in the theoretical setup.
    1.  **Action (Eq. 6 & Appendix B):** The paper correctly notes that the parity-odd operator `L_odd` has mass dimension `[L_odd] = +1`. However, this means the action `S_eff = ∫ d^4x √-g L_odd` has mass dimension `[S_eff] = -4 + 4 + 1 = +1`. An action must be dimensionless in natural units. This is a more severe problem than the operator being non-standard; the entire theoretical starting point is dimensionally ill-defined.
    2.  **Effective Cosmological Constant (Eq. 10):** The equation `Λ_eff = Ξ M_Pl^4 + c ω^2` (with `c=1` implied) is inconsistent. `[Λ_eff]` and `[Ξ M_Pl^4]` have dimension +4 (since `Ξ` is defined as dimensionless in Eq. 24). However, `[ω^2]` has dimension +2. The equation is therefore dimensionally unbalanced.
    3.  **Birefringence Angle (Eq. 17):** The formula for the rotation angle `β` is dimensionally incorrect. The angle `β` must be dimensionless. The right-hand side, `(α/M) √(ρ_θ) / m_θ^2`, has mass dimension `[-1] * [+2] / [+2] = -1`. This invalidates the entire quantitative analysis of Route 4 in Sec. IV.D, which relies on this equation to connect the coupling `α/M` to the observed `β` and `ρ_Λ`. The standard derivation for a pseudoscalar `θ` coupled via `(α/M) θ F F~` yields a rotation angle `β ~ (α/M) Δθ`, which is dimensionless if `θ` is a canonical field. The paper's formula is incorrect.
*   **Required Fix:** These dimensional errors must be corrected. This is not a matter of interpretation; it requires a fundamental re-derivation of the paper's core formulas. If the dimensional inconsistencies cannot be resolved, the corresponding sections and conclusions must be retracted. The analysis of Route 4, in particular, appears to be based on an incorrect physical formula and must be completely reworked.

#### NEW MINOR REVISIONS

**P1A-m4: Incorrect Internal Cross-Reference**
*   **Location:** Abstract (p.1).
*   **Problem:** The abstract states that missing operators are acknowledged "explicitly in Sec. IV and Sec. XI". While Section IV does contain the relevant "Scope" paragraph, Section XI discusses a "Hybrid Dark-Energy Loophole" and does not mention the missing operators.
*   **Required Fix:** The reference to Section XI should be removed from this sentence in the abstract.

---
### Final Summary

The issues identified in this second, more rigorous review are severe. The dimensional inconsistencies in the action, the effective cosmological constant, and the birefringence angle formula are not matters of interpretation but appear to be fundamental errors in the physics. The error in the birefringence formula (Eq. 17) invalidates the quantitative closure argument for one of the four main routes (Route 4).

These new findings, combined with the critical issues from the initial report (reliance on unpublished work, use of an uncontrolled ansatz, and fictional citations), make the manuscript's current form untenable for publication. A thorough and fundamental revision is required to address these points before the paper can be reconsidered.