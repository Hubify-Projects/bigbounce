# P1B R29 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.55.pdf` md5=b776a111 pages=17
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 187.9s

---

## Referee Report: Technical Verification Companion to the ECH Spin-Torsion Program

This manuscript presents three technical analyses intended as a companion to a primary paper on the Einstein-Cartan-Holst (ECH) spin-torsion cosmology program. The three analyses are: (1) a stock-CAMB MCMC analysis of the ΛCDM+ΔNeff model, serving as a null test and proxy for extra radiation; (2) a Monte Carlo validation of a NaMaster-based pseudo-Cℓ pipeline for measuring cosmic birefringence; and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper is, for the most part, commendably transparent about the scope and limitations of its analyses. The validation work is detailed and thorough, and the authors are upfront about issues such as fine-tuning in the ALP model. However, the manuscript suffers from significant structural problems, contains numerous internal-review artifacts unsuitable for publication, and has shortcomings in its reproducibility materials that must be addressed. It requires major revisions before it can be considered for publication in Physical Review D.

### ESSENTIAL Revisions

These issues must be resolved for the paper to be acceptable.

**P1B-E1: Major Structural Reorganization Required (Sec. III, IV, V)**
*   **Location:** Pages 3-5.
*   **Problem:** The presentation of the MCMC results is disorganized and difficult to follow. The text in Section III ("Stock-CAMB ΛCDM+ΔNeff MCMC...") immediately begins discussing results from a `w₀-wₐ` analysis ("Physics interpretation (Table II)"), referencing Table II on page 5, before Table I (the actual ΛCDM+ΔNeff results) has even been presented on page 4. This makes the logical flow of the paper impossible to follow. The `w₀-wₐ` analysis, which is presented as an "empirical anchor" for a "quintom-B scenario," feels disconnected from the main ECH verification narrative and should be presented in its own self-contained section.
*   **Required Fix:** Reorganize the manuscript. Section III should present *only* the ΛCDM+ΔNeff analysis and the corresponding Table I. The `w₀-wₐ` analysis and Table II should be moved to a new, separate section (e.g., after the CMB E-B analysis) that clearly motivates its inclusion as a test of a related scenario. The discussion of results must follow the presentation of the tables they are based on.

**P1B-E2: Removal of Internal Review Artifacts**
*   **Location:** Pages 10, 15, 16.
*   **Problem:** The manuscript contains several elements that appear to be internal notes or artifacts from the authors' review process, which is inappropriate for a formal publication.
    1.  Page 10, Sec. VI: The text "...an earlier draft quoted [0.2, 1.1] with Δφ/fa ≈ 0.65 at m = H₀; those values do not reproduce from the committed integration and are corrected here)." is an internal version-control note.
    2.  Page 15, Appendix B: "Claims Classification" is an internal auditing tool.
    3.  Page 16, Table IV: The "Claims classification for this companion paper" table is an internal checklist and has no place in a published scientific paper.
*   **Required Fix:** Remove all of these internal artifacts. Appendix B and Table IV must be deleted entirely. The text on page 10 should be rephrased to simply state the current, correct values without referencing previous drafts.

**P1B-E3: Incomplete Reproducibility Materials**
*   **Location:** Page 14, Appendix A.
*   **Problem:** The reproducibility section states, "The ΛCDM+ΔNeff proxy chains are not pre-computed (regenerate via reproduce_cosmology.sh, ~4-12h per config on 4 CPU cores)". However, the converged `w₀-wₐ` chain and the ALP-MCMC chains *are* provided as committed bundles. This is inconsistent. The ΛCDM+ΔNeff chains produce the headline results of the first analysis (Table I) and are described as "frozen"; they are central to the paper and must be made directly available to the reader without requiring a computationally expensive regeneration.
*   **Required Fix:** Provide the final, "frozen" ΛCDM+ΔNeff MCMC chains for direct download, consistent with the other chains. All chains supporting headline results in the paper must be provided.

### MAJOR Revisions

These issues represent significant flaws that require careful revision.

**P1B-M1: Misleading "Spectator-ALP" Framing**
*   **Location:** Section VI (p. 10-13) and Abstract.
*   **Problem:** The analysis in Section VI is framed as a "Spectator-ALP Consistency Check." However, as honestly disclosed in footnote 5 (p. 10), the spectator condition (Ω_α ≪ 1) is only satisfied in a small, fine-tuned corner of the parameter space (`θᵢ ~ 0.1`), while the MCMC analysis explores a much wider prior (`θᵢ ∈ [0.01, π]`) where the ALP would behave as a dark energy component, not a spectator field. The MCMC posterior itself prefers regions outside the "natural" parameter box.
*   **Required Fix:** The framing of this section must be revised to more accurately reflect what was done. The title should be changed to something like "Consistency Check with an Axion-Like Particle Model." The abstract and conclusions must clarify that the model can accommodate the data, but only in a non-spectator, dark-energy-like regime or a fine-tuned spectator regime, both of which require "unnatural" parameter choices (either large couplings or a tuned initial misalignment angle).

