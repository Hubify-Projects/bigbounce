# P5 auto-2026-06-08_1354pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7211 chars)
**Wall time**: 316.0s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test …”

Scope of review
- Focus: statistical and methodological rigor, internal arithmetic, propagation of uncertainties, null-procedure consistency, and figure/table coherence.
- I read all 20 pages (including figures, tables, equations, captions). Below I itemize findings with IDs, page/section, issue, and required fix. Severity levels are ESSENTIAL, MAJOR, MINOR, NIT.

ESSENTIAL findings

P5-E1 (Abstract p.1; throughout): Mislabeling of the classifier as “V-Web”
- Text: “We run a V-Web tidal classification … tidal-tensor cosmic-web classifier (Hahn et al. 2007; Cautun et al. 2014) … We retain the ‘V-Web’ label which is sometimes used loosely …”
- Issue: The algorithm implemented is the tidal Hessian/T-Web classifier (density–potential Hessian eigenvalues), not the velocity-shear “V-Web.” The footnote (p.2) acknowledges this but then proceeds to use “V-Web” everywhere, including figures and tables. This is not acceptable for PRD; it confuses two distinct formalisms with different systematics (especially under RSD).
- Required fix: Rename all instances of “V-Web” to “T-Web (tidal-tensor)” or “tidal-tensor web classifier,” including figures/captions/tables, and rewrite the footnote on p.2 accordingly. Where necessary, distinguish from the velocity-shear V-Web with an explicit sentence in Sec. IV.A and the Abstract.

P5-E2 (Sec. VII, p.8–10; Fig. 5): Incoherent sample size and σ in Phase-2 sweep
- Text: “The largest single-cell |σfrom half| across the entire sweep is 11.32 (filament at Rs = 10, λth = 0, n = 3,696,152). This is the catalog-wide ΔfCW monopole … predicted, not measured.”
- Issue: n = 3,696,152 exceeds the total chirality-relevant matched sample (791,635). Reporting a class-level σfrom half for chirality using N that apparently refers to the full 14.6M spectroscopic sample (not the CW/CCW-labeled subset) is methodologically invalid and internally inconsistent. The paragraph mixes prediction and “observed 11.32,” but calls it “predicted, not measured” after presenting it as an observation.
- Required fix: Remove this σfrom half claim or recompute it strictly on the chirality-labeled sample within that sweep cell, with the correct N. If the intent was to illustrate scaling, keep only the theoretical σpred = 2 ΔfCW √N formula with N explicitly defined (and not as an “observed” statistic). Ensure every σ quoted in Sec. VII is computed from the same, clearly stated population.

P5-E3 (Sec. VI.D.b p.7 vs Sec. XI p.17): Contradictory statements on target-program split
- Text A (p.7): “bright (n=775,760) fCW = 0.4970, σ = −5.25; dark (n = 14,782) fCW = 0.5051, σ = +1.25”
- Text B (p.17 Systematics): “target-class split (BGS vs. LRG-ELG-QSO) with BGS-only CW fraction within ±0.001 of LRG-ELG-QSO.”
- Issue: The two statements are incompatible (0.4970 vs 0.5051 is a Δf ≈ 0.0081, not within ±0.001). This undermines the systematics section and any conclusions drawn from it.
- Required fix: Recompute and report the target-program split consistently (same cuts/filters in both places), including uncertainties and an explicit two-proportion z-test. If different filters were applied, state them clearly and explain why the conclusions differ. Remove or correct the “±0.001” claim.

P5-E4 (Multiple sections; Eq. (1) p.4; Sec. V, VI, VII, VIII.F, XV): No propagation of uncertainty in the catalog monopole ΔfCW
- Text: The analysis repeatedly subtracts or compares to a fixed ΔfCW = −0.0026 (“Paper IV monopole”), using σpred = 2 ΔfCW √N, and tests residuals against thresholds, but no uncertainty on ΔfCW is propagated.
- Issue: Treating ΔfCW as known exactly biases subsequent significance statements (σvs monopole, Bonferroni comparisons, ranges). Paper IV is an external, not-yet-peer-reviewed input and quotes fCW uncertainty; that uncertainty must be propagated into σpred and all residuals that rely on it.
- Required fix: Quote the uncertainty on ΔfCW from Paper IV and propagate it into:
  - σpred error bars per class/bin,
  - σvs monopole residual uncertainties,
  - all null comparisons that depend on subtracting the monopole.
  Provide revised significance statements reflecting this uncertainty. If the propagated uncertainty is negligible at your precision, show that quantitatively.

