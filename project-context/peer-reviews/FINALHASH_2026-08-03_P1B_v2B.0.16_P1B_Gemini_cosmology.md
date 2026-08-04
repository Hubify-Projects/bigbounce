# P1B FINALHASH_2026-08-03_P1B_v2B.0.16 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `arxiv/paper1b_namaster_proof.pdf` sha256=2fb957101604066382ddb604da41b9fe3bc2a48ae4a799ca25c2b34eaac6267a pages=6
**Review packet(s)**: `0ca45797ae2d051381913065ddad17667fa7593131257a843f64ed0a287815ef, 7237cae2b941e671d252be6b35fa51e750e2e948f625d57fdc9c0e15ae2e2c95`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 181.2s

---

**Referee Report: P1B**

**Paper:** namaster-proof: Exact pseudo-Cℓ window inference and content-bound validation for reproducible spin-2 analyses
**Journal:** Journal of Open Research Software

This paper presents `namaster-proof`, a Python package for verifying two specific steps in cosmological spin-2 power spectrum analyses: the application of the bandpower window matrix for a uniform polarization rotation and the content-bound validation of results for reproducibility. The paper is well-scoped, clearly written, and addresses a genuine need for robust validation tools in the field. The methodology is sound, and the author is commendably transparent about the software's capabilities and limitations.

However, several critical issues related to versioning and artifact provenance must be addressed before the paper can be considered for publication.

---
### Detailed Findings

#### ESSENTIAL

*   **P1B-E1**
    *   **Section/Page:** Title Page / p. 1
    *   **Problem:** The title page includes a future date ("July 24, 2026") and an internal manuscript revision number ("manuscript revision v2B.0.16"). These are internal versioning artifacts and are not appropriate for a final publication. While Section 10 explains the distinction between the manuscript version and the software version, such metadata should not appear on the final published document.
    *   **Required Fix:** Remove the manuscript revision number and replace the future date with the final submission or acceptance date.

*   **P1B-E2**
    *   **Section/Page:** 10 (Availability) / p. 5
    *   **Problem:** The "Archive" subsection provides placeholder Zenodo DOIs (e.g., `10.5281/zenodo.21481753`) and future deposition dates ("July 21, 2026"). For a paper centered on reproducibility and provenance, the archival links to the software and manuscript must be real, permanent, and resolvable at the time of publication.
    *   **Required Fix:** Deposit the software and manuscript artifacts in the specified archive (Zenodo), obtain the final DOIs, and update the manuscript with these permanent identifiers. The dates must also be corrected to reflect the actual deposition date.

#### MAJOR

*   **P1B-M1**
    *   **Section/Page:** 10 (Availability) / p. 5
    *   **Problem:** The "Validation artifacts" subsection lists a checksum algorithm as "SHA-250" for the `bandpower` artifact. The standard algorithm is SHA-256. This appears to be a typographical error. An incorrect checksum specification undermines the entire purpose of the content-binding receipt system described.
    *   **Required Fix:** Correct "SHA-250" to the intended algorithm, presumably "SHA-256", and verify that the provided hash is correct for that algorithm.

#### MINOR

None.

#### NIT

*   **P1B-N1**
    *   **Section/Page:** 10 (Availability) / p. 5
    *   **Problem:** The "Operating system" description is slightly awkward: "The package supports Linux and Windows with Python 3.10 and 3.11 and Windows with Python 3.12." The repetition of "Windows" is confusing.
    *   **Required Fix:** Rephrase for clarity. For example: "The package is tested on Linux and Windows with Python versions 3.10 through 3.12."

---
## Summary recommendation

**MAJOR REVISIONS**

The paper presents a valuable and well-designed software tool for improving the reproducibility of cosmological analyses. The text is clear, concise, and appropriately scoped. The author's transparency regarding the software's limitations is a significant strength. However, the paper cannot be accepted in its current state due to critical flaws in its own provenance and reproducibility information. The use of placeholder DOIs, future dates, and a typo in a checksum algorithm are unacceptable for a paper whose core contribution is robust artifact validation. These issues are straightforward to fix but are non-negotiable. Once the essential and major revisions are completed, the paper will be a strong candidate for publication.