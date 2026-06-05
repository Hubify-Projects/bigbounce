# P5 R10v3p1 — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (12784 chars)
**Wall time**: 474.3s

---

# Referee Report — P5 (R10v3p1)
**Manuscript:** Environmental Dependence of Spiral Chirality (DESIVAST 3-algorithm + V-Web)
**Submitted to:** Physical Review D

---

## Overview

A 20-page null-result paper testing whether spiral-galaxy chirality depends on cosmic-web environment, anchored on the author's own (unpublished, "Paper IV") chirality catalog cross-matched to DESI DR1. The central scientific claim — "no environment dependence above a known classifier-monopole floor" — is in principle a clean and publishable null. However, on careful audit the paper contains **multiple arithmetic inconsistencies that the body itself does not reconcile**, several of which propagate into the abstract. The bookkeeping is in such poor shape that I cannot recommend acceptance in the current form.

---

## ESSENTIAL FINDINGS

### P5-E1 — Bright/Dark dark-sample totals are arithmetically impossible
**Page 7, §VI D and abstract (page 2).** §VI D states the *total* matched-spiral catalog dark (LRG/ELG/QSO) count is **n_dark = 14,782**. Yet:

- §VI A / abstract: filament-class **dark n = 21,203**
- Abstract: cluster-class **dark n = 4,234**

These two V-Web classes alone require ≥ 25,437 dark galaxies — **exceeding the global dark total by ~10,600**. Adding wall+void dark makes this worse. This is not a rounding issue; it is internally inconsistent by ~70%.

The abstract's headline " |z| ≈ 3.4σ filament bright-vs-dark sign-flip" depends on the **n=21,203** value being correct. Until this is reconciled, the 3.4σ "real residual structure" diagnostic cannot be evaluated. **Fix:** recompute and publish the V-Web × target-program contingency table from the parquet artifact and reconcile *all* numbers in §VI A, §VI D, and the abstract.

### P5-E2 — Filament bright-only n exceeds filament total
**Page 7, §VI A.** "filament bright (n = **416,701**) σ = −2.80 vs filament dark (n = 21,203)."

Table II (page 5) gives filament total **n = 408,187**. A bright-only subsample cannot be larger than the full class. Sum bright+dark = 437,904 ≠ 408,187. **Fix:** correct, or identify which class definition each number refers to and rewrite.

### P5-E3 — Phase 2 sweep cell reports n > parent chirality-relevant sample
**Page 8, §VII.** "The largest single-cell |σ_from half| across the entire sweep is 11.32 (filament at R_s = 10, λ_th = 0, **n = 3,696,152**)."

The chirality-relevant matched-spiral catalog is 791,635 (abstract) / 812,793 (Table II sum). No V-Web class can have n = 3.7 × 10⁶ spirals at *any* (R_s, λ_th); that count exceeds the catalog by ~4.5×. The σ_pred ≈ −10 reconciliation argument therefore evaluates a number that cannot exist. **Fix:** explain what sample this 3.7M refers to, or correct the count.

### P5-E4 — Headline n=791,635 vs. Table II sum 812,793
**Pages 1, 5 (Table II), 12 (§VIII F).** The abstract and §VI A both describe Table II as "Per-class CW fractions on the 791,635 chirality-relevant spirals," but the column sums to **428 + 6,673 + 408,187 + 397,505 = 812,793**. §VIII F buries an explanation ("21,158-row excess") only on page 12, and the figure-2 caption explicitly says "on n = 791,635 chirality-relevant matched spirals." A reader sees a 2.7% discrepancy that is unflagged at the point of presentation and tagged with **two different sample definitions used interchangeably**. **Fix:** present Table II on a single, declared sample; if a relaxed env-confidence filter is used for the per-class n's, label that explicitly in the caption.

### P5-E5 — DESIVAST void counts inconsistent between §VIII opening and §VIII C
**Page 10:** "1,461 interior voids with VoidFinder, **420** with V2-REVOLVER, and **295** with V2-VIDE."
**Page 11, §VIII C:** "V2-REVOLVER (n_catalog_void = **1,992** effective voids …) and V2-VIDE (n_catalog_void = **1,478**)."

