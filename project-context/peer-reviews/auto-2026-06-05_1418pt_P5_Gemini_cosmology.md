# P5 auto-2026-06-05_1418pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (3692 chars)
**Wall time**: 152.6s

---

## Referee Report on "Environmental Dependence of Spiral Chirality" by H. Golden

**Paper ID:** P5
**Journal:** Physical Review D

This paper investigates the statistical dependence of spiral galaxy chirality on large-scale structure environment, using a cross-match between a new 8.5M-galaxy chirality catalog and the DESI Data Release 1. The primary analysis method involves classifying galaxies into cosmic-web environments (void, wall, filament, cluster) and testing for variations in the clockwise (CW) fraction. The headline result is a null detection: spiral chirality is found to be independent of environment, with observed deviations being consistent with a previously reported catalog-wide systematic offset. The analysis is supported by an extensive set of robustness checks, including multiple environment finders (V-Web, DESIVAST, Tempel+2014), sensitivity sweeps, and systematic tests.

The work is thorough and the statistical treatment is generally of high quality. The authors have performed a commendable number of cross-checks to validate their null result. However, there are several essential and major issues that preclude publication in its present form.

---
### Detailed Findings

#### ESSENTIAL REVISIONS

**P5-E1: Foundational Reliance on Non-Peer-Reviewed Companion Work (Paper IV)**
- **Location**: Abstract (p.1), Section II (p.2), and throughout the manuscript.
- **Problem**: The entire analysis is predicated on the validity of the chirality catalog and, more critically, the classifier-monopole offset (`Δfcw = -0.0026`) derived in "Paper IV [3]". This source is cited as "companion work, not yet peer-reviewed" and "in preparation". A manuscript submitted to PRD cannot have its central claims and inputs be fundamentally dependent on an unpublished, un-reviewed, and inaccessible result. This makes the present work's conclusions conditional and unverifiable by the standards of this journal.
- **Required Fix**: The paper can only be considered for publication after Paper IV has been accepted for publication in a peer-reviewed journal. In the interim, the authors must, at a minimum, provide a self-contained summary of the relevant methods and results from Paper IV in an appendix. This appendix must include: (1) a brief description of the classifier architecture and training procedure; (2) the method for establishing the `Δfcw = -0.0026` offset and its uncertainty; and (3) the evidence supporting its interpretation as a classifier systematic rather than a cosmological signal. The current text treats these crucial inputs as given, which is unacceptable.

#### MAJOR REVISIONS

**P5-M1: Insufficiently Prominent Caveat on Redshift-Space Distortions (RSDs)**
- **Location**: Section XIII (p.18); relevant to all V-Web analysis in Sections IV-VII, IX, X.
- **Problem**: The V-Web analysis, which constitutes a large fraction of the paper, is performed in redshift space. The impact of RSDs on the tidal tensor classification is a significant systematic that anisotropically deforms the measured field. While this is discussed in the "Limitations" section, its importance is understated in the main body where the V-Web results are presented. The reader is not made aware of this major caveat until the end of the paper. The order-of-magnitude estimates provided are helpful but are not a substitute for a proper treatment or a more prominent warning.
- **Required Fix**: A dedicated subsection on RSDs must be added to the V-Web methods section (Section IV). This section should state upfront that the analysis is in redshift space and briefly explain the expected anisotropic effects on the tidal tensor eigenvalues (e.g., Kaiser squashing, Fingers-of-God). It should reference the more detailed discussion now in the Limitations section. This ensures the reader correctly contextualizes the V-Web results as they are presented.

**P5-M2: Paper Length and Narrative Structure**
- **Location**: Entire paper.
- **Problem**: At 20 pages, the paper is excessively long for what is ultimately a confirmation of a null hypothesis. While the robustness checks are a strength, the narrative flow is convoluted, with a complex interplay of "primary" vs "secondary" analysis paths, multiple re-analyses, and cross-checks that obscure the main result. The core, most robust finding is the DESIVAST-anchored null test (Sec VIII) and the demonstration that other signals are consistent with the Paper IV monopole (Sec XII.F).
- **Required Fix**: The authors must significantly restructure and shorten the paper to improve clarity and impact. A suggested structure:
    1. Introduction.
    2. Data & Methods (combining chirality catalog summary, DESI data, and a brief overview of classifiers).
    3. The Primary Environmental Test: A Null Result in DESIVAST Voids (presenting the cleanest, most robust result from Sec VIII and XI first).
    4. Consistency Checks and Systematic Controls (condensing the V-Web, Tempel, ASTRA, tracer-program, and sky-position analyses into a single, focused section that demonstrates the robustness of the primary result).
    5. Discussion & Conclusion.
