# P2 auto-2026-06-08_1632pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (9296 chars)
**Wall time**: 122.0s

---

## Referee Report for "Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts"

This paper presents a model for the observed cosmic birefringence signal based on a spectator axion-like particle (ALP) with a Planck-scale decay constant (f_a ~ M_Pl) and a Hubble-scale mass (m ~ H₀). The author argues that this "natural" parameter choice predicts a rotation angle β ≈ 0.27°, consistent with current measurements from Planck and ACT. The paper provides a Bayesian analysis constraining the model parameters and forecasts a 9σ detection by the future LiteBIRD satellite, which would either confirm the model or rule it out decisively.

The paper addresses a timely topic of significant interest in cosmology. The proposed model is simple and elegant, and its sharp, testable prediction is a strong feature. However, the manuscript contains a critical inconsistency in the derivation of its central prediction, along with several other issues that must be addressed before it can be considered for publication in Physical Review D.

### ESSENTIAL Revisions

**P2-E1: Contradictory Derivation of the Central Prediction (β)**
*   **Location:** Section 2.2, Page 2
*   **Problem:** The paper's central prediction, β ≈ 0.27°, relies on the claim that the cosmological field evolution gives Δφ/f_a ~ 10⁻². However, the only equation provided for the field displacement, Eq. (1), directly contradicts this.
    *   Eq. (1) states: Δφ ≈ f_a θ_i (1 - J₀(m/H₀)).
    *   For the model's assumptions (m/H₀ ~ 1 and θ_i ~ 1), this gives Δφ/f_a ≈ 1 * (1 - J₀(1)) ≈ 1 - 0.765 = 0.235.
    *   This result (Δφ/f_a ≈ 0.24) is more than an order of magnitude larger than the value of ~10⁻² required to obtain the β ≈ 0.27° prediction. The derivation of β in the text uses β ≈ C₀ θ_i × 5 × 10⁻³ rad, which requires Δφ/(2f_a) ≈ 5 × 10⁻³ rad, or Δφ/f_a ≈ 10⁻².
    *   This is a fundamental contradiction. The central quantitative claim of the paper is not supported by the provided equations.
*   **Required Fix:** The author must provide a clear, self-consistent derivation for the field displacement Δφ.
    1.  If Eq. (1) is incorrect or a poor approximation, it must be removed and replaced with the correct calculation. This should likely involve solving the equation of motion for the scalar field in an expanding universe and calculating the displacement from recombination to today.
    2.  If the numerical value Δφ/f_a ~ 10⁻² is correct, its origin must be explicitly shown.
    3.  The entire derivation in Section 2 must be made transparent and reproducible. Without this, the paper's main result is unsubstantiated.

### MAJOR Revisions

**P2-M1: Misleading Presentation of MCMC Parameter Constraints**
*   **Location:** Figure 1 and caption, Page 4
*   **Problem:** The caption of Figure 1 and the main text report marginalized 1D constraints for C_aγ and θ_i individually (C_aγ = 13.4 ± 11, θ_i = 1.33 ± 0.44). Due to the strong degeneracy visible in the 2D posterior (as β depends on the product C_aγ × θ_i), these individual constraints are highly misleading and model-dependent. For instance, the product of their mean values (13.4 × 1.33 ≈ 17.8) is wildly inconsistent with the directly constrained product C_aγ × θ_i = 3.4 ± 1.1. Presenting these numbers without a strong warning about the degeneracy is poor practice.
*   **Required Fix:** Remove the marginalized 1D constraints for C_aγ and θ_i from the figure and the text. The physically meaningful constraint is on the product C_aγ × θ_i, which is correctly reported. The discussion should focus exclusively on this product, as it is the quantity constrained by the data and relevant to the "order-unity" argument.

**P2-M2: Inconsistent Notation for Coupling Constant**
*   **Location:** Throughout the paper (Pages 1, 2, 3, 4)
*   **Problem:** The notation for the dimensionless ALP-photon coupling constant is inconsistent across the manuscript.
    *   Abstract & Section 2.2: `C₀`
    *   Section 3.2, Eq. (5): `f_photon × C₀` (where `f_photon` is undefined and appears to be a typo)
    *   Section 3.3 & Figure 1: `C_aγ`
