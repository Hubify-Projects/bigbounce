# P5 auto-2026-06-08_1632pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (14054 chars)
**Wall time**: 462.0s

---

# Referee Report — Paper P5

**Manuscript:** "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals"

**Submitted to:** Physical Review D

---

## Overall assessment

This is a null result paper that depends entirely on an unpublished companion paper (Paper IV) for its central calibration (∆f_CW = −0.0026 monopole). The headline σ values in the abstract are not "evidence for environment-independence" but rather the catalog-monopole offset propagated through different sample-size bins. The paper acknowledges this — but then spends 20 pages re-deriving the same conclusion many ways. The actual *new* result is one number: ∆f_CW = 0.0007 between DESIVAST voids and non-voids. Whether this merits PRD publication is questionable on novelty grounds alone, especially given Paper IV is "in preparation."

I find numerous arithmetic inconsistencies, internal contradictions, presentation problems, and an inappropriate co-mingling of σ-values from incommensurate null hypotheses. I recommend **REJECT** in current form.

---

## ESSENTIAL findings

### P5-E1 — Paper IV is unpublished and load-bearing
**Pages 1, 2, 20 (refs [3], [4])**
The entire monopole-subtraction calibration ∆f_CW = −0.0026 ± 0.000279, the global parity null, the per-leg systematic budget, and the chirality labels themselves come from Paper IV, which Ref. [3] states is "in preparation; manuscript in preparation." A PRD submission cannot rely on an unpublished, non-peer-reviewed companion as the calibration anchor for every σ-value in its abstract. Either (a) Paper IV must be submitted/accepted first, or (b) all monopole-subtraction calibrations must be re-derived self-consistently within this paper.

### P5-E2 — Abstract σ-values mix incommensurable nulls without qualification
**Page 1, abstract**
The abstract reports per-class σ values "−2.61σ (filament), −4.66σ (cluster), +0.55σ (wall), −0.68σ (void)" as σ-from-half *and* then claims these "track the catalog-wide ∆f_CW = −0.0026 classifier-monopole offset … not an environmental signal." This conflates two different null hypotheses (deviation from 0.5 vs. deviation from Paper IV monopole). The headline numbers as written are *highly significant* deviations from the literal stated null (f_CW = 0.5). The abstract must explicitly distinguish σ_from-half from σ_vs-monopole at every juxtaposition. Per the reviewer instructions: this is flagged ESSENTIAL.

### P5-E3 — Arithmetic inconsistency in CW + CCW count
**Page 3, Table I**
Table I reports CW = 393,592 and CCW = 398,043. Sum = 791,635 ✓ (matches "Chirality-relevant").
But the abstract page 1 states n = 791,635 with "f_CW = 0.4980 (filament)" + similar — let me check the cluster value:
- Cluster: n_CW = 197,284, n = 397,505 → f_CW = 197,284/397,505 = **0.49631** (paper says 0.4963 ✓)
- σ_from_half = (197,284 − 198,752.5)/(0.5·√397,505) = −1,468.5/315.24 = **−4.658** (paper says −4.66 ✓)
- Filament: 203,261/408,187 = **0.49796** (paper says 0.4980 ✓)
- σ = (203,261 − 204,093.5)/(0.5·√408,187) = −832.5/319.45 = **−2.606** (paper says −2.61 ✓)
- Void: 207/428 = **0.48364** (paper says 0.4836 ✓)
- σ = (207 − 214)/(0.5·√428) = −7/10.344 = **−0.677** (paper says −0.68 ✓)
- Wall: 3,359/6,673 = **0.50337** (paper says 0.5034 ✓)
- σ = (3,359 − 3,336.5)/(0.5·√6,673) = 22.5/40.84 = **+0.551** ✓

Sum of class n: 428 + 6,673 + 408,187 + 397,505 = **812,793**, not 791,635. The paper acknowledges this on page 12 ("812,793 env-labeled spirals … the 21,158-row excess …") but the *headline table* (Table II) sums to a different total than the abstract's stated chirality-relevant n. This is buried; it must be stated at first use of Table II on page 5 that ∑n_class ≠ 791,635.

### P5-E4 — σ_pred prediction inconsistent with σ_obs
**Pages 6, 13**
Paper computes σ_pred(filament) ≈ −3.16, σ_pred(cluster) ≈ −3.28 from ∆f_CW = −0.0026 at the listed n. Let me recheck:
- σ_pred(filament) = 2·0.0026·√408,187 = 0.0052 × 638.9 = **3.32**, not 3.16
- σ_pred(cluster) = 2·0.0026·√397,505 = 0.0052 × 630.5 = **3.28** ✓
Page 6 quotes 3.16 for filament; Table X area on page 9 quotes 3.32 for filament. The two are inconsistent within the paper. The 3.16 value appears to be wrong arithmetic.

Also: the abstract claims observed cluster σ = −4.66 is consistent with monopole prediction of −3.28, but the residual |−4.66 − (−3.28)| = 1.38σ — fine. Filament residual: |−2.61 − (−3.32)| = 0.71σ — also fine. These need to be stated as residuals at every comparison.

### P5-E5 — Table II "range" line is misleading
**Page 5, Table II**
The "range" entry of 0.0198 under f_CW is the range across classes — but it is presented in a row that gives the impression of an aggregate statistic. The void value (0.4836) is at n=428 and dominated by counting noise. The range is driven by the void outlier, not by environment dependence. Stated this way, "range 1.98 percentage points" appears throughout the paper (abstract page 1, conclusions page 19) without immediate context that this is dominated by a single small-n bin. Flag and fix.

