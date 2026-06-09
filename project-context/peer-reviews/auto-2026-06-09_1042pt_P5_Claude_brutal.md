# P5 auto-2026-06-09_1042pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (15736 chars)
**Wall time**: 443.6s

---

# Referee Report: P5 — "Environmental Dependence of Spiral Chirality"

## Overall Assessment

This paper presents an environmental null test for spiral galaxy chirality using DESI DR1, anchored on a chirality catalog from a companion paper (Paper IV) that is **not yet peer-reviewed and not publicly available**. The paper performs many cross-checks, but suffers from severe structural problems: (1) the foundational input is unpublished and unrefereed, (2) the "headline" is a null result whose statistical power is undermined by acknowledged systematics, (3) extensive post-hoc analysis paths with explicit admission that no pre-registration was filed, (4) the abstract and body make claims that on close inspection are weaker than presented, (5) there is a real 3.4σ residual (filament bright-vs-dark sign-flip) that is acknowledged but then dismissed by anchoring the headline on a different analysis path, and (6) the EFT operator in Appendix A is acknowledged to be non-covariant and non-gauge-invariant — a serious problem for a PRD submission.

The paper is too long (20 pages) for what is fundamentally a null result. I recommend rejection in current form.

---

## ESSENTIAL Findings

### P5-E1: Foundational catalog is unpublished, unrefereed, and not provided
**Abstract, p.1; §II, p.2; §III A, p.3**
> "We cross-match the 8,474,531-galaxy chirality catalog of Paper IV [3] (companion work, not yet peer-reviewed)..."
> "Paper IV [3] (a companion work by the same author, currently in preparation and not yet peer reviewed; the present manuscript treats its catalog and quoted monopole offset as inputs whose uncertainty is propagated explicitly below)"

Reference [3] is "in preparation; manuscript in preparation." The entire analysis depends on a per-galaxy CW/CCW classification catalog whose construction, validation, systematics quantification, and ∆f_CW = −0.0026 monopole offset are not documented in any refereed source. PRD cannot accept a paper whose primary observable depends entirely on an undocumented, non-peer-reviewed catalog by the same author.

**Required fix:** Either Paper IV must be accepted/published first, or its key methodology and validation must be reproduced in full within this paper as a self-contained Appendix. The σ_pred = −2∆f_CW√N construction used throughout cannot be quoted from a non-existent paper.

### P5-E2: Headline σ values from different null procedures juxtaposed without "not directly comparable" qualifiers
**Abstract, p.1**
> "Per-class CW fractions on the 791,635 chirality-relevant spirals are, in order of decreasing n: 0.4980 (filament; n=408,187, −2.61σ), 0.4963 (cluster; n=397,505, −4.66σ)..."

These σ values are "from-half" (deviation from 0.5), but the abstract immediately interprets them as "tracking the catalog-wide ∆fCW = −0.0026 classifier-monopole offset." This conflates two distinct nulls: (i) the parity null at 0.5, and (ii) the catalog-monopole null at 0.4974. The reader is given numbers under one null and interpretation under another, without a clear "these σ values are not the environment-test significance" warning. The actual environment-test residuals (Table X: |σ| < 1.15) appear 11 pages later.

**Required fix:** The abstract must report the monopole-subtracted σ values as the headline, not σ_from-half. Or it must explicitly state "the σ values quoted in the abstract are not environment-test significances."

### P5-E3: "Largest matched-sample environmental-dependence test of spiral chirality in DESI DR1" — unsupported novelty claim
**§VIII B, p.11**
> "This DESIVAST-anchored re-analysis is the largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date..."

This is necessarily true only because nobody else has done this test on DR1 yet. Claiming "largest" when no prior work exists in this configuration is not a substantive novelty claim. Furthermore, it is anchored on a non-peer-reviewed catalog (P5-E1).

**Required fix:** Remove "largest" framing or compare to specific prior DR1/Legacy analyses (Shamir 2022 is cited but is on Legacy not DR1).

### P5-E4: 3.4σ filament bright-vs-dark sign-flip dismissed by re-anchoring, not resolved
**Abstract, p.2; §VI A, pp.7–8**
> "The joint two-sample z-test on the bright-vs-dark fCW difference is |z| ≈ 3.4σ on the filament class... The headline environment-independence statement of this paper is anchored on the DESIVAST primary analysis below (§VIII), which is constructed to be insensitive to this residual"

A 3.4σ residual that the authors admit cannot be cleanly partitioned between selection-function origin and astrophysical signal is being explicitly hidden behind an analysis-path choice. This is exactly the "garden of forking paths" the authors say they want to bound (§V B), but they then walk straight into it. The DESIVAST primary path is at z ≤ 0.24 BGS-only, so by construction it cannot test the filament bright-vs-dark signal that the authors flag as the strongest residual. This is not a resolution; it's a dodge.

**Required fix:** The 3.4σ residual is either a real result (and the headline "no environmental dependence" claim is wrong) or it is a systematic (and must be characterized as such, not buried). The current "we anchor on a different analysis where this can't be tested" framing is unacceptable.

### P5-E5: Appendix A EFT operator is acknowledged to be non-covariant and non-gauge-invariant
**Appendix A, p.19**
> "the explicit (L̂ · ẑ) factor breaks rotational invariance via the fixed coordinate-system unit vector ẑ"
> "are quantities defined in a chosen synchronous-comoving slicing... and are not manifestly gauge invariant"
> "We have not carried out that construction"

