# P3 R53 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R53_P3/paper3_draft.pdf` md5=464d4066 pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (9321 chars)
**Wall time**: 154.3s

---

## Referee Report on "Spectrally Unusual Sources at Scale..."

This paper presents a large-scale anomaly detection study across seven astronomical surveys, resulting in a catalog of over 378,000 unique anomalous sources. The authors apply a consistent autoencoder framework (BIGAE), develop a "Path-C" native-retraining protocol to address cross-survey domain shift, and perform extensive validation and characterization of the resulting catalog. The work culminates in cosmological applications, including a forecast for primordial non-Gaussianity (`f_NL`) constraints and a consistency check of the NANOGrav gravitational-wave background signal with matter-bounce cosmology predictions.

The paper is exceptionally thorough in its methodology, validation, and documentation of limitations. The transparency regarding methodological challenges (e.g., the LAMOST training bias, the eROSITA score-axis irreproducibility, the quarantined ACT data) is commendable and sets a high standard for work in this area. The cosmological analyses are appropriately cautious, with careful attention to systematics and statistical interpretation.

However, the paper requires significant revision before it can be considered for publication in Physical Review D. There are two essential issues related to incomplete analysis and data release preparation, along with major issues concerning clarity and length that impede readability.

### ESSENTIAL Revisions

**P3-E1: Incomplete Analysis of Data Leakage from Preprocessing**
*   **Section/Page:** §II B α, page 3
*   **Problem:** The authors correctly identify a methodological flaw: for the tabular surveys (eROSITA, NEOWISE, Gaia), feature-scaling statistics were fit on the full dataset rather than only the training split. This constitutes data leakage from the validation/test set into the model's preprocessing stage. While the authors perform a bounded robustness check for the "load-bearing eROSITA tier," they state that "The corresponding checks for the NEOWISE and Gaia tiers remain queued."
*   **Required Fix:** Publishing a paper with known, unquantified methodological flaws in two of the contributing catalogs is unacceptable. The analysis is incomplete. The authors must perform and report the results of these robustness checks for NEOWISE and Gaia. The statement that these checks are "queued" must be replaced with the results of the completed analysis. The impact on the anomaly rankings and catalog composition for these surveys must be quantified and discussed.

**P3-E2: Placeholder in Data Availability Section**
*   **Section/Page:** Data availability, page 23
*   **Problem:** The Data Availability section contains the placeholder text: "A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission)."
*   **Required Fix:** For a manuscript to be accepted, all data products and code must be finalized and have their persistent identifiers (like a Zenodo DOI) in place. This placeholder must be replaced with the actual, functional DOI for the catalog data.

### MAJOR Revisions

**P3-M1: Unclear and Confusing Footnotes in Table I**
*   **Section/Page:** Table I, page 7
*   **Problem:** The footnotes in this crucial summary table are difficult to parse. Specifically, footnote ♡ defines the SDSS threshold and then refers to "the 19,253-object score-knee set of footnote♡". A footnote cannot refer to itself. This appears to be a symbol/formatting error that renders the description of the SDSS thresholding logic incomprehensible. The distinction between the "continuity slice" (77,905 objects) and the "top-1% proper" set (19,253 objects) is critical for understanding the catalog's construction and must be stated clearly.
*   **Required Fix:** Rewrite and re-format the footnotes for Table I to be unambiguous and self-contained. Ensure all symbols are unique and correctly referenced. The logic for every survey's threshold choice must be transparent to the reader without requiring detective work.

**P3-M2: Excessive Length and Pacing**
*   **Section/Page:** Entire manuscript
*   **Problem:** At 29 pages, the paper is excessively long for its primary contributions. The main text is dense with survey-specific details that, while important for completeness, detract from the main narrative of the methodology and its key findings. The extensive survey-by-survey breakdown in Section III, in particular, could be streamlined.
*   **Required Fix:** The paper should be restructured to improve readability and focus. I recommend a maximum length of 20 pages for the main text (excluding references and appendices). To achieve this, consider moving the detailed results for the secondary or "exploratory" surveys (e.g., Gaia, eROSITA, NEOWISE) into an appendix. The main body should focus on the core methodology (Path-C rebuild), the results from the primary surveys that anchor the work (DESI, SDSS, LAMOST), the cross-survey analysis, and the cosmological applications. This would make the paper more accessible while retaining the full detail for dedicated readers in the appendices.

### MINOR Revisions

**P3-m1: Typo in Introduction**
*   **Section/Page:** §I, page 2
*   **Problem:** The text reads: `[33] ((fnL) ≈ 0.7 bispectrum-only forecast)`. The double parenthesis is a typographical error.
*   **Required Fix:** Correct to a single set of parentheses.

