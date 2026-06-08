# P1B auto-2026-06-08_1354pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (9542 chars)
**Wall time**: 465.5s

---

# Referee Report: P1B
## "Technical Verification Companion to the ECH Spin-Torsion Program..."

---

## Overall Assessment

This is a "technical verification companion" to a theory paper that is **explicitly marked as "in preparation"** (ref. [1]). It documents three analyses (with a fourth slipped in unannounced) and then proceeds to disclaim what each analysis can and cannot establish. The level of disclaiming is so extensive — the abstract itself says the MCMC carries "no torsion modifications" and "is not evidence for or against the ECH spin-torsion framework," the NaMaster MC is "not a sky-detection significance claim," and the ALP check is "not a distinctive ECH prediction" — that very little load-bearing positive content remains. After honest scoping, this paper documents (i) a stock-CAMB null result of ∆N_eff consistent with zero (uninformative w.r.t. the framework it purports to verify), (ii) a pseudo-Cℓ pipeline self-test (a software check, not science), and (iii) an ALP scan that re-derives a well-known result from prior literature [21] under conditions the authors themselves admit require ∼25× misalignment tuning.

This does not clear the PRD bar. I am also flagging a substantial number of internal-audit / review-log prose insertions, sample-count inconsistencies, and arithmetic claims that do not survive recomputation.

---

## ESSENTIAL findings

### P1B-E1 — Companion paper to an unpublished work (no usable theoretical anchor)
**Pages 1–2, refs [1], [4], [5], [6].** Reference [1] (the main theory paper this manuscript is allegedly verifying) is listed as `(in preparation)`. References [4], [5], [6] are likewise all "in preparation" by the same author. The abstract and §I explicitly frame this manuscript as a *verification companion* to [1]. PRD cannot adjudicate verification of an unpublished, unrefereed manuscript. The entire framing collapses without [1] being publicly available and peer-reviewable.
**Required fix:** Either submit jointly with [1] so both can be refereed together, or rewrite as a standalone methods/MCMC paper that does not depend on unpublished theoretical claims for its scope, scientific motivation, or interpretation.

### P1B-E2 — Abstract claims three analyses; body contains a fourth that is not in the abstract
**Page 1 (abstract) vs page 3–4 (Table II and surrounding text).** Abstract enumerates exactly three analyses. Yet §III and Table II present a *separate* DESI DR2 w0wa MCMC (128,385 samples, 16 chains, full quintom-B headline `w0 + wa = −1.48 ± 0.15`, claimed "+4.3σ departure from ΛCDM"). This is a major analysis that is nowhere in the abstract, nowhere in §I's scope statement, and does not appear in the conclusions except as a "Forward" note.
**Required fix:** Either remove Table II and all surrounding w0wa discussion entirely, or revise the abstract, §I scope statement, and conclusions to add the fourth analysis explicitly. Currently the paper's stated scope and its actual content disagree.

### P1B-E3 — "Corresponds exactly to the canonical 3.6σ Hubble tension" — does not
**Page 4–5, MB–H0 offset paragraph.** The text says the 0.155 mag offset is "∼3.2σ relative to the chain's σ_MB = 0.049 marginal width and corresponds **exactly** to the canonical 3.6σ Hubble tension." Recomputing: 0.155/0.049 = 3.16σ. The canonical Hubble tension between this chain (H0 = 67.69 ± 1.06) and Riess (73.04 ± 1.04) is √(1.06² + 1.04²) = 1.485, giving (73.04 − 67.69)/1.485 = 3.60σ. **3.16σ ≠ 3.60σ "exactly."** The factor differs by 14% in the σ-distance and propagates to a factor ~2 in p-value. The "exact correspondence" claim is incorrect.
**Required fix:** Replace "corresponds exactly" with "is broadly consistent with," and explain why the σ-distance is smaller in the MB axis (the MB σ does not include the H0 marginal contribution that drives the H0-axis tension).

### P1B-E4 — Review-log / "earlier reviewer / earlier draft" prose in body text
The manuscript contains multiple sentences that read as response-to-referee material rather than published-paper text. Each instance below must be removed and replaced with a clean assertion:

