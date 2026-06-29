# P4 RA-INT — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/P4_RA.pdf` md5=96b864b6 pages=24
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 229.2s

---

**Referee Report on "Survey-Scale Galaxy Chirality with Equivariant TTA..."**

This paper presents a new, large catalog of galaxy chirality classifications for 8.47 million DESI Legacy Survey galaxies, including 3.2 million spirals. The primary scientific result is a null detection of a real-space chirality dipole, which constrains isotropy-breaking physics. The paper's main methodological contributions are the use of a flip-equivariant Vision Transformer pipeline to mitigate classifier bias and a detailed investigation of a "monopole-mask leakage" systematic that can produce spurious dipole signals. The analysis is exceptionally thorough, with a clear hierarchy of estimators, extensive systematics checks, and a high degree of transparency regarding potential limitations.

The paper is well-structured, the arguments are sound, and the conclusions are strongly supported by the evidence presented. The level of detail provided in the main text and appendices is commendable and sets a high standard for reproducibility in this type of analysis. The paper is a significant contribution and is suitable for publication in Physical Review D after minor revisions.

Below is a list of findings and required corrections.

---
### ESSENTIAL Revisions

**P4-E1**
- **Section:** Data Availability (p. 23)
- **Problem:** The paper contains placeholder dates and version tags that are not appropriate for a final publication. Specifically, the paper is dated "June 28, 2026", and the catalog release tag is "v2026.04". The text also states that a persistent archival DOI has not yet been minted.
- **Required fix:** Before publication, replace all placeholder dates and version tags with the final, correct information. An archival DOI (e.g., from Zenodo) for the specific version of the data and code used in the final paper must be created and included.

---
### MAJOR Revisions

*(No findings classified as MAJOR.)*

---
### MINOR Revisions

**P4-M1**
- **Section:** IV.C. Dipole Analysis (p. 7)
- **Problem:** The text claims that a confidence-cut sweep "shows the null is invariant across the entire high-confidence regime". However, the quoted z-scores (`z = +0.41, +1.14, +0.51 at 0.6, 0.7, 0.8`) vary by a factor of ~2.8. While all values are consistent with the null hypothesis (i.e., not significant detections), "invariant" is too strong a word for this level of fluctuation.
- **Required fix:** Rephrase to more accurately reflect the result. For example: "shows the result is robustly consistent with the null hypothesis across the entire high-confidence regime, with all z-scores remaining below a significance threshold of 1.2".

**P4-M2**
- **Section:** IV.B. Global CW Fraction (p. 6)
- **Problem:** The text makes an uncomputed quantitative claim: "The slab-to-slab scatter about the global fcw = 0.49735 is ≤ 2.7σ per slab, consistent with the coherent low-l systematic structure...". A claim with a specific number like "2.7σ" should be directly traceable to a calculation or a referenced artifact.
- **Required fix:** Provide the calculation for the 2.7σ value or, preferably, cite the specific analysis artifact file where this result can be verified, as is done for most other claims in the paper. For example, add a parenthetical "(artifact ... .json)".

**P4-M3**
- **Section:** VII. Conclusions (p. 15, item c)
- **Problem:** This section discusses the canonical-mask `l=1` residual, quoting a value of `+3.64σ` from a 500-MC run, and then immediately notes that a 10⁴-permutation recompute in Table III gives `z = +7.93σ`. While the abstract and Table III caption explain this discrepancy (different null run sizes and conventions), the conclusion section would benefit from a clearer, self-contained explanation. The large difference between the two values for the same diagnostic quantity could be confusing to a reader who missed the earlier caveats.
- **Required fix:** Add a brief sentence within this paragraph clarifying why the two numbers are different and why the `+3.64σ` value is the one used for continuity with the leakage analysis, while the `+7.93σ` is the higher-statistics result for that specific field convention. This would strengthen the standalone clarity of the conclusion.

---
### NIT (Cosmetic)

*(No findings classified as NIT.)*

---
## Summary recommendation
**ACCEPT WITH MINOR CORRECTIONS**

This is an excellent, high-rigor paper that makes a valuable contribution to both observational cosmology and data analysis methodology. The primary null result is robustly established, and the deep dive into systematics is a crucial piece of work for the community. The authors are exceptionally careful in qualifying their results and providing the necessary details for reproducibility. The paper is a model of how to conduct and present a null-result analysis in the face of complex systematics. After addressing the minor points listed above, particularly the essential update of placeholder information, the paper will be ready for publication.