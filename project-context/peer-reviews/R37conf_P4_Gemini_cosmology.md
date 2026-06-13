# P4 R37conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v182.pdf` md5=d3785514 pages=23
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (11332 chars)
**Wall time**: 199.9s

---

## Referee Report for "Survey-Scale Galaxy Chirality with Equivariant TTA..."

This paper presents a comprehensive analysis of galaxy chirality using a new, large catalog of 8.47 million galaxies from the DESI Legacy Surveys. The authors employ a Vision Transformer with Test-Time Averaging (TTA) to produce a bias-hardened catalog and perform a detailed search for a cosmic chirality dipole. The primary results are a null detection of a real-space dipole and a thorough characterization of several systematics, most notably a "monopole-mask leakage" channel that can mimic a dipole signal in harmonic-space analyses.

The work is methodologically sophisticated, transparent, and rigorous. The authors' attention to detail in separating primary cosmological estimators from systematics diagnostics, their careful qualification of statistical significance from different null tests, and their open handling of a withdrawn result from a previous analysis version are all commendable and set a high standard for this type of analysis. The paper's main contribution is a robust null result that significantly constrains the amplitude of a potential late-universe chirality dipole, supported by an exhaustive suite of systematics checks.

However, the manuscript requires revisions to meet the publication standards of Physical Review D. Several sections contain internal jargon, confusing references to previous analysis versions, and placeholder information in the data availability statement that must be rectified. The clarity of a few key technical descriptions also needs improvement to ensure the work is fully self-contained and reproducible by the community.

Below is a detailed list of required changes.

---
### Detailed Findings

#### ESSENTIAL

**P4-E1**
*   **Section:** Data Availability (p. 21)
*   **Problem:** The repository and data release information contains future dates and placeholders.
    *   "Repository state for this version: commit 53b41d12 (v1.0.180, June 2026)"
    *   "Catalog: ... Release tag: v2026.04."
*   **Required Fix:** These must be replaced with the actual, final dates, version numbers, and commit hashes corresponding to the version of the manuscript submitted for publication. The use of future-dated placeholders is unacceptable in a final manuscript.

**P4-E2**
*   **Section:** Data Availability (p. 21)
*   **Problem:** The text contains a confusing and methodologically questionable statement about the authority of the PDF versus the code repository.
    *   "One structural consequence of the two-step stamp-then-pin protocol: the \texttt{tex} source stored at the stamp commit necessarily cites the previous version's hash (the pin commit that writes the new hash lands one commit after the stamp), so the rendered PDF, not the in-repo source at the stamp hash, is the authoritative carrier of this pin."
*   **Required Fix:** This statement is opaque and suggests a flawed version control workflow. For a publication in a physics journal, the code repository at the specified commit hash must be sufficient to reproduce the results in the paper. The paper and the repository must be in sync. This entire explanation should be removed and replaced with a clear, standard statement that the cited repository commit corresponds to the analysis presented in the paper.

#### MAJOR

**P4-M1**
*   **Section:** Appendix B.d (p. 17)
*   **Problem:** The text describes a confusing situation where some galaxy probabilities are derived from a "separate raw-catalog inference pass" rather than the main "equivariant pass," leading to inconsistencies.
    *   "These excursions... occur exclusively on rows whose raw probabilities derive from the separate raw-catalog inference pass rather than the equivariant pass (the 88,278-row intersection where both raw legs and the equivariant raw companion columns are populated shows zero violators)..."
*   **Required Fix:** The manuscript must clearly explain why two different inference pipelines were used and why their outputs were mixed in the final catalog. This is a significant potential source of systematic error. The description should be clarified, and the authors should justify why this does not impact the main results, or re-process the affected rows to ensure a uniform pipeline is used for the entire catalog.

**P4-M2**
*   **Section:** Appendix E, Footnote 5 (p. 20-21)
*   **Problem:** The footnote and its reference in the text use what appears to be internal jargon or a typo ("alog C"), and the explanation is extremely dense.
    *   Text (p. 20): "...the Catalog C-full +4.31σ monopole-preserving pre-MASTER pseudo-C(l=1) estimator⁵..."
    *   Footnote 5 (p. 21): "The "monopole-preserving" Catalog-C-full +4.31σ is the single-mode pymaster pseudo-C(l=1) evaluated on the equivariant Catalog C full-footprint fcw field..."
