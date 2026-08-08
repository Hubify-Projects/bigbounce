# P3 INT-EXTDB2check — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=5bf37274 pages=30
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (2952 chars)
**Wall time**: 119.8s

---

## Referee Report: "Spectrally Unusual Sources at Scale..." by Houston Golden

**Report ID:** PRD-2026-06-P3-INT-EXTDB2check

This paper presents a large-scale anomaly detection catalog, the "Path-C" catalog, derived from 37.3 million sources across seven major astronomical surveys using an autoencoder framework. The work is ambitious in scope, combining spectroscopic, photometric, and CMB data. The author has clearly undertaken a significant amount of work, and the paper is commendably transparent about many of its methodological limitations, pipeline choices, and provenance issues.

However, the paper in its current form suffers from several significant issues, primarily related to the framing and presentation of its primary results. The abstract and headline numbers are misleading regarding the scientific impact and scale of the catalog when compared to prior work on a like-for-like basis. The presentation of the cosmological forecasts is also confusing and frames a null result in an overly optimistic light. These issues require substantial revision before the paper can be considered for publication in Physical Review D.

Below is a detailed list of required revisions.

---
### ESSENTIAL Revisions

**P3-E1: Misleading framing of catalog scale and novelty (Abstract, §III A, §VII)**
*   **Section/Page:** Abstract (p. 1), §III A (p. 6), §VII Conclusions (p. 22).
*   **Problem:** The abstract and title lead with enormous numbers (269,317 / 378,280 anomalies) and claim the catalog is "~141× the size of the largest prior single-survey anomaly catalog [11]". However, the paper itself later reveals in §III A that a like-for-like comparison restricted to science-class targets yields only 2,468 DESI anomalies, which is "~0.9× the benchmark's 2,685". The paper explicitly states that "~98.7% of [DESI] clusters fall on sky-fiber or filler spectra". This means the headline number is almost entirely dominated by non-science targets, and the claimed 141x (or 73x for DESI-only) increase is an artifact of comparing a full-instrument-stream scan to a science-target-only scan. This is a critical flaw in the presentation. The abstract buries this crucial context in a parenthetical, which is insufficient.
*   **Required Fix:** The abstract, introduction, and conclusions must be rewritten to lead with the scientifically meaningful, like-for-like comparison. The fact that the catalog is dominated by non-science targets must be stated upfront, not as a secondary detail. The 141x/73x figures should be removed from their prominent positions or heavily caveated at every mention as not being a science-target comparison. The paper's primary contribution should be framed as a comprehensive scan of the *full data stream*, with the distinction from a science-target scan made central to the narrative.

**P3-E2: Inconsistent and confusing presentation of the f_NL Fisher forecast (Abstract, §V, Appendix C, Fig. 9)**
*   **Section/Page:** Abstract (p. 1), §V (p. 17), Fig. 9 (p. 19).
*   **Problem:** The presentation of the f_NL forecast is convoluted and inconsistent.
    1.  The primary result from the data is a bias measurement `ajk = 0.19 ± 0.65`, which is consistent with zero. The de-biased analysis correctly concludes "no multi-tracer improvement at current S/N".
    2.  Despite this, the abstract highlights a "central 9.4% improvement" and a central forecast of σ(fNL) = 8.14. The body correctly identifies this as an optimistic, noise-biased forecast, but the abstract's framing is misleading.
    3.  Figure 9, which illustrates the multi-tracer improvement, is based on a *fixed* bias prior `a = 0.15`. However, the caption and the main text of §V state that the paper's primary forecast uses the *empirically measured* (and uncertain) bias, which yields no improvement. The figure is therefore illustrating a hypothetical scenario, not the paper's main result. This is a direct contradiction.
*   **Required Fix:**
    1.  The abstract must be rewritten to state clearly that the empirical analysis is consistent with **no improvement** in the f_NL constraint. The 9.4% figure must be explicitly described as a noise-biased, central-value-only forecast pending a higher S/N bias measurement, not as a summary of the current constraint.
    2.  The caption of Figure 9 must be rewritten to state unambiguously that it shows a reference forecast for a *fixed, hypothetical bias prior (a=0.15)* and does **not** represent the primary, empirically-derived result of the paper, which is consistent with zero improvement. The title of the figure should also reflect this.

