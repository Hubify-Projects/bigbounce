# P3 2026-06-04_R6clean — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 91.8s

---

## Referee Report for PRD

**Manuscript ID:** [Assigned by Editor]
**Title:** Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and Native-Trained Novelty Fractions from 37.3 Million Sources and Map Patches
**Author:** Houston Golden

This paper presents a very large-scale anomaly detection campaign across seven major astronomical surveys, resulting in a catalog of nearly 380,000 unique anomalous sources. The work is notable for its methodological rigor, including a "Path-C" protocol involving per-survey native model retraining to address cross-domain contamination, extensive validation through cross-validation and injection-recovery tests, and a careful assessment of the catalog's novelty. The paper further explores cosmological applications, providing an updated multi-tracer forecast for primordial non-Gaussianity (fNL) and a consistency check of the matter-bounce scenario against pulsar-timing-array data.

The technical content of the paper is of a very high standard. The analysis is thorough, and the authors demonstrate a sophisticated understanding of the subtleties involved, from the details of the machine learning methodology to the theoretical underpinnings of the cosmological forecasts. The honest reporting of limitations, systematic effects (like the LAMOST training bias), and null results (the Planck x ACT cross-correlation and the statistically insignificant fNL improvement) is commendable. The handling of the Fisher forecast for fNL, including the correct treatment of Fisher information positivity and the verification that GR projection effects are sub-dominant, is exemplary.

However, the paper in its current form is not suitable for publication. The presentation, structure, and length are significant obstacles to its accessibility and impact. The manuscript reads more like an internal technical report or an audit document than a finished scientific paper. The core results are buried in an overwhelming amount of detail, internal bookkeeping, and remnants of the authors' own review process. A major restructuring and rewriting effort is required.

### ESSENTIAL Revisions

**ID: P3-E1**
**Section:** VI D (Path-C Rebuild Residual Caveats), pp. 26-30
**Problem:** This 5-page section is the most significant issue with the manuscript. It is not a coherent discussion of caveats but rather a disorganized collection of internal audit notes, resolutions to previous issues, derivations of core results, and summaries of points made elsewhere. It severely disrupts the flow of the paper and makes the key results difficult to follow. It contains numerous phrases that are artifacts of an internal review process, such as "Resolution:", "gate status: CLOSED", "No table restructure is required", "an earlier computation quoted the envelope as... which contained an arithmetic error", and "The recompute confirms option (ii)". Furthermore, critical results, such as the derivation of the correct Fisher-positivity-respecting error envelope for the fNL forecast (items i, j), are inappropriately placed in a "caveats" section.
**Required Fix:** This section must be completely dismantled.
1.  Remove all internal review language and audit-trail-style phrasing.
2.  Move core results and derivations (e.g., the detailed Fisher information positivity analysis, the Jaccard consistency arithmetic, the dedup arithmetic) to the appropriate main sections (e.g., Section V for the fNL forecast, Section IV C for the cross-survey matching).
3.  Move genuine, unresolved limitations to the main limitations section (VI C).
4.  Information that is purely for clarification of a methodological choice (e.g., the threshold consistency discussion) should be integrated more smoothly into the relevant methods section (e.g., Section II or III).
5.  The entire paper must be proofread to remove any other such internal-review artifacts. For example, the caption of Table III (p. 17) contains the phrase "this revised table lists both explicitly," which should be removed.

**ID: P3-E2**
**Section:** General (Length and Structure)
**Problem:** At 49 pages, the paper is excessively long for a journal article, even considering the scope. The density of information, particularly in the abstract and introduction, makes it very difficult to parse the main takeaways. The narrative is frequently interrupted by deep dives into methodological minutiae that would be better placed in an appendix.
**Required Fix:**
1.  The paper must be significantly shortened and restructured into a main paper (~15-20 pages) and a set of detailed appendices.
2.  The main paper should focus on the high-level summary of the methodology (Path-C), the key results (catalog scale, novelty fraction, the LAMOST/SDSS contamination lessons), and the main conclusions of the cosmological applications.
3.  Detailed derivations, exhaustive lists of validation checks (like the itemized list in §VI D), and extensive image galleries should be moved to appendices.
4.  The abstract must be rewritten to be more concise. It should state the main results (e.g., the catalog size, the ~17.8% novelty fraction, the fNL forecast being consistent with no improvement) without the overwhelming numerical detail and sub-clauses.

### MAJOR Revisions

