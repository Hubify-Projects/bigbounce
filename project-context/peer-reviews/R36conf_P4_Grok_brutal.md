# P4 R36conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v180.pdf` md5=26c9c91f pages=22
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 111.3s

---

**Referee Report**

**Paper:** P4 (PRD) — Survey-Scale Galaxy Chirality with Equivariant TTA… (Golden)

**Findings**

**P4-E1 (ESSENTIAL)**  
Section: Title page / abstract (p. 1) and throughout (e.g., pp. 2, 4, 7, 9, 12, 15–18).  
Problem: Repeated internal-audit / version-control language appears in the body and captions (“An earlier version of this paper reported… that result is withdrawn (Appendix A)”, “superseded”, “provenance audit”, “artifact c11_…json”, “v1.0.180”, “R7/R8”, “dated June 12, 2026”, “manuscript revision v1.0.76”, etc.). These are not scientific content.  
Required fix: Remove every such phrase, filename, commit hash, and version tag from the submitted manuscript. Replace with a clean Data Availability statement only.

**P4-E2 (ESSENTIAL)**  
Section: Abstract (p. 1) vs. body (pp. 4, 7–9, 11).  
Problem: Abstract states a clean “null real-space chirality dipole” (+0.41σ) while the body repeatedly reports +3.64σ, +7.28σ, +7.93σ, etc., residuals in the same canonical mask, then attributes them post-hoc to systematics. The abstract claim is stronger and differently ordered than the final calibrated body statement.  
Required fix: Rewrite abstract to state the primary result together with the explicit systematic floor and the precise falsification threshold used.

**P4-E3 (ESSENTIAL)**  
Section: Table I (p. 5) and all subsequent tables/figures that juxtapose rows (i)–(vii).  
Problem: Multiple null procedures (isotropic bootstrap, block-bootstrap, label-shuffle, depth-stratified, monopole-only generative, etc.) are presented side-by-side with σ values; the required qualifier “not directly comparable across rows” appears only once in a footnote and is not repeated at every juxtaposition.  
Required fix: Add the explicit non-comparability statement in the table caption and at every location where two different-null σ values appear in the same paragraph or figure.

**P4-M1 (MAJOR)**  
Section: Entire manuscript (22 pages).  
Problem: Paper length far exceeds the incremental contribution (a null result plus an 8-anchor systematics audit on an already-published classifier). PRD norm for such a methods/null paper is ≤10–12 pages.  
Required fix: Condense to ≤12 pages; move all but the two primary estimators and the single most diagnostic figure to a concise appendix or separate methods note.

**P4-M2 (MAJOR)**  
Section: Sec. IV D and Appendix D (pp. 9–11, 18–19).  
Problem: The +3.64σ canonical-mask residual is labeled “non-primary” and “systematics-attributed,” yet no quantitative test demonstrates that the residual vanishes once the claimed depth/morphology correlation is removed. The argument is therefore circular.  
Required fix: Provide a controlled test (e.g., morphology-matched or depth-matched re-analysis) that explicitly shows the residual drops below the chosen threshold.

**P4-M3 (MAJOR)**  
Section: Abstract and Sec. VI A (pp. 1, 12).  
Problem: The 50 %-recovery-at-3σ threshold (A₅₀ ≈ 0.75 %) is presented as the falsification boundary, but the Fisher floor calculation (Eq. 4) assumes full-sky coverage while the actual f_sky = 0.494. The numerical mismatch is not propagated.  
Required fix: Recompute the Fisher floor with the actual masked geometry and state the corrected value.

**P4-N1 (MINOR)**  
Section: Fig. 8 caption and Table III (pp. 10–11).  
Problem: Axis labels and table headers mix “apod.” and “canonical” conventions without a one-line legend; readers must cross-reference Appendix A.  
Required fix: Add a compact legend or footnote.

**P4-N2 (MINOR)**  
Section: References (pp. 21–22).  
Problem: Several arXiv IDs and journal citations contain minor transcription inconsistencies (e.g., page numbers, DOI formatting) that do not affect traceability but violate PRD style.  
Required fix: Standardize.

**P4-NIT1 (NIT)**  
Duplicate phrasing (“canonical canonical-mask”) appears once in the rendered text.  
Required fix: Proofread.

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript contains multiple instances of internal bookkeeping language that have no place in a journal submission, presents an abstract whose headline claim is not aligned with the final calibrated body statement, and juxtaposes non-comparable significance values without the required repeated qualification. In addition, the paper is roughly twice the appropriate length for its incremental contribution. These are not cosmetic issues; they prevent a reader from assessing the statistical claims at the standard expected by Physical Review D. A cleaned, condensed resubmission that removes every provenance note, aligns the abstract with the body, and supplies the missing controlled test for the dominant residual would be required before further consideration.