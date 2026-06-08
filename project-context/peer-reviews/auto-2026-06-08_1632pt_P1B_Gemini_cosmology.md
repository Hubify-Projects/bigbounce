# P1B auto-2026-06-08_1632pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 131.5s

---

## Referee Report on "Technical Verification Companion to the ECH Spin-Torsion Program..."

**ID:** P1B

This paper presents three technical analyses intended to support a broader program on Einstein-Cartan-Holst (ECH) cosmology: (1) a `ACDM+Neff` MCMC analysis as a null test, (2) a `NaMaster` pipeline validation for cosmic birefringence, and (3) a consistency check of cosmic birefringence with a spectator axion-like particle (ALP) model.

The paper contains useful technical validations and parameter constraints. The `ACDM+Neff` analysis is competently executed and correctly interpreted as a null result. The `NaMaster` pipeline validation is a valuable cross-check. The ALP consistency analysis is detailed and commendably transparent about the fine-tuning required.

However, the manuscript suffers from several significant issues that preclude its publication in Physical Review D in its current form. These include a mathematically incorrect calculation in a key table, a major cosmological claim that is not substantiated with the appropriate statistical evidence, misleading framing of one of the analyses, and the inclusion of inappropriate content. The overall structure is also disjointed, reading as three separate notes rather than a cohesive paper.

Major revisions are required to address these points.

---
### ESSENTIAL Revisions

**P1B-E1**
*   **Section:** III / Table II, footnote b
*   **Page:** 4
*   **Problem:** The explanation and calculation of the pivot equation of state parameter, `w_pivot`, and its uncertainty are incorrect. The formula provided for the variance, `σ_wpivot^2 = σ_w0^2 + (1-ap)^2 σ_wa^2`, appears to be the variance of a sum of uncorrelated variables, which contradicts the stated purpose of decorrelating `w0` and `wa`. Furthermore, applying the standard formula for the variance of a decorrelated parameter, `Var(w_pivot) = Var(w0) - (Cov(w0,wa)^2)/Var(wa)`, with the numbers derivable from the footnote (`Cov(w0,wa) = (1-ap)Var(wa)`), leads to a negative variance.
*   **Required Fix:** The entire footnote must be rewritten. The authors must use the standard, correct definitions for the pivot redshift and the equation of state at that redshift. The calculation of `w_pivot` and its uncertainty must be corrected and verified. If the authors are using a non-standard definition, it must be clearly defined and justified.

**P1B-E2**
*   **Section:** V.B, "Results"
*   **Page:** 6
*   **Problem:** The paper reports a strong preference for a phantom `w0-wa` model, with parameters deviating from the LCDM point `(-1, 0)` by `+4.3σ` and `-3.6σ` respectively. However, the authors then state, "We do not report ... In B Bayes-factor model-comparison numbers in this paper," and argue that a dedicated nested-sampling run is required. Claiming a >4σ model preference without providing the corresponding Bayesian evidence is not sufficiently rigorous for PRD. The parameter tension in a Metropolis-Hastings chain does not directly equate to evidence for a more complex model.
*   **Required Fix:** The authors must either:
    1.  Perform the necessary nested sampling analysis (e.g., with PolyChord or MultiNest) on the identical likelihood stack and report the Bayes factor (ln B) for the `w0-wa` model versus LCDM.
    2.  If they cannot provide the Bayes factor, they must substantially downgrade the claims. The results should be framed strictly as a parameter tension within the `w0-wa` model, explicitly stating that this does not constitute evidence for the model itself over LCDM. All language implying a model preference or a "canonical quintom signature" being favored by the data must be removed.

**P1B-E3**
*   **Section:** Appendix B / Table III
*   **Page:** 10
*   **Problem:** Table III, "Claims classification for this companion paper," is inappropriate for a scientific publication. It appears to be an internal author checklist or a summary for reviewers, breaking the formal structure of a research paper.
*   **Required Fix:** Remove Table III and its reference in the text entirely. The claims and their verification status should be evident from the main body of the paper.

---
### MAJOR Revisions

**P1B-M1**
*   **Section:** VI and Appendix C
*   **Page:** 6, 7, 9
*   **Problem:** The analysis is framed as a "Spectator ALP Consistency Check," but this is misleading. As revealed in footnote 5 (page 9), the MCMC analysis uses a prior on the initial misalignment angle, `θi ∈ [0.5, 2]`, which the authors admit is "NOT the spectator-consistent sub-range" (`θi ~ 0.1`). The chosen prior range corresponds to a regime where the ALP would behave as a dark energy component, not a spectator field. The main text does not adequately reflect this crucial distinction.
*   **Required Fix:** Reframe the entire analysis in Section VI. It should be presented as a constraint on a general ultra-light/dark-energy ALP model. The "spectator" case should then be discussed as a specific, fine-tuned sub-region of the parameter space. The `~25x` fine-tuning required to enter the spectator regime, currently mentioned in passing and in footnotes, must be given more prominence in the main text and abstract to accurately represent the model's (lack of) naturalness.