**P1B-M2: Garbled Formula and Unclear Notation**
*   **Location:** Page 7 (NaMaster pipeline) and Page 11 (Birefringence value).
*   **Problem:**
    1.  Page 7: The formula for per-pixel noise RMS is given as `σ_pix = Δρ [π/(180×60)]//)`. The `//)` appears to be a typo or rendering error, making the expression unintelligible. While the calculated value of 1.455 μK is correct, the formula presented is not.
    2.  Page 11, Eq (3): The expression for β includes the term `α_EM x 8`. This is ambiguous notation. From the calculation, it appears `α_EM` is the fine-structure constant and 8 is the value of a model-dependent coupling coefficient, `C_aγ`. This should be written clearly as `C_aγ α_EM`.
*   **Required Fix:**
    1.  Correct the formula for `σ_pix` on page 7. A clear expression, such as `σ_pix = Δ_P / √Ω_pix`, where `Δ_P` is the noise level in μK-arcmin and `Ω_pix` is the pixel area in arcmin², should be used.
    2.  Correct the notation in and around Eq (3) on page 11. Replace `α_EM x 8` with standard notation like `C_aγ α_EM` and explicitly state that `C_aγ = 8` for this fiducial calculation.

**P1B-M3: Uncomputed Quantitative Claims (Rule 17)**
*   **Location:** Page 12, paragraph starting "The resulting posterior is broad...".
*   **Problem:** The text makes several statements about posterior mass fractions based on different priors (e.g., flat-θᵢ vs. flat-cosθᵢ) without providing a clear pointer to the artifact or table where these numbers can be verified. For example, "the quoted spectator-sliver posterior fractions would decrease further under that prior swap". While a direct rerun is mentioned later, the claim is presented without immediate support.
*   **Required Fix:** For every quantitative claim about posterior fractions or parameter shifts under different analysis choices (e.g., different priors), provide a specific artifact name or table entry where the supporting number can be found. The claim about the `cos(θ_i)` prior is supported by a parenthetical reference later, but this should be standard practice for all such claims.

### MINOR Revisions

**P1B-m1: Confusing One-Sided Limit Definition**
*   **Location:** Page 3, paragraph starting "Frozen MCMC program...".
*   **Problem:** The definition of the one-sided 95% upper limit is non-standard: "read from the posterior CDF at the 95th percentile of the ΔNeff > 0 half". This is confusing. A standard one-sided 95% upper limit corresponds to the 95th percentile of the *full* posterior distribution.
*   **Required Fix:** Either use the standard definition for the one-sided limit or provide a much clearer explanation and justification for this unconventional choice. If the standard definition is used, the value should be re-calculated.

**P1B-m2: Irrelevant Content in Reproducibility Appendix**
*   **Location:** Page 14, Appendix A.
*   **Problem:** The "What is NOT included" list contains the item: "No CNN galaxy classifier is included; the hierarchical fit uses published catalog labels." This appears to be content related to a different paper in the series (Paper IV is mentioned) and is irrelevant to the MCMC and CMB analyses in this manuscript.
*   **Required Fix:** Remove this irrelevant sentence from Appendix A.

**P1B-m3: Inconsistent Citation for SH0ES Data**
*   **Location:** Page 4, footnote a; Page 16, reference [9].
*   **Problem:** The text and YAML configurations refer to `HO.riess2020Mb`, implying data from a 2020 or 2021 paper. However, the citation provided is Riess et al. 2022 [9]. While the 2022 paper is the most recent, the specific likelihood used should be cited precisely.
*   **Required Fix:** Ensure the citation matches the exact likelihood version used in the analysis. If the `M_B` value is from one paper and the `H₀` value from another, this should be stated explicitly for clarity.

### NITs (Cosmetic)

**P1B-N1: Duplicate Phrase**
*   **Location:** Page 8, footnote 3.
*   **Problem:** The text reads "...the appropriate quantity for evaluating the deconvolution pipeline. It is not the significance of the recovered angle itself. The sky-fraction sweep artifact...". The sentence structure is slightly awkward.
*   **Required Fix:** Consider rephrasing for clarity, e.g., "This quantity, which evaluates the pipeline's ability to recover a known signal, is distinct from the statistical significance of the recovered angle itself."

## Summary recommendation

**MAJOR REVISIONS**

This manuscript contains three well-executed and thoroughly documented technical analyses. The authors' commitment to transparency regarding the scope, limitations, and potential systematic effects in their work is a significant strength. However, the paper is not yet ready for publication. The severe structural disorganization, which obscures the main results, and the inclusion of numerous internal-review artifacts are unacceptable for a journal of this caliber. Furthermore, the incomplete state of the reproducibility materials for the headline MCMC results must be rectified. Once these essential and major issues have been comprehensively addressed, the paper will represent a valuable contribution to the literature.