### P5-E6 — Contingency-test χ² value is internally inconsistent
**Page 8**
Paper states χ² = 4932 with 3 d.o.f. and "p < 10⁻¹⁰⁰⁰". For χ² = 4932 at 3 d.o.f., the right-tail p-value is approximately exp(−2466), which is ~10⁻¹⁰⁷¹ — so p < 10⁻¹⁰⁰⁰ is *true* but is an absurd precision claim for a contingency test on real data with selection-function structure. More importantly: the paper then says max class-to-overall bright-fraction deviation is "1.5 pp" — a 1.5 pp deviation on n ~ 800k giving χ² ~ 5000 is plausible only if the deviation is strongly localized; the χ² and the deviation must be reconciled. The "p < 10⁻¹⁰⁰⁰" claim is physically meaningless because no real survey selection function is the assumed null. State as "highly significant, dominated by selection-function correlation" without the absurd exponent.

### P5-E7 — Pre-registration declaration is post-hoc
**Page 5, §V B**
Paper states explicitly: "a single a priori pre-registered analysis plan was not filed; the choice of which classifier to report as 'primary' is therefore made post-hoc, and we declare it explicitly here to bound the garden-of-forking-paths concern." This is honest, but combined with the multiplicity of stratifications (V-Web ×9 sweep cells × 4 classes, DESIVAST ×3 algorithms, Tempel ×4 classes, ASTRA ×4 classes, HEALPix ×3 NSIDE, density ×5 quintiles, redshift ×4 quartiles, target program ×4, sky-position scans …) the headline-null finding lacks the multiple-testing-corrected interpretation framework needed for a clean PRD result. The Bonferroni-5 budget on the DESIVAST primary path is too narrow given the actual search.

### P5-E8 — DESIVAST primary path lacks proper null test
**Page 11, Table VII**
The primary headline ∆f_CW = 0.0007 (DESIVAST void vs non-void) is reported with σ_void = −1.71 and σ_non-void = −4.59, but no two-sample test statistic for the difference between fractions is reported. A proper z-test for proportion difference:
z = (0.4964 − 0.4971)/√[p(1−p)(1/56,981 + 1/621,964)]
where p = 0.4970 → SE = √[0.25 × (1.755e-5 + 1.608e-6)] ≈ √[4.79e-6] ≈ 0.00219
z = −0.0007/0.00219 = **−0.32**.
The paper does not report this. Without it, "statistically indistinguishable" is unsupported by an explicit test. Provide the z-statistic and 95% CI on ∆f_CW.

### P5-E9 — Three-algorithm DESIVAST n_void mismatch
**Pages 11, 12, Table VIII**
Page 11 states: "V2-REVOLVER (n_void^catalog = 1,992 effective voids…) and V2-VIDE (n_void^catalog = 1,478)". But the original DESIVAST paper (Rincón et al. 2025) numbers, and the abstract of *this* paper page 1, state "420 with V2-REVOLVER, and 295 with V2-VIDE" — wait, the abstract says "VoidFinder, V2-REVOLVER and V2-VIDE watershed" but doesn't give catalog counts; page 10 says "1,461 interior voids with VoidFinder, 420 with V2-REVOLVER, and 295 with V2-VIDE", and page 11 says "1,992 effective voids" and "1,478" for the same algorithms. These numbers are mutually inconsistent within the paper. Reconcile.

Additionally, Table VIII reports V2-REVOLVER n_void = 102,911 (in matched-spiral subsample) while the abstract claims n = 86,276 for the catalog-native GALZONE membership. These are different definitions (sphere-approximation vs catalog-native) — but the abstract just quotes "n = 86,276" without telling the reader that the sphere-based number is different. Clarify in abstract.

### P5-E10 — Pearson correlation null test has confusing reported sample size
**Page 13**
Paper reports r = +0.006 (p = 0.88) at NSIDE = 32 across "n = 727 valid pixels". This is mentioned in the abstract as a load-bearing null. Fine. But the abstract says "the per-pixel Pearson correlation between maximal-void density and chirality σ at NSIDE = 32 across n = 727 valid pixels is r = +0.006 (p = 0.88)" — and on page 13, the result is presented in a robustness sweep where "7 of 9 cells admit a well-sampled Pearson estimate" but those 7 individual correlations are not reported. Provide the full table of 7 correlations.

### P5-E11 — V-Web grid cell size inconsistency
**Pages 3, 16**
Page 3 (§IV A): "Cloud-in-Cell deposit onto a 256³ comoving grid (full DR1 bounding box 6,634 Mpc/h at 256³ → cell 25.9 Mpc/h)."
Page 16 (§X): "the 25.9 Mpc/h cell size in the V-Web 256³ grid is comparable to the EDR rosette transverse extent"
This is consistent — but the smoothing length R_s = 25 Mpc/h is approximately equal to the cell size, which means the smoothing kernel is barely Nyquist-sampled. This must be flagged in the methods section as an explicit caveat: at R_s ~ cell size, the smoothed field has anisotropic discretization artifacts from the CIC deposition. The Phase 2 sweep at R_s = 10 Mpc/h has *sub-cell* smoothing — meaningless. Address.

