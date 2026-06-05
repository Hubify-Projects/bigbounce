# P1B 2026-06-04_R4fixed — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 62.6s

---

**Referee Report on Manuscript P1B**

**To the Editor of Physical Review D,**

This manuscript, "Technical Verification Companion to the ECH Spin-Torsion Program...", presents three distinct technical analyses: a proxy MCMC analysis for an extra radiation-like degree of freedom (∆Neff), a validation of a pseudo-Cℓ pipeline for cosmic birefringence, and a consistency check of birefringence data with a spectator axion-like particle (ALP) model. The analyses themselves appear technically sound, and the author is commendably transparent about the scope and limitations of each result.

However, the manuscript in its current form is not suitable for publication. It suffers from significant structural problems, is written in a highly informal and at times conversational tone, and contains numerous internal-facing artifacts such as file paths, version numbers, and project management notes that are inappropriate for a formal scientific paper. A fourth analysis (a w0-wa MCMC run) is interspersed confusingly throughout the text, disrupting the narrative of the three main analyses advertised in the abstract.

While the core technical contributions are valuable, the paper requires a major structural and stylistic overhaul to meet the standards of Physical Review D.

Below is a detailed list of required revisions.

---

### Detailed Findings

#### ESSENTIAL REVISIONS

*   **P1B-E1: Major Structural Reorganization Required**
    *   **Location:** Throughout the manuscript, primarily Sections III and V, and Table II.
    *   **Problem:** The paper's structure is confusing and illogical. The abstract and introduction promise a discussion of three specific analyses. However, a fourth analysis (a `w0wa` fit, presented in Table II and discussed at length) is introduced without proper framing and interrupts the discussion of the primary `ΛCDM+∆Neff` MCMC analysis. Section III introduces the `∆Neff` proxy, but then digresses into the `w0wa` results. Section V, titled "Cosmological Fits and Model Comparison," returns to the `∆Neff` analysis but is again dominated by discussion of the `w0wa` results from Table II. This makes the paper extremely difficult to follow.
    *   **Required Fix:** The paper must be restructured.
        1.  Merge the content of Section III and Section V into a single, coherent section dedicated to the `ΛCDM+∆Neff` MCMC proxy analysis. This section should contain Table I and the corresponding discussion.
        2.  The `w0wa` analysis (currently in Table II and surrounding text) must be handled separately. Either promote it to a fourth, clearly delineated main analysis (requiring updates to the abstract and introduction) or, more appropriately given the paper's stated focus, move the entire `w0wa` analysis (Table II and its discussion) to an Appendix. The "Forward" section in the Conclusion, which discusses this analysis, should be integrated accordingly or removed.

*   **P1B-E2: Removal of Internal "Claims Classification" Table**
    *   **Location:** Page 10, Table III.
    *   **Problem:** Table III, "Claims classification for this companion paper," is a meta-table that appears to be an internal author-facing checklist of the paper's own claims, complete with a "Status" column (e.g., "Verified", "Omitted"). This is entirely inappropriate for a peer-reviewed scientific publication.
    *   **Required Fix:** Remove Table III completely.

*   **P1B-E3: Removal of Internal Artifacts and Project Management Language**
    *   **Location:** Throughout the manuscript.
    *   **Problem:** The paper is littered with internal-facing notes, file paths, version strings, and project management language that have no place in a final publication. This severely undermines the professionalism of the manuscript.
    *   **Examples:**
        *   Page 2, "Paper I(a) v1A.0.22"
        *   Page 3, footnote `a`, "Sourced from convergence_latest.csv"
        *   Page 4, Table II caption, "reproducibility/cosmology/iter2_converged_2026-05-18/"
        *   Page 4, footnote `a`, "the nested-sampling ln B recompute is queued"
        *   Page 5, "pipelines/h200_results/pod1_namaster_umap_2026-04-29/"
        *   Page 9, "and is queued"
    *   **Required Fix:** Scrupulously remove all such internal artifacts. References to reproducibility materials should point to the top-level repository, with any necessary navigation instructions provided in a README file, not hardcoded as file paths in the paper text. Language like "is queued" must be replaced with formal phrasing such as "is left for future work."

#### MAJOR REVISIONS

