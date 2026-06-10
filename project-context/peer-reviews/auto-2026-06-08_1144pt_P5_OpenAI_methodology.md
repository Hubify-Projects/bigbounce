# P5 auto-2026-06-08_1144pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9809 chars)
**Wall time**: 485.7s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals” (20 pp)

Scope of this review
- Role: methodology rigor for PRD. I audited arithmetic, statistical procedures, internal consistency, figure/table numbers, and whether abstract and conclusions are fully supported by the body. All page numbers below refer to the rendered PDF pages you provided (1–20). All quoted text is taken verbatim from the manuscript.

Overall assessment
The topic is suitable for PRD Methods. The paper is thorough and transparent in many respects (e.g., explicit hyperparameter sweeps, label-shuffle nulls, Bonferroni corrections, pre-/post-selection caveats). However, there are several methodological and arithmetic inconsistencies that must be fixed before this can meet PRD standards. The most serious issues are:
- A hard inconsistency between the reported sample size used to compute a σ-from-half statistic in the Phase 2 sweep and the maximum possible number of chirality-labeled spirals (P5-E1).
- The primary DESIVAST void-membership classifier uses a k-nearest-neighbour shortcut that is not guaranteed to be lossless for point-in-sphere tests (P5-E2).
- Heavy reliance on an unpublished “Paper IV” monopole for significance calibration, while a directly measured P5 monopole on the same matched sample is available and should be used consistently (P5-M1).
- Systematic mixing of different “sigma” notions (one-sample σ-from-half; two-sample z-tests; permutation max-stat p-values) without an explicit, repeated “not directly comparable” qualifier at each juxtaposition, as required by the journal’s methodological clarity standards (P5-E3).
- Persistent misnaming of the Hessian-of-potential tidal-field classifier as “V-Web” when it is a T-Web/Tidal-tensor variant; the current footnote is insufficient for PRD (P5-M2).
- Missing permanent links/DOIs to the “companion data repository” required for reproducibility (P5-E4).

Below I itemize all findings.

ESSENTIAL

P5-E1 (Sec. VII A, p. 9–10)
Problem: In the Phase 2 sweep the paper states: “The largest single-cell |σfrom half| across the entire sweep is 11.32 (filament at Rs = 10, λth = 0, n = 3,696,152). This is the catalog-wide ∆fCW = −0.0026 monopole leaking through the largest sample bin…” The reported n = 3,696,152 cannot be correct for a chirality statistic: the total number of chirality-relevant matched spirals is 791,635 (or 812,793 in the extended env-labeled superset). There is no subset with n ≈ 3.7 million CW/CCW labels on which a σ-from-half for chirality could be computed. This appears to confuse the parent DESI spectroscopic count used to build the field with the chirality-labeled matched-spiral count used to compute fCW.
Required fix: Correct the sample size and re-compute the quoted σfrom half for the Phase 2 cell using the actual chirality-relevant class counts for that hyperparameter setting. If that 11.32 value was mistakenly computed from an unlabeled parent sample, retract it. Provide a per-cell table of class counts {nvoid, nwall, nfil, nclust} for the matched-spiral catalog so that the per-cell σ-from-half and the 0.22 pp range claim are auditable.

P5-E2 (Sec. VIII B, p. 11)
Problem: The DESIVAST-anchored void classification—central to the primary claim—uses a “k = 20 nearest-neighbour KDTree query on the hole centres, sufficient given the 24 Mpc/h maximum hole radius.” This is not guaranteed to be lossless: if more than 20 hole centers lie within 24 Mpc/h of a spiral (possible in dense hole fields), a true enclosing sphere could be missed. A k-NN query is not equivalent to a radius query.
Required fix: Replace the k-NN query with an exact radius query (KDTree.query_ball_point with r = Rmax per hole, or batched bounding-box prefilter + exact point-in-sphere test) or provide a strict proof/empirical verification that no spiral lies within 24 Mpc/h of >20 hole centers. Report the maximum number of hole centers within Rmax for any spiral and confirm that k was safely above that maximum. Recompute nvoid and ΔfCW if needed. This also applies to the V2-REVOLVER and V2-VIDE sphere tests.

