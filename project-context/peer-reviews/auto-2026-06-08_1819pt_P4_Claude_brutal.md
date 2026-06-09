# P4 auto-2026-06-08_1819pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (15539 chars)
**Wall time**: 553.8s

---

# Referee Report — P4
**Manuscript:** "Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122σ Subsample-Mask ℓ=1 Null..."
**Recommendation venue:** Physical Review D

---

## Top-level assessment

This is a null-detection paper inflated to the length and prose density of a discovery paper, with a 70-word title, a 1500-word abstract dominated by self-disclaimers, and a "headline" that is in fact a non-detection. The science underneath (TTA-equivariant classifier on 3.2 M DESI Legacy spirals + MASTER null + monopole-leakage diagnostic) could be a competent PRD methods paper at roughly half the length — but the present manuscript suffers from (i) figure/body numerical contradictions, (ii) sigma values from non-comparable null procedures juxtaposed in title and tables without quantitative reconciliation, (iii) at least one load-bearing headline number (the 99.3% reproduction) that the authors' own Footnote 1 admits depends on a choice they have not yet completed the rerun for, and (iv) a "falsification criterion" set so high that the present null is essentially unfalsifiable at signal amplitudes the paper itself claims to constrain.

Below I list everything I found. No softening.

---

## ESSENTIAL findings (paper cannot be accepted without these fixes)

### P4-E1. Figure 2 caption vs. figure body: numerical contradiction.
**Page 6.** Caption states "Catalog C composition... the equivariant TTA classifier (§III C) assigns N_CW = 1,592,107, N_CCW = 1,609,053, and N_NS = 5,273,371." The figure pie chart on the same page shows **CW = 1,687,069 (19.9%), CCW = 1,634,726 (19.3%), Not-Spiral = 5,152,736 (60.8%)**. These do **not** match the caption, and 1,687,069/(1,687,069+1,634,726) = 0.5079, which is the **Catalog A (raw)** value from Table II, not Catalog C. Either the figure is mislabeled (it is showing Catalog A while the caption claims C) or the underlying numbers were swapped at production. Both downstream claims about the −0.26 % excess and 9.5σ monopole are anchored on N_CW − N_CCW; a reader cannot reproduce them from Fig. 2. **Fix:** regenerate the figure with the actual Catalog C composition and recompute the percentages, or correct the caption.

### P4-E2. Figure 1 caption claims D4 (8-transform) TTA, body uses only Z₂.
**Page 5.** Fig. 1 caption: "the classifier is evaluated on the eight D₄ transforms (four rotations × two reflections)." But §III C (page 3) explicitly states: "**We restrict to 2-fold TTA (original + horizontal flip)** rather than the full D₄ group..." and Catalog C is defined as "2-fold flip TTA" (§III D). The figure shows two columns (original, flipped), not eight. The caption is false. This is the central methodology figure — it must accurately describe what was done. **Fix:** rewrite caption to describe Z₂ TTA, or replace the figure if D₄ was actually used somewhere.

### P4-E3. Title juxtaposes σ values from non-comparable nulls.
The title contains "−0.122σ", and the abstract immediately combines this with "+0.43σ" and "+3.64σ" from three different null procedures (label-shuffle, isotropic bootstrap, per-pixel shuffle). The authors add a paragraph in the abstract acknowledging the values are not directly comparable — which is precisely the admission that the title itself is misleading. PRD title style does not permit advertising a σ value that the paper's own abstract then disclaims. **Fix:** drop the numerical σ values from the title; pick a single primary estimator and quote at most one number, or refactor the title entirely.

### P4-E4. "Asymmetry" vs. "excess" definitional drift produces inconsistent magnitudes.
- §IV B (page 4): "The 3.86× asymmetry-suppression factor from raw **+2.05%** to equivariant **−0.53%**."
- Table II (page 4): A (raw) excess **+0.79%**, C (equivariant) excess **−0.26%**.

If "asymmetry" ≡ 2(f_CW − 0.5), then C gives 2 × (−0.26%) = −0.53% ✓, but A gives 2 × (+0.79%) = +1.58%, not +2.05%. **The +2.05% number is unexplained** and inconsistent with Table II. Either Table II row A is wrong, the +2.05% is wrong, or a third definition is in use. **Fix:** define "asymmetry" and "excess" once, recompute, and reconcile the +2.05% number with Table II row A.

