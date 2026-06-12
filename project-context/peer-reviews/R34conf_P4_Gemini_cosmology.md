# P4 R34conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v176.pdf` md5=baa9467c pages=22
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (10125 chars)
**Wall time**: 213.1s

---

## Referee Report

This paper presents a measurement of the cosmic dipole in galaxy chirality using a new, large catalog of 8.47 million galaxies (3.2 million spirals) from the DESI Legacy Surveys DR8. The authors develop a Vision Transformer-based classification pipeline and use a test-time equivariant averaging technique to mitigate systematic biases. The headline result is a null detection of a real-space chirality dipole, consistent with statistical isotropy. The analysis includes an exceptionally thorough investigation of potential systematics, identifying and quantifying a monopole-mask leakage channel in the spherical harmonic domain. The paper provides strong constraints on a physical dipole, disfavoring previous claims of a significant detection.

The methodology is sound, the analysis is rigorous, and the conclusions are well-supported by the evidence presented. The detailed treatment of systematics is a significant contribution and sets a high standard for future work in this area. The paper is suitable for publication in Physical Review D after addressing the following points.

### ESSENTIAL

**P4-E1: Removal of Internal Versioning and Provenance Notes**
*   **Location:** Abstract (p. 1), Sec. IV.D (p. 9, footnote 2), Appendix A (p. 14-16), and elsewhere.
*   **Problem:** The manuscript contains numerous notes about its own revision history, withdrawn results from earlier versions, and internal provenance audits. For example, the abstract states, "An earlier version of this paper reported a MASTER l = 1 null on a subsample mask that a provenance audit traced to a synthetic-footprint catalog; that result is withdrawn (Appendix A) and no conclusion rests on it." Similar notes appear in footnote 2 on page 9 and extensively in Appendix A.
*   **Fix:** All such "lab notebook" style comments, discussions of withdrawn results, and references to the paper's own evolution must be removed. A published scientific paper should be a final, self-contained report of the corrected, definitive analysis. The history of bug fixes and internal audits, while important for the research process, is not part of the scientific result to be published. The paper should simply present the final, validated analysis and results.

**P4-E2: Removal of Internal File Paths**
*   **Location:** Throughout the paper, e.g., Sec. II.B (p. 2), Sec. IV.C.a (p. 7), Table I footnote (p. 5), and many other places.
*   **Problem:** The text is littered with what appear to be internal file paths to analysis artifacts, e.g., `pipelines/p2_chirality/outputs/canonical_provenance/c17_item13_training_semantics.json`. These are not useful to the reader and are unprofessional in a formal publication.
*   **Fix:** Remove all such file paths. If the intent is to aid reproducibility, these links should be part of the documentation in the public code repository, not in the paper itself. The paper can refer to the repository for detailed artifact provenance.

**P4-E3: Data/Code Archiving and Citability**
*   **Location:** Data Availability section (p. 20).
*   **Problem:** The data release plan is not adequate for publication. It refers to future dates ("June 11, 2026", "v2026.04"), a complex and brittle versioning scheme based on commit hashes, and explicitly states, "A persistent archival DOI (Zenodo deposit...) has not yet been minted".
*   **Fix:** For the paper to be accepted, the data, model, and code must be deposited in a permanent, public archive (such as Zenodo or a university repository) and assigned a citable DOI. All future dates must be replaced with the correct, current dates. The versioning information in the paper must point unambiguously to this static, archived version. The statement that the rendered PDF is the "authoritative carrier" of the correct commit hash is not a sustainable or standard practice.

### MAJOR

**P4-M1: Clarification of Comparison to Previous Work**
*   **Location:** Sec. I (p. 2).
*   **Problem:** The introduction states the result is "inconsistent in amplitude with Shamir's claimed ~3% signal by a factor of ~6-12". This comparison is ambiguous. It is unclear if it compares Shamir's amplitude to the measured (null) amplitude in this work or to the sensitivity limit. A comparison to a null result is not meaningful; the comparison must be made against the sensitivity floor or exclusion limit.
*   **Fix:** Rephrase this comparison to be more precise. The paper should state that a signal of the amplitude claimed by Shamir (~3%) is ruled out at high significance by the present analysis. The factor of inconsistency should be based on the ratio of the claimed amplitude to this paper's falsification threshold (e.g., A_95 ≈ 1.0-1.5%), not the measured value of the dipole. For example: "This result is inconsistent with the ~3% signal amplitude claimed in prior work, which our analysis excludes by a factor of ~2-3 (i.e., 3% / A_95)."

### MINOR

**P4-N1: Parity-Even vs. Parity-Odd Terminology**
*   **Location:** Sec. VI.B (p. 13).
*   **Problem:** The text states "the parity-odd signal lives in the l=0 monopole and even-l multipoles." This is correct. However, for clarity, it would be beneficial to explicitly state why the monopole (l=0) is parity-odd.
*   **Fix:** Briefly explain that the monopole represents a global asymmetry in the number count of CW vs. CCW galaxies (N_CW ≠ N_CCW), which is a parity-odd observable, whereas the dipole (l=1) describes a directional variation of this asymmetry, which is parity-even.