**P1B-M2**
*   **Section:** Overall Structure
*   **Page:** 1-11
*   **Problem:** The paper lacks a clear, unifying narrative. It reads as a collection of three disconnected analyses: a `ACDM+Neff` run, a surprising `w0-wa` result, and an ALP check. The `w0-wa` analysis, in particular, is introduced abruptly in the middle of Section III without motivation in the introduction or abstract. The connection between these three disparate topics and the main ECH program mentioned in the title is tenuous and not well-articulated.
*   **Required Fix:** The authors should restructure the paper to improve its flow and coherence. The introduction should clearly state that three separate verification tasks will be documented and provide a brief rationale for each. The `w0-wa` analysis should be presented in its own distinct section with proper introduction and context, rather than being appended to the `ACDM+Neff` section.

---
### MINOR Revisions

**P1B-m1**
*   **Section:** Abstract and Section VII (Conclusions)
*   **Page:** 1, 8
*   **Problem:** The abstract states the `NaMaster` pipeline-recovery bias is `0.032°`. The main text (page 6) and conclusions (page 8) clarify that the bias is amplitude-dependent, ranging from `0.032°` to `0.040°`.
*   **Required Fix:** Update the abstract to reflect the range of the bias or the worst-case value (`0.040°`) for full transparency.

**P1B-m2**
*   **Section:** III / Figure 1
*   **Page:** 5
*   **Problem:** The number of samples plotted in Figure 1 (119,617) is inconsistent with the number of post-burn-in samples calculated in footnote 1 (123,368). The explanation on page 3 ("additional getdist effective-sample weight-based thinning") is jargon-heavy and confusing for the reader.
*   **Required Fix:** Reconcile the numbers or provide a much clearer, simpler explanation for the discrepancy. For reproducibility, the exact procedure used to generate the plot from the chains should be unambiguous.

**P1B-m3**
*   **Section:** Acknowledgments
*   **Page:** 8
*   **Problem:** The acknowledgment of "Claude (Anthropic) as an AI research assistant" is highly unconventional for a PRD publication. While transparency is commendable, this raises questions about journal policy on AI contributions.
*   **Required Fix:** The authors should consult with the PRD editors to ensure this acknowledgment complies with the journal's current policies. The statement that "All scientific claims... were independently verified by the author" is a necessary and good addition but may not be sufficient.

---
### NIT (Nitpicks / Typos)

**P1B-N1**
*   **Section:** III, Physics interpretation
*   **Page:** 3
*   **Problem:** The sentence "An earlier count erroneously quoted '98.6% quintom-B' weight" is phrased like an internal comment or erratum.
*   **Required Fix:** Rephrase to be more formal, e.g., "Contrary to a preliminary estimate, the converged chain shows..."

**P1B-N2**
*   **Section:** V.B and Table II
*   **Page:** 6, 4
*   **Problem:** The uncertainty on `w0` is given as `±0.044` in the text on page 6 but as `±0.0436` in Table II on page 4.
*   **Required Fix:** Use consistent rounding throughout the manuscript.

**P1B-N3**
*   **Section:** VI
*   **Page:** 7
*   **Problem:** In Equation (3), the multiplication symbol `x` is used (`αEM x 8`).
*   **Required Fix:** Use standard mathematical notation (e.g., a dot, or simply juxtapose with the variable `C_aγ` which seems to be what was intended).

**P1B-N4**
*   **Section:** References
*   **Page:** 10
*   **Problem:** Reference [20] has redundant numbering: "Journal of Cosmology and Astroparticle Physics 05 (057), 057".
*   **Required Fix:** Correct the reference to the standard format, e.g., "JCAP 05 (2020) 057".

---
## Summary recommendation
**MAJOR REVISIONS**

The paper presents several competent technical analyses. However, it is undermined by significant flaws, including a mathematically incorrect key result (P1B-E1), an unsubstantiated claim of model preference (P1B-E2), misleading framing of the ALP analysis (P1B-M1), and inappropriate content (P1B-E3). The paper cannot be accepted without addressing these essential and major points. If the authors can correct the `w_pivot` calculation, provide the required Bayesian evidence for their `w0-wa` claim (or appropriately downgrade it), and reframe the ALP analysis with full transparency, the manuscript could become a valuable contribution.