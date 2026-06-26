# P1B R52 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/public/papers/paper1b_mcmc_companion.pdf` md5=a29137f5 pages=21
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (2935 chars)
**Wall time**: 143.1s

---

**Referee Report for PRD**

**Manuscript Title:** Technical Verification Companion to the ECH Spin-Torsion Program: ACDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model
**Author:** Houston Golden

This paper presents three technical analyses that serve as verification material for a separate program on Einstein-Cartan-Holst (ECH) spin-torsion cosmology. The analyses cover: (1) a stock-CAMB MCMC analysis of the ΛCDM+ΔNeff model to serve as a null test for extra radiation, (2) a Monte Carlo validation of a NaMaster-based pipeline for measuring cosmic birefringence, and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper is exceptionally well-structured, transparent about its methods and limitations, and provides an exemplary level of detail for reproducibility. The author is careful to scope each analysis appropriately, clearly distinguishing between pipeline validation and sky measurement, and between model consistency and model prediction. The numerical checks and robustness tests are thorough.

However, there are several issues that must be addressed before the paper can be considered for publication, the most critical of which is its dependence on companion papers that are not available for review.

---

### **Detailed Findings**

#### **ESSENTIAL**

*   **ID: P1B-E1**
    *   **Location:** References, Page 18
    *   **Problem:** The manuscript is presented as a "technical verification companion" to a main paper, "Paper I(a)" [1], and also cites other key companion papers [6, 7, 8]. All of these references are placeholders: "(2026), companion paper, posted concurrently on arXiv." The current manuscript is not self-contained; it relies on [1] for its core motivation and theoretical context. Without access to these companion papers, it is impossible to evaluate the significance, novelty, and correctness of the work in its intended context.
    *   **Fix:** The manuscript can only be properly reviewed as part of a joint submission with all essential companion papers (especially [1]). The author must provide these papers to the journal for concurrent review.

#### **MAJOR**

*   **ID: P1B-M1**
    *   **Location:** Section IV, Page 7, Equation (1)
    *   **Problem:** The formula for the birefringence template fit appears to be missing a factor. The EB power spectrum induced by a rotation β is $C_\ell^{EB} = \frac{1}{2} \sin(4\beta) (C_\ell^{EE} - C_\ell^{BB})$. Neglecting the small $C_\ell^{BB}$ term, the template for the fit should be $\frac{1}{2} \sin(4\beta) C_\ell^{EE, \text{tmpl}}$. Equation (1) is given as $\chi^2(\beta) = \sum_b [C_{\ell_b}^{EB, \text{decoupled}} - \sin(4\beta) C_{\ell_b}^{EE, \text{tmpl}}]^2$. This is missing the factor of 1/2. While the text below the equation correctly identifies the term as `sin(2β)cos(2β)CEE` (which equals `1/2 sin(4β) CEE`), the equation itself is incorrect. This is a critical formula for the analysis in Section IV.
    *   **Fix:** Correct Equation (1) to include the factor of 1/2: $\chi^2(\beta) = \sum_b [C_{\ell_b}^{EB, \text{decoupled}} - \frac{1}{2}\sin(4\beta) C_{\ell_b}^{EE, \text{tmpl}}]^2$. Verify that the analysis code used this correct formula.

*   **ID: P1B-M2**
    *   **Location:** Section III, Page 4, "Physics interpretation (Table II)"
    *   **Problem:** The text in this subsection discusses the results of a $w_0-w_a$ (CPL) model fit, referencing Table II. However, Section III is dedicated to the "ACDM+ΔNeff MCMC" analysis, whose results are in Table I. This makes the paper's structure confusing, as the discussion is disconnected from the section topic. This text appears to belong in Section V.C, which is explicitly about the $w_0-w_a$ cross-check.
    *   **Fix:** Move the entire "Physics interpretation (Table II)" paragraph and the "Caveats" list (a-e) from page 4 to Section V.C ("w₀wₐ cross-check with stated SN-overlap systematic") on page 10. This will align the discussion with the relevant analysis and improve the logical flow of the paper.

*   **ID: P1B-M3**
    *   **Location:** Section IV, Page 4, Caveat (e)
    *   **Problem:** The analysis of the $w_0-w_a$ model relies on a product likelihood of two overlapping supernova catalogs (DES-SN5YR and Pantheon+) without a joint covariance matrix. The author correctly identifies this as a significant systematic. The text then claims, "the qualitative quintom-B direction (w₀ + wₐ < -1) is plausibly robust," but states that the verification for this claim from control chains "are the subject of a separate follow-up note and do not gate the cross-check reported here." This is insufficient for a peer-reviewed publication. A key result cannot be supported by an unsubstantiated claim of robustness, with the evidence deferred to a future, un-cited note.
    *   **Fix:** The author must either (a) perform the analysis with a proper joint covariance matrix for the SN datasets, or (b) present the results from the "SN-overlap control chains" within this manuscript (e.g., in an appendix) to substantiate the claim that the quintom-crossing result is robust. Deferring this critical validation is not acceptable.