### P4-E5. Headline "99.3% reproduction" admitted by the authors to depend on an incomplete rerun.
**Page 5, Footnote 1.** The footnote is half a page long and contains: *"...a parallel rerun on N(p)all-trial draws is in queue for the canonical-mask sensitivity-budget recompute... the quantitative 99.3% figure is specific to the N_spiral draw."* This is a load-bearing headline number (it appears in the abstract, in Sec. IV D, and in the conclusions §VII a). PRD does not accept headline scalars that the authors themselves cannot defend pending a future run. **Fix:** complete the N_all rerun before submission and report the robust figure, or remove the 99.3% claim from the abstract and headline-finding paragraph.

### P4-E6. Figure 4 σ labels (2.7σ, 2.5σ) do not appear anywhere in Tables III or IV.
**Page 8.** Fig. 4 visibly labels ℓ=1 with "2.7σ" and ℓ=5 with "2.5σ". The body and tables report **+1.68σ** (pre-MASTER, Table IV), **+3.64σ** (post-MASTER, Sec. IV D), **+1.85σ** (without monopole subtraction, Appendix A), and **+6.097σ** (bandpower ℓ_eff=4, Table III). None of these is 2.7σ. The reader cannot map the figure's labels onto the paper's quoted statistics. **Fix:** state explicitly which σ definition each label refers to, and reconcile it with Table III/IV.

### P4-E7. "Monopole subtraction increases σ from +1.85 to +3.64" is unexplained and counter-intuitive.
**Appendix A, page 9.** *"Monopole subtraction reduces decoupled C₁ at ℓ=1 from 2.30×10⁻⁵ to 1.51×10⁻⁵ (∼34%) and increases σ from +1.85 to +3.64."* Removing the leaked monopole reduces the **data** C₁ by 34%, but raises the **z-score** by nearly 2σ. This requires that the null variance drops faster than the data. The paper does not justify this. If the null mean and variance are constructed from per-pixel-shuffles of the monopole-subtracted field, then σ_null is naturally smaller, but this should be stated and the apparent paradox explained. Otherwise this is a red flag indicating the canonical +3.64σ "headline diagnostic" is a function of normalization choice, not of any astrophysical content. **Fix:** quantitatively reconcile the data-down-but-σ-up behavior.

### P4-E8. The catalog-statistics arithmetic is internally inconsistent at the percent level.
**Page 4, §IV A.** "CW 1,592,107 (18.78%), CCW 1,609,053 (18.99%), NS/edge-on 5,273,371 (62.23%); spiral total N_spiral = 3,201,160 (37.78%)." Recompute: 1,592,107 + 1,609,053 + 5,273,371 = **8,474,531**, OK. But 1,592,107 / 8,474,531 = 0.18787, OK; 5,273,371 / 8,474,531 = 0.6223, OK. Catalog count 8,474,531 ≠ HuggingFace dataset count 8,474,688 (page 2); difference 157 attributed to QA failures — OK. But Fig. 2 uses 8,474,531 with **different per-class numbers**. The Catalog C class counts in the body and in Fig. 2 are mutually exclusive. **Fix:** make the body, Fig. 2, and Table II numerically identical for Catalog C.

---

## MAJOR findings (significant revision required)

### P4-M1. The 9.5σ "monopole" is computed from a classifier with 69.91 % independent-GZ1 accuracy.
**Page 3, §II B.** "The independent GZ1 cross-match on 234,282 disjoint matches yields spiral-chirality accuracy **69.91%** (Cohen's κ = 0.40)." Cohen's κ = 0.40 is in the "fair" agreement range. The paper then treats this as the "conservative accuracy floor" and proceeds to claim sub-percent isotropy bounds. A classifier with κ = 0.40 cannot reliably distinguish a 0.26% population asymmetry from training-label leakage. The paper should explicitly compute the *propagated* uncertainty: with per-galaxy error rate ~30 %, the residual classifier bias is sourced by training-label imbalance at amplitude ≳ (1 − 2a) × (label imbalance). The "sub-percent floor" claim is unsupported. **Fix:** propagate the κ = 0.40 to the dipole-amplitude error budget explicitly.

