# P5 auto-2026-06-08_1424pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (12833 chars)
**Wall time**: 433.0s

---

# Referee Report: P5 — Environmental Dependence of Spiral Chirality

## Overall Assessment

This paper reports a null result on environment-dependent spiral chirality using DESI DR1, cross-matching ~792k spirals with V-Web tidal classification and ~57k with DESIVAST voids. The science question is reasonable, and the null result is plausible. However, the paper has **severe structural problems**: it is grossly over-long for a null result, leans entirely on a "Paper IV" companion that is explicitly **not yet peer-reviewed** and not available, contains numerous internal contradictions in the abstract, and engages in extensive post-hoc analysis with a stated lack of pre-registration that the authors themselves flag. The headline "no environment dependence" is at best a null on a heavily systematics-contaminated catalog whose contamination is not characterized in this paper.

---

## ESSENTIAL findings

### P5-E1: Load-bearing dependence on unpublished, non-peer-reviewed companion paper
**Section: Abstract, II, throughout. Pages 1, 2, 18, 20.**

Paper IV [3] is cited as the source of: (i) the 8.47M chirality catalog, (ii) the per-galaxy CW/CCW labels, (iii) the monopole offset ∆fCW = −0.0026 that is subtracted throughout to convert "−5σ" signals into nulls, (iv) the full-sky dipole bound, and (v) the imaging-leg systematics characterization. The reference [3] states "**in preparation; manuscript in preparation**" and the abstract itself admits it is "**not yet peer-reviewed**". The body says "the present manuscript treats its catalog and quoted monopole offset as inputs whose uncertainty is propagated explicitly below."

**This is unacceptable for PRD.** The entire null-result framing requires subtracting a monopole whose value, uncertainty, spatial uniformity, and quality-quartile flatness are all asserted from an unpublished work. Every "−2.61σ → consistent with monopole" claim is unverifiable.

**Required fix:** Either (a) wait for Paper IV to be accepted and cite it properly, (b) include all Paper IV material needed to derive ∆fCW = −0.0026 ± σ from first principles in this paper, or (c) restructure the paper so the null does not depend on the monopole subtraction.

### P5-E2: Abstract internal contradictions on the headline claim
**Section: Abstract. Page 1.**

The abstract simultaneously claims:
- "CW fraction shows no environment dependence above the sensitivity floor"
- Filament σ = −2.61, cluster σ = −4.66 (the cluster result is **5σ from parity**)
- The catalog-monopole offset σpred(cluster) ≈ −3.28 (page 6), which is **also not consistent with the observed −4.66σ at the >1σ level** the paper claims

Recomputation: σpred(cluster) = 2 × 0.0026 × √397,505 = 3.277. Observed = 4.66. Residual = 1.38σ. Then on page 13 Table X claims σvs monopole(cluster) = −1.11. These are not consistent: if the residual is 1.38σ from naive monopole subtraction, but the paper reports −1.11σ after subtraction using fCW(monopole) = 0.4972 (not 0.4974), the abstract should reflect this consistently. The abstract uses ∆fCW = −0.0026 (Paper IV) while the body silently substitutes ∆fCW = −0.0028 ("8% larger than the P4 catalog mean") on page 12.

**Required fix:** Pick one monopole value, justify it, and apply it consistently. The abstract should not claim "−4.66σ on cluster" as a null without showing the actual residual after the correct monopole subtraction.

### P5-E3: Abstract sigma values from non-comparable null procedures presented side-by-side
**Section: Abstract. Page 1.**

The abstract lists σ values from: (a) binomial deviation from 0.5 (cluster −4.66σ), (b) Paper IV-monopole-predicted residual (implicit), (c) label-shuffle p-values (z, density, sky), (d) two-sample z-test (|z| ≈ 3.4σ filament bright vs dark), (e) Pearson p-value (r = 0.006, p = 0.88) — all interleaved without "**these σ values are not directly comparable**" qualification. The review instructions explicitly require this. Specifically, "−4.66σ" (cluster, deviation from 0.5) and "|z| ≈ 3.4σ" (two-sample bright vs dark) are different statistics entirely.

**Required fix:** Add explicit qualifier at each juxtaposition, or use only one null type per claim.

### P5-E4: Contingency test χ² = 4932, p < 10⁻¹⁰⁰⁰ undermines headline
**Section: VI.D, Abstract. Pages 8, 1.**

The abstract reports χ² = 4932 (3 d.o.f.) showing V-Web class and target program are **not** independent, and that this confounds the bright vs dark sign-flip. The abstract then claims "the headline environment-independence statement of this paper is anchored on the DESIVAST primary analysis below, which is constructed to be insensitive to this residual." But this is asserted, not demonstrated. The DESIVAST analysis uses the **same 791,635 spirals**, the same BGS-selection function, and the same V-Web-target-program correlation. The abstract earlier admits the four DESIVAST cross-checks are "methodologically correlated by construction because they reuse the same matched-spiral subsample."

