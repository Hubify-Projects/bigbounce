# P2 auto-2026-06-08_1819pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (13765 chars)
**Wall time**: 421.1s

---

# PRD Referee Report — Paper P2
## "Cosmic Birefringence from a Planck-Scale Axion-Like Particle"

---

## Overview

This is a 7-page single-author paper claiming a "natural" ALP explanation for the Planck+ACT cosmic birefringence signal, with a forecast LiteBIRD test. Stripped of presentation, the physics content is: (i) point out that an ALP with f_a ~ M_Pl, m ~ H_0, θ_i ~ O(1), C_aγ ~ O(1) gives β ~ 0.3°, which is approximately the observed value; (ii) combine two public birefringence measurements; (iii) run three short MCMC chains. None of this is novel — the authors explicitly acknowledge Fujita et al. (2021) showed this years ago. The paper has multiple ESSENTIAL problems, including a broken bibliography, a logical contradiction in its central naturalness argument, and an undefined parameter in the headline numerical result.

---

## ESSENTIAL findings (must fix before acceptance)

### P2-E1 — Entire bibliography broken; no references render
**Sections:** Throughout; pages 1, 2, 3, 4, 6, 7.
Every single citation appears as the unresolved BibTeX marker "**[?]**" or "**?**". Examples: "The Planck HFI analysis [?] reported β = 0.35 ± 0.14°", "in the conventions of ?", "Planck NPIPE [?]", "ACT DR6 [?]", "LiteBIRD is projected to achieve σ(β) ≈ 0.03° on the isotropic birefringence angle [?]", "well-studied in the literature [?]", "Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated…", "Namikawa, Murai & Naokawa [?]", "the companion paper [?]", "Paper I(a) [?]", "complementary and independent test [?]". No reference list exists in the manuscript at all.
**Fix:** Provide a complete, compiled bibliography. A PRD submission cannot be reviewed without one — none of the quoted observational values (Eskilt et al., NPIPE, ACT DR6, LiteBIRD forecast) can be traced. This alone is grounds for rejection at the technical-check stage.

### P2-E2 — Central naturalness claim is mathematically inconsistent with the spectator condition
**Section 5, page 5; abstract, page 1.**
Sec. 5 derives Ω_ϕ ≈ (1/6)(m/H_0)²(f_a/M_Pl)² θ_i² and shows that at the "natural" parameter point (m=H_0, f_a=M_Pl, θ_i=1) one gets Ω_ϕ ≈ 0.17, which is **not** ≪1. The paper acknowledges this and "adopts option (a): θ_i ~ 0.22" to enforce the spectator condition, then writes:

> "The cosmological-birefringence prediction β ≈ 0.27° itself does not depend on which option (a, b, c) is taken: f_a cancels in the β amplitude (Sec. 2.2) and the prediction depends only on θ_i, C_0, and F(m/H_0)."

This is **false**. The cancellation in Sec. 2.2 is over f_a only. The amplitude is β = (α_EM C_aγ/4π) × θ_i × F(m/H_0). It is **linear in θ_i**. Reducing θ_i from 1.0 to 0.22 reduces β by a factor of 4.5, from 0.27° to about 0.06° — i.e. far below the observed signal. The paper cannot simultaneously claim (i) spectator self-consistency with θ_i ≈ 0.22 and (ii) β ≈ 0.27° matching the data, at fixed C_aγ. This is a fatal internal contradiction in the headline result.
**Fix:** Either honestly state the spectator regime predicts β ~ 0.06° (incompatible with observed signal at >3σ), or honestly state that matching the observed β requires Ω_ϕ ~ 0.17 (i.e. the ALP is an O(15%) dark-energy-like component, not a spectator), or boost C_aγ by ~5x to restore β (i.e. C_aγ ~ 40, which is no longer "natural O(1)"). The "naturalness" headline cannot survive.