### P4-M2. 67.6 % of training labels come from CE-ResNet predictions, so reported validation is partially circular.
**Page 3, §II B.** *"67.6% of training labels derive from CE-ResNet predictions; validation metrics against the full training set therefore partially reflect agreement with CE-ResNet rather than independent ground truth."* The authors acknowledge this but then quote 93.7 % three-class accuracy and 94.9 % post-hoc accuracy without disaggregating which fraction comes from independent labels. **Fix:** report accuracy *only* against the 6,637 GZ1 + 2,000 synthetic labels (i.e., excluding CE-ResNet pseudo-labels).

### P4-M3. The +3.64σ residual is not fully explained by the proposed leakage channel.
The generative null reproduces 99.3 % of the **pre-MASTER** pseudo-C₁, leaving a +1.68σ residual (Table IV). After MASTER deconvolution, the canonical-mask **post-MASTER** residual is +3.64σ. Yet the paper attributes both to the same monopole-mask leakage and labels +3.64σ as "systematics-attributed". The cross-spectrum result r_{ℓ=2}(A_p × n_total) = −0.65, σ = −2.89 (Appendix D) is offered as additional evidence — but it concerns ℓ=2, not ℓ=1. The authors do **not** present a quantitative model in which the same depth/morphology systematic generates +3.64σ at ℓ=1 *and* the observed ℓ=2 broadband structure. The "interpretation (ii)" verdict therefore rests on disfavoring (i) and (iii) rather than on a positive fit to (ii). **Fix:** either fit (ii) quantitatively (e.g., a depth/PSF template regression that absorbs the +3.64σ) or explicitly downgrade the verdict to "unresolved residual".

### P4-M4. The falsification criterion is set so high that the result is effectively unfalsifiable.
**Abstract and §VII d.** *"A future survey detecting a chirality dipole at σ > 5 with full amplitude A ≳ A₉₅, where A₉₅ ≈ 1.5–2 %... would be in tension with the present null. We frame the criterion at A₉₅ rather than at A₅₀ because a future 5σ detection at A ~ 0.75 % would be entirely consistent with the present non-detection..."* This is a logical maneuver: the paper claims sensitivity at A ≈ 0.75 % (50 % recovery) but admits a future detection in that band would not falsify it. By that logic, the present "null" excludes only Shamir-class 3 % amplitudes — a much weaker claim than the abstract implies. **Fix:** be explicit that the present analysis excludes only A ≳ 1.5–2 % and not the ≳ 0.75 % band that the title's sub-percent rhetoric implies.

### P4-M5. The hemisphere result pLEE ≤ 10⁻⁴ is dismissed with hand-waving.
**Appendix C.** The direct-MC look-elsewhere test gives pLEE ≤ 10⁻⁴ rejecting the random-label null. The paper then attributes this to "the same sub-percent GZ1-training-label / depth-coupled systematic that sources the global 9.5σ CW-fraction monopole" without quantitative evidence. This is qualitative attribution, not analysis. **Fix:** demonstrate via a depth-stratified or training-bias-corrected version that the hemisphere asymmetry collapses below 1σ.

### P4-M6. Title is unprintable in PRD style.
The title contains five comma-separated clauses, three numerical σ values, and reads as a paper abstract. PRD titles are typically ≤ 15 words. **Fix:** truncate to a single declarative title; example "Equivariant test-time augmentation null on the galaxy chirality dipole in 3.2 million DESI Legacy spirals".

### P4-M7. Comparison with Shamir is qualitative and the matched-footprint analysis is admitted to be missing.
§V A states *"a likelihood-level exclusion requires a matched-footprint Ganalyzer reanalysis under his pipeline + cuts (not performed here)."* Without this, the claim that the present pipeline is "inconsistent with Shamir's ∼3% signal by a factor of ∼6–12" is qualitative. PRD's standard for refuting a published claim is higher. **Fix:** perform the matched-footprint Ganalyzer reanalysis, or remove the comparison and present the null on its own terms.

### P4-M8. Reference [33] (Hivon et al., MASTER) does not appear to be cited in the body.
The paper relies on MASTER deconvolution but cites only NaMaster [32] in the body. Hivon et al. 2002 is in the reference list but I see no in-text citation. **Fix:** cite [33] where MASTER is first invoked, or remove from the bibliography.

