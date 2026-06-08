# P2 auto-2026-06-08_1520pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (9870 chars)
**Wall time**: 365.1s

---

# Referee Report — Paper P2: "Cosmic Birefringence from a Planck-Scale Axion-Like Particle"

## Overview
The paper reframes a well-known model (ALP birefringence with f_a ~ M_Pl, m ~ H_0; Fujita et al. 2021) as a "natural prediction" of β ≈ 0.27°, combines two literature birefringence measurements via Gaussian summary likelihood, runs a modest MCMC, and forecasts LiteBIRD. The contribution is incremental at best, and several headline statements are internally inconsistent or unsupported.

---

## ESSENTIAL findings

### P2-E1 — Theoretical prediction is internally inconsistent (Sec. 2, p. 2)
Eq. (1) gives Δφ ≈ f_a θ_i × (1 − J_0(m/H_0)) ≈ 0.24 f_a θ_i for m/H_0 ~ 1.
Eq. (2) gives β = (C_0/2)(Δφ/f_a).
For C_0 ~ θ_i ~ 1, this yields β ≈ 0.12 rad ≈ **6.9°**, not 0.27°.

Yet the body claims, immediately below Eq. (2): *"the cosmological field evolution gives Δφ/f_a ∼ 10⁻²"* — a factor of ~25 smaller than Eq. (1) itself produces. No derivation is given for this 10⁻² factor; it is asserted parenthetically as "from the ratio of field displacement to decay constant over the Hubble time", which is exactly what Eq. (1) already computed and gave as 0.24.

The "no fine-tuning" headline therefore quietly absorbs a hidden ~3×10⁻² suppression. The model in fact requires C_0 θ_i ≈ 0.04 to reproduce β = 0.27°, which is **not** O(1).
**Fix:** Provide an actual derivation of Δφ between recombination and today. Reconcile with Eq. (1). Then revise the naturalness claim — the model demands a non-O(1) input that the paper currently hides.

### P2-E2 — MCMC posterior contradicts the "order-unity / no fine-tuning" claim (Sec. 3.3, Fig. 1, p. 4)
The triangle plot reports **C_aγ = 13.4 +5.6/−11** as the marginal mode/median. The prior was *flat on [1, 30]*, which by construction excludes O(1) values from below.

- C_aγ ≈ 13 is not "order-unity" by any honest definition.
- Stating C_aγ × θ_i = 3.4 ± 1.1 is **inconsistent** with marginal medians θ_i = 1.33 and C_aγ = 13.4 (product ≈ 18). Either the quoted 3.4 ± 1.1 is wrong, or the marginals in Fig. 1 are wrong, or the parameters are very strongly anti-correlated and the marginals do not summarize the joint posterior — in which case the marginal medians should not be quoted as evidence of naturalness.
- The sentence *"consistent with O(1) values for both parameters individually"* (Sec. 3.3, p. 3) is false given the marginals shown.

**Fix:** Either widen the C_aγ prior to include sub-unity values (which is what "natural" actually means), or retract the naturalness claim. Reconcile the C_aγ × θ_i = 3.4 quote with the marginals.

### P2-E3 — Abstract / body inconsistency on which Planck dataset is used (Abstract p. 1 vs. Sec. 3.1 p. 2)
Abstract: *"using Planck HFI and ACT DR6 data, finding β = 0.242 ± 0.061°"*.
Sec. 3.1: *"Planck NPIPE [Eskilt and Komatsu, 2022]: β = 0.30 ± 0.11°"*.

NPIPE ≠ HFI. They are different reprocessings; HFI 2018 gave 0.35 ± 0.14°, NPIPE gave 0.30 ± 0.11°. The combination in Eq. (4) uses NPIPE + ACT, not HFI + ACT.
**Fix:** Correct the abstract.

### P2-E4 — Double-use of correlated/overlapping data in the headline 3.9σ (Sec. 3.1–3.3)
The combined β = 0.242 ± 0.061° comes from NPIPE + ACT DR6. The MCMC in Sec. 3.3 then uses the Eskilt joint Planck+ACT value β_obs = 0.342 ± 0.094°. These two combinations are **not independent** — they share Planck data — yet the paper quotes both as headline numbers (3.9σ in abstract; 3.64σ in body). This invites a reader to compare them as if they were independent cross-checks, which they are not. Moreover, the combination treating NPIPE and ACT as independent (Eq. 3) ignores any shared foreground modeling and any correlation between Planck-based and ACT-based foreground residuals.
**Fix:** Justify the independence assumption explicitly, or use a single consistent dataset. The paper currently produces a higher headline σ than Eskilt et al. by combining numbers Eskilt would not combine that way.

