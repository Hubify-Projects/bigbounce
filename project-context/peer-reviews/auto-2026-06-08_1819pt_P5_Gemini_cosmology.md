# P5 auto-2026-06-08_1819pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 186.0s

---

Referee Report for "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals"

This paper presents a test for the environmental dependence of spiral galaxy chirality using data from the DESI Data Release 1. The analysis cross-matches a large, pre-existing chirality catalog with DESI spectroscopic redshifts, and employs two main environmental classifiers: a V-Web tidal-tensor classifier run on the full DESI sample, and a void/non-void classification based on the publicly available DESIVAST void catalog. The primary result is a null detection: the fraction of clockwise spirals does not show a statistically significant dependence on cosmic-web environment, once a small, catalog-wide monopole bias (from the input catalog) is accounted for. The analysis is supported by an extensive set of robustness checks, including sensitivity sweeps of hyperparameters, cross-validation against other classifiers (Tempel+2014 FoF, ASTRA), and stratification by various observational properties.

The scientific analysis is thorough and the statistical methods are generally sound. The author has performed a commendable number of cross-checks that strengthen the main conclusion. However, the paper has several essential and major issues in its current form that preclude its publication in Physical Review D.

## ESSENTIAL Revisions

**P5-E1: Impossible Dates (Throughout)**
*   **Section/Page:** Abstract (p. 1), References (p. 20).
*   **Problem:** The paper is dated "June 2026". Furthermore, several key references are cited with future dates. For example, Ullah et al. [11] is cited as `arXiv:2604.02463`, Zapata-Zuluaga et al. [12] as `arXiv:2604.01456`, and Rincón et al. [13] as published in ApJ in 2025. This is impossible and suggests the manuscript is a premature draft.
*   **Fix:** All dates must be corrected to reflect the actual submission date and the correct publication/preprint dates for all references. The paper cannot be considered for publication until this is resolved.

**P5-E2: Critical Dependence on Inaccessible Work (Throughout)**
*   **Section/Page:** Abstract (p. 1), Section I (p. 2), Section II (p. 2), References (p. 20).
*   **Problem:** The entire analysis is predicated on the chirality catalog and the catalog-wide monopole offset (`Afcw = -0.0026`) from "Paper IV [3]". This reference is cited as "companion paper (Paper IV), in preparation; manuscript in preparation." A published work must be verifiable. This is impossible if the input data and its core systematic corrections are not publicly available. The results of this paper cannot be evaluated or reproduced without access to Paper IV.
*   **Fix:** This paper cannot be published until Paper IV is, at a minimum, publicly available on a preprint server like arXiv. The reference must be updated accordingly.

**P5-E3: Post-Hoc Analysis Framing (Section V B, p. 5)**
*   **Section/Page:** Section V B, "Primary vs. secondary analysis paths", p. 5.
*   **Problem:** The author explicitly states that the choice of the "primary" analysis was made "post-hoc" and uses language like "garden-of-forking-paths concern". While the transparency is noted, this framing severely undermines the statistical claims of the paper. It is an admission of potential p-hacking. A paper in a high-impact journal must present a clear, logically motivated analysis path, not a post-facto justification.
*   **Fix:** This section must be completely rewritten. The author should present a logical progression of the analysis. For example, motivate the V-Web analysis as a broad, all-sky initial test, and the DESIVAST analysis as the primary, robust test designed to overcome specific systematics (like survey-edge effects) identified in the initial analysis. The language of "post-hoc" choice and "garden-of-forking-paths" must be removed.

## MAJOR Revisions

**P5-M1: Paper Structure and Focus (Throughout)**
*   **Section/Page:** Throughout.
*   **Problem:** The paper is 20 pages long, which is excessive for a null result. The narrative structure is confusing. The abstract and initial results sections (VI) focus on the V-Web analysis, which is later shown to be inferior and systematics-prone for the void class. The strongest and cleanest result—the DESIVAST-anchored analysis—does not appear until Section VIII on page 10. The numerous cross-checks in Sections IX and X, while valuable, dilute the impact of the primary result.
*   **Fix:** The paper requires significant restructuring.
    1.  Lead with the strongest result. The DESIVAST-anchored analysis (§VIII) should become the core of the main results section.
    2.  The V-Web analysis should be presented as a supporting, all-sky analysis, with its limitations (e.g., the low-z void issue confirmed by the DESIVAST cross-match) clearly stated upfront.
    3.  The extensive cross-validations against Tempel+2014 and ASTRA (§IX, §X) should be significantly condensed and potentially moved to an appendix to improve the flow of the main text. The paper should be shortened to a more appropriate length for its contribution, perhaps 10-12 pages.

