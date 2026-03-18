# 04: Joint Constraint Analysis

**Created:** 2026-03-17
**Status:** IN PROGRESS

---

## The Candidate Model

**DBI Matter Bounce + Partial Curvaton** (from files 02-03)

Parameters:
- c_s: sound speed of the DBI scalar during contraction
- α: curvaton fraction of total ζ (α² = P_{ζ_σ}/P_ζ_total)
- m_σ/H_k: curvaton mass in Hubble units (determines tilt)
- r_dec: curvaton density fraction at decay (determines curvaton f_NL contribution)

### Parameter Relations

The tilt fixes m_σ/H_k as a function of α:
$$
\frac{m_\sigma^2}{H_k^2} = \frac{3(1 - n_s)}{2\alpha^2} = \frac{0.0527}{\alpha^2}
$$

The tensor-to-scalar ratio:
$$
r = r_{\rm DBI} \times (1 - \alpha^2) = 16 c_s \epsilon_{\rm matter} \times (1 - \alpha^2)
$$

where ε_matter is the slow-roll-like parameter during contraction. For matter-dominated contraction, ε = 3(1+w)/2 ≈ 3/2.

$$
r \approx 24 c_s (1 - \alpha^2)
$$

Wait — this gives r = 24 × 0.25 × 0.91 = 5.5 for c_s = 0.25 and α = 0.3. That's way too large!

**Let me reconsider.** The formula r = 16c_sε applies in inflation. In contracting cosmology, the relation is different because perturbations grow on superhorizon scales.

### Correct r in Matter Bounce

In the matter bounce, the tensor and scalar spectra are:

**Tensor:** P_T is set by the Hubble rate during contraction when the mode exits the horizon:
$$
P_T = \frac{2H_k^2}{\pi^2 M_{\rm Pl}^2}
$$

**Scalar (matter field only):** The scalar power spectrum is amplified by the growth of ζ on superhorizon scales. For matter contraction (w = 0):
$$
P_\zeta = \frac{H_k^2}{8\pi^2 M_{\rm Pl}^2 \epsilon c_s} \times (\text{growth factor})^2
$$

The growth factor depends on how long modes spend outside the Hubble radius between horizon exit during contraction and horizon re-entry during expansion. This factor can be VERY large — it's what makes the scalar spectrum dominant.

In the standard matter bounce:
$$
P_\zeta^{\rm matter} \gg P_T
$$

giving r << 1 when the growth factor is large. But the Quintin et al. point is that r is not independently adjustable — it's determined by the dynamics.

**Let me approach this differently.** The observed P_ζ = 2.1 × 10⁻⁹. For this to be correct:
$$
P_\zeta = A_s = 2.1 \times 10^{-9}
$$

The tensor power:
$$
P_T = r \times A_s = r \times 2.1 \times 10^{-9}
$$

The constraint r < 0.036 requires P_T < 7.6 × 10⁻¹¹.

**The question is what P_T the model predicts.** In the matter bounce, P_T depends on the Hubble rate at horizon crossing and the bounce dynamics.

### The Quintin Relation More Carefully

Quintin et al. (2015) derive that for a single-field contracting phase with sound speed c_s:

$$
r = 24 c_s^2 \left(\frac{z_\phi}{z_T}\right)^2
$$

where z_φ and z_T are the pump fields for scalar and tensor modes. The ratio z_φ/z_T depends on the bounce dynamics.

For a symmetric bounce (as in ECH/LQC):
$$
\frac{z_\phi}{z_T} \sim O(1)
$$

So r ~ 24c_s². For c_s = 1: r ~ 24 (hugely excluded). For c_s = 0.25: r ~ 1.5 (still excluded).

**This suggests the DBI sound speed reduction is NOT sufficient** — even c_s = 0.25 gives r ~ 1.5, not 0.03.

### Where Did the File 02 Estimate Go Wrong?

In file 02, I estimated "r ≈ 0.03 for c_s ≈ 0.25" based on r ∝ c_s. But the actual scaling is r ∝ c_s² (from the Quintin formula), AND the proportionality constant is O(10), not O(1).

**Corrected estimate:**
$$
r \sim 24 c_s^2 \quad \text{(for single-field matter bounce)}
$$

To get r < 0.036: need c_s < √(0.036/24) = √(0.0015) = 0.039

**c_s < 0.04 is required.** At c_s = 0.04:
- f_NL^equil ~ −1/c_s² ≈ −625 → **MASSIVELY excluded** by Planck (f_NL^equil = −26 ± 47)

**THE DBI EVASION FAILS.** The c_s needed for small r produces f_NL^equil that is many orders of magnitude too large.

---

## Revised Assessment: Curvaton-Only Model

Given that the DBI route fails, we return to the pure curvaton model.

