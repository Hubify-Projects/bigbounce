# P4 R10v3p1 — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (14779 chars)
**Wall time**: 563.7s

---

# Referee Report — P4 (Round R10v3p1)

**Manuscript:** "Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122σ Subsample-Mask ℓ=1 Null…"

The paper attempts a careful and largely commendable null-result analysis with explicit attention to estimator hierarchy and leakage diagnostics. However, multiple load-bearing numerical inconsistencies, an internally contradictory bias-suppression statistic, an absent derivation of an abstract-level claim, terminology that inverts standard sky-mask conventions, and a complete absence of figures place it below the PRD acceptance bar in its current form.

---

## ESSENTIAL

**P4-E1 — Sec. IV B, p. 4 — Internal inconsistency in headline bias-suppression statistic.**
The text states: *"The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%"*. Neither +2.05% nor −0.53% appears in Table II, which gives Catalog A = +0.79% (raw) and Catalog C = −0.26% (equivariant). If the convention is (CW−CCW)/(CW+CCW)=2·(fCW−0.5), then A=+1.58%, C=−0.52% (close to −0.53% but raw is wrong); if the convention is (fCW−0.5), then values are +0.79%/−0.26%. No reading of Table II reproduces +2.05%. The 3.86× ratio is internally self-consistent but does not connect to the actual catalog statistics. **Fix:** define the quoted asymmetry statistic explicitly, recompute from Table II, and either correct Table II, correct the text, or add the missing intermediate quantity.

**P4-E2 — Abstract + Appendix D, p. 1, p. 8–9 — Missing derivation for an abstract-level discriminator.**
The abstract claims: *"direct cross-spectrum C(Ap × ntotal) at ℓ=2 gives r=−0.65 with σ=−2.89 against permutation null"*. The Appendix D body shows only the ℓ=1 leg-proxy cross-power (r=+0.65 for BASS+MzLS, r=−0.73 for DES). The ℓ=2 result with σ=−2.89 appears only in the closing summary ("Operational conclusion") without supporting calculation, null construction, or pixel-level definition. This is one of the three discriminators used to disfavor interpretation (i). **Fix:** add the explicit ℓ=2 cross-spectrum subsection (estimator, mask treatment, permutation construction, NMC) before the conclusion paragraph.

**P4-E3 — Table IV, p. 5 — Arithmetic error in z-value.**
Pre-MASTER pseudo-C1: data 1.696×10⁻², null (1.685 ± 0.007)×10⁻². Computed z = (1.696−1.685)/0.007 = **1.571**, not **+1.68** as tabulated. Either the central value, null mean, null σ, or quoted z is incorrect. **Fix:** recompute and correct.

**P4-E4 — Sec. II B vs. Data Availability, pp. 3 and 9 — Inconsistent N for GZ1 cross-match.**
Page 3: *"234,282 disjoint matches yields spiral-chirality accuracy 69.91%"*. Page 9: *"the 240,919-galaxy cross-match is 69.91%"*. Same accuracy from two different sample sizes. **Fix:** reconcile and use a single N consistently.

**P4-E5 — Sec. III A + Sec. IV D, pp. 3–4 — Headline-estimator selection is post-hoc and inadequately justified.**
The paper designates the −0.122σ subsample-mask MASTER result as the "headline" while relegating the +3.64σ canonical-mask result (i.e., the same data with the standard mask) to "diagnostic." The subsample mask is a *superset* (fsky=0.659 > 0.49005) — i.e., the result is sensitive to *expanding* coverage to include lower-quality pixels, not to a stricter quality cut. Standard cosmological practice would treat the cleaner/native footprint as primary. A reader can equally credibly read this as a 3.6σ deviation that is *removed* by extending the mask to fsky=0.659 (a step that should add noise, not remove signal). **Fix:** either (i) preregister-style justify the subsample mask as the appropriate analysis mask via a quantitative criterion *that does not depend on which gives a smaller σ*, or (ii) present both as co-headline and let the reader judge.

