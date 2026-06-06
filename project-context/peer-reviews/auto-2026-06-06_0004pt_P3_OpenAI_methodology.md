# P3 auto-2026-06-06_0004pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7206 chars)
**Wall time**: 269.7s

---

Referee report for Physical Review D (methodology)

Overall assessment
The paper reports a very large multi-survey anomaly-detection effort and presents several methodological and cosmological byproducts. However, there are foundational methodological inconsistencies and clarity gaps that must be resolved before the results can be evaluated to PRD standards. The most critical issues are: (i) inconsistent/ambiguous definition and usage of the anomaly score S across surveys and detectors (and even within the same survey under cross-transfer vs native models), (ii) a dimensional error in the Fisher “positivity-respecting” forecasting formula (F0 written as 1/8.982 instead of 1/8.982^2), (iii) unresolved figure references (“Fig. ??”) in the main text, and (iv) use of a quarantined ACT data product (explicitly failing both gate criteria) to support a main-text Planck×ACT “null” statement. There are also several places where distinct σ(fNL) baselines are shown adjacently without explicit cautions about non-comparability, contrary to PRD expectations for statistical rigor. Below I enumerate all detected issues.

Findings

ESSENTIAL

- ID: P3-E1
  Section + page: II.B–II.D, III.C–III.H, Table I, Table III, Fig. 2 caption; multiple pages 2–8
  Problem: Ambiguous/inconsistent definition and reuse of the symbol S (the anomaly score). You state “Throughout this paper, ‘S’ refers without exception to the per-survey standardized (‘z-scored’) reconstruction residual” (Eq. 2). But:
    • SDSS/LAMOST “cross-transfer” scores are on a DESI-trained model and appear to use DESI’s µval, σval; yet later you call SDSS “native re-score top-77,905 at S ≥ 0.1060,” which is not consistent with a z-scored tail threshold (99th percentile of a standard-like variable is ≈ 2.33, not 0.106).
    • eROSITA: Table I footnotes and §III E alternately describe a “data-driven IsolationForest score-knee threshold;” then speak of “S > 0.259 on the eROSITA-native IsolationForest raw-score axis,” but Table III defines SIF,raw on a ∼0–3.5×10^4 scale and SBigAE as the z-scored BigAE MSE. Using S for the IF raw score is inconsistent with the global S definition and contradicts the stated IF scale.
    • NEOWISE and Planck list “Score” values (e.g., NEOWISE “Score = 11.5;” Planck “score range [0.558, 0.621]”) without clarifying which detector/normalization these belong to.
    • Fig. 2 (right) shows S up to 1.9×10^11 while S is defined as a z-score; this is only possible if µval, σval are imported from a different domain (DESI) and denominators are tiny; the caption calls it a “cross-transfer artifact,” but this violates the “without exception” S definition in the text.
  Required fix: Cleanly separate anomaly scores by detector and training domain with unambiguous symbols. For example: SBigAE-native (per-survey z-score), SBigAE-XFER (z-score relative to DESI µval, σval), SIF,raw (IF raw isolation score), SCMB (CMB-CAE loss proxy), etc. Remove the blanket “without exception” claim or make it literally true. For every threshold quoted (e.g., “S ≥ 0.1060”), explicitly state which score is used and why that level corresponds to the quoted percentile or knee. Re-plot figures with correctly labeled axes. Update all text, tables, and footnotes accordingly.

- ID: P3-E2
  Section + page: V, VI.D(i), Table IV; pages 10–13
  Problem: Dimensional/definition error in the Fisher “positivity-respecting” formula. You write “1/σ(fNL)^2 = F0 + c α^2 with F0 = 1/8.982 and c = 0.0747.” This is inconsistent: if σstd = 8.982 at α = 0, then F0 must be 1/σstd^2 = 1/(8.982)^2 ≈ 0.01239, not 1/8.982 ≈ 0.111. Your numerical result σ = 8.14 for α = 0.19 in fact corresponds to F0 = 1/(8.982)^2.
  Required fix: Correct F0 to 1/(8.982)^2 wherever it appears and recheck every forecasted σ(fNL) number and envelope you report (central values and bounds). State explicitly how c was obtained (fit points, configuration, and code), and provide a small table or figure substantiating the fit.

