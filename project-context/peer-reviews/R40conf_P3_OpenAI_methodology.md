# P3 R40conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/paper3_anomaly_catalog.pdf` md5=d1258558 pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6150 chars)
**Wall time**: 319.6s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches”

Scope of review
I reviewed the full 29-page manuscript, auditing all figures, tables, equations, captions, and the abstract. I recomputed the quoted percentages, ratios, confidence intervals, and sigma values from the numbers provided, checked dimensional consistency, tracked the provenance of all abstract and conclusion scalars into the main text, and verified the distinctness of null procedures where multiple σ’s are juxtaposed.

Overall assessment
The paper attempts a large-scale, multi-survey unsupervised anomaly sweep and attaches cosmology-oriented validation and forecasts. The Methods section is unusually transparent about failure modes. However, for a PRD methodology paper, there are several non-negotiable issues: irreproducible scoring axes (eROSITA), incomplete preprocessing provenance (Gaia), train–test leakage in feature scaling for tabular tiers, heavy reliance on internal run-path artifacts in the body text, and release/DOI placeholders. These must be corrected. Additional methodological items require significant clarification or re-analysis (dedicated reproducibility for all tiers, consistent cross-survey thresholding logic, null controls, and sharpening the statistical framing).

Below are itemized findings.

ESSENTIAL (must fix before acceptance)

P3-E1 — Abstract p.1; §III E pp.10–11; Table I footnotes; Data availability p.23
Problem: Irreproducible eROSITA scoring axis used in the released catalog tier. The manuscript states “per-object SBigAE score axis non-reproducible on any of 16 monotone rescalings… the production top-5 values are non-monotone in the committed raw score… the selection is therefore best read as the fixed top-298 cap” and later still uses this tier as a catalog component and reports SIMBAD-unmatched rates, cross-validation overlaps, etc.
Required fix: Either (a) rebuild the eROSITA detector end-to-end with a documented, reproducible score axis (code+weights+fixed scaler fitted on training only) and re-derive all eROSITA-linked results, or (b) remove eROSITA from all primary counts, rates, and cross-method comparisons in the paper (including the 378,280 headline; rerun dedup counts and affected statistics) and confine eROSITA to a clearly demarcated exploratory appendix with membership-only listing. A reproducible DOI with frozen artifacts must accompany the final version.

P3-E2 — §II.B p.3; §III G p.12; Table I footnotes; Data availability p.23
Problem: Gaia DR3 preprocessing is “lineage-inferred.” The exact 20-feature production preprocessing script “was not recovered,” yet Gaia contributes 500 objects and is included in the 378,280 headline and in cross-survey figures. This is not reproducible.
Required fix: Recover or reconstruct the exact production preprocessing (feature list, transforms, constants), re-run Gaia with train-split-only scalers, and update all Gaia-dependent results. If this cannot be guaranteed, remove Gaia from all primary headline totals and analyses and clearly label any remaining Gaia results as exploratory outside the main claims.

P3-E3 — §II.B p.3–4; Eq. (2) p.4; Table I footnotes
Problem: Train–test leakage in feature scaling for tabular surveys (eROSITA, NEOWISE, Gaia). Scalers were fitted on the full sample (including validation/tail) rather than on the training split; only eROSITA has a bounded robustness check; none for NEOWISE/Gaia.
Required fix: Refit scalers on the training split only and retrain/rescore for all tabular tiers (at minimum NEOWISE and Gaia), reporting the impact on (i) top-percentile membership overlap, (ii) rank correlations, and (iii) any headline fractions that use those tiers. If leakage-free reruns cannot be completed, remove the affected tiers from primary counts and from any “largest”/“rate” claims.

