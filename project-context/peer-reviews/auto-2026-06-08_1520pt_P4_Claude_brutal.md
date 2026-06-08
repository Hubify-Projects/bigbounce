# P4 auto-2026-06-08_1520pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (16395 chars)
**Wall time**: 535.6s

---

# Referee Report — Manuscript P4
**Paper title (paraphrased):** Survey-scale galaxy chirality with equivariant TTA — null ℓ=1 dipole on 8.47 M DESI Legacy galaxies (3.2 M spirals)
**Recommendation up front: REJECT (with invitation to resubmit as a substantially shorter methodology note, possibly to a different journal).**

I have read all 11 pages, recomputed every load-bearing scalar, audited the tables and the bibliography, and traced the abstract claims against the body. The paper as submitted has serious problems of (a) novelty/scope vs. PRD bar, (b) internal arithmetic and labeling inconsistencies, (c) residual version-history / audit-trail language inside the body, and (d) presentation that uses multiple different σ conventions interchangeably. A null result is publishable, but only if the bookkeeping is airtight; here it is not.

---

## ESSENTIAL findings (must be fixed before any further consideration)

**P4-E1. Internal audit-trail / "in queue" language in the body.**
Footnote 1 on page 4 contains the following text verbatim:
> "The previous wording 'Binomial(ntotal, p_CW^global)' was ambiguous between N_spiral(p) and N(p)_all; the code in scripts/monopole_null_generative.py uses N_spiral(p) and the headline 99.3% pre-MASTER reproduction figure in Table IV is on the spiral-trial draw. A parallel rerun on N(p)all-trial draws is in queue for the canonical-mask sensitivity-budget recompute and is expected to shift the per-pixel inflation by ⟨N_all/N_spiral⟩ ≈ 1.49 in trial count, with a sub-0.1σ effect on the headline pre-MASTER reproduction figure because mode-coupling decoupling absorbs the trial-count normalization."

This is internal-bookkeeping prose ("previous wording", "in queue", "expected to shift … with a sub-0.1σ effect", forward reference to a script path on disk). It does not belong in a published paper. The "sub-0.1σ" claim is asserted without showing the calculation. **Fix:** either run the parallel rerun now and quote the actual number, or remove the footnote entirely and quote only what was actually computed.

**P4-E2. Headline arithmetic does not match Table II.**
Section IV B states:
> "The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53% demonstrates the dominance of the equivariant TTA processing."

But Table II reports raw (Catalog A) excess **+0.79 %** and equivariant (Catalog C) excess **−0.26 %**. Neither the raw nor the equivariant number quoted in the prose appears in the table; the ratio 0.79 / 0.26 ≈ 3.04 also does not equal 3.86. If the +2.05% / −0.53% are a different observable (e.g. signed real-space dipole amplitudes rather than global CW excess), this is not stated and the reader cannot reconstruct it. **Fix:** make every number in this sentence trace to a row in a table.

**P4-E3. Table II "Dev. (σ)" column does not arithmetically follow from the displayed inputs.**
For Catalog A: (0.5079 − 0.5)/0.000279 = **28.32**, table says **28.8**. For Catalog B: (0.504 − 0.5)/0.000279 = **14.34**, table says **14.6**. For Catalog C: (0.4974 − 0.5)/0.000279 = **−9.32**, table says **9.5**. The discrepancies are not large but they are systematic in one direction, which suggests the σ column was computed from a slightly different N (perhaps full-catalog vs CW+CCW-only) while the central values and quoted error use a different N. The reader has no way to reconcile this. **Fix:** state the N used for each row's σ, or recompute consistently.

**P4-E4. Novelty / contribution does not meet the PRD bar.**
The headline scientific result is a **null** at −0.122 σ on a sample whose chirality labels are 67.6 % inherited from CE-ResNet (Jia 2023) and whose own classifier monopole sits 9.5 σ away from 50/50. The independent GZ1 cross-match accuracy is **69.91 %, κ = 0.40**, which is only modestly above chance for binary chirality. A null measurement at this label-quality level, on a footprint already analyzed by Iye et al. (2021) and Jia et al. (2023), does not constitute a primary cosmology result for Phys. Rev. D. The framing "largest galaxy chirality catalog to date" is at best a data-product claim and is partly a re-labeling of CE-ResNet data. **Fix:** either (i) reframe explicitly as a methodology + data-release note and submit to PASP / JCAP / RASTI, or (ii) demonstrate a *physical* constraint that Iye 2021 and Jia 2023 did not already establish, with a quantitative comparison.