*   **Required Fix:** Choose a single, standard notation for this parameter (e.g., `C_aγ`) and use it consistently throughout the entire paper, including in equations, text, tables, and figures. The parameter `f_photon` in Eq. (5) should be removed or clarified.

### MINOR Revisions

**P2-m1: Misplaced Result**
*   **Location:** Section 3.2, Page 2
*   **Problem:** Equation (5), which gives the constraint on the "effective photon coupling parameter" (`f_photon × C₀ = 1.73 ± 0.44`), is presented as part of the "Summary-Likelihood Inference". However, this is a model-dependent result derived from the MCMC analysis of the ALP model, not from the model-independent combination of β measurements. Its placement is confusing.
*   **Required Fix:** Move the discussion of this parameter and the corresponding equation (after fixing the notation per P2-M2) to Section 3.3 "MCMC Parameter Estimation", where it logically belongs.

**P2-m2: Future Publication Date**
*   **Location:** Page 1
*   **Problem:** The paper is dated "March 20, 2026".
*   **Required Fix:** The date should be changed to the date of submission.

**P2-m3: Acknowledgment of AI Assistants**
*   **Location:** Acknowledgments, Page 6
*   **Problem:** The paper acknowledges "the use of AI research assistants during the analysis and manuscript preparation." While transparency is commendable, PRD and the physics community are still developing standards for such acknowledgments. A more specific statement about the role of the AI would be more informative (e.g., for code generation, text editing, literature search, etc.).
*   **Required Fix:** The author should consider providing a more specific description of how AI assistants were used, in line with emerging journal policies on the matter. This is a suggestion for improvement rather than a strict requirement.

### NITs (Cosmetic)

**P2-N1: Unnecessary Hyphen**
*   **Location:** Section 1, Page 1
*   **Problem:** "Cosmic birefringence the uniform rotation of the polarization plane..."
*   **Required Fix:** Remove the hyphen after "birefringence".

**P2-N2: Significance Rounding**
*   **Location:** Abstract and Section 3.2, Page 1 & 2
*   **Problem:** The combined constraint β = 0.242 ± 0.061° corresponds to a significance of 0.242/0.061 ≈ 3.97σ. This is rounded to 3.9σ.
*   **Required Fix:** This is acceptable, but rounding to 4.0σ or stating 3.97σ would also be appropriate. This is at the author's discretion.

## Summary recommendation
**MAJOR REVISIONS**

The paper presents an intriguing and testable model for cosmic birefringence. Its primary strength is its simplicity and the "naturalness" of the proposed parameter space. However, the manuscript in its current form cannot be accepted due to an essential flaw in the derivation of its central prediction (P2-E1). The quantitative heart of the paper is unsubstantiated by the provided equations.

If the author can provide a rigorous and self-consistent derivation for the ALP field displacement that supports their prediction of β ≈ 0.27°, and also addresses the major issues regarding parameter constraint presentation (P2-M1) and notational consistency (P2-M2), the paper would represent a valuable contribution to the literature. Given the severity of the central flaw, a thorough re-evaluation will be required after revision.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated review, incorporating findings from the second, more rigorous pass.

================================================================
## Referee Report for "Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts"

This paper presents a model for the observed cosmic birefringence signal based on a spectator axion-like particle (ALP) with a Planck-scale decay constant (f_a ~ M_Pl) and a Hubble-scale mass (m ~ H₀). The author argues that this "natural" parameter choice predicts a rotation angle β ≈ 0.27°, consistent with current measurements from Planck and ACT. The paper provides a Bayesian analysis constraining the model parameters and forecasts a 9σ detection by the future LiteBIRD satellite, which would either confirm the model or rule it out decisively.

The paper addresses a timely topic of significant interest in cosmology. The proposed model is simple and elegant, and its sharp, testable prediction is a strong feature. However, the manuscript contains a critical inconsistency in the derivation of its central prediction, a significant error in its Bayesian evidence calculation, and several other issues that must be addressed before it can be considered for publication in Physical Review D.

