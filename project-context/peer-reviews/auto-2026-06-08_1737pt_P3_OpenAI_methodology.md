# P3 auto-2026-06-08_1737pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9127 chars)
**Wall time**: 326.2s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies …” (20 pages)

Scope of this review
- Focus: methodology rigor, statistical validity, internal arithmetic and dimensional consistency.
- I audited the abstract, text, equations, figures, and tables for consistency and recomputed quoted fractions/ratios/sigma claims where possible.

Findings

ESSENTIAL (must fix before PRD consideration)

P3-E1 (Sec. V, p. 11; Table IV (i), p. 13)
Problem: Dimensional/arithmetical error in the Fisher forecast baseline term F0.
- Text: “1/σ(fNL)^2 = F0 + c α^2 with F0 = 1/8.982 and c = 0.0747 … inserting αjk = 0.19 gives σ(fNL) = 8.14.”
- Issue: If σstd = 8.98 is the single-tracer baseline, then F0 must be 1/σstd^2 = 1/8.98^2 ≈ 0.0124, not 1/8.982 ≈ 0.111. As written, (F0, c) are off by ≈ 9×, and 1/σ^2 would imply σ ≈ 3, not 8.14.
Required fix: Correct F0 to 1/σstd^2 = 1/8.98^2 (and anywhere else it appears), re-derive c accordingly, and recompute all dependent numbers (central σ(fNL), the [3.92, 8.98] “1σ envelope,” and any improvement percentages). State clearly which baseline σstd is used and propagate significant figures consistently.

P3-E2 (Abstract p. 1; Sec. V p. 11; Conclusions p. 14)
Problem: Inconsistent improvement percentage for σ(fNL).
- Claim: “σ(fNL) = 8.14 … 7.9% improvement … baseline σstd = 8.98.”
- Check: (8.98 − 8.14)/8.98 = 0.0933 → 9.33% improvement, not 7.9%.
Required fix: Correct the percentage wherever stated, or explain if a different baseline or rounding is used. This must be numerically consistent with the corrected F0 in P3-E1.

P3-E3 (Table I footnotes ♡ and main text Sec. III C, p. 6–7)
Problem: Contradictory SDSS DR18 “top-1%” characterization and inconsistent N.
- Footnote ♡ says “headline … 77,905 at S ≥ 0.1060 is the top-1% continuity slice,” yet 77,905/2,304,830 = 3.38% (your own line) and 77,905/1,925,279 = 4.05%. Elsewhere you also say 19,253 is “top-1%”.
- You also state “native re-score complete across 1,925,279 DR18 spectra” vs. “SDSS DR18 provides 2,304,830 spectra.”
Required fix: Resolve the contradiction. Clearly state the exact N used for each SDSS statistic, justify the 1,925,279 selection (quality cuts?), and correct all “top-1%” labels. Provide a single consistent mapping: (N used) → threshold → count → rate. Update Table I footnote ♡ and §III C accordingly.

P3-E4 (eROSITA threshold axis inconsistency; Table I footnote §, p. 6; Sec. III E/Table III note, p. 7)
Problem: The symbol S is used inconsistently for different detector axes; threshold attribution conflicts.
- Table I footnote says eROSITA’s headline “top-298 cap (equivalent to S > 0.259 on the eROSITA-native IsolationForest raw-score axis)”.
- Section III E/Table III contradicts: “SBigAE … the axis on which the published 298-source catalog headline (S > 0.259) is defined,” and SIF,raw is the IsolationForest axis.
Required fix: Decide and state unambiguously which detector (BigAE vs IF) defines the published eROSITA 298-source set and on which score axis the 0.259 threshold sits. If you keep S as “canonical BigAE z-score,” never use S to denote IF raw scores; use SIF,raw or similar consistently. Audit and correct all occurrences.

