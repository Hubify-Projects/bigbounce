# P4 R56 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R56_P4/chirality_catalog_paper.pdf` md5=? pages=?
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 221.0s

---

**Referee Report on "Survey-Scale Galaxy Chirality with Equivariant TTA..."**

**Report ID:** PRD-2026-XYZ-R1
**Referee:** Anonymous

This paper presents a comprehensive analysis of galaxy chirality using a catalog of 8.47 million galaxies from the DESI Legacy Surveys. The authors develop a Vision Transformer-based classification pipeline with equivariant test-time averaging to produce a catalog of 3.2 million spiral galaxies labeled as clockwise (CW) or counter-clockwise (CCW). The primary scientific result is a null detection of a real-space chirality dipole. The paper includes an exceptionally thorough and rigorous analysis of potential systematics, including a novel demonstration of a "monopole-mask leakage" channel.

The overall quality of the analysis is very high. The authors demonstrate a sophisticated understanding of observational systematics and statistical methods. The clear separation of primary cosmological estimators from systematics diagnostics, and the careful, repeated qualifications regarding the non-comparability of significance values (σ) from different null procedures, are exemplary and should be a model for future work in this area. The methodological finding that a small, uniform classifier bias can couple with survey geometry to produce highly significant but spurious dipole signals is a crucial lesson for the field.

While the work is of high quality, there are several issues that must be addressed before publication can be considered. The most critical is a failure of the reproducibility standard due to the use of placeholder dates and versioning.

## Detailed Findings

### ESSENTIAL

*   **P4-E1**
    *   **Section:** Abstract, Data Availability (Page 1, 22)
    *   **Problem:** The paper is dated "June 26, 2026" on page 1. The Data Availability section on page 22 states "commit 53b41d12 (June 2026)". These are future dates and are clearly placeholders. A paper cannot be published with placeholder dates or commit hashes, as this makes the specific version of the data and code used for the analysis impossible to verify. This is a critical failure of the reproducibility requirement for a data-driven paper.
    *   **Required Fix:** The date of the paper must be updated to the final submission date. The commit hash in the Data Availability section must be updated to the final, frozen commit hash corresponding to the version of the code used to generate all results in the submitted manuscript. The authors must also follow through on their plan to deposit an immutable archival snapshot to a repository like Zenodo and include the resulting DOI in the final manuscript version.

### MAJOR

*   **P4-M1**
    *   **Section:** Entire Manuscript
    *   **Problem:** The paper is 23 pages long. While the appendices contain essential details for reproducibility and validating the authors' claims of rigor, the main body of the paper (pages 1-15) is still quite long for the primary result, which is a null detection. The narrative flow is sometimes interrupted by deep dives into the numerical details of secondary diagnostics that could be moved to an appendix to improve readability.
    *   **Required Fix:** The authors should significantly condense the main text to focus on the primary results and their interpretation. A target of 10-12 pages for the main text seems appropriate. For example, the detailed numerical breakdown of the confidence-cut sweep (end of Sec. IV.C, page 8) and the multiple re-computations of the MASTER significance (Sec. IV.C.b, page 9) could be summarized in the main text with a pointer to the full details in an appendix. The goal should be to present a clear, linear argument in the main text, with the extensive (and excellent) validation work contained in the appendices.

### MINOR

*   **P4-m1**
    *   **Section:** II.A. Galaxy Images (Page 2)
    *   **Problem:** The text describing the imaging campaigns reads: "BASS+MzLS (δ > +32°), DECALS (d<+32°), and a DES overlap region." The symbol for declination in the DECALS description appears to be a "d" rather than the correct Greek letter delta (δ).
    *   **Required Fix:** Ensure consistent and correct typesetting for the declination symbol (δ) throughout the manuscript.

*   **P4-m2**
    *   **Section:** V.A. Shamir (2012, 2020, 2022) (Page 12)
    *   **Problem:** The text states, "the 0.41σ HC (peq > 0.6) simple dipole is well below the 2-4σ dipoles reported by Shamir". This phrasing is ambiguous and could be misinterpreted as comparing significances (σ). The actual comparison, as correctly stated in the introduction (page 2), is between the *amplitude* of the dipole measured in this work (~0.3-0.5%) and the amplitudes reported by Shamir (~2-4%).
    *   **Required Fix:** Rephrase this sentence to make it explicitly clear that the comparison is between dipole *amplitudes* (in units of asymmetry, e.g., percent) and not statistical significances (in units of σ). For example: "...the measured dipole amplitude is well below the 2-4% amplitudes reported by Shamir...".

### NIT

*   **P4-N1**
    *   **Section:** IV.C. Dipole Analysis (Page 7)
    *   **Problem:** Figure 3 is a pie chart that displays the fraction of galaxies in the CW, CCW, and Not-Spiral classes. These exact numbers are already stated clearly in the text in Section IV.A. The figure adds little new information and uses valuable page space.
    *   **Required Fix:** Consider removing Figure 3 to improve the manuscript's conciseness.

*   **P4-N2**
    *   **Section:** Appendix A (Page 16)
    *   **Problem:** The final sentence of Appendix A reads: "the l = 1 row is diagonally dominant".
    *   **Required Fix:** This should be hyphenated: "diagonally-dominant".

## Summary recommendation

**MAJOR REVISIONS**

This is a methodologically superb paper that presents a significant null result in the search for cosmic parity violation. The systematics analysis is state-of-the-art. However, the paper cannot be accepted in its current form due to the essential failure to provide a fixed, verifiable version stamp for the data and code (P4-E1). This must be rectified. Furthermore, the paper would benefit significantly from being restructured and condensed to improve the clarity and impact of its primary conclusions (P4-M1). Once these issues are addressed, the paper will represent a very strong and important contribution to the literature.