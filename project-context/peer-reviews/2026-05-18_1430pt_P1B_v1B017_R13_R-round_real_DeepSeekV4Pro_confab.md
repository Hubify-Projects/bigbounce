# P1B_v1B017_R13 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1430pt
**Wall time**: 182.0s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=17475, completion=11968, reasoning=11167, total=29443

---

## PAPER-DEE-M1 (MAJOR)
**Section 6 (Cosmic Birefringence: Spectator ALP Consistency Check)**  
The stated birefringence range `β ≈ 0.17–0.43°` over `C_{aγ} ∈ [4,12]`, `m/H_0 ∈ [1,3]`, `θ_i ∈ [0.5,2]` is arithmetically inconsistent with the paper’s own numbers.  
Using the conversion `β [deg] = (α_EM/(4π)) × C_{aγ} × (Δφ/f_a)` with `α_EM/(4π) ≈ 0.03326°` and the numerically integrated field-displacement range `Δφ/f_a ∈ [0.2, 1.1]` (stated in the same section), the correct range is **0.027°–0.44°**, not 0.17–0.43°. The lower bound is off by a factor of ~6.  
**Fix:** Replace `0.17–0.43°` with `0.03–0.44°` (or the exact computed bounds) and ensure the text reflects the `Δφ/f_a` range, not `θ_i`.

## PAPER-DEE-M2 (minor)
**Section 8 (Conclusions), NaMaster bias statement**  
The conclusions claim the pipeline recovers injected angles with “bias ≤0.032°”, but Section 4 explicitly reports a worst-case bias of **0.040°** for the `β = 0.342°` injection. The abstract also quotes only the 0.032° figure without qualification.  
**Fix:** Change “bias ≤0.032°” to “bias ≤0.040° (amplitude-dependent; 0.032° for the 0.27° injection)” to match the detailed results.

## PAPER-DEE-M3 (minor)
**Inconsistent `H_0` full-tension value**  
The abstract and Table 1 give `H_0 = 67.68 ± 1.06 km/s/Mpc` for the full-tension combination, but the caveats text accompanying Table 1B (near the SH0ES audit) quotes `67.69 ± 1.06`. The 0.01 discrepancy is likely a typo.  
**Fix:** Harmonise to the single value that appears in the chain output (presumably 67.68, as used in the abstract and Table 1).

## PAPER-DEE-M4 (nit)
**Abstract, NaMaster bias wording**  
The abstract states “pipeline-recovery bias 0.032°” without noting that this applies only to the `β = 0.27°` injection and that the bias is amplitude-dependent (0.040° for the larger injection). This could mislead a reader who skips the main text.  
**Fix:** Add a parenthetical “(for the 0.27° injection)” or replace with “≤0.040°” to match the conclusions once corrected.

## PAPER-DEE-M5 (nit)
**SNR figures lack definition and provenance in the text**  
The pipeline-recovery SNR values (20.32, 25.71) are headline numbers in the abstract and Section 4, but the paper does not define how SNR is computed (e.g., `β̂ / σ_{mean}` from the 500 MC realizations) and no `σ` is reported. A reader cannot verify the SNR from the displayed numbers alone.  
**Fix:** Add a sentence defining SNR (e.g., “SNR = mean recovered β divided by the standard error of the mean across 500 realizations”) and report the corresponding uncertainty.