### P4-M9. Edge-on contamination quantification is internally inconsistent.
**Appendix E.** *"65.7% of visually identified edge-on systems (b/a < 0.3) receive CW or CCW classifications rather than NOT_SPIRAL."* The paper then claims "~10–15% reduction in effective sample size, corresponding to a ~5–8% sensitivity penalty." If 65.7 % of edge-on systems are misclassified as spirals and edge-on systems are themselves a significant fraction of disks, the sensitivity penalty estimate of 5–8 % requires a denominator the paper does not provide. **Fix:** state the fraction of the spiral sub-catalog that is edge-on-contaminated.

### P4-M10. Equation 1 (the head architecture) is presented as if it were a mathematical equation.
**Page 3.** "LayerNorm → 384→512 (GELU, d=0.3) → 512→256 ..." is labeled as equation (1). This is not an equation. Replace with a figure or remove the equation number.

### P4-M11. Table III column headed "Significance (σ)" mixes ℓ=1 (single-mode, post-MASTER subsample mask, **−0.122σ**) with bandpower σ values from the canonical-mask recompute on a different mask. These are not comparable and should not be in the same column without footnote 7's caveat repeated in the table. **Fix:** split into two tables or add a column "mask" and per-row null-procedure footnote.

### P4-M12. The σ_null = 4.290 × 10⁻⁷ in §IV C b is suspiciously tight for 500 MCs.
Quoting four significant figures of a Monte Carlo standard deviation from only 500 realizations is overstated; the relative error on σ from 500 samples is ~3 %. Round appropriately throughout (this affects the −0.122 result: (1.494 − 1.546)/0.429 = −0.121, which rounds to −0.12σ; quoting "−0.122σ" implies three-decimal precision the MC cannot deliver).

---

## MINOR findings

### P4-N1. "−0.53 %" vs "−0.26 %" should both appear in Table II with their definitions explicit.

### P4-N2. Mean classification confidence is reported as 0.951 with median 0.9997 (page 4). This bimodal-looking distribution should get one sentence of explanation.

### P4-N3. "DR8" is referenced as covering BASS+MzLS, DECaLS, DES overlap (page 3) but DES is not a DR8 imaging campaign in the standard sense; clarify.

### P4-N4. Page numbers in the in-text "§IV C" etc. are correct but the TOC on page 2 lists "VII. Conclusions" on page 8 — correct. OK.

### P4-N5. Reference [2] (Shamir 2022 PASJ) is in the reference list but I cannot find a `[2]` in-text citation. Verify.

### P4-N6. "p_CW^global = 0.4974" appears in the abstract — this is the post-equivariant fraction, but in §IV D it is referred to as the input to the binomial draw. Same number, two different roles — make this distinction explicit in §IV D.

### P4-N7. Fig. 3 axis label "(N_CW − N_CCW)/(N_CW + N_CCW)" is correct, but the color scale runs ±0.08 while the largest per-pixel Catalog C asymmetry should — for a clean isotropic catalog — fluctuate as 1/√N_pix. Adding the per-pixel expected scatter as a reference would improve the figure's interpretability.

### P4-N8. "Fisher Poisson floor at 3σ is ~0.29 % full-amplitude" — recompute: 3 × 2 × σ(A/2) = 3 × 2 × 0.048 % = 0.288 % ≈ 0.29 % ✓. OK.

### P4-N9. The phrase "the post-MASTER canonical-mask direct-MC residual is +3.64σ (z = ∆/σ_null moment-ratio; empirical rank pMC = 0.030, i.e. ≈ 1.9σ Gaussian-equivalent;" in the abstract is jarring: stating "3.64σ" and then immediately "≈ 1.9σ Gaussian-equivalent" tells the reader the two-tailed Gaussian conversion is far smaller than the moment-ratio z. Lead with the rank-based value or merge the two.

### P4-N10. The abstract's PACS codes 98.80.-k, 98.62.Ai, 95.75.Mn are reasonable for a galaxy-survey methods paper but PRD generally uses arXiv classification rather than PACS now; PACS was retired in 2010.

---

## Length and scope

The paper is 13 pages with 5 figures, multiple tables, and 5 appendices, for a null result whose primary methodological novelty is "TTA-based equivariance + standard MASTER" applied at the 8.47 M-galaxy scale. The literature comparison is qualitative. The systematic analysis is interesting but does not lead to a positive identification of the +3.64σ residual's source.

**Recommended maximum:** 8 pages including appendices.

---

## Summary recommendation

**REJECT** (with invitation to resubmit after major rework)

