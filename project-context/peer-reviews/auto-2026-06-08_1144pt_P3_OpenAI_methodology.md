# P3 auto-2026-06-08_1144pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (10049 chars)
**Wall time**: 476.0s

---

Referee report for: “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and Native-Trained Novelty Fractions from 37.3 Million Sources and Map Patches”

Scope of review: methodology rigor, statistical validity, derivation chains, internal arithmetic, error propagation, figure/table audit, and consistency of all quantitative claims (per instructions).

Global assessment
- The manuscript presents a large-scale, multi-archive anomaly catalog. However, there are several essential issues that must be corrected before the work is suitable for PRD. Chief among them are: (i) an internal inconsistency in the Fisher forecast formula (units) that propagates to headline σ(fNL) numbers, (ii) mislabeling of the SDSS “top-1%” continuity slice (it is ∼4.05% of the stated 1.925M sample), (iii) unresolved figure cross-references in the main text (Fig. ??), (iv) contradictory and physically implausible training-time and wall-clock runtime accounting, and (v) data availability/accessibility policy that does not meet PRD standards. In addition, several rate and improvement percentages are numerically inconsistent with the paper’s own stated numbers, and some results (Planck×ACT null) rely on a dataset the authors themselves quarantine as methodologically invalid.

Detailed findings (with required fixes)

ESSENTIAL

P3-E1
- Location: Section V.b (page 10) and VI.D(i) (page 12); also Table IV row (i) (page 13)
- Problem: Fisher-forecast formula dimensional error. Text states “1/σ(fNL)^2 = F0 + c α^2 with F0 = 1/8.982 and c = 0.0747.” This is inconsistent with the stated single-tracer baseline σ(fNL)_std = 8.98. With F0 = 1/8.982 ≈ 0.111, the baseline σ would be ≈ 3, not 8.98. The correct constant must be F0 = 1/(8.982)^2 ≈ 0.01239 to make the baseline σ(fNL) = 8.98 when α = 0. The central result σ(fNL) = 8.14 reported for α = 0.19 actually matches the corrected formula with F0 = 1/(8.982)^2 and c ≈ 0.0747.
- Required fix: Correct F0 everywhere it appears to F0 = 1/σ(fNL)_std^2 = 1/(8.982)^2, re-derive all dependent σ(fNL) numbers and uncertainty envelopes (including the [3.92, 8.98] interval, Conclusion 5, Appendix C Table VII, and any text where “Fisher-positivity” is invoked). State explicitly the reference σ(fNL)_std used and show one worked numeric example to remove ambiguity.

P3-E2
- Location: Table I footnote ♡ (page 7), Section III.C (page 5)
- Problem: Mislabeling the SDSS DR18 “top-1% continuity slice.” The paper repeatedly calls the 77,905-object native SDSS slice at S ≥ 0.1060 “top-1%,” but 77,905/1,925,279 ≈ 4.05%, not 1%. In the main text (page 5), you also state “the same 1,925,279-spectrum DR18 sample yields 19,253 anomalies at the harder top-1% score-knee cut S ≥ 0.2051,” which confirms that top-1% is ≈19,253, not 77,905.
- Required fix: Correct all occurrences where 77,905 is described as “top-1%” to “continuity slice of 77,905 objects (≈ 4.05% of the 1.925M native sample) chosen to match the cross-transfer count.” Ensure Table I footnote ♡ and the body text are unambiguous and numerically consistent.

P3-E3
- Location: Sections II.A (page 2), III.B (page 5), possibly elsewhere
- Problem: Unresolved figure cross-references (“Fig. ??”). Examples: “architecture shown schematically in Fig. ??” (page 2), “Figure ?? shows DESI Legacy Survey DR9 grz composite cutouts...” (page 5).
- Required fix: Insert and reference the correct figure numbers with finalized captions, or remove the orphan sentences. PRD cannot accept manuscripts with unresolved internal references.

P3-E4
- Location: Data availability paragraph (page 14)
- Problem: Data/code are “private pending arXiv acceptance; public upon acceptance.” This does not meet PRD requirements for data and code accessibility for referees and, typically, for readers upon publication.
- Required fix: Provide immediate, review-accessible links for all datasets and code (public or via an access link supplied to the editor/referees), or deposit them in PRD/APS supplemental material. Explicitly guarantee public availability upon publication with stable DOIs.

