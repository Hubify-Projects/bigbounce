# P2 R29 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.49.pdf` md5=b2766266 pages=25
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 153.3s

---

## Referee Report: "Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Sensitivity Recast and Forecasts, with a MegaMapper Outlook"

This manuscript presents a detailed forecast for testing the matter bounce cosmological scenario using primordial non-Gaussianity, focusing on the capabilities of the upcoming SPHEREx survey. The authors perform a sensitivity recast of existing SPHEREx forecasts for the key prediction `f_NL = -35/8`, including a novel analysis of the template mismatch arising from the underdetermination of the bounce bispectrum's polynomial form. The paper also provides a comprehensive Bayesian model comparison against inflationary alternatives.

The work addresses an important and timely question. The analysis of the polynomial null space and the careful resolution of the factor-of-two discrepancy in the literature regarding the predicted `f_NL` value are significant contributions. However, the manuscript in its current form suffers from several significant issues in presentation, clarity, and rigor that must be addressed before it can be considered for publication in Physical Review D. The required revisions are substantial.

### ESSENTIAL Revisions

**P2-E1: Abstract-Body Mismatch on Systematic Propagation Method**
*   **Location:** Page 1, Abstract.
*   **Problem:** The abstract states, "the systematic budget is propagated additively in quadrature". This is inconsistent with the methods described in the body. The GR degradation is added in quadrature (Sec. VII.C), but the template mismatch `r` and `b_phi` uncertainty are treated as multiplicative degradations on the signal or `sigma(f_NL)`. The final `3-5 sigma` range is the result of a multi-step process, not a simple quadrature sum of all systematics.
*   **Fix:** The abstract must be rewritten to accurately reflect the degradation procedure used in the body. The body itself should also provide a clear, step-by-step calculation showing how all systematics are combined to derive the final `3-5 sigma` range from the optimistic `5.2-5.5 sigma` starting point.

**P2-E2: Unresolved Internal Correction Notes in Manuscript**
*   **Location:** Page 16, Table III Caption; Page 19, Section IX.D.
*   **Problem:** The manuscript contains two `[Correction note: ...]` blocks. These are internal version-control comments that refer to errors in previous drafts. Their presence in a formal submission is unacceptable and severely undermines confidence in the paper's quality control.
*   **Fix:** Remove these blocks and any other internal-facing commentary. The manuscript must be a clean, final version that stands on its own without reference to its revision history.

**P2-E3: Misleading Headline Bayes Factor Range in Abstract**
*   **Location:** Page 1, Abstract.
*   **Problem:** The abstract presents a headline range of "BF~10-17". The body reveals this range is constructed by combining the result from a physically motivated "recommended" prior (BF ~ 10) with the result from an unphysical, idealized delta-function prior (BF ~ 17). Presenting this as a single envelope is misleading, as it gives undue prominence to the idealized theoretical maximum.
*   **Fix:** The abstract should be revised to state the primary, physically motivated result (BF ~ 10) first. The idealized maximum (BF ~ 17) should be mentioned separately and clearly qualified as an unphysical upper limit that does not account for any theoretical uncertainty. The combined range `10-17` should not be used.

### MAJOR Revisions

**P2-M1: Justification for Paper Length**
*   **Location:** Overall manuscript (25 pages).
*   **Problem:** For a paper framed as a "sensitivity recast," the manuscript is excessively long. The core contributions (null-space analysis, Bayesian comparison) are diluted by verbose prose and sections that could be streamlined.
*   **Fix:** The authors must shorten the manuscript to approximately 15-18 pages. This can be achieved by moving technical details—such as the full polynomial basis discussion (Sec. II.A), the detailed derivation of the Bayes factor (Sec. VI.C), and the `(f_NL, n_fNL)` forecast (Sec. IX.D)—to appendices. The main text should be a clear, concise presentation of the physical motivation, key results, and their implications.

