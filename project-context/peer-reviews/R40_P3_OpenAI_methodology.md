# P3 R40 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=4a8c1172 pages=30
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8427 chars)
**Wall time**: 234.9s

---

Referee report (PRD methodology)

I have read the full manuscript carefully, audited the abstract and conclusions against the body, re-computed quoted ratios and error bars where possible from the provided numbers, and checked statistical and methodological claims.

Overall assessment: The manuscript undertakes an unusually detailed, large-scale multi-archive anomaly search with extensive internal QA. However, several core methodology and reproducibility issues must be resolved for PRD standards. In particular, one released tier (eROSITA) is not reproducible on any score axis; the “catalog‑grade” headline subset mixing and associated counts (269,317 vs 269,117; inclusion of Planck patches) are internally confusing; one of the three “PASS” injection-recovery gates is a masking-geometry QA rather than a detector-sensitivity test (yet is tallied alongside true sensitivity gates, including in the abstract); and one catalog (Gaia) lacks an exact, committed preprocessing script. The data/code release is not yet finalized (no DOI; placeholders remain), which is essential for a methods paper of this kind. There are also several statistical-reporting issues (p-values reported on a stratified design; conflation risks between unlike sigma/“significance” metrics), and a few arithmetic/clarity points that need correction or documentation.

Below I list all required fixes and clarifications, with IDs, locations, quoted text, and required actions.

Findings

ESSENTIAL

P3-E1 — Abstract, p.1; also §IV C and Table I footnotes
Problem: Inconsistent and confusing use of “catalog-grade” counts and strata. Abstract: “the recommended catalog-grade tier contains 269,317 unique entries (269,117 point‑source after dropping the 200 Planck map patches…)”. Later (Table I footnote ♠) and §IV C, the 6‑way “catalog‑grade” dedup (excluding LAMOST) is said to be 269,317 but includes 200 Planck patches; then “point‑source subset is 269,117”. The same section also states “4,379 of the 113,342 LAMOST detections merge into catalog-grade clusters at 5″” which is inconsistent if “catalog‑grade” is defined as the 6‑way (LAMOST‑excluded) merge.
Required fix: Provide a single, unambiguous, table in the main text (not only footnotes) listing:
- The exact per-survey native counts used as inputs to the 7‑way and 6‑way deduplications,
- The unique-object counts for 7‑way (with Planck) and 6‑way (excluding LAMOST), and
- The explicit split between point-source objects and CMB patches for each case.
Reconcile or correct the “4,379 LAMOST merge into catalog‑grade clusters” statement (if 6‑way excludes LAMOST this cannot occur; if the statement refers to the 7‑way run, say so and move it out of the 6‑way context). Update the abstract to match the final, unambiguous definitions.

P3-E2 — §III E (pp. 11–12), Table IV caption, Abstract p.1
Problem: The eROSITA tier’s per-object SBigAE score axis is explicitly “irreproducible on any of 16 monotone rescalings”; the “0.259” threshold cannot be recovered from any committed artifact; only the membership list is reproducible. Yet the abstract and Table I still cite the 298 count alongside other reproducible tallies, and Table IV mentions a non-reproducible threshold.
Required fix: For PRD, either (a) re-derive and publish a fully reproducible per-object score axis and the exact threshold used to select the 298 (with code and frozen artifacts), or (b) move eROSITA to an appendix-only exploratory tier, remove it from all headline counts (including the “catalog‑grade” 6‑way total), and delete all threshold values that cannot be reproduced. In both cases, ensure the abstract and conclusions state clearly whether eROSITA contributes to headline catalog sizes.

P3-E3 — Data availability (p. 23)
Problem: “A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission).” This is a placeholder; no DOI is given. Numerous internal paths (pipelines/.../json) are cited as provenance but are accessible only if the repository is public and frozen at a tagged commit.
Required fix: Before acceptance, provide working DOIs for the data release and a frozen Git tag/commit hash for the code repository that reproduces the exact results in the paper, and verify that all referenced artifacts (JSON/NPY/weights) are accessible and match the paper’s claims. Replace all “will be made public” and “DOI inserted” language with the final DOIs and tag hashes.