**P4-E6 — Abstract, p. 1 — Mismatched σ juxtaposition lacks per-instance qualification.**
The abstract states the convention warning once ("σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators"), then immediately juxtaposes −0.122σ, +0.43σ, +3.64σ, +3.57σ, p=0.030≈1.9σ Gaussian, and σ=−2.89 in close succession without re-flagging at each occurrence. Per review instructions, each side-by-side juxtaposition of σ from distinct nulls should carry explicit "not directly comparable" qualification, especially where +3.64σ is reframed as "≈1.9σ Gaussian-equivalent" via rank — that reframing should appear at each occurrence in the abstract. **Fix:** add the qualifier inline at each juxtaposition or present a single unified table at the abstract footer.

---

## MAJOR

**P4-M1 — Sec. II B, p. 2–3 — Training-label circularity.**
67.6% of training labels are CE-ResNet predictions; thus the validation accuracy (93.7%/94.9%) measures agreement with the prior work the paper claims to "advance beyond." The independent GZ1 floor (69.91%, κ=0.40) is the only label-independent benchmark and is barely above the level at which it cannot disentangle classifier label-noise from a real signal at the 0.75% threshold. The paper acknowledges this but the implication — that the analysis cannot independently rule out a CE-ResNet-inherited systematic — should be stated more sharply in the conclusions.

**P4-M2 — Throughout — No figures.**
The paper analyzes a chirality dipole, sky-mask geometry, a generative monopole null with N=500, a bandpower decomposition, a confidence ladder, four hemispheric/quadrant diagnostics, and a 9-template WLS fit, yet contains **zero figures**. At minimum: (a) a Mollweide of the asymmetry map with the canonical and subsample masks overlaid, (b) the pseudo-Cℓ before/after MASTER on both masks, (c) the monopole-only generative-null distribution vs. the data point, (d) injection-recovery sweep P(σ>3) vs. A. Without these, key claims cannot be visually verified by the reader. PRD-quality cosmology papers do not omit footprint and Cℓ figures.

**P4-M3 — Sec. III A and Table I, pp. 3–4 — "Subsample mask" terminology inversion.**
"Subsample" canonically denotes a *subset*; the paper uses it for the *superset* mask. This is consistently confusing and contradicts the rest of the literature on masked-sky pseudo-Cℓ. Rename throughout (e.g., "extended mask" or "low-threshold mask").

**P4-M4 — Bibliography vs. body text — Substantial uncited references.**
At least the following references appear in the bibliography but are not cited anywhere in the body or appendices: [2] (Shamir PASJ 2022), [11] (Land GZ spin), [13] (Gross & Vitells LEE), [14] (SpArcFiRe), [15] (Motloch), [16] (Lue–Wang–Kamionkowski), [17] (Cabass), [18] (Philcox), [19] (Eskilt 2022), [20] (Cosmoglobe DR1), [21] (Hou), [22] (Cahn), [23] (Komatsu), [24] (Hayes/Davis), [25] (Bamford), [26] (Hart), [27] (Walmsley DECaLS), [28] (Yu), [29] (DESI), [30] (LSST/Ivezić), [33] (Hivon MASTER). For PRD, every bibliography entry must be cited at a specific point in the text. **Fix:** add citations at the appropriate physical points (e.g., LEE in Sec. IV E, MASTER in Appendix A, parity background in Sec. VI B) or remove.

**P4-M5 — Sec. IV D and Sec. VII conclusions — Logical tension in monopole-leakage explanation.**
The monopole-only generative null reproduces 99.3% of the *pre-MASTER* pseudo-C₁. But the headline systematic claim is about the *post-MASTER* +3.64σ residual on the canonical mask. The paper writes: *"Monopole subtraction reduces decoupled C₁ at ℓ=1 from 2.30×10⁻⁵ to 1.51×10⁻⁵ (∼34%) and increases σ from +1.85 to +3.64"* — i.e., subtracting the monopole *increases* the significance. This is counterintuitive and is not derived; it is asserted. A reader cannot tell from the present text whether the post-MASTER residual is (a) a true mode-coupling residual that the generative null calibrates, or (b) an artifact of the specific monopole-subtraction convention. **Fix:** show the post-MASTER residual on the same generative null (binomial monopole-only realizations passed through MASTER) and demonstrate the null also reproduces +3.64σ.

**P4-M6 — Sec. IV C and Appendix A — Real-space dipole p-value vs. σ.**
The real-space dipole significance is quoted as 0.43σ with p=0.30. For a two-sided Gaussian, |z|=0.43 → p=0.667, not 0.30. For a one-sided test, p=0.334. The number p=0.30 is plausible for a one-sided bootstrap p but should be qualified ("isotropic-null bootstrap one-sided"). **Fix:** state which tail definition is used.

