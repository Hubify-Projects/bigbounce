# P2 auto-2026-06-05_1418pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (10287 chars)
**Wall time**: 384.6s

---

# Referee Report — Paper P2: "Cosmic Birefringence from a Planck-Scale Axion-Like Particle"

## Overall Assessment

This paper presents a re-statement of an existing model class (Planck-scale ALP → cosmic birefringence; Fujita, Murai, Nakatsuka & Tsujikawa 2021, explicitly acknowledged on p. 5) wrapped in a Gaussian summary-likelihood combination of two published β measurements. The original methodological content is thin, but that alone is not necessarily fatal. What IS fatal for a PRD submission is a chain of arithmetic and attribution problems that undercut every load-bearing number in the abstract, plus a "naturalness" narrative that contradicts the paper's own equations.

---

## ESSENTIAL findings

### P2-E1 — The "naturalness" prediction β ≈ 0.27° is inconsistent with the paper's own Eq. (1).
**Pages 1–2, §2.2.** Eq. (1) gives Δφ ≈ f_a θ_i × O(1), and the text *explicitly* says "for m/H_0 ∼ 1, 1 − J_0(1) ≈ 0.24". Plugging into Eq. (2):

β = C_0 Δφ / (2 f_a) ≈ C_0 θ_i × 0.24 / 2 ≈ 0.12 rad ≈ **7°** for C_0 ∼ θ_i ∼ 1.

Yet the very next paragraph asserts "the cosmological field evolution gives Δφ/f_a ∼ 10⁻²", contradicting Eq. (1) by more than an order of magnitude. The factor 10⁻² is asserted with no derivation, and it is the only thing that lets the prediction land on 0.27° instead of ~7°. This single unjustified factor is doing all the work in the abstract's "naturally accommodates" claim. **The headline prediction is not derived from the displayed equations.**
**Fix:** Either derive Δφ/f_a from a numerical solution of the Klein–Gordon equation across z = 0–1100 (including matter-domination friction and the dark-energy era), or retract the "natural" framing.

### P2-E2 — "Eskilt et al. joint Planck + ACT analysis" is a phantom citation.
**Abstract, p. 1; §3.1, p. 2; §3.3, p. 3.** The number "β_obs = 0.342 ± 0.094°" is repeatedly attributed to "the Eskilt et al. joint Planck + ACT analysis". No such paper is cited. The Eskilt & Komatsu 2022 reference is WMAP + Planck (NPIPE), not Planck + ACT. The ACT measurement is cited as Diego-Palazuelos & Komatsu 2025. There is no published "Eskilt joint Planck + ACT" combination at 0.342 ± 0.094°. This number appears to be the author's own arithmetic but is presented as if it were a published external measurement, and is then used as the data input for the MCMC and the Bayes factor.
**Fix:** Provide the correct citation, OR clearly state "our own combination" — and reconcile with the value 0.242 ± 0.061° actually computed in Eq. (4).

### P2-E3 — Two different "observed" β values are used inconsistently and silently.
**§3.1–§3.4.** The paper computes a Gaussian summary β_combined = 0.242 ± 0.061° (3.9σ, Eq. 4) but then uses the unrelated value β_obs = 0.342 ± 0.094° (3.6σ, Eskilt mis-attribution) as the *data* for both MCMC parameter estimation (§3.3) and the Savage–Dickey Bayes factor (§3.4). I verified §3.4: with N(0.342, 0.094) and a [0°, 1°] flat prior, Savage–Dickey gives ln B = 5.18 (matches 5.17); with [0°, 2°], 4.48 ✓; with [0°, 0.5°], 5.87 ✓. With the *combined* posterior N(0.242, 0.061), ln B[0,1°] ≈ 6.0, not 5.17. **The Bayes factor is computed against an input the paper does not justify as "the observed value".** This is a methodological inconsistency: an analysis cannot simultaneously claim the combined likelihood gives 0.242 ± 0.061° AND then ignore that result when computing model evidence.
**Fix:** Use one self-consistent "observed" likelihood throughout, or explicitly justify why §3.3 and §3.4 ignore Eq. (4).

