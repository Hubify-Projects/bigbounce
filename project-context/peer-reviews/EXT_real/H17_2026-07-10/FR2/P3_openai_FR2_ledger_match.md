# ledger_match DRAFT — P3 — API_P3_openai.md

> DRAFT for the Opus truth-auditor, NOT a replacement. Conservative threshold (prefers UNMATCHED over a false match). Every UNMATCHED finding — and every low-score MATCHED — still needs a human/Opus source-cited disposition per §3.
>
> ledger: `project-context/peer-reviews/DISPOSITIONS/P3.md` (18 D-ids)  |  findings parsed: 18  |  threshold: 0.3

| # | sev | finding (first 120 chars) | best match | score | status |
|---|-----|---------------------------|-----------|-------|--------|
| 1 | MAJOR | Abstract / Secs. III and VII — The headline “validated catalog-grade subset of 268,519” is not supported by uniform vali | DP3-07 | 0.40 | MATCHED |
| 2 | MAJOR | Secs. II B, III, Table II — The anomaly thresholds are heterogeneous and partly arbitrary: DESI uses S>5, SDSS headline  | DP3-09 | 0.51 | MATCHED |
| 3 | MAJOR | Secs. III A and VII — The DESI headline is dominated by non-primary science spectra, sky/filler fibers, or non-science-t | DP3-07 | 0.75 | MATCHED |
| 4 | MAJOR | Secs. II D, III D, VI A — LAMOST fails the injection-recovery gate and is diagnosed as a 98% blue-excess training-bias a | DP3-02 | 0.08 | **UNMATCHED** |
| 5 | MAJOR | Sec. III E — The eROSITA tier has an irreproducible production score axis, fails detector-sensitivity injection recovery | DP3-08 | 0.30 | MATCHED |
| 6 | MAJOR | Sec. III G — The discovery that the Gaia tier was synthetic-placeholder output indicates severe provenance-control failu | DP3-08 | 0.20 | **UNMATCHED** |
| 7 | MAJOR | Secs. II B, II D, VI D — The validation strategy is insufficient for a catalog-grade claim. Several checks are explicitl | DP3-07 | 0.18 | **UNMATCHED** |
| 8 | MAJOR | Secs. II B and Appendix A — Preprocessing is not consistently reproducible or statistically clean: tabular scalers were  | DP3-01 | 0.13 | **UNMATCHED** |
| 9 | MAJOR | Secs. IV A–IV C — The cross-match and novelty analysis is not adequate for the claimed discovery rate. The 17.8% “genuin | DP3-10 | 0.08 | **UNMATCHED** |
| 10 | MAJOR | Sec. IV B — The spatial analysis is footprint-dominated and not corrected for survey selection functions, completeness,  | DP3-07 | 0.12 | **UNMATCHED** |
| 11 | MAJOR | Sec. V — The fNL application does not deliver a constraint or improvement: the measured bias α=0.19±0.65 is consistent w | DP3-02 | 0.08 | **UNMATCHED** |
| 12 | MAJOR | Sec. V A / Appendix E — The NANOGrav analysis is only a simplified refit of the public free-spectrum KDE likelihood, not | DP3-10 | 0.25 | **UNMATCHED** |
| 13 | MAJOR | Scope / suitability for Physical Review D — The primary deliverable is an astronomical anomaly-candidate catalog with we | DP3-10 | 0.25 | **UNMATCHED** |
| 14 | MAJOR | Reproducibility / data availability — The paper relies heavily on repository artifacts, scripts, JSON files, and future  | DP3-15 | 0.07 | **UNMATCHED** |
| 15 | MINOR | Presentation — The manuscript is excessively caveated, internally repetitive, and difficult to audit. Key definitions su | DP3-07 | 0.53 | MATCHED |
| 16 | MINOR | Figures 3, 4, 8, 9, 11 — Several figures show cross-transfer, display-only, fixed-prior, or non-catalog scores while the | DP3-14 | 0.22 | **UNMATCHED** |
| 17 | MINOR | Tables I–II — The reconciliation of 36.76M, 36.93M, 37.29M, 377,482, 268,519, 387,695, and historical cross-transfer tot | DP3-04 | 0.47 | MATCHED |
| 18 | MINOR | Terminology — “Anomaly,” “candidate,” “detection,” “validated,” “recovery,” and “novelty” are used with different meanin | DP3-07 | 0.18 | **UNMATCHED** |

**Match rate: 6/18 = 33% MATCHED, 12 UNMATCHED.**

Exit 2 — 12 finding(s) need a full §3 truth-audit (genuinely-new candidates or too-weak fingerprint overlap).
