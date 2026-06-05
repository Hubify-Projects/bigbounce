# P5 R10v3 — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K
**Wall time**: 176.9s

---

# Referee Report — P5 "Environmental Dependence of Spiral Chirality"

## Overall assessment

This is a 20-page paper whose central scientific claim is a null result: spiral chirality is statistically independent of cosmic-web environment in DESI DR1. The headline null is plausibly correct, but the manuscript is severely bloated relative to the content, leans heavily on a not-yet-peer-reviewed companion paper ("Paper IV") for its central monopole-subtraction interpretation, repeatedly conflates sigma values from heterogeneous null procedures, and contains a number of arithmetic and presentation problems. The "primary path" designation of the DESIVAST analysis is acknowledged as post-hoc and undermines the headline framing of the abstract, which leads with V-Web.

---

## ESSENTIAL findings

### P5-E1 — Dependence on unpublished companion paper for the core interpretation
**Pages 1–2, 4, 12.** Throughout the paper the interpretation of every large-|σ| value depends on subtracting a "catalog-monopole offset ∆fCW = −0.0026" reported in Paper IV [3], which is explicitly described as "companion work, not yet peer-reviewed" and "in preparation." The entire significance framework (Eq. 1, §V; §VIII F monopole-residual analysis) is built on this number. A PRD submission cannot have its central interpretive scaffolding rest on an unreleased, non-peer-reviewed manuscript by the same author. **Fix:** either submit Paper IV first (and cite the accepted version), or carry the ∆fCW value as a free nuisance parameter fitted from this paper's own data with propagated uncertainty.

### P5-E2 — Post-hoc designation of "primary" analysis
**Page 5, §V B.** The paper explicitly admits: "a single a priori pre-registered analysis plan was not filed; the choice of which classifier to report as 'primary' is therefore made post-hoc." The DESIVAST analysis is then nominated as primary because it produces the cleanest null. This is textbook garden-of-forking-paths after the fact. The title and abstract emphasize "DESIVAST Three-Algorithm Test," but the body's headline Table II is V-Web. **Fix:** the paper must either (a) restructure the abstract and title to remove "primary" language entirely, presenting all classifiers as co-equal cross-checks with a unified multiplicity correction over all classifiers and stratifications, or (b) re-derive significance budgets that include the post-hoc selection penalty.

### P5-E3 — Heterogeneous σ values juxtaposed without "not directly comparable" qualifiers
**Abstract page 1; §VI, §VIII, §IX.** The abstract reports σ values from at least four distinct procedures side-by-side: σ_from_half against the binomial-0.5 null (V-Web classes), σ_from_half on DESIVAST classes (where the null is also 0.5 not f_CW^P5), |σ_obs − σ_pred| residuals after monopole subtraction (density quintiles), and label-shuffle p-values (sky pixels). The reader cannot tell at a glance which σ is referenced to which null. For example "0.4963 (cluster; n=397,505, −4.66σ)" is a σ against parity, but elsewhere "−1.11" is quoted as the same cluster bin "after monopole subtraction." **Fix:** every σ in the abstract and tables must carry an explicit null label (e.g. "σ_parity", "σ_monopole") at every occurrence.

### P5-E4 — Abstract arithmetic: Pearson correlation r = +0.006
**Page 2 / Figure 6 caption (page 14).** The abstract reports "r = +0.006 (p = 0.88)" for the per-pixel maximal-void vs chirality σ correlation, n=727 pixels. For r=0.006 with n=727, the standard z = r·√(n−2) ≈ 0.006·26.94 ≈ 0.16, giving p ≈ 0.87 — consistent. But this is presented as evidence of environmental independence; r = 0.006 is barely distinguishable from "no test was run" given that the σ values themselves carry the catalog-monopole offset. **Fix:** clarify whether the correlation was performed on monopole-subtracted σ or raw σ; if raw, the test is dominated by the same selection-function structure already identified, and the r=0.006 result is not informative.

