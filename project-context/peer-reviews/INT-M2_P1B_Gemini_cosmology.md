# P1B INT-M2 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=b3fe7527 pages=22
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 246.6s

---

Referee Report for "Technical Verification Companion to the ECH Spin-Torsion Program..." by Houston Golden

This paper presents three technical verification analyses related to the Einstein-Cartan-Holst (ECH) spin-torsion cosmology program of a companion paper. The analyses are: (1) a stock-CAMB MCMC analysis of the ΛCDM+ΔN_eff model, serving as a null test; (2) a validation of a NaMaster-based pseudo-C_l pipeline for cosmic birefringence on synthetic skies; and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper is exceptionally well-documented, with a strong emphasis on reproducibility, clear statements of scope, and thorough discussion of caveats and limitations. The analyses are carefully performed and the results are presented with a high degree of transparency. The overall quality of the work is very high and suitable for publication in Physical Review D, pending revisions to address the issues outlined below.

## Findings

### MAJOR

**P1B-M1: Prominence of Statistically Flawed `w_0w_a` Analysis**
*   **Location:** Section III (page 4), Section V.C (page 12), Table II (page 6), Section VII (page 17).
*   **Problem:** The paper presents a `w_0w_a` analysis that combines the DES-SN5YR and Pantheon+ supernova datasets using a simple product likelihood. As the authors correctly and repeatedly state, these datasets have an approximate 20% overlap in events, and combining them without a joint covariance matrix is statistically improper. This procedure artificially narrows the posterior widths and can bias the central values, making any derived "significance" or exclusion of ΛCDM unreliable. While the authors' transparency on this point is commendable, presenting these results in a main-body table (Table II) and discussing them at length in the main text lends them undue weight and risks misinterpretation by readers who may overlook the caveats.
*   **Required Fix:** The entire `w_0w_a` analysis, including Table II and its associated discussion, should be moved to an appendix. This appendix should be clearly titled to reflect the exploratory and methodologically-caveated nature of the analysis (e.g., "Appendix X: Exploratory `w_0w_a` Analysis with Overlap-Uncorrected Supernova Likelihoods"). The main text should be revised to briefly state that this exploratory check was performed but that a definitive analysis requires a proper joint-covariance treatment, directing the reader to the appendix for details. This restructuring would correctly subordinate the flawed analysis while preserving the authors' work.

### MINOR

**P1B-M2: Typographical Error in Birefringence Estimator Equation**
*   **Location:** Section IV, page 10, Equation (1).
*   **Problem:** Equation (1) defines the χ² estimator for the birefringence angle β. The equation is given as:
    `χ²(β) = ∑[C_l^EB,decoupled - sin(4β) C_l^EE,tmpl]²`
    The correct expression for the EB power spectrum induced by cosmic rotation is C_l^EB = (1/2)sin(4β)(C_l^EE - C_l^BB). The equation in the paper is missing the factor of 1/2. The text notes that the underlying analysis code uses the form `sin(2β)cos(2β)`, which is equivalent to `(1/2)sin(4β)`, indicating that this is a typographical error in the paper and not the analysis itself. However, it is a critical formula that must be presented correctly.
*   **Required Fix:** Correct Equation (1) by inserting the missing factor of 1/2:
    `χ²(β) = ∑[C_l^EB,decoupled - (1/2)sin(4β) C_l^EE,tmpl]²`

### NIT (Cosmetic)

**P1B-N1: Abstract Clarity on Birefringence Significance**
*   **Location:** Abstract, page 1.
*   **Problem:** The abstract states: "The primary sky detection significance is the published Planck/ACT DR6 2.7-2.9σ [3, 4] (the β = 0.342° ±0.094°, 3.6σ headline used throughout this paper is from the published PR3+WMAP9 joint analysis of Eskilt & Komatsu [5]...". This phrasing is slightly confusing, as it presents two different significance levels and three different data combinations in one sentence. The paper's spectator-ALP analysis exclusively uses the 3.6σ result from Eskilt & Komatsu [5] as its likelihood.
*   **Required Fix:** For clarity, streamline this part of the abstract to focus on the constraint that is actually used in the paper's analysis. For example: "The analysis is constrained by the published joint WMAP+Planck signal of β = 0.342° ± 0.094° (3.6σ) [5]." The other results can be mentioned in the main text for context.

**P1B-N2: Quantify Fine-Tuning in Abstract**
*   **Location:** Abstract, page 1.
*   **Problem:** The abstract correctly includes the crucial "Spectator-status caveat" and mentions that consistency requires "fine-tuning of the misalignment initial condition". The main text (Sec. VI, page 13) quantifies this as a "≥100× fine-tuning" or "~25×" relative to a different midpoint.
*   **Required Fix:** Add the quantitative measure of fine-tuning (e.g., "~25-fold") to the abstract. This would make the caveat more impactful and immediately convey the scale of the issue to the reader.

## Summary recommendation

**MAJOR REVISIONS**

The paper represents a substantial and high-quality contribution to cosmological methods verification. The authors' commitment to transparency and reproducibility is exemplary. The three analyses are well-motivated and, for the most part, rigorously executed and interpreted. The primary reason for the "Major Revisions" recommendation is the need to restructure the presentation of the `w_0w_a` analysis, which in its current form relies on a statistically flawed likelihood combination. By moving this section to an appendix, the authors can maintain the integrity of the paper's primary, robust conclusions while still documenting their exploratory work. The other requested changes are minor but will improve the clarity and precision of the manuscript. I expect that the authors can address these points straightforwardly, and I look forward to reviewing a revised version.