P3-E4 — §II B (pp. 3–5): Preprocessing and leakage; Gaia reproducibility
Problem: For tabular surveys, feature scalers were fit on the full sample (validation tail included), not only on the training split; only eROSITA has a bounded robustness check. The Gaia tier’s exact 20‑feature production preprocessing script was “not recovered”; the used feature list is lineage-inferred, not the committed production code.
Required fix: For PRD standards, either:
- Re-train Gaia and NEOWISE with scalers fit strictly on the training split, quantify any changes (top‑N overlap, Jaccard), and update the paper accordingly; and for Gaia, deposit the exact preprocessing code used for the published 50k run (or re-run with a committed script and publish that), or
- Immediately reclassify Gaia and NEOWISE as exploratory (remove them from the “catalog‑grade” subset and any PASS-tally), and move their quantitative contributions out of the abstract.
In all cases, add a short quantitative sensitivity table for Gaia and NEOWISE (as you did for eROSITA).

P3-E5 — Abstract p.1; §II D Step 5; Fig. 10 caption (p. 22)
Problem: The injection‑recovery PASS tally counts “NEOWISE mask‑geometry 100%” alongside true detector‑sensitivity gates. Although you note in places that this is a geometry QA that “passes by construction,” the abstract headline still lists it equally among the three PASS gates.
Required fix: Do not count NEOWISE’s masking-geometry check as a detector “PASS” anywhere the PASS tally is quoted (especially the abstract and conclusions). Present the PASS count for detector sensitivity separately (SDSS continuum‑dip, Planck CMB), and list the masking QA in a different bullet/class. Update Fig. 10 legend to visually separate geometry QA from sensitivity tests (e.g., different panel or shading), and adjust any “3 PASS” sentences accordingly.

P3-E6 — §III F (pp. 12–13): Planck tier training/selection leakage
Problem: The released Planck top‑200 anomalies are selected from a scored bank that includes the training patches; while you provide a useful check (48/200 fall into the validation split; overrepresentation of held‑out patches), the tier is still not a held‑out selection.
Required fix: For acceptance as a catalog component (not merely a methodology demonstration), re‑issue the Planck top‑200 from a held‑out scored bank that excludes all training patches (or present a re‑rank filtered to validation-only patches). Alternatively, label the entire Planck tier as exploratory (not catalog‑grade) and remove it from any “validated” tallies.

P3-E7 — §III C (p. 6–8): Misuse of p‑value under stratified sampling
Problem: “Spearman rank correlation between anomaly score and SNR is ρ = −0.03 (p = 0.12 on a stratified subsample…),” but then you note the sample is “deliberately stratified to be log‑uniform in SNR,” making the reported p-value not interpretable as a population test.
Required fix: Remove or replace the p‑value with an appropriate design-based inference (e.g., permutation test respecting the stratification scheme) or report only the effect size (ρ) without p, as you partly suggest. Clarify the sampling design explicitly.

P3-E8 — §IV C (pp. 15–16): Dedup geometry vs. narrative
Problem: The text states “4,379 of the 113,342 LAMOST detections merge into catalog‑grade clusters at 5″” right after defining the “catalog‑grade” as “independent 6‑way (DESI + SDSS native + eROSITA + Planck native + Gaia + NEOWISE)”—which excludes LAMOST. This is internally inconsistent.
Required fix: Specify whether the 4,379 figure refers to overlap within the 7‑way merge or to a separate diagnostic; if the latter, move and label it clearly. Provide a small table enumerating overlap counts per survey pair/triple for both the 7‑way and the 6‑way merges, so readers can trace these numbers.

