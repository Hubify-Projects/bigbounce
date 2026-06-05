# P1A 2026-06-04_R5clean — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 72.7s

---

## Referee Report: P1A

**Paper Title:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Author:** Houston Golden
**Recommendation:** MAJOR REVISIONS

---

### General Comments

This paper presents a systematic, channel-level investigation into whether minimal Einstein-Cartan-Holst (ECH) gravity can serve as a source for late-time dark energy. The author concludes that the four primary channels considered are closed at the amplitude level under a set of stated assumptions. The paper's two main contributions are (1) a "perturbation transparency theorem" for canonical scalar matter, which shows that the Holst sector decouples from standard cosmological perturbations, and (2) a comprehensive catalog of 14 structural and observational constraints (barriers) that collectively close the enumerated dark-energy routes.

The perturbation transparency theorem is a clear and significant result, providing a sharp criterion for testing the theory via non-perturbative observables. The systematic catalog of barriers is thorough and builds a strong, self-contained argument for the paper's main conclusion of channel-level closure. The author is commendably transparent about the paper's limitations, particularly the reliance on a phenomenological, non-EFT ansatz to connect bounce-scale physics to the late-time vacuum energy.

However, the paper suffers from several significant issues that must be addressed before it can be considered for publication. The most critical is the repeated and essential reliance on companion papers that are "in preparation" and not publicly available, which makes key claims unverifiable. Additionally, the manuscript is overly long and repetitive, and contains prose that reads like internal version-control notes rather than a finished scientific article.

The work has the potential to be a valuable contribution, but it requires substantial revision to meet the standards of a peer-reviewed publication.

---

### Findings

#### ESSENTIAL

*   **ID: P1A-E1**
    *   **Location:** Multiple instances, e.g., Sec. II A (p. 5), Sec. III B (p. 8), Sec. V (p. 11), Sec. VII (p. 11).
    *   **Problem:** The paper's quantitative claims and observational inputs rely critically on several companion papers [2, 6, 23, 46] that are cited as "in preparation". This includes:
        1.  The cosmological parameter values (H₀, ∆Neff, etc.) used throughout the paper (p. 5, from [6]).
        2.  The confirmation of the galaxy spin null result (p. 8, from [23]).
        3.  The detailed Fisher forecast for the matter-bounce `f_NL` signature (p. 11, from [2]).
        4.  The MCMC verification and pipeline validation details (Abstract, p. 1, from [6]).
    *   **Required Fix:** All claims essential to the arguments in this paper must be supported by citable, publicly accessible work (e.g., a published paper or an arXiv preprint) or be sufficiently documented within this manuscript itself (e.g., in an appendix). It is not acceptable to base the core results of a paper on unpublished and unavailable work. The author must either provide the necessary details and validation within this paper or wait to submit this manuscript until the companion works are available on a public server like arXiv.

*   **ID: P1A-E2**
    *   **Location:** Sec. XIII, Table III, Footnote ‡ (p. 16).
    *   **Problem:** The footnote provides a "live update" on the status of a running MCMC chain, including the number of accepted samples and the current convergence metric (R̂ - 1). This type of information is inappropriate for a static, archival publication. It reads like a lab notebook entry.
    *   **Required Fix:** Remove the live-update details. The footnote should simply state that the MCMC analysis for the `w₀wₐ` parameter space was not performed for the models in question at the time of writing, and therefore their status is reported as "not tested" or "theoretically consistent" without a quantitative fit assessment.

#### MAJOR

*   **ID: P1A-M1**
    *   **Location:** Throughout the manuscript.
    *   **Problem:** The paper is excessively verbose and repetitive. The central "structural tension" argument between the `N_tot` required for dark energy (≈92) and the `N_tot` that erases the `f_NL` signal (≳60) is presented in detail in the Abstract (p. 1), the Introduction (Sec. I A, p. 3), again in the Surviving Tests section (Sec. XIII, p. 16), and for a fourth time in the Limitations section (Sec. XIV D, p. 17). While the point is important, this degree of repetition is unnecessary and bloats the manuscript. The paper's 21-page length could be significantly reduced by streamlining the prose and consolidating repeated arguments.
    *   **Required Fix:** The author should perform a thorough edit to improve conciseness. Consolidate the discussion of the "structural tension" into one primary location (e.g., Sec. XIV D, where it is framed as a robustness check) and refer back to it briefly elsewhere. The paper should aim for a length of approximately 15-17 pages, which is more appropriate for the scope of its core contributions.

*   **ID: P1A-M2**
    *   **Location:** Multiple instances, e.g., Sec. IV (p. 8), Sec. XII A (p. 15).
    *   **Problem:** The text contains several phrases that appear to be artifacts from the manuscript's revision history or internal author notes. Examples include:
        1.  (p. 8) "this section replaces the single-paragraph forward reference of earlier versions and stands as the referee-grade audit trail of the no-go."
        2.  (p. 8) "Three substantive theory-derivation issues were identified during preparation of this paper and are documented here for the record..."
        3.  (p. 15) "the entries in this section are retained as parameterization-of-fine-tuning diagnostics, not as a viable dynamical channel."
    *   **Required Fix:** Rephrase this text to be appropriate for a formal scientific publication. The author's internal process and the evolution of the manuscript are not relevant to the reader. The points themselves are valid but should be presented as direct scientific statements.

#### MINOR

*   **ID: P1A-m1**
    *   **Location:** Appendix B (p. 19).
    *   **Problem:** In the text following Eq. (B2), there appears to be a typo or inconsistency in the powers of M_Pl. The equation is `ρ_Λ^bounce ~ (α/M) M_Pl^5 ~ 10^-2 M_Pl^4`. The first relation, `ρ_Λ^bounce ~ (α/M) M_Pl^5`, is dimensionally correct for an energy density, since `[α/M] = -1` and `[M_Pl^5] = +5`, yielding a dimension of +4. The second relation, `(α/M) M_Pl^5 ~ 10^-2 M_Pl^4`, implies `(α/M) M_Pl ~ 10^-2`, which is consistent with statements made earlier in the paper. However, the expression as written is confusing.
    *   **Required Fix:** Clarify the expression. For example, state that `ρ_Λ^bounce` is defined as `(α/M) M_Pl^5`, and then note that the dimensionless prefactor is constrained such that `(α/M) M_Pl ≈ 10^-2`, leading to `ρ_Λ^bounce ≈ 10^-2 M_Pl^4`.

*   **ID: P1A-m2**
    *   **Location:** Abstract (p. 1).
    *   **Problem:** The abstract mentions "13 logically-independent mechanism-class constraints (the prior count of 14 retained Barrier 8 as the observational consequence of the perturbation-transparency theorem Barrier 14; merged here...)" This level of detail about the internal bookkeeping of the constraints is confusing for an abstract.
    *   **Required Fix:** Simplify this statement in the abstract. State that the paper reports a set of structural constraints (e.g., "13 logically-independent constraints") that close the enumerated channels, and leave the details of their enumeration and inter-dependencies for the main text (e.g., Table II and its caption).

---

## Summary recommendation

**MAJOR REVISIONS**

This paper presents a valuable and rigorous systematic analysis, with the perturbation transparency theorem being a particularly strong contribution. The author's honesty regarding the foundational ansatz is a major strength. However, the paper is not yet in a state suitable for publication. The reliance on unavailable "in preparation" works for key results is a critical flaw that must be rectified. Furthermore, the manuscript requires significant editing to improve its clarity, conciseness, and professionalism. If the author can address these major issues, the revised manuscript will likely be a welcome addition to the literature.