**ID: P3-M1**
**Section:** III, Table I, p. 15
**Problem:** Table I is the central summary of the survey results, but it is very confusing. It primarily lists the initial "cross-transfer" anomaly counts, which the text repeatedly and correctly states are superseded and in some cases (SDSS, LAMOST) misleading by orders of magnitude. The canonical, final "Path-C native" counts are not present in the main table rows and are mentioned only in footnotes and the text. This forces the reader to piece together the primary results of the paper from disparate text and footnotes, which is unacceptable.
**Required Fix:** Revise Table I to be a clear, stand-alone summary of the paper's final results. It should contain separate, clearly labeled columns for the initial "Cross-transfer" counts (for diagnostic purposes) and the final "Path-C Native" counts (the primary result). The current `Nanom` column should be renamed to clarify it represents the cross-transfer baseline. The footnotes can then be used for secondary details, not for conveying the primary results.

**ID: P3-M2**
**Section:** III C, p. 12
**Problem:** The paper states that for SDSS, the published native anomaly count (77,905) was chosen to match the cross-transfer count as a "bookkeeping convenience for catalog continuity". This is not a physically motivated choice. It mixes results from two different methodologies (a top-percentile cut of the native distribution and a count from a flawed cross-transfer analysis) and undermines the integrity of the native-retrained catalog.
**Required Fix:** Use a consistent, physically motivated threshold for the SDSS native catalog (e.g., the same S > 5 cut used for DESI, or a top-1% cut as used for LAMOST). Report the resulting number of anomalies, even if it does not match the old cross-transfer count. The goal should be to present the most physically sound catalog, not to maintain historical continuity with a flawed baseline.

**ID: P3-M3**
**Section:** V, p. 21, and VI D, p. 27-28
**Problem:** The discussion of the fNL forecast is spread across multiple sections and contains confusing back-and-forth between a flawed linear-extrapolation and the correct positivity-respecting `α²` form. While the final conclusion is correct, the presentation is convoluted. The core derivation of the correct error envelope is buried in the "Residual Caveats" section.
**Required Fix:** Consolidate the entire fNL forecast derivation and discussion into Section V. Clearly state the adopted model (`1/σ² = F₀ + c α²`). Derive the central value and the 1σ/95% credible intervals based on this model and the empirical `α` measurement. The flawed linear approximation should be mentioned only briefly, if at all, to explain why it is incorrect and not used. The final result and its interpretation (consistent with null) should be presented clearly and unambiguously.

### MINOR Revisions

**ID: P3-m1**
**Section:** V, p. 23
**Problem:** The paper correctly notes that GR projection effects are a "gauge-invariant theoretical contamination" that must be subtracted. This is a key theoretical point. However, the subsequent check in §VI D(e) that finds the effect to be <0.02% is buried.
**Required Fix:** While the effect is small, the check is important. A brief statement summarizing the result of this check should be included in Section V when the omission of GR effects is first mentioned, with a pointer to the appendix (where the details of §VI D(e) should be moved) for the full calculation.

**ID: P3-m2**
**Section:** IV D, p. 21
**Problem:** The paper reports a null result for the Planck x ACT cross-correlation and correctly concludes that the CMB anomalies are dominated by survey-specific systematics. This is an important finding.
**Required Fix:** The abstract should briefly mention this null result, as it is a key finding regarding the potential for using this method to find primordial cosmological signals in the CMB.

**ID: P3-m3**
**Section:** Appendix A1, Figure 5, p. 12
**Problem:** The panel labels in Figure 5 use "AE" to denote the Z-arm sub-score `rZ`, which is inconsistent with the use of `S` for the total anomaly score elsewhere. The caption clarifies this, but it is still likely to cause confusion.
**Required Fix:** If possible, modify the panel labels to be less ambiguous (e.g., `rZ` or `S_Z`). If the labels cannot be changed, the clarification in the caption should be made even more prominent (e.g., bolded).

### NITs

**ID: P3-N1**
**Section:** VI D, pp. 28-29
**Problem:** The lettering of the itemized list in this section is incorrect, with two items labeled "(i)" and subsequent items not following a logical sequence.
**Required Fix:** Correct the lettering of the list items (e.g., (i), (j), (k), ...). This will be resolved by the essential revision to dismantle this section, but is noted here for completeness.

## Summary recommendation
**MAJOR REVISIONS**

This manuscript contains the foundation of an excellent and impactful paper. The scale of the analysis is unprecedented, the methodological corrections are well-motivated and effective, and the cosmological applications are handled with a high degree of theoretical rigor. However, the paper is in a state that is closer to a technical note for internal collaboration than a polished, readable manuscript for a top-tier journal. The essential and major revisions outlined above, focusing on a complete restructuring of the paper to improve clarity, flow, and length, and to remove artifacts from the writing process, are necessary before it can be considered for publication. I am confident that if the authors undertake this significant but necessary revision, the resulting paper will be a valuable contribution to the field.