The authors include an "EFT mapping" in the appendix that they themselves admit breaks rotational invariance AND is not gauge invariant. This is a fatal flaw for any EFT construction in a PRD paper. The appendix as written cannot be defended.

**Required fix:** Either remove Appendix A entirely or replace it with a covariant, gauge-invariant construction. Stating "we deliberately keep the parameterization schematic" does not rescue an EFT operator from non-covariance.

### P5-E6: Pre-registration confession with post-hoc primary path designation
**§V B, p.5**
> "a single a priori pre-registered analysis plan was not filed; the choice of which classifier to report as 'primary' is therefore made post-hoc"

The authors openly admit the primary analysis path is chosen post-hoc, after seeing the results across multiple classifiers and stratifications. This is the textbook definition of multiple-comparisons bias. The Bonferroni-5 correction applied only across the 5 DESIVAST estimators does not bound the actual multiplicity, which spans V-Web × Tempel × DESIVAST × ASTRA × T-Web × multiple stratifications.

**Required fix:** Either report a fully family-wise-error-rate-controlled significance across all reported analyses, or explicitly downgrade all results to exploratory status with no claim of detection/non-detection significance.

### P5-E7: σ_pred formula is dimensionally inconsistent / unclear
**§V, Eq. (1), p.4**
> σ_pred = ∆f_CW / (0.5/√N) = 2 · ∆f_CW · √N

For ∆f_CW = −0.0026 and N = 408,187, σ_pred = 2 × (−0.0026) × √408,187 = 2 × (−0.0026) × 638.9 ≈ −3.32. The text says σ_pred(filament) ≈ −3.16 (p.6); recomputed: −3.32. Discrepancy.

For cluster N = 397,505: 2 × (−0.0026) × √397,505 = 2 × (−0.0026) × 630.5 ≈ −3.28. Text agrees on cluster but not filament.

**Required fix:** Recompute σ_pred values throughout; reconcile (3.16 vs 3.32) discrepancy.

---

## MAJOR Findings

### P5-M1: Abstract is excessively long and packs primary results into prose density that obscures the result
**Abstract, pp.1–2**
The abstract is ~1.5 pages and contains multiple numerical results, parenthetical caveats, signed-σ values under inconsistent null hypotheses, and a "Robustness" section. PRD abstracts should be ~300 words. This is closer to 1500.

**Required fix:** Cut abstract by 2/3.

### P5-M2: σ_obs − σ_pred residual quoted as |1.87| with claim "below all Bonferroni thresholds"
**Abstract, p.1**
> "|σmax| = 3.94 across density quintiles... corresponding monopole-subtracted residual is |σobs − σpred| = 1.87, below all Bonferroni thresholds"

The procedure of subtracting a predicted monopole σ from an observed σ to get a "residual" is non-standard. The proper treatment is to subtract ∆f_CW from f_CW and compute the binomial significance of the residual against zero. Quoting |σ_obs − σ_pred| is statistically suspect because the two σ's are not orthogonal (both involve the same N).

**Required fix:** Replace with the proper monopole-subtracted residual significance computation.

### P5-M3: Table III recompute — Quintile 3 σ_obs and σ_pred
**Table III, p.6**
| Quintile | f_CW | σ_obs | σ_pred | |σ_obs − σ_pred| |
| Q3 | 0.4950 | −3.94 | −2.07 | 1.87 |

Check: σ_pred = 2 × 0.0026 × √158,327 = 0.0052 × 397.9 = 2.07 ✓
Check σ_obs at f=0.4950, N=158,327: σ = (0.4950 − 0.5)/(0.5/√158327) = −0.005 × 2 × 397.9 = −3.98. Text says −3.94. Off by 0.04 — possibly rounding from un-rounded f, acceptable.

But: text in §VI C says "|σ|max = 3.94" — consistent with table. OK.

### P5-M4: HEALPix label-shuffle null procedure description is incomplete
**§V A, p.4**
The empirical max-stat null uses "NMC label-shuffle permutations preserving sample size; for each realization we record the maximum absolute σ_from half across the K bins." But the per-pixel sample sizes vary widely across HEALPix pixels (some pixels have ~10 spirals, others ~1000). Whether the shuffle preserves per-pixel N matters for the null distribution.

**Required fix:** Clarify whether per-pixel N is preserved or if labels are globally shuffled.

### P5-M5: Tempel FoF cross-check used as "supporting" cross-survey check is actually SDSS DR10, not DESI
**Abstract, p.1; §IX A, p.13**
The Tempel catalog is on SDSS DR10. Using it as a cross-classifier check on DESI spirals is fine, but the abstract describes it as "a supporting cross-survey consistency check (different parent catalog, SDSS DR10, only ∼14k galaxies in the filament-like bin..." OK, this is disclosed, but the 0.026 pp concordance is highlighted prominently while the small-class disagreements (1.11 pp, 0.62 pp, 0.66 pp) are downplayed.

**Required fix:** Report all four concordance values with equal weight in the abstract or remove the 0.026 pp value from the abstract.

### P5-M6: Per-class n in Table II — Cluster − Filament difference
**Table II, p.5**
- Filament n=408,187, n_CW=203,261. Check: 203,261/408,187 = 0.49795 → reported 0.4980 ✓
- Cluster n=397,505, n_CW=197,284. Check: 197,284/397,505 = 0.49631 → reported 0.4963 ✓
- Wall n=6,673, n_CW=3,359. Check: 3,359/6,673 = 0.50337 → reported 0.5034 ✓
- Void n=428, n_CW=207. Check: 207/428 = 0.48364 → reported 0.4836 ✓

