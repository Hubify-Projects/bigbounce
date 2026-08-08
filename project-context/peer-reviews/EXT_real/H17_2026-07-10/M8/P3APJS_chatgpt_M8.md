VERDICT: REJECT

ISSUES:

[MAJOR] Abstract, §3, and §7 — “validated catalog-grade subset of 268,519.” The headline set has no common selection function: it combines a DESI S>5 cut, an SDSS fixed-size continuity slice, a fixed top-200 Planck quota, and a fixed top-1% NEOWISE quota whose only gate is geometry QA. These selections have incompatible statistical meanings and no common completeness, purity, or false-discovery calibration; exact deduplication does not make their union a validated catalog-grade population. 

ext_P3A_M8

[MAJOR] §3.3 and Table 2 — SDSS headline count of 77,905. The manuscript explicitly states that this number was chosen solely to equal the historical cross-transfer count and is “not a physically or statistically motivated anomaly threshold”; the native top-1% set contains 19,253 objects and the nominal S>5 cut contains only 12. An arbitrary continuity quota contributes roughly 29% of the claimed validated catalog and numerically manufactures the headline count. 

ext_P3A_M8

[MAJOR] §3.1 and Table 3 — DESI catalog composition. Approximately 98.7% of DESI anomaly clusters are not primary science targets, and 86% have DESI_TARGET = 0, including sky fibers and secondary or calibration observations. The manuscript does not demonstrate that these 195,829 entries are anomalous astrophysical sources rather than unusual observing products, sky-subtraction failures, calibration states, or filler-spectrum pathologies. A visual check of only the top 200 cannot establish purity for the remaining 195,629 entries. 

ext_P3A_M8

[MAJOR] §2.2, §6.4(i), and Data Availability — DESI reproducibility. The release mixes real TARGETIDs with internal hashes for 86.6% of DESI rows; the raw native score files and original input linkage were lost, and the manuscript estimates that only about 1.3% of released rows can be re-pulled exactly. Consequently, the catalog’s individual entries, scores, and classifications cannot be independently reproduced or audited, contradicting the claim that the reviewed data product is independently runnable and that every number is recomputable. A complete rerun with stable archive identifiers is required. 

ext_P3A_M8

[MAJOR] §2.2 and §6.4(i) — DESI cross-validation claim. Each fold model scores the full 47,000-object pool, so approximately 80% of each reported score vector is in-sample; the pairwise top-set Jaccard is therefore not a fully out-of-sample catalog test. Moreover, all five proxy models fail the manuscript’s own validation-loss retention gate. These results do not validate the production ensemble, the S>5 threshold, or the 22.5-million-spectrum catalog.

[MAJOR] §2.4 and §6.4 — injection-recovery interpretation. Injection recovery measures sensitivity to the chosen synthetic perturbation, not the purity or physical validity of the selected catalog. The DESI experiment uses the cleanest 5% of spectra, a tail-excluded threshold, and broad injected features that match the detector’s preferred morphology; it does not quantify false positives from sky residuals, arm calibration, continuum normalization, low-S/N data, or target-selection artifacts. The statement that this experiment “establishes that the 268,519 subset is real” is unsupported.

[MAJOR] §3.8 — NEOWISE validation. The only passing test plants sources outside the adopted ecliptic mask and “recovers” them by applying that same mask, so success is guaranteed by construction. No detector-sensitivity, score-stability, train-split-scaler, or contamination test is reported. NEOWISE therefore cannot be included in a catalog labeled “validated”; the manuscript itself acknowledges this deficiency. 

ext_P3A_M8

[MAJOR] §3.6 — Planck validation and selection. The released top-200 patches are selected from a bank that includes training patches; the random train/validation split is not spatially independent because the 10
∘
×10
∘
 patches sample the same correlated sky and may overlap. The 48-versus-30 binomial calculation consequently has an invalid independence assumption and does not rule out leakage. Recovery of artificial Gaussian bumps added after patch standardization also does not establish sensitivity to realistic CMB foregrounds, beams, noise anisotropy, point sources, or mapmaking artifacts.

[MAJOR] §3, §4.3, and the headline count — point sources and CMB regions. Ten-degree Planck map patches are not astronomical objects and cannot be meaningfully deduplicated against point sources with a 5-arcsec friends-of-friends radius. Their 200 entries necessarily survive as distinct records, so appending them to a point-source catalog increases the headline by construction. The CMB-patch product must be separate, with a sky-region representation and an appropriate overlap metric.

