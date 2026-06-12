# P3 R35conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.99.pdf` md5=1e97ec59 pages=28
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 161.6s

---

## Referee Report: Spectrally Unusual Sources at Scale...

**Report ID:** PRD-P3-R35conf-Ref1

## Summary of the Paper

This paper presents a large-scale anomaly detection campaign across seven astronomical surveys (DESI, SDSS, LAMOST, eROSITA, Planck, Gaia, NEOWISE), using a fully-connected autoencoder framework called BIGAE. The primary product is a catalog of 378,280 unique anomalous sources or sky patches. The authors detail a "Path-C" methodology, which emphasizes native retraining of the autoencoder for each survey to overcome cross-transfer artifacts identified in an initial scan. The paper highlights the methodological lesson from a ~98% contamination rate in the LAMOST cross-transfer sample. It provides a genuine novelty fraction of ~17.8% for the top-1000 DESI anomalies against a deep 18-catalog cross-match. Finally, it explores cosmological applications, presenting a multi-tracer forecast for primordial non-Gaussianity (fNL) and a consistency check of the NANOGrav 15-yr result with matter-bounce cosmology predictions.

## General Comments

The paper represents a monumental effort in data processing and analysis, and its scale is impressive. The transparency regarding methodological failures (e.g., the LAMOST training bias, the ACT cross-transfer failure, the eROSITA score irreproducibility) is commendable and provides valuable lessons for the community. The rigorous treatment of the fNL forecast, particularly the handling of the noisy bias measurement and the resulting de-biased null result, meets the high standards of theoretical cosmology.

However, the paper suffers from several significant issues that preclude its publication in the present form. These include the presence of internal version-history language, a critical irreproducibility issue with the eROSITA tier, unprincipled selection criteria for the SDSS tier, and a lack of clarity in the presentation of key results, particularly in the abstract and summary tables. The work is a hybrid catalog/methods/cosmology paper, and while ambitious, this sometimes leads to a loss of focus and a convoluted narrative. The following detailed points must be addressed.

---
## Detailed Findings

### ESSENTIAL Revisions

**P3-E1: Internal version-history language in abstract**
-   **Section/Page:** Abstract, Page 1
-   **Problem:** The abstract contains the phrase: `an earlier draft quoted 264,938/264,738 from headline-minus-LAMOST subtraction arithmetic, which double-removes the 4,379 LAMOST detections that merge into catalog-grade clusters at 5")`. This is internal bookkeeping and has no place in a published scientific paper. It undermines the finality and authority of the work.
-   **Fix:** Remove this entire parenthetical clause. The abstract should only state the final, definitive numbers and methodology.

**P3-E2: Critical irreproducibility of the eROSITA anomaly score**
-   **Section/Page:** §IIIE, Page 10; Table IV, Page 11
-   **Problem:** The paper states that the eROSITA anomaly score axis is irreproducible. `this threshold axis could not be reconciled with the canonical S of Eq. (2)`, `the production Table IV scores are non-monotone in the committed raw artifact (Spearman p = -0.10 across the top five)`, and the Table IV caption states `that score axis is irreproducible from any committed artifact`. This means the eROSITA "anomaly catalog" is merely a static list of 298 objects, not a scored sample. This severely limits its scientific utility for any analysis that requires a score or rank (e.g., score-weighted stacking, threshold variation, comparison with other anomaly detectors).
-   **Fix:** This is a fundamental flaw. While the authors are transparent, this limitation must be stated more forcefully in the abstract and conclusions. The abstract currently says `eROSITA tier released as a n = 298 membership list only`, which is too subtle. It should explicitly state that the score axis is not reproducible. The authors must also add a stronger caveat in the main discussion about the limited utility of this portion of the catalog.