### ESSENTIAL Revisions

**P2-E1: Contradictory Derivation of the Central Prediction (β)**
*   **Location:** Section 2.2, Page 2
*   **Problem:** The paper's central prediction, β ≈ 0.27°, relies on the claim that the cosmological field evolution gives Δφ/f_a ~ 10⁻². However, the only equation provided for the field displacement, Eq. (1), directly contradicts this.
    *   Eq. (1) states: Δφ ≈ f_a θ_i (1 - J₀(m/H₀)).
    *   For the model's assumptions (m/H₀ ~ 1 and θ_i ~ 1), this gives Δφ/f_a ≈ 1 * (1 - J₀(1)) ≈ 1 - 0.765 = 0.235.
    *   This result (Δφ/f_a ≈ 0.24) is more than an order of magnitude larger than the value of ~10⁻² required to obtain the β ≈ 0.27° prediction. The derivation of β in the text uses β ≈ C₀ θ_i × 5 × 10⁻³ rad, which requires Δφ/(2f_a) ≈ 5 × 10⁻³ rad, or Δφ/f_a ≈ 10⁻².
    *   This is a fundamental contradiction. The central quantitative claim of the paper is not supported by the provided equations.
*   **Required Fix:** The author must provide a clear, self-consistent derivation for the field displacement Δφ.
    1.  If Eq. (1) is incorrect or a poor approximation, it must be removed and replaced with the correct calculation. This should likely involve solving the equation of motion for the scalar field in an expanding universe and calculating the displacement from recombination to today.
    2.  If the numerical value Δφ/f_a ~ 10⁻² is correct, its origin must be explicitly shown.
    3.  The entire derivation in Section 2 must be made transparent and reproducible. Without this, the paper's main result is unsubstantiated.

### MAJOR Revisions

**P2-M1: Misleading Presentation of MCMC Parameter Constraints**
*   **Location:** Figure 1 and caption, Page 4
*   **Problem:** The caption of Figure 1 and the main text report marginalized 1D constraints for C_aγ and θ_i individually (C_aγ = 13.4 ± 11, θ_i = 1.33 ± 0.44). Due to the strong degeneracy visible in the 2D posterior (as β depends on the product C_aγ × θ_i), these individual constraints are highly misleading and model-dependent. For instance, the product of their mean values (13.4 × 1.33 ≈ 17.8) is wildly inconsistent with the directly constrained product C_aγ × θ_i = 3.4 ± 1.1. Presenting these numbers without a strong warning about the degeneracy is poor practice.
*   **Required Fix:** Remove the marginalized 1D constraints for C_aγ and θ_i from the figure and the text. The physically meaningful constraint is on the product C_aγ × θ_i, which is correctly reported. The discussion should focus exclusively on this product, as it is the quantity constrained by the data and relevant to the "order-unity" argument.

**P2-M2: Inconsistent Notation for Coupling Constant**
*   **Location:** Throughout the paper (Pages 1, 2, 3, 4)
*   **Problem:** The notation for the dimensionless ALP-photon coupling constant is inconsistent across the manuscript.
    *   Abstract & Section 2.2: `C₀`
    *   Section 3.2, Eq. (5): `f_photon × C₀` (where `f_photon` is undefined and appears to be a typo)
    *   Section 3.3 & Figure 1: `C_aγ`
*   **Required Fix:** Choose a single, standard notation for this parameter (e.g., `C_aγ`) and use it consistently throughout the entire paper, including in equations, text, tables, and figures. The parameter `f_photon` in Eq. (5) should be removed or clarified.

