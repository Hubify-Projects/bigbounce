# P3 D2 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=7c935f19 pages=29
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 344.6s

---

**Referee Report**

**P3-E1 (ESSENTIAL, Abstract p.1 + §V p.18)**  
Abstract states “the de-biased point estimate returns the single-tracer baseline \(\sigma(f_{NL})^{\rm std}=8.98\) exactly (no multi-tracer improvement…)”. Body §V and Fig. 9 show the multi-tracer value is 8.14 (central) with the same 1\(\sigma\) envelope [3.92, 8.98] that already contains the single-tracer baseline; the 6.1 % shift is therefore inside the quoted envelope and is not a detection. The abstract phrasing is stronger than the calibrated body statement.  
**Required fix**: Rewrite abstract sentence to match body’s final calibrated claim verbatim (“no improvement at 0.29\(\sigma\)”).

**P3-E2 (ESSENTIAL, Abstract p.1 + §IV A p.14)**  
Abstract headline novelty fraction “\(\approx17.8\%\) (Wilson 68 % CI \(\pm1.2\%\))” is computed on the DESI top-1 000 stratum only. Body explicitly states this is “not a survey-wide rate”. Abstract omits the scope limitation present in the body’s final statement.  
**Required fix**: Add explicit scope qualifier in abstract or remove the percentage.

**P3-E3 (ESSENTIAL, Table I p.7 + §III D p.5)**  
Table I lists LAMOST native-retrain anomaly rate 0.39 % after 21.5\(\times\) compression, yet §III D states 98 % of those objects are blue-excess training artifacts. The published “Path-C unique” headline (378 280) therefore contains a known dominant artifact population whose fraction is not subtracted from the catalog total. No column or footnote propagates this correction.  
**Required fix**: Either (a) publish only the artifact-cleaned subset or (b) add an explicit “training-bias contaminated” flag column with the 98 % figure.

**P3-M1 (MAJOR, §II B p.3 + §VI A p.20)**  
Five-fold cross-validation Jaccard \(\bar{J}=0.862\) (PASS) is reported only for the 47 k training pool. No equivalent statistic is given for the full 22.5 M DESI stream or for the other six surveys after native retrain. The single scalar cannot be used to certify the released catalog.  
**Required fix**: Supply per-survey, full-catalog Jaccard or equivalent stability metric.

**P3-M2 (MAJOR, Fig. 3 p.10 + §III C p.4)**  
SDSS cross-transfer scores reach \(S\sim10^{11}\) while native-retrain scores truncate at \(S\sim14\). The figure caption and text acknowledge the dynamic-range mismatch but still juxtapose the two histograms without rescaling or explicit non-comparability warning on every panel. Violates instruction 7.  
**Required fix**: Add bold “not on same scale” annotation on every cross-survey comparison figure.

**P3-M3 (MAJOR, §V p.18 + Table VIII p.24)**  
Fisher forecast improvement (6.1 % at \(\alpha=0.15\)) is shown only under the fixed-bias prior. The empirically measured bias \(\alpha_{jk}=0.19\pm0.65\) returns exactly zero improvement. The headline “multi-tracer improvement” is therefore an artifact of an arbitrary prior choice, not data.  
**Required fix**: Remove all improvement percentages that disappear under the measured bias; retain only the de-biased result.

**P3-N1 (MINOR, p.1)**  
Dated “June 19, 2026” — future date on a submitted manuscript. Cosmetic.

**P3-N2 (NIT)**  
Multiple instances of “Path-C” and “native-retrain” used interchangeably without a single glossary entry. Minor nomenclature inconsistency.

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript releases the largest existing multi-survey anomaly catalog but simultaneously demonstrates that the majority of entries in at least one major tier (LAMOST) are training artifacts, that the cosmological constraint is statistically indistinguishable from the single-tracer null, and that headline stability metrics do not extend to the released catalog. The 29-page length is disproportionate to an incremental catalog product whose primary quantitative claims either vanish or require heavy qualification once the documented systematics are propagated. A substantially shortened, artifact-flagged data-release paper with the de-biased \(f_{NL}\) result as the sole cosmology claim could be reconsidered; the present version does not meet PRD standards.