### P2-E5 — "f_photon × C_0 = 1.73 ± 0.44" is undefined (Eq. 5, Sec. 3.2, p. 2)
The quantity "f_photon" is introduced in Eq. (5) with no definition anywhere in the paper. The reader cannot tell whether it is a fudge factor absorbing the missing ~25× of P2-E1, an order-of-magnitude conversion, or a fit parameter. The claim that it is "order-unity, no fine-tuning" cannot be checked.
**Fix:** Define f_photon explicitly, write the equation relating (f_photon, C_0) to β and the field history, and recompute.

### P2-E6 — Bayes factor presented in abstract without prior caveat
Abstract: *"ln B = 5.17 (indicative; prior-dependent, see Sec. 3.4)"*. Sec. 3.4 then shows ln B varies between 4.48 and 5.86 just by halving/doubling the upper prior bound. The number is also computed by Savage–Dickey from a Gaussian fit, not from sampling the unrestricted ALP model evidence. Recomputing from the displayed inputs (Gaussian posterior at 0.342 ± 0.094 vs flat prior on [0°,1°]): ln B ≈ 5.18 ✓ arithmetic-wise, but this is essentially "how far is 0 from the Gaussian", not a model-comparison statement about the ALP model versus alternatives.
**Fix:** Either compute a real model evidence (marginalize over the ALP priors used in Run 2), or downgrade "Bayes factor in favor of nonzero rotation" to "Gaussian-tail tension with β = 0".

### P2-E7 — "9σ" LiteBIRD forecast uses the predicted value, not the measured value (Sec. 4, Eq. 10)
The forecast σ(β) = 0.03° is divided into the *predicted* β = 0.27°, not the *measured* combined β = 0.242° (≈ 8.1σ) or the Eskilt value 0.342° (≈ 11.4σ). The headline 9σ is not from the paper's own data analysis; it is a circular re-statement of the prediction. Phrasing in the abstract *"LiteBIRD … will test this prediction at 9σ"* should make this explicit, and Sec. 4 should report the LiteBIRD significance range corresponding to the 1σ data band, not a single number.
**Fix:** Quote the LiteBIRD significance as a function of the measured central value with confidence band.

### P2-E8 — Run 3 (β-free baseline) has 720 samples (Table 1, Sec. 3.3)
The model-independent baseline (Run 3) has only 720 accepted samples — far below what is needed to characterize a posterior that the paper uses as the reference for "no tension". R̂ − 1 = 0.005 is a chain-mixing diagnostic, not a sample-size diagnostic; with N_eff ~ a few hundred, tail probabilities and any density used in Savage–Dickey are unreliable. The authors acknowledge this once, but proceed to use these chains for the central comparisons (Eqs. 6, 7) and the Bayes factor.
**Fix:** Re-run with ≥ 5 × 10⁴ samples per chain before submission.

---

## MAJOR findings

### P2-M1 — Where does C = 8 in Run 1 come from? (Sec. 3.3, Table 1)
"ALP (C = 8 fixed)" is presented without any motivation in text. Eight is not "natural"; it is not derived. It is also inconsistent with the supposed C_0 ~ 1 used in the Sec. 2 prediction.

### P2-M2 — Cited literature undercuts the contribution
Sec. 6 honestly states: *"Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces β ∼ 0.3°"*. If that is so, the present paper's "prediction" is not a prediction; it is a retread. The advertised novelty in the abstract ("we present predictions") should be downgraded accordingly. The actual original content (MCMC with these particular priors) is thin.

### P2-M3 — Improper "in preparation" reference cited as data source (Refs.)
Namikawa, Murai, Naokawa 2025 is listed as "In preparation; cited for comparison of ALP mass constraints". A PRD submission should not cite unpublished, not-yet-existing work for comparative claims. Either obtain the preprint and cite arXiv ID, or remove.

### P2-M4 — Diego-Palazuelos & Komatsu 2025 reference is incomplete
Cited as "arXiv preprint, 2025" with no arXiv ID, no DOI, no version, no date. This is the source of one of the two headline measurements; it must be properly identified.