- ID: P3-E3
  Section + page: II.A, III.B; pages 2, 5
  Problem: Unresolved figure references (“Fig. ??”; “Figure ??”) remain in the main text:
    • “architecture shown schematically in Fig. ??” (p. 2),
    • “Figure ?? shows DESI Legacy Survey DR9 grz composite cutouts ...” (p. 5).
  Required fix: Resolve all placeholder references with actual figure numbers or remove the sentences. PRD will not accept manuscripts with unresolved cross-references.

- ID: P3-E4
  Section + page: IV.D (main text), Appendix F; pages 10–12, 16–18
  Problem: You use a quarantined ACT DR6 cross-transfer anomaly set (explicitly failing both gate criteria) to support a main-text “Planck × ACT Cross-Correlation: Null Result,” then only partly caveat this in Appendix F. Using a non-validated, gate-failing product to make a main-text statement is methodologically inconsistent.
  Required fix: Move the Planck×ACT cross-correlation to Appendix F, clearly labeled as a diagnostic only, not a science result. Remove “null result demonstrates...” language from the main text, or restate it as a qualitative caution solely about cross-transfer failures. Ensure the abstract and conclusions do not rely on this.

- ID: P3-E5
  Section + page: V, Appendix C and Fig. 8; pages 10–11, 15–16
  Problem: Multiple σ(fNL) baselines (σstd = 8.98; σbaseline-multi = 12.72; dense-limit = 11.71; single-tracer baseline = 16.85) appear adjacent to each other without explicit “not directly comparable” disclaimers each time they are juxtaposed. This risks misinterpretation of improvements across different survey/tracer configurations and likelihood assumptions.
  Required fix: Every time two σ(fNL) values from different configurations appear side-by-side (DESI-only vs canonical 5-tracer vs dense-limit vs single-tracer baselines), insert an explicit statement that they are not directly comparable and specify which data, nuisance parameters, and Fisher blocks each refer to. Prefer a summary table that makes the distinctions explicit.

- ID: P3-E6
  Section + page: V (Landy–Szalay and Fisher forecasting); page 10–11
  Problem: The primary estimators and exact analysis choices are under-specified for reproducibility at PRD standards:
    • Landy–Szalay: The definition of masks, completeness weights, random catalogs (26,920 “anomaly-window-matched randoms”), jackknife regions and their sky geometry, and binning are not fully specified. No covariance estimate or goodness-of-fit is reported beyond αjk ± σ.
    • Fisher forecast: The origin of c = 0.0747 and F0 (after correction) is not shown. It is said to be “verified positive via 5-α refit,” but no details or fit points are documented in the paper.
  Required fix: Provide a reproducibility subsection or an appendix with all estimator definitions, mask footprints, random generation protocol, jackknife regionization, exact bin edges, shot-noise treatment, and the Fisher-code settings and inputs used to obtain F0 and c. Include either a table of the α-fit points or deposit a script and specific tags in the data/code repository referenced in the Data Availability section.

- ID: P3-E7
  Section + page: Abstract (first page), V.A and Appendix E; pages 1, 11–12, 16
  Problem: Bayes factors and “decisive” language for the NANOGrav spectral-index comparison rely on a Savage–Dickey ratio for γ fixed values versus a uniform prior in γ over [0,7]. This is acceptable only if the posterior densities at those points are computed carefully from a converged chain and the prior density is constant across the binning. The text does not show how the posterior density at γ = 3.0 and 4.33 was estimated from the KDE likelihood product or what kernel bandwidths enter. Also, the free-γ and fixed-γ hypotheses are not nested models in the usual sense for a physical SMBHB template; the comparison as implemented should be described more cautiously.
  Required fix: Add a paragraph in Appendix E explicitly describing how the posterior density at the tested γ values was computed from the sampled posterior (bin width or kernel bandwidth, normalization), include a small plot of the marginalized posterior around γ = 3.0 and 4.33, and soften the “decisive” wording to reflect the dependence on the adopted flat prior and KDE product. State explicitly that this is a simple spectral-index hypothesis test on the KDE free-spectrum, not a full timing-residual model comparison for SMBHB vs bounce scenarios.

MAJOR

