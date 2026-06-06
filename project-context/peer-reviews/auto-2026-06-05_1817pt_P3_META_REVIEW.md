# P3 auto-2026-06-05_1817pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 433.9s

---

META-REVIEW (blind-spot audit)

Below are issues that, to the best of my check, none of the five prior referees identified. I focus on cross-reference inconsistencies, hidden conditioning, unit/scale mismatches across sections, and tests that materially affect the catalog’s integrity.

P3-META-E1
- Severity: ESSENTIAL
- Section + page: Appendix D, Fig. 8 caption (p. 16) vs Sec. V (p. 10) and Table IV (p. 13)
- Why others missed it: Attention was on the F0/α-form and % improvement; this cross-reference baseline clash is only visible when comparing Sec. V to Appendix D’s figure text.
- Problem: Two contradictory single-tracer baselines for σ(fNL) are used. Sec. V and Table IV anchor the single-tracer baseline at σ(fNL)std = 8.98, but Fig. 8 explicitly states “single-tracer baseline (σ(fNL) = 16.85).” These cannot both be true in the same Fisher setup.
- Required fix: Reconcile and document a single, experiment-specific baseline. If Fig. 8 pertains to a different configuration (e.g., a SPHEREx-like multi-tracer toy model), label it explicitly and do not call it a “single-tracer baseline” without stating the survey/assumptions. Otherwise, correct Fig. 8’s baseline to 8.98 and regenerate the curve and discussion accordingly.

P3-META-E2
- Severity: ESSENTIAL
- Section + page: Table I footnote ∥ (p. 7)
- Why others missed it: The line occurs deep in a dense, narrative footnote.
- Problem: Arithmetic/counting error about ACT removal: “excluding ACT subtracts exactly 200 from both the input sum and the unique-object count.” From the same table, ACT contributes 20,000 input patches and 200 anomalies; removing ACT changes the processed input total by 20,000, not 200.
- Required fix: Correct the sentence to “excluding ACT subtracts 20,000 from the input-sum and 200 from the anomaly total,” and recheck any summary totals that relied on this phrasing.

P3-META-M1
- Severity: MAJOR
- Section + page: Sec. II.B (p. 2–3), Sec. III.A (p. 4), Appendix B/Table VI (p. 15)
- Why others missed it: Several asked for formulas for rB,rR,rZ, but none flagged the normalization bias this induces.
- Problem: Per-arm residuals rB, rR, rZ are used to classify “band dominance,” but the three DESI arms span unequal wavelength ranges (B≈2600 Å vs R,Z≈1600 Å). If rB,rR,rZ are simple summed residuals over each arm, the longer B arm will be systematically favored, biasing the “B-dominant” classification (22.7% reported). The paper never defines these sub-scores or states whether they are normalized by the per-arm bin count and/or per-pixel noise.
- Required fix: Provide explicit formulas and normalize per-arm residuals by both the number of bins in the arm and the local noise (or use per-pixel inverse-variance weighting). Recompute the arm-dominance taxonomy with the normalized definition and update Table VI counts and any B-dominance diagnostic that relies on unnormalized sums.

P3-META-M2
- Severity: MAJOR
- Section + page: Sec. II.D Step 6 and throughout (5″ deduplication), Table I footnotes (p. 7); Sec. III.E (eROSITA) (p. 6–8)
- Why others missed it: Deduplication radius choice was not scrutinized against per-survey astrometric/PSF scales.
- Problem: A uniform 5″ cross-survey dedup radius is unjustified across surveys with astrometry/PSF spanning milliarcseconds (Gaia) to tens of arcseconds (eROSITA). Using 5″ likely under-deduplicates eROSITA vs optical/IR matches (inflating “unique” counts) and over-deduplicates extremely precise-astrometry matches. This impacts the headline “378,280 unique anomalies.”
- Required fix: Adopt per-survey (or per-pair) error-aware matching (e.g., Bayesian/likelihood-ratio—or at minimum, a larger radius for X-ray→optical, with a false-match control). Recompute the 7-way union with per-pair radii and report the change in unique counts and multi-survey clusters.

P3-META-M3
- Severity: MAJOR
- Section + page: Sec. III.F (Planck) (p. 6–7), Fig. 7 caption (p. 13)
- Why others missed it: Focus was on training time and pass/fail criteria, not on the definition of “σ” for patch injections.
- Problem: The Planck “5σ Gaussian-bump amplitude” injection-recovery test does not define σ for CMB patches (pixel-variance per patch? map-level noise after beam+mask? standardized/whitened residuals?). Without a precise σ definition and whitening procedure, “5σ” has no reproducible meaning across patches with spatially varying noise/beam.
- Required fix: Specify the noise model, whitening/standardization of patches, and the amplitude-to-σ mapping used for injections. Re-run (or re-describe) the injection-recovery with this definition, and report robustness across sky regions with different noise levels (e.g., near ecliptic poles vs elsewhere).

P3-META-M4
- Severity: MAJOR
- Section + page: Sec. III.H (NEOWISE) (p. 8), Fig. 4 (p. 8)
- Why others missed it: The ecliptic-pole masking was discussed; instrument-artifact flagging for WISE was not.
- Problem: The NEOWISE top anomaly is a bright, saturated source with diffraction spikes (Fig. 4)—a classic WISE artifact case. There is no mention of applying standard WISE/NEOWISE artifact and quality flags (cc_flags, nb, w?flg, ph_qual, w?ext_flg). Relying only on the ecliptic-pole mask is insufficient and likely leaves significant instrument-artifact contamination.
- Required fix: Apply standard WISE/NEOWISE artifact-quality cuts (at minimum cc_flags=‘0’ in W1/W2, ph_qual A/B or justified alternative), re-evaluate the NEOWISE anomaly set, and update the top-object example if it is flagged as an artifact. Quantify the fraction removed and the mask’s effect on the 1% selection.

