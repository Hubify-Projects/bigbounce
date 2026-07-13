(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Abstract, §3 “Three-tier catalog structure,” and §7: the statement that “validation establishes that the 268,519 subset is real” is not supported. The reported tests measure reconstruction-ranking stability or recovery of selected synthetic perturbations; they do not measure catalog purity, false-discovery rate, or the astrophysical reality of the released entries. The product should be described as a reconstruction-outlier candidate list unless independent, blinded validation is supplied. 

ext_P3APJS_M17

[MAJOR] Title, Abstract, §3.1, and Table 3: the dominant DESI component is not demonstrably a point-source catalog. The manuscript finds that approximately 98.7% of DESI anomaly clusters lack a primary science-target bit and that 86% have DESI_TARGET = 0, explicitly including sky fibers, fillers, and secondary/calibration observations. These cannot all be counted as “point-source” anomalies. The DESI tier must be partitioned by fiber purpose and source status, with blank-sky and calibration spectra removed from the astronomical-source headline.

[MAJOR] §3.3 and Table 2 footnote ♡: the 77,905-object SDSS contribution is an arbitrary fixed-size “continuity slice” chosen to reproduce the cardinality of an obsolete cross-transfer result. The native top-1% selection contains 19,253 objects, while only 12 satisfy the nominal S>5 criterion. Including all 77,905 in the validated headline makes the catalog size partly a bookkeeping choice rather than an outcome of a calibrated anomaly criterion. A scientifically motivated, pre-specified threshold must be adopted and the headline recomputed.

[MAJOR] §3.4, Table 2 footnote ♠, and §7: the 113,342-object LAMOST tier is admitted to be 98% blue-excess contamination and to fail the 5σ injection-recovery gate at 5.8%, yet it is included in the “inclusive Path-C catalog” of 377,482. A known failure population is not a catalog of astronomical anomalies and should be released only as a diagnostic data product, outside every canonical catalog total.

[MAJOR] §3.1 and Table 3: the DESI science-target accounting is internally inconsistent. The quoted per-class rates imply roughly 0.0075×4.9 million +0.00037×1.5 million ≃37,300 galaxy/QSO anomalies, whereas the positional science-bit recount gives only 2,468. The manuscript’s explanation invokes two filter stacks but does not provide the intersections needed to reconcile a factor of about 15, and the supposedly broader science-bit selection paradoxically yields the much smaller count. Exact source-level contingency tables and join diagnostics are required.

[MAJOR] §3.1, §6.5, and the comparison with Liang et al.: even if the 2,468 count were correct, calling 2,468 versus 2,685 a “like-for-like” 0.92× comparison is misleading because the denominators differ by nearly two orders of magnitude—approximately 20.3 million rows here versus approximately 250,000 spectra in the cited study. The relevant comparison is the rate and selection function, not the absolute number retained.

[MAJOR] §2.2 “In-sample scoring,” §6.4(i), and §3.3: the source-identity statements are mutually incompatible. The manuscript says that 86.6% of released DESI tid values are internal hashes and only about 1.3% of rows are re-pullable, but later states that all 195,790 primary-coadd anomalies join to the DR1 redshift catalog on TARGETID. The paper must explain how both statements can be true and release a stable archive identifier, observation identifier, preprocessing provenance, and source-to-spectrum mapping for every entry.

[MAJOR] §2.2 and §6.4(i): the DESI injection-recovery experiment is not tied to the released selection threshold. The paper places the production S>5 cut near MSE =0.143, yet reports a median MSE of 0.233 on freshly retrieved SPARCL spectra and notes that more than 50% of an uncurated SPARCL sweep is flagged. The injection test instead uses a separate 99th-percentile threshold on a tail-excluded “clean” subset. Consequently, the quoted 99–100% recovery at 5σ is not recovery into the published 0.87% catalog and does not calibrate its completeness.

[MAJOR] §2.4 and §6.4: the validation protocol is not statistically adequate. A validation MSE threshold of 0.30 is not an anomaly-detection validation and is not comparable across 15-, 47-, 496-, and 4096-dimensional inputs with different preprocessing. The alternative 50%-at-5σ criterion is based on selected plant morphologies and supplies no false-positive rate. Moreover, the DESI fold models used for stability checks themselves fail the stated model-retention gate. Survey-specific held-out test sets, empirical null distributions, calibrated operating points, and at least one genuinely independent detector family are required.

[MAJOR] Table 2 caption, §3.3, §6.2, Figures 3–4, and Table 4: the canonical native-retrain products and the obsolete cross-transfer products are repeatedly conflated. Table 2 says SDSS and LAMOST share the DESI-trained score scale while simultaneously presenting native-retrain counts; §6.2 still describes SDSS as a transfer-learning catalog; and the same number, 77,905, denotes two different selections. Figures and classifications derived from the cross-transfer set cannot be used as evidence about the native catalog without an explicit membership comparison and a complete rewrite separating the two analyses.

[MAJOR] §3.6 and Table 7: the Planck validation is compromised by severe spatial leakage. Two hundred thousand 10
∘
×10
∘
 patches drawn from one masked sky map must overlap extensively, yet the train/validation split is random by patch and the full bank—including training patches—is subsequently ranked. The exact-binomial held-out-enrichment calculation therefore violates independence; spatial correlation reduces, rather than increases, the effective sample size. The Gaussian-bump injection is also not representative of realistic CMB foregrounds, beams, correlated noise, or mapmaking residuals. Spatially disjoint block validation and end-to-end simulations are necessary.

[MAJOR] §3.6, §4.3, and the catalog totals: Planck 10
∘
 sky regions are combined numerically with point sources and passed through a 5-arcsec positional deduplication. A patch center is not a source position, and a 5-arcsec match has no meaningful relation to a 10
∘
 region. The CMB-patch product must be published and counted separately rather than included in a single “unique anomaly” headline.

[MAJOR] §3.8: NEOWISE is placed in the validated tier despite having no detector-sensitivity test. Its only gate plants objects outside the fixed ecliptic mask and then “recovers” them by applying that same mask, so 100% recovery is guaranteed by construction. The manuscript also leaves the train-only-scaler robustness test unfinished. NEOWISE must remain exploratory until the anomaly-ranking sensitivity and contamination are tested on independent data or realistic injected variability signals.

[MAJOR] Data Availability and §2.2–§3.7: the reproducibility claims contradict the manuscript’s own provenance disclosures. The text says exact DESI released spectra cannot be rejoined, some NEOWISE feature products existed only on the compute pod, and the Planck checkpoint/tensor was not in the public release; the Data Availability section nevertheless states that no headline depends on unavailable artifacts. It also says LAMOST both contributes approximately 113,000 objects to the 377,482 total and is excluded from released per-object tables and “every headline count.” Acceptance would require a frozen archive containing all processed inputs, weights, mappings, schemas, and an independently tested end-to-end reproduction of every headline number.

[MAJOR] §4.1, Figure 6, and §4.3: “genuine novelty fraction” is an overstatement. Absence from 18 catalogs does not establish a new astrophysical source without catalog-specific footprints, depths, proper-motion propagation, astrometric uncertainties, local chance-match estimates, and manual adjudication; this is especially problematic when the parent DESI list is dominated by sky/filler fibers. The pooled 58.8% statistic is also arithmetically stale—235/400 is described as top-100 samples from three current surveys while the fourth, Gaia, is said to be excluded. Likewise, the random-coincidence estimate for the 637 cross-survey clusters relies on a non-footprint-preserving RA-shift control. These quantities should be recomputed with a probabilistic, geometry-aware cross-match and described as unmatched-candidate fractions.

[MAJOR] §5 and Appendix C: the f
NL
	​

 application is not a defensible cosmological forecast. The measured angular-clustering ratio uses an unconfirmed QSO-candidate sample with no redshift cut and compares it with a reference population having a different, unspecified redshift distribution; such an angular ratio is not directly a large-scale tracer-bias ratio. The fit is made on relatively small angular scales, the empirical result is consistent with zero, the Fisher mapping is an ad hoc F
0
	​

+cα
2
 fit, the 5,384-object bias sample is not reconciled with the 40,192 tracers in Figure 9, and two incompatible absolute Fisher normalizations, 8.98 and 16.85, are used. This section should be removed or developed as a separate analysis with a common selection function, redshift model, covariance, shot noise, and survey window.

[MAJOR] §5.1 and Appendix E: the NANOGrav analysis is scientifically disconnected from the anomaly catalog and does not support the catalog paper’s conclusions. The identification of the PTA spectral-index parameter γ=3 with the cited matter-bounce model is asserted rather than derived through the tensor transfer function and the PTA convention used in Equation E1. The likelihood is a factorized KDE approximation rather than the timing-data likelihood, while the reported 7.14×10
3
 Bayes factor depends on a KDE density evaluated far in the posterior tail without bandwidth or Monte Carlo uncertainty tests. This material should be removed from the catalog submission or presented in a dedicated cosmology paper.

[MINOR] Title, Abstract, Tables 1–2, and manuscript-wide presentation: “37.3 million” is variously defined as 36.76 million retained-native inputs, 36.93 million read/scored entries, or 37.29 million processing-pass volume, including repeated or excised passes. The title should quote one exact, scientifically meaningful denominator. The two-page abstract, repeated warnings, internal filesystem paths, “queued” analyses, and extensive self-audit narrative should be replaced by a concise methods/results presentation and a formal machine-readable catalog-column description.

(3) The central claim is not supported: the manuscript establishes a large, heterogeneous set of reconstruction outliers, but not a reproducible and uniformly validated catalog of 268,519 real astronomical anomalies.