- ID: P3-M1
  Section + page: Fig. 1 caption and panel; page 4
  Problem: The figure title reads “Spatial distribution of all 319,443 anomalies across 8 archives,” and ACT DR6 points appear, yet ACT is quarantined and excluded elsewhere. The caption attempts to frame it as a “cross-transfer baseline,” but the panel remains visually misleading.
  Required fix: Retitle the panel to “Cross-transfer baseline (includes quarantined ACT DR6; not a science result)” and watermark or gray-out the ACT layer in the legend/points. Alternatively, move to an appendix and show only validated Path-C counts in the main text.

- ID: P3-M2
  Section + page: III.C; pages 5–6
  Problem: SDSS native re-score covers 1,925,279 spectra, not the stated DR18 2,304,830; the selection difference is not explained. You still compare rates to the 2.3M total elsewhere (3.38%).
  Required fix: Describe the selection/filtering leading to the 1,925,279 subset (S/N cuts, mask, quality flags). Make all rate comparisons use consistent denominators or clearly mark which denominator is used.

- ID: P3-M3
  Section + page: II.D Step 5 and III.D–III.E; pages 3–7
  Problem: Injection–recovery tests are summarized but insufficiently specified. For spectral surveys, you mention “continuum-dip” and “emission-line” plants; for Gaia “variability-axis injection” and for eROSITA a “subspace-injection,” but exact plant morphologies, widths, equivalent widths, placement, and S/N regimes are absent.
  Required fix: Provide a short table or appendix describing each plant family (functional form, parameter ranges, where injected in spectra/features, noise model), and release the corresponding plant files (you hint these exist) with DOIs or repository paths.

- ID: P3-M4
  Section + page: III.A; page 4
  Problem: “0% artifact rate in the top 200” is asserted without a documented vetting protocol or inter-rater agreement.
  Required fix: Describe the vetting process (number of inspectors, criteria, time windows, how artifacts were defined), and report an uncertainty (e.g., binomial 95% CI) and inter-rater agreement if applicable.

- ID: P3-M5
  Section + page: III.F; page 7
  Problem: Planck native CAE “Top-200 … score range [0.558, 0.621]” is reported without defining the score (MSE, BCE, or a normalized proxy). Criterion (a) “val loss ≤ 0.30” is not strictly comparable to this “score.”
  Required fix: Define the Planck CAE anomaly score explicitly (loss function, normalization, whether it is z-scored), and relate it clearly to the gating criteria.

- ID: P3-M6
  Section + page: III.E (eROSITA) and Table I footnotes; pages 6–8
  Problem: Threshold and score notation for eROSITA conflict: the text mentions a data-driven IsolationForest knee; footnotes call it “S > 0.259 on the eROSITA-native IsolationForest raw-score axis,” but Table III defines SIF,raw on a 0–3.5×10^4 scale. 0.259 cannot be an IF score on that scale.
  Required fix: Correct the threshold description and notation. If 0.259 is a BigAE z-score threshold, say so; if it is a rescaled IF score, define the rescaling and label it differently (e.g., SIF,z).

- ID: P3-M7
  Section + page: Fig. 2 (right panel) and §III.C; pages 5–6
  Problem: Showing S up to 1.9×10^11 for SDSS cross-transfer on a “z-scored” axis is numerically misleading. It likely arises from importing DESI µval, σval to an OOD SDSS population, driving σval effectively tiny for SDSS.
  Required fix: Either (i) replot SDSS cross-transfer on raw MSE (or a bounded transform) to avoid misleading the reader about the dynamic range of a “z-score,” or (ii) change the definition and labeling to SBigAE-XFER with a clear note that it is a DESI-calibrated scale, not a per-survey z-score.

- ID: P3-M8
  Section + page: IV.A Fig. 5; page 9
  Problem: The aggregate SIMBAD-unmatched fraction (58.8%) is presented prominently. While you caution that this overstates genuine novelty, the figure can still be misread.
  Required fix: On the figure itself, add a second axis/annotation with the DESI top-1,000 “genuine novelty” 17.8% as the primary discovery-rate metric, and add a bold in-caption statement: “SIMBAD-unmatched is a database-coverage proxy, not a discovery rate.”

