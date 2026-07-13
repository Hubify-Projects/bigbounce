(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] §3.1, Table 3, and the headline “268,319 point-source anomalies”: The dominant DESI component is not demonstrated to be a source catalog. The manuscript reports that only 2,468 of 190,015 deduplicated DESI anomaly clusters match primary science-target bits, that approximately 98.7% lie on non-primary spectra, and that 86% have DESI_TARGET = 0. A mixture dominated by sky fibers, filler observations, calibration spectra, and uncharacterized secondary programs cannot be counted as unique point-source anomalies without first establishing which rows correspond to actual astrophysical sources. 

ext_P3A_M10

[MAJOR] §2.2 versus §3.3 and §6.4(i), DESI identifier provenance: The manuscript states that only 26,218 released DESI rows contain real TARGETIDs, that 169,611 contain internal hashes, and that only approximately 1.3% of released rows are re-pullable; it later states that all 195,790 primary-coadd anomalies join to the DR1 redshift catalog on TARGETID with 100% success. These statements are mutually incompatible unless an additional mapping exists, and no such released mapping is described. The dominant catalog tier therefore cannot be independently audited at the object level.

[MAJOR] Table 3, DESI science-target reconciliation: The reported GALAXY and QSO rates imply roughly 37,000 anomalies in the validated-TARGETTYPE subset, whereas the positional science-bit recount finds only 2,468 matches. The science-bit catalog is described as broader and as applying fewer quality restrictions, so the assertion that “different filter stacks” explain a factor of approximately 6–16 reduction is not credible. This discrepancy indicates a failure in identifier joining, sample definition, or both.

[MAJOR] §2.2 and §6.4(i), claimed held-out DESI validation: The five fold models each score the full 47,000-spectrum pool, meaning that most objects contributing to each top-set Jaccard comparison were used to train that particular model. Pairwise Jaccard overlap of those full-pool rankings is not fully out-of-fold validation of catalog membership. Moreover, the proxy fold models fail the manuscript’s own retention criterion, with mean best validation loss around 1.91 versus the stated threshold of 0.30. These tests cannot validate the production catalog.

[MAJOR] §6.4(i), DESI injection-recovery: The plants are inserted into the “cleanest 5%” substrate and evaluated against a tail-excluded 99th-percentile clean threshold whose equivalence to the production S>5 catalog selection is not demonstrated. The experiment covers selected broad spikes or continuum perturbations and measures sensitivity to those plants; it does not measure the false-positive rate, catalog purity, contamination by calibration residuals, or validity of existing catalog members. It cannot support the repeated statement that validation establishes that the catalog entries are “real.”

[MAJOR] §3.1 and §6.4(i), visual artifact bound: The inference from 0 visually flagged objects among the top 200 to a ≤1.5% artifact-contamination bound is invalid for the full 195,829-object DESI tier. The top 200 are a score-selected extreme, not a random sample, the inspection was not described as blinded or independently replicated, and the test addresses only a short list of artifact morphologies.

[MAJOR] §2.2, §3.1, and §6.3, reconstruction statistic: The unweighted MSE ignores the supplied per-pixel uncertainties, bad-pixel masks, arm-dependent calibration, and sky-subtraction variance. The manuscript itself identifies 44,436 B-dominant DESI anomalies as potentially calibration-driven and acknowledges that nearly all DESI clusters fall outside the primary science-target sample. Without noise-aware scoring or a convincing stratified artifact audit, the score is not sufficiently controlled for a catalog-grade claim.

[MAJOR] §3.3 and Table 2, SDSS selection: The 77,905-object SDSS tier is chosen solely to preserve the size of the obsolete cross-transfer result. The native top-1% selection contains 19,253 objects and the native S>5 selection contains only 12. A fixed-size “continuity slice” has no statistical or astrophysical justification, yet it supplies approximately 29% of the detections entering the validated headline. Consequently, the value 268,519 is substantially determined by an arbitrary cardinality choice.

[MAJOR] §3.8, NEOWISE validation: NEOWISE is included in the validated tier even though its only gate places synthetic positions outside the adopted latitude mask and then recovers them by applying that same mask. Passing is guaranteed by construction and tests neither the autoencoder nor anomaly sensitivity. The scaler is also fitted to the full sample, and the train-only-scaler robustness test is explicitly unfinished. NEOWISE must be classified as unvalidated or exploratory.

[MAJOR] §3.6 and Table 7, Planck patch independence: The top 200 are selected from 200,000 ten-degree patches drawn from one sky map, while training and scoring use the same patch bank. Patch overlap is neither quantified nor removed; with this number and patch size, strong spatial dependence is unavoidable. A five-arcsecond deduplication of patch centers does not turn overlapping ten-degree cutouts into independent sky regions.

[MAJOR] §3.6, Planck held-out statistic and injection test: The binomial calculation for 48 validation-split patches assumes independent trials despite spatially overlapping patches and shared underlying sky modes. Randomly assigning overlapping cutouts to training and validation sets is not a spatial holdout. The injected five-sigma Gaussian bump is added after per-patch normalization and is not re-normalized, making it an exceptionally conspicuous artificial feature rather than a realistic CMB, foreground, beam, or noise perturbation. The resulting 100% recovery does not validate the released Planck tier.