Sum: 428+6,673+408,187+397,505 = 812,793. But headline is 791,635 chirality-relevant. The 21,158 excess is acknowledged in §VIII F (p.12) but Table II does not note this. The reader sees Table II totaling to 812,793 but text claims n=791,635.

**Required fix:** Add footnote to Table II reconciling 812,793 vs 791,635.

### P5-M7: σ_from_half recompute for cluster
**Table II, p.5**
σ = (n_CW − 0.5N)/(0.5√N) = (197,284 − 198,752.5)/(0.5 × 630.48) = −1468.5/315.24 = −4.66 ✓

Filament: (203,261 − 204,093.5)/(0.5 × 638.9) = −832.5/319.45 = −2.61 ✓

Void: (207 − 214)/(0.5 × 20.69) = −7/10.35 = −0.68 ✓

Wall: (3,359 − 3,336.5)/(0.5 × 81.69) = 22.5/40.85 = +0.551 ✓

All Table II σ values check out.

### P5-M8: Table VII — DESIVAST void f_CW recompute
**Table VII, p.11**
- Void: n=56,981, f=0.4964. n_CW = 28,285 (implied). σ = (28,285 − 28,490.5)/(0.5√56,981) = −205.5/119.4 = −1.72. Text: −1.71 ✓
- Non-void: n=621,964, f=0.4971. n_CW = 309,180. σ = (309,180 − 310,982)/(0.5√621,964) = −1802/394.3 = −4.57. Text: −4.59. Small discrepancy (rounding).

### P5-M9: Table VIII — three-algorithm summary
**Table VIII, p.12**
V2-REVOLVER: n_void=102,911, f=0.4986, σ=−0.88.
Check: σ = (f − 0.5) × 2 × √N = (−0.0014) × 2 × 320.8 = −0.898. Text: −0.88. Close enough.

V2-VIDE: n_void=81,354, f=0.4971, σ=−1.67.
Check: σ = (−0.0029) × 2 × 285.2 = −1.654. Text: −1.67. OK.

But note: §VIII D reports V2-REVOLVER catalog-native n_void = 86,276 with σ=−0.24. Table VIII reports n_void=102,911 with σ=−0.88. These are different statistics (sphere-approximation vs catalog-native). The abstract quotes σ=−0.24 on n=86,276, but Table VIII (the headline three-algorithm summary) uses the sphere-approximation 102,911. This inconsistency between abstract and table-of-record is confusing.

**Required fix:** Clarify in Table VIII or its caption which numbers feed the abstract.

### P5-M10: Phase 2 sweep — largest |σ| = 11.32 is presented as predicted, not measured
**§VII, p.8**
> "The largest single-cell |σ_from half| across the entire sweep is 11.32 (filament at Rs = 10, λth = 0, n = 3,696,152). This is the catalog-wide ∆fCW = −0.0026 monopole leaking through the largest sample bin and is predicted, not measured: σ_pred ≈ −0.0026 · 2√N ≈ −10 matches the observed −11.3 within order unity."

But n = 3,696,152 in the filament class is far larger than the 408,187 filament n in the headline table. Where does 3.7M come from? Is this the total V-Web filament population in DR1 (not just the chirality-relevant subsample)? If so, the sweep is computed on the full DESI sample, not the chirality-matched subsample — but then the σ comparison is not to the same statistic as the headline. The paper does not clearly disambiguate.

**Required fix:** Clarify whether Phase 2 sweep σ values are on chirality-relevant subsample or on full DR1 spectro catalog.

### P5-M11: Page 13, "(a null is not positive evidence; we report it as a controlled-sample non-detection)"
**§VIII B, p.11**
This caveat is correct but is placed in passing inside a paragraph that is otherwise dominated by celebratory framing ("largest matched-sample environmental-dependence test"). The disclaimer should be elevated.

### P5-M12: Footprint mask volume fraction inconsistency
**§IV A, p.3 and Fig. 1, p.4**
Text: "2,417,697 occupied → 3,150,086 in-mask (18.8% of the cube)"
Fig. 1 caption says volume fractions are "in-footprint."

3,150,086 / 256³ = 3,150,086 / 16,777,216 = 18.78% ✓
But: void 24.4%, wall 41.3%, filament 33.3%, cluster 1.0% — these are in-mask, which is 18.8% of cube. So absolute cube fractions are: void 4.6%, wall 7.8%, filament 6.2%, cluster 0.19%. OK, internally consistent if "in-footprint" means "of in-mask cells."

### P5-M13: Reference [11] arXiv ID format suspicious
**Bibliography, p.20**
> "preprint (2026), arXiv:2604.02463"

arXiv:2604.02463 — for a 2026 paper this would be valid if YYMM=2604 (April 2026), but the paper is dated June 2026. This appears to be a real arXiv ID. However, recommend verifying.

Similarly ref [12]: arXiv:2604.01456.

**Required fix:** Verify these arXiv IDs are correct.

### P5-M14: Reference [3] cited extensively but not actually available
**Throughout**
Reference [3] (Paper IV) is cited at least 15 times as the source of the chirality catalog, the ∆f_CW = −0.0026 monopole, the parity-mixture null at σ=0.43, etc. None of these values are independently verifiable.