- ID: P3-M9
  Section + page: V (last paragraph) and Appendix E; pages 11–12, 16
  Problem: The “decisive” Bayes-factor claim uses Jeffreys’ scale for a ratio BMB/SMBHB constructed from two Savage–Dickey values relative to a flat prior over γ. This is a nonstandard comparison of two point-hypotheses within a continuous-parameter model. The text risks over-claiming.
  Required fix: Soften the language to “strong preference under the adopted prior within the KDE free-spectrum likelihood,” and emphasize it is not a full PTA model-comparison result.

MINOR

- ID: P3-N1
  Section + page: II.D (paragraph near end); page 3
  Problem: Duplicate phrasing: “reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository).”
  Required fix: Remove duplication.

- ID: P3-N2
  Section + page: Abstract, II.A; pages 1–2
  Problem: Versioning/placeholder-like phrasing: “Fig. ??” and model-count statements without a figure presently in the paper (“architecture shown schematically in Fig. ??”).
  Required fix: See P3-E3 fix.

- ID: P3-N3
  Section + page: Data availability; page 14
  Problem: “Private pending arXiv acceptance; public upon acceptance.” PRD expects data/code availability upon publication.
  Required fix: Commit to a permanent, publicly accessible DOI-hosted archive upon acceptance; ideally make a private link available to referees now.

- ID: P3-N4
  Section + page: III.H (NEOWISE) and Fig. 4; page 8
  Problem: The NEOWISE “Score = 11.5” is unlabeled by detector/normalization; “extreme W1–W2” needs a quantitative color number.
  Required fix: Label the score type (SBigAE-native) and report the measured W1–W2 value with uncertainty.

- ID: P3-N5
  Section + page: II.C; page 3
  Problem: GPU timings: eROSITA/Gaia/NEOWISE “Training times” of order 1–8 s appear implausibly small without context.
  Required fix: Clarify that these are short single-epoch or few-epoch fits on small models, or correct if misreported. Specify batch sizes and number of epochs.

- ID: P3-N6
  Section + page: III.A; page 4
  Problem: “The three highest-scored anomalies (S = 25.2, 24.6, 24.5) are Z-dominant...” These extend far beyond the S > 5 tail but no spectra are shown in the paper.
  Required fix: Add a small inset figure or appendix spectrum for at least the highest-S object to substantiate the claim.

- ID: P3-N7
  Section + page: IV.B; page 10
  Problem: χ^2 spatial uniformity statement is dominated by varying survey footprints; you note the caveat, but the text could still be quoted out of context.
  Required fix: Add “not interpretable without per-survey selection-function modeling” directly in the main sentence.

- ID: P3-N8
  Section + page: Throughout
  Problem: Use of approximate symbols (∼, ≈) with sometimes excessive precision (e.g., “21.5×” from 44,075/2,054 = 21.46).
  Required fix: Adopt consistent significant figures (e.g., two sig figs) and use exact ratios where appropriate.

Arithmetic and internal-consistency spot checks

- Path-C per-survey sum 388,493; dedup 10,213 → 378,280 unique. Compression 10,213/388,493 = 2.629% (consistent).
- Point-source vs CMB strata: 378,080 + 200 = 378,280 (consistent).
- DESI anomaly rate: 195,829 / 22,504,897 = 0.008701 → 0.87% (consistent).
- SDSS cross-transfer rate: 77,905 / 2,304,830 = 3.38% (consistent).
- LAMOST cross-transfer → native S>5 compression: 44,075 / 2,054 = 21.46 → “21.5×” (consistent).
- SDSS cross-transfer vs S>5 native: 77,905 / 12 = 6,492 → “∼6500×” (consistent).
- eROSITA overlap enrichment: expected 298×9303/930,203 ≈ 2.98; observed 284; enrichment ≈ 95.3× (consistent).
- DESI×SIMBAD false-match estimate: area π(5″)^2 ≈ 78.54″^2; with nSIMBAD ≈ 3.0×10^−5 arcsec^−2, Pfalse ≈ 2.36×10^−3 (consistent with 2.4×10^−3).
- NANOGrav γ posterior differences: (3.0 − 2.567)/0.382 = 1.13σ; (4.33 − 2.567)/0.382 = 4.61σ (consistent).
- Bayes-factor log10 B for 7.14×10^3 is 3.853 (consistent).
- Fisher correction: With corrected F0 = 1/8.982^2 ≈ 0.01239, c = 0.0747, α = 0.19, 1/σ^2 = 0.01239 + 0.0747×0.0361 = 0.015085 → σ = 8.14 (consistent with the reported value once F0 is fixed).