P3-E9 — §III C/Table I footnote ♡ (pp. 8–10): SDSS continuity-slice selection
Problem: The SDSS “headline” 77,905 anomalies are selected via a fixed-size continuity slice (S ≥ 0.1060; 4.05%) sized to equal the cross‑transfer count, rather than a data-driven threshold (e.g., S>5 within the native scale or a fixed percentile). This introduces an arbitrary selection that complicates cross-survey comparability and downstream statistics.
Required fix: Either (a) adopt a principled, pre-declared threshold for SDSS (e.g., top‑1% score‑knee or S>5 native), and move the 77,905 slice to an appendix; or (b) keep the continuity slice but add a quantitative analysis showing how the dedup geometry and all cross‑survey tallies change under the top‑1% and S>5 native thresholds (including unique-object counts and the number of multi‑survey clusters). At minimum, include a compact table with these alternatives in the main text.

MAJOR

P3-M1 — Threshold heterogeneity across surveys; Table I and §II B
Problem: Mixed threshold definitions (absolute S>5 for DESI; fixed-size continuity slice for SDSS; top‑1% for LAMOST/Gaia/NEOWISE; a fixed top‑298 cap for eROSITA; Planck by top‑1% in native patch bank) make cross‑survey rates difficult to interpret.
Required fix: Move the long Table I footnote content into a concise, stand-alone subsection that systematically lists each survey’s threshold, rationale, and consequences for rates and overlap structure. Provide a single summary figure or table that shows, for each survey, the fraction retained under your headline threshold and at least one alternative, with Jaccard overlaps. This clarity is needed for PRD readers.

P3-M2 — §III H (p. 13), Fig. 5 caption: speculative physical interpretation
Problem: The NEOWISE top anomaly interpretation (“circumstellar dust, buried AGN, evolved giant hypotheses”) is speculative from W1/W2 photometry alone.
Required fix: Rephrase to avoid implying a likely astrophysical class. State explicitly that interpretation requires multi-band SED or spectra; keep as hypotheses only.

P3-M3 — §V (pp. 18–19): Fisher “positivity-respecting” mapping details
Problem: You fit 1/σ^2(fNL) = F0 + c α^2 using a “5‑α refit” but do not provide the α grid, fit uncertainties, or goodness‑of‑fit.
Required fix: Add a short table (or figure) listing the α values used, the corresponding σ(fNL) references, the fitted c with uncertainty, and R^2 (or χ^2/dof). State whether heteroskedasticity was accounted for (weights). Deposit the code snippet used for this fit.

P3-M4 — §V A (pp. 18–19), Appendix E: KDE bandwidth and Bayes-factor sensitivity
Problem: Bayes factors rely on a KDE of the posterior at specific γ values. The kernel bandwidth is not reported, and no sensitivity to bandwidth is shown.
Required fix: Report the KDE bandwidth (method/parameter) and show that BMB/free and BSMBHB/free are stable across a reasonable bandwidth range. Alternatively, use a standard kernel with leave‑one‑out bandwidth selection and document it.

P3-M5 — §IV A (pp. 13–14): False-match estimate
Problem: The SIMBAD false-match rate is computed with a single global areal density (n ≈ 3×10^-5 arcsec^-2), yet you note strong density variations (Galactic plane, LMC).
Required fix: Add a HEALPix map (or at least a figure) of local SIMBAD density and show the distribution of per-object Pfalse across the DESI footprint; quote the median and interquartile range. Keep the global figure as a baseline but present the inhomogeneity for completeness.

P3-M6 — §III A (pp. 6–7): Visual inspection of top‑200 DESI anomalies
Problem: “0/200 visually flagged …” without a clear protocol (who reviewed, how many reviewers, what criteria).
Required fix: Add a concise description of the inspection protocol (criteria list, number of independent reviewers, inter‑rater agreement if relevant). Deposit the 200 spectra list.

