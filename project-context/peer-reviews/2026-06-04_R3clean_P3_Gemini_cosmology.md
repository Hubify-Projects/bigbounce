# P3 2026-06-04_R3clean — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 84.9s

---

## Referee Report on "Spectrally Unusual Sources at Scale..." (P3)

This paper presents a large-scale anomaly detection campaign across seven major astronomical surveys, resulting in a catalog of 378,280 unique anomalies. The work is notable for its scale, its multi-wavelength and multi-instrument approach, and its transparent handling of methodological challenges. A core contribution is the "Path-C rebuild" protocol, which uses per-survey native retraining of the autoencoder model to overcome significant cross-transfer artifacts (domain shift issues), such as a 98% contamination in LAMOST and a ~6500x rate inflation in SDSS. The paper further presents two cosmological applications of the resulting catalog: a multi-tracer forecast for primordial non-Gaussianity (fNL) and a consistency check of Pulsar Timing Array data with a matter-bounce gravitational-wave background.

The scientific content of the paper is substantial. The methodology for building and validating the catalog is, for the most part, rigorous and well-documented. The authors are commendably transparent about the limitations of their work, including the failure of some validation gates and the careful distinction between database-coverage metrics and genuine novelty. The cosmological analyses are sophisticated, particularly in the handling of statistical uncertainties in the fNL forecast and the use of Bayesian model comparison for the PTA analysis.

However, the manuscript in its current form has serious structural and stylistic issues that prevent its acceptance. The paper is excessively long for a single publication, and a significant portion of the text is written in an informal, "lab-notebook" style that is inappropriate for a peer-reviewed journal. The revisions required are major.

### ESSENTIAL Revisions

**P3-E1: Paper Length and Scope**
- **Section:** Entire manuscript
- **Problem:** At 50 pages, the paper is excessively long for a Physical Review D article, even for a significant catalog/methods paper. It attempts to combine a detailed description of a massive data product spanning seven surveys with two separate, non-trivial cosmological applications. This over-broad scope makes the paper unwieldy and dilutes the impact of its core contributions.
- **Fix:** The authors must significantly reduce the length of the paper. The recommended maximum length is 25 pages (main text + references). This can be achieved by:
    1.  Restructuring the paper into a primary methods/catalog paper. The cosmological applications (§V, §VIA) should be heavily condensed, presenting only the headline results and deferring detailed derivations and discussions to separate, dedicated papers. The current level of detail on the fNL forecast and PTA analysis is sufficient for standalone publications.
    2.  Moving extensive image galleries (e.g., Figs. 14-22) to a public data repository linked in the text, retaining only a single representative figure (like Fig. 13) in the main paper or appendix.
    3.  Streamlining the text throughout, removing repetitive explanations and integrating the content of the problematic "Residual Caveats" section (§VID) into the main narrative (see P3-E2).

**P3-E2: Unprofessional Prose and Manuscript Structure**
- **Section:** §VID (Path-C Rebuild Residual Caveats, pp. 27-29), and other instances throughout.
- **Problem:** The manuscript contains a large amount of text that reads like an internal audit log, a changelog, or a direct response to a previous review, rather than a formal scientific paper. This is most egregious in §VID, which is structured as a list of "caveats" and their "resolutions." This section contains numerous unprofessional and inappropriate phrases.
    - Examples: "this deferral is closed," "The paper's accuracy-floor exit-criterion for the §pathc_caveats block is satisfied," "a prior version quoted the envelope as [2.04,3.40]...which was hallucinated arithmetic," "This deferral was based on a misread of Table I," "The held-out-only language in earlier drafts...was misleading and has been removed."
- **Fix:** This is an essential revision. The entire "Residual Caveats" section (§VID) must be removed. The valuable scientific content within it (e.g., the detailed Fisher analysis, the GR projection check, the Savage-Dickey calculation, the Jaccard stability arithmetic) must be rewritten in formal scientific prose and integrated into the appropriate sections of the main manuscript. For example, the detailed Fisher positivity analysis belongs in §V, the Jaccard stability clarification belongs in §IIB, and the GR projection check should be discussed within the main fNL forecast section. The paper must be presented as a finished scientific work, not a log of its own construction.

