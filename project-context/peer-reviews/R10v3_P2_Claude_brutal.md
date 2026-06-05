# P2 R10v3 — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K
**Wall time**: 102.6s

---

# Referee Report: P2 — "Cosmic Birefringence from a Planck-Scale Axion-Like Particle"

## Overall Assessment

This paper claims a "natural" ALP explanation for cosmic birefringence, but the actual content amounts to: (a) a one-line back-of-envelope estimate that β ~ 0.27° using hand-waving O(1) factors, (b) a trivial inverse-variance combination of two published measurements, and (c) an underpowered MCMC over priors that essentially recover the input data. There is no new physics, no new derivation, no new data, and the authors themselves admit (Sec. 6) that Fujita et al. (2021) already made the same point. The contribution is effectively zero beyond what's already in the literature.

The paper also contains multiple arithmetic inconsistencies, internally contradictory sigma values, a key derivation that doesn't follow from the equation stated, and a "9σ forecast" that is not earned by the methodology.

---

## ESSENTIAL Findings

### P2-E1: Arithmetic inconsistency in summary-likelihood combination (Sec. 3.2, p. 2)
The paper combines β = 0.30 ± 0.11° (Planck NPIPE) and β = 0.215 ± 0.074° (ACT DR6) and claims:
> β_combined = 0.242 ± 0.061° (3.9σ from zero)

Recomputing inverse-variance weights:
- w₁ = 1/0.11² = 82.6; w₂ = 1/0.074² = 182.6
- β_combined = (82.6·0.30 + 182.6·0.215)/(82.6 + 182.6) = (24.78 + 39.26)/265.2 = **0.2416°** ✓
- σ_combined = 1/√265.2 = **0.0614°** ✓
- Significance = 0.2416/0.0614 = **3.93σ** ✓

The combination is correct, but the **datasets are not independent**: Planck NPIPE and ACT DR6 birefringence analyses share calibration assumptions, foreground modeling philosophies (the Minami–Komatsu self-calibration), and partially overlapping sky. Treating them as independent (Eq. 3) is unjustified and inflates the significance. **Required fix:** Either justify independence with a covariance argument or downgrade the claimed significance.

### P2-E2: The "0.27°" prediction is not derived — it is reverse-engineered
Sec. 2.2 states:
> "the cosmological field evolution gives ∆φ/fa ∼ 10⁻² (from the ratio of field displacement to decay constant over the Hubble time), yielding β ≈ C₀ θ_i × 5×10⁻³ rad ≈ 0.27°"

But Eq. (1) gives ∆φ ≈ f_a θ_i × O(1) with 1 − J₀(1) ≈ 0.24, i.e. ∆φ/f_a ~ 0.24, **not 10⁻²**. There is a factor ~24 inconsistency between Eq. (1) and the statement following Eq. (2). With ∆φ/f_a ~ 0.24 and C₀ ~ θ_i ~ 1, Eq. (2) gives β ~ 0.12 rad ≈ 6.9°, which is ~25× too large.

The "5×10⁻³ rad" factor appears with no derivation. The author has clearly inserted whatever number is needed to land on 0.27°. **This is the central physics claim of the paper and it does not follow from the equations stated.** Required fix: derive ∆φ/f_a explicitly from the Klein–Gordon equation in a ΛCDM background.

### P2-E3: Two different "βobs" values used interchangeably
- Abstract: β_obs = 0.342 ± 0.094° (Eskilt joint)
- Sec. 3.1: combined β = 0.242 ± 0.061° (NPIPE + ACT DR6)
- Sec. 3.3: β_obs = 0.342 ± 0.094° (Eskilt joint, used for MCMC)

The paper conflates these throughout. The abstract reports BOTH "β = 0.242 ± 0.061° (3.9σ from zero)" AND cites "β_obs = 0.342 ± 0.094° from the Eskilt et al. joint Planck + ACT analysis". These are not the same number and differ by >1σ. The methodology silently switches between them. Required fix: pick one analysis and be consistent, or explicitly justify why two different combinations are reported as central results.

### P2-E4: "9σ" LiteBIRD forecast inflated by using prediction not measurement uncertainty
Eq. (10): "Significance = 0.27/0.03 = 9σ"