P3-E5 (Aggregate SIMBAD-unmatched fraction; Fig. 5 and text Sec. IV A p. 10; Table I “Total … 58.8%” p. 6)
Problem: “Aggregate 58.8%” is ill-defined and not reproducible from the given per-survey numbers.
- Unweighted mean of the six per-survey rates (99, 90, 68, 50, 45, 27)% = 63.17%.
- Anomaly-weighted mean (using your cross-transfer anomaly counts per survey, excluding Planck) ≈ 89.8%.
- Median = 59.0%.
Required fix: Define explicitly how “aggregate 58.8%” is computed (weighting scheme and which N enter). Recompute the dashed line in Fig. 5 and the 58.8% text/Table I entry. If you intend a median, say so. If you intend a weighted average, show the weights.

P3-E6 (Fig. 9, p. 17)
Problem: Score labels grossly inconsistent with your defined DESI score scale; metric undefined.
- Figure title says “DESI DR1 Spectral Anomalies,” but labels read “AE=83518, 17663, 9240, …” while you state DESI S ∈ [5, 25.2] (Sec. III A; Table VI).
- You elsewhere note “AE printed as per-arm Z sub-score rZ” for a different panel, but rZ ≈ few, not 10^4–10^5.
Required fix: Define exactly what “AE” is in Fig. 9 (and its units/scale), and ensure it refers to a metric defined in Sec. II. If the objects are not DESI or the numbers belong to a different model/domain, correct the figure title. Prefer replacing with the canonical S and/or rB,rR,rZ values on the DESI scale to avoid confusion.

P3-E7 (Table V, p. 16)
Problem: Physically implausible Planck CMB training time; unit/scale error.
- “Planck CMB … 1.1M parameters … Train time (s): 10.6† … trained on 2×10^5 patches.”
- 10.6 seconds for a 1.1M-parameter conv autoencoder on 200k 64×64 patches is not credible and contradicts the earlier ∼42 h wall-clock description.
Required fix: Correct the units and value (likely hours or 10.6×10^3 s). Audit all training times for consistency with §II C. Provide error bars or at least ranges if measured.

P3-E8 (Notation consistency; multiple locations)
Problem: The paper asserts “S” is the canonical standardized reconstruction residual (Sec. II B, Eq. 2), but elsewhere reuses S for other detectors/axes (e.g., eROSITA; Table I footnote). This risks misinterpretation of thresholds and rates.
Required fix: Enforce unambiguous notation across the entire paper:
- Use SBigAE only for Eq. (2) (per-survey z-scored MSE).
- For IsolationForest, use SIF,raw (or IFscore).
- For CMB conv AE, define a dedicated symbol (e.g., SCMB) and its normalization.
Audit all figures, tables, captions, and footnotes; correct any misuse.

P3-E9 (SDSS Ns inconsistent; Sec. III C p. 6–7; Table I p. 6)
Problem: You report SDSS “Input: 2,304,830 spectra” but “native re-score complete across 1,925,279 DR18 spectra,” and then mix rates and thresholds across these different Ns.
Required fix: Provide a clear, single description of the SDSS sample(s) used: initial cross-transfer N, native re-score N, and why 379,551 spectra were excluded (quality flags? wavelength coverage?). Recompute all quoted percentages for the stated N and eliminate any cross-N comparisons unless corrected.

MAJOR (significant revision required)

P3-M1 (Cross-match methodology robustness; Sec. IV C p. 10)
Problem: Cross-survey deduplication uses a fixed 5″ radius across surveys with heterogeneous astrometry/PSFs and known proper motions (Gaia). You acknowledge under-matching for NEOWISE and plan a future probabilistic match, but the headline coincidence count (637) is sensitive to this choice.
Required fix: Provide a sensitivity analysis in the paper (not deferred): report multi-survey coincidence counts and unique-object compression for 3″, 5″, and 7″ radii, and quantify expected random coincidences per pair at each radius. Alternatively, implement a simple Budavari–Szalay-style probabilistic match with per-survey positional errors and Gaia epoch propagation for this analysis.

