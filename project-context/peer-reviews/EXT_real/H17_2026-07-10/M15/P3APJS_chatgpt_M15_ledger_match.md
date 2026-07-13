# ledger_match DRAFT — P3 — P3APJS_chatgpt_M15.md

> DRAFT for the Opus truth-auditor, NOT a replacement. Conservative threshold (prefers UNMATCHED over a false match). Every UNMATCHED finding — and every low-score MATCHED — still needs a human/Opus source-cited disposition per §3.
>
> ledger: `project-context/peer-reviews/DISPOSITIONS/P3.md` (20 D-ids)  |  findings parsed: 16  |  threshold: 0.3

| # | sev | finding (first 120 chars) | best match | score | status |
|---|-----|---------------------------|-----------|-------|--------|
| 1 | MAJOR | Title, Abstract, §3.1, and §7 — the dominant catalog entries are not established astrophysical sources. DESI contributes | DP3-07 | 0.75 | MATCHED |
| 2 | MAJOR | §2.2, §3.1, and Table 6(b) — the DESI preprocessing and training design are likely selecting domain shift and reduction  | DP3-12 | 0.47 | MATCHED |
| 3 | MAJOR | §2.2 and §6.4(i) — the five-fold Jaccard result is incorrectly characterized as fully out-of-sample validation. Each fol | DP3-06 | 0.36 | MATCHED |
| 4 | MAJOR | §3.1, Table 3, and §6.5 — the DESI target accounting and literature comparison are not reconciled. The quoted per-class  | DP3-07 | 0.46 | MATCHED |
| 5 | MAJOR | §3.3, Table 2, Figure 4, and Table 4 — the SDSS catalog component is defined by an arbitrary count and is characterized  | DP3-14 | 0.72 | MATCHED |
| 6 | MAJOR | §2.4 and §6.4(ii) — injection recovery is being used to claim more than it measures. Recovery of one or two synthetic pe | DP3-07 | 0.34 | MATCHED |
| 7 | MAJOR | §3.8 — NEOWISE does not meet the stated catalog-grade standard. Its only passing test plants positions outside the mask  | DP3-07 | 0.18 | **UNMATCHED** |
| 8 | MAJOR | §3.6 and Table 7 — the Planck validation is methodologically invalid. The native top-200 is a fixed count corresponding  | DP3-06 | 0.83 | MATCHED |
| 9 | MAJOR | §4.1 — the 17.8% “genuinely novel” fraction is not established. The analysis does not first restrict the top-1,000 DESI  | DP3-07 | 0.18 | **UNMATCHED** |
| 10 | MAJOR | §4.3 — the 5″ friends-of-friends operation does not establish unique physical objects. It merges heterogeneous optical o | DP3-20 | 0.40 | MATCHED |
| 11 | MAJOR | §2.2, §3.6, and Data Availability — the central data product is neither independently regenerable nor consistently descr | DP3-15 | 0.44 | MATCHED |
| 12 | MAJOR | Title, Abstract, Table 1, and Table 2 — the 37.3-million scale claim is misleading. The retained-native body sum is 36.7 | DP3-04 | 0.78 | MATCHED |
| 13 | MAJOR | §5, Figure 9, and Appendix C — the f NL ​ application is not a valid downstream inference. An angular clustering ratio f | DP3-10 | 0.17 | **UNMATCHED** |
| 14 | MAJOR | §5.1 and Appendix E — the NANOGrav analysis is unrelated to the catalog and is insufficiently specified. No catalog obse | DP3-16 | 0.12 | **UNMATCHED** |
| 15 | MINOR | §4.2 — the spatial statistics are not interpretable as anomaly-rate tests. A χ 2 test against uniform counts in occupied | DP3-12 | 0.08 | **UNMATCHED** |
| 16 | MINOR | §4.1/Figure 6, Figure 8, and Figure 10 — plotted quantities and denominators are internally inconsistent. The 235/400 ag | DP3-07 | 0.28 | **UNMATCHED** |

**Match rate: 10/16 = 62% MATCHED, 6 UNMATCHED.**

Exit 2 — 6 finding(s) need a full §3 truth-audit (genuinely-new candidates or too-weak fingerprint overlap).
