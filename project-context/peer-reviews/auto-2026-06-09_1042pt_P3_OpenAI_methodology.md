# P3 auto-2026-06-09_1042pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7615 chars)
**Wall time**: 258.4s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies …”

Scope of review
I evaluated the methodology and statistical rigor, consistency of definitions and thresholds across surveys, error propagation, dimensional analysis, arithmetic checks for all quoted ratios/percentages, internal cross-references, and whether sigma-level statements and Bayes factors are used appropriately. All figures, tables, and equations were audited for internal consistency.

Findings

ESSENTIAL (paper cannot be accepted without these fixes)

P3-E1 (Sec. V; p. 11; Sec. VI.D(i); p. 13; Table IV; p. 14)
Problem: Dimensional/definition error in the Fisher “positivity-respecting” form. Text states “1/σ(fNL)^2 = F0 + c α^2 with F0 = 1/8.982 and c = 0.0747.” If σstd = 8.98 is the baseline single-tracer forecast, then F0 must be 1/σstd^2 = 1/(8.98)^2 ≈ 0.01239, not 1/8.98 ≈ 0.1113. The printed F0 is off by a factor ≈ 9, and as written implies σ(α=0) = sqrt(8.98) ≈ 2.996, which contradicts both the baseline and your numerical results. Although several reported σ values (e.g., 8.14 for α=0.19, envelope [3.92, 8.98]) numerically match the corrected F0, the displayed formula and value for F0 are wrong in multiple places.
Required fix: Correct F0 everywhere to F0 = 1/σstd^2 with σstd = 8.98; recompute and re-verify every occurrence that uses or cites F0, including Sec. V, Sec. VI.D(i), Table IV, and any derived envelope statements. Explicitly state σ = 1/sqrt(F0 + c α^2). Add a one-line check showing that α=0 recovers σstd.

P3-E2 (Table I + footnotes; pp. 6–7; Sec. III.C; p. 6)
Problem: Inconsistent and incorrect threshold labelling and denominators for SDSS DR18. You simultaneously use:
- “Input: 2,304,830 spectra” (Sec. III.C),
- “native re-score complete across 1,925,279 DR18 spectra” (Table I footnote, ♡),
- “77,905 (3.38%)” cross-transfer anomalies (clearly 77,905/2,304,830),
- and you call 77,905 a “top-1% continuity slice S ≥ 0.1060” on the 1,925,279-spectrum set, while later stating the “harder top-1% score-knee” yields 19,253 objects.
These cannot all be true. 1% of 1,925,279 is 19,253, not 77,905. 77,905/1,925,279 ≈ 4.05%.
Required fix: 
- Reconcile the denominators: define clearly (and once) the SDSS sample used for each count (2.30M vs 1.93M), including all quality cuts and why the counts differ.
- Correct the “top-1% continuity slice” label for 77,905 to the correct percentile (≈ top-4.05%) or provide the correct N if it is truly top-1%.
- Present a single, unambiguous table listing, for SDSS: Nprocessed, N(top-1% by the survey’s own S), N(S>5), and any additional “score-knee” figures, each with the denominator and percentile explicitly stated.

P3-E3 (Table V; p. 16)
Problem: Physically implausible training time units for the Planck native convolutional autoencoder. The table lists “Train time (s) … Planck CMB … 10.6†” with 2×10^5 patches and a 1.1M-parameter CNN; 10.6 s is impossible on an A100 for the stated workload. Given that DESI/SDSS/LAMOST FC AEs list 1.2–3.6 ks, the Planck entry is almost certainly mis-unitized.
Required fix: Correct the units for Planck training time (likely hours or kiloseconds) and provide the actual wall-clock with hardware spec. Recheck and correct the ACT row too (even though quarantined) if needed for consistency.

