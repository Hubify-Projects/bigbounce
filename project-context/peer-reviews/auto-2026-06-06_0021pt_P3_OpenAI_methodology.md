# P3 auto-2026-06-06_0021pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8679 chars)
**Wall time**: 329.1s

---

Referee report (methodology/statistics) — PRD submission: “Spectrally Unusual Sources at Scale: …”

Scope of this review
- Focus: statistical/methodological rigor, internal consistency, dimensional analysis, derivation chains, figure/table auditing, and arithmetic checks.
- I read the full manuscript (20 pages) including figures, tables, appendices, and captions. Findings below reference the PDF page numbers visible in the rendered document.

Overall assessment
The paper assembles a very large multi-survey anomaly catalog and attempts two cosmological applications. However, there are multiple essential methodological inconsistencies, unresolved placeholders/figure references, and internal arithmetic conflicts that preclude publication in PRD in its current form. In particular: (i) the Fisher-forecast formula uses an incorrect baseline term (F0) in the main text (dimensional/numerical error), (ii) key figure references are unresolved (“Fig. ??”), (iii) the SDSS “top-1%” slice is arithmetically inconsistent with the quoted counts, (iv) several training times in Table V are not credible given the stated training schedule, and (v) baselines for σ(fNL) are internally inconsistent between the main text and Fig. 8. There are also sample-selection ambiguities and duplicated text that must be corrected.

Findings (ESSENTIAL / MAJOR / MINOR / NIT)

ESSENTIAL

P3-E1 (Section V, page 10; Table IV (i), page 13)
Problem: Misdefined Fisher baseline term F0 in “positivity-respecting” form. Text states “1/σ(fNL)^2 = F0 + c α^2 with F0 = 1/8.982 and c = 0.0747,” and Table IV repeats “F0 = 1/8.982.” This is dimensionally/numerically inconsistent with the stated single-tracer baseline σstd = 8.98. For α = 0 the formula should give σ = 8.98, which requires F0 = 1/(8.98)^2 ≈ 0.012387, not 1/8.98 ≈ 0.1113.
Required fix: Correct F0 everywhere to F0 = 1/σstd^2 = 1/(8.98)^2 and recompute any derived quantities that depend on F0. Explicitly show the calculation that yields σ(fNL) = 8.14 for α = 0.19 ± 0.65 with the corrected F0 and c.

P3-E2 (Multiple locations: Section II A page 2; Section II B page 2; Sec. III B page 5)
Problem: Unresolved figure references and missing figure. The text contains “Fig. ??” placeholders (e.g., “architecture shown schematically in Fig. ??”; “per-band contributions … Fig. ??”) and “Figure ?? shows DESI Legacy Survey DR9 grz composite cutouts” for the high‑z QSO candidates. These are critical to the scientific claims (architecture and candidate images), yet absent.
Required fix: Resolve all “Fig. ??” placeholders with actual figures and update the text and captions accordingly. Include the promised image panel for the 12 high‑z QSO candidates with coordinates/IDs.

P3-E3 (Table I footnote ♡, page 7; Section III C page 5; Fig. 2 right caption page 5)
Problem: SDSS “top-1%” arithmetic inconsistency. You repeatedly label the “77,905” SDSS anomalies as a “top-1%” slice, but 77,905/1,925,279 = 4.05%, not 1%. Elsewhere you also say “the same 1,925,279-spectrum DR18 sample yields 19,253 anomalies at the harder top-1% score-knee cut,” which is numerically consistent with 1%. The current presentation is contradictory and misleading.
Required fix: Remove “top-1%” labeling from the 77,905 count and consistently describe it as the chosen continuity slice with its actual fraction (≈4.05%) or redefine the SDSS count if you truly intend a 1% slice (then it must be ≈19,253). Ensure Fig. 2 caption and Table I footnote ♡ match the corrected text.