420 vs 1,992 (≈ 4.7×) and 295 vs 1,478 (≈ 5.0×). These are not reconciled in text. If "interior voids" vs "effective voids" mean different things, the paper must define both terms and explain which one enters which calculation. As written it reads as raw inconsistency.

### P5-E6 — σ_pred(filament) arithmetic
**Page 5, §VI A.** "σ_pred(filament) ≈ −3.16."
Using the formula in Eq. (1) at ∆f_CW = −0.0026 and n = 408,187: 2 × 0.0026 × √408187 = **3.32**, not 3.16. The cluster value (3.28) is correct. Minor in isolation but undermines the "within order-unity" defense of the monopole interpretation, which is the load-bearing argument of the headline.

### P5-E7 — Two different "catalog monopole" values used interchangeably
**Page 12, §VIII F.** The paper switches between ∆f_CW^P4 = −0.0026 (Paper IV) and ∆f_CW^P5 = −0.0028 (8% larger on the matched subsample) without a stable convention. The Table X residuals are computed against f_CW^P5 = 0.4972, while the headline σ values throughout the body are referenced against ∆f_CW^P4 = −0.0026. The "within |σ_vs monopole| < 1.15" claim therefore quietly uses a different reference than the |σ_obs − σ_pred| residual calculation in §VI C and §VII A. **Fix:** declare one canonical reference value and propagate it consistently, or explicitly tabulate both at every juxtaposition.

### P5-E8 — Heavy reliance on companion papers not yet peer reviewed
**Pages 1–2, 17, 19, refs [3,4].** Paper IV supplies the ∆f_CW = −0.0026 monopole that is invoked at every "σ_pred" calculation in this paper. Paper IV is "in preparation; manuscript in preparation." The entire interpretive scaffolding — that filament/cluster −2.6σ/−4.7σ deviations are "the catalog monopole" rather than environmental signals — is supplied by an unpublished work by the same author. PRD cannot accept a paper whose load-bearing systematic is sourced exclusively from a manuscript not yet submitted. **Fix:** Either (a) hold this paper until Paper IV is at least on arXiv/submitted, or (b) derive the monopole from public data inside this paper.

### P5-E9 — Sigma values from different null procedures juxtaposed without comparability disclaimer
**Abstract; §VI A; §VI D; §VIII.** σ_from half (binomial-z vs 0.5), σ_pred (monopole-bias predicted z), |σ_obs − σ_pred| (residual), |σ_vs monopole| (residual from f_CW^P5), and HEALPix max-stat label-shuffle p-values are all reported side-by-side with no explicit "not directly comparable" qualifier at each juxtaposition. The reader is left to parse which σ should be Bonferroni-corrected against which null. Per the brief, this alone is flagged ESSENTIAL.

---

## MAJOR FINDINGS

### P5-M1 — DESIVAST sphere-approximation introduces uncontrolled bias the paper acknowledges then ignores
§VIII D notes the catalog-native V2 zone definition gives smaller |σ| than the sphere-approximation (e.g. V2-REVOLVER: −0.24 vs −0.88). The abstract leads with the **sphere-approximation** ∆f_CW = 0.0007 for VoidFinder but uses the **catalog-native** σ = −0.24 for V2-REVOLVER as the "cleanest" result. Cherry-picking the cleaner method per algorithm overstates internal robustness.

### P5-M2 — "Primary path" designation is post-hoc by author admission
§V B explicitly states "a single a priori pre-registered analysis plan was not filed; the choice of which classifier to report as 'primary' is therefore made post-hoc." This is honest but the abstract still reads as if the DESIVAST primary path were an a-priori-chosen statistic. Given the multi-classifier, multi-stratification structure, the look-elsewhere correction across analysis choices is not accounted for. The Bonferroni-5 correction inside DESIVAST is local; the global garden-of-forking-paths multiplier is not bounded.

### P5-M3 — Tempel concordance is presented as supporting evidence but is methodologically not comparable
§IX A and Fig. 7. The "0.026 pp filament concordance" is between two classifiers (tidal-tensor vs FoF richness) defined on different parent samples (DESI vs SDSS DR10), with different richness-to-tidal mappings. A 0.026 pp agreement at this level of cross-survey, cross-classifier mismatch is, if anything, suspiciously good and likely coincidental given the much larger residuals in other class pairings. Treat as null cross-check, not as positive concordance.