This computes the significance assuming the central value is **exactly** 0.27° with zero theoretical uncertainty. But the author's own MCMC (Eq. 8) gives C_aγ × θ_i = 3.4 ± 1.1, a ~32% uncertainty. Propagating: σ_β,theory ~ 0.27 × 0.32 ≈ 0.087°. Total uncertainty √(0.03² + 0.087²) ≈ 0.092°, giving significance ~3σ, not 9σ. Additionally, "9σ" assumes the LiteBIRD measurement will land exactly at 0.27°; if it lands at the current best fit 0.342°, the distinguishability from β = 0 is what LiteBIRD measures, not what tests this *specific* model. **Required fix:** Distinguish between (a) LiteBIRD's intrinsic sensitivity to nonzero β and (b) LiteBIRD's ability to test this specific prediction at 9σ — the latter is not 9σ.

### P2-E5: Triangle plot (Fig. 1) inconsistent with text
Figure 1 caption: "posterior on the coupling-misalignment product C_aγ × θ_i is centered at 3.4 ± 1.1"

The triangle plot marginals show:
- θ_i = 1.33 +0.44/−1.1
- C_aγ = 13.4 +5.6/−11
- β = 0.324 ± 0.099°

Check: 1.33 × 13.4 = **17.8**, not 3.4. The product C_aγ × θ_i from the marginals is ~18, not 3.4. There is a factor of ~5 inconsistency. Possibly the author is reporting C₀ × θ_i (with C₀ ≠ C_aγ), but this is never clarified. Also, "C_aγ = 13.4" is not "order unity" by any reasonable definition — the prior in Sec. 3.3 explicitly states C_aγ ∈ [1,30], and the posterior median sits at 13, near the middle of the prior, indicating the data does not constrain C_aγ. The "natural O(1)" claim is broken.

### P2-E6: "Order-unity" claim contradicted by the data
Sec. 3.2: "f_photon × C₀ = 1.73 ± 0.44 (order-unity, no fine-tuning)"
Sec. 3.3: "C_aγ × θ_i = 3.4 ± 1.1" claimed "consistent with O(1)"
Fig. 1: C_aγ ≈ 13, θ_i ≈ 1.3, product ≈ 17

A coupling of C_aγ ~ 13 is not "natural" — it is the standard, well-known requirement that ALP explanations of birefringence need anomalously enhanced ABJ couplings (DFSZ has C_aγ ~ O(1), but KSVZ/string-axions can be larger). The paper's central marketing claim — that everything is O(1) with no fine-tuning — is contradicted by its own MCMC. **Required fix:** Either justify C_aγ ~ 13 as natural in a specific UV completion or retract the "no fine-tuning" claim.

### P2-E7: ln B = 5.17 Bayes factor is meaningless as stated
Sec. 3.4 admits "indicative; prior-dependent" but still places the number in the abstract as "ln B = 5.17 (indicative; prior-dependent, see Sec. 3.4)". A Bayes factor that varies by ±0.7 with prior range that the author chose arbitrarily is not evidence — it is a re-parameterization of the prior. Moreover, the Savage–Dickey computation with only N_eff ~ 1000 samples (as the author admits) cannot reliably estimate posterior density at β = 0, where the posterior is by construction far from the mode. **Required fix:** Remove ln B from the abstract, or properly characterize it as not interpretable.

### P2-E8: Sample sizes inadequate for claimed precision
Table 1: Runs of 720, 2160, 6840 samples. The author admits "N_eff ~ 1,000" is inadequate. Yet quotes β = 0.336 ± 0.107° to **three significant figures**, a Bayes factor to **three significant figures** (5.17), and Eq. (8) "3.4 ± 1.1" to two sig figs. With N_eff ~ 1000, the Monte Carlo uncertainty on the posterior mean is ~σ/√N ~ 0.107/√1000 ≈ 0.003° (OK), but the uncertainty on tail estimates needed for Bayes factors is much worse. **Required fix:** Either run longer chains or quote results with appropriate precision.

---

## MAJOR Findings

### P2-M1: No actual ALP simulation
There is no numerical integration of the ALP equation of motion (Klein-Gordon in FRW). Eq. (1) uses J₀ as a heuristic; the actual matter-to-dark-energy transition involves a non-trivial integration that the author waves at ("the precise value depends on the cosmological integration"). For a paper whose central claim is a numerical prediction (β ≈ 0.27°), this is unacceptable.

