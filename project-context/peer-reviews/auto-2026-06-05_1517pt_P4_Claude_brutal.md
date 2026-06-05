# P4 auto-2026-06-05_1517pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (19000 chars)
**Wall time**: 501.0s

---

# Referee Report — Paper P4
**Manuscript**: Survey-Scale Galaxy Chirality with Equivariant TTA…
**Recommendation drafted at end. Reading: full PDF, all 10 pages.**

I read this as a real PRD submission. The thesis — "we measure no chirality dipole at sub-percent sensitivity on 3.2M spirals, and we explain a +3.64σ canonical-mask residual as a leakage systematic" — is potentially publishable, but the manuscript as submitted has multiple essential problems that prevent acceptance: internal numerical inconsistencies, a structural bait-and-switch between "headline null" and "headline systematic," an unjustified mask-of-choice, an under-disclosed dependence on CE-ResNet pseudo-labels, no figures whatsoever, and a sensitivity-floor argument that — when its own dilution factor is honestly applied — does not exclude the Shamir signals it claims to disfavor.

---

## ESSENTIAL findings

### P4-E1 — Internal numerical inconsistency: 2.05% vs +0.79% raw excess
**Section II–IV B, pp. 2, 4.** The abstract/Sec. IV B says "3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%." Table II lists Catalog A excess as +0.79% and Catalog C excess as −0.26%. Under the (CW−CCW)/(CW+CCW) = 2(p−0.5) convention, Catalog C −0.26% gives asymmetry −0.52% ≈ −0.53% (OK), but Catalog A +0.79% gives +1.58%, not +2.05%. The "3.86×" factor (2.05/0.53) is therefore inconsistent with the table from which it should be derived (would actually be 1.58/0.52 ≈ 3.04×). Either the abstract is wrong or Table II is wrong. **Fix**: reconcile and provide a single consistent number for the raw asymmetry, and re-derive the suppression factor.

### P4-E2 — σ–p inconsistency on the real-space dipole headline
**Sec. III A, Sec. IV C, p. 4.** The real-space dipole is reported as "+0.43σ (p = 0.30, isotropic-null bootstrap)." For a standard Gaussian one-sided test, P(Z > 0.43) ≈ 0.334; two-sided ≈ 0.668. p = 0.30 corresponds to ≈ 0.52σ one-sided or ≈ 1.04σ two-sided, not 0.43σ. The convention used (bootstrap rank? amplitude-only?) must be explicitly stated and the discrepancy resolved. As written, one of the two headline numbers in the abstract is internally inconsistent.

### P4-E3 — Training-label independence is overstated
**Sec. II B, p. 2.** "67.6% of training labels derive from CE-ResNet predictions." The paper then trains a ViT on these pseudo-labels and reports a catalog that — by construction — partially reproduces CE-ResNet. The independent GZ1 cross-match yields **κ = 0.40 (fair only)** and 69.91% accuracy. Yet the abstract frames this as "advancing beyond CE-ResNet" and the paper offers the catalog as a community resource. The classifier is essentially a CE-ResNet distillation with a NOT_SPIRAL head and a GZ1-flavored bias. This must be stated plainly in the abstract, not buried. **Fix**: revise abstract/§V B to state the pseudo-label fraction and the κ = 0.40 floor up-front.

### P4-E4 — Sensitivity floor does not actually exclude Shamir
**Sec. VI A, p. 6.** The paper's own dilution-corrected threshold is "**true-underlying** threshold ∼1.88%" (from g = 2a−1 = 0.398 for a = 0.6991). Shamir's claimed signal is ∼2–4%. By the paper's own arithmetic, this brackets a 50%-recovery threshold and does **not** robustly exclude the lower half of Shamir's claimed range. Nevertheless the abstract says the result is "inconsistent in amplitude with Shamir's claimed ∼3% signal by a factor of ∼6–12 under the present pipeline." That factor ignores the dilution caveat the paper itself just disclosed. **Fix**: state the dilution-corrected exclusion honestly, or remove the "factor of 6–12" claim. The two cannot coexist.

### P4-E5 — Internal version-history language in body text
**Sec. IV D, p. 4.** "The canonical-mask direct-MC ℓ=1 value of +3.64σ … were interpreted in **earlier paper versions** as mask-geometric leakage of the global 9.5σ monopole." This is a review-log artifact. Remove. Likewise repeated "non-headline, systematics-attributed" reads as post-hoc rebranding language inserted during revision — tighten or drop.