### P5-M4 — RSD treatment of V-Web is hand-waved
§XIII admits "anisotropic eigenvalue deformation is the dominant channel and is not separable from the sweep-induced shift without a reconstructed-position rerun" and then defers the actual quantification. For a tidal-tensor classifier this is the *primary* systematic. The "~0.2 pp" scalar bound is in §XIII admitted to be of the same magnitude as the Phase 2 sweep range (0.22 pp), i.e. potentially saturating the claimed robustness. The headline robustness claim is therefore not actually demonstrated.

### P5-M5 — Toy EFT mapping (Appendix A) does not contribute and is internally caveated to vanishing
The appendix explicitly disclaims that the operator is (i) not in the cited literature, (ii) not rotationally invariant as written, (iii) not gauge invariant, (iv) not derived. It is then offered as "a guide for future model-building." It does not belong in a PRD paper as written; either remove or rewrite as a properly covariant operator with a real bound.

### P5-M6 — Figure 3 x-axis is unreadable
The "Density-quintile null" panel x-axis label rendered as `Den ∈ [42, 10..D690...(DD7682)...]` etc. The bin edges are scrambled. Caption is fine; axis is not.

### P5-M7 — Figure 6 caption/axis units do not match
The HEALPix maps use Mollweide projection axes labeled "0.0–1.0" rather than RA/Dec. The pixel-count colorbar in the top panel is labeled "Chirality σ from half per pixel" overlapped with "voids/pix" — the title text is overlaid in a way that obscures whether voids/pix or σ is being displayed in the top panel.

### P5-M8 — "Largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date" (page 11) — superlative not earned
This is true only because the author's prior work (Paper IV) is the chirality catalog itself, also unpublished. Without an external comparison, "largest to date" is uninformative. Soften.

### P5-M9 — Page length disproportionate to scientific content
This is a null result on a single binary statistic (CW vs CCW) stratified by one categorical variable (environment). 20 pages, 7 figures, 12 tables, 4 nested cross-checks of the same null is excessive. **Recommended cap: 12 pages.** Sections IX A, IX B, X, and Appendix A can be condensed or removed.

### P5-M10 — V2-VIDE σ for sphere-approximation
Table VIII: V2-VIDE σ_void = −1.67, but §VIII D quotes "V2-VIDE catalog-native −1.06 vs sphere −1.67." Yet abstract says |∆f_CW| < 0.002 for all three. With f_CW^void = 0.4971 and f_CW^non−void = 0.4970, ∆f_CW = -0.0001 ✓. OK on this row, but recompute σ: (0.4971−0.5)·2·√81354 = −0.0029·570.5 = −1.65 ≈ −1.67 ✓. This one passes; flagging only because the surrounding bookkeeping is unreliable.

### P5-M11 — Author affiliation/contact non-standard for PRD
"Independent Researcher" with a non-institutional email. Not disqualifying, but PRD will want a competing-interests statement and clear data-availability beyond a "companion data repository" that is not URL-resolvable in the manuscript.

---

## MINOR FINDINGS

### P5-Mi1 — Refs [11], [12] are 2026 preprints (arXiv 2604.xxxxx, April 2026)
Both are "currently in submission" or pre-publication. The paper relies on them for cross-classifier validation. State explicitly that these are not peer-reviewed at submission.

### P5-Mi2 — "BGS-bright" vs "bright" used interchangeably
The DESI tracer-program nomenclature is bright/dark/backup; BGS-bright is the dominant component but not synonymous with bright. Be consistent.

### P5-Mi3 — Page 12 inline calculation σ_P5_pred ≈ 4.6σ
2 × 0.0026 × √791635 = 0.0052 × 889.74 = 4.63 ✓ — correct.

### P5-Mi4 — V-Web volume fractions labeled inconsistently
Fig. 1 caption: cluster 1.0%, wall+filament 74.5%. Bar chart shows wall 41.3%, filament 33.3% → 74.6%. Trivial rounding.

### P5-Mi5 — "Sub-percent sensitivity" claim for Paper IV
Restated in §XII C. Cannot be evaluated without Paper IV in hand. See P5-E8.

### P5-Mi6 — Random-seed-as-reproducibility
"Deterministic seed: 20260515" (page 19). Single seed is necessary but not sufficient for reproducibility; the companion data repository is not URL-resolved.