P5-E5 (Sec. V.A p.4; throughout): Mixed significance metrics without a clear comparability disclaimer
- Context: The manuscript juxtaposes “σfrom half,” Bonferroni thresholds on Gaussian z, and permutation p-values/max-statistics across sections/figures/tables (e.g., Table V lists a max-|σ| and a permutation p; Sec. VI.D compares class-level σ’s vs Bonferroni; Sec. VII mixes per-cell ranges with σpred justification).
- Issue: Different test statistics (one-sample z vs. permutation-based max-stat p) are compared and interpreted in proximity without a persistent, explicit “not directly comparable” caveat. Per instruction for review, this must be explicitly tagged wherever used side-by-side.
- Required fix: At each instance where two different null procedures or test statistics are placed side-by-side (Gaussian z vs. permutation p or max-|σ| vs. permutation thresholds), add a sentence that they are not directly comparable and are used as complementary diagnostics. Where a decision hinges on one, make that the primary statistic and clearly state the secondary is only a cross-check.

P5-E6 (Data/code availability; multiple pages including Appendix B p.19): Insufficiently specific data/code availability for PRD reproducibility
- Text: “companion data repository,” “HuggingFace catalog,” “deterministic seed: 20260515.”
- Issue: No persistent DOI or exact repository URL is provided; the “companion repository” is not specified. PRD requires reproducibility with durable links.
- Required fix: Provide permanent DOIs (e.g., Zenodo) for:
  - The exact versions of all analysis code and configs,
  - All derived data products used to generate the figures/tables,
  - The precise hash/commit of any third-party catalogs used.
  Include instructions sufficient to reproduce all tables/figures from raw inputs.

MAJOR findings

P5-M1 (Sec. VII p.8–10; Fig. 5; Table VI): Quantifying the statistical meaning of the “range”
- Text: The per-cell class-to-class fCW range is used as a robustness statistic; the max range = 0.22 pp is asserted to be below counting-statistics floors and catalog-monopole-subtracted residuals.
- Issue: While some framing is given (Sec. VII.A), there is no formal hypothesis test mapping the max-range to a null distribution (except for a passing statement about label-shuffle pLEE = 0.41–0.67), and the equivalence between the range and a “residual environmental signal” is asserted rather than established.
- Required fix: For each sweep cell, explicitly report the permutation-based null distribution of the class-to-class range statistic (NMC ≥ 10,000; 1,000 is too small to resolve tails at α=0.01 in a max-stat test across nine cells) and the corresponding p-value. Move the max-range conclusion onto one clearly defined statistic with its own null.

P5-M2 (Sec. VI.B p.6): Logistic regression without uncertainties
- Text: “logistic regression of the CW indicator on {z, |sin δ|, cos α, confidence} gives a z-coefficient of 0.0059 with no significant intercept (0.000652), consistent with no redshift dependence.”
- Issue: Coefficients are reported without standard errors, p-values, model details (link, covariate scaling), or goodness of fit. The numerical magnitudes alone are uninterpretable.
- Required fix: Report standard errors, Wald p-values, and model specification. State the sample size used, covariate scaling, and whether robust SEs were employed. If the regression adds nothing beyond the binned tests, consider removing it.