**The paper cannot simultaneously claim (a) confound is real at >3σ in V-Web, and (b) DESIVAST is "insensitive" to it, without an explicit calculation showing why.**

**Required fix:** Compute the DESIVAST null restricted to BGS-bright-only and to the LRG/ELG/QSO-dark sample separately. If both return ∆fCW < 0.002, the insensitivity claim is supported. Currently it is not.

### P5-E5: Post-hoc primary/secondary designation
**Section: V.B. Page 5.**

The paper explicitly states: "a single a priori pre-registered analysis plan was not filed; the choice of which classifier to report as 'primary' is therefore made post-hoc." It then designates DESIVAST as primary. This is a textbook garden-of-forking-paths concern. The DESIVAST result returns ∆fCW = 0.0007 — the smallest signal among all classifiers — and is selected post-hoc as the primary statistic.

**For PRD this is unacceptable without a rigorous look-elsewhere correction across all analysis paths considered.** The "Bonferroni-5" correction inside DESIVAST does not cover the choice of DESIVAST over V-Web over Tempel over ASTRA.

**Required fix:** Either (a) treat all classifiers symmetrically with proper multi-classifier multiplicity correction, or (b) explicitly justify why DESIVAST is primary on a priori methodological grounds (peer-review status alone is not sufficient).

### P5-E6: Page count grossly excessive for a null result
**Sections: throughout. 20 pages.**

This paper is 20 pages for a null result on a single hypothesis (chirality vs environment), with the headline being ∆fCW = 0.0007 on 56,981 spirals. The paper repeatedly reproduces the same result through ~7 partially-correlated classifiers and ~5 stratifications, all returning null. The Phase 2 sweep, ASTRA EDR cross-check, Tempel FoF cross-check, T-Web overlay, and HEALPix scans collectively occupy ~10 pages and add minimal new constraint power because they all rely on the same matched-spiral subsample.

**Recommended maximum page count: 8–10 pages**, including a single robustness section consolidating the Phase 2 / Tempel / ASTRA / T-Web cross-checks into one table.

### P5-E7: Volume-fraction discrepancy with concurrent literature not reconciled
**Section: IX.B. Page 15.**

The paper acknowledges that V-Web returns void fraction 0.244, while the concurrent T-Web run (Ullah et al. 2026 [11]) returns 0.06–0.16 — a discrepancy of 8–18 percentage points. The paper attributes this to "survey-shell edge artifacts" but **does not quantify the impact on the chirality result**. Since the void class is precisely where the paper's headline differential is computed, an 8–18 pp contamination of the void class definition is a first-order effect.

The paper also admits "0/6 V-Web 'void' spirals fall inside any DESIVAST hole" — i.e., the V-Web void label at z ≤ 0.24 has **0% purity** against DESIVAST. This is a catastrophic classifier failure, not a minor caveat.

**Required fix:** Either (a) drop the V-Web "void" class entirely from the headline tables and report it only as a known-contaminated diagnostic, or (b) quantify the contamination's contribution to ∆fCW with a controlled re-classification.

### P5-E8: Arithmetic inconsistency in Table II totals
**Section: VI.A. Page 5.**

Table II reports n: void 428 + wall 6,673 + filament 408,187 + cluster 397,505 = **812,793**. But the chirality-relevant subsample is stated as **791,635** (Table I, abstract). The discrepancy of 21,158 (~2.7%) is unexplained in §VI.A and only acknowledged buried in §VIII.F on page 12 ("21,158-row excess (2.7%) over the 791,635-spiral headline subsample").

**Required fix:** Reconcile in §VI.A, or restate Table II on the 791,635 subsample.

### P5-E9: Equation (1) sign error / factor of 2 inconsistency
**Section: V. Page 4.**

Equation (1): σ_pred = ∆fCW / (0.5/√N) = 2·∆fCW·√N

With ∆fCW = −0.0026, N = 397,505 (cluster): σ_pred = 2 × (−0.0026) × √397,505 = −3.277. Paper says "σpred(cluster) ≈ −3.28" — OK.

For N = 408,187 (filament): σ_pred = −3.323. Paper says "−3.16" on page 6. **This is inconsistent**: 2 × 0.0026 × √408,187 = 3.323, not 3.16. Where does 3.16 come from?

**Required fix:** Recompute and correct.

### P5-E10: Tempel cross-validation methodologically inappropriate as "robustness"
**Section: IX.A. Page 13.**

The paper presents Tempel FoF concordance ("filament concordance 0.026 pp") as supporting the null. But: (1) the Tempel filament_like fCW = 0.4982 and V-Web filament fCW = 0.4980 are **both subject to the same Paper IV classifier monopole** — they share the input CW/CCW labels. **Two classifiers agreeing on the same classifier-biased input is not independent validation of the null.** The 0.026 pp concordance demonstrates that both classifiers correctly inherit the Paper IV monopole; it tells us nothing about environmental dependence.

