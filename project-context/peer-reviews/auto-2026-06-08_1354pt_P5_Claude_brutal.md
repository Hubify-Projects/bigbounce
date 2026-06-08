# P5 auto-2026-06-08_1354pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (15214 chars)
**Wall time**: 354.3s

---

# Referee Report: Paper P5 — "Environmental Dependence of Spiral Chirality"

## Overview

This paper reports a null detection of environmental dependence in spiral galaxy chirality across DESI DR1, using V-Web tidal-tensor classification and DESIVAST void catalogs. The central claim is reasonable and the analysis is extensive, but the paper has serious structural, methodological, and presentation problems that preclude publication in PRD without major revision.

---

## ESSENTIAL ISSUES

### P5-E1: Headline claim rests on unpublished companion papers
**Section II, p. 2; Refs [3], [4]**
The entire paper is built on "Paper IV" (Ref [3]), which is explicitly described as "companion work, not yet peer-reviewed" and "in preparation." The catalog, the monopole offset ∆fCW = −0.0026, the classifier definition, and the per-galaxy chirality labels all come from this unpublished work. **A PRD paper cannot rest its headline result on an unrefereed companion that the reader cannot evaluate.** Either Paper IV must be submitted/accepted first, or this paper must independently document the classifier, the monopole derivation, and the per-leg systematics it propagates.

**Fix:** Either merge the relevant Paper IV content into this submission, or hold this paper until Paper IV is publicly available and peer-reviewed.

### P5-E2: Post-hoc primary/secondary designation
**Section V B, p. 5**
The authors explicitly state: "a single a priori pre-registered analysis plan was not filed; the choice of which classifier to report as 'primary' is therefore made post-hoc." They then designate DESIVAST as "primary." This is a garden-of-forking-paths admission that the headline statistic was chosen *after seeing the results*. The V-Web cluster class shows −4.66σ and the filament class −2.61σ; these were demoted to "secondary" once they failed to support the null cleanly. The DESIVAST result was promoted because it gave |∆fCW| < 0.002.

This is not acceptable for PRD. A multi-classifier analysis without pre-registration must report all results on equal footing with a joint multiplicity correction, not a post-hoc primary designation.

**Fix:** Report all classifiers on equal footing. Apply a joint multiplicity correction across all environment-class statistics tested (V-Web ×9 sweep cells ×4 classes, DESIVAST ×3 algorithms ×2 zone defs, Tempel ×4 classes, ASTRA, etc.). The "Bonferroni-5" footnote in §V B undercounts the actual multiplicity by an order of magnitude.

### P5-E3: Cluster-class −4.66σ is not adequately resolved
**Section VI A, Table II, p. 5; Section VI D, Table IV, p. 6**
The cluster class shows σ = −4.66 at n = 397,505. The authors attribute this to the Paper IV monopole (predicted σpred ≈ −3.28). But the observed σ = −4.66 vs predicted −3.28 leaves a residual ~1.4σ, which is hand-waved. Then the within-class density quartile decomposition (Table IV) shows Q1 σ = −3.07, Q2 σ = −3.42, Q4 σ = −2.46 — three of four quartiles individually deviate at >2σ in the same direction. The authors call this "not a clean density-dependent effect" because Q3 is null, but this is selective reading: three quartiles align, one doesn't.

The "boundary misclassification leakage" argument is qualitative and not supported by a quantitative re-classification test (e.g., excluding ¯ρ ∈ [1.55, 1.86] overlap region).

**Fix:** Quantify the boundary leakage with a re-classification using a stricter λth, or honestly report that the cluster class shows a residual signal not fully explained by the catalog monopole.

### P5-E4: 3.4σ filament bright-vs-dark sign-flip is buried, not resolved
**Abstract; Section VI D, p. 7-8**
The abstract acknowledges a |z| ≈ 3.4σ filament-class bright-vs-dark sign-flip, with bright at σ = −2.80 and dark at σ = +2.85 — **opposite sign with comparable magnitude**. The authors then state "the current data do not allow us to cleanly partition between" a selection-function origin and a residual astrophysical signal. This is a significant ~3σ signal acknowledged but inadequately resolved, and the abstract's "no evidence for environment-dependent chirality" claim is in tension with this.

If the bright-dark split is real environment-conditioned residual structure at 3.4σ, the headline must be softened. If it is a selection-function leak, the authors must demonstrate this quantitatively (e.g., by reweighting BGS-bright to the dark target redshift distribution).

**Fix:** Either (a) demonstrate the 3.4σ signal is selection-function-driven via a quantitative reweighting test, or (b) report the headline as "consistent with no environment dependence except a 3.4σ filament-class bright/dark sign-flip whose origin is unresolved."