P3-M7 — §III D (pp. 10–11): Injection‑recovery plant definitions
Problem: For LAMOST and SDSS, you mention both continuum‑dip and emission‑line injections with large differences in recovery. Precise plant parametrizations (line widths/EWs, continuum dip amplitude/profile) are not given in the main text.
Required fix: Add a compact table listing injection parameters (amplitude scale, widths, location rules, noise model) for each survey and morphology (continuum vs emission line). Point to the code but also summarize in text.

P3-M8 — §III B (pp. 7–8): High‑z QSO candidates
Problem: The coordinates and spectra are relegated to the repository only; only brief notes appear in text.
Required fix: Include a small table (in the appendix if necessary) listing the 12 candidates with RA, Dec, Redrock z, rZ, and a thumbnail spectrum or link. Clarify that template-fit z are low‑S/N and require confirmation.

P3-M9 — §IV B (p. 15): χ^2 uniformity test
Problem: Reporting χ^2 = 376,713 (ν=24,048; χ^2_ν=15.7) invites over‑interpretation without selection‑function corrections, despite your caveats.
Required fix: Either move this raw χ^2 to an appendix or retain only the effect‑size statement with a stronger caveat, and avoid quoting a precise χ^2 without model corrections. The dust/latitude nulls are the more interpretable results—prioritize them.

MINOR

P3-m1 — Fig. 3 (p. 8) right panel
Problem: Extreme dynamic range (S up to 1.9×10^11) can mislead.
Required fix: Add an inset or annotation reminding that this is a cross-transfer (DESI‑trained) score axis, not comparable to survey‑native S, and that extremes collapse under native retraining.

P3-m2 — Table I readability (pp. 9–10)
Problem: Extremely long footnotes obscure key messages.
Required fix: Move the core threshold and gate criteria into the main text (per P3‑M1); keep only brief clarifying notes in footnotes.

P3-m3 — Confidence intervals for percentages
Problem: Percent fractions (e.g., 77.2% multi-band; 22.7% B‑dominant) are given without uncertainties.
Required fix: Add binomial 68% intervals or note that with N≈195k the statistical uncertainty is negligible compared to systematics.

P3-m4 — Appendix E, Eq. (E1)
Problem: Units and normalization constants are given implicitly.
Required fix: State explicitly the units used for Tobs and fi, and confirm the log base used throughout (common logs).

P3-m5 — Text consistency
Problem: Occasional dense internal-provenance strings (pipelines/.../json) interrupt flow.
Required fix: Keep a clean narrative in the main text; move verbose provenance links to a “Reproducibility notes” appendix or a single consolidated subsection.

NIT

P3-N1 — Typo/notation
Problem: “Nanom” in Table I header is unusual.
Required fix: Use N_anom or just “Anomalies.”

P3-N2 — Hyphenation/style
Problem: Mixed “5-fold”/“5 fold,” inconsistent spaces before units (e.g., “5
′′”).
Required fix: Standardize hyphenation and spacing (arcsec symbol).

P3-N3 — Repeated phrasing
Problem: The “largest-scale/141×” claim appears several times.
Required fix: Keep once in abstract and once in conclusion.

Arithmetic and consistency spot-checks (selected)

- 195,829/22,504,897 = 0.00870 (0.87%): correct.
- 77,905/2,304,830 ≈ 3.38%: correct.
- 44,075/11,418,594 ≈ 0.386% (0.39%): correct.
- Cross-transfer total 319,443 over 37,292,042 ≈ 0.857%: correct.
- Path‑C per‑survey native counts sum 388,493; unique 378,280; 388,493–378,280 = 10,213 collapsed = 637 multi‑survey + 9,576 intra‑survey: consistent.
- 378,080/2,685 ≈ 141.0×; 269,117/2,685 ≈ 100.2×; 195,829/2,685 ≈ 72.9×: consistent with text.
- NEOWISE polar‑cap null area 2 caps of 10°: fraction = 1 − cos 10° ≈ 1.52%; observed 17/436 = 3.90% ≈ 2.6×: consistent.
- SIMBAD false‑match at 5″: π(5″)^2 × 3×10^-5 arcsec^-2 ≈ 0.00236 (0.236%): consistent with “≈0.24%.”
- Fisher envelope: with F0 = 1/8.98^2, c = 0.0747, α = 0.19 gives σ = 8.14 and α±σα ⇒ [3.92, 8.98]: consistent.
- NANOGrav: γ = 2.567 ± 0.382 ⇒ distance to γ = 3.0 is +0.433/0.382 = +1.13σ; to 4.33 is +1.763/0.382 = +4.61σ: consistent.