### P5-Mi7 — DESIVAST hole-count phrasing
Page 10/11: "89,003 + 12,860 = 101,863 interior hole spheres comprising the 3,765 maximal voids." Restated multiple times. Compress.

### P5-Mi8 — "The cluster volume fraction (1.0%) reflects the high-density tail"
Fig. 1 caption repeats body verbatim.

### P5-Mi9 — HEALPix NSIDE=32 expected pixels under 33% sky coverage ≈ 4,055
Quoted 3,303 is ~27% (page 8). Acceptable but the discrepancy could be flagged: which pixels are excluded from the "valid" count? Likely pixels with n_spiral < some threshold but the threshold is not stated.

### P5-Mi10 — Bonferroni-4 threshold quoted as both 2.50 (α=0.05, page 6) and 3.02 (α=0.01, page 6) without consistent disclosure of which α is in use
Standardize.

---

## NITS

### P5-N1 — Duplicate-style phrases
- "supporting, not load-bearing — the primary cross-classifier validation remains..." appears in both §IX A (twice) and Fig. 7 caption. Trim.
- "statistically indistinguishable" appears 6+ times.

### P5-N2 — Mixed Mpc/h and Mpc
Page 10: "800 Mpc cube" (no h) for T-Web reference; rest of paper uses Mpc/h. Standardize.

### P5-N3 — Abstract uses both "BGS-bright" and "BGS bright" (no hyphen)
Pick one.

### P5-N4 — Footnote-style "(supporting, not load-bearing)" parentheticals in main text
Excessive hedging; collapse to a single sentence in the relevant section.

### P5-N5 — "DR1" vs "Data Release 1"
Both used in the same paragraph (page 1). Pick one after first introduction.

### P5-N6 — pages 1–2 abstract is ~1.5 pages long
PRD abstract should be one paragraph. The current abstract is effectively a structured-abstract block running 1.5 pages; this will be rejected by PRD on format alone.

---

## Summary recommendation

**REJECT**

The scientific question is legitimate and the null is in principle a useful publishable result. However, the manuscript fails an internal-consistency audit at the level of basic counting: the dark-sample bookkeeping is impossible (E1), the filament bright-only n exceeds the filament total (E2), a Phase 2 sweep cell reports n exceeding the parent sample (E3), Table II sums to a different n than the abstract and figure 2 claim (E4), DESIVAST void counts differ by ~5× between two paragraphs (E5), and a load-bearing σ_pred is arithmetically off (E6). Layered on top, the entire monopole-interpretation framework imports its key number (∆f_CW = −0.0026) from a companion manuscript that is "in preparation" and not yet on arXiv (E8). The abstract is ~1.5 pages and structurally violates PRD format (N6), the toy EFT appendix is self-disclaimed to be non-derivable (M5), and the page count is roughly 2× what the content supports (M9). I would not send this back to the authors as "major revisions" because the arithmetic problems suggest the underlying analysis pipeline has not been audited end-to-end; the right action is reject and invite a resubmission only after the companion Paper IV is public and a clean internal-consistency pass is completed.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report — P5 (R10v3p1) — SECOND-PASS ADDENDUM

Further audit of the manuscript reveals additional arithmetic, comparability, and cross-reference issues that the first-pass review missed. These are all NEW findings; they do not duplicate items E1–E9 / M1–M11 / Mi1–Mi10 / N1–N6 in the initial report.

---

## NEW ESSENTIAL FINDINGS

### P5-E10 — Phase 2 sweep Table VI does not measure what its caption claims
**Page 8, Table VI; abstract page 1.** Table VI is captioned "range of f_CW across the four cosmic-web classes per sweep cell, in percentage points," and the abstract states "the per-cell range of CW fractions across the four classes never exceeds 0.22 percentage points." Both are inconsistent with Table II:

- Table II canonical run (R_s=25 Mpc/h, λ_th=0): range across all four classes = 0.5034 − 0.4836 = **1.98 pp**.
- Table VI canonical cell (R_s=25, λ_th=0): reports **0.165 pp**.

Factor of 12 mismatch. The only way to reproduce 0.165 pp from the canonical run is to restrict the range to (filament − cluster) = 0.4980 − 0.4963 = 0.0017 = 0.17 pp. **Table VI is therefore reporting the range over only the two volume-dominant classes (filament + cluster), not over all four classes as advertised.** The void and wall classes — the very bins one would expect to be most sensitive to environment-dependent chirality — are excluded from the "robustness" statistic without disclosure.

