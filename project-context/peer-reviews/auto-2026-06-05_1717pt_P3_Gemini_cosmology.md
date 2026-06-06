# P3 auto-2026-06-05_1717pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (2924 chars)
**Wall time**: 137.3s

---

## Referee Report: "Spectrally Unusual Sources at Scale..."

This paper presents a large-scale anomaly detection campaign across seven astronomical surveys, resulting in a catalog of over 378,000 unique anomalous sources. The authors apply a consistent autoencoder framework (BIGAE), develop a "Path-C" native-retraining protocol to handle cross-survey domain shift, and perform extensive internal validation. The primary scientific applications explored are the identification of novel astrophysical objects and the use of these objects as a new tracer population to constrain primordial non-Gaussianity (fNL). A secondary application to Pulsar Timing Array data is also presented.

The scale of the analysis is impressive, and the methodological rigor, particularly the transparency regarding artifacts and limitations (e.g., the LAMOST training bias and the quarantined ACT cross-transfer), is a significant strength. The resulting catalog is a valuable resource for the community.

However, the paper suffers from several significant issues that must be addressed before it can be considered for publication in Physical Review D. These include a numerical error in a key cosmological result, an unfocused structure that dilutes the main contribution, and the relegation of critical methodological details to dense, hard-to-parse footnotes.

### Findings

**ESSENTIAL**

*   **P3-E1 (Bibliography, p. 19):** The entry for reference [33] contains an internal author note that must be removed.
    *   **Problem:** The reference reads: `[33] C. Heinrich, O. Doré, and E. Krause, “Measuring fNL with the SPHEREx Multi-tracer Redshift Space Bispectrum," J. Cosmol. Astropart. Phys. 2024, 074 (2024), arXiv:2311.13082 [astro-ph.CO] [publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity].`
    *   **Fix:** Remove the bracketed internal note: `[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]`.

**MAJOR**

*   **P3-M1 (Cosmological Applications, p. 10):** The quoted percentage improvement for the fNL forecast is arithmetically incorrect. This is a key result of the paper.
    *   **Problem:** The paper states: "The single-tracer DESI QSO baseline is σ(fNL)std = 8.98, so the central 7.9% improvement is consistent with no improvement at <1σ". The new central forecast is σ(fNL) = 8.14. The percentage improvement is calculated as `(σ_old - σ_new) / σ_old`.
    *   **Recomputation:** `(8.98 - 8.14) / 8.98 = 0.0935`, which is a **9.4%** improvement, not 7.9%.
    *   **Fix:** Correct the percentage improvement from 7.9% to 9.4% throughout the manuscript (Abstract, Section V B, Conclusion 5). Re-evaluate the accompanying text discussing the significance of this improvement.

*   **P3-M2 (Paper Structure and Scope, pp. 1, 11, 14):** The paper's structure is unfocused and its length (20 pages) is excessive for a primary catalog/methods paper. The NANOGrav analysis, while interesting, is disconnected from the core anomaly detection work and should be separated.
    *   **Problem:** The paper presents itself as a multi-survey anomaly catalog but dedicates significant space (Abstract, Section V A, Conclusion 5, Appendix E) to a secondary analysis fitting a bounce model to NANOGrav data. This analysis does not use the new anomaly catalog and serves only to dilute the paper's main, and very substantial, contribution.
    *   **Fix:** Restructure the paper to focus on the anomaly catalog, its validation, and its direct application (the fNL forecast). Move the entire NANOGrav analysis to an appendix or, preferably, remove it for inclusion in a separate, dedicated paper. This will tighten the narrative and reduce the page count to a more appropriate length for PRD (~12-15 pages).

*   **P3-M3 (Table I Footnotes, p. 7):** Critical methodological details and validation results are buried in extremely dense footnotes (`||` and `§`) to Table I, making them difficult to find and interpret.
    *   **Problem:** Footnote `||` contains the entire derivation of the final unique object count (388,493 -> 378,280) and the crucial stratification into point-source and map-patch tiers. Footnote `§` contains a key cross-validation result for eROSITA (the 95.3% overlap between BIGAE and Isolation Forest) and introduces a separate 9,303-object reference set not clearly defined elsewhere. This information is essential to understanding the catalog's construction and reliability.
    *   **Fix:** Move the content of these footnotes into the main body of the text. The deduplication and stratification logic belongs in Section IID ("Path-C Rebuild Methodology"). The eROSITA cross-validation result belongs in Section III E, with a clear explanation of the 298-source headline catalog versus the 9,303-source cross-validation set.