P3-META-M5
- Severity: MAJOR
- Section + page: Sec. IV.A (p. 8–9), Table I notes (p. 7)
- Why others missed it: The need for CIs was raised; no one addressed weighting bias in the aggregate statistic.
- Problem: The aggregate “58.8% SIMBAD-unmatched” fraction is influenced by three surveys with predetermined 1% quotas (Planck, Gaia, NEOWISE). Because these quotas are exogenous (not data-driven anomaly rates), the aggregate is effectively a weighted mix of heterogeneous—and in two cases exploratory—selections. As presented, it can be misinterpreted as an intrinsic property of the anomaly population.
- Required fix: Report per-survey SIMBAD-unmatched fractions only; if an aggregate is shown, (i) state the weighting scheme explicitly (e.g., by anomaly count) and (ii) qualify that for quota-driven surveys this is not an estimate of an intrinsic unmatched fraction. Preferably, remove the aggregate or provide both a count-weighted and a survey-weighted average, with clear caveats.

P3-META-m1
- Severity: MINOR
- Section + page: Sec. III.E (eROSITA) (p. 6–7)
- Why others missed it: Wording looks like casual context.
- Problem: The sentence “eastern half under Rosatom proprietary control” is editorial and imprecise for a PRD article. Data-rights boundaries for eROSITA should be neutrally and accurately described (e.g., by sky coverage definition or official data-release documentation).
- Required fix: Replace with a neutral, citable description of DR1 sky coverage and data rights (e.g., “DR1 covers [X] sky fraction as defined in [official citation]; the complementary hemisphere is not included in DR1 under the current data-rights policy”).

P3-META-m2
- Severity: MINOR
- Section + page: Sec. III.E (eROSITA) Table III (p. 8) and text using IF latent injections (Sec. II.D Step 5; Sec. VI.D(ii))
- Why others missed it: They focused on pass/fail and overlap; not on the definition of the injected perturbation.
- Problem: For eROSITA, the “subspace injection” used in injection-recovery and cross-validation is not specified (which latent axes, distribution, and normalization). Without this, the 1.2% “recovery at 5σ” is uninterpretable and not reproducible.
- Required fix: Define the latent-space injection precisely (axis selection, amplitude normalization wrt latent variance, number of draws, and whether features were whitened) and provide a seed/provenance so the test can be reproduced.

P3-META-m3
- Severity: MINOR
- Section + page: Sec. IV.A (“Archival cross-match and genuine novelty fraction”) (p. 8–9)
- Why others missed it: They requested binomial CIs but not match-confusion analysis.
- Problem: The 100% “archival identification” of small, 20-object subsamples via VizieR is reported without any estimate of the multi-catalog false-positive coincidence rate at 5″ when searching across many catalogs. This can easily bias the novelty inference downward in crowded regions (e.g., near the LMC).
- Required fix: For the 20-catalog cross-match at 5″, provide a Monte Carlo false-association rate estimate (e.g., by position scrambling) and report a corrected novelty estimate or at least an uncertainty band that includes cross-match confusion in crowded fields.

P3-META-m4
- Severity: MINOR
- Section + page: Sec. II.B (p. 2–3), Fig. 2 (right) (p. 5)
- Why others missed it: They flagged S inconsistencies, but not numerical stability.
- Problem: The SDSS cross-transfer S distribution extends to S ≈ 1.9 × 10^11 (Fig. 2 right), far beyond any reasonable standardized residual scale. Even as a cross-transfer artifact, this points to potential numerical overflow/underflow or a missing clipping/robust scaling step in score computation or plotting.
- Required fix: Cap extreme scores (e.g., winsorization) or switch to a numerically stable transform for plotting and explicitly state the clipping. Verify that such outliers do not corrupt percentile thresholds or downstream visualizations.

## Meta-review recommendation
MAJOR REVISIONS

Rationale: In addition to the already extensive issues raised by the five referees, the manuscript contains (i) an internal contradiction in the σ(fNL) single-tracer baseline that affects cosmology claims (P3-META-E1), (ii) a concrete counting error regarding ACT’s contribution to the input total (P3-META-E2), and (iii) two methodological problems that directly influence the catalog integrity and uniqueness claim—the uniform 5″ dedup radius across surveys with wildly different astrometry/PSFs (P3-META-M2) and unnormalized per-arm residuals that likely bias DESI “B-dominant” classifications (P3-META-M1). The CMB injection σ definition and NEOWISE artifact screening also need correction before the catalog and its “top anomaly” examples can be trusted at face value.

Given the union of all six reviews
- Blockers (ESSENTIAL/MAJOR) now include: Fisher-baseline dimensional error; percent-improvement misreport; unresolved figure refs; SDSS/LAMOST threshold/S-definition incoherence; missing spatial mask/footprint; implausible training times; novelty fraction without CIs; under-specified bias measurement; confusing native vs cross-transfer catalog definition; SDSS N mismatch; ACT×Planck null without a test statistic; dedup false-coincidence calc missing; GR-effects overstatement; “largest” claim without literature support; data/code availability posture; plus the new baseline inconsistency, ACT input subtraction error, 5″ dedup choice, per-arm normalization, Planck-σ definition, and NEOWISE artifact flags. I count well over a dozen independent major corrections required.
- Confidence of surviving external peer review after addressing all of the above: moderate, conditional on a thorough rewrite/cleanup. The analysis scale and basic idea are strong, but the presentation and several methodological choices must be tightened to PRD standards.