This propagates to a load-bearing abstract sentence. The actual all-four-class Phase 2 range may be ~10× the quoted 0.22 pp.

**Fix:** Either (a) recompute Table VI as a true four-class range and rewrite the abstract, or (b) explicitly declare in caption + abstract that the range is over filament+cluster only, and discuss why the small-N classes are excluded.

### P5-E11 — §XI BGS-vs-LRG-ELG-QSO claim directly contradicts §VI D
**Page 17, §XI vs page 7, §VI D.** §XI states: "target-class split (BGS vs. LRG-ELG-QSO) with **BGS-only CW fraction within ±0.001 of LRG-ELG-QSO**. No test produces a > 3σ residual after Paper IV-monopole correction."

§VI D reports: bright f_CW = **0.4970** (BGS-dominated), dark f_CW = **0.5051** (LRG/ELG/QSO). |∆f_CW| = **0.0081**, which is **8× the bound asserted in §XI** and also drives the 3.4σ filament sign-flip diagnostic the abstract treats as a real residual structure. Two sections of the paper directly contradict each other on the same robustness statement.

### P5-E12 — Multiple Bonferroni thresholds arithmetically incorrect
**Page 5, §V B and page 9, §VII A.** Eq. (2) is correct. The numerical applications are not:

- **§V B:** "Bonferroni-5 family at α = 0.05, per-test threshold |σ|_Bonf_0.05,5 ≈ 2.81." Recomputation: √2·erfc⁻¹(0.05/5) = Φ⁻¹(1 − 0.005) = **2.576**. Not 2.81.
- **§VII A:** "Bonferroni-9 (α = 0.05) threshold |σ|_Bonf_0.05,9 ≈ 3.02." Recomputation: Φ⁻¹(1 − 0.05/(2·9)) = Φ⁻¹(0.99722) = **2.77**. Not 3.02 (which is the K=4, α=0.01 value used elsewhere).

These are not cosmetic: the §VII A conclusion that "zero produces a per-class |σ_vs monopole| residual above the Bonferroni-9 (α = 0.05) threshold" depends on the correct value being 2.77, not 3.02. Several near-threshold σ residuals (e.g., the 2.81-quoted filament class) need to be re-evaluated. At |σ|_Bonf = 2.576, the same DESIVAST estimators are closer to the boundary than the paper claims.

---

## NEW MAJOR FINDINGS

### P5-M12 — Tempel cross-validation hides an opposite-sign concordance in the cluster class
**Page 13, Table XI vs Table II.** The "concordance distance" framing reports only |∆f_CW|, suppressing sign:

| Class pair | f_CW (V-Web) | f_CW (Tempel) | σ (V-Web) | σ (Tempel) |
|---|---|---|---|---|
| filament / filament_like | 0.4980 | 0.4982 | −2.61 | −0.43 |
| cluster / cluster_like | **0.4963** | **0.5029** | **−4.66** | **+0.44** |

The cluster pair has **opposite-sign deviations from parity** at the two classifiers, with V-Web at −4.66σ and Tempel at +0.44σ. The "0.66 pp concordance distance" framing buries this. A true classifier concordance should agree on the direction of the residual; this one does not. The paper uses Tempel as supporting evidence for environment-independence, but the cluster-class sign-flip suggests instead that the V-Web cluster σ is a classifier-specific artifact (consistent with the boundary-leakage interpretation in §VI D, which then weakens the §IX A "concordance" framing rather than strengthens it).

### P5-M13 — NSIDE=32 pixel counts disagree across the paper without declared cuts
**Pages 8, 12, 13–14 (Table V, §VIII F, Fig. 6 caption).** At NSIDE = 32 the paper quotes four different valid-pixel counts:

- Table V: **n_pix = 3,303** (HEALPix scan)
- §VIII F: **1,821 valid pixels** (per-pixel σ_vs monopole moments)
- Fig. 6 caption: **1,496 valid pixels** (σ map, ≥200 spirals/pixel cut)
- §VIII F Pearson: **727 pixels** (≥200 spirals/pixel ∩ ≥1 maximal void)

