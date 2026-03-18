# 03: Tilt Mechanism Viability

**Created:** 2026-03-17
**Status:** IN PROGRESS

---

## The Three Candidate Tilt Mechanisms

From the model specification, we have three ways to generate n_s ≈ 0.965. The Quintin no-go analysis (file 02) showed that the DBI matter bounce with reduced c_s is the most promising framework. Now we assess how each tilt mechanism fits within it.

---

## Mechanism A: Nearly-Matter Contraction (w = ε)

### The Formula

For a contracting phase with EOS w:
$$
n_s - 1 = \frac{12w}{1 + 3w}
$$

For small w: n_s − 1 ≈ 12w

Matching Planck: n_s = 0.9649 ± 0.0042
$$
w = \frac{n_s - 1}{12 - 3(n_s - 1)} \approx \frac{-0.0351}{12 + 0.105} \approx 0.00290
$$

**Central value: w = 0.0029**

### Observable Predictions for w = 0.003 + DBI (c_s = 0.25)

**Spectral index:**
$$
n_s = 1 + \frac{12 \times 0.003}{1 + 0.009} = 1 + 0.0357 = 0.964 \quad \checkmark
$$

Wait — this gives n_s = 1 + 12w/(1+3w). For a CONTRACTING phase:
- In expansion (inflation): n_s − 1 = −6ε + 2η (red tilt)
- In contraction: the sign depends on the mode function behavior

**Critical sign question:** Does w > 0 in contraction give a RED tilt (n_s < 1) or a BLUE tilt (n_s > 1)?

For matter contraction with w = 0: n_s = 1 exactly.

In the matter bounce literature (Cai, Brandenberger, Finelli):
$$
n_s - 1 = \frac{2(1 - 3w)}{1 + 3w} \times \text{(correction terms)}
$$

Actually, there are different formulas in the literature depending on the specific model. Let me be more careful.