P5-E3 (Multiple places: Abstract p. 1; Sec. VI D b–c p. 7–8; Sec. V p. 4–5; Sec. V B p. 5; Tables II–V; Fig. 3)
Problem: Different “sigma” conventions are used side-by-side—one-sample σ-from-half for per-bin deviations; two-sample z-tests for bright vs dark; permutation-based max-stat p-values for HEALPix scans; Bonferroni thresholds interpreted in σ units—without an explicit, repeated statement that these σ values are not directly comparable and refer to different null distributions/statistics. The Abstract itself juxtaposes σ-from-half statements and permutation p-values (“none reach 3σ after look-elsewhere correction”) without clarifying the mapping between p and σ.
Required fix: At every point where different test statistics are juxtaposed, add an explicit qualifier that the σ units correspond to different nulls and are not directly comparable. For HEALPix/density/redshift scans, either (a) report only permutation pLEE values and drop σ language, or (b) add the conversion used to state “3σ” after LEE and ensure a consistent convention. For the bright-vs-dark two-sample tests, state clearly that |z| refers to a two-proportion z under the pooled null and cannot be compared numerically to the one-sample σ-from-half.

P5-E4 (Appendix B, throughout)
Problem: The manuscript repeatedly references a “companion data repository,” but no URL/DOI/permanent archive is provided. For PRD Methods, reproducibility requires a citable, immutable deposit of code, configs, and derived data sufficient to reproduce all tables/figures.
Required fix: Provide a permanent repository link with a DOI (e.g., Zenodo, Figshare) containing: configuration files, scripts, environment specifications, random seeds, and all derived CSVs used to populate Tables I–XII and Figs. 1–7. The seed “20260515” is listed; ensure it is used consistently and documented.

MAJOR

P5-M1 (Sec. V, p. 4–5; Sec. VI A, p. 5–6; Sec. VIII F, p. 12–13; Abstract p. 1)
Problem: The paper calibrates expected deviations using the Paper IV catalog monopole ΔfCW = −0.0026 (unpublished) even though the present matched-spiral sample yields fP5CW = 0.49719 (Δf ≈ −0.00281; −5.00σ) on n = 791,635/812,793. Mixing P4 and P5 monopoles causes small but non-negligible inconsistencies (e.g., predicted σ values, residuals).
Required fix: Use the P5-measured monopole from this paper’s own matched sample consistently for all σpred and residual calculations throughout the manuscript and figures (including Fig. 3 overlays and Sec. VII “σvs monopole” language). Keep the P4 value only for context, and quantify any differences.

P5-M2 (Sec. IV, footnote a on p. 2; title; throughout)
Problem: The classifier implemented is the tidal-tensor/Hessian of potential (“T-Web” in much of the literature), not the velocity-shear “V-Web” of Hoffman et al. 2012. The footnote acknowledges this but continues to label the analysis as “V-Web.” This is terminologically misleading.
Required fix: Rename the classifier consistently to “Tidal-tensor (T-Web) classifier” throughout the paper (title, abstract, body, figures, tables), and reserve “V-Web” for velocity-shear-based classifiers. Keep the historical note in a footnote but correct all labels.

P5-M3 (Sec. VIII B, Table VII p. 11; Sec. VIII C–D, Table VIII p. 12)
Problem: The DESIVAST void vs non-void difference ΔfCW = 0.0007 is presented without an explicit two-sample uncertainty/CI for the contrast. While it is clearly tiny, PRD requires the actual test statistic.
Required fix: Report the standard error and a two-proportion z-test (or exact unconditional test) for ΔfCW (e.g., z ≈ 0.32 for VoidFinder with Nvoid = 56,981, Nnon = 621,964; include 95% CI on Δf). Do the same for V2-REVOLVER and V2-VIDE contrasts, and for the catalog-native GALZONE/ZONEVOID memberships.

P5-M4 (Sec. VII, Table VI p. 8–9; Sec. VII A p. 9–10)
Problem: The Phase 2 sweep reports per-cell max inter-class ranges (≤ 0.22 pp) without providing the per-class counts in each cell. It also compares ranges to per-class “counting-statistics floors,” but those floors are shown only for the canonical cell.
Required fix: Add a supplemental table (or appendix) listing, for each of the nine (Rs, λth) cells: the per-class counts on the chirality-relevant matched sample and the corresponding 1σ binomial uncertainties. State explicitly that the per-cell 0.22 pp range is less than the minimum per-class 1σ across the four classes in that cell, if this is the intended bound.