**Required fix:** State explicitly that classifier concordance on shared CW labels is not independent evidence for the null, and remove "supporting" framing for the Tempel comparison.

---

## MAJOR findings

### P5-M1: "−5σ catalog signal" framing throughout is misleading
**Section: VIII.E, VIII.F. Pages 12.**

The repeated phrasing "the catalog-level −5σ signal" suggests a real detection that requires explanation. In fact this is the Paper IV monopole projected onto the matched sample; it is by construction not an environmental signal. Calling it a "−5σ signal" and then "explaining" it by sky-region or program decomposition presents systematic bias as a discovery being explained away. 

**Required fix:** Reframe as "the Paper IV monopole, which projects to σ = −5.0 at this sample size, is consistent with..." rather than "the −5σ signal."

### P5-M2: Pearson r = +0.006 claimed as "indistinguishable from zero" — true but uninformative
**Section: VIII.F, Abstract. Pages 1, 13.**

The headline Pearson r = +0.006 (p = 0.88) is computed on per-pixel σ_from_half against maximal-void count. At n = 727 pixels, the 95% CI on r is roughly ±0.073. So |r| < 0.073 is the actual constraint; the paper does not state this CI. Furthermore, the per-pixel σ_from_half is itself dominated by Paper IV-monopole leakage (the −5σ structure on the "0 maximal voids/pix" sky region), so the Pearson is testing whether monopole leakage correlates with void density — which is partly a question about sky-mask geometry, not chirality-vs-density.

**Required fix:** Report CI on r, and compute the Pearson on monopole-subtracted σ_vs_monopole instead.

### P5-M3: Density-quintile residual presentation hides borderline result
**Section: VI.C, Figure 3. Pages 6–7.**

Quintile 3 has σ_obs = −3.94, σ_pred = −2.07, residual 1.87σ. The abstract says "|σmax| = 3.94 across density quintiles, pre-monopole-subtraction; the corresponding monopole-subtracted residual is |σobs − σpred| = 1.87, below all Bonferroni thresholds." But the 1.87σ residual quoted is for the **single largest** quintile only; the look-elsewhere correction across 5 quintiles makes 1.87 unremarkable but the absolute deviation 3.94 is not vanishingly small. A label-shuffle null on the max-quintile statistic is not reported.

**Required fix:** Report the label-shuffle max-stat p-value on the 5-quintile family.

### P5-M4: Two-sample z-test |z| ≈ 3.4σ on filament bright/dark not properly accounted for
**Section: VI.D, Abstract. Pages 1, 7.**

A 3.4σ result on the largest single dark sub-class is the strongest non-null detection in the paper. The paper acknowledges this is "the strongest single residual structure in the paper after the catalog-monopole subtraction" and "flagged as a real diagnostic." But the headline still says "no evidence for environment-dependent chirality." 

A 3.4σ on a specific class × program cell, even if explainable post-hoc as a selection-function artifact, must be treated as either (a) a real detection requiring further investigation, or (b) a clearly enumerated false-positive within a multiplicity budget that explicitly includes the class × program × tracer subgroups.

**Required fix:** Compute the multiplicity-corrected p-value on the family of (4 classes) × (4 programs) = 16 cells, and report whether 3.4σ survives.

### P5-M5: RSD treatment of V-Web inadequately quantified
**Section: XIII. Page 18.**