P3-E4 (Section II B, page 2)
Problem: Ambiguous/tunable definition of σval in the anomaly score S. You write: “For DESI DR1, μval ≈ 0.0287 and σval is set such that the S > 5 catalog threshold corresponds to MSE ≈ 0.143.” This reads as if σval were chosen to force a particular numeric mapping rather than being the empirical standard deviation on the validation set (as defined just above).
Required fix: Clarify that σval is the empirical standard deviation of the MSE over the held-out validation set (no tuning), and show that with the measured μval and σval the S = 5 threshold indeed corresponds to MSE ≈ 0.143. Provide the actual σval value used for DESI (and for other surveys where S is used).

P3-E5 (Table V, page 15; Section II B, page 2)
Problem: Implausible training times vs. stated training schedule. Table V lists training times of 7.6 s (eROSITA), 1.2 s (Gaia), 1.6 s (NEOWISE), and 10.6 s (Planck conv AE, 1.1M params) while Section II B says training runs up to 200 epochs (converging at 100–150 epochs) on sizable training sets (e.g., “2×10^5 SMICA patches” for Planck). The reported times are not credible for the described workloads.
Required fix: Provide accurate wall-clock training times (hardware, dataset size, number of epochs) consistent with Section II’s training regimen. If the numbers in Table V are per-epoch or inference times, relabel them and add the total training time. Include training-set sizes for the photometric catalogs.

P3-E6 (Appendix C Fig. 8, page 16; Section V, page 10; Appendix C Table VII, page 15)
Problem: Inconsistent σ(fNL) baselines across the paper. Main text uses σstd = 8.98 (DESI-only single-tracer baseline). Fig. 8 caption/legend instead shows “single-tracer baseline = 16.85, baseline multi-tracer = 12.72, ideal (dense) = 11.71” for the “canonical 5-tracer configuration.” These are inconsistent reference points and confuse the reader about what σstd is being improved upon.
Required fix: Choose a single, unambiguous definition of the baseline(s) and use consistent numbers across the paper. If Fig. 8 explores a different setup, explicitly state that its baselines are for a different configuration and are not directly comparable to σstd = 8.98 used elsewhere. Label all baselines clearly in captions and text.

P3-E7 (Section III A, page 4)
Problem: Duplicated/near-duplicated paragraph content. The paragraph beginning “Across the 6.5 million spectra in DESI DR1 that carry a validated TARGETTYPE classification …” repeats information given just above, with slightly different wording and ordering, risking internal inconsistency.
Required fix: Remove duplication and present a single, consistent statement of DESI class-tagged anomaly rates, with one set of numbers and uncertainties.

P3-E8 (Section III C page 5; Table I and footnotes, page 7; Section II D page 3)
Problem: Sample-selection ambiguity. For SDSS you state “Input: 2,304,830 spectra” but “native re-score 1,925,279 spectra” with no description of the quality cuts producing the latter. For LAMOST you alternately cite 11,418,594 and 1.13×10^7 processed spectra. Rates and “top-x%” claims depend on these denominators.
Required fix: Provide explicit, reproducible selection criteria per survey (quality flags, masks, exclusion lists) and the exact N processed after cuts. Ensure all percentages/“top-x%” labels match those Ns.

P3-E9 (Abstract, page 1; Table I footnote ♠, page 7; Conclusions, page 14)
Problem: Catalog-grade subset definition inconsistent by 200 objects. Abstract recommends “∼265,000 unique objects (DESI + SDSS + eROSITA + Gaia + NEOWISE),” i.e., point sources excluding LAMOST and Planck; this should be 378,080 − 113,342 = 264,738. Table I footnote ♠ gives “catalog-grade tier (DESI + SDSS native + eROSITA + Planck native + Gaia + NEOWISE) is 264,938,” which includes the 200 Planck patches.
Required fix: State unambiguously whether the catalog-grade subset includes Planck patches. Report one consistent number and membership list in the abstract, body, and table. If excluding Planck for object-level work, the number is 264,738; if including Planck, it is 264,938.

P3-E10 (Section II D Step-1 gate, page 3)
Problem: Ad hoc validation loss criterion with no justification. The gate “validation loss ≤ 0.30 after ≤100 epochs” is introduced but not motivated by data scale or noise levels; for spectra you later get ≈0.03 while Planck’s 0.4437 FAIL is overridden by injection tests.
Required fix: Justify the choice of the 0.30 threshold quantitatively (e.g., relative to normalized input scales) or replace with a scale-invariant criterion (e.g., percentile of validation residuals vs. training). Clearly state why 0.30 is meaningful and how conclusions would change if tightened/loosened.