P3-E5
- Location: Section IV.D Planck × ACT (page 10) and Appendix F (pages 16–18); Abstract (page 1) and Conclusions (pages 13–14) if any inference is drawn
- Problem: Methodological invalidity of the Planck×ACT cross-correlation result. The ACT anomaly set is explicitly quarantined and fails both gates (Appendix F), yet Section IV.D presents a null cross-correlation as a scientific inference (“demonstrates that CMB patch anomalies…are dominated by survey-specific systematics”). A result predicated on a known invalid input cannot be positioned as a main-text conclusion.
- Required fix: Move the Planck×ACT cross-correlation entirely to the appendix with an explicit statement that it is a non-result for methods diagnostics only; remove any interpretive language in the main text and conclusions implying scientific inference from the quarantined ACT set.

P3-E6
- Location: Table V (page 15), Section II.C (pages 3–4)
- Problem: Inconsistent and physically implausible timing/training-time accounting.
  - Table V “Train time (s)” entries (e.g., Planck native conv AE “10.6 s” on 2×10^5 patches; eROSITA “7.6 s”; Gaia “1.2 s”) are not credible given the stated architectures and 100–200 epoch schedules elsewhere. 
  - Section II.C reports total wall-clock “approximately 42 hours,” yet the given high-throughput inference rates imply ∼9–10 hours aggregate (DESI 19,705 s ≈ 5.47 h; LAMOST at 950/s on 11.4M ≈ 3.3 h; SDSS at 1,100/s on 2.3M ≈ 0.6 h; others negligible). The stated wall-clock total is incompatible with your own throughputs unless significant additional overhead is explained.
- Required fix: Replace Table V “Train time (s)” with accurate, reproducible timings (include hardware, batch size, epochs, and data volumes per training). Reconcile the 42 h wall-clock with the throughputs (e.g., include I/O, CPU preprocessing, retry/failures), and provide a transparent timing breakdown. If times are inference-only or for partial subsets, label them accordingly.

P3-E7
- Location: Abstract (page 1), Section V.b (page 10), Conclusions (page 14)
- Problem: Inconsistent “percent improvement” statement. With σ(fNL)_std = 8.98 and σ(fNL) = 8.14 (for α = 0.19), the fractional improvement is (8.98 − 8.14)/8.98 ≈ 9.36%, not 7.9% as stated in multiple places (“7.9% improvement consistent with no improvement”). The 1σ envelope [3.92, 8.98] matches the corrected F0 formulation but highlights the mismatch in the central-value improvement percentage.
- Required fix: Correct the improvement percentage to ≈ 9.3% (or recompute σ(fNL) after fixing P3-E1 and then report the correct percentage). Ensure consistency in Abstract, Section V, Conclusions, and Table VII narrative.

P3-E8
- Location: Section III.C (page 5) and Table I (page 7)
- Problem: SDSS DR18 denominators are inconsistent and under-explained. You first state input “2,304,830 spectra,” then report the native re-score “complete across 1,925,279 spectra,” with multiple rate/statements tied to these different denominators; Table I still lists Ntotal = 2,304,830 for SDSS.
- Required fix: Clearly state the SDSS subset selection leading to 1,925,279 spectra (cuts, quality flags) and consistently use this denominator when quoting native rates. Update Table I or add an explicit note that Ntotal therein corresponds to the cross-transfer scan, while the native re-score used a reduced sample, providing the reason.

P3-E9
- Location: Section IV.A (page 9), Conclusions (pages 13–14)
- Problem: The extended archival cross-match novelty fraction (17.8%) is reported only at the “DESI top-1,000” stratum and characterized as “single-sample point estimate,” but it appears in the Abstract and Conclusions as a general catalog property. This is at risk of being overgeneralized.
- Required fix: Explicitly qualify every instance (Abstract and Conclusions included) as “17.8% at the DESI DR1 top-1,000 score stratum against 20 all-sky catalogs; full-catalog novelty fraction unmeasured.” Consider adding a confidence interval for the 17.8% binomial proportion with stated matching incompleteness assumptions.

P3-E10
- Location: Section III.F (page 6)
- Problem: Planck native CMB anomaly “score range [0.558, 0.621]” is inconsistent with the global S definition (Eq. 2) described as z-scored MSE. The range reported looks more like a raw loss or a non-z-scored metric.
- Required fix: Specify the exact score definition used for Planck native patches (e.g., raw conv-AE reconstruction loss, normalized how?), and avoid reusing the symbol S unless it obeys Eq. (2). If it differs, use a distinct symbol and define it.