Abstract-last drift sweep

The abstract is unusually detailed and, after cross-checking, largely aligned with the calibrated statements in the body. However, three points must be corrected in the abstract to match calibrated statements:

- Do not count NEOWISE’s masking‑geometry test as an injection‑recovery PASS (see P3‑E5).
- Clarify the “catalog‑grade 269,317” and “269,117 point‑source” definitions as per P3‑E1 or adjust the numbers once reconciled.
- Either remove eROSITA from headline tallies or state explicitly that it is a membership‑only exploratory tier that does not contribute to the “catalog‑grade” subset (after you resolve P3‑E2).

Provenance surfaces

The Data Availability section includes placeholders and promises. For PRD, final DOIs, a frozen code release, and accessible artifacts are mandatory (P3‑E3). Statements like “consumers should verify against that manifest” are fine once the manifest and tag exist, not before.

Standalone-reader test

Several critical definitions (injection parameters; precise thresholds; Planck held‑out status; Gaia preprocessing) are currently partly in repository links or not recovered. Bring the load-bearing ones into the paper (P3‑E2, E4, M7).

Effect sizes and non-comparability of sigma metrics

The manuscript is generally careful to separate different sigma/“significance” conventions (forecast σ(fNL), gamma posterior shifts, jackknife Z for α). Maintain that separation and, where two sigmas appear in the same paragraph, add an explicit “not directly comparable” clause (you already do for σ(fNL) vs γ; keep it wherever they co-occur).

Page length

At 30 pages, the manuscript is long for its primary contributions (catalog construction and methodology). If the authors address the essential issues, I recommend trimming by consolidating long footnotes (Table I) into a single threshold/gate subsection, moving verbose provenance into one appendix, and shortening the spatial χ^2 section. A target length of ≈24–26 pages should be achievable without loss of content.

## Summary recommendation
MAJOR REVISIONS

The study is ambitious and potentially impactful, but core methodology/reproducibility issues must be corrected: (i) eROSITA’s irreproducible score axis must be fixed or removed from headline results; (ii) the “catalog‑grade” subset definitions and counts must be reconciled and clearly tabulated; (iii) the NEOWISE geometry QA must be removed from the “PASS” injection‑recovery tally; (iv) Gaia/NEOWISE preprocessing leakage and missing Gaia code must be resolved or these tiers demoted; (v) the Planck top‑200 must be selected from a held‑out bank or labeled exploratory; and (vi) the data/code DOI releases must be finalized. Addressing these, plus the listed major/minor issues, will bring the manuscript to PRD methodology standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (fresh pass)

ESSENTIAL

P3-E10 — §IV B (p. 15): Cramér’s V expression/number mismatch
Problem: The text prints “Cramér’s V = √(χ²/(N·(k−1))) = 376,713/(378,280×24,047) ≈ 0.0064.” The numeric substitution shown is χ²/(N·(k−1)), not its square root; χ²/(N·(k−1)) ≈ 4.14×10−5, while √(χ²/(N·(k−1))) ≈ 0.0064. As written, the algebraic form and the numeric substitution are inconsistent.
Required fix: Correct the displayed calculation to show the square-root step explicitly (or remove the intermediate fraction). Verify all subsequent use of this effect-size is consistent with the intended √-form.