MAJOR

P3-M1 (Section V, page 10; “1σ envelope”)
Problem: The “1σ envelope [3.92, 8.98]” for σ(fNL) derived from αjk = 0.19 ± 0.65 implicitly takes α ∈ [0, 0.84] due to α^2. This is a non-linear, folded mapping; quoting it as a “1σ envelope” without showing the full propagated posterior in σ can mislead.
Required fix: Provide a proper propagation of uncertainty from the Gaussian α posterior through 1/σ^2 = F0 + c α^2 (e.g., Monte Carlo sampling) and report the resulting credible interval for σ(fNL). If you retain the endpoint mapping, explicitly label it as such and provide the Monte Carlo result in the appendix.

P3-M2 (Section IV D, page 10; Appendix F, pages 16–18)
Problem: Planck × ACT cross-correlation “null” lacks quantitative test description (e.g., statistic, p-value, null model). Currently qualitative.
Required fix: Specify the cross-correlation estimator, sky mask, number of realizations or analytic null, and report a p-value or confidence interval for the observed overlap. If using random rotations/Monte Carlo, give N_MC and show that it supports the claimed null.

P3-M3 (Section IV A b., page 9)
Problem: Expected false-match counts are given (e.g., “≲10 across all survey pairs”) without supplying inputs (surface densities per survey and matching-radius combinations).
Required fix: Provide the densities used and the computation for each pair (or at least for the highest-density pairs) to justify the “≲10” statement, or move it to an appendix with the arithmetic.

P3-M4 (Section III H Fig. 4, page 8; Section II B, page 2)
Problem: NEOWISE “Score = 11.5” appears, but earlier S was defined as the per-survey z-scored MSE with survey-dependent (μval, σval). It is unclear whether NEOWISE’s “score” is on the same S scale, and what the selection threshold was (you say “top-1%”).
Required fix: State explicitly the score definition used for NEOWISE, the threshold value corresponding to top-1%, and how “11.5” relates to the distribution (e.g., percentile). Add this to the caption or main text.

P3-M5 (Table III, page 8)
Problem: eROSITA Top-5 table lists Dec only, missing RA; also the “SIF,raw” axis spans 0–3.5×10^4 per text but the top source shows 34,182.
Required fix: Include RA and Dec for all sources. Clarify the IsolationForest raw-score range in the text or adjust the table/caption so the ranges agree.

P3-M6 (Section IV C, page 10–11; Fig. 6)
Problem: DESI×SDSS “three highest-confidence cross-survey detections” are asserted as validated (e.g., “known QSO,” “uncataloged BAL QSO”) but no redshift measurements or line IDs are reported in the text/panel captions to substantiate these identifications.
Required fix: Provide measured redshifts and specific line identifications for the three examples and clarify the evidence for BAL classification (e.g., Mg II absorption trough equivalent width).

P3-M7 (Claims of “largest” and “∼141×,” Abstract page 1; Conclusions page 14)
Problem: The “∼141× the size of the largest prior single-survey anomaly catalog [11]” and “DESI-only axis … ∼73× like-for-like increase” claims are not directly computed in-text. Liang et al. [11] reported 2,685 anomalies on ~250k EDR spectra (1.07%). Your DESI has 195,829 anomalies; 195,829/2,685 ≈ 73, which is the DESI-only factor. The 141× appears to compare your 378,080 point sources to 2,685, but this is not “like-for-like single-survey.”
Required fix: Rephrase “141×” to avoid suggesting a like-for-like single-survey comparison. State explicitly what is being compared, or remove the “141×” claim.

MINOR

P3-m1 (Section II C, page 3)
Problem: “The CMB and photometric surveys each required < 10 seconds of GPU time.” This mixes training and inference language. From Table V, the times appear to be per-inference scan; training times are treated elsewhere.
Required fix: Clarify whether this refers to inference-only and separate out training times to avoid confusion.