P5-M3 (Sec. VIII.A p.10–11): “0/6” DESIVAST-vs-T-Web void overlap used to support “survey-edge artifact dominated”
- Text: “Restricting to z ≤ 0.24 leaves only n = 6 V-Web void-class spirals … 0/6 lie inside any DESIVAST hole … consistent with survey-shell systematics … the V-Web void class at low z is dominated by survey-edge density artifacts…”
- Issue: n=6 is too small to support the strong “dominated by” language; the inference is not statistically warranted from 0/6. This should be framed as anecdotal/illustrative, not evidential.
- Required fix: Either:
  - Provide a robust quantitative test of V-Web void purity vs. mask proximity over the full void-labeled sample (e.g., distribution of distances to the survey mask compared to non-voids; fraction of void-class cells near low-coverage regions), or
  - Soften the claim and present this as an illustration only, deferring the purity statement to the independent T-Web comparison (Sec. IX.B) and the DESIVAST-based void re-projection (Sec. VIII.B–E).

P5-M4 (Sec. VIII.B–C p.11–12; Table VII–VIII): Absent two-sample significance for ΔfCW comparisons
- Text: E.g., DESIVAST VoidFinder: f_void = 0.4964 vs f_non-void = 0.4971 → Δf = 0.0007; qualitative “statistically indistinguishable.”
- Issue: No formal two-proportion z-test or confidence interval on Δf is given. This is easy to provide and central to the “no difference” claim.
- Required fix: For each DESIVAST algorithm (VoidFinder, V2-REVOLVER, V2-VIDE), provide:
  - Δf with a 68% and 95% CI (e.g., Newcombe/Wilson),
  - Two-proportion z-test statistic and p-value,
  - A unified statement that all three are consistent with Δf = 0 within Xσ.

P5-M5 (Sec. VI.D p.6–7; Table IV): Within-class density-stratified findings need exact bin definitions and uncertainties
- Text: Quartiles and mean densities are reported, with σfrom half per quartile; interpretation relies on non-monotonicity.
- Issue: No fCW values or CIs are listed; only σfrom half are shown. The bin definitions for “density quartiles” (exact variable, normalization) are not fully specified.
- Required fix: Report fCW and their 95% CIs per quartile; specify precisely how “per-galaxy density field” is normalized (e.g., log-density? smoothed δ?), and the quartile thresholds.

P5-M6 (Sec. V.A p.4): Bonferroni thresholds formula and usage
- Text: “|σ|_Bonf = √2 erfc^{-1}(α/K)”
- Issue: The formula corresponds to a two-sided Gaussian tail if erfc is used appropriately; however, later numerical thresholds are quoted without always stating whether they are two-sided and what K is after masking bad/empty bins.
- Required fix: Explicitly state two-sided correction and the effective K used in each application (after dropping small-N or empty bins). Where empirical max-stat permutation pLEE is available, make it the primary LEE control; otherwise justify Bonferroni use for correlated bins.

P5-M7 (Sec. V.B p.5; Abstract p.1; Conclusions p.18): Primary estimator declared post hoc; headline vs. primary path mismatch
- Text: The Abstract headline presents the T-Web class fractions; Sec. V.B then declares DESIVAST void re-projection as “primary” post hoc.
- Issue: The “primary” estimator should be declared before showing results to avoid garden-of-forking-paths concerns in a PRD methods paper.
- Required fix: Reorder the presentation so that the primary DESIVAST analysis is introduced and motivated before the T-Web results, or explicitly justify why the T-Web table appears as the headline when the primary is DESIVAST. Keep the post-hoc admission, but bring the primary test forward.

P5-M8 (Sec. VIII, XIII p.17): RSD claims vs. smoothing scale
- Text: DESIVAST “essentially RSD-immune” at the per-object membership-test level; later, the scalar σv/(aH) vs. Rs heuristic is used to argue sub-percent contamination.
- Issue: The RSD immunity claim is qualitative; some numbers are quoted but without a formal bound for the DESIVAST binary void/non-void misclassification rate induced by RSD given the published void radii distribution.
- Required fix: Add a simple quantitative bound: e.g., for each void, fraction of boundary-shell volume of thickness σv/(aH) relative to void volume, aggregated over the void population; translate to an upper bound on membership flips. This will align the claim with numbers.

MINOR findings

P5-m1 (Sec. III.C–D p.3): Match-separation summary
- Text: “Median separation 0.0066 arcsec; p99 0.30 arcsec.”
- Comment: Given that both catalogs inherit coordinates from the same imaging leg for many targets, a near-zero median is plausible. Still, provide a histogram or at least quartiles to reassure readers there is no unit bug (mas vs. arcsec).
- Fix: Add a small inset/histogram or a table with p25/p50/p75.