### The Curvaton Evasion

With a curvaton dominating ζ:
- r = r_single × (1 − α²)²
- For the curvaton to sufficiently dominate: α² > 0.99 (need r_single ~ O(10) to be suppressed to r < 0.036)
- This means α > 0.995 — the curvaton almost completely dominates

With α > 0.995:
- f_NL^local ≈ (−35/8)(1 − 0.99)² + (−1.25)(0.99)² ≈ (−4.4)(10⁻⁴) + (−1.25)(0.98) ≈ −0.0004 − 1.23 ≈ −1.23
- **f_NL ≈ −1.23** — the curvaton f_NL dominates

**Can f_NL = −1.23 be distinguished from inflation (f_NL ≈ 0)?**

With SPHEREx: σ(f_NL) ~ 1–2. So f_NL = −1.23 would be ~0.6–1.2σ from zero. **Barely distinguishable.**

With MegaMapper: σ(f_NL) ~ 0.5. So f_NL = −1.23 would be ~2.5σ from zero. **Marginally detectable.**

**This is much weaker than f_NL = −4.4 (which would be 8.8σ with MegaMapper), but it's not zero.**

### Can We Get a More Negative f_NL from the Curvaton?

Standard curvaton f_NL = 5/(4r_dec) − 5r_dec/6 − 5/3

For r_dec → 1: f_NL → −1.25
For r_dec = 0.5: f_NL = 5/2 − 5/12 − 5/3 = 2.5 − 0.42 − 1.67 = +0.42
For r_dec = 0.2: f_NL = 25/4 − 1/6 − 5/3 = 6.25 − 0.17 − 1.67 = +4.42
For r_dec small: f_NL → +∞

**The curvaton f_NL is POSITIVE for r_dec < 0.9, and only negative for r_dec close to 1.**

The maximally negative curvaton f_NL is −1.25 (at r_dec = 1). This is a FIXED prediction in the curvaton-dominated regime.

### What About Self-Interaction of the Curvaton?

If the curvaton has a self-interaction potential V(σ) beyond quadratic:
$$
V(\sigma) = \frac{1}{2}m^2\sigma^2 + \frac{\lambda}{4}\sigma^4 + ...
$$

The non-Gaussian contribution from the self-interaction:
$$
f_{\rm NL}^{\rm self} \sim \frac{\lambda \sigma_*^2}{m^2}
$$

This can be either sign depending on the sign of λ. If λ < 0 (negative quartic):
$$
f_{\rm NL}^{\rm self} < 0
$$

This could push f_NL more negative. However:
- λ < 0 makes the potential unbounded from below (instability)
- The fine-tuning is: need λ to be just right to give f_NL ≈ −4.4

This is possible but adds a free parameter and requires a specific potential shape. Not very predictive.

---

## The Joint Constraint Landscape

### Scenario 1: Pure Curvaton (r_dec → 1)

| Observable | Prediction | Observation | Status |
|-----------|-----------|-------------|--------|
| n_s | 0.965 (tunable via m_σ) | 0.9649 ± 0.0042 | ✓ |
| r | < 0.001 (strongly suppressed) | < 0.036 | ✓ |
| f_NL^local | −1.25 | −0.9 ± 5.1 | ✓ (but not distinctive) |
| f_NL^equil | ~0 | −26 ± 47 | ✓ |
| α_s | ~ −(n_s − 1)² ≈ −0.001 | −0.005 ± 0.007 | ✓ |

**All constraints satisfied, but f_NL = −1.25 is not very distinctive.** It would require MegaMapper-class precision to even detect at 2.5σ.

### Scenario 2: DBI + Curvaton — RULED OUT

The DBI sound speed gives r ∝ c_s², and the c_s needed for r < 0.036 produces excluded equilateral non-Gaussianity.

### Scenario 3: LQC Dressed-Metric + Curvaton

Wilson-Ewing (2013) showed LQC corrections suppress r to ~10⁻⁴ WITHOUT needing c_s < 1 or a curvaton for r suppression. But n_s still needs a tilt mechanism.

If we use LQC for r suppression and a curvaton ONLY for tilt (not for r):
- The curvaton fraction α can be small (just enough for tilt)
- This means the matter-bounce f_NL contribution is preserved

With LQC r_LQC ≈ 10⁻⁴ and curvaton fraction α:
$$
r = r_{\rm LQC} \times (1 - \alpha^2) + ... \approx 10^{-4} \quad \checkmark
$$

$$
f_{\rm NL}^{\rm local} = (-35/8)(1 - \alpha^2)^2 + f_{\rm NL}^{\rm curv} \times \alpha^4
$$