Only the 727 and 1,496 numbers have stated cuts. The 1,821 → 1,496 difference (~325 pixels) is unexplained. The 3,303 → 1,821 difference (~1,482 pixels) is also unexplained. A reader cannot reconstruct which pixels enter which moment statistic.

### P5-M14 — HEALPix scan coverage fractions imply undisclosed per-pixel cuts
**Page 8, Table V.** Total HEALPix pixels at NSIDE = 16/32/64 are 3,072/12,288/49,152. The paper's "valid" counts are 1,054/3,303/7,208, giving sky-coverage fractions of **34%/27%/15%**. These should be approximately equal for the same survey footprint at all NSIDEs; the monotonic decrease implies a per-pixel minimum-spiral-count cut that is not declared. Without disclosure of this cut, the look-elsewhere correction in §V A (which assumes K = 1,054 at NSIDE = 16) is not reproducible.

### P5-M15 — Three samples carry the V-Web class label without consistent declaration
**Throughout.** The paper uses three different denominators for V-Web-class statistics without consistent flagging:

- **791,635** (Table I, abstract, Fig. 2 caption) — the headline "chirality-relevant" sample. The tracer-program breakdown in §VI D (775,760 bright + 14,782 dark + 875 backup + 218 other = 791,635) is on this sample.
- **812,793** (Table II implied sum, §VIII F explicit) — the "relaxed env-confidence" sample. This is the basis of the Table II per-class n's and the bright-fraction contingency (§VI D, n_bright+dark = 811,609).
- A **third, larger** sample is implied by the filament-class bright n = 416,701 (§VI A) and dark n = 21,203 (abstract). Filament bright alone exceeds Table II's filament total of 408,187, so these numbers cannot come from either of the two samples above.

Per the initial review, the bookkeeping is contradictory (P5-E1, E2). This new finding identifies that the inconsistency is structural: the paper interleaves statistics on at least three differently-defined samples and presents them as if they refer to one.

### P5-M16 — σ_pred for cluster at n=397,505 also off
**Page 5, §VI A.** Text gives σ_pred(cluster) ≈ −3.28. Recompute: 2·0.0026·√397,505 = 0.0052·630.48 = **3.28** ✓. This one is correct. (Flagging only because §VI A also gives σ_pred(filament) = 3.16, which P5-E6 already showed is wrong: should be 3.32. The two σ_pred values were computed inconsistently — one to 3 sig figs, the other appears mis-typed or computed with a different ∆f_CW.)

### P5-M17 — V2-VIDE non-void σ in Table VIII does not reproduce
**Page 12, Table VIII.** V2-VIDE n_void = 81,354, so n_non-void = 678,945 − 81,354 = 597,591. With f_CW^non-void = 0.4970:
σ_pred = (0.4970 − 0.5)·2·√597,591 = −0.003·1,546.08 = **−4.64**.

Table VIII reports **−4.59**, off by ~1%. Small but flagging because the same column for VoidFinder reproduces (−4.59 against 621,964: −0.0029·1,577.4 = −4.57, OK); only V2-VIDE is off. Likely a stale value not updated when n was changed.

---

## NEW MINOR FINDINGS

### P5-Mi11 — "Within ±0.002 of global" footprint-split claim unsupported
**Page 17, §XI.** No per-leg f_CW table is shown. Paper IV is cited as the source of the per-leg σ tracking but the actual bound stated here (±0.002) is asserted without numbers in this paper or any back-of-envelope check. Cf. §VI E sky-position stratification which shows much larger per-pixel variation (Table V max |σ| = 4.13 at NSIDE = 32).

### P5-Mi12 — V2-REVOLVER and V2-VIDE void counts inconsistent across paragraphs (separate from P5-E5)
**Page 10 vs page 11 §VIII C vs page 11 §VIII D.** Beyond the 420 vs 1,992 / 295 vs 1,478 discrepancy already flagged (P5-E5), the V2-REVOLVER "n_void" appears as: 102,911 (point-in-sphere, page 11 Table VIII), 86,276 (catalog-native GALZONE, page 11 §VIII D), and 1,992 (effective voids, page 11 §VIII C). Three different things called "n_void" in three consecutive paragraphs.

