# P4 RC-INT — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/P4_RC.pdf` md5=a53c7966 pages=24
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 141.9s

---

**Referee Report on "Survey-Scale Galaxy Chirality with Equivariant TTA..."**

This paper presents a search for a cosmic chirality dipole using a new, large catalog of 8.47 million galaxies from the DESI Legacy Surveys, of which 3.2 million are classified as spirals. The authors employ a Vision Transformer with a test-time equivariant averaging (TTA) procedure to classify galaxies as clockwise (CW), counter-clockwise (CCW), or non-spiral. The primary scientific result is a null detection of a real-space chirality dipole, consistent with the standard cosmological model. The paper's main contribution, beyond the null result itself, is an exceptionally rigorous and transparent analysis of systematic effects. It identifies and quantifies a "monopole-mask leakage" channel as a significant contaminant in harmonic-space analyses and establishes a clear falsification criterion for future studies.

The methodology is sound, and the systematics analysis is thorough and serves as a valuable guide for future research in this area. The authors are commendably careful in distinguishing between different estimators and null hypotheses, explicitly stating when and why statistical significances are not directly comparable. The paper is well-structured, and the claims in the abstract are well-supported by the detailed analysis in the body and appendices.

While the paper is of high quality and suitable for publication in Physical Review D, several revisions are required to meet the journal's standards for clarity and reproducibility.

---
### ESSENTIAL Revisions

**P4-E1**
*   **Section/Page:** Title page (p. 1)
*   **Problem:** The paper is dated "June 29, 2026". This is a significant typographical error that must be corrected.
*   **Fix:** Replace the date with the correct submission date.

**P4-E2**
*   **Section/Page:** Throughout the text (e.g., p. 3, 5, 7, 8, 9, 12, 13, 14, 17, 18, 19, 21, 22, 23)
*   **Problem:** The paper makes extensive use of "artifact" pointers to support its claims (e.g., `artifact pipelines/p2_chirality/outputs/canonical_provenance/c17_item13_training_semantics.json`). These are local file paths, not functional hyperlinks. This makes it impossible for a reader to verify the claims or reproduce the analysis directly from the paper, as they would have to manually reconstruct the full URL and navigate the repository structure. This severely undermines the paper's otherwise excellent commitment to reproducibility.
*   **Fix:** Convert every "artifact" pointer into a full, functional hyperlink that points directly to the specific file or directory in the public code repository (e.g., `https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p2_chirality/...`). This is essential for the paper to be a useful and verifiable scientific document.

**P4-E3**
*   **Section/Page:** Data Availability (p. 23)
*   **Problem:** The section states, "A persistent archival DOI (Zenodo deposit of the versioned release) has not yet been minted; until it is, the versioned release tag above is the citable artifact." While this is acceptable for a preprint, a final published version in PRD must have a permanent, citable DOI for the data and code release. The current text is a placeholder.
*   **Fix:** Before publication, the authors must create the archival snapshot of the catalog and analysis artifacts, deposit it in a permanent repository (e.g., Zenodo), and replace the placeholder text with the actual DOI. The text should be updated to reflect that this is the final, citable version.

---
### MAJOR Revisions

*No major revisions are identified. The core scientific content and structure are sound. The essential fixes above are primarily related to reproducibility and presentation.*

---
### MINOR Revisions

**P4-M1**
*   **Section/Page:** Table III Caption (p. 11)
*   **Problem:** The caption contains a typographical error in a unit: "null mean 0.57 × 10¯º". The superscript "º" appears to be a typo for "-6".
*   **Fix:** Correct the unit to `10⁻⁶` to be consistent with the other values in the table and standard scientific notation.

**P4-M2**
*   **Section/Page:** Figure 3 (p. 7)
*   **Problem:** The percentages in the pie chart (CW 18.8%, CCW 19.0%, Not-Spiral 62.2%) are rounded differently from the more precise values given in the text in Sec. IV A (p. 5) (CW 18.787%, CCW 18.987%, NS 62.226%). While the discrepancy is small, it can cause confusion.
*   **Fix:** Either update the figure percentages to match the precision in the text (e.g., 18.79%, 18.99%, 62.23%) or add a note to the caption stating that the values are rounded for display.

**P4-M3**
*   **Section/Page:** Abstract (p. 1) and Sec. III A (p. 3)
*   **Problem:** The abstract contains the sentence: "The +3.64σ value is from a 500-MC direct run on the canonical unapodized mask; the 10⁴-permutation canonical unapodized row in Table III gives +7.93σ; both are systematics-attributed diagnostics from different null-run sizes and mask/weight conventions (Sec. IIIA), not two independent detection claims." This is an excellent and crucial clarification. However, the reference to Sec. IIIA is slightly misplaced, as that section defines notation, while Sec. III B (Declared Analysis Hierarchy) is where the estimators are actually declared and distinguished.
*   **Fix:** While not strictly incorrect, for maximum clarity, consider changing the reference to "(see Secs. IIIA and IIIB)" or simply "(see Sec. IIIB)" to point the reader more directly to the estimator hierarchy declaration.

---
### NIT (Cosmetic)

**P4-N1**
*   **Section/Page:** Sec. IV C, footnote 1 (p. 9)
*   **Problem:** The footnote reads: "Catalog-A pre-MASTER l = 1: single-mode pseudo-C(l=1) on the canonical mask ... with-out MASTER deconvolution, per-pixel label-shuffle null (same estimator family as the canonical Catalog-C +3.64σ result; Sec. IV D)." The phrasing "same estimator family as the canonical Catalog-C +3.64σ result" is slightly awkward.
*   **Fix:** Suggest rephrasing for clarity, for example: "...per-pixel label-shuffle null. This uses the same estimator family as the +3.64σ result for Catalog C (see Sec. IV D)."

---
## Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

This is an exemplary paper that performs a careful, rigorous, and transparent search for a galaxy chirality dipole. The null result is robustly established, and the detailed systematics analysis is a significant contribution to the field. The authors' diligence in qualifying their statistical claims and providing a clear hierarchy of estimators is commendable and sets a high standard for observational cosmology papers. The paper is well-suited for publication in Physical Review D.

The recommendation for acceptance is contingent on the **essential** revisions being addressed. The futuristic date must be corrected, the local file paths must be converted to functional hyperlinks to ensure reproducibility, and a permanent DOI for the data release must be provided for the final publication. The other minor points should also be addressed to improve the paper's final quality.