- **Page 3, "Caveats" paragraph:** *"An earlier count erroneously quoted '98.6% quintom-B' weight; in the actual converged chain..."*
- **Page 3, fn (a):** *"note: prior caveat promised a Savage-Dickey ratio on the converged 2D (w, wa) marginal, but with zero free-w0wa samples at the LCDM point the KDE estimator fails catastrophically"*
- **Page 4 (multiple):** *"This addresses earlier reviewer concerns that the reported 67.68 was inconsistent with active SH0ES likelihood; inspection confirms..."*
- **Page 4–5:** *"A concern was raised that the joint posterior mean ... was inconsistent with an active sn.pantheonplus likelihood, claiming a Cobaya YAML alias failure. Direct arithmetic audit:..."* and the subsequent multi-sentence rebuttal of the "YAML alias failure" claim ending in *"— NOT a YAML alias failure"*.
- **Page 6:** *"the bias was initially characterized as strictly 'stable across all three injections' at 0.032°, but the 0.342° injection actually gives 0.040°..."*
- **Page 7:** *"§VI for the explicit numerical derivation correcting the earlier C_aγ θ_i product"*

None of this belongs in a journal submission. It reads as the author's audit log against their own prior drafts. **Required fix:** Strip all such language. Present each result cleanly as the final, correct value; do not rebut errors that no published reader will ever see.

### P1B-E5 — Pipeline-recovery SNR figures (20.32, 25.71) juxtaposed to published 2.4–2.9σ
The abstract correctly flags the distinction, but in §IV body text (page 5) the high SNR is reported in equation form `β̂_NaMaster = 0.238° (pipeline-recovery SNR = 20.32)`, immediately followed by "for β = 0.342° (the published joint WMAP+Planck value [2]), the pipeline recovers 0.302° at SNR = 25.71." A reader who looks up Eq. (1) without also reading the abstract footnote and the immediately preceding "Scope note" paragraph could easily confuse this with a sky-detection significance. The mode-coupling-noise σ ≈ 0.012° implied by these SNR values is roughly 6–9× smaller than the published Planck NPIPE and ACT DR6 statistical errors. **Required fix:** At every juxtaposition of the MC-recovery SNR with any sky-detection number, restate the "not directly comparable; MC recovery only" qualifier inline, not just in the section header.

### P1B-E6 — "ECH spin-torsion" framing for analyses that contain no spin-torsion
The paper repeatedly states (e.g. §III header, abstract, §VI) that the MCMC carries "no torsion modifications" and the ALP birefringence is "not a distinctive ECH prediction." Yet the title remains "Technical Verification Companion to the ECH Spin-Torsion Program." If the analyses do not actually probe the theory, the title overclaims. **Required fix:** Retitle to honestly reflect content (e.g., "ΛCDM+∆N_eff MCMC, NaMaster Pipeline Validation, and ALP Birefringence Consistency Check" — drop "ECH" and "Verification" from the title).

---

## MAJOR findings

### P1B-M1 — Sample-count stratification is incoherent across abstract, table, figure, and footnote
Abstract: **309,189**. Table I: 176,240 + 132,949 = 309,189 raw. Fn 1: 216,432 post-burnin (both chains). Fig. 1 caption: 119,617 post-burnin. Fn 1 also gives 123,368 (analytical full-tension 70% burn-in) and 123,129 (chain count). And then 114,992 raw for a separate "ongoing" Planck-only chain. None of these is presented as *the* operationally relevant sample count for the headline ∆N_eff posterior. The footnote acknowledges this but does not resolve it.
**Required fix:** Pick one definition (raw, post-burnin, or ESS-thinned), report it cleanly per chain, and cite it consistently in abstract, table, and figure.

### P1B-M2 — Spectator-ALP "natural parameters" headline is contradicted by fn 4
Abstract and §VI summarize: "a field with f_a ∼ M_Pl, m ∼ H0 is consistent with the published joint WMAP+Planck value." Fn 4 (page 7) discloses that the spectator regime (Ω_a ≪ 1) actually requires θ_i ∼ 0.1, which is **25× tuning below the prior midpoint** θ_i ∼ 0.5 used to produce the "natural parameters" headline. The fine-tuning is so severe that the term "natural" is no longer accurate; this is fine-tuned, with a quantitative factor 25× now buried in a footnote. The abstract briefly notes a "fine-tuning of the misalignment initial condition" but does not quote the 25× figure.
**Required fix:** Move the 25× quantification into the abstract, or change "natural parameters" to "fine-tuned-misalignment parameters" throughout.