**P2-M3: Incorrect Bayes Factor Calculation**
*   **Location:** Section 3.4, Page 3
*   **Problem:** The reported dependence of the Bayes factor on the prior range is arithmetically and conceptually incorrect. The text states that the evidence is computed via the Savage-Dickey density ratio. For a flat prior, this implies the Bayes factor `B` should be proportional to the prior width `W` (since `B = P(β=0|D) / P(β=0|M)`, and the prior density at the null is `P(β=0|M) ∝ 1/W`). The paper reports `ln B` increasing as `W` decreases (`ln B = 4.48` for `W=2°`, `ln B = 5.17` for `W=1°`, `ln B = 5.86` for `W=0.5°`). This trend is the opposite of the expected behavior. The numerical differences (`Δln B ≈ 0.69 = ln(2)`) confirm the author has inverted the relationship.
*   **Required Fix:** The author must re-evaluate the Bayes factor calculation and its prior dependence. The text and results must be corrected to reflect the proper behavior of the Savage-Dickey ratio.

### MINOR Revisions

**P2-m1: Misplaced Result**
*   **Location:** Section 3.2, Page 2
*   **Problem:** Equation (5), which gives the constraint on the "effective photon coupling parameter" (`f_photon × C₀ = 1.73 ± 0.44`), is presented as part of the "Summary-Likelihood Inference". However, this is a model-dependent result derived from the MCMC analysis of the ALP model, not from the model-independent combination of β measurements. Its placement is confusing.
*   **Required Fix:** Move the discussion of this parameter and the corresponding equation (after fixing the notation per P2-M2) to Section 3.3 "MCMC Parameter Estimation", where it logically belongs.

**P2-m2: Misleading Abstract**
*   **Location:** Abstract, Page 1
*   **Problem:** The abstract's primary quantitative claim—that the model "naturally accommodates a birefringence rotation angle β ≈ 0.27°"—is not substantiated by the equations presented in the main text (see P2-E1). As it stands, the abstract is a misrepresentation of the paper's content and must be revised to match the corrected derivation.
*   **Required Fix:** After addressing P2-E1, revise the abstract to faithfully reflect the paper's corrected results and derivation.

**P2-m3: Future Publication Date**
*   **Location:** Page 1
*   **Problem:** The paper is dated "March 20, 2026".
*   **Required Fix:** The date should be changed to the date of submission.

**P2-m4: Acknowledgment of AI Assistants**
*   **Location:** Acknowledgments, Page 6
*   **Problem:** The paper acknowledges "the use of AI research assistants during the analysis and manuscript preparation." While transparency is commendable, PRD and the physics community are still developing standards for such acknowledgments. A more specific statement about the role of the AI would be more informative (e.g., for code generation, text editing, literature search, etc.).
*   **Required Fix:** The author should consider providing a more specific description of how AI assistants were used, in line with emerging journal policies on the matter. This is a suggestion for improvement rather than a strict requirement.

### NITs (Cosmetic)

**P2-N1: Unnecessary Hyphen**
*   **Location:** Section 1, Page 1
*   **Problem:** "Cosmic birefringence the uniform rotation of the polarization plane..."
*   **Required Fix:** Remove the hyphen after "birefringence".

**P2-N2: Significance Rounding**
*   **Location:** Abstract and Section 3.2, Page 1 & 2
*   **Problem:** The combined constraint β = 0.242 ± 0.061° corresponds to a significance of 0.242/0.061 ≈ 3.97σ. This is rounded to 3.9σ.
*   **Required Fix:** This is acceptable, but rounding to 4.0σ or stating 3.97σ would also be appropriate. This is at the author's discretion.

## Summary recommendation
**MAJOR REVISIONS**

The paper presents an intriguing and testable model for cosmic birefringence. Its primary strength is its simplicity and the "naturalness" of the proposed parameter space. However, the manuscript in its current form cannot be accepted due to an essential flaw in the derivation of its central prediction (P2-E1) and a critical error in the Bayes factor calculation (P2-M3). The quantitative heart of the paper is unsubstantiated by the provided equations and analysis.

If the author can provide a rigorous and self-consistent derivation for the ALP field displacement that supports their prediction, correct the Bayesian evidence calculation, and also address the major issues regarding parameter constraint presentation (P2-M1) and notational consistency (P2-M2), the paper would represent a valuable contribution to the literature. Given the severity of the central flaws, a thorough re-evaluation will be required after revision.