P5-m2 (Sec. VI.C p.6–7; Fig. 3; Table III): Projected-density proxy definition
- Text: “k=5 NN spiral on the sphere” used as projected-density proxy.
- Fix: State whether the NN set is restricted to the chirality-relevant subset or to all matched primaries; and whether masking/holes were handled (e.g., great-circle distances within footprint only).

P5-m3 (Sec. IX.A p.15–16; Fig. 7; Table XI): Tempel FoF mapping
- Text: Mapping multiplicity bins to V-Web classes is heuristic.
- Fix: Clarify that the filament-like pairing is used only as a coarse check; include the two-sample Δf with CI for the filament pair to substantiate the 0.026 pp concordance claim (currently stated but not numerically demonstrated with a CI).

P5-m4 (Sec. VIII.E p.12; Table IX): Maximal-void binning
- Text: HEALPix NSIDE=16 bins “0, 1–2, 3–5, 6+.”
- Fix: Report the number of pixels per bin and their sky-area fractions to contextualize the n’s; explicitly state if the “0” bin lies outside the DESIVAST footprint (you imply this, but a mask-plot or a sentence with exact area fractions would help).

P5-m5 (Sec. IX.B p.15): Comparison to concurrent T-Web analysis
- Text: “void fraction higher by +8–18 pp,” “knot lower by 3–5 pp.”
- Fix: Provide a direct apples-to-apples comparison on your own T-Web run by recalculating in a cubic sub-volume similar to [11], or clearly tag the comparison as qualitative only. The stated ranges should be tied to exact tracer and volume definitions.

P5-m6 (Sec. X p.16–17; Table XII): ASTRA overlap
- Text: Noverlap = 25,186; “per-galaxy classifier agreement is poor … but headline null recovered.”
- Fix: Briefly quantify the level of disagreement (e.g., confusion matrix percentages or an Adjusted Rand Index) to support the “poor agreement” statement.

P5-m7 (Sec. V p.4): NMC = 1000 permutations
- Text: For the LEE scans, the paper states consistency between Bonferroni and empirical max-stat to ~10%.
- Fix: Increase to NMC ≥ 10,000 for LEE-calibrating the max-statistic in the HEALPix scans and the density-quintile scan, or justify why 1,000 is sufficient for the quoted p’s. Also report Monte Carlo SE on the estimated pLEE.

P5-m8 (Sec. VI.A p.5; Table II): Jeffreys intervals
- Text: The figure shows Jeffreys 95% CIs but the table lists only point estimates and σfrom half.
- Fix: Add CIs in the table for completeness.

NITs (cosmetic/clarity)

P5-n1 (Multiple pages): Typographical “2563”
- Replace “2563” with “256^3” everywhere.

P5-n2 (Abstract p.1; Sec. IV.B p.4; Fig. 1): Percentages and units
- Ensure all reported fractions that appear as percentages in text are labeled “percentage points (pp)” when reporting differences (you do so in many places; make it universal).

P5-n3 (Sec. V p.4): Equation (1) typesetting
- Make the denominator unambiguous: σpred = ΔfCW / (0.5/√N) = 2 ΔfCW √N.

P5-n4 (Sec. VIII.F p.13): “P5 monopole” vs “P4 monopole”
- Keep terminology consistent: use “Paper IV monopole” when referring to the external catalog-wide offset; reserve “P5” for this paper’s matched subsample monopole.

P5-n5 (Sec. VIII.E p.12; Fig. 6 caption): Spell out “NSIDE = 32” consistently; avoid switching between numerals and variables.

P5-n6 (Sec. VI.E p.8; Table V): Clarify “npix”
- State explicitly whether npix refers to “valid” pixels after cuts and what those cuts were.

Arithmetic checks performed (selected highlights)

- Table I sums check out: CW+CCW=791,635; NS+chirality-relevant = 2,232,212; SPECTYPE sums to matched primaries; imaging-leg counts sum correctly. Median separation plausibly near zero because both catalogs inherit Legacy imaging coords.