### P2-M5 — Inconsistent treatment of Eskilt central value vs. NPIPE value
The abstract claims β_obs = 0.342 ± 0.094° (the Eskilt joint analysis). But Eq. (4)'s combined value uses NPIPE 0.30 ± 0.11° as the Planck input. So the headline "3.6σ Eskilt signal" and the headline "3.9σ combined" use different Planck numbers. The relationship between these is never spelled out.

### P2-M6 — Self-calibration caveat is acknowledged but not propagated into the σ budget
Sec. 6 ("Calibration systematics") concedes that ~0.1–0.3° residual systematics may exist. The combined error bar 0.061° is purely statistical. The implied total error including the systematic floor would *swamp* the statistical uncertainty and make the 3.9σ headline unsupportable. The paper does not propagate this systematic anywhere into the quoted significance.

### P2-M7 — Paper length disproportionate to actual content
The genuinely new content is: (i) an arithmetic combination of two published numbers (one line); (ii) three short MCMC runs with O(1000) samples; (iii) a LiteBIRD significance calculation that is a single division. This is a Brief Report, not a 6-page PRD article.
**Recommended length:** ≤ 3–4 pages, or merge with the companion papers.

### P2-M8 — Companion-paper cross-references are inappropriate for an independent submission (Sec. 5, Sec. 6)
References to "Golden 2026a" (ECH bounce) and "Golden 2026b" (matter-bounce f_NL) as submitted-simultaneously companion papers are not actionable for the reader. They should either be removed from the body claims or replaced with self-contained statements.

### P2-M9 — "Naturalness" rhetoric is undefended (Abstract, Sec. 2.2, Sec. 7)
"Natural" appears 5+ times. The actual hidden tuning (P2-E1) is ~30:1; the C_aγ posterior (P2-E2) is ~13. The word "natural" is doing rhetorical work the analysis does not support.

---

## MINOR findings

### P2-m1 — Fig. 1 caption claims "centered at 3.4 ± 1.1" for C_aγ × θ_i, but the panel labels show C_aγ = 13.4 and θ_i = 1.33. The product of marginal medians is ~17.8, not 3.4. Either the caption refers to a different (joint) quantity, or one of the numbers is mis-reported. Clarify.

### P2-m2 — Eq. (1) writes 1 − J_0(m/H_0)/J_0(0); since J_0(0) = 1, this is just 1 − J_0(m/H_0). Why the explicit J_0(0)? Cosmetic.

### P2-m3 — Sec. 2.1: "frozen during radiation and matter domination (Hubble friction exceeds the mass) and begins rolling at z ∼ O(1) when H(z) ∼ m". For m ~ H_0 the field begins moving only in the dark-energy era; the exact onset depends on m/H_0. The paper's prediction is sensitive to this; please show the actual numerical solution rather than the leading Bessel approximation.

### P2-m4 — Sec. 4: "depending on the self-calibration strategy and systematic error budget" — this caveat undermines the "9σ" headline but is buried. Move to the forecast line.

### P2-m5 — Eq. (8) reads "C_aγ × θ_i = 3.4 ± 1.1". Units / dimensions of C_aγ should be stated (dimensionless? in what convention?).

### P2-m6 — Sec. 6: "matter-bounce non-Gaussianity f_NL = −35/8 provides a complementary and independent test [Golden, 2026b]" — irrelevant to this paper; remove or move to a one-line outlook.

### P2-m7 — Table 1: "Samples" of 720 / 2160 / 6840 — are these total samples or per-chain? Across how many chains? Burn-in?

### P2-m8 — Sec. 7 conclusion: "no fine-tuning of dimensionless parameters" is contradicted (P2-E1, P2-E2). Rewrite.

### P2-m9 — Acknowledgments: "The author acknowledges the use of AI research assistants during the analysis and manuscript preparation." PRD now requires AI-use disclosure with specifics on which parts (analysis vs. text). Please specify.

### P2-m10 — "Eskilt et al. joint Planck + ACT analysis" appears repeatedly; the reference list contains Eskilt & Komatsu 2022 (not "et al.") and Diego-Palazuelos & Komatsu 2025. There is no entry for an Eskilt-led joint Planck+ACT paper. Either supply the missing reference or correct the attribution throughout.

