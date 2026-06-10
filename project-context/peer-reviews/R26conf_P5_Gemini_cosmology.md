# P5 R26conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.56.pdf` md5=4061bf5c pages=27
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (11546 chars)
**Wall time**: 161.9s

---

**Referee Report: P5-R26conf**

**Manuscript Title:** Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across 791,635 DR1 Matched Spirals

This paper presents a comprehensive search for an environmental dependence of spiral galaxy chirality using data from the DESI Data Release 1. The author cross-matches a large chirality catalog with the DESI redshift catalog and uses multiple cosmic-web classification algorithms (V-Web, DESIVAST, Tempel+2014 FoF) to test for variations in the clockwise (CW) fraction across voids, walls, filaments, and clusters. The headline result is a null detection at the current sensitivity, consistent with the global parity-mixture null from a companion paper (Paper IV). The analysis is exceptionally thorough, including numerous robustness checks, sensitivity sweeps, and systematics tests.

While the underlying analysis appears to be rigorous and detailed, the manuscript in its current form has several essential and major issues related to clarity, structure, and reliance on unpublished work that prevent it from being acceptable for publication in Physical Review D.

---
### **Detailed Findings**

#### **ESSENTIAL REVISIONS**

**P5-E1: Reliance on Unavailable Prerequisite Work**
*   **Section:** II, III, V, and throughout.
*   **Problem:** The entire analysis is fundamentally dependent on the input chirality catalog and the catalog-wide monopole offset (`Δfcw = -0.0026`) from "Paper IV [3]". This reference is repeatedly cited as a "companion work, not yet peer-reviewed" and "in preparation". A core result cannot be published in PRD when its input data and primary systematic calibration are from a work that is not publicly available (e.g., on arXiv). The validity of the classifier, the test-time augmentation, and the crucial monopole measurement cannot be assessed by the reviewer or the community.
*   **Required Fix:** The manuscript cannot be published until Paper IV is publicly available on a preprint server (e.g., arXiv) and cited accordingly. All claims relying on Paper IV's results must be directly traceable to the public version of that manuscript.

**P5-E2: Inclusion of Internal Debugging and Analysis History**
*   **Section:** Multiple instances, including:
    *   Page 10, Sec. VI.D.c: "An earlier draft quoted filament bright/dark n of 416,701/21,203 with a 3.4σ two-sample split; those values were computed on an unfiltered nearest-label join... and are withdrawn..."
    *   Page 15, Sec. VIII.D: "An earlier draft reported n_void = 86,276 / 64,514 with σ = -0.24 / -1.06; those values reproduce exactly only under a zone-indexing defect... The corrected per-cap join values above supersede them..."
    *   Page 20, Sec. IX.B: "An earlier draft quoted an overlap of 110,586; that join omitted the matched-primary deduplication filter and is withdrawn..."
*   **Problem:** The manuscript is littered with self-corrections, references to "earlier drafts," and descriptions of bugs that were fixed during the analysis. This language is appropriate for an internal lab notebook or a version history on arXiv, but it is entirely inappropriate for a formal journal publication. It severely undermines confidence in the final results by creating a narrative of error and correction, rather than presenting a polished, verified final analysis.
*   **Required Fix:** Remove all such language from the manuscript. The paper should present the final, correct, and verified analysis and results only. The history of how the author arrived at those results is not relevant for the publication.

#### **MAJOR REVISIONS**

**P5-M1: Abstract Clarity and Length**
*   **Section:** Abstract, page 1.
*   **Problem:** The abstract is excessively long and dense, reading more like a compressed summary of the entire paper than a concise introduction for a general audience. It is packed with a dizzying array of numbers, p-values, sample sizes, and acronyms, making it nearly impenetrable. An abstract should state the question, the method, the main result, and its significance, not list every secondary null test performed.
*   **Required Fix:** Rewrite the abstract completely. It should be no more than half its current length. Focus on the primary question (chirality vs. environment), the main dataset (DESI DR1), the primary method (DESIVAST-anchored void test), the headline result (a clean null), and the resulting upper bound. The detailed statistics of secondary V-Web classes and other cross-checks do not belong in the abstract.

**P5-M2: Paper Length and Structure**
*   **Section:** Entire manuscript.
*   **Problem:** At 27 pages, the paper is too long for what is ultimately a null result. While the thoroughness is commendable, the presentation makes it difficult for a reader to distinguish the primary analysis path from the numerous secondary consistency checks. The narrative is frequently interrupted by asides, details of withdrawn results, and justifications that could be streamlined.
*   **Required Fix:** Significantly restructure and shorten the paper. The primary analysis path (DESIVAST-anchored test, Sec. VIII) should be the clear focus of the main text. Many of the secondary checks (e.g., the detailed V-Web Phase 2 sweep, Tempel cross-check, ASTRA cross-check, some systematics) should be summarized in the main text and moved to an appendix. The main text should be streamlined to focus on the most robust and important results, aiming for a total length closer to 15-18 pages.

