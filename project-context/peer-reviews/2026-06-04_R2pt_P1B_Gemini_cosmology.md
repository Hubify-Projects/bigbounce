# P1B 2026-06-04_R2pt — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 67.4s

---

**Referee Report on HUBIFY-2026-001B**

**Paper:** Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+∆Neff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model
**Author:** Houston Golden

This paper presents three technical analyses intended to support a larger program on Einstein-Cartan-Holst (ECH) cosmology. The analyses are: (1) a stock-CAMB MCMC analysis of the ΛCDM+∆Neff model, reported as a null-consistency test; (2) a Monte Carlo validation of a NaMaster pseudo-Cℓ pipeline for measuring cosmic birefringence; and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper contains several useful and well-scoped technical results. The distinction between pipeline validation and sky detection is clearly and correctly made, as is the disclosure of the fine-tuning required for the spectator-ALP interpretation. The underlying numerical work appears to be sound.

However, the manuscript in its current form is not suitable for publication. It is written in the style of an internal project report or a lab notebook, not a formal scientific paper. It is replete with internal versioning tags, file paths, project management language, and a running commentary on the history of the analysis and previous errors. Furthermore, the structure is deeply flawed, with results from different analyses interleaved in a confusing manner.

The paper requires a complete rewrite to address these fundamental issues of presentation, tone, and structure. While the scientific content is potentially valuable, it is obscured by the unprofessional format. My recommendation is for Major Revisions.

---
### Detailed Findings

#### ESSENTIAL

*   **P1B-E1 (Throughout): Inappropriate Internal Language and Audit Trail.**
    *   **Problem:** The paper is filled with language that belongs in internal documentation, not a scientific publication. This includes references to internal bug-tracking, versioning, and reviewer comments. This severely undermines the professionalism and readability of the manuscript.
    *   **Examples:**
        *   p. 1, fn. a: "(per R-upgraded-round4 GEM-m2 and to preempt the recurring PR3-vs-PR4 reviewer reflag)"
        *   p. 3, fn. a: "Not the stale mid-burn-in diagnostic convergence_gpu_20260305_stale.csv"
        *   p. 3, text: "Earlier internal bookkeeping (corrected fire #25) erroneously quoted..."
        *   p. 4, fn. b: "(R8 GEM-B3 nit)"
        *   p. 7, fn. 4: "(per R-upgraded-round4 GEM-B1 spectator-prose / numerical-scan reconciliation)"
        *   p. 10, fn. 5: "(per R-upgraded-..."
    *   **Required Fix:** Remove all such internal-facing language, audit trails, and meta-commentary. The paper should present the final, verified scientific results and methods in a formal, objective tone. Footnotes containing essential physics caveats (e.g., fn. 4 and 5 on the ALP) must be completely rewritten to remove the internal tags and present the information professionally.

*   **P1B-E2 (Sec. VII, Sec. VIII, Tables III & IV): Reporting on "Ongoing" and "In-Flight" Work.**
    *   **Problem:** The paper reports the status of ongoing calculations, presents project management tables, and discusses future updates as if they are part of the current work. A scientific paper must be a self-contained report of completed and verified work.
    *   **Examples:**
        *   p. 8, Sec. VII: The entire section is a status update, e.g., "The coordinated update ... is in flight for Paper I(a) Table II".
        *   p. 9, Table III: This "Cross-paper status table" with "Readiness" and "Key blocker" columns is a project management tool and has no place in a publication.
        *   p. 9, Table IV: Lists chains as "Ongoing" and "CONVERGED". The caption provides a live-update history of the chain's convergence.
        *   p. 9, "Forward." section: Describes a chain that is currently running and reports its status "as of 2026-05-18 07:53 UTC".
    *   **Required Fix:** Remove all discussion of work that is not complete. The paper should only report on the final, converged chains and frozen results that form the basis of its conclusions. Tables III and IV must be removed. Section VII must be removed or rewritten to be a simple statement of purpose without the status-update language. The "Forward" section must be removed.

#### MAJOR