The paper contains real and publishable methodological content — equivariant TTA combined with MASTER deconvolution on the largest spiral-chirality catalog assembled to date, and a clean generative-null demonstration of monopole-mask leakage — but in its present form it has at least eight essential numerical or figure/body inconsistencies (Fig. 1 caption misdescribes the TTA group; Fig. 2 numbers contradict Catalog C; Fig. 4 σ labels match nothing in the text; the headline 99.3 % figure is admitted to depend on an incomplete rerun; the "monopole subtraction increases σ" claim is unexplained), the title juxtaposes σ values from non-comparable nulls in violation of the authors' own disclaimer, the falsification criterion is set such that the result excludes only the Shamir 3 % class and not the ≈0.75 % band the abstract rhetorically claims, the classifier's independent-GZ1 accuracy is only 69.9 % (κ = 0.40) so sub-percent claims require an explicit error budget the paper does not provide, and the comparison with prior literature is qualitative rather than likelihood-level. A 13-page manuscript of this scientific weight cannot be accepted at PRD with these issues outstanding; with the numerical inconsistencies repaired, the title restructured, the 99.3 % rerun completed, the κ = 0.40 error budget propagated, and the length cut to ≲ 8 pages, the underlying work would be appropriate for resubmission.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report — P4 (Second Pass)

Re-reading with the fresh-eyes checklist surfaced a number of additional issues that the first pass missed. Several are arithmetic-level and load-bearing.

---

## ADDITIONAL ESSENTIAL findings

### P4-E9. Catalog tiers have different spiral totals; this is hidden, and Table II's σ column is internally inconsistent.

Recomputing from Fig. 2's actual pie-chart numbers: 1,687,069 + 1,634,726 = **3,321,795 spirals**. But §IV A states the Catalog C spiral total is **3,201,160**. Difference: 120,635 galaxies.

This is not just a Fig. 2 typo (P4-E1). It reveals that the argmax-class assignment **changes between Catalogs A, B, C** — a galaxy can be classified as spiral under raw softmax but as not-spiral under equivariant TTA (or vice versa). The paper never discloses this.

Worse, Table II compounds the error:

- **Listed σ = 0.000279 for all three rows.**
- Recompute for Cat C: σ = √(0.4974·0.5026 / 3,201,160) = 2.794×10⁻⁴ ✓, gives z = 0.00265/0.000279 = **9.50σ ✓**.
- Recompute for Cat A using listed σ: 0.0079/0.000279 = **28.32σ**, not the **28.8σ** shown. To reproduce 28.8σ requires σ = 2.74×10⁻⁴, which corresponds to N ≈ 3,321,795 — i.e., Cat A's *true* (different) spiral count.
- Recompute for Cat B: 0.004/0.000279 = **14.34σ**, not **14.6σ**. Reproducing 14.6σ likewise requires a different N.

So Table II silently uses three different N values to compute the three Dev. columns, while the σ column displays a single value. Either the σ column is wrong for rows A and B, or the Dev. column is wrong for rows A and B. **Fix:** state per-tier N, recompute σ per-tier, and disclose that the spiral subsample size depends on the catalog tier.

### P4-E10. Training-label arithmetic does not close.

§II B: "(1) Galaxy Zoo 1: 6,637 galaxies; (2) CE-ResNet: 17,153 galaxies; (3) Synthetic hard negatives: 2,000 artificial images. The combined training set contains **26,636** images."

Recompute: 6,637 + 17,153 + 2,000 = **25,790**, not 26,636. **Difference: 846 galaxies**, fully unexplained. This is the training set on which the headline 93.7 % accuracy is computed.

### P4-E11. Appendix E reveals a "+4.31σ monopole-preserving dipole" for full Catalog C — never reconciled with the headline +0.43σ.

Appendix E b: *"the Catalog C-full +4.31σ monopole-preserving dipole collapses to +0.62σ (HC-broad-0.6) and +0.87σ (HC-strict)."*