### P2-E3 — Undefined parameter f_photon in headline equation (Eq. 5)
**Section 3.2, page 3; abstract.**
Eq. (5) and the abstract report "the effective photon coupling f_photon × C_0 = 1.73 ± 0.44 (order-unity, no fine-tuning)". The symbol f_photon is **never defined** in the paper. There is no formula, no relation to g_aγ, no relation to α_EM/4πf_a, no normalization convention. Attempting to back-derive it from β = 0.242° and standard relations gives C_aγ × (∆ϕ/f_a) ≈ 7.3, not 1.73. The headline claim of "order unity, no fine-tuning" is therefore both unverifiable and inconsistent with the model equations as written in Sec. 2.2.
**Fix:** Provide an explicit definition of f_photon, an equation relating it to the rotation angle, and a check that 1.73 is consistent with β = 0.242° and the C_aγ posterior in Sec. 3.3 (which centers at 13.4, not at "1.7").

### P2-E4 — Mutually inconsistent "fiducial" scenarios for the β ≈ 0.27° claim
**Sections 2.1, 2.2, abstract.**
The abstract advertises β ≈ 0.27°. Sec. 2.1 states "the fiducial case m = H_0, θ_i = 1, … yields ∆ϕ/f_a ≈ 0.65". Sec. 2.2 then computes the example with C_aγ = 8, θ_i = 1, **m ≈ 2 H_0**, ∆ϕ/f_a ≈ 1.07, giving β ≈ 0.29°. Plugging the actual Sec. 2.1 fiducial (m=H_0, ∆ϕ/f_a = 0.65) and C_aγ = 8 into Eq. (2) gives β ≈ (1/137)(8/4π)(0.65) × (180/π)° = **0.17°**, not 0.27°. The abstract's "0.27°" corresponds to neither stated fiducial; it is a third, undisclosed choice.
**Fix:** Pick one fiducial point, state it explicitly, and quote its β.

### P2-E5 — Bayes factor ln B = 5.17 not reproducible from quoted numbers
**Section 3.4, page 3.**
Savage-Dickey applied to the summary likelihood β = 0.242 ± 0.061° with flat prior on [0°, 1°]:
B_10 = p(β=0|prior) / p(β=0|data) ⇒ p(β=0|data) = (1/√(2π)·0.061)·exp(−(0.242)²/(2·0.061²)) ≈ 2.5×10⁻³ ⇒ ln B ≈ ln(1/2.5×10⁻³) ≈ **6.0**, not 5.17.
Using the MCMC posterior β = 0.336 ± 0.107° instead gives ln B ≈ 3.6. Neither reproduces the quoted 5.17. The author should specify which posterior was used and provide a reproducible calculation. With Run-3 having only 720 accepted samples (acknowledged page 3), the tail probability driving any Bayes-factor estimate is unreliable.
**Fix:** Provide explicit Savage-Dickey arithmetic with the exact posterior density used, or recompute with a chain of adequate length (≥50,000 samples, as the author themselves identifies).

### P2-E6 — Double-counting in summary-likelihood combination
**Section 3.1, page 2.**
The author combines "Planck NPIPE: β = 0.30 ± 0.11°" and "ACT DR6: β = 0.215 ± 0.074°" as independent likelihoods to get 0.242 ± 0.061° (Eq. 4). But the Eskilt et al. joint analysis (used elsewhere as βobs = 0.342 ± 0.094°) is itself a joint fit to both datasets. Combining Eskilt with the individual values, and using the combined NPIPE+ACT result side-by-side with Eskilt to test the same prediction, mixes overlapping information. Foreground-residual systematics in particular are correlated between NPIPE and ACT analyses (shared dust models). The "independent errors" assumption (Eq. 3) is unjustified and inflates the quoted 3.9σ.
**Fix:** Either justify independence quantitatively or drop one combination. The two distinct values 0.242 vs. 0.342, used interchangeably to "match" the model prediction, must be reconciled.