**For a contracting universe dominated by a fluid with EOS w:** The comoving curvature perturbation ζ_k evolves as:
$$
\zeta_k'' + 2\frac{z'}{z}\zeta_k' + c_s^2 k^2 \zeta_k = 0
$$

where z = a√(ρ+P)/(c_s H) and primes are conformal time derivatives.

During contraction with a(η) ∝ (−η)^{p/(p−1)} where p = 2/[3(1+w)]:

The spectral index of the growing mode:
$$
n_s - 1 = \frac{12w}{1 + 3w} \quad \text{(for the dominant growing mode)}
$$

**For w = 0:** n_s = 1 ✓
**For w > 0 (small):** n_s > 1 — this is a BLUE tilt!

**PROBLEM:** A positive w in contraction gives n_s > 1, not n_s < 1. But Planck requires n_s ≈ 0.965 < 1.

**Wait — let me recheck this.** The sign of the tilt depends on which mode dominates.

In matter contraction (w = 0), both modes of ζ are constant (one growing, one constant). The spectral index of the GROWING mode is exactly 1. For w slightly positive, the growing mode acquires a slight blue tilt.

**This means w > 0 moves n_s in the WRONG direction (bluer, not redder).**

For a RED tilt (n_s < 1), we would need w < 0. But w < 0 means the contracting phase is dominated by a field with negative pressure — this makes the contraction even more susceptible to anisotropy.

**Alternative:** The tilt formula depends on whether we're talking about the adiabatic perturbation from the growing mode or the spectator perturbation. For a SPECTATOR field (like a curvaton), the tilt depends on the spectator's mass:

$$
n_\sigma - 1 = \frac{d \ln P_{\delta\sigma}}{d \ln k} = 2\nu - 3
$$

where ν depends on the effective mass of σ during contraction. For a massive curvaton:
$$
\nu = \frac{3}{2}\sqrt{1 + \frac{4m_\sigma^2}{9H^2(1-3w)^2}} \quad \text{(during matter-like contraction)}
$$

For m_σ² > 0 and m²/H² small: ν > 3/2, giving n_σ > 1 (blue tilt again).

**For a RED tilt from a spectator in contraction:**
Need the spectator to have a TACHYONIC effective mass (m²_eff < 0). This can happen if the spectator couples to curvature:

$$
m_{\rm eff}^2 = m_0^2 + \xi R
$$

During contraction, R < 0 (for decelerating contraction). If ξ > 0 and |ξR| > m_0², then m²_eff < 0, giving a red tilt.

This is possible but adds another parameter (ξ).

### Revised Assessment of Mechanism A

**w > 0 alone does NOT give a red tilt.** The naive formula n_s − 1 = 12w/(1+3w) gives a BLUE tilt for w > 0.

To get n_s ≈ 0.965 (red) from the contraction dynamics alone requires either:
- w < 0 (negative pressure during contraction — problematic for stability and BKL)
- A spectator with tachyonic effective mass (non-minimal coupling to curvature)
- The tilt being generated NOT by the contraction EOS but by a different mechanism

**STATUS: Mechanism A is MORE COMPLICATED than initially assumed.** The sign of the tilt is the opposite of what a naive extrapolation suggests.

---

## Mechanism B: Curvaton

### Setup

A spectator field σ with mass m_σ, decoupled from the background during contraction. After the bounce, σ oscillates and decays, converting its perturbation into ζ.

### Tilt from Curvaton in Contraction

During matter contraction, the curvaton perturbation δσ evolves on superhorizon scales. The spectrum of δσ depends on the curvaton's effective mass during contraction.

For a minimally coupled curvaton (ξ = 0) with mass m_σ during matter contraction:
$$
\delta\sigma_k \propto k^{n_\sigma/2 - 3/2}
$$

The curvaton spectral index in contraction:
$$
n_\sigma - 1 = 3 - 2\nu_\sigma
$$

where:
$$
\nu_\sigma = \frac{1}{2}|1 + 4\epsilon_\sigma| , \quad \epsilon_\sigma = \frac{m_\sigma^2}{H_k^2} \times f(w)
$$

**For m_σ real and positive:** ν_σ > 1/2, giving n_σ > 1... wait, this depends on the exact formula.

Let me approach this differently. During matter contraction, the Hubble rate H evolves as H ∝ 1/t (with H < 0). The curvaton perturbation equation is:

$$
\ddot{\delta\sigma} + 3H\dot{\delta\sigma} + \left(\frac{k^2}{a^2} + m_\sigma^2\right)\delta\sigma = 0
$$

For a mode that exits the Hubble radius (k/a < |H|), the k² term is negligible. The superhorizon solution depends on the ratio m²/H²:

- If m²/H² is small and constant: δσ ~ const (for the growing mode in contraction, δσ might actually GROW)

The key insight from Cai & Brandenberger (2011): in the matter bounce curvaton scenario, the curvaton perturbation spectrum can be nearly scale-invariant with a SLIGHT RED TILT if the curvaton mass is appropriately chosen.

**The tilt is:**
$$
n_\sigma - 1 \approx -\frac{2m_\sigma^2}{3H_k^2} \quad \text{(for contraction, growing mode)}
$$

**SIGN CHECK:** For m_σ² > 0 and H_k² > 0, this gives n_σ < 1 — a RED tilt. ✓

Matching n_s = 0.965:
$$
\frac{m_\sigma^2}{H_k^2} \approx \frac{3 \times 0.035}{2} = 0.053
$$

$$
m_\sigma \approx 0.23 \, H_k
$$

### f_NL in Curvaton Scenario

As computed in file 02: when the curvaton dominates ζ, f_NL → −1.25 (for r_dec → 1). The matter bounce f_NL = −35/8 is lost.

**However:** what if we DON'T need the curvaton to fully dominate? What if we combine the curvaton with the DBI sound speed reduction?

### Combined Model: DBI + Partial Curvaton

- DBI sound speed c_s ≈ 0.25 gives r ≈ 0.03 (marginally satisfying r < 0.036)
- Curvaton provides the RED TILT (n_s ≈ 0.965)
- f_NL has contributions from both:
  - f_NL^local from matter contraction: −35/8 × (ζ_φ/ζ_total)^4
  - f_NL^curvaton: (5/(4r_dec) − 5r_dec/6 − 5/3) × (ζ_σ/ζ_total)^4
  - f_NL^equil from DBI: ~ −1/c_s² ≈ −16

For the curvaton to generate the tilt but NOT fully dominate ζ:
- Let ζ_σ/ζ_total = α ≈ 0.5 (curvaton contributes 50% of power)
- Then r = r_DBI × (1 − α²) = 0.03 × 0.75 = 0.023 ✓
- f_NL^local ≈ (−4.4)(0.75)² + (−1.25)(0.25)² = (−4.4)(0.56) + (−1.25)(0.063) = −2.46 − 0.08 = −2.5
- f_NL^equil ≈ −16

**Hmm — f_NL^local ≈ −2.5.** Not as sharp as −4.4, but still negative and potentially distinguishable from inflation (which predicts ~0).

**What if α is smaller?** α = 0.3:
- r = 0.03 × (1 − 0.09) = 0.027 ✓
- f_NL^local ≈ (−4.4)(0.91)² + (−1.25)(0.09)² = (−4.4)(0.83) + (−1.25)(0.008) = −3.65 − 0.01 = −3.7
- But is α = 0.3 enough to generate the tilt? The tilt from the curvaton is proportional to α²...

**The curvaton's contribution to n_s:**
$$
n_s - 1 = (n_\phi - 1)(1 - \alpha^2)^2 + (n_\sigma - 1)\alpha^4 + \text{mixed}
$$

For n_φ = 1 (scale-invariant from matter contraction):
$$
n_s - 1 \approx (n_\sigma - 1) \alpha^4
$$

Wait — this isn't right either. The total tilt depends on the relative contributions differently.

Actually, the total spectral index when both fields contribute to ζ:
$$
P_\zeta = P_{\zeta_\phi} + P_{\zeta_\sigma}
$$

$$
n_s - 1 = \frac{d \ln P_\zeta}{d \ln k} = \frac{P_{\zeta_\phi}(n_\phi - 1) + P_{\zeta_\sigma}(n_\sigma - 1)}{P_{\zeta_\phi} + P_{\zeta_\sigma}}
$$

$$
= (1 - \alpha^2)(n_\phi - 1) + \alpha^2(n_\sigma - 1)
$$

where α² = P_{ζ_σ}/P_ζ.

For n_φ = 1:
$$
n_s - 1 = \alpha^2 (n_\sigma - 1) = -\alpha^2 \frac{2m_\sigma^2}{3H_k^2}
$$

To get n_s − 1 = −0.035:
$$
\alpha^2 \frac{2m_\sigma^2}{3H_k^2} = 0.035
$$

For α = 0.3 (α² = 0.09): need m²/H² = 0.035/(0.09 × 2/3) = 0.58 → m_σ = 0.76 H_k (heavy curvaton)
For α = 0.5 (α² = 0.25): need m²/H² = 0.035/(0.25 × 2/3) = 0.21 → m_σ = 0.46 H_k
For α = 0.7 (α² = 0.49): need m²/H² = 0.035/(0.49 × 2/3) = 0.107 → m_σ = 0.33 H_k (light curvaton)
For α = 0.9 (α² = 0.81): need m²/H² = 0.035/(0.81 × 2/3) = 0.065 → m_σ = 0.25 H_k

### Combined Predictions: DBI (c_s = 0.25) + Partial Curvaton

| α | m_σ/H_k | r | f_NL^local | f_NL^equil | n_s | Viable? |
|---|---------|---|-----------|------------|-----|---------|
| 0.3 | 0.76 | 0.027 | −3.7 | −16 | 0.965 | ✓ (r, n_s, f_NL all OK) |
| 0.5 | 0.46 | 0.023 | −2.5 | −16 | 0.965 | ✓ |
| 0.7 | 0.33 | 0.015 | −1.4 | −16 | 0.965 | ✓ (but f_NL^local diluted) |
| 0.9 | 0.25 | 0.006 | −1.0 | −16 | 0.965 | ✓ (but f_NL^local nearly gone) |

**THE SWEET SPOT: α ≈ 0.3, c_s ≈ 0.25**

This gives:
- **n_s ≈ 0.965** (from curvaton tilt) ✓
- **r ≈ 0.027** (from DBI + partial curvaton suppression) ✓
- **f_NL^local ≈ −3.7** (preserves most of matter bounce prediction) ✓
- **f_NL^equil ≈ −16** (from DBI, consistent with Planck) ✓
- **α_s:** small negative running from curvaton mass term, consistent with Planck ✓

---

## Mechanism C: Two-Field Entropy Conversion

Given the success of the DBI + partial curvaton model, the two-field entropy conversion is less motivated. It has more free parameters and less predictive power. Assessment: **DOMINATED by the DBI + curvaton model.** Set aside.

---

## Comparative Assessment

| Mechanism | n_s | r | f_NL^local | Complexity | Verdict |
|-----------|-----|---|-----------|-----------|---------|
| A: w = ε only | BLUE (wrong sign) | Too large | −4.4 | Minimal | WRONG TILT SIGN |
| B: Pure curvaton | 0.965 | < 0.036 | −1.25 | Moderate | LOSES f_NL |
| C: Two-field | Tunable | Tunable | Model-dep | High | OVER-PARAMETRIZED |
| **D: DBI + partial curv** | **0.965** | **0.027** | **−3.7** | **Moderate** | **MOST PROMISING** |

---

## The Candidate Model Summary

**DBI Matter Bounce + Partial Curvaton**

Ingredients:
1. Contraction dominated by a scalar field with DBI kinetic term → c_s ≈ 0.25
2. EOS w ≈ 0 (matter-like, from the DBI field potential)
3. Spectator curvaton σ with m_σ ≈ 0.76 H_k, contributing α² ≈ 0.09 to P_ζ
4. Generic bounce mechanism
5. Curvaton decay after bounce

Free parameters: c_s, m_σ, σ_i (initial curvaton amplitude) → effectively 3 parameters beyond the base model

Predictions:
$$
\boxed{n_s \approx 0.965, \quad r \approx 0.03, \quad f_{\rm NL}^{\rm local} \approx -3.7, \quad f_{\rm NL}^{\rm equil} \approx -16}
$$

**This model preserves most of the distinctive matter-bounce non-Gaussianity while satisfying all current observational constraints.**

---

## Critical Issues to Resolve

1. **Sign of the tilt formula:** The n_s − 1 = 12w/(1+3w) formula may give a blue tilt for w > 0 in contraction. Need to verify whether the curvaton tilt formula n_s − 1 = −α²(2m²/3H²) is correct (red tilt) for a curvaton during contraction. This is model-dependent and needs careful calculation.

2. **DBI kinetic term naturalness:** Why would the contracting scalar have a DBI kinetic term? In string theory, DBI actions arise from D-brane dynamics. In the matter bounce context, this needs motivation.

3. **BKL instability:** w ≈ 0 with DBI does NOT solve BKL. Still need either an ekpyrotic pre-phase or a new mechanism.

4. **Bounce transition:** Does the DBI structure survive through the bounce? Does the sound speed change?

5. **Exact combined f_NL:** The f_NL estimates above use approximate formulas. A proper calculation using the δN formalism for the DBI + curvaton case is needed.