### P4-E6 — Zero figures
**Entire paper.** This is a methods paper claiming an angular dipole measurement, a power-spectrum reduction, a mask-leakage generative null, an injection-recovery sweep, multiple multipole bandpowers, and a 5-anchor systematic study. There are **no figures at all**: no sky map of A_p, no MASTER C_ℓ vs ℓ, no monopole-leakage null distribution histogram, no injection-recovery curve, no apodization comparison, no peq-stratified dipole. PRD methods papers need visualization. The absence of plots prevents a referee from cross-checking the tables visually and is sufficient on its own for major revision. **Fix**: minimum required — (i) Mollweide A_p map; (ii) Cℓ vs ℓ with null band on both masks; (iii) injection-recovery curve; (iv) generative-null histogram with measured value marked.

### P4-E7 — Bait-and-switch on what the "headline" is
**Abstract vs. Sec. VII a, pp. 1, 6.** Abstract: "The headline scientific result is a null ℓ=1 chirality-dipole observable on the analysis subsample mask: …−0.122σ." Conclusions §VII a: "**Headline finding: a quantifiable monopole-mask leakage channel.**" These are two different headline claims. The paper needs to commit to one. The current structure looks like the paper was originally a +3.64σ detection that has been retitled as a null without a clean rewrite. **Fix**: pick one headline framing and propagate consistently through title, abstract, and conclusions.

### P4-E8 — Choice of "subsample mask" as headline is unmotivated
**Sec. III A, Sec. IV C–D, pp. 3–4.** The headline null is on the "strict-superset subsample mask" (fsky = 0.659, n = 5,547,858 *weighted*), but the canonical analysis sample is 3.2M spirals on fsky = 0.49. The subsample mask is **larger** in fsky and includes non-spiral-weighted pixels, while the canonical mask is what previous chirality analyses would use. The paper offers no principled reason — derived **before** seeing the answers — for promoting the subsample-mask result to headline while demoting the canonical-mask result to "systematic." The natural reading is that the headline mask was chosen because it gave the desired null. **Fix**: provide a pre-registered mask-selection criterion, or report both as primary with equal weight and no rhetorical asymmetry.

### P4-E9 — σ from different nulls juxtaposed in tables without per-cell qualifier
**Table I, Table III, Table IV, p. 4–5.** The abstract adds a global "not directly comparable" note, but Table I shows columns "Null" and "σ" side by side with values from MC label-shuffle, isotropic bootstrap, monopole-only generative null, max-stat MC, and pp-shuffle. A reader scanning Table I will read −0.122, +0.43, +3.64, +1.68 as commensurable. Per the review instruction set, this is essential. **Fix**: add an explicit per-row footnote tying σ to its null, or replace σ with the null-conditioned p-value, or split the table by null type.

---

## MAJOR findings

### P4-M1 — Title overload
The title runs ~50 words with three quantitative claims (a null, a leakage channel, a residual). PRD titles should state the result, not the entire abstract. **Fix**: a 12–18-word title capturing the headline (whichever is chosen per E7).

### P4-M2 — "Falsification criterion" is rhetorical, not statistical
Abstract & §VII d: "A future survey detecting a chirality dipole at σ > 5 with full amplitude ≳ 0.75% would falsify the present null." A null cannot be "falsified" by a higher-amplitude detection in a different survey/pipeline unless a matched re-analysis is performed. The paper itself notes that a matched Ganalyzer reanalysis was not done. The "falsification criterion" should be stated as: a matched-pipeline re-analysis of DESI Legacy that detects A > [threshold]. As written it is unfalsifiable.

### P4-M3 — Cohen's κ = 0.40 is underplayed
§II B presents κ = 0.40 as a "conservative accuracy floor." Standard interpretation: κ = 0.40 is "fair" agreement, barely above chance for a balanced binary task. This should be discussed in the abstract or at minimum the abstract's claim of accuracy floor 69.91% needs the κ value attached.

### P4-M4 — Hemisphere asymmetry swing from p_LEE ≤ 10⁻⁴ to < 1σ is suspicious
§IV E and Appendix C: "direct-MC pLEE ≤ 10⁻⁴" is then "reduced to < 1σ" by Bonferroni/BH across ~650 directions. A Bonferroni penalty of order 650 turns 4σ into ~3σ at most, not <1σ. **Fix**: show the actual LEE-corrected number (z-value or post-LEE p) and reconcile with the bound. The current language switches between "rejection of the random-label null" and "attributed to systematic," which is not a quantitative LEE calculation.

### P4-M5 — Multipole bandpower interpretation is opaque
Table III shows ℓ_eff = 4 at +6.097σ labeled "Mask-coupled monopole leakage" and ℓ_eff = 9, 14, 19, 24 at +2.2–2.6σ each labeled "Residual mask coupling." But the headline ℓ = 1 mode on the **same** canonical mask is +3.64σ (Sec. IV D) — also mask-coupling-attributed. Why does the same systematic produce qualitatively different σ at every multipole bin, all branded "residual mask coupling"? Either give a model of the systematic that predicts the multipole pattern or stop labeling each row with the systematic.

