# P3 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-maint_P3_v3_1_63
**Wall time**: 426.6s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=66367, completion=13116, reasoning=11905, total=79483

---

## PAPER-DEE-B1 — BLOCKER
**Section:** Abstract, Conclusions, §4.1 (SIMBAD cross-match).  
**Issue:** The aggregate SIMBAD‑unmatched fraction of **58.8%** is a headline number in both the abstract and conclusions, yet it cannot be reproduced from the per‑survey anomaly counts and unmatched percentages displayed in Table I. Using the table values (DESI 99% of 195,829; SDSS 90% of 77,905; LAMOST 50% of 44,075; eROSITA 68% of 298; Gaia 27% of 500; NEOWISE 45% of 436) gives an unmatched total of ≈286,600 out of ≈319,000 coordinate‑bearing anomalies, i.e. **≈89.8%**, not 58.8%. No raw unmatched counts, weighting formula, or companion artifact is provided to resolve the discrepancy.  
**Fix:** Either (a) correct the aggregate to match the displayed per‑survey data and explain the weighting, or (b) supply the exact unmatched counts and the arithmetic that yields 58.8%, and deposit the cross‑match output as a named parquet/JSON artifact.

## PAPER-DEE-B2 — MAJOR
**Section:** Abstract, §5, Conclusions.  
**Issue:** The Fisher‑forecast baseline numbers **σ(f_NL)=8.98** (single‑tracer DESI QSO) and **σ(f_NL)=8.43** (α=0.15) are used to anchor the Fisher‑positivity form (F₀, c), the 7.9% improvement, and the central forecast σ=8.14. None of these scalars is traceable to a specific on‑disk script or artifact. The paper cites Heinrich et al. methodology but does not provide a reproducibility artifact (e.g., a Fisher‑matrix JSON or a driver script) that produces 8.98 and 8.43.  
**Fix:** Deposit the Fisher pipeline code and a JSON output (e.g., `fisher_baseline.json`) that records the exact σ values for α=0 and α=0.15, and reference that artifact in the abstract and §5.

## PAPER-DEE-B3 — minor
**Section:** Abstract, §4.1, Conclusions.  
**Issue:** The genuine novelty fraction of **~17.8%** (178/1,000) for the DESI top‑1,000 anomalies is a key discovery metric, but the paper does not name a specific companion artifact (e.g., a cross‑match table or summary JSON) that contains the 822/1,000 match count. The text only refers to a “companion data release” without a filename.  
**Fix:** Add a sentence pointing to the exact artifact (e.g., `desi_top1000_xmatch_20catalogs.parquet` or a summary JSON) that records the per‑catalog match status and the 178‑object novelty list.

## PAPER-DEE-B4 — minor
**Section:** Abstract, §5.  
**Issue:** The statement that the matter‑bounce f_NL=−35/8 prediction is “preliminarily testable at **3–5σ significance** with SPHEREx” is a forward‑looking forecast with no traceable Fisher‑matrix artifact or script. No on‑disk product is cited that produces this significance range.  
**Fix:** Either remove the specific significance claim from the abstract (retaining only the qualitative statement) or deposit the SPHEREx Fisher forecast artifact and reference it explicitly.

## PAPER-DEE-B5 — nit
**Section:** Conclusions (item 5, legacy fixed‑α headline).  
**Issue:** The **16.4% improvement** for DESI+SDSS combined tracers is mentioned as a legacy reference but is not derived from any displayed numbers or artifact in the paper. Its provenance is untraceable.  
**Fix:** Either drop the 16.4% figure or provide the Fisher‑matrix artifact that produced it, with a clear note that it is superseded.

## PAPER-DEE-B6 — nit
**Section:** Abstract, §3.3, Conclusions.  
**Issue:** The **98% blue‑excess** fraction for LAMOST anomalies is a specific percentage used to illustrate training‑bias contamination, but no companion artifact (e.g., a JSON with per‑wavelength residual classifications) is cited that would allow independent verification of the 98% figure.  
**Fix:** Deposit the classification output (e.g., `lamost_blue_excess_fraction.json`) and reference it in the text.