### P5-E5 — Inconsistent population counts in §VIII F
**Page 12, §VIII F.** The text reports "f_CW^P5 = 0.4972 (−5.07σ on n = 812,793 env-labeled spirals)" and then explains a "21,158-row excess (2.7%) over the 791,635-spiral headline subsample." 791,635 + 21,158 = 812,793 ✓. However the text then says the same monopole is "−5.00σ on the 791,635-spiral chirality-relevant sample" and gives ∆f_CW^P5 ≈ −0.0028. Let me check: σ = 2·0.0028·√791,635 = 2·0.0028·889.7 ≈ 4.98 ≈ 5.00 ✓. But for the 812,793 case: σ = 2·∆f·√812,793 should give −5.07 → ∆f ≈ 2.81×10⁻³, not 2.8×10⁻³ exactly. The two are consistent. **However**, the more serious issue is that the reader is told two different superset definitions exist (791,635 vs 812,793) and the 21,158-row excess is given a hand-wavy justification ("relaxed env-label confidence used by the cosmic-web pipeline but excluded from the headline by a stricter env-class-uncertainty filter") that is never quantitatively defined elsewhere in the paper. **Fix:** define the two filters explicitly and reconcile in a single table.

### P5-E6 — Table II σ values: recomputation discrepancy for cluster
**Page 5, Table II.** For cluster: n=397,505, n_CW=197,284, f_CW=0.4963. σ = (197284 − 0.5·397505)/(0.5·√397505) = (197284 − 198752.5)/(315.24) = −1468.5/315.24 = **−4.658**. Quoted: −4.66 ✓.
For filament: n=408,187, n_CW=203,261, f = 0.49796... quoted 0.4980 ✓. σ = (203261 − 204093.5)/(0.5·√408187) = −832.5/319.45 = **−2.606**. Quoted: −2.61 ✓.
For wall: n=6,673, n_CW=3,359, f = 0.50337; σ = (3359 − 3336.5)/(0.5·81.69) = 22.5/40.84 = **+0.551**. Quoted +0.55 ✓.
For void: n=428, n_CW=207, f = 0.4836; σ = (207 − 214)/(0.5·20.69) = −7/10.34 = **−0.677**. Quoted −0.68 ✓.
**Arithmetic in Table II checks out.** No fix needed here, but document that the audit was performed (this finding is downgraded — flagging because the audit was non-trivial, not because numbers fail).

### P5-E7 — V-Web volume fractions: arithmetic inconsistency
**Page 4, Fig. 1 caption.** Reports {void 0.244, wall 0.413, filament 0.333, cluster 0.010}. Sum = 1.000 ✓. But text says "wall+filament fraction (74.5%)" — actual sum = 0.413 + 0.333 = 0.746 = 74.6%, not 74.5%. Minor but the kind of arithmetic slop that erodes trust. **Fix:** correct to 74.6% or round consistently.

### P5-E8 — Tracer-program bright fCW: arithmetic check
**Page 7, §VI D point b.** Bright: n=775,760, fCW=0.4970, claimed σ=−5.25. σ = 2·(0.4970−0.5)·√775,760 = 2·(−0.003)·880.77 = **−5.285**. Quoted −5.25. Close but rounded; mild. **More importantly:** 775,760 + 14,782 + 875 + 218 = **791,635** ✓ matches the chirality-relevant sample. OK.

But: "bright (BGS-dominated; n = 775,760)" returns σ=−5.25 while the catalog as a whole returns σ ≈ −5.00 to −5.07. If bright dominates 98% of the sample and shows a stronger σ than the whole, the dark sample's claimed σ=+1.25 cannot offset this in a weighted average unless arithmetic is consistent. Let me check: ∆f from bright at σ=−5.25 ⇒ ∆f = −0.00298. ∆f from dark at σ=+1.25 ⇒ ∆f = +0.00514. Weighted ∆f = (775760·(−0.00298) + 14782·(+0.00514) + 875·0.0143 + 218·(−0.0046))/791635 = (−2312 + 76 + 13 − 1)/791635 = −2224/791635 = −0.00281. Then σ_whole = 2·(−0.00281)·√791635 = −5.00. **Consistent.** Good.

