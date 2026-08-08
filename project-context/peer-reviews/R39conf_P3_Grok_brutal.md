# P3 R39conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/paper3_anomaly_catalog.pdf` md5=8533c5a7 pages=29
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 136.7s

---

**Referee Report**

**Paper:** Spectrally Unusual Sources at Scale… (Golden, 2026 preprint)

**Journal target:** Phys. Rev. D

**Date of review:** Round R39conf

**Findings**

**P3-E1 (ESSENTIAL) — Internal version-history language (p. 6, Fig. 2 caption)**  
“(superseded by the Path-C native catalog)”.  
This is explicit draft-control / version-tag prose. Required fix: remove every occurrence of “superseded”, “Path-C rebuild”, “before/after diagnostic”, “quarantined”, and all gate-PASS/FAIL bookkeeping from the published text and captions. Replace with neutral scientific language.

**P3-E2 (ESSENTIAL) — Abstract drift on novelty fraction (abstract vs. §IV A, p. 13)**  
Abstract states “a genuine novelty fraction of 178/1000 ≈ 17.8 %”. Body text qualifies this as a single-sample point estimate from the top-1 000 stratum only, obtained against a heterogeneous 18-catalog baseline whose coverage is incomplete for the majority of photometric detections. The abstract omits the coverage caveat and the fact that the 17.8 % figure is not a catalog-wide rate. Required fix: rewrite abstract sentence to match the calibrated body statement exactly, including the “top-1 000 stratum” qualifier and the explicit database-coverage limitation.

**P3-E3 (ESSENTIAL) — Non-comparable anomaly scores placed side-by-side without repeated qualification (pp. 3–4, Table I, Fig. 3)**  
S > 5 thresholds are defined on survey-specific validation pools; the text states once (p. 3) that absolute S values “are not cross-survey comparable”. Subsequent tables, figures, and rate comparisons treat the S > 5 cuts as equivalent. Required fix: insert the explicit non-comparability statement at every juxtaposition of per-survey rates or headline counts.

**P3-M1 (MAJOR) — Paper length vs. claimed contribution**  
29 pages + 8 tables + 11 figures for a catalog whose primary cosmological deliverable is a 6.1 % central-value shift in a Fisher forecast that remains < 1 σ from the null. PRD page limit for a methods + catalog paper with marginal new-physics reach is ~15–18 pages. Required fix: condense to ≤ 18 pages or move the bulk of the per-survey diagnostics and gate tables to a companion data-release paper.

**P3-M2 (MAJOR) — Training-bias artifact dominates one survey (p. 10, §III D)**  
98 % of the LAMOST native-retrain anomalies are blue-excess objects whose selection is explicitly attributed to the training-set composition. The paper nevertheless releases the full 113 342-object LAMOST slice as part of the “canonical” 378 280 catalog. Required fix: either (a) remove the LAMOST slice from the headline catalog or (b) publish a quantitatively de-biased subsample with the bias correction demonstrated on the same objects.

**P3-M3 (MAJOR) — Fisher forecast relies on untested assumptions about tracer density (p. 18, Fig. 11)**  
The 6.1 % improvement is computed under the dense-tracer Poisson-shot-noise limit. The actual surface density of the gold/silver subsamples lies well below the dense-tracer threshold shown in Fig. 11. No recalculation with the measured densities is provided. Required fix: recompute σ(f_NL) at the actual number densities of the GOLD and SILVER subsamples and report the revised central value and envelope.

**P3-M4 (MAJOR) — “Largest-scale” claim unsupported (abstract + p. 2)**  
The abstract asserts “the largest-scale application … of which we are aware”. The only quantitative comparison offered is to Liang et al. (2023) on 250 k spectra. No systematic literature search or table of prior multi-survey anomaly searches is supplied. Required fix: either remove the superlative or provide a documented comparison that includes at least the three largest published single-survey and multi-survey anomaly searches.

**P3-N1 (MINOR) — Duplicate phrase (p. 7, Table I footnote)**  
“canonical canonical-mask” appears in the production-script reference. Required fix: correct typographical duplication.

**P3-N2 (NIT) — Future date in header (p. 1)**  
“(Dated: June 2026)”. Cosmetic; remove or replace with arXiv submission date.

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript contains multiple instances of internal version-control language, an abstract that overstates the novelty fraction without the body’s coverage caveats, and non-comparable per-survey anomaly scores that are nevertheless compared throughout the results. The cosmological claim reduces to a sub-σ shift in a Fisher forecast whose key assumption (dense-tracer limit) is violated by the actual sample. The paper is also ~50 % longer than warranted by its incremental physics return. These issues are fixable but require substantial rewriting, removal of internal bookkeeping, and re-calculation of the forecast at realistic tracer densities. Until those revisions are made the paper does not meet PRD standards.