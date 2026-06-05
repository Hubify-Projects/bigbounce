# P3 auto-2026-06-05_1418pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 639.3s

---

Meta-review — new issues not caught by any of the 5 prior referees

P3-META-E1
Severity: ESSENTIAL
Section + page: II.B (Training and Scoring), p. 2
Why others missed it: Reviewers critiqued thresholds and cross-transfer scales but did not read the score definition sentence closely.
Specific problem (quote the text): “For DESI DR1, µval ≈ 0.0287 (validation MSE) and σval is set such that the S > 5 catalog threshold corresponds to MSE ≈ 0.143 on the rescaled scale.”
Required fix: You cannot “set” σval after defining S as a standardized residual S = (MSE − µval)/σval. σval must be the empirical standard deviation of MSE on the held-out validation set. Recompute S with the measured σval; if you want to anchor a fixed absolute MSE threshold, then define and use a separate, explicitly named threshold variable (e.g., MSE_thr), not a redefined σval. Audit all DESI S values, rates, and any downstream comparisons that depended on this calibration.

P3-META-E2
Severity: ESSENTIAL
Section + page: Table I footnote (Path-C catalog-grade subset), p. 7; Data availability paragraph, p. 14
Why others missed it: Several referees noted ambiguity in the “catalog-grade” count, but no one checked the arithmetic consistency.
Specific problem: The footnote claims a “catalog-grade tier (DESI + SDSS native + eROSITA + Planck native + Gaia + NEOWISE) is 264,938.” Summing these per-survey Path-C counts gives 195,829 + 77,905 + 298 + 500 + 419 + 200 = 275,151. Subtracting the global dedup count 10,213 produces 275,151 − 10,213 = 264,938 — exactly the quoted “catalog-grade” number. This reuses the full 7-way dedup compression on a reduced 6-survey subset without recomputing overlaps, which is generally invalid (subsets have different overlap structure; many intra-survey duplicates are LAMOST-specific and should drop).
Required fix: Recompute the unique-object count for the stated “catalog-grade” subset with a fresh, restricted dedup pass and report the true subset-specific duplicate count. Provide the dedup manifest for that subset (cluster sizes, survey membership).

P3-META-M3
Severity: MAJOR
Section + page: II.D Step 6 (7-way positional dedup at 5″), p. 4; IV.A novelty cross-match, p. 8–9
Why others missed it: Reviewers asked for matching protocol details and proper motion handling but did not flag the single 5″ radius as survey-inappropriate.
Specific problem: A uniform 5″ cone for all pairings is not defensible across surveys with very different astrometric uncertainties and source densities (e.g., eROSITA X-ray sources often have 1σ positional errors >5″; Gaia has sub-arcsecond precision; NEOWISE has multi-arcsecond PSFs). This single-radius choice biases both (a) dedup compression (missed true cross-survey matches for X-ray/IR; spurious matches in dense optical regions) and (b) the “genuine novelty” rate.
Required fix: Adopt survey-pair-specific match radii based on convolved 2D error ellipses (or Rayleigh-equivalent search radii at a fixed false association probability), incorporate proper-motion corrections for Gaia, and recompute (i) the 7-way dedup clusters and (ii) the novelty statistics. Provide pairwise match confusion matrices with per-pair radii and expected spurious-match rates.

P3-META-M4
Severity: MAJOR
Section + page: II.D Step 2 (Native CMB retrain), III.F (Planck CMB), p. 4, 6
Why others missed it: Critics focused on the Planck CAE score scale and timing, not on sample partitioning.
Specific problem: The Planck native CAE is “trained on 2×10^5 SMICA patches” while the anomalies are selected from “Input: 20,000 SMICA CMB map patches.” The paper does not state whether the 20,000 inference patches were excluded from the 200,000-patch training set. If not, the anomaly selection is potentially contaminated by training–test leakage on the sky.
Required fix: Explicitly document the patch-extraction strategy (tiling, stride, mask), and guarantee disjoint training/validation/test sky partitions (with coordinates/hashes) for the Planck CAE. If leakage is present, retrain with proper splits and reissue the Planck top-200 list.

P3-META-M5
Severity: MAJOR
Section + page: II.B (per-band residuals), III.B (candidate selection using rZ), p. 2, 5
Why others missed it: Requests for rB/rR/rZ formulas were made, but not the comparability problem.
Specific problem: Per-arm sub-scores rB, rR, rZ are compared directly (e.g., “Z-arm dominated”) without stating any normalization for differing arm lengths, pixel counts, or noise properties after downsampling. If rZ integrates more samples or different noise variances than rB/rR, the dominance criterion can be biased.
Required fix: Define rB, rR, rZ rigorously (including normalization by the number of valid pixels and, ideally, noise weighting). Re-evaluate any selections based on “Z-dominance” after normalization; report the impact on the z≈6 quasar candidate list.