P3-E4 (Sec. IV.D; p. 10)
Problem: “Planck × ACT cross-correlation: Null result” is asserted without a quantitative statistic or significance test. Statements like “do not cluster above random overlap” and qualitative attributions (scanning/noise differences) need a testable metric (e.g., cross-correlation function, randomization tests, p-value or effect size with uncertainty).
Required fix: Provide the cross-correlation estimator, the measured amplitude with uncertainty (jackknife or bootstrap), and the null test/p-value. If you cannot compute this rigorously for this submission, the claim must be softened to a qualitative observation and moved to an appendix, explicitly labelled as hypothesis-generating only.

P3-E5 (Sec. II.B; p. 3; cross-ref forward to VI.D(b))
Problem: Broken internal reference. You write “see §VI D (b) for the full OOD reconciliation” but Sec. VI.D uses roman numerals (i), (ii), not lettered (b), and no corresponding “(b)” exists.
Required fix: Fix the cross-reference to the correct subsection ID.

P3-E6 (Sec. IV.B; p. 9)
Problem: HEALPix pixel count inconsistent with Nside=64. You state “across 38,330 HEALPix pixels (Nside = 64)” with dof=38,329. Nside=64 has 12 Nside^2 = 49,152 pixels. If a mask or footprint selection reduces to 38,330, this must be explicitly stated (and how the mask is constructed) because the χ^2 value and dof depend on it.
Required fix: State the sky mask/footprint used to select 38,330 pixels; explain the dof calculation and whether empty/zero-exposure pixels were excluded. Otherwise the χ^2 statistic is uninterpretable.

P3-E7 (Data availability; p. 15)
Problem: Code/data are stated as “private pending arXiv acceptance; public upon acceptance.” PRD requires reproducibility at publication; a significant fraction of results (e.g., object lists, thresholds) rely on the external repository.
Required fix: Make the dataset and code publicly accessible at the time of acceptance (preferably at submission), or deposit as PRD Supplemental Material with a DOI. State a fixed DOI/URL in the manuscript.

P3-E8 (Method harmonization; Table I + Sec. II.B–D; pp. 5–7)
Problem: The main anomaly-rate comparisons across surveys mix different, sometimes ad hoc, thresholding schemes (absolute S>5 for DESI; survey-dependent percentiles; eROSITA knee on a different detector; top-1% fixed-count for Gaia/NEOWISE/Planck). You do acknowledge non-comparability in footnotes, but the paper still quotes and plots cross-survey “rates” (e.g., Fig. 1 caption, Table I) as if comparable.
Required fix: Provide a harmonized results table where each survey reports a consistent percentile-based selection (e.g., top-1%) and, separately, the survey’s native S>5 absolute-cut count if used. For all rate comparisons in the text, reference only the harmonized table. Alternatively, explicitly mark all cross-survey “rates” as not comparable wherever they appear.

MAJOR (significant revision required)

P3-M1 (Conclusions item 6; p. 14 vs. Sec. II.B; p. 3)
Problem: Inconsistent OOD stability statistic. The conclusions list “OOD control-vs-control 0.874 (PASS)”. Earlier, Sec. II.B reports the production-vs-5-seed-control Jaccard J̄prod×ctrl = 0.732. The 0.874 figure and its construction are not described earlier.
Required fix: Add a subsection describing the “control-vs-control 0.874” computation (sample, seeds, definition), and reconcile it with the 0.732 figure. Present both with uncertainties or ranges, and explain their intended use.

P3-M2 (Sec. VI.D(ii); Fig. 7; p. 13)
Problem: Injection–recovery methodology for Gaia/eROSITA/LAMOST lacks critical detail: how is the per-object noise σ defined; how are injections added (feature-space vs latent space vs raw photometry/spectra); how are detection thresholds handled per survey; and how are recovery fractions aggregated?
Required fix: Provide a compact methods box (or appendix) defining σ, the injection morphologies for each survey, sample sizes per amplitude, and the exact recovery criterion. Include error bars on the recovery curves in Fig. 7 (binomial ±1σ at least).