### P2-E7 — Abstract overclaim: "no fine-tuning" vs. acknowledged ~25× tuning
**Abstract; Sec. 5; Sec. 7.**
Abstract: "order-unity, no fine-tuning". Sec. 5: "(a) suppressing θ_i to ~ √0.05 θ_nat ≈ 0.22 (a ~25× fine-tuning of the initial misalignment relative to the natural prior midpoint)". These cannot both be true. A 25× tuning of a continuous parameter is fine-tuning by any standard definition.
**Fix:** Remove "no fine-tuning" from the abstract or remove Sec. 5's admission. The current text is contradictory in load-bearing claims.

---

## MAJOR findings

### P2-M1 — MCMC chains far too short for Bayes-factor or tail inference
**Table 1, page 3.** Sample sizes 720–6,840, N_eff ~ 1,000. The author admits "the small effective sample sizes limit the precision of tail estimates and evidence calculations". Yet a quantitative ln B = 5.17 is reported in the abstract and headlines the model-selection claim. Either rerun with chains of the appropriate length or remove the Bayes factor from the headline.

### P2-M2 — Notation drift: C_aγ vs. C_0
The abstract uses C_0; Sec. 2.2 introduces C_aγ; Sec. 3.3 uses C_aγ in the MCMC; Eq. 5 reverts to C_0; Sec. 7 mixes them. The reader cannot tell whether these are the same quantity. C_aγ in Run 2 posterior is 13.4 (Fig. 1), while "C_0 ~ 1" is claimed throughout the prose.

### P2-M3 — Sec. 3.3 MCMC posterior contradicts "natural O(1)" claim
**Fig. 1 (page 4).** The Run-2 posterior shows C_aγ = 13.4 (+5.6/−11), θ_i = 1.33, log₁₀(m/eV) = −31.4. C_aγ ≈ 13 is at the boundary of "natural" (paper allows C_aγ ∈ [4,12] as the natural range in Sec. 2.2; 13.4 is outside this). The MCMC therefore prefers parameter values just outside the paper's own "natural" interval. The "C_aγ × θ_i = 3.4 ± 1.1" summary (Eq. 8) obscures that the data prefer larger anomaly coefficient and smaller misalignment than the headline scenario.

### P2-M4 — f_NL = −35/8 claim is a non-sequitur
**Section 7, page 6.** "The matter-bounce non-Gaussianity f_NL = −35/8 provides a complementary and independent test [?]." No derivation, no analysis, no relation to the ALP model under study. The paper claims independence from bounce cosmology elsewhere (abstract). Drop this sentence or relegate to a footnote, or move it to the companion paper.

### P2-M5 — ECH gravitational framework is purely decorative
**Sections 6, 8.** The "ECH" framework appears twice with the explicit caveat "this motivation is qualitative—no derivation connects the Holst action to a specific ALP potential or coupling". By the paper's own admission, ECH adds nothing falsifiable. It should be removed or reduced to a one-line citation; in current form it merely advertises the companion paper.

### P2-M6 — LiteBIRD σ(β) = 0.03° uncritical citation
**Section 4.** The 9σ test depends entirely on σ(β) ≈ 0.03°, presented as a fixed number. The official LiteBIRD literature places this in the 0.03°–0.1° range depending heavily on self-calibration strategy and foreground residuals; the author mentions this once in Sec. 7 but then uses the optimistic value uncritically to claim "9σ". Show the forecast σ-range and the corresponding sigma-range explicitly.

### P2-M7 — Calibration systematics discussion mismatched with quoted significance
**Section 7.** Author concedes residual 0.1–0.3° systematics may exist, which is **larger than the signal** β = 0.27°. This makes the "3.9σ from zero" headline (abstract, Sec. 3.2) misleading: the statistical error bar 0.061° is dominated by a not-yet-bounded systematic ~5× larger. The abstract must reflect this if Sec. 7 is to remain.

