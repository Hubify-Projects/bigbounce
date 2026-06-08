# P2 auto-2026-06-08_1354pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (11399 chars)
**Wall time**: 253.3s

---

# Referee Report: Paper P2 — "Cosmic Birefringence from a Planck-Scale Axion-Like Particle"

## Overall Assessment

This paper claims to present a "natural" ALP model for cosmic birefringence with Planck-scale decay constant. The actual content is: (1) a back-of-envelope estimate that β ~ 0.27° is order-unity-consistent with observations, (2) a trivial inverse-variance combination of two literature measurements, and (3) a small MCMC fit. The paper itself admits (Sec. 6) that Fujita et al. (2021) already demonstrated essentially the same result. There is no new physics, no new data, no new method. The MCMC machinery is applied to summary statistics, not to the underlying CMB data. The "9σ LiteBIRD test" is arithmetic on existing forecasts. This does not meet the PRD bar.

---

## ESSENTIAL Findings

### P2-E1: Headline σ values are inconsistent and not directly comparable
**Page 1 (abstract), Page 2 (Sec. 3.1, 3.2):**
The abstract simultaneously quotes:
- β_obs = 0.342 ± 0.094° (Eskilt et al. joint)
- β_combined = 0.242 ± 0.061° (3.9σ)

These are presented as if compatible, but they differ by **>1σ** in central value (0.342 vs 0.242). The "combined" value uses Planck NPIPE (0.30 ± 0.11°) and ACT DR6 (0.215 ± 0.074°) — which when combined by inverse variance give:
- σ_comb = 1/√(1/0.11² + 1/0.074²) = 0.0614° ✓
- β_comb = (0.30/0.11² + 0.215/0.074²) × σ_comb² = (24.79 + 39.26) × 0.00377 = 0.241° ✓

So the arithmetic is correct, but then the paper switches to βobs = 0.342 ± 0.094° for the MCMC. **The reader is left with two incompatible "headline" measurements being used in different sections without explanation of which to believe.** The 3.9σ "combined" result and the MCMC posterior centered at 0.336° cannot both be correct descriptions of the data.

**Required fix:** Pick one likelihood, justify it, and use it consistently. State explicitly that the NPIPE+ACT combination and the Eskilt joint EB-fit are NOT independent and should not be presented side-by-side as separate validations.

### P2-E2: The "prediction" β ≈ 0.27° is not a prediction
**Page 2, Sec. 2.2:**
> "the cosmological field evolution gives ∆ϕ/fa ∼ 10⁻²(from the ratio of field displacement to decay constant over the Hubble time), yielding β ≈ C₀ θᵢ × 5 × 10⁻³ rad ≈ 0.27°"

This is circular. The text says ∆ϕ/fa ~ 10⁻² but Eq. (1) gives ∆ϕ/fa ≈ θᵢ × (1−J₀(1)) ≈ 0.24 θᵢ — which would yield β ~ 7° for θᵢ ~ 1, C₀ ~ 1. The factor of ~30 discrepancy between Eq. (1) ("0.24") and the text ("10⁻²") is unexplained. The number 5×10⁻³ rad = 0.286° is reverse-engineered to match the data. **The claim of "no fine-tuning" is false** because the integration factor is being adjusted from O(0.24) to O(10⁻²) without derivation.

**Required fix:** Either derive the cosmological integration explicitly (solve the KG equation with realistic w_DE(z)) or remove all claims of "naturalness" and "no fine-tuning."

### P2-E3: Equation (5) is dimensionally and conceptually wrong
**Page 2, Sec. 3.2:**
> "fphoton × C₀ = 1.73 ± 0.44"

This is presented as derived from the data, but nowhere is "fphoton" defined. From Eq. (2), β = C₀θᵢ/2 × O(1), so the data constrains the product C₀θᵢ × (integration factor). The quantity "fphoton × C₀ = 1.73 ± 0.44" appears to be β_combined/0.14° but no derivation is provided. Equation (8) gives Cₐγ × θᵢ = 3.4 ± 1.1 from the MCMC, which is inconsistent with Eq. (5) by factor ~2.