P3-M2 (DESI in-sample overlap and OOD instability; Sec. II B p. 2–3; Sec. VI D(b) Table IV p. 13–14)
Problem: The DESI score threshold S > 5 applied to curated DR1 yields 0.87%, but applied to a random uncurated SPARCL sweep flags >50% of spectra (you attribute this to catalog curation). This is a large domain shift that undermines generalization of the 0.87% rate, and only partial controls are shown.
Required fix: Provide a more robust out-of-sample evaluation: define an OOD test set with the same curation as DR1, quantify the shift in the MSE distribution and S threshold transferability, and show that the 0.87% figure is stable under reasonable OOD perturbations. If not, qualify the 0.87% headline accordingly.

P3-M3 (Landy–Szalay two-point details; Sec. V p. 11)
Problem: The bias-ratio αjk derivation lacks critical details for reproducibility and error control (mask, random catalog generation, RR/DR normalization, edge effects, completeness, angular binning definition).
Required fix: Add a methods subsection specifying: the Landy–Szalay estimator used, sky mask, number density and construction of randoms, area-normalization, θ-bin edges, jackknife region definition, and the handling of survey systematics (fiber assignment, imaging depth). Provide a consistency check (e.g., fit stability under varying RR size and jackknife tiling).

P3-M4 (Fig. 2 right caption exaggeration; p. 5)
Problem: “spanning twelve orders of magnitude from the threshold (S = 5) to S = 1.9 × 10^11” is numerically incorrect: log10(1.9×10^11/5) ≈ 10.58.
Required fix: Correct the statement to a quantitatively accurate value (e.g., “~10.6 orders of magnitude”).

P3-M5 (Use/mix of SDSS cross-transfer vs native distributions; Sec. III C p. 6–7; Fig. 2 caption p. 5)
Problem: The text and figure juxtapose SDSS cross-transfer and native re-score distributions without a consistently labeled separation, potentially confusing which population underpins each quantitative claim (rates, thresholds, clusters).
Required fix: Clearly segregate cross-transfer results (for diagnostic only) from native re-score results (for any catalog statements). In captions and text, label each panel/number as “cross-transfer” or “native” and avoid combining them in a way that could be misread as a single distribution.

MINOR (address but paper can proceed)

P3-n1 (Duplication/typo; Sec. II D p. 3)
Problem: Repeated phrase: “reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository)”.
Required fix: Remove the duplicated clause.

P3-n2 (Style/terminology)
Problem: Frequent use of “PASS/FAIL” in all caps and “FAIL-with-diagnostic” reads as internal QA notes rather than scientific prose.
Required fix: Consider using “passes/fails [criterion]” in text and reserve all-caps for figure labels only if necessary.

P3-n3 (Planck/ACT usage clarity; Sec. III F and App. F)
Problem: While you quarantine ACT, you still use it for the Planck×ACT null test. The status is clear in Appendix F but could be restated briefly in the main text where the null result is reported.
Required fix: Add a one-sentence reminder in Sec. IV D that the ACT anomalies are from the quarantined cross-transfer set and the test is methodological only.

P3-n4 (Conclusions p. 14)
Problem: “OOD control-vs-control 0.874 (PASS)” appears in conclusions but is not introduced/sourced earlier.
Required fix: Provide the corresponding description and result in the body text (Sec. II B or VI D), or remove it from conclusions.

P3-n5 (Units/axes)
Problem: Some figures list “Probability density” without indicating normalization or binning; Planck “score” axis is unlabeled (CMB-specific metric?).
Required fix: Clarify axes units/normalization and, for Planck, name the score used (e.g., normalized MSE or latent distance).

P3-n6 (Reference [33] bookkeeping note; p. 19)
Problem: The reference includes editorial text “publication-year 2024; bibkey label retained …”.
Required fix: Remove internal editorial notes from the bibliography.

NIT (cosmetic)

P3-N1 (Hyphenation artifacts)
Problem: PDF linebreak hyphenation artifacts (“pro­cessed”, “sur­veys”) throughout.
Required fix: Clean typesetting before final submission.

