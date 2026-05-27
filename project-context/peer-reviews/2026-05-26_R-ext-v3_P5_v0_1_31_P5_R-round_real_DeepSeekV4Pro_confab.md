# P5 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v3_P5_v0_1_31
**Wall time**: 383.8s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=26381, completion=12234, reasoning=10549, total=38615

---

## Adversarial Peer Review — Provenance & Reproducibility of Load‑Bearing Scalars

### PAPER-DEE-M1 (MAJOR) — Abstract filament concordance 0.026 pp cannot be reproduced from displayed values
**Location:** Abstract, “filament-class concordance 0.026 pp”; §VII.E “filament_like_vs_filament: 0.026 pp”.  
**Issue:** The abstract and body claim a Tempel‑vs‑V‑Web filament‑class concordance of 0.026 percentage points. The only displayed V‑Web filament CW fraction is 0.4980 (Table II) and the Tempel filament_like CW fraction is 0.4982 (Table III); their difference is 0.0002 = 0.02 pp, not 0.026 pp. The paper does not provide the V‑Web filament CW fraction on the Tempel‑overlap subsample, so the claimed 0.026 pp is unverifiable and appears inconsistent with the numbers shown.  
**Fix:** Either (a) report the V‑Web filament CW fraction on the overlap subsample and show the calculation yielding 0.026 pp, or (b) correct the concordance to 0.02 pp (the value implied by the displayed fractions). A static JSON artifact with the per‑class overlap CW fractions would also satisfy the provenance requirement.

### PAPER-DEE-N1 (nit) — Conclusions give rounded CW fractions but quote a range inconsistent with those rounded values
**Location:** §Conclusions, “{0.484, 0.503, 0.498, 0.496}, a range of 1.98 percentage points”.  
**Issue:** The displayed rounded values have max − min = 0.503 − 0.484 = 0.019 = 1.9 pp, not 1.98 pp. The range 1.98 pp is correct for the precise values (0.5034 − 0.4836) but the reader cannot recover it from the numbers printed in the conclusions.  
**Fix:** Either print the precise fractions (0.4836, 0.5034, 0.4980, 0.4963) in the conclusions, or compute the range from the rounded values (1.9 pp).
