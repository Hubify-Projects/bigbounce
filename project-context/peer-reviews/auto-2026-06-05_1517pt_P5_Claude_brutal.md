# P5 auto-2026-06-05_1517pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (14874 chars)
**Wall time**: 470.8s

---

# Referee Report: Environmental Dependence of Spiral Chirality (Paper P5)

**Reviewer:** Brutal-honesty PRD referee
**Submission:** Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test...

---

## Overall assessment

This paper reports a **null result** on environmental dependence of spiral chirality, predicated on a **companion paper (Paper IV) that is explicitly stated to be "in preparation" and "not yet peer reviewed."** The entire methodological foundation — the chirality labels themselves, the catalog-monopole offset ΔfCW = −0.0026 that is subtracted throughout, the parity-conserving null benchmark — comes from an unpublished work by the same author. This is a fatal structural defect for a PRD submission. Beyond this, the paper is grossly inflated relative to its scientific content (a null result reported across ~20 pages with extensive duplicative cross-checks), and the headline statistical framing repeatedly slides between "null detection" and "controlled bound" without distinguishing them carefully.

I list specific findings below.

---

## ESSENTIAL findings

### P5-E1 — Foundation rests on an unpublished, non-peer-reviewed companion paper
**Section II, Abstract, throughout**
The chirality labels, the global parity null, AND the −0.0026 catalog-monopole offset that is subtracted from essentially every reported σ in this paper, all come from "Paper IV [3]," which Ref. [3] itself identifies as "in preparation; manuscript in preparation." The abstract acknowledges "companion work, not yet peer-reviewed." A PRD paper cannot have its entire signal-vs-null comparison anchored on an unpublished pipeline whose systematics the reader cannot independently evaluate. The catalog-monopole subtraction is the single most load-bearing operation in the paper — without it, the headline σ values are −2.61σ (filament) and −4.66σ (cluster), which would be detections, not nulls. **Required fix:** Paper IV must be publicly available, refereed, and citable before this paper can be evaluated, OR this paper must demonstrate the monopole independently from inputs available in this manuscript. The current chain of inference is non-reproducible.

### P5-E2 — Paper II (Ref. [4]) is also "in preparation" but cited as substantive context
**Section XII.B, Ref. [4]**
"Paper II [4] and Paper III (both companion, not-yet-published works by the same author) provide independent discriminators." Citing unpublished companion work as load-bearing context fails PRD standards.

### P5-E3 — Post-hoc designation of "primary" analysis path
**Section V.B (page 4-5)**
The author explicitly admits: "a single a priori preregistered analysis plan was not filed; the choice of which classifier to report as 'primary' is therefore made post-hoc." Given that the paper reports results from at least five environment classifiers (V-Web, Tempel FoF, DESIVAST VoidFinder, V2-REVOLVER, V2-VIDE, ASTRA, T-Web overlay) with multiple stratifications each, and the "primary" analysis is selected after seeing results, the multiplicity correction is not credible. The five-DESIVAST-estimator Bonferroni argument addresses only the primary path's internal multiplicity; it does not address the post-hoc selection of DESIVAST as primary from the larger family. **Required fix:** Either pre-register before public posting, or explicitly report the family-wise error rate across ALL classifiers and stratifications tested, with appropriate correction.

### P5-E4 — Sigma values from different null procedures juxtaposed without disclaimer
**Abstract, Table II, throughout**
The abstract reports per-class σ values (−2.61, −4.66, +0.55, −0.68) alongside DESIVAST ∆fCW = 0.0007 and label-shuffle p = 0.372 alongside HEALPix max-stat p-values, without distinguishing these statistics' incompatibility. The V-Web class σ values are computed against fCW = 0.5 (parity), but are then re-interpreted against the Paper IV monopole; meanwhile the DESIVAST ∆fCW null is a direct void-vs-non-void comparison. These are not directly comparable, but no disclaimer accompanies the juxtaposition in the abstract or in Table II.

### P5-E5 — The "−4.66σ cluster" headline number is not a real environmental signal but is presented as one
**Table II, page 5; Abstract**
The paper reports a cluster σ_from_half = −4.66 and then immediately notes this is "tracking" the −0.0026 catalog monopole, with σ_pred(cluster) ≈ −3.28. But the actual residual deviation |σ_obs − σ_pred| ≈ 1.38σ is not displayed in Table II. Reporting −4.66σ as the headline statistic without showing the monopole-residual in the same table is misleading; readers will quote −4.66σ. **Required fix:** Table II must show σ_from_half, σ_pred, AND |σ_obs − σ_pred| as three columns. The same applies to all per-class tables throughout.