---

## MAJOR findings

### P5-M1 — Abstract is excessively long and dense
**Page 1–2**
The abstract is ~1100 words and essentially contains the entire paper. PRD abstracts are typically ≤ 250 words. Rewrite to ≤ 300 words focused on (1) what was measured, (2) the headline ∆f_CW = 0.0007 result, (3) the bound implied, (4) caveats. Move the Robustness paragraph and the four DESIVAST re-projections into the body.

### P5-M2 — Title is excessive
**Page 1**
"A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals" — the title parses the methodology rather than stating the result. Suggest: "Environmental Independence of Spiral Chirality in DESI DR1: A DESIVAST and V-Web Null Test."

### P5-M3 — Page count vs. content
**Whole paper**
The paper is 20 pages for what amounts to a one-number null result (∆f_CW = 0.0007 ± [unreported uncertainty]). Sections VI D, VI E, IX A, IX B, X all establish the *same* null with different classifiers. Recommended length: 10–12 pages. Remove or move to appendix: Section VII per-cell significance framework (3 pages establishing the obvious), the full Tempel cross-validation (1.5 pages — concordance 0.026 pp is the only sentence needed), the ASTRA per-object cross-validation (the V-Web vs ASTRA per-galaxy disagreement undermines its value), the within-class density stratification (already null).

### P5-M4 — Footnote (a) on page 2 acknowledges classifier-name misnomer
**Page 2, footnote a**
"for backward compatibility with prior analyses we retain the 'V-Web' label which is sometimes used loosely for the family of tidal-field classifiers."
The classifier used is properly called T-Web (tidal). The paper itself notes this. "Backward compatibility with prior analyses" is not a valid reason — this is the author's own work. Rename to T-Web throughout, and remove this footnote.

### P5-M5 — Phase 2 sweep at R_s = 10 Mpc/h is ill-defined
**Page 8, Table VI**
At R_s = 10 Mpc/h with cell size 25.9 Mpc/h, the smoothing kernel is below Nyquist and the tidal-tensor calculation is not well-defined. Yet Table VI reports a result at this cell. Either justify why this is meaningful or remove the three R_s = 10 cells.

### P5-M6 — Figure 1 axis labels not described
**Page 4, Figure 1**
Pie chart shows {Void 24.4%, Wall 41.3%, Filament 33.3%, Cluster 1.0%}. These sum to 100.0% ✓. Caption claims void = 0.244 but earlier text and pie say 24.4%. Consistent. But the figure provides no information beyond the four numbers — it is filler. Convert to a single inline sentence.

### P5-M7 — Figure 3 left-panel axis label is broken
**Page 7, Figure 3**
The x-axis label on the left panel reads "Den ∈ [42, 1...]" with what appears to be overlapping text including "[116399][176...][317833][2096...]". This is an unreadable figure. The bin-edge labels are corrupted. Fix the rendering.

### P5-M8 — Figure 6 caption mentions "Top: count … Bottom: per-pixel chirality" — but figure axes show 0.0–1.0
**Page 14, Figure 6**
The figure shows what appears to be a Mollweide projection but the visible axis labels are 0.0, 0.2, 0.4, 0.6, 0.8, 1.0 which are not sky coordinates. Either the projection is not properly labeled or the figure is mis-rendered. Color bar for the bottom panel is labeled "σ" with range -6 to 6, but the caption says "σ range −3.45 to +3.48". Mismatch.

### P5-M9 — Asymmetric reporting of "concentrated entirely in the 0 maximal voids per pixel bin"
**Page 1 (abstract), Page 12 (Table IX)**
Abstract says the −5σ "concentrated entirely in the '0 maximal voids per pixel' bin". Table IX shows:
- 0 voids/pix: σ = −4.75 (n = 378,511)
- 6+ voids/pix: σ = −2.04 (n = 258,060)

The 6+ bin is *not* zero — it is −2σ. "Concentrated entirely" is an overstatement. Recompute: at n = 378,511 and ∆f = −0.0026, σ_pred = −3.20 (paper gets −3.20 ✓), residual = −1.55. At n = 258,060, σ_pred = −2.64, residual = +0.60. So the residual is concentrated in the 0-voids/pix bin — but the abstract claim is too strong. Recast.

### P5-M10 — Tracer-program decomposition opposite-sign finding is underreported
**Page 1 (abstract), Pages 7–8**
"the joint two-sample z-test on the bright-vs-dark f_CW difference is |z| ≈ 3.4σ on the filament class" — a 3.4σ opposite-sign discrepancy is a *real residual* by the paper's own admission. It exceeds the Bonferroni-5 threshold |σ| = 2.81 the paper sets for primary tests. The paper handles this by declaring the DESIVAST primary path "constructed to be insensitive to this residual" and flagging the result for follow-up. This is defensible but inadequately reasoned. The 3.4σ filament sign-flip, if real, is a result and the paper should engage with it more seriously than as a footnote.