P3-META-M6
Severity: MAJOR
Section + page: II.B (Eq. 1), p. 2; III A–D (spectroscopic anomaly scoring)
Why others missed it: Reviewers flagged SNR decorrelation testing but not the core choice of loss.
Specific problem: The anomaly detector minimizes and scores unweighted per-element MSE on spectra. For spectroscopic data with known per-pixel uncertainties and strong wavelength-dependent variances, an unweighted MSE creates a unit- and SNR-dependent objective and score. The stated Spearman ρ ≈ −0.03 on a small stratified subsample does not validate this choice broadly.
Required fix: Either (a) re-train and re-score with noise-weighted residuals (χ^2 per pixel using pipeline flux variances) or (b) at minimum, whiten inputs by per-pixel noise estimates before training/score computation, and then re-test SNR dependence across the full catalog. Report how weighted vs unweighted choices change the S-distribution and top-anomaly content.

P3-META-M7
Severity: MAJOR
Section + page: III.A (DESI DR1), p. 4
Why others missed it: Focus was on rates and thresholds; the validation claim itself slipped by.
Specific problem (quote): “Spectral inspection of the top 200 confirms a 0% artifact rate.” No blinding, inter-rater agreement, or independent cross-check is described; “0%” suggests unwarranted certainty for a single-inspector, non-blind assessment.
Required fix: Reevaluate the top-200 with a blinded, two-rater protocol; report inter-rater agreement (κ) and a binomial confidence interval for the artifact fraction. Replace “0%” with the measured estimate and its CI (e.g., Clopper–Pearson).

P3-META-M8
Severity: MAJOR
Section + page: IV.C (7-way dedup: expected random coincidences), p. 10
Why others missed it: Others questioned general matching details but not this specific end-to-end arithmetic.
Specific problem (quote): “For the 7-way 5″ deduplication, the expected random coincidence contribution is ≲ 10 across all survey pairs against 637 observed multi-survey clusters (<2% contamination).” Given the large numbers of anomalies and heterogeneous footprints, ≲10 total random overlaps is implausibly low without a detailed area–density model; no derivation is provided.
Required fix: Provide a quantitative, per-pair sky-overlap and number-density model (accounting for footprints and masks) and compute the expected random-coincidence distribution with uncertainties. If ≲10 cannot be supported, correct the contamination estimate and its interpretation.

P3-META-m9
Severity: MINOR
Section + page: II.B (image cutout scales), III.B/III.H figure captions, p. 2, 5, 8
Why others missed it: The numbers look internally consistent on a quick read.
Specific problem: The DESI Legacy Survey grz cutouts are described as 128×128 ≈ 54″ per side and 256×256 ≈ 108″ per side, implying ~0.422″/pix. This differs from common LS pixel scales (e.g., 0.262″ DECam, 0.396″ BASS/MzLS). If the cutouts are resampled, state that; otherwise, the implied plate scale is ambiguous.
Required fix: Specify the image source (DECam/BASS/MzLS), the resampling and pixel scale used for cutouts, and ensure captions reflect the actual pixel scale.

P3-META-m10
Severity: MINOR
Section + page: IV.A (novelty, 20-catalog list), p. 9
Why others missed it: They asked for a catalog list/table but not a key missing piece about angular-resolution harmonization.
Specific problem: The 20-catalog CDS X-Match is used to assert 82.2% archival IDs, but the text does not state whether catalog PSFs/resolution and deblending differences were accounted for (e.g., splitting one infrared source into multiple optical components). This can inflate the “archival-ID rate.”
Required fix: Describe the cross-match resolution harmonization (e.g., collapsing multiple optical components within the IR beam before counting matches) and re-tabulate the archival-ID rate under that rule.

Meta-review recommendation
REJECT

Given the union of all six reviews, there are multiple essential and major blockers: (i) the S-score standardization inconsistency (σval “set” to hit an MSE threshold), (ii) re-use of the full-sample dedup compression to claim a subset’s “catalog-grade” unique count, (iii) survey-inappropriate single 5″ dedup/match radius, (iv) unaddressed Planck CAE train–test leakage risk, plus numerous previously flagged arithmetic, cross-referencing, and forecasting inconsistencies. I count at least 10 essential/major blockers across the six reports. My confidence that the paper would survive external peer review without a substantial rewrite is low; the work is potentially valuable, but it needs a careful methodological overhaul, consistent accounting, and removal or clear segregation of exploratory/diagnostic elements before PRD can consider it.