### P5-M15: σ from "joint two-sample z-test" filament bright-vs-dark
**§VI A "filament-class within-class decomposition," p.7**
Bright n=416,701 σ=−2.80; Dark n=21,203 σ=+2.85. The abstract says |z| ≈ 3.4σ.

Joint test: z = (f_bright − f_dark)/√(σ²_bright + σ²_dark) where σ_i = 0.5/√N_i.
f_bright = 0.5 − 2.80 × 0.5/√416701 = 0.5 − 0.00217 = 0.49783
f_dark = 0.5 + 2.85 × 0.5/√21203 = 0.5 + 0.00978 = 0.50978

Δf = 0.50978 − 0.49783 = 0.01195
σ_combined ≈ √(0.5²/416701 + 0.5²/21203) = √(6e−7 + 1.18e−5) = √(1.24e−5) = 0.00352
z = 0.01195/0.00352 = 3.39 ≈ 3.4σ ✓

The 3.4σ value is correct, but the interpretation in the abstract is then deferred to "future Rubin/LSST + DESI DR2 follow-up." For a residual at 3.4σ in the largest sample of the paper, this deferment is inadequate.

### P5-M16: "On-DESI DESIVAST cross-classifier" framing — is it actually a different classifier?
**§V B, p.5**
The "primary robustness evidence is the on-DESI DESIVAST cross-classifier." But DESIVAST is a void catalog, not a four-class cosmic-web classifier (acknowledged in §VIII). So it's tested only on the void axis. The claim of cross-classifier robustness across all four classes is therefore not supported by DESIVAST.

### P5-M17: Headline says "no environment dependence above the sensitivity floor" but sensitivity floor not quantified
**Abstract, p.1**
> "the CW fraction shows no environment dependence above the sensitivity floor set by the Paper IV catalog-monopole offset of ∼0.2 pp"

What is the 95% upper limit on environment-dependent ∆f_CW per class? The paper never quotes this in a single line. This is the actual physical bound the paper produces, and it should be the headline number.

**Required fix:** Quote a single 95% upper limit on |∆f_CW^env − ∆f_CW^monopole| per class.

---

## MINOR Findings

### P5-Mi1: "8.47M" vs "8,474,531" — inconsistent precision in abstract
**Abstract, p.1**
"8,474,531-galaxy chirality catalog" vs §XII C "8.47 M chirality catalog" — fine, but should be consistent.

### P5-Mi2: Pie chart (Fig. 1) is filler
**Fig. 1, p.4**
The four volume fractions {0.244, 0.413, 0.333, 0.010} are stated in the text. The pie chart adds nothing. PRD figures should be load-bearing.

### P5-Mi3: Fig. 6 Mollweide projection has axis labels "0.0 to 1.0" on x and y — these are not sky coordinates
**Fig. 6, p.14**
The figure caption says "Mollweide projection" but the axes show 0.0–1.0 numerical values, not RA/Dec. The axis labels are wrong or vestigial from a normalized coordinate system.

**Required fix:** Either remove axis tick labels or label them properly as RA/Dec.

### P5-Mi4: Fig. 3 caption description does not match panel content
**Fig. 3, p.7**
Caption text describes "left/right" panels; the left panel y-axis range is 0.485–0.510 but the description says "tracks the monopole prediction within counting statistics." Hard to verify from the figure visually.

### P5-Mi5: "DESIVAST" sometimes parsed as "DESIVAST" sometimes as "DESI-VAST"
**Various**
Reference [13] uses "DESI-VAST" (with hyphen). Body uses "DESIVAST" without. Pick one.

### P5-Mi6: "Cautun et al. [7] geometric default λth = 0"
**§IV A, p.4**
Cautun 2014 in fact recommends λ_th ≈ 0.4 as a fiducial value based on calibration; λ_th = 0 is one specific choice. Citing Cautun as the "default" for λ_th = 0 is misleading.

**Required fix:** Verify the Cautun fiducial value and cite accurately.

### P5-Mi7: Footnote a on p.2 explains "V-Web" vs "T-Web" terminology — should be in main text or §IV
The disambiguation that this is actually T-Web (Hahn 2007), not V-Web (Hoffman 2012), is buried in a footnote. The title says "T-Web (Hahn 2007) Tidal-Tensor" so this acknowledgment is good, but the body persistently uses "V-Web" which is wrong nomenclature. The footnote admits this: "we retain the 'V-Web' label which is sometimes used loosely."

**Required fix:** Use "T-Web" throughout or "tidal-tensor classifier"; "V-Web" is incorrect terminology.

### P5-Mi8: Equation (1) σ_pred sign
"σ_pred = ∆f_CW / (0.5/√N) = 2 · ∆f_CW · √N"
With ∆f_CW = −0.0026, this gives negative σ_pred (correctly). But the abstract sometimes writes "σ_pred = −2∆f_CW√N" which would flip the sign for negative ∆f_CW. Confusing sign conventions throughout.

### P5-Mi9: HEALPix N_pix in Table V — 1054 for NSIDE=16
**Table V, p.8**
For NSIDE=16, full-sky N_pix = 12 × 16² = 3072. The 1054 reported must be in-footprint pixels. Should be noted.

### P5-Mi10: Reproducibility checklist references "companion data repository" but no URL provided
**p.19**
"All scripts and configuration files are available in the companion data repository." No URL or DOI given.

**Required fix:** Provide a Zenodo DOI or GitHub URL.

