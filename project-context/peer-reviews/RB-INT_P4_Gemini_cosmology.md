# P4 RB-INT — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/P4_RB.pdf` md5=b8dc2625 pages=24
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 171.8s

---

**Referee Report on "Survey-Scale Galaxy Chirality with Equivariant TTA..."**

This paper presents a new, large-scale catalog of galaxy chirality for 8.47 million DESI Legacy Survey galaxies, with 3.2 million classified as spirals. The primary scientific result is a null detection of a real-space chirality dipole, consistent with statistical isotropy. The paper's main methodological contributions are a bias-hardening pipeline using flip-equivariant test-time averaging (TTA) and a detailed characterization of systematics, particularly a "monopole-mask leakage" channel that can produce spurious dipole-like signals in harmonic-space analyses. The work is exceptionally rigorous, transparent about its limitations, and provides a comprehensive suite of null tests and systematic checks. The analysis is of high quality and the conclusions are well-supported by the evidence presented.

The paper is suitable for publication in Physical Review D, pending minor revisions. The findings are significant for cosmology, particularly for searches for parity violation and tests of the cosmological principle. The methodological work provides a valuable blueprint for future large-scale morphological studies.

Below is a list of required corrections.

---
### ESSENTIAL

**P4-E1:** Section: Title page / Data Availability (p. 1, 23)
*   **Problem:** The paper is dated "June 29, 2026", and the data release tag is "v2026.04". These are placeholder future dates.
*   **Required fix:** Update the date to the current submission date and the release tag to the actual version tag corresponding to the submitted analysis.

---
### MAJOR

(No findings classified as MAJOR)

---
### MINOR

**P4-M1:** Section: Throughout (e.g., Table I, p. 5; Sec. IV C, p. 8)
*   **Problem:** The paper frequently links to internal file paths for analysis artifacts (e.g., `pipelines/p2_chirality/outputs/dipole/catalog_c_summary.json`). While the root code repository is provided, these paths are not directly useful to a reader of the PDF and will not be stable.
*   **Required fix:** For the final publication version, either remove these internal paths or, preferably, replace them with permanent links to the specific files within the archival repository (e.g., a Zenodo link or a link to the specific file on the tagged GitHub release).

**P4-M2:** Section: Abstract (p. 1)
*   **Problem:** The abstract contains a parenthetical statement: "(The +3.64σ value is from a 500-MC direct run on the canonical unapodized mask; the 10^4-permutation canonical unapodized row in Table III gives +7.93σ; both are systematics-attributed diagnostics from different null-run sizes, not two independent detection claims.)". While the transparency is commendable, this level of detail about different run configurations for a secondary diagnostic is excessive for an abstract and hinders readability. The core point is that the harmonic-channel residuals are systematics-attributed and arise from different estimators than the primary null result.
*   **Required fix:** Condense this parenthetical. For example: "(These harmonic-channel residuals are systematics-attributed diagnostics from distinct estimators and null procedures, and are not directly comparable to the primary real-space result.)". The full detail is appropriate for the main text but not the abstract.

---
### NIT

**P4-N1:** Section: Table III Caption (p. 11)
*   **Problem:** The caption for Table III is extremely long, spanning almost half a page. While the information is valuable for reproducibility, its length makes the table difficult to parse.
*   **Required fix:** Consider moving some of the detailed explanatory text (e.g., the definition of rank-p, the discussion of the heavy-tailed null) into the main body text or a footnote, leaving the caption to focus on defining the columns and the specific configurations used for the table's two main blocks.

**P4-N2:** Section: Footnote 5 (p. 22)
*   **Problem:** This footnote is exceptionally dense and contains a complex, multi-part argument comparing different estimators and their relation to the monopole-mask leakage channel. It is critical for understanding the results in Appendix E, but its format as a single, long paragraph of a footnote makes it very difficult to follow.
*   **Required fix:** The content of this footnote is important enough that it should be promoted into the main body of Appendix E.b. It should be restructured as a proper paragraph with clear sentences to improve readability and highlight its importance to the argument.

---
## Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

This is an excellent and meticulously executed paper. The scientific result—a robust null detection of the galaxy chirality dipole at unprecedented scale—is significant. The methodological contributions, particularly the demonstration of how equivariant averaging removes a large, spurious signal and the detailed modeling of the monopole-mask leakage systematic, are of great value to the field. The author demonstrates an exemplary level of rigor and transparency, anticipating and addressing potential issues, clearly stating limitations, and carefully distinguishing between primary results and secondary diagnostics. The paper sets a high standard for this type of analysis. After addressing the minor points listed above, primarily concerning placeholder dates and artifact linking, the paper will be a strong addition to the literature.