[MAJOR] Title, abstract, Tables 1–2, and the central aggregate count: The catalog unions non-equivalent units—individual spectra, tabular sources, and ten-degree CMB patches—selected with non-comparable score axes, arbitrary percentiles, a continuity cap, and different validation standards. Such lists may be released with explicit provenance flags, but their summed count and aggregate “rate” have no homogeneous scientific meaning. The quoted 37.3 million also combines retained inputs, historical processing passes, and subsequently excised products rather than a single set of unique catalog objects.

[MAJOR] §4.1, “17.8% genuine novelty”: Absence from 18 catalogs does not establish genuine novelty. This is especially serious because the DESI top-ranked population is dominated by non-primary and likely sky/filler positions, for which absence of an imaging counterpart is expected. The calculation does not condition on catalog footprint, depth, source type, target status, or positional uncertainty, and the 178 objects are not confirmed through imaging inspection or spectroscopy. The result is an unmatched-position fraction, not a discovery rate.

[MAJOR] §3.1 and §6.5, “like-for-like” comparison with Liang et al.: The 2,468 count is drawn from all primary DESI classes over a 20.3-million-row DR1 bitmask catalog, whereas the cited comparison is a DESI EDR Bright Galaxy Survey analysis of roughly 250,000 spectra with a different model, threshold, quality selection, and object accounting. Similar absolute counts from denominators differing by nearly two orders of magnitude are not a like-for-like performance comparison.

[MAJOR] §3.5, §3.7, and Data Availability, release integrity: The release description is internally inconsistent. The 377,482 total is repeatedly defined as including the LAMOST exploratory tier, but Data Availability says LAMOST is excluded from the released per-object tables and every headline count; Gaia is said to be removed from the released catalog, yet a released Gaia exploratory block is also described; and the eROSITA production score is unrecoverable. The paper also lacks a complete catalog-column specification covering identifiers, units, null values, score axes, validity flags, duplicate handling, and selection membership.

[MAJOR] End-to-end provenance: The irreproducible eROSITA score axis, synthetic Gaia fallback, loss of the DESI production inputs and identifier linkage, and inability to rescore nearly all released DESI rows are systemic production failures, not peripheral caveats. An author-conducted audit and reproducible deduplication of already selected lists do not replace an independent end-to-end regeneration of the retained tiers from public archive records.

[MAJOR] §4.3, cross-survey associations: The claim that 637 multi-survey clusters are genuine detections at more than 60 times the chance expectation is based on an RA-shift control that the manuscript concedes does not preserve footprint geometry, followed by an area rescaling and extrapolation to other survey pairs. No local-density model, survey mask, per-source astrometric covariance, or geometry-preserving random catalog is used. A probabilistic, survey-specific cross-match is required before these associations can be interpreted.

[MAJOR] §5, f
NL
	​

 application: An angular clustering amplitude for a photometric candidate sample without a measured redshift distribution cannot be inserted directly as the relative bias in a three-dimensional multi-tracer Fisher forecast. The 5,384-object bias sample is not shown to represent the distinct 40,192-object redshift-binned forecast population. Table 9’s linear dependence on α also conflicts with the manuscript’s adopted 1/σ
2
=F
0
	​

+cα
2
 form, and Figure 11 uses a separate absolute normalization. This section is not a reproducible cosmological forecast and should be removed or rebuilt as a separate analysis.

[MAJOR] §5.1, NANOGrav application: This analysis does not use the anomaly catalog and provides no evidence for the catalog’s central claim. Treating factorized free-spectrum posterior KDE products as the effective likelihood, and deriving decisive fixed-index Bayes factors from KDE tail densities, requires a dedicated validation of prior removal, KDE bandwidth, inter-bin covariance, and tail stability that is not presented. It belongs in a separate PTA paper.

[MINOR] Figures 2–4, 8, and 10: These figures prominently display obsolete cross-transfer results, quarantined ACT data, the removed synthetic Gaia curve, or non-catalog display scores. Despite lengthy captions, they obscure which products are actually released and validated. The main text should show native-model results and move historical failure demonstrations to an appendix.

[MINOR] Terminology throughout: “Five sigma,” “validated,” “real,” “genuine novelty,” “detection,” “point source,” and “catalog grade” are applied to different and sometimes incompatible quantities. A standardized reconstruction residual is not a Gaussian detection significance, and an injection amplitude is not the same quantity as the catalog score.

[MINOR] Organization: The manuscript repeatedly re-litigates count reconciliation, exclusions, and caveats in the abstract, introduction, tables, discussion, conclusions, and data statement, while omitting essential catalog documentation and direct validation plots. The historical cross-transfer narrative and unrelated cosmology material should be removed so that the paper can focus on sample construction, selection functions, quality control, and the machine-readable catalog.

(3) The central claim is not supported by the evidence presented: the headline catalog is dominated by unverified non-primary DESI spectra, depends on arbitrary or constructively passing selections, treats non-independent CMB patches as unique anomalies, and cannot be independently regenerated at the object level.
