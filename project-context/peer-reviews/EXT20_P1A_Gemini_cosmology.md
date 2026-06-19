# P1A EXT20 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=198cb994 pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 163.4s

---

## Referee Report on "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"

**Manuscript ID:** [Assigned by journal]
**Author:** Houston Golden
**Journal:** Physical Review D

### Summary of the Paper

This manuscript presents a comprehensive theoretical and phenomenological investigation of minimal Einstein-Cartan-Holst (ECH) gravity as a potential source for late-time dark energy. The author enumerates and assesses four distinct "routes" for generating a dark-energy component from spin-torsion interactions. The central claims are: (1) a "channel-level closure" of these four routes, finding them to be either amplitude-suppressed or subject to a fine-tuning/naturalness objection that relocates the cosmological constant problem rather than solving it; (2) a "perturbation transparency" theorem, demonstrating that for canonical scalar matter, the Holst sector decouples from all scalar and tensor perturbation equations of motion, leaving them identical to those in standard General Relativity; and (3) the identification of a structural tension between the inflationary e-fold number required for the ECH dark-energy mechanism and the survival of a matter-bounce non-Gaussianity signature (`fNL = -35/8`). The paper also discusses the consistency of a spectator axion-like particle (ALP) with observed cosmic birefringence.

The paper contains several valuable contributions, most notably the perturbation-transparency theorem and the structural tension argument. The systematic cataloging of constraints is also a useful organizational effort. However, the manuscript suffers from significant structural issues, primarily the heavy reliance on a non-rigorous "scaling ansatz" for its dark energy claims and its dependence on multiple companion papers that are not yet available for independent review.

### General Comments

The manuscript is ambitious, detailed, and demonstrates a deep command of the relevant physics. The perturbation-transparency result (Section X) is elegant, appears correct, and represents a novel and important contribution to the literature on ECH cosmology. Similarly, the structural tension argument (Section XIV D), which pits the `N_tot ≈ 92` e-folds needed for dark energy against the erasure of the `fNL` signal, is a powerful and original consistency check.

Despite these strengths, the paper requires major revisions before it can be considered for publication in Physical Review D.

1.  **The Foundational "Ansatz":** The entire dark-energy-generation part of the argument rests on a "phenomenological on-shell scaling ansatz" (Appendix B). The author is commendably transparent about this, stating explicitly that the leading parity-odd operator has the wrong mass dimension (`+1` instead of `+4`) and that its promotion to a dark energy density is "not a controlled EFT calculation." This admission, while honest, relegates a significant portion of the paper to a speculative "what if" exercise. The strong "closure" language used in the abstract and introduction is not fully supported when the foundation of the mechanism being "closed" is an ansatz rather than a derived result from the ECH action. The paper should be restructured to more clearly separate the rigorous, derivable results (the transparency theorem, the structural tension) from the consequences of the speculative ansatz.

2.  **Reliance on Companion Papers:** The manuscript is not self-contained. It makes load-bearing references to at least four other papers by the same author ([2], [6], [23], [46]) that are described as "in preparation" or "posted concurrently." This is unacceptable for a submission to a peer-reviewed journal. For example, the cosmological parameter values quoted throughout (e.g., in Table IV) are derived from an MCMC analysis in paper [6]. The detailed `fNL` forecast and strategy are in paper [2]. Without public, stable (i.e., arXiv-posted) versions of these companion works, it is impossible for a referee to verify key inputs and assess the full context of the claims. The paper must be made self-contained, or all companion papers must be made publicly available on arXiv and cited with their identifiers.

3.  **Framing and Scope:** The abstract is overly long and dense, reading more like an executive summary. It frames the paper as a "closure" of dark energy routes, but the most robust conclusions are actually the *decoupling* of ECH from standard observables (perturbation transparency) and the *inconsistency* of the ECH dark-energy mechanism with other bounce observables (`fNL`). The surviving "predictions" (`fNL` and `β`) are correctly identified as not being specific to ECH. The framing should be revised to lead with the strongest, most rigorous results. The "closure" of the dark energy routes should be presented as conditional on the foundational ansatz.

### List of Required Revisions

#### ESSENTIAL

*   **P1A-E1 (Throughout): Companion Papers.** The paper cannot be reviewed properly while relying on non-public companion works. The author must, prior to resubmission, post all cited companion papers ([2], [6], [23], [46]) to a public preprint server like arXiv and update the citations to include the arXiv identifiers. All claims that depend on results from those papers (e.g., MCMC parameter values, `fNL` forecast details) must be verifiable by the reader.
*   **P1A-E2 (Abstract, Sec I, Sec IV, Sec XV): Reframing around the Ansatz.** The speculative nature of the dark energy mechanism must be made clear from the outset. The abstract and introduction must be rewritten to state upfront that the dark-energy mapping relies on a phenomenological scaling ansatz, not a rigorous derivation. The "closure" result should be described as conditional on this ansatz. The paper's primary, unconditional contributions—the perturbation-transparency theorem and the structural tension—should be given greater prominence.
*   **P1A-E3 (Abstract, p. 1): Juxtaposition of Significance Values.** The abstract presents several significance values (3.6σ for `β`, 2.9σ for `β`, and 2.6-5σ for `fNL`). The text correctly notes that the `β` values are not directly comparable, but this crucial caveat must be present *every single time* such numbers are placed side-by-side to avoid misleading the reader. The sentence "...these significances, and the SPHEREx forecast 2.6-5σ quoted above, arise from different null procedures and are not directly comparable in a single tension table" is good, but this principle must be applied universally.
*   **P1A-E4 (p. 1): Placeholder Date.** The date of the paper is given as "June 18, 2026". This placeholder must be removed and replaced with the date of submission.