### P5-M11 — Recompute the 3.4σ filament joint z-test
**Page 1, abstract**
Filament bright (n = 416,701, σ = −2.80) and filament dark (n = 21,203, σ = +2.85).
f_bright = 0.5 + (−2.80)·0.5/√416,701 = 0.5 − 0.00217 = 0.49783
f_dark = 0.5 + 2.85·0.5/√21,203 = 0.5 + 0.00979 = 0.50979
∆f = 0.01196
SE = √[0.25·(1/416,701 + 1/21,203)] = √[0.25·(2.40e-6 + 4.72e-5)] = √1.24e-5 = 0.00352
z = 0.01196/0.00352 = **3.40** ✓
Arithmetic OK. But: the filament bright n = 416,701 plus filament dark n = 21,203 = 437,904, which exceeds the filament total n = 408,187 in Table II by 29,717. The bright/dark split is on a *different* subsample than the headline filament class. State explicitly which sample is which.

### P5-M12 — Inconsistent treatment of CL=95% Jeffreys vs Bonferroni
**Throughout**
The paper mixes 95% Jeffreys binomial CIs, Bonferroni-4 at α = 0.05 (|σ| = 2.50), Bonferroni-4 at α = 0.01 (|σ| = 3.02), Bonferroni-5 at α = 0.05 (2.81), and Bonferroni-5 at α = 0.01 (3.09) seemingly arbitrarily. Each table needs to state which threshold is being used and why.

### P5-M13 — Eq. (1) sign convention
**Page 4, Eq. (1)**
σ_pred = ∆f_CW / (0.5/√N) = 2·∆f_CW·√N
At ∆f_CW = −0.0026, this gives negative σ_pred for *every* sample size — so the prediction is that *every* class should show a negative σ_from_half. The fact that the void and wall classes do not (σ_void = −0.68 but |σ_pred| at n=428 = 0.11; σ_wall = +0.55 but σ_pred at n=6,673 = −0.42) is glossed over. The wall class actually has the *opposite sign* from the monopole prediction. State this.

### P5-M14 — Reproducibility — "available in the companion data repository"
**Throughout**
The paper says "available in the companion data repository" at least 8 times but provides no URL to the repository. The "bamfai/galaxy-chirality-catalog" HuggingFace link is given but the "companion data repository" with all the configs, sweep CSVs, and drivers is unnamed. Provide URL.

### P5-M15 — Reference [11] and [12] arXiv IDs are not valid 2024/2025/2026 format
**Page 20, Refs [11], [12]**
arXiv:2604.02463 and arXiv:2604.01456. The arXiv numbering scheme uses YYMM, so 2604.xxxxx would correspond to April 2026 — the paper is "dated June 2026" so that's borderline plausible for a recent submission, but the verification cannot proceed unless these arXiv IDs are real. If these are forecasts of forthcoming work, they should be labeled as such. Given the paper repeatedly refers to "concurrent literature" and "in submission to MNRAS", these citations may be speculative/forthcoming. Flag for verification.

### P5-M16 — Ref [13] arXiv ID
**Page 20, Ref [13]**
arXiv:2411.00148 (DESIVAST). This appears valid (Nov 2024). OK.

### P5-M17 — "Largest matched-sample environmental-dependence test of spiral chirality in DESI DR1"
**Page 11**
"This DESIVAST-anchored re-analysis is the largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date" — DESI DR1 is recent; "largest" is trivially true if it's the *first*. Reword as "first to our knowledge" or remove the superlative.

### P5-M18 — The "void-bin smallness" caveat undermines the abstract
**Page 6**
The abstract reports V-Web void σ = −0.68 at n = 428 — but the paper acknowledges this is "statistical noise" and "the 95% binomial credible interval is f_void_CW ∈ [0.435, 0.530]". The headline V-Web void result therefore tells us nothing. The paper should remove this from the abstract and lead with DESIVAST.

### P5-M19 — RSD treatment is inadequately quantified
**Pages 10, 18**
Section XIII acknowledges the V-Web positions are in redshift space, then notes "the anisotropic eigenvalue deformation above is the dominant channel and is not separable from the sweep-induced shift without a reconstructed-position rerun." This is a major systematic that is not propagated into the headline σ-budget. At the ~0.2 pp Phase 2 sweep range, this is the same order as the systematic itself. Either redo with reconstructed positions or fold a quantitative RSD systematic into the error budget.

### P5-M20 — Appendix A toy EFT mapping is undisciplined
**Page 19, Appendix A**
"We deliberately keep the parameterization schematic." then "the literal ẑ form is a coordinate-aligned schematic, not a covariant operator" then "the toy operator above should therefore be read as a heuristic parametrization in this specific slicing, not as a covariant EFT operator." This is a one-page caveat-fest about an operator the paper itself says is not derivable from the cited literature. Remove the appendix; it adds no value.

---

## MINOR findings

### P5-m1 — Page 1 abstract has "16.4 × 10⁶ ZWARN=0 input rows"
The page 3 §III B says "full DR1 input is 16,361,731 rows … ZWARN==0". 16,361,731 = 16.36M, not 16.4M. Minor rounding inconsistency.

### P5-m2 — Page 6, Section VI A: "The dashed horizontal line is parity (f_CW = 0.5); the dotted red line is the Paper IV global f̄_CW = 0.4974 classifier-monopole offset."
Figure 2 caption matches. OK.

### P5-m3 — Page 1 abstract — "n_DESIVAST_void = 56,981"
Recompute from Table VII: 56,981 ✓.

### P5-m4 — Page 8: "p < 10⁻¹⁰⁰⁰"
See E6 — meaningless precision.

### P5-m5 — Page 12 says "5.07σ on n = 812,793"
σ = 2·∆f·√N with f = 0.4972 → ∆f = −0.0028, σ = 2·0.0028·√812,793 = 0.0056·901.6 = 5.05. Paper says 5.07; OK to 1 dp.