### P1B-M3 — ∆N_eff "bounce-class compatibility check" is not informative
Page 3 (after Table I): The authors concede that "minimal-ECH" predicts ∆N_eff ≈ 0 *by construction*. Therefore a null ∆N_eff measurement cannot discriminate between minimal-ECH and ΛCDM. The paper acknowledges this but still presents the analysis as part of its three load-bearing "verification" tasks. The result is uninformative as a verification.
**Required fix:** Either provide a discriminating analysis (modified-Boltzmann run with actual torsion sector) or downgrade this from "verification" to "internal consistency check" and shorten accordingly.

### P1B-M4 — Liu et al. [11] cross-validation is not a like-for-like comparison
Page 5: "Liu et al. constrained an EC torsion model... Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8." Liu et al. fit a *torsion-modified* model; the present chain uses *stock CAMB with no torsion*. The two posteriors are constraints on different models and a "0.5σ agreement" is meaningless without specifying what is being compared.
**Required fix:** Either remove this "cross-validation" or recompute the comparison restricted to the genuinely shared parameter axis (e.g., H0 in ΛCDM-equivalent limit).

### P1B-M5 — Equation (3) cannot be reconciled with Equation (2) without invisible parameter rescaling
Eq. (2) gives `∆ϕ/f_a ≈ 0.65 (m = H0, θ_i = 1)`. Eq. (3) inserts a factor `1.07`, claimed to be valid for "C_aγ = 8, θ_i = 1, m ≈ 2H0". Between the two equations the field-displacement value silently moves from 0.65 → 1.07 (factor 1.65) with no equation, no numerical justification, no plot. The body text on page 7 says the β ≈ 0.27° fiducial corresponds to "midpoint m ≈ 1.8 H0, ∆ϕ/f_a ≈ 1.0," but how this is consistent with Eq. (2)'s `0.65 at m = H0` is unexplained.
**Required fix:** Add a numerical-ODE result for m = 1.8 H0 (the actual fiducial), or replace Eq. (2)/(3) with a plot of ∆ϕ/f_a vs m/H0 at θ_i = 1.

### P1B-M6 — w0wa "departure from ΛCDM at +4.3σ" headline
Page 3 and Table II report the w0 marginal as `(marg.-tail, +4.3σ)` with the footnote conceding the LCDM point is unsampled and "the +4.3σ figure is a posterior-tail extrapolation distance only, not a Bayes-factor or ln B exclusion and not a frequentist tension." That is exactly correct — and is exactly why the +4.3σ should not appear as a headline number in the same row of a results table. Side-by-side placement of a number and a footnote saying "this number does not mean what it appears to mean" is misleading even with the footnote.
**Required fix:** Replace "+4.3σ" with a model-comparison-deferred entry (e.g., "—"). Move the marginal-tail-distance discussion to a methodology paragraph.

### P1B-M7 — DESI DR2 w0wa chain Bayes-factor deferral makes the headline unsupported
§V.B (page 6) and Appendix A both defer ∆AIC, ∆BIC, and ln B to "a follow-up nested-sampling analysis." Without any of these statistics, the claim that w0wa "disfavors ΛCDM" rests entirely on the marginal-tail-extrapolation distance which the authors themselves concede is not a tension or evidence statement. The body still says "the canonical quintom signature" and "phantom crossing required." These are model-comparison claims that the deferred statistics cannot support.
**Required fix:** Either run the nested sampling, or strip every "disfavors LCDM" / "quintom signature" claim that requires model comparison.

### P1B-M8 — Unconverged Planck-only chain referenced multiple times
Page 2 (abstract), page 2 (§III), page 7 (conclusions) all reference a third Planck-only Cobaya chain at `R̂ − 1 ∼ 0.05` (an order of magnitude above the conventional convergence threshold) and explicitly state it is "still accumulating." A non-converged chain has no place in a published manuscript even with disclaimers.
**Required fix:** Remove all mention of the third chain until it converges.

