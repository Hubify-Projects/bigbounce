# Non-Gaussianity Outlook

**Date:** 2026-03-16

---

## Purpose

Assess whether the spin-torsion bounce implies distinctive
non-Gaussian signatures in the scalar sector, without computing
full bispectra. This is a feasibility screen only.

---

## Sources of Non-Gaussianity in Bouncing Cosmologies

### Source 1: Nonlinear mode coupling at the bounce

During the bounce, the background curvature is Planck-scale
(R ~ M_Pl²). Nonlinear interactions between perturbation modes
are enhanced by the strong curvature.

The strength of mode coupling scales as:

```
f_NL ~ (Φ)² × (curvature/k²) ~ Φ × (k_b/k)²
```

For observable modes: k/k_b ~ 10⁻²⁸.
Enhancement: (k_b/k)² ~ 10⁵⁶.

BUT: this enhancement multiplies the PERTURBATION amplitude Φ,
which is ~ 10⁻⁵ (from the observed A_s). So:

```
f_NL ~ 10⁻⁵ × 10⁵⁶ ~ 10⁵¹
```

This would be ENORMOUS non-Gaussianity. Is this real?

**NO.** The (k_b/k)² enhancement only applies to modes that
interact at the bounce scale. Observable modes are super-Hubble
at the bounce and DO NOT interact (their wavelengths are far
larger than the causal horizon at the bounce).

The correct estimate for super-Hubble modes:

```
f_NL ~ O(1) × (Φ)    (from nonlinear ζ conservation)
     ~ O(1) × 10⁻⁵
     ~ 10⁻⁵ to O(1)
```

This is the GENERIC level of non-Gaussianity in any model
with nearly Gaussian primordial perturbations. The bounce
adds nothing.

### Source 2: Growing mode nonlinearity

The growing mode amplifies by 10⁸⁴ for CMB modes. At second
order, the product of two growing modes could produce an
enhanced non-Gaussian signal.

Second-order contribution:

```
Φ⁽²⁾ ~ (Φ_growing)² ~ (10⁸⁴ × Φ₀)²
```

This is enormous. But by the same time-reversal symmetry
that resolves the growing mode at linear order, the second-order
growing mode ALSO maps to a decaying mode after the bounce.

The symmetry argument extends to all orders of perturbation
theory: the time-reversal symmetry maps growing → decaying at
every order. No growing mode contamination at any order.

### Source 3: Spin-torsion four-fermion interaction

The (J⁵)² interaction at the bounce is nonlinear. Could it
generate non-Gaussian perturbations?

The effective interaction:

```
L_spin ~ -(3πG/2) (J⁵)² ~ -(3πG/2) n_s²
```

where n_s is the spin density. The perturbation of n_s:

```
δn_s ~ δρ × (∂n_s/∂ρ)
```

The quadratic nature of (J⁵)² generates a contribution to the
bispectrum:

```
⟨δΦ δΦ δΦ⟩ ∝ (3πG)² × ⟨(δJ⁵)² δΦ⟩ × ...
```

Order of magnitude:

```
f_NL^{torsion} ~ (ρ/ρ_crit) × (k/k_b)² ~ 1 × 10⁻⁵⁶
```

The (k/k_b)² factor comes from the fact that the torsion
interaction is localized at the bounce (spatial extent ~ 1/k_b).
For k ≪ k_b: the overlap integral is suppressed by (k/k_b)².

**Result: f_NL^{torsion} ~ 10⁻⁵⁶ at CMB scales. Negligible.**

### Source 4: Non-Gaussianity from the pre-bounce mechanism

The pre-bounce mechanism (whatever creates the scalar spectrum)
may itself produce non-Gaussianity. This is model-dependent
and outside the scope of the minimal bounce.

---

## Comparison with Known Bounce Non-Gaussianity

| Model | f_NL | Observable? |
|-------|------|------------|
| Inflation (single-field) | ~O(n_s - 1) ~ 0.04 | Barely (future) |
| Matter bounce | ~O(1) | Potentially |
| Ekpyrotic | ~O(1) to O(10) | Potentially |
| LQC bounce | ~O(1) | Potentially |
| **Spin-torsion bounce** | **~10⁻⁵⁶** (torsion) or **O(1)** (generic) | **NO** (torsion) / **Maybe** (generic) |

The spin-torsion-SPECIFIC non-Gaussianity is negligible (10⁻⁵⁶).
Any observable non-Gaussianity would come from the pre-bounce
mechanism, not the bounce itself.

---

## Is a Full Bispectrum Calculation Worth Doing?

**NO.** The arguments above show:

1. Super-Hubble modes don't interact at the bounce (causal
   disconnection at k ≪ k_b).
2. Time-reversal symmetry protects against growing mode
   contamination at all orders.
3. The torsion-specific contribution is suppressed by
   (k/k_b)² ~ 10⁻⁵⁶ at observable scales.

A full bispectrum calculation would confirm these estimates
at the cost of significant effort, with no scientific payoff.

---

## Summary

| Source | f_NL at CMB scales | Spin-torsion specific? |
|--------|-------------------|----------------------|
| Mode coupling at bounce | ~O(1) (generic) | NO |
| Growing mode nonlinearity | 0 (time-reversal) | YES (symmetry) |
| Torsion (J⁵)² | ~10⁻⁵⁶ | YES (but negligible) |
| Pre-bounce mechanism | Model-dependent | NO |

**No distinctive non-Gaussian signal from the bounce at
observable scales. Not worth further investigation.**