P5-M5 (Sec. VI D b–d, p. 7–8)
Problem: The text reports a “joint two-sample z-test on the bright-vs-dark fCW difference … |z| ≈ 3.4σ on the filament class” without giving the underlying counts (nCW, nCCW) per program and per class. The cluster-class “|z| ≈ 0.5σ” also lacks explicit inputs (e.g., the stated nclusterdark = 4,234 is not shown in a table).
Required fix: Provide the explicit bright/dark CW/CCW counts per class (at least for filament and cluster) and the exact z-value and p-value (two-sided). State whether a look-elsewhere correction was applied over the four classes. Clarify that this two-sample z is a different statistic from the one-sample σ-from-half used elsewhere.

P5-M6 (Sec. V, Eq. (2) p. 4–5; Table V p. 8)
Problem: The Bonferroni thresholds and permutation-based pLEE are both used. While this is acceptable, the paper should state explicitly which is the primary for each scan and avoid combining Bonferroni σ-thresholds with permutation p-values in the same sentence without mapping.
Required fix: For each multi-bin scan (density quintiles, redshift bins, HEALPix), choose a single primary correction approach (you say empirical max-stat null is primary; keep that) and demote the Bonferroni threshold to a cross-check, reported in parallel but not interpreted in σ units adjacent to permutation p-values.

P5-M7 (Sec. VIII A, p. 10–11)
Problem: The “0/6 V-Web ‘void’ spirals inside any DESIVAST holes” diagnostic is fine as a qualitative illustration, but it is presented as evidence of “0% concordance” without quoting the uncertainty of such a tiny sample.
Required fix: Rephrase to “0 of 6 (95% Clopper–Pearson 95% CI: 0–46%)” or remove any implication of a quantitative purity statement from this anecdotal sample.

MINOR

P5-m1 (Sec. VI A, p. 5–6)
Problem: Arithmetic discrepancy in predicted σ for the filament class: text states “σpred(filament) ≈ −3.16,” but with Δf = −0.0026 and N = 408,187, σpred = 2·Δf·√N ≈ −3.32. Cluster σpred ≈ −3.28 matches.
Required fix: Correct σpred(filament) to −3.32 (or to the value corresponding to the exact Δf used, if you switch to P5).

P5-m2 (Abstract p. 1; Table VI p. 8)
Problem: Units for ranges mix percentage points and raw fractions: e.g., “never exceeds 0.22 percentage points (max 0.0022 at Rs = 25, λth = 0.3).”
Required fix: State ranges consistently in percentage points (pp) throughout, and avoid mixing with fractional notation in parentheses.

P5-m3 (Sec. VI B, p. 6)
Problem: “logistic regression of the CW indicator on {z, |sin δ|, cos α, confidence} gives a z-coefficient of 0.0059 with no significant intercept (0.000652)…” The regression details (exact sample size after filters, covariate definitions, link function, standard errors) are not shown.
Required fix: Provide the coefficient standard errors and p-values, sample size, and exact model specification in an appendix table.

P5-m4 (Sec. V, p. 4–5)
Problem: “Exact binomial 95% credible interval” is repeatedly referenced as Jeffreys. Good choice, but the prior should be stated once (Beta(0.5,0.5)), and whether the interval is equal-tailed.
Required fix: Add one sentence specifying the Jeffreys prior and equal-tailed interval computation.

P5-m5 (Sec. VIII E, Table IX p. 12)
Problem: The interpretation “−4.75σ concentrated entirely in ‘0 maximal voids per pixel’ bin” is fine but mixes one-sample σ-from-half with an overlay of a monopole-predicted σpred residual in the same paragraph.
Required fix: Add one clarifying sentence separating the one-sample σ and the monopole-residual discussion, or present the latter as a separate row with σobs, σpred, and residual.

P5-m6 (Sec. IX B, p. 15)
Problem: “p < 10−1000” is not informative and exceeds numerical precision; similar stylistic issues occur elsewhere.
Required fix: Report −log10 p or simply “p ≪ 10−10” to avoid pseudo-precision.

P5-m7 (Sec. III D, Table I p. 3)
Problem: Extremely small median angular separation 0.0066″ is plausible if positions are shared, but surprising. No issue per se, but a one-line note that Legacy and DESI coordinates are largely identical for many targets would help readers.
Required fix: Add a short explanatory note.

P5-m8 (Sec. V B, p. 5)
Problem: “Primary vs. secondary” analysis path language is transparent but unusual in PRD; it’s acceptable, but please move part of it to Methods and define precisely which result is the single headline test (DESIVAST void vs non-void) with pre-declared statistic (two-proportion difference).
Required fix: Tighten language to a concise paragraph in Methods; ensure the headline test statistic is explicit.