*   **Required Fix:** Please clarify what "alog C" or "Catalog-C-full" means in this context. Is it different from the main "Catalog C"? The footnote should be rewritten for clarity, defining all terms and avoiding overly dense phrasing to ensure an external reader can understand the distinction being made.

**P4-M3**
*   **Section:** Appendix E.d (p. 21)
*   **Problem:** The text analyzes results from an "earlier... estimator convention," which is confusing and irrelevant to the final paper.
    *   "...with per-threshold significances spanning 6.3-8.3σ under the earlier (pre-galaxy-weighted-subtraction) estimator convention of that sweep..."
*   **Required Fix:** All analysis presented in the paper should use the final, declared analysis conventions. Quoting results from outdated conventions is confusing and unnecessary. This sentence should be re-written to report the results of the sweep using the current, final estimator convention, or removed if it is not relevant.

**P4-M4**
*   **Section:** Appendix A.a (p. 15)
*   **Problem:** The description of the field convention uses internal-sounding jargon.
    *   "...copied verbatim from that channel's committed generator (artifact c9a records both field declarations)..."
*   **Required Fix:** Rephrase this for a general scientific audience. Avoid terms like "committed generator." A clearer phrasing would be, for example, "This convention matches the output of the data processing script (see artifact c9a), which..." The goal is to make the procedure understandable without needing access to the internal workings of the authors' pipeline.

#### MINOR

**P4-m1**
*   **Section:** Abstract (p. 1) and Results (p. 9, Table III p. 11)
*   **Problem:** There is a minor inconsistency in the quoted significance for the apodized footprint MASTER residual.
    *   Abstract: "+7.28σ, apodized footprint"
    *   Sec IV.C (p. 9): "+7.28σ for Wp=Nall"
    *   Table III (p. 11): "+7.31" for the same quantity from a higher-statistics 10⁴-permutation run.
*   **Required Fix:** For consistency, use the value from the highest-statistics run (Table III) throughout the manuscript, including the abstract. The text on page 9 already notes the small difference, but the abstract should report the final, most precise value.

**P4-m2**
*   **Section:** Text below Figure 1 (p. 3)
*   **Problem:** The accounting of the training set image counts is difficult to follow.
    *   "the 826-image difference between the source manifest (25,790) and the combined pool (26,616) arises entirely from horizontal-flip augmentation applied to the training split only..."
*   **Required Fix:** Please clarify the arithmetic. For example: "The source manifest contains 25,790 images. For the 80/20 training/validation split, the training portion (20,632 images) was augmented with horizontal flips. After [e.g., removing duplicates or some other step], the final training set size became 21,293 images, for a total pool of 26,616." The current explanation is ambiguous.

#### NIT

**P4-N1**
*   **Section:** Abstract (p. 1)
*   **Problem:** Duplicate phrase.
    *   "...canonical unapodized mask; the 10⁴-permutation canonical unapodized row..."
*   **Required Fix:** Suggest rephrasing to avoid repetition, e.g., "...canonical unapodized mask; the corresponding 10⁴-permutation row in Table III gives..."

---
## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, impactful paper that performs a rigorous and transparent analysis of galaxy chirality. The results are significant for cosmology, and the methodological detail is exemplary. The recommendation for "MAJOR REVISIONS" is not due to any fundamental flaw in the analysis or conclusions, which appear sound. Rather, it is driven by the presence of placeholder information, internal jargon, and several confusing technical descriptions that currently prevent the paper from being a clear, standalone, and reproducible scientific document. Once the authors address the issues listed above—particularly the essential items in the Data Availability section and the major points regarding clarity and consistency—the paper will be an excellent candidate for publication in Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the review you just wrote on this paper:

================================================================
## Referee Report for "Survey-Scale Galaxy Chirality with Equivariant TTA..."

This paper presents a comprehensive analysis of galaxy chirality using a new, large catalog of 8.47 million galaxies from the DESI Legacy Surveys. The authors employ a Vision Transformer with Test-Time Averaging (TTA) to produce a bias-hardened catalog and perform a detailed search for a cosmic chirality dipole. The primary results are a null detection of a real-space dipole and a thorough characterization of several systematics, most notably a "monopole-mask leakage" channel that can mimic a dipole signal in harmonic-space analyses.

The work is methodologically sophisticated, transparent, and rigorous. The authors' attention to detail in separating primary cosmological estimators from systematics diagnostics, their careful qualification of statistical significance from different null tests, and their open handling of a withdrawn result from a previous analysis version are all commendable and set a high standard for this type of analysis. The paper's main contribution is a robust null result that significantly constrains the amplitude of a potential late-universe chirality dipole, supported by an exhaustive suite of systematics checks.