### P4-M6 — Cross-spectrum r = −0.65, σ = −2.89 is overstated as a "smoking gun"
Appendix D b-c-g: a −2.89σ cross-correlation against permutation null is interpreted as confirming the leakage explanation. −2.89σ is mild evidence, not confirmation. Soften "smoking gun"-style framing in §IV D / §VII a.

### P4-M7 — Bibliography entries [1]–[3] need checking
Refs [1], [2], [3] are all Shamir. Ref [2] is given as PASJ 74, 1114 (2022); ref [3] as MNRAS 516, 2281 (2022). Verify these are not the same paper with different metadata. Reviewers should not be the ones doing this check. Also, the order [1]=2020, [2]=2022, [3]=2022, [4]=2012 is non-chronological and the in-text citation "Shamir (2012, 2020, 2022) [4]" only points to one of them, which is misleading.

### P4-M8 — 9.5σ monopole is shrugged off
§IV B: a 9.5σ deviation of the CW fraction from 0.5 is dismissed as "a classifier artifact, not a physical signal" because it is "spatially uniform." But a 9.5σ monopole is exactly what was invoked to source the +3.64σ canonical mask leakage in §IV D. The paper cannot simultaneously argue (i) the monopole has no spatial structure and (ii) the monopole couples through patchy mask geometry to produce a +3.64σ ℓ = 1 signal. Reconcile.

### P4-M9 — "Subsample mask" weights are not transparent
Table I caption defines N_map_weighted = Σ N_all,p but the body never explains how a 5.55M weighted-sum mask of 8.47M total objects relates to a 3.2M-spiral sample. The reader cannot tell what is being deconvolved. **Fix**: pseudo-code or explicit equation for the field input to NaMaster on the subsample mask.

### P4-M10 — Edge-on dilution is asserted but unbounded
§VI A, Appendix E: 65.7% of edge-on (b/a < 0.3) objects receive CW/CCW labels; "5–8% sensitivity penalty" is asserted without derivation. For a chirality measurement this is load-bearing. Provide the derivation or remove the quantitative number.

### P4-M11 — "8 bias tests all pass" is meaningless without thresholds derived from the science target
Appendix B / Table V: thresholds (r > 0.80, > 80%, < 0.10, etc.) are chosen ad hoc, and the paper itself admits they are "generous relative to the 0.75% empirical sensitivity floor." Then their passing tells the reader essentially nothing about whether the catalog can support a 0.75%-amplitude isotropy test. **Fix**: replace with bias bounds at the science-required precision, or remove this table.

---

## MINOR findings

### P4-m1 — Repeated "non-headline, systematics-attributed" phrase
Used three times verbatim. Consolidate.

### P4-m2 — "canonical-N MASTER" terminology is confusing
"Canonical-N" suggests a number N; it actually means "applied to the canonical mask." Rename.

### P4-m3 — Abstract's "Note: σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators" is welcome but does not absolve P4-E9. Reinforce at each table.

### P4-m4 — "PACS numbers: 98.80.-k, 98.62.Ai, 95.75.Mn"
PACS has been deprecated by PRD-style journals; PRD uses subject headings or omits codes. Remove or replace with PhySH.

### P4-m5 — Cosine-annealing-warm-restart with T0=10, Tmult=2 and 80 epochs (Appendix B)
T0=10, Tmult=2 across 80 epochs gives restarts at 10, 30, 70 epochs — i.e., the production best checkpoint at epoch 79 was just before a restart. Either this is a coincidence worth noting, or the scheduler description is wrong.

### P4-m6 — Mean confidence 0.951, median 0.9997
The median > mean by 5 percentage points indicates a long left tail of low-confidence galaxies; this should be stated more carefully because it informs the 471k HC subsample.

### P4-m7 — Subsample-mask MASTER input field undisclosed
Appendix A says "monopole subtraction is performed at the data-vector construction step." OK — but is the **subsample** mask field input the same A_p as the canonical mask field, or is it monopole-subtracted differently? State explicitly.

### P4-m8 — "DESI Legacy DR8 brick-boundary classifier artifacts (confirmed by vanishing to −0.03σ in the brick-interior subsample)"
This is an interesting claim that should be in the body, not Appendix C, since it bears on §IV's reliability across the survey.

### P4-m9 — Reference [11] (Land et al. 2008) is cited nowhere I can find in the body text. Check.

### P4-m10 — "headline" appears 12+ times. Reduce to ≤ 3.