**Required fix:** Define every symbol. Reconcile Eqs. (5) and (8).

### P2-E4: MCMC is a fit to ONE number, claimed as "parameter estimation"
**Page 3, Sec. 3.3, Table 1:**
The "likelihood" being sampled is a single Gaussian on β_obs = 0.342 ± 0.094°. This is not parameter estimation — it is sampling a 1D Gaussian. Running 2,160 / 6,840 / 720 samples on a 1-3 parameter model with a single-datum Gaussian likelihood and then quoting R̂−1 < 0.01 as evidence of "convergence" is methodologically empty. The posterior on β simply reproduces the input Gaussian. The "Caγ × θᵢ = 3.4 ± 1.1" constraint is entirely set by the prior on Caγ ∈ [1,30] combined with the single β measurement.

The MCMC adds nothing. The "Caγ = 13.4₋₁₁⁺⁵·⁶" posterior shown in Fig. 1 is dominated by the prior boundary [1,30], not the data.

**Required fix:** Either remove the MCMC section as it adds no information, OR fit the actual CMB EB power spectrum (which would be a real analysis). The current framing misrepresents the rigor of the analysis.

### P2-E5: Bayes factor ln B = 5.17 is meaningless under the stated procedure
**Page 3, Sec. 3.4:**
Savage-Dickey on a 1-datum Gaussian likelihood with flat prior β ∈ [0°, 1°] gives:
- Posterior density at β=0: ~exp(−(0.342)²/(2×0.094²))/√(2π×0.094²) ≈ exp(−6.62)/0.236 ≈ 0.00558
- Prior density at β=0: 1/1° = 1
- ln(prior/posterior) = ln(1/0.00558) = 5.19 ✓

So the number is just the Gaussian tail probability at zero, with a *prior range chosen by the author*. With β ∈ [0°, 10°] the "evidence" would be ln B ≈ 7.5; with β ∈ [0°, 0.3°] it would be < 1. This is not evidence for ALP physics — it is evidence that 0.342 ± 0.094 ≠ 0, which we already knew.

**Required fix:** Remove the Bayes-factor framing or replace with proper model comparison against a physically-motivated alternative (e.g., calibration systematic with informative prior).

### P2-E6: "9σ LiteBIRD test" is arithmetic, not a forecast
**Page 3, Sec. 4, Eq. (10):**
> "Significance = 0.27/0.03 = 9σ"

This is not a forecast — it is division. A proper forecast requires (i) the LiteBIRD likelihood, (ii) the model parameters being tested, (iii) marginalization over systematics. The 0.03° LiteBIRD sensitivity is for the angle itself, not for distinguishing β = 0.27° from alternative ALP parameter values. If LiteBIRD measures β = 0.34°, the model "passes" at 9σ from zero but is in 2σ tension with the prediction 0.27°.

**Required fix:** Either present a real Fisher forecast on the ALP parameter space, or downgrade the claim to "if β ≈ 0.27° is real, LiteBIRD will see it at ~9σ from zero."

### P2-E7: Triangle plot (Fig. 1) contradicts body text
**Page 4, Fig. 1:**
The figure caption says "Cₐγ × θᵢ is centered at 3.4 ± 1.1." But the marginal posteriors shown are:
- θᵢ = 1.33₋₁.₁⁺⁰·⁴⁴
- Cₐγ = 13.4₋₁₁⁺⁵·⁶

Product of medians: 1.33 × 13.4 = 17.8, not 3.4. Even taking lower-tail values: the product cannot give 3.4 ± 1.1 from these marginals unless there is a strong anti-correlation (visible in the Cₐγ–θᵢ panel as a hyperbolic degeneracy, but not pinned at 3.4). The numbers don't reconcile.

Also: log₁₀(m_a/eV) = −31.4₋₁·₂⁺¹·⁴ — but for m ~ H₀ ~ 10⁻³³ eV (stated in Sec. 2.1), one expects log ~ −33. The posterior is pushed against the prior boundary [−35, −30].