**P4-N2: Truncated vs. Rounded Percentages**
*   **Location:** Sec. IV.A (p. 4).
*   **Problem:** The paper states that "percentages truncated rather than rounded at the second decimal". This is an unusual convention. While it is explicitly stated, standard practice is to round.
*   **Fix:** The authors should consider using standard rounding for all quoted values unless there is a strong reason for truncation. If they retain truncation, the justifying note should be kept.

### NIT

**P4-T1: Footnote on Earlier Run**
*   **Location:** Sec. IV.C.a (p. 7, footnote 1).
*   **Problem:** The footnote describes a change in a value (0.43σ -> 0.41σ) due to a "selection-filter defect". This is another instance of version history that should be removed.
*   **Fix:** Remove the footnote. The paper should only report the final, corrected value.

## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, methodologically innovative paper with a significant result for cosmology. The analysis is exceptionally thorough, and the detailed investigation of systematics is a model for the field. The paper is well-structured, and the conclusions are robustly supported. However, it is currently written more like a technical note with a visible development history than a formal journal article. The ESSENTIAL revisions—removing all internal file paths, version history, and future-dated/incomplete data release information—are non-negotiable for meeting the standards of Physical Review D. Once these elements of unprofessional presentation are corrected and the data/code are properly archived with a DOI, the paper will be a strong candidate for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated review, incorporating the new findings from the second, more rigorous pass.

================================================================
## Referee Report

This paper presents a measurement of the cosmic dipole in galaxy chirality using a new, large catalog of 8.47 million galaxies (3.2 million spirals) from the DESI Legacy Surveys DR8. The authors develop a Vision Transformer-based classification pipeline and use a test-time equivariant averaging technique to mitigate systematic biases. The primary result is a null detection of a real-space chirality dipole, consistent with statistical isotropy. The analysis includes an exceptionally thorough investigation of potential systematics, identifying and quantifying a monopole-mask leakage channel in the spherical harmonic domain. The paper provides strong constraints on a physical dipole, disfavoring previous claims of a significant detection.

The methodology is sound, the analysis is rigorous, and the conclusions are well-supported by the evidence presented. The detailed treatment of systematics is a significant contribution and sets a high standard for future work in this area. The paper is suitable for publication in Physical Review D after addressing the following points.

### ESSENTIAL

**P4-E1: Removal of Internal Versioning and Provenance Notes**
*   **Location:** Abstract (p. 1), Sec. IV.D (p. 9, footnote 2), Appendix A (p. 14-16), and elsewhere.
*   **Problem:** The manuscript contains numerous notes about its own revision history, withdrawn results from earlier versions, and internal provenance audits. For example, the abstract states, "An earlier version of this paper reported a MASTER l = 1 null on a subsample mask that a provenance audit traced to a synthetic-footprint catalog; that result is withdrawn (Appendix A) and no conclusion rests on it." Similar notes appear in footnote 2 on page 9 and extensively in Appendix A.
*   **Fix:** All such "lab notebook" style comments, discussions of withdrawn results, and references to the paper's own evolution must be removed. A published scientific paper should be a final, self-contained report of the corrected, definitive analysis. The history of bug fixes and internal audits, while important for the research process, is not part of the scientific result to be published. The paper should simply present the final, validated analysis and results.

**P4-E2: Removal of Internal File Paths**
*   **Location:** Throughout the paper, e.g., Sec. II.B (p. 2), Sec. IV.C.a (p. 7), Table I footnote (p. 5), and many other places.
*   **Problem:** The text is littered with what appear to be internal file paths to analysis artifacts, e.g., `pipelines/p2_chirality/outputs/canonical_provenance/c17_item13_training_semantics.json`. These are not useful to the reader and are unprofessional in a formal publication.
*   **Fix:** Remove all such file paths. If the intent is to aid reproducibility, these links should be part of the documentation in the public code repository, not in the paper itself. The paper can refer to the repository for detailed artifact provenance.

**P4-E3: Data/Code Archiving and Citability**
*   **Location:** Data Availability section (p. 20).
*   **Problem:** The data release plan is not adequate for publication. It refers to future dates ("June 11, 2026", "v2026.04"), a complex and brittle versioning scheme based on commit hashes, and explicitly states, "A persistent archival DOI (Zenodo deposit...) has not yet been minted".
*   **Fix:** For the paper to be accepted, the data, model, and code must be deposited in a permanent, public archive (such as Zenodo or a university repository) and assigned a citable DOI. All future dates must be replaced with the correct, current dates. The versioning information in the paper must point unambiguously to this static, archived version. The statement that the rendered PDF is the "authoritative carrier" of the correct commit hash is not a sustainable or standard practice.

**P4-E4: Unprofessional Language**
*   **Location:** Abstract (p. 1), Sec. I (p. 2), Sec. VII.c (p. 14), and elsewhere.
*   **Problem:** The paper uses phrases like "headline scientific result", "headline finding", "headline exclusion". This is journalistic language, not formal scientific language appropriate for a PRD article.
*   **Fix:** Replace all instances of "headline" with more formal phrasing, such as "primary", "main", or "principal". For example, "The headline scientific result is..." should become "The primary scientific result is...".