### P4-m11 — "subsample mask" defined as "strict-superset" — superset of what? Define unambiguously on first use.

### P4-m12 — fsky = 0.49005 quoted to five significant figures while other fsky values are quoted to three. Standardize.

### P4-m13 — Software list (Appendix end) lists "timm [39]" and "NaMaster/pymaster" but no version for NaMaster except in Appendix A ("pymaster 2.6"). Add to software list.

---

## NITS

- **P4-n1**: "Headline" in conclusions §VII has lowercase "headline" but the section opens "*a. Headline finding*". Standardize capitalization.
- **P4-n2**: Page 4 Table III: "Joint χ²/dof (38 bandpowers)" but Table III shows only 5 bandpowers and one single mode. The 38 number is unexplained.
- **P4-n3**: Eq. (B1) uses bold **p** and italic *S*; consistency with notation elsewhere needs checking.
- **P4-n4**: "≈1.9σ Gaussian-equivalent" in abstract is from p = 0.030 (one-sided ≈ 1.88σ). Standard rounding gives 1.88σ, not 1.9σ. Minor.
- **P4-n5**: Repetition: "The Catalog C residual (9.5σ from 0.5000…)" — minor.
- **P4-n6**: "0.84 deg²" for HEALPix Nside = 64: actual mean pixel area is 4π/49,152 sr = 0.839 deg². OK.

---

## Length recommendation

The actual scientific content — a null on one mask + a +3.64σ residual on another + a leakage model — fits in **6 PRD pages with figures**. The current 10-page version is padded with hedge phrases, multiply-stated headline framings, and an appendix of diagnostics that all conclude "still consistent with systematic." Recommended maximum: **7 PRD-formatted pages including 4 figures**.

---

## Summary recommendation

**REJECT** (resubmission encouraged after major restructuring).

The underlying measurement program — a transformer-based chirality catalog of DESI Legacy with equivariant TTA, MASTER deconvolution, and a generative monopole-leakage null — is interesting and within PRD scope. But this manuscript fails first-pass PRD acceptance for compounding reasons: (i) internal numerical inconsistencies between the abstract and Table II (P4-E1) and between the quoted σ and p (P4-E2); (ii) a headline mask whose selection is unmotivated and looks results-conditioned (P4-E8); (iii) training labels 67.6% inherited from CE-ResNet combined with a κ = 0.40 GZ1 cross-match that the abstract does not disclose (P4-E3); (iv) the paper's own dilution math (1.88% true-underlying threshold) does not actually exclude the Shamir signal class that the abstract claims to disfavor "by a factor of 6–12" (P4-E4); (v) zero figures in a methods paper of this scope (P4-E6); (vi) a structural bait-and-switch between "headline null" (abstract) and "headline finding: leakage channel" (conclusions) (P4-E7); (vii) review-log language ("earlier paper versions") still present in body text (P4-E5). I encourage the authors to commit to a single headline framing, perform a pre-registered or principled mask selection, honestly state the dilution-corrected exclusion against Shamir, add the required figures, and resubmit.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report — Second Pass (Fresh-Eyes Re-Examination)

I went back through the paper with the checklist and found a substantial number of additional issues, many arithmetic. The original review captured the structural/framing problems but underweighted numerical cross-checking. The new findings reinforce the REJECT recommendation and add additional load-bearing arithmetic failures.

---

## ADDITIONAL ESSENTIAL findings

### P4-E10 — Catalog A vs Catalog C conflation in the leakage demonstration
**Abstract; Sec. IV C, IV D; Table IV.** The "99.3% leakage" demonstration is internally muddled across catalogs:
- Sec. IV C says **Catalog A** (raw) produces "+6.48σ pre-MASTER pseudo-Cℓ in the lowest bandpower" from a **+0.79% CW excess** (per Table II).
- Sec. IV D says the monopole-only null is run "at p_CW^global = 0.4974" — that is the **Catalog C** monopole value (a CCW excess, +0.26%, +9.5σ in Table II).
- Table IV's "data" entry 1.696×10⁻² is the pre-MASTER pseudo-Cℓ; only +1.68σ above the monopole-only null.
- The abstract says the monopole-only null "reproduces 99.3% of the observed pre-MASTER pseudo-C₁".

If the +6.48σ pre-MASTER value is Catalog A's, then the "99.3% reproduction" test using Catalog C's monopole (p=0.4974) is testing the wrong monopole — a CCW excess generating a CW-leg pre-MASTER. Catalog A's monopole is ∼3.04× larger (per Table II, ignoring P4-E1's numerical confusion), and a linear-leakage estimate would predict ∼3× larger pseudo-C₁. The paper does not run the monopole-only null on the Catalog A monopole, where the leakage claim would actually need to be demonstrated. **Fix**: run the binomial-monopole null at p_CW = 0.5079 (Catalog A) and confirm it reproduces +6.48σ pre-MASTER; otherwise the headline-leakage story applies only to Catalog C.