P3-m2 (Figure 2 right caption, page 5)
Problem: “spanning twelve orders of magnitude from the threshold (S = 5) to S = 1.9×10^11.” The ratio is ~3.8×10^10 (~10.58 decades), not 12 decades.
Required fix: Adjust wording to “over ten decades” or compute the precise span.

P3-m3 (Bibliography [33], page 19)
Problem: Editorial aside in the reference: “[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]”.
Required fix: Remove editorial comments; provide standard PRD reference formatting.

P3-m4 (Data availability, page 14)
Problem: “private pending arXiv acceptance; public upon acceptance.” PRD requires data to be accessible to referees prior to publication; the current statement is not appropriate for a final publication.
Required fix: Make the dataset public upon resubmission or provide an anonymized archive link accessible to referees and readers independent of arXiv acceptance.

P3-m5 (Notation and footnote symbols, Table I page 7)
Problem: Nonstandard symbols (♡, ♠, ⋆, ∥) and long, narrative footnotes hinder readability and are atypical for PRD.
Required fix: Convert to standard numeric footnotes/endnotes and move extended narrative clarifications to the main text or an appendix.

NIT

P3-n1 (Typos/grammar, multiple pages)
- “quasi-matter bounce” sometimes “quasi-matter bounce model predicts fNL = −35/8 …” but later “scalar-only w = 0 matter-bounce class.” Consider uniform terminology.
- Replace em dashes used as minus or range symbols with proper minus/en dash where appropriate.

P3-n2 (Units/axes, multiple figures)
- Ensure all axes that are probability densities specify whether linear/log scale and units (e.g., Fig. 2 “Probability density” on log y-axis).

P3-n3 (Table VI, page 15)
- “Artifact suspect 96 (0.05%) score range 10.0–21.0.” Consider adding how “artifact suspect” was determined.