MAJOR

P3-M1
- Location: Section V.b (page 10), Appendix C (pages 15–16), Table VII (page 15), VI.D(i) (page 12)
- Problem: The “Fisher-positivity-respecting” ansatz 1/σ^2 = F0 + c α^2 lacks a methodological derivation and appears ad hoc. The text references a “5-α refit” but provides no details. Moreover, you present a “local-linear propagation σ ≈ 8.98 − 3.66 α” as failing because α crosses zero; this narrative is confusing without a clear underlying Fisher model.
- Required fix: Provide a brief derivation or justification for the quadratic-in-α form from the underlying Fisher matrix of the multi-tracer configuration, including definitions of α, F0, c, and the tracer counts/noise assumptions used to fit c. State the 5 α values used in the refit, show the fit residuals, and justify positivity. Remove or clarify the “local-linear propagation” sentence.

P3-M2
- Location: Section IV.D (page 10) and Conclusions (page 14)
- Problem: Overinterpretation of the Planck×ACT null as evidence that “CMB patch anomalies…are dominated by survey-specific systematics,” even with caveats. Given ACT is quarantined, an informative null cannot be claimed.
- Required fix: After moving this to an appendix (per P3-E5), ensure all main text and conclusions do not draw physical inferences from the Planck×ACT exercise.

P3-M3
- Location: Figures 2 (page 5, right panel)
- Problem: Probability density axis has ticks labeled up to 10^14 (“Prob. density”), which is nonsensical for a normalized density (should integrate to 1). While the panel is described as transfer-learning artifact, axes must remain meaningful.
- Required fix: Recompute and plot a properly normalized probability density (or a count histogram with explicit unit/normalization), adjust axis labels and tick values accordingly, and verify that the dynamic range presentation is methodologically sound.

P3-M4
- Location: Section II.D Step 5 (page 3) and Figure 7 (page 13)
- Problem: Injection-recovery descriptions are often qualitative (e.g., “continuum-dip,” “emission-line,” “Gaussian-bump” for CMB) without precise definitions (widths, equivalent widths, amplitude-to-noise mapping, duration for variability plants, etc.). For a methods paper, the injection families and thresholds must be specified to ensure reproducibility.
- Required fix: Provide precise parameterizations (functional form, width in pixels/Å, amplitude relative to local noise, placement, randomized seeds, number of realizations), and publicly release the planting code or exact configuration used.

P3-M5
- Location: Section III.C (page 5), Table I footnotes ♡ (page 7)
- Problem: Terminology inconsistency (“cross-transfer count,” “native slice,” “top-1%,” “score-knee”) in a load-bearing comparison. Readers cannot unambiguously understand which SDSS counts are used for which conclusions.
- Required fix: Introduce a clear threshold taxonomy table early in the SDSS section that lists: (a) native S>5 count (12), (b) native top-1% cut and count (19,253), (c) continuity slice equal to 77,905 with its actual percentile (≈4.05%), (d) transfer-learning count (77,905). Use these consistently across text and tables.

P3-M6
- Location: Section II.C (page 3–4) and Table V (page 15)
- Problem: Throughput accounting lacks uncertainty/variability assessment. Given single-GPU runs, repeatability may vary with I/O and CPU preprocessing. Claims like “The CMB and photometric surveys each required < 10 seconds of GPU time” need explicit qualifiers (excluding preprocessing).
- Required fix: State explicitly what is included in “GPU time” (forward passes only) vs. “wall-clock,” and provide ranges or averages over repeated runs. If one-off, denote as such and avoid broad generalizations.

P3-M7
- Location: Section III.F (page 6)
- Problem: The Planck native conv-AE “validation loss = 0.4437” is reported without stating the loss normalization (per-pixel MSE? scaled/whitened input?).
- Required fix: Define the loss function, normalization (e.g., inputs rescaled to unit variance), and its expected scale so the value is interpretable and comparable.

MINOR

P3-n1
- Location: Section I (page 1), Abstract (page 1), Conclusions (pages 13–14)
- Problem: Claims of scale/novelty (“largest multi-archive anomaly search to date”) are plausible but unsupported by a brief literature comparison beyond [11].
- Required fix: Add a short sentence with concrete figures from the most comparable multi-archive anomaly works (if any), or rephrase to “to our knowledge.”