### P4-E11 — Training-label count is internally inconsistent
**Sec. II B, p. 2.** The paper lists: GZ1 6,637 + CE-ResNet 17,153 + synthetic 2,000 = **25,790 labels**. The text then says "The combined training set contains **26,636 images**." 846 labels are unaccounted for. **Fix**: reconcile the totals or disclose the missing source.

### P4-E12 — "67.6% of training labels derive from CE-ResNet" matches neither denominator
**Sec. II B, p. 2.** With the listed counts:
- 17,153/25,790 = **66.5%**
- 17,153/26,636 = **64.4%**
- 67.6% requires a denominator of 25,375 — not given anywhere.

This is a load-bearing number because it controls how much "independent ground truth" the catalog claims. **Fix**: state which denominator gives 67.6% (or correct it), and report the κ = 0.40 GZ1 result against the actual independent-label fraction (which is at most 25%).

### P4-E13 — "+3.64σ" headline number is the moment-ratio, while the empirical rank gives only ~1.9σ
**Abstract; Table I; Sec. IV D; Sec. VII a–b.** The abstract reports "+3.64σ ... empirical rank p_MC = 0.030, i.e. ≈1.9σ Gaussian-equivalent". These are two different statistical statements:
- **Moment-ratio z**: (data − null_mean)/null_std = 3.64σ
- **Empirical rank**: 15/500 = 0.030 → 1.88σ Gaussian-equivalent

A factor-of-~2 discrepancy between moment-ratio and rank p-value is exactly the signature of a **heavy-tailed null distribution**. The paper's headline "+3.64σ" leverages a Gaussianity assumption that the empirical null itself violates by a factor of 2. The honest single-number summary is **1.9σ** (empirical), not 3.64σ. Yet "+3.64σ" appears in the title, abstract, Table I, and conclusions, while "1.9σ" appears only as a parenthetical in the abstract.

This is significant because the entire systematic-attribution narrative is built around treating "+3.64σ" as the residual to be explained. If the actual significance is ∼1.9σ, the whole Appendix D 5(6)-anchor edifice is excessive: a 1.9σ excess on a patchy mask needs no Appendix D at all. Conversely, if the moment-ratio "3.64σ" is the honest number, the null distribution non-Gaussianity needs to be discussed because it threatens the −0.122σ subsample-mask null as well.

**Fix**: pick one significance convention (preferably empirical rank), apply consistently across all estimators in Table I, and propagate.

---

## ADDITIONAL MAJOR findings

### P4-M12 — Appendix A C₁ magnitude is 10× larger than Table III's ℓ=1
**Appendix A vs Table III.** Appendix A: "Monopole subtraction reduces decoupled C₁ at ℓ=1 from 2.30×10⁻⁵ to 1.51×10⁻⁵". Table III row 1: ℓ=1 single mode C₁ = **1.494×10⁻⁶ sr**. These differ by a factor of **10.1**.

Reading carefully, Appendix A is reporting the canonical-mask value (which yields +3.64σ), while Table III row 1 is the subsample-mask value (which yields −0.122σ). If so, the canonical-mask C₁ is 10× larger than the subsample-mask C₁ — directly relevant to the leakage interpretation and worth highlighting. But neither the body nor the appendix says this explicitly; a reader has to infer from "the canonical-mask number" at the end of Appendix A. **Fix**: add a sentence comparing the two masks' C₁ values and how this comparison supports (or constrains) the leakage explanation.

### P4-M13 — Table II "Dev. (σ)" column is systematically inflated by ~2-3%
**Table II, p. 4.** With σ = √(p(1−p)/N) at N = 3,201,160 and p ≈ 0.5, σ = 0.000279 (as stated). Then:
- A (raw): |0.0079|/0.000279 = **28.32σ**, paper says 28.8 (off by 1.7%)
- B (calibrated): |0.004|/0.000279 = **14.34σ**, paper says 14.6 (off by 1.8%)
- C (equivariant): |0.0026|/0.000279 = **9.32σ**, paper says 9.5 (off by 1.9%)

To get 28.8, 14.6, 9.5 simultaneously, σ would need to be ≈0.000274, corresponding to N ≈ 3.33M — larger than the quoted N_spiral = 3.21M. The σ column either uses a different N (not declared) or contains errors. **Fix**: either change σ to 0.000274 with the implied N declared, or recompute the Dev column with σ = 0.000279.