Arithmetic cross-checks (selected audits)
- Unique-count arithmetic: 195,829 + 77,905 + 113,342 + 298 + 200 + 500 + 419 = 388,493; minus 10,213 = 378,280 (OK). Point-source unique = 378,280 − 200 = 378,080 (OK).
- NEOWISE polar-cap excess: two caps of radius 10° occupy 1 − cos 10° ≈ 1.519% of the sky; observed 17/436 ≈ 3.90%; ratio ≈ 2.57× (OK, matches 2.6×).
- SIMBAD false-match rate: n ≈ 3×10−5 arcsec−2, π(5")^2 ≈ 78.54 arcsec^2 ⇒ Pfalse ≈ 2.36×10−3; ×195,829 ≈ 462 (OK).
- χ^2 ν = 143,936/38,329 ≈ 3.76 (OK).
- NANOGrav spectral-index offsets: Δγ(3.0) = 0.433/0.382 = 1.13σ; Δγ(4.33) = 1.763/0.382 = 4.61σ (OK).
- Cross-transfer counts and dedup compression: 10,213/388,493 = 2.629% (OK).

Length and focus
At 20 pages, the paper is long for the primary methodological contributions claimed. A significant fraction of the text is devoted to narrative footnotes and path-rebuild commentary. After revision, I recommend capping the main paper at ~16 pages by:
- Moving the long Table I footnote explanations to an appendix.
- Consolidating repeated DESI text.
- Tightening the cosmological-forecast discussion to one main section plus an appendix with Fisher details.

## Summary recommendation
MAJOR REVISIONS

Justification: The manuscript has multiple essential methodological and presentation issues that must be corrected before it can meet PRD standards: an incorrect Fisher baseline term (F0) in the main text (dimensional error), unresolved figure placeholders, inconsistent SDSS “top-1%” labeling vs arithmetic, implausible training times relative to the declared training schedule, and inconsistent σ(fNL) baselines between text and figures. There are also sample-selection ambiguities and duplicated text. These issues are fixable, but require a careful, quantitative revision with corrected equations, consistent baselines, fully resolved figures, explicit selection criteria, and reproducible training/inference reporting.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P3-E11 (Global; Sections II.B p.2, III.E p.6–8, III.F p.6, III.H Fig. 4 p.8, Table I p.7)
Problem: Inconsistent and ambiguously defined anomaly “score” scales across surveys despite the blanket statement “Throughout this paper, ‘S’ refers without exception to the per-survey standardized (‘z-scored’) reconstruction residual.” Examples:
- Planck native CMB tier: “score range [0.558, 0.621] (top 1%).” A z-score at 0.56–0.62 cannot represent a top-1% tail (which would be ≳2.33σ if Gaussian, and in any case should be in the extreme right tail).
- eROSITA: headline cut “S > 0.259 (top 0.03%).” A z-score threshold of 0.259 is near the distribution center, not at 0.03% tail. Even allowing for non-Gaussianity, calling this S a “z-scored” residual is misleading if top-0.03% corresponds to S ≈ 0.26.
- NEOWISE Fig. 4: “Score = 11.5” shown for the top object, but NEOWISE selection is described as “top 1%,” and there is no definition of how this 11.5 relates to the per-survey z-score S.
- Table I mixes “S > 5.0” (DESI, SDSS native alt), “top-1%” (Planck, Gaia, NEOWISE), and “S > 0.259” (eROSITA) while the text asserts a single canonical S definition.
Required fix: Unify the score nomenclature. Either (a) reserve S exclusively for the BigAE-standardized MSE and report actual S thresholds for each survey (with μval, σval) or (b) rename non-BigAE or non-standardized quantities (e.g., “MSEraw,” “IFraw,” “ConvAE-MSE”) and stop calling them S. For each survey, give the exact threshold value on the score axis actually used, its percentile, and show how “top-1%” maps to that axis. Correct all captions (Planck, NEOWISE) accordingly.

P3-E12 (Abstract p.1 vs Data availability p.14)
Problem: Contradictory data-access statements. Abstract: “The catalog, model weights, and reproducibility scripts are publicly released.” Data availability: dataset is “private pending arXiv acceptance; public upon acceptance.”
Required fix: Make the artifact(s) publicly accessible at resubmission (or provide an anonymous, referee-accessible link) and ensure the abstract, body, and Data availability section give the same final access status.

P3-E13 (Conclusions bullet 6 p.14 vs Section II.B p.3)
Problem: OOD Jaccard stability inconsistency. Section II.B reports J̄prod×ctrl = 0.732 for production-vs-5-seed-control. Conclusions bullet 6 instead states “OOD control-vs-control 0.874 (PASS)”—a different statistic not defined in the main text—and omits the 0.732 figure.
Required fix: Define the “control-vs-control 0.874” measurement in the main text (sample, folds, and procedure), reconcile it with the 0.732 figure, and present a single, consistent OOD-stability summary in both Section II.B and the Conclusions.

P3-E14 (Section IV.A.b p.9 vs Section IV.C p.10–11)
Problem: Contradictory DESI×SDSS random-coincidence narrative. The false-match paragraph claims that for the DESI×SDSS cross-match at 3″ the “expected random coincidence count is ∼2.3, comparable to the 3 observed matches,” yet Section IV.C reports 637 multi-survey clusters from the 7-way 5″ deduplication (which must include many DESI×SDSS overlaps). The “3 observed matches” cannot be the full-sample DESI×SDSS coincidence count.
Required fix: State explicitly the sample sizes and selection for the “3 observed matches” case (e.g., “the three highlighted examples in Fig. 6 only,” or “top-N subset only”). Provide the surface densities and sample sizes actually used in the 3″ expectation calculation. Clarify the relation between that calculation and the 637 multi-survey clusters from full-catalog deduplication.

MAJOR

P3-M8 (Figure 1 caption p.4)
Problem: Ambiguous inclusion/exclusion of ACT. The caption title says “across 8 archives” and the legend includes ACT DR6, consistent with the 319,443 cross-transfer baseline. The body of the caption then states “ACT DR6 is quarantined and excluded,” which reads as if it were absent from the figure.
Required fix: Clarify explicitly that ACT is included in this baseline map (but excluded from the canonical Path-C results). Adjust wording to avoid implying it is absent from the plot.

P3-M9 (Figure 5 p.9; Table I p.7)
Problem: Aggregate SIMBAD-unmatched fraction (58.8%) appears to be based on the cross-transfer baseline rather than the canonical Path-C native-retrained catalogs, yet the surrounding text discusses catalog-grade novelty and Path-C protocol. Mixing baseline and Path-C tallies in the same novelty discussion can mislead.
Required fix: Report the aggregate SIMBAD-unmatched fraction for the canonical Path-C catalogs (and separately, if desired, the cross-transfer baseline), and label which is used in each plot and paragraph. Ideally, provide both figures with clear captions (“cross-transfer baseline” vs “Path-C native”).

P3-M10 (Section III.A p.4; “0% artifact rate in top 200”)
Problem: Unsupported QA claim. A blanket “0% artifact rate in top 200” is asserted without describing the artifact taxonomy, criteria, or inter-rater procedure.
Required fix: Provide the artifact-vetting protocol (who/what/when), definitions, and at least inter-rater agreement or a minimal rubric (with examples). Otherwise soften the claim to “no artifacts identified on visual inspection” and move the diligence to an appendix with exemplars.

P3-M11 (Section II.D Step 5 p.3; Fig. 7 p.13; Section III.H p.8)
Problem: NEOWISE “mask injection-recovery = 100%” is not comparable to the spectral or CMB amplitude injections; it tests a geometric cut rather than detection sensitivity. Plotting it on the same amplitude x-axis in Fig. 7 risks overstating equivalence.
Required fix: Separately report “mask robustness” tests (geometric/systematics cuts) from “signal-detection” injections (spectral, CMB). If kept in Fig. 7, clearly annotate NEOWISE as a binary-geometry control, not a detection-amplitude recovery curve.

MINOR

P3-m6 (Table IV p.13; Section II.B p.3)
Problem: Cross-reference mismatch for OOD reconciliation. Section II.B promises details in “§VI D (b),” while Table IV’s resolution column for item (b) says “reconciled in §II.” This makes the derivation trail unclear.
Required fix: Point both references to the same definitive location (either §VI D(b) with details or a subsection in §II), and ensure the promised derivation is actually present there.

P3-m7 (Appendix C Fig. 8 p.16 vs main text)
Problem: Baseline labeling ambiguity persists within Fig. 8 alone. The caption mentions “canonical 5-tracer configuration of §V” but does not remind the reader that these baselines (single-tracer 16.85, baseline multi 12.72, ideal 11.71) are not the DESI-only σstd = 8.98 baseline used elsewhere.
Required fix: Add a first-sentence caption note: “This figure uses a separate 5-tracer Fisher setup; its baselines are not comparable to the DESI-only σstd = 8.98 used in §V main text.”

P3-m8 (Section III.F p.6; score definition)
Problem: Planck native “score range [0.558, 0.621]” is reported without stating whether this is raw MSE, normalized MSE, or the canonical S. This fuels the global score-scale confusion (see E11).
Required fix: Explicitly specify the score axis for Planck (e.g., “ConvAE MSE standardized by μval, σval” or “raw MSE”), and align the label with Table I.

P3-m9 (Figure 2 right caption p.5)
Problem: Axis description is incomplete for “Probability density” on a log–log plot. The y-axis label in the panel is linear units “Prob. density” but the caption says “log–log scale,” and there is no unit note.
Required fix: State clearly “both axes in log scale” and whether the density is kernel-estimated or histogram-based with bin-width normalization.

NIT

P3-n3 (Figure/caption wording consistency)
- Figure 1 axis title “Right Ascension” with a Mollweide projection could use “RA (deg, increasing left-to-right)” to avoid confusion, since RA typically increases to the left in equatorial sky maps.

P3-n4 (Terminology consistency)
- Use one term consistently for the CMB “patch score” (MSE, S, or another), and avoid mixing “score,” “S,” and “MSE” in adjacent sentences for the same survey.

Explanation
These items were not covered in the initial review and emerged after re-checking score definitions across surveys, comparing baseline vs Path-C novelty statistics, reconciling cross-match narratives, and re-auditing figure captions against body text. The most consequential additions are the global score-scale inconsistency (E11), the contradictory data-access claims (E12), the OOD-stability mismatch (E13), and the ambiguous DESI×SDSS random-coincidence calculation (E14). Addressing these will materially improve methodological clarity and reproducibility.