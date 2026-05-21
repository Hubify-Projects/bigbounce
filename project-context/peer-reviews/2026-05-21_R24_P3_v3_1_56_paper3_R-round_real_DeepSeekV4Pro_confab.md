# paper3 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R24_P3_v3_1_56
**Wall time**: 243.6s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=64209, completion=10375, reasoning=9739, total=74584

---

## PAPER-DEE-B1: MAJOR — Genuine novelty fraction (17.8 %) lacks any on-disk cross‑match artifact  
**Line:** abstract (“genuine novelty fraction of ∼17.8 %”), Conclusions item 2, and §4.1.  
**Issue:** The paper presents 17.8 % (178/1000) as the <q>primary</q> discovery rate from cross‑matching the top‑1000 DESI anomalies against 20 curated all‑sky catalogs. No parquet, CSV, JSON, or script- output file is provided that records the match result for each object or the final 178‑object list. A reader cannot verify the figure without re‑performing a cross‑match that requires access to those 20 catalogs (several of which are not trivially available as a single bulk download). This violates the provenance requirement for a headline claim.  
**Fix:** Deposit the full cross‑match table (e.g., `desi_top1000_xmatch_20cats.parquet`) as part of the data release, and cite it in the text.

## PAPER-DEE-B2: minor — SIMBAD‑unmatched fraction (58.8 %) not stored in released catalog  
**Line:** Conclusions (“SIMBAD‑unmatched fraction: 58.8 %”), §4.1.  
**Issue:** The aggregate 58.8 % missing‑from‑SIMBAD fraction is a load‑bearing metric in the conclusions. The released anomaly catalog (`pathc_unique_objects_no_act.parquet`) does not contain a SIMBAD‑match flag or counterpart identifier, so a user must re‑run the SIMBAD cone search to reproduce the number. The provenance chain ends at the coordinates, not at the fraction itself.  
**Fix:** Add a `simbad_match` boolean column (and matched identifier column) to the unified catalog, or provide a companion file with the per‑object SIMBAD status.

## PAPER-DEE-B3: minor — Validation‑loss numbers for SDSS/LAMOST native retrains lack artifact citations  
**Line:** Conclusions (“gate‑PASS validation MSE on SDSS (0.0311) and LAMOST (0.0329)”), §3.3, §3.4, and §7.  
**Issue:** The exact validation losses 0.0311 and 0.0329 are the gate criteria that admit those detectors into the final catalog. While the Planck native CMB retrain cites a `training_losses.json` artifact, no analogous frozen file is referenced for the SDSS or LAMOST native runs. The scripts can reproduce the values, but the precise numbers claimed are not backed by a persisting, named artifact.  
**Fix:** Include `training_losses.json` (or equivalent) for the SDSS and LAMOST native retrains in the repository and cite them where the loss values are asserted.

*No blocker‑grade findings.*
