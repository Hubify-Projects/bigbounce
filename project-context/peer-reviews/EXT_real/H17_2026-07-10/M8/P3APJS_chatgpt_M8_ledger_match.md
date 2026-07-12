# ledger_match DRAFT — P3 — P3APJS_chatgpt_M8.md

> DRAFT for the Opus truth-auditor, NOT a replacement. Conservative threshold (prefers UNMATCHED over a false match). Every UNMATCHED finding — and every low-score MATCHED — still needs a human/Opus source-cited disposition per §3.
>
> ledger: `project-context/peer-reviews/DISPOSITIONS/P3.md` (20 D-ids)  |  findings parsed: 17  |  threshold: 0.3

| # | sev | finding (first 120 chars) | best match | score | status |
|---|-----|---------------------------|-----------|-------|--------|
| 1 | MAJOR | Abstract, §3, and §7 — “validated catalog-grade subset of 268,519.” The headline set has no common selection function: i | DP3-06 | 0.69 | MATCHED |
| 2 | MAJOR | §3.3 and Table 2 — SDSS headline count of 77,905. The manuscript explicitly states that this number was chosen solely to | DP3-14 | 0.55 | MATCHED |
| 3 | MAJOR | §3.1 and Table 3 — DESI catalog composition. Approximately 98.7% of DESI anomaly clusters are not primary science target | DP3-07 | 0.57 | MATCHED |
| 4 | MAJOR | §2.2, §6.4(i), and Data Availability — DESI reproducibility. The release mixes real TARGETIDs with internal hashes for 8 | DP3-15 | 0.31 | MATCHED |
| 5 | MAJOR | §2.2 and §6.4(i) — DESI cross-validation claim. Each fold model scores the full 47,000-object pool, so approximately 80% | DP3-01 | 0.27 | **UNMATCHED** |
| 6 | MAJOR | §2.4 and §6.4 — injection-recovery interpretation. Injection recovery measures sensitivity to the chosen synthetic pertu | DP3-07 | 0.40 | MATCHED |
| 7 | MAJOR | §3.8 — NEOWISE validation. The only passing test plants sources outside the adopted ecliptic mask and “recovers” them by | DP3-12 | 0.08 | **UNMATCHED** |
| 8 | MAJOR | §3.6 — Planck validation and selection. The released top-200 patches are selected from a bank that includes training pat | DP3-06 | 0.58 | MATCHED |
| 9 | MAJOR | §3, §4.3, and the headline count — point sources and CMB regions. Ten-degree Planck map patches are not astronomical obj | DP3-06 | 0.43 | MATCHED |
| 10 | MAJOR | §3.4, §7, and Data Availability — LAMOST and release-accounting contradiction. LAMOST fails injection recovery and is id | DP3-20 | 0.33 | MATCHED |
| 11 | MAJOR | §2.2, Table 2, Figures 3–4, Table 4, and §6.2 — score and model provenance. The text alternately says that SDSS and LAMO | DP3-14 | 0.28 | **UNMATCHED** |
| 12 | MAJOR | §4.1 — “17.8% genuine novelty fraction” and “discovery rate.” Absence from 18 selected catalogs is not evidence that an  | DP3-07 | 0.18 | **UNMATCHED** |
| 13 | MAJOR | §4.3 — cross-survey validation and random-coincidence estimate. The released DESI–SDSS comparison gives four positional  | DP3-14 | 0.11 | **UNMATCHED** |
| 14 | MAJOR | §3.1, Table 3, and §6.5 — “like-for-like” comparison with Liang et al. Comparing 2,468 anomalies with a prior catalog of | DP3-07 | 0.40 | MATCHED |
| 15 | MAJOR | §5 and Appendix C — multi-tracer f NL ​ application. The forecast is not reproducible from the information provided: the | DP3-10 | 0.17 | **UNMATCHED** |
| 16 | MAJOR | §5.1 and Appendix E — NANOGrav analysis. This analysis is not enabled by, or logically connected to, the anomaly catalog | DP3-13 | 0.13 | **UNMATCHED** |
| 17 | MINOR | §4.2 — spatial statistics. A Poisson uniformity test over only occupied HEALPix pixels from several highly nonuniform su | DP3-07 | 0.28 | **UNMATCHED** |

**Match rate: 9/17 = 53% MATCHED, 8 UNMATCHED.**

Exit 2 — 8 finding(s) need a full §3 truth-audit (genuinely-new candidates or too-weak fingerprint overlap).
