VERDICT: REJECT

ISSUES:

[MAJOR] Central catalog definition (§§2.2–3; Tables 1–2): The 268,519-object “validated catalog-grade” subset is not selected by a coherent statistical criterion. DESI uses S>5, SDSS uses a fixed-size slice chosen to reproduce an earlier count, Planck and NEOWISE use predetermined top-percentile counts, and NEOWISE has no detector-sensitivity validation. Their union is therefore an aggregation of incompatible selections, not a uniformly validated catalog.

[MAJOR] SDSS headline component (§3.3; Table 2 footnote ♡): The 77,905-object SDSS contribution is explicitly chosen to equal the obsolete cross-transfer count. The native top-1% selection contains 19,253 objects and the nominal S>5 selection only 12. No sensitivity, purity, score-knee, or astrophysical argument justifies including the additional approximately 58,000 objects, yet this arbitrary choice materially determines the headline count and deduplication results.

[MAJOR] DESI injection-recovery validation (§2.2; §6.4(i)): The decisive injection test does not reproduce the released catalog selection. The manuscript places the catalog S>5 threshold near MSE =0.143, while freshly retrieved SPARCL spectra have median MSE approximately 0.233 and more than half are flagged by that threshold. The injection test instead uses a separately constructed 99th-percentile, tail-excluded clean-holdout threshold. Recovery at that different threshold does not validate the sensitivity, contamination, or membership of the released S>5 catalog.

[MAJOR] DESI object provenance and reproducibility (§2.2; Data Availability): The released identifier field contains real DESI TARGETIDs for only 13.4% of rows, with internal hashes for 86.6%; the manuscript estimates that only approximately 1.3% of released rows can be retrieved from SPARCL by identifier. The production raw-score files and input linkage were lost. A catalog whose entries cannot be reliably mapped back to archival spectra or independently rescored is not an acceptable ApJS data product, and this directly contradicts the assertion of complete reproducibility.

[MAJOR] DESI population interpreted as real astrophysical sources (§3.1; §3.3): Approximately 98.7% of DESI anomaly clusters lack a primary science-target bit and 86% have DESI_TARGET = 0, while only approximately 0.1% of anomaly-matched spectra reportedly have ZWARN = 0. A Redrock best-fit SPECTYPE is not evidence that a sky, calibration, secondary-program, or failed-fit spectrum is a genuine galaxy or QSO. The manuscript therefore does not establish that the dominant component of the catalog consists of astrophysical objects rather than data-quality and targeting-system anomalies.

[MAJOR] Irreconcilable DESI denominator accounting (§3.1; Table 3): The reported per-class rates imply of order 3.7×10
4
 anomalies among the approximately 4.9 million galaxy and 1.5 million QSO TARGETTYPE spectra, whereas the science-bit recount finds only 2,468 matches. Describing the discrepancy as two “filter stacks” does not provide a valid shared-object reconciliation, particularly when the table claims the same per-class denominators. The target-class composition and all derived comparisons must be rebuilt from stable shared identifiers.

[MAJOR] Claimed comparison with Liang et al. (§3.1; §6.5): Comparing 2,468 DR1 candidates with 2,685 EDR candidates and calling the result “like-for-like” is invalid. The surveys have very different input sizes, target selections, quality cuts, duplicate handling, models, and anomaly thresholds. Absolute catalog counts cannot be compared without matched denominators and a common selection function.

[MAJOR] Training-set representativeness and spectral preprocessing (§§2.1–2.2): A 47,000-spectrum training pool is used for 22.5 million DESI spectra, but its construction is not documented by target class, fiber type, spectrograph, tile, observing conditions, calibration state, S/N, or failure mode. Exact layer widths, masks, bad-pixel treatment, inverse variances, wavelength resampling, missing-arm handling, and output activation are also absent from the manuscript. Given the dominance of non-primary spectra in the output, representativeness is a load-bearing untested assumption.

[MAJOR] Validation does not establish catalog purity or completeness (§2.4; §6.4): Validation-loss thresholds measure reconstruction of the training distribution, not anomaly-detection performance, and the same numerical loss gate is applied across unlike input domains. The injection families—broad continuum dips, emission spikes, latent perturbations, and Gaussian map bumps—are not shown to represent the empirical anomaly population. There is no labeled benchmark, blinded random-sample inspection, class-dependent completeness, calibrated false-positive rate, or comparison with an independent detector architecture. The statement that validation establishes that the subset “is real” is unsupported.

[MAJOR] Planck catalog construction (§3.6; Table 7): The model is trained and scored on the same bank of spatially overlapping 10
∘
×10
∘
 patches, and the released sample is an arbitrary top-200 count. A 5-arcsec deduplication of patch centers treats extended sky regions as point objects and does not merge overlapping patches that may encode the same structure. The post-standardization 5σ Gaussian injection is an artificial, readily detectable perturbation, and the held-out-membership enrichment assumes independence that the manuscript itself concedes is violated. A valid map catalog requires spatially disjoint training/test regions, region-overlap clustering, and validation against realistic CMB foreground and noise simulations.

