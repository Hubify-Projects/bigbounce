# Phase 3: Initial Conditions — Vacuum State Selection

**Date:** 2026-03-13
**Status:** ANALYSIS — three candidate vacuum states documented with consequences

---

## 1. The Problem

The Mukhanov-Sasaki equation:
```
v_k'' + [c_s² k² − U_s(τ)] v_k = 0
```

is a second-order ODE. It requires two initial conditions (v_k and v_k' at some initial time τ_i).

In standard inflation on a classical expanding background, the initial conditions are set in the far past (τ → −∞) where all modes are deep inside the Hubble radius (k ≫ aH) and the WKB approximation is valid:

```
v_k(τ) → (1/√(2ω_k)) exp(−i ∫ ω_k dτ),    ω_k = √(c_s² k² − U_s)
```

This is the **Bunch-Davies vacuum** — the unique state that looks like Minkowski vacuum at short distances.

**In a bouncing cosmology, this prescription fails** because:

1. There is no τ → −∞ limit in the contracting phase where all modes are sub-Hubble (some modes are always super-Hubble during the contraction)
2. The bounce itself is a non-adiabatic event that can excite modes
3. The pre-bounce contraction may have its own quantum state that is not the Bunch-Davies vacuum of the post-bounce expansion

This is a **genuine theoretical ambiguity**, not a technical difficulty. Different choices lead to physically distinct predictions.

---

## 2. Candidate Initial Conditions

### 2a. Bunch-Davies Vacuum (in the contracting phase)

**Prescription:** Set v_k to the positive-frequency WKB mode in the deep contracting phase, at a time when the mode is well inside the Hubble radius:

```
v_k(τ_i) = 1/√(2ω_k(τ_i))
v_k'(τ_i) = −i ω_k(τ_i) × v_k(τ_i)
```

with τ_i chosen so that k ≫ |z''/z|^{1/2} at τ_i (mode is sub-Hubble).

**Assumption:** The pre-bounce contracting phase has a well-defined adiabatic regime.

**Validity:** Only works for modes that are sub-Hubble at some point during the contraction. For modes that are always super-Hubble (very long wavelengths), this prescription is not applicable.

**Consequences:**
- Produces particle creation through the bounce (Bogoliubov mixing)
- Modes that pass through the bounce pick up a phase and amplitude modification
- The resulting P_R(k) has oscillatory features at k ~ k_bounce (the Hubble scale at the bounce)
- IR modes (k ≪ k_bounce) are strongly modified; UV modes (k ≫ k_bounce) are unaffected

**Literature:** Used by de Blas & Olmedo (2016); some LQC calculations adopt this.

**Risk:** If the contracting phase itself has been through prior dynamical evolution (e.g., if the parent BH interior has non-trivial quantum state), the Bunch-Davies assumption in the contraction is unjustified.

### 2b. Fourth-Order Adiabatic Vacuum

**Prescription:** Set initial conditions using the WKB expansion to fourth adiabatic order:

```
v_k(τ_i) = (1/√(2W_k(τ_i))) exp(−i ∫^{τ_i} W_k dτ')
```

where W_k is the fourth-order WKB frequency:

```
W_k² = ω_k² − (1/2)(W_k''/W_k) + (3/4)(W_k'/W_k)²
```

solved iteratively to O(ω_k⁻⁴).

**Assumption:** The state minimizes the energy density to fourth adiabatic order at the initial time.

**Validity:** More robust than zeroth-order Bunch-Davies when ω_k is changing rapidly. Still requires an adiabatic regime to exist at τ_i.

**Consequences:**
- Reduces spurious particle creation from the initial time surface
- Gives a "cleaner" bounce signal — less contamination from initial-state artifacts
- Standard approach in Agullo-Ashtekar-Nelson LQC perturbation calculations
- P_R(k) features are qualitatively similar to Bunch-Davies but with different oscillation phase and amplitude at intermediate k

**Literature:** Agullo, Ashtekar, Nelson (2012-2013); Zhu, Cleaver, Ashtekar (2017)

**Risk:** The adiabatic expansion may break down near the bounce where ω_k changes rapidly. Fourth-order may not be sufficient.

### 2c. Bounce-Modified Vacuum State

**Prescription:** Impose the quantum state AT the bounce (τ = τ_bounce) rather than in the contracting phase. Require the state to be:
- Regular at the bounce point
- Symmetric under time reversal τ → −τ (if the bounce is symmetric)
- Minimize some energy functional defined on the bounce surface

Two sub-options:

**2c-i. No-boundary-like state:** Impose regularity at the bounce (no incoming wave from τ → −∞). This is analogous to the Hartle-Hawking no-boundary proposal applied to the bounce surface.

```
v_k(τ_bounce) = finite
v_k'(τ_bounce) = 0     [time-reversal symmetric]
```

**2c-ii. Thermal state:** The pre-bounce contraction of the parent BH interior produces a thermal bath at temperature T ~ T_Pl at the bounce. The initial state is a thermal density matrix rather than a pure state:

```
⟨|v_k|²⟩ = (1/2ω_k) × coth(ω_k/2T)
```

This interpolates between vacuum (T → 0) and classical (T → ∞).

**Consequences of bounce-modified states:**
- No-boundary: strongly suppresses long-wavelength modes → enhanced IR suppression relative to adiabatic vacuum
- Thermal: adds a thermal noise floor → could wash out or enhance small-scale features depending on T/ω_k
- Both: remove the need to specify an initial time surface in the contraction

**Literature:** Wilson-Ewing (2013); Bolliet, Barrau, Grain, Schander (2016)

**Risk:** The no-boundary condition is mathematically clean but physically unmotivated beyond analogy. The thermal state requires knowing T at the bounce, which depends on the parent BH properties.

---

## 3. How the Vacuum Choice Affects P_R(k)

### 3a. Qualitative Comparison

```
ln P_R(k)
  ^
  |
  |    ──────────────────────────── standard slow-roll (scale-invariant)
  |
  |    ╱╲╱╲──────────────────── BD vacuum (oscillations at k ~ k_bounce)
  |   ╱    ╲
  |  ╱      ─────────────────── 4th-order adiabatic (smoother oscillations)
  | ╱
  |╱────────────────────────── no-boundary (strong IR suppression)
  |
  └──────────────────────────── k
    k ≪ k_bounce  k ~ k_bounce  k ≫ k_bounce
```

### 3b. Quantitative Differences

| Feature | Bunch-Davies | 4th Adiabatic | No-Boundary | Thermal |
|---------|-------------|---------------|-------------|---------|
| IR power (k ≪ k_bounce) | Suppressed | Less suppressed | Strongly suppressed | Enhanced |
| Oscillation amplitude | Large | Moderate | Small | Washed out |
| Oscillation phase | ψ_BD | ψ_BD + Δψ | Different | Noisy |
| UV power (k ≫ k_bounce) | Unchanged | Unchanged | Unchanged | Slightly enhanced |
| PBH implications | Depends on oscillation amplitude | Depends on oscillation amplitude | Weak features → fewer PBHs | Thermal noise → more PBHs? |

### 3c. The Scale That Matters

For this framework with N_tot = 92:
```
k_bounce ~ a_bounce × H_max ~ e^{−92} × H_inf × (H_bounce/H_inf)
         ~ 5.86 × 10¹⁴ Mpc⁻¹
```

This corresponds to:
```
M_bounce ~ 7.68 × 10¹⁶ g ~ 3.86 × 10⁻¹⁷ M_☉
```

The vacuum choice mainly affects modes with k ≲ k_bounce. Modes at CMB scales (k ~ 10⁻⁴ to 10⁻¹ Mpc⁻¹) are separated by ~10¹⁸ orders of magnitude in k from k_bounce — they are completely unaffected by the vacuum choice.

**The vacuum choice matters ONLY for small-scale observables** (PBHs, μ-distortions, small-scale gravitational waves).

---

## 4. Recommended Strategy

### 4a. For Paper 2

1. **Run separate chains for each vacuum choice.** Do not treat the vacuum as a continuous parameter. The three choices (BD, 4th adiabatic, no-boundary) are discrete model classes.

2. **Report results for all three.** Identify which observables are robust (same prediction for all vacuum choices) and which are vacuum-dependent.

3. **Identify discriminating observables.** If different vacuum choices predict different PBH abundances or μ-distortion amplitudes, state this explicitly — it tells experimentalists what to measure.

### 4b. Prior on Vacuum Choice

There is no objective prior over vacuum states. The theoretically most conservative approach:
- 4th-order adiabatic vacuum as the "reference" (most studied in LQC)
- Bunch-Davies as a limiting case
- No-boundary as a physically motivated alternative
- Thermal state requires additional input (T at bounce)

### 4c. What Would Resolve the Ambiguity

The vacuum state ambiguity can in principle be resolved by:
1. A full quantum gravity calculation of the perturbation state through the BH collapse → bounce transition
2. Observational discrimination: if PBH abundance or μ-distortion signals are detected, the amplitude selects the vacuum

Neither is available now. This is a genuine limitation.

---

## 5. Implementation Notes

For numerical evolution (Phase 4), the initial conditions translate to:

**Bunch-Davies / adiabatic:**
```
Set τ_i in deep contraction where k² ≫ |U_s(τ_i)|
v_k(τ_i) = 1/√(2k c_s(τ_i))
v_k'(τ_i) = −i k c_s(τ_i) v_k(τ_i)
```

**No-boundary:**
```
Set τ_i = τ_bounce
v_k(τ_bounce) = A_k (to be determined by normalization)
v_k'(τ_bounce) = 0
```

**Thermal:**
```
Same as adiabatic but with statistical ensemble:
⟨|v_k|²⟩ = (1/2kc_s) coth(kc_s/2T)
Requires Monte Carlo sampling over initial phases
```