P3-N2 (Rounding consistency)
Problem: Mix of 2 vs 3 significant figures across percentages and counts.
Required fix: Standardize (e.g., two significant figures on percentages unless otherwise warranted).

P3-N3 (Abstract wording)
Problem: “June 2026” date is fine; but repeated quantitative parentheticals could be streamlined.
Required fix: Optional; editorial polishing.

Verification of selected arithmetic/claims (spot checks)

- Path-C per-survey sum: 195,829 + 77,905 + 113,342 + 298 + 200 + 500 + 419 = 388,493; unique after 10,213 dedups = 378,280; compression = 10,213/388,493 = 2.629%. Consistent.
- Point-source vs CMB: 378,280 − 200 = 378,080 point sources. Consistent.
- “141× largest prior catalog” vs Liang et al. 2,685: 378,080/2,685 ≈ 140.8. Consistent.
- “DESI-only 73× increase”: 195,829/2,685 ≈ 72.9. Consistent.
- NEOWISE polar caps: observed 17/436 = 3.90%; uniform fraction in |becl| > 80° caps = 1 − cos(10°) = 1.519%; ratio ≈ 2.57×. Consistent.
- DESI anomaly rate: 195,829/22,504,897 = 0.00870 → 0.87%. Consistent.
- eROSITA published fraction: 298/930,203 = 0.032% (“top-0.03%”). Consistent.
- NANOGrav σ-shifts: (3.00 − 2.567)/0.382 = 1.13σ; (4.33 − 2.567)/0.382 = 4.61σ. Consistent.

Notes on length/scope
- The paper is long (20 pages including appendices) but attempts to cover a large multi-survey pipeline. Given the number of corrections required (especially to core statistical definitions and inconsistent counts/thresholds), I recommend tightening the presentation after the essential fixes. A target length of ≈16–18 pages could be achieved by moving some QA prose and extended footnotes into a concise Methods appendix.

## Summary recommendation
MAJOR REVISIONS

Rationale: The manuscript contains several core inconsistencies in statistical definitions and arithmetic (F0 dimensional error; inconsistent σ(fNL) improvement; contradictory SDSS “top-1%” and sample sizes; inconsistent use of S across detectors; ill-defined “aggregate 58.8%”; a figure with mislabeled/undefined score scales; and a non-credible Planck training-time entry). These go to the heart of methodological clarity and reproducibility and must be corrected. Once these essential issues are resolved and key methods details are added (cross-match sensitivity, two-point estimator specs, DESI OOD stability), the paper could meet PRD’s methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS AFTER SECOND-PASS AUDIT

ESSENTIAL (must fix before PRD consideration)

P3-E10 (Sec. II B, p. 2)
Problem: Threshold-family statement contradicts later SDSS usage.
- Text: “DESI DR1 and SDSS DR18 use an absolute canonical-S cut at S > 5.0.”
- Conflict: Throughout Sec. III C and Table I footnote ♡ you use SDSS top-percentile cuts (and explicitly highlight that S > 5 selects only 12 sources). This is not just the earlier “top-1%” inconsistency (P3-E3): here the methods section asserts the wrong threshold family upfront.
Required fix: Correct Sec. II B to reflect the actual SDSS thresholds used (cross-transfer top-1% continuity slice and native re-score thresholds), and explicitly segregate “diagnostic cross-transfer” from “native” usage.

P3-E11 (SDSS category logic vs SIMBAD match rate; Table II note p. 7 vs Sec. III C text)
Problem: Contradictory explanation of the “Uncategorized” class.
- Table II note says 52.7% “Uncategorized” reflects objects that match a SIMBAD entry but lack a type.
- Body text says SDSS anomalies are SIMBAD-unmatched at 90% (i.e., only ≈10% match SIMBAD).
Required fix: Clarify the taxonomy pipeline. If “Uncategorized” does not rely on SIMBAD types, rewrite the note; if it does, the 52.7% figure is incompatible with a 10% SIMBAD match rate. Provide a consistent, reproducible categorization rule.

