VERDICT: REJECT

ISSUES:

[MAJOR] Abstract, §III, and Table II — the headline catalog size is analyst-defined rather than statistically measured. The 268,519 total includes 77,905 SDSS objects selected explicitly to preserve the earlier cross-transfer count, even though the native top-1% set contains 19,253 objects and the native S>5 set only 12; Planck and NEOWISE likewise contribute predetermined fixed-count or fixed-percentile selections. The claim of producing the largest validated anomaly catalog is therefore driven substantially by arbitrary quotas. The catalog must use pre-specified operating points calibrated for false-discovery rate, completeness, and purity, with validation performed at the exact released thresholds. 

ext_P3_W1

[MAJOR] Abstract, §II D, §III, and §VI D — “validated catalog-grade” is not established by the stated gates. Injection recovery measures sensitivity to selected synthetic perturbations, not the contamination or astrophysical reality of the unmodified catalog entries. No false-positive rate, null-sample rejection rate, blind expert classification, recovery of an independently labeled anomaly population, or independent model-family comparison is provided for the spectroscopic catalog. NEOWISE’s gate is guaranteed by the mask construction, DESI is certified only for one broad-feature morphology, and SDSS reaches 64% for one continuum-dip plant; these heterogeneous tests cannot support a common catalog-grade designation. 

ext_P3_W1

[MAJOR] §III A and the abstract — the DESI entries have not been shown to be point-source anomaly candidates. The manuscript reports that approximately 98.7% of DESI clusters lack a primary science-class target bit and that 86% have DESI_TARGET = 0, encompassing sky fibers and other non-primary observations, yet the abstract counts almost the entire validated catalog as point sources. A Redrock template label or positional catalog join does not by itself demonstrate that each spectrum corresponds to an astrophysical source rather than blank-sky, calibration, secondary-program, or reduction pathology. The non-object spectra must be separated and validated before a point-source count is quoted. 

ext_P3_W1

[MAJOR] §III A and Table III — the claimed “like-for-like” DESI benchmark is not reconciled. The stated class rates imply tens of thousands of anomaly spectra in the approximately 4.9-million GALAXY and 1.5-million QSO subsets, whereas the science-bit positional recount produces only 2,468 anomaly clusters. Invoking different filter stacks does not resolve this discrepancy without an object-level flow table showing multiplicities, rejected rows, and shared identifiers. Moreover, comparing 2,468 objects from a roughly 20.3-million-row DR1 selection with 2,685 objects from a roughly 250,000-spectrum EDR study, under different models and thresholds, is not a like-for-like performance comparison; rates at matched purity and completeness are required. 

ext_P3_W1

[MAJOR] §II A–B, §III C–D, and Table II — the released scoring pipeline is insufficiently and inconsistently specified. The manuscript does not fully state the layer widths, spectral interpolation and masking rules, treatment of inverse variance and bad pixels, training-sample construction, or all quality cuts needed to reproduce the spectroscopic scores. Table II describes SDSS and LAMOST as sharing the DESI-trained score scale while the methods and survey sections describe native per-survey models and native validation normalization. Prominent figures and taxonomies use historical cross-transfer samples while the headline catalog uses native rescoring. One unambiguous score definition and end-to-end pipeline must be given for every released tier. 

ext_P3_W1

[MAJOR] §II B and §VI D(i) — the held-out checks do not validate the released DESI production ranking. The released 22.5-million-spectrum catalog was scored with training spectra included, while the fold-stability calculations use deliberately short-trained proxy models whose mean best validation loss is 1.91 and which all fail the manuscript’s own 0.30 retention gate. No full held-out inference of the production ensemble is available, and applying the production threshold to an uncurated SPARCL sample flags more than 50% rather than 0.87%, demonstrating extreme dependence on catalog curation. Jaccard agreement among failed proxy models cannot replace out-of-sample validation of the released production scores. 

ext_P3_W1

[MAJOR] §III F and Table VII — the Planck tier is not a validated catalog of independent CMB regions. The top 200 are selected from a training-inclusive bank of potentially overlapping 10
∘
×10
∘
 patches, yet “uniqueness” is assessed using a 5-arcsecond center separation that is meaningless for regions of this size. The binomial held-out-enrichment calculation assumes independent patches despite acknowledged spatial correlation, and validation-set overrepresentation can arise simply from a train–validation reconstruction gap. In addition, the gate is evaluated at a 99th-percentile threshold while the released top 200 of 200,000 correspond to the 99.9th percentile. Independent nonoverlapping sky holdouts, end-to-end CMB-plus-noise-plus-foreground simulations, and region-scale deduplication are required. 

