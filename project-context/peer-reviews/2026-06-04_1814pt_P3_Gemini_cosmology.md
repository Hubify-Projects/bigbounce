# P3 2026-06-04_1814pt — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 69.3s

---

**Referee Report on HUBIFY-2026-003**

This paper presents a large and comprehensive catalog of anomalous astronomical sources, compiled by applying an autoencoder-based anomaly detection framework to seven major astronomical surveys. The total catalog contains over 378,000 unique anomalies from 37.3 million sources. The authors present the catalog construction, validation, and high-level properties. They further explore cosmological applications, including a forecast for constraints on primordial non-Gaussianity (`f_NL`) using the anomalies as a new tracer population, and a consistency check between the matter-bounce cosmological model and recent pulsar-timing-array data.

The scale of the catalog and the multi-survey nature of the work represent a significant contribution to the field of astronomical data analysis. The cosmological applications, while preliminary, are well-motivated and demonstrate the potential scientific utility of the catalog. The analysis appears to be carefully done, with laudable transparency about methodological pitfalls, null results, and the evolution of the analysis.

However, the paper in its current form is not suitable for publication in Physical Review D. The presentation is severely hampered by a format that resembles an internal technical document or a software release note rather than a scientific paper. It is excessively long, filled with internal project jargon and version-control artifacts, and its structure makes it very difficult for a reader to distinguish between primary scientific results, methodological lessons, and the history of the analysis. A complete restructuring and rewriting are required before the paper can be considered further.

## Detailed Findings

### ESSENTIAL

**P3-E1: Removal of Internal Jargon, Audit Tags, and Changelog-Style Prose**
-   **Location:** Throughout the manuscript.
-   **Problem:** The paper is replete with internal version numbers (e.g., "v3.1.73", "v3.1.68 closure"), internal analysis tags (e.g., "Wave 14-VVV", "R15 GEM-B1 closure", "Wave 14-KKKK"), and entire sections written as a changelog of resolved issues (e.g., §VI D, "Path-C Rebuild Residual Caveats", with entries like "CLOSED v3.1.56 via on-disk artifact."). This is entirely inappropriate for a peer-reviewed scientific publication. It makes the paper nearly unreadable and obscures the scientific narrative under a mountain of project management artifacts.
-   **Fix:** All internal versioning, code names, and audit tags must be removed from the manuscript. The content of sections like §VI D must be completely rewritten. Important methodological resolutions should be integrated into the relevant methods sections (§II) or discussion (§VI) in standard scientific prose. The history of bug fixes and analysis updates is not relevant to the final scientific paper and should be removed.

**P3-E2: Major Restructuring and Reduction in Length**
-   **Location:** Entire manuscript.
-   **Problem:** At 50 pages, the paper is excessively long for its primary contribution. The structure mixes final results with detailed descriptions of superseded "cross-transfer" baseline analyses, making the narrative difficult to follow. Extensive appendices, particularly the image galleries, and detailed per-survey results contribute to the bloat.
-   **Fix:** The paper must be restructured and significantly condensed to a length appropriate for PRD (target: 15-20 pages for the main text).
    1.  The main text should focus exclusively on the final "Path-C" methodology and results. The initial "cross-transfer" analysis, which was found to be flawed, should be briefly summarized in an appendix as a methodological cautionary tale, not given prominence in the main text. Figures related to this baseline (e.g., Fig. 3, Fig. 6) should be moved to this appendix.
    2.  The per-survey results in §III should be summarized at a high level, with detailed tables and breakdowns moved to an appendix or supplemental material.
    3.  The cosmological applications (§V) should be presented more concisely, focusing on the key results and their interpretation.
    4.  The numerous image galleries (Appendices A2-A10) should be provided as supplemental material online, not embedded in the main PDF.

**P3-E3: Rewrite of Abstract**
-   **Location:** Page 1.
-   **Problem:** The abstract is dense, overly technical, and contains internal section references (e.g., "§VIA", "§VID"), making it inaccessible to a broad audience. It reads more like an executive summary for project insiders.
-   **Fix:** The abstract must be rewritten to be a clear, self-contained summary of the paper's key scientific results. It should state the scale of the catalog, the most important findings (e.g., the genuine novelty fraction, the LAMOST training-bias lesson), and the headline cosmological results, all without using internal jargon or references.