P3-M3 (Sec. IV.A; pp. 8–9)
Problem: 17.8% “genuine novelty fraction” lacks uncertainty. A 178/1000 binomial fraction has a clear statistical uncertainty; moreover, the catalog list may be incomplete (cross-match incompleteness, surface density priors).
Required fix: Report a binomial confidence interval (e.g., Wilson 68%/95%) on 17.8%; briefly discuss systematic uncertainties (choice of 20 catalogs, 5″ radius). Make clear that this is valid only for the top-1,000 DESI stratum.

P3-M4 (Sec. III.C; p. 6; Fig. 2 right panel)
Problem: The extreme SDSS cross-transfer S values (up to 1.9×10^11) arise from a z-scored reconstruction error but the normalization set (μval, σval) is not stated for SDSS cross-transfer (trained on DESI). Without these, the scale of S is uninterpretable, and could indicate numerical instability.
Required fix: Provide μval and σval used to z-score SDSS cross-transfer MSE (or state explicitly that S is computed with DESI μval, σval). If different scalings are used in different contexts (cross-transfer vs native), state both, and ensure figures and thresholds reference the correct axis.

P3-M5 (Sec. IV.C; p. 10)
Problem: “Expected random coincidence contribution ≲ 10 across all survey pairs against 637 observed multi-survey clusters” is asserted without showing the surface densities, sky fractions, or the analytic/probabilistic model used.
Required fix: Provide the calculation or a reference-quality derivation (pairwise sky densities, matching radius, footprint overlaps) that yields ≲ 10, with uncertainty bands. Otherwise, soften the claim.

P3-M6 (Sec. V A; p. 12; Appendix E; pp. 16–18)
Problem: Savage–Dickey Bayes factors are quoted (BMB/free = 3.23; BSMBHB/free = 4.52×10−4; hence BMB/SMBHB ≈ 7.14×10^3) without showing how the posterior density at the nested parameter value is estimated (KDE bandwidth, sampling error) or the prior density normalization at that point (given finite bounds).
Required fix: Add a short paragraph in Appendix E describing numerical details: how you evaluate posterior density at γ = 3.0 and 4.33 (KDE kernel, bandwidth selection), and the prior density factor for the stated uniform prior. Quote numerical uncertainties on the Bayes factor estimates (e.g., via bootstrap).

P3-M7 (Sec. III.B; p. 5)
Problem: The z ≈ 6 quasar-candidate set (12 objects) is only described qualitatively, with key identifiers deferred to the external repository. For a PRD methods paper tying cosmology to tracer populations, this is insufficient.
Required fix: Include a table in the manuscript (main text or appendix) listing coordinates, redshifts, per-arm sub-scores, and a brief classification for the 12 candidates.

MINOR (address but paper can proceed)

P3-m1 (Sec. II.D; p. 4)
Problem: Duplicate phrasing: “reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository).”
Required fix: Remove the duplicated parenthetical; keep a single, clear statement.

P3-m2 (Sec. III.A; p. 5; Table VI; p. 16)
Problem: Minor tension between text and table: the text emphasizes Z-dominant top scores (S = 25.2, 24.6, 24.5), while Table VI lists Z-dominant with “score range 5.1–25.2,” and only 19 Z-dominant objects. This is fine but could be misread as implying Z-dominant dominate the tail.
Required fix: Add a one-sentence clarification that Z-dominant are rare but occupy the extreme-score tail.

P3-m3 (Fig. 1 caption; p. 4; Table I; p. 6)
Problem: Figure 1 shows the cross-transfer baseline including ACT, while the main text emphasizes ACT is quarantined in Path-C. The caption explains, but readers may still conflate with canonical results.
Required fix: Add “Diagnostic only; not used for science results” to the first line of the Fig. 1 caption.

P3-m4 (Sec. III.H; p. 9; Fig. 4)
Problem: The NEOWISE top anomaly “score = 11.5” appears on the canonical-S axis but the survey’s μval and σval are not given anywhere.
Required fix: Provide μval and σval (or at least their order-of-magnitude) for NEOWISE in the methods or a footnote so that S values are interpretable.

