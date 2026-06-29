# RCEXT P3 Gemini — chat: https://gemini.google.com/u/0/app/35ef8be8599472df
VERDICT: MAJOR REVISIONS

Provider: Gemini (Flash/regular)
PDF: RCEXT_P3.pdf (md5: f6b8d9a5e16fc5f4f3301433c9c556dc)
Harvested: 2026-06-29

---

Recommendation: MAJOR REVISIONS

1. Summary

This manuscript presents a massive multi-archive astronomical anomaly detection pipeline applying the BIGAE framework across 37.3 million sources spanning seven major surveys (DESI DR1, SDSS DR18, LAMOST DR10, eROSITA DR1, Planck, Gaia DR3, and NEOWISE). Following an initial cross-transfer evaluation, the author executes a "Path-C Rebuild" protocol utilizing native per-survey retraining and a positional deduplication scheme. Secondary sections attempt to leverage these high-bias tracers to constrain primordial non-Gaussianity and interpret the NANOGrav 15-year gravitational-wave background data.

2. Blockers (Crucial Architectural/Methodological Flaws)

Irreproducible and Non-Monotone eROSITA Score Axis: The author explicitly notes that the published eROSITA threshold (0.259) could not be reconciled with the canonical anomaly score S or any tested Isolation Forest metric across 16 monotone rescalings. Crucially, the production scores are non-monotone with respect to the committed raw reconstruction-score artifact (Spearman ρ=−0.10 for the top five). If the score axis is corrupted by an uncommitted post-hoc step, publishing these specific SBigAE values is scientifically invalid. Remedy: Re-score the eROSITA dataset entirely using the clean, documented raw pipeline, rebuild the top tier on a strictly reproducible monotone axis.

Methodological Leakage via Full-Sample Normalization Scalers: Tabular catalog data (eROSITA, NEOWISE, Gaia) are scaled using robust transforms fit on the full sample rather than exclusively on the training split. This introduces validation data leakage. The author's internal check reveals a ~15-17% extreme-tail membership churn when fixing this bug. Remedy: Normalization constants must be fit strictly on the training partition.

3. Majors

Inflated Headline Multipliers and Selection Framing: The abstract and conclusions lean heavily on a ~141× benchmark increase and a ~73× DESI full-stream multiplier. However, ~98.7% of the raw DESI anomalies fall on sky-fibers, filler tiles, or calibration spectra rather than legitimate science targets. On a like-for-like science-target basis, yields are ≈0.9× smaller than prior single-survey benchmarks. Remedy: The abstract and conclusions must be recast to prominently state the science-target comparison (≈0.9×) alongside the stream volume metrics.

Uncontrolled Selection Functions in Spatial Analysis: The spatial uniformity analysis yields χν²=15.7, dominated by inhomogeneous footprints. Reporting a raw spatial χ² statistic without accounting for angular selection functions provides no useful physical insight.

Over-Optimistic Central Fisher Forecast Tracking Noise Bias: The text highlights a central forecast of σ(fNL)=8.14 (a 9.4% improvement over the standard baseline of 8.98). However, because the Fisher mapping is convex in α, inserting the noisy point estimate (αjk=0.19±0.65) introduces an uncorrected squaring noise bias. The de-biased estimate yields exactly zero cosmological improvement. Remedy: The abstract and summary must clearly establish that current data limits show no statistical improvement on fNL bounds.

4. Minors

Guaranteed NEOWISE Validation Mockery: The NEOWISE mask injection test plants synthetic signals at |b_ecl|>80.5° and "recovers" them by applying the mask |b_ecl|<80°. Passing at 100% is mathematically guaranteed by construction and validates nothing about detector sensitivity.

DESI B-Dominant Systematic Hypothesis: 22.7% (44,436 sources) of the DESI anomalies are flagged as B-dominant, strongly pointing to a local instrumental calibration systematic in the blue arm. This should be prioritized or explicitly noted as a primary data caveat in the main text.

Acronym Ambiguity: Ensure that standard metrics (ECDF, probit, ESS) are explicitly defined at first mention.

5. Strengths

Scale and Scope: This work scales unsupervised autoencoder anomaly detection to ~37 million sources, a level rarely attempted in the literature.

Candid Methodological Transparency: The author documents and preserves clear diagnostic benchmarks of algorithmic failure modes (e.g., the 98% blue-excess training bias artifact in LAMOST and the cross-transfer domain shift in SDSS), providing profound pedagogical value.

Comprehensive Data Release: The provision of open-source reproducibility scripts, MCMC provenance chains, model weights, and staged dataset manifests sets an exemplary standard for modern computational astrophysics.
