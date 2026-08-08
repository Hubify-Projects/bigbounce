# ledger_match DRAFT — P3 — P3_chatgpt_FR1b.md

> DRAFT for the Opus truth-auditor, NOT a replacement. Conservative threshold (prefers UNMATCHED over a false match). Every UNMATCHED finding — and every low-score MATCHED — still needs a human/Opus source-cited disposition per §3.
>
> ledger: `project-context/peer-reviews/DISPOSITIONS/P3.md` (18 D-ids)  |  findings parsed: 17  |  threshold: 0.3

| # | sev | finding (first 120 chars) | best match | score | status |
|---|-----|---------------------------|-----------|-------|--------|
| 1 | MAJOR | Abstract, §III, and §VII — claim of a “validated catalog-grade” subset. The validation procedures do not establish that  | DP3-07 | 0.40 | MATCHED |
| 2 | MAJOR | §III A and Table III — irreconcilable DESI population accounting. The dominant DESI component is said to consist overwhe | DP3-11 | 0.79 | MATCHED |
| 3 | MAJOR | §III A and §VI E — invalid “like-for-like” comparison with Liang et al. Comparing 2,468 anomalies selected from approxim | DP3-07 | 0.46 | MATCHED |
| 4 | MAJOR | §III C and Table II — the SDSS contribution is chosen arbitrarily. The 77,905-object native SDSS tier is explicitly defi | DP3-14 | 0.50 | MATCHED |
| 5 | MAJOR | fraction of the 268,519 headline count is determined by an arbitrary continuity convention and could be changed by tens  | DP3-07 | 0.34 | MATCHED |
| 6 | MAJOR | §III C, Table IV, and Figs. 3–4 — cross-transfer and native SDSS catalogs are conflated. The UMAP/HDBSCAN clusters, cool | DP3-14 | 0.78 | MATCHED |
| 7 | MAJOR | §II B–D and §VI D — the score and validation gates do not define a statistically controlled catalog. A standardized reco | DP3-06 | 0.36 | MATCHED |
| 8 | MAJOR | §II B(c) and §VI D(i) — DESI generalization is not established for the production catalog. The training set contains onl | DP3-12 | 0.90 | MATCHED |
| 9 | MAJOR | §III F and Table VII — the Planck tier is not a validated CMB-anomaly catalog. The model is trained and scored on the sa | DP3-06 | 0.58 | MATCHED |
| 10 | MAJOR | §IV A and Fig. 6 — “genuine novelty fraction” is not demonstrated. Absence from 18 catalog cone searches is an unmatched | DP3-07 | 0.18 | **UNMATCHED** |
| 11 | MAJOR | §V and Appendix C — the f NL ​ forecast is internally inconsistent and physically under-specified. The empirical angular | DP3-10 | 0.39 | MATCHED |
| 12 | MAJOR | §V A and Appendix E — the NANOGrav analysis does not support a matter-bounce inference. This analysis does not use the a | DP3-18 | 0.46 | MATCHED |
| 13 | MAJOR | §II D, §§III E–G, and the Data Availability statement — reproducibility claims conflict with the documented provenance.  | DP3-08 | 0.40 | MATCHED |
| 14 | MAJOR | Title, Abstract, Tables I–II, and §VII — the 37.3-million scale claim is misleading. The manuscript gives three differen | DP3-04 | 0.78 | MATCHED |
| 15 | MAJOR | Overall scope and suitability for Physical Review D. The manuscript combines an astronomical data-catalog paper, an inco | DP3-10 | 0.25 | **UNMATCHED** |
| 16 | MINOR | §IV B–C — spatial and coincidence diagnostics are non-informative under the adopted nulls. The occupied-pixel Poisson χ  | DP3-10 | 0.08 | **UNMATCHED** |
| 17 | MINOR | Figures and presentation. Several prominent figures display superseded, failed, or removed analyses rather than the prim | DP3-07 | 0.40 | MATCHED |

**Match rate: 14/17 = 82% MATCHED, 3 UNMATCHED.**

Exit 2 — 3 finding(s) need a full §3 truth-audit (genuinely-new candidates or too-weak fingerprint overlap).