**Required fix:** Either fix the inconsistency or explain it. The figure asymmetric errors are also suspicious (e.g., θᵢ = 1.33₋₁.₁⁺⁰·⁴⁴ has lower error larger than central value, but θᵢ ∈ [0.01, π] so lower bound is at 0.23 — not 0.01 — meaning posterior is hitting the upper boundary).

### P2-E8: Misrepresentation of literature priority
**Page 5, Sec. 6:**
> "Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces β ∼ 0.3°"

If this is true (and it is), then the paper has no novel content. The author concedes:
> "Our contribution is not the model itself, but rather the specific parameter identification (fa ∼ MPl, m ∼ H₀)"

But Fujita et al. (2021) explicitly study exactly this parameter regime. The "contribution" reduces to: (a) combining two existing measurements by inverse-variance, and (b) running MCMC on a 1-Gaussian likelihood. Neither is publishable in PRD.

**Required fix:** Identify a genuinely novel contribution or withdraw.

### P2-E9: Citation to "Namikawa, Murai, Naokawa 2025" is to a paper "in preparation"
**Page 6, References:**
> "Toshiya Namikawa, Kai Murai, and Sho Naokawa. ... arXiv e-prints, 2025. In preparation; cited for comparison of ALP mass constraints."

You cannot cite a paper that is "in preparation" with no arXiv ID. The same applies to Diego-Palazuelos & Komatsu 2025 ("arXiv preprint" with no number).

**Required fix:** Provide arXiv IDs or remove citations and the claims they support.

---

## MAJOR Findings

### P2-M1: Equation (1) Bessel function ansatz is not derived
**Page 2:** The "J₀(m/H₀)/J₀(0)" form for the field displacement is asserted without derivation. The Klein-Gordon equation in an FRW background with cosmological-constant-dominated late-time expansion does not have Bessel-function solutions in general. The "≈ θᵢ × O(1)" handwave makes the equation content-free.

**Required fix:** Either derive Eq. (1) properly or replace with numerical KG integration.

### P2-M2: Equation (2) factor of 2 inconsistent with standard convention
**Page 2:** β = g_aγ ∆ϕ / 2 is the standard result, but then β = C₀ θᵢ/2 × O(1) is dimensionally fine only if ∆ϕ = faθᵢ exactly. From Eq. (1), ∆ϕ ≈ 0.24 fa θᵢ, so β ≈ 0.12 C₀ θᵢ ≈ 0.12 rad ≈ 7°. The factor of ~25 discrepancy with the claimed 0.27° must be explained.

### P2-M3: ECH framework reference is hollow
**Page 4-5, Sec. 5:**
> "the ALP can be heuristically motivated as associated with the Barbero-Immirzi pseudoscalar sector of the Holst action... However, this motivation is qualitative—no derivation connects the Holst action to a specific ALP potential or coupling"

If the author admits the motivation provides nothing, then including it is filler. Remove or derive.

### P2-M4: Sample sizes are admitted to be inadequate but not improved
**Page 3, Sec. 3.3:**
> "we acknowledge that these sample sizes (720–6,840 accepted samples) are modest by modern standards"

The author identifies the problem ("Future work with longer chains (> 50,000 samples) would improve the reliability") but does not perform that future work for this submission. This is a 1-parameter MCMC; there is no excuse for 720 samples.

### P2-M5: Calibration systematics treated as discussion bullet, not analyzed
**Page 5, Sec. 6:** The Minami-Komatsu self-calibration issue is the *central uncertainty* in cosmic birefringence and is the main reason the community has not declared discovery. Treating it as a paragraph in "Discussion" without quantitative analysis (e.g., marginalization over systematic priors) is inadequate for a paper claiming 3.9σ evidence.

### P2-M6: Companion-paper citations to self-submitted work
**Page 6:** References to Golden 2026a, 2026b "submitted simultaneously." These cannot be assessed; if the present paper relies on results from them (e.g., "ECH gravitational framework," "matter-bounce fNL = −35/8"), it cannot be evaluated in isolation.