*   **P1B-M1: Unprofessional and Informal Tone**
    *   **Location:** Throughout the manuscript.
    *   **Problem:** The writing style is often conversational, defensive, and informal, reading more like a lab notebook or a response to reviewers than a formal paper.
    *   **Examples:**
        *   Page 2, footnote 1: "Sample-count stratification (reconciliation)"
        *   Page 3, "note: prior caveat promised a Savage-Dickey ratio... the KDE estimator fails catastrophically"
        *   Page 4, "MB–H0 joint-posterior offset check. A concern was raised..." and "claiming a Cobaya YAML alias failure"
        *   Page 5, "NOT a YAML alias failure"
        *   Page 7, footnote 4: "Backreaction disclosure"
    *   **Required Fix:** Rewrite the entire manuscript in a formal, objective, and academic tone. Defensive posturing ("A concern was raised...") should be replaced with neutral statements of validation ("As a validation check, we verified..."). Informal labels ("disclosure", "reconciliation") must be replaced with standard scientific terminology. The description of why a Savage-Dickey analysis is not viable should be stated formally and consistently (the phrasing on page 9 is much better than on page 3).

*   **P1B-M2: Confusing Presentation of MCMC Sample Counts**
    *   **Location:** Page 2 (footnote 1), Page 3 (footnote 1 cont.), Page 5 (Fig. 1 caption).
    *   **Problem:** The number of MCMC samples for the full-tension run is presented in a confusing manner. The abstract gives a total of 309,189. Page 2 gives raw counts of 176,240 and 132,949. Footnote 1 calculates a post-burn-in count of ~216,432 for both chains, and ~123,368 for the full-tension subset. The caption for Figure 1 then gives a number of 119,617, described as "getdist-thinned". The relationship between these numbers is convoluted and spread across multiple locations.
    *   **Required Fix:** Consolidate and clarify the sample count accounting in a single, clear statement. For example, in the main text where the analysis is first described, state the number of raw samples, the fraction removed as burn-in, the resulting number of post-burn-in samples, and finally the number of effective samples after any thinning, which is the number used for plotting and parameter estimation.

#### MINOR REVISIONS

*   **P1B-m1: Manuscript Date**
    *   **Location:** Page 1.
    *   **Problem:** The manuscript is dated "2026-06-03 PDT," which is a future date.
    *   **Required Fix:** Correct the date to the submission date.

*   **P1B-m2: Informal Footnote Label**
    *   **Location:** Page 1, footnote `a`.
    *   **Problem:** The footnote begins with "Eskilt & Komatsu 2022 disambiguation:". The label "disambiguation" is informal.
    *   **Required Fix:** Remove the label and rephrase the footnote to neutrally explain the dataset versions. E.g., "The analysis in [2] used the Planck PR3+WMAP9 datasets. The public code associated with [2], which we use here, was subsequently updated to use the Planck PR4/NPIPE datasets..."

*   **P1B-m3: Unusual Formatting in Table of Contents**
    *   **Location:** Page 1, Contents.
    *   **Problem:** The entry for Section III has a parenthetical note: "Generic Radiation-Proxy Test (Not a Spin-Torsion Theory Module)". While the clarification is useful, it is unconventional to have such a note directly in the table of contents.
    *   **Required Fix:** Remove the parenthetical from the table of contents. The point is already made clearly and appropriately in the abstract and in the text of Section III.

#### NITS

*   **P1B-n1: Typo**
    *   **Location:** Page 4.
    *   **Problem:** The text reads "verified by direct .input.yaml inspection". There is an extraneous space before the period.
    *   **Required Fix:** Correct to "direct .input.yaml inspection". Consider rephrasing to avoid the raw filename, e.g., "verified by inspection of the input configuration file".

*   **P1B-n2: Typo**
    *   **Location:** Page 5, Section IV.
    *   **Problem:** The "Foreground and noise model" paragraph begins with a hyphen: "Foreground and noise model.-".
    *   **Required Fix:** Remove the hyphen.

---

## Summary recommendation
**MAJOR REVISIONS**

The manuscript presents a set of useful and well-scoped technical verification studies. The author's transparency regarding the limitations of the analyses is a significant strength. However, the paper is not yet in a publishable state due to severe issues with its structure, tone, and the inclusion of inappropriate internal-facing material. The disorganized presentation of the `w0wa` analysis obscures the paper's three primary contributions, and the informal, defensive language detracts from the scientific credibility of the work. If the author undertakes a thorough restructuring and rewriting of the manuscript to address the essential and major points listed above, it could become a valuable contribution to the literature.