# EXT21 P3 Gemini — chat: https://gemini.google.com/u/1/app/731dc3a25b127584

Recommendation: MINOR REVISIONS

Review of "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches"

Overview and Summary

This paper presents an exceptionally large-scale unsupervised anomaly detection campaign using the BIGAE (BigBounce Integrated Galaxy Autoencoder) framework across seven major astronomical archives. The author processes 37.3 million objects from photometric, spectroscopic, and cosmic microwave background (CMB) datasets. Following a multi-step "Path-C" native retraining protocol and a 5-arcsecond positional deduplication, the work establishes a canonical catalog of 378,280 unique anomalies. This is broken down into 378,080 point sources and 200 Planck CMB map patches.

Beyond catalog generation, the manuscript explores downstream applications, evaluating the genuine novelty fraction of the top DESI anomalies via deep multi-catalog cross-matching, performing an angular two-point bias analysis on a high-redshift quasar (QSO) candidate sample to constrain primordial non-Gaussianity (fNL), and fitting a matter-bounce power-law template to the NANOGrav 15-year gravitational-wave background (GWB) data.

General Evaluation

This manuscript represents a major computational and methodological feat. Applying machine learning anomaly detection uniformly across heterogeneous multi-survey datasets is notoriously difficult due to domain shifts, selection effects, and data quality variations.

The paper is braced by a commendable level of transparency. The author openly documents data retrieval losses, unrecovered production scripts, and an irreproducible scoring axis for the eROSITA subset. Rather than sweeping these pipeline irregularities under the rug, the author quantifies their impact, establishes rigorous workarounds (e.g., treating the eROSITA top-298 list as canonically membership-only), and extracts valuable open-source machine learning lessons for the broader astronomical community.

The catalog holds significant value as a community discovery engine. The paper is well within the scope of MNRAS, and I recommend it for publication after a few minor revisions and clarifications are addressed.

Major Comments

1. Provenance, Reproducibility, and Data Safety

The disclosure that the eROSITA SBigAE scoring axis is non-reproducible due to an uncommitted post-hoc rescaling step is a serious concern for a catalog paper. However, the author expertly mitigates this by providing the exact raw score artifact and shifting the analytical framework to a canonical, reproducible n=298 membership list. The text must include a prominent, explicit warning in the Abstract or the Data Availability section advising downstream users not to perform score-weighted stacking or threshold re-derivations using the published production scores.

Similarly, for the Gaia DR3 tier, the production preprocessing script was lost and its properties are lineage-inferred. The author states that rankings are "best-available rather than fully reproducible." Please explicitly list the exact 20 features used in the final table or README to ensure future workers can approximate the inputs as closely as possible.

2. Clearer Dissection of the DESI Stream vs. Science Targets

The text notes a sharp definition split regarding the DESI dataset: the raw scan flags 195,829 anomalies (0.87% of the full 22.5 million spectra stream). However, a positional recount reveals that only 2,468 clusters (1.3%) actually coincide with primary main-survey science targets. The remaining ~98.7% fall on sky fibers, secondary targets, or filler spectra.

This is a critical nuance. While the full-stream scan is valid as an exhaustive exploration of "everything DESI pointed a fiber at," it means the massive size increase (~141× prior catalogs) is highly driven by unclassified or engineering exposures. The text should ensure that readers are structurally cautioned against directly comparing the full-stream rate definition with target-class restricted catalogs in prior literature without this target-filtering context.

3. The Value of the LAMOST "Failure Mode"

Section VI.A provides an excellent methodological lesson on training bias. Discovering that 98% of the initial cross-transfer LAMOST anomalies were a blue-excess training artifact highlights why single-survey machine learning catalogs can be fragile. The inclusion of this exploratory tier and the subsequent 21.5× rate reduction after native retraining is a highly valuable result that should be highlighted as a key architectural takeaway.

Minor and Technical Points

- Nomenclature Calibration: The decision to explicitly separate the anomaly score symbol S from spectroscopic redshift z to avoid statistical ambiguity is highly appreciated. It keeps the statistical text highly scannable.

- NEOWISE Masking Sanity Check: In Section III.H, the author notes that the NEOWISE injection-recovery test passes at 100% by construction because it plants synthetic sources outside the ecliptic-pole mask boundary and checks if they are filtered. The text rightly defines this as a quality assurance check for mask geometry implementation rather than an independent measure of the detector's sensitivity to physical features. This distinction should be carefully preserved in the summary tables so readers do not conflate it with the SDSS or Planck sensitivity tests.

- NANOGrav Prior Sensitivity: In Appendix E, the author notes that the Savage-Dickey Bayes factor comparing the matter-bounce model against an idealized circular-orbit SMBHB model (BMB/SMBHB = 7.14×10³) is highly prior-sensitive. It drops to ≈200 under a narrow, data-centered prior. Since the core SMBHB reference value (γ = 4.33) sits in the exponentially suppressed tail of the posterior, the text accurately concludes that this factor is decisive only against the idealized circular-orbit framework, while environmentally modified SMBHBs remain consistent with the recovered γ = 2.567 ± 0.382. This balanced stance is appropriate and prevents over-interpreting the result as an unambiguous cosmological detection.

- Data Scale Clarification: In Table I, the totals are clearly broken out into the initial cross-transfer baseline and the primary Path-C native-retrained catalog. The clarifying note that the total-row rates are accounting metrics rather than intrinsic physical anomaly frequencies is well-taken and helps protect against misquotation.

Summary of Recommendation

This paper is highly innovative, mathematically rigorous, and exceptionally transparent about its real-world engineering constraints. Addressing the data preservation warnings noted above will finalize this manuscript to the high standard expected for publication in MNRAS. No further extensive review cycles should be necessary.