### P5-m6 — Page 13: residual −1.55σ in 0-voids bin
σ_pred = 2·0.0026·√378,511 = 0.0052·615.2 = 3.20 ✓
Observed −4.75, residual −1.55 ✓

### P5-m7 — Page 6: density quintile residual table
σ_pred at N = 158,327: 2·0.0026·√158,327 = 0.0052·397.9 = 2.07 ✓
Quintile 3: σ_obs = −3.94, residual = 1.87 ✓

### P5-m8 — Page 14 Figure 7 caption text: "← filament_like 0.4982"
The Tempel filament_like fraction. The "←" arrow seems to be a leftover annotation marker. Check the figure renders properly.

### P5-m9 — Page 11, last paragraph: "5σ-class P4 monopole signature"
"P4 monopole" — what does "P4" mean? This appears throughout (P4, P5) but is never defined in the body. From context, P4 = Paper IV, P5 = this paper. State explicitly.

### P5-m10 — Page 12: "the prior per-class σ_from_half values of −2.61σ (filament) and −4.66σ (cluster) reported in the headline table were entirely the P4-catalog-monopole signature"
"Entirely" is an overstatement — the cluster residual is −1.11σ in Table X. Reword: "largely consistent with".

### P5-m11 — Figure 5 has cells with text in white that may be unreadable depending on color
Heatmap fine. Cell at (R_s=25, λ=0.3) = 0.22 highlighted as max ✓.

### P5-m12 — Page 9 first sentence under §V B section continued: "Across nine (R_s, λ_th) cells, the maximum per-cell inter-class f_CW range is below the per-class counting-statistics floor"
"Below the per-class counting-statistics floor" is misleading because the floor varies per class (0.08 pp filament/cluster, 2.4 pp void). The 0.22 pp range exceeds the filament/cluster floor but is below the void floor. Reword.

### P5-m13 — Some Bonferroni thresholds are stated inconsistently
Page 5: "Bonferroni-5 at α = 0.01" gives 3.09. Recompute: 2-sided, threshold = Φ⁻¹(1 − 0.005/5) = Φ⁻¹(0.999) = 3.09 ✓.
Page 8: "Bonferroni-4 |σ| = 2.498" — Φ⁻¹(1 − 0.025/4) = Φ⁻¹(0.99375) = 2.498 ✓.
Page 12: "Bonferroni-4 |σ| = 2.50 threshold at α = 0.05" — same as above ✓.

### P5-m14 — Page 18: "Phase 2 sweep at R_s = 10 Mpc/h" smoothing length
See M5.

### P5-m15 — Page 1: "no published bounce or inflation model currently predicts a specific environment-conditional chirality signature at this scale"
This is a weak motivation for the paper. State it more honestly: we are setting a constraint on a class of models that does not currently exist. The "empirical upper bound on any future model" framing is reasonable but should not pretend to constrain known physics.

### P5-m16 — "Survey-shell" terminology not defined
Pages 9, 11, 15, etc. use "survey-shell systematic" without defining it. From context, it appears to mean the thin-spherical-shell geometry of DESI versus a cubic periodic box. Define on first use.

---

## NITs

### P5-n1 — Page 1: "≳ 25 Mpc/h smoothing scale" appears with "h" italicized inconsistently throughout
### P5-n2 — Page 4: equation (1) σ_pred = ∆f_CW/(0.5/√N) = 2·∆f_CW·√N — sign should be flagged; if ∆f_CW < 0 then σ_pred < 0 always; perhaps |σ_pred|
### P5-n3 — Page 7: Tracer-program list "bright (BGS-dominated; n = 775,760), dark (n = 14,782), backup (n = 875), other (n = 218)" sums to 791,635 ✓
### P5-n4 — Page 8: "(approximate richness-to-tidal mapping; filament-class concordance 0.026 pp; supporting rather than load-bearing"
The phrase "supporting rather than load-bearing" appears multiple times. Consider consolidating.
### P5-n5 — Page 11: "These are different definitions" — the paper switches between "void" defined as ≥1 hole containment vs. catalog-native GALZONE membership. The reader can follow but it requires care.
### P5-n6 — Page 19, references: Ref [11] author is "H. I. Ullah, M. Awais, T. Matos, and J. F. Suárez-Pérez" — "Suárez-Pérez" appears OK with accents.
### P5-n7 — Page 17: "The headline statistics, filtered to classes with n ≥ 100 to suppress small-sample artifacts" — but Table XII still includes n=3 (V-Web void+wall) results that are noted are filtered out by the n ≥ 100 cut. Just say the cut.
### P5-n8 — Page 1: "(Dated: June 2026)" — paper is dated in the future relative to most submission timelines. OK if intentional.
### P5-n9 — Multiple uses of "headline" as adjective. Stylistically OK but overused.

---

## Summary recommendation

**REJECT**