This would streamline the narrative, prioritize the strongest evidence, and reduce the total length to a more appropriate ~12-15 pages.

**P5-M3: Use of Future Dates and Placeholder References**
- **Location**: Abstract (p.1, dated June 4, 2026), Section IX B (p.15), References [11], [12], [13].
- **Problem**: The manuscript is dated "June 4, 2026" and cites several key papers with future publication years (2025, 2026) and what appear to be placeholder arXiv IDs. This is unprofessional and inappropriate for a formal journal submission. It gives the strong impression of a preliminary draft.
- **Required Fix**: All dates must be updated to the time of submission. All references must be to publicly available papers (on arXiv or in a journal). If the cited works are not yet public, they must be cited as "in preparation" or "private communication," and cannot be load-bearing. The date of the manuscript itself must be the submission date.

#### MINOR REVISIONS

**P5-m1: Clarification of `sigma_null,p99` in Table V**
- **Location**: Table V (p.8).
- **Problem**: The column header `sigma_null,p99` is ambiguous. It appears to represent the 99th percentile of the *maximum absolute sigma* statistic across all pixels from the label-shuffle simulations.
- **Required Fix**: Change the column header to a less ambiguous notation like `|σ|_max^null(p99)`. Add a sentence to the caption clarifying: "The `σ_null,p99` column gives the 99th percentile of the maximum absolute deviation (`|σ|max`) found across all pixels in a single simulation, drawn from 1,000 label-shuffle realizations."

**P5-m2: Inconsistent Use of `σ` Notation**
- **Location**: Throughout.
- **Problem**: The paper uses `σ` to denote statistical significance (e.g., `-4.66σ`). However, `σ` is also used in standard cosmological contexts for physical dispersions (e.g., `σ_v` for velocity dispersion, `σ_rsd` for RSD displacement). While generally clear from context, this can lead to confusion.
- **Required Fix**: For clarity and precision, the authors should consider using `z` or `S` for the significance value (e.g., `z = -4.66`) to distinguish it from physical dispersions. If they elect to retain `σ`, they must add a footnote at its first use clarifying that it denotes statistical significance in units of standard deviations from the null hypothesis.

#### NITPICKS (COSMETIC)

**P5-N1: Typo in Abstract**
- **Location**: Abstract (p.1).
- **Problem**: "none reach 30 after look-elsewhere correction". The number should be `3σ`.
- **Required Fix**: Change "30" to "3σ".

**P5-N2: Typesetting Error in Figure 6**
- **Location**: Figure 6 caption and likely figure panel (p.14).
- **Problem**: The text contains typesetting errors: "Chirality ofrom half peYqPpirals ≥ 206...". The caption text also reads "per-pixel chirality ofrom half".
- **Required Fix**: Correct the text to "σ from half" in the caption and ensure the corresponding label in the figure panel is corrected.

**P5-N3: Awkward Phrasing in Table III Caption**
- **Location**: Table III caption (p.6).
- **Problem**: "Per-quintile σobs - σpred residual table."
- **Required Fix**: Rephrase for better readability, e.g., "Residuals between the observed significance (σobs) and the monopole-predicted significance (σpred) for each density quintile."

---
### Summary recommendation

**MAJOR REVISIONS**

This paper presents a comprehensive and statistically rigorous null test for the environmental dependence of spiral galaxy chirality. The depth of the analysis, particularly the extensive suite of robustness checks and systematic tests, is a significant strength. The primary result, anchored on the clean and large DESIVAST void catalog, is a robust null finding.

However, the paper cannot be accepted in its current form due to one essential and several major issues. The most critical is its foundational reliance on "Paper IV," a companion work that is not yet peer-reviewed, which makes the present manuscript's results unverifiable. Furthermore, the extensive V-Web analysis is performed in redshift space, and the impact of RSDs is not given sufficient prominence in the main text. Finally, the paper's excessive length and convoluted structure detract from the clarity of its otherwise strong core message, and the use of future dates and placeholder citations is unprofessional.