### P5-E5: σ values from incompatible null procedures juxtaposed without warning
**Throughout, especially Abstract and §VI**
The paper mixes:
- σfrom_half = (nCW − 0.5N)/(0.5√N) (binomial-from-parity)
- σvs_monopole = (fobs − f_P5_monopole) / standard error (binomial-from-monopole)
- Label-shuffle empirical p-values
- σpred predicted from Paper IV monopole

These are juxtaposed throughout (e.g., abstract: "filament; n=408,187, −2.61σ" alongside "wall; n=6,673, +0.55σ") without the explicit qualification that they share the same null but are not corrected for the catalog monopole. The reader cannot tell whether −4.66σ on cluster is meaningful without redoing the arithmetic.

**Fix:** Every reported σ must be tagged with its null reference (parity vs monopole). The headline table should report both σfrom_half and σvs_monopole side-by-side.

### P5-E6: Volume fractions inconsistent
**Section IV B, p. 4; Caption Fig. 1**
Text says "{void 0.244, wall 0.413, filament 0.333, cluster 0.010}". Sum = 1.000 ✓. But the abstract states the V-Web void class at z ≲ 0.24 is "survey-edge artifact dominated." If 24.4% of the in-footprint volume is V-Web void, but only 428 of 791,635 chirality-relevant spirals (0.054%) end up in void, the volume-to-galaxy mapping is grossly inconsistent. The text mentions "small cluster volume fraction of 1%" but writes "(the small cluster volume fraction of 1% plus the sparse r ≤ 17.8 DESI Legacy spiral selection yields a small chirality-relevant void sample)" — this seems to confuse cluster (1%) with void (24.4%) volume fractions. **This is a likely copy-paste error in a load-bearing sentence.**

**Fix:** Correct the sentence in §VI A and quantify the volume-vs-galaxy-count mismatch for the void class.

### P5-E7: HEALPix scan p-values disagree between abstract and Table V
**Abstract: p = 0.61/0.135/0.413**
**Table V: p = 0.607/0.135/0.413**
Minor numerical inconsistency, but the abstract's 0.61 vs Table V's 0.607 should match to the digits reported. Also: at NSIDE=32, "|σ|obs_max = 4.13" with p = 0.135 — this is suspiciously close to crossing significance and the look-elsewhere distinction must be made explicit. Recompute: with 3303 pixels, naive Bonferroni for 4.13σ gives p ~ 3303 × 7×10⁻⁵ ≈ 0.23, which is not quite the reported 0.135 but in the right ballpark for empirical max-stat. Acceptable, but the discrepancy in digits is sloppy.

### P5-E8: Arithmetic check on density quintile residuals (Table III)
The text says "at N = 158,327 per quintile the predicted |σpred| = 2·|−0.0026|·√158327 ≈ 2.07". Check: 2 × 0.0026 × √158327 = 2 × 0.0026 × 397.9 = 2.069 ✓. The residual |σobs − σpred| for quintile 3 = |−3.94 − (−2.07)| = 1.87 ✓. **However**, the comparison "below the Bonferroni-5 threshold |σ|Bonf_0.01,5 = 3.09" applies to |σobs|, not to the residual. The residual statistic 1.87 is not a Bonferroni-corrected significance — it is a deviation from the *predicted* offset, which has its own uncertainty from the Paper IV ∆fCW = −0.0026 ± 0.000279 (~10% uncertainty on the monopole). The quoted ±0.000279 from Paper IV propagates to σpred uncertainty of order 0.2 at N=158,327, which is not negligible. **This uncertainty is never propagated.**

**Fix:** Propagate the Paper IV monopole uncertainty into all σvs_monopole residuals.

### P5-E9: Footnote 'a' theoretical inconsistency
**Page 2, footnote a**
The footnote acknowledges that what is called "V-Web" throughout is actually the **T-Web** (tidal-tensor) of Hahn 2007, not the velocity-shear V-Web of Hoffman 2012. Using deliberately misleading nomenclature "for backward compatibility" in a PRD paper is unacceptable. The classifier is the T-Web; call it the T-Web. The §IX B comparison to Ref [11] (an actual T-Web paper) is then a like-for-like comparison and not the cross-methodology check the authors imply.

**Fix:** Rename "V-Web" to "T-Web" throughout. This significantly weakens the §IX B "concurrent-literature cosmic-web cross-validation" claim, which must be rewritten.