- Table II and Fig. 2 σfrom half recompute correctly from N and fCW within rounding:
  - Void (N=428, f=0.4836): σ ≈ −0.678; listed −0.68.
  - Wall (N=6,673, f=0.5034): σ ≈ +0.556; listed +0.55.
  - Filament (N=408,187, f=0.4980): σ ≈ −2.55; listed −2.61 (small rounding/hidden precision in f).
  - Cluster (N=397,505, f=0.4963): σ ≈ −4.67; listed −4.66.
  Range 1.98 pp matches.

- Density quintiles (Table III): With N ≈ 158,327/bin, σpred = 2|Δf|√N ≈ 2.07; residuals as listed (e.g., quintile 3: observed −3.94 vs pred −2.07 ⇒ residual 1.87).

- DESIVAST void vs non-void (Table VII): Nvoid = 56,981; f=0.4964 ⇒ σ ≈ −1.72; Nnon=621,964; f=0.4971 ⇒ σ ≈ −4.56. Δf=0.0007 corresponds to z ≈ 0.32 on a two-proportion test (consistent with “indistinguishable,” but please add the formal statistic).

- Three-algorithm DESIVAST (Table VIII): Spot-checks of σfrom half within expected rounding.

- HEALPix maximal-void stratification (Table IX): σ values recompute correctly from N and f. Paper IV monopole residuals mentioned in the text (−1.55σ and +0.60σ) also check out approximately.

- Monopole-subtracted residuals (Table X): Residual σ vs fP5_CW recompute correctly.

- Tempel FoF (Table XI): σfrom half recomputes within rounding.

Unsupported or over-strong claims

P5-U1 (Sec. VIII.A p.10–11): “Dominated by survey-edge artifacts” for the T-Web void class at z ≲ 0.24 is too strong given n=6; see P5-M3 fix.

P5-U2 (Sec. VIII.F p.13): “Direct single-test demonstration” that all T-Web class-level σ values are projections of the Paper IV monopole
- Comment: The monopole-subtracted residuals are small (|σ| < ~1.15), but to call it a “direct single-test demonstration” is stronger than warranted without propagating ΔfCW uncertainty (P5-E4). Soften the language after uncertainty propagation.

P5-U3 (Sec. VIII.D p.12): “The V2-REVOLVER catalog-native σ = −0.24 is the cleanest single chirality-in-voids measurement in this paper”
- Comment: “Cleanest” should be justified (e.g., lowest estimated systematics plus largest N after edge-exclusion). Otherwise rephrase to “lowest |σ| at large N among our void definitions.”

P5-U4 (Sec. VIII.E p.12): The strong emphasis that the −5σ catalog-level signal is “entirely” in the no-coverage pixels should be kept qualitative unless backed by a variance decomposition. As written, it’s plausible but not proven. Consider softening to “concentrated.”

Other comments

- The manuscript is very long relative to its core contribution (environment-conditional null). A leaner paper would increase clarity. Consider reducing length to ~14 pages by moving secondary cross-checks (Tempel, ASTRA details, some HEALPix scans) into an Appendix or a data release note.

- Avoid fantastical p-values like “p < 10−1000” (Sec. VI.D.d p.8). Report numerical limits consistent with double precision or Monte Carlo resolution (e.g., p < 10−300, or “p ≪ 10−10”).

- The EFT toy appendix is clearly labeled as schematic and non-binding. That is acceptable as long as it remains explicitly illustrative and does not creep into the main conclusions.

## Summary recommendation
MAJOR REVISIONS

The central result (no detectable environment dependence of spiral chirality at the stated sensitivity) is plausible and the arithmetic for most headline numbers checks out. However, several essential issues must be corrected for PRD: incorrect “V-Web” nomenclature, an internally inconsistent Phase-2 σ claim tied to an impossible N, a serious contradiction between two places reporting the target-program split, and missing propagation of the external monopole uncertainty into all “monopole-subtracted” significance statements. Additional major clarifications are needed for the DESIVAST/T-Web void purity claim (n=6 is not evidential), the formal two-sample tests for Δf in DESIVAST analyses, and the statistical meaning of the per-cell range in the sensitivity sweep. Addressing these items will materially improve methodological rigor and align the paper with PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (fresh pass)