P5-m9 (Figures 1–7)
Problem: Axis labels and units are generally fine, but add units to smoothing scale Rs on relevant figure captions if not already present (Mpc/h).
Required fix: Add “Mpc/h” where missing in captions.

NITPICKS

P5-n1 (Multiple)
Typographical: remove extra spaces around multiplication signs in “2563”, standardize to “256^3”.
P5-n2 (Sec. VIII A, p. 10)
Minor phrasing: “flat-ΛCDM” → “flat ΛCDM”; “units h−1 Mpc consistent with the DESIVAST hole catalog” could be rephrased for clarity.
P5-n3 (Sec. XII C, p. 18)
“leaves no room for a residual environment-dependent chirality of the Shamir 2022 amplitude.” Soften to “rules out such an effect at the percent level probed here,” unless you add an explicit numerical upper bound.

Page length
The manuscript is dense for the core claim (environment-independence within DESI DR1), with long diagnostic sections. I recommend condensing to ~14–16 pages by moving secondary cross-check details (Tempel/Astra overlays, some HEALPix scans, small-sample anecdotes like the 0/6 V-Web voids) to an appendix, once the essential methodological fixes above are addressed.

Bibliography checks
- [5] Hahn et al. 2007 MNRAS 375, 489: OK.
- [6] Hoffman et al. 2012 MNRAS 425, 2049: OK.
- [7] Cautun et al. 2014 MNRAS 441, 2923: OK.
- [13] Rincón et al. 2025 ApJ 982, 38; DOI given: OK.
- [11] and [12] are 2026 arXiv preprints: acceptable as concurrent literature overlays, not validation.
- [9] Shamir 2022 MNRAS 516, 2281: OK.

Internal arithmetic spot checks
- Table II σ-from-half values recompute correctly for all four classes.
- “Range 1.98 pp” matches 0.5034 − 0.4836 = 0.0198.
- Density quintile residual |σobs − σpred| = 1.87 for quintile 3: matches Table III.
- HEALPix counts at NSIDE = 32 (npix = 3,303) imply ~27% sky coverage, plausible; please clarify that “npix” is “valid pixels in footprint” to avoid confusion with 12 NSIDE^2 total.

Dimensional analysis
- Eq. (1) dimensionless: OK.
- Grid, box, and smoothing units consistent (Mpc/h): OK.

## Summary recommendation
MAJOR REVISIONS

Justification
The central claim (no environment dependence beyond a small, catalog-wide monopole) is likely correct and is well supported by the DESIVAST primary analysis and multiple cross-checks. However, several essential methodological and arithmetic issues must be fixed before PRD publication: an outright inconsistency in the Phase 2 sweep sample size used to quote a σ value; the non-lossless k-NN implementation in the DESIVAST point-in-sphere test; inconsistent reliance on an unpublished P4 monopole rather than the P5-measured one; and mixing of incompatible “sigma” conventions without explicit caveats at each juxtaposition. These are correctable with focused revisions, additional tables of per-cell counts, and a permanent code/data deposit. Once addressed, along with renaming the classifier to T-Web and adding the missing two-sample tests/intervals for key contrasts, the paper should be suitable for PRD Methods.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER SECOND-PASS AUDIT (fresh eyes)

Note: I only list issues not already raised in my initial review. Numbering continues the prior scheme.

ESSENTIAL

P5-E5 (Sec. VI D b, p. 7; Sec. XI, p. 17)
Problem: Internal contradiction on target-class splits. In Sec. VI D b the “bright vs dark” split is explicitly equated to BGS vs LRG/ELG/QSO and shows a large difference (fCW bright 0.4970 vs dark 0.5051; Δ ≈ 0.0081). Sec. XI later states, as a systematics null, “BGS vs. LRG-ELG-QSO … BGS-only CW fraction within ±0.001 of LRG-ELG-QSO.”
Required fix: Reconcile these statements using the same definition and sample for both splits. If “bright vs dark” is not the same as “BGS vs LRG/ELG/QSO,” say so and show both analyses, with explicit counts for each. If they are the same split (as implied in VI D b), then one of the two statements is wrong and must be corrected. Provide the exact CW/CCW counts for BGS-only and LRG/ELG/QSO-only on the chirality-relevant sample to resolve this.