The paper's central finding (∆f_CW = 0.0007 between DESIVAST voids and non-voids on n = 56,981 spirals) is a credible null result, but the manuscript fails PRD standards in three critical ways: (1) it depends on an unpublished companion paper [Paper IV] for its monopole calibration, making the headline σ-values uncheckable by an external referee; (2) the abstract mixes σ-from-half and σ-vs-monopole values without explicit qualification at every juxtaposition, and reports a 3.4σ tracer-program sign-flip as essentially a footnote rather than as a result that must be confronted; (3) the manuscript is twice as long as the contribution warrants, with multiple internal arithmetic inconsistencies (E3, E4, E9), an undefined "companion data repository", and an Appendix A toy-EFT discussion that the authors themselves disavow as non-covariant. The DESIVAST three-algorithm cross-check is sound methodologically and is the strongest part of the paper, but it deserves a focused 10-page paper, not a 20-page narrative with five additional secondary classifiers and a post-hoc primary/secondary declaration. Resubmit after (a) Paper IV is accepted somewhere, (b) the abstract is shortened to ≤300 words and σ-conventions are made explicit, (c) arithmetic errors are fixed, (d) the 3.4σ filament sign-flip is properly addressed as either a result or a systematic with quantitative attribution, and (e) the manuscript is condensed to ~10 pages.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report — Paper P5 (Second-Pass Findings)

After re-examining the paper with the focused checklist, I find several additional issues, including one that is **more serious than anything in my first pass**: a fundamental arithmetic inconsistency in the tracer-program decomposition that undermines the bright/dark sign-flip discussion.

---

## NEW ESSENTIAL findings

### P5-E12 — Filament-class dark sample exceeds total dark sample (impossible)
**Pages 1 (abstract), 7, 8**

This is a **critical internal contradiction**. The paper reports:
- **Total dark sample** (LRG, ELG, QSO across all V-Web classes): n = 14,782 (page 7)
- **Filament-class dark** alone: n = 21,203 (page 7, abstract)
- **Cluster-class dark** alone: n = 4,234 (abstract)

The sum filament_dark + cluster_dark = 25,437 already exceeds the total dark sample (14,782) by 72%. This is **arithmetically impossible**. Either:
(a) the per-V-Web-class bright/dark counts come from a different (larger) parent sample than the "total dark" count, in which case the comparison is on apples-to-oranges samples and the headline 3.4σ sign-flip is not what is claimed; or
(b) the numbers contain stale values from an earlier analysis iteration.

Compounding evidence: page 7 states filament_bright = 416,701 and filament_dark = 21,203, summing to 437,904 — but Table II reports filament_total = 408,187. The bright+dark exceeds the V-Web-class total by 29,717 (7.3%).

A further inconsistency: page 8 states "the per-V-Web-class bright/(bright+dark) ratio is {0.981, 0.962, 0.966, 0.989}" so the filament ratio is **0.966**. But page 7's explicit numbers give 416,701/(416,701+21,203) = **0.9516**. The same paper reports two incompatible filament bright/dark ratios.

The abstract's headline 3.4σ filament sign-flip and the entire §VI A bright/dark interpretation rest on numbers that do not internally reconcile. The χ²=4932 contingency analysis (P5-E6) was also computed on some sample — which one? This must be fixed before any meaningful interpretation of the sign-flip.

### P5-E13 — Cluster z-quartile Z3 σ = −3.14 exceeds the stated Bonferroni-4 α=0.01 threshold but is described as "none crossing"
**Page 7, §VI D footnote-text passage**

The paper writes: "Marginalizing over density, the cluster σ_from half per z-quartile is −2.33 (Z1), −1.73 (Z2), **−3.14 (Z3)**, and −2.12 (Z4). All four z-quartile deviations sit in the −1.7 to −3.2σ band, **none individually crossing the Bonferroni-4 |σ| = 3.02 threshold at α = 0.01**."

But |−3.14| = 3.14 > 3.02. Z3 **does** cross the stated threshold. The cluster z-quartile decomposition therefore contains exactly the kind of localized post-correction excursion the paper's headline says does not exist. Either the threshold needs to be recomputed and stated correctly, or Z3 needs to be acknowledged as crossing.

### P5-E14 — Misquoted Bonferroni-9 threshold in Phase 2 framework
**Page 9, §VII A**

The paper states: "zero produces a per-class |σ_vs monopole| residual above the Bonferroni-9 (α = 0.05) threshold |σ|_Bonf_{0.05,9} ≈ 3.02".

Using Eq. (2) of the paper: |σ|_Bonf = Φ⁻¹(1−α/2K). For α=0.05, K=9:
Φ⁻¹(1−0.025/9) = Φ⁻¹(0.99722) = **2.77**, not 3.02.
(The value 3.02 is the K=4, α=0.01 threshold the paper quotes correctly elsewhere on page 15.)

For α=0.01, K=9: Φ⁻¹(1−0.005/9) = Φ⁻¹(0.99944) = **3.25**, also not 3.02.

This is a stale-number / copy-paste error that the paper uses to assert a more permissive bound than it should. With the correct 2.77 threshold at α=0.05, Phase 2 cells in which any single class shows |σ_vs_monopole| > 2.77 (none reported, but residuals are not given per cell) would need re-examination.

---

## NEW MAJOR findings

### P5-M21 — Filament σ_pred misquoted as −3.16 (correct is −3.32)
**Page 6**

The paper writes "σ_pred(filament) ≈ −3.16 and σ_pred(cluster) ≈ −3.28". Using Eq. (1) at ∆f_CW = −0.0026:
- σ_pred(filament) = 2·(−0.0026)·√408,187 = **−3.32**, not −3.16
- σ_pred(cluster) = 2·(−0.0026)·√397,505 = **−3.28** ✓

