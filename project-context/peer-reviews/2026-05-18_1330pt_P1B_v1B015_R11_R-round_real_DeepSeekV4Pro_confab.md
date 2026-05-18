# P1B_v1B015_R11 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1330pt
**Wall time**: 292.8s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=17388, completion=9613, reasoning=8535, total=27001

---

# Adversarial Peer Review: NUMBERS WITHOUT TRACEABLE SOURCES

## PAPER-DEE-B1 (BLOCKER) — ALP β-range arithmetic error
**Location:** Section 6 (Cosmic Birefringence), paragraph “Birefringence value.”  
**Issue:** The text states “The prediction spans β≈0.17–0.43° over C_{aγ}∈[4,12], m/H0∈[1,3], θ_i∈[0.5,2]”. Using the paper’s own Δϕ/f_a range [0.2, 1.1] and α_EM/(4π) ≈ 5.8×10⁻⁴, the correct product is β ∈ [4×0.2, 12×1.1] × 5.8×10⁻⁴ rad = [0.00046, 0.00766] rad = [0.027°, 0.44°]. The lower bound 0.17° is inflated by a factor of ~6 and cannot be obtained from the stated parameter ranges.  
**Fix:** Replace “0.17–0.43°” with the computed range “0.03–0.44°” or re-derive the lower bound with a transparent formula.

---

## PAPER-DEE-B2 (BLOCKER) — NaMaster bias ceiling contradicts measured bias
**Location:** Abstract (bias 0.032°) and Conclusions (“bias ≤ 0.032°”) vs. Section 4 (“Δβ̂ = 0.040° at injection β=0.342°”).  
**Issue:** The conclusions assert a pipeline bias ceiling of ≤0.032°, but the body explicitly reports a bias of 0.040° for the Planck+ACT injection and states “we carry forward the NaMaster systematic floor as 0.04°”. This is a direct internal contradiction.  
**Fix:** Change the conclusions to “bias ≤ 0.040°” or clearly differentiate the two injection cases and state the worst-case bias.

---

## PAPER-DEE-B3 (MAJOR) — NaMaster SNR lacks auxiliary uncertainty
**Location:** Abstract and Section 4, “SNR=20.32”.  
**Issue:** The SNR is a ratio of recovered β̂ to its standard error, but the paper provides no σ_{β̂} (standard deviation across MC realizations). Without this number, the SNR cannot be verified from the displayed values, and the reader cannot reconcile it with the 0.032° bias or the noise model.  
**Fix:** Report the MC standard deviation of β̂ (or directly the standard error of the mean) used to compute SNR=20.32.

---

## PAPER-DEE-B4 (MAJOR) — Opaque factor 1.07 in β line
**Location:** Section 6, display equation: β ≈ (α_EM × 8)/(4π) × 1.07 ≈ 0.29°.  
**Issue:** The dimensionless factor 1.07 appears without derivation or definition. It is not linked to any previously stated Δϕ/f_a value (0.65, 1.0, etc.), and no calculation shows how 1.07 emerges for m≈2H₀, θ_i=1. The number is load‑bearing for the 0.29° claim yet is mathematically orphaned.  
**Fix:** Define the factor explicitly as Δϕ/f_a for those parameter values and provide the integration result that yields 1.07, or remove the line in favor of the later fiducial 0.27° derivation.

---

## PAPER-DEE-B5 (minor) — No artifact pointer for ΔN_eff/H₀ posteriors
**Location:** Abstract and Table 1 (ΔN_eff, H₀).  
**Issue:** The primary MCMC posteriors (ΔN_eff = −0.020 ± 0.169, H₀ = 67.68 ± 1.06, etc.) lack a direct reference to a frozen summary file (JSON/GetDist output) analogous to the URL given for the iter2 posterior (“posterior_summary.txt”). The chains must be regenerated, and no static artifact is cited.  
**Fix:** Point to a specific on‑disk posterior summary file (e.g., a GetDist table) in the reproducibility repository for each frozen combination.

---

## PAPER-DEE-B6 (nit) — “w_0 + w_a” error missing covariance statement
**Location:** Table 1B, row “w_0 + w_a”.  
**Issue:** The error ±0.1485 on the linear combination w₀+wₐ is listed without any mention of the correlation/covariance between w₀ and wₐ. The paper does not confirm that the error was computed including the cross‑term, and a reader cannot verify the value from the marginal errors alone.  
**Fix:** Add a footnote stating that the error is computed from the full posterior covariance matrix, possibly showing the derived correlation coefficient.
