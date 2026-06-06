# P3 auto-2026-06-05_1717pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 370.9s

---

Meta-review: unseen issues and blind spots

P3-META-E1
- Severity: ESSENTIAL
- Section + page: §II.B (definition of S), p. 2–3; Table I footnotes, p. 7; §III.C–D, p. 6
- Why others missed it: Reviewers flagged Planck/NEOWISE score ambiguity, but not the internal impossibility of the reported “top-1%” S thresholds under the paper’s own z-score definition.
- Specific problem: The paper states “Throughout this paper, ‘S’ refers without exception to the per-survey standardized (‘z-scored’) reconstruction residual” (Eq. (2)). Yet the SDSS native re-score uses “top-77,905 at S ≥ 0.1060” and LAMOST native uses “top-113,342 at S ≥ 0.4613” as “top‑1% slices.” For a z-scored variable, the 99th percentile is ≈2.33, not 0.106 or 0.461. eROSITA’s headline cut “S > 0.259” (also called “score-knee”) has the same problem.
- Required fix: Audit and correct all per-survey S thresholds. Either (a) show the actual per-survey z-score distributions and report 99th-percentile values near 2.33, or (b) admit that the quoted quantities are not z-scores and rename them (e.g., raw-MSE, rescaled MSE), providing their precise definitions. Do not call a threshold “top-1%” on a z-score axis if its numeric value is inconsistent with a z-score distribution.

P3-META-E2
- Severity: ESSENTIAL
- Section + page: §II.B (DESI S-definition detail), p. 2–3
- Why others missed it: Focus was on the Fisher error; nobody audited the internal logic of how σval is set.
- Specific problem: “For DESI DR1, μval ≈ 0.0287 … and σval is set such that the S > 5 catalog threshold corresponds to MSE ≈ 0.143.” In a z-score, σval must be empirically measured on the validation set, not “set such that” a chosen threshold maps to a desired MSE. This undercuts the very definition of S as a standardized statistic.
- Required fix: Replace the “set such that” construction with the actual measured σval from the held-out validation split, and then derive the implied MSE threshold (report both μval, σval, and the resulting MSE at S=5). If the paper intended to anchor S to a fixed MSE threshold, drop the “z-scored” language and re-define S transparently as an affine rescaling.

P3-META-E3
- Severity: ESSENTIAL
- Section + page: §II.A–B (inputs and loss), pp. 2–3; §III.E–H (photometric/cat surveys), pp. 6–8
- Why others missed it: Attention centered on thresholds and rates; no one interrogated feature scaling in the MSE loss.
- Specific problem: The per-element MSE is computed over heterogeneous catalog features (eROSITA: 47, Gaia: 20, NEOWISE: 15) with no description of feature standardization. Without per-feature normalization (e.g., zero-mean, unit-variance), MSE is dominated by numerically large-scale features, making “anomaly” scores ill-defined and unreproducible. The same applies to spectra: the paper does not define flux normalization (continuum normalization, error weighting, per-arm scaling).
- Required fix: Document preprocessing for every survey: per-feature standardization method (mean/variance or robust scaler), units and transforms (logs, colors), and for spectra, flux normalization and whether per-pixel uncertainties were used to weight the loss. Provide an ablation/sensitivity test showing that anomaly rankings are stable to reasonable changes in feature scaling.

P3-META-E4
- Severity: MAJOR
- Section + page: §II.B and Appendix B, pp. 2–3, 15
- Why others missed it: Per-band “dominance” was treated descriptively; no one checked for normalization bias.
- Specific problem: The per-arm residuals rB, rR, rZ are computed over wavelength subsets of unequal lengths (B covers the longest interval, Z the shortest). If r• are not normalized by the number of bins per arm, “dominance” is biased toward arms with more bins. The method does not state any such normalization.
- Required fix: Define rB, rR, rZ as mean per-pixel residuals (i.e., normalize by bin count in each arm) or otherwise justify the weighting. Recompute the per-arm dominance fractions under a normalized definition and update any conclusions that rely on these labels.

P3-META-E5
- Severity: MAJOR
- Section + page: §II.D Step 6; §IV.C, pp. 3, 10
- Why others missed it: Matching radius concern was raised, but epoch/proper-motion was not.
- Specific problem: 7-way positional deduplication is performed at a fixed 5″ without any correction for epoch differences or proper motions (e.g., Gaia epoch ≈ 2016 vs NEOWISE ≈ 2014.5, DESI/SDSS earlier epochs). High–proper-motion stars can move >5″ over survey baselines, producing false non-matches or incorrect merges.
- Required fix: Propagate Gaia positions to the epochs of the other surveys before cross-matching, and quantify how many pairs change status when epoch propagation is applied. Provide an upper bound for missed/false merges due to proper motion, or adopt a probabilistic match that incorporates proper-motion uncertainties.

P3-META-E6
- Severity: MAJOR
- Section + page: §II.C (GPU inference pipeline) vs. Table V, pp. 3, 15
- Why others missed it: Training-time implausibility was flagged, but not the wall-clock inconsistency across sections.
- Specific problem: The text claims “total processing time…≈ 42 hours,” dominated by DESI (19,705 s ≈ 5.5 h) and LAMOST (no time given), with “CMB and photometric surveys each < 10 s.” Using the stated throughputs in Table V, the sum of inference times across DESI (~5.5 h), LAMOST (~3.3 h), SDSS (~0.6 h), and others (~minutes) is ≈10 hours, not 42. The 4× disparity is unexplained.
- Required fix: Provide a reconciled wall-clock breakdown—preprocessing, I/O, training time per survey (epochs), and inference—so that 42 h can be reproduced. If 42 h included training and CPU preprocessing, state and quantify those components explicitly.