**P4-E5. Side-by-side σ values from incomparable nulls in the section headings and discussion.**
Although the abstract carries the disclaimer that σ values are "not directly comparable across estimators", the body repeatedly juxtaposes them without re-stating the qualifier, e.g.

- Sec. III A: "(σ_dipole = 0.43, p = 0.30); and … on the analysis subsample mask … −0.122σ" — no caveat at the point of juxtaposition.
- Sec. IV C: "Catalog A (raw) shows a 2.31 σ real-space dipole and a +6.48 σ pre-MASTER pseudo-Cℓ" — two different estimators, single sentence, no comparability statement.
- Sec. VII: "Equivariant post-processing collapses the real-space dipole to 0.43 σ; MASTER mode-coupling deconvolution independently collapses the pseudo-Cℓ to the canonical −0.122 σ null" — these are computed on different masks (full-catalog vs subsample) with different nulls; presented as parallel reductions.

Per reviewing protocol this is an essential finding. **Fix:** at every juxtaposition, name the null and the mask, or use distinct symbols (e.g. σ_iso, σ_pp, σ_mc).

**P4-E6. Reported "3.64 σ" vs empirical rank "1.9 σ" is misleading.**
Abstract: "+3.64σ (z = ∆/σ_null moment-ratio; empirical rank p_MC = 0.030, i.e. ≈ 1.9σ Gaussian-equivalent)." This is a 1.7σ-equivalent gap between two ways of reporting the *same* test. The 3.64 is then quoted in **at least six places** as the headline canonical-mask number (Abstract, Sec. III A, Sec. IV C, Table III, Table I, Sec. VII). The honest number is the empirical rank, ≈ 1.9 σ one-tail (the moment-ratio is inflated by a heavy-tailed null). **Fix:** use the rank-equivalent significance in all headline statements and relegate the moment-ratio to a footnote.

**P4-E7. Table III mixes two different masks in one table without separate null-mean columns.**
Row 1 (ℓ = 1 single mode) is on the subsample mask (fsky = 0.659); rows 2–6 are bandpowers on the canonical-N mask (fsky = 0.491). For rows 2–6 the displayed Cℓ values cannot reproduce the "Significance (σ)" column from the displayed σ_null alone: e.g. ℓeff = 9 has Cℓ = −0.248 × 10⁻⁶, σ_null = 0.574 × 10⁻⁶, but Significance = **+2.232 σ**, implying a null mean of ≈ −1.5 × 10⁻⁶ (not shown). The σ for ℓeff = 4 (3.21/0.804 = 3.99 if mean is 0) requires null mean ≈ −1.69 × 10⁻⁶ to reach +6.097 σ. **Fix:** add an explicit "null mean" column, or split into two tables (one per mask).

---

## MAJOR findings

**P4-M1. The 9.5 σ classifier monopole is the dominant systematic and is under-disclosed.**
The Catalog C global CW fraction sits at 0.4974, i.e. 9.5 σ from 50/50. This is also the source of every leakage discussed in Sec. IV D. Yet the Data Availability section says only that this is a "0.26% (9.5σ)" residual "attributed to GZ1 human-handedness training bias." The paper does not show that the residual is spatially uniform with the rigor required to absorb it: the claim "all 7 equatorial coordinate slabs within 0.5 % of 50/50" is asserted but the table is "available in the companion data repository," not in the paper. **Fix:** include the 7-slab table in the body or an appendix, with per-slab σ.

**P4-M2. 67.6 % of training labels are CE-ResNet outputs. The "independent" validation is largely circular.**
The text concedes "validation metrics against the full training set therefore partially reflect agreement with CE-ResNet rather than independent ground truth." Yet the comparison in Sec. V B is presented as if the present catalog is an independent cross-check of CE-ResNet. It is not — it is partly a smoothing of CE-ResNet's labels. **Fix:** quote performance only against the GZ1-only labels, and remove all comparative claims based on metrics that include CE-ResNet pseudo-labels.