### P5-E10: References [11] and [12] are dated 2026 with arXiv IDs 2604.xxxxx
**References [11], [12], p. 20**
arXiv IDs "2604.02463" and "2604.01456" correspond to April 2026 submissions. Given that the present paper is dated "June 2026" and these are described as "contemporaneous" / "currently in submission to MNRAS," it is impossible for the reviewer (or any reader at the actual submission date) to verify these citations. If these are real, fine — but the cross-validation against unpublished, unverifiable contemporaneous work in §IX B and §X cannot carry weight in a PRD submission. **Reference [13] is dated 2025 ApJ — verify the citation is real (arXiv:2411.00148 → DESIVAST paper does exist).**

**Fix:** Either provide verifiable references or remove cross-validation claims that depend on unverifiable concurrent work.

---

## MAJOR ISSUES

### P5-M1: Paper is too long for its contribution
The paper is 20 pages of dense text for a null result. The headline is "no environment dependence above ~0.2 pp catalog monopole." This could be communicated cleanly in 8-10 pages. The extensive multi-stratification analysis reads as a hedge against criticism rather than a focused null test.

**Fix:** Reduce to ≤12 pages. Move ASTRA EDR cross-validation, Tempel cross-validation, and Phase 2 sweep details to supplemental material or a companion data paper.

### P5-M2: Abstract sentence structure makes claims unreadable
The abstract is one of the worst I have read in recent PRD submissions. Single sentences run 6-8 lines. Statistical caveats are nested 3-deep. Example: the sentence beginning "Headline result: the CW fraction shows no environment dependence..." contains the qualifier "(systematic-dominated for V-Web filament/cluster at n ≳ 4×10⁵)" mid-sentence and ends 9 lines later. A PRD abstract should be readable in one pass.

**Fix:** Rewrite the abstract. Target 150-200 words. State the headline cleanly, give the controlling result (DESIVAST ∆fCW = 0.0007), and stop.

### P5-M3: "Survey-scale" / "largest" framing
**Section VIII B, p. 11**
"This DESIVAST-anchored re-analysis is the largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date" — within "to date" this is trivially true since no published comparable analysis exists. Drop the superlative.

### P5-M4: Per-pixel Pearson correlation r = +0.006 over-interpreted
**Section VIII F, p. 13; Fig. 6**
The Pearson r = 0.006 at p = 0.88 is described as "statistically indistinguishable from zero" and used as load-bearing evidence. With n = 727, the 95% CI on r is approximately ±0.073 — the result is consistent with |r| up to 0.07, which is not "indistinguishable from zero" in a useful astrophysical sense. The robustness statement that 7/9 cells in the (NSIDE × cut) grid give |r| < 0.11 is fine, but the framing should be "consistent with a small or null correlation," not "indistinguishable from zero."

### P5-M5: Logistic regression z-coefficient unreported with uncertainty
**Section VI B, p. 6**
"a z-coefficient of 0.0059 with no significant intercept (0.000652)" — the intercept is given but the slope uncertainty is not. The reader cannot assess significance.

### P5-M6: Table IV redshift quartile cross-check arithmetic
**Section VI D, p. 6-7**
"cluster σfrom_half per z-quartile is −2.33, −1.73, −3.14, −2.12". Sum of squares = 5.43+2.99+9.86+4.49 = 22.77, so combined |σ_combined| = √22.77 ≈ 4.77 ≈ matches the catalog −4.66σ within rounding ✓. Acceptable.

### P5-M7: ASTRA EDR cross-validation is methodologically incoherent
**Section X, p. 16**
The authors state V-Web puts 100% of the EDR-overlap spirals into filament+cluster (no void or wall), while ASTRA argmax distributes 11.9/31.7/35.2/21.3% across the four classes. They then claim "the chirality-vs-environment headline is recovered identically by both." This is meaningless: if V-Web's classifier collapses to ~2 classes on this subsample, the "agreement" is a tautology — both classifiers see ~null because the sample is too uniform in V-Web to test anything. **This is not a robustness check; it is a degenerate sample.**

**Fix:** Either remove §X or honestly state that the per-galaxy classifier disagreement (~0% overlap on void+wall labels) means the comparison does not validate the headline.

### P5-M8: f_CW range "1.98 percentage points" misleading
**Abstract, §VI A**
The 1.98 pp range across four classes is dominated by the void bin (n=428, σ ~ 5pp counting noise) at 0.4836. Excluding void (which the authors elsewhere admit is sample-limited and contaminated), the range is 0.4963 to 0.5034 = 0.71 pp, dominated by the wall bin (n=6,673). The high-n classes (filament+cluster) range over only 0.17 pp. **The 1.98 pp headline is set entirely by sample-size-limited bins.**

**Fix:** Report the range qualified by sample size, or report separately for high-n and low-n bins.

