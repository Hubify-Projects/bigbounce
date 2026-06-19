# P2 R40 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=dbcc5834 pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (7267 chars)
**Wall time**: 204.8s

---

# Referee Report

**Paper:** "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook" by Houston Golden

**Recommendation:** ACCEPT WITH MINOR CORRECTIONS

**Summary:**
This paper presents a detailed forecast for testing the matter-bounce scenario using primordial non-Gaussianity measurements from the SPHEREx and proposed MegaMapper surveys. The primary prediction tested is the local non-Gaussianity parameter `f_NL = -35/8`. The work is a sensitivity recast of existing forecasts, but it adds significant value through several original contributions: (1) a thorough resolution of a factor-of-two discrepancy in the theoretical literature regarding the predicted `f_NL` value, (2) a detailed quantification of the template mismatch between the matter-bounce signal and the standard local template, (3) a comprehensive and transparent systematic budget, and (4) a robust Bayesian model comparison framework.

The paper is exceptionally well-researched, methodologically sound, and transparent about its assumptions and limitations. The resolution of the Cai et al. vs. Li et al. discrepancy via an explicit operator-algebra derivation in the appendix is a particularly strong contribution that clarifies the field. The numerical calculations appear correct, and the systematic budget is well-justified. The distinction between different observables (gauge-frame vs. physical-frame) and analysis channels (bispectrum vs. scale-dependent bias) is handled with the necessary rigor.

The paper meets the high standards of Physical Review D and represents a valuable contribution to the field of primordial cosmology. The required revisions are minor and intended to further improve clarity and presentation.

---
### Detailed Findings

#### ESSENTIAL
(None)

#### MAJOR
(None)

#### MINOR

**P2-M1: Clarification of Bayes Factor Bookkeeping in Abstract**
- **Section:** Abstract, Page 1
- **Problem:** The abstract states: "Table II reports the r→1 endpoint values while the abstract headline applies the noise-weighted r ≈ 0.84 rebooking". This is a bit confusing for a reader trying to reconcile the abstract's headline BF values (≈ 9–14) with the table's values (≈ 10–17) without reading the full body. While correct, the phrasing could be more direct.
- **Required Fix:** Suggest rephrasing for clarity. For example: "...at Bayes factor BF ≈ 9–14. This result applies a noise-weighted template-mismatch correction (r ≈ 0.84) to the ideal Bayes factors of BF ≈ 10–17 (reported in Table II), which assume perfect template recovery (r=1)." This makes the relationship between the numbers explicit within the abstract itself.

**P2-M2: Derivation of Bayes Factor Formula**
- **Section:** VI.C, Page 12
- **Problem:** The paper presents the closed-form Bayes factor in Eq. (9) without derivation. While the formula is correct, its form is not immediately obvious. A brief sketch of the derivation would improve the self-contained nature of this critical section.
- **Required Fix:** Add a short paragraph or a footnote outlining the derivation of Eq. (9) from the integral definition of the marginalized likelihood. This would involve defining the likelihoods for the two models (`p(D|M_bounce) = L(D|f_NL=-35/8)`) and evaluating the integral for the uniform-prior competitor model (`p(D|M_inf) = ∫ L(D|f_NL) p(f_NL|M_inf) df_NL`).

**P2-M3: Ambiguity in "Template-corrected baseline" row in Table IV**
- **Section:** Table IV, Page 20
- **Problem:** The "Template-corrected baseline" row reports a significance of "5.2-5.5σ headline". This range incorporates the uncertainty on `r` and the `ε`-correction. However, subsequent rows appear to use a single central value from this range as their starting point for adding further systematics. This makes it slightly ambiguous what the true "baseline" denominator is for the subsequent calculations.
- **Required Fix:** Clarify the baseline. Either change the "5.2-5.5σ" entry to a single number representing the central case (e.g., 5.25σ, from `r=0.84`), or add a note to the caption explicitly stating that all subsequent rows are derived from the central value `σ_eff = 0.7 / 0.84`. The latter is preferable for transparency.

#### NIT (Nitpicks / Typos)