P3-m5 (Bibliography; pp. 19–20)
Problem: Ref. [33] note about “publication-year 2024; bibkey retained as Heinrich2023” is an internal bookkeeping remark embedded in the reference text.
Required fix: Move such notes to a footnote or remove; keep references in standard journal style.

P3-m6 (Sec. II.C; p. 3)
Problem: Wall-clock accounting mixes inference, I/O, retraining, and a pod-restart anecdote. This is informative but could be cleaner.
Required fix: Consider moving detailed timings to an appendix table with consistent units.

NITS (cosmetic)

P3-n1 Various
- Ensure consistent use of “×” (times) and scientific notation spacing (e.g., 7.1×10^3 vs 7.14×10^3 used elsewhere).
- Standardize significant figures across rates (e.g., report 0.87% as 0.870% if others are at 3 s.f.).
- Ensure consistent capitalization of “Galactic” vs “galactic”.

Length and focus
At 20 pages, the manuscript is dense with catalog operations and survey-by-survey caveats. For PRD, which prioritizes methodological rigor, I recommend streamlining the survey operations narrative (Sections III–IV) by:
- Consolidating threshold definitions into a single harmonized table,
- Moving descriptive/operational timing details to appendices,
- Keeping the cosmology-facing methodology (Fisher formalism, bias measurement, injection-recovery protocols) in the main text.
Target length: 15–17 pages after consolidation.

Sigma comparability
Different σ notions are used: (i) posterior standard deviation for γ in the PTA analysis (parameter-shift “+1.13σ”), (ii) Fisher forecast σ(fNL), (iii) injection amplitude multiples of noise σ. You generally keep contexts distinct and add caveats; however, please insert explicit reminders when two σ’s appear in close proximity (e.g., Abstract last sentences; Sec. V header paragraph) that they are not directly comparable.

Audit of abstract and conclusions scalars
- 378,280 unique anomalies; 378,080 point-source + 200 patches: consistent with “Path-C unique” row and footnote explanation.
- “~141× the size of the largest prior single-survey anomaly catalog [11]”: 378,080 / 2,685 ≈ 140.8. OK.
- “DESI-only axis … ~73× like-for-like increase”: 195,829 / 2,685 ≈ 73.0. OK.
- “17.8% genuine novelty fraction”: 178/1,000. OK (but add CI; see P3-M3).
- “21.5× LAMOST rate compression”: 44,075 / 2,054 ≈ 21.46. OK.
- “~6500× SDSS rate compression”: 77,905 / 12 ≈ 6,492. OK, but see P3-E2 about mislabelled “top-1%”.
- “DESI 5-fold Jaccard 0.862”: matches Sec. II.B. OK.
- Six injection–recovery gates: SDSS 64%, Planck 100%, NEOWISE 100%, LAMOST 5.8%, Gaia 5.2%, eROSITA 1.2%: matches Fig. 7 and text. OK.
- “αjk = 0.19 ± 0.65; σ(fNL) = 8.14 with envelope [3.92, 8.98]”: Numerically OK with corrected F0 (see P3-E1). The printed F0 value is wrong and must be fixed.
- NANOGrav “γ = 2.567 ± 0.382; +1.13σ from 3.0; +4.61σ from 4.33; BMB/SMBHB ≈ 7.1×10^3”: arithmetic checks out.

Additional recommendations
- Provide a compact “Thresholds and Gatekeeping” table in the main text that lists, for each survey: Nprocessed, training pool size, μval, σval (if applicable), S-threshold(s) used, anomaly count(s) at each threshold, and whether the injection–recovery gate passed. This will greatly improve clarity.
- For spatial analyses, either remove the χ^2 uniformity test (since selection functions dominate) or move to appendix with a clear caveat and mask definition (see P3-E6).

## Summary recommendation
MAJOR REVISIONS

