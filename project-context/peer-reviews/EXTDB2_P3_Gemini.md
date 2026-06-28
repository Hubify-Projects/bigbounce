# EXTDB2 P3 Gemini — chat: https://gemini.google.com/u/0/app/0b65c78f2b735200

Provider: Gemini Flash
PDF md5: d3d662cb8d0c737032580465397911f2
Harvested: 2026-06-28

---

Referee Report
Manuscript Title: Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 269,317 Recommended-Tier (378,280 Total) Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches
Author: Houston Golden (Independent Researcher)
Date of Review: June 28, 2026

1. Recommendation
MAJOR REVISIONS

The manuscript details an impressive computational and methodological effort. The scale of the work is commendable, and the author demonstrates robust scientific integrity by shifting from a flawed "cross-transfer" framework to a survey-native retraining pipeline ("Path-C"). However, several critical bookkeeping discrepancies, unmodeled selection effects, and misleading messaging choices regarding novelty rates and cosmological constraints prevent publication in its current form.

2. BLOCKERS
None. (The manuscript contains significant issues but none that represent structural or fatal scientific fraud/irreparable damage that would trigger an immediate REJECT.)

3. MAJORS

Major 1 — DESI Core Population Inconsistency: In the introduction and abstract, the DESI pipeline is framed as a massive expansion over the Liang et al. [11] benchmark (~73x increase in the full-stream scan). However, the spatial and target-type recount in §III A reveals that ~98.7% of the DESI anomaly clusters fall on sky-fibers, filler tiles, or calibration exposures. When strictly restricted to validated science targets, the catalog yields 2,468 clusters—≈0.9× the size of the Liang et al. benchmark. The author must rewrite the abstract, introduction, and conclusions to clarify that this is a scan of everything a fiber was pointed at, and transparently soften the "73x size increase" marketing.

Major 2 — Unmodeled Spatial Selection Functions: The spatial uniformity test yields a highly non-uniform distribution (χ²=376,713 for 24,048 degrees of freedom). While the author correctly points out this is dominated by inhomogeneous footprint geometries, the paper draws cosmological applications from these tracer reservoirs. Drawing Fisher forecasts or claiming spatial latitude null results without mapping the angular selection functions, completeness maps, and per-tile fiber collision targeting weights introduces severe systematic vulnerabilities.

Major 3 — Overstating Novelty in Visuals: Figure 6 and Table I prominently highlight the "SIMBAD-unmatched fraction" (e.g., ~99% for DESI, 90% for SDSS). However, §IV A explicitly states that this metric vastly overstates catalog novelty due to database indexing limits, and that the deep multi-catalog cross-match via CDS X-Match yields a genuine novelty fraction of only 17.8%. The author is engaging in double-presentation: leading with a flashy ~99% metric while burying the real 17.8% figure in prose. Figure 6 should either be updated to focus on the 17.8% genuine novelty fraction or explicitly titled "Database Incompleteness Mapping."

Major 4 — Noise Bias in Fisher Forecast Reporting: In §V and §VII, the central forecast of σ(fNL)=8.14 is presented as a 9.4% improvement over the standard baseline. Yet, the author admits that inserting the noisy α̂_jk into a convex mapping introduces a squaring noise bias (E[α̂²]=α²+Var(α̂)). The de-biased point estimate returns exactly zero improvement. Elevating the 9.4% improvement to headline status while the true de-biased result shows no multi-tracer improvement is a selective presentation choice that must be corrected.

Major 5 — Irreproducible eROSITA Anomaly Axis: The author acknowledges that the published eROSITA threshold (0.259) and individual S_BigAE scores cannot be reproduced from any committed artifact or monotone rescaling due to an undocumented post-hoc step. For a data-release publication, releasing a component where the primary score axis is unrecoverable is unacceptable. Must either re-score using fully documented committed raw artifact pipeline or clearly downgrade eROSITA section to reflect "membership-only" status.

4. MINORS

Minor 1 — Data Footprint Discrepancy: Table I lists total processed sample as 37,292,042 (cross-transfer) or 37,272,042 (Path-C). The title claims 37.3 million sources. Round consistently or explain the explicit definition of the headline denominator.

Minor 2 — SDSS Filtering Metadata Drop: Section III C states 3,394 SDSS spectra failed retrieval during the re-scoring pass. Author needs to state whether these missing objects could systematically impact the top-1% score-knee threshold cuts (S≥0.2051).

Minor 3 — Data Leakage vs. Hold-out Validation: For the Planck CMB native convolutional autoencoder, 152 of the top-200 anomalies were found to belong to the training split. While the author proves via a spatial binomial test this is likely driven by spatial boundary-region power correlations rather than memorization leakage (p≈4×10^{-4}), future workflows should explicitly filter training data out of anomaly catalogs. This distinction should be explicitly added as a warning in the data-availability section.

5. Strengths

1. Rigorous Analytical Self-Correction: The transition from the initial cross-transfer architecture to the survey-specific native retraining loop ("Path-C") shows exceptional methodological rigor. Detecting that 98% of cross-transfer LAMOST anomalies were blue-excess artifacts and compressing this bias by 21.5x via native-retrain control serves as a phenomenal case study for the machine learning community.

2. Exemplary Deterministic Resiliency: Staging inference dynamically, using checkpoints at HEALPix/plate boundaries, and logging pod provisions ensures high computational reproducibility despite encountering unexpected physical disruptions (such as the 11-hour network-induced SDSS pod restart).

3. High-Value Candidate Discovery: Despite filtering caveats, the pipeline successfully uncovers genuine physical anomalies, such as the uncataloged BAL QSO at z≈0.86 confirmed across both DESI and SDSS epochs, and the highly variable TIC 374313355. This proves the immense value of the catalog as an exploratory community engine.