**P2-N1: Author Email Address**
- **Section:** Page 2
- **Problem:** The author's email address is listed as `houston@hubify.com`. This appears to be a non-institutional or placeholder address.
- **Required Fix:** The author should replace this with a standard institutional or permanent professional email address.

**P2-N2: Minor Typo in Table II Caption**
- **Section:** Table II, Page 15
- **Problem:** The caption text "...prediction f_NL ≈ 0.015 (effectively f_NL = 0 at survey precision)..." is slightly confusing. While the value is negligible, stating it's "effectively 0" could be misread.
- **Required Fix:** Suggest rephrasing to "...prediction f_NL ≈ 0.015, which is negligible at the precision of these surveys...".

**P2-N3: Inconsistent use of `b_phi` vs `b_φ`**
- **Section:** Throughout, e.g., Page 10, 16, 17, 20
- **Problem:** The PNG bias parameter is referred to as `b_phi` in some places and `b_φ` in others (e.g., Table IV uses `b_φ`, while the text on p17 uses `b_phi`).
- **Required Fix:** Use a consistent notation throughout the manuscript, preferably the LaTeX `\varphi` (`b_φ`) for clarity.

---
## Summary recommendation
**ACCEPT WITH MINOR CORRECTIONS**

The paper is a strong, rigorous, and valuable contribution. The analysis is thorough, and the conclusions are well-supported. The resolution of the theoretical ambiguity in the `f_NL` prediction is a significant service to the community. The requested revisions are minor and aimed at improving the already high level of clarity and reproducibility. The paper is well-suited for publication in Physical Review D after these minor points are addressed.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated referee report, incorporating the findings from the "fresh eyes" review.

================================================================
# Referee Report

**Paper:** "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook" by Houston Golden

**Recommendation:** ACCEPT WITH MINOR CORRECTIONS

**Summary:**
This paper presents a detailed forecast for testing the matter-bounce scenario using primordial non-Gaussianity measurements from the SPHEREx and proposed MegaMapper surveys. The primary prediction tested is the local non-Gaussianity parameter `f_NL = -35/8`. The work is a sensitivity recast of existing forecasts, but it adds significant value through several original contributions: (1) a thorough resolution of a factor-of-two discrepancy in the theoretical literature regarding the predicted `f_NL` value, (2) a detailed quantification of the template mismatch between the matter-bounce signal and the standard local template, (3) a comprehensive and transparent systematic budget, and (4) a robust Bayesian model comparison framework.

The paper is exceptionally well-researched, methodologically sound, and transparent about its assumptions and limitations. The resolution of the Cai et al. vs. Li et al. discrepancy via an explicit operator-algebra derivation in the appendix is a particularly strong contribution that clarifies the field. The numerical calculations appear correct, and the systematic budget is well-justified. The distinction between different observables (gauge-frame vs. physical-frame) and analysis channels (bispectrum vs. scale-dependent bias) is handled with the necessary rigor.

The paper meets the high standards of Physical Review D and represents a valuable contribution to the field of primordial cosmology. The required revisions are minor and intended to further improve clarity and presentation.

---
### Detailed Findings

#### ESSENTIAL
(None)

#### MAJOR
(None)

#### MINOR

**P2-M1: Clarification of Bayes Factor Bookkeeping in Abstract**
- **Section:** Abstract, Page 1
- **Problem:** The abstract states: "Table II reports the r→1 endpoint values while the abstract headline applies the noise-weighted r ≈ 0.84 rebooking". This is a bit confusing for a reader trying to reconcile the abstract's headline BF values (≈ 9–14) with the table's values (≈ 10–17) without reading the full body. While correct, the phrasing could be more direct.
- **Required Fix:** Suggest rephrasing for clarity. For example: "...at Bayes factor BF ≈ 9–14. This result applies a noise-weighted template-mismatch correction (r ≈ 0.84) to the ideal Bayes factors of BF ≈ 10–17 (reported in Table II), which assume perfect template recovery (r=1)." This makes the relationship between the numbers explicit within the abstract itself.