### P2-E4 — "Caγ × θ_i ∼ O(1)" claim is false; the marginal posterior is C_aγ ≈ 13.4.
**Eq. (8), p. 3; Fig. 1 caption, p. 4.** The text claims "C_aγ × θ_i = 3.4 ± 1.1, consistent with O(1) values for both parameters individually." But Fig. 1 itself shows the marginal C_aγ = 13.4⁺⁵·⁶₋₁₁ — that is, an order of magnitude above unity and prior-rail dominated (the prior is flat on [1, 30] and the posterior fills the upper half of it). Calling C_aγ ≈ 13 "O(1)" is dishonest. Additionally, the naive product of central marginal modes 1.33 × 13.4 = 17.8 is in 13σ tension with the quoted 3.4 ± 1.1 — this is presumably because the 1D marginals are not the maximum of the joint, but the paper does not explain the discrepancy, and the joint posterior is just the degeneracy line C_aγ × θ_i ≈ const.
**Fix:** State plainly that C_aγ is unconstrained except along the C_aγ × θ_i degeneracy direction; drop the "individually O(1)" claim; or motivate a tighter prior on C_aγ.

### P2-E5 — Run 1 fixes C = 8 with no justification, undermining the "no fine-tuning" claim.
**Table 1, p. 3.** Run 1 fixes "C = 8" (and is described as "ALP (C = 8 fixed)" without ever explaining what value of C this corresponds to physically or why 8 is the right number for a "natural" ABJ coefficient that the text elsewhere says is "order-unity". Choosing C = 8 is, by the paper's own naturalness framing, a tuning by nearly an order of magnitude. Headline numbers in §3.3 (β_ALP = 0.336 ± 0.107°) come from this fixed-C run.
**Fix:** Justify C = 8 from a specific UV completion, or drop Run 1 as the headline number.

### P2-E6 — MCMC sample sizes are inadequate for the claims, and the paper admits it without acting on it.
**§3.3, p. 3.** 720 to 6,840 accepted samples is extremely small for a multi-parameter cosmological inference. The paper concedes this ("Future work with longer chains (> 50,000 samples) would improve the reliability of the posterior tails and Bayes factor") — yet the Bayes factor in the abstract (ln B = 5.17) is computed precisely from these inadequate tails. Acknowledging a problem does not fix it.
**Fix:** Re-run with N_eff ≥ 10⁴ before quoting any ln B in the abstract.

### P2-E7 — The "9σ test" assumes the prediction is a point value, but the paper's own posterior has σ ≈ 0.1°.
**§4, p. 3.** The "Significance = 0.27/0.03 = 9σ" calculation treats the prediction as exactly 0.27°. But §3.3 reports β_ALP = 0.336 ± 0.107° (or 0.324 ± 0.099° from Run 2 in Fig. 1). Theoretical uncertainty from the C_0 × θ_i prior and the cosmological integration factor (admitted "O(1)") is ≳ 0.1°. A proper forecast adds these in quadrature with the 0.03° LiteBIRD error, giving discriminating power closer to 2–3σ for *exclusion* of the ALP if β is measured to be zero. The "9σ test" headline is not earned.
**Fix:** Replace with a forecast that propagates the theoretical uncertainty.

### P2-E8 — "Order-unity, no fine-tuning" in the abstract is contradicted by the body.
**Abstract; §3.2 Eq. (5); §3.3 Eq. (8).** The abstract states "f_photon × C_0 = 1.73 ± 0.44 (order-unity, no fine-tuning)" while the body's MCMC actually requires C_aγ × θ_i = 3.4 ± 1.1 with C_aγ ≈ 13. These are not the same quantity, "f_photon" is never defined, and one of the two is in tension with naturalness.
**Fix:** Define f_photon. Reconcile Eq. (5) and Eq. (8). Drop "no fine-tuning" until consistent.

### P2-E9 — "Namikawa, Murai & Naokawa (2025)" cited as "In preparation".
**Reference list, p. 6.** PRD does not accept "in preparation" citations that the paper uses to credit "superior ALP mass constraints" (§6, p. 5). This is a comparison the paper relies on to position its own contribution.
**Fix:** Either provide a published reference/arXiv number, or remove the comparison.

### P2-E10 — Significance figures from different null procedures placed side-by-side without comparability statements.
**Abstract.** "3.6σ isotropic birefringence signal (β_obs = 0.342 ± 0.094°)" and "β = 0.242 ± 0.061° (3.9σ from zero)" are juxtaposed without the explicit "these are different statistics" qualification. They are not directly comparable: one is an external (mis-attributed) datum, the other is the paper's own Gaussian summary combination using different inputs. Per PRD norms, every such juxtaposition needs a "not directly comparable" qualifier.

---

## MAJOR findings

### P2-M1 — The combined likelihood ignores correlated systematics.
**§3.2.** Eq. (3) assumes "independent errors" for Planck NPIPE and ACT DR6 β estimates. Both use the Minami–Komatsu self-calibration method; both share the foreground spectral model assumption discussed in §6. Treating their errors as independent is optimistic and inflates the headline 3.9σ. The §6 calibration-systematics paragraph essentially admits this but the abstract claim doesn't reflect it.

### P2-M2 — Eq. (1) is stated without a derivation.
The "1 − J₀(m/H₀)" form is not derived; J₀ would arise from a specific dynamical approximation (a Bessel-function approximation to the K-G equation in matter domination), and the radiation-era and Λ-era contributions are not represented in this expression. This formula cannot simultaneously be valid across the full redshift range it is being used for.

### P2-M3 — "Bounce cosmology" is name-dropped without serving any purpose.
**§5.** The paper claims the prediction is independent of bounce cosmology and then says it can be motivated in ECH — but immediately concedes "this motivation is qualitative — no derivation connects the Holst action to a specific ALP potential or coupling". The section is content-free and exists only to cross-link to companion papers (Golden 2026a,b). For PRD, remove or compress to one sentence.

### P2-M4 — Figure 1's β posterior (0.324 ± 0.099°) is not the same as Eq. (6)'s (0.336 ± 0.107°).
These come from different runs (2 vs 1) but the body never reconciles or even mentions the Run-2 β posterior shown in the figure. A naive reader will read the figure as showing Eq. (6).

### P2-M5 — Diego-Palazuelos & Komatsu 2025 cited with no arXiv number and no journal.
"arXiv preprint, 2025." is insufficient for PRD. The quoted central value 0.215 ± 0.074° must be traceable.

### P2-M6 — The abstract's "9σ significance — either confirming the signal or ruling out the ALP explanation decisively" is a false dichotomy.
LiteBIRD measuring, say, β = 0.15 ± 0.03° would neither confirm nor rule out the ALP class — it would simply reduce C_0 × θ_i. The dichotomy presented is rhetorical.

### P2-M7 — No corner plot for Run 1 (the headline run).
Run 1 produces the headline β = 0.336 ± 0.107°, but the only triangle plot shown (Fig. 1) is Run 2. The reader cannot inspect Run 1's posterior structure.

---

## MINOR findings

### P2-m1 — Eq. (1) sign convention. "1 − J₀(m/H₀)/J₀(0)" with J₀(0) = 1 is redundant; either drop the denominator or replace with an integral form that actually requires it.

### P2-m2 — "f_photon × C_0" in Eq. (5) is never defined; f_photon does not appear elsewhere.

### P2-m3 — §3.1 calls the ACT measurement "ACT DR6 [Diego-Palazuelos and Komatsu, 2025]" — this is normally attributed to the ACT Collaboration; cite collaboration plus first author convention.

### P2-m4 — Figure 2 lacks a legend explanation of "Model 0", "Model 2", "Model 2b" labels — the text refers to "Run 1, 2, 3", not "Model 0/2/2b". Notation inconsistency.

### P2-m5 — Significance arithmetic in abstract: 0.342 / 0.094 = 3.638σ, called "3.6σ"; 0.242 / 0.061 = 3.97σ, called "3.9σ" — fine, but tag both as rounded.

### P2-m6 — "consumer hardware" in acknowledgments is informal for PRD.

### P2-m7 — "AI research assistants" in acknowledgments needs to be specified per emerging journal policy (which model, what role).

---

## NITS

### P2-N1 — "indicative" is used twice for the same Bayes factor; pick one.
### P2-N2 — "3.6σ" appears in abstract; body sometimes says "3.5σ" (p. 1, "Combined, the evidence exceeds 3.5σ"). Be consistent.
### P2-N3 — Page 5, "model class is well-studied in the literature" — give a citation density commensurate.
### P2-N4 — Table 1 column header "R̂ − 1" should specify Gelman–Rubin in the caption (it does mention "Gelman-Rubin" in the text but not in the caption).
### P2-N5 — Eq. (10) labels "0.27/0.03 = 9σ" — should be 9 (dimensionless) or "9σ-equivalent", not literally "9σ" without a null model statement.

## Page-count assessment

The genuinely original content here is: a Gaussian summary of two β measurements, an underpowered MCMC against a model already in the literature, and a Savage–Dickey Bayes factor. That is 2–3 pages of content. The bounce-cosmology section adds nothing and could be removed. **Recommended max length: 4 pages** (PRD Brief Communication / Letter format would be more appropriate than a full Article).

---

## Summary recommendation

**REJECT** (resubmission permitted after major rewrite).

The paper's headline "natural prediction β ≈ 0.27°" is not derived from its own Eq. (1) — it relies on an undefended factor of 10⁻² that contradicts the displayed Bessel-function expression by an order of magnitude. The "observed" value 0.342 ± 0.094° is attributed throughout to a nonexistent "Eskilt et al. joint Planck + ACT analysis", the paper's own Gaussian combination yields a different value (0.242 ± 0.061°), and the two are used inconsistently across §3.2, §3.3, and §3.4. The Bayes factor and MCMC use the mis-attributed value while the abstract advertises the self-combined value. The "no fine-tuning" / "order-unity" rhetoric is contradicted by Fig. 1, which shows C_aγ ≈ 13 against a [1, 30] prior — i.e., prior-rail dominated and not natural. Sample sizes (≤6840) are admitted inadequate for the quoted ln B. The forecast "9σ test" treats a >0.1° theoretical uncertainty as zero. The novelty over Fujita et al. 2021 is candidly admitted on p. 5 to be "not the model itself", which leaves the inference framework — and that framework has the arithmetic/attribution problems above. None of these are cosmetic; together they invalidate every load-bearing number in the abstract. The paper is not yet at PRD standard.

---

## PASS 2 — self-critique findings (what initial review missed)

# Addendum to Referee Report — Second-Pass Findings

## ESSENTIAL findings (new)

### P2-E11 — Abstract mislabels the input dataset: "Planck HFI" vs body's "Planck NPIPE".
**Abstract, p. 1; §3.1, p. 2.** The abstract states "We perform a Gaussian summary-likelihood inference using **Planck HFI and ACT DR6** data". But §3.1 explicitly uses "**Planck NPIPE** [Eskilt and Komatsu, 2022]: β = 0.30 ± 0.11°" — and the paper itself (§3.1) says it *discards* the Planck HFI value (Minami & Komatsu 2020, β = 0.35 ± 0.14°) "which uses improved foreground cleaning". So the abstract advertises the very dataset the body deliberately rejects. NPIPE and HFI are different processing pipelines with different systematics and different reported β values. This is not a typo — it's a wrong-dataset attribution in the headline claim.
**Fix:** Change "Planck HFI" to "Planck NPIPE" in the abstract.

### P2-E12 — Eq. (5)'s "f_photon × C₀ = 1.73 ± 0.44" implies a natural scale of 0.14°, in direct contradiction to the paper's advertised 0.27° prediction.
**Eq. (5), p. 2; abstract.** The quantity f_photon is never defined, but reverse-engineering from the numbers:
- 0.242° / 1.73 = **0.140°** (and 0.061° / 0.44 = 0.139°) — consistent.

So Eq. (5) implicitly defines the "natural" β scale as 0.140°. But the paper's central claim — repeated 8 times across abstract, §2.2, §4, §6, and §7 — is that the natural ALP prediction is β ≈ **0.27°**. If 0.27° is correct, then f_photon × C₀ should be 0.242 / 0.27 ≈ **0.90 ± 0.23**, not 1.73 ± 0.44. Either:
(a) The natural scale is 0.14° (and the abstract's "0.27°" claim is wrong by ×2), OR  
(b) The natural scale is 0.27° (and Eq. 5's "1.73" is wrong by ×2).

Both cannot be true. The "order-unity, no fine-tuning" advertisement in the abstract depends on Eq. (5) being ~1, and on the prediction being 0.27°. These two requirements are mutually inconsistent.
**Fix:** Define f_photon explicitly. State the assumed normalization. Reconcile with §2.2.

### P2-E13 — The "Δφ/f_a ∼ 10⁻²" assertion in §2.2 is a factor of 24 smaller than what Eq. (1) actually yields, constituting hidden tuning.
**§2.2, p. 2.** Eq. (1) is explicit: Δφ/f_a ≈ θ_i × (1 − J₀(m/H₀)) ≈ θ_i × 0.24 for m ∼ H₀. The very next paragraph then asserts, without derivation, "the cosmological field evolution gives Δφ/f_a ∼ 10⁻²". This is 24× smaller than what the displayed equation gives. The paper labels the factor 0.24 as "O(1)" and the factor 0.01 as also "O(1)" within four lines of each other, with no derivation bridging them. The "no fine-tuning" claim cannot survive a factor-of-24 unexplained suppression. This is the same problem as E1 but sharpens it: the contradiction is between two adjacent paragraphs of the same section.

---

## MAJOR findings (new)

### P2-M8 — The Bessel function in Eq. (1) is the wrong solution for a scalar field in a matter-dominated universe.
**Eq. (1), p. 2.** The standard KG equation φ̈ + 3Hφ̇ + m²φ = 0 in matter domination (H ∝ 1/t, a ∝ t^(2/3)) has solutions involving J_{3/2}, *not* J₀. J₀ arises for a flat (constant-H) background. The formula "1 − J₀(m/H₀)/J₀(0)" is presented as if it were the result of the cosmological integration, but no derivation is given, and the functional form does not correspond to any standard limit. The paper itself hedges: "the precise value depends on the cosmological integration through the matter and dark-energy eras" — yet Eq. (1) is a fixed Bessel expression that does not encode any matter-era or Λ-era physics.
**Fix:** Derive Eq. (1) explicitly, or replace with a numerical integration of the KG equation across z = 0–1100.

### P2-M9 — Figure 2's "Observed" green band is plotted at β_obs = 0.342°, but Eq. (4)'s combined value 0.242° is not shown anywhere.
**Figure 2, p. 5; Eq. (4), p. 2.** The figure caption says the three model posteriors are "consistent with the observed value β_obs = 0.342 ± 0.094°". But the headline combined constraint of §3.2 is β = 0.242 ± 0.061° (Eq. 4). The figure therefore visually compares the MCMC posteriors to the *mis-attributed* Eskilt value, not to the paper's own combination. A reader looking at Figure 2 has no way to see that the paper's own §3.2 combination is 1.0σ *lower* than what's plotted. This compounds E3: the inconsistency between §3.2 and §3.3 is reified in the published figure.

### P2-M10 — Run 1 (C fixed at 8) gives a *wider* β posterior than Run 2 (C free). This is inverted.
**Eq. (6), p. 3; Fig. 1 caption, p. 4.** Fixing a parameter should narrow or leave unchanged the marginal posterior on derived quantities; it cannot widen it. Yet:
- Run 1 (C = 8 fixed): β = 0.336 ± **0.107**°
- Run 2 (C free): β = 0.324 ± **0.099**°

The free-C run is 7% *tighter* than the fixed-C run. This is the opposite of what fixing a parameter should do. The most likely explanations are: (a) MCMC noise from the ≤6,840 sample chains, (b) the two runs use different priors on something else not stated, or (c) the runs are not actually nested as claimed.
**Fix:** Re-examine; either re-run, or state explicitly which prior differs.

### P2-M11 — Run 3 (β free) is a self-test: it merely reproduces the input.
**Eq. (7), p. 3.** Run 3 fits β alone to the assumed observed value β_obs = 0.342 ± 0.094° with a uniform prior, and recovers β = 0.344 ± 0.096° — within MCMC noise of the input. This is not a cross-check of anything; it is a verification that the MCMC code can reproduce its input data, presented as if it were independent evidence ("the model-independent fit"). The 720-sample chain produces noise consistent with σ/√N ≈ 0.0035° and σ/√(2N) ≈ 0.0025°, which fully accounts for the (0.344 − 0.342) and (0.096 − 0.094) shifts. Listing this as "Run 3" alongside the ALP runs implies it tests something distinct; it doesn't.

### P2-M12 — Eq. (1) gives J₀(0) = 1 in the denominator — a trivial redundancy concealing the absence of normalization derivation.
**Eq. (1).** The form "1 − J₀(m/H₀)/J₀(0)" is identical to "1 − J₀(m/H₀)" since J₀(0) = 1. Writing it with the denominator implies a ratio-of-amplitudes derivation, but there isn't one — the formula is just a heuristic. This is cosmetic but signals that the equation was patched together rather than derived.

---

## MINOR findings (new)

### P2-m8 — Arithmetic: 5×10⁻³ rad ≠ 0.27°.
**§2.2.** "5 × 10⁻³ rad ≈ 0.27°" — actually 5×10⁻³ × 180/π = **0.286°**. To get exactly 0.27°, the displacement needs to be 4.71 × 10⁻³ rad, not 5 × 10⁻³. The numbers in the "natural calculation" don't agree to the precision they're quoted.

### P2-m9 — Table 1 column header "C = 8 fixed" — is "C" the same as C₀ (Eq. 2) or C_aγ (Eq. 8)?
The text uses both notations and never clarifies that they refer to the same coupling coefficient. If C₀ = 8 is "fixed at 8" for naturalness, why is the free-C run's prior [1, 30] rather than e.g. [0.1, 10]?

### P2-m10 — MCMC implementation unspecified.
§3.3 reports samples, chains, and R̂, but never says which sampler (emcee? Cobaya? MultiNest? a custom Metropolis-Hastings?), what proposal distribution, how many walkers, what burn-in fraction, or what thinning. For PRD reproducibility this is unacceptable.

### P2-m11 — Prior on β in Run 3 unstated.
The Run 3 "β free" MCMC must have a prior on β; it is never specified. Given that Run 3 is also used implicitly as a sanity check on the input likelihood, this is needed.

### P2-m12 — "Improved foreground cleaning" claim is unsupported.
§3.1: "we adopt the updated Eskilt value which uses improved foreground cleaning." No quantitative comparison is provided; "improved" is asserted, not argued. (And the value adopted from "Eskilt et al. joint Planck + ACT" doesn't exist per E2.)

### P2-m13 — "Caγ × θ_i ∼ O(1) values for both parameters individually" — the marginal on log₁₀(m_a/eV) = −31.4⁺¹·⁴₋₁·₂ is also prior-rail dominated.
Fig. 1 shows the mass posterior peaking at the upper edge of the prior [−35, −30]. The mode at −31.4 is within 1.4 of the upper prior boundary at −30. This is an additional, undiscussed prior-rail effect on the mass parameter — the data don't constrain m, only the prior does.

---

## NITS (new)

### P2-N6 — In the conclusion (p. 6), "anomaly coefficient C₀ and initial misalignment θ_i are model-dependent parameters of order unity whose product sets the amplitude" — this concedes the abstract's "no fine-tuning" framing, but the abstract was not updated.
### P2-N7 — Fig. 1 shows the β posterior with an asymmetric value (no asymmetry stated in the body's reporting). Inconsistent precision representation.
### P2-N8 — Page-numbering: the paper's "9σ test" appears in §4 (p. 3) but the false-dichotomy framing recurs in §6 (p. 5), §7 (p. 6), and the abstract. Same statement made four times without modification.
### P2-N9 — "5×10⁻³ rad ≈ 0.27°" (§2.2) — should be "≈ 0.29°" or "0.27° if Δφ/f_a = 4.7×10⁻³".
### P2-N10 — Notation: the paper alternates between β, β_obs, β_combined, β_ALP, β_free — five symbols for closely related quantities, with no notation table.

---

## Summary of new findings

The second pass uncovered:
- **3 new ESSENTIAL** issues (E11–E13): a wrong-dataset attribution in the abstract, a hidden internal inconsistency between Eq. (5)'s implicit natural scale (0.14°) and the advertised prediction (0.27°), and a 24× hidden suppression factor in §2.2.
- **5 new MAJOR** issues (M8–M12): including a wrong-Bessel-function physics error, an inverted Run 1/Run 2 width ordering, and a Run 3 that merely recovers its input.
- **6 new MINOR** issues (m8–m13) and **5 new NITS** (N6–N10).

The most consequential additions are **E12** (Eq. 5 cannot be simultaneously "1.73 ± 0.44 (order unity)" AND consistent with β_natural = 0.27°), **E13** (the 10⁻² factor in §2.2 is 24× the Bessel-function answer in Eq. 1 of the same section), and **M8** (the cited Bessel function is not the right one for matter-era field dynamics). E12 and E13 strengthen the rejection: they show the "no fine-tuning" claim is internally contradicted twice over by the paper's own equations within two pages of each other.

The initial review's reject recommendation stands, with these additional findings reinforcing it. The hidden inconsistencies in §2.2 and Eq. (5) were not visible without recomputing reverse-engineered normalizations from the displayed numbers.