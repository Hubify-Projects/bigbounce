# P1A 2026-06-04_1814pt — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 57.4s

---

**Referee Report on HUBIFY-2026-001A: "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"**

This paper presents a systematic assessment of four specific channels within minimal Einstein-Cartan-Holst (ECH) theory as potential sources for late-time dark energy. The main conclusion is a "channel-level closure," arguing that none of the enumerated routes are viable under the stated assumptions. The central new theoretical result is a "perturbation-transparency theorem," which demonstrates that for canonical scalar matter, the Holst sector decouples from all scalar and tensor perturbations, rendering the Barbero-Immirzi parameter unobservable in these channels. The paper also discusses surviving, mechanism-independent predictions of the broader bounce cosmology paradigm.

The work is ambitious and attempts to bring a high degree of structure to a complex theoretical space. The perturbation-transparency theorem is a clear and valuable result. The systematic cataloging and critique of the dark-energy routes is a useful exercise. However, the manuscript in its current form has several essential issues that preclude its publication.

---
### **Detailed Findings**

**ESSENTIAL**

*   **P1A-E1: Unverifiable Claims from "In Preparation" Companion Papers.**
    *   **Location:** Throughout the paper, e.g., Abstract (p. 1), Sec. I A (p. 3), Sec. III B (p. 8), Sec. VII (p. 11), Sec. XV (p. 18), and multiple references [2, 6, 23, 46].
    *   **Problem:** The paper's phenomenological claims and observational constraints rely heavily on results from at least four companion papers cited as "(in preparation)". These include:
        *   The SPHEREx Fisher forecast for f_NL [2].
        *   The ΛCDM+ΔN_eff MCMC analysis, NaMaster pipeline validation, and ALP parameter fitting [6].
        *   The galaxy spin chirality analysis and null result [23].
        *   The multi-survey anomaly catalog [46].
    *   As these papers are not publicly available, it is impossible for a referee to verify the correctness of the inputs used in the present manuscript. A peer-reviewed paper must be self-contained or rely on citable, public work.
    *   **Required Fix:** The authors must make these companion papers publicly available (e.g., by posting them to arXiv). Alternatively, they must incorporate the essential methods, derivations, and results from those papers into the present manuscript (e.g., in appendices) so that all claims can be independently verified.

*   **P1A-E2: Internal Versioning and Draft-History Artifacts.**
    *   **Location:** Throughout the paper.
    *   **Problem:** The manuscript is littered with internal metadata and comments that are inappropriate for a formal journal submission. This suggests a lack of careful proofreading. Examples include:
        *   Abstract (p. 1): "(Dated: June 2, 2026 PDT — v1A.0.44)"
        *   Sec. XIV D (p. 17): "R14 GEM-N1 closure: prior shorthand mixed a comoving k on the LHS with k_SPHEREX^phys on the RHS which was notationally sloppy and has been removed"
        *   Sec. XI (p. 15): "...the earlier synthetic-Gaussian-likelihood value γ = 3.20±0.42 used in pre-real-KDE drafts..."
        *   Sec. IV (p. 8): "...replaces the single-paragraph forward reference of earlier versions..."
        *   Sec. IV B (p. 9): "The earlier-draft analysis that compared a rotation rate..."
        *   Appendix B (p. 19): "...misled by an apparent “fix” in earlier drafts."
    *   **Required Fix:** The authors must perform a thorough proofread of the entire manuscript and remove all such internal versioning information, dates, and comments referring to the paper's drafting history.

**MAJOR**

*   **P1A-M1: Weak Justification for Inflationary Suppression Prefactor.**
    *   **Location:** Sec. II C 1 (p. 6) and Sec. XII A (p. 15).
    *   **Problem:** The derivation of the inflationary dilution factor in Eq. (11), specifically the `(T_reh/M_GUT)^(3/2)` prefactor, is justified on grounds of "dimensional-analysis aesthetic" and a "phenomenological phase-space ansatz" rather than a first-principles calculation. The paper is commendably honest about this weakness, but it undermines the quantitative precision of the subsequent `N_tot ≈ 92` constraint. While the parallel "reheating thermal-reset" argument provides a qualitative backstop, the quantitative argument rests on this weakly-justified factor.
    *   **Required Fix:** The authors should explicitly discuss the robustness of their conclusions to O(1) or even order-of-magnitude uncertainties in this prefactor. They should clarify that while the `N_tot ≈ 92` figure is sensitive to this choice, the overall conclusion of a large required e-fold count (and the resulting structural tension with f_NL) holds regardless. The discussion in Sec. XII A should be strengthened to make this point more clearly.

*   **P1A-M2: Overly Complicated Structure and Jargon.**
    *   **Location:** Abstract (p. 1), Sec. IX (p. 12), Table II (p. 13).
    *   **Problem:** The paper organizes its arguments around a complex hierarchy of "foundation studies (A-G)", "observational research branches (H, J, L, M, N, O)", and "barriers (1-14)". This structure is not standard and makes the paper difficult to parse. For example, the abstract's reference to "7 foundation studies... and 6 observational research branches" is jargon that is unhelpful to a reader before they have studied the paper's internal classification scheme.
    *   **Required Fix:** The authors should streamline this presentation. The abstract should state the key physical constraints directly without referring to the internal "Foundation/Branch" naming scheme. In Sec. IX, the introduction should more clearly explain the motivation for this classification. While the catalog is useful, its presentation could be made more accessible.

**MINOR**

*   **P1A-m1: Confusing Phrasing in Abstract.**
    *   **Location:** Abstract (p. 1).
    *   **Problem:** The sentence "we report 13 logically-independent mechanism-class constraints (the prior count of 14 retained Barrier 8... merged here...)" is convoluted and contains unnecessary parenthetical history for an abstract.
    *   **Required Fix:** Simplify this to state the final number of constraints and their purpose. For example: "We establish 13 logically-independent constraints that collectively map the parameter space of these minimal ECH channels." The details of the counting can be left to the main text.

*   **P1A-m2: Scope of the Perturbation-Transparency Theorem.**
    *   **Location:** Sec. X (p. 14).
    *   **Problem:** The theorem is a key result, but its implications could be stated more prominently. It cleanly separates the observables sensitive to the Holst sector (non-perturbative, like birefringence) from those that are not (all scalar/tensor perturbations).
    *   **Required Fix:** Consider adding a short, clear summary statement at the beginning of Sec. X or the end of the introduction that highlights this clean dichotomy as a primary positive takeaway of the analysis.

**NIT**

*   **P1A-N1: Inconsistent Use of `f_NL` vs. `fNL`.**
    *   **Location:** Throughout the paper.
    *   **Problem:** The subscript for the non-Gaussianity parameter is sometimes italicized (`f_NL`) and sometimes not (`fNL`).
    *   **Required Fix:** Use a consistent notation throughout the manuscript, preferably `f_NL`.

---
## Summary recommendation

**MAJOR REVISIONS**

The paper presents a valuable and systematic critique of a class of dark energy models, and its central theoretical result on perturbation transparency is elegant and useful. The overall goal of closing theoretical routes at the "channel level" is well-motivated. However, the manuscript cannot be published in its current state. The reliance on multiple "in preparation" companion papers for key observational results is an essential flaw that makes the work unverifiable. Furthermore, the manuscript requires a thorough cleaning to remove numerous internal versioning markers and drafting notes. If the authors can make the results from their companion works public and verifiable, and address the other issues raised in this report, the revised manuscript would likely be suitable for publication in Physical Review D.