P3-META-E7
- Severity: MAJOR
- Section + page: §V (QSO-candidate multi-tracer sample), p. 10
- Why others missed it: Reviewers focused on LS estimator details; the upstream sample definition was not scrutinized.
- Specific problem: The paper reports an α measurement for a “5,384 QSO‑candidate sample,” but never defines how the anomaly catalog is converted into QSO candidates (selection features, thresholds, redshift cuts, star/galaxy separation, AGN diagnostics). Without a reproducible selection, the αjk result is not auditable.
- Required fix: Describe the QSO-candidate selection in full: features (e.g., emission-line flags, colors), cuts, redshift range, masking, and checks against known QSO catalogs. Provide a table listing sample sizes after each cut and a machine-readable list of the 5,384 objects.

P3-META-E8
- Severity: MAJOR
- Section + page: §II.A–B, §III.A–C, pp. 2–6
- Why others missed it: The community expects observed-frame analyses; the redshift–anomaly entanglement was not examined.
- Specific problem: Spectra are analyzed in observed-frame wavelength. Without rest-framing or conditioning on redshift, redshift itself can drive reconstruction residuals (e.g., “Z-dominant high-z” objects), making high-z a de facto anomaly signature rather than astrophysical novelty. There is no test for “score vs. redshift” on the mainstream sample.
- Required fix: Report S vs. pipeline redshift for a stratified random subsample, and/or repeat the analysis with rest-frame normalization (or a conditional AE with z as input) to show that the anomaly signal is not merely redshift-driven. If high-z is intended as part of the anomaly signature, state this explicitly and adjust the interpretation.

P3-META-E9
- Severity: MAJOR
- Section + page: §II.D Step 5 (injection–recovery), §III.F–H, pp. 3, 6–8
- Why others missed it: They questioned pass/fail status but not the definition of “σ” for injections.
- Specific problem: The injection amplitude is given in “multiples of local noise σ,” yet there is no definition of σ for spectra (per-pixel variance from pipelines? smoothed estimates?) or for CMB patches (map-space noise model). Without this, a “5σ” plant is undefined and unreproducible.
- Required fix: Define σ precisely per survey (source of uncertainties, any smoothing/windowing, how σ is aggregated over injected regions), and publish the planting scripts/parameters. Include validation plots showing injected-vs-recovered distributions at each amplitude.

P3-META-E10
- Severity: MAJOR
- Section + page: §II.D Step 5; §III.H, pp. 3, 8
- Why others missed it: The mask sanity-check result (100% recovery) was accepted at face value.
- Specific problem: NEOWISE “mask injection–recovery” is used as a gate-equivalent PASS (1000/1000). But treating a geometric mask-veto as an “injection–recovery” test of an anomaly detector conflates systematic-cleaning with detector sensitivity; it is not comparable to signal injections in the other surveys.
- Required fix: Replace the NEOWISE “mask injection” with a substantive anomaly-signal injection appropriate for IR photometry (e.g., synthetic color/variability outliers) and report 5σ recovery under that protocol. Keep the mask analysis as a separate systematics check, not a substitute for injection–recovery.

P3-META-E11
- Severity: MINOR
- Section + page: Introduction and citations, pp. 1–2; refs [13,14,35], p. 19
- Why others missed it: The numerical fNL value was accepted; the reference provenance was not cross-checked.
- Specific problem: The claim “the quasi-matter bounce model predicts fNL = −35/8” is cited to [13,14,35], but [13] (Wands 2010) is an inflation review and not a primary source for the bounce fNL prediction. This weakens the provenance of the central cosmological motivation.
- Required fix: Cite a primary derivation of fNL = −35/8 within the matter-bounce framework (e.g., Cai et al. 2009 JCAP 0905:011) and keep [13] as a general background reference only, or remove it from the predictive citation list.

P3-META-m12
- Severity: MINOR
- Section + page: §IV.A (“genuine novelty fraction”), p. 9; Abstract p. 1
- Why others missed it: They requested protocol detail; none asked for uncertainty on the point estimate.
- Specific problem: The 17.8% “genuine novelty” fraction for the top‑1,000 DESI anomalies is reported with no uncertainty. A simple binomial 95% CI (Wilson) should accompany such a headline percentage.
- Required fix: Add binomial confidence intervals (e.g., 17.8% [95% CI: x–y%]) and state explicitly that this applies to the top-1,000 stratum, not the full catalog.

P3-META-m13
- Severity: MINOR
- Section + page: §IV.C (duplicates), p. 10
- Why others missed it: They checked total compression but not intra-survey provenance.
- Specific problem: The paper reports “9,576 intra-survey duplicates” collapsed at 5″ but does not apportion them by survey. Given per-survey data models (e.g., DESI coadds vs. exposures), this number needs context to be plausible.
- Required fix: Provide a breakdown of intra-survey duplicates by survey and a sentence explaining the sources (repeat observations, blended sources, variable-star multiplets, etc.).


## Meta-review recommendation
MAJOR REVISIONS

Given the union of all six reviews, there are multiple essential errors and ambiguities that block acceptance: the Fisher F0 misdefinition, inconsistent/incorrect improvement percentages, unresolved figure references, non-reproducible novelty and LS-bias protocols, unrealistic training/processing timings, ambiguous score definitions across surveys, and, additionally from this meta-review, fundamental contradictions in the definition and numerical use of the z-scored anomaly measure S, lack of feature-scaling documentation, per-band normalization bias, unmodeled proper-motion in cross-matching, and misuse of a mask test as an injection-recovery gate. I count at least 10 essential/major blockers across reviews. Confidence that the paper would survive external peer review after addressing all items is medium: the core dataset is valuable, but the methodological/expository issues are substantial and must be corrected with precise, auditable documentation and consistent definitions.