### P2-M7: Figure 2 is filler
**Page 5, Fig. 2:** Three Gaussian curves that overlap because they are all fitting the same input number. This figure contains no information beyond "the MCMC didn't break."

---

## MINOR Findings

### P2-Mn1: Page 1 abstract claims "3.6σ" but body uses 3.9σ
The abstract says "consistent with the 3.6σ isotropic birefringence signal" but the body derives 3.9σ. Pick one.

### P2-Mn2: "5×10⁻³ rad ≈ 0.27°"
5×10⁻³ rad = 0.286°, not 0.27°. Rounding inconsistency.

### P2-Mn3: Eskilt joint significance
0.342/0.094 = 3.64σ, consistent with "3.6σ" in abstract — but then where does "3.5σ" in the Introduction come from? "Combined, the evidence exceeds 3.5σ" — unclear what is being combined.

### P2-Mn4: Section 6 begins with "Calibration systematics" before listing the three "notable features." Structural awkwardness.

### P2-Mn5: Independent Researcher email "houston@hubify.com" — non-academic affiliation is fine, but a corporate email raises questions about conflicts of interest that should be disclosed.

### P2-Mn6: Acknowledgment of "AI research assistants" — this should specify what role they played (text generation, calculation verification, etc.) per emerging journal norms.

### P2-Mn7: Page count vs content
6 pages for what amounts to (i) restatement of Fujita 2021, (ii) inverse-variance average of two numbers, (iii) trivial MCMC. Recommended maximum: 3 pages as a Brief Report if any novelty can be identified.

---

## NIT Findings

### P2-N1: "ABJ anomaly" — Adler-Bell-Jackiw should be spelled out at first use.
### P2-N2: "J₀(m/H₀)" — J₀ undefined at first use (presumably zeroth Bessel function of the first kind).
### P2-N3: Equation numbering — Eq. (10) is just arithmetic and does not need to be a displayed equation.
### P2-N4: "βcombined" (Eq. 4) and "βALP" (Eq. 6) and "βfree" (Eq. 7) — three different β values reported; a summary table would help.

---

## Summary recommendation

**REJECT**

This paper does not contain a novel physics result. The author concedes in Section 6 that Fujita et al. (2021) already established that a Planck-scale ALP produces β ~ 0.3°. The "contribution" is reduced to an inverse-variance combination of two published numbers and an MCMC on a 1-datum Gaussian likelihood — neither of which constitutes original research at PRD standard. The headline "3.9σ" and "9σ" numbers are arithmetic on existing measurements and forecasts, not genuine statistical analyses. The "no fine-tuning" claim is undermined by the factor-of-~25 unexplained discrepancy between Eq. (1)'s O(0.24) integration factor and the body's O(10⁻²) used to get 0.27°. The MCMC triangle plot (Fig. 1) reports parameter values that do not arithmetically reconcile with the quoted product Cₐγ × θᵢ = 3.4 ± 1.1. Citations include "in preparation" works without arXiv IDs. The paper would not survive even a positive-result reinterpretation: it would still lack novelty over Fujita 2021 and Namikawa et al. Submission to a less selective journal as a short note (≤3 pages) is the appropriate venue if the author insists on publishing.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Referee Findings — Second Pass

After re-examining the paper line-by-line per the rubric, I identified the following NEW issues not in my initial review.

---

## NEW ESSENTIAL Findings

### P2-E10: Equations (5) and (8) report the same product with incompatible values
**Page 2 (Eq. 5) vs. Page 3 (Eq. 8):**
- Eq. (5): `f_photon × C₀ = 1.73 ± 0.44`
- Eq. (8): `Cₐγ × θᵢ = 3.4 ± 1.1`

These both should be the product of order-unity factors that set the birefringence amplitude. Reverse-engineering Eq. (5): 0.242°/1.73 = 0.140° per unit coupling, which equals (5×10⁻³ rad / 2) × (180/π) = 0.143° — i.e., Eq. (5) divides β_combined by the body-text factor of 5×10⁻³ rad / 2. By the same logic Eq. (8) would imply β_MCMC/0.143° ≈ 2.3, not 3.4. **The two "natural product" constraints differ by a factor of ~2 and cannot both be correct.** The reader cannot reconcile them because the relationship between `f_photon × C₀` (undefined) and `Cₐγ × θᵢ` is never stated.