P3-E4 — Abstract p.1–2; §II.D p.5; throughout body and captions
Problem: Frequent use of internal provenance strings, pathnames, and run labels (e.g., pipelines/p3_anomaly_engine/…, r24conf_…, pod_runs/pod_provision_20260418.json) within the scientific narrative. PRD articles should not embed ephemeral run-paths, nor rely on audit-artifact filenames as part of the scientific argument.
Required fix: Move all pathnames and internal run labels to a Supplementary Materials or data-release README, and replace every in-body mention with a stable DOI/commit hash reference and a text description of what was validated. The main text must stand alone.

P3-E5 — Data availability p.23; Abstract p.2
Problem: Non-final archiving language. The manuscript says “will be publicly released with the arXiv posting,” “A Zenodo DOI will be minted at submission,” “will be made public.” PRD requires finalized, citable artifacts at acceptance. 
Required fix: Provide minted, versioned DOIs and immutable commit hashes for all datasets, weights, scripts, and figures referenced in the manuscript, and update the Data Availability section accordingly. Remove all future-tense placeholders.

P3-E6 — §III H p.13; Fig. 10 p.22; Abstract p.1
Problem: The NEOWISE “injection-recovery PASS (100%)” is a deterministic geometry mask check, not a detector sensitivity test, yet it is counted in the “3 PASS” headline numbers. Although caveats exist in body text, the top-level tally still conflates unlike gates.
Required fix: In every location where the “3 PASS” gate result is tallied (Abstract, §II.D Step 5, §VI.D and Conclusions), rephrase to “2 PASS (detector sensitivity) + 1 PASS (mask-geometry QA by construction).” The abstract must carry this explicit qualifier (“not a detector-sensitivity test”) next to the NEOWISE figure (it currently does; retain it) and the body must avoid any place where the three are summarized as equivalent PASSes without that qualifier.

P3-E7 — §IV.B p.15
Problem: Cramér’s V expression typesetting ambiguity. The text shows “Cramér’s V = sqrt(χ^2/(N·(k−1))) ≈ 0.0064” but the interim numeric layout omits the square root in the fraction while quoting the square-rooted value. This risks misinterpretation.
Required fix: Correct the formula display to unambiguously show V = sqrt(χ^2/(N(k−1))). Report both the pre-sqrt ratio (≈ 4.14 × 10−5) and V ≈ 0.00644, and keep the same interpretation.

P3-E8 — §IV.C p.15–16; Fig. 7; Dedup description and controls
Problem: Cross-survey deduplication control uses RA-only shifts at fixed Dec, which does not preserve local source density near survey edges or at high declination. The paper acknowledges this but still uses the result as a “heuristic control.”
Required fix: Provide a geometry-preserving null (e.g., random 3D rotations of positions on the sphere or HEALPix phase scrambling within survey masks) to estimate random-coincidence expectations, and update the “expected coincidences” sentences (e.g., §IV.A(b) and §IV.C) with these values and uncertainties.

P3-E9 — Abstract p.1–2; §I p.2; §VII p.22
Problem: “Largest-scale multi-archive anomaly search” claims are anchored only to a single-survey reference [11] and do not demonstrate that no larger-scale multi-archive anomaly search exists. PRD requires such superlatives to be substantiated.
Required fix: Either (a) provide a systematic comparative table of prior multi-archive anomaly searches (sample sizes, methods, catalogs released) demonstrating that this work is largest, or (b) soften all superlatives to “to our knowledge” and restrict comparisons to precisely documented baselines.

P3-E10 — Abstract p.1–2; §V p.18–19; §VII p.22
Problem: Juxtaposition of σ(fNL) Fisher forecasts and NANOGrav γ significance without an explicit “not directly comparable” qualifier in the Abstract. The body contains such disclaimers, but the abstract places these next to each other.
Required fix: Add a sentence in the Abstract explicitly stating that the σ(fNL) Fisher forecast and the NANOGrav spectral-index significance are derived from different observables and statistical frameworks and are not directly comparable; neither constitutes a detection.

MAJOR (significant revision)

