# P2 R24conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.46.pdf` md5=45ee3af4 pages=23
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (4866 chars)
**Wall time**: 164.2s

---

**Referee Report on "Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREX Forecasts, with a MegaMapper Outlook"**

**Manuscript ID:** [INTERNAL]
**Journal:** Physical Review D

This paper presents a detailed forecast for testing the matter bounce cosmological scenario using upcoming measurements of primordial non-Gaussianity (PNG) from the SPHEREX survey, with an outlook towards the proposed MegaMapper survey. The primary prediction under investigation is the local-type non-Gaussianity parameter `f_NL = -35/8 = -4.375`, a distinctive feature of the quasi-dust matter bounce model.

The authors conduct a comprehensive analysis that includes:
1.  A novel quantification of the template mismatch between the matter-bounce bispectrum and the standard local template, including an analysis of a theoretical ambiguity (null space) in the bounce bispectrum's polynomial representation.
2.  A detailed forecast for the detection significance with SPHEREX, propagating a systematic error budget that includes template mismatch, GR projection effects, and PNG bias uncertainties.
3.  A Bayesian model comparison to quantify the discriminating power of SPHEREX to favor the bounce model over various inflationary alternatives.
4.  A clarification of a factor-of-two discrepancy in the predicted `f_NL` value present in the literature, tracing it to the operator algebra of the in-in formalism.

The paper is thorough, technically detailed, and addresses several important subtleties in forecasting and model testing. The analysis of the polynomial null space and the resolution of the literature convention ambiguity are valuable contributions. The overall scientific content is of high quality and suitable for publication in Physical Review D, pending major revisions to address issues of presentation and structure.

---
### **Detailed Findings**

#### **MAJOR REVISIONS**

**P2-M1: Unprofessional "Correction Note" and "Withdrawn" Language**
*   **Classification:** MAJOR
*   **Location:** Page 15, Table III Caption; Page 17, Section D, paragraph 3.
*   **Problem:** The manuscript contains explicit notes about corrections and withdrawn results from previous, un-submitted versions of the paper.
    *   Page 15: `[Correction note: an earlier version of this table quoted BF values ... that could not be reproduced ... they are replaced here by the fully documented closed-form computation.]`
    *   Page 17: `[Correction note: an earlier version of this analysis quoted substantially tighter joint constraints ... those values could not be reproduced from documented survey inputs and are withdrawn.]`
*   **Required Fix:** This language is inappropriate for a journal submission. It reads like an internal audit log. The paper should present only the final, validated results. All such "correction notes" and references to withdrawn values from prior internal drafts must be removed. The final manuscript should be a clean, definitive statement of the authors' work, not a commentary on its own development history.

**P2-M2: Paper Structure and Focus (Cosmic Birefringence Section)**
*   **Classification:** MAJOR
*   **Location:** Page 18, Section E, paragraph 3.
*   **Problem:** The paper, while long at 23 pages, is mostly well-justified in its length due to the depth of the primary analysis. However, the subsection on cosmic birefringence feels tacked on and dilutes the paper's strong focus on PNG. While it is an interesting complementary probe, it is not integrated into the main forecast or systematic analysis and is treated superficially compared to the rest of the paper.
*   **Required Fix:** To improve focus and conciseness, the authors should significantly shorten this subsection to a brief mention in the "Caveats" or "Conclusion" section, or move the entire discussion to an appendix. The main body of the paper should remain focused on the PNG forecasts, which are its core contribution.

#### **MINOR REVISIONS**

**P2-m1: Clarity of Bayesian Factor Spread in the Abstract**
*   **Classification:** MINOR
*   **Location:** Page 1, Abstract; Page 12, Table II.
*   **Problem:** The abstract states: "the GR-marginalization variation ... introduces a separate BF ≈ 5–7 spread". This specific range is difficult to locate and verify in the main body. It is derived from the "delta-prior narrow-competitor row" of Table II, combined with the GR-variation scenarios of Table III, but this connection is only explained in a dense footnote on Table II.
*   **Required Fix:** The origin of this `BF ~ 5-7` range should be stated more clearly in the main text of Section VI (Bayesian Comparison) to make the abstract's claim more easily traceable. For instance, a sentence explicitly stating how the GR degradation scenarios from Table III map onto the baseline results of Table II would improve clarity.

**P2-m2: Signposting of Distinct Fisher Analyses**
*   **Classification:** MINOR
*   **Location:** Page 17, Section D.
*   **Problem:** The paper presents results from two distinct Fisher matrix analyses: (i) the headline bispectrum-only forecast from Heinrich et al. [4], and (ii) a new, separate joint `(f_NL, n_fNL)` forecast using scale-dependent bias (SDB). The distinction is made clearly on page 17, but a reader might be confused earlier in the paper, as both SPHEREx and SDB are mentioned throughout.
*   **Required Fix:** The authors should add a sentence early in the paper (e.g., in the Introduction or Section IV) to signpost that two separate forecast methodologies will be discussed: a bispectrum-only forecast for the primary `f_NL` constraint, and a separate SDB-based forecast for the joint `(f_NL, n_fNL)` running. This would improve the narrative flow and prevent potential confusion.

#### **NIT-PICKS (Cosmetic)**

**P2-N1: Inconsistent Sigma Symbol Usage**
*   **Classification:** NIT
*   **Location:** Page 1, Abstract.
*   **Problem:** The sigma symbol for statistical significance is used inconsistently. The text contains "3-50", "5.2-5.50", "5.20", etc.
*   **Required Fix:** Standardize the notation to use the Greek letter sigma (`σ`) throughout. For example: `3-5σ`, `5.2-5.5σ`, `5.2σ`.