### P5-Mi11: "Deterministic seed: 20260515" — single seed cannot characterize stochastic variation
**p.19**
A single seed for 1000 MC permutations is fine, but other seed-dependent results should be cross-checked.

### P5-Mi12: Phase 2 sweep cell at R_s=10, λ_th=0 with |σ|=11.32 is in a region where the monopole prediction does fit, but the cell isn't reported as "in spec" anywhere
**§VII, p.8**
For completeness, the comparison should be tabulated.

### P5-Mi13: "Survey-edge artifact dominated at z ≲ 0.24" — acknowledged but not characterized
**Abstract**
The V-Web void at z ≲ 0.24 is acknowledged as survey-edge-dominated, which means the V-Web classifier in the void regime is broken. This is a serious methodological problem stated in the abstract and never properly resolved (only deferred to DESIVAST).

### P5-Mi14: ASTRA EDR cross-validation: "V-Web and ASTRA argmax disagree strongly on per-galaxy environment labels"
**§X, p.17**
Disagreement is so strong that "V-Web puts essentially the entire sample into filament (31.7%) and cluster (68.3%), with only 3 spirals total in the V-Web void + wall classes." This is a damning indictment of the V-Web classifier on the EDR overlap, dismissed as "the survey-shell density-grid systematic." If V-Web cannot reliably classify EDR-overlap galaxies, can it reliably classify DR1 galaxies? Not addressed.

### P5-Mi15: BGS bright vs dark contingency χ² = 4932 with p < 10⁻¹⁰⁰⁰
**§VI A d, p.8**
χ²=4932 with 3 dof gives a p-value that astronomical. Quoting "<10⁻¹⁰⁰⁰" is fine but the maximum class-to-overall deviation is 1.5 pp — meaningfully small. The contradiction between massive χ² significance and small physical effect should be noted: it's a sample-size artifact, the populations are simply too large for any small structural correlation to be hidden.

### P5-Mi16: "Range of CW fractions across the four classes never exceeds 0.22 percentage points"
**Abstract, p.1**
But Table II shows range = 0.0198 = 1.98 pp for the canonical run. The 0.22 pp comes from the Phase 2 sweep where the void class (n=428) is replaced by larger n. Conflation of canonical vs sweep ranges.

**Required fix:** Either report 1.98 pp for canonical OR explain why Phase 2 has tighter range despite being a "sweep."

---

## NITS

### P5-N1: "Paper IV [3]" cited as both [3] (in bibliography) and "Paper IV" in body — pick one citation style.

### P5-N2: Title is too long: "A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across 791,635 DR1 Matched Spirals" — this is title + abstract crammed together.

### P5-N3: Multiple "see §X" references without page numbers in the displayed text (LaTeX cross-refs not always rendering).

### P5-N4: "Hubify.com" email address for an "Independent Researcher" — fine, but the affiliation "Independent Researcher, Los Angeles, California, USA" combined with three companion papers all "in preparation" by the same author raises questions about the research program's maturity.

### P5-N5: Page 6, "These figures bracket parity" — colloquial language.

### P5-N6: "Within order-unity of observation" used as a precision statement (p.6). Order-unity ≠ confirmed agreement.

### P5-N7: Unicode characters (∼, ≳, ≲, ̄) sometimes render correctly, sometimes as raw escape codes in the PDF. Production check needed.

### P5-N8: "Galaxy positions used for the V-Web tidal-tensor estimate are in observed redshift space rather than corrected to real space" (§XIII, p.18) — this acknowledgment of RSD systematic is followed by a long hedge that effectively says "we don't quantify it." For a tidal-tensor classifier, RSD is not a minor concern.

---

## Page Count Assessment

The paper is 20 pages for a null result with one 3.4σ acknowledged residual that is dodged. PRD null results of this type typically warrant 8–12 pages.

**Recommended maximum: 10 pages.**

The following sections can be cut or moved to a supplementary repository:
- §VII Phase 2 sensitivity sweep (heatmap is one figure)
- §IX Additional cosmic-web cross-checks (Tempel comparison)
- §X ASTRA EDR cross-validation (acknowledged to be small sample with classifier disagreement)
- Appendix A (acknowledged broken EFT)

---

## Summary recommendation

**REJECT**

The paper is built on an unpublished, non-peer-reviewed companion catalog whose key calibration (∆f_CW = −0.0026 monopole offset) is the single quantity against which every "null" result in this paper is benchmarked. The headline "no environment dependence" claim is undermined by an explicitly acknowledged 3.4σ filament bright-vs-dark residual that the authors dispose of by re-anchoring on a different analysis path (DESIVAST at z ≤ 0.24) that cannot by construction test the residual. The EFT operator in Appendix A is admitted to be non-rotationally-invariant and non-gauge-invariant — fatal for any PRD theoretical content. The analysis path is openly post-hoc with no pre-registration, and the multiple-comparisons accounting is insufficient. Abstract is 4× too long and reports σ values from one null while interpreting under another. Recommend rejection. A resubmission would require: (1) Paper IV [3] published and refereed first; (2) the 3.4σ residual either confirmed or systematically eliminated, not dodged; (3) Appendix A removed or properly constructed; (4) pre-registered or family-wise-error-corrected significance statements; (5) reduction to ~10 pages.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report (Second Pass): P5 — Additional Findings