**P4-M7 — Sec. V A, p. 5 — Comparison-with-prior-work claim is unsupported.**
*"This is inconsistent in amplitude with Shamir's claimed ∼3% signal by a factor of ∼6–12 under the present pipeline, though a matched-footprint Ganalyzer reanalysis is required for a likelihood-level exclusion."* The "factor of 6–12" is repeated in the abstract and conclusions but never derived (0.75/3 ≈ 1/4, not 1/6 to 1/12). **Fix:** show the derivation, or remove the factor claim and replace with the empirical-floor inequality alone.

**P4-M8 — Sec. VI A — Sensitivity-floor inputs.**
σ(A/2)≈0.048% is quoted without derivation (no Fisher matrix, no spiral-pair counting). 3·2·σ(A/2) = 3·0.096% = 0.288% ≈ 0.29% reproduces the quoted floor, so the arithmetic is internally consistent, but the 0.048% input number is presented without justification. **Fix:** derive σ(A/2) explicitly.

**P4-M9 — "Dated: June 2026" — Future date.**
Title page lists "(Dated: June 2026)" and Data Availability "Release tag: v2026.04." If the manuscript is being submitted now, the future date suggests preprint/draft status; PRD requires a current date.

**P4-M10 — Table III, p. 5 — Joint χ²/dof = 4.24 left dangling.**
The joint χ² over 38 bandpowers is 161.2 (effective p ≪ 10⁻¹⁵), described as "Dominated by mask-coupled monopole." This is a 12σ-equivalent global rejection of the null on the canonical mask. The paper handwaves this away as residual mask coupling but does not show that a binomial-monopole + MASTER chain reproduces a χ² of this magnitude. Without that closure, the joint χ² remains an undismissed problem. **Fix:** pass the generative monopole-only null through MASTER and tabulate the resulting joint χ² distribution.

---

## MINOR

**P4-m1 — Sec. I, p. 2 — Shamir 2020 reference probably misattributed.** The text describes Shamir 2020 as reporting on "DESI Legacy samples" with "nearly 1.3 × 10⁶ spiral galaxies." Reference [1] is the ApSS 365, 136 (SDSS + Pan-STARRS) paper; the DESI Legacy sample paper is [3] (MNRAS 516, 2281, 2022). The sample-size attribution appears swapped. Verify and correct.

**P4-m2 — Abstract — "≈1.9σ Gaussian-equivalent" for p=0.030.** Two-sided p=0.030 → |z|=2.17; one-sided p=0.030 → z=1.88. State which convention is used.

**P4-m3 — PACS codes 98.80.-k, 98.62.Ai, 95.75.Mn.** APS retired the PACS system in 2010. PRD no longer requires nor recommends them.

**P4-m4 — Sec. III B, p. 3 — three-class output and softmax notation.** Equation (1) writes "256→3 (softmax)" inline. Softmax is on the logits, not a layer width; rewrite as "→ 256→3 logits; softmax over CW/CCW/NS."

**P4-m5 — Sec. III C — D₄-TTA description.** Two hold-out samples (N=1,558 and N=1,988) are described, then the conclusion is sample-noise. The hold-outs are small relative to 3.2M; a single ~10k-galaxy D₄ test would be more convincing.

**P4-m6 — Sec. IV C — "0.84 deg² per pixel" at NSIDE=64.** Correct value is 4π·(180/π)²/(12·64²) ≈ 0.839 deg², OK.

**P4-m7 — Hemisphere LEE statement.** Section IV E says "+3.3σ" in [0.5,0.6) bin and "All signal-hunt diagnostics … point to the same conclusion"; Appendix C says "+3.29σ." Pick one.

**P4-m8 — Appendix E — "axis-ratio cross-match" deferred.** A b/a cross-match with the DESI Legacy sweep is routine and should be in this paper if edge-on contamination is claimed to set the sensitivity floor at the ∼5–8% level.

**P4-m9 — Table I — "pp-shuffle" abbreviation undefined on first use.** State that "pp-shuffle" = per-pixel random-label permutation.

**P4-m10 — "Cohen's κ = 0.40."** For a 50/50 binary problem at 69.91% raw agreement, κ ≈ 2(0.6991−0.5) = 0.398, OK. Note this is in the "moderate" range and acknowledge.

