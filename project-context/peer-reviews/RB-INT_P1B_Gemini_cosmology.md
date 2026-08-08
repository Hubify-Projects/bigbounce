# P1B RB-INT — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=1cb9ff66 pages=22
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 211.0s

---

## Referee Report on "Technical Verification Companion to the ECH Spin-Torsion Program: ACDM+∆Neff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model"

This paper presents three technical analyses that serve as a verification companion for a separate theoretical work on Einstein-Cartan-Holst (ECH) cosmology. The analyses are: (1) a stock-CAMB MCMC analysis of the ΛCDM+∆Neff model to serve as a null test, (2) a Monte Carlo validation of a NaMaster-based pipeline for measuring cosmic birefringence, and (3) a consistency check of the observed birefringence signal with a generic spectator axion-like particle (ALP) model.

The paper is exceptionally well-structured and transparent. The author has taken great care to precisely define the scope and limitations of each analysis, which is commendable. The distinction between what is a direct test, a pipeline validation, or a consistency check is made explicit at every stage. The reporting of results is accompanied by thorough discussions of caveats, potential systematics (such as supernova catalog overlaps), and the physical interpretation of statistical findings. The commitment to reproducibility, with detailed appendices, archived data and code, and explicit versioning, is a model for papers of this type.

The scientific content is sound. The calculations presented are verified to be correct, and the conclusions drawn are well-supported by the results shown. The paper does not overstate its claims; on the contrary, it provides a sober and realistic assessment of what can be concluded from the analyses. For these reasons, the paper is a strong candidate for publication in Physical Review D. However, a few minor revisions are required to correct some small but potentially confusing issues.

### Findings

#### ESSENTIAL

None.

#### MAJOR

**P1B-M1**
*   **Section/Page:** Sec. V.C, bottom of page 12, referencing a typo on page 6.
*   **Problem:** At the bottom of page 6, the text states: "any KDE-based distance is quoted because the product-likelihood SN overlap narrows the widths (Table II);". This sentence appears to be a typographical error, likely intending to say "**no** KDE-based distance is quoted". The current phrasing is confusing and contradicts the numerous, correct caveats elsewhere in the paper (e.g., footnote (a) to Table II, and the text on page 12) which state that no σ-distance or significance is quotable for the `w₀wₐ` chain due to the uncorrected systematic. This typo inverts the meaning of a critical caveat.
*   **Required Fix:** Correct the sentence at the bottom of page 6 to read "no KDE-based distance is quoted...".

#### MINOR

**P1B-m1**
*   **Section/Page:** Sec. V.B, page 12.
*   **Problem:** The paragraph beginning "Independent re-run cross-check (this version)." contains the parenthetical "(this version)", which reads like an internal author's note that was not removed before submission.
*   **Required Fix:** Rephrase the sentence to remove the internal-sounding note. For example, "A dedicated re-run of the Planck+BAO+SN configuration was performed for cross-checking purposes." or similar.

**P1B-m2**
*   **Section/Page:** Sec. III, page 5.
*   **Problem:** The text immediately following Table I discusses the `w₀wₐ` chain, stating "In the converged chain there are zero free-w₀wₐ samples at the ΛCDM point...". However, Table I presents results for the ΛCDM+∆Neff proxy, while the `w₀wₐ` analysis is the subject of Table II. Placing this discussion here could cause confusion for the reader.
*   **Required Fix:** Move this paragraph and the subsequent discussion of the `w₀wₐ` chain's CPL trajectory to Section V.C, where the `w₀wₐ` chain and Table II are formally discussed.

**P1B-m3**
*   **Section/Page:** Sec. IV, page 10, Eq. (1).
*   **Problem:** The chi-squared estimator in Eq. (1) uses the approximation `C_l^EB ≈ 1/2 sin(4β) C_l^EE`, which is valid when `C_l^BB ≪ C_l^EE`. The full expression is `C_l^EB = 1/2 sin(4β) (C_l^EE - C_l^BB)`. While the use of the approximation is acceptable for this pipeline test (and its impact is implicitly absorbed into the measured bias), it would be best practice to state the approximation explicitly for full clarity.
*   **Required Fix:** Add a brief note after Eq. (1) clarifying that the expression neglects the `C_l^BB` term, which is a standard approximation in this context.

#### NIT

**P1B-N1**
*   **Section/Page:** Abstract, page 1.
*   **Problem:** The abstract states "the ∆Neff extension does not reduce the residual ~3.6σ tension". While technically correct, the computed value is 3.61σ. Using "~3.6σ" is acceptable, but for the highest precision, stating "3.6σ" or "3.61σ" would be slightly better.
*   **Required Fix:** Consider changing "~3.6σ" to "3.6σ" for consistency with the precision of other reported values. This is a cosmetic suggestion.

***

## Summary recommendation

**MINOR REVISIONS**

The paper is of high quality, demonstrating rigor, transparency, and a clear understanding of the methods and their limitations. It represents a valuable contribution as a technical foundation for its companion work. The recommendation is for publication after the minor revisions listed above are addressed. The "MAJOR" finding is critical for clarity but is a simple one-sentence correction. The other points will further improve the paper's readability and precision.