P3-n2
- Location: Section III.A (page 4), Table VI (page 15)
- Problem: Small rounding mismatches in percentages (e.g., “R-dominant (0.02%), Z-dominant (0.01%), Artifact suspects (0.05%)”) are fine but note that these are 0.017%, 0.0097%, and 0.049% respectively.
- Required fix: Optionally add one extra significant figure or a footnote stating rounding convention.

P3-n3
- Location: Section II.D (page 3)
- Problem: Slight duplication in phrasing: “reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository).”
- Required fix: Remove duplication; say once and point to a specific repository/DOI.

P3-n4
- Location: Section IV.A (page 9), Fig. 5 (page 9)
- Problem: The caution that SIMBAD-unmatched overstates novelty is appropriate; add in the caption that all fractions are at 5″ radius and provide the rough false-match probability (already computed in text) to align methods sections with the figure.

P3-n5
- Location: Section H (page 8), Fig. 4 (page 8)
- Problem: The NEOWISE top anomaly “Score = 11.5” should reference the definition of S for NEOWISE (Eq. 2) with the survey’s μval, σval for clarity.
- Required fix: Add a sentence in the caption linking the score to Eq. (2) and specify if this is the canonical-S or another measure.

NIT

P3-z1
- Location: References [33] (page 19–20)
- Problem: Bracket note “[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]” is internal-bookkeeping style.
- Required fix: Remove bracketed commentary; keep standard citation format.

P3-z2
- Location: Minor typos and spacing (e.g., extra spaces before degree symbols, inconsistent hyphenation of “cross-transfer,” occasional “Ceffyl” capitalization inconsistencies).
- Required fix: Copy-edit pass for consistency.

Arithmetic and consistency spot-checks (selected)
- DESI anomaly rate 195,829/22,504,897 ≈ 0.00870 → 0.87% (consistent).
- 7-way deduplication: Sum 388,493 − 10,213 = 378,280; compression 10,213/388,493 ≈ 2.629% (consistent).
- LAMOST native “top-1% slice” 113,342/11,418,594 ≈ 0.992% (consistent).
- NEOWISE polar-cap null fraction 1 − cos 10° ≈ 1.519% and observed 3.9% → 2.6× (consistent).
- Improvement for σ(fNL): As flagged in P3-E7, 8.98 to 8.14 is ≈ 9.36% improvement, not 7.9%.
- χ2 test: 143,936/38,329 ≈ 3.76 (consistent).

Length
- The paper is dense (20 pages) for a primary-methods catalog. Given the number of appendices and extensive footnotes, the main text could be streamlined (e.g., move the cross-transfer diagnostics and ACT material fully to appendices). Recommended target length for the main body: ≤ 15 pages, with detailed diagnostics in appendices.

## Summary recommendation
MAJOR REVISIONS

Justification: The manuscript contains essential methodological inconsistencies that affect key headline results: the Fisher-forecast formula is dimensionally mis-specified in the text (yet used as if corrected), SDSS slice labeling is incorrect (“top-1%” vs ~4.05%), multiple unresolved figure references remain in the main text, runtime/training-time accounting is internally inconsistent and in places implausible, and the Planck×ACT null is treated as an inference despite reliance on a quarantined dataset. Data/code availability does not meet PRD standards at submission. Addressing these essential and major issues, along with the specified minor corrections, is required before the paper can be considered for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER SECOND-PASS AUDIT (fresh eyes)

Only issues not already listed in my initial report are included. Labels follow the same convention.

ESSENTIAL

P3-E11
- Location: Section IV.A (page 9), Fig. 5 caption/text, Table I context
- Problem: The “aggregate SIMBAD-unmatched fraction 58.8%” is arithmetically inconsistent with the per-survey fractions and counts given. A count-weighted aggregate over the SIMBAD-matchable surveys is ≈83%–90% depending on whether you use the Path-C native counts or the cross-transfer counts:
  - Using Path-C native counts (DESI 195,829; SDSS 77,905; LAMOST 113,342; eROSITA 298; Gaia 500; NEOWISE 419) gives 321,183.4/388,293 ≈ 82.7%.
  - Using the cross-transfer counts in Table I (DESI 195,829; SDSS 77,905; LAMOST 44,075; eROSITA 298; Gaia 500; NEOWISE 436) gives 286,557.6/319,043 ≈ 89.8%.
  The reported 58.8% equals the median of the six survey-wise percentages, not a count-weighted aggregate. Calling it “aggregate” is misleading.