---

## NITs

### P2-N1 — Eq. (10): "Significance = 0.27/0.03 = 9σ". State this as "≈ 9". Single-significant-figure quote.
### P2-N2 — Fig. 2 axis: "Posterior density" with no normalization. Are these PDFs or peaks-normalized to 1? Caption says posteriors but max is 1.0; if peak-normalized, label "relative density".
### P2-N3 — "Diego-Palazuelos and Komatsu" — verify author order; the ACT DR6 birefringence work is collaborative.
### P2-N4 — Eq. (5) formatting: "f_photon × C_0 = 1.73 ± 0.44" — no units, no definition. (Already escalated to E5.)
### P2-N5 — Title says "Predictions, Constraints, and LiteBIRD Forecasts" — "Predictions" is singular substantively (one number, β). Consider "Prediction".

---

## Summary recommendation
**REJECT** (with re-submission possible after substantial rewrite).

The paper's central "natural prediction" β ≈ 0.27° contains a quantitatively inconsistent step (Eq. 1 gives a result ~25× larger than the headline prediction; the gap is closed by an undefined, undisclosed factor presented as "cosmological integration"), the MCMC posterior produces C_aγ ≈ 13 from a prior that *excluded* O(1) values, which the authors then describe as "consistent with O(1)". Abstract and body disagree on the Planck dataset used (HFI vs. NPIPE); the headline 3.9σ combines two non-independent measurements; the headline 9σ LiteBIRD forecast divides by the predicted value rather than the data band; the Bayes factor is presented as model-comparison evidence but is just a Savage–Dickey Gaussian-tail; one critical reference is "in preparation". The genuinely original contribution beyond Fujita et al. 2021 is too thin to justify 6 PRD pages. The paper needs a corrected derivation, an honest naturalness audit, longer chains, a single consistent dataset choice, and probably condensation to a Brief Report.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Findings — Second Pass

## ESSENTIAL (new)

### P2-E9 — The "spectator" claim is physically wrong (Sec. 2.1, Sec. 5)
The paper repeatedly calls the ALP a "spectator field" (Sec. 5: *"The ALP is a spectator field"*; Abstract: *"spectator axion-like particle"*). Compute the ALP energy density:

ρ_φ = (1/2)φ̇² + V(φ) ≈ V_max = 2 m² f_a²  (frozen field at θ_i ~ π)

With m = H_0, f_a = M_Pl (reduced Planck mass = 2.4 × 10¹⁸ GeV) and the critical density ρ_crit = 3 H_0² M_Pl²:

Ω_φ,max = 2 m² f_a² / (3 H_0² M_Pl²) = **2/3 ≈ 0.67**

Even for the moderate θ_i ≈ 1.33 in the Run-2 posterior (Fig. 1), Ω_φ ≈ 0.15–0.20, comparable to Ω_DE. The ALP in this setup is *not* a spectator; it is a quintessence-scale contribution to the cosmic energy budget. The Run-2 prior allows θ_i ∈ [0.01, π], so the posterior samples include regions where the ALP carries the entire dark-energy density.

This creates two failures the paper does not address:
1. **Background consistency.** The use of ΛCDM expansion history (implicit in J_0(m/H_0), in the LiteBIRD forecast σ(β) = 0.03°, in the Eskilt et al. likelihood adoption) is inconsistent with a field carrying tens of percent of ρ_crit.
2. **Existing constraints.** Planck + BAO + SNe place stringent limits on early-dark-energy and late-dark-energy contributions of this magnitude. The MCMC priors do not enforce these.

**Fix:** Either (i) restrict f_a ≪ M_Pl or θ_i ≪ 1 to enforce spectator behavior (which destroys the "natural f_a ~ M_Pl, θ_i ~ 1" headline), or (ii) treat the ALP as quintessence and propagate the background modification through the analysis. The current text has it both ways.

### P2-E10 — MCMC β posteriors are mutually inconsistent across runs (Eqs. 6–7; Fig. 1)
The three β posteriors are:

| Run | Model | β posterior | Free params |
|---|---|---|---|
| 1 | ALP, C = 8 fixed | 0.336 ± 0.107° | θ_i, log_{10} m |
| 2 | ALP, C free | 0.324 ± 0.099° (Fig. 1) | θ_i, log_{10} m, C_aγ |
| 3 | β free | 0.344 ± 0.096° | β |