P3-M1 — §II.B p.4; §III A p.8
Problem: DESI S-threshold calibration. The absolute S > 5 threshold is anchored to DESI (µval ≈ 0.0287 ⇒ S > 5 → MSE ≈ 0.143 implies σval ≈ 0.0229). However, the training pool contributes to the scored set, and only k-fold/OOD stability on the 47k pool is reported. No OOD stability is shown for the full DESI catalog vs. retrain seeds.
Required fix: Provide an OOD stability analysis for a large, unseen DESI subset at survey scale (not just the 103k SPARCL sweep that was not DESI-curated), reporting Jaccard overlap of top-k sets vs. retrain seeds and the production model. Confirm that the absolute S > 5 cut is stable at catalog scale.

P3-M2 — §III C pp.9–10; Fig. 3 right; Table I footnotes
Problem: SDSS cross-transfer vs. native-rescore axes. The paper shows S up to 1.9 × 10^11 on the cross-transfer S-axis. These are presented as “z-scored” but the scale is dominated by cross-domain µ, σ. While this is explained, it would benefit from an explicit sanity check that S is not numerically degenerate (e.g., float overflow, underflow).
Required fix: Add a brief numeric note confirming that the S computation remained stable (e.g., 64-bit accumulators, no inf/nan in the tail) and that these values are genuine reconstructions under the DESI µ, σ, not numeric artifacts.

P3-M3 — §IV.A p.13–14; Fig. 6
Problem: The “aggregate 58.8% SIMBAD-unmatched fraction” is computed at 3″ radius on top-100 for four surveys, while Table I per-survey unmatched use 5″. The paper notes the difference, but the figure could be misread as a discovery-rate headline.
Required fix: On Fig. 6, annotate the 3″ cone used for the aggregate explicitly in the axis label or caption, and add “database coverage metric; not a discovery rate” on the figure (matching the body text caveat). Consider moving the 58.8% number out of the abstract-level summary bullets entirely, deferring to the 17.8% genuine novelty fraction.

P3-M4 — §IV.C p.15–16
Problem: Budavari–Szalay/epoch-propagated matching is deferred, yet the 5″ dedup radius is stated as conservative for NEOWISE-sized PSF and strict for Gaia. This risks undercounting true cross-survey coincidences, especially with NEOWISE.
Required fix: Provide a sensitivity table of multi-survey coincidence counts using per-survey-appropriate radii (e.g., 1″ for Gaia/optical; up to 6″ for NEOWISE) and, if possible, adopt a simple probabilistic cross-match (positional error ellipses only) to bound the effect on the 637 cross-survey coincidences.

P3-M5 — §V p.18
Problem: Fisher forecast calibration constants. The manuscript uses F0 = 1/(8.98)^2 and c = 0.0747 from a “5-α refit” without showing how c was obtained (data points, fit errors).
Required fix: Provide the α-grid, the fitted functional form, uncertainties on c, and demonstrate the robustness of the forecast envelope to reasonable c variations. Include a plot or table in an appendix.

P3-M6 — §III A p.8; Table II p.9
Problem: Reported GALAXY 95% CI “±0.02%” appears conservative; a binomial 95% interval for 0.75% on ~4.9M is ≈ ±0.0076% (normal approximation). The QSO interval ±0.003% is consistent.
Required fix: Recompute and report exact (Clopper–Pearson or Wilson) 95% CIs for both classes. If the ±0.02% value was chosen for another reason (e.g., systematics floor), state it explicitly.

P3-M7 — §III F p.11
Problem: Planck CAE top-200 patches include 152 training patches. Although the paper argues against memorization (over-representation in validation split), the released set still mixes train/val and is not held-out.
Required fix: Provide, in Supplementary, the ranking stability of training vs. validation subsets and a check that removing all training patches from the scored bank and rescoring does not materially alter the top-200 list (overlap, ρ).