**P3-m2: Confusing Wording in Figure 2 Caption**
*   **Section/Page:** Figure 2, page 6
*   **Problem:** The caption states: "the canonical Path-C unique count of 378,280 is not a deduplication of this baseline". This is confusing. The intent is to clarify that the map shows the historical cross-transfer baseline, while the final unique count is derived from the separate, native-retrained catalogs.
*   **Required Fix:** Rephrase for clarity. For example: "This map shows the initial cross-transfer anomaly baseline for historical context. The canonical Path-C unique count of 378,280 (see Table I) is derived from the subsequent native-retrained catalogs and is not a deduplication of the sources shown here."

### NIT (Cosmetic)

**P3-N1: Incorrect Date**
*   **Section/Page:** Title block, page 1
*   **Problem:** The paper is dated "June 19, 2026".
*   **Required Fix:** Correct this to the current submission date.

## Summary recommendation

**MAJOR REVISIONS**

This is a substantial and valuable piece of work that demonstrates a high level of rigor and transparency. The authors have produced a significant new catalog and have been admirably forthcoming about the limitations and methodological challenges encountered. The paper has the potential to be an important reference in the field. However, it cannot be published in its current state. The incomplete analysis of the pre-processing data leakage for the Gaia and NEOWISE surveys is an essential flaw that must be rectified. Furthermore, the paper's excessive length and lack of clarity in key areas, such as the footnotes of Table I, present significant barriers to the reader. Once the authors have completed the required analysis, fixed the clarity issues, and restructured the paper to be more concise, it will likely be suitable for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated review, incorporating the new findings from the second, more detailed examination.

================================================================
## Referee Report on "Spectrally Unusual Sources at Scale..."

This paper presents a large-scale anomaly detection study across seven astronomical surveys, resulting in a catalog of over 378,000 unique anomalous sources. The authors apply a consistent autoencoder framework (BIGAE), develop a "Path-C" native-retraining protocol to address cross-survey domain shift, and perform extensive validation and characterization of the resulting catalog. The work culminates in cosmological applications, including a forecast for primordial non-Gaussianity (`f_NL`) constraints and a consistency check of the NANOGrav gravitational-wave background signal with matter-bounce cosmology predictions.

The paper is exceptionally thorough in its methodology, validation, and documentation of limitations. The transparency regarding methodological challenges (e.g., the LAMOST training bias, the eROSITA score-axis irreproducibility, the quarantined ACT data) is commendable and sets a high standard for work in this area. The cosmological analyses are appropriately cautious, with careful attention to systematics and statistical interpretation.

However, the paper requires significant revision before it can be considered for publication in Physical Review D. There are two essential issues related to incomplete analysis and data release preparation, along with major issues concerning clarity and length that impede readability.

### ESSENTIAL Revisions

**P3-E1: Incomplete Analysis of Data Leakage from Preprocessing**
*   **Section/Page:** §II B α, page 3
*   **Problem:** The authors correctly identify a methodological flaw: for the tabular surveys (eROSITA, NEOWISE, Gaia), feature-scaling statistics were fit on the full dataset rather than only the training split. This constitutes data leakage from the validation/test set into the model's preprocessing stage. While the authors perform a bounded robustness check for the "load-bearing eROSITA tier," they state that "The corresponding checks for the NEOWISE and Gaia tiers remain queued."
*   **Required Fix:** Publishing a paper with known, unquantified methodological flaws in two of the contributing catalogs is unacceptable. The analysis is incomplete. The authors must perform and report the results of these robustness checks for NEOWISE and Gaia. The statement that these checks are "queued" must be replaced with the results of the completed analysis. The impact on the anomaly rankings and catalog composition for these surveys must be quantified and discussed.

**P3-E2: Placeholder in Data Availability Section**
*   **Section/Page:** Data availability, page 23
*   **Problem:** The Data Availability section contains the placeholder text: "A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission)."
*   **Required Fix:** For a manuscript to be accepted, all data products and code must be finalized and have their persistent identifiers (like a Zenodo DOI) in place. This placeholder must be replaced with the actual, functional DOI for the catalog data.

### MAJOR Revisions

**P3-M1: Unclear and Confusing Footnotes in Table I**
*   **Section/Page:** Table I, page 7
*   **Problem:** The footnotes in this crucial summary table are difficult to parse. Specifically, footnote ♡ defines the SDSS threshold and then refers to "the 19,253-object score-knee set of footnote♡". A footnote cannot refer to itself. This appears to be a symbol/formatting error that renders the description of the SDSS thresholding logic incomprehensible. The distinction between the "continuity slice" (77,905 objects) and the "top-1% proper" set (19,253 objects) is critical for understanding the catalog's construction and must be stated clearly.
*   **Required Fix:** Rewrite and re-format the footnotes for Table I to be unambiguous and self-contained. Ensure all symbols are unique and correctly referenced. The logic for every survey's threshold choice must be transparent to the reader without requiring detective work.

