# EXTDB P3 Gemini — chat: https://gemini.google.com/u/0/app/81b0c544ffc40432

Provider: Gemini
Model/Tier: Flash (regular)
PDF: /tmp/EXTDB_P3.pdf
Submitted: 2026-06-27
Harvested: 2026-06-27
Round: EXTDB (DE-BIASED)

---

Referee Report (MNRAS / PRD / JCAP)

1. Recommendation
MAJOR REVISIONS

2. Summary of the Work
This manuscript presents a massive multi-survey astronomical anomaly detection framework applying the deterministic "BIGAE" autoencoder architecture across 37.3 million sources spanning seven major archives (DESI DR1, SDSS DR18, LAMOST DR10, eROSITA DR1, Planck, Gaia DR3, and NEOWISE). By transitioning from initial cross-survey model transfers to a "Path-C" native-retraining rebuild, the author compiles a catalog of 378,280 unique anomalies. The work also attempts downstream cosmological applications, utilizing anomaly-detected high-redshift QSO candidates to probe primordial non-Gaussianity (fNL) and cross-referencing matter-bounce predictions against NANOGrav 15-year pulsar timing data.

3. BLOCKERS

B1 — Irreproducible Anomaly Scores and Axis Mismatch in the eROSITA Tier.
The author explicitly flags that the published per-object S_BigAE score axis for eROSITA DR1 cannot be reproduced under any of 16 monotone rescalings or Isolation Forest retrains. The production threshold of 0.259 contradicts the actual raw threshold of 3.41 found in the committed artifacts. An unrecoverable, undocumented post-hoc scaling step means downstream users cannot perform score-weighted stacking or axis re-derivations. Releasing a static membership list is insufficient for a peer-reviewed data catalog when the underlying scoring function is fundamentally non-reproducible.

B2 — Invalidated Detector Sensitivity in the NEOWISE Injection-Recovery Gate.
The manuscript lists NEOWISE as one of the "3 PASS" surveys under the injection-recovery validation protocol. However, Section III.H reveals that this test merely planted synthetic sources within the ecliptic polar cap (|becl| > 80°) and "recovered" them by applying the fixed catalog geometric mask (|becl| < 80°). This is a software quality assurance check on masking geometry, not an actual detector-sensitivity test. Grouping it as a completed sensitivity pass is scientifically invalid.

B3 — Unquantified Completeness in Exploratory Tiers.
Three major surveys failed the standard 50% injection-recovery gate at 5σ: LAMOST (5.8%), Gaia (5.2%), and eROSITA (1.2%). Releasing massive tiers (~113,000 objects for LAMOST) where the pipeline's true sensitivity to anomalies is effectively zero or untracked is a major blocker for systematic scientific utilization.

4. MAJORS

M1 — Pervasive Training-Sample and Selection Conditioning in Gaia DR3.
The 100-tree Isolation Forest cross-validation refit on an expanded Gaia sample yielded a stability metric of only 41.0%. This proves that over half of the published Gaia anomaly selections are intensely conditioned on the localized training sample split rather than tracing robust physical outliers. The survey tier should be explicitly stripped of its "catalog-grade" baseline until a dedicated, cross-validated run is completed.

M2 — Definitional Recount Discrepancies in DESI Focus.
The headline frames the DESI-only subset as a massive ~73× scale increase over the prior Liang et al. benchmark. Yet a strict science-class target recount reveals that only 2,468 DESI clusters fall on validated primary science spectra, while ~98.7% fall on unclassified filler or sky fibers. When restricted like-for-like, the catalog is actually slightly smaller (≈0.9×) than the prior benchmark. Headlining the full raw data stream count without prominently placing this order-of-magnitude physical target drop in the main text is highly misleading.

M3 — Lack of True Independence in Isolation Forest Validation.
The Isolation Forest was trained directly on the 16-dimensional BIGAE latent features rather than raw catalog properties, making the two models highly dependent. Framing this as an objective validation cross-check overstates the statistical significance of the match.

5. MINORS

m1 — Validation Data Leakage in Feature Preprocessing Scaling. For the tabular catalogs (eROSITA, NEOWISE, Gaia), the feature standardization statistics were fit across the full sample rather than strictly on the training split. This introduces forward data leakage.

m2 — Blue-Arm Calibration Artifact Contamination. Over 44,000 DESI anomalies (22.7%) are flagged as purely "B-dominant," consistent with an instrumental calibration artifact. Downstream users require a definitive cross-match strategy.

m3 — Non-Representative Score Normalization Explaining Extreme SDSS Ranges. Figure 3 (Right) displays an SDSS transfer-learning score extension stretching down to S≈1.9×10^11. The text should clarify this is an artificial inflation caused by cross-survey domain shift.

m4 — Uncertainty Overestimation in Multi-Tracer fNL Central Forecast. The central multi-tracer forecast claiming a 9.4% improvement (σ(fNL)=8.14) is heavily affected by squaring noise bias. The de-biased point estimate returns exactly zero improvement (σ(fNL)=8.98). The abstract and conclusion text must lead directly with the de-biased flat constraint.

6. Strengths

1. Unprecedented Multi-Archive Scale: The consolidation and processing of 37.3 million separate sources across distinct spectro-photometric sky footprints represent an extraordinary technical hurdle successfully cleared by the BIGAE pipeline.
2. Rigorous Post-Transfer Native Diagnostics: The identification and transparent documentation of the 98% blue-excess training bias in LAMOST, alongside the massive 6,500× rate compression in SDSS after native retraining, provide critical cautionary lessons for big-data unsupervised networks.
3. Astrometric Audit Completeness: The transitive friend-of-friends chain audit across all multi-member clusters effectively confirms that single-link cluster transitive bridging did not falsely distort the 7-way positional deduplication at 5″.
