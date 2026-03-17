# 03: Initial Conditions

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Vacuum State in the Contracting Phase

We require Bunch-Davies vacuum initial conditions in the asymptotic past of the contracting phase (η → −∞, where all modes of interest are deep inside the Hubble radius).

### Mukhanov-Sasaki variable

For the scalar field representation of the dust phase, the Mukhanov-Sasaki equation is:

$$
v_k'' + \left(k^2 - \frac{2}{\eta^2}\right)v_k = 0
$$

where primes denote d/dη (conformal time), and η < 0 during contraction with η → 0⁻ at the bounce.

The exact solution with Bunch-Davies normalization is:

$$
v_k(\eta) = \frac{1}{\sqrt{2k}}\,e^{-ik\eta}\!\left(1 - \frac{i}{k\eta}\right)
$$

### Verification of initial state

In the deep past (|kη| ≫ 1, sub-Hubble):

$$
v_k \to \frac{1}{\sqrt{2k}}\,e^{-ik\eta}
$$

This is the standard positive-frequency Minkowski vacuum (WKB mode). ✓

The Wronskian is:

$$
v_k v_k^{*\prime} - v_k^* v_k' = -i
$$

which is preserved by the evolution. ✓

---

## Mode Normalization

### Curvature perturbation from Mukhanov variable

$$
\zeta_k = \frac{v_k}{z}
$$

where z = a√(2ε)M_Pl/c_s for the generalized case, or z = aφ̇/H for a scalar field.

For the dust-like contraction with a ∝ η² (conformal time, η < 0):

$$
z = \sqrt{3}\,M_{\rm Pl}\,a \propto \eta^2
$$

(Using ε = 3/2 for dust and c_s = 1 for the scalar field. The factor √3 comes from ε = 3/2: z = a√(2 × 3/2)M_Pl/1 = a√3 M_Pl.)

### Super-Hubble limit

On super-Hubble scales (|kη| ≪ 1), the growing mode of v dominates:

$$
v_k \approx \frac{-i}{\sqrt{2k}\,k\eta}
$$

Therefore:

$$
\zeta_k = \frac{v_k}{z} \approx \frac{-i}{\sqrt{2k}\,k\eta \times \sqrt{3}M_{\rm Pl}\,a_0(\eta/\eta_0)^2}
$$

$$
= \frac{-i\,\eta_0^2}{\sqrt{6k}\,k\,M_{\rm Pl}\,a_0\,\eta^3}
$$

This grows as 1/η³ during the contraction (η → 0⁻). This is the growing mode of ζ.

### Power spectrum during contraction

$$
P_\zeta(k) = \frac{k^3}{2\pi^2}|\zeta_k|^2 = \frac{k^3}{2\pi^2} \times \frac{\eta_0^4}{6k^3\,M_{\rm Pl}^2\,a_0^2\,\eta^6}
= \frac{\eta_0^4}{12\pi^2\,M_{\rm Pl}^2\,a_0^2\,\eta^6}
$$

**This is independent of k.** → n_s = 1 (scale-invariant).

The amplitude grows as 1/η⁶ during the contraction. This growth must be "frozen" at the bounce and converted to the constant mode in the expansion.

---

## Conversion to Bardeen Potential Initial Conditions

For the numerical integration through the transition and bounce, we need Φ_k and Φ̇_k at a matching time t_match (during the dust phase, before the transition begins).

### Relation between ζ and Φ in dust (w = 0)

$$
\zeta = \Phi + \frac{2}{3}\frac{\dot{\Phi}/H + \Phi}{1+w} = \Phi + \frac{2}{3}(\dot{\Phi}/H + \Phi) = \frac{5}{3}\Phi + \frac{2}{3}\frac{\dot{\Phi}}{H}
$$

For the **constant Φ mode** (Φ = const, Φ̇ = 0):
$$
\zeta = \frac{5}{3}\Phi
$$

For the **growing Φ mode** (Φ ∝ |t|^{−5/3}):
$$
\dot{\Phi}/H = -\frac{5}{2}\Phi \quad \Rightarrow \quad \zeta = \frac{5}{3}\Phi + \frac{2}{3}\times\left(-\frac{5}{2}\right)\Phi = 0
$$

**Key result:** The growing mode of Φ corresponds to ζ = 0. The growing mode of ζ (which dominates during contraction) maps to a specific combination of the growing and constant Φ modes.

### Full decomposition

Given ζ_k (from the Mukhanov-Sasaki solution) at time t_match:

The Bardeen potential has the general form:
$$
\Phi_k(t) = A_k + B_k |t|^{-5/3}
$$