### P1B-M9 — Bibliography: Disambiguation footnote on [2] reveals an analysis-data mismatch
Abstract footnote `a` explains: "the published PRD paper [2] ... analyzes Planck PR3 + WMAP9; the public reproduction code released by the authors at github.com/LilleJohs/Cosmic_Birefringence was subsequently updated to use Planck PR4 / NPIPE. Throughout this paper, the labels 'PR4/NPIPE' attached to the Eskilt+Komatsu likelihoods refer to the code-repository dataset (which is what the ALP-MCMC re-runs actually use); the abstract β = 0.342° ± 0.094° (3.6σ) headline is from the published PR3+WMAP9 joint analysis." Translation: the headline number reported as a comparison target uses a different dataset than the in-paper ALP-MCMC. This is a data-likelihood mismatch wrapped in a footnote, not a clarification.
**Required fix:** Either re-run the ALP-MCMC against the *published* PR3+WMAP9 likelihoods so the comparison is like-for-like, or report the Eskilt+Komatsu number that matches whatever PR4/NPIPE dataset the repository actually uses (not the headline).

### P1B-M10 — Eq. (4) and its 3.9σ are explicitly disowned but remain in the manuscript
Eq. (4) gives `β_combined = 0.241° ± 0.061° (3.9σ)`, immediately followed by "(Auxiliary cross-check only.) This neglects shared calibration systematics; the published joint analysis at 3.6σ [2] is the headline." If the authors do not endorse it, it should not be a numbered equation.
**Required fix:** Demote Eq. (4) to inline text or remove.

### P1B-M11 — "Third [Planck-only] combination ongoing" in abstract
The abstract literally states "plus a third Planck-only combination ongoing." An ongoing analysis is not appropriate for an abstract.
**Required fix:** Remove from abstract; revisit only after convergence.

### P1B-M12 — Length disproportionate to net new content
After honest scoping, the net new content of this manuscript is: (i) one ∆N_eff null posterior in stock CAMB, (ii) a NaMaster pipeline self-validation, (iii) a recapitulation of an ALP scan whose physics is from Fujita et al. [21]. Ten dense pages with extensive footnotes is too long for this content; the natural length is ≤ 5–6 pages excluding references.

---

## MINOR findings

### P1B-N1 — H0 inconsistency 67.68 vs 67.69
Table I (page 3) and abstract: H0 = 67.68 ± 1.06 (full-tension). Page 4 body: "The full-tension chain returns H0 = 67.69 ± 1.06." 0.01 km/s/Mpc rounding inconsistency.

### P1B-N2 — Table II χ²-total arithmetic
10.6 + 10983.9 + 3043.0 = 14037.5; table reports 14037.4. The 0.1-unit "weighted-sample-vs-channel-mean" footnote `b` is technically defensible but cosmetically poor; report the sum directly or report the weighted-mean total without claiming it equals the channel sum.

### P1B-N3 — Fn. 1 (page 2) is itself nearly a page long
The footnote spanning page 2 → page 3 contains five distinct sample counts (309,189, 216,432, 119,617, 123,368, 123,129, 114,992). It reads as a recapitulation of an internal sample-counting audit. Compress to a single sentence with one canonical post-burnin number.

### P1B-N4 — "Independent verification (production 500-realization run, April 2026)"
Page 5: dating language ("April 2026," "Production") is internal-bookkeeping framing. Drop.

### P1B-N5 — "spin_torsion.input.yaml" referenced in body text
Page 5 names an internal YAML file ("the parameters are correctly aliased per the spin_torsion.input.yaml configuration"). Filenames are appropriate to a repository README, not to a journal body text.

### P1B-N6 — "We emphasize" / "Note that" / "Caveat" sentence headers throughout
The paper relies heavily on caveat headers. Each one inflates the "scope note" prose and reduces narrative clarity.

### P1B-N7 — Figure 1 caption sample count differs from text
Figure 1 caption: "119,617 post-burnin samples, getdist-thinned from 176,240 raw; footnote 1." The caption defers to a footnote for justification of its own sample-count claim. Caption should be self-contained.

### P1B-N8 — Table III "Status" column
"Verified" is used for parameter posteriors that the authors elsewhere say are uninformative w.r.t. the theory they claim to verify. The word "Verified" should be replaced with "Reported" or "Computed."