### P5-E9 — Contingency χ² claim
**Page 8, §VI D point d.** Claims χ² = 4932 with 3 d.o.f., p < 10⁻¹⁰⁰⁰. For χ² ≈ 4932 with 3 dof, log10(p) is roughly −χ²/(2·ln10) ≈ −1071. p < 10⁻¹⁰⁰⁰ is therefore numerically plausible. **However**, presenting a contingency test with χ²=4932 from total n=811,609 as physically meaningful is misleading: with that sample size, any selection-effect correlation will produce astronomical χ². The "max class-to-overall bright-fraction deviation 1.5 pp" is the physically meaningful number, and the abstract's emphasis on the χ² value is the wrong statistic to feature. **Fix:** demote the χ² value or supplement with effect-size measure (Cramér's V, which for χ²=4932, n=811k, k=2: V = √(4932/811609) ≈ 0.078 — small effect).

### P5-E10 — Filament dark sample arithmetic
**Page 7, §VI D point c.** Filament dark: n=21,203, σ=+2.85. ∆f = +2.85/(2·√21203) = +2.85/291.22 = +0.00979 ⇒ f_CW = 0.5098. Filament bright: n=416,701, σ=−2.80 ⇒ ∆f = −0.00217 ⇒ f_CW = 0.4978. **But** filament headline n=408,187 (Table II), not 416,701. The 8,514-row mismatch between "filament class" in the tracer-stratification and "filament class" in the headline is unexplained. Either two different filament-class definitions are being used or the bright+dark+backup+other split doesn't conserve filament n. **Fix:** reconcile the filament class population across §VI A and §VI D.

### P5-E11 — Bonferroni threshold arithmetic
**Page 4, Eq. (2) + page 5 text.** "For K = 5 density quintiles at α = 0.01, Eq. (2) gives |σ|^Bonf_{0.01,5} ≈ 3.09". Two-sided Bonferroni: per-test α/K = 0.002; z = √2 erfc⁻¹(0.002) = Φ⁻¹(0.999) = 3.090. ✓
"For K = 1054 NSIDE-16 HEALPix pixels at α=0.05, |σ|^Bonf_{0.05,1054} ≈ 4.05". α/K = 4.74e-5; z = Φ⁻¹(1 − 2.37e-5) ≈ 4.07. Quoted 4.05 — close, acceptable.
"Bonferroni-4 |σ|=2.498 threshold at α=0.05" (page 15). α/K = 0.0125, z = Φ⁻¹(0.99375) = 2.498 ✓.
"Bonferroni-4 |σ|=3.02 at α=0.01" (page 6). α/K=0.0025; z = Φ⁻¹(0.99875) = **3.023**. Quoted 3.02 ✓. But also quoted "Bonferroni-4 |σ|=2.50" on page 6 ("|σ|<2 are uniformly small ... Bonferroni-4 |σ|=2.50 threshold at α=0.05") — this is the same threshold elsewhere quoted as 2.498. Inconsistent rounding. Trivial.

### P5-E12 — Page count vs scientific content
The paper is 20 pages plus references for a null result with a single load-bearing measurement (∆f_CW ≲ 0.002 across void/non-void). This is a 6–8 page paper at most. The proliferation of sections (V-Web, Phase 2 sweep, Tempel, ASTRA, T-Web overlay, DESIVAST 3-algorithm, catalog-native V2, maximal-void HEALPix, P4-monopole-residual analysis, tracer-program decomposition, within-class density quartiles, redshift quartiles, EFT toy mapping) creates an illusion of depth that is actually a sequence of consistency cross-checks of the same null. **Fix:** cut to 8–10 pages; relegate Phase 2 sensitivity sweep, Tempel cross-validation, ASTRA EDR, T-Web overlay, and Appendix A to a single appendix or to the companion data repository.

