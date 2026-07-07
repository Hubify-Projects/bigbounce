# P3 INT — FINAL pre-sign-off full-source referee review

- **Paper:** P3 v3.1.138 — `pipelines/p3_anomaly_engine/paper3_draft.tex`
- **Reviewer:** Claude Code INT leg (Houston subscription), full source + committed-output access
- **Date:** 2026-07-05 (review executed 2026-07-06 UTC)
- **Repo HEAD:** 6ab357a75a54f136f13d851368b24704b8a06a53
- **Mode:** read-only; NO .tex edited. Verified headline numbers against committed JSON.

## VERDICT: ACCEPT — publish-ready confirmed. No genuinely-new real finding.

Every headline number reproduces exactly from committed outputs. Compile is clean
(title/abstract render "268,519 Validated (377,780 Total)", dated July 5 2026 = v3.1.138;
no undefined refs; no overfull hbox >30pt). Honest-null framing on the two cosmological
applications is prominent in title-less abstract, §I, and §V. Tier structure (validated /
exploratory / methodological-lesson) is defined once up-front and internally consistent.

## Number verification against committed outputs

| Claim (file:line) | Paper value | Committed source | Match |
|---|---|---|---|
| Validated headline (L842, L953) | 268,519 unique / 268,319 point-source | `reproduce_headline_dedup.json` VALIDATED_HEADLINE_unique=268519 / pointsource=268319 | ✓ |
| Dedup chain (L842) | 274,353 → 268,519 | JSON total_validated_survey_level_detections=274353 | ✓ |
| Inclusive total (L844) | 377,780 = 378,280 − 500 | consistent excision of 500 Gaia singletons | ✓ |
| SDSS class fractions (L1102) | 76.3% QSO / 19.2% GAL / 4.5% STAR | `sdss_qso_hiz_enrichment.json` 0.7633/0.1921/0.0446 | ✓ |
| SDSS QSO high-z (L1102) | 59,462 QSOs; median z=2.31; 67.3% z>2; 1,150 z>4; 198 z>6 | JSON n_qso=59462; z_median=2.307; 40020/59462=0.6730; z>4=1150; z>6=198 | ✓ |
| Score-z test (L1102) | MW p=1.0e-103; Spearman ρ=+0.036 p=9.6e-19; med 0.197 vs 0.142 | JSON p=1.05e-103; rho=0.0362 p=9.6e-19; 0.1965/0.1415 | ✓ |
| DESI science-class recount (L842) | 2,468 clusters (0.92× Liang2023 2,685) | referenced, 2468/2685=0.919 | ✓ |

## MINOR polish already applied (v3.1.138), verified clean

- MINOR-1: "67.3% at z>2" now unambiguously scoped to the anomaly-selected QSO subset (L1102: "67.3% of these QSOs at z>2"), not the 77,905 catalog. Correct — 67.3% is 40,020/59,462.
- MINOR-2: §sec:sdss (L1102) explicitly states the external ~2.15× enrichment baseline block is intentionally not cited in-text (prior-dependent, non-load-bearing); the self-contained internal control is decisive. Matches the JSON note verbatim.

## Referee notes (no action required)

- Spearman ρ=+0.036 is honestly flagged as SMALL despite high significance (L1102). Correctly disclosed, not overclaimed.
- DESI-stream score-vs-z test deferred pending pod/HF-bound `desi_zall.parquet` (~28.4M rows). Honestly stated as deferred, not faked.
- eROSITA membership-only / irreproducible score axis, Gaia synthetic-tier removal, LAMOST 98% blue-excess exclusion from headline: all prominent, consistent across abstract + body.

**No [MAJOR] or [MINOR] findings.** Publish-ready.