### P2-M8 — Eskilt 0.342 ± 0.094° vs author combination 0.242 ± 0.061°: large discrepancy unexplained
The difference 0.10° between the two "combined" values is comparable to the headline ALP prediction itself (0.27°). A reader cannot tell which the model is being tested against. The 1σ "match" claim in Sec. 3.3 (β_ALP=0.336 vs β_obs=0.342) uses Eskilt; the 0.46σ "match" implicit in Sec. 3.2 (β=0.242 vs prediction 0.27) is to the author's own combination. The "consistent at 1σ" headline is not robustly demonstrated against either.

### P2-M9 — Equation (11) inconsistent with stated natural range
Sec. 2.2 claims natural θ_i ∈ [0.5, 2]. Plugging θ_i = 2, m/H_0 = 3, f_a/M_Pl = 1 into Eq. (11) gives Ω_ϕ = (1/6)(9)(4) = 6, i.e. **600% of critical density**. This shows the spectator condition is violated across most of the claimed "natural prior" range, not just at the midpoint. The Sec. 2.2 prediction range β ∈ [0.17°, 0.43°] is therefore largely from a cosmologically unphysical part of parameter space.

---

## MINOR findings

### P2-N1 — "Indicative; prior-dependent" hedge in abstract while still headlining ln B = 5.17
The abstract hedges in parentheses but still leads with the number. Move ln B to Sec. 3.4 only; do not headline.

### P2-N2 — "F(m/H_0)" introduced in abstract without ever being defined
**Abstract; Sec. 2.2 et seq.** F(m/H_0) is invoked five times but never written down as a function (only numerical values "0.65", "1.07" are given). Provide an explicit expression or tabulated values.

### P2-N3 — Acknowledgment: "use of AI research assistants" without specification
**Page 7.** PRD policy increasingly requires disclosure of which assistants were used for what task. Specify.

### P2-N4 — "Independent Researcher" affiliation with consumer hardware
The choice of platform is irrelevant if results reproduce; however the paper's broken bibliography, modest chains, and undefined symbols suggest insufficient proofreading. Recommend submission via an institutional collaborator who can vet the manuscript before resubmission.

### P2-N5 — Figure 1 contour shading and Figure 2 KDE smoothing not specified
Captions do not state whether dark/light bands are 1σ/2σ marginals, or what smoothing/kernel was used. Minor but standard PRD requirement.

### P2-N6 — Length vs. content
The paper is 7 pages but the actual new content is roughly two paragraphs (the explicit f_a-cancellation observation and the LiteBIRD forecast number). The model and prediction are explicitly attributed to Fujita et al. (2021). Recommended page count: 4 pages, PRL-style, after the essentials above are repaired — or, more honestly, this should be a comment/note rather than a research article in PRD.

### P2-N7 — Abstract significance "3.9σ from zero" is from a likelihood the author admits double-counts (see P2-E6)
Once independence is corrected, σ(β) and significance will both move. State the value with the correct correlation structure or drop the parenthetical.

---

## Summary recommendation

**REJECT**