**P5-M3: Confusing Sample Definitions and Accounting**
*   **Section:** Abstract, Sec. VI.A, Fig. 3 caption, Sec. VIII.F.
*   **Problem:** The paper uses multiple, slightly different sample sizes and definitions (e.g., "791,635 unique chirality-relevant matched spirals", "812,793 env-labeled spiral rows", "783,820 unique env-matched spirals"). The distinction is due to repeat observations (coadds) in DESI, but this is not explained clearly upfront. The caption of Figure 3, for example, is very confusing. This makes it difficult to track which sample is being used for which statistic and to verify the results.
*   **Required Fix:** Add a dedicated, clear paragraph or table early in the Data section (Sec. III) that defines each sample count used in the paper, explains exactly why they differ (unique galaxies vs. coadd rows), and states which count is used for which analysis path. All subsequent references and figure captions must use this terminology consistently. The primary results should be reported on the unique-galaxy sample where possible, as this is the physically relevant quantity.

#### **MINOR REVISIONS**

**P5-m1: Clarification of Retracted Statistic from Companion Paper**
*   **Section:** II, page 3.
*   **Problem:** The text mentions that "an earlier harmonic-space... l=1 statistic was withdrawn in Paper IV v1.0.166 after a provenance audit traced its mask to a synthetic footprint." While transparent, this level of detail about a retracted result in a companion paper is distracting and adds clutter.
*   **Required Fix:** Shorten this to a single, simple statement that the real-space dipole null from Paper IV is the current, robust result, without detailing the history of previously withdrawn statistics.

**P5-m2: Small Discrepancy in Input Row Count**
*   **Section:** Abstract and Sec. III.B, pages 1 & 3.
*   **Problem:** The abstract states "16.4 x 10^6 ZWARN=0 input rows", while the body (Sec. III.B) states "16,361,731 rows". This is a minor inconsistency.
*   **Required Fix:** Use the precise number (16.36 million) in the abstract or ensure the rounded number is consistent.

**P5-m3: Verification of Quoted Statistics from External Work**
*   **Section:** XIII, page 24.
*   **Problem:** The paper compares its null result to "Shamir 2022 [9]", which reported a "~2-4% large-scale asymmetry". The current paper correctly states its result leaves no room for such a signal. However, it is good practice to verify that the characterization of the external work is precise.
*   **Required Fix:** Please double-check that the "2-4%" figure is an accurate and fair representation of the claim in Shamir 2022, and clarify if that was a dipole, monopole, or other type of asymmetry, to make the comparison as sharp as possible.

---
### **Summary recommendation**

**MAJOR REVISIONS**

The author has performed an impressively comprehensive and statistically rigorous analysis that represents a significant amount of work. The paper provides a strong null result on the environmental dependence of spiral chirality, which is a valuable contribution to the field. However, the manuscript is not yet ready for publication. The reliance on an unavailable companion paper and the inclusion of extensive internal-review language are essential barriers to publication that must be addressed. Furthermore, the paper's structure, length, and clarity need a major overhaul to make the results accessible and to properly highlight the primary scientific conclusion.

If the author can (1) wait for Paper IV to become public, (2) completely remove all "earlier draft" and bug-fix history, and (3) substantially rewrite the manuscript for clarity and conciseness by restructuring it into a more focused main text with appendices, a revised version would be a strong candidate for publication in Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated referee report, incorporating the new findings from the second, more rigorous review.

================================================================
**Referee Report: P5-R26conf**

**Manuscript Title:** Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across 791,635 DR1 Matched Spirals

This paper presents a comprehensive search for an environmental dependence of spiral galaxy chirality using data from the DESI Data Release 1. The author cross-matches a large chirality catalog with the DESI redshift catalog and uses multiple cosmic-web classification algorithms (V-Web, DESIVAST, Tempel+2014 FoF) to test for variations in the clockwise (CW) fraction across voids, walls, filaments, and clusters. The headline result is a null detection at the current sensitivity, consistent with the global parity-mixture null from a companion paper (Paper IV). The analysis is exceptionally thorough, including numerous robustness checks, sensitivity sweeps, and systematics tests.

While the underlying analysis appears to be rigorous and detailed, the manuscript in its current form has several essential and major issues related to clarity, structure, and reliance on unpublished work that prevent it from being acceptable for publication in Physical Review D.

