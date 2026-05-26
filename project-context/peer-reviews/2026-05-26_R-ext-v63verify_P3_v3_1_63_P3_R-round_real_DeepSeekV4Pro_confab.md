# P3 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v63verify_P3_v3_1_63
**Wall time**: 189.8s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=66463, completion=10297, reasoning=9314, total=76760

---

## Findings

### PAPER-DEE-B1 — BLOCKER
**Section:** Abstract, LAMOST native-retrain claim  
**Issue:** The abstract states that the native LAMOST autoencoder "retains a ~98% blue‑excess instrumental contamination signature in the released anomaly scores."  The paper body (Sec. 3.3, Path‑C native‑retrain paragraph) explicitly reports that the native retrain reduced the cross‑transfer anomaly rate by 21.5× and "direct[ly] numerical[ly] confirm[s] that the 98% blue‑excess signature was a cross‑transfer catalog‑calibration artifact rather than an astrophysical signal."  The abstract therefore makes a quantitative claim that is directly contradicted by the paper’s own results and is not supported by any on‑disk artifact.  
**Fix:** Remove the unsupported “~98%” figure for the native LAMOST scores or replace it with the actual post‑native contamination fraction (which the paper itself defers to a future validation step).

### PAPER-DEE-M1 — MAJOR
**Section:** Abstract and Sec. 4.1  
**Issue:** The “genuine novelty fraction of ~17.8% (178/1000)” for the DESI top‑1000 anomalies, obtained by cross‑matching against “NED, VizieR, and 20 all‑sky catalogs,” is a load‑bearing headline result.  No companion artifact (JSON/parquet, CDS X‑Match output table, or a script with a deterministic seed) is cited anywhere in the paper.  The absence of a traceable on‑disk source prevents reproduction of this number.  
**Fix:** Provide the cross‑match table (e.g., `top1000_cds_xmatch.parquet`) and reference it in the data‑availability statement, or include a deterministic script that reproduces the CDS X‑Match query and yields the same 178/1000 counts.

### PAPER-DEE-m1 — minor
**Section:** Sec. 5, local‑linear approximation  
**Issue:** The text gives α = 0.19 and the slope −3.66, then quotes the linear‑approximation σ(f_NL) = 8.27.  Arithmetic with the displayed values (8.98 − 3.66 × 0.19 = 8.2846 → 8.28) yields 8.28, not 8.27.  The 0.01 discrepancy may be a rounding artefact, but it cannot be reproduced exactly from the stated numbers.  
**Fix:** Either adjust the displayed value to 8.28 or clarify that the slope actually used is −3.666... and recalculate the product accordingly.

### PAPER-DEE-m2 — minor
**Section:** Sec. 5, Fisher‑positivity coefficient  
**Issue:** The Fisher‑positivity‑respecting asymptotic form uses F₀ = 1/8.98² and c = 0.0747, derived from the two anchor Fisher runs σ(f_NL)=8.98 (α=0) and σ(f_NL)=8.43 (α=0.15).  Neither of these anchor Fisher outputs is directly backed by a named on‑disk file or script reference.  The paper defers a full Fisher‑grid re‑estimate (caveat (i)), so the current c is a provisional Taylor expansion; still, the provenance of the two numbers that fix it should be traceable.  
**Fix:** Add a companion artifact (e.g., `fisher_anchor_alpha0_fNL_8.98.json` and `fisher_anchor_alpha0.15_fNL_8.43.json`) or point to the specific Fisher‑pipeline script and its outputs in the reproducibility suite.

### PAPER-DEE-m3 — minor
**Section:** Abstract vs. Conclusions (Sec. 7)  
**Issue:** The abstract quotes the central Fisher forecast as σ(f_NL) = 8.14 (positivity‑respecting form), while Conclusion 5 gives σ(f_NL) = 8.27 ± 2.37 (local‑linear approximation).  Both are presented as headline numbers without a clear statement of which should be used.  The conclusion does not mention the 8.14 value, creating an unnecessary narrative inconsistency.  
**Fix:** Settle on a single canonical central forecast (preferably the positivity‑respecting value) and present it uniformly in abstract and conclusions, relegating the local‑linear number to a clearly labeled historical/approximate note.