#### MAJOR

*   **P1A-M1 (Abstract): Abstract Length and Clarity.** The abstract is currently 53 lines long and excessively detailed. It should be condensed to a standard PRD length (roughly half its current size) and focus on the main, robust conclusions. The detailed breakdown of the four routes and the numerical values of `β` and its uncertainties should be left to the main text.
*   **P1A-M2 (p. 8, Eq. 11): Derivation of the `(T_reh/M_GUT)^3/2` Factor.** The derivation of this crucial prefactor for the inflationary dilution is described as a "dimensional-analysis aesthetic" and a "phenomenological phase-space ansatz." This is too weak for a quantitative argument. While a full first-principles derivation may be beyond the scope, the author must provide a more physical justification or, failing that, perform a sensitivity analysis to show how the conclusions (e.g., `N_tot ≈ 92`) depend on this factor. As it stands, it undermines the quantitative precision of the dark energy argument.
*   **P1A-M3 (p. 4, Table I): Oversimplification in Executive Summary.** The entry "Testable prediction? `fNL = -35/8`" is misleading. As the main text and abstract clarify, this is a prediction of the *matter-bounce class*, not ECH specifically. The table should be revised to reflect this, e.g., "Surviving class-level prediction?".
*   **P1A-M4 (p. 23, Sec. XIV D): The `fNL` Erasure Argument.** This is one of the strongest and most novel parts of the paper. It deserves more prominence. The author should consider moving a summary of this structural tension argument from the "Limitations" section into the main results (e.g., Section XII or a new dedicated section) as it represents a powerful, model-independent constraint on combining bounce-generated `fNL` with a long period of subsequent inflation.

#### MINOR

*   **P1A-N1 (p. 4, "Companion paper"): MCMC Details.** The text states that MCMC details are in a companion paper. While the full chains are not required, the main paper should at least specify the datasets, priors, and likelihoods used to derive the cosmological parameters in Table IV for the sake of clarity and completeness.
*   **P1A-N2 (p. 8, Fig 3): Figure Utility.** The caption for Figure 3 correctly states that the ECH curve is an "illustrative parameter-set comparison... not a derived prediction." Given this, the figure itself adds little value, as it simply shows that a `ΛCDM`-like model with slightly different parameters and a small `ΔN_eff` is similar to `ΛCDM`. The author should consider removing this figure to save space.
*   **P1A-N3 (p. 18, Fig 5): Fine-Tuning Score.** The bottom panel of Figure 5 is an excellent visualization. However, the label "Fine-Tuning Score" could be more precise. The axis represents the logarithm of the ratio of energy scales, e.g., `log10(M_Pl^4 / ρ_Λ)`. The caption should clarify the precise definition of the score.
*   **P1A-N4 (p. 25, "Surviving tests"): LiteBIRD `β` Forecast.** The calculation of the `~0.73σ` significance for discriminating the spectator-ALP `β=0.27°` from the current WMAP+Planck central value is excellent. However, the text says "the test is dominated by the current Planck term". This should be quantified. A simple quadrature sum `sqrt(0.094^2 + 0.03^2) ≈ 0.0987` shows the final uncertainty is indeed close to the Planck uncertainty, confirming the statement. This is a good detail to include.

#### NIT

*   **P1A-T1 (Throughout): Acronyms.** The paper uses a large number of acronyms (ECH, NJL, EA, ALP, LQC, etc.). While standard in the field, a single list or table of acronyms could improve readability for a broader audience.
*   **P1A-T2 (p. 11, Eq. 13): Equation Labeling.** The equation for the NJL interaction is labeled `L_tor^NJL`. Since torsion has been integrated out, a label like `L_eff^NJL` might be more appropriate.

### Summary Recommendation

**MAJOR REVISIONS**

This manuscript contains novel and significant results that are suitable for publication in Physical Review D, particularly the perturbation-transparency theorem and the structural tension between dark energy generation and `fNL` survival. However, in its current form, the paper's core claims about dark energy are built on a speculative ansatz, and its arguments are not verifiable due to a heavy reliance on non-public companion papers.

For the paper to be acceptable, the author must:
1.  Make all companion papers publicly available on the arXiv and cite them properly.
2.  Restructure the paper to clearly distinguish between the rigorous, derivable results and the speculative consequences of the scaling ansatz. The abstract and introduction must be rewritten to reflect this, leading with the most robust contributions.
3.  Address the other specific points listed above.

If these major revisions are carried out successfully, the resulting manuscript would represent a strong and valuable contribution to the cosmology literature.