However, the manuscript requires revisions to meet the publication standards of Physical Review D. Several sections contain internal jargon, confusing references to previous analysis versions, and placeholder information in the data availability statement that must be rectified. The clarity of a few key technical descriptions also needs improvement to ensure the work is fully self-contained and reproducible by the community.

Below is a detailed list of required changes.

---
### Detailed Findings

#### ESSENTIAL

**P4-E1**
*   **Section:** Data Availability (p. 21)
*   **Problem:** The repository and data release information contains future dates and placeholders.
    *   "Repository state for this version: commit 53b41d12 (v1.0.180, June 2026)"
    *   "Catalog: ... Release tag: v2026.04."
*   **Required Fix:** These must be replaced with the actual, final dates, version numbers, and commit hashes corresponding to the version of the manuscript submitted for publication. The use of future-dated placeholders is unacceptable in a final manuscript.

**P4-E2**
*   **Section:** Data Availability (p. 21)
*   **Problem:** The text contains a confusing and methodologically questionable statement about the authority of the PDF versus the code repository.
    *   "One structural consequence of the two-step stamp-then-pin protocol: the \texttt{tex} source stored at the stamp commit necessarily cites the previous version's hash (the pin commit that writes the new hash lands one commit after the stamp), so the rendered PDF, not the in-repo source at the stamp hash, is the authoritative carrier of this pin."
*   **Required Fix:** This statement is opaque and suggests a flawed version control workflow. For a publication in a physics journal, the code repository at the specified commit hash must be sufficient to reproduce the results in the paper. The paper and the repository must be in sync. This entire explanation should be removed and replaced with a clear, standard statement that the cited repository commit corresponds to the analysis presented in the paper.

#### MAJOR

**P4-M1**
*   **Section:** Appendix B.d (p. 17)
*   **Problem:** The text describes a confusing situation where some galaxy probabilities are derived from a "separate raw-catalog inference pass" rather than the main "equivariant pass," leading to inconsistencies.
    *   "These excursions... occur exclusively on rows whose raw probabilities derive from the separate raw-catalog inference pass rather than the equivariant pass (the 88,278-row intersection where both raw legs and the equivariant raw companion columns are populated shows zero violators)..."
*   **Required Fix:** The manuscript must clearly explain why two different inference pipelines were used and why their outputs were mixed in the final catalog. This is a significant potential source of systematic error. The description should be clarified, and the authors should justify why this does not impact the main results, or re-process the affected rows to ensure a uniform pipeline is used for the entire catalog.

**P4-M2**
*   **Section:** Appendix E, Footnote 5 (p. 20-21)
*   **Problem:** The footnote and its reference in the text use what appears to be internal jargon or a typo ("alog C"), and the explanation is extremely dense.
    *   Text (p. 20): "...the Catalog C-full +4.31σ monopole-preserving pre-MASTER pseudo-C(l=1) estimator⁵..."
    *   Footnote 5 (p. 21): "The "monopole-preserving" Catalog-C-full +4.31σ is the single-mode pymaster pseudo-C(l=1) evaluated on the equivariant Catalog C full-footprint fcw field..."
*   **Required Fix:** Please clarify what "alog C" or "Catalog-C-full" means in this context. Is it different from the main "Catalog C"? The footnote should be rewritten for clarity, defining all terms and avoiding overly dense phrasing to ensure an external reader can understand the distinction being made.

**P4-M3**
*   **Section:** Appendix E.d (p. 21)
*   **Problem:** The text analyzes results from an "earlier... estimator convention," which is confusing and irrelevant to the final paper.
    *   "...with per-threshold significances spanning 6.3-8.3σ under the earlier (pre-galaxy-weighted-subtraction) estimator convention of that sweep..."
*   **Required Fix:** All analysis presented in the paper should use the final, declared analysis conventions. Quoting results from outdated conventions is confusing and unnecessary. This sentence should be re-written to report the results of the sweep using the current, final estimator convention, or removed if it is not relevant.

**P4-M4**
*   **Section:** Appendix A.a (p. 15)
*   **Problem:** The description of the field convention uses internal-sounding jargon.
    *   "...copied verbatim from that channel's committed generator (artifact c9a records both field declarations)..."
