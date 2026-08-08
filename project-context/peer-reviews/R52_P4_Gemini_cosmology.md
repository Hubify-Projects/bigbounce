# P4 R52 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p2_chirality/chirality_catalog_paper.pdf` md5=c47abc18 pages=23
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 205.8s

---

## Referee Report on "Survey-Scale Galaxy Chirality with Equivariant TTA..."

**To the Editor of Physical Review D,**

This paper presents a search for a cosmic dipole in the chirality of spiral galaxies using a new, large catalog of 8.47 million galaxies from the DESI Legacy Surveys. The authors construct a catalog of 3.2 million spiral galaxies classified by a Vision Transformer and perform a rigorous analysis of potential systematic effects. The primary scientific result is a null detection of a real-space chirality dipole, consistent with statistical isotropy. The paper makes a significant methodological contribution by demonstrating and quantifying a "monopole-mask leakage" channel, whereby a small, uniform classifier bias can create a spurious, large-scale dipole signal when coupled with the non-uniform sky coverage of a survey. The use of equivariant test-time averaging (TTA) is shown to be essential for mitigating this systematic.

The analysis is exceptionally thorough, and the paper is written with a high degree of clarity and precision. The authors carefully distinguish between different statistical estimators and null hypotheses, provide a comprehensive suite of systematic checks, and are commendably cautious in their claims. The public release of the catalog, model, and analysis code is a major strength and sets a high standard for reproducibility. The work provides a strong constraint on isotropy-breaking physics and serves as a crucial methodological guide for future large-scale morphology studies.

The paper is of high quality and is suitable for publication in Physical Review D. I recommend acceptance after the following minor points are addressed.

---
### Findings

#### MAJOR REVISIONS

**P4-M1: Conclusion Structure**
*   **Location:** Section VII. Conclusions, page 14.
*   **Problem:** Conclusion point (c), "Canonical-N MASTER l=1 direct compute," discusses the reconciliation of results from two different Monte Carlo runs (+3.64σ from a 500-MC run vs. +7.93σ from a 10⁴-permutation run). While this is an important internal consistency check, it reads more like a technical note on the analysis pipeline than a top-level scientific or methodological conclusion of the paper. It disrupts the flow of the main takeaways, which are about the physics constraints and the broader methodological lessons.
*   **Required Fix:** Move the content of conclusion (c) to a more appropriate location, such as a footnote or the relevant methods section (e.g., Appendix A or D). The main conclusions should focus on the primary results: the null dipole, the constraints on new physics, the importance of bias hardening, and the discovery of the monopole-mask leakage channel.

#### MINOR REVISIONS

**P4-N1: Inaccurate Wording in Abstract**
*   **Location:** Abstract, page 1.
*   **Problem:** The sentence "and the unthresholded-sample sensitivity is attributed to a low-confidence-tail systematic in Sec. IV" uses the word "sensitivity" incorrectly. Sensitivity refers to the ability of an experiment to detect a signal (e.g., the minimum detectable amplitude). The text is referring to a measured *excess* or *signal* in the unthresholded sample.
*   **Required Fix:** Replace "sensitivity" with a more appropriate word, such as "excess" or "signal." For example: "and the excess in the unthresholded sample is attributed to a low-confidence-tail systematic..."

**P4-N2: Placeholder Date**
*   **Location:** Page 1, under the author line.
*   **Problem:** The date is listed as "(Dated: June 13, 2026)," which is in the future. This is clearly a placeholder.
*   **Required Fix:** Replace the placeholder with the actual date of submission.

**P4-N3: Table III Caption Length**
*   **Location:** Table III, page 11.
*   **Problem:** The caption for Table III is exceptionally long, containing a full paragraph of detailed explanation. While the information is valuable for correctly interpreting the table, its length makes the table less scannable and mixes caption-like descriptions with text-like exposition.
*   **Required Fix:** Consider shortening the caption to focus on defining the table's contents. The more detailed explanations (e.g., the calculation of rank-p, the discussion of the heavy-tailed null) could be moved to the main body text where the table is introduced, or into a footnote.

**P4-N4: Table X Readability**
*   **Location:** Table X, page 20.
*   **Problem:** The table correctly omits z-values for the collinear leg-fraction templates. However, the cells in the 'z' column for these rows are left blank. This is slightly ambiguous.
*   **Required Fix:** To improve clarity, place an explicit symbol such as "—" or "N/A" in the empty cells of the 'z' column for the `leg BASS+MzLS`, `leg DECaLS`, and `leg DES` rows to indicate that the value is intentionally not applicable.

#### NIT-PICKS (Cosmetic)

**P4-N5: Author Email Address**
*   **Location:** Page 1, footnote.
*   **Problem:** The contact email `houston@hubify.com` appears to be a non-institutional or potentially temporary address.
*   **Required Fix:** While not a requirement, the author might consider providing a more permanent or institutional email address for long-term correspondence. This is merely a suggestion.

---
## Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

This is an excellent paper that represents a significant and carefully executed piece of work. The scientific result is a robust null detection that provides important constraints, and the methodological contributions are of great value to the field. The analysis is rigorous, the systematic checks are comprehensive, and the conclusions are well-supported. The paper is written to a very high standard. The required revisions are minor and will serve to further improve the clarity and structure of the presentation.