---

## NITS

**P4-n1 — "primary cosmological estimators."** "Cosmological" is generous for a classifier-output asymmetry observable; "primary dipole estimators" is more accurate.

**P4-n2 — "demonopole-subtracted" (Appendix D).** Awkward neologism; use "monopole-subtracted."

**P4-n3 — Sec. VI A — "GZ1-dilution factor ≈0.63".** Source of 0.63 is not given (presumably 1 − 0.6991 contrast, or 2·0.6991 − 1 = 0.398; neither matches 0.63 directly). State the derivation.

**P4-n4 — Inline " " in "p_eq".** Use macros for consistent notation throughout.

---

## Length assessment

10 pages for a null result with this many estimator branches is appropriate; the paper is *not* too long. If figures (P4-M2) are added, expect 12–14 pages.

---

## Summary recommendation

**MAJOR REVISIONS**

The paper's central scientific position — a sub-percent null with a quantified leakage channel and an explicit injection-recovery floor — is a genuine and useful contribution at survey scale, and the equivariant TTA framing is honest about its limits. However, the manuscript fails several PRD-essential checks: an internally inconsistent "3.86×" suppression statistic that does not match Table II (E1), a load-bearing ℓ=2 cross-spectrum result in the abstract whose derivation is absent (E2), an arithmetic error in Table IV (E3), an inconsistent GZ1 cross-match N (E4), an inadequately defended choice of "headline" mask given that the so-called subsample mask is actually a superset (E5), absence of all figures (M2), a substantial uncited bibliography (M4), and an underived "factor of 6–12" exclusion vs. Shamir (M7). The joint χ²=161/38 on the canonical-mask bandpowers (M10) is not closed by the present monopole-only null and remains an undismissed problem. The author should resolve all ESSENTIAL items, supply the missing derivations and figures, and either rename or justify the mask hierarchy before this can be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report — P4 (Round R10v3p1) — SUPPLEMENTARY FINDINGS

A second pass with explicit attention to the checklist items A–J turned up the following issues not in the initial report.

---

## ESSENTIAL (new)

**P4-E7 — Abstract, p. 1 — Wrong table reference for null-procedure mapping (item D).**
The abstract reads: *"σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators; see Table II for the mapping of each result to its null."* But Table II is the **global CW fraction across catalog tiers** (no null-procedure column). The null-procedure mapping is in **Table I** (column "Null"). This is a load-bearing cross-reference in the abstract and it points to the wrong table. **Fix:** change "Table II" → "Table I".

**P4-E8 — Appendix C, p. 8 — Internally contradictory look-elsewhere arithmetic (item I).**
Two claims back-to-back: *"The direct-MC look-elsewhere test (N = 10,000 random-label shuffles) gives p_LEE ≤ 10⁻⁴"* and *"the conservative Bonferroni/BH penalty across ∼650 tested directions reduces post-LEE significance to < 1σ."* A *direct max-statistic MC* on label-shuffled realizations **is already trial-corrected** (by construction the maximum across all directions is computed in each null realization). Applying Bonferroni on top is over-correction. If the direct-MC genuinely gives p ≤ 10⁻⁴, then the post-trial significance is ≈ 3.7σ, not "<1σ". Conversely, if the per-direction MC was *not* maximized and Bonferroni is appropriate, then p_LEE ≤ 10⁻⁴ as a global statement is wrong. The two statements cannot both be correct. **Fix:** clarify what statistic the MC used and pick one (probably either the un-corrected per-direction p with Bonferroni, or a max-statistic MC without Bonferroni).

**P4-E9 — Abstract + Sec. VI A, pp. 1 and 6 — Sensitivity floor sample does not match the headline-null sample (item F).**
The headline null is the **−0.122σ MASTER result on Catalog C at N_spiral = 3,201,160** (full equivariant spiral catalog, subsample mask). The empirical falsification criterion is set from injection-recovery on the **HC-spiral subsample at N = 471,049** (Sec. VI A). These are different samples by a factor of ~7. The Fisher floor of 0.29% scales as 1/√N, so the floor on the full 3.2M sample is ~0.29%, but on the HC subsample is ~0.76% (which is why the empirical recovery hits 50% at A=0.75%). The paper applies the HC subsample's 0.75% threshold to the Catalog-C null as if they were the same sensitivity, then states a falsification criterion at "≥10⁷ galaxies … amplitude ≳0.75%" — but at 10⁷ galaxies the floor would be much smaller than 0.75%. **Fix:** clarify whether the falsification criterion refers to (a) any dipole detected on a Catalog-C-sized sample at A>0.75%, (b) the HC-subsample-equivalent sensitivity at 10⁷ galaxies (which gives a different number), or (c) something else. Currently the criterion is internally inconsistent.

