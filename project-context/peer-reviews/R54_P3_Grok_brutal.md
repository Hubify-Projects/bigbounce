# P3 R54 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/private/tmp/R54_P3/paper3_draft.pdf` md5=84563f72 pages=29
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 298.2s

---

**Referee Report**

**P3-E1 (ESSENTIAL)** — Abstract (p. 1)  
The abstract states a “genuine novelty fraction of 178/1,000 ≈ 17.8% (Wilson 68% CI ±1.2%)”. The body (IV.A, p. 13) gives exactly this number only for the top-1,000 DESI stratum against 18 curated catalogs; the 17.8% figure is never shown to be survey-wide or catalog-grade. Required fix: replace with the precise, survey-stratified statement that appears in §IV.A or remove the aggregate claim.

**P3-E2 (ESSENTIAL)** — Abstract (p. 1) & §V (p. 18)  
Abstract claims “a central forecast \(\sigma(f_{NL})=8.14\) with \(1\sigma\) envelope [3.92,8.98]”. The body (§V.b) shows this value only after inserting the measured \(\alpha_{jk}=0.19\pm0.65\) into the Fisher form; the de-biased single-tracer baseline is exactly 8.98 (no improvement). The abstract therefore presents a derived quantity as the headline result while the text states “no multi-tracer improvement at current S/N”. Required fix: either remove the 8.14 number from the abstract or add the explicit qualifier that appears in the final paragraph of §V.

**P3-E3 (ESSENTIAL)** — §II.D & Table I (p. 7)  
The Path-C headline (378,280 unique objects) is obtained only after a 7-way 5″ deduplication whose result (10,213 duplicates) is stated without an accompanying geometric or random-coincidence calculation inside the main text. The 2.63% compression is presented as a data product rather than a derived quantity. Required fix: supply the explicit random-coincidence integral (or cite a numbered equation) that justifies treating the 637 multi-survey clusters as non-random.

**P3-M1 (MAJOR)** — Length & scope  
The manuscript is 29 pages (including 10 figures, 8 tables, 7 appendices). PRD methods papers on anomaly detection or catalog construction are routinely required to be ≤18–20 pages. The cosmological section (§V) occupies only ~1.5 pages and yields a null result at <1\(\sigma\). Required fix: cut to ≤20 pages or split into a catalog paper + a short methods letter.

**P3-M2 (MAJOR)** — §III.D & §VI.A (LAMOST training-bias)  
98% of the released LAMOST anomalies are identified as a training-set artifact (blue-excess). The paper nevertheless releases 113,342 objects from this survey as part of the “canonical” catalog. The text itself calls this “the single most important methodological lesson”. Required fix: either (a) move the entire LAMOST tier to an exploratory appendix or (b) demonstrate that a post-hoc color cut removes the artifact while preserving the claimed science content.

**P3-M3 (MAJOR)** — Fig. 3 & §III.C (SDSS score distribution)  
The right-hand panel shows the SDSS anomaly-score tail extending to \(S\sim10^{11}\). The caption and text attribute this to “cross-transfer score-axis effect”. No quantitative comparison of the native SDSS versus DESI-trained score distributions is supplied, nor is a Kolmogorov–Smirnov statistic given. Required fix: add a direct native-versus-transferred score histogram with effect-size statistic.

**P3-M4 (MAJOR)** — §IV.A & Fig. 6 (novelty fraction)  
The 17.8% “genuine novelty” claim rests on a 5″ NED+VizieR match rate of 82.2% for the DESI top-1,000. The paper acknowledges that SIMBAD-unmatched fractions are “database-coverage measurements, not discovery rates”. The abstract nevertheless presents 17.8% as a discovery metric. Required fix: replace “genuine novelty fraction” with “fraction absent from SIMBAD+NED+VizieR at 5″” everywhere the phrase appears.

**P3-N1 (MINOR)** — Abstract date  
“(Dated: June 19, 2026)” is a future date. Replace with the actual submission or arXiv date.

**P3-N2 (MINOR)** — Multiple instances of “Path-C” without definition on first use in the abstract and introduction.

**P3-N3 (NIT)** — Inconsistent use of “canonical” (sometimes means native-retrain, sometimes means the final deduplicated list). Standardize terminology.

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript presents an undeniably large catalog and a transparent (if lengthy) reproducibility framework. However, the abstract contains at least two quantitative claims that are stronger than, or ordered differently from, the final calibrated statements in the body; the LAMOST tier is released despite the paper’s own demonstration that it is dominated by a training artifact; the manuscript is ~50% longer than typical PRD catalog papers while the cosmological application is null at <1\(\sigma\); and several headline numbers (compression fraction, novelty fraction, Fisher forecast) are presented without the explicit random-coincidence or geometric controls required for a methods journal. These issues are fixable but require substantial rewriting and shortening before the paper can meet PRD standards.