Re-examining the paper with fresh eyes against the specific failure modes listed yielded several substantial new issues missed on the first pass, including a flat numerical impossibility in the most-prominent residual structure result (filament bright/dark), a σ_pred computation that is internally inconsistent between two adjacent table rows, and a sample-mismatch in the Phase 2 robustness claim that materially weakens the headline robustness statement.

---

## ESSENTIAL Findings (NEW)

### P5-E8: Filament bright/dark sample sizes are arithmetically IMPOSSIBLE
**Abstract, p.2; §VI A "Filament-class within-class decomposition," p.7**

The paper reports:
> "filament bright (n=416,701) σ=−2.80 vs filament dark (n=21,203) σ=+2.85"

But:
- Table II (p.5): n_filament = **408,187** total.
- §VI A tracer-program stratification (p.7): n_dark = **14,782** total across all V-Web classes.

The filament-class subset cannot exceed the total filament class (416,701 + 21,203 = **437,904 > 408,187**), AND the filament dark subset cannot exceed total dark sample (**21,203 > 14,782**). Both are physical impossibilities.

This is exactly the 3.4σ residual the abstract flags as "the strongest single residual structure in the paper" and the load-bearing reason the primary path is moved to DESIVAST. The numbers underlying this 3.4σ claim do not add up.

The joint z-test computation IS internally consistent with n_bright=416,701, n_dark=21,203 — meaning the 3.4σ value follows from these specific numbers, which cannot be drawn from the headline filament sample.

**Required fix:** Either correct the filament bright/dark counts (and recompute the 3.4σ accordingly), or clarify what sample the bright/dark numbers come from. As written, the "strongest residual structure" is built on impossible counts.

### P5-E9: σ_pred(filament) = −3.16 is internally inconsistent with σ_pred(cluster) = −3.28 under the same ∆f_CW
**§VI A, p.6**

> "predicting σ_pred from ∆f_CW = −0.0026 gives σ_pred(filament) ≈ −3.16 and σ_pred(cluster) ≈ −3.28"

Recompute with same ∆f_CW = −0.0026:
- Filament: 2 × 0.0026 × √408,187 = 0.0052 × 638.9 = **−3.32** (text: −3.16, off by 5%)
- Cluster: 2 × 0.0026 × √397,505 = 0.0052 × 630.5 = **−3.28** (matches text)

The filament σ_pred = −3.16 implies ∆f_CW = −0.00247, while the cluster σ_pred = −3.28 implies ∆f_CW = −0.00260. Using a different ∆f_CW for two rows in the same sentence is incoherent. The error then propagates: the entire claim "we interpret these as the global monopole leaking through the larger-sample bins" depends on agreement between σ_pred and σ_obs.

**Required fix:** Recompute σ_pred(filament). Verify all σ_pred values throughout (§VIII E quotes σ_pred values that may also be affected).

---

## MAJOR Findings (NEW)

### P5-M18: Phase 2 sweep range (0.22 pp) is computed on a different sample than the headline range (1.98 pp)
**§VI A vs §VII, pp.5–8; Table II vs Table VI**

- Table II canonical: range across 4 V-Web classes = 0.5034 − 0.4836 = **1.98 pp** on 791,635 chirality-relevant spirals.
- Table VI canonical cell (Rs=25, λth=0): range = **0.165 pp**.
- Phase 2 §VII: filament n at Rs=10 is "3,696,152" — clearly the full ~14.6M DR1 spectro sample, not the chirality-relevant 791,635.

So the Phase 2 sweep is operating on the V-Web environment classification of the FULL DR1 spectroscopic catalog, while the headline is computed on the chirality-matched subsample. These are different statistics. The Phase 2 robustness claim ("max per-cell inter-class range across nine cells is 0.22 pp") therefore does NOT bound the headline 1.98 pp range under hyperparameter variation; it bounds a different sample's range.

**Required fix:** Re-run the Phase 2 sweep on the 791,635-spiral chirality-relevant subsample (not the 14.6M parent catalog). The current Phase 2 sweep does not robustly support the headline.

### P5-M19: V-Web void class is concentrated at z > 0.24, contradicting abstract characterization
**Abstract, p.1; §VIII A, p.10**

Abstract: "0.4836 (void; n=428, −0.68σ — survey-edge artifact dominated **at z ≲ 0.24**, see DESIVAST-anchored re-projection below)"

§VIII A: "Restricting the matched-spiral catalog to z ≤ 0.24 (the DESIVAST BGS limit) leaves only n=6 V-Web void-class spirals"

So 422 of 428 V-Web void spirals (98.6%) are at z > 0.24. The abstract's "artifact dominated at z ≲ 0.24" characterization addresses only 1.4% of the void class. The remaining 98.6% — the bulk of the void class — is uncharacterized. The paper provides no explanation for why the V-Web "void" classification is so heavily concentrated at high redshift (presumably this is a low-density survey-shell artifact at the far redshift limit, but this is not stated).

Critically, this also means the DESIVAST cross-check (z ≤ 0.24) tests only 1.4% of the V-Web void class it is meant to "anchor." The DESIVAST-anchored re-projection's 56,981 void spirals are an essentially disjoint sample from the V-Web 428 void spirals.

**Required fix:** Characterize the z > 0.24 V-Web void population (which is 99% of the void class). Clarify that DESIVAST does not directly cross-validate the V-Web void class spirals.

### P5-M20: Title "Three-Algorithm Test on 56,981 Void Spirals" is misleading
**Title, p.1; Table VIII, p.12**