P3-E12 (Appendix C vs Section V configuration mismatch; App. C Fig. 8 caption p. 15 vs Sec. V/Table VII)
Problem: Inconsistent “tracer/bin” configuration across sections.
- App. C Fig. 8: “canonical 5-tracer configuration of §V.”
- Table VII and Sec. V: repeatedly refer to the “full 7-bin Fisher result.”
Required fix: State unambiguously whether the forecasts in Sec. V and App. C are for 5 tracers or 7 bins (or if “bin” ≠ “tracer,” define both and where each is used). Make the configurations consistent across text, tables, and figures or label them as distinct scenarios with clear crosswalk.

P3-E13 (Mislabeling of uncertainty band; Sec. V p. 11 vs Table IV (i) p. 14)
Problem: The same [3.92, 8.98] band is called a “1σ envelope” in Sec. V and a “95% envelope” in Table IV (i).
Required fix: Decide which confidence level this band represents, recompute with the corrected F0/c from P3-E1, and use one consistent label everywhere.

P3-E14 (Cumulative training-time inconsistency; Table V p. 16 vs §II C p. 3)
Problem: Training-time column values are not credible collectively and contradict your own 32 h “native-retraining pass overhead.”
- Table V totals (summing all “Train time (s)”) are ≈ 8,300 s (~2.3 h). This is irreconcilable with the ~32 h overhead you attribute largely to retraining/processing beyond pure inference.
Required fix: Correct all training times (units and magnitudes), and reconcile with §II C’s wall-clock breakdown. If Table V reports per-epoch or per-checkpoint times, say so explicitly.

P3-E15 (Forecast σ scales inconsistent between Sections; App. C Fig. 8 vs Sec. V/Table VII)
Problem: σ(fNL) scales disagree without explanation.
- Sec. V/Table VII baseline: σstd = 8.98 (DESI-only). App. C Fig. 8 reports “single-tracer baseline = 16.85” and “dense-tracer limit = 11.71” for what is presented as the §V configuration.
Required fix: Explain the different baselines (different experiment, sky area, kmax, redshift binning?) and ensure Section V and Appendix C clearly state the setup assumptions so numbers are not conflated. If Fig. 8 is not the same experiment as Sec. V, relabel accordingly.

P3-E16 (Training set size claim vs actual; Sec. II D Step 1 p. 3 vs Sec. II B/III A)
Problem: Native-retrain Step 1 claims “2–5×10^5-spectrum” training subsets “for each survey,” but DESI is trained on 47,000 (Sec. II B, III A).
Required fix: Correct Step 1 to state the actual per-survey training-set sizes used (DESI 47k; others as appropriate), and avoid blanket statements that are untrue for at least one anchor survey.

P3-E17 (Epoch-limit inconsistency; Sec. II B p. 2 vs Sec. II D Step 1 p. 3)
Problem: Sec. II B says “up to 200 epochs with early stopping,” while the Step-1 gate is “validation loss ≤ 0.30 after ≤ 100 epochs.”
Required fix: Harmonize the epoch limits and explicitly note which limit applied to which survey/model.

MAJOR (significant revision required)

P3-M6 (Unsupported bound on dedup sensitivity; Sec. IV C p. 10)
Problem: The manuscript asserts that alternate cross-match radii “cannot change the unique-object count by more than the 10,213 total compression observed at 5″.” That bound is unjustified; increasing the radius can, in principle, produce additional merges far beyond the current compression.
Required fix: Remove the bound or justify it with an explicit sensitivity study. As requested in P3-M1, report multi-survey coincidences and unique-object counts for 3″/5″/7″ (and expected random overlaps), or switch to a probabilistic cross-match.