Justification: The manuscript contains several critical methodological inconsistencies and a key dimensional error in the Fisher forecast formula. Threshold labelling for SDSS is inconsistent and misleads about percentiles; training time units for the Planck CNN are clearly wrong; the Planck×ACT “null” needs a quantitative test; and the spatial χ^2 analysis lacks mask specification. These are fixable, but they must be corrected for PRD-level methodological rigor. The cosmology-facing results are otherwise promising and, with the required corrections and clarifications, the paper could meet PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P3-E9 (Sec. IV.A; Fig. 5; Table I)
Problem: The aggregate SIMBAD-unmatched fraction “58.8%” is inconsistent with the per-survey fractions and counts shown elsewhere. Using the six surveys with SIMBAD cross-matching in Table I (DESI 195,829 at 99%; SDSS 77,905 at 90%; LAMOST 44,075 at 50%; eROSITA 298 at 68%; NEOWISE 436 at 45%; Gaia 500 at 27%) yields:
- Unweighted mean: (99+90+50+68+45+27)/6 = 63.2%, not 58.8%.
- Count-weighted mean: 286,560 unmatched out of 319,043 total = 89.8%, not 58.8%.
If DESI’s fraction is only measured on its top-10k, you must not mix that with full-catalog totals for other surveys without harmonization.
Required fix: Recompute and report the aggregate on a consistent basis (same strata and denominators). If you intend a different aggregation (e.g., unique-object level after dedup, or a restricted RA/Dec footprint), state the exact construction and provide the inputs so the 58.8% can be reproduced.

P3-E10 (Appendix C Fig. 8 vs. Sec. V and Table IV)
Problem: Incoherent Fisher baselines. Sec. V/Table IV adopt σstd = 8.98 (also used to define F0), but Fig. 8 caption says “single-tracer baseline (σ = 16.85)” and “dense-tracer limit (σ = 11.71)” for the “canonical 5-tracer configuration of §V.” These are incompatible with the σstd = 8.98 baseline used throughout the main text (and with the positivity form that relies on it).
Required fix: Unify the forecasting setup. Either explain that Fig. 8 refers to a different experiment/assumption set (and cross-reference where that setup is defined), or recompute Fig. 8 to the same baseline (σstd = 8.98). State clearly which baseline σstd underlies F0 everywhere. As printed, readers cannot reconcile Section V with Appendix C.

P3-E11 (Fig. 6 vs. Sec. IV.C and Abstract)
Problem: Contradiction in the “known QSO” cross-survey match. Panel (a) DESI shows Score = 3.2 and panel (b) SDSS shows Score = 2.8 — both below your anomaly thresholds (DESI uses S > 5; SDSS cross-transfer or native also exceeds 5 for inclusion). Yet the text says “Known QSO … independently flagged by both surveys.” It was not flagged as an anomaly by either survey at your stated thresholds.
Required fix: Correct the claim. Either (i) clarify that this object is shown only as a cross-survey spectral consistency check and was not in the anomaly catalogs, or (ii) fix the plotted scores/threshold explanation if these S values are not on the same scale used for selection.

P3-E12 (Abstract vs. Data availability)
Problem: Abstract claims “The catalog, model weights, and reproducibility scripts are publicly released,” but the Data availability section says “private pending arXiv acceptance; public upon acceptance.”
Required fix: Make these consistent. If public now, provide the working public DOI/URL in both places. If not yet public, soften the Abstract to “will be released upon acceptance” and provide an embargoed DOI that will resolve at publication.

P3-E13 (Sec. III.C Table II vs. SDSS SIMBAD fraction elsewhere)
Problem: Table II says “Uncategorized 52.7% … reflects objects that match a SIMBAD entry but lack a specific astrophysical type classification,” which alone would imply >40k SIMBAD matches among 77,905 SDSS anomalies. Elsewhere you state SDSS SIMBAD-unmatched is 90% (i.e., only ~7.8k matches).
Required fix: Resolve the contradiction. If “Uncategorized” refers to your internal emission-line taxonomy, remove the SIMBAD interpretation from the Table II note. If it truly reflects SIMBAD matches, correct the 90% unmatched statement and all downstream uses.