The title implies a three-algorithm test on a sample of 56,981 void spirals. In fact:
- VoidFinder: n_void = 56,981
- V2-REVOLVER: n_void = 102,911 (sphere) or 86,276 (catalog-native)
- V2-VIDE: n_void = 81,354 (sphere) or 64,514 (catalog-native)

The three algorithms are run on different sample sizes spanning 56,981 to 102,911. "56,981" is only the VoidFinder count. A reader cannot reconstruct from the title alone whether the three algorithms are run on the same 56,981 spirals.

**Required fix:** Title should say something like "Test of ≳ 57k–103k Void Spirals" or "VoidFinder n=56,981 (cross-checked with V2-REVOLVER and V2-VIDE)."

### P5-M21: "Statistically indistinguishable" claim for ∆f_CW = 0.0007 lacks upper-limit quote
**§VIII B, p.11; Abstract**

The paper reports VoidFinder ∆f_CW = 0.0007 between void and non-void and calls it "statistically indistinguishable." At n_void = 56,981, the 95% CI on the void fCW is roughly ±0.0041; on ∆f_CW the 1σ ≈ 0.0042. So ∆f_CW = 0.0007 ± 0.0042 (1σ), giving a 95% upper bound of |∆f_CW| < 0.009 (0.9 pp).

This is the actual physical bound the paper produces on environment-dependent chirality. It is never stated as such. The 1.98 pp / 0.22 pp / 0.0007 numbers are scattered throughout but no single quoted line says "we constrain |∆f_CW^env| < X at 95% confidence."

**Required fix:** Quote a single 95% upper bound on environment-dependent ∆f_CW per V-Web class and per DESIVAST analysis.

### P5-M22: "Paper III" cited in §XII B but missing from bibliography
**§XII B, p.17; Bibliography p.20**

> "Paper II [4] and Paper III (both companion, not-yet-published works by the same author)"

Reference [4] is Paper II. There is no "Paper III" in the bibliography. References list [1]–[13] but no Paper III. Either a numbering error or missing reference.

**Required fix:** Add Paper III to bibliography or remove the citation.

### P5-M23: σ_obs − σ_pred residual procedure repeated in §VIII E without statistical justification
**§VIII E, p.12**

The naïve "residual = σ_obs − σ_pred" subtraction (already flagged in P5-M2) is repeated in §VIII E:
> "the observed −4.75σ leaves a residual of −1.55σ"
> "and the observed is −2.04σ, residual +0.60σ"
> "The asymmetry between the two bin residuals quantifies the sky-region-conditioned systematic"

This asymmetry argument is built on subtraction of two non-orthogonal σ statistics. Statistically the proper test is to compute (f_observed − f_predicted)/SE on the residual fraction, then compute significance. The current procedure conflates two different reference points and the "asymmetry" claim of 2.15σ across the two bins has no clear statistical interpretation.

**Required fix:** Replace with proper monopole-subtracted residual fraction significance.

### P5-M24: Reproducibility statement "Available in companion data repository" appears 7+ times without ever providing a URL
**§V, §VI A, §VII, §VIII F, §IX A, §X, Appendix B**

Every mention of the analysis driver scripts, sweep configs, sixteen-cell tables, Pearson cross-checks, and Phase 2 sweep CSVs points the reader to "the companion data repository." Appendix B says: "All scripts and configuration files are available in the companion data repository." No URL, no DOI, no GitHub link.

Combined with P5-E1 (Paper IV not available), this means the paper cannot be independently verified by the referee or reader at the time of submission.

**Required fix:** Provide a Zenodo DOI or GitHub URL before resubmission.

---

## MINOR Findings (NEW)

### P5-Mi12: §VIII C VoidFinder ∆f_CW sign description is unclear
**§VIII C, p.11**

> "V2-REVOLVER returns fCW^void = 0.4986 slightly above fCW^non-void = 0.4967 (the opposite sign of VoidFinder's small difference)"

VoidFinder: f^void = 0.4964 < f^non-void = 0.4971 (void lower). Table VIII reports ∆f_CW = +0.0007 (defined as f^non-void − f^void).
V2-REVOLVER: f^void = 0.4986 > f^non-void = 0.4967 (void higher). Table VIII reports ∆f_CW = −0.0019.

The "opposite sign" is correct under the (f^non-void − f^void) sign convention, but the body sentence is confusingly worded. Reader has to parse the table to verify.

### P5-Mi13: §VIII E sky-position residuals only "match" the systematic narrative at one of two bins
**§VIII E, p.12**

The 0-voids/pix bin (n=378,511): residual −1.55σ, interpreted as imaging-leg systematic.
The 6+ voids/pix bin (n=258,060): residual +0.60σ, "fully null."

But the 1-2 voids/pix bin (n=19,247, σ_obs = −0.43) and 3-5 voids/pix bin (n=23,127, σ_obs = −0.09) are not discussed in this residual framework. The selective presentation of only two bins' residuals is a small instance of cherry-picking.

### P5-Mi14: §IX A Tempel filament fCW concordance claim is 0.026 pp but two-decimal table differs
**§IX A, Table XI, p.14**

Table XI: Tempel filament_like fCW = 0.4982. Table II: V-Web filament fCW = 0.4980. Difference = 0.0002 = **0.02 pp**, not 0.026 pp as quoted.

Likely the underlying un-rounded values give 0.026 pp, but the table-rounded values give 0.02 pp. Either the table should show more decimals or the quoted value should be 0.02.