**P4-M3. Hemisphere LEE rejection at pLEE ≤ 10⁻⁴ is reported and then dismissed.**
Appendix C: "The direct-MC look-elsewhere test (N = 10,000 random-label shuffles) gives pLEE ≤ 10⁻⁴ (rejection of the random-label null); the conservative Bonferroni/BH penalty across ∼ 650 tested directions reduces post-LEE significance to < 1σ." A 10⁻⁴ rank rejection is not absorbed by Bonferroni at N≈650; 0.0001 × 650 = 0.065, still ≈ 1.8 σ family-wise. The reduction to "< 1σ" is asserted, not derived. **Fix:** show the actual look-elsewhere computation; do not invoke Bonferroni qualitatively.

**P4-M4. Citation [2] (Shamir 2022 PASJ) does not appear in the body.**
I cannot find any reference to "[2]" in the body of the manuscript; the body cites [1], [3], and [4] when discussing Shamir. **Fix:** either cite [2] explicitly or remove from the bibliography.

**P4-M5. The "Fisher Poisson floor" of 0.29 % vs "empirical 50%-rec-3σ" of 0.75 % vs "true-underlying" 1.88 % are tossed around without a clean falsification statement.**
Sec. VI A gives three different sensitivity scales. The abstract's falsification criterion is "σ > 5 with full amplitude ≳ 0.75 %", but this threshold is the 50 %-recovery threshold on the HC pipeline, not the 5-σ-detection threshold. The two are conceptually different. **Fix:** state precisely what amplitude a future survey must detect at what σ on what footprint to falsify.

**P4-M6. The "5-anchor" systematic analysis (Sec. IV D / Appendix D) for the canonical-mask 3.64 σ is presented as definitive, but the WLS-fit-based "z = −264.5" and then "z ≈ −18.1 after block-bootstrap" should not appear at all.**
A 264.5 σ result from a naive WLS posterior, even with the bootstrap-corrected −18.1, is not a credible number to quote in physics. It is a sign that the noise model is wrong. **Fix:** either fix the noise model or do not report these numbers.

**P4-M7. Abstract length and density.**
The abstract is essentially a long-form executive summary running over 50 lines with embedded notes such as "Note: σ values throughout this paper are defined relative to their respective null procedures…" PRD abstracts should be a single tight paragraph. **Fix:** compress to ≤ 300 words.

**P4-M8. Title length.**
The seven-line title with three subtitles ("A −0.122 σ Subsample-Mask ℓ=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual …") is not acceptable for PRD. **Fix:** ≤ 20 words.

**P4-M9. The training-set composition versus validation accuracy story is incomplete.**
The GZ1 independent cross-match accuracy is 69.91 %. Using the dilution factor g = 2a − 1 = 0.398, the *physical* dipole signal is suppressed by 0.398 in the classifier output. This means the present empirical "0.75 % at 3σ" floor implies an underlying detectable signal of ≈ 1.88 %, which is barely below the Shamir 3 % claim. The exclusion of Shamir is therefore not as strong as the abstract implies ("inconsistent in amplitude with Shamir's claimed ∼3% signal by a factor of ∼ 6–12"). The factor of ∼6 is only achieved by comparing 3 % to the *uncorrected* 0.5 %–0.75 % sensitivity, ignoring the very dilution factor the paper itself documents. **Fix:** consistently apply the dilution factor when stating the Shamir exclusion.

**P4-M10. "First", "largest", "novel" framings are at best partial.**
"Largest galaxy chirality catalog to date" — CE-ResNet's catalog was 1.95 M; the present is 3.2 M *spirals*; this is true, but the 1.6× factor stated is largely a consequence of using essentially the same parent sample with a different cut. The contribution is incremental, not survey-scale-new. **Fix:** soften the "survey-scale" / "largest" framing.

---

## MINOR findings

**P4-N1.** Page 4: "(C_meas − ⟨C_null⟩)/σ_null = −0.122σ"; the displayed numbers give (1.494 − 1.546)/0.429 = −0.121 σ, which rounds to −0.12 σ, not −0.122 σ. State at least one more decimal place on the input C values or round consistently.

**P4-N2.** Page 5 Table IV: data 1.696×10⁻², null (1.685 ± 0.007)×10⁻², z displayed as +1.68; recompute gives (1.696 − 1.685)/0.007 = 1.57. The 11→1.68 discrepancy implies a more precise underlying data value (~1.6968?) that should be displayed.