**P2-M2: Derivation of Bayes Factor Formula**
- **Section:** VI.C, Page 12
- **Problem:** The paper presents the closed-form Bayes factor in Eq. (9) without derivation. While the formula is correct, its form is not immediately obvious. A brief sketch of the derivation would improve the self-contained nature of this critical section.
- **Required Fix:** Add a short paragraph or a footnote outlining the derivation of Eq. (9) from the integral definition of the marginalized likelihood. This would involve defining the likelihoods for the two models (`p(D|M_bounce) = L(D|f_NL=-35/8)`) and evaluating the integral for the uniform-prior competitor model (`p(D|M_inf) = ∫ L(D|f_NL) p(f_NL|M_inf) df_NL`).

**P2-M3: Ambiguity in "Template-corrected baseline" row in Table IV**
- **Section:** Table IV, Page 20
- **Problem:** The "Template-corrected baseline" row reports a significance of "5.2-5.5σ headline". This range incorporates the uncertainty on `r` and the `ε`-correction. However, subsequent rows appear to use a single central value from this range as their starting point for adding further systematics. This makes it slightly ambiguous what the true "baseline" denominator is for the subsequent calculations.
- **Required Fix:** Clarify the baseline. Either change the "5.2-5.5σ" entry to a single number representing the central case (e.g., 5.25σ, from `r=0.84`), or add a note to the caption explicitly stating that all subsequent rows are derived from the central value `σ_eff = 0.7 / 0.84`. The latter is preferable for transparency.

**P9-m1: Typo in Covariance Correction Scaling Text**
- **Section:** IV, Page 9
- **Problem:** The text describing the non-Gaussian covariance correction states that the fractional correction scales as `f_NL^2 Δ^2`. However, the displayed Eq. (7) shows the scaling is `f_NL^2 Δ(k)`. The text has an extra, erroneous power of `Δ`.
- **Required Fix:** Correct the text to read `f_NL^2 Δ`, matching Eq. (7).

**P10-m2: Arithmetic Error in Photo-z Outlier Dilution Factor**
- **Section:** V (Shot-noise caveat), Page 10
- **Problem:** The text calculates a dilution factor for catastrophic photo-z outliers as `~ f_cat / (1+f_cat)^2 ≈ 0.008` for a catastrophic fraction `f_cat = 0.1`. The correct calculation is `0.1 / (1.1)^2 = 0.0826...`, which is `~0.083`, a factor of 10 larger than stated. This error affects the claim that the effect is "well below the 5% level". At 8.3%, the effect is not negligible.
- **Required Fix:** Correct the numerical value from `0.008` to `0.083`. The author should then re-evaluate the subsequent claim. If the conclusion that the dominant effect is a ~5% smearing comes from a different argument (e.g., from Ref. [26]), this should be clarified to resolve the inconsistency.

#### NIT (Nitpicks / Typos)

**P2-N1: Author Email Address**
- **Section:** Page 2
- **Problem:** The author's email address is listed as `houston@hubify.com`. This appears to be a non-institutional or placeholder address.
- **Required Fix:** The author should replace this with a standard institutional or permanent professional email address.

**P2-N2: Minor Typo in Table II Caption**
- **Section:** Table II, Page 15
- **Problem:** The caption text "...prediction f_NL ≈ 0.015 (effectively f_NL = 0 at survey precision)..." is slightly confusing. While the value is negligible, stating it's "effectively 0" could be misread.
- **Required Fix:** Suggest rephrasing to "...prediction f_NL ≈ 0.015, which is negligible at the precision of these surveys...".

**P2-N3: Inconsistent use of `b_phi` vs `b_φ`**
- **Section:** Throughout, e.g., Page 10, 16, 17, 20
- **Problem:** The PNG bias parameter is referred to as `b_phi` in some places and `b_φ` in others (e.g., Table IV uses `b_φ`, while the text on p17 uses `b_phi`).
- **Required Fix:** Use a consistent notation throughout the manuscript, preferably the LaTeX `\varphi` (`b_φ`) for clarity.

---
## Summary recommendation
**ACCEPT WITH MINOR CORRECTIONS**

The paper is a strong, rigorous, and valuable contribution. The analysis is thorough, and the conclusions are well-supported. The resolution of the theoretical ambiguity in the `f_NL` prediction is a significant service to the community. The requested revisions are minor and aimed at improving the already high level of clarity and reproducibility. The paper is well-suited for publication in Physical Review D after these minor points are addressed.