**P3-E3: Internal version-history language in body**
-   **Section/Page:** §IV B, Page 13
-   **Problem:** The text contains the sentence: `(An earlier draft quoted 38,330 pixels with χ²/dof = 3.76; that artifact's pixel-selection and variance model could not be recovered from the committed analysis tree, and the figure is withdrawn in favor of the reproducible recompute above.)`. As with P3-E1, this is inappropriate internal-review commentary.
-   **Fix:** Delete this entire parenthetical sentence. Present only the final, reproducible result.

### MAJOR Revisions

**P3-M1: Confusing "gold tier" definitions**
-   **Section/Page:** §II A, Page 2, Figure 1 Caption
-   **Problem:** The caption for Figure 1 refers to "83 gold-tier anomalies" which are a "ranked visual-display set". It then distinguishes this from the "116-object GOLD QSO-candidate confidence tier of §V". Using "gold" for two different, non-overlapping sets of objects is highly confusing for the reader.
-   **Fix:** Rename one of the sets. For example, the 83-object set could be called the "Exemplar Set" or "Visual-Inspection Set" to avoid ambiguity with the quantitative "GOLD" tier used in the cosmological analysis. This change must be propagated throughout the manuscript.

**P3-M2: Data leakage in feature scaler fitting**
-   **Section/Page:** §II B a, Page 3
-   **Problem:** The authors state: `Because the scalers are fit on the full sample rather than the training split alone, a small amount of validation-set (including tail) information enters the normalization constants`. This is a form of data leakage and violates best practices in machine learning. The authors perform a robustness check for eROSITA and find `~15-17% extreme-tail churn`, which is a significant level of instability. Their conclusion that "rankings are robust" while "memberships carry quantified ~15% churn" is contradictory. A 15% change in the top members means the ranking is *not* robust at the tail, which is precisely where anomaly detection operates.
-   **Fix:** The authors must rephrase their conclusion to accurately reflect the quantified instability. They should acknowledge this as a significant limitation for the Gaia and NEOWISE tiers where the check was not performed. The abstract and conclusions should carry a caveat about this methodological weakness. The recommendation that "Future pipelines should fit normalization constants strictly on the training split" should be elevated to a key methodological takeaway.

**P3-M3: Confusing structure of Table I**
-   **Section/Page:** Table I, Page 7
-   **Problem:** Table I presents both the initial (flawed) "cross-transfer" counts and is used to construct the final "Path-C" counts via a complex set of footnotes. The `Nanom` column shows cross-transfer values for most surveys, but the native value for DESI. The final native-retrained counts for SDSS and LAMOST are only given in a footnote. This is convoluted and prone to misinterpretation.
-   **Fix:** Restructure the presentation. A clearer approach would be two separate, smaller tables: one for the "Before: Cross-Transfer Baseline" and one for the "After: Path-C Native-Retrained Results". This would make the paper's core methodological improvement much easier to understand.

**P3-M4: Prominence of non-science-target contamination**
-   **Section/Page:** §III A, Page 5-6; Table II, Page 8
-   **Problem:** The paper finds that `~98.7% of DESI anomaly clusters fall on sky-fiber, secondary-target, or filler spectra`. This is a crucial result, as it implies the vast majority of the largest anomaly sample are not associated with primary science targets. While this is detailed in the body, its significance is understated in the abstract and conclusions. The abstract's initial presentation of the 195,829 DESI anomalies and the "73x increase" is misleading without this immediate context.
-   **Fix:** The abstract must be revised to state this finding upfront. For example, after giving the 195,829 number, it should immediately clarify that ~99% of these are not on primary science targets, and that the like-for-like science-target anomaly count is only ~0.9x the previous benchmark. This provides a more honest and accurate summary of the DESI catalog's nature.

