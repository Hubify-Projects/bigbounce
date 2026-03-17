# 01: Background Solution — Dust Contraction → ECH Bounce → Radiation Expansion

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Overview

We construct a background cosmology with three phases:

1. **Dust contraction** (t ≪ −t_tr): pressureless matter, w = 0
2. **Transition** (t ∼ −t_tr): smooth EOS change w: 0 → 1/3
3. **ECH bounce + radiation expansion** (t ∼ 0 onward): torsion-modified Friedmann, w = 1/3

The bounce occurs at ρ = ρ_crit when the ECH torsion correction becomes dominant.

---

## Governing Equations

### Modified Friedmann equations (ECH)

The Einstein-Cartan-Holst torsion correction modifies the Friedmann equation to:

$$
H^2 = \frac{\rho}{3M_{\rm Pl}^2}\left(1 - \frac{\rho}{\rho_{\rm crit}}\right)
$$

Taking the time derivative and using energy conservation ρ̇ = −3H(1+w)ρ:

$$
\dot{H} = -\frac{(1+w)\rho}{2M_{\rm Pl}^2}\left(1 - \frac{2\rho}{\rho_{\rm crit}}\right)
$$

Energy conservation:

$$
\dot{\rho} = -3H(1+w)\rho
$$

### Parameters (fixed by ECH framework)

| Parameter | Value | Source |
|-----------|-------|--------|
| ρ_crit | 0.21 M_Pl⁴ | ECH torsion coupling, κ_s from Barbero-Immirzi γ = 0.274 |
| M_Pl | 2.435 × 10¹⁸ GeV | Reduced Planck mass |
| α² | 8πGρ_crit/3 = ρ_crit/(3M_Pl²) ≈ 1.76 M_Pl² | Bounce timescale parameter |

### Equation of state transition

We parametrize the EOS as a smooth function:

$$
w(t) = \frac{1}{3} \cdot \frac{1}{2}\left[1 + \tanh\!\left(\frac{t + t_{\rm tr}}{\Delta t_{\rm tr}}\right)\right]
$$

- For t ≪ −t_tr: w → 0 (dust)
- For t ≫ −t_tr: w → 1/3 (radiation)
- t_tr: transition time (free parameter, sets when dust → radiation occurs)
- Δt_tr: transition width (free parameter)

We require the transition to complete well before the bounce (ρ_tr ≪ ρ_crit), so that the bounce occurs cleanly in the radiation era.

---

## Phase-by-Phase Analytic Solutions

### Phase 1: Dust contraction (ρ ≪ ρ_crit, w = 0)

When ρ ≪ ρ_crit, the modified Friedmann equation reduces to standard GR:

$$
H^2 \approx \frac{\rho}{3M_{\rm Pl}^2}, \quad \dot{H} \approx -\frac{\rho}{2M_{\rm Pl}^2}
$$

With w = 0 and ρ ∝ a⁻³:

$$
a(t) = a_{\rm ref}\left(\frac{t}{t_{\rm ref}}\right)^{2/3}, \quad H = \frac{2}{3t}, \quad \rho = \frac{4M_{\rm Pl}^2}{3t^2}
$$

(Here t < 0 during contraction, and a → 0 as t → 0⁻.)

### Phase 2: Transition region

No analytic solution. Solved numerically with the smooth w(t) interpolation.

### Phase 3: Near the bounce (radiation, ρ → ρ_crit)

With w = 1/3 and ρ near ρ_crit, the exact ECH bounce solution (from Branch H) is:

$$
a(t) = a_b\left(1 + 4\alpha^2 t^2\right)^{1/4}
$$

$$
H(t) = \frac{2\alpha^2 t}{1 + 4\alpha^2 t^2}
$$

$$
\rho(t) = \frac{\rho_{\rm crit}}{1 + 4\alpha^2 t^2}
$$

Properties at the bounce (t = 0):
- a(0) = a_b (minimum scale factor)
- H(0) = 0 (turning point)
- Ḣ(0) = 2α² ≈ 3.52 M_Pl² > 0 (expansion begins)
- ρ(0) = ρ_crit = 0.21 M_Pl⁴

### Phase 4: Radiation expansion (ρ ≪ ρ_crit, w = 1/3)

Standard radiation-dominated expansion:

$$
a(t) \propto t^{1/2}, \quad H = \frac{1}{2t}, \quad \rho = \frac{3M_{\rm Pl}^2}{4t^2}
$$

---

## Numerical Implementation

### ODE system

We solve the system:

$$
\frac{da}{dt} = aH
$$

$$
\frac{dH}{dt} = -\frac{(1+w)\rho}{2M_{\rm Pl}^2}\left(1 - \frac{2\rho}{\rho_{\rm crit}}\right)
$$

$$
\frac{d\rho}{dt} = -3H(1+w)\rho
$$

with w = w(t) given by the smooth transition function.

This system is regular at the bounce: H passes through zero smoothly, Ḣ > 0, ρ = ρ_crit.

### Initial conditions

Start at t = t_start ≪ −t_tr (deep in the dust contraction):

$$
a(t_{\rm start}) = a_{\rm ref}\left|\frac{t_{\rm start}}{t_{\rm ref}}\right|^{2/3}
$$

$$
H(t_{\rm start}) = \frac{2}{3t_{\rm start}} < 0
$$

$$
\rho(t_{\rm start}) = \frac{4M_{\rm Pl}^2}{3t_{\rm start}^2}
$$

### Parameter choices for Phase 1a

We use Planck units throughout (M_Pl = 1):

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| ρ_crit | 0.21 | ECH framework |
| t_tr | 100 t_Pl | Transition well before bounce |
| Δt_tr | 10 t_Pl | Smooth but not too extended |
| t_start | −10⁴ t_Pl | Deep in dust phase |
| a_b | 1 | Normalization convention |

The transition density at t = −t_tr:
ρ_tr = 4/(3 × t_tr²) ≈ 4/(3 × 10⁴) ≈ 1.3 × 10⁻⁴ M_Pl⁴

Since ρ_tr/ρ_crit ≈ 6 × 10⁻⁴ ≪ 1, the transition is well-separated from the bounce. ✓

---

## Continuity Verification

The background must satisfy:
1. **a(t) continuous**: ✓ (solved as continuous ODE)
2. **H(t) continuous**: ✓ (H is a dynamical variable)
3. **ρ(t) continuous**: ✓ (ρ is a dynamical variable)
4. **Correct bounce**: H = 0 at ρ = ρ_crit, Ḣ > 0 ✓
5. **Correct asymptotics**: a ∝ |t|^{2/3} for t ≪ −t_tr, a ∝ t^{1/2} for t ≫ t_bounce ✓

---

## Key Physical Scales

| Scale | Expression | Value (Planck units) |
|-------|-----------|---------------------|
| Bounce scale | k_b = a_b√(2α) | ≈ 1.88 |
| Bounce frequency today | f_b ≈ k_b/(2πa_0) | ≈ 8 GHz |
| CMB mode | k_CMB ≈ 0.05 Mpc⁻¹ | ≈ 10⁻²⁸ k_b |
| Scale separation | k_CMB/k_b | ≈ 10⁻²⁸ |

**Critical observation:** All cosmologically observable modes have k/k_b ≈ 10⁻²⁸. They are deeply super-Hubble throughout the transition and bounce. The bounce is a sub-resolution event for these modes.