This manuscript has six ESSENTIAL defects: the entire bibliography fails to render (every citation is a literal "[?]"); the central naturalness claim is internally contradictory (Sec. 5's spectator requirement θ_i ≈ 0.22 reduces β to ~0.06°, falsifying the headline 0.27°); the headline coupling 1.73 ± 0.44 uses an undefined parameter f_photon; multiple inconsistent "fiducials" are quoted across the abstract and Secs. 2.1/2.2; the Bayes factor does not reproduce; and the summary-likelihood combination double-counts overlapping Planck/ACT information. The novel scientific content beyond Fujita et al. (2021), which the author explicitly credits with the same prediction, is minimal. Even if the author corrected all six ESSENTIAL items, the paper would shrink to a short note and would still need to defend a model whose preferred parameters are admitted to require either ~25× misalignment fine-tuning or Ω_ϕ ~ 0.17 — neither of which is the "no fine-tuning" claim sold in the abstract. I recommend rejection without prejudice to a substantially revised resubmission (or to relocating the content to the companion paper).

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Findings — Fresh Re-Examination of P2

Below are issues my initial pass missed. They are organized by the issue-classes in the prompt and numbered to continue from the initial review.

---

## ESSENTIAL findings (additional)

### P2-E8 — Fig. 1 m-axion posterior is at m ≈ 28 H₀, fatally contradicting the paper's "m ∼ H₀" premise
**Fig. 1 (page 4); abstract; Sec. 2.1; Sec. 2.2.**
The triangle plot shows the marginal posterior median **log₁₀(m_a/eV) = −31.4 (+1.4/−1.2)**, i.e. m_a ≈ 4 × 10⁻³² eV. Converting H₀ = 67.4 km/s/Mpc → H₀ ≈ 1.4 × 10⁻³³ eV gives:

m_a / H₀ ≈ **27.6**, with 1σ upper bound at m_a/H₀ ≈ **700** (since the +1.4 upper error hits the prior edge at log₁₀(m/eV) = −30).

The paper's entire physical setup is built on m ∼ H₀ (abstract, Sec. 2.1: "field is frozen during radiation and matter domination and begins rolling at z ∼ O(1) when H(z) ∼ m"). For m ≈ 28 H₀, the ALP has been oscillating since z ≳ 5 and behaves like cold dark matter; ∆ϕ between recombination and today averages over many oscillations rather than monotonically displacing by O(f_a). The observable birefringence formula β = g_aγ ∆ϕ/2 with ∆ϕ ∼ θ_i f_a is no longer valid in the regime preferred by the data.

The paper either (i) is using a different m in the MCMC than the m in Sec. 2, (ii) has a bug in the field-evolution integration that lets large-m solutions also produce β ∼ 0.3°, or (iii) the "natural" parameter point and the "data-preferred" parameter point are completely different regions of parameter space. None of these is acknowledged, and any of them invalidates the central claim.
**Fix:** Reconcile the m_a posterior with the model. If the data prefer m ≫ H₀, the paper's entire naturalness narrative collapses.

### P2-E9 — m-axion posterior rails against the prior upper boundary; inference invalid
**Fig. 1; Sec. 3.3.**
Prior: log₁₀(m/eV) flat on [−35, −30]. Posterior: median −31.4, **upper 1σ = −30.0**, i.e. exactly at the prior edge. Posteriors that are rail-against-prior cannot be used for parameter inference or for evidence calculations — by definition the data prefer values outside the prior, and the marginal "constraint" is artifact of the prior boundary. The Bayes factor in Eq. (9), the C_aγ × θ_i product in Eq. (8), and the β posterior in Eq. (6) are all computed inside this railing chain.
**Fix:** Extend the m prior to log₁₀(m/eV) ∈ [−35, −27] (or larger), rerun, and check whether the posterior now finds a proper maximum or continues to rail upward.

### P2-E10 — Eq. (8) "C_aγ × θ_i = 3.4 ± 1.1" is mathematically inconsistent with Fig. 1's marginals
**Sec. 3.3, Fig. 1.**
Fig. 1 shows C_aγ = 13.4 (+5.6/−11) and θ_i = 1.33 (+0.44/−1.1). Naive product of marginal medians: 13.4 × 1.33 ≈ **17.8**, factor of ~5 above the Eq. (8) value 3.4. Even if Eq. (8) reports the median of the per-sample product (which can differ from product-of-medians under strong anticorrelation), it should still be consistent with the observable β via the model:

β [°] ≈ (α_EM / 4π) × (180/π) × C_aγ × θ_i × F(m/H₀) ≈ 0.0333° × C_aγ × θ_i × F

For the same Run-2 chain that reports β = 0.324° (Fig. 1, panel 4) and m/H₀ ≈ 28 (which gives F ≪ 1 in the oscillating regime), C_aγ × θ_i must be **much larger than 10**, not 3.4. For F ≈ 1 (the would-be near-Hubble regime), C_aγ × θ_i = 0.324/0.0333 ≈ **9.7**. Eq. (8)'s value of 3.4 is incompatible with the same chain's β posterior under either limit.
**Fix:** Either Eq. (8) is computed from a different chain or with the wrong statistic; clarify which, and verify consistency with β and F.

### P2-E11 — Headline β = 0.27° is geometrically impossible with strict "O(1)" parameters
**Abstract; Sec. 2.2.**
Combining β = 0.0333° × C × θ × F with the constraint F ≤ π (since |ϕ| ≤ πf_a along an axion field) gives the upper bound

β_max [°] ≤ 0.0333 × C × θ × π ≈ 0.105° × C × θ.

For C = 1 and θ = 1 (the literal "O(1)" values claimed in the abstract: "order-unity initial misalignment θ_i ∼ O(1) and order-unity photon anomaly coefficient C_0 ∼ O(1)"), the absolute maximum β is **0.105°**, i.e. ~2.6× below the claimed 0.27°. Achieving β = 0.27° requires C × θ ≥ 2.6 even in the maximally favorable rolling regime, and far more (~8–10) in the realistic regime with F ≲ 1. The literal "O(1) × O(1) = 0.27°" claim cannot be reconciled with the field equations.
**Fix:** Either inflate the headline parameter scenario (e.g. C ~ 8, θ ~ 1 — which is what Sec. 2.2 actually does, but the abstract hides this), or acknowledge that "order unity" in this paper means "order C_aγ ~ 8".

### P2-E12 — "f_photon × C₀ = 1.73 ± 0.44" decodes to β-rescaled-by-the-old-Planck-error-bar
**Sec. 3.2, Eq. (5); abstract.**
Working backward from the numbers: β = 0.242 ± 0.061°, and 0.242 / **0.14** = 1.729, while 0.061 / **0.14** = 0.436. These match Eq. (5) to four digits. The denominator **0.14°** is the σ of the original Planck HFI measurement quoted in Sec. 1 ("β = 0.35 ± 0.14°"). 

So the "effective photon coupling" Eq. (5) is not a coupling at all — it is β in units of the σ of a superseded measurement. The "order-unity, no fine-tuning" interpretation is then circular: it says "our central value is ~1.7× the old measurement's error bar", which is purely a statement about how big the signal is in units of an old uncertainty, not a statement about coupling naturalness. This must be removed from the abstract or properly redefined.
**Fix:** Either (i) derive f_photon × C₀ from first principles with explicit units and show that 1.73 has physical meaning, or (ii) retract Eq. (5) and the "order-unity, no fine-tuning" claim as currently stated.

---

## MAJOR findings (additional)

### P2-M10 — Sec. 2.2 "natural prediction range β ∈ [0.17, 0.43]°" understates the true range from the stated priors
**Sec. 2.2.**
The paper states: "The prediction spans β ≈ 0.17–0.43° across the natural parameter range m/H₀ ∈ [1, 3], θ_i ∈ [0.5, 2], C_aγ ∈ [4, 12]". Using β = 0.0333° × C × θ × F:

- Min corner: C = 4, θ = 0.5, F ≈ 0.4 (low m) → β ≈ **0.027°**
- Max corner: C = 12, θ = 2, F ≈ 1.5 (high m, before deep oscillation) → β ≈ **1.2°**

So the actual range from the paper's own "natural priors" spans roughly 0.03° to 1°+, not 0.17–0.43°. The bracket the paper quotes is suspiciously narrow and just-so centered on β_obs. The fact that the model "comfortably brackets the observed value" is then trivial — any sufficiently wide prior brackets any observation.
**Fix:** Quote the actual prior-predictive range from the stated priors, not a curated subset.

### P2-M11 — Stale forecast: LiteBIRD significance uses β = 0.27° while MCMC posterior centers at 0.32–0.34°
**Sec. 4.**
Sec. 4 forecasts "Significance = 0.27/0.03 = 9σ", but the same paper's MCMC posteriors give β_ALP = 0.336 (Run 1) and β_obs = 0.342. Using these, LiteBIRD significance is 0.336/0.03 = **11.2σ** or 0.342/0.03 = **11.4σ**. The "9σ" abstract claim is computed from a number that disagrees with the paper's own posterior at the >2σ level. This is a stale-number issue (different sections inherit different "predictions" without reconciliation).

### P2-M12 — "Consistent at 1σ" (Sec. 7) is not the right summary statistic for β_pred vs β_obs
**Sec. 7.**
The paper writes "the prediction matches the combined Planck + ACT measurement at 1σ". The summary-likelihood combined value is 0.242 ± 0.061°; the headline prediction is 0.27°. The discrepancy is (0.27 − 0.242)/0.061 = **0.46σ**, not 1σ. Versus Eskilt 0.342 ± 0.094°: (0.342 − 0.27)/0.094 = **0.77σ**. Neither matches "at 1σ". The number used to "match" is also the headline number derived to match. The implicit hedge "at 1σ" rounds a 0.5–0.8σ discrepancy upward in a way that overstates fidelity.

### P2-M13 — Bayes-factor prior-sensitivity scan internally inconsistent
**Sec. 3.4.**
ln B = 5.17 for [0°, 1°]; 4.48 for [0°, 2°]; 5.86 for [0°, 0.5°]. Savage-Dickey ln B for uniform priors of width L gives Δln B = ln(L₁/L₂) between two prior ranges. From [0°, 1°] to [0°, 2°]: Δln B = ln(1/2) = −0.693. Paper reports 5.17 − 4.48 = +0.69. **Sign is correct, magnitude matches.** From [0°, 1°] to [0°, 0.5°]: Δln B = ln(2) = +0.693. Paper reports 5.86 − 5.17 = +0.69. **Matches.** So the prior-scaling is self-consistent. However, when I compute the absolute value of ln B (assuming β = 0.242 ± 0.061° posterior with L = 1°), I obtain ln B ≈ **5.98**, not 5.17 — an offset of ~0.8 in all three values. This suggests either (i) ln B was computed using a different posterior than the summary-likelihood one quoted in the abstract, or (ii) there is a missing systematic correction. The reader needs to be told which.

### P2-M14 — Eq. (11) Planck-mass convention ambiguity (factor of ~2 in Ω_ϕ)
**Sec. 5.**
Eq. (11) is Ω_ϕ ≈ (1/6)(m/H₀)²(f_a/M_Pl)² θ_i². The prefactor 1/6 corresponds to **reduced** Planck mass M_Pl = (8πG)⁻¹/² ≈ 2.4 × 10¹⁸ GeV. For standard Planck mass M_Pl = G⁻¹/² ≈ 1.22 × 10¹⁹ GeV the prefactor becomes 4π/3 ≈ 4.2. The paper uses "M_Pl" without specifying. At f_a = M_Pl (whichever convention), this shifts Ω_ϕ at the fiducial point from 0.17 to as high as ~0.7 (or to ~0.04 in the other direction). The "spectator vs dark-energy-like" determination in Sec. 5 is sensitive to this factor.
**Fix:** State convention explicitly and propagate it through Sec. 5.

### P2-M15 — Sec. 2.1 "begins rolling at z ∼ O(1)" assumes m ∼ H₀ but is repeated even where m ≠ H₀ in the analysis
**Sec. 2.1, repeated three times.**
The claim "field is frozen during radiation and matter domination and begins rolling at z ∼ O(1) when H(z) ∼ m" is correct for m ~ H₀ but **false** for the m ~ 28 H₀ regime preferred by the MCMC. For m = 28 H₀, H(z) = m at z ≈ 7 (deep matter-dominated era), and ∆ϕ between then and today is suppressed by oscillation averaging, not by Hubble friction. The Sec. 2.1 narrative is regime-specific and is being applied outside its regime of validity throughout the paper.

---

## MINOR findings (additional)

### P2-N8 — F(m/H₀) referenced in abstract but never tabulated or plotted
**Abstract; Sec. 2.2 et seq.** Despite F being the central kinematic function controlling β, only two data points are given (F(1) ≈ 0.65, F(2) ≈ 1.07). A plot of F over m/H₀ ∈ [0.1, 100] would let the reader assess where the MCMC posterior on m sits relative to where β is observable.

### P2-N9 — Abstract "3.6σ" vs main-text "3.9σ" vs forecast 9σ — three null procedures juxtaposed
The 3.6σ comes from Eskilt's joint-EB fit. The 3.9σ comes from the author's Gaussian summary likelihood of NPIPE+ACT separately. The 9σ is a forecast against β = 0. These three values use three different null procedures and three different data combinations; the paper switches among them as headline numbers without flagging incomparability.

### P2-N10 — Acknowledgments admit "use of AI research assistants" but the bibliography failure (P2-E1) is exactly the kind of error LLM-assisted writing introduces
The unresolved-citation pattern ("[?]" throughout) plus the unrebuilt LaTeX is characteristic of LLM-generated drafts that were never fully compiled. Combined with the load-bearing arithmetic errors (P2-E10, P2-E11, P2-E12), the author should be asked to confirm that human verification of the numerical results was performed and to specify what was AI-generated vs human-checked.

### P2-N11 — Table 1 says "Run 3 = β free, 720 samples", but Eq. (7) reports β_free = 0.344 ± 0.096°
Reporting a posterior σ of 0.096° from only 720 samples is on the edge of credibility (Monte Carlo error on σ scales as 1/√(2N) ≈ 2.6%, so σ is known to ±0.003°), but the agreement with Eskilt's 0.094° σ is suspicious — almost certainly because the prior is effectively the Eskilt likelihood and the chain is just re-sampling it, in which case Eq. (7) is not an independent measurement.

### P2-N12 — Sec. 2.2 says "DFSZ-type" gives C_aγ = 8, but DFSZ is C_aγ = 8/3 ≈ 2.67
The standard DFSZ axion has E/N − 1.92 with E/N = 8/3, giving C_aγ ≈ 0.75 in the usual normalization. C_aγ = 8 is more KSVZ-like or a UV-completion-specific anomaly. The "natural DFSZ-type value" label is technically wrong.

---

## Summary of the additional findings

Five additional ESSENTIAL issues (P2-E8 through P2-E12), six MAJOR (P2-M10 through P2-M15), and five MINOR. The most damaging are:

1. **P2-E8/E9:** The MCMC posterior on the axion mass strongly prefers m ~ 28 H₀ and rails against the prior upper boundary at m ~ 700 H₀. This contradicts the paper's central premise that m ~ H₀, invalidates the field-dynamics narrative, and makes the marginal "constraint" a prior artifact.

2. **P2-E10:** Eq. (8) (C_aγ × θ_i = 3.4 ± 1.1) is numerically incompatible with the same Run-2 chain's β posterior of 0.324°, under any value of F(m/H₀).

3. **P2-E11:** With genuinely "O(1)" values (C = θ = 1), β is bounded above by ~0.10°, so the headline 0.27° is geometrically incompatible with the abstract's literal description of "order-unity" parameters.

4. **P2-E12:** The "effective photon coupling f_photon × C₀ = 1.73 ± 0.44" decodes to β in units of the *old* (superseded) Planck HFI error bar of 0.14° — not a physical coupling. The "order-unity, no fine-tuning" claim is then either circular or undefined.

My initial review was incomplete: it correctly identified the spectator/naturalness contradiction and the broken bibliography but missed the fact that the MCMC itself does not support the central physical regime (P2-E8/E9), missed the geometric upper bound on β at strictly O(1) parameters (P2-E11), and missed that the headline "coupling" parameter is β divided by an outdated error bar (P2-E12). My rejection recommendation stands, but on substantially stronger grounds: the paper is internally inconsistent at the level of its own MCMC chains, not merely at the level of presentation.