**MINOR**

*   **P3-m1 (Table I, p. 7):** The "Total (cross-transfer, ACT-incl.)" summary row is confusing as ACT DR6 is not listed in the main table, making the total counts difficult to verify.
    *   **Problem:** The table presents a summary total that includes a survey not itemized in the table itself. A reader cannot sum the columns to reproduce the total.
    *   **Fix:** Either add a (clearly marked as quarantined) row for ACT DR6 to the table so the totals are verifiable, or rephrase the summary row label to make its provenance clear without requiring reference to the caption (e.g., "Baseline total including quarantined ACT DR6 scan").

*   **P3-m2 (Abstract, p. 1):** The abstract mentions a "recommended catalog-grade subset is ~265,000 unique objects" but the rationale for this specific subset (explicitly excluding LAMOST) is not fully clear until much later in the paper.
    *   **Problem:** The abstract front-loads a specific catalog subset without immediately providing the context that the excluded LAMOST tier is considered an "exploratory" set contaminated by a "methodological lesson".
    *   **Fix:** Briefly append the reason for the exclusion in the abstract sentence itself, e.g., "...~265,000 unique objects..., which excludes the exploratory LAMOST tier found to be dominated by a training-bias artifact."

### Summary recommendation

**MAJOR REVISIONS**

This paper details a massive and valuable effort to produce the largest multi-survey anomaly catalog to date. The methodological work, especially the development of the "Path-C" protocol and the transparent reporting of its successes and failures, is of high quality. However, the manuscript in its current form is not acceptable for publication. A key cosmological result is based on a straightforward arithmetic error. The paper's narrative is unfocused, blending the primary catalog work with a disconnected secondary analysis, resulting in excessive length. Finally, critical details about the catalog's construction and validation are obscured in footnotes. The authors must correct the numerical forecast, significantly restructure the paper to focus on the core contribution, and present essential information more clearly in the main text. Upon successful completion of these major revisions, the paper will be a strong candidate for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a more rigorous, second-pass review of the paper.

**MAJOR**

*   **P3-M4 (Abstract and Section III E, pp. 1, 6):** The abstract and main text prominently feature an "eROSITA cross-validation stability 81.5%", which is a misleading representation of the validation performed.
    *   **Problem:** A close reading of Table I footnote `§` and Section III E reveals that the 81.5% figure is the self-consistency (XV-stability) of a secondary *Isolation Forest* model, not the primary BIGAE model used to generate the canonical eROSITA anomaly catalog. The more relevant validation metric presented is the 95.3% overlap between the top anomalies from the primary BIGAE method and this secondary Isolation Forest method. By highlighting the 81.5% figure, the abstract implies a direct self-consistency check of the main method which was not performed; instead, a strong cross-method consistency (95.3%) was found and is arguably the more powerful result.
    *   **Fix:** The abstract and Section III E should be revised to state the cross-method validation result clearly. For example, the abstract could state: "eROSITA anomalies show a 95.3% recovery rate from an independent Isolation Forest-based detector, confirming the model-independence of the top candidates." The 81.5% self-stability of the secondary method should be de-emphasized or clarified as context for that method's reliability.

**MINOR**

*   **P3-m3 (Internal Cross-References, pp. 6, 10):** There are multiple incorrect internal cross-references throughout the manuscript that point to a non-existent "§VID".
    *   **Problem:** In Section III E, references are made to "§VID (f)". In Section V B, references are made to "§VID caveat (i)", "§VID caveat (j)", and "§VID (e)". This section does not exist. These references appear to be typos for items in Table IV. For example, "§VID (f)" likely refers to Table IV, item (f), which discusses the BIGAE vs. IF overlap for eROSITA.
    *   **Fix:** Systematically find and replace all incorrect "§VID" references with the correct references, which appear to be items in Table IV (e.g., "Table IV(f)").

*   **P3-m4 (Equation E1, p. 16):** The Pulsar Timing Array power spectral density model in Equation (E1) is dimensionally inconsistent.
    *   **Problem:** The equation contains the term `(y - 3) log10(fyr)`. The quantity `fyr` represents a frequency of 1 cycle/year and therefore has units of inverse time. It is formally incorrect to take the logarithm of a dimensional quantity.
    *   **Fix:** Rewrite the equation to use a dimensionless frequency ratio. This is typically done by referencing all frequencies to a reference frequency, which in this context is `f_ref = 1/yr`. The term should be written as `(y - 3) log10(f_i / f_ref)`. While the existing form is a common shorthand in the PTA literature, a formal publication should be dimensionally consistent.