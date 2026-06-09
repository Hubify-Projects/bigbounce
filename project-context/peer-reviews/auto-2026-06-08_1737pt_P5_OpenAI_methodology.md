# P5 auto-2026-06-08_1737pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (10801 chars)
**Wall time**: 459.3s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals”

Scope of review
I evaluated methodology rigor: statistical validity, estimator definitions, error propagation, internal arithmetic consistency, and correctness of quoted numbers and significances. I recomputed every quoted scalar in the abstract and main results from the provided tables/figures/equations. Findings below are organized as ESSENTIAL, MAJOR, MINOR, and NIT, each with an ID, page reference, issue, and required fix.

ESSENTIAL FINDINGS

P5-E1 (pp. 5–6; Table II and Fig. 2; also p. 12 Table X cross-reference)
Problem: Inconsistent sample size between text and table/figure for the “headline” V-Web environment results.
- Text (p. 5) and Fig. 2 caption state the analysis uses n = 791,635 chirality-relevant spirals.
- Table II’s per-class counts sum to 408,187 + 397,505 + 6,673 + 428 = 812,793 — not 791,635.
- The sum of nCW in Table II (207 + 3,359 + 203,261 + 197,284 = 404,111) matches the nCW reported later for the 812,793-superset (p. 12), confirming Table II is actually on 812,793, not 791,635.
Required fix:
- Reconcile sample sizes. Either:
  a) Recompute Table II and Fig. 2 on the 791,635-subsample and propagate corrected σ and ranges everywhere they are cited; or
  b) Explicitly state that the “headline” V-Web class table/plot use the 812,793 relaxed env-label superset and change all corresponding text and captions. Ensure internal consistency across the paper (including the abstract claim “on 791,635 chirality-relevant spirals”).

P5-E2 (p. 11; §VIII B, Table VII)
Problem: Denominator ambiguity in the DESIVAST-anchored void analysis. You define nlz = 678,945 “matched spirals” at z ≤ 0.24, then report void n = 56,981 and non-void n = 621,964 and compute fCW and σ using those N as denominators. This implies 100% of those galaxies carry CW/CCW labels, which contradicts Table I’s catalog-wide labeled fraction (791,635/2,232,212 ≈ 35.5%). Inference of N from σ and f (void: σ = −1.71 at f = 0.4964) returns N ≈ 56.4k, i.e., you used the full class counts as denominators.
Required fix:
- State explicitly whether nlz = 678,945 counts only chirality-relevant (CW/CCW) objects or all matched objects (including NS). Provide, for each class (void and non-void), the actual number of chirality-relevant galaxies used to compute fCW (nlabel) and the corresponding nCW and nCCW. If you did include NS objects in N, recompute fCW and σ correctly using only CW+CCW as denominators and update Table VII and related narrative. If the low-z subset happens to be ≈100% chirality-relevant, state and document it.

P5-E3 (pp. 5–6 and passim)
Problem: Mixed null statistics are interleaved across the paper (σfrom half vs σ relative to the P4/P5 monopole; permutation p-values; Bonferroni thresholds). While you usually label them, the “headline” environment section (§VI A) and summary statements use σfrom half, but subsequent interpretation relies on σpred from the catalog monopole without always reiterating that the nulls are different and not directly comparable. Table X introduces “σvs monopole,” but Table II and Fig. 2 do not warn the reader about non-comparability next to σpred references in the same section.
Required fix:
- Wherever σfrom half is juxtaposed with σpred (catalog monopole) or σvs monopole, add an explicit, local sentence that these statistics are defined under different nulls and are not directly comparable unless explicitly converted. Annotate Fig. 2 caption and the surrounding text accordingly. Ensure every table/figure that mixes these statistics includes this caveat.

P5-E4 (p. 8 §VI D.d; also Abstract, p. 2 §II; passim)
Problem: Terminology: You compute a tidal-tensor classifier from the smoothed density field (the so-called T-Web in Hahn+2007; the “V-Web” of Hoffman+2012 uses velocity shear). You explicitly acknowledge this on p. 2 n.a. but persist in labeling the classifier as “V-Web” throughout. This will confuse readers and misattributes prior art.
Required fix:
- Rename the classifier consistently to T-Web (tidal-tensor from density) across the manuscript, including figures, tables, and supplementary files. If you keep “V-Web” anywhere, insert “(density tidal-tensor; T-Web)” alongside and provide a global note in the introduction committing to T-Web terminology.

