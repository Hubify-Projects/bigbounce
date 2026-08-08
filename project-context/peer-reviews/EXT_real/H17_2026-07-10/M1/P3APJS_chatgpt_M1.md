(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Abstract, §3, and Conclusions — “validated catalog-grade subset of 268,519.” This number has no coherent scientific selection function. The SDSS contribution of 77,905 was chosen specifically to preserve the size of an obsolete cross-transfer sample, whereas the native top-1% selection contains 19,253 objects and the nominal S>5 cut contains 12; Planck and NEOWISE use predetermined top-ranked counts, and NEOWISE’s only “validation” is a mask test that passes by construction. Reproducing the arithmetic of the 5″ deduplication does not validate the constituent detections. 

ext_P3A_M1

[MAJOR] §3.1 and Table 3 — DESI objects are not established to be astrophysical point sources. DESI contributes 195,829 of the 274,353 pre-dedup detections in the validated headline, yet only 2,468 of 190,015 DESI clusters match primary science-class targets at 1″, and the manuscript states that approximately 98.7% fall on non-primary, sky, or filler spectra. Sky-fiber and calibration spectra cannot be counted as “point-source anomalies” merely because they have fiber coordinates; every retained DESI entry must first be associated with a real target or explicitly classified as an instrumental/background-spectrum anomaly.

[MAJOR] §3.1 and Table 3 — the DESI science-target bookkeeping is internally unreconciled. The reported validated-TARGETTYPE rates imply roughly 4.9M×0.75%+1.5M×0.037%≈37,300 GALAXY/QSO anomalies, while the claimed like-for-like science-target yield is only 2,468. The table asserts that the relevant rows use the same per-class denominators but different filter stacks; this does not establish which numerator is the actual science-target anomaly catalog and therefore does not support the claimed 0.92× comparison with Liang et al.

[MAJOR] §2.4 and §6.4 — injection recovery is incorrectly treated as evidence of catalog purity. Recovering selected synthetic broad continuum dips, emission spikes, or Gaussian CMB bumps measures sensitivity to those planted morphologies; it does not demonstrate that the hundreds of thousands of real-data outliers are astrophysical, nor does it estimate their false-positive rate. The DESI test uses a cleanest-5% substrate, the Planck test uses an extremely broad 5σ bump, and the NEOWISE test only verifies a hard-coded coordinate mask. The statement that these tests establish that the catalog “is real” is not logically supported.

[MAJOR] §2.2 and §6.4(i) — the DESI held-out validation is not a validation of the released production catalog. Each fold scores the full 47,000-object pool, so most objects in each score vector were used to train that fold; the short-trained fold models also fail the manuscript’s own validation-loss retention criterion and are not the production ensemble. The full 22.5-million-spectrum out-of-fold re-inference is explicitly unavailable because the required score products were left on an exited compute pod. Jaccard stability among undertrained proxy models cannot establish the validity or membership stability of the released production selection.

[MAJOR] §3.6 — the Planck validation is invalid because the train/validation units are not independent. The 200,000 10
∘
×10
∘
 patches are extracted from one sky map and must overlap extensively; a random patch split therefore leaks the same sky structure between training and validation. The released top-200 are selected from the full in-sample bank. Moreover, an excess of high-error validation patches over training patches is exactly what can result when training examples are reconstructed preferentially well; it does not rule out memorization. The quoted binomial probability assumes independent patches and is unusable without spatial blocking, while no CMB simulations, half-mission difference maps, alternative component-separation maps, or foreground/noise nulls are presented.

[MAJOR] §2.2, §3.1, and §6.3 — the anomaly score is inadequately controlled for survey noise and calibration systematics. Spectra are downsampled to 496 bins and scored with unweighted MSE after per-spectrum normalization, without inverse-variance weighting, pixel masks, or an explicit model of sky subtraction, arm-edge noise, throughput, observing conditions, or fiber calibration. The unresolved population of approximately 44,000 DESI B-dominant objects is itself consistent with a calibration mode. For NEOWISE, normalization is fit on the full sample and the train-only-scaler robustness test remains unperformed because the feature table is unavailable. These omissions preclude a defensible selection function or contamination estimate.

[MAJOR] §4.1 and Figure 6 — “17.8% genuine novelty” is not established. Absence from a collection of positional source catalogs does not demonstrate that a spectrum represents a previously unknown astrophysical object, particularly when the DESI anomaly sample is dominated by sky/filler fibers. The 178 objects require verified source associations, inspection of the underlying targeting and imaging records, and astrophysical confirmation before being called genuinely novel. The separate 58.8% statistic is also internally invalid: it is described as pooling three top-100 samples but is computed as 235/400 using a historical fourth sample containing the subsequently removed synthetic Gaia tier.

[MAJOR] §3.3, §3.4, Figures 3–4, and Table 4 — the reported astrophysical populations do not characterize the released native catalogs. The SDSS UMAP/HDBSCAN clusters, the 84% cool-dwarf fraction, and the emission-line taxonomy are explicitly derived from the DESI-trained cross-transfer sample, not from the released native SDSS selection. Likewise, the 98% LAMOST blue-excess fraction is measured before native retraining, and the manuscript admits that the post-retrain arm-dominance distribution was never recomputed. These cross-transfer failure-mode diagnostics are nevertheless presented in the Conclusions as properties of the final catalog.

[MAJOR] §4.3 — the deduplication does not define “unique physical objects.” A uniform 5″ friends-of-friends merge is applied across heterogeneous spectroscopic targets, WISE-derived sources, repeated fiber observations, and centers of 10
∘
 Planck map patches. A CMB patch center has no meaningful 5″ point-source association radius, and a single fixed radius does not account for astrometric error ellipses, proper motion, source crowding, or the NEOWISE PSF. The point-source and CMB products must be separate catalogs, and inter-survey associations require a probabilistic match model rather than being folded into one physical-object count. 

ext_P3A_M1

[MAJOR] Data Availability, §2.2, §2.4, §3.5, and §3.7 — the reproducibility claim is contradicted by the manuscript’s own provenance record. The eROSITA production score axis is irreproducible; the Gaia table was synthetic; the DESI production score parquets needed for full held-out re-inference are unavailable; the Planck checkpoint and patch tensor are stated not to be in the public release; and the NEOWISE derived feature table required for a basic leakage test existed only on the compute pod. The catalog and DOI are also described prospectively rather than supplied as an immutable reviewable release. This is incompatible with the assertion that every result is independently recomputable and is disqualifying for an ApJS catalog submission.

[MAJOR] §5 and Appendix C — the f
NL
	​

 application is not a valid result of this catalog. The empirical bias measurement is consistent with zero, and the manuscript’s own de-biasing returns exactly the single-tracer baseline. The bias is measured on 5,384 photometric QSO candidates with no redshift cut, whereas Figure 9 forecasts with a different 40,192-object redshift-binned sample; no common selection function, n(z), contamination model, covariance, or demonstrated bias transfer connects those samples. The cα
2
 mapping is an imposed parametrization, and Appendix C uses a separate absolute Fisher normalization. The section should be removed or rebuilt as a separate analysis.

[MAJOR] §5.1 and Appendix E — the NANOGrav analysis is disconnected from the catalog and its interpretation is overstated. It uses a factorized KDE approximation to a published free-spectrum posterior rather than a timing-data likelihood, and the large fixed-index Bayes-factor ratio only compares two idealized spectral slopes within that approximation. It does not discriminate a matter bounce from the broader SMBHB model class; the manuscript’s own environmental caveat concedes that SMBHB models can occupy the recovered slope range. This material does not support the catalog and should not be part of this submission.

[MINOR] Title, Tables 1–2, and Figures 2–4, 8, and 10 — the presentation preserves obsolete and non-catalog quantities. The “37.3 million” title figure counts processing passes and superseded inputs rather than a single unique source/patch population; several principal figures show cross-transfer, quarantined, or removed tiers instead of the released catalog; Figure 10 calls itself the full validation summary while omitting the DESI injection-recovery curve; and Figure 8 prints non-catalog display scores that cannot be checked against the selection threshold. All headline tables and figures must describe only the exact released membership and production scores.

(3) The central claim that the manuscript delivers a validated, catalog-grade set of 268,519 unique astrophysical anomalies is not supported by the evidence presented.