---
### **Detailed Findings**

#### **ESSENTIAL REVISIONS**

**P5-E1: Reliance on Unavailable Prerequisite Work**
*   **Section:** II, III, V, and throughout.
*   **Problem:** The entire analysis is fundamentally dependent on the input chirality catalog and the catalog-wide monopole offset (`Δfcw = -0.0026`) from "Paper IV [3]". This reference is repeatedly cited as a "companion work, not yet peer-reviewed" and "in preparation". A core result cannot be published in PRD when its input data and primary systematic calibration are from a work that is not publicly available (e.g., on arXiv). The validity of the classifier, the test-time augmentation, and the crucial monopole measurement cannot be assessed by the reviewer or the community.
*   **Required Fix:** The manuscript cannot be published until Paper IV is publicly available on a preprint server (e.g., arXiv) and cited accordingly. All claims relying on Paper IV's results must be directly traceable to the public version of that manuscript.

**P5-E2: Inclusion of Internal Debugging and Analysis History**
*   **Section:** Multiple instances, including:
    *   Page 10, Sec. VI.D.c: "An earlier draft quoted filament bright/dark n of 416,701/21,203 with a 3.4σ two-sample split; those values were computed on an unfiltered nearest-label join... and are withdrawn..."
    *   Page 15, Sec. VIII.D: "An earlier draft reported n_void = 86,276 / 64,514 with σ = -0.24 / -1.06; those values reproduce exactly only under a zone-indexing defect... The corrected per-cap join values above supersede them..."
    *   Page 20, Sec. IX.B: "An earlier draft quoted an overlap of 110,586; that join omitted the matched-primary deduplication filter and is withdrawn..."
*   **Problem:** The manuscript is littered with self-corrections, references to "earlier drafts," and descriptions of bugs that were fixed during the analysis. This language is appropriate for an internal lab notebook or a version history on arXiv, but it is entirely inappropriate for a formal journal publication. It severely undermines confidence in the final results by creating a narrative of error and correction, rather than presenting a polished, verified final analysis.
*   **Required Fix:** Remove all such language from the manuscript. The paper should present the final, correct, and verified analysis and results only. The history of how the author arrived at those results is not relevant for the publication.

#### **MAJOR REVISIONS**

**P5-M1: Abstract Clarity and Length**
*   **Section:** Abstract, page 1.
*   **Problem:** The abstract is excessively long and dense, reading more like a compressed summary of the entire paper than a concise introduction for a general audience. It is packed with a dizzying array of numbers, p-values, sample sizes, and acronyms, making it nearly impenetrable. An abstract should state the question, the method, the main result, and its significance, not list every secondary null test performed.
*   **Required Fix:** Rewrite the abstract completely. It should be no more than half its current length. Focus on the primary question (chirality vs. environment), the main dataset (DESI DR1), the primary method (DESIVAST-anchored void test), the headline result (a clean null), and the resulting upper bound. The detailed statistics of secondary V-Web classes and other cross-checks do not belong in the abstract.

**P5-M2: Paper Length and Structure**
*   **Section:** Entire manuscript.
*   **Problem:** At 27 pages, the paper is too long for what is ultimately a null result. While the thoroughness is commendable, the presentation makes it difficult for a reader to distinguish the primary analysis path from the numerous secondary consistency checks. The narrative is frequently interrupted by asides, details of withdrawn results, and justifications that could be streamlined.
*   **Required Fix:** Significantly restructure and shorten the paper. The primary analysis path (DESIVAST-anchored test, Sec. VIII) should be the clear focus of the main text. Many of the secondary checks (e.g., the detailed V-Web Phase 2 sweep, Tempel cross-check, ASTRA cross-check, some systematics) should be summarized in the main text and moved to an appendix. The main text should be streamlined to focus on the most robust and important results, aiming for a total length closer to 15-18 pages.

**P5-M3: Confusing Sample Definitions and Accounting**
*   **Section:** Abstract, Sec. VI.A, Fig. 3 caption, Sec. VIII.F.
*   **Problem:** The paper uses multiple, slightly different sample sizes and definitions (e.g., "791,635 unique chirality-relevant matched spirals", "812,793 env-labeled spiral rows", "783,820 unique env-matched spirals"). The distinction is due to repeat observations (coadds) in DESI, but this is not explained clearly upfront. The caption of Figure 3, for example, is very confusing. This makes it difficult to track which sample is being used for which statistic and to verify the results.
*   **Required Fix:** Add a dedicated, clear paragraph or table early in the Data section (Sec. III) that defines each sample count used in the paper, explains exactly why they differ (unique galaxies vs. coadd rows), and states which count is used for which analysis path. All subsequent references and figure captions must use this terminology consistently. The primary results should be reported on the unique-galaxy sample where possible, as this is the physically relevant quantity.