**P4-E10 — Abstract + Sec. II/III, throughout — Ambiguous definition of "high-confidence" cut (item F).**
The abstract says *"471 049 high-confidence per-spiral after p_CW^eq > 0.9"*. Section VI A then uses *"HC-broad-0.6 (p_eq > 0.6, N = 949,584) and HC-strict (p_eq > 0.8, N = 624,660)"* — note the unsubscripted "p_eq" with no CW/CCW specifier. Read literally, "p_CW^eq > 0.9" would only retain galaxies the model strongly classifies as CW (excluding strongly-classified CCW galaxies entirely), introducing a massive CW bias. The intended cut is presumably max(P_CW^eq, P_CCW^eq) > 0.9, but this is never stated. **Fix:** define the HC cut explicitly. Given that the entire dipole sensitivity is computed on this subsample, the definition cannot be ambiguous.

---

## MAJOR (new)

**P4-M11 — Sec. IV B, p. 4 — Likely misattribution of the 9.5σ monopole to "GZ1 training-label CW excess" (item I).**
Section IV B lists candidate mechanisms for the 9.5σ monopole, naming first *"GZ1 training-label CW excess."* But Sec. II B states 67.6% of training labels derive from CE-ResNet predictions; GZ1 contributes only 6,637/26,636 ≈ 24.9%. CE-ResNet is by construction architecturally equivariant, so its labels should not carry a CW excess — meaning the monopole more plausibly originates in (a) the small GZ1 fraction acting on a fine-tuned head, or (b) the present ViT's residual orientation bias, or (c) a survey-photometric asymmetry, or (d) a downstream contamination of CE-ResNet's pseudo-labels by Galaxy Zoo human bias (acknowledged in Data Availability). The presentation in Sec. IV B does not match the 24.9%-of-labels attribution; the monopole-source narrative needs to be re-ordered or supported by an ablation (training without GZ1 labels). **Fix:** either present a clear ablation or replace the candidate-mechanism ordering with a more careful, percentage-weighted discussion.

**P4-M12 — Table V vs. Sec. IV B, pp. 4 and 8 — T8 acceptance threshold is too loose to detect the systematic that drives the entire leakage channel (item J).**
Table V (T8): *"CW/CCW balance: 50 ± 10%, Result 49.7%, PASS."* But the actual deviation is **9.5σ from 50%** at the binomial level, and this 0.26% offset is precisely the systematic that couples to mask geometry and produces the +3.64σ canonical leakage (the entire generative null of Sec. IV D). The bias-hardening suite's most relevant test, by its own threshold, cannot detect a systematic that drives the paper's principal leakage channel. **Fix:** tighten T8 to a binomial-significance-based threshold (e.g., "|f_CW − 0.5| < 3σ_binomial"), or explicitly acknowledge T8's insensitivity in the suite's discussion.

**P4-M13 — Sec. IV C vs. IV D — Subsample-mask Cℓ is ~10× smaller in amplitude than the canonical-mask Cℓ; this is the source of the "headline" choice but is not explained (item A).**
The subsample-mask post-MASTER ℓ=1 amplitude is C₁ = 1.494 × 10⁻⁶ (Sec. IV C). The canonical-mask post-MASTER ℓ=1 amplitude, with the same monopole subtraction, is 1.51 × 10⁻⁵ (Sec. IV D parenthetical). That is **a factor ~10 difference in C₁** between two masks on the same data. Going from canonical (fsky=0.490) to subsample (fsky=0.659) adds noisier pixels — yet the Cℓ amplitude **decreases by an order of magnitude**. This is anomalous. Either (a) the subsample mask drastically dilutes a real signal living in the canonical region, (b) the canonical mask carries a large mask-coupling residual that the subsample mask largely averages out, or (c) the two C₁ values are computed with different conventions and not strictly comparable. The reader has no way to assess (a)/(b)/(c) from the present text. **Fix:** explain the factor of 10 explicitly, with the same units/conventions on both sides, and (critically) show that the subsample-mask null isn't just an averaging-down of a real localized signal.