A 4.31σ result on the same Catalog C as the headline 0.43σ implies that the headline result is obtained only after monopole subtraction, which **the abstract and §IV C never disclose**. The full-catalog physical observable, prior to any subtraction, is 10× more significant than the title number. The paper does not explain whether monopole subtraction is justified for a parity test (the monopole itself is a parity-violating channel for a pseudoscalar field; see also Sec. VI B's own statement that "the parity-odd signal lives in the ℓ = 0 monopole"). **Fix:** explicitly state whether the headline 0.43σ subtracts the monopole and, if so, justify on what statistical/physical grounds doing so is permitted for what the paper itself describes as a parity-odd channel.

### P4-E12. Fig. 4 caption text describes a two-panel figure but the figure is a single bar chart of five multipoles.

*"Top: ℓ = 1 dipole power. Bottom: ℓ = 2 quadrupole."* The displayed figure has one panel showing ℓ = 1 through ℓ = 5 side-by-side as bars. There is no top/bottom split. Combined with P4-E6 (figure σ labels match nothing), Fig. 4's caption is decoupled from the figure body.

### P4-E13. Z-score for the +1.68σ pre-MASTER residual does not recompute.

Table IV row 1: data 1.696×10⁻², null (1.685 ± 0.007)×10⁻², z = **+1.68**.
Recompute: (1.696 − 1.685)/0.007 = 0.011/0.007 = **+1.57**, not +1.68. Off by 7 %. With four-significant-figure data this should be exact.

The same line is the source of the abstract's headline "99.3 %" claim (1.685/1.696 = 99.35 %), so the arithmetic of the canonical leakage demonstration matters.

### P4-E14. The "sample-purity ladder" test in Appendix C is circular.

*"The +3.3σ signal in the 1.87M-galaxy [0.5, 0.6) confidence bin does not survive the sample-purity ladder: cutting to p_eq > 0.6 gives −0.03σ."*

Cutting to p_eq > 0.6 **removes** the [0.5, 0.6) bin entirely. Of course the +3.3σ from that bin disappears in a sample that no longer contains the bin. This proves nothing about whether the in-bin signal is systematic or astrophysical. The correct test is to stratify *within* the [0.5, 0.6) bin by an independent variable (depth, leg, declination) and show that the signal correlates with the proposed nuisance. **Fix:** replace with a non-circular within-bin test.

---

## ADDITIONAL MAJOR findings

### P4-M13. Footnote 1 mis-states the role of W_p; the asymmetry field A_p does not contain W_p.

Footnote 1 (page 5): *"…N(p)_all = NCW(p) + NCCW(p) + NNS(p) that appears as the weighting field W_p in the A_p definition."*

But Eq. (3): A_p = (N^p_CW − N^p_CCW)/(N^p_CW + N^p_CCW). There is no W_p in A_p. W_p is the NaMaster mask weight (Appendix A: "NaMaster weight (mask) map assigns W_p = N^(p)_all"). The footnote conflates the survey-depth mask weight with the field denominator and then says the future N_all rerun matters for "the field it is reproducing" — but the field A_p only contains spirals. This raises doubt about whether the authors themselves have a consistent picture of what the generative null is reproducing. **Fix:** rewrite Footnote 1 to clean up the field vs. weight distinction, and re-examine whether the N_spiral vs. N_all rerun is a substantive change to the headline 99.3 % claim or a non-issue.

### P4-M14. Abstract uses "n = 5,547,858" as if it were a galaxy count.

Abstract: *"…the MASTER-deconvolved single-mode pseudo-C₁ on the strict-superset subsample mask (n = 5,547,858, fsky = 0.659) yields −0.122σ…"*

Table I clarifies that 5,547,858 is N_map,weighted = Σ_p W_p, a **sum of pixel weights** that includes the ~62 % not-spiral galaxies in the survey-depth proxy. It is **not** a count of spirals participating in the dipole estimator. The actual spiral count entering Catalog C is 3,201,160. The abstract's "n = 5,547,858" reads to any cosmologist as "the sample contains 5.5 M analyzable objects," which is false. **Fix:** abstract should quote both the spiral count and (if desired) the weighted-pixel sum, with both labeled.

### P4-M15. The 9.5σ monopole interpretation contradicts the paper's own ℓ-parity statement.

§VI B: *"The ℓ = 1 dipole observable is parity-even... the parity-odd signal lives in the ℓ = 0 monopole and even-ℓ multipoles."*

The 9.5σ Catalog C monopole (Table II) is therefore **the parity-odd channel** by the paper's own taxonomy. Yet §IV B classifies it as a classifier artifact (GZ1 training bias / orientation systematic / photometric asymmetry). The paper does not quantify how it distinguishes a real cosmological parity-odd ℓ = 0 signal from a 0.26 % classifier bias at κ = 0.40. The very channel that would carry a primordial parity-violating signal is dismissed by appeal to systematics without a quantitative bound on what fraction of the 9.5σ could be primordial. **Fix:** either explicitly compute a parity-odd ℓ = 0 bound after marginalizing over the GZ1-training-bias amplitude, or state that the present analysis makes no parity-odd claim.

### P4-M16. ~20 references are listed in the bibliography but never cited in the body.

Searching the body text for in-text citations of [1]–[39]: I find no in-text use of references [2], [11], [13]–[31] except where noted in the running text. The most striking absences:

- **[24] Hayes, Davis, & Silva (2017)**, *"On the nature and correction of the spurious winding bias in Galaxy Zoo 1"* — directly relevant to the paper's discussion of the GZ1 training-label bias (§IV B, §II B), but **not cited** at any of those locations.
- **[13] Gross & Vitells**, the standard LEE reference, not cited where look-elsewhere is discussed (§VI, Appendix C).
- **[33] Hivon et al.** (MASTER) — the algorithm whose name is in the headline — never cited in body (already P4-M8).
- **[28] Yu et al.**, primordial chirality from galaxy spins — directly germane to the discussion in §VI B.
- **[16]–[23]** on cosmic parity violation, all uncited despite §VI B specifically discussing "primordial parity-violating tensor amplitudes" and the parity-odd analog.

**Fix:** either cite these where appropriate (especially [24] at the GZ1-bias discussion) or remove them from the bibliography.

### P4-M17. "30× extension" of Iye et al. is arithmetically incorrect.

§V A: *"corroborate and extend the methodological critique of Iye et al. (2021) [5] with 3.2×10⁶ spirals (**30× extension**)."*

Shamir's original SDSS catalog re-analyzed by Iye et al. has 1.27×10⁵ galaxies (per the citation in §I). 3.2×10⁶ / 1.27×10⁵ = **25×**, not 30×. **Fix:** quote 25× or recompute with the correct denominator.

### P4-M18. Median classification confidence 0.9997 is inconsistent with 1.87M spirals in [0.5, 0.6) confidence bin.

§IV A: *"Mean classification confidence is 0.951, **median 0.9997**."* 

Appendix C: *"the **+3.3σ in the 1.87M-galaxy [0.5, 0.6) bin**."*

If median p_max is 0.9997, then by definition < half the catalog has p < 0.9997. But 1.87 M of the 3.20 M spirals (58 %) are in the [0.5, 0.6) confidence bin alone — meaning a majority of spirals have low confidence. The "median 0.9997" likely refers to a different metric (perhaps p_max across all 8.47 M including very-confident not-spirals) than the "confidence bin" stratification in Appendix C. **Fix:** define "confidence" once and disambiguate which subset / which probability is being summarized.

### P4-M19. Catalog A asymmetry "+2.05 %" still has no derivation, even using Fig. 2's (Cat-A-like) numbers.

Resolving P4-E4 using P4-E1+P4-E9: the Fig. 2 pie counts are Catalog A. Recomputing Cat A's asymmetry from those: (1,687,069 − 1,634,726)/(1,687,069 + 1,634,726) = **+1.576 %**, not +2.05 %. So even when Fig. 2's actual numbers are used, the +2.05 % cited in §IV B is unrecoverable. The "3.86× asymmetry-suppression factor" claim is built on this unexplained +2.05 %. **Fix:** trace the +2.05 % to its source, or recompute the suppression factor (it would be 1.576/0.529 = 2.98, not 3.86).

### P4-M20. T1 and T7 in the bias-hardening suite (Table V) are not real tests.

- **T1 (flip-swap r = 1.000):** By construction of Eq. (2), the equivariant probability is built to satisfy this exactly. Reporting r = 1.000 against threshold > 0.80 is a tautology, not a test.
- **T7 (calibration: "qualitative", "PASS"):** No quantitative metric, no threshold. Simply an assertion of PASS.

These reduce the substantive bias-hardening suite from 8 tests to ≤ 6 tests. **Fix:** either remove T1 and T7 from the suite, or replace them with quantitative independent tests.

---

## ADDITIONAL MINOR findings

### P4-N11. Eq. (B1) is missing a normalization summary.

L = L_CE + λ · (1/N) Σ ‖p(x) − S p(x̃)‖² with λ = 0.5. Units: cross-entropy is in nats; the squared probability-difference is dimensionless. The two terms have different scales and λ = 0.5 is an empirical balance. Standard but should be acknowledged.

### P4-N12. §V B states "0.4974 ± 0.0003" while Table II states "0.4974 ± 0.000279".

0.0003 vs. 0.000279: a 7 % rounding inconsistency in the abstract-class statistic.

### P4-N13. Appendix A claims the canonical mask has no apodization, but Appendix D presents an apodized variant on the same mask.

Appendix A: *"Apodization: none on the canonical mask; C² 2° apodization on the subsample mask."*

Appendix D a: *"C² 2° apodization gives +3.57σ at fsky = 0.482, essentially unchanged from the binary-mask +3.64σ"* — and §IV C / Sec. IV D establish the +3.64σ result is on the canonical mask.

So Appendix D applies a C² 2° apodization to the canonical mask, which Appendix A says wasn't done. Resolvable by stating "apodization for diagnostic only," but as written the appendices contradict.

### P4-N14. Page 8 §VI A: f_sky = 0.46 appears without provenance.

The Fisher floor computation uses f_sky = 0.46. Catalog C operates on either f_sky = 0.659 (subsample mask) or f_sky = 0.49005 (canonical mask). 0.46 is neither, and is not defined anywhere.

### P4-N15. P(σ > 3) = 0.55 at A = 0.75 % means the 50 %-recovery threshold is at A < 0.75 %.

The paper rounds 55 % recovery at A = 0.75 % into "50 %-recovery-at-3σ threshold at A = 0.75 %". A linear interpolation between (0.5 %, 15 %) and (0.75 %, 55 %) gives the 50 % crossing at A ≈ 0.72 %. The headline 0.75 % is slightly conservative — fine, but the rounding should be acknowledged.

### P4-N16. §III A item (iv) hemisphere maximum-asymmetry 3.05σ ≠ Table I row (iv) p_LEE ≤ 10⁻⁴.

Two distinct statistics from the same analysis (uncorrected hemisphere max, and LEE-MC p-value) are tabulated as the same row. They are connected but they report different quantities; pick one summary statistic per row.

### P4-N17. Table III header is "Cℓ" but rows 2–6 are bandpowers, not single multipoles.

Standard notation would use Bℓ or C_b for bandpowers. The mixed labeling makes the first row (single-mode ℓ = 1) and subsequent rows look like the same quantity at different ℓ, which they are not.

### P4-N18. Catalog C "spiral fraction is consistent with magnitude-limited survey expectations" (§IV A) is unsupported.

No reference is given for what the expected spiral fraction is at the DR8 magnitude limit. The 37.78 % spiral fraction is presented as a sanity check without a comparison number.

### P4-N19. Acknowledgments cite NaMaster as "NaMaster/pymaster" without a reference number; first body-text usage of NaMaster in §IV C does cite [32].

The Acknowledgments should consistently use the bibliography number.

### P4-N20. Abstract has 1,500 words including disclaimers; this is twice the PRD style guideline.

The abstract is structurally a mini-introduction. PRD style asks for ≤ ~250 words.

---

## Net effect on recommendation

The first-pass recommendation was REJECT with invitation to resubmit. This second pass reinforces that recommendation. In particular:

- **P4-E9** (silent N-mismatch in Table II + Fig. 2 mislabeling) means the Catalog A/B/C composition itself is not internally consistent in the manuscript.
- **P4-E11** (a +4.31σ monopole-preserving full-catalog dipole that the abstract does not mention) is the kind of discovery-suppressing methodological choice that needs explicit justification in the body, not relegation to Appendix E.
- **P4-E10** (training set arithmetic miss by 846 galaxies) and **P4-E13** (z-score arithmetic miss on the headline 99.3 % claim) suggest the manuscript was not numerically proofread before submission.
- **P4-M15** (the 9.5σ parity-odd monopole channel dismissed without quantitative bound) and **P4-M16** (~20 uncited references, including [24] which is directly relevant to the paper's own GZ1-bias discussion) suggest the parity-physics framing is underdeveloped.

The combined verdict stands: the underlying methodology is real and publishable in compressed form, but the present manuscript is not. A thorough rebuild — numerical consistency pass on every table, every figure caption rewritten to match its figure, every appendix reconciled with the main text, the ℓ=0 parity-odd channel treated with the same rigor as ℓ=1, the falsification criterion honestly framed at the amplitude actually excluded, and the length cut by 40 % — is required before this can be considered for PRD.