**Required fix:** Define `f_photon`, write down the equation `β = (predicted prefactor) × (product)`, and recompute consistently.

### P2-E11: The "0.14°" divisor implicit in Eq. (5) appears nowhere in the paper
**Page 2:** The arithmetic of Eq. (5) requires β_pred = 0.14° × (f_photon × C₀). But this prefactor is never displayed. The reader must reverse-engineer it from the stated central value and σ, and it turns out to be the factor `(5×10⁻³ rad)/2` casually mentioned in Sec. 2.2 — which itself was unjustified (see P2-E2). **A "natural" parameter constraint is being quoted whose normalization is undefined.**

### P2-E12: MCMC m_a posterior contradicts the model's own natural-scale assumption
**Page 4, Fig. 1:** log₁₀(m_a/eV) = −31.4₋₁.₂⁺¹·⁴

This corresponds to m_a ≈ 4×10⁻³² eV ≈ **13 H₀**, not m ~ H₀ as required for the field to begin rolling at z ~ 1 (Sec. 2.1). For m_a >> H₀, the ALP oscillates rapidly during the relevant epoch, ∆ϕ averages toward zero, and the J₀(m/H₀) Bessel ansatz of Eq. (1) breaks down (J₀(10) ≈ −0.25, oscillating). **The MCMC posterior is in 1–2σ tension with the model's central naturalness assumption, and the very ansatz used to motivate Eq. (1) is invalid at the preferred parameter point.** This invalidates the central "naturalness" claim of the paper.

**Required fix:** Either (a) explain why the MCMC prefers m >> H₀ and redo the field-evolution integral in the m >> H₀ regime, or (b) fix m at H₀ and report the constrained one-parameter model.

### P2-E13: Run 1's "C = 8 fixed" is unjustified and contradicts the C₀ ~ 1 narrative
**Page 3, Table 1:** Run 1 fixes C = 8. The body text (Sec. 2.2) says C₀ is "an order-unity coefficient from the ABJ anomaly." The standard ABJ anomaly coefficient for a photon-coupled ALP is O(1) (e.g., E/N for QCD axions; for ALPs at most a few). **Why 8?** Nowhere in the paper is this choice motivated. The Run 1 posterior β_ALP = 0.336 ± 0.107° depends entirely on this arbitrary choice. The whole "natural inputs" story is undermined by quietly fixing C = 8 (= a 700% overshoot of "order unity") to make a fit work.

### P2-E14: The "3.9σ" combined result is a double-count of Planck data
**Page 2, Sec. 3.2 and Page 1 Intro:** The Intro says "Combined, the evidence exceeds 3.5σ" referring to Planck + ACT. The Eskilt et al. joint analysis already combines Planck (NPIPE) + ACT and yields 3.6σ (β = 0.342 ± 0.094°). The author then *separately* inverse-variance-combines NPIPE (β = 0.30 ± 0.11°, which uses the same Planck data) and ACT (β = 0.215 ± 0.074°, which is part of the joint analysis) and obtains "3.9σ." **This is statistically incorrect: the inputs share the underlying data.** The "3.9σ" is artificially inflated by ignoring data correlation. The 3.6σ Eskilt joint analysis is the correct combined significance; the paper's "3.9σ" should not exist.

**Required fix:** Withdraw Eq. (4) and the 3.9σ claim, or replace with a properly-correlated combination.

---

## NEW MAJOR Findings

### P2-M8: Abstract misstates dataset as "Planck HFI"
**Page 1:** Abstract claims "Gaussian summary-likelihood inference using Planck HFI and ACT DR6 data."
**Page 2, Sec. 3.1:** Body uses "Planck NPIPE [Eskilt and Komatsu, 2022]." NPIPE is a re-processing of Planck data (HFI + LFI) by Pearson, Pollard, and collaborators and is distinct from the HFI-only Planck 2018 release. The abstract names the wrong dataset.