**P4-M14 — Throughout — "+3.64σ" repeatedly cited without the ≈1.9σ Gaussian-equivalent caveat (item E/F).**
The abstract acknowledges *"+3.64σ ... empirical rank p_MC = 0.030, i.e. ≈1.9σ Gaussian-equivalent"*, but the body subsequently quotes "+3.64σ" approximately 10 times (Sec. III A, IV C, IV D, V A, VII a, VII b, Appendix D) without the rank-equivalent qualifier. The factor-2 discrepancy between parametric z = Δ/σ_null and the empirical rank p indicates **heavy tails in the null distribution**, which means +3.64σ is misleading as a frequentist statement. The honest number is p_MC = 0.030 ≈ 1.9σ. **Fix:** every occurrence of "+3.64σ" in the body should be paired with "(p_MC = 0.030; ≈1.9σ Gaussian-equivalent)", or replaced by the empirical-rank number entirely. The current asymmetric treatment overstates the canonical-mask residual significance.

**P4-M15 — Bibliography order — References are not in citation order (item D).**
Body text first cites Shamir 2012 (as [4]) in Sec. I, then Shamir 2020 (as [1]), then Shamir 2022 MNRAS (as [3]). PRD style is citation-order numbering; here numbering appears either alphabetical-by-year-within-author or arbitrary. The numbering does not match the citation order in the body. **Fix:** renumber to citation order, or confirm with PRD that an alternative numbering scheme is permitted.

**P4-M16 — Sec. IV C — One-sided vs. two-sided p-value not declared (item E, partly noted as M6 but extended).**
*"0.43σ (p = 0.30 from the isotropic-null bootstrap)."* For two-sided Gaussian, |z|=0.43 → p≈0.667; for one-sided, p≈0.334. Neither matches 0.30 exactly. The 0.30 value implies a slightly different empirical-tail definition (perhaps the fraction of bootstrap realizations with amplitude exceeding the observed value, on a chi-distribution for the dipole-amplitude statistic, which is not Gaussian). **Fix:** state explicitly the bootstrap p-definition (chi-distributed amplitude, one-sided in amplitude space, etc.).

---

## MINOR (new)

**P4-m11 — Table II — Sign convention for "Dev. (σ)" not stated; Catalog C value shown as 9.5 not −9.5 (item A).** Caption defines Dev. = (f_CW − 0.5)/σ, which is −9.32 for Catalog C, but the table shows 9.5 (positive, magnitude only). State the convention or sign the entries.

**P4-m12 — Table II arithmetic precision (item A).** Catalog A Dev. = 0.0079/0.000279 = 28.32, table shows 28.8. Catalog B Dev. = 0.0040/0.000279 = 14.34, table shows 14.6. Catalog C Dev. = 0.0026/0.000279 = 9.32, table shows 9.5. All three are systematically ~1.5–2% higher than the recomputed values. Either σ is slightly smaller than 0.000279 (perhaps N is slightly smaller than 3,201,160 for the binomial denominator), or the rounded percentages are below the true values. **Fix:** show unrounded inputs.

**P4-m13 — Section IV A — "Mean classification confidence is 0.951, median 0.9997" (item A).** Median strictly greater than mean implies a strong **left-skew** (long low-confidence tail). Quote interquartile range or a histogram caption; readers cannot interpret "0.951/0.9997" without distribution context.

**P4-m14 — Section V A — "0.32% maximum regional asymmetry" (item H).** Region undefined. Per hemisphere? Per HEALPix pixel? Per quadrant? Without a region definition this is not directly comparable to Shamir's per-bin asymmetries.

**P4-m15 — Section VI A — "full amplitude" vs "half amplitude" convention not declared (item C).** "Fisher Poisson floor at 3σ is ∼0.29% full-amplitude" — dipole amplitudes are often half-peak; the factor of 2 matters for the comparison to Shamir's "∼3%". State the convention once at first use and use consistently.