### P1B-N9 — "Acknowledges the use of Claude (Anthropic)"
This is acceptable per current journal AI-use disclosure norms, but PRD specifically requires the author to take full responsibility — present language is adequate. No fix required; flagging for editorial awareness.

### P1B-N10 — Fn 5 (page 9) duplicates fn 4 (page 7) content
The "backreaction / spectator-status" disclosure appears in fn 4 (page 7) and again in fn 5 (page 9) with substantially overlapping text. Consolidate.

---

## Summary recommendation

**REJECT**

The manuscript is a verification companion to an unpublished theory paper, is dominated by review-log prose and scope disclaimers, and after honest scoping contains essentially no new physical result that PRD would accept on its own merits: the MCMC carries no torsion physics, the pipeline test is software self-validation, the ALP check reproduces a previously published mechanism under fine-tuned parameters. Compounding these structural issues are an unannounced fourth analysis (w0wa DESI), a "corresponds exactly to 3.6σ" claim that recomputes to 3.16σ, sample-count inconsistencies across abstract/table/figure/footnote, internal audit prose ("earlier reviewer concerns," "earlier draft", "An earlier count erroneously quoted"), an unconverged chain (R̂−1 ∼ 0.05) referenced in the abstract, and a data-likelihood mismatch between the headline β = 0.342° (PR3+WMAP9) and the in-paper ALP-MCMC (PR4/NPIPE per the code repo). These are not addressable by minor revision; the paper needs to be either withdrawn until its companion theory paper [1] is published, or refactored as a standalone methods/MCMC note of ≤ 6 pages with the title, abstract, scope, and conclusions all rewritten to reflect what it actually demonstrates.

---

## PASS 2 — self-critique findings (what initial review missed)

# Supplementary Findings (Fresh-Eyes Pass)

After re-examining the manuscript with explicit arithmetic recomputation and cross-table consistency checks, the most consequential finding is that **the w0wa results in Table II are internally inconsistent at the level of basic statistics — the reported pivot redshift, marginal widths, and σ_wpivot cannot all have come from the same chain.** This is more serious than anything in my initial pass and is documented in detail below.

---

### P1B-E7 — Table II ap, σ_w0, σ_wa, and σ_wpivot are mutually inconsistent (Cauchy-Schwarz violation; arithmetic error in footnote b)

**Page 4, Table II and footnote b.** The footnote provides explicit numerical derivations of the pivot redshift and σ_wpivot. Each step recomputes incorrectly.

**Step 1: The implied Cov(w0, wa) from ap = 0.668 violates the Cauchy-Schwarz bound.**

The footnote formula is `ap = 1 − Cov(w0, wa)/Var(wa)`. With ap = 0.668 and σ_wa = 0.1864 (so Var(wa) = 0.03475):
- Cov(w0, wa) = (1 − 0.668) × 0.03475 = 0.01153

The Cauchy-Schwarz bound for any real chain is |Cov| ≤ σ_w0 × σ_wa = 0.0436 × 0.1864 = **0.00813**. The implied Cov = 0.01153 exceeds this bound by 42%, giving a nominal correlation |ρ| ≈ 1.42. **This is mathematically impossible for any real probability distribution.**

**Step 2: σ(w0 + wa) = 0.1485 implies Cov of the opposite sign.**

From the reported sum σ:
- σ²(w0 + wa) = σ²_w0 + σ²_wa + 2 Cov(w0, wa)
- 0.1485² = 0.0436² + 0.1864² + 2 Cov
- 0.02205 = 0.001901 + 0.03475 + 2 Cov
- 2 Cov = −0.01460
- Cov ≈ **−0.00730** (negative, |Cov| within Cauchy-Schwarz bound)

This is the *opposite sign* from the +0.01153 implied by ap. Both cannot be true of one chain.

**Step 3: Footnote b's arithmetic verification of σ_wpivot is explicitly wrong.**

Footnote b writes: `σ²_wpivot = σ²_w0 + (1 − ap)² σ²_wa = (0.0436)² + (0.3320)²(0.1864)² = (0.0301)²`

Recomputing: (0.0436)² + (0.3320)²(0.1864)² = 0.001901 + 0.003830 = **0.005731**, giving σ = **0.0757**. The claim `(0.0301)² = 0.000906` is off by a factor of ~6.3 in variance.