For α = 0.3 (curvaton provides 9% of power, rest from matter field):
- r ≈ 10⁻⁴ × 0.91 ≈ 9 × 10⁻⁵ ✓
- f_NL ≈ (−4.4)(0.83) + (−1.25)(0.008) = −3.65 − 0.01 = −3.7
- n_s = 1 + 0.09 × (n_σ − 1) → need n_σ − 1 = −0.39 → m_σ/H_k = 0.76

For α = 0.5:
- r ≈ 10⁻⁴ ✓
- f_NL ≈ (−4.4)(0.56) + (−1.25)(0.063) = −2.46 − 0.08 = −2.5
- n_s = 1 + 0.25 × (n_σ − 1) → need n_σ − 1 = −0.14 → m_σ/H_k = 0.46

**THIS IS THE VIABLE MODEL:**

| Observable | Prediction (α = 0.3) | Prediction (α = 0.5) | Observation |
|-----------|---------------------|---------------------|-------------|
| n_s | 0.965 | 0.965 | 0.9649 ± 0.0042 ✓ |
| r | ~10⁻⁴ | ~10⁻⁴ | < 0.036 ✓ |
| f_NL^local | **−3.7** | −2.5 | −0.9 ± 5.1 ✓ |
| f_NL^equil | ~0 | ~0 | −26 ± 47 ✓ |
| α_s | ~−0.001 | ~−0.001 | −0.005 ± 0.007 ✓ |

---

## The Critical Dependence on LQC

**The viable model REQUIRES LQC-type perturbation corrections to suppress r.**

Without LQC: r ~ O(10) for single-field matter bounce → need curvaton to completely dominate → lose f_NL

With LQC: r ~ 10⁻⁴ independently → curvaton only needs to provide tilt → f_NL is preserved

**This is a genuine finding:** The matter bounce is ONLY viable (with distinctive f_NL) if the bounce produces perturbation-level corrections that suppress tensor modes. ECH does NOT do this (perturbation-transparent). LQC DOES (dressed-metric approach).

### Implications for Our ECH Program

The ECH bounce cannot support this model because:
1. ECH perturbations = classical GR (Branch Vb result)
2. No tensor suppression at the bounce
3. The model requires LQC-type quantum-geometry corrections

**However:** The ECH and LQC modified Friedmann equations are IDENTICAL at the background level: H² = (ρ/3M²)(1 − ρ/ρ_c). The difference is ONLY at the perturbation level. This means:

- The model works in LQC but not in ECH
- The distinction between ECH and LQC becomes OBSERVATIONALLY CRITICAL
- If LQC is the correct quantum gravity completion: the model predicts {n_s ≈ 0.965, r ~ 10⁻⁴, f_NL ≈ −3.7}
- If ECH is correct: the model fails (no r suppression)

**This is actually a GOOD result for the research program.** It identifies a TESTABLE difference between two quantum gravity frameworks.

---

## Future Experiment Predictions

For the LQC + partial curvaton model (α = 0.3):

| Experiment | Observable | Prediction | Sensitivity | σ detection |
|-----------|-----------|-----------|-------------|-------------|
| LiteBIRD | r | ~10⁻⁴ | σ(r) ~ 0.001 | Not detectable |
| CMB-S4 | n_s | 0.965 | σ(n_s) ~ 0.002 | Standard |
| CMB-S4 | f_NL^local | −3.7 | σ(f_NL) ~ 2.5 | 1.5σ |
| SPHEREx | f_NL^local | −3.7 | σ(f_NL) ~ 1.5 | 2.5σ |
| MegaMapper | f_NL^local | −3.7 | σ(f_NL) ~ 0.5 | **7.4σ** |
| CMB-S4 | f_NL^equil | ~0 | σ ~ 20 | Not detectable |
| BICEP Array | r | ~10⁻⁴ | σ(r) ~ 0.003 | Not detectable |

**The smoking gun: MegaMapper measures f_NL^local = −3.7 ± 0.5.** This would be a 7.4σ detection, immediately ruling out single-field inflation (which predicts f_NL ≈ 0) and consistent with the matter bounce.

---

## Is This Model Fine-Tuned?

**Parameter count:** 3 beyond the base model (c_s = 1 assumed, so: m_σ, α, r_dec → effectively n_s, α, r_dec)
**Inflation comparison:** Single-field inflation has 2 parameters (V₀, V'/V). Our model has 3. Comparable.

**Naturalness issues:**
- m_σ/H_k ≈ 0.76: this is O(1), natural
- α ≈ 0.3: the curvaton contributes 9% of the total power — this requires σ_i ≈ 0.3 M_Pl, natural
- r_dec ≈ 1: the curvaton fully decays — this requires Γ_σ to be small enough for σ to dominate, moderate tuning

**Overall: comparable to inflation in parameter count, and no severe fine-tuning.**