---
### MAJOR Revisions

**P3-M1: Mixing of validated and exploratory tiers in headline numbers (Abstract, Title)**
*   **Section/Page:** Abstract (p. 1), Title.
*   **Problem:** The headline numbers (269,317 recommended, 378,280 total) include components (Gaia and eROSITA) that the paper itself states "fail injection-recovery validation" and are an "explicit exploratory addendum". While this is disclosed, including them in the main count blurs the line between validated and unvalidated results. A PRD paper should lead with its most robust, validated findings.
*   **Required Fix:** The title and abstract should lead with the "validated catalog-grade" number (≥ 268,519). The full count including the exploratory tiers can be mentioned subsequently, but the distinction must be made clearer from the outset. For example: "A Multi-Survey Catalog of ≥268,519 Validated Anomalies (378,280 Total including Exploratory Tiers)...".

**P3-M2: Convoluted presentation of f_NL forecast envelope (Abstract, §V)**
*   **Section/Page:** Abstract (p. 1), §V (p. 17).
*   **Problem:** The paper presents the final f_NL constraint as a 1σ "envelope" [3.92, 8.98]. The text explains this is the propagated image of the 1σ uncertainty on the bias parameter `a`, and not a 68% credible interval on σ(fNL). This is a non-standard and potentially confusing way to report a constraint. The key physical result is that the uncertainty on the bias `a` is too large to claim any improvement over the single-tracer baseline.
*   **Required Fix:** The abstract and §V should state the conclusion more directly: "The uncertainty in the measured tracer bias (ajk = 0.19 ± 0.65) is too large to confirm any improvement from the multi-tracer technique. The constraint remains consistent with the single-tracer baseline of σ(fNL) = 8.98." The "envelope" can be presented as a supplementary diagnostic showing the range of possible constraints consistent with the current data, but it should not be framed as the primary result itself.

**P3-M3: Understated impact of full-sample scaler fitting (Method, §II B)**
*   **Section/Page:** §II B (p. 3).
*   **Problem:** The paper discloses that for tabular surveys, feature scalers were fit on the full data sample, not just the training set. This is a form of data leakage. A robustness check for eROSITA shows a top-298 membership churn of 15-17%, which is a non-trivial effect. The paper's conclusion that "per-survey rates and within-survey rankings are robust to the scaler choice" seems too strong given this level of churn in the extreme tail.
*   **Required Fix:** The language describing the impact of this choice should be softened. The 15-17% churn should be described as a significant, quantified uncertainty on extreme-tail membership. The recommendation that "Future pipelines should fit normalization constants strictly on the training split" should be elevated from a parenthetical to a main conclusion of this methodological analysis.

---
### MINOR Revisions

*(No findings classified as MINOR in this review.)*

---
### NITs (Cosmetic)

**P3-N1: Future date in byline (p. 1)**
*   **Problem:** The paper is dated "June 28, 2026".
*   **Required Fix:** Correct the date to the actual submission date.

**P3-N2: Non-standard author contact (p. 2)**
*   **Problem:** The author contact is a corporate-style email address (`houston@hubify.com`). While not forbidden, it is unusual for an academic publication.
*   **Required Fix:** Consider providing a more standard academic or persistent contact email if available.

**P3-N3: Confusing wording in Figure 2 caption (p. 7)**
*   **Problem:** The sentence "the canonical Path-C unique count of 378,280 is not a deduplication of this baseline" is awkwardly phrased. The phrase "deduplication only ever reduces its input" is a tautology.
*   **Required Fix:** Rephrase for clarity. E.g., "The canonical Path-C unique count of 378,280 is derived from the per-survey native-retrained catalogs, not from a deduplication of the 319,443 cross-transfer detections shown here."

