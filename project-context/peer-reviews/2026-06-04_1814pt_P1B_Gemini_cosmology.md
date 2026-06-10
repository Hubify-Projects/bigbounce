# P1B 2026-06-04_1814pt — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 75.1s

---

## Referee Report on HUBIFY-2026-001B

**Paper:** Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+∆Neff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model
**Round:** 2026-06-04_1814pt

This paper presents three technical analyses intended to support a broader program on Einstein-Cartan-Holst (ECH) cosmology. The analyses are: (1) a standard ΛCDM+∆Neff MCMC analysis, reported as a null-consistency test; (2) a Monte Carlo validation of a NaMaster-based pseudo-Cℓ pipeline for cosmic birefringence; and (3) a consistency check of the observed birefringence signal with a standard spectator axion-like particle (ALP) model.

The scientific content and the core analyses appear to be sound. The author is commendably careful in defining the scope and limitations of each analysis. For instance, the distinction between a generic radiation-proxy test and a direct test of ECH theory is made clear, as is the distinction between pipeline-recovery signal-to-noise and on-sky detection significance. The disclosure of the fine-tuning required in the spectator-ALP model is also a point of strength.

However, the manuscript in its current form is entirely unsuitable for publication in a scientific journal. It is written not as a formal, archival paper, but as an internal, "live" technical note for a project. It is replete with internal version numbers, audit tags, filenames, file paths, references to previous errors in the document, and status updates on ongoing computational jobs. Entire sections and tables are dedicated to cross-paper project management, which has no place in a final publication.

While the underlying work may be of publishable quality, the manuscript requires a complete and thorough rewrite to remove all non-scientific, non-archival content and to adhere to the standards of a formal scientific publication.

---
### Findings

#### ESSENTIAL

*   **P1B-E1: Removal of all internal audit tags, review artifacts, and process notes.** The manuscript is filled with language that appears to be from an internal review process. This is unprofessional and must be completely removed. The paper should present the final, verified results, not the history of their verification.
    *   **Location:** Page 1, Footnote a.
    *   **Problem:** Text reads: "(per R-upgraded-round4 GEM-m2 and to preempt the recurring PR3-vs-PR4 reviewer reflag)".
    *   **Fix:** Remove this entire parenthetical note. The footnote should begin with "The published PRD paper...".
    *   **Location:** Page 3, Physics interpretation.
    *   **Problem:** Text reads: "(corrected fire #25)".
    *   **Fix:** Remove the tag.
    *   **Location:** Page 4, Table II, Footnote b.
    *   **Problem:** Text reads: "(R8 GEM-B3 nit)".
    *   **Fix:** Remove the tag.
    *   **Location:** Page 5, MB-H0 joint-posterior offset check.
    *   **Problem:** Text reads: "An earlier truth-audit falsification argued...".
    *   **Fix:** Rephrase to state the physical point directly without referencing internal audits. E.g., "A direct check of the posterior against the Pantheon+ constraint clarifies the origin of the Hubble tension in this model."
    *   **Location:** Page 7, Footnote 4.
    *   **Problem:** Text reads: "(per R-upgraded-round4 GEM-B1 spectator-prose / numerical-scan reconciliation)".
    *   **Fix:** Remove this tag.
    *   **Location:** Page 10, Appendix C, Footnote 5.
    *   **Problem:** Text reads: "(per R-upgraded-round4 GEM-B1, cross-link to footnote 4 in Sec. VI)".
    *   **Fix:** Remove this tag. The footnote on page 11 is a duplicate and should also be removed.