P3-M8 — §III H p.13; Fig. 5
Problem: The NEOWISE “top anomaly” is presented with a qualitative physical interpretation (dust/AGN/giant). Without spectroscopy, this is speculative.
Required fix: Tone down the interpretation in the caption/body (e.g., “candidate scenarios consistent with photometry; requires follow-up”), or move the panel to Supplementary.

P3-M9 — §II.D p.5; gate thresholds
Problem: Heuristic gate thresholds (val loss ≤ 0.30 within ≤ 100 epochs; ≥ 50% recovery at 5σ; Jaccard ≥ 0.70/0.50) are acknowledged as heuristic. For a methodology paper, power/sensitivity choices should be justified.
Required fix: Provide a brief rationale for the chosen gate levels (e.g., empirical separations from FAIL/PASS across retrains, expected power at n=500 injections), and, where a gate sits close to a boundary (SDSS 64% vs 50%), report sensitivity to reasonable threshold changes.

MINOR (addressable without major rework)

P3-m1 — Abstract p.1; §III A p.8; Table II p.9
Problem: “∼98.7% of DESI anomaly clusters fall on sky-fiber, secondary-target, or filler spectra.” Recomputed: 1 − 2,468/190,015 ≈ 98.70% (ok). Please add the exact fraction and its binomial CI (e.g., ±0.03%).
Required fix: Report explicit fraction with CI once in §III A.

P3-m2 — §II.B p.4
Problem: Mixing “z-scored” with redshift z. Although you state the disambiguation, there are a few places where “z-score” appears near “redshift z” (e.g., SDSS figures).
Required fix: Globally replace “z-score” with “standardized score S” in figure labels/captions where both concepts appear.

P3-m3 — §III C p.9; Table I footnote ♡
Problem: Three SDSS thresholds/slices appear. The manuscript is careful, but a consolidated table would help.
Required fix: Add a small table listing SDSS thresholds vs. counts (S>5=12; top-1% S≥0.2051=19,253; continuity slice S≥0.1060=77,905) in §III C.

P3-m4 — §IV.A p.14
Problem: SIMBAD false-match density nSIMBAD ≈ 3.0 × 10−5 arcsec−2 used for 5″ cones → Pfalse ≈ 2.36 × 10−3. Good; please include the basis for nSIMBAD (e.g., object count/sky area) or cite source.
Required fix: Add a sentence or footnote citing the density derivation.

P3-m5 — §III F p.11; Table VI
Problem: Planck CAE training wall-clock “not preserved.” For completeness, report GPU-hours if retrievable, or remove the row of timing from the table footnote.
Required fix: Either provide an estimate with uncertainty or explicitly state “training wall-clock not recorded.”

NIT (cosmetic/editorial)

P3-n1 — Throughout
Problem: Hyphenation artifacts (e.g., “surveys—see,” “per-survey”), minor typos.
Required fix: Global proofread post-typesetting.

P3-n2 — Fig. 3 right panel
Problem: Axis units for S on a log–log scale with extreme dynamic range may be misread.
Required fix: Add “S (standardized reconstruction residual; DESI scale)” to axis label/caption.

P3-n3 — §VII bullets p.22
Problem: Mixed notation for σ(fNL)std vs. σ(fNL).
Required fix: Define σ(fNL)std once in the conclusions or use a consistent symbol, and avoid comparing to the Appendix C internal-normalization values without a boldface “not comparable” label.

Computation and arithmetic spot-checks (no action needed unless authors disagree)
- Ratios/percentages in the abstract and body check out: 195,829/2,685 ≈ 72.9×; 2,468/2,685 ≈ 0.92 (≈0.9×); 178/1,000 = 17.8% with SE ≈ 1.21%; LAMOST compression 44,075/2,054 ≈ 21.5×; SDSS compression 77,905/12 ≈ 6,492×; dedup compression 10,213/388,493 ≈ 2.629%; NEOWISE polar-cap fraction excess 3.9%/1.52% ≈ 2.57×; αjk significance 0.19/0.65 ≈ 0.29σ; Fisher mapping from F0 and c reproduces σ(fNL)=8.14, envelope [3.92, 8.98]; NANOGrav deviations 1.13σ and 4.61σ are consistent.
- Cramér’s V recomputes to ≈ 0.00644 given χ2 = 376,713, N = 378,280, k − 1 = 24,047.