Adding free parameters (Run 2 has *more* free parameters than Run 1) should *not* tighten the marginal β posterior. Yet σ(β) decreases from 0.107° (Run 1) → 0.099° (Run 2). Either:
- The ALP-model priors are doing significant work in Run 2 (e.g., upper-bounded C_aγ prior pulls C_aγ × θ_i toward smaller values, which tightens β), or
- The Run 2 posterior is broken (e.g., chain collapsed onto a sub-region of the C_aγ × θ_i degeneracy).

In either case, the *narrowing* of the β posterior as parameters are added is a red flag that the priors are informative — directly contradicting the "natural / no fine-tuning" narrative.

**Fix:** Show the joint (β, θ_i, C_aγ, log m) corner-plot for both runs and explain the narrowing.

---

## MAJOR (new)

### P2-M10 — Run 3's prior on β is unspecified (Sec. 3.3, p. 3)
Section 3.3 specifies priors for θ_i, log m, C_aγ but never states the prior on β used in Run 3 (the β-free model-independent fit). The Sec. 3.4 Savage–Dickey calculation assumes β ∈ [0°, 1°] flat. If this is the same prior used in Run 3, the boundaries are not far from the posterior (β = 0.344 ± 0.096°: 1σ tail extends to 0.44°, well within prior; 4σ tail at 0.728° also within). But the lower bound at 0° is informative — it truncates the Gaussian at zero, biasing the mean upward. Without explicit statement, the reader cannot evaluate.

### P2-M11 — Figure 2 legend disagrees with Table 1 (Fig. 2 vs Sec. 3.3)
Figure 2 legend: "Model 2: ALP (C = 8)", "Model 2b: ALP (C free)", "Model 0: beta free".
Table 1 / body: "Run 1: ALP (C = 8 fixed)", "Run 2: ALP (C free)", "Run 3: β free".

The reader must infer Model 2 ↔ Run 1, Model 2b ↔ Run 2, Model 0 ↔ Run 3. The presence of "Model 0", "Model 2", "Model 2b" (no Model 1, no Model 2a) strongly suggests this paper was extracted from a longer manuscript with a different model taxonomy, and the figure was not regenerated.

### P2-M12 — Mass posterior is bounded by the prior from above (Fig. 1)
Fig. 1 reports log_{10}(m_a/eV) = −31.4 +1.4/−1.2. The +1σ upper edge is at log_{10}(m_a/eV) ≈ −30.0, which is **exactly the prior upper bound** ("log_{10}(m/eV) flat on [−35, −30]"). The mass is unconstrained from above by the data; the quoted uncertainty is set by the prior. This should be stated explicitly, and the prediction's robustness to the prior boundary should be tested.

### P2-M13 — Eq. (1) uses a matter-dominated Bessel formula but the dynamics span the matter–Λ transition (Sec. 2.1)
The formula Δφ = f_a θ_i [1 − J_0(m/H_0)] is the exact solution for a massive scalar in a matter-dominated (a ∝ t^{2/3}) cosmology. For m ~ H_0, the field begins moving precisely during the matter–Λ transition (z ~ 0.5), where this approximation breaks. The Sec. 2.1 admission *"the precise value depends on the cosmological integration through the matter and dark-energy eras"* signals the author knows this, but proceeds to use the matter-era Bessel value (0.24) anyway. Either compute the integral numerically through ΛCDM, or quote a range covering the systematic.

### P2-M14 — The "natural" prediction sits below the data; the MCMC reveals data-driven fitting (Eqs. 6–7 vs Sec. 2.2)
Sec. 2.2 advertises β ≈ 0.27° as the natural prediction. The Run-1 ALP posterior gives β = 0.336 ± 0.107° — i.e., the MCMC moves the inference *away* from 0.27° toward the data (0.342°). The shift is (0.336 − 0.27)/0.107 = 0.6σ in the MCMC, and (0.342 − 0.27)/0.094 = 0.77σ vs data. So the headline "ALP model reproduces the observed birefringence with no tension" is accurate only because the MCMC is pulling C × θ_i to *correct* the natural prediction's undershoot. This is fitting, not predicting.