**Step 4: σ_wpivot ≈ 0.030 IS recoverable, but only with the covariance cross-term, and only with the OPPOSITE Cov that contradicts ap.**

The correct full-variance formula is:
- σ²_wpivot = σ²_w0 + (1 − ap)² σ²_wa + 2(1 − ap) Cov(w0, wa)

With Cov = −0.00730 (the value implied by σ_sum = 0.1485):
- σ²_wpivot = 0.001901 + 0.003830 + 2(0.332)(−0.00730) = 0.000884
- σ_wpivot = **0.0297 ≈ 0.030** ✓

So σ_wpivot ≈ 0.030 is self-consistent with σ_sum = 0.1485, but this same Cov yields:
- ap = 1 + Cov/Var(wa) = 1 + (−0.00730)/0.03475 ≈ **0.790**, not 0.668.

**Conclusion:** Of the four numbers {σ_w0 = 0.0436, σ_wa = 0.1864, σ_sum = 0.1485, σ_wpivot = 0.0301, ap = 0.668}, at most four can be simultaneously consistent. The set as reported is over-constrained and self-contradictory.

**Required fix:** Recompute the full 2×2 covariance from the actual MCMC chain, report Cov(w0, wa) explicitly, and demonstrate consistency of ap, σ_wpivot, and σ_sum with that single covariance matrix. If the chain is from DESI DR2 and σ_w0 and σ_wa are the marginal widths, expect σ_wpivot ≳ 0.03 and ap ≈ 0.7–0.8 (consistent with the de Putter–Linder zp ≈ 0.4 range that the paper claims to depart from but actually probably should be hitting).

### P1B-M13 — Pivot-redshift formula uses the wrong sign convention

**Page 4, footnote b.** The formula `ap = 1 − Cov(w0, wa)/Var(wa)` has the opposite sign from the standard Linder 2003 / de Putter–Linder 2008 convention:

Standard: `ap = 1 + Cov(w0, wa)/Var(wa)`

Derivation: requiring Cov(w_p, w_a) = 0 with w_p = w_0 + (1 − a_p) w_a gives (1 − a_p) = −Cov(w_0, w_a)/Var(w_a), hence a_p = 1 + Cov/Var(wa).

In DESI w0wa posteriors, Cov(w0, wa) < 0 generically, giving ap < 1 (the standard ap ≈ 0.7–0.8 range). The paper's reversed-sign formula combined with a negative Cov would give ap > 1, i.e., zp < 0, which is unphysical. The footnote's combination only "works" with a positive Cov — but a positive Cov is then incompatible with the reported σ_sum < √(σ²_w0 + σ²_wa). This is the root cause of E7.

**Required fix:** Correct the sign in the formula, or clearly indicate the alternative sign convention being used, and re-derive ap from the chain Cov.

### P1B-M14 — Cosmological/nuisance parameter partition inconsistent between Table I and Table II

**Pages 3, 4.** Table I footnote: "17 sampled parameters (7 cosmological + 10 Planck likelihood nuisance...)". Table II caption: "8 cosmological + 9 nuisance parameters" (total still 17).

The same Mb absolute-SN-magnitude parameter is listed under "Planck likelihood nuisance" in Table I but apparently re-classified for Table II. The two chains have different model parameterizations (w0wa adds two parameters), so the classification is fluid, but the inconsistency is unexplained and confusing.

**Required fix:** Adopt a single parameter-classification taxonomy across both tables and apply it consistently.

### P1B-N11 — Footnote 4 misreferences "Eq. (1)-adjacent disclaimer"

**Page 7, footnote 4.** Refers to "the abstract spectator-status restriction θ_i ≪ 1 (Eq. (1)-adjacent disclaimer)". Eq. (1) is the NaMaster recovery β̂_NaMaster = 0.238° on page 5; the θi ≪ 1 disclaimer is in the abstract on page 1, not adjacent to Eq. (1) in §IV. **Required fix:** Reference the abstract directly.

### P1B-N12 — σ(χ²_total) does not satisfy the quadrature sum of channel σ's

