(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Abstract, §II B–D, §III, and Tables I–II — the 268,519-object “validated catalog-grade” set has no coherent statistical definition. DESI uses an absolute standardized-MSE cut, SDSS uses a fixed-size 77,905-object slice chosen solely to reproduce an obsolete cross-transfer count, Planck uses a fixed top-200 count, and NEOWISE uses a predetermined top-1% count followed by a mask. These cuts control neither a common false-discovery rate nor survey-specific purity or completeness. The authors’ own alternative SDSS threshold changes the input catalog by 58,652 objects, demonstrating that the headline number is principally a threshold convention rather than a measured population. A script that reproduces the deduplication arithmetic does not validate the scientific membership. 

h17_P3

[MAJOR] Title, Abstract, and Tables I–II — the claimed “native-trained scan of 37.3 million” is arithmetically inconsistent with the documented processing. The Table I native read/scored pools sum to approximately 36.94 million, not 37.3 million. Conversely, the Table II Path-C denominator of 37,272,042 equals the six surveys’ public-archive denominators plus the 50,000-source synthetic Gaia run; it also uses the full SDSS and LAMOST archive sizes rather than the smaller actually rescored pools, and 20,000 rather than 200,000 Planck patches. Thus the headline scan volume silently incorporates the removed synthetic Gaia tier and data that were not processed by the claimed native pipeline.

[MAJOR] §III A, Table III, and §VI E — the comparison with Liang et al. is not “like-for-like.” Using the manuscript’s own numbers, this work finds 2,468 anomalies among 20,299,155 science-bit rows, approximately 0.012%, whereas Liang et al. found 2,685 among approximately 250,000 spectra, approximately 1.07%. The yield rates differ by roughly a factor of 88. Comparing only the absolute counts and reporting “0.92×” suppresses the radically different denominators, thresholds, releases, quality cuts, and target definitions. Table III additionally places “∼2,685 targets” in the denominator column even though 2,685 is the comparison catalog’s anomaly count.

[MAJOR] §III A versus §III C — the manuscript does not establish that the DESI detections are astrophysical point sources. Section III A states that approximately 98.7% of deduplicated DESI anomaly clusters lack a primary science-target bit and that 86% have DESI_TARGET = 0, consistent with sky fibers, filler spectra, and secondary observations. Section III C then calls 98.8% of the matched entries “galaxies” and uses this as proof that they are real objects, although only approximately 0.1% have secure ZWARN = 0 redshifts. A Redrock best-fit template assigned to a poor-quality or sky spectrum does not establish a physical source. The unexplained change from 195,829 to 195,790 DESI entries compounds the bookkeeping problem. Consequently, the claims of 268,319 “point-source” anomalies and of source-catalog novelty are not justified.

[MAJOR] §II B–D and §VI D — the validation protocol establishes model stability for selected perturbations, not catalog validity. Jaccard overlap between retrainings measures reproducibility of one model family, not correctness, purity, or astrophysical origin; validation loss is not an anomaly-detection metric. The injection tests use a small number of hand-selected signal morphologies, including broad perturbations on the cleanest 5% of spectra, and the manuscript does not demonstrate that their recovery threshold is identical to the production catalog threshold. The same DESI cut flags 52.8% of the nominal OOD sample versus 0.87% of the production stream, a 61-fold calibration failure that is labeled a “curation effect” rather than resolved. No representative false-positive estimate, blinded validation set, or catalog-wide precision/completeness assessment is provided.

[MAJOR] §II A–B and §VI C–D — the dominant spectroscopic catalog is insufficiently robust to preprocessing and model choice. Spectra are downsampled by a factor of 16, normalized per spectrum, and scored with an unweighted MSE that ignores wavelength-dependent uncertainties, masks, covariance, and known calibration structure. The authors’ own injection results show that narrow lines require at least 15σ while broad continuum deformations are readily selected. No independent model family or even a simple PCA/robust-reconstruction baseline is applied to DESI, SDSS, or LAMOST. The result is therefore a ranking of residuals specific to this preprocessing and architecture, not a validated general anomaly catalog.

[MAJOR] §III C, Table IV, Fig. 4, and Conclusion item 3 — cross-transfer and native SDSS populations are conflated. The UMAP/HDBSCAN clusters, the 84% cool-dwarf statement, and Table IV are explicitly computed from the DESI-trained cross-transfer set. The released Path-C tier is a native-retrained set whose cardinality was deliberately forced to the same value, 77,905. No membership overlap between the two sets is reported. Equal cardinality does not permit physical classifications derived from the cross-transfer population to be attributed to the native catalog, yet the manuscript repeatedly does so.

[MAJOR] §III F, Table I, and Table VII — the Planck tier does not meet the claimed validation standard. The released 200 patches are the top 200 of a 200,000-patch bank, which is 0.10%, not the “top 1%” stated in Table I. The count is inherited from the earlier 20,000-patch scan rather than selected from the native score distribution. The model is scored on its training patches, with 152 of the top 200 in the training partition; the claimed held-out enrichment significance assumes independent Bernoulli trials even though 10° patches from one sky map overlap and are spatially correlated. Moreover, a 5″ deduplication of patch centers cannot determine whether 10° sky regions are independent or substantially overlapping. Recovery of conspicuous Gaussian bumps added after per-patch standardization is not sufficient validation of CMB anomalies against foregrounds, beam effects, anisotropic noise, and scanning systematics.

[MAJOR] §III H — the NEOWISE component cannot be designated “validated.” The injection test places synthetic positions outside the ecliptic mask and then checks that the same deterministic mask rejects them; 100% recovery is guaranteed by construction and provides no information about detector sensitivity or catalog purity. The feature scaler is fit on the full sample, the train-only-scaler robustness test remains unperformed, and the origin and selection function of the restricted 43,518-source parent sample are not adequately specified. This tier is exploratory, not catalog-grade.

[MAJOR] §IV A–C — the novelty, spatial-systematics, and cross-survey-validation claims are not supported by the stated tests. Absence from 18 catalogs is an unmatched-catalog fraction, not “genuine novelty,” especially when most DESI entries may be sky or filler fibers; no visual or spectroscopic confirmation of the 178 unmatched cases is supplied. The Galactic-latitude and dust tests do not divide anomaly counts by the corresponding parent-survey source density, so they are not tests of anomaly rate. The random-coincidence estimate for the 637 cross-survey clusters relies on approximate footprints and RA-only shifts that the authors acknowledge are not geometry preserving. A uniform 5″ association radius is also inappropriate across subarcsecond optical positions, NEOWISE sources, and degree-scale CMB patches. These analyses cannot establish that the observed associations or spatial nulls are astrophysical.

[MAJOR] Data Availability, §II B, §III E–G, and §VI D — the end-to-end reproducibility claim is contradicted by the manuscript’s own provenance record. The public release and Zenodo DOI remain future commitments; the DOI is still a placeholder. The DESI full held-out reinference is blocked by missing native score products, the Planck checkpoint and patch tensor are reported to reside on an exited node, the NEOWISE derived feature table is unavailable for the required scaler test, the eROSITA production score axis is irrecoverable, and the initially retained Gaia output was synthetic. Deduplicating committed membership lists is not equivalent to reproducing the data acquisition, preprocessing, training, scoring, thresholding, and validation chain. Given the documented provenance failures, the retained tiers require independent end-to-end reproduction before publication.

[MAJOR] §V and Appendix C — the f
NL
	​

 forecast is not a valid inference from the catalog. The measured angular clustering ratio is obtained from a QSO-candidate sample with no redshift cut and is defined relative to the full anomaly sample, not demonstrably relative to the standard tracer entering the Fisher model. The conversion F=F
0
	​

+cα
2
, the clipping of negative α, and the estimator max(0,
α
^
2
−σ
α
2
	​

) do not constitute a likelihood or posterior propagation. The reported “1σ envelope” is therefore not an uncertainty interval. The bias measurement uses 5,384 objects, Fig. 9 uses a distinct 40,192-object tracer population, and Appendix C introduces yet another Fisher normalization. The necessary n(z), survey window, covariance, shot noise, tracer overlap, and systematic model are not provided consistently. This section requires a new analysis, not revision of wording.

[MAJOR] §V A, Appendix E, and journal scope — the NANOGrav calculation is disconnected from the anomaly catalog and does not support a PRD-level physics conclusion. The manuscript does not demonstrate that the per-bin free-spectrum posterior KDEs were converted into likelihoods by dividing out their sampling priors, and it discards inter-bin covariance. The Bayes factor against γ=4.33 is determined by a KDE estimate far in the posterior tail, yet no bandwidth or likelihood-construction robustness test is presented. Comparing only with a fixed circular-SMBHB index is not a comparison with the astrophysical SMBHB model class, as the manuscript itself concedes. This calculation uses none of the anomaly catalog and should not be presented as its cosmological application. Once the unsupported f
NL
	​

 and NANOGrav sections are removed, the submission is principally an astronomical catalog-engineering paper rather than a Physical Review D physics result.

[MINOR] Throughout — the manuscript requires a complete numerical and editorial consistency audit. Examples include the Planck “top 1%” versus 0.10% contradiction, 195,829 versus 195,790 DESI entries, the 235/400 “top-100 of three surveys” aggregate whose denominator comes from four surveys and whose text both includes and excludes Gaia, duplicate “single architecture” limitations, the incorrect statement that positive spatial correlations inflate rather than reduce the effective sample size, and repeated use of “5σ” both for standardized reconstruction-score units and for injected signal amplitude.

(3) The central claim that the manuscript provides a validated, catalog-grade set of 268,519 unique anomaly candidates is not supported by the evidence presented because the membership is assembled from arbitrary heterogeneous cuts and lacks established source identity, purity, selection functions, and end-to-end reproducibility.