**P5-M2: Clarification of the "Real Residual" (Section VI A, p. 2 & Section VII d, p. 8)**
*   **Section/Page:** Abstract (p. 1), p. 2, p. 8.
*   **Problem:** The paper identifies a `|z| ≈ 3.4σ` sign-flip in the filament class between the "bright" and "dark" tracer samples. It is flagged as a "real residual structure" and a "real diagnostic to be disentangled by future... follow-up". However, the paper also argues that the BGS-selection-function-origin is the "strongest sign" for its source. The language is ambiguous. Is this an astrophysical signal or a systematic? The non-independence of V-Web class and target program (`p < 10^-1000`) strongly suggests it is a systematic leaking through the analysis chain.
*   **Fix:** The author must be clearer in their interpretation. The evidence points strongly toward a systematic effect tied to the BGS target selection. The paper should state this as the most likely interpretation, rather than presenting it as a potentially new astrophysical signal. The "real diagnostic" language should be toned down to reflect that it is most likely a diagnostic of residual systematics in the DESI BGS sample when split by environment.

## MINOR Revisions

**P5-m1: Toy EFT Model (Appendix A, p. 19)**
*   **Section/Page:** Appendix A, p. 19.
*   **Problem:** The toy EFT mapping is highly speculative. The operator form is not derived from a fundamental theory and, as the author correctly notes, has invariance issues. While presented with appropriate caveats, it adds little to the paper's core observational result and may be a distraction.
*   **Fix:** The author should consider removing this appendix. If they choose to retain it, the "toy" and "schematic" nature must be emphasized even more strongly, perhaps in the main text where the appendix is first mentioned.

**P5-m2: Redundant Wording in Abstract**
*   **Section/Page:** Abstract, p. 1.
*   **Problem:** The abstract contains the phrase "four DESIVAST-anchored re-projections of the V-Web null on a ~130x larger void sample (methodologically correlated by construction because they reuse the same matched-spiral subsample, but spanning the VoidFinder sphere-growing vs. ZOBOV watershed algorithmic axes)". This level of methodological detail is too verbose for the abstract.
*   **Fix:** Condense this sentence to be more direct, for example: "...and four robustness tests using the DESIVAST void catalog, which provides a ~130x larger void sample and spans multiple void-finding algorithms."

## NITs

**P5-N1: Footnote Placement (p. 2)**
*   **Section/Page:** p. 2.
*   **Problem:** Footnote `a` is attached to the end of the first paragraph of the introduction. However, it defines the "tidal-tensor formulation" which is first mentioned in the abstract and used in the V-Web method.
*   **Fix:** Move the footnote anchor to the first mention of "V-Web tidal classification" in the abstract or the first mention of the method in the body (Section IV).

**P5-N2: Citation Style (p. 5)**
*   **Section/Page:** Section V B, p. 5.
*   **Problem:** The citation `Rincón et al. 2025, ApJ 982, 38 [13]` is unconventional. The year and journal details are usually left to the bibliography.
*   **Fix:** Use a standard citation style, e.g., "Rincón et al. [13]".

## Summary recommendation

**MAJOR REVISIONS**

The paper presents a statistically powerful and robust null result that represents a significant contribution to the search for parity violation in cosmology. The depth of the robustness and systematics checks is a major strength. However, the paper is not acceptable for publication in its current form. The essential issues of impossible dates and a critical reliance on an inaccessible "in preparation" manuscript (Paper IV) must be resolved before the paper can be properly reviewed. Furthermore, the paper requires a major restructuring to improve its narrative clarity, focus, and length, and the framing of the analysis plan must be revised to remove any suggestion of post-hoc statistical choices. If the author can satisfactorily address these points, the revised manuscript would likely be suitable for publication.