I recommend that the paper undergo major revisions to address these points. The authors must provide a self-contained validation of the inputs from Paper IV (or wait for its publication), restructure the manuscript for clarity and brevity, and give the RSD caveat its due prominence. Once these significant issues are addressed, the paper will represent a valuable and robust contribution to the field.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a more rigorous, second-pass review of the paper.

---
### Additional Findings from Second-Pass Review

**A. ARITHMETIC**

**P5-M4: Major Arithmetic and Consistency Error in Figure 7**
- **Location**: Figure 7 (p.16) and associated text in Section IX.A (p.14).
- **Problem**: There is a significant and contradictory error regarding the "filament concordance" between the V-Web and Tempel+2014 classifiers.
    - The annotation on the figure explicitly states: `|f_CW^Web - f_CW^Tempel| = 0.026 pp`.
    - The figure caption states: "V-Web filament fcw = 0.4980 ... vs Tempel filament_like fcw = 0.4982 ... differ by 0.026 percentage points".
    - The main body text (Sec IX.A) states: "filament_like_vs_filament: 0.026 pp".
    - However, a direct calculation using the numbers provided in the caption and in Tables II and XI (`0.4982 - 0.4980`) yields a difference of `0.0002`, which is **`0.02` percentage points**, not `0.026`. This is an order of magnitude smaller than the value repeatedly claimed. This discrepancy is not a rounding error and suggests a stale, incorrect number has been propagated through the text, caption, and figure annotation. This error undermines the quantitative claims of the cross-validation.
- **Required Fix**: The authors must find the source of this error, correct the value of `0.026 pp` to the correctly calculated `0.02 pp` throughout the manuscript (including the figure annotation), and verify that this change does not affect any of their qualitative conclusions about the concordance.

**P5-m3: Minor Arithmetic Inconsistencies in Table III**
- **Location**: Table III (p.6).
- **Problem**: The reported `σ_obs` values do not perfectly align with the reported `fcw` values for the stated sample size (`N=158,327` per quintile). For example, for Quintile 1, `fcw = 0.4976` should yield `σ = (0.4976 - 0.5) * 2 * sqrt(158327) ≈ -1.91`, but the table lists `-1.94`. Similarly, for Quintile 3, `fcw = 0.4950` yields `σ ≈ -3.98`, while the table lists `-3.94`.
- **Required Fix**: The authors must re-calculate and reconcile the `fcw` and `σ_obs` columns. While these small differences do not alter the paper's conclusion (the residuals remain below the Bonferroni threshold), such inconsistencies reduce confidence in the overall numerical precision of the analysis.

**B. FIGURE-CAPTION VS BODY-CLAIM**
*(This section is covered by P5-M4 above, which is the most significant instance of this issue.)*

**C. EQUATION DIMENSIONAL CONSISTENCY**
*No additional findings.*

**D. INTERNAL CROSS-REFERENCES**

**P5-m4: Incorrect Internal Cross-References**
- **Location**: Abstract (p.1) and Section X (p.17).
- **Problem**: The manuscript contains incorrect internal section references, which can mislead the reader.
    1.  In the abstract, the discussion of survey-edge artifacts dominating the V-Web void class points to "§IX B". The correct discussion is in Section VIII.A.
    2.  In Section X, the list of supporting analyses refers to the "DESI-VAST per-galaxy cross-match, §IXB". The DESIVAST analysis is the primary result and is detailed in Section VIII.
- **Required Fix**: All internal cross-references must be carefully checked and corrected. These errors suggest the paper was restructured without updating all corresponding pointers.

**E. NULL PROCEDURE COMPARABILITY**
*No additional findings.*

**F. ABSTRACT FAITHFULNESS**
*No additional findings.*

**G. UNSUPPORTED NOVELTY CLAIMS**
*No additional findings.*

**H. UNQUANTIFIED HEDGES**
*No additional findings.*

**I. APPENDIX VS MAIN-TEXT MISMATCH**
*No additional findings.*

**J. STALE NUMBERS**
*(This is the likely cause of P5-M4 and P5-m3.)*