**P4-N3.** Page 5 says the monopole-only null reproduces "99.3%" of the observed power. From Table IV: 1.685 / 1.696 = 0.9935 → 99.4 %. Trivial but inconsistent with the abstract figure of 99.3 %.

**P4-N4.** Page 6: "the post-LEE significance drops below |σ| < 1" — double negation, should be "below 1 σ" or "|σ| < 1".

**P4-N5.** Appendix B Table V "T8: CW/CCW balance 50 ± 10 %" passes at 49.7 % — but the catalog actually carries a 9.5 σ deviation from 50 %. Passing only because the 10 % threshold is two orders of magnitude looser than the 1-σ floor of 0.028 %. This is misleading framing; the test is uninformative.

**P4-N6.** Sec. IV A: "Mean classification confidence is 0.951, median 0.9997." A median > mean implies a skewed distribution; both numbers together suggest a bimodal distribution. Comment on the distribution.

**P4-N7.** Edge-on contamination handling (65.7 % of b/a < 0.3 receive CW/CCW): the "5–8 % sensitivity penalty" is asserted but not derived. The natural systematic is that edge-on disks have ambiguous chirality, which biases the residual toward 50/50 not toward a dipole, but this is asserted, not shown.

**P4-N8.** The paper says the parent sample is "8,474,688" but the final catalog is "8,474,531" with 157 quality-check failures. Fine, but Table II gives Catalog C as 0.4974 ± 0.000279 with Nspiral = 3,201,160; the 0.000279 implicitly assumes N = 3,201,160, not 8,474,531. Make this explicit.

**P4-N9.** "Cohen's κ = 0.40" with 69.91 % accuracy on 234,282 cross-match. Check: κ = (0.6991 − 0.5)/(1 − 0.5) = 0.398 → 0.40. Consistent, but the chance baseline should be stated.

**P4-N10.** Single-author paper using "we" throughout. Acceptable but not standard.

**P4-N11.** Sec. VI C lists "Open Follow-up and Future Directions" — three items, all gated as "do not change the headline" — this is reads as defensive hedging and could be cut.

**P4-N12.** Several arXiv IDs are not formatted to PRD style (mix of "arXiv:2208.13866" vs "[arXiv:2010.11929]" inside brackets in Ref. [12]).

**P4-N13.** Disclosure "AI tool usage" on page 10 is appropriate but should mention which sections were AI-edited (per current PRD norms).

---

## NIT findings

**P4-NIT1.** "patchy survey-mask geometry" appears multiple times; consider unifying terminology.
**P4-NIT2.** The bibliographic entry [35] gives an incomplete citation: "A. Zonca, L. Singer, D. Lenz et al., J. Open Source Softw. 4, 1298 (2019)." — no title.
**P4-NIT3.** "Software:" and "Facilities:" lines under Acknowledgments are AJ/ApJ style, not PRD style.
**P4-NIT4.** Footnote 1 on page 4 (already flagged in E1) is unusually long for a footnote.
**P4-NIT5.** Table I row labels "(i)", "(ii)" duplicate the bullet list labels in Sec. III A — minor redundancy.

---

## Page-budget assessment
The paper is 11 pages for a methodology-plus-null-result. The actual physics content (null at −0.122 σ on the subsample mask; the monopole-leakage diagnostic) can be conveyed in ≤ 6 pages plus 1 page of appendices. Most of the canonical-mask 3.64 σ analysis is in service of explaining away a number that is not a detection. **Recommended maximum: 7 pages including appendices.**

---

## Summary recommendation
**REJECT.**

The paper reports a null result on a chirality observable using a catalog that is largely re-labeled CE-ResNet output, with a 9.5 σ classifier monopole, a 69.9 % independent-label accuracy, and a "headline" 3.64 σ residual that the authors themselves correctly attribute to systematics (and which they elsewhere quote as 1.9 σ rank-equivalent). The science contribution does not exceed Iye 2021 in conclusion or Jia 2023 in pipeline rigor. On top of that, the manuscript contains internal audit-trail language ("in queue", "previous wording was ambiguous"), Table II σ values that do not arithmetically follow from the displayed inputs, an inconsistency between the body's "+2.05 % → −0.53 %" framing and Table II's +0.79 % / −0.26 %, and a title and abstract that are far outside PRD norms. I do not see a path to acceptance at PRD; the authors should either reframe this as a data-release / methodology note for a more appropriate venue (PASP, RASTI, JCAP) or substantially compress the physics content and re-derive the systematic-rejection arguments with a single, consistent significance convention before resubmission anywhere.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report — Manuscript P4 (Second Pass, Fresh-Eyes Review)

