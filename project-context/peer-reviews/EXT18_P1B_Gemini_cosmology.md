# P1B EXT18 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=5a3c98e9 pages=21
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 145.9s

---

**Referee Report for Physical Review D**

**Manuscript ID:** [Assigned by journal]
**Title:** Technical Verification Companion to the ECH Spin-Torsion Program: ACDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model
**Author(s):** Houston Golden

This paper presents three technical analyses intended to support a separate work ("Paper I(a)") on an Einstein-Cartan-Holst (ECH) spin-torsion cosmology. The analyses are: (1) a Markov Chain Monte Carlo (MCMC) analysis of the ΛCDM+ΔNeff model as a proxy for extra radiation, (2) a validation of a pseudo-C_l pipeline for measuring cosmic birefringence, and (3) a consistency check of a spectator Axion-Like Particle (ALP) model against birefringence observations.

The technical quality of the work is exceptionally high. The analyses are performed carefully, with extensive robustness checks and a commendable level of transparency regarding limitations, caveats, and potential systematics. The authors are meticulous in distinguishing between pipeline validation figures and sky-measurement significance, and in quantifying the degree of fine-tuning required in the ALP model. The provision of detailed reproducibility materials is exemplary.

However, the manuscript has several issues that must be addressed before it can be considered for publication in Physical Review D. The most significant are its lack of self-containment, making it difficult to assess as a standalone contribution, and some structural choices that impede clarity.

---

### Detailed Findings

#### ESSENTIAL

*   **P1B-E1: Standalone Readability and Scientific Context**
    *   **Location:** Section I, Page 2, and throughout.
    *   **Problem:** The paper is explicitly framed as a "technical verification companion" to "Paper I(a) [1]". The entire motivation for the presented analyses (e.g., why ΔNeff is a relevant proxy, why birefringence is of interest in an ECH context) is deferred to this other paper. While the technical execution is self-contained, the scientific context is not. A reader cannot understand *why* these specific calculations are being performed without reading another manuscript, which may not be available or peer-reviewed. This violates the principle that a paper in a journal like PRD should be a self-contained contribution.
    *   **Required Fix:** The Introduction (Section I) must be expanded to provide the minimal necessary physical background from Paper I(a). This should include a concise explanation of the ECH spin-torsion framework, why it motivates a search for an effective ΔNeff, and how it relates to cosmic birefringence. The goal is to make the present manuscript intelligible and its scientific relevance clear on its own merits, without requiring the reader to consult reference [1].

#### MAJOR

*   **P1B-M1: Manuscript Structure and Clarity**
    *   **Location:** Section III (page 4) and Section V.C (page 10).
    *   **Problem:** The results of a `w0-wa` analysis (detailed in Table II) are first discussed under "Physics interpretation" in Section III, which is ostensibly about the ΛCDM+ΔNeff MCMC. The main description of this chain is then deferred to Section V.C. This is confusing and disrupts the logical flow. The `w0-wa` analysis is methodologically distinct from the ΔNeff proxy test and should be presented in its own clearly delineated section.
    *   **Required Fix:** Restructure the paper. Create a new, separate section for the `w0-wa` analysis. This section should contain the motivation, methods, results (including the discussion currently on page 4), and caveats for that specific analysis. This will improve the paper's organization and make the distinction between the different analyses clearer.

#### MINOR

*   **P1B-m1: Ambiguous σ-value Comparison in Abstract**
    *   **Location:** Abstract, Page 1.
    *   **Problem:** The abstract states "the ∆Neff extension does not reduce the residual ~3.6σ tension with the SHOES local-distance-ladder H₀". While correct, this 3.6σ is a comparison between two datasets (CMB+BAO+SN vs. SHOES). Later, the abstract mentions the "published Planck/ACT DR6 2.7-2.9σ" detection of birefringence and a "3.6σ headline" from Eskilt & Komatsu [5]. These are null-hypothesis test significances. While the paper is generally excellent at distinguishing these, the abstract places them in close proximity without explicit qualification.
    *   **Required Fix:** Add a clarifying phrase to the abstract to ensure no ambiguity. For example, after mentioning the 3.6σ H₀ tension, add a parenthetical like "(a dataset-discrepancy metric)". This maintains precision and upholds the high standard of statistical clarity demonstrated elsewhere in the paper.

*   **P1B-m2: Inconsistent Use of Minus Sign/Dash**
    *   **Location:** Throughout, e.g., Figure 3 caption (page 7), Table II (page 20).
    *   **Problem:** The paper uses both a standard hyphen-minus (-) and a long dash (–) for subtraction and in parameter names (e.g., `β – βinj`, `w0-wa`). This is inconsistent.
    *   **Required Fix:** Use a standard, consistent typographical symbol for the minus sign in all mathematical expressions and parameter names throughout the manuscript.

*   **P1B-m3: Redundant Information in Bibliography**
    *   **Location:** Bibliography, Page 18, Ref. [25].
    *   **Problem:** The citation for Cobaya reads: "Journal of Cosmology and Astroparticle Physics 05 (057), 057". The "(057)" and "057" are redundant. The year is also missing.
    *   **Required Fix:** Correct the citation to the standard format, e.g., "J. Cosmol. Astropart. Phys. 05 (2021) 057". Review all other references for similar formatting errors.

*   **P1B-m4: Unclear File Path in Reproducibility Section**
    *   **Location:** Page 8, "Reproducibility" paragraph.
    *   **Problem:** The text describing the archived artifacts contains a long, nested parenthetical with file paths: `reproducibility/p1_namaster_500mc/ (mirroring the executed pod run pipelines/h200_results/pod1_namaster_umap_2026-04-29/)`. This is difficult to parse and the "mirroring" language is ambiguous.
    *   **Required Fix:** Rephrase for clarity. State what is in the primary repository path and, if necessary, explain its provenance in a separate, clearer sentence.

#### NIT (Nitpicks)

*   **P1B-N1: Future Date on Manuscript**
    *   **Location:** Page 1.
    *   **Problem:** The manuscript is dated "June 13, 2026".
    *   **Required Fix:** Change the date to the current submission date.

*   **P1B-N2: Equation (1) Template Factor**
    *   **Location:** Page 7, discussion of Eq. (1).
    *   **Problem:** The text states the template fit is to `sin(2β)cos(2β)CEE`. The equation itself shows `sin(4β)CEE,tmpl`. While mathematically proportional (`sin(4β) = 2sin(2β)cos(2β)`), using different forms in the text and equation is slightly confusing.
    *   **Required Fix:** Harmonize the text and the equation. For example, change the text to state the fit is to a template proportional to `sin(4β)CEE`.

*   **P1B-N3: Awkward Phrasing in Footnote 1**
    *   **Location:** Footnote 1, Page 3.
    *   **Problem:** The sentence "The 106,361 figure at 20% is the value reported by GetDist..." is slightly awkward.
    *   **Required Fix:** Rephrase for better flow, e.g., "The 106,361 sample count for a 20% burn-in is the value reported by GetDist...".

---

### Summary recommendation

**MAJOR REVISIONS**

The manuscript represents a significant amount of high-quality technical work. The authors' commitment to rigor, transparency, and reproducibility is outstanding and sets a high standard. However, the paper in its current form is not a standalone scientific contribution, as its entire motivation and context are outsourced to another paper. This is a critical flaw for a publication in Physical Review D. Additionally, the paper's structure can be improved to enhance clarity. Once the essential and major issues are addressed, particularly the lack of self-containment, the manuscript will be a strong candidate for publication.