[MAJOR] §3.4, §7, and Data Availability — LAMOST and release-accounting contradiction. LAMOST fails injection recovery and is identified as 98% training-bias contamination, yet approximately 113,000 LAMOST detections are included in the 377,482 “inclusive catalog.” The Data Availability section then states that LAMOST is excluded from the released per-object tables and from every headline count. Both statements cannot be true, and the published 377,482-object product cannot be reproduced from the release as described. 

ext_P3A_M8

 

ext_P3A_M8

[MAJOR] §2.2, Table 2, Figures 3–4, Table 4, and §6.2 — score and model provenance. The text alternately says that SDSS and LAMOST scores use native per-survey normalization and that they remain on the DESI-trained cross-transfer scale. Several figures and classifications use the failed historical cross-transfer runs while adjacent text discusses native catalog entries. The manuscript therefore does not provide an unambiguous mapping from each released row to its model, preprocessing version, score axis, and selection threshold.

[MAJOR] §4.1 — “17.8% genuine novelty fraction” and “discovery rate.” Absence from 18 selected catalogs is not evidence that an object is genuinely novel, especially when the parent DESI sample is dominated by sky/filler fibers that may have no astrophysical source at the fiber position. The analysis lacks catalog coverage masks, depth and morphology completeness, proper-motion handling, source-versus-sky verification, systematic image inspection, and spectroscopic confirmation. The defensible quantity is an archival-catalog-unmatched fraction for a specified sample, not a discovery rate. 

ext_P3A_M8

[MAJOR] §4.3 — cross-survey validation and random-coincidence estimate. The released DESI–SDSS comparison gives four positional matches against a heuristic expectation of 2.75 and is explicitly not significant. The manuscript nevertheless extrapolates an RA-shift control that does not preserve footprint geometry into a claim of fewer than ten random matches among 637 cross-survey clusters and less than 2% contamination. This requires survey-specific angular random catalogs, coverage masks, source-density variation, and astrometric-error likelihoods; the current calculation does not support the validation claim.

[MAJOR] §3.1, Table 3, and §6.5 — “like-for-like” comparison with Liang et al. Comparing 2,468 anomalies with a prior catalog of 2,685 by absolute count is not like-for-like when the denominators differ by nearly two orders of magnitude, the target definitions and quality cuts differ, and the anomaly thresholds are unrelated. The manuscript must compare rates, completeness, and purity on an actually matched sample and selection function.

[MAJOR] §5 and Appendix C — multi-tracer f
NL
	​

 application. The forecast is not reproducible from the information provided: the QSO-candidate sample has no redshift cut, the angular-bias measurement has very low significance, the coefficient c is imported from an internal refit without a complete Fisher specification, observational systematics and shot noise are not consistently propagated, and Appendix C uses incompatible absolute normalizations. Mapping a symmetric 1σ interval in α through a clipped nonlinear function is an envelope, not a confidence interval on σ(f
NL
	​

). This section should not remain as a scientific result of the catalog paper.

[MAJOR] §5.1 and Appendix E — NANOGrav analysis. This analysis is not enabled by, or logically connected to, the anomaly catalog. It uses a factorized KDE free-spectrum approximation rather than the timing likelihood, while the treatment of the original free-spectrum priors and inter-bin dependence is insufficiently documented for independent assessment. The large point-hypothesis Bayes-factor ratio is then emphasized despite the manuscript conceding that realistic environmental SMBHB models occupy the same spectral-index range. This material requires a separate, fully developed analysis and should be removed here.

[MINOR] §4.2 — spatial statistics. A Poisson uniformity test over only occupied HEALPix pixels from several highly nonuniform survey footprints has no interpretable null hypothesis, and null correlations with Galactic latitude or dust do not test instrumental systematics without the parent-survey selection functions. The quoted χ
2
 and significance values should be removed rather than retained as “diagnostics.”

CENTRAL CLAIM: No—the manuscript demonstrates that a pipeline can rank reconstruction outliers at large scale, but it does not establish a uniformly selected, independently validated, scientifically interpretable, and reproducible catalog of 268,519 anomalies.