### P2-M2: The "MCMC" is essentially fitting noise
The likelihood is a single Gaussian on β_obs = 0.342 ± 0.094°. With only one data point and 2–3 free parameters (θ_i, m, C_aγ), the posterior on β must be ≈ the input data by construction (Eqs. 6, 7 both ≈ 0.34°). This is not a test of the model — it is a sanity check on the parameterization. The author presents it as if it validates the model.

### P2-M3: log₁₀(m/eV) prior of [−35, −30] is exotic and unmotivated
Sec. 3.3 uses log₁₀(m/eV) ∈ [−35, −30]. m ~ H₀ corresponds to log₁₀(m/eV) ≈ −33. The prior is fine for that, but Fig. 1 shows the posterior on log₁₀(m_a/eV) = −31.4 +1.4/−1.2, which is **two orders of magnitude heavier than H₀** (~10⁻¹ eV·10⁻³³ ≈ 10⁻³³ eV). This contradicts the central claim "m ~ H₀". The data prefers m ~ 100 H₀.

### P2-M4: Self-citation to non-existent companion papers
References [Golden 2026a] and [Golden 2026b] are "companion paper, submitted simultaneously". No arXiv ID, no DOI. PRD does not accept references to unsubmitted/unverifiable companion work as load-bearing citations. Sec. 5 leans heavily on [Golden 2026a] for the "ECH gravity" motivation; Sec. 6 leans on [Golden 2026b] for non-Gaussianity. Required fix: either provide arXiv IDs or remove the citations.

### P2-M5: ECH gravity invocation is purely decorative
Sec. 5 admits: "this motivation is qualitative — no derivation connects the Holst action to a specific ALP potential or coupling". So why is it in the paper? It exists only to cross-promote the companion paper. Required fix: remove Sec. 5 entirely or replace with a single sentence.

### P2-M6: "Independent Researcher" + "AI research assistants"
The Acknowledgments state "The author acknowledges the use of AI research assistants during the analysis and manuscript preparation." Combined with the level of derivation handwaving (E2), arithmetic inconsistencies (E1, E5), and circular MCMC (M2), the paper has the hallmarks of LLM-generated calculation. Required fix: this is not disqualifying per se, but every numerical claim must be reproducible from a publicly available computational notebook. Currently none is provided.

### P2-M7: "3.6σ" vs "3.9σ" — which is it?
Abstract: "3.6σ isotropic birefringence signal (β_obs = 0.342±0.094° from the Eskilt et al. joint Planck + ACT analysis)". Check: 0.342/0.094 = 3.64σ ✓. Also abstract: "0.242 ± 0.061° (3.9σ from zero)". Both are reported with no clear hierarchy. The body uses both interchangeably. Pick one as primary.

### P2-M8: Eskilt 2022 ≠ Eskilt joint Planck + ACT
The Eskilt & Komatsu 2022 paper is the WMAP + Planck combination. The "Eskilt et al. joint Planck + ACT" referenced in the abstract is a separate analysis. The citation list does not include a Planck+ACT joint Eskilt analysis. Required fix: cite the actual reference for β = 0.342 ± 0.094°.

### P2-M9: Fujita et al. 2021 already made this prediction
Sec. 6 explicitly states: "Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces β ∼ 0.3°". Given this, the contribution of the present paper is unclear. The author claims "the specific parameter identification (f_a ~ M_Pl, m ~ H₀)" — but Fujita et al. consider exactly this regime. The paper does not advance the state of the literature.

### P2-M10: No treatment of anisotropic birefringence
The paper discusses only isotropic β. ALP models generically predict anisotropic birefringence with a specific power spectrum. ACT and Planck both have anisotropic constraints that constrain this scenario. Ignoring this is a significant omission.

### P2-M11: Namikawa, Murai & Naokawa cited as "in preparation"
> "Toshiya Namikawa, Kai Murai, and Sho Naokawa. Constraints on axion-like particles from cosmic birefringence. arXiv e-prints, 2025. In preparation; cited for comparison of ALP mass constraints."

Cannot cite unsubmitted work as evidence. Required fix: remove or provide arXiv ID.

---

## MINOR Findings

### P2-Mi1: Figure 2 axis and caption
Figure 2 caption says "All three are consistent with each other and with the observed value β_obs = 0.342 ± 0.094°". The figure axis shows β [deg] ranging −0.1 to 0.8. The vertical dotted line at 0.342° is visible. OK, but the green shaded band is not defined in the caption. Required fix: define the shaded band.

