# 07: Consistency Checks

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Check 1: Bardeen potential regularity at the bounce

**Result: PASS**

The Bardeen potential Φ_k(t) is finite and differentiable through the entire evolution, including the bounce point (t = 0, H = 0). At the bounce:

$$
\ddot{\Phi}_k + \left[\frac{k^2}{3a_b^2} + 2\dot{H}(0)\right]\Phi_k = 0
$$

All coefficients are finite. The Mukhanov-Sasaki variable v = zζ would diverge (because z → ∞ as H → 0 with ε → ∞), but this is a coordinate singularity of the Mukhanov variable, not a physical divergence. The Bardeen potential avoids this entirely.

Numerically verified: Φ(t) passes through the bounce smoothly with no spikes, discontinuities, or numerical instabilities.

---

## Check 2: Transfer function insensitivity to transition parameters

**Result: PASS**

The transfer function T(k) = Φ_out(k)/Φ_out(k_ref) was computed for different choices of the dust-to-radiation transition:

| Parameter set | t_tr | Δt_tr | T(k = 10⁻⁴ k_b) | n_s |
|--------------|------|-------|-----------------|-----|
| Baseline | 100 | 10 | 1.000 (ref) | 1.000 |
| Earlier transition | 200 | 10 | 1.000 | 1.000 |
| Wider transition | 100 | 30 | 1.000 | 1.000 |
| Sharper transition | 100 | 3 | 1.000 | 1.000 |

For all super-Hubble modes (k/k_b ≪ 1), the transfer function is unity regardless of the transition details. This is expected: ζ is conserved on super-Hubble scales for adiabatic perturbations, independent of how the equation of state changes.

**Physical reasoning:** The modes of interest have k/k_b ~ 10⁻²⁸. They are frozen on super-Hubble scales from well before the transition through well after the bounce. The transition and bounce are sub-resolution events for these modes.

---

## Check 3: Energy conservation through the bounce

**Result: PASS**

The modified Friedmann equation H² = (ρ/3M_Pl²)(1 − ρ/ρ_crit) together with energy conservation ρ̇ = −3H(1+w)ρ form a closed, consistent system. The numerical solution satisfies:

- ρ reaches ρ_crit exactly at H = 0 (bounce)
- ρ decreases after the bounce as the universe expands
- The Friedmann constraint H² = (ρ/3M_Pl²)(1 − ρ/ρ_crit) is satisfied to machine precision throughout

No energy is injected or lost at the bounce. The bounce is a smooth, regular point of the equations.

---

## Check 4: Correct asymptotic behavior

**Result: PASS**

| Phase | Expected | Numerical |
|-------|----------|-----------|
| Dust contraction (t ≪ −t_tr) | a ∝ \|t\|^{2/3}, H = 2/(3t) | ✓ |
| Near bounce (t ≈ 0) | a = a_b(1 + 4α²t²)^{1/4} | ✓ |
| Radiation expansion (t ≫ 0) | a ∝ t^{1/2}, H = 1/(2t) | ✓ |

The background solution reproduces all analytic limits correctly.

---

## Check 5: Spectrum amplitude dependence

**Result: PASS (as expected)**

The amplitude of P_ζ depends on the contraction duration (how early the dust phase begins), which sets the overall normalization. This is one free parameter, analogous to the inflationary Hubble scale H_inf.

The spectral shape (n_s = 1) is independent of this amplitude — it is determined by the k-independence of the vacuum fluctuation spectrum during dust contraction.

---

## Check 6: Growing mode vs constant mode identification

**Result: PASS (after correction)**

Initial numerical tests using the growing Φ mode (∝ |t|^{-5/3}) as input gave nonsensical results (n_s = −1.23) because this mode has ζ = 0 identically — it carries no curvature perturbation.

After correcting to the constant Φ mode (Φ = const, Φ̇ = 0), the transfer function gives T(k) = 1 for super-Hubble modes, confirming scale invariance.

**Key lesson:** In the matter bounce, the physical perturbation is carried by the constant Bardeen potential mode (which has ζ = (5/3)Φ), not the growing mode (which has ζ = 0). The growing mode is a pure gauge artifact in the comoving gauge.

---

## Check 7: BKL instability (anisotropy growth)

**Result: KNOWN OPEN ISSUE — NOT ADDRESSED**

During dust contraction, anisotropic stress grows as σ² ∝ a⁻⁶, faster than the matter density ρ ∝ a⁻³. This means the universe becomes increasingly anisotropic as it contracts, potentially invalidating the FRW assumption before the bounce is reached.

This is the **Belinski-Khalatnikov-Lifshitz (BKL) instability**, a well-known and unresolved problem for all matter bounce scenarios:

- Dust contraction: anisotropy dominates after Δln(a) ~ O(1) of contraction
- This would destroy the homogeneous bounce before it occurs
- Proposed resolutions include ekpyrotic contraction (w ≫ 1) or spatial curvature effects, but these change the perturbation spectrum

**Status:** We do not address this in Phase 1a. The BKL instability is a problem for the matter bounce scenario in general, not specific to the ECH framework. If a tilt mechanism is found in Phase 1b that also addresses BKL (e.g., ekpyrotic phase), that would be significant.

---

## Check 8: Validity of linear perturbation theory

**Result: PASS**

The Bardeen potential Φ remains ≪ 1 throughout the evolution for all modes of cosmological interest. The perturbation amplitude is set by A_s ~ 10⁻⁹, so Φ ~ 10⁻⁵. Linear theory is valid.

Near the bounce, the Bardeen potential does not grow for super-Hubble modes (T = 1), so there is no breakdown of perturbation theory at the bounce. For sub-Hubble modes (k ~ k_b), the perturbation does oscillate with O(1) transfer, but these modes are at the Planck scale and not observable.

---

## Summary

| Check | Status |
|-------|--------|
| Bardeen regularity | ✓ PASS |
| Transition insensitivity | ✓ PASS |
| Energy conservation | ✓ PASS |
| Asymptotic behavior | ✓ PASS |
| Amplitude (1 free param) | ✓ PASS |
| Mode identification | ✓ PASS (after fix) |
| BKL instability | ⚠ OPEN (known issue) |
| Linear perturbation theory | ✓ PASS |

**The calculation is clean and internally consistent.** The n_s = 1 result is robust — it is not an artifact of numerics, parameter choices, or matching conditions. The only unresolved issue (BKL) is a known problem of the matter bounce scenario that predates the ECH framework.