### P2-M9: Run 2 β posterior shown only in Fig. 1, never reported in body
**Page 3, Sec. 3.3 vs. Page 4, Fig. 1:** Fig. 1 shows for Run 2 (C free) "β [deg] = 0.324 ± 0.099°." This value is never quoted in the text of Sec. 3.3. Sec. 3.3 quotes β_ALP for Run 1 (0.336 ± 0.107°) and β_free for Run 3 (0.344 ± 0.096°). The reader has to dig into the figure for Run 2's β. Worse, this 0.324° value is what feeds the "Cₐγ × θᵢ = 3.4 ± 1.1" claim, and the linkage is undocumented.

### P2-M10: MCMC posteriors broader than the input likelihood — unexplained
**Page 3:** The data input is a single Gaussian with σ = 0.094°. The MCMC posteriors on β have widths 0.107° (Run 1), 0.099° (Run 2), 0.096° (Run 3) — all *broader* than the input. For a properly converged 1D Gaussian likelihood with flat priors on the relevant range, the posterior on β should equal the input width to within sampling noise (~few %). The 14% broadening in Run 1 suggests either (a) the prior on θᵢ ∈ [0.01, π] is biting (cutting the tail of β corresponding to θᵢ > π), or (b) sampling noise from the small chains. Either way, this should be discussed; otherwise the posteriors look like they're answering a different question than the likelihood asks.