**P3-M2: Excessive Length and Pacing**
*   **Section/Page:** Entire manuscript
*   **Problem:** At 29 pages, the paper is excessively long for its primary contributions. The main text is dense with survey-specific details that, while important for completeness, detract from the main narrative of the methodology and its key findings. The extensive survey-by-survey breakdown in Section III, in particular, could be streamlined.
*   **Required Fix:** The paper should be restructured to improve readability and focus. I recommend a maximum length of 20 pages for the main text (excluding references and appendices). To achieve this, consider moving the detailed results for the secondary or "exploratory" surveys (e.g., Gaia, eROSITA, NEOWISE) into an appendix. The main body should focus on the core methodology (Path-C rebuild), the results from the primary surveys that anchor the work (DESI, SDSS, LAMOST), the cross-survey analysis, and the cosmological applications. This would make the paper more accessible while retaining the full detail for dedicated readers in the appendices.

### MINOR Revisions

**P3-B1: Arithmetic Mismatch in Figure 9 Caption**
*   **Section/Page:** Figure 9, page 19
*   **Problem:** The caption states that the seven redshift bins for the AI anomaly tracers "total 40,192 tracers." However, a manual sum of the counts labeled on the bars in the right-hand panel (61 + 174 + 2,645 + 11,853 + 14,709 + 9,328 + 1,350) equals 40,120. This is a discrepancy of 72.
*   **Required Fix:** Correct the total in the caption to 40,120, or verify the numbers on the plot and correct them if they are in error.

**P3-D1: Broken Internal Cross-Reference**
*   **Section/Page:** Abstract, page 1
*   **Problem:** The first paragraph references "§VIE" when discussing the size benchmark. The manuscript does not contain a section VI E.
*   **Required Fix:** Correct the reference to point to the appropriate section, or remove it if the context is sufficiently provided by the citation to [11].

**P3-m1: Typo in Introduction**
*   **Section/Page:** §I, page 2
*   **Problem:** The text reads: `[33] ((fnL) ≈ 0.7 bispectrum-only forecast)`. The double parenthesis is a typographical error.
*   **Required Fix:** Correct to a single set of parentheses.

**P3-m2: Confusing Wording in Figure 2 Caption**
*   **Section/Page:** Figure 2, page 6
*   **Problem:** The caption states: "the canonical Path-C unique count of 378,280 is not a deduplication of this baseline". This is confusing. The intent is to clarify that the map shows the historical cross-transfer baseline, while the final unique count is derived from the separate, native-retrained catalogs.
*   **Required Fix:** Rephrase for clarity. For example: "This map shows the initial cross-transfer anomaly baseline for historical context. The canonical Path-C unique count of 378,280 (see Table I) is derived from the subsequent native-retrained catalogs and is not a deduplication of the sources shown here."

**P3-m3: Unclear Units in Equation E1**
*   **Section/Page:** Appendix E, page 25, Eq. (E1)
*   **Problem:** The equation for the log-power `log10 P_i` contains terms like `y*log10(f_i)` where `f_i` is a frequency with units. Taking the logarithm of a dimensional quantity is mathematically ill-defined. While this is a common abuse of notation, it should be clarified.
*   **Required Fix:** For clarity, explicitly state the normalization convention. For example, add a sentence after the equation such as: "Frequencies `f_i` and `f_yr` are treated as dimensionless ratios relative to a reference frequency of 1 Hz."

**P3-m4: Ambiguous Self-Reference**
*   **Section/Page:** §II B b, page 4
*   **Problem:** The text discussing the preprocessing for tabular surveys says "see §II B for the per-survey specification". This is a self-reference to the entire subsection. The specific details are in the preceding sub-subsection, §II B α.
*   **Required Fix:** Change the reference from "§II B" to the more specific "§II B α" for clarity.

### NIT (Cosmetic)

**P3-N1: Incorrect Date**
*   **Section/Page:** Title block, page 1
*   **Problem:** The paper is dated "June 19, 2026".
*   **Required Fix:** Correct this to the current submission date.

## Summary recommendation

**MAJOR REVISIONS**

This is a substantial and valuable piece of work that demonstrates a high level of rigor and transparency. The authors have produced a significant new catalog and have been admirably forthcoming about the limitations and methodological challenges encountered. The paper has the potential to be an important reference in the field. However, it cannot be published in its current state. The incomplete analysis of the pre-processing data leakage for the Gaia and NEOWISE surveys is an essential flaw that must be rectified. Furthermore, the paper's excessive length and lack of clarity in key areas, such as the footnotes of Table I, present significant barriers to the reader. Once the authors have completed the required analysis, fixed the clarity issues, and restructured the paper to be more concise, it will likely be suitable for publication.