I have re-read the paper one sentence at a time, recomputed every displayed scalar against its inputs, traced every bibliographic entry, and audited the abstract against the body. The first-pass review missed a number of substantive issues. I append them below in the same format. Several rise to the Essential level and would on their own justify the REJECT recommendation. **The Essential-level training-set arithmetic discrepancy (P4-E8) is the most serious new finding: the paper's most basic data-description numbers do not add up.**

---

## NEW ESSENTIAL findings

**P4-E8. The training-set composition does not arithmetically close.**
Sec. II B lists three label sources:
- "Galaxy Zoo 1: 6,637 galaxies"
- "CE-ResNet: 17,153 galaxies"
- "Synthetic hard negatives: 2,000 artificial images"

Sum: 6,637 + 17,153 + 2,000 = **25,790**. But the very next sentence states:
> "The combined training set contains 26,636 images (80/20 train/validation split)."

There are **846 unaccounted images** (3.3% of the training set). The same paragraph then claims:
> "67.6% of training labels derive from CE-ResNet predictions"

Recomputing: 17,153 / 25,790 = **66.5 %**; 17,153 / 26,636 = **64.4 %**. Neither matches **67.6 %**. For 67.6 % to be correct, the CE-ResNet count would have to be ≈17,434 (denominator 25,790) or ≈18,006 (denominator 26,636) — neither matches the displayed 17,153. **Three numbers in two adjacent sentences do not reconcile with each other.** Because the entire downstream interpretation of the GZ1 cross-match accuracy (69.91 %) and the dilution factor g = 0.398 depends on understanding what the classifier was trained on, this is an Essential-level inconsistency. **Fix:** state the actual training-set composition (and where the 846 extra labels come from), and recompute the CE-ResNet share.

**P4-E9. The abstract conflates two distinct null procedures into a single phrase.**
Abstract: "post-MASTER canonical-mask direct-MC residual is +3.64σ (z = ∆/σ_null moment-ratio; empirical rank pMC = 0.030, i.e. ≈1.9σ Gaussian-equivalent; **500-MC binomial per-pixel-shuffle null**)."

The string "binomial per-pixel-shuffle null" is not a coherent procedure. The paper uses two genuinely different N=500 nulls:
- **Per-pixel random-label permutation** (Sec. IV C, Appendix A): shuffles CW/CCW assignments among spirals within the existing pixel structure. This produces the +3.64 σ value.
- **Per-pixel binomial draw** (Sec. IV D, Table IV): draws fresh CW counts from Binomial(N_spiral(p), p_global_CW). This produces the +1.68 σ generative-null residual.

These have different null distributions and address different questions (label isotropy vs. monopole-leakage). The abstract welds the two names together, leaving the reader unable to determine which null produced the +3.64 σ. **Fix:** name only the per-pixel label-permutation null at the point where +3.64 σ is quoted; relegate the binomial null to its own sentence about the generative test.

**P4-E10. Monopole subtraction *increases* the canonical-mask significance from +1.85 σ to +3.64 σ — unexplained and counter-narrative.**
Appendix A states:
> "Monopole subtraction reduces decoupled C₁ at ℓ = 1 from 2.30 × 10⁻⁵ to 1.51 × 10⁻⁵ (∼34%) and increases σ from +1.85 to +3.64 (the canonical-mask number)."

Subtracting a known systematic (the 9.5 σ classifier monopole) reduces the signal amplitude by 34 % yet nearly doubles the significance. Arithmetically, this requires the null standard deviation to fall by ~3× (from ~1.24 × 10⁻⁵ to ~4.1 × 10⁻⁶) — a finding that *strengthens* the case that there is a real residual on the canonical mask, contrary to the paper's narrative that the canonical-mask result is "consistent with monopole leakage." The pre-subtraction +1.85 σ value appears only inside Appendix A and is never reconciled with the leakage interpretation in Sec. IV D. **Fix:** either explain why removing the dominant systematic strengthens the residual (and what this implies for the leakage hypothesis), or revise the interpretation in Sec. IV D and the abstract.