#### **MINOR**

*   **ID: P1B-m1**
    *   **Location:** Section IV, Page 4, "Physics interpretation" and "Caveats"
    *   **Problem:** The paper reports posterior tail distances for the $w_0-w_a$ parameters in units of "σ" (e.g., "+4.3σ in w₀"). The text and footnotes clarify that this is not a standard statistical significance but rather the distance from the ΛCDM point to the posterior mean in units of the marginal posterior width. While the clarification is present, using the "σ" notation is potentially misleading and may be misinterpreted as a formal detection significance.
    *   **Fix:** Rephrase to avoid the "σ" notation for this specific quantity. For example, state it as "the posterior mean for $w_0$ is displaced by 4.3 times its marginal standard deviation from the ΛCDM value of -1." This maintains precision while reducing the potential for misinterpretation.

#### **NIT**

*   **ID: P1B-N1**
    *   **Location:** Title page, Page 1
    *   **Problem:** The paper is dated "June 14, 2026". This is a future date, presumably a placeholder.
    *   **Fix:** Update the date to the current submission date.

---

### **Summary recommendation**

**MAJOR REVISIONS**

The manuscript represents a high-quality body of technical work, characterized by its rigor, transparency, and attention to reproducibility. The author has done an excellent job of carefully scoping the analyses and providing detailed validation and robustness checks. The paper would be a valuable contribution to the community.

However, in its current state, it is not suitable for publication. The **essential** issue is its reliance on multiple companion papers that were not provided for review, making it impossible to assess the work in its full context. This must be rectified by a joint submission. Furthermore, the paper contains a few **major** issues, including a likely error in a key equation, a significant structural confusion in the presentation of results, and an unsubstantiated claim of robustness for one of its findings.

Assuming the author can provide the companion papers and address the major revisions listed above, the manuscript has a clear path to publication in Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from the second, more rigorous review.

---

### **ADDITIONAL FINDINGS**

#### **MAJOR**

*   **ID: P1B-M4**
    *   **Location:** Section III, Page 4, "Caveats" paragraph
    *   **Problem:** This paragraph contains multiple broken internal cross-references that severely impact readability. The text refers to "fn. a" and "fn. b" which do not exist on that page. These appear to be intended references to the footnotes of Table II (on page 20), which discuss the posterior-tail extrapolation and the pivot scale, respectively. This suggests a copy-editing or restructuring error that was not fully resolved, leaving the text confusing and difficult to parse.
    *   **Fix:** Systematically correct all broken cross-references in this section. For example, "fn. a" should be explicitly changed to "see footnote (a) of Table II". This correction is critical for the reader to follow the argument.

#### **MINOR**

*   **ID: P1B-A1**
    *   **Location:** Section VI, Page 12, "MCMC parameter estimation" paragraph
    *   **Problem:** The text assesses the consistency between the ALP model fit (`β_ALP = 0.336° ± 0.10°`) and the observational constraint (`β_obs = 0.342° ± 0.094°`) by calculating a combined uncertainty `σ_comb = sqrt(σ_ALP² + σ_obs²)`. This formula is appropriate for the difference between two independent measurements. However, in this case, the model posterior for `β_ALP` is *derived from* the likelihood of `β_obs`. They are not independent. The calculation, while arithmetically correct, is statistically misleading. The proper way to state consistency is to note that the posterior mean of the model is well within the 1σ uncertainty of the data.
    *   **Fix:** Rephrase the consistency statement to be statistically sound. Instead of calculating a combined sigma, state that the model's posterior mean (`0.336°`) is only `(0.342 - 0.336) / 0.094 ≈ 0.06` standard deviations away from the central value of the data constraint. This is a clearer and more appropriate demonstration of consistency.

*   **ID: P1B-m2**
    *   **Location:** Section IV, Page 7, Equation (1)
    *   **Problem:** The quantity defined as `χ²(β)` is dimensionally inconsistent. A chi-squared statistic must be dimensionless, but the expression given is a sum of squared power spectra, which has units of `(μK²)²`. The text clarifies that this is an "unweighted" fit with "no σ_b² divisor," but this is a significant abuse of standard notation. The procedure is a valid least-squares minimization, but the quantity being minimized is not a formal chi-squared statistic.
    *   **Fix:** For clarity and correctness, either rename the quantity in Eq. (1) to something like `S(β)` (for sum of squares) or explicitly state in the text that this is a least-squares residual sum, not a formal chi-squared statistic, and is used as a proxy for the log-likelihood under an assumption of uniform variance.