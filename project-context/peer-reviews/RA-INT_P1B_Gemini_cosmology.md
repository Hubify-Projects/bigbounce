# P1B RA-INT — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=f2838e5b pages=22
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 187.8s

---

**Referee Report for PRD Manuscript**

**Manuscript ID:** [Assigned by editor]
**Title:** Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model
**Author:** Houston Golden

This paper presents three technical verification analyses related to the Einstein-Cartan-Holst (ECH) spin-torsion cosmology program detailed in a companion paper. The analyses are: (1) a stock-CAMB MCMC analysis of the ΛCDM+ΔNeff model to serve as a null-consistency test; (2) a Monte Carlo validation of a NaMaster pseudo-Cℓ pipeline for measuring cosmic birefringence; and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper is exceptionally well-written, methodologically sound, and demonstrates a very high level of scientific rigor and transparency. The scope of each analysis is clearly defined, and crucial limitations and caveats are stated prominently and repeatedly, which is exemplary. The author makes a clear distinction between what is a direct test, a consistency check, a pipeline validation, and a sky measurement. The reproducibility materials are thorough and well-documented. The paper is a model of careful scientific work.

The analyses themselves are valuable contributions. The ΔNeff analysis provides a clean, updated constraint confirming the null result. The NaMaster pipeline analysis is a useful piece of methods work that carefully characterizes a known pipeline bias and convincingly identifies its source. The spectator-ALP analysis correctly concludes that the model can accommodate the observed signal, but highlights the significant fine-tuning of both the initial conditions and the coupling constant required, providing a clear and honest assessment of the model's status.

The manuscript is in excellent shape and is suitable for publication in Physical Review D after some minor corrections are addressed.

---

### **Detailed Findings**

#### **MAJOR**
(None)

#### **ESSENTIAL**
(None)

#### **MINOR**

**P1B-M1: Ambiguity of 3.6σ tension source in Abstract**
*   **Location:** Abstract, page 1
*   **Problem:** The abstract states that the ΔNeff extension "does not reduce the residual ~3.6σ tension with the SHOES local-distance-ladder H₀". This phrasing, immediately following the paper's own H₀ results, could imply the 3.6σ value is derived from the MCMC chains presented in the paper. The body (e.g., page 1, analysis (3)) correctly clarifies that "the 3.6σ headline used throughout this paper is from the published PR3+WMAP9 joint analysis of Eskilt & Komatsu [5]".
*   **Fix:** To avoid any ambiguity, the abstract should explicitly attribute the 3.6σ value to its source. Suggest adding a citation to [5] in the abstract at the first mention of the 3.6σ tension, similar to how it is done in the body.

**P1B-M2: Clarity of birefringence signal reference in Abstract**
*   **Location:** Abstract, page 1
*   **Problem:** The abstract mentions "The primary sky detection significance is the published Planck/ACT DR6 2.7-2.9σ [3, 4] (the β = 0.342° ±0.094°, 3.6σ headline used throughout this paper is from the published PR3+WMAP9 joint analysis of Eskilt & Komatsu [5]...)". This sentence combines two different results (the 2.7-2.9σ from Planck/ACT and the 3.6σ from WMAP+Planck). While the body is clear, the abstract would benefit from stating which specific measurement (i.e., the 3.6σ result from [5]) serves as the primary constraint for the spectator-ALP analysis.
*   **Fix:** Restructure the sentence to clearly state that the 3.6σ WMAP+Planck joint analysis result from [5] is the primary observational constraint used for the spectator-ALP consistency check.

#### **NIT (Cosmetic)**

**P1B-N1: Minor numerical inconsistency in w₀wₐ results**
*   **Location:** Section V.C, page 12
*   **Problem:** The text quotes posterior readouts for the `w₀wₐ` chain: `w₀ = -0.812 ± 0.044`, `wₐ = -0.667 ± 0.186`, and `w₀ + wₐ = -1.48 ± 0.15`. These values are slightly different from those in Table II (page 6), which are `w₀ = -0.8122 ± 0.0436`, `wₐ = -0.6666 ± 0.1864`, and `w₀ + wₐ = -1.4788 ± 0.1485`. The differences appear to be due to rounding.
*   **Fix:** Ensure the numbers in the text and Table II are consistent to the same number of significant figures, or add a note that the text values are rounded from the table.

**P1B-N2: Confusing sentence regarding numerical precision**
*   **Location:** Section VI, page 14
*   **Problem:** The sentence "rounding to two significant figures on Δφ/fₐ would give 4.65 × 10⁻³, so the third significant figure is sensitive to the precision of the EOM integration" is confusing. The calculation that yields 4.65 × 10⁻³ is not obvious from the context, and the sentence detracts from the otherwise clear main calculation which uses the four-figure value for Δφ/fₐ.
*   **Fix:** Please rephrase this sentence for clarity or remove it. The main point about the sensitivity to the precision of Δφ/fₐ is already made by the choice to use the four-figure value.

**P1B-N3: Use of informal jargon**
*   **Location:** Throughout
*   **Problem:** The term "load-bearing" is used frequently to describe results or assumptions that are central to the paper's conclusions. While its meaning is clear, it is informal.
*   **Fix:** Consider replacing "load-bearing" with more standard academic phrasing such as "primary," "key," "central," or "critical" in some instances for a more formal tone. This is a stylistic suggestion at the author's discretion.

**P1B-N4: Typo in likelihood name**
*   **Location:** Section VII, page 18
*   **Problem:** In the "Data and Code Availability" section, a likelihood name appears to have a copy-paste error: "planck_2018_lensing.k_2018_lensing.clik".
*   **Fix:** Correct this to "planck_2018_lensing.clik".

---

### **Summary recommendation**

**ACCEPT WITH MINOR CORRECTIONS**

The paper is an outstanding example of rigorous and transparent scientific analysis. It presents three well-executed and clearly reported technical studies. The author's meticulous attention to scoping, limitations, and reproducibility is commendable and meets the highest standards of the field. The required corrections are minor and address small points of clarity and consistency. I strongly recommend this manuscript for publication in Physical Review D once these minor points have been addressed.