### P5-E6 — Abstract arithmetic inconsistency: ∆fCW magnitude
**Abstract, page 1**
The abstract states the monopole offset is "∼0.2 pp" (systematic-dominated sensitivity floor) but then reports "∆fCW = −0.0026" elsewhere (i.e., 0.26 pp). The "0.2 pp" is then used as a benchmark for the Phase 2 sweep max range of 0.22 pp. So the claim "the per-cell range never exceeds 0.22 percentage points" is being implicitly compared against a 0.26 pp offset that has been rounded down to ~0.2 pp. This is sleight-of-hand. The Phase 2 max range (0.22 pp) actually EQUALS the catalog monopole magnitude (0.26 pp) to within counting noise.

### P5-E7 — Arithmetic check on density-quintile residual fails Bonferroni claim
**Section VI.C, Table III, page 6**
Table III reports quintile 3 has |σ_obs − σ_pred| = 1.87. The text states the Bonferroni-5 threshold at α=0.01 is |σ|_Bonf = 3.09. But the |σ_obs| = 3.94 BEFORE subtraction crosses neither bonferroni threshold cleanly when one considers the raw observed σ; the paper switches between raw and residual without clearly stating which is the test statistic. More problematically: the "Bonferroni-5" threshold is being applied to a residual, but the null distribution of the residual is not the standard normal — subtracting a fixed prediction from a binomial test statistic does not preserve the unit variance assumption embedded in Eq. (2). The threshold comparison as stated is not statistically valid.

### P5-E8 — Tracer-program contingency χ² = 4932 result undermines the headline interpretation
**Section VI.A.d, page 8**
The paper finds V-Web class and target program are NOT independent (p < 10⁻¹⁰⁰⁰). The author then acknowledges: "We therefore cannot assert V-Web class orthogonality to the target-program split, and the |z| ≈ 3.4σ bright-vs-dark sign-flip in the filament class is best read as a real residual structure that the current data do not allow us to cleanly partition." This is a 3.4σ residual the author cannot explain. The abstract buries this as a "diagnostic" while claiming a clean null. **This is the most significant finding in the paper and it is hedged into oblivion.** A 3.4σ tracer-conditional sign-flip in the dominant V-Web class is not a clean environmental null. Either it is real residual systematics (in which case the paper does not yet have a clean null for the V-Web headline), or it is real physics (in which case the headline is wrong). The paper cannot have it both ways.

### P5-E9 — DESIVAST "primary" path z ≤ 0.24 cannot test the V-Web filament/cluster headline
**Section VIII**
The DESIVAST analysis is restricted to z ≤ 0.24 and tests only void vs non-void. It does NOT test the V-Web cluster −4.66σ deviation that drives the headline σ-table. So designating DESIVAST as "primary" allows the author to avoid addressing the residual structure in the cluster class. The void-only DESIVAST result is consistent with parity, but this does not validate the V-Web tidal classifier's filament/cluster bins at z > 0.24, which carry the bright-vs-dark sign flip.

### P5-E10 — Length grossly disproportionate to result
This is a null result. The paper is 20 pages. The core finding can be reported in 6–8 pages. Sections IX.A (Tempel), IX.B (T-Web overlay), X (ASTRA), and the within-class density-stratified follow-up could be appendices or supplementary material. PRD expects compact reporting; this is closer to an internal technical report.

---

## MAJOR findings

### P5-M1 — Abstract claim "no environment dependence" overstates a controlled null
**Abstract**
The abstract states "no evidence for environment-dependent chirality beyond the catalog-monopole offset at current sensitivity." Given the unresolved 3.4σ tracer sign-flip in filament class, this language is too strong. A null detection conditioned on subtracting a systematic the author cannot fully characterize is not a clean "no evidence" statement.

### P5-M2 — V-Web void bin (n=428) is acknowledged to be uninformative but is still in the headline table
**Table II**
The void class with n=428 and σ = −0.68 has 95% binomial CI fCW ∈ [0.435, 0.530]. This bin constrains essentially nothing yet appears in the headline table on equal footing with the n ≈ 400,000 bins. The paper acknowledges this in the text but the table presentation is misleading.

### P5-M3 — RSD treatment is hand-waved
**Section XIII**
The RSD limitations section concludes: "we explicitly do not quantify the propagated uncertainty in the present paper: a full quantification ... requires the proper Zel'dovich-reconstructed re-classification, which we defer to a companion follow-up." The author then estimates the boundary-crossing population at ~2–4 × 10⁴ galaxies, distributed across class boundaries. This is the same order of magnitude as the per-class chirality deviations being interpreted. A PRD-level null requires this uncertainty to be propagated.