- Required fix: Replace 58.8% with a clearly defined statistic: either (a) the count-weighted aggregate (report both Path-C and cross-transfer variants and specify which you use), or (b) explicitly state “median across surveys = 58.8%.” Update Fig. 5 caption/body accordingly.

P3-E12
- Location: Fig. 6 panels (a, b) and Section IV.C (page 10–11)
- Problem: Contradiction between figure values and catalog definition. Panel (a) DESI score = 3.2 and panel (b) SDSS score = 2.8 are below the anomaly thresholds (DESI’s catalog uses S > 5; SDSS selections are via the stated continuity/top-percentile cuts). Yet Section IV.C says this object was “independently flagged by both surveys,” implying both are anomalies. As shown, that cannot be true.
- Required fix: Either (i) replace these plots with the actual anomalous pair used in the 5″ cross-survey dedup (both S above the applied thresholds), or (ii) relabel “Match 1” explicitly as a non-anomalous control illustrating spectral consistency, and remove it from the “independently flagged” narrative.

P3-E13
- Location: Section II.B “Two threshold families” (page 2–3)
- Problem: Methods-text inconsistency. The paragraph states “DESI DR1 and SDSS DR18 use an absolute canonical-S cut at S > 5.0,” but the actual SDSS selections used in the paper are not S > 5.0 (they are 12 objects at S > 5, a 19,253-object native top-1% slice, and a 77,905-object continuity slice at S ≥ 0.1060 ≈ 4.05%). This conflicts with the stated methods.
- Required fix: Correct Section II.B to reflect the thresholds that were actually used for SDSS (list all three SDSS cuts with their purposes, and state explicitly that the continuity slice at 77,905 objects is ≈4.05%, not 1%). Cross-link to the SDSS threshold taxonomy (see also P3-M5 in the first report).

P3-E14
- Location: Table II caption/body explanation (page 8) vs. SDSS SIMBAD match rate (Section III.C, page 5; Table I)
- Problem: Logical inconsistency. Table II says the 52.7% “Uncategorized” class “reflects objects that match a SIMBAD entry but lack a specific astrophysical type.” However, the paper states that 90% of SDSS anomalies are SIMBAD-unmatched. Both cannot be true if “Uncategorized” is defined as SIMBAD-matched-but-untyped.
- Required fix: Clarify what “Uncategorized” means. If it is a pipeline-internal class unrelated to SIMBAD, rewrite to avoid implying SIMBAD matching; if it is tied to SIMBAD, the 52.7% fraction is incompatible with the 90% unmatched rate and must be corrected.

P3-E15
- Location: Appendix C Fig. 8 caption and curve labels (page 16) vs. Section V baselines
- Problem: Baseline σ(fNL) inconsistencies. Fig. 8 labels “single-tracer baseline = 16.85” and “baseline multi-tracer = 12.72,” while the body repeatedly uses σ(fNL)_std = 8.98 as the baseline. These are not reconciled or defined, and they refer to different configurations without warning. This creates a cross-figure/body mismatch and risks invalid comparisons.
- Required fix: Define all baselines and configurations (which survey(s), number of tracers, kmax, volumes, priors). Ensure the same baseline is used consistently across Section V, Appendix C, and figure captions, or clearly state when a different configuration is being illustrated.

P3-E16
- Location: Section IV.B (page 10)
- Problem: HEALPix pixel count vs. Nside mismatch. Text claims analysis “across 38,330 HEALPix pixels (Nside = 64),” but Nside = 64 has 49,152 full-sky pixels. If 38,330 is a masked/covered subset, state the mask and its construction.
- Required fix: Specify the sky mask or selection that leads to 38,330 pixels at Nside = 64, and revise the dof statement accordingly. If full sky was intended, correct the pixel count.

P3-E17
- Location: Fig. 9 caption and panel annotations (page 17) vs. Section III.B paragraph on rZ
- Problem: Unit/label inconsistency. Fig. 9 panels show “AE=” values as large as 83,518, but Section III.B says panel labels report the Z-arm sub-score rZ with typical mean ≈ 3.9 for the z ≈ 6 candidates. AE ≈ 10^4–10^5 is irreconcilable with rZ ≈ O(1–10). The plotted quantity is not what the body text says it is.
- Required fix: Correct the plotted label to the actual quantity and units (e.g., raw per-arm MSE, unnormalized residual sum, or another metric), or rescale to the canonical rZ definition. Update the caption to match.

MAJOR

