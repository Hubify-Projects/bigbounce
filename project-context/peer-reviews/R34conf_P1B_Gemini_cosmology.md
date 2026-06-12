# P1B R34conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.59.pdf` md5=7fbac464 pages=19
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 167.5s

---

**Referee Report for "Technical Verification Companion to the ECH Spin-Torsion Program..."**

This paper presents three technical analyses intended to support a companion paper on Einstein-Cartan-Holst (ECH) cosmology. The analyses are: (1) a stock-CAMB MCMC analysis of the ΛCDM+ΔNeff model as a proxy for new radiation-like physics, (2) a Monte Carlo validation of a NaMaster-based pipeline for measuring cosmic birefringence, and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper is exceptionally transparent regarding its methodology, scope, and limitations. The authors take great care to distinguish between pipeline validation and sky detection, and between model-consistency checks and unique theoretical predictions. The level of detail provided for reproducibility, including disclosure of minor bugs in analysis scripts, is commendable.

However, the paper suffers from significant structural problems that impede readability and from several instances of unprofessional language that are not suitable for publication. The framing as a "companion paper" is also problematic for a self-contained journal article. Major revisions are required to address these issues before the paper can be considered for publication in Physical Review D.

---
### ESSENTIAL

**P1B-E1: Removal of Internal Versioning Language**
*   **Location**: Multiple instances across the paper.
*   **Problem**: The manuscript contains several phrases that refer to its own revision history. This is unprofessional and inappropriate for a final publication.
    *   Page 7, Footnote 3: "...quoted in an earlier draft of this footnote."
    *   Page 9, Section VI: "...an earlier draft quoted [0.2, 1.1] with Δφ/fa ≈ 0.65 at m = H₀ those values do not reproduce from the committed integration and are corrected here)."
    *   Page 10, Section VI: "...an earlier draft quoted [0.17,0.43]° from a joint-trajectory scan for which no artifact survives, and that range is superseded by the committed grid scan."
*   **Required Fix**: Remove all such references to previous drafts, superseded values, and the process of correction. The paper should present only the final, correct results.

---
### MAJOR

**P1B-M1: Paper Structure and Mixing of Analyses**
*   **Location**: Primarily Sections III and IV (pages 3-5).
*   **Problem**: The paper's structure is highly confusing. Section III is titled "Stock-CAMB ΛCDM+ΔNeff MCMC", but it abruptly introduces results from a completely different `w₀wₐ` analysis (which is detailed later in Table II). The "Caveats" on page 4 exclusively discuss this `w₀wₐ` analysis, not the ΔNeff run that is the subject of the section. This mixing of two separate analyses makes the paper extremely difficult to follow.
*   **Required Fix**: The paper must be restructured. The ΛCDM+ΔNeff analysis and the `w₀wₐ` analysis must be presented in separate, sequential sections. Each section should have its own clear description of the model, datasets, and results, including any relevant caveats. The current Section III should be split, with all `w₀wₐ` material moved to a new, dedicated section.

**P1B-M2: Standalone Readability and "Companion Paper" Framing**
*   **Location**: Abstract and Introduction (pages 1-2).
*   **Problem**: The paper is explicitly framed as a "technical verification companion to... Paper I(a) [1]". While context is important, a paper in PRD must be self-contained and motivated on its own terms. A reader should not be required to read another paper (especially a concurrent submission) to understand the scientific motivation for the analyses presented. The "What is NOT in this paper" section, for example, is entirely about the other paper.
*   **Required Fix**: Revise the introduction to provide a concise, self-contained motivation for the three analyses. While it can and should cite Paper I(a) for deeper theoretical background, the introduction must establish *why* a test of ΔNeff, a birefringence pipeline validation, and an ALP consistency check are scientifically interesting in their own right. The abstract and introduction should be rewritten to stand on their own.

**P1B-M3: Analysis with Overlapping Supernova Datasets**
*   **Location**: Page 4, Caveat (e).
*   **Problem**: The `w₀wₐ` analysis combines the DES-SN5YR and Pantheon+ supernova catalogs using a simple product likelihood, which ignores the ~20% of shared events and different systematic treatments. The authors correctly identify this as a source of bias. However, they proceed with this analysis and claim the main qualitative conclusion is "plausibly robust". This is an unquantified assertion. Presenting results from an analysis known to be biased, without quantifying the bias, does not meet PRD standards.
*   **Required Fix**: The authors must either (a) replace this analysis with one of the "queued SN-overlap control chains" mentioned in the text, or (b) perform a quantitative estimate of the bias and demonstrate that it does not affect their conclusions. If neither is possible, the results from this analysis must be much more strongly caveated as preliminary and illustrative, and should not be presented as a primary result of the paper.

---
### MINOR

**P1B-m1: Paper Length**
*   **Location**: Entire manuscript.
*   **Problem**: At 19 pages, the paper is quite long for what amounts to three verification studies. The confusing structure contributes significantly to the length.
*   **Required Fix**: The restructuring required in P1B-M1 should naturally help shorten and focus the paper. The authors should aim for a more concise presentation, targeting a length closer to 12-15 pages, which would be more appropriate for the paper's contribution.

**P1B-m2: Informal Phrasing in Footnote**
*   **Location**: Page 6, Footnote 3.
*   **Problem**: The phrasing "The 'pipeline-recovery SNR= 20.32' figure (and analogously 25.71 for the β = 0.342° injection below) is the template-fit SNR of the driver script..." is somewhat informal.
*   **Required Fix**: Rephrase more formally, for example: "The pipeline-recovery signal-to-noise ratio (SNR), defined as the significance of a template fit to the injected signal, is 20.32 for the β=0.27° injection. This SNR is calculated via..."

---
### NIT (Nitpicks)

**P1B-N1: Future Date on Title Page**
*   **Location**: Page 1, byline.
*   **Problem**: The date of the paper is listed as "June 11, 2026".
*   **Required Fix**: Correct the date to the submission date.

---
## Summary recommendation

**MAJOR REVISIONS**

The paper presents a set of methodologically sound and carefully executed technical analyses. The authors' commitment to transparency, detailed reporting, and reproducibility is exemplary. However, the current manuscript is not acceptable for publication due to severe structural flaws that mix up distinct analyses, making the paper confusing and difficult to read. Furthermore, the reliance on a companion paper for its core motivation and the inclusion of unprofessional internal-review language are inappropriate for a PRD article. The authors must undertake a significant restructuring to create a clear, self-contained, and professionally written manuscript. If these structural and presentational issues are fully addressed, the paper could become a valuable contribution.