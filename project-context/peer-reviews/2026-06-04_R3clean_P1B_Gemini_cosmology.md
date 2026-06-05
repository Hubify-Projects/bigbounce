# P1B 2026-06-04_R3clean — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 67.6s

---

## Referee Report: P1B-2026-06-04_R3clean

**Paper Title:** Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+∆Neff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model

**Journal:** Physical Review D

---

This paper presents three technical analyses intended to support a larger research program on Einstein-Cartan-Holst (ECH) cosmology. The three documented tasks are: (1) a `ΛCDM+∆Neff` MCMC analysis using public codes and data, (2) a validation of a `NaMaster`-based pipeline for CMB E-B deconvolution, and (3) a consistency check between the observed cosmic birefringence signal and a generic spectator axion-like particle (ALP) model.

The technical work within each of the three stated analyses appears to be sound. The pipeline validation (2) is particularly well-scoped, with a clear and crucial distinction made between pipeline signal recovery and on-sky detection significance. The ALP consistency check (3) correctly identifies and quantifies the significant fine-tuning required to maintain the spectator assumption, which is a key physical insight.

However, the manuscript in its current form is not acceptable for publication. It suffers from severe structural problems and is written in a manner that falls far below the professional standards of a scientific journal. The paper reads as an internal technical note or a draft with review comments still embedded, rather than a finished manuscript. A fourth, unrelated analysis is introduced without context, completely disrupting the paper's narrative. The manuscript requires a complete rewrite to address these fundamental issues.

### ESSENTIAL Revisions

These issues must be fully addressed before the paper can be reconsidered for publication.

*   **P1B-E1: Unscoped and Disruptive `w0waCDM` Analysis**
    *   **Location:** Introduced on p. 3, Table II (p. 4), Sec. V (p. 6), and elsewhere.
    *   **Problem:** The paper's title, abstract, and introduction clearly define a scope of three specific analyses. However, a fourth analysis—a `w0waCDM` fit to DESI DR2 and other data (the "iter2" chain)—is introduced abruptly on page 3 and dominates large portions of the text (e.g., Sec. V). This analysis is thematically disconnected from the other three and is not part of the paper's stated goals. Its inclusion makes the paper's structure incoherent and deeply confusing for the reader.
    *   **Required Fix:** The author must choose one of two options:
        1.  **(Recommended)** Completely remove the `w0waCDM` ("iter2") analysis and all associated text, tables (Table II), and discussion. This would make the paper focused and consistent with its stated scope.
        2.  Completely rewrite the paper from the title and abstract onwards to properly frame it as a paper about four analyses, with a clear motivation for why the `w0waCDM` analysis belongs with the other three. This would be a substantially different paper.

*   **P1B-E2: Unprofessional Language and Review Artifacts**
    *   **Location:** Throughout the manuscript.
    *   **Problem:** The paper is littered with internal notes, references to internal file names, issue tracker IDs, and direct responses to previous review cycles. This is entirely inappropriate for a formal publication.
    *   **Examples:**
        *   p. 3, Table I, fn. a: "Sourced from convergence_latest.csv... Not the stale mid-burn-in diagnostic convergence_gpu_20260305_stale.csv... preserved as a transparency artifact only."
        *   p. 3, fn. 2: "The earlier draft footnote that quoted “123,129 post-burnin” as a both-chains total was an arithmetic error..."
        *   p. 3, Physics interpretation: "Earlier internal bookkeeping (corrected fire #25) erroneously quoted..."
        *   p. 4, text: "This addresses earlier reviewer concerns..." and "A concern was raised that..."
        *   p. 10, Table III: The entire "Claims classification" table is an internal project management artifact and has no place in a scientific paper.
    *   **Required Fix:** The author must perform a thorough review of the entire manuscript and remove all such artifacts. The tone must be rewritten to be formal, objective, and suitable for a peer-reviewed journal. Table III must be deleted.