P5-E5 (p. 8 §VI D.b vs. p. 17 §XI)
Problem: Contradictory statements about target-program split. In §VI D.b you report bright (BGS) fCW = 0.4970 and dark fCW = 0.5051 on the full matched-spiral catalog — an 0.81 pp difference — and emphasize a sign flip by environment. In §XI “Systematics and null tests” you state: “target-class split (BGS vs. LRG-ELG-QSO) with BGS-only CW fraction within ±0.001 of LRG-ELG-QSO,” which directly contradicts §VI D.b.
Required fix:
- Recompute and restate the §XI systematics split or correct the text. If §XI refers to a different selection (e.g., after P5-monopole subtraction, or after restricting to some subset), specify the exact sample and provide the corresponding numbers. As written, it is internally inconsistent and undermines the systematics narrative.

P5-E6 (pp. 4–5; §IV and throughout the V-Web/T-Web pipeline description)
Problem: No treatment of the DESI radial selection function in building δ(x). You form δ = ρ/ρ̄ − 1 on a single global mean over an in-footprint mask spanning 0.01 ≤ z ≤ 2 with strongly redshift-dependent n(z). Without correcting for the selection function (or restricting to a volume-limited subsample), the overdensity field — and thus the tidal-tensor eigenvalues and class boundaries — are biased by survey depth variations and mask geometry. You allude to “survey-shell artifacts,” but the present pipeline lacks even a first-order correction (e.g., random catalogs, FKP-like weights, radial normalization, or per-slice means).
Required fix:
- Either (a) implement a proper selection-function correction when constructing δ (e.g., use random catalogs to estimate ρ̄(x) within the mask and per-z-slices), and rerun the T-Web classification; or (b) explicitly demote all full-sample T-Web environment claims to a purely illustrative, secondary diagnostic and move them to an appendix, restricting headline quantitative statements to the DESIVAST-anchored (volume-limited) analysis. If you take (b), revise language in §VI A currently calling the T-Web result “headline.”

MAJOR FINDINGS

P5-M1 (p. 6 §VI A)
Problem: Miscomputed σpred for the filament class under the Paper IV monopole. You state σpred(filament) ≈ −3.16 for ∆fCW = −0.0026 and N = 408,187. The correct value is σpred = 2|∆f|√N = 0.0052 × √408,187 = 0.0052 × 638.9 ≈ 3.32 (negative sign). Cluster σpred ≈ −3.28 is correct.
Required fix:
- Correct the filament σpred and propagate the corrected comparison text.

P5-M2 (p. 9 §VII A; p. 6 §V B “Multiplicity bookkeeping”)
Problem: Incorrect Bonferroni threshold quoted. For five tests at family-wise α = 0.05, you state |σ|Bonf ≈ 2.81 (p. 6). The correct two-sided threshold is zα/(2K) with α/K = 0.01 ⇒ |z| ≈ 2.576. Your general formula (Eq. 2) would also yield ≈2.576. The 2.81 value is too stringent by ~0.23σ.
Required fix:
- Replace 2.81 by 2.576 (or 2.58) and confirm that none of your DESIVAST five primary statistics cross the corrected threshold. Adjust any textual claims that referenced 2.81.

P5-M3 (pp. 1–2 Abstract; p. 10 Fig. 5 caption; passim)
Problem: Mixed units for Phase-2 sweep range. Abstract: “range never exceeds 0.22 percentage points (max 0.0022 at Rs = 25, λth = 0.3).” One is in percentage points (pp), the other is a fraction. Similar mixing appears elsewhere.
Required fix:
- Use a single unit consistently (either 0.22 pp or 0.0022 in fractional units) in every occurrence, including captions and text.

P5-M4 (pp. 8–9; Table V and Fig. 4)
Problem: HEALPix max-σ look-elsewhere p-values are reported from NMC = 1000 draws but without uncertainty. At p ≈ 0.135, the Monte Carlo standard error is ≈ sqrt[p(1−p)/(NMC+1)] ≈ 0.011. You do not quantify this, and the exact thresholding statement “no NSIDE returns p < 0.05” is fine, but readers should see the MC precision.
Required fix:
- Add the MC uncertainty on reported permutation p-values (e.g., p = 0.135 ± 0.011), or state the generic ±1σ precision for all permutation p-values in Methods and refrain from over-interpreting differences of a few ×10−3–10−2.