*   **P1B-E2: Removal of all references to prior errors and draft versions.** The paper frequently refers to errors in previous versions or drafts. A published paper should be the final, corrected version of record; the process of arriving at it is not part of the paper itself.
    *   **Location:** Page 3, Footnote 1.
    *   **Problem:** Text reads: "The earlier draft footnote that quoted '123,129 post-burnin' as a both-chains total was an arithmetic error...".
    *   **Fix:** Remove this sentence and simply state the final, correct sample counts.
    *   **Location:** Page 3, Physics interpretation.
    *   **Problem:** Text reads: "Earlier internal bookkeeping ... erroneously quoted '98.6% quintom-B' weight...".
    *   **Fix:** Remove this and state the correct result for the converged chain.
    *   **Location:** Page 6, NaMaster results.
    *   **Problem:** Text reads: "(prior versions described the bias as strictly 'stable across all three injections' at 0.032°, but the 0.342° injection actually gives 0.040°)".
    *   **Fix:** Remove the parenthetical. State the final finding directly: "The absolute bias is small (0.032°-0.040°) and scales mildly with the injected amplitude."

*   **P1B-E3: Removal of all "live document" status updates and language.** The paper is written as if it is a living document, with updates on runs that are "ongoing", "queued", or have just "converged". A scientific paper must report on completed work.
    *   **Location:** Abstract.
    *   **Problem:** "...plus a third Planck-only combination ongoing".
    *   **Fix:** Remove this phrase. The abstract should only summarize the completed, converged analyses.
    *   **Location:** Page 4, Text.
    *   **Problem:** "this is queued for v1B.0.15+ pending a separate pod-side nested-sampling run".
    *   **Fix:** Remove this. Simply state that the calculation requires nested sampling and was not performed in this work.
    *   **Location:** Section VII (Page 8).
    *   **Problem:** This entire section is a status update. Phrases like "what remains pending", "queued for v1B.0.16+", "The coordinated update ... is in flight" are unacceptable.
    *   **Fix:** Remove Section VII entirely. The paper must be self-contained and not serve as a "cross-paper anchor" for another manuscript's footnote. If the w0wa results are to be used, they should be presented as final results in Section V/VIII.
    *   **Location:** Page 9, Table IV Caption and Status column.
    *   **Problem:** The table lists jobs as "Ongoing" and "CONVERGED". The caption gives a detailed history of the convergence of a specific run with timestamps.
    *   **Fix:** Remove the "Status" column. Remove the narrative from the caption. The table should simply list the final properties (dataset, parameters, N_samples, R-1) of the completed runs used in the paper. Unconverged/ongoing runs should not be included.
    *   **Location:** Page 9, "Forward" paragraph.
    *   **Problem:** This entire paragraph describes an ongoing run and its "Current status".
    *   **Fix:** Remove this paragraph entirely.
    *   **Location:** Page 10, "back into the cross-paper P1(a) Sec. Structural Tension headline...".
    *   **Problem:** More project management language.
    *   **Fix:** Remove this paragraph.

*   **P1B-E4: Removal of project management tables.** The paper contains tables that serve an internal project management function, not a scientific one.
    *   **Location:** Page 9, Table III.
    *   **Problem:** "Cross-paper status table" lists versions, "Readiness", and "Key blocker". This is entirely inappropriate for a publication.
    *   **Fix:** Remove Table III.
    *   **Location:** Page 11, Table V.
    *   **Problem:** "Claims classification for this companion paper" is a self-referential table that classifies the paper's own claims. This is not standard scientific practice.
    *   **Fix:** Remove Table V.

*   **P1B-E5: Removal of raw filenames and file paths.** The text and footnotes contain raw filenames and directory paths, which is not appropriate for formal publication.
    *   **Location:** Page 3, Footnote a.
    *   **Problem:** "Sourced from convergence_latest.csv", "convergence_gpu_20260305_stale.csv".
    *   **Fix:** Describe the source of the information (e.g., "from the chain's convergence diagnostics") without giving filenames.
    *   **Location:** Page 4, Table II Caption.
    *   **Problem:** "...chain manifest at reproducibility/cosmology/iter2_converged_2026-05-18/".
    *   **Fix:** This information belongs in a formal Data Availability statement, not in a table caption. It should be presented as a URL or a reference to the repository.
    *   **Location:** Page 4, Text.
    *   **Problem:** "...audit on-record at shoes_yaml_audit.md (under reproducibility/cosmology/)".
    *   **Fix:** Remove this.