Scope and length
Given the breadth of material (seven+ archives, multiple detector variants, cosmological forecasts), the 20-page length is reasonable. However, clarity would benefit from consolidating all score definitions and thresholds into a single early table and moving all cross-transfer diagnostics (including Fig. 1 and ACT content) to appendices. Recommended maximum for the main text after consolidation: 16–18 pages, with detailed diagnostics in appendices.

Bibliography
Spot checks show plausible citations and years. Ensure that Heinrich et al. is consistently cited as 2024 in the main text to match the reference entry, and correct any arXiv-label inconsistencies you note in Table VII footnote.

## Summary recommendation
MAJOR REVISIONS

The work is potentially impactful, but the anomaly-score definition inconsistencies, the Fisher forecasting formula error, unresolved figure references, and reliance on a quarantined ACT product for a main-text statement are incompatible with PRD methodological standards. These issues are fixable. Please implement the essential fixes (score-symbol cleanup and re-labeling throughout; corrected Fisher constants and rechecked σ(fNL); resolved figures; relocation/caveating of ACT content; explicit non-comparability of σ baselines; and sufficient estimator detail for reproducibility). With these addressed, plus the listed major/minor items, the paper can be reassessed.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER SECOND PASS (PRD rigor checklist)

ESSENTIAL

- ID: P3-E8
  Section + page: III.C and Table I footnotes; pages 5–7
  Problem: Arithmetic inconsistency in what is labeled “top-1%” for SDSS DR18. The text and footnote state “top-77,905 native slice at S ≥ 0.1060” and call it “top-1% continuity slice,” but 77,905/1,925,279 = 4.05%, not 1%. Elsewhere you also give 3.38% (77,905/2,304,830) as the cross-transfer rate. The only value consistent with “top-1%” on the 1,925,279 subset is ≈19,253 (which you also mention for a different cut).
  Required fix: Correct all “top-1%” labels and associated explanations for SDSS DR18. Clearly state which subset size and which threshold correspond to each count (77,905 vs 19,253), and ensure the “top-1%” descriptor is only used where the arithmetic matches.

- ID: P3-E9
  Section + page: Fig. 8 caption vs Section V main text; pages 16 vs 10–11
  Problem: Contradictory “single-tracer baseline” values for σ(fNL). Section V adopts σstd = 8.98 (DESI-only baseline), but Fig. 8 caption states “single-tracer baseline (σ(fNL) = 16.85).” These are both called “baseline” without context and refer to different null procedures/configurations.
  Required fix: Reconcile and relabel baselines. Explicitly identify which experiment/tracer and Fisher block each baseline corresponds to, and avoid using “single-tracer baseline” for two different values. If Fig. 8’s 16.85 refers to a different survey, redshift range, kmax, or nuisance block, state that and use a distinct name.

- ID: P3-E10
  Section + page: IV.B; page 10
  Problem: Spatial χ2 test degrees-of-freedom and pixel count appear inconsistent with HEALPix Nside = 64. All-sky at Nside=64 has 12 Nside^2 = 49,152 pixels. You state “38,330 HEALPix pixels (Nside = 64), χ2 = 143,936, dof = 38,329.” The reduced pixel count and dof are not explained (masking? empty bins?).
  Required fix: Specify exactly how many pixels entered the test and why (mask/footprint union, occupancy filter), how dof was computed (Nbins minus constraints), and what expected counts were used. If only a subset of pixels was analyzed, state the selection rule and update the dof accordingly.

MAJOR

- ID: P3-M10
  Section + page: V (a); page 10
  Problem: The “full 5,384 QSO-candidate sample” used for the Landy–Szalay bias measurement is not defined. The paper does not document how these candidates were selected from the anomaly catalog (features, thresholds, redshift/line cuts, cross-matches).
  Required fix: Add a precise definition of the QSO-candidate selection pipeline (inputs, cuts, any ML classifier, quality flags, and sky mask), and provide counts per cut so readers can reproduce the 5,384 number.