### P4-M14 — Table III "Joint χ²/dof = 161.2/38" lists 38 bandpowers but shows only 6
**Table III, p. 5.** The χ² test claims 38 degrees of freedom. The table displays 6 modes: ℓ=1 single + 5 bandpowers (ℓ_eff = 4, 9, 14, 19, 24). With the 5-band values listed (+6.097, +2.232, +2.626, +2.229, +2.470), I compute Σz² ≈ 60.1, far below 161.2. To reach 161.2 either the missing 32 bandpowers contain comparable excess power (in which case the table is misleading by suppression) or the χ² is computed differently. **Fix**: show all bandpowers or explain how 161.2 is obtained from the displayed 6.

### P4-M15 — "Five-anchor systematic analysis" enumerates six anchors
**Sec. IV D, p. 4–5.** The text reads: "five-anchor systematic analysis of the +3.64σ canonical-mask residual (**cross-spectrum, leg-proxy, density-stratified, boundary-distance, full-catalog injection, block-bootstrap WLS fit**)". That parenthetical lists six items. Appendix D headers (a)–(g) are: apodized-mask, multipole-spectrum, leg-proxy, density-stratified, boundary-distance, WLS fit, operational conclusion = 6 anchors + conclusion. **Fix**: either rename to "six-anchor" or remove one item from the parenthetical list to match the stated count.

### P4-M16 — Fisher floor uses fsky = 0.46, matching neither analysis mask
**Sec. VI A, p. 6.** The Fisher Poisson floor derivation uses "fsky = 0.46". But the canonical mask has fsky = 0.49005, and the subsample mask has fsky = 0.659. No mask in the paper has fsky = 0.46. If the Fisher floor used fsky = 0.49 (canonical), the threshold would be 0.29% × √(0.46/0.49) = 0.28% — a ∼2% effect — but the choice should be motivated. **Fix**: state which mask the Fisher floor refers to, or correct.

### P4-M17 — "Maximum regional asymmetry 0.32%" is undefined in the main text but anchors the Shamir-exclusion claim
**Sec. V A, p. 5.** The factor-of-"6–12" exclusion of Shamir's 2–4% signal is derived as 2–4% / 0.32% ≈ 6–12. But "0.32% maximum regional asymmetry" is defined nowhere in the paper — what region? what threshold? hemisphere? quadrant? pixel? — and does not appear in any table. **Fix**: define the 0.32% number explicitly with a region size, or replace the exclusion factor with the dilution-corrected sensitivity floor (P4-E4 in original review).

### P4-M18 — "471,049 high-confidence after p_CW^eq > 0.9" in abstract has no clear referent in the body
**Abstract vs Sec. VI A and Appendix E.** The abstract specifies "471 049 high-confidence per-spiral after p_CW^eq > 0.9". The body's HC subsample sizes are: HC-broad-0.6 (N=949,584) and HC-strict at p_eq > 0.8 (N=624,660). The 471,049 number appears in Sec. VI A as "HC-spiral subsample" with no threshold attached. There is no body-text confirmation that 471,049 corresponds to p_eq > 0.9. **Fix**: state the threshold explicitly where the number first appears in the body.

### P4-M19 — The 9.5σ monopole cannot be simultaneously "spatially uniform" and the source of mask-coupled leakage
**Sec. IV B vs Sec. IV D, p. 4.** §IV B argues the 9.5σ monopole is harmless because "all 7 equatorial coordinate slabs within 0.5% of 50/50" — i.e., spatially uniform. §IV D then argues this same monopole "couples through patchy survey-mask geometry to inflate the raw pseudo-Cℓ at ℓ=1". 

These cannot both be load-bearing claims. A perfectly uniform monopole on a patchy mask DOES leak into ℓ=1 via the mode-coupling kernel — that is real and is the leakage mechanism. But then the "spatial uniformity" defense in §IV B does not exclude a dipole; it merely says the monopole is uniform, while the patchy mask still produces the leakage. §IV B reads as if uniformity makes the monopole harmless, which it does not. **Fix**: rewrite §IV B to say the monopole is uniform, and explicitly state that this uniformity is consistent with (not protective against) the §IV D mask-coupling leakage.

### P4-M20 — Augmentation appears to hurt accuracy
**Appendix B, p. 7.** "Headline 93.7% three-class accuracy (with augmentation active); post-hoc evaluation without augmentation yields **94.9%**." Augmentation increasing test-time accuracy by removing it is unusual and suggests either (a) the validation set is also augmented during training-time eval, or (b) the augmentations are too aggressive (off-distribution). For a chirality classifier in particular, certain augmentations (random rotation, flip) may be confounded with the label itself. **Fix**: clarify the eval protocol; if val is augmented during training-time eval, that is non-standard and should be disclosed.

