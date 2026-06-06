# P3 auto-2026-06-06_0004pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 345.1s

---

META-REFEREE REPORT — focus on blind spots none of the 5 prior referees caught

P3-META-E1
- Severity: ESSENTIAL
- Section + page: III.C (pp. 5–6) vs. Table II caption (p. 8)
- Why others missed it: Each referee checked SDSS rates and thresholds but not the internal logic of the SDSS-by-class table against the SIMBAD match rate.
- Specific problem (quote): SDSS text: “SIMBAD-unmatched: 90%.” Table II caption: “The 52.7% ‘Uncategorized’ fraction reflects objects that match a SIMBAD entry but lack a specific astrophysical type classification in the database.”
- Required fix: Reconcile the SDSS SIMBAD-match accounting. If “Uncategorized” is a pipeline class unrelated to SIMBAD, say so and remove the SIMBAD-based explanation. If it is SIMBAD-matched, then the 90% unmatched headline is wrong for the SDSS anomaly set and must be corrected with audited counts. Provide a per-class breakdown of SIMBAD matches vs non-matches that sums to the headline fraction.

P3-META-E2
- Severity: ESSENTIAL
- Section + page: II.C GPU Inference Pipeline (p. 3) vs. Table V (p. 15)
- Why others missed it: They commented on plausibility of single-line training times but did not add up wall-clock claims against stated throughputs.
- Specific problem (quote): “Total processing time … approximately 42 hours (wall-clock), dominated by the DESI DR1 scan (19,705 s) … The CMB and photometric surveys each required < 10 seconds of GPU time.” Table V shows spectroscopic inference throughputs of ~1,142 spectra/s (DESI) and ~950 spectra/s (LAMOST). For 11.4M LAMOST spectra this implies ~3.3 h GPU time; adding 5.5 h for DESI and “<10 s” for the rest yields ≲9 h total GPU time, not 42 h.
- Required fix: Provide per-survey wall-clock logs broken down into CPU pre-processing, I/O, GPU inference, and any retraining passes. If the 42 h includes CPU-bound steps, queue waits, or multiple re-scorings, state that explicitly and reconcile with the Table V throughputs.

P3-META-M1
- Severity: MAJOR
- Section + page: II.D Step 6 (p. 3), IV.C (p. 10), III.E (p. 6)
- Why others missed it: They scrutinized dedup counts but not whether a fixed 5″ radius is appropriate across very different astrometric regimes.
- Specific problem (quote): “7-way positional dedup at 5″.” A single 5″ match radius is too tight for eROSITA X-ray positions (typical 1σ–2σ of several arcseconds to >10″, especially off-axis), risking severe under-count of true cross-survey coincidences and biasing the “low redundancy” conclusion.
- Required fix: Redo cross-survey dedup with survey-specific (and, for eROSITA, source-specific) positional uncertainties (e.g., likelihood-ratio or Bayesian cross-match using error ellipses), and report how many additional physically plausible associations appear. At minimum, provide a sensitivity analysis (5″, 10″, 20″) and propagate its effect on the “637 multi-survey coincidences” and the unique-object headline.

P3-META-M2
- Severity: MAJOR
- Section + page: II.B (p. 3), VI.D(b) Table IV (p. 13)
- Why others missed it: They noted domain-shift issues but not the implication of the “>50% anomalies” statement for the robustness of the DESI S>5 thresholding.
- Specific problem (quote): “Applying [the S > 5 threshold] to a random uncurated SPARCL sweep flags > 50% of spectra (a catalog-curation effect, not a threshold artifact…).” This admits that the principal DESI anomaly rate (0.87%) depends critically on prior catalog curation; the S>5 threshold is not portable or survey-agnostic as implied elsewhere.
- Required fix: Quantify and publish the exact curation filters that define the DESI scoring population and show the anomaly fraction as a function of those filters. Provide an external calibration of the S>5 cut (e.g., using a held-out DESI-quality pool independent of curation, or percentile-based normalization) and demonstrate that the headline rate is not an artifact of preselection.

P3-META-M3
- Severity: MAJOR
- Section + page: II.D Step 1 (p. 3), III.E–III.G (pp. 6–8)
- Why others missed it: They asked for more injection/recovery detail but did not question the validity of the absolute loss threshold used as a gate.
- Specific problem (quote): “Retained if (a) validation loss ≤ 0.30 after ≤ 100 epochs, or (b) injection–recovery ≥ 50% at 5σ.” The gating constant 0.30 is an arbitrary, model- and preprocessing-dependent MSE with no cross-survey normalization; for spectroscopic AEs the reported values are ~0.03, while the Planck CAE is 0.44. For Gaia/eROSITA, (a) is not even reported.
- Required fix: Replace (a) with a scale-invariant gate (e.g., validation loss divided by train loss, or a per-feature normalized NLL) and report the corresponding metric for all surveys, including Gaia and eROSITA. State clearly which branch ((a) or (b)) each retained survey satisfied.