The 3.32 value appears correctly in §VII A, page 9 ("3.32σ (filament)"), so the paper internally contradicts itself on the same number on two pages. The page-6 value of −3.16 implies ∆f_CW = −0.00247, which is not the Paper IV-quoted value. The 5% error in σ_pred propagates into the headline interpretation that the filament σ_obs = −2.61 "tracks" the monopole: at σ_pred = −3.32 the residual is 0.71σ; at σ_pred = −3.16 it's 0.55σ. Small but worth fixing.

### P5-M22 — Suspicious filament-fraction coincidence between V-Web and ASTRA on EDR overlap
**Page 16–17, §X**

The paper writes:
> "ASTRA argmax distributes the 25,186 spirals as 11.9% void / 31.7% sheet / 35.2% filament / 21.3% knot, while V-Web puts essentially the entire sample into filament **(31.7%)** and cluster (68.3%)"

The V-Web filament fraction and the ASTRA sheet fraction are both reported as exactly 31.7%. This is almost certainly a copy-paste error: two independent classifiers run on the same EDR-overlap subsample producing **identical** filament/sheet percentages to three significant figures is implausible. The correct V-Web filament fraction is likely close to but not identical to 31.7%. This needs to be re-verified from the underlying data — and given that the entire ASTRA cross-validation rests on this comparison, the per-class fractions for V-Web on the EDR overlap need independent confirmation.

Additionally, "only 3 spirals total in the V-Web void + wall classes" out of 25,186 (0.012%) is implausibly low — the V-Web in-footprint volume fraction for void+wall is 65.7%. Even with EDR-rosette-shell selection-function distortion, three spirals is suspicious and suggests a label-filtering or merge-key issue in the cross-match.

### P5-M23 — VoidFinder catalog count cited inconsistently across the paper
**Pages 1 (abstract), 10, 11**

The paper cites three different VoidFinder counts without reconciling:
- Abstract: "VoidFinder sphere-growing" (no count)
- Page 10 (§VIII): "1,461 interior voids with VoidFinder, 420 with V2-REVOLVER, and 295 with V2-VIDE"
- Page 11 (§VIII A): "101,863 interior hole spheres comprising the 3,765 maximal voids"
- Page 11 (§VIII C): V2-REVOLVER "n_void_catalog = 1,992 effective voids" and V2-VIDE "n_void_catalog = 1,478"

So VoidFinder has 1,461 (p.10), 3,765 maximal (p.11), and 101,863 hole spheres (p.11). V2-REVOLVER has 420 (p.10) and 1,992 (p.11). V2-VIDE has 295 (p.10) and 1,478 (p.11). No mapping between these numbers is given. The reader cannot verify which is the "correct" catalog size for the three-algorithm robustness claim. (This expands on P5-E9.)

### P5-M24 — Page 8 bright-fraction ratios use a different sample size than page 7 bright/dark counts
**Pages 7 vs. 8**

Page 8 reports "n_bright+dark = 811,609 spirals" for the contingency test. But the bright/dark count breakdown on page 7 sums to bright (775,760) + dark (14,782) + backup (875) + other (218) = 791,635 — the headline matched-spiral count. 811,609 − 791,635 = 19,974, a sample-size shift that is not explained where it appears. The χ²=4932 contingency test is on the larger sample; the per-class bright/dark counts elsewhere are on the smaller sample. This explains some but not all of P5-E12's inconsistencies — even on the 811,609 sample, total dark cannot be 14,782 while filament-class dark is 21,203.

### P5-M25 — Wall class σ has opposite sign to monopole prediction; paper claim that σ values "track" monopole is selectively applied
**Page 6, Table II**

σ_pred(wall) at n = 6,673 = 2·(−0.0026)·√6,673 = −0.425
σ_obs(wall) = **+0.55** (opposite sign)
σ_pred(void) at n = 428 = 2·(−0.0026)·√428 = −0.108
σ_obs(void) = **−0.68** (same sign but 6× the magnitude)

The paper's claim on page 6 that "the negative σ values in filament and cluster track the catalog-wide classifier-monopole offset" is true but cherry-picks the two classes where the σ has the same sign as the prediction. For wall, the sign is opposite, and for void, the magnitude is 6× the prediction. State this honestly: the monopole-tracking claim does **not** hold uniformly across the four classes; it holds only for filament and cluster, where the large N forces the σ to inherit the monopole sign.

### P5-M26 — Page 7 16-cell decomposition has cells crossing Bonferroni-16 threshold but paper does not address this
**Page 7, §VI D**

The paper reports "(Z3, D2) at σ = −3.00, (Z1, D4) at σ = −2.70, (Z4, D1) at σ = −2.67" as the strongest cells in the 16-cell z×density decomposition. Bonferroni-16 at α = 0.05: Φ⁻¹(1−0.025/16) = Φ⁻¹(0.99844) = **2.95**. So (Z3, D2) at σ = −3.00 **exceeds** the Bonferroni-16 α=0.05 threshold by 0.05σ. The paper does not state the threshold for the 16-cell decomposition, so this is undisclosed. A cell that survives Bonferroni-16 should be flagged, not just enumerated.

### P5-M27 — V2-REVOLVER non-void σ = −4.94 residual is not addressed
**Page 11, Table VIII**

