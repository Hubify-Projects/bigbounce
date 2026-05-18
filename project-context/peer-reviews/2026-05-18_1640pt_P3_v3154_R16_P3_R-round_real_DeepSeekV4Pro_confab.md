# P3 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1640pt_P3_v3154_R16
**Wall time**: 115.2s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=62826, completion=7205, reasoning=6051, total=70031

---

## PAPER-DEE-B1 — BLOCKER
**Section:** §7 (Conclusions), item 2; also §4.1 and Fig. 4.  
**Issue:** The aggregate SIMBAD‑unmatched fraction of **58.8%** is a headline conclusion number, but it cannot be reproduced from the per‑survey unmatched percentages and anomaly counts displayed in the paper. Weighting the given rates (DESI ~99%, SDSS 90%, LAMOST ~50%, eROSITA 68%, NEOWISE 45%, Gaia 27%) by the corresponding anomaly counts yields ~90%, not 58.8%. No companion artifact is cited that would resolve this arithmetic contradiction.  
**Fix:** Either correct the aggregate fraction to match the per‑survey numbers (and provide the exact matched/unmatched counts per survey), or supply the specific artifact (e.g., a SIMBAD cross‑match summary JSON) that produces 58.8% and explain the weighting method.

## PAPER-DEE-B2 — BLOCKER
**Section:** Abstract; §7 (Conclusions), item 1; §6.4 deferral (a).  
**Issue:** The primary headline number **378,280 unique anomalies** is explicitly flagged as pending recompute because of an unresolved arithmetic discrepancy. The paper states that under the all‑pairwise assumption the correct figure would be 387,856, and the union‑find cluster manifest recompute has not been completed. A headline count that is acknowledged as potentially wrong by ~2.5% and lacks a verified on‑disk artifact is not acceptable for a catalog paper.  
**Fix:** Complete the recompute and update the headline to the verified value, or clearly mark the number as provisional and provide the verified upper/lower bounds with a pointer to the exact artifact that will supersede it.

## PAPER-DEE-M1 — MAJOR
**Section:** Abstract; §4.1 (“Archival cross‑match and genuine novelty fraction”); §7 (Conclusions), item 2.  
**Issue:** The **genuine novelty fraction of ~17.8%** (178/1,000) for the DESI top‑1,000 anomalies is a key discovery metric, but no specific companion artifact path is given for the cross‑match against 20 all‑sky catalogs. The paper only refers to a “companion data release” without a filename. The number is therefore unverifiable from the materials described.  
**Fix:** Provide the exact artifact path (e.g., `crossmatch_desi_top1000_novelty.json` or a parquet table) and confirm that it contains the 822/178 breakdown.

## PAPER-DEE-M2 — MAJOR
**Section:** §4.1; Fig. 4 caption; §7 (Conclusions), item 2.  
**Issue:** The per‑survey SIMBAD‑unmatched fractions listed in the text (SDSS 90%, eROSITA 68%, LAMOST ~50%, NEOWISE 45%, Gaia 27%, DESI ~99%) are used to compute the aggregate 58.8%, but the arithmetic is inconsistent (see B1). Moreover, no artifact is cited for any of these per‑survey fractions; they appear only as narrative percentages. The SIMBAD cross‑match status is presumably in the released catalog, but the specific file and column are not identified.  
**Fix:** Add a reference to the exact catalog column that contains the SIMBAD match flag, and provide a summary artifact (e.g., `simbad_unmatched_summary.json`) that reproduces all per‑survey unmatched counts and the aggregate.

## PAPER-DEE-m1 — minor
**Section:** Abstract; §2.2; §6.4 caveat (i).  
**Issue:** The 5‑fold cross‑validation Jaccard stability numbers (J̄ = 0.862, 546 unique, 399 in all five folds) are traceable to `pathc_desi_kfold/results/kfold_stability_summary.json`, but the paper also quotes a production‑vs‑control Jaccard of 0.7320 from a separate 103k‑spectrum holdout. The artifact for that holdout (`jaccard_100k_results.json`) is mentioned, but the 0.7320 value is not explicitly stated to be inside that file; the text only says “Companion artifact: `pipelines/p3_anomaly_engine/jaccard_100k_results.json`.” The number is likely there, but the link is slightly loose.  
**Fix:** State explicitly that the 0.7320 (and the control‑vs‑control 0.8738) are recorded in `jaccard_100k_results.json`.

## PAPER-DEE-n1 — nit
**Section:** Abstract; §1; §7.  
**Issue:** The abstract and conclusions repeatedly use the rounded figure **37.3 million sources**, but the exact sum of the survey totals in Table I is 37,272,042 (or 37,292,042 with ACT). The difference is ~0.1%, which is harmless, but the paper never states the precise sum. For a catalog paper that otherwise reports counts to the unit, this approximation is a minor inconsistency.  
**Fix:** Either quote the exact total (e.g., “37,272,042 point sources and map patches”) or explicitly note that “37.3 million” is rounded from the exact sum given in Table I.