P3-M8
- Location: Section II.D Step 5, Fig. 7 (pages 3 and 13), Sections III.F/H
- Problem: Cross-survey comparability of injection-recovery “PASS/FAIL” is not established. The six curves represent different, non-comparable plants (continuum dips vs emission lines in spectra, Gaussian bumps in CMB maps, and even a NEOWISE “ecliptic-pole mask” treated as an “injection” test). Presenting them on a single recovery-vs-amplitude plot suggests comparability that is not justified.
- Required fix: Partition the figure by plant family and survey type, or explicitly state that the curves are not comparable across surveys. Provide a per-survey, per-plant definition table (amplitude, width, placement, noise normalization) and restrict PASS/FAIL gate comparisons to like-for-like plants.

P3-M9
- Location: Appendix C Table VII and narrative (pages 15–16) vs. Section V “Fisher-positivity” usage
- Problem: Internal methodological inconsistency. Table VII states σ(fNL) values are obtained by linear scaling from the α = 0.15 Fisher result, whereas Section V adopts the “positivity-respecting” quadratic formula 1/σ^2 = F0 + c α^2. For α ≠ 0.15 the two methods yield different numbers (e.g., at α = 0.05, 8.80 by linear scaling vs. ≈ 8.92 by the quadratic with F0 corrected per P3-E1). This is a stale-number/method-mismatch.
- Required fix: Choose one method (preferably the properly derived Fisher model) and recompute Table VII accordingly. Clearly state the method in both places and reconcile any remaining differences.

P3-M10
- Location: Section II.D Step 1 (page 3), Sections III.E/G/H
- Problem: Gate criteria completeness. For photometric/catalog surveys (eROSITA, Gaia, NEOWISE) you do not report the native BigAE validation loss used for criterion (a), while reporting injection/IF-based diagnostics elsewhere. It is unclear whether these surveys formally PASS Step 1 via (a) or (b) or are being retained under exceptions.
- Required fix: Report the native BigAE validation loss values (scale, normalization) for eROSITA, Gaia, and NEOWISE; state explicitly which criterion each survey meets to PASS Step 1. If any fail both criteria, justify retention or adjust the Path-C protocol text.

P3-M11
- Location: Section III.A (page 4)
- Problem: Over-strong novelty statement without a documented null: “none of the top 100 [DESI anomalies] appear in any database” (after cross-matching to SIMBAD, NED, AllWISE, Milliquas, Gaia DR3, SDSS). Given that virtually all real astrophysical objects have photometric catalog entries (Gaia/WISE/SDSS imaging), this needs precise definition of “appear” (e.g., spectroscopic/classified vs. photometric detections) and/or evidence.
- Required fix: Define “appear in any database” (does this exclude photometric-only catalogs? what match radius? how were blended/saturated sources handled?), provide a machine-readable list of the top 100 with match results, and temper the claim if it was meant as “no classified counterpart.”

MINOR

P3-m6
- Location: Section III.A (page 4)
- Problem: Paragraph duplication. The “Across the 6.5 million spectra in DESI DR1 that carry a validated TARGETTYPE…” paragraph appears twice with near-identical text.
- Required fix: Remove the duplicate and keep a single, consolidated presentation.

P3-m7
- Location: Section IV.C footnote text and Table I footnote ♠ (page 7 and 10–11)
- Problem: Catalog-grade vs exploratory-tier arithmetic not independently reproducible from the paper. The text gives “catalog-grade tier … 264,938 unique objects” but the derivation (how overlaps with LAMOST are subtracted) is not shown.
- Required fix: Provide the exact arithmetic and overlap counts used to arrive at 264,938 from the dedup manifest (or add a supplementary table listing the unique-count contributions per survey after dedup).

NIT

P3-z3
- Location: Section IV.D (page 10) and Appendix F
- Problem: Potentially misleading phrasing about ACT sky distribution (“concentrate along the Galactic plane”). ACT’s science maps avoid most of the Galactic plane; if the cross-transfer anomalies concentrate there due to failure modes, say so explicitly to avoid implying an ACT survey strategy.
- Required fix: Rephrase to “the ACT cross-transfer anomaly set (methodologically invalid) concentrates along the Galactic plane due to failure modes,” or remove the strategy inference.

Explanation of coverage
- I rechecked arithmetic, figure–text consistency, dimensional consistency, cross-references, comparability of procedures, abstract–body alignment, novelty claims, hedges, appendix/main alignment, and stale numbers. The new items above were not included in my first report and materially affect clarity, correctness, or reproducibility.