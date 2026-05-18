# P1B_v1B018_R14 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1500pt
**Wall time**: 290.7s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=17488, completion=15916, reasoning=15357, total=33404

---

## PAPER-DEE-B1 (minor) – Conclusions bias bound contradicts body

**Section:** 8 (Conclusions), line: “bias ≤ 0.032° at SNR consistent with the ACT-noise floor.”  
**Issue:** The body (Sec. 4) explicitly reports a worst-case bias of 0.040° for the β=0.342° injection and states “we carry forward as the NaMaster systematic floor” 0.04°. The conclusions’ “≤ 0.032°” is therefore false for the full set of injections.  
**Fix:** Change to “bias ≤ 0.04° (worst-case)” or “bias ≤ 0.040°”.

## PAPER-DEE-B2 (nit) – NaMaster SNR values lack displayed uncertainties

**Section:** Abstract and Sec. 4 (lines: “SNR=20.32”, “SNR=25.71”).  
**Issue:** The SNR figures are headline scalars in the abstract, but the paper gives no recovered uncertainty (σ) for β̂. The arithmetic SNR = β̂/σ cannot be verified from displayed values alone.  
**Fix:** State the recovered σ (e.g., “β̂=0.238° ± 0.012°, SNR=20.32”) or provide the formula and the MC standard deviation.

## PAPER-DEE-B3 (nit) – ALP field-displacement range has no traceable script

**Section:** 6 (ALP consistency check), line: “Δφ/f_a ∈ [0.2, 1.1]”.  
**Issue:** This range is load-bearing for the naturalness argument (C_{aγ} ∼9–51). The paper says “Numerical integration … yields” but provides no script, output file, or dataset that produces Δφ/f_a.  
**Fix:** Add a reference to the integration code (e.g., a path in the reproducibility repository) or a table of computed displacements.

## PAPER-DEE-B4 (nit) – Liu et al. cross-validation σ differences unverifiable

**Section:** 3 (end of Sec. 3), line: “Our MCMC agrees at 0.5σ in H₀ and 0.4σ in σ₈.”  
**Issue:** The Liu et al. values for H₀ and σ₈ are not quoted, so the claimed σ differences cannot be checked against displayed numbers.  
**Fix:** Quote the Liu et al. central values and uncertainties, or state the numerical differences and combined errors.
