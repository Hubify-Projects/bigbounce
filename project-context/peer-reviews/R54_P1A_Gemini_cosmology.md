# P1A R54 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R54_P1A/paper1a_ech_nogo.pdf` md5=439212bf pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 128.1s

---

**Referee Report for Physical Review D**

**Manuscript ID:** [Assigned by system, e.g., CZ12345]
**Title:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Author(s):** Houston Golden

This paper presents a systematic assessment of four potential channels through which minimal Einstein-Cartan-Holst (ECH) gravity could source late-time dark energy. The author concludes that all four channels are closed under stated assumptions, based on a combination of amplitude suppression, naturalness arguments, and a catalog of 13 independent "barriers". The central theoretical result is a "perturbation-transparency" theorem, showing that for canonical scalar matter, the Holst sector decouples from all scalar and tensor perturbation equations of motion. The paper also identifies a structural tension between the requirements for the dark-energy mechanism and the survival of a key matter-bounce observable (`fNL`).

The work is ambitious and systematic. The perturbation-transparency result is elegant and appears sound. The framework of enumerating routes and barriers is a valuable, structured approach to a complex theoretical space. The intellectual honesty regarding the paper's assumptions and limitations (particularly the "on-shell scaling ansatz") is commendable.

However, the manuscript in its current form has several ESSENTIAL and MAJOR issues that preclude its publication in Physical Review D. The most critical problems are its heavy reliance on non-public, "in preparation" companion papers for load-bearing results and the weak, "aesthetic" justification for a key factor in the dark-energy dilution equation. The paper is also excessively long for its core contributions.

Significant revisions are required to address these points.

---
### Detailed Findings

#### ESSENTIAL

*   **P1A-E1**
    *   **Section/Page:** Abstract & Title Page / p. 1
    *   **Problem:** The paper is dated "June 19, 2026". Submitting a paper with a future date is unprofessional and inappropriate for a journal submission.
    *   **Fix:** The date must be corrected to the actual date of submission.

*   **P1A-E2**
    *   **Section/Page:** Throughout, e.g., Abstract (p. 1), Sec. I B (p. 4), Sec. III A/B (p. 10), Sec. X G (p. 21), Sec. XIII (p. 23), References.
    *   **Problem:** The paper is not self-contained and relies critically on at least four companion papers cited as "in preparation" or "posted concurrently on arXiv" (`[2]`, `[6]`, `[23]`, `[46]`). Load-bearing results are imported from these non-public sources, including:
        1.  All cosmological parameter values (`H₀`, `ΔNeff`, etc.) used for consistency checks (from `[6]`).
        2.  The SPHEREx `fNL` forecast (`2.6-5σ`), which is a key surviving prediction (from `[2]`).
        3.  The galaxy spin asymmetry null result, which closes an observational channel (from `[23]`).
        4.  The NANOGrav PTA reanalysis (`γ_PTA`), used for discriminating bounce models (from `[46]`).
    *   **Fix:** All claims and numerical values essential to the paper's arguments must be derived within this manuscript or cited from publicly available, peer-reviewed (or at least arXiv-posted) sources. The "in preparation" citations are unacceptable. The author must either integrate the necessary derivations and results into this paper (likely in appendices) or remove the claims that depend on them. For example, the `H₀` and `ΔNeff` values in Table I and Table IV should be removed or replaced with standard Planck 2018 values, with a note that the author's framework is consistent with them. The `fNL` and `β` forecasts must be fully derived and justified within this paper if they are to be presented as key results.

#### MAJOR

*   **P1A-M1**
    *   **Section/Page:** Sec. II C 1 & Appendix B / pp. 8, 26
    *   **Problem:** The dark-energy dilution factor `D_inf` in Eq. (11) contains a prefactor `(T_reh / M_GUT)^(3/2)`. The justification for the `3/2` power is stated as "dimensional-analysis aesthetic at this level rather than calculated from a thermal partition function" and a "phenomenological phase-space ansatz". This is insufficient for a rigorous derivation in PRD. The entire quantitative argument for `N_tot ≈ 92` e-folds, and the resulting "structural tension" in Sec. XIV D, depends directly on this weakly-justified factor.
    *   **Fix:** The author must either provide a first-principles derivation for this `3/2` power or significantly downgrade all conclusions that rely on it. If a derivation is not possible, the `N_tot ≈ 92` value should be presented as a purely illustrative estimate, and the "structural tension" argument must be re-framed as a qualitative observation contingent on this undemonstrated scaling.