### P5-M4 — T-Web (Ref. [11]) cross-check uses an unrefereed concurrent paper
**Section IX.B**
Ref. [11] is described as "currently in submission to MNRAS; we do not treat it as peer-reviewed external validation but rather as a contemporaneous independent measurement." If you are not treating it as peer-reviewed external validation, why is it in the paper? It either supports or it doesn't.

### P5-M5 — ASTRA cross-check has poor per-galaxy agreement
**Section X**
The V-Web and ASTRA argmax classifiers disagree massively on per-galaxy environment labels: V-Web puts 100% of the EDR overlap into filament+cluster (with only 3 spirals in void+wall), while ASTRA puts 11.9% in void. The conclusion that "both classifiers recover the same chirality null" is trivially true when both classifiers agree the null holds for ANY partition of the data, but it is NOT independent cross-validation of the environmental claim because the two classifiers are fundamentally disagreeing about what "environment" means. The author acknowledges this but still lists ASTRA as a robustness cross-check.

### P5-M6 — Bibliography issues
- Ref. [3] (Paper IV): "in preparation" — cannot serve as primary reference
- Ref. [4] (Paper II): "in preparation"
- Ref. [11]: arXiv:2604.02463 — implausible arXiv identifier format (arXiv IDs follow YYMM.NNNNN; "2604" implies April 2026 — verify this isn't a placeholder)
- Ref. [12]: arXiv:2604.01456 — same concern
- These two arXiv IDs being from "month 04" of "year 26" need to be verified, especially given the paper's dated "June 4, 2026"

### P5-M7 — "Two complementary nulls" claim in Section V is weakened by reality
**Section V**
The paper claims to run "(i) a label-shuffle permutation" and "(ii) a position-shuffle." Neither addresses the real systematics issue: the −0.0026 monopole is a CLASSIFIER-residual bias, and neither shuffle null tests against classifier bias. The shuffles test the null hypothesis "fCW = 0.5 per bin," which is not the relevant null.

### P5-M8 — Cluster within-class density stratification interpretation is strained
**Section VI.D, Table IV**
The cluster Q3 quartile returns σ = −0.37 ("statistically null") while Q1 returns −3.07 and Q2 returns −3.42. The author attributes this to "boundary-misclassification leakage from filament," but provides no quantitative model for why boundary leakage would manifest as σ = −3.07 in low-density cluster cells AND σ = −2.46 in high-density cluster cells while leaving Q3 alone. This is post-hoc rationalization.

### P5-M9 — Sample-size dropdown 791,635 → 812,793 unexplained
**Section VIII.F**
"f^P5_CW = 0.4972 (−5.07σ on n = 812,793 env-labeled spirals — the 21,158-row excess (2.7%) over the 791,635-spiral headline subsample..." Why does the env-labeled sample have 21,158 MORE spirals than the chirality-relevant sample? The reverse should be true (every chirality spiral has an env-label since V-Web is run on all spectro galaxies). Either there's a definition switch or there's a data-flow inconsistency.

### P5-M10 — Appendix A toy EFT mapping does not belong in a PRD null-result paper
**Appendix A**
The author admits the operator is "a toy parametrization introduced in this work, inspired by but not derived from the cited parity-violating-gravity literature," that it is "not contained in either Alexander & Yunes [1] ... or Lue-Wang-Kamionkowski [2]," that it "breaks rotational invariance," that it is "not manifestly gauge invariant," and that "we have not carried out [the gauge-invariant] construction." A rotational-non-invariant, gauge-non-invariant, ad-hoc toy operator that does not appear in the literature should not be in a PRD appendix. This is filler.

### P5-M11 — Figure 1 (pie chart) is filler
**Figure 1, page 4**
A pie chart of four volume fractions is information already conveyed in two sentences of text. Wastes space.

---

## MINOR findings

### P5-Mi1 — Date inconsistency
The paper is dated "June 4, 2026" but cites work from "2026 April" (Ref. [11]) and the [REVIEWER METADATA] block (correctly excluded) suggests a 2026 review round. The dating implies a future paper, which is unusual for current submission. This may be intentional preprint-style dating, but should be verified.

### P5-Mi2 — Figure 2 axis: y-axis range cut off at parity could be misread
**Figure 2**
The y-axis spans roughly 0.42–0.53; the void class CI extends down to ~0.43. A reader scanning quickly may mistake the void bin's wide CI as a real low-CW outlier.

### P5-Mi3 — Figure 3 right panel: axis label overlap
**Figure 3**
The x-axis labels show "Q1, Q2, Q3, Q4, Q5" with bin-edge values overlaid that are nearly illegible. Caption claims "k=5 NN density proxy"; the displayed quintile edges are huge integers — units?

### P5-Mi4 — Figure 4 HEALPix Mollweide projection — caption claim
**Figure 4**
Caption asserts "no coherent large-scale structure beyond random pixel-level scatter." This is a judgment, not a fit. A power-spectrum or angular-correlation estimator across the pixel σ map would actually test this; the visual inspection cannot.

### P5-Mi5 — Section VI.E reports max-|σ|_obs = 4.13 at NSIDE=32 with p = 0.135
**Table V**
A 4.13σ deviation surviving as p = 0.135 only via look-elsewhere correction is interesting but the abstract claim "none reach 3σ after look-elsewhere correction" is true only with look-elsewhere correction — the raw deviation IS above 3σ. The abstract should disclose both raw and LEE-corrected.

### P5-Mi6 — "Eq. (1)" σ_pred formula presentation
**Eq. (1), page 4**
σ_pred = ΔfCW / (0.5/√N) = 2·ΔfCW·√N
With ΔfCW = −0.0026 and N = 397,505 (cluster): σ_pred = 2 × (−0.0026) × 630.5 = −3.28 ✓
With N = 408,187 (filament): σ_pred = 2 × (−0.0026) × 638.9 = −3.32 ✓ (paper states "−3.16" — minor inconsistency: the paper computes σ_pred(filament) ≈ −3.16, but the correct value is −3.32)

**Recompute:** 2 × 0.0026 × √408187 = 2 × 0.0026 × 638.89 = 3.32. The paper says −3.16 in Section VI.A. **Arithmetic error.**

### P5-Mi7 — Density-quintile arithmetic
**Table III**
Q1: fCW = 0.4976, N = 158,327 → nCW = 78,784.5 → σ = (78784.5 − 79163.5)/√(158327·0.25) = −379/198.95 = −1.91
Paper reports −1.94. Within rounding.

Q3: fCW = 0.4950, N = 158,327 → σ = (0.4950 − 0.5)·2·√158327 = −0.005 × 795.8 = −3.98
Paper reports −3.94. Within rounding.

### P5-Mi8 — Table I row count check
Matched primary 2,349,908 vs after dedup 2,232,212: 117,696 duplicates removed (5.0%). Chirality-relevant 791,635; CW 393,592 + CCW 398,043 = 791,635 ✓. CW/total = 0.4972, not the 0.4974 quoted from Paper IV. The 0.4974 is from the parent Paper IV catalog; the matched subsample is 0.4972. Should be acknowledged consistently.

### P5-Mi9 — Section VI.A's "σ_pred(cluster) ≈ −3.28" then headline shows −4.66
**Section VI.A**
The author writes "predicting σ_pred from ΔfCW = −0.0026 gives σ_pred(filament) ≈ −3.16 and σ_pred(cluster) ≈ −3.28, both within order-unity of observation." The observed cluster is −4.66; |residual| = 1.38σ. The "within order-unity" phrasing minimizes the fact that the residual is large enough to potentially reflect real structure (and indeed the bright/dark sign-flip suggests it does).

### P5-Mi10 — "BGS pairwise velocity dispersion" σ_v ≲ 400 km/s
**Section XIII**
The typical pairwise velocity dispersion in groups/clusters is closer to 500–700 km/s; 400 km/s is at the lower end. The "≲ 400" is selectively quoted to make σ_v/aH small.

### P5-Mi11 — Section VIII.A "0/6" check has trivial statistical power
The 0/6 V-Web void disagreement check is presented as evidence but a sample of 6 cannot constrain anything meaningfully. Reporting this as a "n = 6 per-galaxy classifier-disagreement check" in the abstract overstates its weight.

---

## NITS

### P5-N1 — "σ_from half" italicization and spacing inconsistent throughout
### P5-N2 — "ApJ 982, 38 (2025)" with "Phys. Rev. D" target submission — formatting style choices
### P5-N3 — "DESIVAST [13]" hyphenation: "three-algorithm" appears as both "three-algorithm" and "three algorithm"
### P5-N4 — Multiple occurrences of "the the" and double articles — copyedit pass needed
### P5-N5 — "p < 10^−1000" is meaningless and should be replaced with "p ≪ 10^−10" or similar; floating-point underflow is not a useful statistic
### P5-N6 — Use of "headline" 20+ times is informal for PRD
### P5-N7 — Figure 5 sensitivity heat-map values would be clearer as a labeled table than a 3×3 grid
### P5-N8 — Inconsistent use of "Mpc/h" vs "h⁻¹ Mpc"

---

## What the paper would need to become acceptable

1. Paper IV must be published, refereed, and citable. The catalog-monopole subtraction must be either independently derived in this paper or imported from a public, peer-reviewed source.
2. The 3.4σ filament bright-vs-dark sign-flip must be resolved or honestly headlined as an unresolved residual systematic.
3. Length cut to ~8 pages, with Tempel/ASTRA/T-Web cross-checks moved to supplementary material.
4. Tables must report σ_obs, σ_pred, AND residuals.
5. Abstract must accurately reflect the controlled-null nature of the result, not state "no evidence" given known unresolved systematics.
6. RSD propagation must be quantitative.
7. Appendix A toy EFT mapping should be removed or substantially developed (gauge-invariant version).
8. Post-hoc multiplicity from multi-classifier testing must be properly addressed.

---

## Summary recommendation

**REJECT**

This paper cannot be accepted by PRD in its current form. The most fundamental issue is that the entire analytical framework — chirality labels, parity-null benchmark, and the −0.26 pp catalog-monopole offset that is subtracted from every reported deviation — comes from an explicitly unpublished, non-peer-reviewed companion paper by the same author. PRD cannot accept a paper whose central inferential machinery is non-citable. Beyond this structural defect, the headline "null" conceals an unresolved 3.4σ tracer-program-conditioned sign-flip in the dominant V-Web class that the author acknowledges cannot be cleanly partitioned between systematics and physics, the "primary" analysis path is post-hoc designated after seeing results from at least seven classifiers, the abstract overstates a controlled-null result as "no evidence for environment dependence," and the paper is grossly inflated at 20 pages for what is at core a single null result. The author should resubmit once Paper IV is publicly refereed, the filament sign-flip is honestly addressed in the abstract, the manuscript is cut to ~8 pages, and all per-class tables report both raw σ and monopole-residual σ as separate columns.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Findings on Second Pass

My initial review missed substantial arithmetic and internal-consistency issues. A second careful pass found multiple numerical contradictions, including several that touch the headline tables directly. The most significant new findings:

---

## NEW ESSENTIAL findings

### P5-E11 — Table II row counts contradict the text label
**Table II, Section VI.A, Abstract**
Table II lists per-class n: 428 + 6,673 + 408,187 + 397,505 = **812,793**. But §VI.A states "Table II reports CW fraction by cosmic-web class on the 791,635 chirality-relevant matched spirals." The abstract makes the same claim. Sum of nCW across the table: 207 + 3,359 + 203,261 + 197,284 = **404,111**, which exceeds Table I's CW total of 393,592 by 10,519. §VIII.F belatedly discloses that Table II actually uses an enlarged 812,793-spiral sample with a "relaxed env-label confidence" filter — but Table II's caption, §VI.A's headline sentence, the abstract, and §XV (Conclusions) all describe this as the "791,635 chirality-relevant matched spirals" result. **The headline number-of-galaxies claim in the abstract is false.**

### P5-E12 — Filament bright + dark counts EXCEED filament total
**Section VI.A.c**
The paper reports "filament bright (n = 416,701) σ = −2.80 vs filament dark (n = 21,203) σ = +2.85." Sum = 437,904. But Table II reports filament total n = 408,187. The bright sub-sample alone (416,701) already exceeds the parent class. This is impossible arithmetic. Cross-check: total BGS-bright reported in §VI.A.d is 775,760 across all classes; cluster bright (derived from cluster_dark = 4,234 and bright-ratio 0.989) would be ~380,742; filament bright + cluster bright = 797,443 > 775,760 (total bright). The bright/dark decomposition is **numerically inconsistent with itself and with Table II.** Given that the 3.4σ joint z-test in the abstract is computed from these numbers, the central caveat of the paper rests on internally inconsistent counts.

### P5-E13 — §XI claims directly contradict §VI.A.d's tracer decomposition
**Section XI, Section VI.A.d**
§XI states "target-class split (BGS vs. LRG-ELG-QSO) with BGS-only CW fraction within ±0.001 of LRG-ELG-QSO." But §VI.A.d explicitly reports BGS-bright fCW = 0.4970 and LRG/ELG/QSO-dark fCW = 0.5051 — a difference of **0.0081 (8.1× the ±0.001 claim)**. Additionally, §XI claims "No test produces a > 3σ residual after Paper IV-monopole correction," but the abstract, §VI.A.c, and §VI.A.d all feature a **3.4σ filament bright-vs-dark sign-flip** as the major unresolved residual. §XI's systematics summary is flatly incompatible with the paper's own findings reported elsewhere.

### P5-E14 — Internal inconsistency on cross-class range: 0.2 pp vs 1.98 pp
**Section XII.C vs Section XV / Table II**
§XII.C: "The present paper's per-environment CW fractions sit at ∼ 0.497 with range ∼ 0.2 percentage points across the four V-Web classes." §XV (Conclusions) and Table II: "{0.484, 0.503, 0.498, 0.496}, a range of 1.98 percentage points." These are off by **a factor of ~10**. The 0.2 pp figure is being used in §XII.C to argue against the Shamir 2022 2–4% asymmetry; if the actual range is 1.98 pp, the comparison is much weaker. This is either a stale number or a deliberate choice to quote the high-n subset only, but the discrepancy is not flagged.

### P5-E15 — Per-pixel residual std=1.184 misinterpreted as "consistent with shot noise"
**Section VIII.F**
The paper reports for the per-pixel σ_vs_monopole distribution at NSIDE=32 over 1,821 valid pixels: "mean +0.020, std 1.184, skewness +0.044, and excess kurtosis +0.825. The unit standard deviation (within ∼18%, consistent with finite-pixel sample-size fluctuation), zero skewness, and modest positive kurtosis are all consistent with a pure shot-noise residual around the P4-monopole."

This statistical interpretation is wrong:
- **Std error of sample std** on n=1,821 normal samples ≈ 1/√(2·1820) = 0.0166. The observed std=1.184 is (1.184−1)/0.0166 = **11σ above unity**, not "within ∼18%." This implies substantial excess variance beyond shot-noise (extra variance σ²_extra ≈ 0.40, an extra ~0.63σ-equivalent per-pixel systematic).
- **Std error of excess kurtosis** on n=1,821 ≈ √(24/1821) = 0.115. The observed excess kurtosis 0.825 is **7.2σ from zero** — not "modest," and inconsistent with a normal/shot-noise residual.

The claim that the per-pixel distribution is "consistent with pure shot-noise around the P4-monopole" is contradicted by the very statistics quoted. There IS extra per-pixel structure; the paper's "single-test demonstration" that V-Web class σ values are sample-size projections of the P4 monopole is unfounded as stated.

### P5-E16 — Phase 2 sweep filament n=3,696,152 exceeds matched-spiral catalog size
**Section VII**
"The largest single-cell |σ_from half| across the entire sweep is 11.32 (filament at Rs = 10, λth = 0, n = 3,696,152)." But the chirality-relevant matched catalog is 791,635 spirals (Table I), and even the looser env-labeled set is 812,793 (§VIII.F). A V-Web filament class with n = 3.7 million spirals on which fCW = 0.4971 is computed is **impossible** — there are only ~800k chirality labels available. Either the n value is wrong, or σ = −11.32 is computed against a different N, or the entire Phase 2 cell is mislabeled. The σ_pred ≈ −10 quoted does match 2·0.0026·√3.7M, so the formula is being applied to a sample size that doesn't exist in our chirality data.

---

## NEW MAJOR findings

### P5-M12 — Arithmetic error in σ_pred(filament) = −3.16
**Section VI.A**
The paper computes σ_pred(filament) = 2·(−0.0026)·√408,187 = **−3.32**, not −3.16 as quoted. σ_pred(cluster) = −3.28 is correct. The filament value is wrong and propagates into the "within order-unity of observation" justification for treating the filament σ = −2.61 as monopole-only. Residual after monopole subtraction: filament |σ_obs − σ_pred| = |−2.61 − (−3.32)| = 0.71, not 0.55. Minor but indicative of unchecked arithmetic.

### P5-M13 — VI.A.d max bright-fraction deviation is misstated
**Section VI.A.d**
Per-class ratios {0.981, 0.962, 0.966, 0.989} against overall 0.978. Deviations: +0.003, −0.016, −0.012, +0.011. Max |deviation| = **1.6 pp** (wall class), not 1.5 pp as the paper states. Minor but indicates limited arithmetic verification.

### P5-M14 — Bright-ratio decomposition is internally inconsistent
**Section VI.A.c, VI.A.d**
The bright/dark ratios in §VI.A.d (0.981/0.962/0.966/0.989) cannot be reconciled with the bright/dark COUNT decomposition in §VI.A.c. From the ratios: filament bright fraction = 0.966, so filament_dark/filament_total = 0.034. With filament_total = 408,187, filament_dark = 13,879. But §VI.A.c reports filament_dark = 21,203. These imply different filament totals (and §VI.A.c's bright count exceeds any sensible total — see P5-E12). The two subsections cannot both be correct.

### P5-M15 — Bright-ratio decomposition contradicts BGS-bright total
**Section VI.A.d**
Total BGS-bright in §VI.A.d is 775,760. If cluster bright/dark ratio is 0.989 with n_cluster_dark = 4,234, cluster_bright ≈ 380,742; if filament bright = 416,701 (as claimed in §VI.A.c), the two classes together account for 797,443 bright spirals — exceeding the total bright sample size (775,760). The decomposition is over-determined and inconsistent.

### P5-M16 — Catalog-wide monopole stated as 0.4974 but matched sample is 0.4972
**Section II, Section VIII.F**
§II quotes "CW fraction of 0.4974 ± 0.000279" from Paper IV as the global parity result. Computing from Table I: 393,592/791,635 = 0.49719 (i.e. 0.4972). §VIII.F acknowledges f^P5_CW = 0.4972 on the env-labeled subsample but does not flag that this differs from the 0.4974 reference value used throughout, even though the difference (0.0002) is at the same scale as the per-class residuals being interpreted.

### P5-M17 — Kurtosis claim "consistent with pure shot-noise" is statistically false
**Section VIII.F** (separately from P5-E15)
The text reads: "modest positive kurtosis are all consistent with a pure shot-noise residual." Excess kurtosis 0.825 with SE 0.115 on n=1,821 is a 7.2σ deviation from normal. This is not "modest" by any standard definition; positive kurtosis at this significance indicates heavy tails inconsistent with the Gaussian shot-noise null the paper invokes.

### P5-M18 — Section IV.B ¯ρ_cell = 4.64 galaxies/cell — check on density assumptions
**Section IV.B**
2,417,697 occupied cells from 14,622,283 galaxies → 6.05 galaxies/cell. Paper reports 4.64 galaxies/cell, which is 14,622,283 / 3,150,086 in-mask cells = 4.64 ✓. But this means the V-Web overdensity field is normalized against the dilated in-mask volume rather than the occupied volume. This is a methodological choice that affects which cells classify as voids (the dilated mask absorbs ~23% additional empty cells, lowering ¯ρ and pushing more genuinely empty cells toward δ = 0). This is the mechanism producing the +8–18 pp V-Web void excess mentioned in §IX.B but is not analyzed quantitatively.

### P5-M19 — Tempel "filament_like_vs_filament 0.026 pp" understates classifier-definition mismatch
**Section IX.A**
The 0.026 pp concordance is presented as a tight cross-validation. But the Tempel filament_like class includes only FoF richness 5–20 multiplicity, whereas V-Web filament is a continuous tidal-tensor class with 33.3% volume fraction. The two classifiers' samples differ by ~30× in n and have entirely different selection functions. A 0.026 pp agreement on two such differently-defined samples likely reflects both being close to the Paper IV monopole (which they should be, by construction) rather than measuring a common physical filamentary chirality field.

### P5-M20 — Coverage fraction inconsistency NSIDE 16 vs 32
**Table V, §VI.E**
NSIDE=16 occupied: 1,054 of 3,072 = 34.3% sky coverage. NSIDE=32 occupied: 3,303 of 12,288 = 26.9%. Higher-NSIDE coverage fraction is LOWER, which is unusual — sub-dividing pixels at higher NSIDE should preserve coverage fraction if a threshold isn't being applied. The paper does not specify the per-pixel galaxy-count threshold used to mark a pixel "occupied" at each NSIDE. Without this, the LEE correction K-value is under-specified.

---

## NEW MINOR findings

### P5-Mi12 — Section III.D 99th-percentile separation 0.30″ matches caption but separation distribution not shown
The "p99 separation = 0.30″" claim with no histogram makes the systematics-radius sweep ({0.5, 1, 2, 3, 5}″) producing only a ~4% band hard to verify visually.

### P5-Mi13 — DESIVAST VoidFinder hole counts: 89,003 + 12,860 = 101,863 ✓; "3,765 maximal voids" stated but the per-galaxy classification uses the 101,863 hole-spheres
The paper conflates "maximal voids" (3,765) and "interior hole spheres" (101,863) at several points without distinguishing which serves which test. The 0/6 test uses 101,863 holes; the HEALPix stratification uses 3,765 maximal voids; both are introduced as "DESIVAST."

### P5-Mi14 — Section VIII.B states k=20 KDTree query "sufficient given the 24 Mpc/h maximum hole radius"
But §VIII.E quotes maximal-void effective radii 10–32 Mpc/h. 24 Mpc/h vs 32 Mpc/h: a small inconsistency in the stated max radius; the membership test could miss matches at large radii if k=20 nearest neighbors is the threshold.

### P5-Mi15 — Section VIII.C V2-VIDE max effective radius "55.9 Mpc/h" much larger than the "24 Mpc/h" stated in §VIII.B
Confirms the inconsistency above; V2-VIDE specifically extends to 55.9 Mpc/h, so the k=20-NN sufficiency argument cannot apply to that algorithm at the largest void radii.

### P5-Mi16 — Section VI.E label-shuffle p-values at NSIDE=16 quoted as 0.607 in Table V vs 0.61 in abstract
Minor rounding inconsistency.

### P5-Mi17 — Section VI.A.d "n_cluster_dark = 4,234" not derivable from displayed ratios
With cluster bright ratio 0.989 and total cluster 397,505, cluster_dark expected = 397,505 × 0.011 = 4,373, not 4,234 as the paper reports. The implied bright ratio from {4,234 dark, 397,505 total} is 0.9893 ≈ 0.989 ✓ to 3 decimals, but 4,234 vs 4,373 indicates the bright fraction is 0.98935 vs 0.98890 — small discrepancy from rounding propagation.

### P5-Mi18 — Section XV conclusion lists range "1.98 percentage points" but §XII.C says "∼0.2 percentage points"
Same factor-10 error, repeated. (See P5-E14.)

---

## NEW NITS

### P5-N9 — Eq (1) presentation: σ_pred = ΔfCW / (0.5/√N) = 2·ΔfCW·√N — algebraically correct, but the 0.5 in denominator is unmotivated to the reader (it's the binomial std/√N at fCW=0.5)
### P5-N10 — "p < 10⁻¹⁰⁰⁰" (§VI.A.d) is meaningless floating-point underflow, repeated from P5-N5
### P5-N11 — V-Web volume fraction "{0.244, 0.413, 0.333, 0.010}" appears with sums 1.000 but the abstract describes "wall+filament fraction (74.5%)" — sum should be 0.413 + 0.333 = 0.746 = 74.6%. Minor rounding.
### P5-N12 — Section VIII.A: "VoidFinder NGC/SGC FITS files ... 89,003 + 12,860 = 101,863 interior hole spheres comprising the 3,765 maximal voids" — the phrasing "comprising" obscures the ~27:1 hole-to-maximal-void ratio; a clearer statement would help
### P5-N13 — "k=5 NN" density-quintile axis labels in Fig 3 are illegible (also flagged in original review as P5-Mi3)

---

## Revised bottom line

The second pass identified several **disqualifying arithmetic errors** that should have been caught in the original review:

1. **Table II's per-class n's sum to 812,793, not the 791,635 claimed in the abstract.**
2. **Filament bright + dark counts in §VI.A.c exceed the filament total.** The 3.4σ caveat in the abstract is computed from internally inconsistent counts.
3. **§XI's systematics summary makes claims (BGS within ±0.001 of LRG-ELG-QSO; no >3σ residuals) that are directly contradicted by §VI.A.d.** This is not a hedge or interpretation difference; the two sections quote incompatible numbers.
4. **§XII.C claims a 0.2 pp cross-class range; §XV and Table II show 1.98 pp.** The discussion's comparison to Shamir 2022 is wrong by an order of magnitude.
5. **§VIII.F misinterprets a 7σ-significant kurtosis excess as "consistent with shot-noise."**
6. **Phase 2 sweep cites a filament n = 3,696,152 that exceeds the matched chirality catalog size.**

Combined with the issues flagged in the first pass — particularly the unpublished-companion-paper foundation, the post-hoc primary-classifier designation, and the unresolved 3.4σ tracer sign-flip — the paper has **structural foundations that fail PRD reproducibility standards, AND demonstrable arithmetic errors in the headline tables and tracer decomposition**. My recommendation strengthens to **REJECT**, with the additional recommendation that the author rebuild the per-class count bookkeeping from scratch and reconcile the Table II / VI.A.c / VI.A.d / VIII.F sample-size accounting before any resubmission to any journal.