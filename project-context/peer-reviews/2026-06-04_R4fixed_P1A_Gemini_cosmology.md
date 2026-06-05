# P1A 2026-06-04_R4fixed — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 88.3s

---

**Referee Report for PRD Manuscript P1A**

This paper presents a systematic, channel-level analysis of four potential routes for generating late-time dark energy from a minimal Einstein-Cartan-Holst (ECH) framework in a bouncing cosmology. The author(s) conclude that all four routes fail at the amplitude level under a set of stated assumptions. The central theoretical result is a "perturbation-transparency theorem," which shows that for canonical scalar matter, the Holst sector decouples from all scalar and tensor perturbation observables, rendering the Barbero-Immirzi parameter γ invisible to these probes. The paper also discusses surviving, mechanism-independent predictions of the broader bounce-cosmology paradigm, namely a specific non-Gaussianity signature (f_NL = -35/8) and cosmic birefringence from a spectator field.

The paper's strengths lie in its systematic cataloging of constraints and its intellectual honesty regarding its core assumptions, particularly the phenomenological nature of the link between the ECH sector and dark energy. The perturbation-transparency theorem is a clear and valuable result. However, the manuscript suffers from several significant issues that preclude its publication in the present form. The most critical problems are its heavy reliance on unpublished companion papers for key observational and numerical results, and a flawed and confusing dimensional analysis of the core parity-odd operator that underpins the entire dark-energy argument.

## Findings

### ESSENTIAL

*   **P1A-E1 (Throughout): Reliance on "In Preparation" Companion Papers.**
    *   **Problem:** The manuscript's key quantitative results and observational inputs rely on at least four companion papers cited as "in preparation" ([2], [6], [23], [46]). This includes the MCMC cosmological parameter analysis (H0, ΔNeff), the NaMaster pipeline validation, the galaxy spin null result, the PTA spectral index analysis, and the SPHEREx f_NL forecast. A paper submitted for publication cannot be based on results that are not publicly available for scrutiny.
    *   **Fix:** All companion papers that provide essential inputs to this manuscript must be made publicly available (e.g., on arXiv) and cited accordingly. The current manuscript cannot be properly evaluated or accepted until this is done.

*   **P1A-E2 (Appendix B, p. 19): Flawed Dimensional Analysis of the Parity-Odd Operator.**
    *   **Problem:** Appendix B, which is critical to the entire dark-energy argument, contains a dimensionally incorrect key equation and a confusing explanation. Equation (B2), `ρ_Λ^bounce ~ (α/M) M_Pl^5`, is dimensionally inconsistent. The left side has units of [Mass]^4, while the right side has units of [Mass]^-1 * [Mass]^5 = [Mass]^4. While the units match, the subsequent text `~ 10^-2 M_Pl^4` implies `(α/M) M_Pl ~ 10^-2`. This would mean the equation should be `ρ_Λ^bounce ~ [(α/M) M_Pl] M_Pl^4`. The current presentation is incorrect and makes the foundation of the N_tot ≈ 92 calculation impossible to verify. The subsequent discussion attempting to construct a dimension-+4 operator is also unclear.
    *   **Fix:** The author must correct Equation (B2) and rewrite Appendix B to provide a clear, dimensionally consistent, and verifiable account of the "phenomenological on-shell scaling ansatz." This is the central assumption for the dark energy connection, and its formal basis must be presented without errors.

### MAJOR

*   **P1A-M1 (Figure 1, p. 4): Outdated Information in Figure.**
    *   **Problem:** Figure 1, the main conceptual map of the paper, contains outdated information. It lists the PTA result as "γ = 3.0 v.s. data 3.20 ± 0.42". However, the main text (p. 15) explicitly states this value is superseded by a new analysis yielding `γ = 2.567 ± 0.382`. The figure must reflect the final results presented in the paper.
    *   **Fix:** Update Figure 1 to be consistent with the final results and analysis presented in the main text.

*   **P1A-M2 (Sec. IV, p. 8): Inappropriate "Internal Monologue" Section.**
    *   **Problem:** The paragraph on p. 8 beginning "Three substantive theory-derivation issues were identified..." reads like an internal review note, not formal prose for a scientific paper. It documents the author's process of correcting their own misunderstandings (e.g., on the parity of a squared pseudovector, on dimensional analysis). These are standard calculations, and documenting them as "substantive issues" is inappropriate.
    *   **Fix:** Remove this entire paragraph. The corrected, final arguments should simply be presented in the relevant sections without commentary on the author's previous draft-level errors.