P3-META-M4
- Severity: MAJOR
- Section + page: II.D Step 1 (p. 3) vs. II.B (p. 2)
- Why others missed it: Focus stayed on SDSS/LAMOST thresholds rather than training set sizes.
- Specific problem (quote): Step 1: “trained on a 2–5×10^5-spectrum quality-selected subset of each survey’s own data.” Earlier: “47,000 spectra for DESI.” The DESI training set is an order of magnitude below the stated Path-C prescription.
- Required fix: Provide the actual training-set sizes used per survey (DESI, SDSS, LAMOST, etc.) and correct the Step 1 description. If DESI is an exception, justify it and discuss sensitivity of scores to training-pool size.

P3-META-M5
- Severity: MAJOR
- Section + page: II.A–II.B (pp. 2–3), III.E–III.H (pp. 6–8)
- Why others missed it: They focused on score-symbol confusion, not on per-feature units entering a global MSE.
- Specific problem (quote): Inputs for photometric/catalog surveys are heterogeneous feature vectors (“47, 20, and 15 features… minimizing per-element MSE”), but no per-feature standardization/whitening is described. A raw MSE across magnitudes, fluxes, angles, flags, etc. is not dimensionally homogeneous and can be dominated by high-variance features.
- Required fix: Document the exact preprocessing for all features (scaling, whitening, clipping, handling of categorical/Boolean fields) and, if not already done, recompute scores with standardized features. State how this changes the anomaly rank-order for eROSITA/Gaia/NEOWISE and the derived thresholds.

P3-META-m1
- Severity: MINOR
- Section + page: II.D Step 4 (p. 3) vs. Fig. 7 caption (p. 13) and III.H (p. 8)
- Why others missed it: They flagged lack of quantitative color but not the sign inconsistency in the ecliptic mask text.
- Specific problem (quote): Step 4: “NEOWISE ecliptic-pole mask (|becl| < 80°) retains 419/436…”. Fig. 7 caption: “NEOWISE … PASS, 1000/1000 = 100% at |becl| > {85°, 82°, 80.5°}.” The inequality direction flips between sections, making it unclear which regions are masked or tested.
- Required fix: Harmonize the mask definition and the injection test description (clearly define “inside mask” vs “outside mask”), and restate the PASS claim with the correct inequality and geometry.

P3-META-m2
- Severity: MINOR
- Section + page: Abstract (p. 1) vs. Table I footnote ♠ (pp. 7–8)
- Why others missed it: They focused on ACT/Planck gating but not on the composition of the “catalog-grade subset.”
- Specific problem (quote): Abstract: “recommended catalog-grade subset is ∼265,000 unique objects (DESI + SDSS + eROSITA + Gaia + NEOWISE).” Footnote ♠: “catalog-grade tier (DESI + SDSS native + eROSITA + Planck native + Gaia + NEOWISE) is 264,938 unique objects.” One includes Planck, the other does not.
- Required fix: Decide whether the catalog-grade tier includes Planck CMB patches and make the definition and count consistent in abstract, body, and footnotes. If point-source-only is intended, say so and provide the corresponding number.

P3-META-m3
- Severity: MINOR
- Section + page: III.A (p. 4)
- Why others missed it: They did not scan for text duplication.
- Specific problem (quote): The paragraph beginning “Across the 6.5 million spectra in DESI DR1 that carry a validated TARGETTYPE classification…” appears twice with near-identical wording and numbers.
- Required fix: Deduplicate and ensure a single, clearly sourced statement of these rates.

P3-META-N1
- Severity: NIT
- Section + page: II.B (p. 2–3)
- Why others missed it: They focused on S-definition conflicts, not on the mapping of S to MSE.
- Specific problem (quote): “For DESI DR1, µval ≈ 0.0287 … and σval is set such that the S > 5 catalog threshold corresponds to MSE ≈ 0.143 on the rescaled scale.” The phrase “σval is set such that” suggests post-hoc calibration rather than a true validation-set-derived standard deviation.
- Required fix: Clarify that σval is the empirical validation-set standard deviation of MSE and show the computation leading to MSE ≈ 0.143 for S=5, or correct the wording if an explicit rescaling was applied.

## Meta-review recommendation
MAJOR REVISIONS

Given the union of all six reviews, there are multiple essential and major blockers: core inconsistencies in SDSS×SIMBAD accounting; wall-clock/throughput contradictions; a non-robust fixed 5″ cross-survey match radius; hidden conditioning of the DESI threshold to a curated set; an arbitrary, non-normalized gating criterion; inconsistent training-set-size description; and missing feature-standardization for catalog surveys. I count at least 6 blockers that must be resolved (my E1–E2, M1–M5), on top of the substantial issues already raised by the other referees (score-definition overhaul, Fisher-forecast correction and documentation, ACT/Planck usage, SDSS “top-1%” arithmetic, figure placeholders, etc.). My confidence that the paper would survive an external PRD review after addressing all these points is moderate: the dataset and effort are impressive, but the methodology and presentation require a careful, comprehensive revision to meet PRD standards.