### P5-M9: Reproducibility checklist is empty
**Page 19, "REPRODUCIBILITY CHECKLIST"**
"Single config file (available in companion data repository)" — no URL, no DOI, no repository name. "All Phase 2 sweep cell configs persisted in companion data repository" — same. The HuggingFace catalog reference "bamfai/galaxy-chirality-catalog" appears but no DOI or persistent ID. This does not meet PRD reproducibility standards.

### P5-M10: Appendix A EFT operator is acknowledged as non-derivable and non-gauge-invariant
**Page 19**
The authors honestly state the toy operator is "not contained in either Alexander & Yunes [1] ... or Lue–Wang–Kamionkowski [2]", "rotational invariance" is broken via "fixed coordinate-system unit vector ẑ", and the gauge-invariance status is unresolved. They then provide an "order-of-magnitude bound" |gφ(∇φ)/H₀| ≲ 10⁻². **An order-of-magnitude bound on an operator the authors admit is not rotationally invariant and not gauge-invariant has no physical meaning and should not appear in the paper.** This is empty content.

**Fix:** Remove Appendix A or rewrite it to either (a) cite a real operator and derive the bound from it, or (b) explicitly label it as a toy and remove the numerical bound.

### P5-M11: Selection of "chirality-relevant" subset not justified
**Throughout**
791,635 of 2,232,212 matched-primary (35%) carry "unambiguous post-TTA equivariant CW or CCW label." The 1,440,577 NS (no-signal) galaxies are dropped. The reader is not told whether NS-rate varies with environment. If NS-rate is environment-dependent (e.g., higher in dense regions due to merger/disturbance), then the chirality-relevant subset is environment-biased and the null is partially trivial.

**Fix:** Report NS-fraction by V-Web class and DESIVAST void/non-void. If it varies, propagate as a systematic.

### P5-M12: "−5σ catalog-level signal" framing
**Section VIII E and abstract**
The repeated reference to "−5σ catalog-level signal" being "concentrated entirely in the 0 maximal voids per pixel bin" is misleading. After monopole subtraction (which is the cleaner statistic the paper itself promotes in §VIII F), the catalog-level signal is consistent with zero. The "−5σ" framing is from the wrong null (parity, not monopole) and only persists because the authors keep using σfrom_half rather than σvs_monopole. This is an internal contradiction in the paper's own statistical framing.

---

## MINOR ISSUES

### P5-Mi1: Figure 1 pie chart
**P. 4**
The cluster slice (1.0%) is not visually distinguishable in a pie chart at this scale. A bar chart would be more informative.

### P5-Mi2: Figure 3 x-axis labels
The density bin edges are written as illegible overlapping numbers in scientific notation. Caption acknowledges "Den ∈ [42, 10...]" but the axis is unreadable.

### P5-Mi3: Figure 4 caption inconsistency
Caption says "|σ|obs_max = 4.13 vs the label-shuffle null |σ|null,p99_max = 4.78 gives a look-elsewhere p = 0.135." This is the same as Table V at NSIDE=32. Caption text says "no NSIDE returns p < 0.05" but only one NSIDE is shown — this should be "no NSIDE in the scan returns p < 0.05."

### P5-Mi4: Figure 5 heatmap
Cell at Rs=25, λth=0 shows "0.17" but Table II shows the canonical run's f_CW range is 0.0198 = 1.98 pp. **0.17 ≠ 0.198.** Either the table or the figure is wrong, or these are computed on different sample definitions. Investigate.

### P5-Mi5: Citation [9] Shamir 2022 amplitude
Paper says "Shamir 2022 reported a ∼2−4% large-scale asymmetry on ∼1.3×10⁶ Ganalyzer-classified galaxies." Verify this against the cited paper's actual claim.

### P5-Mi6: Duplicate phrasing
**Section VIII E, p. 12**: "the cleanest chirality σ values in this paper are the pixels with the most maximal-void coverage, not the fewest." Slightly awkward but acceptable.

### P5-Mi7: Mixed precision
σ values are reported variously to 2, 3, or 4 significant figures with no consistency (e.g., −2.61σ, −4.66σ, +0.55σ in Table II; −1.71 vs −4.59 vs +0.0007 in Table VII). Standardize.

### P5-Mi8: Equation (1)
σpred = ∆fCW / (0.5/√N) = 2·∆fCW·√N. Algebra correct ✓. But the "/" formatting is ambiguous; use displayed math clearly.

### P5-Mi9: Footnote-a placement
Footnote 'a' is on page 2 but the body claim it caveats ("V-Web") appears in the abstract on page 1. Reader doesn't see the caveat until they're past the headline.