MAJOR

P3-M10 — Fig. 10 and §VI D(ii): Mixed x-axes (detector sensitivity vs geometry QA) plotted on the same “injection amplitude” axis
Problem: Fig. 10 overlays recovery curves for SDSS/LAMOST/eROSITA/Gaia (true sensitivity vs amplitude in units of noise σ) with NEOWISE’s masking-geometry QA (latitude-threshold “plants” recovered by a fixed mask), yet all are shown against a common “Injection amplitude (× noise σ)” axis. This conflates qualitatively different abscissas and can mislead a reader into interpreting the NEOWISE curve as a sensitivity result.
Required fix: Separate geometry QA results into a distinct panel or clearly different axis styling, and remove them from any sensitivity PASS count (cf. your own caveat text). Label axes unambiguously for each class. Cross-reference this separation in the abstract and conclusions when summarizing PASS tallies.

P3-M11 — Appendix E Eq. (E1): Dimensional/definition clarity for the PTA free-spectrum mapping
Problem: The power-law template uses a leading 1/2 factor and includes a −log10 Tobs term: log10 ρi = ½[2log10 A − log10(12π²) + (γ−3)log10 fyr − γ log10 fi − log10 Tobs]. This deviates from the standard continuous PSD form P(f) = A²/(12π²)(f/fyr)−γ (up to unit factors). It’s unclear whether ρi denotes a discretized per-bin amplitude, a PSD mapped to Fourier-coefficient variance, or another convention. Units (yr, Hz), the role of the extra ½, and the appearance of Tobs need explicit derivation for dimensional consistency.
Required fix: Provide a short derivation or citation that connects Eq. (E1) to the ceffyl free-spectrum convention, making clear: (i) what ρi represents, (ii) why the ½ factor appears, (iii) how Tobs enters when mapping continuous PSDs to discretized bin amplitudes, and (iv) the units (and log base, if not base 10). Confirm that, in the continuous limit, Eq. (E1) reduces to the standard PSD expression.

P3-M12 — Abstract and §I/§VI E: “Largest/multi-archive” claim support
Problem: The “largest-scale application … across multiple astronomical archives” claim is anchored to a single-survey benchmark [11]. No systematic multi-archive comparison is provided.
Required fix: Either (a) add a brief literature census (even a small table) comparing multi-archive anomaly searches (if any) by size/scope/model, or (b) rephrase to “largest-scale of which we are aware; benchmarked against the largest prior single-survey catalog [11]” and move the stronger “largest multi-archive” phrasing out of the abstract.

P3-M13 — §III F (pp. 12–13): Planck validation p-value assumptions
Problem: The “overrepresentation toward held-out patches (naive binomial p ≈ 4 × 10−4)” assumes independent patches. Given 10°×10° gnomonic tiles and potential tiling overlap/correlation, independence may not hold.
Required fix: Quantify patch overlap or correlation (e.g., report the effective number of independent patches via block bootstrap or spatial thinning) and recompute an appropriate p-value; alternatively, present only the effect size (48/200 validation vs ~30 expected) without p, with a clear caveat about non-independence.

MINOR

P3-m6 — §IV B (p. 15): Cramér’s V notation consistency
Problem: Beyond P3-E10’s numeric correction, the typeset form “p χ² p /(N·(k−1))” suggests a formatting artifact. Ensure the square root is typeset unambiguously as √(χ²/(N·(k−1))).
Required fix: Fix notation; optionally add a one-line definition of k and N and reference the exact χ² table used.

P3-m7 — §IV A, Fig. 6 caption: Matching-radius consistency and labeling
Problem: The figure’s dashed “aggregate 58.8%” is computed at 3″ while most per-survey unmatched fractions (and the text default) use 5″. The caption notes this, but the plot itself does not indicate the 3″ basis prominently.
Required fix: Add “3″ pooled run” directly on the figure or in the legend, and consider adding a 5″ pooled figure or a sentence giving the 5″ pooled fraction for completeness.