**P3-M5: Unprincipled SDSS "continuity slice" selection**
-   **Section/Page:** Table I footnote ♡, Page 7
-   **Problem:** The SDSS anomaly set is not a simple significance-based cut. It is a `fixed-size continuity slice sized to equal the cross-transfer count`. This is an ad-hoc selection criterion motivated by internal consistency rather than a principled statistical threshold. It makes the physical interpretation of the SDSS anomaly rate (3.38%) and the comparison with other surveys problematic.
-   **Fix:** The authors must provide a stronger justification for this choice in the main text. They should also discuss how this ad-hoc selection impacts the interpretation of the SDSS results and any cross-survey comparisons involving SDSS. This limitation should be explicitly mentioned in the Discussion/Limitations section.

**P3-M6: Convoluted presentation of DESI numbers in abstract**
-   **Section/Page:** Abstract, Page 1
-   **Problem:** The abstract's presentation of the DESI catalog size is confusing. It gives the 141x, 100x, and 73x numbers, then immediately qualifies the 73x with the 0.9x recount. This sequence of claim and immediate, complex retraction is hard to follow.
-   **Fix:** Restructure the abstract for clarity. Start with the total unique point-source count (378,080). Then, when introducing the DESI component (195,829), immediately provide the crucial context: state that this is a full-spectrum scan and that when restricted to primary science targets for a like-for-like comparison, the count is 2,468 (~0.9x the benchmark). This is a more direct and less misleading narrative.

### MINOR Revisions

**P3-m1: Prominence of superseded figure**
-   **Section/Page:** Figure 2, Page 6
-   **Problem:** Figure 2 shows the "Cross-transfer baseline map," which the caption and text repeatedly state is "superseded by the Path-C native catalog." While useful as a diagnostic, giving a full-width figure to a superseded, non-science result is questionable.
-   **Fix:** Consider moving this figure to an appendix on methodology, or combining it into a multi-panel figure with the final Path-C spatial distribution to create a direct "before and after" comparison.

**P3-m2: Misleading description of NEOWISE injection test**
-   **Section/Page:** §III H, Page 12; Figure 10, Page 21
-   **Problem:** The text reports `Mask injection-recovery: 1000/1000 = 100% (gate PASS)`. However, it clarifies that this test "passes by construction" and is a "masking-geometry sanity check... not a detector-sensitivity test". The headline "3 PASS" in Figure 10's caption is therefore misleading, as one of the passes is not a true recovery test.
-   **Fix:** The text and Figure 10 caption must be more explicit. The headline should be "2 PASS + 1 Geometry-QA" or similar. The abstract's summary of injection-recovery gates should also reflect this distinction.

**P3-m3: Placeholder DOI**
-   **Section/Page:** Acknowledgments / Data availability, Page 22
-   **Problem:** The data availability section contains the placeholder: `A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission)`.
-   **Fix:** This must be replaced with the actual DOI before publication.

### NITs

**P3-N1: Typo in fNL constraint summary**
-   **Section/Page:** Abstract, Page 1
-   **Problem:** The text reads `central forecast σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] (the envelope - not the convex central value - is the appropriate summary of the present constraint;`. The trailing parenthesis is a single parenthesis, likely a typo from a nested structure.
-   **Fix:** Correct the bracketing, likely by removing the single parenthesis.

---
## Summary recommendation

**MAJOR REVISIONS**

This paper has the potential to be a landmark contribution to astronomical anomaly detection and its application to cosmology. The scale is unprecedented, and the methodological insights, particularly regarding the necessity of native retraining, are of great value to the field. The cosmological analyses are performed with a high degree of rigor.

However, the manuscript in its current state is not acceptable for publication in Physical Review D. The presence of internal-review artifacts (P3-E1, P3-E3) is an essential flaw that must be corrected. The irreproducible nature of the eROSITA scores (P3-E2) is a major scientific limitation that must be communicated more clearly and forcefully. Furthermore, issues with data leakage (P3-M2), unprincipled selection criteria (P3-M5), and confusing presentation of key results (P3-M3, P3-M4, P3-M6) significantly detract from the paper's impact and clarity.

The authors are urged to undertake a major revision to address these points. A successful revision would significantly improve the paper's clarity, rigor, and long-term value as a reference for the community.