### P5-Mi15: Fig. 6 axes are normalized 0.0–1.0 coordinates, not labeled as Mollweide RA/Dec
**Fig. 6, p.14**

Caption says "Mollweide projection (equatorial coordinates)" but the axes show 0.0–1.0 tick labels. This is a vestigial artifact from matplotlib's coordinate system; the axes should either show RA/Dec or be removed entirely.

### P5-Mi16: §VI A footnote a (p.2) notes "V-Web" terminology is "loose" but body continues to use it everywhere
**Footnote a, p.2; throughout**

The footnote on p.2 acknowledges that the classifier used (Hahn 2007 tidal-tensor) is correctly called T-Web; V-Web (Hoffman 2012) requires velocity reconstruction not performed here. The title says "T-Web (Hahn 2007)" but the body uses "V-Web" hundreds of times. The footnote rescue ("we retain the 'V-Web' label which is sometimes used loosely") does not actually justify mis-naming the classifier throughout the body.

### P5-Mi17: §IX A "small_group" vs "wall" mapping logic is not defended
**§IX A, p.13**

The mapping {Tempel multiplicity ∈ [2,5)} → V-Web wall is a quite particular choice. Why not map small_group → filament_like? The mapping affects the per-bin σ comparisons and could in principle be tuned to maximize concordance. Without a pre-registered mapping rule, the comparison framework is post-hoc.

### P5-Mi18: §VII final paragraph cites Bonferroni-9 threshold |σ| = 3.02 but K = 9 × 4 classes = 36 effective bins
**§VII A, p.9**

> "the Bonferroni-9 (α = 0.05) threshold |σ|^Bonf_0.05,9 ≈ 3.02"

But the sweep tests 4 classes × 9 cells = 36 per-cell-class σ values. The proper multiplicity is K=36 (if class is independent) or K=9 (if reduced to per-cell maximum). The text uses K=9, which under-corrects.

### P5-Mi19: §VIII B uses "k=20-nearest-neighbour scipy.spatial.KDTree query" — but K=20 may be insufficient at hole boundary regions
**§VIII B, p.11**

A k=20 KDTree query for point-in-sphere test against 101,863 sphere centres assumes the 20 nearest sphere centres include the containing sphere. Near sphere overlaps and at high local sphere density, this may not be true. The completeness of the point-in-sphere assignment is not validated.

### P5-Mi20: §VIII A "minimum spiral-to-nearest-hole separations span 28.7–158.1 Mpc/h" — 6 numbers not given
**§VIII A, p.10**

Only the range is given; individual separations not provided. With n=6 the full distribution should be reportable.

### P5-Mi21: §X ASTRA per-galaxy disagreement framed as robustness; could equally be framed as classifier crisis
**§X, p.16–17**

V-Web and ASTRA argmax agree on essentially zero galaxies on the EDR overlap: V-Web puts ~100% into filament+cluster, while ASTRA distributes 11.9/31.7/35.2/21.3 across the four classes. The paper frames "both give the same null" as a robustness result, but it equally indicates that on this sample neither classifier is meaningful at the per-galaxy level. The framing privileges the null outcome.

### P5-Mi22: Acronym "ZWARN" used in abstract without expansion
**Abstract, p.1**

> "16.4 × 10⁶ ZWARN=0 input rows"

ZWARN is DESI redshift warning flag terminology; should be defined on first use (it is defined indirectly in §III B but not at abstract use).

### P5-Mi23: "Goldenrod" sample mass-scale not given
**Throughout**

The chirality catalog is described as "spirals" but no stellar-mass cut, magnitude cut beyond r ≤ 17.8, or selection-function characterization is given. The 791,635-spiral subsample is treated as homogeneous; whether DESIVAST voids preferentially exclude high-mass spirals (a selection effect) is not checked.

### P5-Mi24: §VIII F "the per-class n_CW values on the 812,793 superset sum to 404,111 giving fCW = 0.49719" — verify
**§VIII F, p.12**

404,111 / 812,793 = 0.49718 → 0.4972 ✓ matches text.
But Table II per-class n_CW sums: 207 + 3,359 + 203,261 + 197,284 = **404,111** ✓
And per-class n sums to 812,793 (verified earlier).

But the Table II per-class data are explicitly the 812,793 superset, NOT the 791,635 headline. The reader is told the headline is on 791,635 (Table I) but Table II's n's sum to 812,793. So Table II is on a different sample than headline — flagged in P5-M6 but more concerning given that the abstract repeatedly references "791,635 chirality-relevant spirals" while Table II is on 812,793.

**Required fix:** Either (a) restrict Table II to the 791,635 sample, or (b) clearly mark Table II as the 812,793 superset.

---

## Summary of Second-Pass Conclusion

The first-pass review identified the major structural problems. The second pass reveals that the **numerical foundations of the paper's flagship residual claim (3.4σ filament bright/dark sign-flip) are impossible** — the subset counts exceed the parent — and that the **Phase 2 robustness sweep is conducted on a different sample** than the headline (14.6M parent vs 791,635 chirality subsample), so it does not bound what it claims to bound. Combined with the σ_pred internal inconsistency between two adjacent table rows (P5-E9), the per-bin arithmetic of the paper does not hold up to checking.

Beyond the items in the first-pass review, P5-E8, P5-E9, P5-M18, and P5-M19 each individually warrant rejection or major revision. Together with the first-pass essential findings, the paper requires substantial rework before resubmission.