P3-M7 (Planck CMB patches counted in “catalog-grade tier”; Table I footnote ♠ p. 6 vs Abstract/§IV stratification)
Problem: You recommend using the 378,080 point-source tier for object-level science, yet in Table I footnote ♠ you include Planck map patches in the “catalog-grade tier” (stated as 264,938 unique objects).
Required fix: Make the catalog-grade tier definition consistent with the “point-source only” guidance. Report the catalog-grade point-source count explicitly (and separately list the 200 CMB regions if you retain them as a separate stratum).

P3-M8 (Per-arm residual definitions missing; Sec. II B p. 2; Sec. III A/B)
Problem: rB, rR, rZ are used for band-dominance and high-z selection, but their definitions (exact formula, normalization, windowing, noise weighting) are not provided.
Required fix: Define rB, rR, rZ precisely (units/normalization) so others can reproduce the band-dominance classification and the z≈6 selection cuts.

P3-M9 (High-z QSO redshifts; Sec. III B p. 5)
Problem: You report z = 6.0–6.23 for 12 candidates but do not state how z was measured (template fit? line centroid? pipeline redrock? uncertainties?).
Required fix: Add a short methods note on redshift estimation and provide an uncertainty or quality flag for each candidate (even if deferred to the repository).

P3-M10 (Top-200 DESI “0% artifact rate” lacks protocol; Sec. III A p. 4)
Problem: The claim is based on “spectral inspection” without a defined protocol.
Required fix: Describe the inspection procedure (number of inspectors, blind or not, criteria for artifact vs astrophysical, inter-rater agreement). Otherwise soften the claim and/or move it to a qualified statement.

MINOR (address but paper can proceed)

P3-n7 (Conclusions p. 14 and Sec. IV D p. 10)
Problem: The Planck×ACT “null” is based on the quarantined ACT cross-transfer anomalies. The caveat appears in App. F and Sec. IV D, but the Conclusions list it without reminder.
Required fix: In Conclusions (and where first reported), add a clause stating this is a methodological null using a quarantined ACT set, not a science-grade ACT result.

P3-n8 (Redundant/duplicated prose; Sec. III A p. 4–5)
Problem: The DESI per-class anomaly-rate paragraph appears twice with minor rewording.
Required fix: Remove duplication for clarity.

P3-n9 (p-value phrasing; Table I footnote § and §III E)
Problem: “hypergeometric two-sided p ≈ 0” is not appropriate scientific phrasing.
Required fix: Report a bound (e.g., p < 1e−x) based on numerical precision or a computed value.

P3-n10 (Random-overlap estimate; Sec. IV A(b) p. 9)
Problem: The statement “expected random coincidence contribution is ≲ 10 across all survey pairs” is given without a calculation.
Required fix: Provide the numbers used (surface densities, sky area, matching radius) or move this to an appendix with the calculation.

P3-n11 (Figure 6, caption p. 11)
Problem: “Score” is unlabeled as to which axis (SBigAE vs SCross-transfer). This is an instance-specific ambiguity beyond the global notation issue (P3-E8).
Required fix: Label each panel’s score with the detector/axis (e.g., SBigAE, transfer S, native S) to avoid confusion.

NIT (cosmetic)

P3-N4 (Ambiguous wording; Table I footnote ∥ p. 6)
Problem: “excluding ACT subtracts exactly 200 from both the input sum and the unique-object count” is ambiguous (appears to refer to total processed N as well).
Required fix: Rephrase to “subtracts 200 from the anomaly-count sum (not from the total processed N, which drops by 20,000 patches).”

P3-N5 (Axis range oddity; Sec. III F p. 7)
Problem: Planck native “score range [0.558, 0.621]” for top-1% anomalies is very narrow and unlabeled.
Required fix: Name the score (SCMB) and briefly explain its scale/distribution so the narrow span is interpretable.

Explanation
This second pass focused on arithmetic cross-checks, caption–body consistency, dimensional sanity of equations, internal cross-references, null-procedure comparability, abstract faithfulness, novelty support, appendix–main alignment, and stale-number signs. The items above are new relative to the initial report and target additional inconsistencies and missing methods details that affect reproducibility and interpretability.