ext_P3_W1

[MAJOR] §IV A — the 17.8% “genuine novelty fraction” is not a discovery fraction. Absence from 18 catalogs does not establish that an entry is a previously unknown astrophysical object; it can result from incomplete footprint coverage, depth limits, masking, astrometric or proper-motion errors, source blending, fiber placement on blank sky, or cross-match failures. The paper does not provide catalog-by-catalog coverage and depth tests, forced-photometry checks, local false-negative estimates, or blind visual confirmation of the 178 objects. This quantity must be described as a multi-catalog unmatched fraction unless the candidates are individually validated. 

ext_P3_W1

[MAJOR] §IV C — the 637 cross-survey coincidences do not constitute the claimed cross-survey validation. The count includes the failed LAMOST exploratory tier, no complete survey-pair matrix is supplied, and the claimed random-coincidence expectation of at most approximately 10 is extrapolated largely from a non-geometry-preserving RA-shift test for one pair. The assertion that all other survey-pair contributions sum to less than one is not demonstrated from the masks and local source densities. Only three coincidences receive spectroscopic examination. Survey-specific astrometric uncertainties, geometry-preserving scrambled controls, and per-pair purity estimates are needed before these matches can be used as validation evidence. 

ext_P3_W1

[MAJOR] §V — the f
NL
	​

 forecast is not supported by the empirical bias measurement. An angular clustering ratio between the 5,384 QSO candidates and the full anomaly population cannot be interpreted as a linear-bias ratio without matched redshift distributions, angular selection functions, completeness, and contamination; the candidate sample explicitly has no redshift cut. The measured bias is then inserted into a phenomenological 1/σ
2
=F
0
	​

+cα
2
 fit whose Fisher inputs and covariance are not derived in the manuscript, while the reference figure uses a distinct 40,192-object redshift-binned tracer sample. The resulting envelope is not a posterior interval, and the truncated “de-biased” α
2
 estimate is not a substitute for marginalizing over bias uncertainty. This application requires a new, self-consistent forecast or should be removed. 

ext_P3_W1

[MAJOR] §V A and Appendix E — the NANOGrav analysis neither validates the catalog nor tests a physical matter-bounce model. It is entirely independent of the anomaly catalog and fits a generic two-parameter power law to factorized KDE free-spectrum products. The manuscript does not derive why the specific bounce realization predicts a pure γ=3 spectrum throughout the PTA band, connect the fitted amplitude to bounce parameters, or validate the KDE-tail Bayes factors against a full timing likelihood and bandwidth/covariance variations. The large ratio between two fixed spectral-index hypotheses is not evidence for bounce cosmology, particularly when realistic environmental SMBHB spectra are not included in the model comparison. This analysis should be separated into a dedicated study. 

ext_P3_W1

[MAJOR] Tables I–II, §II B–D, and Data Availability — the provenance and reproducibility claims are internally inconsistent. The retained-native body rows sum to 36,758,058 inputs, while the cross-transfer total is 37,292,042; the explicitly described Planck replacement and ACT scan account for only 200,000 of the 533,984 difference, leaving 333,984 inputs without an exact ledger. The manuscript simultaneously claims that every result is independently recomputable and states that production score parquets, the Planck checkpoint and tensor, some feature tables, and other pod-side products are unavailable or lost. A future release promise and repository-local paths are not reviewable evidence; a frozen public archive with an immutable DOI, hashes, exact input manifests, and executable end-to-end reproduction must exist before publication. 

ext_P3_W1

[MINOR] §III C, §IV B, and overall organization — several statistical and presentation claims should be moderated. The SDSS correlation ρ=0.036 is practically tiny despite its small p-value, and the statement that instrumental effects cannot generate a score–redshift trend ignores redshift-dependent target selection, signal-to-noise, line migration across spectrograph arms, and fit quality. The footprint-dominated spatial χ
2
 adds no interpretable result. More broadly, the manuscript combines a catalog paper, an f
NL
	​

 forecast, and an unrelated PTA analysis, with extensive repetition and implementation paths; these should be split and substantially streamlined. 

ext_P3_W1

No—the manuscript shows that its pipeline can rank reconstruction residuals, but it does not support the central claim that 268,519 entries constitute a validated, catalog-grade set of astrophysical anomaly candidates.