---

## MAJOR findings

### P5-M1 — Title vs body emphasis mismatch
The title is "A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals", framing DESIVAST as the primary test. But §VI A is labeled "Cosmic-web environment (headline)" and presents V-Web first. The body order should follow the post-hoc-declared primary path, which would put §VIII (DESIVAST) before §VI (V-Web). **Fix:** reorder sections to match the primary/secondary declaration, or rewrite the title.

### P5-M2 — Appendix A EFT mapping is unjustified and should be removed
**Pages 19.** The "toy EFT mapping" introduces an operator ℒ_parity ⊃ g_φ (∇_i φ)(∇_i ρ/ρ_bg)(L̂·ẑ) that the appendix admits is (a) not derived from any cited reference, (b) rotationally non-invariant via the explicit ẑ factor, (c) not gauge-invariant. This is a contribution-free addition that risks being miscited. **Fix:** remove Appendix A entirely, or reduce to a single sentence stating that bounds on ∆f_CW could in principle constrain late-time parity-violating operators, deferred to future work.

### P5-M3 — RSD discussion handwaves the key step
**Pages 10, 18.** The DESIVAST RSD-immunity argument relies on "σ_v/(aH) ≲ 5 Mpc/h at z ≲ 0.24 is several times smaller than the void effective radii." But DESIVAST voids span effective radii 10–32 Mpc/h, and 5 Mpc/h compared to a 10 Mpc/h void is only a factor of 2, not "several times smaller." The smallest voids are RSD-comparable to their own radii. **Fix:** restrict the RSD-immunity claim to voids with R_eff > 15 Mpc/h or compute the actual void-radius distribution and stratify by it.

### P5-M4 — V-Web Cartesian mapping is incorrect for surveys
**Page 3, §IV A step 3.** The Cartesian map (X, Y, Z) = χ(cos δ cos α, cos δ sin α, sin δ) is standard. But the V-Web is then computed on a 256³ cube spanning 6,634 Mpc/h, with the survey footprint occupying only 18.8% of the cube. The vast majority of the volume is empty mask cells, and the Gaussian smoothing is done in periodic Fourier space across this empty volume. This creates known edge artifacts that the paper acknowledges (the +8–18 pp void-fraction excess vs T-Web). **Fix:** the headline V-Web result should not rest on a single classifier with this known mask bias; either re-run on a properly masked grid or downweight this section.

### P5-M5 — Phase 2 sweep claim of robustness
**Page 8, §VII.** The Phase 2 sweep "confirms the result is invariant to V-Web hyperparameter choices." But the sweep keeps the same 14.6M parent sample and the same chirality labels — the variations are only in smoothing scale and eigenvalue threshold, which redistribute the same galaxies across the four class labels. The catalog monopole is conserved by construction. **The sweep does not test what the paper claims it tests.** A real robustness check would vary the chirality labels or the parent sample. **Fix:** acknowledge the sweep only tests sensitivity to class assignment, not to the underlying chirality signal.

### P5-M6 — Figure 5 has unreadable cell labels
**Page 10, Fig. 5.** Cell labels include "0.220" written over a yellow background — but several cells have similar values and the discrimination ratio between cells (0.05 to 0.22 pp) is well below counting-statistics floors stated in the same section. The heat-map is essentially noise visualized as if it were structure. **Fix:** caption should explicitly state "all cells consistent with shot noise" or remove the figure.

### P5-M7 — Figure 4 Mollweide
**Page 9, Fig. 4.** The figure caption claims "no coherent large-scale structure beyond random pixel-level scatter," but the figure is small, the color scale runs only −4.5 to +4.5σ, and the survey-mask outline dominates visually. The reader cannot independently verify the "no coherent structure" claim. **Fix:** provide a difference map between observed and label-shuffle null, or quantify a coherence statistic (Cℓ at low ℓ on the binarized map).