P5-M5 (pp. 8, 12; internal labels)
Problem: Internal tag “P5” appears in figure titles/captions and text (e.g., Fig. 4 title; p. 12 “P5 matched-spiral catalog monopole”). This is an internal project label, not a scientific descriptor.
Required fix:
- Remove “P5” from the scientific text, figure titles, and captions. Replace by a neutral descriptor (e.g., “this work”).

MINOR FINDINGS

P5-m1 (p. 15; Table XI and Fig. 7 caption/body text)
Problem: Reported V-Web vs Tempel “filament” concordance is quoted as 0.026 pp but from the table values fV−Web = 0.4980 and fTempel = 0.4982, the difference is 0.0002 = 0.02 pp.
Required fix:
- Correct 0.026 pp to 0.02 pp (or provide the exact values used if more precise numbers underlie the plot).

P5-m2 (p. 8 §VI D.b)
Problem: The reported two-sample z ≈ 3.4σ for filament bright vs dark is consistent with a back-of-envelope recomputation using your own σ and N values; however, please add the actual fbright and fdark used and the pooled-variance formula to make this reproducible.
Required fix:
- Provide fCW and n for bright/dark in the filament class (you already give n), and either the z formula or the computed p-value.

P5-m3 (p. 12 §VIII F; Fig. 6 caption vs. main text)
Problem: Pixel counts differ across related statements without explicit cross-reference: Fig. 6 bottom says “1,496 valid pixels (≥ 200 spirals)”, main text uses 727 pixels for the Pearson correlation (those with both ≥ 200 spirals and ≥ 1 maximal void). This is presumably by design but is not made explicit in the caption.
Required fix:
- Clarify in the figure caption that 1,496 pixels meet the ≥ 200-spiral cut, of which 727 also contain ≥ 1 maximal void and enter the Pearson calculation.

P5-m4 (p. 3 §III B vs. p. 4 §IV A step 1)
Problem: Slight inconsistency in parent-sample filtering description. §III B says SPECTYPE ∈ {GALAXY, QSO}; §IV A step 1 uses SPECTYPE = GALAXY to construct the tidal field.
Required fix:
- Clarify explicitly that QSO targets are excluded from the T-Web construction (but may remain in the matched catalog counts), and harmonize the wording.

P5-m5 (p. 10 §VIII A/B)
Problem: VoidFinder hole radius statements are inconsistent in specificity. You use a fixed k = 20 KDTree query, citing “24 Mpc/h maximum hole radius,” but the text does not provide the actual distribution/range for VoidFinder holes, while later you provide maxima for V2-REVOLVER/V2-VIDE.
Required fix:
- Add the maximum VoidFinder hole effective radius from the DESIVAST release and justify the KDTree neighbor count with that number.

P5-m6 (p. 8 §VI D title and paragraph)
Problem: Title says “Within-class density-stratified cluster + filament follow-up.” Absent are explicit nCW values or fCW per quartile; only σ are shown.
Required fix:
- Add fCW per quartile (or at least the deviations ∆f to permit independent recomputation of σ).

P5-m7 (p. 6 §V B “Multiplicity bookkeeping”)
Problem: The “primary vs secondary” analysis designation is post hoc. You are transparent about it, but the phrase “headline result rests on DESIVAST” conflicts with §VI A’s header calling the T-Web table a headline.
Required fix:
- Make the section headers consistent with the declared primary analysis (DESIVAST). Rename §VI A accordingly.

NITPICKS

P5-n1 (p. 9 §VII header line)
Problem: Typo: “Ngrid = 256 × λth ∈ {0.0, 0.1, 0.3}” conflates grid size and eigenvalue threshold.
Required fix:
- Replace by “Ngrid = 256^3; λth ∈ {0.0, 0.1, 0.3}”.

P5-n2 (p. 8 §VI D.a)
Problem: “Bonferroni-4 |σ| = 3.02 threshold at α = 0.01” could be given with more standard rounding (3.03).
Required fix:
- Optional: round consistently; no change in substance.

P5-n3 (p. 8 §VI D.d)
Problem: “p < 10−1000” is not meaningful numerically and suggests unjustified precision.
Required fix:
- Replace by “p ≪ 10−10” or “p effectively zero at machine precision,” and state the exact χ^2 calculator/library if you keep a numeric bound.