- ID: P3-M11
  Section + page: II.D Step 5; III.E–III.G; pages 3, 6–8
  Problem: Injection–recovery gate comparators are not aligned with published thresholds for all surveys. Example: eROSITA’s catalog selection uses an IsolationForest knee (and a 298-source top cut), but the injection–recovery is reported “above the 99th-percentile clean-MSE threshold” (BigAE axis) rather than on the IF axis used for the catalog. This mixes detectors/thresholds when assessing gate performance.
  Required fix: For each survey, perform injection–recovery and report recovery against the same score/detector and threshold used for the catalog selection (or provide both, clearly demarcated). State the exact threshold values (percentile or score) used for the gate test per survey.

- ID: P3-M12
  Section + page: V (c) and VI.D(e); pages 11, 12–13
  Problem: The GR projection correction claim “|Δσ/σ| < 0.02% at kmax = 0.2 h Mpc−1 (plane-parallel monopole, sub-% of b)” is presented as a precise number without an explicit computation, code setting, or reference to a reproducible configuration.
  Required fix: Provide a brief derivation or a pointer to a code/config reproducing this bound (inputs, tracer biases, redshift kernels). Otherwise soften to a qualitative statement with an order-of-magnitude reference.

- ID: P3-M13
  Section + page: Table V (Planck CMB row) and III.F; pages 15, 7
  Problem: Implausible training time for the Planck native CAE. You report training on 2×10^5 masked patches for a 1.1×10^6-parameter CNN completed in 10.6 s on an A100. That is orders of magnitude too small unless this is per-epoch or a short warm-up.
  Required fix: Clarify the number of epochs, total wall-clock training time, batch size, and optimizer settings. If 10.6 s is per-epoch or a small tune stage, report the full training duration.

MINOR

- ID: P3-N9
  Section + page: III.E; page 6
  Problem: eROSITA political/proprietary phrasing: “eastern half under Rosatom proprietary control.” The mission is SRG/eROSITA with data policies tied to Roscosmos/IKI and the DE/RU consortia; “Rosatom” is incorrect.
  Required fix: Replace with accurate wording (e.g., “eastern hemisphere not included in DR1; Russian consortium data are not publicly released in this DR”).

- ID: P3-N10
  Section + page: Table I footnote §; page 7–8
  Problem: Hypergeometric significance reported as “p ≈ 0.” This is not a numeric statement.
  Required fix: Provide a numerical upper bound (e.g., p < 1×10^−X) from an exact calculation.

- ID: P3-N11
  Section + page: II.B vs VI.D(i); pages 2–3, 12–13
  Problem: OOD holdout size inconsistency: “100k unseen DESI spectra” (p. 3) vs “an independent 103,000-spectrum OOD holdout” (p. 12).
  Required fix: Harmonize the number and justify the chosen sample size; if it changed, update both locations.

- ID: P3-N12
  Section + page: VII (Conclusions, item 6) vs II.B; pages 14, 3
  Problem: A new Jaccard value appears in Conclusions (“OOD control-vs-control 0.874”) that is not documented earlier; Section II.B reports Jprod×ctrl = 0.732 with gate PASS.
  Required fix: Either document the 0.874 measurement in the body (dataset, seeds, folds) or remove it from the conclusions to avoid introducing a stale/undocumented number.

- ID: P3-N13
  Section + page: III.B and figure labelling; page 5
  Problem: The text notes that panel labels report “AE” (legacy) rather than the total “S,” which can confuse readers given the global S notation disputes.
  Required fix: Add a parenthetical in the caption clarifying that “AE” is rZ (per-arm sub-score) and not the canonical S, or relabel the figure to avoid dual nomenclature.

- ID: P3-N14
  Section + page: II.D, Table I footnotes; pages 3, 7
  Problem: Nonstandard footnote glyphs (♡, ♠) may not be accepted in PRD style and can be ambiguous in monochrome prints.
  Required fix: Replace with numeric/lettered footnotes and ensure they are unambiguous in black-and-white.

Explanation
This second pass focused on fresh arithmetic checks, figure–text consistency, dimensional sanity, internal cross-references, and null-procedure comparability. The most important newly identified issues are the SDSS “top-1%” arithmetic error (P3-E8) and contradictory σ(fNL) “single-tracer baseline” values between Fig. 8 and Section V (P3-E9), both of which can materially mislead readers. The χ2 pixel/dof explanation (P3-E10) and missing definition of the 5,384-object QSO-candidate sample (P3-M10) are also critical for reproducibility.