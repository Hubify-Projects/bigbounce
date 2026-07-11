(1) VERDICT: REJECT

(2) ISSUES: 

h17d_P3

[MAJOR] Abstract, §III, and Conclusions — claim of a “validated catalog-grade” subset of 268,519 anomalies: No analysis establishes catalog purity or a false-discovery rate. Injection–recovery measures sensitivity to selected synthetic perturbations; it does not determine whether high-scoring real entries are astrophysical sources rather than calibration errors, sky-subtraction residuals, noise excursions, or distribution-shift failures. The reconstruction loss is not inverse-variance weighted, and the 0/200 visual-artifact result applies only to the top-ranked 200 objects, not to a representative sample of 268,519. The word “validated” is therefore unsupported.

[MAJOR] §III C and Table II — SDSS catalog definition: The 77,905-object SDSS tier is explicitly a fixed-size “continuity slice” chosen to reproduce the obsolete cross-transfer count, not a threshold selected from the native score distribution. The same native run gives 19,253 objects at its top-1% cut and only 12 at S>5. Because 77,905 detections enter the 274,353 pre-dedup validated total, the headline 268,519 count depends materially on a post-hoc numerical choice with no statistical or physical justification.

[MAJOR] §III H and the three-tier catalog definition — NEOWISE validation: NEOWISE is included in the “validated catalog-grade” tier even though its only gate plants sources outside the adopted ecliptic mask and then applies that same mask, guaranteeing 100% “recovery” by construction. This checks code geometry, not anomaly-detector sensitivity, ranking stability, completeness, or purity. A tier with no detector validation cannot be grouped with detector-sensitivity-passing surveys under a catalog-grade label.

[MAJOR] §III A and §VI D(i) — dominant DESI population is not the population that was validated: The manuscript states that approximately 98.7% of deduplicated DESI anomaly clusters have no primary science-class target bit and that 86% have DESI_TARGET = 0, so sky, filler, secondary, and calibration spectra dominate the 195,829 detections. The production-ensemble injection test instead uses 20,000 re-pulled spectra classified as GALAXY, QSO, or STAR. It therefore does not validate the population responsible for almost the entire DESI headline. Redrock assigning a SPECTYPE does not establish that a sky or low-quality spectrum is a real astrophysical source, especially when the paper reports secure ZWARN=0 redshifts for only about 0.1% of the anomaly-matched DESI spectra.

[MAJOR] §III A and Table III — irreconcilable DESI science-target accounting: The quoted per-class rates imply roughly 0.0075×4.9M+0.00037×1.5M≈37,300 anomalies in the validated-TARGETTYPE galaxy and QSO subsets, whereas the positional science-bit recount finds only 2,468. The explanation that a broader bitmask catalog with fewer quality cuts reduces the count by a factor of about 15 is not logically sufficient; an explicit one-to-one identifier audit is required. Until this discrepancy is resolved, neither the 2,468 figure nor the claim that 98.7% of anomalies are non-science targets is reliable.

[MAJOR] §III A and §VI E — comparison with Liang et al.: Comparing 2,468 anomalies with 2,685 and calling the result “0.92×” like-for-like ignores the denominators. The manuscript’s own figures correspond to approximately 0.012% on 20.3 million rows versus approximately 1.07% on 250,000 spectra, a rate difference of nearly two orders of magnitude. Absolute counts from samples differing by roughly a factor of 80 are not a matched benchmark.

[MAJOR] §II B, §II D, and §VI D(i) — the claimed out-of-sample DESI stability test is not out of sample: Each fold model is trained on 80% of the 47,000-spectrum pool and then scores the full pool; consequently, 80% of every fold score vector is in-sample. Pairwise Jaccard overlap between those five vectors is not an out-of-fold top-set stability statistic. A proper cross-fitted catalog would score each object only with the model whose training set excluded that object. Moreover, all five proxy models fail the paper’s own validation-loss gate, with best mean validation loss 1.91 versus the 0.30 criterion, so their ranking stability cannot validate the production ensemble.

[MAJOR] §II B and Table II — inconsistent anomaly-score definition: Equation (2) defines S using each native survey’s validation mean and standard deviation, but Table II states that native SDSS and LAMOST share the DESI-trained score scale. Native thresholds S=0.1060, 0.2051, and 0.4613, the DESI S>5 threshold, Planck raw MSE, and the irrecoverable eROSITA production axis are then discussed under overlapping “score” terminology. The manuscript does not provide a single unambiguous mapping from released columns to model, preprocessing state, μ
val
	​

, σ
val
	​

, and selection rule for every tier. This prevents an end-to-end reproduction of the catalog selection.

[MAJOR] §III F and Table VII — Planck validation is invalid: The native model is trained and scored on the same 200,000-patch bank, and the randomly split 10
∘
×10
∘
 patches necessarily overlap strongly on the sky, so train and validation sets are not spatially independent. The binomial calculation for 48 validation members among the top 200 assumes independent trials and cannot be used to “rule out memorization.” The injection adds a broad 5σ, σ=8-pixel bump after per-patch standardization without re-standardizing, making the planted feature exceptionally conspicuous. No validation against half-mission difference maps, frequency dependence, foreground templates, end-to-end CMB-plus-noise simulations, or a spatial block holdout is presented. The 200 patches are therefore reconstruction outliers, not validated CMB anomalies.

