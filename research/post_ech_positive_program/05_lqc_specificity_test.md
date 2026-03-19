# LQC Specificity Test

## The Question

Does Loop Quantum Cosmology add real perturbative specificity beyond the generic matter-bounce signal, or is it just another bounce mechanism producing the same generic predictions?

## Observable-by-Observable Assessment

### 1. Scalar Bispectrum f_NL (Amplitude)
**GENERIC_BOUNCE_ONLY**

The f_NL = -35/8 comes from the contracting phase, computed using standard GR perturbation theory with Bunch-Davies vacuum. LQC modifies the bounce dynamics but NOT the contracting-phase perturbation equations. The bispectrum is generated BEFORE the bounce.

LQC could modify f_NL through bounce-generated non-Gaussianity, but:
- The bounce is brief (Δη_bounce << 1/k for CMB modes)
- The non-Gaussianity generated during the bounce itself is suppressed by (k/k_bounce)^n for CMB-scale modes
- LQC effective equations preserve the perturbation conservation laws on superhorizon scales

**Verdict: f_NL = -35/8 is mechanism-independent. LQC adds negligible correction.**

### 2. Scalar Bispectrum Shape
**GENERIC_BOUNCE_ONLY**

The shape function A_T is determined by the contracting-phase mode functions and cubic action. These are independent of the bounce mechanism. The "loosely local" shape with specific equilateral and folded amplitudes is generic.

### 3. Scalar Power Spectrum (Low-k Behavior)
**LQC_MODIFIED (but likely too weak)**

LQC predicts a specific modification to the power spectrum at very large scales (k ~ k_bounce), where the bounce duration is comparable to the mode wavelength. This produces:
- Oscillatory features at k ~ k_bounce (but k_bounce >> k_CMB by many orders)
- A suppression of power at k < k_bounce

However: k_bounce ~ √(ρ_crit)/M_Pl ~ M_Pl, which corresponds to frequencies ~ 10⁹ Hz (GHz). CMB scales are at k ~ 10⁻⁴ Mpc⁻¹. The ratio k_CMB/k_bounce ~ 10⁻⁶⁰. LQC modifications are utterly negligible at CMB scales.

**Verdict: LQC_MODIFIED in principle but TOO_WEAK_TO_MATTER at any observable scale.**

### 4. Tensor-to-Scalar Ratio r
**GENERIC_BOUNCE_ONLY**

In the matter bounce, both scalar and tensor perturbations have scale-invariant spectra generated during the contracting phase. The ratio r is set by the background dynamics during contraction, not by the bounce mechanism.

The generic prediction is r ~ O(1) (both modes grow equally in matter contraction). This is INDEPENDENT of whether the bounce is ECH, LQC, or something else.

**Problem:** r ~ O(1) is already excluded by Planck + BICEP (r < 0.036). This is a GENERIC tension for matter-bounce models, not an LQC-specific issue.

### 5. Tensor Spectrum Tilt n_T
**GENERIC_BOUNCE_ONLY**

n_T ≈ 0 (scale-invariant) from the matter contraction. Independent of bounce mechanism.

### 6. Initial State / Vacuum Choice
**LQC_SPECIFIC (potentially)**

In standard matter bounce: Bunch-Davies vacuum in the infinite contracting past.
In LQC: the bounce occurs at finite time, and the vacuum state might be set by the LQC dynamics rather than the infinite past. This could produce a different "initial state" for the post-bounce expansion, potentially modifying the perturbation spectrum.

However: the standard assumption in LQC bounce cosmology is that modes far inside the Hubble radius at the bounce are well-approximated by the BD vacuum. This is valid for all CMB-scale modes (which are far sub-Hubble at the bounce).

**Verdict: LQC_SPECIFIC in principle but matching to BD vacuum is standard and well-justified.**

### 7. Consistency Relation Violation
**GENERIC_BOUNCE_ONLY**

The Maldacena consistency relation f_NL = (5/12)(1-n_s) is violated in the matter bounce because the growing mode invalidates the assumptions. This violation is generic to ALL growing-mode cosmologies, not LQC-specific.

### 8. Bounce-Transfer Signature
**LQC_MODIFIED (potentially real)**

The transfer matrix connecting pre-bounce to post-bounce perturbations depends on the specific bounce dynamics. LQC gives a SPECIFIC transfer matrix computed from the effective Friedmann equation with quantum corrections.

This could produce:
- Mode-dependent transfer coefficients (not just a phase shift)
- Mixing between growing and decaying modes at the bounce
- k-dependent modifications to the power spectrum normalization

However: for modes well outside the Hubble radius at the bounce (k << k_bounce), the transfer is nearly trivial (ζ conserved on superhorizon scales). The correction is of order (k/k_bounce)² ~ negligible for CMB modes.

**Verdict: LQC_MODIFIED but TOO_WEAK_TO_MATTER for CMB/LSS observables.**

## Overall Assessment

| Observable | Classification |
|-----------|---------------|
| f_NL amplitude | GENERIC_BOUNCE_ONLY |
| f_NL shape | GENERIC_BOUNCE_ONLY |
| Power spectrum (CMB) | GENERIC_BOUNCE_ONLY |
| Low-k features | LQC_MODIFIED but TOO_WEAK (k_CMB/k_bounce ~ 10⁻⁶⁰) |
| Tensor-to-scalar ratio | GENERIC_BOUNCE_ONLY (and in tension with data) |
| Tensor tilt | GENERIC_BOUNCE_ONLY |
| Initial state | LQC_SPECIFIC in principle, BD in practice |
| Bounce transfer | LQC_MODIFIED but TOO_WEAK |
| Consistency relation | GENERIC_BOUNCE_ONLY |

## Verdict

**LQC adds NO real perturbative specificity at observable scales.**

The strongest bounce signal (f_NL = -35/8) is completely mechanism-independent. LQC-specific effects are confined to k ~ k_bounce (Planck-scale frequencies), which is 60 orders of magnitude away from any observation.

**The best science is mechanism-ROBUST, not mechanism-SPECIFIC.** This is actually a strength: the f_NL prediction doesn't depend on choosing ECH vs LQC vs any other bounce mechanism. It tests the entire bounce paradigm.