*   **P1A-M3 (Sec. XIV A, p. 17): MCMC Proxy Limitation is Understated.**
    *   **Problem:** The "Limitations" section reveals a critical methodological weakness: "MCMC proxy: Stock CAMB with ΔNeff is a phenomenological proxy, not a bespoke spin-torsion Boltzmann module." This means the cosmological constraints used to test the ECH framework were derived using a code that does not actually implement the ECH physics. This is a major caveat that must be made clear much earlier and more prominently in the paper.
    *   **Fix:** Add a clear statement in the Abstract and the Introduction (Sec. I) explaining that the MCMC analysis relies on a phenomenological proxy (ΔNeff) for the effects of ECH, not a first-principles implementation.

*   **P1A-M4 (Sec. IV & XII B): Missing Details in Main Argument.**
    *   **Problem:** The discussion in Sec. XII B (p. 15) provides a key physical reason for the failure of the NJL condensate route: "The condensate route fails because the scalar/pseudoscalar channel is repulsive at γ = 0.274 and subcritical." This crucial detail is absent from the main argument in Sec. IV A, where the route is closed only on grounds of Planck suppression and parity.
    *   **Fix:** Move this more specific physical argument from the discussion into the main "no-go" section (Sec. IV A) to strengthen the primary claim.

### MINOR

*   **P1A-m1 (Throughout): Repetitive Arguments and Internal Artifacts.**
    *   **Problem:** The paper contains several instances of version-history artifacts (e.g., "not the ~ 35 misstated in earlier drafts" on p. 19; "The prior analysis that compared..." on p. 9). Furthermore, the "structural tension" argument (N_tot vs f_NL) is presented in full detail at least three times (Abstract, Sec. XIII, Sec. XIV D). This makes the paper longer than necessary.
    *   **Fix:** Remove all internal review artifacts and commentary on previous drafts. Consolidate the repetitive "structural tension" argument into a single, clear section (Sec. XIV D seems most appropriate) and refer back to it. The paper could be significantly tightened from 21 pages to a more concise ~15-16 pages.

*   **P1A-m2 (Abstract, p. 1): Non-Standard Notation.**
    *   **Problem:** The notation "RAŘ" for the gravitational Chern-Simons term is non-standard. The Pontryagin density is written as "∝ RR" when it should be "∝ R R̃" or "∝ Rμνρσ *Rμνρσ".
    *   **Fix:** Use standard notation, such as `R ∧ R` or `Tr(R ∧ R)` for the Chern-Simons term and `R R̃` for the Pontryagin density, to avoid ambiguity.

*   **P1A-m3 (Sec. IV & XI, p. 2): Informal Section Titles.**
    *   **Problem:** Section titles such as "Four-Route No-Go" and "The Hybrid Dark-Energy Loophole" are overly informal for a publication in Physical Review D.
    *   **Fix:** Revise these titles to be more formal. For example: "Closure of Four Standard ECH Channels" and "Analysis of a Hybrid Dark-Energy Scenario."

*   **P1A-m4 (Table III, p. 16): Overly Detailed Footnote.**
    *   **Problem:** Footnote ‡ in Table III provides excessive real-time detail about an MCMC chain that is currently running. This level of "work-in-progress" reporting is not appropriate for a static publication.
    *   **Fix:** Condense the footnote to a simple statement that the MCMC analysis was not extended to include a free `w0-wa` model for the reported results.

### NIT

*   **P1A-n1 (p. 1): Future Date.**
    *   **Problem:** The paper is dated "June 2, 2026 PDT".
    *   **Fix:** Replace with the current submission date.

*   **P1A-n2 (p. 1): Placeholder Email.**
    *   **Problem:** The contact email appears to be a placeholder.
    *   **Fix:** Provide a stable, professional contact email.

## Summary recommendation

**MAJOR REVISIONS**

The manuscript presents a valuable and systematic investigation of a well-motivated theoretical framework. The perturbation-transparency theorem is a clear, publishable result, and the overall "channel-level closure" argument is a useful contribution to the literature. However, the paper is not yet in a publishable state. The essential requirements are to make all supporting data and analysis from companion papers publicly available and to correct the fundamental errors in the dimensional analysis that underpins the dark-energy claims. Furthermore, major revisions are needed to improve the paper's structure, clarity, and professionalism by removing internal artifacts, clarifying the limitations of the MCMC analysis, and updating figures to be consistent with the text. If the author can satisfactorily address these points, the revised manuscript would likely be suitable for publication.