*   **P1A-M2**
    *   **Section/Page:** Entire manuscript
    *   **Problem:** The paper is 29 pages long. While comprehensive, its length is not justified by the scope of the novel contributions. The core new results are the perturbation-transparency theorem (Sec. X), the systematic catalog of barriers (Sec. IX), and the structural tension argument (Sec. XIV D). The rest is a mix of review, application of standard arguments (e.g., the NJL and ALP closures), and detailed exposition that could be streamlined.
    *   **Fix:** The manuscript should be substantially condensed. I recommend a target length of 15-18 pages for the main body. Material that is standard review or detailed but non-essential derivation should be moved to appendices or supplementary material. For example, the detailed descriptions of all 14 barriers could be summarized in the main text with full descriptions moved to an appendix. The introduction and theoretical framework sections could also be made more concise.

*   **P1A-M3**
    *   **Section/Page:** Sec. IV, Appendix B / pp. 10-14, 26
    *   **Problem:** The dark-energy mapping relies on a parity-odd operator (Eq. 6) with an off-shell mass dimension of +1. The paper correctly and honestly identifies that promoting this to a dimension +4 Lagrangian density requires a "phenomenological on-shell scaling ansatz". While this honesty is appreciated, it remains a fundamental weakness of the proposed dark-energy mechanism. The conclusions of the paper are conditional on this ansatz.
    *   **Fix:** The conditional nature of the dark-energy mapping needs to be emphasized even more strongly in the abstract and conclusions. The abstract currently states the mapping "rests on" the ansatz, which is good, but it should also state that the quantitative conclusions about `N_tot` and the structural tension are therefore also conditional and not derived from a controlled EFT.

#### MINOR

*   **P1A-m1**
    *   **Section/Page:** Abstract (p. 1), Sec. XV (p. 25)
    *   **Problem:** The abstract and conclusions juxtapose the WMAP+Planck `β` significance (`~3.6σ`) and the ACT DR6 significance (`~2.9σ`). The abstract correctly notes they "arise from different null procedures and are not directly comparable". However, this crucial caveat should appear every time these numbers are presented together to prevent misinterpretation by the reader. It is missing from the juxtaposition in the conclusions (Sec. XV, point 2).
    *   **Fix:** Add the "not directly comparable" caveat to the discussion in Section XV and any other location where these two significance values are mentioned together.

*   **P1A-m2**
    *   **Section/Page:** Table I / p. 4
    *   **Problem:** The `fNL` forecast is quoted as "2.6-5σ realistic" in the footnote. The main text (Sec. VII, footnote 6) explains this range. However, presenting a range for a significance is unusual. It conflates different assumptions about systematics into a single number.
    *   **Fix:** The table and abstract should quote the most conservative, fully-systematics-degraded forecast (`2.6σ`) as the headline number, and mention the more optimistic `5σ` figure as a possibility under ideal conditions in the text/footnote. This provides a clearer and more conservative picture.

*   **P1A-m3**
    *   **Section/Page:** Fig. 3 Caption / p. 8
    *   **Problem:** The caption for the orange "Spin-Torsion" curve states it uses `H₀ = 69.2 km/s/Mpc` and `Ωm = 0.310`, while the ACDM reference uses Planck-VI best-fit values. It is described as an "illustrative parameter-set comparison". This is fine, but it's not clear why these specific, non-standard values were chosen for the ECH benchmark.
    *   **Fix:** Briefly justify the choice of these cosmological parameters for the illustrative ECH curve. Are they a previous best-fit from some other model or dataset? Or are they simply chosen to produce a visible deviation? Clarify this.

#### NIT

*   **P1A-N1**
    *   **Section/Page:** Footnote a, p. 2
    *   **Problem:** The footnote contains a minor typo/grammatical error: "The Holst dual contraction has only one curvature."
    *   **Fix:** Should probably read "The Holst dual contraction involves only one curvature tensor." or similar for clarity.

*   **P1A-N2**
    *   **Section/Page:** Sec. IV D, footnote 4 / p. 13
    *   **Problem:** The footnote states: "The θ-versus-φ alternation in the body of this paper is purely a choice...". The phrasing "θ-versus-φ alternation" is slightly awkward.
    *   **Fix:** Rephrase for clarity, e.g., "The use of either θ or φ in the body of this paper is a purely notational choice...".

---
### Summary recommendation

**MAJOR REVISIONS**

This manuscript presents a valuable and systematic theoretical investigation into ECH-gravity as a source for dark energy. The perturbation-transparency theorem is a strong, novel result, and the structured "barrier" analysis provides a useful framework for constraining this and other models. However, the paper cannot be published in its current state. The reliance on unpublished companion papers for key results violates the journal's requirement for self-contained, verifiable research. Furthermore, a central pillar of the quantitative dark-energy argument rests on a physically unjustified "aesthetic" ansatz. The manuscript's excessive length also obscures its core contributions. If the author can rectify these major issues by integrating the necessary supporting material, providing a more rigorous physical basis for the dilution model (or appropriately qualifying the conclusions), and substantially condensing the text, the revised manuscript could be a significant contribution worthy of publication in Physical Review D.