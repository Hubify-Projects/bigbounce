# paper3 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R23_P3_v3_1_56
**Wall time**: 237.4s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=64244, completion=8693, reasoning=7812, total=72937

---

## PAPER-DEE-B1 — BLOCKER — Abstract: false claim of ~98% blue-excess retention in native LAMOST autoencoder

**Location:** Abstract, sentence beginning “the native LAMOST autoencoder retains a ~98% blue‑excess instrumental contamination signature”.

**Issue:** The paper’s LAMOST native‑retrain section (§3.4) does **not** report any measurement of the residual blue‑excess fraction in the native model. Caveat (ii) in §6.4 explicitly states that quantifying the residual colour skew “is part of the post‑rescore validation and will be reported alongside the final catalog” — i.e., the number has not been derived. The “98%” figure is inherited from the cross‑transfer analysis and is unsupported by any on‑disk artifact for the native model.

**Fix:** Remove the unsupported percentage from the abstract. Replace with a statement that the residual contamination of the native LAMOST anomaly set has not yet been measured, or cite a specific analysis artifact that reports it.

---

## PAPER-DEE-M1 — MAJOR — Abstract & Conclusions: genuine novelty fraction (17.8%) lacks traceable artifact

**Location:** Abstract and Conclusions, “genuine novelty fraction of ∼17.8%” from cross‑matching the top‑1 000 DESI anomalies against 20 all‑sky catalogues.

**Issue:** The paper provides no file path, script, or archive identifier for the cross‑match result. The data‑availability section lists primary object tables and injection‑recovery JSON files, but nothing that records the 178/1 000 count. The 17.8% figure is a prominent headline number that cannot be reproduced from the documented artifacts.

**Fix:** Add an explicit pointer to the cross‑match artifact (e.g., a parquet or CSV in the data release) or describe the precise query and catalogue list in a reproducible appendix. Until then, the figure should be downgraded to a private estimate.

---

## PAPER-DEE-M2 — MAJOR — Fisher‑positivity coefficient c = 0.0747 and σ(f_NL)=8.14 rely on an unsubstantiated anchor

**Location:** §5 and caveat (i) in §6.4; the derivation of the Fisher‑positivity parametric form.

**Issue:** The coefficient $c = 0.0747$ is stated to follow from two anchor values $\sigma(0)=8.98$ and $\sigma(0.15)=8.43$. No Fisher‑pipeline artifact for the $\alpha=0.15$ point is cited, and the arithmetic from the rounded values yields $c\approx 0.0743$, not $0.0747$. Although the resulting $\sigma(f_{\rm NL})=8.14$ is stable, the provenance of the central value is incomplete; readers cannot trace the exact Fisher run that produced $\sigma(0.15)=8.43$.

**Fix:** Either release the Fisher pipeline artifact that gives the $\alpha=0.15$ anchor (with a checksum), or retract the exact $c$ coefficient and report $\sigma(f_{\rm NL})$ directly from the two‑anchor interpolation with the numbers as given.

---

## PAPER-DEE-m1 — minor — “37.3 million” is 0.3% above the actual sum of processed sources

**Location:** Abstract and Introduction, total data volume claim.

**Issue:** The table sum of processed sources/patch counts is 37 272 042 (22 504 897 + 2 304 830 + 11 418 594 + 930 203 + 20 000 + 50 000 + 43 518). This rounds to 37.3 million only if one rounds to two significant digits; the precise value is 37.27 million. The paper’s “37.3 million” without any rounding qualifier suggests a precision that the underlying data do not support.

**Fix:** Write “37.27 million” or “∼37.3 million” to indicate rounding.