**P2-N2: Typographical Error**
*   **Classification:** NIT
*   **Location:** Page 11, Section VI.C, subsection α.
*   **Problem:** The text reads: "prediction and detection atr fi fbounce". This appears to be a typo.
*   **Required Fix:** Correct this to "at `f_NL^bounce`" or similar, for example: "prediction and detection at the bounce fiducial `f_NL^bounce = -3.68`".

**P2-N3: Colloquial Figure Caption**
*   **Classification:** NIT
*   **Location:** Page 17, Figure 6 Caption.
*   **Problem:** The caption legend description "kills live lane" is colloquial and not appropriate for a formal scientific publication.
*   **Required Fix:** Replace this with more formal language, such as "disfavors quasi-dust bounce, consistent with standard inflation".

---
### **Summary recommendation**

**MAJOR REVISIONS**

This is a strong, comprehensive, and valuable paper that performs a rigorous forecast for a key cosmological model. The scientific analysis is of high quality, particularly the novel treatment of the bispectrum template's theoretical uncertainties and the definitive resolution of a literature ambiguity. The work is well-suited for publication in Physical Review D.

However, the manuscript is marred by presentational issues, most notably the inclusion of internal "correction notes" that are unprofessional for a final submission. These must be removed. Additionally, a minor restructuring to improve focus would strengthen the paper. Once these revisions are made, the paper will represent a significant and polished contribution to the field.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the second-pass review, incorporating new findings based on the detailed checklist.

================================================================
**Referee Report on "Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREX Forecasts, with a MegaMapper Outlook" (Second Pass)**

This second review pass applies a rigorous checklist to the manuscript, focusing on arithmetic, internal consistency, and other details often missed in an initial reading. The findings below are *in addition* to those from the first report.

---
### **Detailed Findings (New)**

#### **MINOR REVISIONS**

**P2-m3: Clarity of Figure 1 and its Caption**
*   **Classification:** MINOR
*   **Location:** Page 5, Figure 1.
*   **Problem:** The figure plots the shape function `B_NL` for the specific kinematic slice where two momenta are held equal, `B_NL(k1, k, k)`. However, the markers on the plot correspond to general benchmark configurations (equilateral, folded). The "Folded" benchmark `(k1 = 2k2 = 2k3)` does not lie on the plotted slice. While the green triangle marker is placed at the correct value (`-2.250`), its position on the x-axis (`k1/k = 0.5`) corresponds to a different folded configuration `(k1, 2k1, 2k1)`. This is potentially confusing.
*   **Required Fix:** The caption should be clarified to state that the solid line represents the `B_NL(k1, k, k)` slice, while the markers indicate the values for standard benchmark configurations, which may or may not lie on this specific slice.

**P2-m4: Inappropriate Location of the Joint `(f_NL, n_fNL)` Analysis**
*   **Classification:** MINOR
*   **Location:** Page 17, Section IX.D.
*   **Problem:** A key piece of original analysis—the joint Fisher forecast for `(f_NL, n_fNL)`—is located in a subsection of the "Discussion" section. This is not a standard location for presenting new results. The cross-reference in the abstract to "§IX" for this analysis is therefore correct but points the reader to a confusing place. This structural choice diminishes the visibility and impact of this analysis.
*   **Required Fix:** The authors should create a new, dedicated section for the joint `(f_NL, n_fNL)` forecast (e.g., a new Section VIII, with subsequent sections renumbered). This would give the analysis the prominence it deserves and improve the paper's logical flow.

**P2-m5: Nuance in Comparison of Different Survey Forecasts**
*   **Classification:** MINOR
*   **Location:** Page 16, Section IX.B.
*   **Problem:** The paper compares the headline SPHEREX bispectrum forecast with forecasts from DESI, Euclid, and LSST, which are primarily based on the scale-dependent bias (SDB) effect. While presenting these as complementary is correct, the text does not explicitly state that the underlying observables (bispectrum vs. power spectrum) and their primary systematic vulnerabilities are different.
*   **Required Fix:** Add a sentence to clarify this distinction. For example: "It is important to note that while the SPHEREx bispectrum channel is robust against ultra-large-scale systematics, the SDB-based forecasts from DESI and Euclid will be more sensitive to them, representing a complementary but distinct observational challenge."

---
### **Summary of Checks (No Issues Found)**

A detailed re-examination of the manuscript was performed according to the specified checklist. The following areas were found to be robust with no new issues identified:

*   **(A) Arithmetic:** All numerical claims, percentages, and significance values re-calculated from the paper's inputs were found to be correct. The internal consistency between tables was particularly strong.
*   **(C) Equation Dimensional Consistency:** All displayed equations were checked and found to be dimensionally consistent.
*   **(F) Abstract Faithfulness:** The abstract provides an excellent, accurate, and well-nuanced summary of the paper's main results and caveats.
*   **(G) Unsupported Novelty Claims:** The paper's primary claim to novelty ("for the first time...") is appropriately hedged and supported by a stated literature search.
*   **(H) Unquantified Hedges:** Statements of "consistency" or "tension" were found to be well-supported by quantitative statistical values throughout the manuscript.
*   **(I) Appendix vs. Main-Text Mismatch:** The appendices fully and accurately support the claims made about them in the main text, particularly regarding the resolution of the literature discrepancy on `f_NL`.
*   **(J) Stale Numbers:** Apart from the "correction notes" identified in the first review, no other evidence of inconsistent or stale numerical values was found.

This second pass confirms the technical solidity of the paper. The new findings are minor and aimed at improving clarity and structure. The major revisions identified in the first report remain the primary barrier to publication.