ESSENTIAL

P5-E7 (Sec. VI.A p.5 vs Sec. VII/Table VI p.8–9; Abstract p.1): Phase-2 “range” is numerically incompatible with the canonical run
- Issue: The canonical T-Web/V-Web class fractions in Table II span 0.4836–0.5034 ⇒ a range of 1.98 pp at Rs = 25 Mpc/h, λth = 0. Yet Table VI reports the per-cell class-to-class fCW range for that same cell as 0.165 pp, and the Abstract states the max range across all cells “never exceeds 0.22 pp.” These cannot both be true if the statistic is the unadjusted range of fCW across classes on the same chirality-labeled sample.
- Required fix: Recompute and reconcile. Explicitly define which population and which statistic the “range” uses (raw fCW, monopole-subtracted fCW, weighted by class Ns, or computed on a different subset). If it is a different statistic (e.g., monopole-subtracted or computed on a different sample), state that clearly in Sec. VII and in the Abstract, and correct Table VI and any text that currently says “range of fCW.” If it is indeed fCW on the same sample, correct the numbers; the Rs = 25, λth = 0 cell should reflect ~1.98 pp, not 0.165 pp.

P5-E8 (Sec. VIII introduction p.10 vs Sec. VIII.C p.11–12): Contradictory DESIVAST void counts for V2-REVOLVER/VIDE
- Text conflict: “420 with V2-REVOLVER, and 295 with V2-VIDE” (p.10) versus “V2-REVOLVER (n_catalog void = 1,992), V2-VIDE (n_catalog void = 1,478)” (p.11–12).
- Issue: Two incompatible sets of void counts are reported for the same catalogs.
- Required fix: Correct the catalog statistics and cite the exact DESIVAST tables/columns used (with file names). Make the counts internally consistent throughout the section and anywhere else they are referenced. If different definitions are intended (e.g., “maximal” vs “effective” vs “interior”), label them explicitly.

P5-E9 (Sec. VIII.E p.12/Table IX vs Fig. 6 caption): HEALPix NSIDE and pixel statistics mismatch
- Text: Sec. VIII.E and Table IX analyze “NSIDE = 16” (bins 0, 1–2, 3–5, 6+ maximal voids per pixel). 
- Fig. 6 caption: “NSIDE = 32,” “885 occupied pixels, median 4 voids/pix” for the top panel; bottom panel references “1,496 valid pixels.”
- Issue: The figure and the body text use different NSIDEs and pixel stats without cross-referencing; readers cannot tell which result corresponds to which grid.
- Required fix: Align the figure with the text or explicitly state that Fig. 6 is at NSIDE=32 as a separate visualization, not the same analysis as Table IX. Include consistent counts/area fractions and clearly label which NSIDE each statistic uses.

MAJOR

P5-M9 (Sec. VIII.B–D p.11–12; Table VII–VIII): Ambiguity in the composition of the z ≤ 0.24 sample used for DESIVAST tests
- Text: nlz = 678,945 is described as the “matched-spiral subsample,” then partitioned into nvoid = 56,981 and nnon−void = 621,964 (summing to 678,945). fCW is then computed for both bins.
- Issue: It is unclear whether 678,945 is the chirality-labeled subset (CW/CCW only) or all matched primaries (including NS). fCW can only be computed on the labeled subset. The current wording conflates “matched-spiral” with “chirality-relevant.”
- Required fix: State explicitly that nlz = 678,945 is the number of chirality-relevant objects at z ≤ 0.24 if that is the case; otherwise provide the chirality-relevant counts used to compute fCW in void and non-void and ensure the totals in Table VII/VIII refer to that labeled subset. Add nCW and nCCW per bin (void, non-void) for transparency.

MINOR