P5-E6 (HEALPix pixel accounting inconsistent across sections/figures)
Problem: The manuscript uses several different “valid pixel” counts at NSIDE = 32 without clearly stating the selection applied each time:
- Table V: npix = 3,303 (valid pixels in footprint).
- Sec. VIII F: “distribution … across 1,821 valid pixels.”
- Fig. 6 (bottom caption): “1,496 valid pixels,” with an additional subset “n_both_pix = 727.”
These are three different totals at the same NSIDE, and the applied per-pixel spiral-count and/or void-count thresholds are not consistently stated alongside each number.
Required fix: Standardize and document the per-pixel selection for each analysis (minimum spirals per pixel, requirement of ≥1 maximal void, sky mask, etc.). Add a small table summarizing, for NSIDE = 32, the exact cuts and resulting pixel counts used in Table V, Sec. VIII F, and Fig. 6. Use consistent “valid pixels in footprint” phrasing everywhere to avoid confusion.

MAJOR

P5-M8 (Sec. VII A, p. 9–10; Table VI)
Problem: The inference “the max per-cell fCW range (≤ 0.22 pp) is below the wall- and void-class counting-statistics floors, therefore no (Rs, λth) cell shows an inter-class signal” is methodologically weak because it ignores the much smaller 1σ for the filament/cluster classes (~0.08 pp). A 0.22 pp inter-class range can exceed the 1σ for the largest classes even if it is below the 1σ of the smallest classes; comparing “range” to the largest of the four class uncertainties is not a valid uniformity test.
Required fix: Replace (or supplement) the “range vs floor” argument with a proper heteroskedastic test of equality of proportions across the four classes within each cell (e.g., chi-squared test for K proportions or a GLM/logistic regression with class dummies). Report per-cell test statistics and p-values (corrected for the 9-cell sweep). Keep Table VI but do not rely on the “range < largest σ” heuristic as the primary significance argument.

P5-M9 (Sec. IX A, p. 15–16)
Problem: The “0.2 pp concordance spec” used to judge Tempel vs V-(T-)Web agreement is ad hoc and not justified. It is introduced as a target without derivation or uncertainty propagation.
Required fix: Justify the 0.2 pp spec by propagating binomial (or Jeffreys) uncertainties for both classifiers into a formal tolerance for |fTempel − fV−(T)Web| (e.g., compute a 95% CI for the difference). Use that uncertainty-based criterion instead of an arbitrary 0.2 pp band.

MINOR

P5-m10 (Eq. 1 on p. 4; Fig. 3 caption on p. 7)
Problem: Sign and notation inconsistencies for σpred. Eq. (1) writes “σpred = ΔfCW/0.5/√N = 2·ΔfCW·√N” (correct, but needs parentheses for clarity). Fig. 3 caption states “σpred = −2ΔfCW√N,” which would flip the sign if ΔfCW < 0. In the body/table, σpred values are computed as 2ΔfCW√N (negative here).
Required fix: Standardize to σpred = 2ΔfCW√N everywhere, add parentheses in Eq. (1) as σpred = (ΔfCW/0.5)/√N = 2ΔfCW√N, and fix the Fig. 3 caption.

P5-m11 (Sec. VI D d, p. 8)
Problem: The contingency test (V-Web class × bright/dark) reports χ2 = 4932 on 3 d.o.f. with an effect-size-free interpretation (“not independent”) despite the absolute bright-fraction differences being only ~1.5 pp. Given the huge N, significance is guaranteed, but practical significance is unclear.
Required fix: Report an effect size (e.g., Cramér’s V) with an interpretation, and include the observed bright-fraction per class with 95% CIs to contextualize the strength of association.

P5-m12 (Sec. VII A, p. 9–10)
Problem: Conceptual confusion about the monopole and inter-class fCW range. The text suggests “re-distributing the catalog monopole across classes” could affect the per-cell fCW range. The global monopole is a common offset to all classes; it cancels in inter-class differences in f (though not in σ-from-half). The f-range is therefore insensitive to the monopole by construction.
Required fix: Remove or correct the “re-distribution” phrasing. Clarify that inter-class f differences are expected to be near zero under a pure monopole and that any non-zero range reflects sampling noise and/or residual systematics, not “which class carries the monopole.”

P5-m13 (Sec. VII, p. 8)
Problem: Typo in the sweep definition: “Rs ∈ {10, 25, 50} Mpc/h × Ngrid = 256 × λth ∈ {0.0, 0.1, 0.3}.” Ngrid should be 256^3 and independent of λth.
Required fix: Correct to “Rs ∈ {10, 25, 50} Mpc/h × λth ∈ {0.0, 0.1, 0.3} on a fixed 256^3 grid.”

