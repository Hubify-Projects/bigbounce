# EXT Review — P3 × ChatGPT
- paper: P3
- version: v3.1.137
- reviewer: ChatGPT
- model: Pro Extended
- timestamp: 2026-07-06T19:12:02Z
- chat_url: https://chatgpt.com/c/6a4bfc41-3ac0-83e8-9b67-84839835d2cc
- pdf: /tmp/round_P3.pdf

## Raw verbatim response

(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Abstract / title / §III / §VII, “268,519 validated catalog-grade anomalies”: the manuscript uses “validated” and “catalog-grade” for a heterogeneous set whose components are not uniformly validated detections: DESI is validated only for broad/extended injected morphologies, SDSS uses a fixed-size continuity slice, Planck is an in-sample fixed top-200 patch list, and NEOWISE passes only a masking-geometry QA test “by construction,” not a detector-sensitivity test; this does not support a single validated anomaly catalog in the usual sense. 

round_P3

[MAJOR] Abstract / §III A / §VII, claimed scale relative to prior work: the manuscript itself states that the like-for-like DESI science-target recount is 2,468 anomalies, about 0.92× the cited prior benchmark of 2,685, while the larger ∼73× and ∼141× factors compare full instrument-stream or inclusive process counts against a science-target catalog; this makes the headline “largest catalog” framing scientifically misleading.

[MAJOR] §III A, DESI component dominating the validated count: ∼98.7% of DESI anomaly clusters are reported to fall on sky-fiber, filler, or non-primary-class spectra rather than science targets, yet 195,829 DESI entries dominate the “validated” headline; the manuscript does not establish that these are astrophysical source anomalies rather than fiber-assignment, calibration, sky, or stream-processing artifacts.

[MAJOR] §II B–§III C, SDSS “validated” count of 77,905: the SDSS number is explicitly a fixed-size continuity slice chosen to equal the cross-transfer count, while the strict DESI-style S > 5 threshold gives only 12 objects and the native top-1% gives 19,253; using 77,905 as a validated catalog component is an arbitrary selection, not a physically or statistically justified anomaly threshold.

[MAJOR] §III H / Fig. 10, NEOWISE validation: the NEOWISE gate plants objects outside a fixed ecliptic mask and “recovers” them by applying that same mask, so the 100% pass is guaranteed by construction; including NEOWISE in the validated subset on this basis conflates mask implementation QA with anomaly-detector sensitivity.

[MAJOR] §III F, Planck CMB tier: the Planck top-200 are selected from a scored bank that includes training patches, the validation loss fails the stated loss criterion, the claimed anti-memorization evidence uses a binomial argument that the text itself notes is invalidated by patch spatial correlations, and no CMB foreground/noise/systematics model is used to show that the selected patches are physical anomalies.

[MAJOR] §III D / §VI A / §VII, inclusive 377,780 catalog: the inclusive headline retains ∼113,000 LAMOST entries from a tier explicitly diagnosed as a 98% blue-excess training-bias artifact with failed injection-recovery; flagging this as exploratory does not make it appropriate to present in the same headline catalog count.

[MAJOR] §III E, eROSITA provenance: the eROSITA score axis is admitted irreproducible, the production threshold cannot be reconstructed from committed artifacts, and the detector fails the 5σ injection-recovery gate at 1.2%; a rank-only membership list may be auditable, but it is not a validated anomaly measurement and should not support scientific catalog claims.

[MAJOR] §II D / Table V / §VI D, validation gates: the pass/fail thresholds are described as heuristic engineering choices rather than statistically calibrated or pre-registered criteria, and several key gates are morphology-specific artificial injection tests that do not demonstrate completeness or purity for the actual observed anomaly populations.

[MAJOR] §IV A / Fig. 6, novelty claims: the manuscript repeatedly reports SIMBAD-unmatched fractions while acknowledging that SIMBAD absence is not discovery and that broader archival cross-matching identifies all tested SDSS/eROSITA/NEOWISE SIMBAD-unmatched samples; the 17.8% “genuine novelty” value is only a DESI top-1,000 point estimate and cannot justify catalog-wide novelty language.

[MAJOR] §IV C, cross-survey validation: the 637 multi-survey coincidences are a tiny fraction of the total, the DESI×SDSS positional matches are statistically comparable to random expectations before spectroscopic inspection, and no rigorous probabilistic cross-match or follow-up program supports using these coincidences as validation of the full catalog.

[MAJOR] §V / Appendix C, fNL application: the empirical bias measurement is α = 0.19 ± 0.65, only 0.29σ from null, and the de-biased forecast returns exactly the single-tracer baseline; the cosmology section therefore contributes no demonstrated constraint and should not be presented as evidence of scientific utility beyond a speculative workflow example.

[MAJOR] §V A / Appendix E, NANOGrav application: the analysis uses a factorized free-spectrum KDE approximation, compares fixed spectral-index templates, and admits that environmentally modified SMBHB models can produce γ ∼ 2.5–3; the Bayes factor against an idealized circular SMBHB index is therefore not a robust physical model-comparison result for PRD.

[MAJOR] Data availability / reproducibility statements: the work depends heavily on scripts, JSON artifacts, model weights, and catalogs said to be in a companion repository or to be released later, while several production artifacts were lost, unrecovered, or reconstructed; a PRD submission cannot rely on unavailable private pipeline artifacts for its central numerical claims.

[MINOR] §III G / Fig. 6 / historical captions: Gaia is said to be removed from all catalog counts because the output was synthetic, yet Gaia still appears in figures, historical denominators, and captions; this creates avoidable ambiguity about what is actually part of the submitted result.

[MINOR] Tables I–II and captions: the manuscript uses multiple incompatible denominators and threshold families in adjacent headline tables, including full-stream spectra, validated TARGETTYPE subsets, zall-pix rows, fixed-size slices, top-percentile cuts, and strict S cuts; the result is too difficult to audit and invites misquotation.

[MINOR] §II B / notation and score definition: “canonical S” is not actually canonical across surveys because Planck uses raw MSE, eROSITA uses an unrecovered score-knee axis or raw-rank membership, and several thresholds are fixed-count selections; the notation should not imply a common anomaly-score semantics.

(3) The central claim that the manuscript establishes a validated catalog-grade set of 268,519 anomalies is not supported by the evidence presented.
