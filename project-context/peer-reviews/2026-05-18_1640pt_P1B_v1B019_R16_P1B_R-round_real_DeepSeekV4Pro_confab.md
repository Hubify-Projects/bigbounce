# P1B R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1640pt_P1B_v1B019_R16
**Wall time**: 240.5s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=17945, completion=8906, reasoning=8422, total=26851

---

## PAPER-DEE-M1 (minor) — Undefined SNR figures unverifiable

**Location:** Abstract, Sec.~4 (around Eq.~\ref{eq:beta_namaster}), and throughout.  
**Issue:** The pipeline‑recovery SNR values (20.32, 25.71) are reported as headline numbers but never defined. No formula (e.g. mean‑recovered angle divided by MC standard deviation) appears anywhere, and no standard deviation is shown. A reader cannot reproduce or verify these SNR numbers from any displayed values.  
**Fix:** In Sec.~4, define SNR (e.g. SNR = β̂ / σ_β̂) and report the MC standard deviation of the recovered angle (or the equivalent SNR = 1/σ_β,relative). Update the text to make the calculation traceable.

## PAPER-DEE-M2 (minor) — Inconsistent \(H_0\) value

**Location:** Table~\ref{tab:verification} vs. SH0ES‑audit paragraph (below Table~\ref{tab:iter2_posterior}).  
**Issue:** The table gives \(H_0 = 67.68 \pm 1.06\) km s⁻¹ Mpc⁻¹, while the audit paragraph states \(H_0 = 67.69 \pm 1.06\). The abstract uses 67.68. The 0.01 difference is a trivial typo but makes the paper self‑contradictory.  
**Fix:** Reconcile to a single value (e.g. 67.68, which matches the table) throughout the text and abstract.

## PAPER-DEE-M3 (minor) — Incorrect bias bound in conclusions

**Location:** Conclusions section.  
**Issue:** The conclusions claim “bias ≤ 0.032°” based on the 0.27° injection, but Sec.~4 reports a bias of 0.040° for the 0.342° injection. The true worst‑case bias is 0.040°, so the “≤ 0.032°” statement is incorrect.  
**Fix:** Change the conclusions to “bias ≤ 0.040°” to match the data in Sec.~4.