**P3-N4: Inconsistent terminology for anomaly score (p. 4)**
*   **Problem:** The paper uses "standardized ('z-scored' in the statistical sense) reconstruction residual" to define the score S. It then adds a note to avoid calling S 'z' to prevent confusion with redshift. While the intent is good, the repeated parenthetical is cumbersome.
*   **Required Fix:** Define it clearly once in §II B and then simply refer to it as the "standardized anomaly score S" throughout.

---
## Summary recommendation

**MAJOR REVISIONS**

This paper represents a substantial effort to produce a large and methodologically interesting anomaly catalog. The author's transparency regarding difficult issues like the eROSITA score irreproducibility, the LAMOST training bias, and various residual caveats is a major strength of the work.

However, the paper cannot be accepted in its current form. The framing of the catalog's scale in the abstract and conclusions is fundamentally misleading, comparing a full-instrument-stream scan to a science-target-only scan without making this crucial context clear upfront. This exaggerates the paper's contribution to science-ready anomaly discovery by two orders of magnitude. Furthermore, the presentation of the cosmological f_NL forecast is confusing and obscures the null nature of the result.

These are not superficial issues; they go to the heart of the paper's claimed contributions. A significant revision of the abstract, introduction, and conclusions is required to present the results in a clear, accurate, and appropriately scoped manner that meets the standards of Physical Review D. If the authors can successfully reframe the paper around its genuine, well-supported findings, it could become a valuable contribution to the literature.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from the "fresh eyes" review.

---
### ADDITIONAL FINDINGS (Second Pass)

**P3-M4: Unaddressed provenance issue for Gaia features (§II B, Appendix A)**
*   **Section/Page:** §II B (p. 3), Appendix A (p. 24).
*   **Problem:** The paper discloses that the exact 20-feature preprocessing script for the published Gaia run was not recovered from backups and that the specification is "lineage-inferred" from a later, 21-feature successor script. This is a significant reproducibility and provenance issue. While the Gaia tier is already flagged as "exploratory" for failing injection recovery, this adds a second, independent reason for its results to be treated with caution. The implications of this are understated.
*   **Required Fix:** The main text (e.g., in §III G or the conclusion) should explicitly discuss the impact of this missing provenance. Does this irreproducibility in the feature generation step cast doubt on the stability of the anomaly rankings themselves for the Gaia component? The paper should recommend that the Gaia results not be used for any quantitative analysis until this can be rectified in a future data release. The abstract's description of the Gaia component should also reflect this additional uncertainty.

**P3-m1: Typographical and Stale Cross-References in Abstract and Body**
*   **Section/Page:** Abstract (p. 1), Conclusion (p. 23).
*   **Problem:** The paper contains several incorrect internal cross-references, which hinders navigation and verification of claims.
    1.  The abstract refers to `§VIE` for the size benchmark. This section does not exist. The reference should likely be to §I or §VII.
    2.  The abstract refers to `Table V` for "per-survey validity flags". Table V is titled "Path-C residual caveats" and does not contain this information. The validity flags are discussed in the conclusion (§VII) and throughout §III.
    3.  The conclusion (p. 23) refers to `§IID` to justify the `≥` sign in the validated catalog count. The justification is described in the abstract and §I, whereas §IID details the general rebuild methodology.
*   **Required Fix:** All internal cross-references must be checked and corrected to point to the appropriate sections, tables, or figures.

**P3-N5: Ambiguous sentence structure in Abstract**
*   **Section/Page:** Abstract (p. 1).
*   **Problem:** The sentence "the recommended point-source subset is 269,117 unique entries (validated catalog-grade ≥ 268,319 point-source once the Gaia+eROSITA exploratory components are also removed)" is grammatically ambiguous and could be misread as equating the "recommended" tier with the "validated catalog-grade" tier.
*   **Required Fix:** Rephrase for clarity to make the subset relationship explicit. For example: "...the recommended point-source subset of 269,117 unique entries contains a validated catalog-grade subset of ≥ 268,319 entries (the remainder being exploratory)..."