P5-n4 (pp. 1–2 Abstract)
Problem: “∼0.2 pp” vs. later “∆fCW ≈ −0.0026” (0.26 pp) — pick one precision level.
Required fix:
- Use consistent significant figures (e.g., 0.26 pp) in the abstract.

Methodological notes and recomputations checked
- Table II σfrom half values match direct recomputation from n and nCW.
- Range across classes in Table II is 1.98 pp as stated.
- Density-quintile σobs − σpred residual 1.87 (Table III, quintile 3) matches direct recomputation.
- Phase-2 per-cell ranges in Table VI max at 0.220 pp; matches text.
- DESIVAST void/non-void ∆fCW = 0.0007 (Table VII) matches the tabulated f values; σ magnitudes are consistent with the listed N (subject to P5-E2 clarification).
- Three-algorithm DESIVAST differences |∆fCW| < 0.002 (Table VIII) consistent with recomputations by inverting σ.
- HEALPix “0-voids/pixel” bin σpred = −3.20 and residual −1.55σ (Table IX) are arithmetically correct.
- σvs monopole in Table X matches recomputation using fP5 = 0.49719.
- Tempel+2014 class-level σ (Table XI) match recomputation from n and nCW.

Length and focus
The manuscript is 20 pages and attempts to cover multiple classifiers, sweeps, and cross-checks. Given that the declared primary result is the DESIVAST-anchored void null, the paper can be tightened:
- Recommendation: limit the main text to the DESIVAST-anchored analysis, the minimal T-Web cross-check with corrected selection-function discussion, and a succinct set of null tests. Move extended sweeps (nine-cell grid), ASTRA per-object overlap, and some HEALPix scans to an appendix. Target ≤ 14 pages for the main text.

## Summary recommendation
MAJOR REVISIONS

The core DESIVAST-anchored result (no void/non-void chirality difference at the ∼10−3 level) appears numerically sound and appropriately cautious. However, there are critical internal inconsistencies (sample-size mismatch between text and Table II/Fig. 2; contradictory target-program split statements; ambiguous denominators in the DESIVAST section), a methodological deficiency in the construction of the full-sample tidal-tensor field without selection-function correction, and confusing terminology (“V-Web” vs “T-Web”). These issues must be corrected for PRD-level methodological rigor. With the essential/major fixes above, the paper could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P5-E7 (Abstract vs declared primary; pp. 1–2 vs. p. 5 §V.B and §VIII heading)
Problem: Abstract frames the “headline result” around the V-/T-Web cross-check (per-class CW fractions on the “791,635 chirality-relevant spirals”), whereas §V.B explicitly declares the DESIVAST-anchored void analysis as the primary load-bearing result. The abstract’s lead sentence (“Headline result: the CW fraction shows no environment dependence … within DESI DR1 at V-Web resolution”) is inconsistent with this declared primary. This is more than wording: the abstract’s specific per-class numbers are on the 812,793 superset (see P5-E1 from the first review) and the V-/T-Web pipeline lacks a selection-function correction (P5-E6).
Required fix:
- Rewrite the abstract so that the declared primary (DESIVAST three-algorithm void analysis) anchors the headline claim and numbers, with the V-/T-Web cross-check clearly designated as a secondary diagnostic. Ensure the sample size stated in the abstract matches the dataset actually used for the numbers quoted (see P5-E1).

P5-E8 (Internal cross-reference inconsistency; p. 10 §VIII RSD paragraph)
Problem: The sentence “This is in contrast to the V-Web secondary path (§XIII), where the tidal-tensor eigenvalue field is computed from redshift-space …” points readers to §XIII as if it described the V-/T-Web pipeline. §XIII is a limitations section (which does discuss RSD caveats), not the pipeline description (that is in §IV). This is confusing and misdirects the reader looking for methodological details.
Required fix:
- Change the reference to “(see §IV for the V-/T-Web pipeline; RSD limitations are discussed in §XIII)” or equivalent, so the reader lands on the method where promised.

MAJOR