### MAJOR

**P3-M1: Clarification of the `f_NL` Forecast and its Null-Result Nature**
-   **Location:** Abstract, §V, §VII.
-   **Problem:** The paper presents a forecast for `σ(f_NL)` based on an empirically measured bias enhancement factor `α_jk = 0.19 ± 0.65`. This measurement is consistent with zero at `0.29σ`. Consequently, the data provide no statistically significant evidence for an improvement in `f_NL` constraints. While the paper acknowledges this (e.g., "consistent with no improvement at < 1σ"), the presentation is convoluted and could lead readers to misinterpret the result as a positive detection of multi-tracer improvement.
-   **Fix:** The authors should state clearly and upfront in the abstract and relevant sections that their measurement of the bias enhancement is consistent with zero. The reported central-value forecast (`σ(f_NL) = 8.14`) should be explicitly framed as a projection of the potential improvement *if* the central value of `α` were to be confirmed with much higher precision, while emphasizing that the current data do not support this. The careful handling of the Fisher positivity and the retraction of the incorrect linear error propagation is commendable but needs to be presented more clearly as part of the final, correct analysis, not as a historical note.

**P3-M2: Theoretical Scoping of Cosmological Analysis**
-   **Location:** §V, Appendix E.
-   **Problem:** The paper connects the `f_NL` constraints and the NANOGrav GWB spectral index to a specific "quasi-matter bounce" model. While this provides a compelling motivation, the scope of the model class being tested is very narrow (scalar-only, w=0).
-   **Fix:** The authors should be more explicit about the limitations of their theoretical interpretation. They correctly note that the `f_NL` and `γ_GW` predictions decouple in broader model classes. This point should be emphasized in the main discussion (§V) to ensure readers do not over-interpret the NANOGrav consistency check as evidence for the entire bouncing cosmology paradigm. The current presentation is careful but could be more prominent.

### MINOR

**P3-m1: GR Projection Effects Presentation**
-   **Location:** §V (p. 24) and §VI D(e) (p. 28).
-   **Problem:** The paper first states that GR projection corrections are omitted and defers a recompute plan (§V), but later resolves this in the "caveats" section (§VI D(e)), showing the effect is negligible. This creates confusion.
-   **Fix:** The resolution should be presented in the main text where the issue is raised. A simple statement in §V that the effects were calculated and found to be negligible (`<0.02%`) would suffice, with the details in an appendix if necessary.

**P3-m2: Title and Keywords**
-   **Location:** Page 1.
-   **Problem:** The title is long and contains jargon ("Path-C", "Native-Trained") that is not meaningful to a reader prior to reading the paper.
-   **Fix:** The authors should consider a shorter, more accessible title, for example: "A Multi-Survey Catalog of 378,000 Spectrally Unusual Sources and Applications to Cosmology."

**P3-m3: Inconsistent Terminology for Standardized Score**
-   **Location:** §II B (p. 5).
-   **Problem:** The paper defines the canonical anomaly score `S` but frequently refers to the process of calculating it as "z-scoring", which creates a potential ambiguity with redshift `z`. The authors are aware of this and note it, but consistent use of "standardized score" or "S-score" in the prose would improve clarity.
-   **Fix:** Replace instances of "z-scored" with "standardized" or a similar unambiguous term when referring to the statistical score `S`.

## Summary recommendation

**MAJOR REVISIONS**

The paper reports on a work of significant scale and potential impact. The creation of this multi-survey anomaly catalog is a valuable contribution, and the cosmological analyses, though preliminary, are well-motivated and carefully executed. However, the manuscript is not written in the style of a scientific journal article. It is formatted as a technical data release note, complete with an internal audit trail that makes it unpublishable in its current form. The paper requires a complete rewrite to focus the narrative on the key scientific results, remove all internal jargon and versioning artifacts, and drastically reduce its length. If the authors undertake this major revision to produce a focused, professional, and readable scientific paper, the underlying work is of sufficient quality to warrant publication in Physical Review D.