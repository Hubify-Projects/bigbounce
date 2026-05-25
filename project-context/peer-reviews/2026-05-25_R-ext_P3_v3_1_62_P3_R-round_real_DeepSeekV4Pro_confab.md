# P3 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-25_R-ext_P3_v3_1_62
**Wall time**: 197.0s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=65462, completion=6281, reasoning=5687, total=71743

---

## PAPER-DEE-B1 [BLOCKER] — Genuine novelty fraction 17.8 % has no traceable provenance

**Location:** Abstract; Section 4.1 (“Archival cross-match and genuine novelty fraction”); Conclusions item 2.

**Issue:** The headline result *“genuine novelty fraction of ∼17.8 %”* (178/1,000 DESI anomalies unmatched against 20 all-sky catalogs) is a load‑bearing scalar used throughout the paper to characterize the catalog’s discovery rate. No companion artifact (JSON, parquet, script log, or explicit file path) is cited that contains the per‑object match status or the 822/1,000 number. The text states that the full characterization “requires the deeper NED+VizieR sweep detailed in the companion data release” but does not identify a definitive on‑disk record of this particular cross‑match. Without such an artifact, the 17.8 % figure is unverifiable and cannot be reproduced from the paper alone.

**Fix:** Release a machine‑readable file (e.g., `top1000_desi_novelty_crossmatch.parquet` or `.json`) listing the 1,000 anomaly IDs, the match outcome against each of the 20 catalogs, and the derived unmatched count (178). Update the abstract and §4.1 to cite that file explicitly.

---

## PAPER-DEE-M1 [MAJOR] — “37.3 million sources” total is inconsistent with the Path-C per‑survey counts

**Location:** Abstract, first sentence.

**Issue:** The abstract states that the campaign applied the framework to *“37.3 million sources and CMB map patches across seven retained astronomical archives”*. The per‑survey totals in Table 1 (Path‑C unique row) sum to **37,272,042** — which is 37.27 million, not 37.3 million. The 37.3 million figure matches the *cross‑transfer baseline total* (37,292,042) that **includes** the quarantined ACT DR6 patches, not the seven‑retained‑survey dataset. The discrepancy is small in percentage but misleads by attributing a scale that includes ACT to the final, ACT‑excluded catalog. The arithmetic on the displayed numbers cannot reproduce “37.3 million”.

**Fix:** Replace “37.3 million” with the exact Path‑C total (37,272,042) and round to 37.27 million, or clarify that the quoted 37.3 million is the original cross‑transfer scan (including ACT) and distinguish it from the Path‑C dataset used for all later results.
