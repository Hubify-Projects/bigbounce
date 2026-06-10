# P1A 2026-06-04_R6clean — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 92.5s

---

# Referee Report

**Paper:** Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Author:** Houston Golden
**Manuscript ID:** [Assigned by editor]

This paper undertakes a systematic assessment of four potential routes for generating late-time dark energy from the minimal Einstein-Cartan-Holst (ECH) framework, coupled with a Loop Quantum Cosmology bounce. The author concludes that all four channels fail at the amplitude level under a set of stated assumptions. The paper's main contributions are the channel-level closure argument, a "perturbation-transparency theorem" for canonical scalar matter, and the identification of a "structural tension" between the requirements for the dark-energy mechanism and the preservation of a key observational signature of matter bounces (`f_NL`).

The paper is well-structured and commendable for its transparency regarding its scope and assumptions. The perturbation-transparency theorem is a clean, useful result, and the careful distinction between ECH-specific predictions and broader bounce-class or spectator-field observables is a strength.

However, the manuscript contains several essential and major issues that must be thoroughly addressed before it can be considered for publication. These include a likely error in a core physical calculation, contradictory claims between figures and text, and a confusing and inconsistent presentation of the key dimensional ansatz.

## Findings

### ESSENTIAL

**P1A-E1: Inappropriate inclusion of transient computational details.**
*   **Section/Page:** XVI, Table III, footnote ‡ (page 16).
*   **Problem:** The footnote provides a real-time status update of an ongoing MCMC computation, including the number of accepted samples and the current, non-converged Gelman-Rubin statistic (`R̂ − 1 ≈ 3×10−2`). This level of transient detail is inappropriate for a static, peer-reviewed scientific article. It reads as a progress report rather than a finished analysis.
*   **Required Fix:** The footnote must be rewritten to remove all specific, transient numerical values. It should state concisely that the analysis for this model is in progress and has not yet yielded a converged result suitable for drawing conclusions. For example: "The MCMC analysis for this model, including a free `w0-wa` parameterization, is in progress. As it has not yet converged to publication-quality standards, we report it as 'not tested' at the posterior level."

### MAJOR

**P1A-M1: Potentially incorrect calculation of physical wavenumber evolution.**
*   **Section/Page:** Abstract (p. 1), Sec. I.A (p. 3), Sec. XIV.D (p. 17).
*   **Problem:** The paper's "structural tension" argument relies on calculating the physical wavenumber of a mode at the bounce (`kbounce_phys`). The formula used is `kbounce_phys ~ kSPHEREx_phys * e^(Ntot-Nexit)`. This appears to be physically incorrect. The physical wavenumber `k_phys` scales as `1/a`. The ratio of physical wavenumbers between the bounce and horizon exit is `k_phys(bounce) / k_phys(exit) = a_exit / a_bounce = e^(N_exit)`. The paper's formula uses `N_tot - N_exit`, which is the number of e-folds of inflation *after* the mode has exited the horizon. The physics of how a mode is stretched before exit should depend on `N_exit` (≈ 60), not `N_tot - N_exit` (≈ 32). This represents an enormous numerical difference (`e^60` vs. `e^32`) and calls into question the quantitative aspect of the structural tension claim.
*   **Required Fix:** The author must provide a rigorous derivation for the formula `kbounce_phys ~ kSPHEREx_phys * e^(Ntot-Nexit)`. If the formula is incorrect, the calculation must be redone using the correct physical scaling (`e^(N_exit)`), and the conclusions of the structural tension argument in Sec. XIV.D (and its summaries in the abstract and introduction) must be revised accordingly.

**P1A-M2: Contradictory and unsupported claim regarding Ekpyrotic models.**
*   **Section/Page:** I, Figure 1 (page 4).
*   **Problem:** Figure 1, a central schematic of the paper's argument, places a dashed box labeled "structurally closed (this paper)" around the "Ekpyrotic" mechanism. However, the paper's analysis focuses on a quantum bounce within LQC and ECH. There is no section or argument presented in the text that justifies the closure of the entire class of ekpyrotic models. Furthermore, Table III on page 16 lists "Ekpyrotic" as a distinct model to be tested, not as one that has been closed. This is a direct contradiction.
*   **Required Fix:** The label "structurally closed (this paper)" must be removed from the "Ekpyrotic" box in Figure 1. The paper's claims must be strictly limited to the scope of the analysis performed, which does not cover the general ekpyrotic scenario.