**P4-m16 — Section IV C, eqn (3) — Definition of A_p uses spirals only, but the depth weight W_p in Appendix A uses N_all = CW+CCW+NS (item C).** The estimator multiplies a spiral-only signal by a depth weight that includes non-spirals. This is justifiable as a survey-completeness weight but should be stated as a modeling choice: the assumption is that local spiral density tracks total galaxy density up to a uniform fraction. Edge-on contamination (35% of edge-ons classed as not-spiral; Appendix E) violates this slightly.

**P4-m17 — Appendix D — Amplitude A = 4.55×10⁻³ described as "0.23% in f_CW units" (item A).** 0.23% = 2.3×10⁻³ is half of 4.55×10⁻³. Convention ambiguity (full vs half amplitude) appears here also. State explicitly.

**P4-m18 — Section II A — "Walmsley et al. … 8.7M galaxies" vs Smith42 dataset "8,474,688" (item H).** Walmsley GZ DESI quotes 8.7M, Smith42 ships 8.47M. Cross-match completeness is therefore ~97.4%; state explicitly and note any selection bias from the ~2.6% lost galaxies (likely faint-end or border cases that could be morphology-correlated).

**P4-m19 — Section III A bullet (i) and bullet (ii) — Different sample sizes for "primary" estimators (item I).** Estimator (i) uses full Catalog C N=3,201,160; estimator (ii) uses subsample-mask N=5,547,858 (which is the depth-weighted galaxy count including non-spirals, not a spiral count — but the inline text doesn't say so). The "n=5,547,858" in the abstract is therefore not directly comparable to "Catalog C N_spiral=3,201,160" but reads as if it were. **Fix:** annotate "n = depth-weighted galaxy count (Table I caption)."

**P4-m20 — Appendix D, "demonopole-subtracted A_p" (item J).** Same data field A_p that, elsewhere in the same appendix, is described both with and without monopole subtraction. The leg-proxy r values (+0.65, −0.73) are reported but the monopole-subtraction state is not consistently specified at each cross-power statement.

---

## NITS (new)

**P4-n5 — Eq. (B1) — λ = 0.5 is hard-coded without ablation.** A hyperparameter-sensitivity table would belong in Appendix B.

**P4-n6 — Section III B — "PNS, PCW, PCCW (softmax)" — softmax over a 3-vector with NS class explicitly listed.** Good design, but the relative class weighting in L_CE is not given. Class imbalance: NS ≈ 8% of training set (2,000/26,636) but 62% of catalog. State the class weights.

**P4-n7 — Software list — NaMaster cited as "[32]" in body but absent from software list explicit citation.** The software list says "NaMaster/pymaster" without citation; [32] is the actual reference. Add bracketed citation.

**P4-n8 — Section III C — "flip-swap correlation = 1.000" is by construction after Eq. (2) and not a measurement.** State this as definitional.

**P4-n9 — Section IV D — "From 2.30×10⁻⁵ to 1.51×10⁻⁵" — but the pre-MASTER value in Table IV is 1.696×10⁻², which is ~750× larger.** Different stages (decoupled vs pseudo-Cℓ) and units (dimensionless ratio vs steradian) should be explicit in a single normalization to avoid confusion.

**P4-n10 — "Subsample mask" appears 10+ times; "superset mask" once.** Once renamed (P4-M3 in initial report), update the abstract too.

---

## Brief summary of new findings

The second pass adds **4 ESSENTIAL items** (wrong-table reference in abstract; logical contradiction in hemisphere LEE; sample-mismatch between sensitivity floor and headline null; ambiguous HC-cut definition), **6 MAJOR items** (monopole-attribution to GZ1 vs CE-ResNet inconsistency; T8 threshold too loose to detect the systematic that drives the leakage channel; unexplained ~10× C₁ amplitude gap between subsample and canonical masks; under-qualified "+3.64σ" body usage; bibliography order; one-sided/two-sided p convention), and **10 minor/nit items** spanning convention statements, derivations, and notation.

The fresh-eyes pass focused on items A (arithmetic) and I (appendix-vs-body) found additional internal inconsistencies that were not detectable from a single read-through. The recommendation remains **MAJOR REVISIONS**, now with a strengthened case: in particular P4-E8 (LEE contradiction), P4-E9 (sample mismatch), and P4-M13 (factor-10 mask-amplitude gap that selects the "headline" result) materially affect the manuscript's primary scientific framing.