Length and focus
The paper is long (29 pages) relative to the verified methodology contribution, in part due to numerous internal path references and audit artifacts embedded in the main text. I recommend a maximum of 22 pages for the main article, moving (i) run-path provenance, (ii) extended retrieval-failure/cross-transfer history, and (iii) detailed gallery panels to Supplementary Materials or a data-release document. The main text should focus on methods, validation, and headline results with rigorous, reproducible claims only.

## Summary recommendation
MAJOR REVISIONS

Justification
The work is ambitious and the authors are unusually candid about failure modes, but core methodological standards for PRD are not yet met. The eROSITA axis irreproducibility and Gaia preprocessing gaps are unacceptable for a methods paper; feature-scaling leakage must be removed; reliance on internal run-path artifacts must be excised from the main text; and dataset/weights/code DOIs must be finalized. Several methodological controls (geometry-preserving null for dedup, explicit α→σ(fNL) calibration details) must be added. Once these essential and major issues are addressed, the paper can be reevaluated.

---

## PASS 2 — self-critique findings (what initial review missed)

P3 — ADDITIONAL FINDINGS AFTER SECOND-PASS (A–J AUDIT)

P3-E11 — Table I Planck denominator/rate inconsistency (Abstract/Table I; §III F; Table I footnote ♢)
Problem: The Rate(%) cell for Planck is listed as 1.00% (200/20,000), but the released Path-C tier is the top-200 from a 2×10^5 native bank (0.10%). Ntotal in Table I also reflects the 20,000 cross-transfer input, not the 200,000 native-rescore bank used for the published selection. Although the caption footnote notes this, the table remains internally inconsistent and propagates into the total-row “bookkeeping rate.”
Required fix: Make the Planck row denominator self-consistent with the released selection. Either (a) change Rate to “fixed-count (200); N/A” and annotate Ntotal with both inputs (“20,000 cross-transfer; 200,000 native”), or (b) report 0.10% and set Ntotal = 200,000 for the native Path-C row. Update the total-row “Rate” or mark it explicitly as “not a rate” when fixed-count tiers are present.

P3-M11 — Gate epoch-limit ambiguity (Path-C Step 1; §II D p.5; §III F; Table VI footnote †)
Problem: Step-1 gate text reads “retained if (a) validation loss ≤ 0.30 after ≤ 100 epochs, or (b) injection-recovery ≥ 50% at 5σ.” The native Planck CAE ran a 150-epoch schedule and is retained by criterion (b). The current wording leaves it unclear whether the ≤100-epoch limit applies to both branches or only to (a).
Required fix: Clarify that the ≤100-epoch limit applies only to criterion (a) and that criterion (b) imposes no epoch cap. If the 100-epoch limit was intended globally, justify the Planck exception or rerun within the stated cap.

P3-M12 — Injection–recovery uncertainty not shown (Fig. 10; §II D Step 5; §III C/D/F/H)
Problem: Recovery fractions (e.g., SDSS 64% at 5σ) are presented as point values without binomial error bars. With n=500 plants, the 1σ binomial CI at 64% is ~±4.2%, i.e., the margin vs the 50% gate is modest.
Required fix: Add binomial CIs (or shaded bands) for all recovery curves at each amplitude in Fig. 10 and quote the 5σ CIs in text for the PASS/FAIL determinations.

