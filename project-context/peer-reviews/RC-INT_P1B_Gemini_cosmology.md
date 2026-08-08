# P1B RC-INT — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=0b1108a9 pages=22
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 184.2s

---

**Referee Report for Manuscript [Paper ID]**

**Title:** Technical Verification Companion to the ECH Spin-Torsion Program: ACDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model

**Author:** Houston Golden

---

This manuscript presents three technical analyses intended as a companion to a theoretical paper on Einstein-Cartan-Holst (ECH) spin-torsion cosmology. The analyses are: (1) a stock-CAMB MCMC analysis of the ΛCDM+ΔNeff model as a proxy for extra radiation, (2) a validation of a NaMaster-based pseudo-Cℓ pipeline for measuring cosmic birefringence, and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper is exceptionally well-structured, with a clear and upfront delineation of the scope and limitations of each analysis. The authors are careful to distinguish between pipeline validation and sky detection, and between model accommodation and model prediction. The level of detail provided for reproducibility is exemplary, including specific software versions, likelihood configurations, sample counts, and links to public repositories with code and data products. The numerical results presented are internally consistent and have been cross-checked by the reviewer where possible.

The manuscript is suitable for publication in Physical Review D, subject to minor corrections. The work provides a valuable and methodologically sound set of verification studies that will be useful to the community, regardless of the status of the specific ECH theory it is intended to support.

---

### **Detailed Findings**

#### **ESSENTIAL**
*None.*

#### **MAJOR**
*None.*

#### **MINOR**

**P1B-m1:**
*   **Section/Page:** IV, p. 10, Eq. (1)
*   **Problem:** Equation (1) for the χ² estimator is missing a factor of 1/2 in the model term. The text states the model is `sin(4β) CEE,tmpl`, whereas the correct expression for the induced EB power spectrum from a rotation β is `(1/2) sin(4β) CEE`.
    ```
    χ²(β) = Σ [CEB,decoupled - sin(4β) CEE,tmpl]²  (1)
    ```
*   **Required Fix:** Correct the equation to include the factor of 1/2.
    ```
    χ²(β) = Σ [CEB,decoupled - (1/2) sin(4β) CEE,tmpl]²  (1)
    ```
    Note: The reviewer confirms that footnote 4 on the same page presents the correct formula (`CEB,th = sin(2β)cos(2β)CEE = 1/2 sin(4β)CEE`), and the numerical results of the analysis appear to be based on the correct implementation. This is therefore a typographical error in the main equation display.

**P1B-m2:**
*   **Section/Page:** VI, p. 14, footnote 6 and related text.
*   **Problem:** The discussion of the fine-tuning required for the spectator-ALP scenario uses the phrase `a ~25x fine-tuning of the misalignment initial condition`. This is slightly ambiguous. The calculation in footnote 6 shows that the ALP energy density `Ωα` scales as `θi²`. A 25x reduction in `Ωα` (e.g., from `θi=0.5` to `θi=0.1`) corresponds to a 5x reduction in the initial angle `θi`. While the reduction in the available parameter-space volume might be ~25x, the tuning is on the linear parameter `θi`.
*   **Required Fix:** Clarify the language to distinguish between the tuning of the parameter `θi` (a factor of ~5) and the resulting suppression of the energy density `Ωα` (a factor of ~25). For example: "...a ~5x tuning of the misalignment initial condition `θi` is required, corresponding to a ~25x suppression of the ALP energy density...".

#### **NIT (Nitpicks)**

**P1B-N1:**
*   **Section/Page:** Abstract, p. 1
*   **Problem:** The abstract lists the H₀ tension as `~3.6σ`. The calculation on page 7 yields 3.61σ.
*   **Required Fix:** For consistency and precision, consider reporting this as `3.6σ` throughout, or `~3.6σ` if rounding is intended. The current usage is acceptable but could be tightened.

**P1B-N2:**
*   **Section/Page:** References, p. 22, citation [9]
*   **Problem:** The text (e.g., p. 3) refers to the likelihood as `HO.riess2020Mb`, while citing the 2022 Riess et al. paper (ApJL 934, L7). This could be confusing for readers trying to trace the exact data version used.
*   **Required Fix:** Add a brief clarifying sentence or a note in the text or bibliography explaining that the `riess2020Mb` likelihood name from the public code distribution is being used with the updated constraints from the cited 2022 paper.

---

## Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

This is a high-quality, methodologically rigorous paper that serves as an excellent example of a technical verification study. The authors demonstrate a clear understanding of the subtleties of their analyses and are transparent about all limitations and potential systematics. The work is thorough, well-documented, and easily reproducible. The findings are presented in a careful and well-scoped manner. After the minor corrections listed above are addressed, the manuscript will be a strong contribution to the literature and is recommended for publication.