### P2-M15 — Eq. (3) assumes independent errors without checking (Sec. 3.2)
The Gaussian product likelihood (Eq. 3) is valid only if the NPIPE and ACT DR6 measurements have independent statistical errors. They share: (i) overlapping sky regions, (ii) shared foreground templates (often Planck-derived for ACT), (iii) the same Minami–Komatsu self-calibration framework whose systematics correlate across experiments. No correlation matrix is shown. If the effective correlation is ρ = 0.3, the combined σ widens from 0.061° to ~0.073° and the headline 3.9σ drops to 3.3σ.

---

## MINOR (new)

### P2-m11 — Eq. (5) introduces f_photon with no prior definition.
Sec. 2.2 uses C_0 alone in the rotation formula. Sec. 3.2 then writes "f_photon × C_0 = 1.73 ± 0.44" without defining f_photon. Numerically, 0.242/1.73 = 0.140°, suggesting f_photon = β / (β_unit × C_0) where β_unit ≈ 0.14° is some reference; but no such reference is stated. The notation appears to be extracted from a separate framework not described here.

### P2-m12 — Mass prior log_{10}(m/eV) ∈ [−35, −30] is unjustifiably wide.
For "m ~ H_0", the natural prior centers on log_{10}(m/eV) ≈ −33 with width ≲ 1 decade. The 5-decade flat prior dilutes the evidence calculation and lets the posterior drift to log_{10}(m/eV) ≈ −31.4, two orders of magnitude *above* H_0 — directly contradicting the "m ~ H_0" naturalness premise.

### P2-m13 — Run-3 sample count (720) is too small even for a 1D Gaussian fit characterization.
The body asserts β_free = 0.344 ± 0.096° to three significant figures. With Neff ~ 700, the MC error on the mean is ~σ/√N ≈ 0.0036° and on σ is ~σ/√(2N) ≈ 0.0026°. The reported precision is at the edge of statistical reliability.

### P2-m14 — Sec. 2.2 states "every input is O(1) in natural units" while Eq. (2) carries an explicit "× O(1)" factor.
"O(1)" appears four times in two paragraphs. One of these (the cosmological integration factor) is in fact 0.04 if you reproduce Eq. (1) → Eq. (2) honestly (see P2-E1). Calling 0.04 "O(1)" stretches the term.

### P2-m15 — The mass m ~ H_0 implies a field that just started rolling.
For m = H_0, the field begins rolling at z = 0; integrated Δφ from CMB to today is dominated by the very last e-fold. The Bessel approximation in Eq. (1) is least accurate exactly when the field begins rolling at z ~ 0. The dominant systematic on the prediction is therefore the m/H_0 ratio, but the MCMC marginalizes over a 5-decade range in m — meaning the "prediction" depends on a parameter the data does not constrain.

---

## NITs (new)

### P2-N6 — Fig. 2 legend lists three models but does not include posterior central values or widths in the legend boxes.
### P2-N7 — Eq. (1) writes 1 − J_0(m/H_0)/J_0(0) with J_0(0) = 1 in the denominator; cosmetic.
### P2-N8 — Table 1 column "Status" with three identical "Converged" entries is uninformative.
### P2-N9 — Sec. 2.2: "C_0 is an order-unity coefficient from the ABJ anomaly" — but in Run 1 the paper *fixes* C = 8. Eight is neither O(1) nor a generic ABJ-anomaly value; specify which UV completion produces C = 8 (it is the value sometimes quoted for KSVZ axions with specific charge assignments — say so).
### P2-N10 — Reference list mixes "and" vs "et al." inconsistently; the paper references "Eskilt et al. joint Planck + ACT" but the bibliography only contains "Eskilt and Komatsu 2022".

---

## Summary of what the first pass missed

The most important new finding is **P2-E9**: the "spectator" assertion is incompatible with the ALP carrying up to ~70% of the critical density at θ_i ~ π and ~17% at θ_i ~ 1, which is exactly the regime the paper claims is "natural". The phenomenology of the model is therefore inconsistent: a true spectator cannot have these parameters, and a non-spectator changes the cosmological background used to derive the very birefringence prediction. The first pass focused on the surface-level "naturalness" tuning of C_0 θ_i (P2-E1) but missed that the model setup is physically untenable independent of that. Second-most important is **P2-E10**: the β-posterior narrows as parameters are added, which is mathematically suspicious and indicates the MCMC priors (not the data) are driving the fit.