P5-M6 (Contingency test counts and deviations; p. 8 §VI.D.d)
Problem: The contingency-test paragraph states “nbright+dark = 811,609 spirals,” “overall matched-spiral ratio 0.978,” and “max class-to-overall bright-fraction deviation 1.5 pp,” with per-class bright fractions {void 0.981, wall 0.962, filament 0.966, cluster 0.989}.
- Arithmetic check: with the quoted overall 0.978, the largest class-to-overall deviation is actually 1.6 pp (wall: 0.962 vs 0.978), not 1.5 pp.
- Internal-consistency check: earlier program counts for the 791,635 chirality-relevant sample are bright 775,760 and dark 14,782 (total bright+dark 790,542), implying an overall bright fraction of 0.980 (including backup/other gives 0.980; excluding them gives 0.982). None equals 0.978. The 811,609 bright+dark count also does not align with any previously stated sample (it appears to be the 812,793 superset minus a different backup/other tally, but that isn’t stated).
Required fix:
- Provide the exact sample used for the contingency test (is it the 812,793 superset? which program categories are included?), list the bright/dark counts per class and in total, and recompute the class-to-overall deviations. If 0.978 is the overall bright fraction on a different sample than §VI.D.b, say so and reconcile the different baselines. Correct the “1.5 pp” to the actual value (likely 1.6 pp) once counts are clarified.

P5-M7 (Catalog-native void membership boolean vs. narrative; p. 12 §VIII.D)
Problem: You state the catalog-native definition “excludes the survey-mask edge galaxies,” but the explicit boolean you give is OUT = 0 ∧ VOID0 ≥ 0 ∧ ZONE ≥ 0 — which does not filter on EDGE (you mention the EDGE flag earlier in the sentence). As written, this boolean does not enforce “edge-exclusion.”
Required fix:
- Either include the EDGE exclusion explicitly (and DEPTH if intended), or revise the narrative to reflect the exact boolean used. Report how many galaxies are dropped by EDGE (and/or DEPTH) to justify the “edge-excluding” claim.

P5-M8 (Permutation resolution/precision; pp. 8–9 §VI.E and p. 9 §VII.A)
Problem: All permutation/LEE p-values are based on NMC = 1000. For p near conventional thresholds, this yields a coarse resolution (min step ≈ 0.001; 1σ MC error ≈ 0.01 at p ≈ 0.1). Although you now add an uncertainty in some places (see new MINOR below), several p-values (e.g., p = 0.135, 0.135 vs 0.135±0.011) are close enough to family-wise thresholds that a factor-10 increase in NMC is warranted to avoid MC noise dominating the interpretation.
Required fix:
- Increase NMC to ≥ 10,000 for all reported permutation tests (HEALPix and sweep max-σ) or explicitly state that the p-values are “coarse” due to NMC = 1000 and confirm that conclusions are unchanged with a higher NMC on the most borderline case(s).

P5-M9 (Redshift logistic regression under-specified; p. 6 §VI.B)
Problem: The logistic regression claim (“z-coefficient 0.0059 with no significant intercept (0.000652)”) is not reproducible: no standard errors, CIs, model formula, link function, covariate scaling, or sample size are reported. “No significant intercept” without uncertainty is not meaningful.
Required fix:
- Report the full model specification, coefficient estimates with standard errors (or 95% CI), z- or Wald p-values, sample size, and pseudo-R^2. Clarify whether covariates were standardized and whether multicollinearity was checked.

P5-M10 (Survey-shell artifact claim needs a quantitative map-level demonstration; pp. 13–15 §IX.B and p. 11 §VIII.A)
Problem: The claim that the excess V-/T-Web “void” fraction is driven by survey-shell edge artifacts is plausible, but the support provided is qualitative (comparison to an external DR1 T-Web paper and a 0/6 overlap of low-z “voids” with DESIVAST holes). A quantitative in-sample demonstration is missing.
Required fix:
- Add a map-level quantification on DR1: e.g., show the cross-correlation of “void”-labeled cells with mask-boundary distance, or the void-class fraction as a function of mask-edge proximity, with uncertainty bands. This can be brief (one panel or a short table), but it should numerically support the survey-shell explanation.

MINOR

P5-m8 (NSIDE=32 pixel-count inconsistency; p. 13 §VIII.F vs. Fig. 6 caption)
Problem: §VIII.F states “distribution … across the 1,821 valid pixels” at NSIDE=32, whereas Fig. 6 bottom caption says “1,496 valid pixels (≥ 200 spirals).” Later in the same paragraph the Pearson correlation is computed on 727 pixels (≥1 maximal void and ≥200 spirals). The 1,821-pixel count is unexplained.
Required fix:
- Clarify the three counts in one place: total valid pixels used for σvs-monopole, those passing the ≥200-spiral cut, and those also containing ≥1 maximal void (for the Pearson). Make the figure caption precise about which subset each panel/statistic refers to.