### P5-M8 — Figure 6 axes labeling
**Page 14, Fig. 6.** Both Mollweide panels are labeled with axes ranging "0.0 to 1.0" on x and y, which is not the natural coordinate for a Mollweide projection. The colorbar labels are partially overlapping ("Chirality σ_{from half} per pixel (n_spirals ≥ 200, z ≤ 0.24)"). **Fix:** clean up axes, remove the 0–1 numerical labels, place colorbars below each panel cleanly.

### P5-M9 — Tempel concordance metric is a soft test
**Page 14, §IX A.** The 0.026 pp filament-class concordance is described as the load-bearing concordance metric, but two classifiers operating on the same galaxies and both biased by the same Paper IV monopole will trivially agree on fCW at the class level if the class definitions overlap substantially. This is not an independent cross-validation, it is a consistency check that both classifiers preserve the catalog monopole. **Fix:** state explicitly that the Tempel-V-Web concordance is dominated by shared classifier-monopole bias and is not an independent test.

### P5-M10 — ASTRA cross-check explicitly admits classifier disagreement
**Page 16–17, §X.** "ASTRA argmax distributes the 25,186 spirals as 11.9% void / 31.7% sheet / 35.2% filament / 21.3% knot, while V-Web puts essentially the entire sample into filament (31.7%) and cluster (68.3%), with only 3 spirals total in the V-Web void + wall classes." This is a catastrophic per-galaxy classification disagreement on the EDR overlap, yet the paper claims the chirality null is "recovered identically by both." The reason is trivial: both classifiers carry the same Paper IV monopole, so any class-averaged fCW will sit near 0.4974 regardless of which galaxies are in which class. This is not robustness; it is a tautology. **Fix:** acknowledge that the ASTRA cross-check is uninformative given the per-galaxy disagreement, and remove the "strong robustness result" language.

### P5-M11 — Section IX B reads as advocacy
**Page 15.** The paper extensively justifies why the V-Web/T-Web volume-fraction discrepancy (8–18 pp in void class!) is "consistent with the survey-shell systematic" rather than a classifier mismatch. The void fraction differing by up to 18 pp between two ostensibly equivalent classifiers should be flagged as a serious problem, not explained away. **Fix:** report the V-Web/T-Web discrepancy as a limitation that bounds the trustworthiness of the V-Web headline.

### P5-M12 — "Range of 1.98 percentage points" in the conclusion
**Page 19, §XV.** The conclusion states "{0.484, 0.503, 0.498, 0.496}, a range of 1.98 percentage points dominated by counting statistics." The 1.98 pp range is the void-vs-wall difference: 0.503 − 0.484 = 0.019. But the void bin has 95% CI [0.435, 0.530] (per §VI A): the CI alone is ~10 pp wide. Describing "1.98 pp" as the range without immediately stating the void CI is misleading. **Fix:** state the range alongside the void-class CI in the same sentence.

### P5-M13 — Reference [11] is described as "in submission to MNRAS" and used as concordance evidence
**Page 15.** The text states "Ref. [11] is currently in submission to MNRAS; we do not treat it as peer-reviewed external validation but rather as a contemporaneous independent measurement." But the section then proceeds to invoke its agreement as supporting the V-Web result. Either it is an independent validation or it is not. **Fix:** remove the T-Web comparison or move it to a discussion-only paragraph with explicit "preprint, not load-bearing" labeling at every quantitative claim.

### P5-M14 — Abstract claim "DESI Data Release 1 redshifts provide the environmental anchor"
**Page 1, abstract.** DR1 redshifts do not "provide the environmental anchor" — they provide the galaxy positions from which the V-Web tidal-tensor is computed. The V-Web is the anchor; DR1 is the input. Phrasing inflates DR1's role. **Fix:** rewrite.