### P4-M21 — Recall asymmetry of 1.2 pp does not predict the quoted raw bias
**Appendix B; Sec. IV C; Table II.** With CW recall 93.8% and CCW recall 92.6%, the implied observed CW fraction under balanced truth and symmetric false-positive rates is 0.938/(0.938+0.926) = 0.5032, giving a 0.32% excess and a raw asymmetry A = 2(0.5032−0.5) = 0.64%.

But the paper claims:
- Catalog A raw excess +0.79% (Table II)
- Catalog A raw asymmetry +2.05% (Sec. IV B)

The "predicted from recall" value 0.32%/0.64% does not match either. **Fix**: either the recall numbers are wrong, or the raw-excess numbers are wrong, or there is a structural confound (e.g., false-positive rate asymmetric) that needs to be exposed.

### P4-M22 — "~650 hemisphere directions" for LEE conflicts with 10° hemisphere-pair count
**Sec. VI; Appendix C.** Appendix C: "Testing all hemisphere-pairs at 10° increments: maximum asymmetry 3.05σ." 10° spacing on the sphere gives ≈4π/(10°)² = 412 pixels, or ≈206 antipodal pairs. The text §VI: "Bonferroni/BH across ∼650 directions." Neither 412 nor 206 is ~650. **Fix**: state the LEE pixelization explicitly.

### P4-M23 — p_LEE ≤ 10⁻⁴ and "<1σ post-Bonferroni" are incompatible
**Sec. VI; Appendix C.** The text states the direct-MC LEE-corrected p-value is ≤10⁻⁴ (corresponding to ≈3.7σ post-LEE), but then says "the conservative Bonferroni/BH penalty across ∼650 tested directions reduces post-LEE significance to <1σ." 

These are both supposed to be LEE corrections of the same hemisphere-maximum statistic. They cannot disagree by ~3σ unless they are testing different statistics. The most charitable read is that the direct-MC rejects the random-label null (because of the residual classifier monopole) while Bonferroni on the dipole interpretation gives <1σ — but the paper does not say this cleanly. Currently both numbers appear as "the LEE significance". **Fix**: distinguish the two tests cleanly; do not present them as if they were redundant LEE corrections.

### P4-M24 — Real-space dipole "isotropic-null bootstrap" σ→p mapping not specified
**Sec. IV C, p. 4.** The "0.43σ (p = 0.30)" mapping (already flagged in original P4-E2) is consistent with a 3-DOF chi-distribution null on the dipole amplitude vector. Under chi₃ with appropriate scaling, p = 0.30 at z = 0.43 is plausible. But the paper never states whether the σ is computed as (A_meas − ⟨A_null⟩)/std(A_null), or as the quantile-equivalent Gaussian z of the bootstrap rank p-value. Different choices give different numbers for the same data. **Fix**: state the σ→p convention used for the isotropic bootstrap and apply consistently.

---

## ADDITIONAL MINOR findings

### P4-m14 — Spiral fraction arithmetic small mismatch
3,201,160 / 8,474,531 = 37.774% (rounds to 37.77%), but paper says 37.78%. Trivial.

### P4-m15 — "30× extension" of Iye et al. is loose
3.2M / ∼1.27×10⁵ = 25×, not 30×. Trivial.

### P4-m16 — Appendix A: "monopole subtraction reduces ... and increases σ from +1.85 to +3.64"
This implies the un-monopole-subtracted canonical-mask result was +1.85σ. This number does not appear elsewhere. Worth tabulating: pre-MASTER +1.68σ, pre-monopole-subtraction post-MASTER +1.85σ, post-both +3.64σ. Currently scattered.

### P4-m17 — Cosine warm-restart schedule predicts restarts at epochs 10, 30, 70
With T₀=10, T_mult=2, restarts at 10, 30, 70, 150. Epoch 79 (the best checkpoint) is 9 epochs into a fresh restart cycle (cycle starts at 70). Just-post-restart selection of the "best" checkpoint is unusual; could be coincidence. (Original m5 noted this; this expands the arithmetic.)

### P4-m18 — Mean confidence 0.951, median 0.9997
Median exceeds mean by ~5 pp. Standard interpretation: long lower tail. The HC subsample at peq > 0.9 (471,049 / 3,201,160 = 14.7%) is a small fraction of spirals, consistent with this skew. But the paper does not show the confidence histogram, and one cannot independently verify the 471,049 number from the catalog statistics provided.