[MAJOR] §III C, Table IV, Figure 4, and Conclusion item 3 — SDSS scientific characterization is performed on the wrong catalog: The 14 HDBSCAN clusters, the “84% cool dwarfs” result, and the emission-line taxonomy are explicitly derived from the rejected DESI-to-SDSS cross-transfer set. They are nevertheless summarized as properties of “SDSS anomalies” and of the released catalog. The native 77,905-object continuity slice may have different membership and population fractions; the characterization must be rerun on the actual released tier.

[MAJOR] §IV A and §IV C — novelty and cross-survey validation claims: Absence from 18 catalogs does not establish a “genuine novelty fraction.” The analysis lacks catalog-footprint accounting, depth/completeness modeling, source-dependent match radii, proper-motion propagation, deblending checks, and confirmation that a physical source exists at each fiber position. This is especially consequential because the DESI sample is dominated by non-primary and blank-sky/filler fibers. The 178 objects are at most uncataloged candidates. Likewise, the claim that 637 multi-survey clusters exceed random coincidences by more than 60× is based on a non-geometry-preserving RA shift for one survey pair and an unsupported assertion that all other pair contributions sum to less than one. Pairwise spherical-rotation or footprint-conditioned null tests are required. Applying a 5-arcsec point-source deduplication to the centers of 10
∘
 Planck patches is also physically meaningless.

[MAJOR] §V — empirical bias measurement and f
NL
	​

 forecast: An angular-correlation amplitude ratio cannot be interpreted as a linear-bias ratio unless the two samples have matched redshift distributions and angular selection functions. The 5,384 QSO candidates have no redshift cut and are compared with the heterogeneous full anomaly population, so the measured α conflates bias, redshift projection, masks, and contamination. The empirical sample of 5,384 objects is also not the 40,192 redshift-binned tracer population used in Figure 9. Consequently, the measured α=0.19±0.65 does not calibrate the Fisher calculation, and neither the 8.14 central value nor its stated envelope is a defensible forecast.

[MAJOR] §V and Appendix C — the forecast does not test the stated matter-bounce bispectrum and is internally inconsistent: The source of f
NL
	​

=−35/8 explicitly states that the matter-bounce shape is not exactly local and that identifying this number with f
NL
local
	​

 is only a loose shorthand. The manuscript nevertheless inserts it into a standard local-PNG multi-tracer treatment without deriving the squeezed tracer response or the template overlap. 
arXiv
 Independently, the main-text form 1/σ
2
=F
0
	​

+cα
2
 gives σ(f
NL
	​

)=5.67 at α=0.5, as the manuscript itself states in §VI, while Table IX gives 7.15 from a linear scaling; Figure 11 then uses an incompatible single-tracer normalization of 16.85 instead of 8.98. These are different forecasts, not interchangeable representations of one calculation.

[MAJOR] §V A and Appendix E — NANOGrav result: Fitting a two-parameter power law to all 30 free-spectrum bins is known to bias the recovered amplitude and spectral index because the signal falls below white noise at about the first 14 bins; NANOGrav’s methods explicitly warn against adding more bins for that model. 
arXiv
 Free-spectrum-refit validation studies also show the inferred slope shallowing toward γ∼2−3 as high-frequency bins are added because of unmodeled or white-noise contamination. 
arXiv
 Thus γ=2.567 may be an analysis artifact. In addition, the cited matter-bounce literature predicts a primordial scale-invariant tensor spectrum, whereas the NANOGrav convention defines γ through h
c
	​

∝f
(3−γ)/2
; no cosmological transfer calculation is supplied that yields the asserted γ=3. 
arXiv
+1
 The quoted 7.14×10
3
 Bayes-factor ratio also depends on a tiny KDE tail density, with no bandwidth, bin-number, free-spectrum-approximation, or noise-model uncertainty.

[MAJOR] Data Availability statement and reproducibility claims: The manuscript promises that the repositories will become public rather than providing an accessible frozen review artifact. More seriously, it states that native production score files, raw production spectra, the Planck checkpoint and patch tensor, and some feature tables reside on exited or wiped compute nodes; the eROSITA score axis is unrecoverable; and an earlier Gaia product was an undetected synthetic fallback. Reproducing the final deduplication from already-selected lists is not end-to-end reproducibility of training, scoring, thresholding, and validation. The central results cannot be accepted until all load-bearing inputs, checkpoints, score vectors, manifests, and executable environments are available and independently rerun.

[MAJOR] Overall scope: The NANOGrav analysis uses no object, score, tracer, or other output from the anomaly catalog and is not an application of it. The manuscript combines an astronomical outlier catalog, an inadequately calibrated large-scale-structure forecast, and an unrelated PTA reanalysis. These require separate studies; their combination obscures rather than strengthens the scientific case for any one result.

[MINOR] Title, Abstract, and Tables I–II — scan-volume accounting: The paper alternates among 36.758 million retained-native inputs, 36.93 million read/scored inputs, and 37.292 million cross-transfer-inclusive processing passes, then describes 37.3 million as a rounded-up source count. Historical rescoring passes, quarantined data, synthetic or excised feature-table reads, and unique astronomical inputs must not be combined under one “sources and patches scanned” number.

[MINOR] Organization and presentation: The manuscript is excessively repetitive, repeatedly restates the same caveats, embeds internal repository paths throughout the scientific narrative, duplicates limitations such as single-architecture dependence, and retains figures and analyses explicitly labeled obsolete, quarantined, or non-diagnostic. Substantial restructuring is required before the scientific content can be evaluated efficiently.

(3) The central claim is not supported: the manuscript shows that the pipeline can generate a large numerical reconstruction-outlier list, but it does not demonstrate that 268,519 entries constitute a validated catalog of real astrophysical anomalies.