### P5-M15 — Abstract void σ value
**Page 1.** "void; n = 428, −0.68σ — survey-edge artifact dominated at z ≲ 0.24, see DESIVAST-anchored re-projection below". Calling a −0.68σ deviation on n=428 a "survey-edge artifact" is overclaiming — at this sample size the deviation is simply consistent with noise, and the interpretation as a survey-edge artifact is borrowed from the DESIVAST cross-match. **Fix:** describe the void σ as statistically null at this n; defer artifact discussion to the appropriate section.

---

## MINOR findings

### P5-Mi1 — Abstract is far too long
The abstract spans roughly two pages of dense prose and includes a sub-section labeled "Robustness." This is unusable as an abstract. **Fix:** cut to ≤ 350 words.

### P5-Mi2 — Sigma value reporting precision
Throughout, σ values are reported to two decimal places (−4.66, −2.61, +0.55) while corresponding f_CW values are reported to four decimals (0.4980). The σ precision implies a precision in nCW that the four-decimal fCW does not support consistently.

### P5-Mi3 — "Catalog-monopole offset of ∼0.2 pp" in abstract
Abstract states sensitivity floor "∼0.2 pp" but the Paper IV offset is quoted as 0.0026 = 0.26 pp. These differ by a factor of ~1.3.

### P5-Mi4 — Table III σ_pred uniformity
Table III lists σ_pred = −2.07 for all five quintiles, derived from ∆f_CW = −0.0026 at N=158,327. Check: 2·0.0026·√158327 = 2·0.0026·397.9 = **2.069** ✓. Good.

### P5-Mi5 — Figure 7 collision with text
**Page 16, Fig. 7.** The right panel has text "← filament_like 0.4982" overlapping data points and an arrow that doesn't render cleanly. Also "|f_CW^{V-Web} − f_CW^{Tempel}| = 0.026 pp" annotation in the left panel is partially obscured.

### P5-Mi6 — V2-REVOLVER catalog double-counting
**Page 11, Table VIII.** Lists "n_void^catalog = 1,992 effective voids" in text but the table reports n_void = 102,911 matched spirals in V2-REVOLVER voids. The text says 1,992 effective voids in §VIII C — but earlier (§VIII) said "420 with V2-REVOLVER." 420 vs 1,992 vs 295 vs 1,478 — inconsistent void counts for the same algorithms across pages. **Fix.**

### P5-Mi7 — Paper IV reference is itself self-referential
**Reference [3].** "in preparation; manuscript in preparation" is repeated twice in a single reference. Edit.

### P5-Mi8 — "(supporting, not load-bearing)" parenthetical
**Page 14.** The parenthetical appears verbatim multiple times across §IX A and the figure caption (Fig. 7). Once is enough.

### P5-Mi9 — Date "June 4, 2026"
Future date; presumably the intended submission date. Make sure this is consistent with arXiv stamping.

### P5-Mi10 — "Per-pixel signed σ_from_half ... σ range −3.45 to +3.48"
**Page 14, Fig. 6 caption.** Two sigfigs of range from a 1,496-pixel scan; this is just the empirical max from shot noise. Not informative.

### P5-Mi11 — Two different "Bonferroni-4" thresholds
Page 6 text uses both 2.50 (α=0.05) and 3.02 (α=0.01) within consecutive paragraphs without consistent flagging of which α is in use.

### P5-Mi12 — Confidence-threshold "p_cls_eq^max ∈ {0.4, 0.5, ...}"
**Page 17, §XI.** Notation never defined.

### P5-Mi13 — "0/6 V-Web 'void' spirals fall inside any DESIVAST hole"
**Pages 1, 10.** n=6 is too small to support the abstract-level claim of "survey-edge artifact dominated." Move to limitations.

### P5-Mi14 — Mixing pp and σ in robustness summaries
"|∆fCW| < 0.002" (a fraction) and "|σvoid| < 2" (a normalized deviation) are quoted as equivalent robustness statements. They are not: ∆f and σ scale differently with N.

### P5-Mi15 — Abstract closing on "≳ 5× larger" cluster-dark sample
**Page 2.** Future-data appeal in the abstract is inappropriate.