**P4-E11. "30× extension" of Iye et al. (2021) is arithmetically wrong.**
Sec. V A:
> "These conclusions corroborate and extend the methodological critique of Iye et al. (2021) [5] with 3.2×10⁶ spirals (30× extension)."

Iye et al. analyzed Shamir's SDSS catalog of ≈1.27 × 10⁵ galaxies (cited by the same paper at Sec. I as "∼ 1.27 × 10⁵"). The ratio 3.2 × 10⁶ / 1.27 × 10⁵ = **25.2×**, not 30×. A headline scale claim in the comparison section should be exact. **Fix:** state 25× or recompute.

---

## NEW MAJOR findings

**P4-M11. The sensitivity floor is derived on a 6.8× smaller subsample than the analysis catalog and not scaled up.**
Sec. III A bullet (vi) and Sec. VI A:
> "empirical injection-recovery on the HC-spiral subsample (N = 471,049)..."
> "The empirical injection-recovery sweep on the HC-spiral subsample (N = 471,049, N_MC,null = 1000, N_MC,inj = 100 per amplitude) gives P(σ > 3) = 0.55 at A = 0.75%..."

The full analysis catalog is N_spiral = 3,201,160 — 6.8× larger. The Poisson floor scales as 1/√N, so the full-catalog 50 %-rec-3σ threshold should be ≈0.75 % / √6.8 ≈ 0.29 % (which matches the Fisher floor quoted in the same section). The 0.75 % empirical floor is the HC-subsample floor, not the analysis-catalog floor; using it as the falsification threshold ("≳0.75%" in the abstract) gives a 2.6× more pessimistic limit than the actual sensitivity supports. **Fix:** either run injection-recovery on the full catalog or state explicitly that the falsification threshold is the HC-subsample value and that the full-catalog sensitivity is tighter.

**P4-M12. fsky = 0.46 in the Fisher floor does not match either declared mask.**
Sec. VI A: "Fisher Poisson floor at 3σ is ∼0.29% full-amplitude (from σ(A/2)≈0.048% at N_spiral = 3,201,160, **fsky = 0.46**)."

But Table I and Appendix A declare only two masks: canonical (fsky = 0.49005) and subsample (fsky = 0.659). Neither is 0.46. **Fix:** identify which mask fsky = 0.46 refers to, or reconcile to the declared values.

**P4-M13. The hemisphere-LEE p-value language is internally inconsistent.**
Appendix C c:
> "The direct-MC look-elsewhere test (N = 10,000 random-label shuffles) gives **pLEE ≤ 10⁻⁴ (rejection of the random-label null)**; the conservative Bonferroni/BH penalty across ∼650 tested directions reduces post-LEE significance to <1σ."

A direct-MC max-statistic test that maximizes over directions in the shuffled data automatically incorporates the look-elsewhere effect. If it does, then Bonferroni on top is double-correcting. If the MC was not max-statistic (i.e., the p-value is per-direction), then the symbol "pLEE" is misnamed and the test does not in fact reject the random-label null at 10⁻⁴ globally. The phrase "(rejection of the random-label null)" reads as the per-direction interpretation, but the symbol "pLEE" implies the corrected one. **Fix:** clarify which test was performed, rename the symbol, and apply only one correction.

**P4-M14. "Strict-superset subsample mask" terminology is inverted from natural reading.**
The "subsample mask" has fsky = 0.659; the "canonical mask" has fsky = 0.49005. So the *subsample* mask is the *larger* mask, and the *canonical* mask is its subset. A reader naturally expects "subsample" to be smaller than "canonical." This usage is never explicitly defined in the body; one must reverse-engineer it from the fsky values. Compounding this, the abstract refers to "strict-superset subsample mask" without explaining what it is a superset of. **Fix:** rename, e.g., to "extended-coverage mask" vs. "high-purity mask", and define the set inclusion explicitly at first use.