P5-m9 (Sec. VI.A p.6): Miscomputed σpred for filament under the Paper IV monopole
- Text: “σpred(filament) ≈ −3.16 and σpred(cluster) ≈ −3.28” at Δf = −0.0026.
- Check: σpred = 2Δf√N. For Nfil = 408,187, σpred ≈ −3.32; for Ncl = 397,505, σpred ≈ −3.28 (cluster is fine, filament is not).
- Fix: Correct the filament σpred and revise any comparisons that rely on −3.16.

P5-m10 (Sec. VI.D.d p.8): Bright-fraction deviation arithmetic
- Text: “max class-to-overall bright-fraction deviation 1.5 pp” with class bright fractions {0.981, 0.962, 0.966, 0.989} vs overall 0.978.
- Check: Deviations are {+0.3, −1.6, −1.2, +1.1} pp; the maximum is 1.6 pp, not 1.5 pp.
- Fix: Correct the stated maximum deviation.

P5-m11 (Sec. VII p.8): Notational glitch for the sweep configuration
- Text: “Ngrid = 256 × λth ∈ {0.0, 0.1, 0.3}”
- Issue: As written it suggests multiplication by λth. Presumably you intend Ngrid = 256^3 with λth swept over {0.0, 0.1, 0.3}.
- Fix: Clarify to “Ngrid = 256^3; λth ∈ {0.0, 0.1, 0.3}.”

P5-m12 (Sec. VIII.E p.12; Table IX): Pixel statistics context
- Text: Bins listed with n per bin, but no counts of pixels per bin or sky-area fractions.
- Fix: Add the number of HEALPix pixels and their sky-area fractions per bin to contextualize the sample sizes; explicitly state that the “0” bin lies outside DESIVAST coverage (as implied in the text).

P5-m13 (Sec. IX.B p.15): Qualitative T-Web comparison could be misread as quantitative
- Text: Void fraction differences quoted as “+8–18 pp,” knot “3–5 pp,” from a concurrent DR1 analysis on an 800 Mpc cube with tracer-specific cuts, versus your thin-shell all-spectro run.
- Fix: Either provide an apples-to-apples sub-volume/tracer re-computation on your side, or explicitly tag the comparison as qualitative only in the body (not just implied by caveats).

P5-m14 (Global): Mixed h units
- Issue: The manuscript alternates between “Mpc/h” and “h−1 Mpc.”
- Fix: Choose one convention and apply it consistently.

P5-m15 (Sec. VI.E p.8; Table V): Multiple NSIDE choices imply multiple tests
- Issue: Three NSIDEs are scanned and each reported with an empirical p. While all are nonsignificant, the multiplicity across NSIDEs is not acknowledged.
- Fix: Add a brief note that scanning over NSIDE adds another look-elsewhere layer; confirm the qualitative conclusion (all p’s > 0.05) is unchanged after a simple Bonferroni over the three NSIDEs.

P5-m16 (Appendix A p.18–19): Dimensional consistency of the toy operator
- Issue: Lparity ⊃ gϕ (∇ϕ)(∇ρ/ρbg)(L̂·ẑ) as written does not display units consistent with a Lagrangian density. You flag this as schematic and non-covariant, but a sentence on dimensional normalization would help avoid confusion.
- Fix: Add a sentence noting that gϕ carries the compensating dimensions to yield a Lagrangian density and that the operator is a heuristic parametrization in a fixed slicing.

P5-m17 (Abstract p.1; Sec. VII p.8–10): Units on “range” values
- Issue: The Abstract mixes “0.22 percentage points (max 0.0022)” without explicitly stating that 0.0022 is the fractional equivalent.
- Fix: Clarify once (e.g., “0.22 percentage points, i.e., 0.0022 in absolute fraction”) and use one convention thereafter.

P5-m18 (Sec. V.A p.4; Eq. 2 usage in text): Effective K for Bonferroni after filtering
- Issue: Several places reference Bonferroni thresholds but do not always state the effective K after dropping empty/small-N bins.
- Fix: State the effective K for each application (e.g., after removing pixels with fewer than Nmin spirals) to make thresholds reproducible.

NO repeats of prior findings are included above. These items are in addition to the issues already identified in the initial review.