[MAJOR] NEOWISE validation (§3.8): The reported 100% recovery is guaranteed by planting sources outside a latitude mask and then applying that same mask. This is a software-geometry unit test, not validation of the autoencoder ranking. It cannot support inclusion in a “catalog-grade” tier; actual feature-space injection tests, null controls, and the missing train-only-scaler robustness test are required.

[MAJOR] Novelty claim (§4.1): Absence from 18 positional catalogs is mislabeled “genuine novelty.” It can result from blank-sky fibers, coordinate or association failures, catalog footprint and depth limitations, proper motion, blending, extended morphology, or source variability. This is especially serious because the DESI sample is overwhelmingly non-primary-target spectra. Each candidate must first be shown to correspond to an astrophysical source, and the cross-match must model footprint coverage, local source density, astrometric uncertainty, proper motion, and match reliability. The defensible quantity is an “unmatched candidate fraction,” not a discovery or novelty fraction.

[MAJOR] Data-release definition is internally inconsistent (Data Availability): The manuscript says that LAMOST is excluded from the released per-object tables and from every headline count, while repeatedly defining the 377,482-object headline as including approximately 113,000 LAMOST anomalies. The same section describes a 378,480-row file containing ACT, synthetic Gaia, and eROSITA rows despite their stated excision. The catalog, manifest, row counts, score axes, validity flags, units, and inclusion rules are therefore not unambiguously specified.

[MAJOR] Inclusion of a known failed tier (§3; §3.4; Conclusions): The 377,482-object “inclusive” result contains the LAMOST population that fails injection recovery and is reported to be 98% a training-bias artifact. Counting these entries as a primary catalog result, using them in “largest catalog” multipliers, and deduplicating them with validated components is scientifically misleading. They should appear only in a failure-analysis appendix and should contribute to no catalog-size claim.

[MAJOR] End-to-end provenance control (§3.5; §3.7; Data Availability): A synthetic Gaia fallback entered the production outputs, the eROSITA score axis is unrecoverable, DESI score/input linkage was lost, and parts of the Planck validation depend on artifacts stated to reside on an exited compute node. These are not isolated cosmetic defects; they show that the production workflow lacked adequate provenance safeguards. Acceptance would require a clean end-to-end regeneration from immutable archival inputs, with stable source identifiers, checksummed intermediate products, frozen environments, and independent verification of every released row.

[MAJOR] Headline scan volume (title, abstract, Tables 1–2): The manuscript gives 36.758 million, 36.93 million, and 37.292 million as different versions of the scanned volume and explicitly constructs 37.3 million by counting historical processing passes and pre-excision feature-table reads. Processing events and repeated passes are not unique astronomical inputs. The title and abstract must use the number of unique records scored by the final retained pipeline.

[MAJOR] Cosmological applications (§5; Appendices C and E): The f
NL
	​

 analysis combines a 5,384-object bias sample with a 40,192-object Fisher tracer sample and a 1,122-object confidence subset without demonstrating compatible redshift distributions or selection functions; it also uses incompatible absolute Fisher normalizations, 8.98 and 16.85. The NANOGrav factorized-KDE analysis is unrelated to the anomaly catalog and its extreme tail Bayes factor is not validated against a full timing likelihood or bandwidth/systematic alternatives. These analyses do not validate the catalog and should be removed or submitted separately.

[MINOR] Obsolete and non-catalog figures (Figs. 3, 4, and 8): Several principal figures display cross-transfer populations that are not the released native catalog, or show figure-script “display scores” that are explicitly not catalog scores. Regenerate all science figures from the exact released rows and scores, with stable identifiers and one unambiguous score definition per panel.

[MINOR] Validation-summary inconsistency (Fig. 10; abstract; §6.4): Figure 10 omits the dominant DESI injection-recovery result while the abstract describes DESI, SDSS, and Planck as detector-sensitivity passes; the caption and text give different pass tallies. The plotted curves, survey count, and gate summary must agree exactly.

[MINOR] Presentation and scope: The manuscript is highly repetitive and repeatedly foregrounds “largest,” “141×,” “73×,” and “process-volume” comparisons that it later concedes are not scientifically comparable. The paper should be shortened substantially and reorganized around a clearly defined catalog, its selection function, validation, column schema, and demonstrated use cases.

CENTRAL CLAIM: The central claim that 268,519 catalog-grade anomalies have been validated is not supported by the evidence presented, because the dominant DESI and SDSS components lack a coherent selection function, reliable per-object provenance, and validation tied to the actual released catalog threshold. 

ext_P3A_M6