#### MAJOR

*   **P1B-M1: Broken internal references.** The paper contains references to sections or tables that do not exist, likely artifacts of the drafting process.
    *   **Location:** Page 4, Table II, Footnote a.
    *   **Problem:** Reference to "§ Headline-result discussion". This section does not exist.
    *   **Fix:** Correct the reference to point to the relevant discussion in the main text, or remove it.
    *   **Location:** Page 6, Section V.B.
    *   **Problem:** Reference to "Table 1B". This table does not exist.
    *   **Fix:** Correct the reference or remove it.

*   **P1B-M2: Reporting on unconverged MCMC runs.** The paper repeatedly mentions a Planck-only run that is "ongoing" with R-1 ~ 0.05.
    *   **Location:** Abstract, Section VIII, Table IV.
    *   **Problem:** Results from unconverged chains should not be included in a final publication, even as a side note. It gives the paper an unfinished feel and adds no scientific value.
    *   **Fix:** Remove all mentions of this ongoing, unconverged run. The paper should be based solely on the two frozen, converged dataset combinations.

*   **P1B-M3: Future-dated analysis.**
    *   **Location:** Page 6, first paragraph.
    *   **Problem:** The text states a NaMaster run was performed in "(run, April 2026)". This is a future date.
    *   **Fix:** Correct this date. If it is a placeholder, the work is not complete and should not be in the paper. If it is a typo, it must be fixed.

#### MINOR

*   **P1B-m1: Internal versioning in text.** The paper is littered with internal version numbers for the manuscript itself and its dependencies.
    *   **Location:** Page 1, Dated line ("v1B.0.42"); Page 2, Intro ("v1A.0.22"); Page 3, Caveats ("v1B.0.14"); Page 4, Text ("v1B.0.14"); etc.
    *   **Fix:** Remove all such version numbers from the manuscript body and metadata. The journal will assign its own identifiers.

*   **P1B-m2: Code snippets in prose.** The text contains phrases that look like code arguments rather than descriptive prose.
    *   **Location:** Page 5, Section IV.
    *   **Problem:** "beam=bPlanck_l w_l^pix", "purify_b=True, purify_e=False".
    *   **Fix:** Describe these settings in prose or typeset them properly as mathematical expressions. For example, "The field is initialized with the Planck beam and the corresponding pixel window function." and "B-mode purification is enabled to suppress E-to-B leakage."

*   **P1B-m3: Typo in physics argument.**
    *   **Location:** Page 7, end of page.
    *   **Problem:** The text states "∆ϕ/fa ∝ θi along the underdamped trajectory". The symbol for the initial misalignment angle is θ_i, not θ.
    *   **Fix:** Correct the typo to read "∆ϕ/fa ∝ θ_i".

*   **P1B-m4: Repetitive text.**
    *   **Location:** Page 6, Section V.B.
    *   **Problem:** The paragraph on model-comparison statistics repeats the same point about the Savage-Dickey ratio being non-viable and nested sampling being required several times.
    *   **Fix:** Condense this paragraph to state the point once, clearly.

#### NIT

*   **P1B-N1: Inconsistent section formatting.**
    *   **Location:** Page 6, Section V.B.
    *   **Problem:** The section is "B. Results", but the first paragraph is labeled "a.".
    *   **Fix:** Remove the "a." to make the formatting consistent.

---
## Summary recommendation
**MAJOR REVISIONS**

The scientific analyses presented in this paper appear to be sound, correctly performed, and appropriately scoped. The author demonstrates a clear understanding of the limitations of the methods and is transparent about important caveats, such as model fine-tuning. However, the manuscript is written in the style of an internal, collaborative technical note, not a formal scientific paper for archival publication. It is filled with project management language, status updates, internal audit tags, and other non-scientific content that renders it unpublishable in its current state.

A major revision is required, which must involve a complete rewrite of the manuscript to remove all such artifacts. The author should focus on presenting the completed scientific work in a self-contained, professional, and archival manner. If this is done, the underlying scientific contribution is likely worthy of publication.