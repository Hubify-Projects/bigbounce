# P3 R24conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.81.pdf` md5=aa791276 pages=24
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 207.2s

---

**Referee Report on "Spectrally Unusual Sources at Scale..."**

**To the editor of Physical Review D,**

I have reviewed the manuscript "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and Native-Trained Novelty Fractions from 37.3 Million Sources and Map Patches" by Houston Golden. The paper presents a very large-scale anomaly detection campaign across seven major astronomical surveys. The methodology is thorough, the analysis is rigorous, and the authors are commendably transparent about the limitations and validation status of their results. The work provides a valuable catalog to the community and presents interesting, albeit preliminary, applications to cosmology.

The paper is of high quality and potentially suitable for publication in Physical Review D. However, I have identified several issues that require revision before the manuscript can be accepted. My primary concerns relate to the presentation of the main cosmological forecast in the abstract, which could be misinterpreted, and the justification for including results from surveys that failed primary validation gates in the main scientific catalog.

Below is a detailed list of findings.

---

### Detailed Findings

#### ESSENTIAL

*   **P3-E1 | Section: Abstract | Page: 1**
    *   **Problem:** The abstract leads with a biased central-value forecast for the constraint on primordial non-Gaussianity: "a central forecast σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] (9.4% improvement consistent with no improvement at <1σ...)". The main text (Section V.b, p. 14) correctly and transparently explains that the noisy measurement of the bias parameter `a` introduces a "squaring noise bias" and that the properly de-biased result shows *no improvement* over the single-tracer baseline. The abstract's presentation, while technically qualified, is misleading as it highlights a non-robust central value. For a journal with PRD's standards of rigor, the abstract must reflect the most robust conclusion from the analysis.
    *   **Required Fix:** The abstract must be revised to lead with the de-biased null result for the fNL constraint. The biased central-value forecast and its corresponding "9.4% improvement" should be either removed from the abstract or heavily demoted and explicitly described as a biased estimate, with the de-biased null result stated as the primary finding.

#### MAJOR

*   **P3-M1 | Section: Abstract | Page: 1**
    *   **Problem:** The abstract describes the "LAMOST exploratory tier (~113,000 objects retained as a methodological lesson... injection-recovery gate FAIL)". This number corresponds to a top-1% slice of the *native-retrained* data (Table I, footnote ♢), not the initial cross-transfer result (which was 44,075 objects). The phrasing could be misinterpreted as implying the 113k objects are the direct result of the failed cross-transfer, which is not the case.
    *   **Required Fix:** Clarify the origin of the 113,000 LAMOST objects in the abstract. For example: "...which excludes the LAMOST exploratory tier (a top-1% slice of ~113,000 objects from the native-retrained data, retained as a methodological lesson...)."

*   **P3-M2 | Section: V.A | Page: 14**
    *   **Problem:** The paper reports a Savage-Dickey Bayes factor of BMB/SMBHB = 7.14×10³, described as "decisive" evidence for the matter-bounce model over the supermassive black hole binary model as the source of the NANOGrav signal. While the calculation is documented, it relies on a public Kernel Density Estimate (KDE) of the NANOGrav posterior, not a full analysis of the pulsar timing data. The text notes this is an approximation. A "decisive" claim from an approximate likelihood analysis is too strong.
    *   **Required Fix:** Temper the language surrounding the Bayes factor. The authors should explicitly state that this "decisive" preference is conditional on the accuracy of the KDE likelihood product and the specific choice of priors. The potential impact of inter-bin correlations not captured by the free-spectrum product should be mentioned as a caveat.

