# P3_v3143 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_1030pt_P3_v3143_R5_R-round_real
**Wall time**: 313.3s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=56448, completion=6141, reasoning=4875, total=62589

---

# Adversarial Peer Review — Provenance Audit of Load-Bearing Scalars

## PAPER-DEE-B1 (BLOCKER) — Headline unique count 378,280 is arithmetically inconsistent and unverified

**Location:** Abstract, Sec. 6.4 item (a), Conclusions, Table 1 Path-C row.

**Issue:** The paper reports 637 multi-survey coincidences (all pairwise) and a survey-level sum of 388,493. Under the all-pairwise assumption, the unique count must be \(388,493 - 637 = 387,856\), not 378,280. The shortfall of 9,576 is acknowledged as an unresolved deferral (“pending recompute”), yet the abstract and conclusions still quote 378,280 as the canonical catalog size. No JSON/script on disk produces 378,280; the number is contradicted by the paper’s own coincidence count.

**Fix:** Resolve the union-find cluster manifest (recompute the true coincidence count, account for intra-survey duplicates) and update the headline to the verified value. Until then, the paper must replace 378,280 with the arithmetic upper bound 387,856 or explicitly retract the number.

---

## PAPER-DEE-M1 (MAJOR) — SIMBAD-unmatched aggregate 58.8% is derived from the superseded cross-transfer baseline

**Location:** Abstract, Sec. 4.1, Fig. 4, Conclusions.

**Issue:** The 58.8% SIMBAD-unmatched fraction and the per-survey rates (e.g., LAMOST ~50%, SDSS 90%) are computed from the cross-transfer anomaly sets (Table 1 cross-transfer row). The Path-C native retrains drastically changed the anomaly populations (LAMOST 44,075 → 113,342; SDSS 77,905 → 12 at S>5). The novelty fractions have not been recomputed on the released Path-C catalogs, so the headline “58.8%” does not describe the final data product.

**Fix:** Re-run SIMBAD cross-matching on the Path-C native anomaly sets and update all aggregate and per-survey unmatched fractions. If not feasible before publication, clearly label the 58.8% as a cross-transfer diagnostic only and remove it from the abstract/conclusions.

---

## PAPER-DEE-M2 (MAJOR) — SDSS clustering and DESI×SDSS cross-matches rely on the inflated cross-transfer catalog

**Location:** Sec. 3.3 (SDSS UMAP clustering), Sec. 4.3 (three highlighted cross-matches), Conclusions.

**Issue:** The SDSS anomaly population used for the UMAP/HDBSCAN clustering (77,905 objects) and the DESI×SDSS positional cross-matches is the cross-transfer scan, which the paper itself shows is inflated ~6500× relative to the native SDSS (12 sources at S>5). The three highlighted cross-match objects (known QSO, TIC 374313355, BAL QSO candidate) were identified using the cross-transfer SDSS catalog; their status in the native SDSS catalog is unknown. Presenting these as results of the multi-survey campaign misrepresents the final catalog.

**Fix:** Either re-perform the clustering and cross-matching on the Path-C native SDSS anomaly set (and report the outcome, even if null) or explicitly demote these findings to “cross-transfer baseline diagnostics” and remove them from the conclusions.

---

## PAPER-DEE-M3 (MAJOR) — Genuine novelty fraction 17.8% lacks a traceable artifact

**Location:** Abstract, Sec. 4.1 (“Archival cross-match and genuine novelty fraction”), Sec. 6.3, Conclusions.

**Issue:** The 17.8% (178/1,000) novelty fraction for DESI top-1,000 anomalies is a load-bearing discovery metric, but no specific file (JSON/parquet) containing the cross-match results against the 20 all-sky catalogs is cited. The paper references a “companion data release” without a path or checksum. The number cannot be reproduced from the information provided.

**Fix:** Deposit the cross-match table (e.g., `desi_top1000_xmatch_20catalogs.parquet`) in the public repository and cite it explicitly in the text. The artifact must include the matched catalog names and per-object match status.

---

## PAPER-DEE-m1 (minor) — Inconsistent baseline in abstract: 319,443 includes ACT, 388,493 excludes ACT

**Location:** Abstract (“The initial cross-transfer baseline identified 319,443 … supersedes this with 388,493 … ACT~DR6 excluded”).

**Issue:** The 319,443 total includes the quarantined ACT 200 patches (as stated in Table 1 footnote), but the 388,493 sum explicitly excludes ACT. The comparison is not like-with-like and overstates the increase from the rebuild.

**Fix:** Provide the ACT-excluded cross-transfer sum (319,243) for a consistent before/after comparison, or clearly note that the 319,443 includes ACT and the 388,493 does not.

---

## PAPER-DEE-m2 (minor) — SDSS contribution to Path-C sum mixes threshold definitions

**Location:** Table 1 Path-C row footnote, Sec. 3.3 (“Path-C native-retrain in flight”), Conclusions.

**Issue:** The SDSS native count used in the 388,493 survey-level sum is 77,905 (top-1% continuity slice at S≥0.1060), not the field-defining S>5 threshold (12 sources). This inflates the sum and the subsequent deduplicated headline, mixing absolute and percentile thresholds across surveys without a uniform policy.

**Fix:** Either adopt a homogeneous threshold for the headline sum (e.g., S>5 for all spectroscopic surveys) or explicitly flag the sum as a heterogeneous mix and provide a threshold-homogeneous version for users who require consistent selection.