*   **Required Fix:** Rephrase this for a general scientific audience. Avoid terms like "committed generator." A clearer phrasing would be, for example, "This convention matches the output of the data processing script (see artifact c9a), which..." The goal is to make the procedure understandable without needing access to the internal workings of the authors' pipeline.

#### MINOR

**P4-m1**
*   **Section:** Abstract (p. 1) and Results (p. 9, Table III p. 11)
*   **Problem:** There is a minor inconsistency in the quoted significance for the apodized footprint MASTER residual.
    *   Abstract: "+7.28σ, apodized footprint"
    *   Sec IV.C (p. 9): "+7.28σ for Wp=Nall"
    *   Table III (p. 11): "+7.31" for the same quantity from a higher-statistics 10⁴-permutation run.
*   **Required Fix:** For consistency, use the value from the highest-statistics run (Table III) throughout the manuscript, including the abstract. The text on page 9 already notes the small difference, but the abstract should report the final, most precise value.

**P4-m2**
*   **Section:** Text below Figure 1 (p. 3)
*   **Problem:** The accounting of the training set image counts is difficult to follow.
    *   "the 826-image difference between the source manifest (25,790) and the combined pool (26,616) arises entirely from horizontal-flip augmentation applied to the training split only..."
*   **Required Fix:** Please clarify the arithmetic. For example: "The source manifest contains 25,790 images. For the 80/20 training/validation split, the training portion (20,632 images) was augmented with horizontal flips. After [e.g., removing duplicates or some other step], the final training set size became 21,293 images, for a total pool of 26,616." The current explanation is ambiguous.

#### NIT

**P4-N1**
*   **Section:** Abstract (p. 1)
*   **Problem:** Duplicate phrase.
    *   "...canonical unapodized mask; the 10⁴-permutation canonical unapodized row..."
*   **Required Fix:** Suggest rephrasing to avoid repetition, e.g., "...canonical unapodized mask; the corresponding 10⁴-permutation row in Table III gives..."

---
### Additional Findings from Rigorous Re-examination

#### MAJOR

**P4-M5**
*   **Section:** Abstract (p. 1), Table III (p. 11), and Sec. VII.C (p. 14)
*   **Problem:** The paper presents two highly discrepant significance values for the same key systematic diagnostic—the `l=1` residual on the canonical mask—and the explanation is insufficient. The abstract and Sec. VII.C quote `+3.64σ` from a "500-MC direct run," while Table III reports `+7.93σ` from a "10⁴-permutation" run. A >2x difference in significance for the same quantity is alarming. The text attributes this to different null-run sizes and conventions but does not adequately explain why the results are so different or which is more reliable. This inconsistency undermines confidence in the characterization of this crucial systematic.
*   **Required Fix:** The authors must provide a clear, quantitative explanation for this discrepancy. This should include: (1) A precise definition of the two null generation procedures (e.g., "per-pixel random-label permutation" vs. "per-galaxy label-shuffle"). (2) A justification for why they yield such different results for the harmonic-space estimator when they are shown to be similar for the real-space estimator. (3) A clear statement on which null procedure is more physically motivated and statistically robust for this test. The paper should then consistently use the result from the most appropriate procedure, rather than presenting two conflicting values.

#### MINOR

**P4-m3**
*   **Section:** Methods (p. 3)
*   **Problem:** The text states that the GZ1 accuracy floor is propagated to isotropy bounds "via the sub-percent systematic floor in Sec. IV C." This cross-reference is unclear. Section IV C presents the primary dipole null result, while the concept of the sensitivity floor (and its value) is derived and discussed in Section VI A.
*   **Required Fix:** Please clarify the connection between the GZ1 accuracy, the systematic floor, and the final isotropy bound. The reference should be corrected to point to the relevant discussion (likely Sec. VI A), and the sentence should be rephrased to make the logical link more explicit.

---
## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, impactful paper that performs a rigorous and transparent analysis of galaxy chirality. The results are significant for cosmology, and the methodological detail is exemplary. The recommendation for "MAJOR REVISIONS" is not due to any fundamental flaw in the analysis or conclusions, which appear sound. Rather, it is driven by the presence of placeholder information, internal jargon, and several confusing technical descriptions that currently prevent the paper from being a clear, standalone, and reproducible scientific document. Once the authors address the issues listed above—particularly the essential items in the Data Availability section and the major points regarding clarity and consistency—the paper will be an excellent candidate for publication in Physical Review D.