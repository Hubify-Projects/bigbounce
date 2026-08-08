# P4 R38conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v183.pdf` md5=34b06870 pages=23
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 219.8s

---

**Referee Report: PRD Submission [Paper ID Redacted]**
**Title:** Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)

This paper presents a new, large-scale catalog of galaxy chirality (handedness) for 8.47 million galaxies from the DESI Legacy Surveys DR8, with 3.2 million classified as spirals. The authors use a Vision Transformer (ViT) classifier and introduce a key methodological innovation: test-time equivariant averaging (TTA) to enforce flip-equivariance and mitigate systematic biases. The primary scientific result is a null detection of a real-space chirality dipole, consistent with a statistically isotropic universe. The paper also provides a detailed diagnosis of systematic effects, identifying and quantifying a "monopole-mask leakage" channel that can produce spurious dipole-like signals in harmonic-space analyses.

The analysis is exceptionally thorough, rigorous, and self-critical. The authors maintain a clear and necessary distinction between their primary cosmological estimators and secondary systematics diagnostics. The methodological contributions, particularly the bias-hardening suite and the quantification of the leakage channel, represent a significant advance for this field of study and serve as a template for future large-scale morphology analyses. The conclusions are well-supported by the extensive evidence presented.

The paper is of very high quality and is suitable for publication in Physical Review D after addressing the following points.

---
### **Detailed Findings**

#### **ESSENTIAL**

*   **P21-E1:** **Section: DATA AVAILABILITY (Page 21)**
    *   **Problem:** The repository state is pinned to a future date and a pre-release version number: "commit 53b41d12 (v1.0.180, June 2026)". For a manuscript submitted for publication, all data and code artifacts must be in a persistent, citable, and final state corresponding to the submitted version. Future-dated placeholders are not acceptable for archival purposes.
    *   **Required Fix:** The authors must update the commit hash, version tag, and date to reflect the exact state of the repository at the time of submission. A persistent archival DOI (e.g., from Zenodo or a similar service) for the catalog and code should be provided in the final version of the manuscript, as the authors have indicated is planned.

#### **MAJOR**

*   None.

#### **MINOR**

*   **P2-M1:** **Section: II.B. Training Labels (Page 2)**
    *   **Problem:** The sentence describing the origin of the 826-image difference in the training set is slightly convoluted: "...the 826-image difference between the source manifest (25,790) and the combined pool (26,616) arises entirely from horizontal-flip augmentation applied to the training split only — the validation split (n_val=5,323) is never augmented...". While the meaning can be parsed, it requires careful re-reading.
    *   **Required Fix:** Rephrase for clarity. For example: "The combined source manifest contains 25,790 images. We perform an 80/20 split for training and validation. The training split is augmented with horizontal flips, increasing the total pool size to 26,616 images (N_train = 21,293, N_val = 5,323). The 826-image difference arises from this augmentation of the training set; the validation set is not augmented."

#### **NIT (Cosmetic)**

*   **P15-N1:** **Section: VII. Conclusions (Page 15)**
    *   **Problem:** In section (d), the phrase "pre-MASTER pseudo-C_l" appears twice in the same sentence: "...leakage channel that sources the +6.48σ pre-MASTER pseudo-C_l (the post-MASTER residuals are systematics-attributed; Sec. IV D)."
    *   **Required Fix:** Consider rephrasing to avoid the repetition, for example: "...leakage channel that sources the +6.48σ signal in the pre-MASTER pseudo-C_l power..."

---
### **Verification of Calculations and Claims**

I have spot-checked numerous calculations throughout the manuscript, including significance values, percentages, and asymmetry conversions. All checked calculations were found to be correct and consistent with the data presented in the tables and figures.

*   The distinction between parity-even (l=1 dipole) and parity-odd (l=0 monopole, even-l multipoles) observables is correctly and consistently maintained.
*   The abstract accurately reflects the nuanced findings of the main text, including all necessary caveats. The abstract-last drift sweep (pattern-045) reveals no discrepancies.
*   The juxtaposition of significance values (σ) derived from different null hypotheses is always accompanied by explicit and correct qualifications that they are not directly comparable (e.g., Abstract, Page 9, Table III caption).
*   The figures and tables are clear, well-labeled, and directly support the claims made in the text. Figure 7, in particular, provides a powerful visual demonstration of the paper's core methodological result.
*   The claim of providing the "largest chirality-labeled galaxy catalog to date" appears to be well-founded, exceeding the size of previously published catalogs (e.g., Jia et al. 2023, Shamir 2022b) by a significant margin.

---
## Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

This is an exemplary paper that combines a large astronomical dataset with a sophisticated, robust, and transparent analysis methodology. The scientific result—a null search for a cosmic chirality dipole at unprecedented scale and sensitivity—is significant. Equally important is the paper's methodological contribution, which provides a clear roadmap for controlling subtle systematics in large-scale morphological studies and a compelling explanation for previously reported signals of this type. The work is of high impact and meets the rigorous standards of Physical Review D. Acceptance is recommended once the essential issue regarding the data availability and archival state is resolved.