P5-m14 (Sec. VIII F, p. 13)
Problem: The per-pixel σvs monopole summary uses NSIDE = 32 and quotes moments over “1,821 valid pixels” without the per-pixel spiral-count threshold (contrast with Fig. 6 requiring ≥ 200 spirals, giving 1,496 pixels).
Required fix: State the minimum per-pixel spiral count used for the 1,821-pixel summary, and harmonize with Fig. 6 thresholds or explain the difference.

P5-m15 (Sec. V, p. 4–5)
Problem: Monte Carlo resolution/uncertainty for permutation pLEE values is not reported. With NMC = 1,000, the standard error on p ≈ 0.1 is ~0.0095.
Required fix: Report pLEE with Monte Carlo uncertainty or increase NMC for the primary scans (e.g., to 10,000) and state the effective resolution.

P5-m16 (Sec. III A, XI references to “per-leg” splits)
Problem: The text states that imaging-leg provenance is retained and that per-leg systematics are propagated, but no per-leg fCW values or tests are shown for this paper’s matched sample.
Required fix: Either include a small table of fCW per imaging leg for the matched sample (with σ-from-half and/or residual vs monopole) or drop the claim that per-leg splits are “propagated” here (and point to Paper IV for the detailed leg-level analysis).

P5-m17 (Sec. V, p. 4–5)
Problem: Equation (2) (Bonferroni z-threshold) is used as a cross-check, but the text sometimes interprets Bonferroni thresholds and permutation p-values in proximity without clearly separating the two (even after the general statement that permutation is primary).
Required fix: In each section where both appear (e.g., Fig. 3 caption/body, HEALPix scan), add a one-line reminder that Bonferroni is a conservative cross-check and that the primary inference is from the empirical max-stat pLEE.

P5-m18 (Sec. II and VIII F)
Problem: Paper IV’s “~9.5σ” monopole significance and the 2Δf√N mapping used elsewhere in this paper imply different uncertainty models for the same ∆f (binomial vs. catalog-level error). This can confuse readers about which uncertainty model is being used when propagating to σpred in this paper.
Required fix: Add a footnote clarifying that in this paper σpred uses a pure binomial model on the P5 matched sample, while the ~9.5σ cited for Paper IV used Paper IV’s own catalog-level uncertainty; emphasize that only the P5 binomial model is used for predictions in this manuscript.

P5-m19 (Sec. VIII B, p. 11)
Problem: The KDTree k-NN shortcut justification references “24 Mpc/h maximum hole radius,” but later V2-REVOLVER/VIDE effective radii are up to ~56 Mpc/h. Even aside from P5-E2’s losslessness objection, the stated 24 Mpc/h bound is not applicable to those catalogs.
Required fix: Clarify that the 24 Mpc/h bound applies only to VoidFinder interior holes, and state the corresponding Rmax used for V2-REVOLVER/VIDE tests. Then address P5-E2 by using radius queries or proving k is safely above the maximum number of centers within the applicable Rmax for each catalog.

NITPICKS

P5-n4 (Notation)
- Use “256^3” consistently (several places show “2563”).
- “flat-ΛCDM” → “flat ΛCDM.”
- In Eq. (1) add parentheses to avoid operator-precedence ambiguity: σpred = (ΔfCW/0.5)/√N.

P5-n5 (Abstract/claims language)
“the largest matched-sample environmental-dependence test … to date” is plausible but unreferenced. Consider softening or adding a sentence comparing N and z-range to prior published chirality–environment studies, if any.

P5-n6 (Fig. captions)
Add/standardize units “Mpc/h” for Rs and radii everywhere; ensure all captions that mention Rs include units.

P5-n7 (Systematics list, Sec. XI)
The “confidence-threshold sweep” and “match-radius sweep” are summarized by qualitative bounds (±0.001, < 0.001). Consider moving a compact numeric table with the exact values to an appendix for completeness.

Reason for additional findings
The second pass focused on cross-section consistency (especially HEALPix pixel accounting), conceptual clarity in the Phase 2 inference (range vs heteroskedastic uncertainties), and contradictions between program/tracer splits across sections. Several sign/notation inconsistencies (σpred), missing effect-size/context for very large-χ^2 results, and documentation gaps (pixel thresholds; per-leg splits) surfaced that were not flagged in the initial review. These are all addressable with targeted edits, added tables, and clearer definitions.