**P1A-M3: Confusing and dimensionally inconsistent presentation of the core ansatz.**
*   **Section/Page:** Appendix B, Eq. (B2) (page 19).
*   **Problem:** The dimensional analysis and phenomenological scaling that underpins the entire dark-energy mapping is presented in a highly confusing and inconsistent manner. Equation (B2), `ρ_Λ^bounce ~ (α/M) M_Pl^5 ~ 10^-2 M_Pl^4`, is dimensionally flawed as written. While `(α/M) M_Pl^5` has the correct units of `[Mass]^4`, equating it to `10^-2 M_Pl^4` implies `(α/M) M_Pl ~ 10^-2`, which is a relation between quantities, not an identity. This makes the logic of the appendix very difficult to follow and verify.
*   **Required Fix:** Appendix B must be completely rewritten for clarity and correctness. The author should clearly separate: (1) The statement of the phenomenological ansatz (e.g., `ρ_Λ^bounce = C · M_Pl^4`); (2) The dimensional analysis showing how a dimension-4 operator can be constructed (e.g., using a coupling `α M_Pl^3 / M`); and (3) The phenomenological argument for estimating the dimensionless constant `C` (e.g., `C ~ (α/M)M_Pl`). All equations must be presented in a dimensionally consistent form.

### MINOR

**P1A-m1: Inconsistent notation and undefined terms.**
*   **Section/Page:** Abstract (p. 1).
*   **Problem:** The notation for the Pontryagin density is inconsistent, appearing as `R ∧ R̃` and later as `RR̃` (missing the tilde). Additionally, the subscript `BI` in `γ_BI` is used without definition.
*   **Required Fix:** Use a single, consistent notation for the Pontryagin density throughout the manuscript. Define the subscript `BI` as "Barbero-Immirzi" at its first use, or simply use the standard symbol `γ`.

**P1A-m2: Physically weak justification for a key prefactor.**
*   **Section/Page:** II.C.1 (page 6).
*   **Problem:** The derivation of the `(T_reh / M_GUT)^(3/2)` factor in the inflationary dilution term `D_inf` is justified with vague, non-rigorous language such as "dimensional-analysis aesthetic" and a "parity-odd density-of-states factor". While the author is commendably transparent about the weakness of this argument, it remains a significant weak point in the quantitative derivation of `N_tot ≈ 92`.
*   **Required Fix:** The author should either provide a more physically grounded, albeit schematic, argument for this factor or further emphasize its speculative nature in the main text. It should be made clearer that the paper's stronger "reheating thermal-reset" argument for closure is independent of this factor.

**P1A-m3: Typo in physical constant.**
*   **Section/Page:** I.A (page 3).
*   **Problem:** The text reads "pcrit ~ 0.27-0.41 PP1".
*   **Required Fix:** Correct "PP1" to the standard notation for the Planck density, `ρ_Pl`.

### Comments on Paper Length

The manuscript is 21 pages long. While the content is substantial, the core novel contributions could be presented more concisely. The detailed catalog of 14 "barriers" in Section IX, many of which are standard concepts in cosmology, adds considerable length. The paper's impact could be improved by restructuring it into a more focused main text (e.g., 10-12 pages) that highlights the four-route closure, the perturbation-transparency theorem, and the structural tension, with the exhaustive barrier catalog moved to an appendix or supplementary material. This is a suggestion for the author to consider.

## Summary recommendation
**MAJOR REVISIONS**

The paper presents a valuable, systematic investigation of a class of modified gravity models as a source for dark energy. The work is thorough, and the author is careful to state the limitations and assumptions. However, the manuscript is not ready for publication due to several major flaws. The physical calculation underlying the "structural tension" argument appears incorrect and must be corrected. The claims made in a central figure are not supported by the text. The presentation of the core dimensional ansatz is confusing and must be clarified. Once these significant issues have been fully addressed, the revised manuscript will likely be a strong candidate for publication in Physical Review D.