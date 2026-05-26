# P4 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v134verify_P4_v1_0_134
**Wall time**: 181.6s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=97144, completion=7041, reasoning=6766, total=104185

---

## PAPER-DEE-A1 (MAJOR)

**Location:** Abstract, sentence: "The real-space post-TTA Catalog C dipole is $+0.43\sigmaunit$ ($p=0.30$, $\sim\!0.6\%$ residual amplitude)."

**Issue:** The "$\sim\!0.6\%$ residual amplitude" is a load-bearing scalar in the abstract, but the body of the paper never reports the best‑fit dipole amplitude for Catalog C. Section \ref{sec:dipole} only gives the significance ($0.43\sigma$) and $p$‑value; no amplitude value, derivation, or artifact‑backed provenance appears anywhere. The reader cannot verify this number from the text or from a cited file, and the arithmetic linking it to the cited significance is not shown.

**Fix:** Either (a) report the dipole amplitude in Section \ref{sec:dipole} with an explicit reference to the artifact that produced it (e.g., `dipolar_analysis.log`), or (b) remove the "$\sim\!0.6\%$ residual amplitude" phrase from the abstract and rely solely on the significance $+0.43\sigma$ and $p=0.30$, which are already sufficient to convey the null result.
