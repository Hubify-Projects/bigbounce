# P4 2026-06-04_1814pt — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 71.1s

---

## Referee Report for Paper P4

**Paper ID:** P4
**Round:** 2026-06-04_1814pt

### General Comments

This paper presents a comprehensive and methodologically detailed analysis of galaxy chirality using a large dataset of 3.2 million spiral galaxies from the DESI Legacy Surveys. The primary scientific result is a null detection of a cosmological chirality dipole (the ℓ=1 axial-vector mode), placing a strong constraint on this potential signature of isotropy violation. A key strength of the work is its rigorous treatment of systematic effects, including the development of an equivariant Test-Time Augmentation (TTA) pipeline to mitigate classifier bias and a detailed investigation of how a small classifier monopole can leak into a spurious dipole signal due to survey geometry. The authors correctly distinguish between the parity-even nature of the dipole observable (an isotropy test) and parity-odd observables (a direct parity test), a subtlety often overlooked in the literature.

While the analysis is exceptionally thorough and the commitment to reproducibility is commendable, the manuscript in its present form is not suitable for publication. Its excessive length (56 pages) and the inclusion of numerous internal project artifacts obscure the main scientific contributions. The paper reads more like an internal technical report than a polished journal article. The revisions required are primarily structural, aimed at improving clarity, conciseness, and professionalism. If these revisions are undertaken, the paper will represent a significant and valuable contribution to the field.

### Findings

#### ESSENTIAL

**P4-E1: Excessive Length and Structure**
*   **Location:** Entire manuscript.
*   **Problem:** At 56 pages, the paper is far too long for a Physical Review D article, even for a methods and catalog paper. The core narrative is diluted by an exhaustive level of detail in the main text, including deep dives into multiple subsidiary null tests, pipeline variants, performance benchmarks, and verbose descriptions of artifacts. This makes the paper extremely difficult to read and obscures the primary scientific results.
*   **Fix:** The paper must be substantially restructured. A main text of approximately 20-25 pages should present the core motivation, the primary methodology (the ViT+TTA pipeline), the headline null result for the dipole, and a concise summary of the investigation that attributes the canonical-mask residual to systematics. The vast amount of supplementary detail—including the full multi-null battery analysis, robustness checks (e.g., pixel-count sweeps), detailed comparisons of different estimators, and full file paths for artifacts—should be moved to appendices or a separate supplementary document.

**P4-E2: Internal Artifacts and Unprofessional Language**
*   **Location:** Throughout the manuscript (e.g., pp. 1, 2, 6, 9, 50).
*   **Problem:** The manuscript is filled with internal project identifiers (`HUBIFY-2026-004`), manuscript version numbers (`v1.0.153`, `paper4-v1.0.153`), and language referring to the review process itself (e.g., "fixed at v1.0.76 of this manuscript"). Full, raw file paths are frequently embedded in the main prose. This is unprofessional and inappropriate for a peer-reviewed journal article.
*   **Fix:** All internal identifiers, version numbers, and references to the manuscript's own evolution must be removed. References to data and code artifacts should be consolidated in the Data Availability section and cited concisely in the text (e.g., "see artifact [ID] in the data release [Ref]").

#### MAJOR

**P4-M1: Title is Overly Long and Technical**
*   **Location:** Page 1.
*   **Problem:** The current title is a multi-line summary of the paper's results rather than a title. It is unwieldy and laden with jargon that is only defined within the paper, making it inaccessible.
*   **Fix:** The title must be shortened to be concise and impactful. A suggested alternative: "A Null Search for a Cosmological Chirality Dipole in 3.2 Million DESI Legacy Spirals". The details about the leakage channel and systematic residuals belong in the abstract.

**P4-M2: Abstract is Overly Dense**
*   **Location:** Page 1.
*   **Problem:** While the abstract is technically accurate, it is a "firehose" of numerical results, sigma values from different nulls, and pipeline-specific jargon. It is nearly impenetrable to a reader not already intimately familiar with the work.
*   **Fix:** The abstract should be rewritten to be more accessible. It should state the high-level scientific conclusions clearly: (1) The paper presents the most sensitive search to date for a cosmological galaxy chirality dipole and finds a null result. (2) It demonstrates how uncorrected systematics can generate spurious signals and quantifies a specific leakage mechanism. (3) It provides a large, publicly available, bias-corrected catalog of galaxy chiralities. The specific numerical values should be reserved for the main text.

#### MINOR

**P4-MI1: Parity-Even vs. Parity-Odd Framing**
*   **Location:** Abstract, Section VI.G.
*   **Problem:** The paper correctly identifies the dipole (ℓ=1) of the projected chirality field as a parity-even, axial-vector observable that tests isotropy. This is a crucial point. However, the paper sometimes retains the language of "parity-violating chirality dipole" for continuity with prior literature. This could cause confusion.
*   **Fix:** While acknowledging the historical terminology is useful, the authors should be more consistent in using the more precise "isotropy-breaking dipole" or "axial-vector dipole" terminology, especially in the abstract and conclusions, to reinforce this important physical distinction.

#### NIT (Nitpicks)

**P4-N1: Duplicate Phrase**
*   **Location:** Page 42, Section F.
*   **Problem:** The text contains a duplicate phrase: "this closes the mask-definition mask-definition robustness question".
*   **Fix:** Remove the duplicated words.

**P4-N2: Formatting and Minor Typos**
*   **Location:** Throughout.
*   **Problem:** There are several minor formatting issues and typos. For example, on page 1, "471 049" should be "471,049". On page 3, the use of multiple em-dashes in a single sentence makes it difficult to parse.
*   **Fix:** The manuscript would benefit from a thorough copy-edit to fix typos, improve punctuation, and ensure consistent formatting.

### Summary recommendation

**MAJOR REVISIONS**

The paper presents a high-quality, rigorous, and important null result in observational cosmology. The detailed treatment of systematics is exemplary and provides a valuable lesson for the field. However, the manuscript is not in a state suitable for publication. The excessive length and poor structure make it difficult to read and obscure the key results. The inclusion of internal project artifacts is unprofessional. The authors must undertake a major restructuring of the paper, condensing the main text to a readable length and moving extensive details to appendices. The title and abstract also require significant revision for clarity and impact. Given the high quality of the underlying scientific work, I recommend that the paper be reconsidered after these major structural revisions have been implemented.