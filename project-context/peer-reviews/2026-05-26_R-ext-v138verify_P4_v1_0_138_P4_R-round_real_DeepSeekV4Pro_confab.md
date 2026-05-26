# P4 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v138verify_P4_v1_0_138
**Wall time**: 235.9s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=101135, completion=11055, reasoning=10678, total=112190

---

## PAPER-DEE-M1 (minor)
**Location:** Abstract, line "∼0.6% residual amplitude" for the real‑space dipole.  
**Issue:** The abstract states a residual dipole amplitude of ∼0.6 % for the Catalog C real‑space dipole, but the body of the paper (Sec. 4.3) reports only the significance (+0.43σ, p=0.30) and never gives the fitted amplitude or its uncertainty. No artifact or calculation is cited that yields 0.6 %.  
**Fix:** Either remove the unsupported amplitude from the abstract, or add the best‑fit dipole amplitude (with error) to Sec. 4.3 and reference the artifact (e.g., `dipolar_analysis.log` or `summary.json`) that contains it.

## PAPER-DEE-M2 (minor)
**Location:** Discussion, v1.0.138 extended joint‑fit paragraph (Sec. VI.D).  
**Issue:** The text reports “z(data vs 1.7%) = –250.2” from A_dipole = 0.225 % f_CW and σ = 0.006 % f_CW. Simple arithmetic gives (0.225 – 1.7) / 0.006 = –245.8, a discrepancy of 4.4σ. The displayed numbers do not reproduce the stated z‑score.  
**Fix:** Provide the exact unrounded values used in the calculation, or correct the rounding so that the quoted amplitude, uncertainty, and z‑score are mutually consistent.

---

**No blocker‑grade findings.** The remaining headline numbers in the abstract and conclusions are traceable to specific JSON artifacts or analytic derivations described in the paper.