P3-m8 — §IV C (p. 15–16): “≤ 10 random coincidences” across survey pairs lacks derivation
Problem: The statement “expected random coincidence contribution is ≲10 across all survey pairs” is not supported by a calculation (unlike the SIMBAD false-match estimate).
Required fix: Provide a brief derivation or simulation-based estimate (pairwise density × area × number of pairs, with footprint masking), or remove this sentence and retain only the observed 637 multi-survey clusters plus the RA-shift control where used.

P3-m9 — §III C (p. 9): SDSS retrieval-failure phrasing
Problem: “a further 3,394 spectra, 0.18% nominal, failed retrieval during the re-score” could be misread relative to the 1,925,279 re-score pool and the 2,304,830 total. The majority drop comes from quality cuts, not retrieval failure.
Required fix: Rephrase to make clear that 379,551 spectra were excluded by quality cuts, and 3,394 additional spectra (0.18% of the re-score pool) failed retrieval.

P3-m10 — §III H (p. 13): NEOWISE mask injection count is ambiguous
Problem: “Mask injection-recovery: 1000/1000 = 100% … planted at |becl| > {85°, 82°, 80.5°}” leaves unclear whether 1000 is total across all latitudes or per-latitude cohort.
Required fix: State the number of injected sources per latitude cohort and total (e.g., 1000 total = ~333 per cohort), and confirm the recovery criterion.

P3-m11 — §IV C (p. 15–16): Coordinates for highlighted cross-survey matches
Problem: The three DESI×SDSS matches are discussed but coordinates are not listed in the paper (only in the repo).
Required fix: Add a small table (or footnote) with RA/Dec (ICRS), survey IDs, and classes for the three matched objects.

P3-m12 — §III F/Table VI: Reproducibility of the “200/200 overlap” Planck top-200 ranking
Problem: You report “200/200 reproduced; Spearman ρ > 0.9999999.” GPU nondeterminism can affect exact reproduction unless seeds and determinism flags are set.
Required fix: State the random seed(s), determinism settings, and whether CuDNN deterministic mode or similar was used; or qualify that reproduction was achieved on the quoted hardware/software stack.

P3-m13 — Fig. 7 bottom-right panel: Unexplained horizontal reference line
Problem: The red dashed line in “Score vs Galactic distance” is unlabeled; it appears to be the DESI S=5 threshold, but this isn’t stated.
Required fix: Label the reference line (e.g., “S=5 threshold”) or remove it if not discussed.

P3-m14 — §V A and Appendix E: Jeffreys’ scale usage
Problem: You label BMB/SMBHB as “decisive” per Jeffreys’ scale, but immediately (correctly) caution on prior sensitivity and environmental SMBHB models.
Required fix: Consider softening the Jeffreys-language in the main text (keep the numerical Bayes factors, with the existing caveats).

NIT

P3-N4 — Minor style in Fig. 5 caption text overlay
Problem: The overlay text shows “Score = 11.5 | ( , ) = (180.59°, 0.56°)” with stray delimiters.
Required fix: Clean the annotation to “Score = 11.5; (RA, Dec) = (180.59°, 0.56°).”

P3-N5 — Global: “Actively scored bank includes training data” phrasing
Problem: In §III F, “the native bank is scored in full — including the patches used for training” could be misread.
Required fix: Add “(selection made on the full bank; to avoid leakage, provide a validation-only top-200 or label as exploratory)” and cross-link to your resolution per P3-E6.

Explanation
This fresh pass focused on arithmetic consistency, figure–text alignment, unit/definition clarity in equations, comparability of null procedures/sigma values, and abstract faithfulness. The new issues above were not covered in the original report and, if addressed, will further strengthen methodological rigor and clarity. If the authors resolve the earlier essential items plus these additional points, the manuscript will better meet PRD methodology standards.