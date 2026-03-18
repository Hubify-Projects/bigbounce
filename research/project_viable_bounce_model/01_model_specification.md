# 01: Model Specification — Minimal Viable Bounce Model

**Created:** 2026-03-17
**Status:** IN PROGRESS

---

## The Goal

Define the minimum-ingredient bounce model that could simultaneously satisfy:
1. n_s ≈ 0.965
2. f_NL^local ≈ −4.4 (or calculable variant)
3. r < 0.036
4. α_s consistent with Planck (−0.005 ± 0.007)
5. BKL stability during contraction
6. A clean bounce mechanism

---

## The Base Model: Single-Field Matter Bounce

**Background:**
- Contraction phase: a(t) ∝ (-t)^{2/3} for matter (w = 0)
- Bounce: generic (modified Friedmann, e.g., H² = (ρ/3M²)(1 − ρ/ρ_c))
- Expansion: radiation domination after bounce

**Predictions (single-field, w = 0):**
| Observable | Prediction | Observation | Status |
|-----------|-----------|-------------|--------|
| n_s | 1.000 | 0.9649 ± 0.0042 | EXCLUDED (8.3σ) |
| r | O(1) — see Quintin | < 0.036 | EXCLUDED |
| f_NL^local | −35/8 ≈ −4.375 | −0.9 ± 5.1 | Compatible |
| α_s | 0 | −0.005 ± 0.007 | Compatible |

**Two fatal problems:** n_s = 1 and r = O(1). The f_NL prediction is the asset we want to preserve.

---

## Extension A: Nearly-Matter Contraction (w = ε)

Replace exact dust (w = 0) with a scalar field whose EOS has small positive pressure.

**Mechanism:** A scalar field φ with potential V(φ) in the contraction phase. If V(φ) provides a small positive pressure contribution, w = P/ρ = (φ̇²/2 − V)/(φ̇²/2 + V) = ε > 0.

**Tilt formula:**
$$
n_s - 1 = \frac{12w}{1 + 3w} \approx 12w \quad \text{for small } w
$$

Matching n_s = 0.965 requires w ≈ 0.00292.

**Free parameters:** 1 (the EOS w, or equivalently the scalar potential slope)

**What changes:**
- n_s: FIXED (by design, w = 0.003)
- f_NL: needs computation — is f_NL(w = 0.003) still ≈ −35/8?
- r: the Quintin scaling r ∝ |f_NL|^{4/3} — does it still apply for w ≠ 0?
- α_s: small running, needs computation

**Critical unknowns (awaiting literature research):**
1. f_NL(w) for small w — does it diverge, stay constant, or change sign?
2. r(w) for small w — does the Quintin relation change?
3. BKL stability — w = 0.003 << 1, so BKL instability still present

---

## Extension B: Matter Bounce + Curvaton

Keep w = 0 contraction for the background. Add a spectator curvaton field σ with mass m_σ.

**Mechanism:** During contraction, both φ (matter) and σ (curvaton) are present. The matter field φ dominates the background (w = 0). The curvaton σ acquires perturbations δσ. After the bounce, σ oscillates and decays, converting its isocurvature perturbation into curvature perturbation ζ.

**Tilt from curvaton:**
$$
n_s - 1 \approx -\frac{2m_\sigma^2}{H_k^2}
$$
where H_k is the Hubble rate when mode k exits the horizon during contraction.

Matching n_s = 0.965 requires m_σ ≈ 0.13 H_k.

**r suppression:** The curvaton enhances P_ζ without affecting P_T:
$$
r = r_{\rm single} \times \left(\frac{\zeta_\phi}{\zeta_{\rm total}}\right)^2
$$
If the curvaton dominates ζ (r_dec → 1), then r is suppressed by (ζ_φ/ζ_total)² ≪ 1.