The V2-REVOLVER non-void σ is −4.94 at n = 576,034 (= 678,945 − 102,911). Compute σ_pred = 2·(−0.0026)·√576,034 = **−3.95**. Residual = |−4.94 − (−3.95)| = **0.99σ**, fine. But the paper does not perform this residual calculation for the V2-REVOLVER non-void σ even though it's the strongest non-void deviation in Table VIII. The implied f_CW for V2-REVOLVER non-void is 0.4967, corresponding to ∆f_P5 ≈ −0.0033 — 27% larger than the Paper IV catalog mean −0.0026, the same kind of subsample-conditioned enhancement the paper acknowledges for the BGS-bright leg on page 12. This deserves the same explicit residual-on-the-monopole engagement.

### P5-M28 — Density-quintile Q3 σ vs. Bonferroni-5 inconsistency
**Page 6, Table III, abstract**

The abstract says density Q3 has |σ|_max = 3.94 and "below all Bonferroni thresholds" after monopole subtraction. But the paper's stated Bonferroni-5 at α=0.01 is 3.09. The **pre-subtraction** Q3 σ = −3.94 exceeds 3.09 by 0.85σ. The abstract elides this by going directly to the monopole-subtracted residual 1.87. State explicitly that the raw signal does cross 3σ Bonferroni-5 and that the headline null relies on the Paper IV monopole subtraction.

---

## NEW MINOR findings

### P5-m7 — Page 9 §VII A states σ_pred(wall) = 0.42σ
"σ_pred for V-Web monopole ranges from 0.10σ (void) through 0.42σ (wall) to 3.27σ (cluster) and 3.32σ (filament)"
Recompute: 2·0.0026·√6,673 = **0.425** ≈ 0.42 ✓. Same as cluster 3.28 vs stated 3.27 — OK; filament 3.32 ✓.
But page 6 still says filament = 3.16. Internal inconsistency (see P5-M21).

### P5-m8 — Page 6 cluster Q1 reasoning
The paper claims the cluster −4.7σ is "concentrated at the cluster/filament class boundary." But Q3 (most-typical-density cluster cells) at σ = −0.37 and Q4 (densest) at σ = −2.46 are not the boundary; the boundary is Q1 (least-dense). The text correctly identifies Q1+Q2 as the boundary, but then Q4 at −2.46 (densest, far from boundary) does not support a pure boundary-leakage story — Q4 should be cleanest. The boundary-leakage interpretation explains Q1 and Q2 but not Q4. Address.

### P5-m9 — "1,000 permutations" vs "NMC = 1000" 
Throughout the paper N_MC is sometimes 1,000 and sometimes 1000. Cosmetic, but adopt one convention.

### P5-m10 — Page 12 sky-position bin descriptions assume reader knows NGC/SGC split
"the survey-mask outside the BGS bright-side NGC+SGC coverage region" — the BGS NGC vs SGC subdivision is not previously introduced. Define on first use.

### P5-m11 — Page 18: "we explicitly do not quantify the propagated uncertainty"
The paper acknowledges it does not propagate the RSD systematic into the headline error budget. For a PRD paper this is a significant gap (see P5-M19), but the explicit honesty is appreciated. The fix is to either propagate or to widen the quoted ∆f_CW = 0.0007 confidence interval to reflect the un-quantified RSD floor.

### P5-m12 — Page 19 §XV "no published bounce or inflation model currently predicts an environment-conditional chirality signature"
This is asserted twice but no literature review supports it. A claim that no published model predicts a signal is a survey-of-literature claim and requires either citations of negative-result reviews or a more honest "we are not aware of a published model that predicts..." formulation.

### P5-m13 — Table VIII V2-REVOLVER ∆f_CW = −0.0019 vs. abstract's "|∆f_CW| < 0.002"
The abstract claims "|∆f_CW| < 0.002 at all three independent void definitions" but V2-REVOLVER's |∆f_CW| = 0.0019 satisfies this by 0.0001, i.e., the bound is functionally tight at one significant figure rather than "all three < 0.002" as a robust statement. A reader might infer that the bound is comfortably met by all three; in fact it is barely met by one. Reword as "|∆f_CW| ≤ 0.002".

---

## Summary of cumulative referee position

The combined first- and second-pass findings make a strong case for **rejection in current form**. The most serious new issues are:

1. **P5-E12** (filament-class dark > total dark) — the bright/dark numbers in the headline 3.4σ sign-flip do not internally reconcile, meaning the abstract's most-engaged-with non-null finding rests on numbers that cannot be true as written.

2. **P5-E13** (Z3 σ=−3.14 falsely claimed not to cross Bonferroni-4) — a stated threshold crossing is denied in text, undermining the multiple-testing accounting.

3. **P5-E14** (Bonferroni-9 threshold misquoted) — a fundamental statistical threshold is wrong by ~10%, shifting interpretation across the entire Phase 2 framework.

Combined with the load-bearing dependence on an unpublished Paper IV (P5-E1), the absence of a proper two-sample test on the headline DESIVAST ∆f_CW (P5-E8), the ~20-page treatment of a one-number null, and the multiple residual structures (3.4σ filament sign-flip, V2-REVOLVER 27%-enhanced monopole) that are flagged but not resolved, this manuscript needs substantial revision before it is ready for a PRD round. **Reject with invitation to resubmit** after Paper IV is published, after the bright/dark arithmetic is reconciled across all sections, and after the σ-threshold accounting is recomputed.