**P4-M15. Many bibliographic entries are not cited in the body.**
A spot-check of the reference list against the body finds the following references uncited in the body text:
- [2] Shamir 2022 PASJ (already noted in first pass as M4)
- [13] Gross & Vitells (LEE methodology — should be cited where LEE is discussed)
- [14] Davis & Hayes SpArcFiRe
- [15] Motloch et al.
- [16] Lue, Wang, Kamionkowski
- [17] Cabass, Ivanov, Philcox
- [18] Philcox 2022 BOSS
- [19] Eskilt & Komatsu
- [20] Eskilt et al. Cosmoglobe
- [21] Hou, Slepian, Cahn
- [22] Cahn, Slepian, Hou
- [23] Komatsu Nature Reviews
- [24] Hayes, Davis, Silva (winding-bias correction — should be cited in the GZ1 discussion)
- [25–27] Bamford / Hart / Walmsley Galaxy Zoo papers
- [28] Yu et al. primordial-chirality (directly relevant to the parity-violation discussion in Sec. VI B)
- [33] Hivon et al. MASTER (foundational to the entire Sec. IV C method!)

The omission of [33] (the original MASTER paper) from the body when the entire pseudo-Cℓ analysis relies on it is particularly striking. **Fix:** cite or remove. PRD requires every reference to appear in the body.

**P4-M16. The edge-on contamination "65.7 %" and "10–15 % sensitivity dilution" are quoted without showing the underlying cross-match.**
Sec. VI A: "Edge-on galaxy contamination (65.7% of b/a<0.3 objects receive CW/CCW labels...) reduces effective sample size by ∼10–15%."
Appendix E a: "In our catalog, 65.7% of visually identified edge-on systems (b/a<0.3) receive CW or CCW classifications... An axis-ratio cross-match with DESI Legacy photometric catalogs **is the canonical follow-up**."

The 65.7 % number requires either a visual identification (by whom, on what sample, with what kappa?) or an axis-ratio cross-match — which Appendix E itself says is "the canonical follow-up", i.e. has not been done. The 10–15 % sensitivity dilution is then derived from 65.7 % without showing the derivation. **Fix:** show the cross-match (or visual identification) and the derivation, or remove the quantitative claim and replace with a qualitative caveat.

**P4-M17. Appendix A C₁ values are on a different mask than Sec. IV C without saying so.**
Sec. IV C: C_meas = **1.494 × 10⁻⁶** (subsample mask, fsky = 0.659).
Appendix A: "Monopole subtraction reduces decoupled C₁ at ℓ = 1 from **2.30 × 10⁻⁵** to **1.51 × 10⁻⁵**" (canonical mask, fsky = 0.49005, implicit).

These differ by a factor of 10 in absolute scale because they are on different masks, but the appendix does not state which mask its numbers refer to. A reader trying to verify the +3.64 σ canonical-mask result against the Sec. IV C deconvolution will fail to reconcile the numbers. **Fix:** explicitly tag every C₁ value with its mask.

**P4-M18. Per-imaging-leg decomposition is presented without a stated combination rule.**
Appendix C e:
> "The full-catalog [0.5, 0.6) confidence bin +3.29σ decomposes as BASS+MzLS +0.30σ / DECaLS +4.50σ / DES +2.46σ"

There is no combination rule given that takes the three per-leg σ values to the full-catalog +3.29 σ. With per-leg sample sizes N_leg unspecified and per-leg variances unspecified, the reader cannot verify whether +3.29 σ is the correct combination, nor whether DECaLS's +4.50 σ is the dominant contributor or simply the largest fluctuation. **Fix:** give per-leg N, per-leg variance, and the inverse-variance combination rule.

---

## NEW MINOR findings

**P4-N14.** The Catalog A CW excess +0.79 % is not consistent with the stated CW/CCW recalls. With CW recall = 93.8 %, CCW recall = 92.6 %, a true 50/50 input yields predicted CW excess = 0.5 × (0.938 − 0.926) = 0.6 %, not 0.79 %. The discrepancy is ≈25 %. Likely due to a non-50/50 true input balance, but this is not stated.

**P4-N15.** Sec. III B says "2-fold TTA (original + horizontal flip) rather than the full D₄ group". The Z₂ group used is the chirality-flip subgroup of D₄. Saying "rather than D₄" is fine, but the comparison logic ("mirrors flip chirality, rotations don't") would more cleanly motivate using the chirality-flip Z₂ (one reflection axis), not the dihedral Z₂. Clarify whether the "horizontal flip" is the only mirror tested.

**P4-N16.** Sec. III A bullet (iv) describes the diagnostic as "hemisphere maximum-asymmetry (3.05σ local maximum)" while Table I row (iv) describes the same diagnostic as "hemisphere LEE (MC)" with "pLEE ≤ 10⁻⁴". The two presentations of the same row report different statistics. Pick one or list both with a clear delineation.