### MAJOR Revisions

**P3-M1: "In Flight" and Colloquial Language**
- **Section:** §IIICα (p. 12), §IIIDa (p. 15)
- **Problem:** The paper uses the phrase "Path-C native-retrain in flight" to describe the results of the native retraining for SDSS and LAMOST. This suggests the analysis is ongoing, which is confusing for a paper reporting final results. The results should be presented in the past tense.
- **Fix:** Rewrite these sections to describe the completed analysis and its results. For example, instead of "Re-scoring...has now completed," use "Re-scoring...was completed." Remove all instances of "in flight" and similar colloquialisms.

**P3-M2: GR Projection Effects in fNL Forecast**
- **Section:** §V (p. 23) and §VID(e) (p. 27)
- **Problem:** The main text (§V) states that `O(H^2/k^2)` general-relativistic projection corrections are omitted from the theoretical template, correctly identifying them as a potential theoretical systematic. The check that justifies this omission is buried in the "Residual Caveats" section (§VID(e)). For a paper submitted to a theoretical physics journal, this check is a crucial part of the main analysis.
- **Fix:** Integrate the results of the GR projection check from §VID(e) into the main cosmological applications section (§V). The main text should state that the effect was checked and found to be negligible (`<0.02%` on `σ(fNL)`) for the kinematic range considered in the forecast, thereby justifying its omission from the final template.

### MINOR Revisions

**P3-m1: Clarification of fNL Forecast Status**
- **Section:** Abstract, §V, §VII
- **Problem:** The paper presents two fNL forecasts: one for the full sample and one for a high-confidence "Gold+Silver" subset. The full-sample result (`αjk = 0.19 ± 0.65`) is consistent with no improvement in `σ(fNL)`. The high-confidence result has a much larger central value for `α` but also a much larger error bar, also making it consistent with no improvement. The paper correctly identifies the full-sample result as the "load-bearing headline."
- **Fix:** Ensure that the abstract and conclusions maintain the clear and cautious framing present in the main text: the current data provides a central-value forecast for improvement but does not constitute a statistically significant detection of a non-zero bias enhancement (`α`) or a guaranteed improvement to `σ(fNL)`. The phrasing "pending higher-S/N follow-up" is appropriate and should be retained.

**P3-m2: PTA Analysis Framing**
- **Section:** §VA, §VII
- **Problem:** The PTA analysis provides "decisive" Bayesian evidence for a matter-bounce spectral index over an SMBHB-only model. The paper is careful to state this does not constitute evidence *for* bounce cosmology, but rather evidence *against* a specific alternative at the sensitivity of the current data.
- **Fix:** This framing is good, but given the potential for misinterpretation, it would be beneficial to add a sentence explicitly stating that other physical models (e.g., inflation with a blue-tilted tensor spectrum, cosmic strings) could also be consistent with the data and are not tested here. This reinforces the limited scope of the model comparison being performed.

### NITs

**P3-N1: Date Format**
- **Section:** Title page
- **Problem:** The date is given as "June 4, 2026." While this may be a placeholder, future dates are unconventional.
- **Fix:** Use the date of the current submission.

## Summary recommendation

**MAJOR REVISIONS**

The paper presents a scientifically valuable and large-scale dataset, accompanied by sophisticated validation and analysis. The core methodological contribution—demonstrating the necessity and success of native retraining to correct for severe domain-shift artifacts—is an important lesson for the field of unsupervised anomaly detection in astronomy. The cosmological applications are timely and handled with appropriate theoretical care.

However, the manuscript is not in a publishable state. Its excessive length and, most critically, the inclusion of extensive informal, colloquial, and "internal-log" style prose render it unprofessional and difficult to read. The "Residual Caveats" section, in particular, must be completely refactored, with its contents rewritten and integrated into the main scientific narrative. The work is strong enough to warrant publication after these significant structural and stylistic issues are addressed. I recommend that the paper be returned to the authors for major revisions to bring it to the professional standard required by Physical Review D.