*   **P3-M3 | Section: III.E, III.G | Pages: 7, 9**
    *   **Problem:** The eROSITA and Gaia anomaly sets are included in the final unique object count, despite failing the pre-defined injection-recovery validation gate (eROSITA: 1.2% recovery; Gaia: 5.2% recovery, both vs. 50% threshold). The paper is transparent about this failure but justifies inclusion based on secondary metrics (e.g., high cross-validation stability for eROSITA) or by labeling the set "exploratory" (Gaia). For a catalog of this importance, the criteria for inclusion should be uniformly applied. Including sets that fail a primary validation gate in the main headline count weakens the overall robustness of the catalog.
    *   **Required Fix:** The authors must provide a much stronger justification for including the eROSITA and Gaia anomalies in the primary catalog. Alternatively, and preferably, these sources should be moved to a separate appendix or an "exploratory" tier, and the headline number of 378,280 should be adjusted accordingly, with the main catalog containing only sources from surveys that passed all validation gates.

#### MINOR

*   **P3-m1 | Section: Table I | Page: 8**
    *   **Problem:** The table includes a summary row "Total (cross-transfer, ACT-incl.)" with 319,443 anomalies. The caption correctly identifies this as a "before/after diagnostic," but its prominent placement directly above the final "Path-C unique" result could lead to confusion and incorrect citation.
    *   **Required Fix:** To prevent confusion, I recommend moving the "cross-transfer baseline" row out of the main results block, perhaps to a footnote or a separate table in an appendix dedicated to methodological diagnostics.

*   **P3-m2 | Section: V.b | Page: 14**
    *   **Problem:** The paper defines two distinct sets of objects with the "gold" moniker: the 83-object "gold-tier" visualization set from Figure 1 and the 116-object "GOLD" QSO-candidate confidence tier used in the fNL forecast. While the text clearly distinguishes them, the overlapping terminology is a source of potential confusion for the reader.
    *   **Required Fix:** Rename one of the tiers to avoid ambiguity. For example, the visualization set could be called the "Display Sample" or "Visual Gold Sample," while the forecast set remains the "GOLD Confidence Tier."

*   **P3-m3 | Section: II.B, Eq. (1) | Page: 2**
    *   **Problem:** The notation in Equation (1) for Mean-Squared Error could be slightly clearer. The text below the equation defines `x_hat = BIGAE(x)`.
    *   **Required Fix:** For immediate clarity, write the reconstruction directly in the equation, e.g., `MSE(x) = (1/N) * Σ(x_i - BIGAE(x)_i)²`.

*   **P3-m4 | Section: IV.C | Page: 11**
    *   **Problem:** The text mentions that a more sophisticated "Budavári-Szalay probabilistic cross-match" is a "refinement for a future catalog revision," implying the current fixed-radius method is a simplification. The defense of the 5" radius is good, but the sentence leaves an open question.
    *   **Required Fix:** Briefly state why the probabilistic cross-match was not implemented in the current work (e.g., lack of uniform error ellipse information across all seven surveys, computational complexity) to provide closure for the reader.

#### NIT

*   **P3-N1 | Section: Title Block | Page: 1**
    *   **Problem:** The paper is dated "(Dated: June 2026)". This is likely a typo.
    *   **Required Fix:** Correct the date to the current year of submission.

*   **P3-N2 | Section: I | Page: 1**
    *   **Problem:** The author's contact email is a non-academic domain (`houston@hubify.com`). This is unusual but not a formal error.
    *   **Required Fix:** No fix required, just an observation.

---

### Summary recommendation

**MAJOR REVISIONS**

This is a landmark effort in astronomical anomaly detection, impressive in both its scale and its methodological rigor. The "Path-C" native-retraining protocol is well-motivated and convincingly demonstrated to be superior to a naive cross-transfer approach. The paper's honest and detailed treatment of validation, limitations, and potential biases is a model for future work in this area.

However, the issues raised, particularly the potentially misleading presentation of the fNL constraint in the abstract (P3-E1) and the inclusion of data from validation-failed surveys in the headline results (P3-M3), are significant. These points must be addressed to meet the high standards of Physical Review D. Once these and the other, more minor, issues are satisfactorily resolved, the manuscript will represent a major contribution to the field.