P5-m9 (Bright/dark sign-flip reproducibility; p. 7 §VI.D.c)
Problem: You quote filament bright and dark σ values (−2.80 and +2.85) and a joint two-sample |z| ≈ 3.4, but do not provide the corresponding fCW for bright and dark (or the pooled-variance formula) to enable reproduction.
Required fix:
- Provide fbright, fdark, and n for the filament class (you already list n, but repeat them for clarity), and either the two-sample z formula used or the exact p-value.

P5-m10 (Overall “bright-fraction 0.978” ambiguous; p. 8 §VI.D.d)
Problem: The “overall matched-spiral bright-fraction 0.978” conflicts with simple ratios computed earlier on the 791,635 sample (0.980 including backup/other; 0.982 bright/(bright+dark)). It may be computed on a different sample (e.g., 812,793 superset). As written, it is not reproducible.
Required fix:
- State explicitly which sample the 0.978 value is computed on and provide the underlying counts so readers can reproduce it.

P5-m11 (Permutation p-values: add generic MC error once globally; pp. 8–9)
Problem: The HEALPix p-values are quoted without uncertainty in Table V but with more context in the text/figure (still no explicit ±). A single methods sentence quantifying the typical 1σ MC error for NMC = 1000 would prevent over-interpretation.
Required fix:
- In Methods (§V), add: “Permutation p-values are reported with 1σ Monte Carlo uncertainty σp ≈ sqrt[p(1−p)/(NMC+1)] (e.g., ±0.011 at p ≈ 0.135 with NMC = 1000).” Optionally add ±σp to Table V entries.

P5-m12 (VoidFinder radius bound consistency; p. 11 §VIII.A and p. 12 §VIII.B/C)
Problem: You fix k = 20 in the KDTree query “given the 24 Mpc/h maximum hole radius,” but you later give maxima for V2-REVOLVER (43.5) and V2-VIDE (55.9) without providing the VoidFinder maximum. The 24 Mpc/h figure is undocumented in the text.
Required fix:
- Add the actual maximum VoidFinder effective radius from DESIVAST to justify the k = 20 choice (and confirm the chosen neighbor count covers 3σ of the radius distribution).

P5-m13 (Jeffreys interval phrasing; p. 4 §V)
Problem: You refer to “exact binomial 95% credible interval” and then specify Jeffreys. Jeffreys is a Bayesian credible interval with a Beta(1/2,1/2) prior; it is not “exact” in the Clopper–Pearson sense.
Required fix:
- Rephrase to “Jeffreys 95% binomial credible interval” (drop “exact”) to avoid confusion with Clopper–Pearson.

P5-m14 (Small arithmetic slip in text; p. 8 §VI.D.d)
Problem: “max class-to-overall bright-fraction deviation 1.5 pp” should be 1.6 pp given the quoted fractions (0.962 vs 0.978).
Required fix:
- Replace “1.5 pp” with “1.6 pp” (or update both numbers once the overall fraction is reconciled per P5-M6).

P5-m15 (Figure 6 caption clarity; p. 14)
Problem: The top map uses NSIDE = 32 for maximal-void counts (885 occupied pixels, median 4 per pixel). Earlier in §VIII.E you quote NSIDE = 16 for a similar stratification (297 occupied pixels, median 14). Readers may assume a mismatch.
Required fix:
- Add a parenthetical in the Fig. 6 caption noting “NSIDE = 32 here (NSIDE = 16 variant discussed in §VIII.E), hence different occupied-pixel counts and medians.”

NIT

P5-n5 (Typo/format; p. 12 §VIII.F)
Problem: “At the HEALPix-NSIDE-= 32 per-pixel level” has a stray hyphen after NSIDE.
Required fix:
- Remove the stray hyphen: “At the HEALPix NSIDE = 32 per-pixel level …”

P5-n6 (Unit rounding consistency; multiple places following “pp”)
Problem: Some per-class ranges and deltas are given in pp with two decimals and others as 0.0xxx fractions. While you already address the largest instance (P5-M3), small instances remain scattered.
Required fix:
- Standardize to either pp or fractional units throughout figures and text; if pp, round consistently to two decimals unless higher precision is needed for a specific comparison.

Explanation
I did not repeat issues from the first review. The new items focus on fresh inconsistencies uncovered by recomputing values, reconciling sample counts, checking cross-references, and probing places where the narrative overclaims without a quantitative support figure or where method details are insufficient for reproduction.