P3-M13 — Appendix E Eq. (E1) dimensional clarity (Appendix E)
Problem: The quantity ρi in Eq. (E1) is not defined dimensionally. The formula mixes log10(12π^2), fi, fyr, and Tobs in a way standard for strain/cross-power conventions, but the exact convention (characteristic strain vs energy density vs timing-residual power) is not stated. Units of A and normalization of ρi are therefore ambiguous.
Required fix: Define ρi and A explicitly (e.g., “ρi ≡ log10 Cii with Cii in s^2; A is the strain amplitude at fyr,” or the precise PTA convention used), and verify unit consistency in (E1). Cite the standard PTA reference for that normalization.

P3-M14 — Random-coincidence estimate for “≲10” lacks a method (Section IV C, “7-way 5″ dedup… expected random coincidence contribution is ≲10”)
Problem: The “≲10” expected chance coincidences across all survey pairs are quoted without a stated procedure (footprint masks, local density, or rotation-based null).
Required fix: Provide the method (e.g., full-sky rotation scrambling within masks or HEALPix-phase randomization) and uncertainty for this global expectation, or remove the number.

P3-m10 — Dedup audit precision (Section IV C; FoF audit)
Problem: The “maximum pairwise separation is 4.999″” suggests rounding at the 0.001″ level; the decision boundary is reported as “≤5″.”
Required fix: State the numerical precision and exact comparison operator used in the dedup (≤ vs <), and round max distances to a precision that does not suggest false accuracy.

P3-m11 — DESI×SDSS RA-shift control vs geometry-preserving null (Section IV A(b) and §IV C)
Problem: In one place you quote “empirical RA-shifted-control expectation 2.75” for DESI×SDSS 3″ matches, but the main dedup analysis (rightly) cautions that RA-only shifts do not preserve geometry.
Required fix: Replace the RA-shift expectation with a geometry-preserving null (random 3D rotations or within-mask scrambling) and quote the revised expectation and uncertainty in both places where that expectation is used.

P3-m12 — Table/figure consistency for “fixed-count tiers” (Table I; §III E/F/H)
Problem: The Rate column mixes measured rates and predetermined fixed-count tiers (Planck, Gaia, NEOWISE, eROSITA), with clarifying footnotes but still headline-like percentages in the main cells.
Required fix: Replace all fixed-count tier rates with “fixed-count (N); N/A” in the Rate column to avoid misinterpretation at a glance, and rely on footnotes for context.

P3-m13 — Fig. 5 plate scale/size mismatch (Fig. 5 caption)
Problem: The caption states “256 × 256 pixels (108″ × 108″).” DESI LS DR9 has 0.262″/px, so 256 px correspond to ~67.1″ per side, not 108″.
Required fix: Correct the angular size (≈67″ × 67″), or state the resampling scale used if different from LS DR9 native 0.262″/px.

P3-m14 — Abstract/body minor inconsistency on Planck “rate” (Abstract p.1; §III F; Table I)
Problem: The Abstract calls Planck “top-1%” (relative to 20,000 cross-transfer patches) while the released tier is top-200 of 200,000 native patches (0.1%). The body explains this, but the Abstract may mislead.
Required fix: In the Abstract, append “(fixed-count top-200 in native 200k bank; 0.10%)” to avoid confusion.

P3-m15 — Explicit radius on DESI SIMBAD 0.2% top-10k check (Section III A)
Problem: The DESI top-10k SIMBAD match rate (0.2%) does not state the cone radius at that point (later you standardize on 5″).
Required fix: Add “(5″ cone)” when reporting the 0.2% to keep all radii explicit.

Explanation
This second-pass focused on cross-table consistency, caption–body alignment, equation units, and additional null-control clarity. Most arithmetic spot-checks remain consistent, and several earlier issues (eROSITA irreproducible axis, Gaia preprocessing, leakage scalers, superlative claims, mask-geometry PASS conflation, and dedup nulls) were already flagged in the first review. The new items above aim to remove residual internal inconsistencies, clarify gate definitions and uncertainties, and correct a concrete plate-scale error in Fig. 5.