### P5-Mi16 — Inconsistent dash style
em-dashes, en-dashes, and hyphens used interchangeably ("survey-edge", "BGS-selection-function- conditioned" with stray spaces).

### P5-Mi17 — "p < 10⁻¹⁰⁰⁰" reporting
χ² values reported with absurd-precision p-values (page 8) suggest a `scipy.stats.chi2.sf` underflow; report as "p < 10⁻³⁰⁰" or similar, with explicit numerical floor.

### P5-Mi18 — DESIVAST primary cross-check "n = 56,981"
The title's "56,981 Void Spirals" figure is from VoidFinder only. The three-algorithm DESIVAST result has different per-algorithm n. Title should clarify "VoidFinder" or report a range.

### P5-Mi19 — Pearson r reporting n=727
**Page 14, Fig. 6 caption.** The body text (page 13) says n_pix^both = 727, but the figure caption says the bottom panel has 1,496 valid pixels. These are different subsamples; clarify which corresponds to the r=0.006 statistic.

### P5-Mi20 — Section VIII F "DESIVAST primary analysis (§VIII)" self-reference
Cross-references inside §VIII pointing back to §VIII.

---

## NITs

### P5-N1 — Author affiliation
"Independent Researcher, Los Angeles, California, USA" — atypical for PRD; acceptable but unusual for a 20-page methods paper.

### P5-N2 — "Bamfai/galaxy-chirality-catalog"
HuggingFace path. Make sure this is anonymized for double-blind review if applicable.

### P5-N3 — Conflicting notation "σ_from half" vs "σ from half"
With and without subscript italics across the paper.

### P5-N4 — "≳ 25 Mpc/h V-Web smoothing scale" appears in abstract, intro, discussion, conclusions
Repeated verbatim 4+ times.

### P5-N5 — Equation (1)
"σ_pred = ∆f_CW / (0.5/√N) = 2 · ∆f_CW · √N" — algebraically correct but the sign convention (negative ∆f gives negative σ) should be explicit.

### P5-N6 — Footer
No journal info, no PRD-specific formatting.

### P5-N7 — References
[11] and [12] both arXiv:2604.* — appears to be future-dated arXiv IDs. Verify.

### P5-N8 — "5σ-class P4 monopole signature"
Page 11. "5σ-class" is a nonstandard descriptor.

### P5-N9 — "∼ 9.5σ catalog-level monopole reported in Paper IV"
Page 12. The Paper IV monopole was quoted in the intro at "0.4974 ± 0.000279", and 0.0026/0.000279 ≈ 9.3 — close to 9.5 but not exact. Reconcile.

### P5-N10 — Conclusion section is 4 paragraphs for a one-sentence finding
Could be reduced to two sentences.

---

## Summary recommendation

**REJECT**

This is a 20-page paper reporting a null result whose interpretive scaffolding depends critically on an unpublished, non-peer-reviewed companion paper by the same author; whose "primary" analysis path is explicitly admitted to be selected post-hoc from among many; whose abstract conflates sigma values from incompatible null procedures throughout; whose central "robustness" cross-checks (Phase 2 sweep, ASTRA classifier, Tempel FoF) are either tautological consequences of the shared monopole, or operate on disjoint per-galaxy classifications that make their agreement on class-averaged f_CW meaningless; and whose V-Web headline rests on a classifier whose own internal volume fractions disagree with an independent classifier by up to 18 pp in the void class. The actual scientific content — DESIVAST void chirality consistent with non-void at ∆f_CW = 0.0007 — could be reported credibly in a Letter of 4–6 pages once Paper IV is published. As submitted, the manuscript is not in a state where the headline claims can be evaluated as significance statements rather than as scaled projections of an unpublished catalog-wide bias. Resubmit after Paper IV is accepted, after the abstract is rewritten to be ≤ 350 words with consistent null labeling, after the body is cut to ≤ 10 pages, and after the primary/secondary declaration is either pre-registered or replaced by a unified multiplicity budget.