*   **P1B-M1 (Throughout, esp. Sec. III & V): Flawed Paper Structure.**
    *   **Problem:** The paper's structure is illogical and confusing. Methods are not clearly separated from results. The two distinct MCMC analyses (ΛCDM+∆Neff and w0-wa) are mixed together. For instance, Section III is titled for the ∆Neff MCMC, but the text abruptly pivots to discussing the w0-wa results of Table II. Section V, "Cosmological Fits," appears after the NaMaster analysis and seems to repeat results from Section III.
    *   **Required Fix:** The paper must be completely restructured. A logical flow would be:
        1.  Introduction
        2.  Data and MCMC Methodology (describing all datasets and configurations for both MCMC analyses)
        3.  Analysis 1: ΛCDM+∆Neff Proxy Test (presenting the methods specific to this run and its results, i.e., Table I)
        4.  Analysis 2: Dark Energy Constraints from a w0-wa Model (presenting the results of this separate analysis, i.e., Table II)
        5.  Analysis 3: NaMaster Pipeline Validation
        6.  Analysis 4: Spectator ALP Consistency Check
        7.  Conclusions

*   **P1B-M2 (Throughout): Rewriting of "Corrective" Statements.**
    *   **Problem:** The text frequently references and corrects errors or misleading statements from previous internal drafts or versions of the analysis. This audit trail is inappropriate for a final publication.
    *   **Examples:**
        *   p. 3, fn. 1: "The earlier draft footnote that quoted '123,129 post-burnin' as a both-chains total was an arithmetic error..."
        *   p. 5, text: "An earlier truth-audit falsification argued that the joint posterior mean... was inconsistent..."
        *   p. 6, text: "prior versions described the bias as strictly 'stable across all three injections' at 0.032°, but the 0.342° injection actually gives 0.040°"
        *   p. 9, text: "...correcting the earlier Caγθi product"
    *   **Required Fix:** Remove all such historical corrections. The manuscript should present only the final, correct values and statements without reference to prior mistakes.

*   **P1B-M3 (p. 4, p. 5): Defensive Tone and Internal Verification Language.**
    *   **Problem:** The paper uses a defensive tone and describes verification steps in terms of internal processes and file inspections, rather than standard scientific practice.
    *   **Examples:**
        *   p. 4, text: "...this is the canonical Hubble-tension result, not a YAML omission."
        *   p. 5, text: "...NOT a YAML alias failure..."
        *   p. 4, text: "verified v1B.0.14 by direct .input.yaml inspection"
        *   p. 4, text: "the audit on-record at shoes_yaml_audit.md (under reproducibility/cosmology/)"
    *   **Required Fix:** Rephrase all such statements in a neutral, objective, and scientific manner. For example, instead of describing a YAML audit, simply state the parameters and priors used in the analysis. The results should stand on their own without defensive posturing.

#### MINOR

*   **P1B-m1 (Throughout): Inclusion of File Names and Paths.**
    *   **Problem:** The text contains numerous raw file names and directory paths.
    *   **Examples:** `convergence_latest.csv`, `spin_torsion.input.yaml`, `reproducibility/cosmology/iter2_converged_2026-05-18/`, `pod1_namaster_umap_2026-04-29/`.
    *   **Required Fix:** Remove all such file names and paths from the main body and footnotes. Refer to data products conceptually (e.g., "the convergence statistics," "the input parameter file") and ensure the reproducibility repository is well-documented so users can find the relevant files.

*   **P1B-m2 (p. 1, p. 2): Internal Version Numbers in Text and References.**
    *   **Problem:** The paper includes internal version numbers for itself and its companion papers.
    *   **Examples:** "v1B.0.42" in the dateline, "Paper I(a) v1A.0.22" in the text.
    *   **Required Fix:** Remove all such version numbers. References should point to the archival version (e.g., arXiv ID or journal reference) of the papers, not a specific draft version.

*   **P1B-m3 (p. 3, fn. a): Unprofessional Footnote Content.**
    *   **Problem:** Footnote 'a' of Table I is confusing and contains unnecessary implementation details.
    *   **Problematic Text:** "Sourced from convergence_latest.csv: worst row is ns in the full-tension combination at R̂ − 1 = 9.74 × 10−4..."
    *   **Required Fix:** State the convergence metric simply and directly. For example: "The Gelman-Rubin statistic for all sampled parameters is R̂ − 1 < 3 × 10−3, with the worst-performing parameter being ns in the full-tension case (R̂ − 1 = 9.7 × 10−4)."

---
## Summary recommendation

**MAJOR REVISIONS**

The paper contains a set of potentially valuable and well-scoped technical analyses that could be suitable for publication as a companion paper. However, the manuscript is currently unacceptable due to its pervasive use of internal project-management language, its reporting of ongoing work, its deeply flawed structure, and its unprofessional tone. The author must undertake a complete rewrite to transform the document from a set of research notes into a formal scientific paper. If the author can successfully restructure the paper and excise all the inappropriate content, the underlying scientific contribution may be worthy of publication.