#### **MINOR REVISIONS**

**P5-m1: Clarification of Retracted Statistic from Companion Paper**
*   **Section:** II, page 3.
*   **Problem:** The text mentions that "an earlier harmonic-space... l=1 statistic was withdrawn in Paper IV v1.0.166 after a provenance audit traced its mask to a synthetic footprint." While transparent, this level of detail about a retracted result in a companion paper is distracting and adds clutter.
*   **Required Fix:** Shorten this to a single, simple statement that the real-space dipole null from Paper IV is the current, robust result, without detailing the history of previously withdrawn statistics.

**P5-m2: Small Discrepancy in Input Row Count**
*   **Section:** Abstract and Sec. III.B, pages 1 & 3.
*   **Problem:** The abstract states "16.4 x 10^6 ZWARN=0 input rows", while the body (Sec. III.B) states "16,361,731 rows". This is a minor inconsistency.
*   **Required Fix:** Use the precise number (16.36 million) in the abstract or ensure the rounded number is consistent.

**P5-m3: Verification of Quoted Statistics from External Work**
*   **Section:** XIII, page 24.
*   **Problem:** The paper compares its null result to "Shamir 2022 [9]", which reported a "~2-4% large-scale asymmetry". The current paper correctly states its result leaves no room for such a signal. However, it is good practice to verify that the characterization of the external work is precise.
*   **Required Fix:** Please double-check that the "2-4%" figure is an accurate and fair representation of the claim in Shamir 2022, and clarify if that was a dipole, monopole, or other type of asymmetry, to make the comparison as sharp as possible.

---
### **Additional Findings from Second Review**

**P5-N1: Minor Arithmetic Discrepancies**
*   **Section:** VI.A (p. 7) and Table X (p. 17).
*   **Problem:** A few key statistical values do not exactly match re-computation from the provided inputs, suggesting a lack of final polish or the use of stale numbers from a previous analysis version.
    *   The omnibus χ² test for homogeneity across V-Web classes is quoted as 3.55, but re-calculation from the counts in Table II yields 3.71.
    *   In Table X, the monopole-subtracted residuals `σ_vs_monopole` for the filament (+0.99) and cluster (-1.11) classes differ slightly from the re-calculated values (+1.03 and -1.13, respectively).
*   **Required Fix:** Please re-verify all calculations and ensure that all reported values are consistent with the final data tables presented in the manuscript.

**P5-N2: Inconsistent Equation in Figure Legend**
*   **Section:** Figure 5 (p. 9) and Eq. (1) (p. 5).
*   **Problem:** The legend of Figure 5 (right panel) gives the formula for the predicted deviation as `σ_pred = -2Δfcw * sqrt(N)`. This contradicts the definition in Eq. (1), `σ_pred = 2Δfcw * sqrt(N)`. The plot appears to be correct (showing a negative prediction for a negative `Δfcw`), but the formula in the legend contains a spurious minus sign.
*   **Required Fix:** Correct the formula in the legend of Figure 5 to be consistent with Eq. (1).

**P5-N3: Undefined Acronyms in Abstract**
*   **Section:** Abstract (p. 1).
*   **Problem:** The abstract uses the acronym "TTA" (presumably "test-time augmentation") without definition. This term is technical and relies on knowledge of the methods in the unavailable Paper IV, making the abstract less accessible.
*   **Required Fix:** Define all acronyms on first use in the abstract, or rephrase to avoid them where possible.

---
### **Summary recommendation**

**MAJOR REVISIONS**

The author has performed an impressively comprehensive and statistically rigorous analysis that represents a significant amount of work. The paper provides a strong null result on the environmental dependence of spiral chirality, which is a valuable contribution to the field. However, the manuscript is not yet ready for publication. The reliance on an unavailable companion paper and the inclusion of extensive internal-review language are essential barriers to publication that must be addressed. Furthermore, the paper's structure, length, and clarity need a major overhaul to make the results accessible and to properly highlight the primary scientific conclusion. The minor arithmetic and consistency errors found on second review reinforce the need for a thorough final polish.

If the author can (1) wait for Paper IV to become public, (2) completely remove all "earlier draft" and bug-fix history, and (3) substantially rewrite the manuscript for clarity and conciseness by restructuring it into a more focused main text with appendices, a revised version would be a strong candidate for publication in Physical Review D.