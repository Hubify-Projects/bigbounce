# P3 EXT20 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=62d7b294 pages=30
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 118.2s

---

**REFEREE REPORT — Physical Review D**

**Manuscript:** Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies… (Houston Golden)

**Round:** External (first submission)

### ESSENTIAL issues (paper cannot be accepted without fixes)

**P3-E1 (Abstract, p. 1; §IV A, p. 14)**  
Abstract states a “genuine novelty fraction of 178/1,000 ≈ 17.8% (Wilson 68% CI ±1.2%)”. Body text explicitly qualifies this as a *database-coverage measurement* against 18 catalogs, not a true astrophysical novelty rate, and notes that SIMBAD-unmatched fractions “overstate true catalog novelty”. The abstract claim is stronger than the calibrated body statement.  
*Required fix:* Rewrite abstract sentence to match the body’s final, caveated wording or remove the percentage.

**P3-E2 (Abstract, p. 1; §V, pp. 17–18; Table VIII, p. 24)**  
Abstract and §V present a 6.1% central improvement in \(\sigma(f_{NL})\) (8.98 → 8.43). Body and Table VIII show this is obtained only under the fixed-bias prior \(\alpha=0.15\) using the *empirical* \(\alpha_{jk}=0.19\pm0.65\); the de-biased single-tracer baseline returns exactly the original value (8.98). The paper states “no multi-tracer improvement at current S/N”. Abstract omits the null result.  
*Required fix:* Abstract must state that the multi-tracer gain is statistically consistent with zero.

**P3-E3 (§II B, p. 4; §III C–D, pp. 8–9; Table I footnotes)**  
Anomaly score \(S\) is defined per-survey on *native-retrain* validation sets whose \(\mu_{val},\sigma_{val}\) differ (DESI: 0.0287; SDSS/LAMOST use different retrains). Text repeatedly states “absolute \(S\) values are not comparable across independently trained surveys”. Yet the catalog merges all surveys into a single ranked list and headline numbers. This is an internal inconsistency.  
*Required fix:* Either (a) publish only per-survey ranked lists with explicit non-comparability warnings on every combined figure/table, or (b) demonstrate a survey-independent ranking metric.

**P3-E4 (§III D, p. 9; §VI A, p. 20)**  
98% of LAMOST anomalies are flagged as a “training-bias artifact” (blue-excess). The paper still includes the full 44,075-object LAMOST tier in the headline 378,280 count and only later notes it is “exploratory”. This violates the claim of a uniformly processed multi-survey catalog.  
*Required fix:* Move the entire LAMOST tier to an explicitly labeled “exploratory / training-contaminated” supplement or remove it from the primary catalog.

### MAJOR issues

**P3-M1 (Length vs. contribution)**  
30-page manuscript whose primary deliverable is a catalog whose majority objects are either (a) training artifacts, (b) already-known cool dwarfs, or (c) objects whose anomaly status is not reproducible across architectures. PRD page limit for a catalog/methods paper of this type is typically ≤18–20 pages. The present length is not justified by the strength of the cosmological result (null).

**P3-M2 (§IV A, p. 14; Fig. 6)**  
The 17.8% “genuine novelty” figure is derived from a 1,000-object top-ranked subset cross-matched to 18 catalogs. No equivalent calculation is shown for the full 378k catalog, nor is a control sample of *non-anomalous* sources processed identically. The number is therefore not demonstrated to be a property of the anomaly population.

**P3-M3 (§V B, p. 18; Fig. 9)**  
The per-redshift-bin Fisher forecast improvement is shown only for the fixed \(\alpha=0.15\) prior. No figure or table shows the result under the empirical posterior on \(\alpha_{jk}\) or under a flat prior. The claimed “central 9.4% improvement” is therefore prior-dependent and not robustly demonstrated.

**P3-M4 (Reproducibility, §II and Data Availability)**  
All numerical results depend on >20 committed but non-frozen pipeline scripts, JSON configuration files, and “production recipe” runs whose exact commit hashes and random seeds are not provided in the manifest. A standalone reader cannot recompute the headline 378,280 number or the 17.8% fraction from the text alone.

### MINOR issues

**P3-m1** Multiple instances of internal bookkeeping language remain in footnotes and table captions (“Path-C native-retrained counts are the canonical results”, “superseded by the Path-C native catalog”, “R7” style references). These must be removed.

**P3-m2** Fig. 3 right panel y-axis spans >14 orders of magnitude with no justification for the dynamic range or discussion of numerical stability of the MSE tail.

**P3-m3** Equation (2) normalizes by survey-specific \(\sigma_{val}\), yet the text never states whether the quoted \(S>5\) threshold is applied before or after this per-survey rescaling when constructing the merged catalog.

**P3-m4** Bibliography contains several arXiv-only citations used as load-bearing evidence for the matter-bounce prediction without quoting the exact numerical forecast from those papers.

### NITs

- Inconsistent use of “Path-C” vs. “native-retrain” terminology across captions and body.
- Several figure captions contain parenthetical asides that belong in the main text (“not a like-for-like comparison”).
- Typo: “coadd-vs-catalog” (p. 6) should be “coadd vs. catalog”.

## Summary recommendation

**REJECT**

The manuscript fails to meet PRD standards on three independent grounds: (1) the abstract makes quantitative claims that are explicitly caveated or contradicted in the body; (2) the anomaly score is not on a common scale across surveys, yet the paper presents a single merged catalog and headline statistics; (3) the cosmological result is a null detection whose marginal numerical improvement disappears under the de-biasing procedure the authors themselves apply. The combination of an over-long manuscript, pervasive training-set artifacts, and irreproducible pipeline dependencies makes the work unsuitable for Physical Review D in its current form. A substantially shortened, per-survey version that treats the LAMOST tier as exploratory and removes all overstated novelty and \(f_{NL}\) claims might be reconsiderable at a methods-oriented journal, but not at PRD.