### MAJOR

**P4-M1: Clarification of Comparison to Previous Work**
*   **Location:** Sec. I (p. 2).
*   **Problem:** The introduction states the result is "inconsistent in amplitude with Shamir's claimed ~3% signal by a factor of ~6-12". This comparison is ambiguous. It is unclear if it compares Shamir's amplitude to the measured (null) amplitude in this work or to the sensitivity limit. A comparison to a null result is not meaningful; the comparison must be made against the sensitivity floor or exclusion limit.
*   **Fix:** Rephrase this comparison to be more precise. The paper should state that a signal of the amplitude claimed by Shamir (~3%) is ruled out at high significance by the present analysis. The factor of inconsistency should be based on the ratio of the claimed amplitude to this paper's falsification threshold (e.g., A_95 ≈ 1.0-1.5%), not the measured value of the dipole. For example: "This result is inconsistent with the ~3% signal amplitude claimed in prior work, which our analysis excludes by a factor of ~2-3 (i.e., 3% / A_95)."

**P4-M2: Clarity of the Falsification Criterion**
*   **Location:** Abstract (p. 1), Sec. VII.e (p. 14).
*   **Problem:** The abstract and conclusions state the falsification criterion as "a future ≥ 5σ detection at amplitude A ≥ A95". This is slightly confusing. A 5σ detection is a statement about statistical significance, while A ≥ A95 is a statement about the measured amplitude relative to the current experiment's sensitivity. A future experiment could have much better sensitivity, allowing it to detect a signal with A < A95 at >5σ significance. The current phrasing conflates the condition on the signal's amplitude with the condition on its statistical significance.
*   **Fix:** Clarify the logic by separating the two conditions. A better phrasing might be: "A future detection of a dipole with amplitude A ≥ A95 (where A95 is the 95% detection-efficiency threshold of the present analysis), if established at high significance (e.g., ≥ 5σ), would be in tension with this null result." This separates the amplitude threshold (defined by this work's sensitivity) from the statistical significance requirement (a general standard for discovery).

### MINOR

**P4-N1: Parity-Even vs. Parity-Odd Terminology**
*   **Location:** Sec. VI.B (p. 13).
*   **Problem:** The text states "the parity-odd signal lives in the l=0 monopole and even-l multipoles." This is correct. However, for clarity, it would be beneficial to explicitly state why the monopole (l=0) is parity-odd.
*   **Fix:** Briefly explain that the monopole represents a global asymmetry in the number count of CW vs. CCW galaxies (N_CW ≠ N_CCW), which is a parity-odd observable, whereas the dipole (l=1) describes a directional variation of this asymmetry, which is parity-even.

**P4-N2: Truncated vs. Rounded Percentages**
*   **Location:** Sec. IV.A (p. 4).
*   **Problem:** The paper states that "percentages truncated rather than rounded at the second decimal". This is an unusual convention. While it is explicitly stated, standard practice is to round.
*   **Fix:** The authors should consider using standard rounding for all quoted values unless there is a strong reason for truncation. If they retain truncation, the justifying note should be kept.

**P4-N3: Gaussian-Equivalent Sigma**
*   **Location:** Abstract (p. 1), Sec. VII.c (p. 14).
*   **Problem:** The paper quotes a `p_MC` value and then a "Gaussian-equivalent" sigma (e.g., `p_MC=0.030`, `Gaussian-equivalent ≈ 1.9σ`). While this is a common practice, the conversion depends on whether the test is one-sided or two-sided. The convention should be stated explicitly.
*   **Fix:** Add a brief note specifying the convention used for the Gaussian-equivalent sigma (e.g., "computed as the one-sided inverse error function of the empirical p-value").

### ARITHMETIC & TYPOS

**P4-A1: Minor Arithmetic Discrepancy in Table II**
*   **Location:** Table II (p. 5).
*   **Problem:** The `Dev. (σ)` value for Tier A (raw) is listed as `+28.72`. A direct calculation from the other numbers in the row (`(0.507879 - 0.5) / 0.000274`) yields `+28.75`.
*   **Fix:** Please double-check this calculation and correct the value in the table if necessary. The discrepancy is minor and may be due to rounding of un-displayed digits, but it should be verified.

**P4-T1: Footnote on Earlier Run**
*   **Location:** Sec. IV.C.a (p. 7, footnote 1).
*   **Problem:** The footnote describes a change in a value (0.43σ -> 0.41σ) due to a "selection-filter defect". This is another instance of version history that should be removed, per point P4-E1.
*   **Fix:** Remove the footnote. The paper should only report the final, corrected value.

## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, methodologically innovative paper with a significant result for cosmology. The analysis is exceptionally thorough, and the detailed investigation of systematics is a model for the field. The paper is well-structured, and the conclusions are robustly supported. However, it is currently written more like a technical note with a visible development history than a formal journal article. The ESSENTIAL revisions—removing all internal file paths, version history, unprofessional language, and future-dated/incomplete data release information—are non-negotiable for meeting the standards of Physical Review D. Once these elements of presentation are corrected and the data/code are properly archived with a DOI, the paper will be a strong candidate for publication.