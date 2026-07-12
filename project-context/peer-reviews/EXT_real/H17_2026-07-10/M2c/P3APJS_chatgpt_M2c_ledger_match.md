# ledger_match DRAFT — P3 — P3APJS_chatgpt_M2c.md

> DRAFT for the Opus truth-auditor, NOT a replacement. Conservative threshold (prefers UNMATCHED over a false match). Every UNMATCHED finding — and every low-score MATCHED — still needs a human/Opus source-cited disposition per §3.
>
> ledger: `project-context/peer-reviews/DISPOSITIONS/P3.md` (20 D-ids)  |  findings parsed: 19  |  threshold: 0.3

| # | sev | finding (first 120 chars) | best match | score | status |
|---|-----|---------------------------|-----------|-------|--------|
| 1 | MAJOR | Abstract; §3 three-tier catalog definition; Table 2; §4.3 — The claimed “validated catalog-grade” count of 268,519 is no | DP3-09 | 0.69 | MATCHED |
| 2 | MAJOR | §3.1 and Table 3 — The DESI science-target accounting is internally inconsistent. A 0.75% anomaly rate among approximate | DP3-07 | 0.64 | MATCHED |
| 3 | MAJOR | §2.2 and §6.4(i) — The DESI cross-validation is incorrectly described as a fully out-of-sample re-score. Each fold model | DP3-01 | 0.27 | **UNMATCHED** |
| 4 | MAJOR | §2.2, §2.4, and §6.4(i) — No production-level held-out validation of the released DESI membership is available. The full | DP3-05 | 0.22 | **UNMATCHED** |
| 5 | MAJOR | §3.1 and §6.1 — The manuscript has not established that the dominant DESI tier consists of astrophysical sources rather  | DP3-11 | 0.58 | MATCHED |
| 6 | MAJOR | §2.4 and §6.4(ii) — The injection-recovery program measures sensitivity to selected artificial perturbations, not catalo | DP3-07 | 0.18 | **UNMATCHED** |
| 7 | MAJOR | §2.2 and §6.3 — The spectroscopic selection function is not characterized sufficiently for a catalog paper. DESI is trai | DP3-07 | 0.24 | **UNMATCHED** |
| 8 | MAJOR | §3.3, Figures 3–4, and Table 4 — The SDSS cross-transfer population and released native-retrained population are conflat | DP3-14 | 0.89 | MATCHED |
| 9 | MAJOR | §3.3 — The SDSS score–redshift result is overinterpreted. A Spearman coefficient of 0.036 is negligible in effect size,  | DP3-12 | 0.17 | **UNMATCHED** |
| 10 | MAJOR | §3.6 and Table 7 — The Planck train/validation split is severely spatially leaked. The analysis draws 200,000 overlappin | DP3-06 | 0.51 | MATCHED |
| 11 | MAJOR | §3.6 — The Planck injection test is not a sufficient physical validation. A 5σ Gaussian bump is added after per-patch st | DP3-06 | 0.51 | MATCHED |
| 12 | MAJOR | §4.1 — The 17.8% “genuine novelty fraction” is not established. Absence of a positional match in a selected list of cata | DP3-07 | 0.18 | **UNMATCHED** |
| 13 | MAJOR | §4.1 and Figure 6 — The reported 58.8% aggregate SIMBAD-unmatched fraction has an impossible denominator. It is describe | DP3-08 | 0.20 | **UNMATCHED** |
| 14 | MAJOR | Title, Abstract, Table 1, and Table 2 — The “37.3 million” scan volume is misleading. The retained-native body rows sum  | DP3-04 | 0.90 | MATCHED |
| 15 | MAJOR | Data Availability statement — The release description directly contradicts the catalog definition. It says the LAMOST ti | DP3-20 | 0.33 | MATCHED |
| 16 | MAJOR | §5, Figure 9, and Appendix C — The f NL ​ forecast is not internally consistent. The empirical bias is measured on 5,384 | DP3-10 | 0.17 | **UNMATCHED** |
| 17 | MAJOR | §5.1, Appendix E, and Table 10 — The claimed 7.14×10 3 “decisive” Bayes factor is driven by a KDE estimate of the poster | DP3-18 | 0.34 | MATCHED |
| 18 | MAJOR | §3.2 — The twelve z≃6 quasar candidates are not adequately validated. Their redshifts are low-continuum-S/N Redrock temp | DP3-11 | 0.21 | **UNMATCHED** |
| 19 | MINOR | Figures 1, 2, 6, and 8 — Several figures are unsuitable as evidence for the released product: Figure 1 force-includes th | DP3-07 | 0.40 | MATCHED |

**Match rate: 10/19 = 53% MATCHED, 9 UNMATCHED.**

Exit 2 — 9 finding(s) need a full §3 truth-audit (genuinely-new candidates or too-weak fingerprint overlap).