**P4-N17.** Sec. IV C: the formula "(C_meas − ⟨C_null⟩)/σ_null = −0.122σ" gives 0.121 from the displayed numbers (1.494, 1.546, 0.429); the paper says 0.122. Likely from one extra decimal place not shown. Round consistently. (Companion to N1.)

**P4-N18.** Appendix D b says "σ_ℓ=2 = +4.73" for the single-multipole canonical-mask test, while Table III row 2 says "+6.097σ" for the bandpower ℓ ∈ [2,6]. These are two different estimators (single mode vs. bandpower) and may both be correct, but the paper does not present the single-mode ℓ = 2 alongside the bandpower, leaving the reader to look in two places to understand the broadband structure. Display both in one table.

**P4-N19.** Abstract: "471 049 high-confidence per-spiral after p_eq_CW > 0.9". But Appendix E uses HC-broad-0.6 = 949,584 and HC-strict = 624,660, with thresholds p_eq > 0.6 and p_eq > 0.8 respectively. The abstract's 471,049 implies p_eq > 0.9. Three different HC thresholds appear (0.6, 0.8, 0.9) with three different N values; consolidate into one table.

**P4-N20.** Sec. VI A: "We estimate ∼10–15% reduction in effective sample size, corresponding to a ∼5–8% sensitivity penalty." The 5–8 % follows from 10–15 % only if sensitivity ∝ 1/√N (factor √(1.10) ≈ 1.049 to √(1.15) ≈ 1.072, giving 4.9 %–7.2 %). State the scaling.

**P4-N21.** The cosine-annealing schedule (T₀ = 10, T_mult = 2) gives cycle boundaries at epochs 10, 30, 70, 150,... The best checkpoint at epoch 79 is 9 epochs into the third cycle — i.e., right after the third restart. This is suspicious: training that selects the best checkpoint right after a learning-rate restart often reflects a momentary minimum rather than a converged optimum. Worth noting in the discussion of model stability.

**P4-N22.** "Mean classification confidence is 0.951, median 0.9997" (Sec. IV A): mean below median for a [0,1]-bounded probability distribution implies a heavy left tail with a sharp peak near 1.0. Suggests a bimodal distribution (high-confidence spirals + a tail of borderline). Worth showing the histogram, especially given the per-confidence-bin systematic discussions in Sec. IV E.

---

## NEW NIT findings

**P4-NIT6.** Table III has six rows but is captioned as having a 38-bandpower joint χ². The 38 bandpowers are not shown.
**P4-NIT7.** The Catalog C "Dev. (σ)" column in Table II is missing a minus sign on the 9.5 entry — sign of the deviation is suppressed only for Catalog C, asymmetrically with A and B.
**P4-NIT8.** "Smith42/galaxies" dataset is cited only via URL, not via a published reference. Standard practice would be to cite a DOI or upstream paper.
**P4-NIT9.** "v2026.04" release tag for a paper dated June 2026 — verify this dates correctly.
**P4-NIT10.** Appendix A second paragraph: "Bandpower vs single-ℓ estimator distinction. The reported MASTER ℓ = 1 result is the single-multipole bin from ℓ = 1 to ℓ = 1" — this is a one-multipole bin in a bandpower object, not a "bandpower from ℓ=1 to ℓ=1". Reword.

---

## Why these matter

Three of the new findings are individually serious enough to demand revision before publication:

1. **P4-E8** (training-set arithmetic): The most basic data-description numbers in Sec. II B do not add up. This is the kind of error that erodes referee confidence in every downstream number.
2. **P4-E9** (abstract welds two distinct nulls): A naïve reader of the abstract cannot determine which null gave the +3.64 σ. Given that the entire interpretation in Sec. IV D rests on distinguishing the two nulls, this is a load-bearing ambiguity.
3. **P4-E10** (monopole subtraction *raises* significance): This actively undermines the paper's stated interpretation. If the canonical-mask residual gets *stronger* when the dominant systematic is removed, the leakage narrative needs new arguments. The paper does not provide them.

My recommendation stands: **REJECT**, with the additional observation that the new findings raise the bar for any resubmission. Before the manuscript is resubmitted anywhere, the authors should rebuild every load-bearing arithmetic chain from the input data forward, ensuring closure at every step.