The paper devotes substantial text to the RSD limitation, ultimately admitting "we explicitly do not quantify the propagated uncertainty in the present paper: a full quantification... requires the proper Zel'dovich-reconstructed re-classification, which we defer to a companion follow-up." For a paper whose headline is "no environment dependence at V-Web resolution," an unquantified RSD-induced class-shuffling at the 2–4×10⁴ galaxy level (per the paper's own estimate) is a first-order concern.

**Required fix:** At minimum, run a reconstruction-free sanity check using only galaxies far from class boundaries (e.g. |λ − λth| > 2σ_λ) and confirm the null is preserved.

### P5-M6: Figure 1 — pie chart of volume fractions adds no information
**Section: IV.B, Figure 1. Page 4.**

A pie chart for 4 numbers is filler. The same information could be a single sentence. PRD figures should carry analytical content.

**Required fix:** Remove Figure 1 or merge with Figure 5.

### P5-M7: Figure 5 heat-map shows 9 cells with max range 0.22 pp — figure is overkill
**Section: VII, Figure 5. Page 10.**

A 3×3 heat-map for a result already stated as "max 0.22 pp" is filler. A single inline number suffices.

### P5-M8: Figure 6 axes are not labeled in physical units
**Section: VIII.F, Figure 6. Page 14.**

The Mollweide projection has axes labeled "0.0, 0.2, 0.4, 0.6, 0.8, 1.0" with no indication of coordinate system (RA/Dec? Galactic? Equatorial as stated in text?). The colorbar is labeled "σ" but the top panel needs explicit units (voids/pixel).

**Required fix:** Add proper coordinate labels and units.

### P5-M9: Reference [11] arXiv ID format suspicious
**Section: Bibliography. Page 20.**

arXiv:2604.02463 — arXiv IDs encode year-month as YYMM. 2604 implies April 2026. Date on paper is "June 2026" so this is consistent in principle, but at submission a referee cannot verify either (a) the cited paper exists, or (b) the volume fractions quoted on page 15 are accurate. Same for [12] arXiv:2604.01456. These are both labeled "preprint (2026)" or "(2026)" — unrefereed. The paper relies on them for an "approximate concordance" claim that the V-Web result agrees with an independent T-Web run.

**Required fix:** Confirm both papers exist on arXiv and that the quoted volume fractions match. If unverifiable, remove the comparison.

### P5-M10: Date on title page is "June 2026"
**Section: Title page. Page 1.**

If this is a real submission, the date should be the actual submission date. "June 2026" with arXiv IDs in the 2604 (April 2026) range and no DR2 yet suggests this may be a future-dated draft or a near-future submission. Either way the date should be accurate.

### P5-M11: Reference [13] DESIVAST — verify the void counts
**Section: VIII, Bibliography. Pages 10, 20.**

Paper claims 1,461 VoidFinder voids and 89,003+12,860=101,863 interior holes, plus 420 V2-REVOLVER and 295 V2-VIDE. Abstract says "n_DESIVAST_void = 56,981" matched spirals; page 12 reports nvoid for V2-REVOLVER = 102,911 and for V2-VIDE = 81,354. The relationship between "number of voids" and "number of matched spirals inside voids" needs an explicit volume-filling fraction so a reader can sanity-check.

**Required fix:** Report DESIVAST volume-filling fractions per algorithm and verify against Rincón et al. 2025 [13].

### P5-M12: Per-cell label-shuffle p-values inconsistent across sections
**Section: VII.A, Abstract. Pages 1, 9.**

Abstract: "HEALPix scans... with label-shuffle nulls p = 0.61/0.135/0.413". Table V (page 8) reports p = 0.607/0.135/0.413. Close but the first value disagrees. Phase 2 page 9 says "pLEE = 0.41–0.67 across the nine cells."

**Required fix:** Reconcile the abstract p = 0.61 with body p = 0.607 (likely rounding) and ensure consistency.

### P5-M13: Abstract claims "first" / "largest" implicitly through framing
**Section: Abstract, VIII.B. Pages 1, 11.**

"This DESIVAST-anchored re-analysis is the largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date" — the qualifier "to date" makes this trivially true (no other DR1 spiral chirality-environment test exists in the literature). The framing is misleading.

**Required fix:** Remove or weaken the "largest" claim.

### P5-M14: Bonferroni-4 threshold quoted inconsistently
**Section: VI.D, IX.A. Pages 6, 15.**

Page 6: "below the Bonferroni-4 |σ| = 2.50 threshold at α = 0.05"
Page 15: "Bonferroni-4 |σ|^Bonf_{0.05,4} = 2.498 threshold at α = 0.05"

Same threshold cited as 2.50 and 2.498 in different sections (acceptable rounding) but elsewhere as "Bonferroni-4 |σ| = 3.02 threshold at α = 0.01" — three different numbers for the same correction at slightly different α. Tabulate once.

### P5-M15: Phase 2 "max |σ| = 11.32 at filament" presented misleadingly
**Section: VII. Page 8.**

11.32σ on filament at Rs=10 with n=3,696,152. This is the monopole leaking through a sample 9× larger than the canonical filament sample. Reporting this number prominently without immediately stating "this is the monopole" risks confusion. The sentence does follow up correctly, but the presentation is suboptimal for a quick reader.

---

## MINOR findings

### P5-m1: "p < 10⁻¹⁰⁰⁰" is meaningless
**Section: VI.D. Page 8.** Quote any p-value below ~10⁻¹⁰ as < 10⁻¹⁰ or omit. χ² floating-point underflow gives meaningless extreme p.

### P5-m2: "the same monopole shows up as −5.00σ on the 791,635-spiral chirality-relevant sample"
**Section: VIII.F. Page 12.** Recompute: 2 × 0.0026 × √791,635 = 4.626σ. Paper says −5.00σ observed corresponds to ∆fCW ≈ −0.0028, "8% larger than P4 catalog-mean". So either ∆fCW = −0.0026 or ∆fCW = −0.0028; pick one and propagate consistently.

### P5-m3: "Jeffreys binomial credible interval" vs "exact binomial 95% credible interval"
**Sections: V, VI.A.** §V says "exact binomial 95% credible interval" but Fig 2 caption says "95% Jeffreys binomial credible intervals". Jeffreys is one form of credible interval (Bayesian with Jeffreys prior), not "exact" (Clopper-Pearson). Pick terminology and stick with it.

### P5-m4: "p_max_cls_eq" notation
**Section: XI. Page 17.** Unexplained notation for "confidence-threshold sweep." Define.

### P5-m5: Reference [3] Paper IV format issue
**Bibliography.** "in preparation; manuscript in preparation" — duplicated phrase.

### P5-m6: Reference [4] Paper II — same duplicated phrase
**Bibliography.** "in preparation; manuscript in preparation".

### P5-m7: "5.07σ on n = 812,793" arithmetic
**Section: VIII.F. Page 12.** 2 × 0.0028 × √812,793 = 5.046σ ≈ −5.07σ if using observed ∆fCW = 0.0028. OK but state ∆fCW used.

### P5-m8: Footnote 'a' on page 2 is a definition that should be in the body
**Section: I. Page 2.** Long footnote explaining T-Web vs V-Web nomenclature. This is a load-bearing methodological clarification and should be in §IV proper.

### P5-m9: Two-way contingency test description ambiguous
**Section: VI.D. Page 8.** "four-by-two on nbright+dark = 811,609 spirals" — but earlier total bright+dark+backup+other was 790,635 (775,760+14,782+875+218) on the **chirality-relevant** sample. The 811,609 number for contingency disagrees with this sum and is unexplained.

### P5-m10: "Abstract Robustness" referenced like a section
**Section: IX.A, X. Pages 14, 16.** "see Abstract Robustness" — abstract subsections are not standard cross-reference targets. Use proper section references.

### P5-m11: HEALPix per-pixel scan |σ|^null,p99 vs reported "p"
**Table V. Page 8.** Table reports |σ|^obs vs |σ|^null,p99 and a p value. The relationship between the p99 of the null and the reported p is not explicitly defined.

### P5-m12: V-Web volume fraction precision claim
**Fig 1 caption. Page 4.** "cluster volume fraction (1.0%)" — the precision implied by "1.0" suggests ±0.05% but no uncertainty given.

### P5-m13: Abstract footnote 'a' belongs with methodology
**Page 2.** Footnote on tidal-tensor formulation should be in §IV.

### P5-m14: "Houston Golden" + "Independent Researcher" — affiliation/conflict
**Title page.** PRD allows independent researchers but the heavy reliance on companion "Papers II, III, IV" by the same author, none yet peer-reviewed, is a structural problem (see E1).

---

## NIT findings

### P5-N1: "consistent with 2σ on the binomial null" phrasing
**Abstract.** Awkward.

### P5-N2: Table III column header "σ_obs − σ_pred" formatting
**Page 6.** Use proper math typesetting.

### P5-N3: Figure 3 caption — "k= 5" missing space.

### P5-N4: Repeated "load-bearing" language across many sections — stylistic tic.

### P5-N5: Page 7 caption Fig 3: "dotted blue lines mark the Bonferroni-5 thresholds at α = 0.01" — the figure shows red diamonds for σ_pred and bars for σ_obs; the blue dotted lines should be clearly labeled in the legend.

### P5-N6: "garden-of-forking-paths" — colloquial; use "multiple-comparisons" in PRD.

### P5-N7: Many compound English constructions ("BGS-selection-function-conditioned imaging-leg systematics") strain readability.

### P5-N8: Page 13 "near-perfect null" — physics journals avoid evaluative language; use "consistent with zero at σ < 0.5".

### P5-N9: Date "June 2026" with arXiv IDs from April 2026 — verify consistency with submission date.

---

## Summary recommendation

**REJECT**

This paper does not meet PRD standards on multiple essential grounds. (1) Its central quantitative claims — every "−2.61σ" or "−4.66σ → consistent with monopole" — depend entirely on a monopole value ∆fCW = −0.0026 sourced from a companion paper that is explicitly unpublished and not peer-reviewed; the paper itself does not provide that calculation. (2) The abstract presents a "no environment dependence" headline alongside a −4.66σ cluster deviation, a 3.4σ filament bright-vs-dark sign-flip, and a χ² = 4932 confound between V-Web class and target program, without ever reconciling these in a unified statement. (3) The "primary" DESIVAST analysis is explicitly chosen post-hoc with no pre-registration, and the paper makes no proper multi-classifier multiplicity correction. (4) The V-Web "void" class has 0% concordance with DESIVAST voids — a complete classifier failure that is acknowledged but not propagated to the headline tables. (5) The paper is roughly twice as long as warranted for a null result and reproduces the same conclusion through ~7 partially-correlated analyses. The science question is legitimate and a properly executed version of this analysis would be publishable; this version is not. Recommend resubmission only after Paper IV is accepted and the manuscript is restructured to 8–10 pages with a single, properly-multiplicity-corrected null statement.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Findings on Re-Examination

## NEW ESSENTIAL findings

### P5-E11: Phase 2 sweep "n = 3,696,152" exceeds chirality-relevant sample cap by ~4.7×
**Section: VII. Page 8.**

The paper states: "The largest single-cell |σ_from half| across the entire sweep is 11.32 (filament at Rs = 10, λth = 0, n = 3,696,152). This is the catalog-wide ∆fCW = −0.0026 monopole leaking through the largest sample bin and is predicted, not measured: σ_pred ≈ −0.0026·2√N ≈ −10."

The chirality-relevant matched-spiral subsample is **791,635** (Table I, abstract, repeatedly). σ_from_half is a binomial statistic on CW/CCW labels, which exist only on the chirality-relevant subsample. Therefore no V-Web class — at any (Rs, λth) — can contain more than 791,635 spirals. The quoted n = 3,696,152 is **4.67× the cap**.

Possibilities:
- (a) Stale number from a pre-dedup or pre-NS-filter run;
- (b) σ_pred reverse-engineered from a target σ value (the σ_pred ≈ −10 quoted is computed *forward* from N = 3.7M, which the paper acknowledges: "σ_pred ≈ −0.0026·2√N ≈ −10 matches the observed −11.3"), so the entire arithmetic is performed on an impossible N;
- (c) The number is correct because Phase 2 uses a different (larger) chirality population than the headline — but this would itself invalidate Phase 2 as a "robustness check on the headline."

The "Phase 2 sweep confirms the result is robust" sentence in the conclusions therefore rests on an arithmetically impossible σ value.

**Required fix:** Either correct n to the true Phase 2 sample size and recompute σ_from_half, or explicitly document which population Phase 2 runs on.

### P5-E12: Filament bright/dark counts internally inconsistent with own contingency-test bright fraction
**Section: VI.D. Page 7–8.**

Two statements appear in the same subsection:
1. "filament bright (n = 416,701) σ = −2.80 vs filament dark (n = 21,203) σ = +2.85"
2. "The per-V-Web-class bright/(bright+dark) ratio is {0.981, 0.962, 0.966, 0.989} across {void, wall, filament, cluster}"

Compute from statement 1: filament bright fraction = 416,701 / (416,701 + 21,203) = 416,701 / 437,904 = **0.9516**.

Statement 2 says filament bright fraction = **0.966**.

These disagree by 1.5 pp — outside the contingency-test "max class-to-overall deviation in bright-fraction is 1.5 pp" claim itself (which would put filament between 0.963 and 0.993, not at 0.9516).

A second arithmetic mismatch: filament total in Table II is **408,187** (chirality-relevant subsample); statement 1's bright+dark sum is **437,904** — 7.3% larger than the entire filament class. Even granting the 21,158-row excess "812,793-row env-labeled superset" footnote on page 12, that adjustment scales filament from 408,187 → 408,187 × (812,793/791,635) ≈ 419,100, still 4.5% short of 437,904.

Compounded: the cluster_dark = 4,234 (abstract) implies cluster total (bright+dark) ≈ 4,234 / 0.011 = 385,000 if the ratio 0.989 is correct, still 3.2% short of Table II cluster = 397,505.

Both the |z| ≈ 3.4σ filament bright-vs-dark sign-flip and the χ² = 4932 contingency test are built on these inconsistent counts. The bright-vs-dark sign-flip is the strongest non-null result in the paper and is repeatedly cited in the abstract; the underlying n values do not reconcile with the headline sample sizes.

**Required fix:** Reconcile the filament bright/dark counts with both (a) Table II filament total and (b) the contingency-table bright-fractions reported in the same section. Recompute the 3.4σ z-statistic on the corrected counts.

### P5-E13: Bonferroni-9 threshold mis-quoted as 3.02 (true value ≈ 2.77)
**Section: VII.A. Page 9.**

"zero produces a per-class |σ_vs monopole| residual above the Bonferroni-9 (α = 0.05) threshold |σ|^Bonf_{0.05,9} ≈ 3.02"

Recompute: |σ|^Bonf_{α,K} = √2 · erfc⁻¹(α/K). With α = 0.05, K = 9: α/K = 0.00556. The two-sided z satisfying P(|Z| > z) = 0.00556 is z ≈ 2.77.

Verify by analogy with the paper's other Bonferroni quotes:
- K = 5, α = 0.01: paper says 3.09 ✓ (correct)
- K = 4, α = 0.01: paper says 3.02 ✓ (correct)
- K = 4, α = 0.05: paper says 2.50 ✓ (correct)
- K = 1054, α = 0.05: paper says 4.05 ✓ (correct)
- **K = 9, α = 0.05: paper says 3.02 — actually ≈ 2.77 ✗**

The Bonferroni-9 quote appears to have been confused with the Bonferroni-4 α=0.01 threshold (also 3.02). This matters because at the true threshold 2.77, the Phase 2 per-cell maximum |σ_vs monopole| is closer to the cutoff than the paper claims.

**Required fix:** Correct to 2.77 and re-check whether any sweep-cell residual crosses.

---

## NEW MAJOR findings

### P5-M16: σ_pred = −3.16 for filament does not match ∆fCW = −0.0026 (gives −3.32)
**Section: VI.A. Page 6.**

"predicting σpred from ∆fCW = −0.0026 gives σpred(filament) ≈ −3.16 and σpred(cluster) ≈ −3.28"

Compute σ_pred(filament) = 2 × 0.0026 × √408,187 = 0.0052 × 638.9 = **−3.32**, not −3.16.
Compute σ_pred(cluster) = 2 × 0.0026 × √397,505 = 0.0052 × 630.5 = **−3.28** ✓

The cluster value is consistent; the filament value is off by 5%. The only way to get −3.16 from filament N is ∆fCW ≈ −0.00248. The paper silently swaps ∆fCW values between sections (−0.0026 in the abstract/intro, −0.0028 implied by §VIII.F, possibly −0.00248 here). This is the third inconsistency in the monopole baseline.

**Required fix:** Recompute or correct.

### P5-M17: Smoothing scale Rs = 25 Mpc/h ≈ V-Web cell size 25.91 Mpc/h
**Section: IV. Page 3.**

The canonical V-Web uses Rs = 25 Mpc/h on a 256³ grid spanning 6,634 Mpc/h, giving cell size 25.91 Mpc/h. The smoothing scale is effectively **equal to the cell size**, so Gaussian smoothing performs no inter-cell averaging — each cell is essentially smoothed by itself. The Phase 2 cell Rs = 10 Mpc/h is below the grid resolution, which means the smoothing operation is degenerate (sub-pixel) at one-third of the sweep cells.

Standard tidal-tensor practice requires Rs ≳ 2–3 × cell-size to avoid Nyquist aliasing in the FFT-based smoothing kernel and to ensure the eigenvalue spectrum is well-defined. The paper does not mention this constraint.

**Required fix:** Either rerun on a 512³ grid (cell size ≈ 13 Mpc/h, supporting Rs = 25 and 50), or explicitly characterize the cell-size aliasing impact on the Phase 2 sweep and on the canonical run. The Phase 2 robustness claim under Rs ∈ {10, 25, 50} cannot be sustained if the bottom two cells are at or below grid resolution.

### P5-M18: V-Web step 12 "NN-interpolate smoothed log-density" is ill-defined where smoothing produces ρ ≤ 0
**Section: IV.A step 12. Page 4.**

"NN-interpolate the per-cell label + smoothed log-density to each galaxy."

Gaussian smoothing of δ in Fourier space can produce smoothed (1+δ) ≤ 0 in deeply underdense regions (especially after the survey-mask edge dilation, where the mask itself contributes spurious overdensity gradients). log(1+δ) is then undefined or −∞. The paper does not say how this is handled (cutoff floor? Imaginary-part discard? Replacement with mean?). This matters because the §VI.D within-class density quartiles rely on the per-galaxy log-density values for binning.

**Required fix:** State the handling of non-positive smoothed (1+δ) cells, and confirm the density-quartile bins are insensitive to the choice.

### P5-M19: Table VIII ∆fCW sign convention not stated
**Section: VIII.C, Table VIII. Page 12.**

Table VIII columns: VoidFinder ∆fCW = +0.0007; V2-REVOLVER −0.0019; V2-VIDE −0.0001. Working from the void and non-void f values, the convention is ∆fCW = f_non-void − f_void. This is the opposite of the natural ordering "void vs non-void." The table's column header reads "∆fCW" without specifying which direction.

Compounding: the abstract says "∆fCW = 0.0007, statistically indistinguishable" without sign clarification. A reader testing whether voids show *more* or *less* CW than non-voids cannot extract that from the abstract directly.

**Required fix:** Define convention explicitly in Table VIII caption and abstract.

### P5-M20: "3,765 maximal voids" not reconciled with the 1,461/420/295 algorithm-specific void counts
**Section: VIII vs VIII.E. Pages 10 vs 12.**

Page 10: "1,461 interior voids with VoidFinder, 420 with V2-REVOLVER, and 295 with V2-VIDE."
Page 12: "the 3,765 maximal voids (NGC = 3,241 + SGC = 524)."

1,461 + 420 + 295 = 2,176, not 3,765. The relationship between "interior voids" and "maximal voids" is not defined; presumably "maximal" includes edge-touching voids that fail the interior cut, but this isn't stated. The HEALPix maximal-void analysis in §VIII.E uses all 3,765, while the void-membership tests in §VIII.B use only the interior-void hole spheres. A reader cannot determine whether the void-membership cross-checks and the HEALPix stratification are based on the same underlying void catalog.

**Required fix:** Define "maximal" vs "interior" void in §VIII intro and clarify which analysis uses which.

---

## NEW minor findings

### P5-m9: Cluster bright/dark counts also inconsistent with Table II
**§VI.D, Page 7.** With cluster bright/(bright+dark) = 0.989 and dark = 4,234, implied bright = 380,766 and total cluster (bright+dark) = 385,000. Table II cluster = 397,505. Difference 3.2%. Combined with P5-E12, the bright/dark decomposition systematically undercounts vs Table II.

### P5-m10: HEALPix p = 0.61 (abstract) vs 0.607 (Table V)
**Abstract, Table V.** Minor rounding inconsistency: 0.607 → 0.61 is acceptable, but compare with 0.135 (kept to 3 sig figs) and 0.413 (also 3 sig figs). Use uniform precision.

### P5-m11: ρ̄_cell = 4.64 verified but cube volume not stated
**§IV.A.** 14,622,283 galaxies / 3,150,086 in-mask cells = 4.64 ✓. But the physical volume corresponding to 3,150,086 cells × (25.91 Mpc/h)³ = 5.5 × 10¹⁰ (Mpc/h)³ is not stated, making cross-comparison with cosmological volume estimates impossible without reverse engineering.

### P5-m12: Abstract enumerates "four DESIVAST-anchored re-projections" but lists three (i, ii, iii, iv)
**Abstract.** The (i)–(iv) enumeration in the abstract is described as "four DESIVAST-anchored re-projections" but item (ii) explicitly combines "VoidFinder + V2-REVOLVER + V2-VIDE" (three algorithms), so the count of distinct re-projections is closer to 6 (or 5, depending on whether GALZONE counts). The "four" framing is loose.

### P5-m13: "n_DESIVAST_void = 56,981 (∼ 130× the V-Web void sample size)"
**Abstract.** 56,981 / 428 = 133.1, so "∼ 130×" is OK. But the V-Web void sample at z ≤ 0.24 is what's actually comparable — that may be smaller than 428. Need a like-for-like comparison.

### P5-m14: Footnote 'a' contains a methodologically important distinction (T-Web vs V-Web nomenclature)
**Page 2 footnote.** The footnote acknowledges that the paper uses the *Hahn 2007 T-Web* (tidal-tensor) classifier but calls it "V-Web" throughout for backward compatibility. The Hoffman et al. 2012 V-Web uses velocity shear (not tidal tensor). The body cites both [5] and [6] as if they describe the same classifier, but they do not. This nomenclature decision should be in the methods section, not a footnote, and the citations should be disambiguated.

### P5-m15: "ASTRA EDR Noverlap = 25,186" but V-Web puts only 3 of these in void+wall classes
**§X. Page 16–17.** "with only 3 spirals total in the V-Web void + wall classes" — n = 3 is essentially zero coverage. The cross-classifier headline statistics in Table XII for V-Web on the 25,186 subsample exclude classes with n < 100, so the void/wall bins are silently dropped. This should be stated explicitly in the table caption.

---

## Summary of NEW findings

| Severity | Finding | Type |
|---|---|---|
| E11 | Phase 2 n = 3.7M exceeds chirality cap by 4.7× | Arithmetic impossibility |
| E12 | Filament bright/dark counts contradict contingency bright-fraction and Table II | Stale numbers / load-bearing on 3.4σ |
| E13 | Bonferroni-9 threshold mis-quoted (2.77, not 3.02) | Arithmetic error |
| M16 | σ_pred(filament) = −3.16 inconsistent with ∆fCW = −0.0026 | Arithmetic error |
| M17 | V-Web Rs = 25 Mpc/h ≈ cell size 25.91 Mpc/h | Methodological |
| M18 | Step 12 log-density undefined where smoothed (1+δ) ≤ 0 | Methodological gap |
| M19 | Table VIII ∆fCW sign convention unspecified | Presentation |
| M20 | 3,765 maximal voids vs 2,176 interior voids unreconciled | Catalog ambiguity |
| m9–m15 | Various rounding, nomenclature, and presentation issues | Minor |

The most consequential additions are E11 (Phase 2 sample size impossible), E12 (the 3.4σ filament sign-flip — the strongest non-null result in the paper — rests on internally inconsistent counts), and M17 (the V-Web smoothing scale is at grid resolution, undermining the Phase 2 robustness sweep). E13 and M16 demonstrate that the σ_pred arithmetic that converts the "−4.66σ cluster" deviation into a null is not consistently performed.