### P4-m19 — N_MC discrepancy real-space vs MASTER
Abstract gives real-space N_MC = 10,000 (bootstrap) and MASTER N_MC = 500 (label-shuffle). The factor-20 difference is not explained; MASTER is the more expensive computation but 500 trials gives a granular p-value (minimum 1/500 = 0.002 ≈ 2.9σ Gaussian). At an empirical p of 15/500 = 0.030, the 1σ uncertainty on the rank is √(15·485/500)/500 ≈ 0.0076 → relative uncertainty 25%. For a primary-cosmological-estimator p-value this is coarse. Noted but minor.

### P4-m20 — "Mean classification confidence is 0.951, median 0.9997" with median 0.9997
A median of 0.9997 implies half the catalog has confidence > 99.97% — i.e., the model is extremely overconfident on most galaxies. This is consistent with no calibration, but it conflicts with §VII T7 "Calibration qualitative PASS" in Table V. Minor framing issue.

### P4-m21 — Spiral-fraction "consistent with magnitude-limited survey expectations" is unsupported
**Sec. IV A.** No reference value or range for the expected DESI-Legacy r<19 spiral fraction is cited. Hand-wave hedge.

### P4-m22 — "0.32% maximum regional asymmetry" should not be hand-waved
Per P4-M17, this number anchors the Shamir comparison. Currently undefined.

---

## ADDITIONAL NITS

### P4-n7 — Table I row "(iv) hemisphere LEE (MC)" reports "p_LEE ≤ 10⁻⁴" in the σ column
The σ column should contain σ, not p. Mixing the two types of statistic in the same column violates the column header. **Fix**: split into σ and p columns, or footnote the conversion.

### P4-n8 — Table I "Null" column repeats "pp-shuffle" three times
"pp-shuffle" is presumably "per-pixel-shuffle" — define on first use.

### P4-n9 — Eq (B1): permutation matrix S
S permutes only the (CW, CCW) entries of a 3-vector, leaving NS unchanged. State explicitly to avoid ambiguity.

### P4-n10 — Reported σ at ℓ=1 (subsample, MASTER) is "−0.122σ" but the table lists 1.494 and 1.546 with σ 0.429; my recomputation gives −0.121σ. Round/truncation choice, trivial.

### P4-n11 — Table II "Dev. (σ)" header should arguably use sign-convention symbol since all three values are reported as positive magnitudes but the Catalog C residual is a CCW excess (negative). The "Dev." column hides the sign.

### P4-n12 — "Catalog A (raw) shows a 2.31σ real-space dipole" — but Table I shows real-space dipole only for Catalog C (+0.43σ). The Catalog A and Catalog B real-space dipole values are quoted in body text only. Either include in Table I or footnote that the table is Catalog C only.

### P4-n13 — "1.6× the spiral coverage" comparison to CE-ResNet is presented as a novelty advantage. CE-ResNet is 1.95M; this paper's Catalog C spiral count is 3.20M; ratio = 1.64× ≈ 1.6× ✓. But 1.6× is modest. Frame honestly.

### P4-n14 — "All three tiers share 8,474,531 rows in Apache Parquet format" — but Catalog A/B/C have different fractions of spirals/NS classifications, so they do not "share" classifications, only row count. Minor wording.

### P4-n15 — Sec. IV E: "+3.3σ signal in the 1.87M-galaxy [0.5, 0.6) confidence bin" vs Appendix C: "+3.29σ". Round-tripping, trivial.

---

## Updated summary recommendation

**REJECT.** The arithmetic re-audit strengthens the case substantially. In addition to the original 9 essential findings, the second pass identifies:

- **P4-E10**: The 99.3% leakage demonstration uses the wrong catalog's monopole.
- **P4-E11/E12**: The training-label arithmetic is doubly inconsistent (count and percentage).
- **P4-E13**: The headline "+3.64σ" is the moment-ratio z, but the actual empirical rank gives only ~1.9σ. A factor-of-2 discrepancy in the central canonical-mask number suggests the empirical null has heavy tails, which is itself a result the paper does not engage with. This same heavy-tailed null could change the −0.122σ headline subsample-mask "null" as well (if heavy-tailed, the rank-equivalent significance could differ).

The arithmetic-level inconsistencies (Table II σ off by 2-3%; Appendix A vs Table III off by 10×; training labels missing 846; recall asymmetry not predicting raw bias; six-vs-five anchors; 38-vs-6 bandpowers) form a pattern showing that the manuscript has not been arithmetically reconciled across its sections. This is independent of the framing issues identified in the first pass.

For a paper whose entire scientific claim is a sub-percent measurement against a structured systematic, the level of within-paper numerical drift is incompatible with PRD-level rigor. The authors should reconcile all numerics, commit to one significance convention (empirical rank preferred), rerun the leakage null on the Catalog A monopole, and resubmit.