**P2-M2: Inconsistent Bookkeeping of Template Mismatch in Bayesian Analysis**
*   **Location:** Page 12, Section VI.
*   **Problem:** The main Bayesian results presented in Table II and the abstract are calculated using a method that effectively ignores the template mismatch (`r=1` bookkeeping). A more physically correct calculation that accounts for the mismatch (`sigma_eff = sigma/r`) is presented in a subsection (VI.a) as a minor correction, showing a modest reduction in the Bayes factors. The headline result should be based on the most physically accurate methodology.
*   **Fix:** The main analysis, including Table II, must be recalculated and presented using the physically correct bookkeeping that accounts for the template mismatch. The abstract and all conclusions must be updated with these revised (and slightly weaker) Bayes factors.

**P2-M3: Overstated Claim of Novelty**
*   **Location:** Page 1, Abstract.
*   **Problem:** The abstract claims to "quantify, for the first time to our knowledge, the template mismatch". This claim is too strong. The non-local nature of the matter bounce bispectrum is known from the original literature, and the mismatch is implicitly quantifiable from the published shape functions. The novelty of this work lies in the *systematic and thorough* nature of the quantification across different weighting schemes and including the null-space uncertainty.
*   **Fix:** Soften the claim to more accurately reflect the contribution. For example: "We present the first systematic quantification of the template mismatch..." or "We perform a detailed analysis of the template mismatch...".

**P2-M4: Insufficient Detail on Derivation of Final Systematic Budget**
*   **Location:** Page 1, Abstract; Page 9, Section IV.
*   **Problem:** The paper does not provide an explicit calculation that combines all enumerated systematic effects to arrive at the headline "realistic range" of `3-5 sigma`. The components are listed, but their individual quantitative impacts and the method of their combination are not shown.
*   **Fix:** Add a table or a dedicated paragraph that clearly itemizes each source of systematic uncertainty, the assumed degradation factor for each, and the explicit calculation that combines them to produce the final `3-5 sigma` forecast.

### MINOR Revisions

**P2-MIN1: Inconsistent Use of `sigma` Symbol**
*   **Location:** Throughout the manuscript.
*   **Problem:** The symbol `sigma` is used for at least three different quantities: the standard deviation of a measurement (e.g., `sigma(f_NL)`), singular values from an SVD (`sigma_i` on p. 4), and the width of a Gaussian prior (`sigma_theory` on p. 12). This overloading can cause confusion.
*   **Fix:** Please use distinct symbols for these different quantities. For example, use `s_i` for singular values and `w_prior` or `Delta_theory` for the prior width, reserving `sigma` for standard deviation.

**P2-MIN2: Awkward Phrasing in Abstract**
*   **Location:** Page 1, Abstract.
*   **Problem:** The sentence beginning "the systematic budget is propagated..." is long and convoluted, mixing the description of the method with its justification.
*   **Fix:** Please simplify and split this sentence for clarity.

**P2-MIN3: Table III Caption Clarity**
*   **Location:** Page 16, Table III.
*   **Problem:** The caption is overly long and contains information that belongs in the main text, as well as a reference to a correction note that should be removed.
*   **Fix:** Shorten the caption to describe only the contents of the table. Move all discussion and interpretation to the main body of the text.

### NITs (Cosmetic)

**P2-NIT1: Typo in Abstract**
*   **Location:** Page 1, Abstract.
*   **Problem:** "Heinrich et al. o(fNL) = 0.7".
*   **Fix:** Change `o(fNL)` to `sigma(fNL)`.

**P2-NIT2: Future Date on Manuscript**
*   **Location:** Page 1.
*   **Problem:** The paper is dated "June 10, 2026".
*   **Fix:** Please use the submission date.

**P2-NIT3: Inconsistent Citation Style**
*   **Location:** Throughout the text.
*   **Problem:** The manuscript mixes numeric `[1]` and author-year `(Cai et al. 2009)` citation styles.
*   **Fix:** Please use a single, consistent citation style, preferably the numeric style required by the journal.

## Summary recommendation
**MAJOR REVISIONS**

This manuscript contains a valuable and thorough analysis of an important topic. The detailed work on the bispectrum's polynomial null space and the clarification of the theoretical prediction for `f_NL` are commendable. However, the paper is marred by significant presentational flaws, including internal review notes left in the text, a misleading abstract, and a lack of clarity in the derivation of key results. These issues prevent the paper from meeting the high standards of Physical Review D. I recommend that the paper be reconsidered for publication only after the authors have undertaken a thorough revision to address all the essential and major points listed above.