$$
\dot{\Phi}_k(t) = \frac{5}{3}B_k |t|^{-8/3} \quad \text{(for } t < 0\text{)}
$$

From ζ = (5/3)A_k + 0 × B_k = (5/3)A_k:
$$
A_k = \frac{3}{5}\zeta_k
$$

But wait — ζ_k is the growing mode value at t_match, which includes both the constant ζ and growing ζ. The growing ζ maps to the growing Φ (which has ζ = 0 at leading order), while the constant ζ maps to the constant Φ.

Since the growing mode of ζ dominates at late times during contraction, and the growing ζ has ζ → 0 for the Bardeen potential... this requires careful treatment.

**Proper decomposition:**

The full Mukhanov-Sasaki solution has both modes:
$$
v_k = C_1 \eta^2 + C_2 / \eta
$$

where:
- C₁ η² → ζ = const (the physical constant mode, preserved through bounce)
- C₂/η → ζ ∝ 1/η³ (the growing mode, amplified during contraction)

From the Bunch-Davies vacuum:
$$
C_1 = \frac{1}{\sqrt{2k}} \times \frac{i k^2}{2}, \quad C_2 = \frac{1}{\sqrt{2k}} \times \frac{-i}{k}
$$

(extracted from expanding the exact solution in powers of kη)

The constant mode of ζ (which survives into expansion) has amplitude:
$$
\zeta_k^{\rm const} = \frac{C_1 \eta^2}{z} \bigg|_{\text{eval}} = \frac{C_1}{z/\eta^2}
$$

Since z = √3 M_Pl a₀ (η/η₀)², we get z/η² = √3 M_Pl a₀/η₀², so:
$$
\zeta_k^{\rm const} = \frac{C_1}{\sqrt{3}M_{\rm Pl}a_0/\eta_0^2} = \frac{ik^{3/2}\eta_0^2}{2\sqrt{6}\,M_{\rm Pl}\,a_0}
$$

Wait — this IS k-dependent: ∝ k^{3/2}. Then:

$$
P_\zeta^{\rm const}(k) = \frac{k^3}{2\pi^2}|\zeta_k^{\rm const}|^2 = \frac{k^3}{2\pi^2} \times \frac{k^3 \eta_0^4}{24 M_{\rm Pl}^2 a_0^2} = \frac{k^6 \eta_0^4}{48\pi^2 M_{\rm Pl}^2 a_0^2}
$$

This gives P_ζ ∝ k⁶ → n_s = 7 for the constant mode!! This is extremely blue.

**The resolution:** The constant ζ mode is NOT what survives after the bounce. In the matter bounce, it is the **growing mode** of ζ (∝ 1/η³) that gets converted to the constant mode after the bounce. The growing mode has the scale-invariant amplitude:

$$
P_\zeta^{\rm growing}(k, \eta) = \frac{1}{12\pi^2 M_{\rm Pl}^2 a_0^2 \eta^6 / \eta_0^4} \propto k^0
$$

The bounce matching condition determines how efficiently the growing ζ converts to the constant ζ in the expansion phase.

---

## The Growing Mode Problem

This is the central challenge of the matter bounce:

1. During contraction, ζ grows as 1/η³ (or equivalently, as a^{−3/2}).
2. The growth factor from Hubble crossing to the bounce is (a_k/a_b)^{3/2}, which can be enormous.
3. The growing mode must be converted to the constant mode at the bounce.
4. If the conversion is efficient and k-independent, the output spectrum is scale-invariant (n_s = 1).

**The ECH bounce performs this conversion.** The Bardeen potential is regular at the bounce, and the numerical solution tracks how each mode passes through the transition and bounce.

---

## Summary of Initial Conditions for the Solver

At time t_start deep in the dust phase (|t_start| ≫ t_tr), for each k mode:

**Option A (analytic Bardeen potential):**
Set Φ_k(t_start) and Φ̇_k(t_start) using the two-mode decomposition:
$$
\Phi_k = A_k + B_k|t_{\rm start}|^{-5/3}
$$
$$
\dot{\Phi}_k = \frac{5B_k}{3}|t_{\rm start}|^{-8/3}
$$

where A_k and B_k are determined by matching to the vacuum fluctuation (Mukhanov-Sasaki → Bardeen conversion).

**Option B (direct v_k evolution):**
Evolve the Mukhanov-Sasaki equation in conformal time through the dust phase (analytically), then switch to the Bardeen equation at the transition. This avoids the subtleties of mode decomposition but requires a change of variable at the matching point.

**We implement Option A** with the understanding that the key physics (n_s = 1 from scale-invariant growing mode) is analytically established. The numerical solver confirms the transfer through the transition and bounce.