**Table II.** Reported σ(χ²_total) = 5.6. The channels: σ²_BAO + σ²_CMB + σ²_SN = 1.8² + 5.3² + 1.6² = 33.89, giving quadrature sum √33.89 = 5.82. Reported total σ (5.6) is *smaller* than the quadrature sum, which would require *anti*-correlated channel variations (unusual for independent likelihoods on a single chain). Minor inconsistency; either the quadrature assumption is wrong, or one channel σ is misreported.

### P1B-N13 — Min ESS efficiency unusually low and not flagged

**Table I.** Min ESS = 4744 (full-tension) and 4692 (Planck+BAO+SN). Post-burnin sample counts are 119,617 and ~93,000 respectively (taking the figure-caption number as canonical for full-tension). ESS efficiency is ~4% and ~5%. Acceptable but at the low end; the worst-mixing parameter and its autocorrelation length are not identified. **Required fix:** Identify the slowest-mixing direction and confirm via trace plots in the supplementary materials.

### P1B-N14 — MB posterior σ (0.049) is *larger* than the SH0ES prior σ (0.027)

**Page 4, MB–H0 audit paragraph.** The H0.riess2020Mb likelihood imposes a Gaussian prior MB = −19.253 ± 0.027 mag. Yet the chain posterior is MB = −19.263 ± 0.049 mag. An informative prior combined with additional data should *narrow* the posterior, not broaden it. The σ-broadening is plausibly attributable to tension between SH0ES, Pantheon+, and Planck pulling the chain in different directions, but this should be explicitly explained.

**Required fix:** Explain why σ_MB_posterior > σ_MB_prior. If this is a tension-induced broadening (the joint likelihood is bimodal or has heavy tails), state so explicitly; if it indicates a non-Gaussian posterior, this also undermines the use of `Mean ± σ` summary statistics in Table II.

### P1B-N15 — Eq. (4) "3.9σ" rounding asymmetric

**Page 7.** β_combined = 0.241°/0.061° = 3.95σ rounds to 4.0σ to one decimal place. The paper reports 3.9σ. Minor; given that the equation is already "auxiliary cross-check only" (M10), this is cosmetic.

### P1B-N16 — Pipeline mode-coupling noise floor (σ ≈ 0.012°) is not justified vs ACT-noise level

**Page 5, Eq. (1).** SNR = 20.32 at β = 0.238° implies internal noise σ ≈ 0.0117° on β̂. SNR = 25.71 at β = 0.302° implies σ ≈ 0.0118°. These are mutually consistent ✓ but are ~6–10× smaller than the published ACT DR6 statistical error (σ_β = 0.074°) and Planck NPIPE (σ_β = 0.11°), despite the paper claiming the MC uses "ACT-noise level ∆_P = 10 µK·arcmin." The MC-recovery σ < sky σ is a separate point requiring explanation — possibly the difference between EE+BB-cross MC recovery vs full sky-detection significance with foreground marginalization.

**Required fix:** Explain why the pipeline MC σ on β is ~10× smaller than ACT's sky σ on β, despite identical-sounding noise levels. The discrepancy is one of the reasons the SNR cannot be conflated with sky detection — but this needs to be quantified, not just stated.

### P1B-N17 — "Joint-trajectory scan" claim unsupported by any plot or table

**Page 7.** The β envelope [0.17°, 0.43°] is asserted to come from "a joint-trajectory scan over the coupled (Caγ, m/H0, θi) space" rather than an independent-extremes product. The actual joint trajectory, its sampling density, or the marginalized 2D slices that establish the [0.17°, 0.43°] envelope are not plotted or tabulated anywhere. The reader cannot verify the claim.

**Required fix:** Provide at least one figure or table summarizing the joint scan.

---

## Updated Summary

The new findings strengthen, rather than alter, the rejection recommendation. In particular, **P1B-E7 (Table II statistical inconsistency)** is a structural arithmetic problem in a load-bearing table that cannot be patched with a footnote — at least one number must be recomputed from the chain itself before the w0wa headline result can be considered defensible. Combined with E1 (verification of an unpublished theory paper), E2 (unannounced fourth analysis), E3 (3.2σ ≠ 3.6σ "exactly"), and the review-log prose throughout (E4), the manuscript requires substantial restructuring, not minor revision.