*   **P1B-E3: Inconsistent Reproducibility Materials**
    *   **Location:** Appendix A, p. 8.
    *   **Problem:** The list of reproducibility materials includes code for analyses that are not presented in the paper, such as `galaxy_spins/spin_fit_stan.py` and `data_build/build_galaxy_spin_dataset.py`. The paper states these topics are covered in a future "Paper IV". Their inclusion here is confusing and erroneous.
    *   **Required Fix:** The reproducibility manifest must be corrected to only include materials directly relevant to the analyses actually performed and described in *this* manuscript.

### MAJOR Revisions

*   **P1B-M1: Incoherent Paper Structure**
    *   **Location:** Primarily Sec. III, IV, and V.
    *   **Problem:** Even if the `w0waCDM` analysis were to be properly introduced, the current structure is confusing. Results from the `ΛCDM+∆Neff` MCMC and the `w0waCDM` MCMC are interwoven without clear separation. Section V, "Cosmological Fits and Model Comparison," almost exclusively discusses the `w0waCDM` results, despite this section logically following the `ΛCDM+∆Neff` analysis.
    *   **Required Fix:** The paper must be restructured to present each analysis in a self-contained manner. For example: Section III: `ΛCDM+∆Neff` Analysis and Results. Section IV: `NaMaster` Pipeline Validation. Section V: Spectator ALP Consistency Check. The current mixing of topics must be resolved.

*   **P1B-M2: Key Physical Result Buried in Footnotes**
    *   **Location:** Abstract (p. 1), Sec. VI/VII (p. 7-8), fn. 4 (p. 7), fn. 5 (p. 9).
    *   **Problem:** A key finding of the spectator-ALP analysis is that reconciling the model with the observed birefringence signal requires a `~25x fine-tuning` of the initial misalignment angle to ensure the ALP's energy density does not overclose the universe (i.e., to remain a "spectator"). This is a significant physical constraint on the model. However, this result is primarily discussed in footnotes and mentioned only briefly in the abstract and conclusions.
    *   **Required Fix:** This fine-tuning argument is a main result and should be elevated from the footnotes into the main body of Section VI. The physical implications should be discussed clearly in the main text and summarized prominently in the conclusions.

### MINOR Revisions

*   **P1B-m1: Informal File Path References**
    *   **Location:** p. 5, "Reproducibility" paragraph.
    *   **Problem:** The text references a full, specific directory path: `pipelines/h200_results/pod1_namaster_umap_2026-04-29/`. This is too specific and brittle.
    *   **Required Fix:** Refer to the location of the materials conceptually within the main repository link provided elsewhere (e.g., "The relevant scripts and data are available in the `pipelines` directory of the repository [ref].").

*   **P1B-m2: Unprofessional Capitalization**
    *   **Location:** p. 7, fn. 4; p. 9, fn. 5.
    *   **Problem:** Words like "RETAINED" and "NOT" are capitalized for emphasis. This is stylistically inappropriate for a formal publication.
    *   **Required Fix:** Remove the unnecessary capitalization and convey emphasis through prose.

*   **P1B-m3: Footnote in Abstract**
    *   **Location:** p. 1, Abstract, footnote `a`.
    *   **Problem:** Placing a detailed dataset disambiguation in a footnote to the abstract is unconventional. The note that "The repository README is the authoritative source" is also not standard academic prose.
    *   **Required Fix:** Move the content of this footnote to the main body of the paper, for instance, in the Datasets and Configuration section (e.g., Sec. V A).

### Paper Length and Scope

The paper's length (11 pages) is not an issue. If the extraneous `w0waCDM` analysis is removed as recommended, the paper will be shorter and more focused, which is appropriate for a "technical verification companion". The core issue is not length but the inclusion of unscoped content and a complete lack of professional polish.

---

## Summary recommendation

**MAJOR REVISIONS**

The paper contains three useful and technically sound verification analyses that are worthy of publication. However, the manuscript is presented in a completely unacceptable state. It is structurally incoherent due to the inclusion of an unmotivated fourth analysis and is filled with unprofessional language and internal review artifacts that should have been removed long before submission. The paper requires a complete rewrite to bring it to a publishable standard. I recommend that the author remove the `w0waCDM` analysis to create a focused, coherent paper, and then perform a thorough edit to remove all unprofessional content and restructure the text logically.