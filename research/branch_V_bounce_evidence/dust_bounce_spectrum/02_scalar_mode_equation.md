# 02: Scalar Mode Equation

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Choice of Variable

The standard Mukhanov-Sasaki variable v_k = zζ_k, with z = a√(2ε)/c_s, diverges at the bounce because ε = −Ḣ/H² → ∞ as H → 0. This is a coordinate singularity, not a physical one.

**We use the Bardeen potential Φ_k in cosmic time.** The Bardeen potential is gauge-invariant, finite, and differentiable through the entire evolution including the bounce (as verified in Branch K).

---

## The Bardeen Potential Equation

For adiabatic perturbations of a perfect fluid with equation of state w and adiabatic sound speed c_s², the Bardeen potential satisfies:

$$
\ddot{\Phi}_k + (4 + 3c_s^2)\,H\,\dot{\Phi}_k + \left[\frac{c_s^2 k^2}{a^2} + 2\dot{H} + (3 + 3c_s^2)\,H^2\right]\Phi_k = 0
$$

### Verification at key limits

**Dust phase (w = 0, c_s² = 0, ρ ≪ ρ_crit):**

$$
\ddot{\Phi}_k + 4H\dot{\Phi}_k + \left[2\dot{H} + 3H^2\right]\Phi_k = 0
$$

Using H = 2/(3t) and Ḣ = −2/(3t²): the effective mass term vanishes:
2Ḣ + 3H² = −4/(3t²) + 4/(3t²) = 0

So:

$$
\ddot{\Phi}_k + \frac{8}{3t}\dot{\Phi}_k = 0
$$

Solutions: Φ = A + B|t|^{−5/3}. ✓

**Bounce point (H = 0, w = 1/3, ρ = ρ_crit):**

$$
\ddot{\Phi}_k + \left[\frac{k^2}{3a_b^2} + 2\dot{H}(0)\right]\Phi_k = 0
$$

This is a simple harmonic oscillator with frequency ω² = k²/(3a_b²) + 2Ḣ(0). All coefficients are finite. ✓

**Radiation expansion (w = 1/3, c_s² = 1/3, ρ ≪ ρ_crit):**

$$
\ddot{\Phi}_k + 5H\dot{\Phi}_k + \left[\frac{k^2}{3a^2} + 2\dot{H} + 4H^2\right]\Phi_k = 0
$$

Matches the Branch K equation. ✓

---

## The Sound Speed Problem

For the dust phase, c_s² = 0 means the pressure gradient term c_s²k²/a² vanishes. All k modes evolve identically — the Bardeen equation is the same for k = 0 and k = 10⁶. There is no dispersive behavior, no Hubble crossing, and no way to imprint a k-dependent spectrum from the Bardeen equation alone.

**This is the reason why perfect pressureless dust cannot generate a primordial spectrum.** The spectrum must come from something else: either a scalar field (which has c_s = 1 at the fundamental level but behaves as dust on average), or quantum vacuum fluctuations of the gravitational field itself.

### Resolution: scalar field representation

The standard matter bounce scenario models the dust as a massive scalar field φ with V(φ) = ½m²φ². For m ≫ H, the field oscillates rapidly and the time-averaged equation of state is ⟨w⟩ = 0 (dust-like). But the fundamental sound speed for perturbations of a scalar field is **c_s = 1** (propagation at the speed of light).

For the Mukhanov-Sasaki equation of the scalar field perturbation:

$$
v_k'' + \left(k^2 - \frac{z''}{z}\right)v_k = 0 \quad \text{(conformal time)}
$$

where z = aφ̇/H (in cosmic time Hubble).

For the dust-like phase with a ∝ |η|² (matter domination in conformal time):

$$
\frac{z''}{z} \approx \frac{2}{\eta^2}
$$

(time-averaged, valid for modes with k ≪ m).

The Mukhanov-Sasaki equation becomes:

$$
v_k'' + \left(k^2 - \frac{2}{\eta^2}\right)v_k = 0
$$

This is identical to the tensor equation for a matter-dominated universe, and has exact Hankel function solutions.

---

## How Torsion Affects the Background Quantities

The ECH torsion modification enters **only through the modified Friedmann equation:**

$$
H^2 = \frac{\rho}{3M_{\rm Pl}^2}\left(1 - \frac{\rho}{\rho_{\rm crit}}\right)
$$

This affects the perturbation equation through:
1. **H(t)**: modified near the bounce (H → 0 at ρ = ρ_crit instead of H → ∞ at ρ → ∞)
2. **Ḣ(t)**: sign reversal (Ḣ > 0 at bounce vs Ḣ < 0 in standard GR)
3. **a(t)**: minimum at the bounce instead of a = 0 singularity

Torsion does **NOT** modify:
- The perturbation equation itself (the form of the Bardeen equation is unchanged)
- The adiabatic sound speed c_s (determined by matter content, not gravity)
- The initial conditions (set in the low-density regime where torsion is negligible)

**The torsion effect on perturbations is entirely through the background:** a(t), H(t), Ḣ(t) are modified near ρ ~ ρ_crit, and these modified coefficients enter the Bardeen equation.

---

## Assumptions

1. **Adiabatic perturbations only.** We do not include isocurvature modes. In a single-fluid model, this is automatic.

2. **Linear perturbation theory.** Valid for Φ ≪ 1, which holds for all modes of cosmological interest.

3. **Scalar field representation for the dust phase.** We use the effective z''/z = 2/η² for the Mukhanov-Sasaki equation during dust contraction. This assumes the scalar field mass m is much larger than the Hubble rate during the relevant period.

4. **Smooth w(t) transition.** The dust-to-radiation transition is modeled as a continuous change in w, not a discontinuous matching.

5. **No anisotropy.** The background is FRW throughout. We do not address the BKL instability of the dust contraction (this is a known problem for the matter bounce scenario; see Consistency Checks).

---

## Numerical Implementation Strategy

Given the c_s subtlety, we implement a two-stage approach:

### Stage 1: Mukhanov-Sasaki equation (dust phase only)

Solve v_k'' + (k² − 2/η²)v_k = 0 analytically in the dust contraction phase. The Bunch-Davies solution gives:

$$
v_k = \frac{1}{\sqrt{2k}}\,e^{-ik\eta}\!\left(1 - \frac{i}{k\eta}\right)
$$

On super-Hubble scales (|kη| ≪ 1), the growing mode dominates:

$$
v_k \approx \frac{-i}{\sqrt{2k}\,k\eta}
$$

Extract the curvature perturbation: ζ_k = v_k / z.

### Stage 2: Bardeen potential (transition + bounce + expansion)

At the start of the transition region, convert from (v_k, v_k') to (Φ_k, Φ̇_k) using the gauge-invariant relations, and switch to the Bardeen equation in cosmic time.

The Bardeen equation with c_s² transitioning from c_s²(dust) to 1/3 is solved numerically through the transition and bounce.

After the bounce, in the radiation expansion, extract the constant-mode amplitude of Φ_k and convert to ζ_k = (3/2)Φ_k (constant mode in radiation).

### Stage 3: Power spectrum extraction

$$
P_\zeta(k) = \frac{k^3}{2\pi^2}\,|\zeta_k|^2
$$

evaluated on super-Hubble scales after the bounce.