MAJOR

P3-M8 (Sec. II.B; Sec. III.B; per-arm sub-scores)
Problem: The per-arm sub-scores rB, rR, rZ are used for selection (e.g., “Z-arm dominated” high-z candidates) but their exact definition and normalization are not given. It is unclear whether rB,R,Z are raw MSEs, re-z-scored by per-band validation statistics, or fractions of the total S, and how they sum to the reported total S.
Required fix: Provide the explicit formulae for rB, rR, rZ, including any normalization and how they relate to S. State the bandpass wavelength boundaries (including edge handling/downsampling) and whether per-band μ,σ were used.

P3-M9 (Fig. 3 vs. text; cluster counts)
Problem: The caption/text say “3 latent-space populations,” but the left panel contains a legend string (“14 clusters, 95.4% clustered”) suggesting HDBSCAN produced 14 clusters. This is confusing about what is being shown and how the 3 populations relate to those clusters.
Required fix: Quantify how the 14 HDBSCAN clusters map into the 3 “populations” (e.g., cluster groups A/B/C with sizes). Add those numbers in the caption or text so readers can reconcile the statements.

P3-M10 (Appendix E, end of first paragraph)
Problem: Mis-citation. “Chain … and fitter script are deposited in the companion data repository [18]” uses [18] to cite NANOGrav, not your repository. This makes it impossible to locate your scripts from the text.
Required fix: Replace [18] with the correct repository citation/URL/DOI. If you intend both (NANOGrav dataset and your code), cite both explicitly.

MINOR

P3-m7 (Sec. III.A; p. 5)
Problem: Duplicated/near-duplicated prose. The paragraph starting “Across the 6.5 million spectra in DESI DR1 …” repeats core elements of the previous paragraph (Z-dominant tail, anomaly rates by class).
Required fix: Deduplicate for clarity.

P3-m8 (Table I footnote ♠ vs. Sec. II.D stratification)
Problem: The “catalog-grade tier” in the LAMOST footnote lists “DESI + SDSS native + eROSITA + Planck native + Gaia + NEOWISE” yet earlier you caution that Planck patches are not point sources and should not be used in object-level analyses. This mixes strata and could confuse readers about what is “catalog-grade” for object-level science.
Required fix: Clarify that the catalog-grade point-source tier excludes Planck, and give the point-source-only count explicitly wherever “catalog-grade” is quoted.

P3-m9 (Fig. 2 right; caption wording)
Problem: The caption says “spanning twelve orders of magnitude from the threshold (S=5) to S=1.9×10^11.” That span is ≈ 11.6, not “twelve” (and the lower end is not 1 by definition, so “orders” wording is awkward for a z-score-like axis).
Required fix: Reword to “about eleven orders of magnitude” or give the precise numeric span without the “orders” phrasing.

P3-m10 (Table I footnotes vs. Sec. VI.D indexing style)
Problem: Mixed caveat indexing styles: the text uses roman (i), (ii), … in §VI.D, Table IV uses lettered (a)–(j), and some footnotes reference “§VI D (v)” which could be read as roman numeral 5 or letter v.
Required fix: Standardize the caveat indexing (all roman or all letters) and update all cross-references accordingly.

NITS

P3-n2 (Formatting)
- Several inline references to equations toggle between “Eq. 2” and “Equation (2)”; standardize.
- Ensure consistent hyphenation of “cross-transfer” and capitalization of “Galactic.”
- Use consistent significant figures for reported rates and percentages in the same table/paragraph.

Rationale for fresh findings
The new items were uncovered by explicitly recomputing aggregate rates from per-survey fractions (P3-E9), checking figure–text numerical consistency (P3-E11, P3-M9), comparing baselines across sections (P3-E10), cross-checking Table II’s SIMBAD note against earlier SDSS-unmatched rates (P3-E13), and scanning for cross-section contradictions (P3-E12, P3-M10). These issues are independent of those in the initial review and materially affect interpretability, internal consistency, and reproducibility.