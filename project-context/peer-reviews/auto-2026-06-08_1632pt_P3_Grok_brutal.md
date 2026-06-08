# P3 auto-2026-06-08_1632pt — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 65.0s

---

**Referee Report**

**P3-E1 (ESSENTIAL, §II.D p.3, Table I p.7)**  
The paper applies three qualitatively different anomaly thresholds (fixed \(S>5\) for DESI, top-percentile slices for SDSS/LAMOST, fixed top-1% for Planck/Gaia/NEOWISE). The headline 378,280 count therefore mixes incompatible selection functions. No quantitative demonstration is given that the resulting rank-ordering is stable under a single uniform cut. Required fix: recompute the entire catalog under one threshold family and show the overlap matrix.

**P3-E2 (ESSENTIAL, §III.D p.4, Table I footnote ‡)**  
98% of the LAMOST “anomalies” are explicitly identified as training-set blue-excess artifacts. These objects are nevertheless retained in the released catalog (exploratory tier). The 21.5× rate compression after native retrain is presented as a success metric while the residual contamination remains >50% of the published list. This violates the claim that the catalog contains “genuine novelty.”

**P3-E3 (ESSENTIAL, abstract & §V.A p.10)**  
The abstract states a 7.9% improvement in \(\sigma(f_{NL})\) relative to the single-tracer baseline. The measured \(\alpha_{jk}=0.19\pm0.65\) is statistically consistent with zero at <1\(\sigma\). The quoted improvement is therefore a central-value forecast, not a detection. The abstract must be rewritten to remove the implication of a positive result.

**P3-E4 (ESSENTIAL, §III.F p.6 & Appendix F)**  
ACT DR6 is formally quarantined (both gate criteria failed) yet the 200 Planck patches are still counted in the 378,280 total. The cross-survey deduplication therefore mixes a validated Planck sample with a null ACT sample without any joint spatial test. The 200-patch stratum must be removed from the headline number or shown to be consistent with the ACT null result.

**P3-M1 (MAJOR, §II.B p.2)**  
Five-fold cross-validation Jaccard indices are reported only for the top-1% slice. No stability metric is given for the full \(S>5\) catalog that is actually released. The production-vs-control Jaccard of 0.732 is cited only for the training pool, not the science catalog.

**P3-M2 (MAJOR, Fig. 2 right panel & §III.C p.5)**  
The SDSS DR18 score distribution spans twelve orders of magnitude because the model was trained on DESI spectra. The extreme tail (\(S>10^{10}\)) is dominated by M7–T2 dwarfs that are out-of-distribution for the DESI training set. The paper presents these as “anomalies” while simultaneously acknowledging they are calibration artifacts. The scientific framing is therefore inconsistent.

**P3-M3 (MAJOR, §IV.A p.9)**  
The 17.8% “genuine novelty fraction” is obtained only after an archival cross-match against 20 curated catalogs. The SIMBAD-unmatched fraction (58.8%) is repeatedly labeled a “database-coverage measurement, not a discovery rate.” The abstract nevertheless advertises the catalog as containing 378k anomalies without this qualification.

**P3-N1 (NIT, throughout)**  
Multiple instances of “Path-C” internal nomenclature and footnote markers that refer to an unpublished companion repository. These should be removed or replaced with self-contained descriptions.

**P3-N2 (NIT, Table I p.7)**  
The two summary rows (“Total (cross-transfer)” and “Path-C unique”) are visually almost identical; the difference is explained only in a 12-line footnote. A clearer visual separation is required.

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript presents an ambitious multi-survey anomaly search but the scientific utility of the released catalog is compromised by heterogeneous selection functions, acknowledged training artifacts that dominate several survey subsamples, and an abstract that overstates a statistically null \(f_{NL}\) result. These issues are not cosmetic; they directly affect the central claim that the catalog constitutes a clean, large-scale discovery resource. A revised version must (i) adopt a single, documented threshold across all surveys, (ii) excise or explicitly flag the LAMOST artifact population, (iii) correct the abstract’s \(f_{NL}\) language, and (iv) remove the quarantined ACT contribution from the headline count. Until these changes are made the paper does not meet PRD standards for methodological transparency and reproducibility.