### P5-Mi10: NS exclusion at Tempel cross-match
**Section IX A**
110,586 overlap with Tempel, but only 4 classes break down to 58,539+31,838+14,317+5,892 = 110,586 ✓. Arithmetic OK.

### P5-Mi11: Author affiliation
"Independent Researcher, Los Angeles" — acceptable for PRD, but the paper depends heavily on DESI collaboration data and an unrefereed companion paper from the same independent author. Reviewer should be aware there is no institutional oversight.

---

## NITS

### P5-N1: Date "(Dated: June 2026)" inconsistent with referenced "2026 April" papers
Acceptable if the cited concurrent works are real, but flag for verification.

### P5-N2: Section heading inconsistency
"§IX B" referenced in §IX A text but the section is titled "Concurrent-literature DR1/EDR cosmic-web cross-validation" — verify navigation.

### P5-N3: "BAMFAI" / "bamfai" username
Unusual identifier for a serious catalog. Cosmetic.

### P5-N4: "0/6 V-Web 'void' spirals fall inside any of the 101,863 DESIVAST VoidFinder holes"
n=6 is statistically meaningless. The fact that this null observation is in the abstract is overweighted relative to its information content.

### P5-N5: Equation (3) p-value
pLEE = (1 + #{...})/(1 + NMC). Standard but verify boundary handling.

---

## Summary recommendation

**REJECT**

This paper has a defensible underlying result — a null detection of environmental dependence in spiral chirality — but it cannot be accepted at PRD in its current form. The fatal issues are: (1) the central claim depends on an unpublished, unrefereed companion paper (Paper IV) whose monopole offset and classifier the reader cannot verify; (2) the primary/secondary classifier designation is explicitly post-hoc by the authors' own admission, undermining the headline null; (3) a 3.4σ filament bright-vs-dark sign-flip is acknowledged but inadequately resolved while simultaneously claiming "no evidence for environment dependence"; (4) the "V-Web" classifier is admitted in a footnote to actually be the T-Web, making the §IX B cross-classifier comparison degenerate; (5) the paper relies on 2026-April arXiv references that cannot be independently verified at the stated submission date; (6) the paper is 20 pages for a null result that should fit in 10. The authors should resolve Paper IV's publication status, rewrite with a pre-registered or properly multiplicity-corrected analysis plan, quantitatively dispatch the 3.4σ filament residual, and resubmit a much shorter version. Acceptable resubmission would require addressing all ESSENTIAL items and most MAJOR items.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Referee Findings (Fresh-Eyes Pass)

After re-examining the paper with closer arithmetic and cross-reference checks, I found several substantive issues my initial review missed. The most serious is a flat internal contradiction in sample sizes that propagates into the paper's marquee 3.4σ "filament bright-vs-dark sign-flip" claim.

---

## NEW ESSENTIAL ISSUES

### P5-E11: Filament-dark sample size is mathematically impossible
**Section VI D, p. 7–8; Abstract**

The tracer-program decomposition reports total **dark** sample n = 14,782 (LRG+ELG+QSO; sums to 791,635 with bright 775,760 + backup 875 + other 218 ✓).

But the very next page reports **"filament dark (n = 21,203)"** as the basis for the headline 3.4σ bright-vs-dark sign-flip claim.

**21,203 > 14,782 is impossible** — a subset (filament-class darks) cannot exceed its parent (all darks).

The abstract also cites "cluster_dark = 4,234." Adding filament-dark + cluster-dark = 21,203 + 4,234 = 25,437, which already exceeds the total dark count 14,782 by a factor of ~1.7, even before counting void+wall darks.

This invalidates either (a) the dark-program total, (b) the filament-dark sub-count, or (c) the headline 3.4σ z-test (the verbal z-test arithmetic in the abstract checks out *given* n_dark = 21,203, but n=21,203 is internally inconsistent with the paper's own total).

**Fix:** Resolve which number is wrong. If filament-dark is correct, the tracer-program total is wrong (and the 5σ bright-program signal needs recomputing). If the tracer-program total is correct, then the 3.4σ sign-flip — which the abstract elevates as the strongest residual structure — vanishes or shrinks.

This is the most serious arithmetic error in the paper.

### P5-E12: Table II per-class counts sum to 812,793, not 791,635
**Section VI A, Table II caption; Fig. 2 caption**

Table II reports per-class counts: void 428 + wall 6,673 + filament 408,187 + cluster 397,505 = **812,793**.

The table caption and Fig. 2 caption both state the table is computed "on the 791,635 chirality-relevant matched spirals." The discrepancy is 21,158 spirals (2.7%).

§VIII F acknowledges this exact discrepancy in a parenthetical: "the 21,158-row excess (2.7%) over the 791,635-spiral headline subsample is the population of CW/CCW-labelled spirals whose V-Web env-class assignment passes the relaxed env-label confidence used by the cosmic-web pipeline but is excluded from the headline by a stricter env-class-uncertainty filter."

So **the headline Table II uses the 812,793 superset, not the 791,635 chirality-relevant subsample** that the table caption advertises. This is a stale/inconsistent number that propagates into every per-class σ value in the headline.

The σ values would shift modestly under the stricter filter (the paper claims invariance "to 4 decimals" but does not provide the table at the 791,635 sample).

**Fix:** Either re-run Table II on the 791,635 sample as the caption claims, or correct the caption to state 812,793. Same for Fig. 2.

### P5-E13: Phase 2 sweep range conflicts with Table II range at canonical configuration
**Section VII, Table VI, Fig. 5 vs Section VI A, Table II**

Table II (canonical Rs=25, λth=0) gives a range across the four classes of {0.4836, 0.5034, 0.4980, 0.4963} → range = 0.0198 = **1.98 pp**.

Table VI / Fig. 5 cell (Rs=25, λth=0) gives "fCW range across env classes" = **0.165 pp** (10× smaller).

The reported Phase 2 number 0.165 pp matches the range across only filament+cluster (|0.4980−0.4963| = 0.17 pp), suggesting Phase 2's "range across the four cosmic-web classes" silently excludes void and/or wall (the small-N bins).

If Phase 2 silently drops the small-N classes, the abstract claim "Phase 2 sensitivity sweep ... confirms the result: the per-cell range of CW fractions across the four classes never exceeds 0.22 percentage points" is **literally false** — the canonical cell range across four classes is 1.98 pp, not 0.165 pp.

If Phase 2 uses different per-class sample sizes (because re-running V-Web with different Rs reassigns class labels), this must be stated and the per-cell per-class n's reported.

**Fix:** Either include void/wall in the Phase 2 range and report the corrected (much larger) values, or change "across the four cosmic-web classes" to "across the two high-N classes (filament+cluster)" in §VII, abstract, and Fig. 5 caption.

### P5-E14: Sign convention for ∆fCW reversed between abstract/Table VIII and text
**Abstract, §VIII B–C, Table VIII**

Table VIII reports VoidFinder ∆fCW = **+0.0007** with fvoid_CW = 0.4964 < fnon-void_CW = 0.4971.

V2-REVOLVER ∆fCW = **−0.0019** with fvoid_CW = 0.4986 > fnon-void_CW = 0.4967.

The sign convention is therefore ∆fCW = fnon-void − fvoid. But the abstract states: "fvoid_CW = 0.4964 vs fnon-void_CW = 0.4971, ∆fCW = 0.0007, statistically indistinguishable" — leaving the sign convention ambiguous. The §VIII B text uses "differing by only 0.0007 (0.07 percentage points)" as an unsigned magnitude.

Different lines mix signed and unsigned ∆fCW. Standardize and state the sign convention explicitly.

---

## NEW MAJOR ISSUES

### P5-M13: Bonferroni-threshold convention inconsistent across sections
**Eq. (2), §V A; §V B multiplicity bookkeeping; §VI D**

Equation (2) is |σ|_Bonf = √2 · erfc⁻¹(α/K). Recomputing:

- §V A: K=5, α=0.01 → √2·erfc⁻¹(0.002) = 3.09 ✓ matches paper (one-sided)
- §V A: K=1054, α=0.05 → √2·erfc⁻¹(4.7×10⁻⁵) ≈ 4.04 ✓ matches paper's 4.05 (one-sided)
- §VI D: K=4, α=0.05 → √2·erfc⁻¹(0.0125) = 2.50 ✓ matches paper (one-sided)
- §V B: K=5, α=0.05 → equation gives √2·erfc⁻¹(0.01) = **2.58**, but paper writes **2.81**

The 2.81 value corresponds to a *two-sided* Bonferroni at α/(2K), not the one-sided form of Eq. (2). So §V B is using a different (more conservative) convention than the rest of the paper, without comment. This is a real inconsistency in the multiplicity bookkeeping that controls the headline "no DESIVAST estimator crosses |σ|=2.81" claim.

Under the consistent one-sided convention (matching Eq. 2), the threshold is 2.58, and the VoidFinder voidσ=−1.71 result is further from crossing, while the V2-REVOLVER non-void σ=−4.94 still crosses heavily — but that's the non-void bin, not the primary statistic.

**Fix:** Pick one convention, apply it consistently, and recompute all Bonferroni thresholds.

### P5-M14: §VIII F "8% larger" residual reasoning is unsupported
**Section VIII F, p. 12**

The paper writes: "Arithmetic reconciliation: the P4 monopole ∆f_P4_CW = −0.0026 projects to σ_P5_pred ≈ 4.6σ on the chirality-relevant subsample; the observed −5.00σ corresponds to ∆f_P5_CW ≈ −0.0028, ∼8% larger than the P4 catalog-mean. This residual 8% enhancement is consistent with the spectroscopically-confirmed subsample being more strongly weighted to the BGS-bright leg..."

The "consistent with" is unquantified. The Paper IV monopole has uncertainty ±0.000279 quoted in §I, so the 1σ range on the projection is ∆fCW ∈ [−0.00288, −0.00232]. The observed −0.0028 sits at +0.7σ from the P4 central value, which is fully consistent with statistical fluctuation alone — no BGS-bright-leg explanation needed. The paper invents a physical interpretation for a noise-level offset.

**Fix:** State that the 8% offset is at +0.7σ of the P4 monopole uncertainty and therefore needs no additional explanation. Remove the unquantified "consistent with the spectroscopically-confirmed subsample being more strongly weighted to BGS-bright leg" claim, which would otherwise need a quantitative subsample-weight calculation to support.

### P5-M15: Abstract HEALPix p-value digit disagrees with Table V
**Abstract: p = 0.61/0.135/0.413**
**Table V: p = 0.607/0.135/0.413**

The first value 0.61 vs 0.607 — already flagged in P5-E7 as a minor consistency issue, but on re-examination it's worth noting that the NSIDE=64 p=0.413 in the abstract was originally claimed in Table V as well. Verify all three to the digit.

### P5-M16: Cross-reference: abstract "see §IX B" for V-Web void survey-edge artifact is misdirected
**Abstract, footnote-style cross-reference**

The abstract reads: "the V-Web void class at z ≲ 0.24 is sample-size limited at n = 428 chirality-relevant spirals and dominated by survey-edge artifacts (see §IX B)."

§IX B ("Concurrent-literature DR1/EDR cosmic-web cross-validation") discusses the +8-18pp V-Web vs T-Web void fraction discrepancy, attributing it to survey-shell geometry. But the n=428 small-sample issue and the direct DESIVAST cross-check that 0/6 V-Web voids fall in DESIVAST holes is in **§VIII A**, not §IX B. The cross-reference to §IX B is partial; the more direct demonstration is §VIII A.

### P5-M17: §VIII A 0/6 result misweighted
**Section VIII A, p. 10–11; Abstract robustness paragraph**

The abstract cites the "0/6 V-Web 'void' spirals fall inside any of the 101,863 DESIVAST VoidFinder holes at z ≤ 0.24" as a supporting check. Binomial p(0/6 | p_match=0.084) = (0.916)^6 = 0.59, i.e., **a 59% probability under the null that 0/6 land in voids by chance**, given the 8.4% DESIVAST void fraction at z≤0.24. This is a null observation with no statistical power, but the abstract presents it as evidence of disagreement ("0/6 V-Web 'void' spirals fall inside any DESIVAST hole"). Honestly characterize: at n=6 the test has no power to discriminate.

### P5-M18: §VI A "void volume fraction of 1%" — likely typo
**Section VI A, p. 6**

"the small cluster volume fraction of 1% plus the sparse r ≤ 17.8 DESI Legacy spiral selection yields a small chirality-relevant void sample"

The cluster volume fraction is 1.0% (correct), but the relevant fraction for the *void* sample size is the **void** volume fraction (24.4%). The sentence appears to confuse void and cluster. Given void volume = 24.4% and chirality-relevant void n=428 out of 791,635, the fraction is 0.054%, vastly below the 24.4% volume fraction — exactly the survey-edge artifact §VIII A and §IX B describe.

The current sentence justifies the small void n by appealing to the cluster volume fraction, which is nonsensical.

---

## NEW MINOR ISSUES

### P5-Mi12: Fig 5 cell label discrepancy
The Fig 5 heatmap cell at (Rs=25, λth=0) reads "0.17" per the caption text in §VII (which says "0.17"), but Table VI gives 0.165 for that cell. 0.17 ≠ 0.165 — likely just rounding in the figure label but worth standardizing.

### P5-Mi13: Cluster z-quartile combined σ check
§VI D reports cluster z-quartiles σ = (−2.33, −1.73, −3.14, −2.12) at n = 99,377+3×99,376 = 397,505 ✓. If these were independent equal-N draws from the same fCW, combined σ would be the mean σ × 2 (variance-weighted). Mean(σ) = −2.33, times 2 = −4.66 ✓ matches catalog cluster σ. OK, consistent.

### P5-Mi14: §X EDR overlap arithmetic
N_ASTRA = 648,428; N_overlap = 25,186. The paper says ASTRA argmax distributes "11.9% void / 31.7% sheet / 35.2% filament / 21.3% knot" → sums to 100.1%; one of the four is rounded up by 0.1pp. Cosmetic.

### P5-Mi15: §VIII C V2-REVOLVER catalog values
"V2-REVOLVER (n_catalog_void = 1,992 effective voids, maximum effective radius 43.5 Mpc/h)" — but the abstract says "V2-REVOLVER and V2-VIDE watershed" with 420 V2-REVOLVER voids. 1,992 vs 420 — two different counts in two different places. Possibly distinguishing "effective" vs "maximal" voids, but the difference is not explained.

### P5-Mi16: ASTRA EDR sample TARGETID overlap
"Noverlap = 25,186 spirals that carry all three labels" — but earlier the abstract says the EDR rosettes overlap with P5 is the "smallest subsample." 25,186 vs the n=428 V-Web void bin: which is smaller? n=428 is smaller. The "smallest" claim depends on definition.

### P5-Mi17: §IX A Tempel concordance metric is one-sided
"|f_Tempel_CW − f_V-Web_CW|" reported only as a magnitude. For low-N classes the counting-statistics floor easily exceeds 0.026 pp; the "concordance within spec" claim for filament is meaningful, but the failure for void/wall/cluster doesn't necessarily imply classifier disagreement — it could be sample-size noise. The text acknowledges this, but the framing of "0.2 pp spec" as load-bearing is not defended (where does 0.2 pp come from?).

### P5-Mi18: Eq. (2) is given as the family-wise threshold but used as a per-test threshold in §V B
"per-test threshold is |σ|_Bonf,0.05,5 ≈ 2.81" — this is the *family-wise* α=0.05 threshold *under* a Bonferroni-K=5 correction. Saying "per-test threshold" obscures that it's the corrected (family-wise-controlled) threshold. Cosmetic but pedagogically misleading.

### P5-Mi19: §V "deterministic-seeded NumPy default_rng (seed fixed in the pipeline config)"
The seed value is not given here; only in the Reproducibility Checklist (20260515). The pipeline config file is also not given by URL. So "seed fixed in the pipeline config" is unverifiable from the manuscript alone.

---

## NEW NITS

### P5-N6: Section labels jump
Sections IX A (Tempel) and IX B (concurrent literature) are both "additional cosmic-web cross-checks" but the abstract calls Tempel a "supporting cross-survey consistency check" while §IX B is "concurrent-literature." The hierarchy doesn't match the abstract's promotion of DESIVAST to primary.

### P5-N7: 791,635 / 812,793 / 14,782 / 21,203 numbers
The paper rotates through at least three sample-size totals in its analyses (791,635 chirality-relevant; 812,793 V-Web-classified; 678,945 z≤0.24) without ever providing a single table summarizing which N is used for which statistic. This makes verification very hard.

### P5-N8: Reference [13] Rincón formatting
DOI given as "10.3847/1538-4357/adb559" — verify (the suffix "adb559" is a real ApJ DOI form). Acceptable.

### P5-N9: Appendix A operator dimensions
The schematic operator L_parity ⊃ g_φ (∇_i φ)(∇^i ρ/ρ_bg)(L̂·ẑ) has dimensions that depend on the choice of φ normalization; the paper does not specify whether φ is canonically normalized (dim 1) or dimensionless. The "bound" |g_φ(∇φ)/H_0| ≲ 10⁻² therefore has no unique physical meaning. Already mostly covered in P5-M10.

### P5-N10: "to date" qualifier
§VIII B "the largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date" — already flagged in P5-M3. Note "to date" is doing a lot of work; the only competitor catalogs are Shamir 2022 (different methodology) and the unrefereed companion Paper IV.

---

## Summary of new-pass findings

The most damaging new finding is **P5-E11** (filament-dark n=21,203 > total dark n=14,782) — a flat numerical impossibility that undermines the headline 3.4σ bright-dark sign-flip claim. Combined with **P5-E12** (Table II sums to 812,793, not 791,635) and **P5-E13** (Phase 2 range conflicts with Table II range by 10×), the paper has three independent sample-size bookkeeping inconsistencies that propagate into headline numbers. These were missed in my initial pass because I checked individual σ values against their bin counts rather than checking bin counts against parent totals.

The Bonferroni convention inconsistency (P5-M13) is a subtle but real methodological issue that the authors should fix.

The recommendation remains **REJECT** in its current form; the new findings strengthen rather than weaken that recommendation.