**f_NL in curvaton scenario:** This is the critical question.
- If curvaton dominates: f_NL^curvaton = 5/(4r_dec) − 5r_dec/6 − 5/3
- For r_dec → 1: f_NL → 5/4 − 5/6 − 5/3 = −5/4 ≈ −1.25
- For r_dec small: f_NL → 5/(4r_dec) → large positive

**Key tension:** If the curvaton dominates ζ (to suppress r), then f_NL is set by the CURVATON, not by the matter contraction. We LOSE the distinctive f_NL = −35/8 prediction.

**Free parameters:** 3 (m_σ, initial amplitude σ_i, decay rate Γ_σ — equivalently: n_s, r_dec, r)

---

## Extension C: Two-Field Entropy Conversion

Two fields φ and χ both present during contraction. φ is the matter field (w ≈ 0), χ provides a second degree of freedom. At or near the bounce, an isocurvature-to-curvature transfer occurs.

**Mechanism:** The two fields have different EOS or potentials, creating a relative perturbation (isocurvature mode S). At the bounce, a transfer function T_RS converts S into ζ with possible k-dependence.

**Tilt:** n_s − 1 depends on the transfer function, which is model-dependent.

**f_NL:** Depends on the nonlinear transfer. Could preserve, modify, or erase the matter bounce f_NL.

**Free parameters:** Many (two potentials, transfer function, coupling). This is over-parametrized.

---

## Extension D: Hybrid — Nearly-Matter + Curvaton

Combine w ≈ 0.003 contraction with a light curvaton. The curvaton provides ADDITIONAL tilt and r suppression, while the modified EOS provides a base tilt.

**Motivation:** If w = 0.003 already gives n_s ≈ 0.965 from the adiabatic mode, the curvaton only needs to suppress r (not generate the full tilt). This means r_dec can be larger → curvaton contribution to f_NL is smaller → the underlying matter bounce f_NL may dominate.

**This is potentially the sweet spot:** the tilt comes from w ≠ 0, and the curvaton just suppresses r.

**Free parameters:** 2 main (w and curvaton r_dec)

---

## Model Comparison

| Model | Free params (beyond base) | n_s fix | r fix | f_NL prediction | BKL | Overall |
|-------|--------------------------|---------|-------|----------------|-----|---------|
| A: w = ε | 1 | ✓ (w = 0.003) | ? (Quintin?) | ? (f_NL(w)) | ✗ (w < 1) | NEEDS COMPUTATION |
| B: Curvaton | 3 | ✓ (m_σ) | ✓ (r_dec) | LOSES −35/8 | ✗ (still w=0) | KILLS f_NL PREDICTION |
| C: Two-field | Many | ✓ | ✓ | Model-dependent | ✗ | TOO MANY PARAMETERS |
| D: w = ε + curvaton | 2 | ✓ (w) | ✓ (r_dec) | MAY PRESERVE | ✗ (w < 1) | MOST PROMISING — NEEDS CALC |

---

## Critical Questions (Being Researched)

1. **f_NL(w) for w = 0.003:** Does the matter bounce f_NL change significantly for small w?
2. **Quintin no-go for w ≠ 0:** Does the r ∝ |f_NL|^{4/3} relation hold?
3. **Curvaton f_NL in bounce:** When the curvaton partially dominates, what is the combined f_NL?
4. **BKL for all models:** w < 1 means BKL instability survives in every variant

---

## Minimum Ingredients Assessment

**The absolute minimum viable model appears to require:**
1. A contraction phase with w slightly above 0 (for tilt)
2. A bounce mechanism (generic)
3. Either a curvaton (for r suppression) or a mechanism to decouple r from f_NL

**The BKL problem persists in ALL near-matter models.** This is the most serious structural issue — it cannot be solved by any of Extensions A-D. It requires either:
- An initial ekpyrotic phase before the matter phase (adds complexity)
- A new mechanism (e.g., anisotropy damping at the bounce)
- Accepting it as a fine-tuning of initial conditions

**Pending:** Agent research results on Quintin evasion, f_NL(w), and BKL solutions.