### P2-Mi2: J₀ derivation in Eq. (1)
The J₀ function appears with no derivation. For a cosine potential, the field oscillation gives Bessel-like solutions; the author should either derive this or cite the analytic result.

### P2-Mi3: "f_photon × C₀" terminology
This product is never defined. Is f_photon a dimensionful decay constant in units of M_Pl? Is it C₀ × θ_i? The notation switches across sections (C₀, C_aγ, f_photon) without a defined glossary.

### P2-Mi4: Page count vs content
6 pages including references for a paper with no new derivation, no new simulation, no new data, and an MCMC that fits a single Gaussian data point. The actual content fits in ~2 pages. Recommended maximum: 3 pages as a "Brief Report" or "Comment".

### P2-Mi5: Eq. (2) factor confusion
β = (g_aγ/2) ∆φ = (C₀/2f_a) ∆φ. But the standard relation is β = (g_aγ/2)(φ_late − φ_early). For φ ≈ f_a θ_i × O(1), this gives β = (C₀ θ_i/2) × O(1), as written. The O(1) absorbing 1−J₀(1) ≈ 0.24 makes the final coefficient 0.12, not 0.005 (see E2).

### P2-Mi6: "5×10⁻³ rad" → "0.27°" arithmetic
5×10⁻³ rad × (180/π) = 0.286° (not 0.27°, but close enough). OK.

### P2-Mi7: Abstract claim "fphoton × C0 = 1.73 ± 0.44" 
Why this specific product, and what does the numerical value mean physically? The abstract reports it as if it were a coupling measurement, but it is an emergent parameter from a Gaussian combination of two measurements — not a constraint on fundamental physics.

---

## NITs

### P2-N1: Equation cross-reference (Eq. 3)
"We use two independent birefringence measurements for the summary-likelihood combination (Eq. 3)" — Eq. 3 is two paragraphs later. OK, but a forward reference to an equation appearing on the same page is fine.

### P2-N2: Inconsistent reference formatting
Some references have DOIs (Minami & Komatsu, Eskilt & Komatsu) and some don't (Diego-Palazuelos & Komatsu).

### P2-N3: Email in author block
"houston@hubify.com" — fine, but unusual for a PRD submission from a corporate domain by an "Independent Researcher".

### P2-N4: Date "March 20, 2026"
Future-dated submission. Not flagged as wrong; standard practice for camera-ready dates.

---

## Cross-Reference Audit (Abstract vs Body)

| Abstract claim | Body verification |
|---|---|
| β ≈ 0.27° prediction | Sec. 2.2 — **NOT derived**, see E2 |
| β_obs = 0.342±0.094° (3.6σ) | Sec. 3.1 — Eskilt joint cited, 3.64σ ✓ |
| β = 0.242±0.061° (3.9σ from zero) | Sec. 3.2 — arithmetic correct, but independence assumption questionable (E1) |
| f_photon × C₀ = 1.73 ± 0.44 (no fine-tuning) | Sec. 3.2 — but Fig. 1 shows C_aγ ~ 13 (E6) |
| ln B = 5.17 | Sec. 3.4 — admittedly prior-dependent (E7) |
| σ(β) ≈ 0.03° → 9σ | Sec. 4 — overstated (E4) |

---

## Summary recommendation

**REJECT**

This paper does not meet the threshold for publication in Physical Review D. The central physics claim — β ≈ 0.27° from a natural ALP — is not derived from the equations stated (the factor 5×10⁻³ rad/(O(1)) in Sec. 2.2 contradicts Eq. (1) by a factor ~25). The MCMC posterior on Fig. 1 contradicts the textual claim of "order-unity" couplings (C_aγ ~ 13, m ~ 100 H₀). The "9σ" LiteBIRD forecast does not propagate theoretical uncertainty and is overstated by a factor of ~3. The Bayes factor is admittedly prior-dependent and not interpretable at the chain length used. The author acknowledges that Fujita et al. (2021) already made this prediction, leaving no clear contribution. Companion papers cited as load-bearing references do not exist in any verifiable form. The paper is best characterized as a derivative repackaging of existing literature combined with an inverse-variance combination of two published numbers, padded to six pages.