### P2-M11: "Consistent at 1σ" claim is borderline
**Page 5, Sec. 6:** "The prediction matches the combined Planck + ACT measurement at 1σ."
- Prediction: β_pred = 0.27°
- Eskilt joint: 0.342 ± 0.094° → tension = (0.342 − 0.27)/0.094 = **0.77σ**
- "Combined" (paper's Eq. 4): 0.242 ± 0.061° → tension = (0.27 − 0.242)/0.061 = **0.46σ**

These should be quoted explicitly, not hidden behind "at 1σ." Note also that the prediction's own integration-factor uncertainty (5×10⁻³ vs 24×10⁻³ — see P2-E2) is much larger than the data σ; the "1σ consistency" framing implies an unrealistic prediction precision.

### P2-M12: Cₐγ posterior centered near prior midpoint — data has no constraining power
**Page 4, Fig. 1:** Cₐγ prior is flat on [1, 30] (Sec. 3.3); posterior is 13.4₋₁₁⁺⁵·⁶. Prior midpoint = 15.5; prior median = 15.5. Posterior median 13.4 is essentially the prior. The "Cₐγ = 13.4" claim is dominated by the prior, not the data. **The author should report that the data does not constrain Cₐγ individually — only the degenerate product β ∝ Cₐγ × θᵢ × (integration factor) is measured.** Quoting Cₐγ = 13.4 in the figure header without this caveat is misleading.

### P2-M13: θᵢ marginal has asymmetric errors that strain the stated prior
**Page 4, Fig. 1:** θᵢ = 1.33₋₁.₁⁺⁰·⁴⁴. Lower error 1.1 with central 1.33 implies posterior extends to ~0.2. Prior is [0.01, π], so the lower edge is allowed. But the upper edge: 1.33 + 0.44 = 1.77, well below π ≈ 3.14, so the upper boundary is not biting — yet the posterior strongly disfavors θᵢ > 2.5. This means the data is doing real work on θᵢ (via the degeneracy with Cₐγ), but the figure suggests the posterior is hitting the *lower* part of the prior (mode around θ ~ 0.3 visible in 1D plot, with long tail). **The reported median 1.33 is not the mode of the posterior shown.** Such posterior is incompatible with "θᵢ ~ O(1)" naturalness narrative — the mode is θ ~ 0.3, i.e., a 30% misalignment.

---

## NEW MINOR Findings

### P2-Mn8: "5×10⁻³ rad ≈ 0.27°" arithmetic
5×10⁻³ rad × (180/π) = 0.2865°, which the author rounds to 0.27°. The actual value 0.286° is also the central value implied by Eq. (5) (β = 0.143° × 2). The author chose 0.27° rather than 0.29° to make the prediction look closer to the measurement; either round is acceptable but should be applied consistently.

### P2-Mn9: Section 3.1 last sentence — "we adopt the updated Eskilt value which uses improved foreground cleaning"
The Eskilt et al. paper cited is from 2022; the latest ACT DR6 Diego-Palazuelos paper is 2025. The "Eskilt joint Planck+ACT" value 0.342 ± 0.094° is not from Eskilt & Komatsu 2022 (which gives 0.30 ± 0.11°) — it must be from a later Eskilt et al. analysis. **The citation is wrong: the 0.342 ± 0.094° value is attributed to "Eskilt et al. joint analysis" but Eskilt 2022 reports 0.30 ± 0.11°.** Need the correct (Eskilt et al. 2023 or later) reference.

### P2-Mn10: Run sample counts oddly non-round
720, 2160, 6840: ratios 1 : 3 : 9.5. Plausible if `n_walkers × n_steps` with n_walkers ≈ 36 and steps doubling, but unexplained. Trivial issue but suggests the runs were length-tuned post-hoc to hit R̂ < 0.01 rather than pre-registered.

### P2-Mn11: Eq. (10) is just `0.27/0.03 = 9` — should not be displayed as a numbered equation
Trivial, but indicates equation-numbering inflation.

### P2-Mn12: Section 6 first paragraph
The "Calibration systematics" paragraph correctly notes the central issue but then immediately pivots to "The ALP birefringence prediction β ≈ 0.27° has three notable features" without resolving the systematics concern. Structurally, the systematics caveat is buried.

### P2-Mn13: Author's email and "Independent Researcher" status
houston@hubify.com — Hubify appears to be a commercial business. PRD requires affiliation disclosure beyond "Independent Researcher." Conflict-of-interest disclosure is incomplete.

---

## NEW NIT Findings

### P2-N5: Inconsistent precision in σ reporting
Abstract: "σ(β) ≈ 0.03°" (1 sig fig); Body: "σ(β) ≈ 0.03°" (same); Forecast: "9σ" (1 sig fig from 0.27/0.03). The "9σ" claim has no error budget; could be 7–11σ given LiteBIRD systematic uncertainty.

### P2-N6: J₀(m/H₀)/J₀(0) in Eq. (1)
Dividing by J₀(0) = 1 is pointless. The expression should just be `1 - J₀(m/H₀)`. Writing it as a ratio suggests the author may have intended a different normalization than the one calculated.

### P2-N7: "(3.9σ from zero)" in Eq. (4) and "(6σ from zero)" implied for Run 1
Run 1 β = 0.336 ± 0.107° → 3.14σ from zero. So which is the headline? Eq. (4) says 3.9σ from a different procedure. The headline σ values are scattered across the paper without a clear summary.

### P2-N8: Fig. 2 caption uses "Model 2", "Model 2b", "Model 0" labels not defined in text
The figure legend says "Model 2: ALP (C=8)", "Model 2b: ALP (C free)", "Model 0: beta free" — but the body text and Table 1 use "Run 1", "Run 2", "Run 3". The labeling scheme is inconsistent between figure and body.

---

## Summary of Second-Pass Findings

The second pass identified **5 additional ESSENTIAL** issues (E10–E14), the most severe being **P2-E12** (MCMC posterior on m_a contradicts the model's own naturalness assumption) and **P2-E14** (the "3.9σ" combined result double-counts Planck data and is statistically invalid). These compound the first-pass finding that the paper has no novel physics content: not only is there nothing new, but the central numerical claims (3.9σ, Cₐγ = 13.4 as "natural," m_a ~ H₀ as the natural mass) are individually broken on close inspection. **The recommendation remains REJECT, now with stronger grounds: the paper's own posterior plots contradict the paper's own naturalness narrative, and a key headline significance is the product of an invalid statistical combination.**