### P5-Mi13 — Fig. 7 numerical concordance off slightly from §IX A
**Fig. 7 caption page 16 vs §IX A page 13.** Caption reports "V-Web filament f_CW = 0.4980 (n = 408,187) vs Tempel filament_like f_CW = 0.4982 (n = 14,317) differ by 0.026 percentage points." At the rounded values shown (0.4980, 0.4982), the difference is 0.02 pp, not 0.026. The 0.026 pp value is recoverable from higher-precision sources (203261/408187 − 7133/14317 = 0.000258 = 0.026 pp), but the caption's own numbers do not reproduce it.

### P5-Mi14 — Page 12 σ_P5_pred = "≈ 4.6σ"
2·0.0026·√791,635 = 4.627. Quoted ≈ 4.6 ✓. (Verification, no error.)

### P5-Mi15 — V-Web volume fraction sum
Fig. 1 caption: 0.244 + 0.413 + 0.333 + 0.010 = **1.000** ✓ (verification).
Text-stated "wall+filament fraction (74.5%)": 41.3 + 33.3 = **74.6%**, off by 0.1 pp rounding. Trivial.

### P5-Mi16 — Per-class CW count check on Table II
207 + 3,359 + 203,261 + 197,284 = **404,111** CW.
Table I gives total CW = 393,592 on n=791,635.
Implied "extra" CW in the 812,793 superset: 404,111 − 393,592 = **10,519**.
"Extra" total: 21,158.
"Extra" CCW: 21,158 − 10,519 = 10,639.
Extra-sample f_CW ≈ 10,519 / 21,158 = **0.497**, indistinguishable from the rest. Consistent at least within itself.

---

## NEW NITS

### P5-N7 — "T-Web DR1 BGS volume fractions" sum to 1.02
Page 15: {0.16, 0.45, 0.37, 0.04}_BGS sums to 1.02. Rounding admissible but flag.

### P5-N8 — Two different σ values for "the catalog-level monopole"
Abstract: "−5σ catalog-level signal" appears 3 times. §VIII F clarifies this is −5.07σ on n=812,793 or −5.00σ on n=791,635. Pick one and use consistently in the abstract.

### P5-N9 — "Survey-shell systematic" first introduced without definition
Page 11 first uses "survey-shell systematic that drives the V-Web vs T-Web void-fraction discrepancy" before §IX B (page 15) explains what it is. Forward reference is implicit. Add a §VIII B forward pointer or define on first use.

### P5-N10 — "approximate concordance" hedge
Page 15: "approximate concordance for two independent classifiers run on overlapping but non-identical samples of the same survey." Unquantified hedge. Either show the per-class V-Web−T-Web ∆ explicitly or remove the framing.

---

## Why the first-pass review missed these

The second pass added 3 essential findings (E10–E12), 6 major (M12–M17), 6 minor (Mi11–Mi16), and 4 nits (N7–N10). The first pass focused on:

- Sample-size impossibilities at the level of obvious additions (the 14,782 vs 21,203 + 4,234 contradiction).
- Stale-number arguments at face value.
- Methodological / structural objections.

What was missed and recovered on the second pass:
- **Phase 2 Table VI** (E10): the most consequential new finding. The single sentence in the abstract — "per-cell range of CW fractions across the four classes never exceeds 0.22 percentage points" — turns out to be quantitatively false at face value; the range across all four classes is 1.98 pp at canonical, and Table VI must be measuring something narrower (filament + cluster only). This invalidates the Phase 2 robustness pillar.
- **§XI vs §VI D contradiction** (E11): two robustness statements in the same paper directly contradict on the same statistic.
- **Bonferroni arithmetic** (E12): two of three quoted Bonferroni thresholds are arithmetically wrong, the second of which (3.02 at K=9, α=0.05) is load-bearing for the Phase 2 §VII A conclusion.
- **Tempel cluster-class sign-flip** (M12): hidden by the absolute-value "concordance distance" metric, this directly contradicts the "supporting" framing of §IX A.
- **NSIDE=32 four-way pixel count inconsistency** (M13).
- **V2-VIDE non-void σ** (M17): the kind of stale number that survives across paper revisions.

These additions sharpen the recommendation: this is not a paper that can be salvaged through major revisions. The arithmetic-consistency failure rate is high enough that the analysis pipeline itself needs an end-to-end audit, not just textual edits. The recommendation remains **REJECT**, with the new findings strengthening the case.