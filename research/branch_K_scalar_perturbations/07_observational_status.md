# Observational Status

**Date:** 2026-03-16

---

## What the Bounce Predicts for the Scalar Sector

### Direct predictions (from the bounce alone)

| Observable | Prediction | Status |
|-----------|-----------|--------|
| Scalar transfer function T(k) | 1.000 for k ≪ k_b | Consistent (no distortion) |
| Scalar spectral tilt modification | Δn_s = 0 | Consistent (no modification) |
| Running modification | Δ(dn_s/d ln k) = 0 | Consistent |
| Scalar amplitude modification | ΔA_s = 0 | Consistent |
| Tensor-to-scalar ratio r | ~10⁻⁵⁵ | Consistent (r < 0.03) |
| Non-Gaussianity f_NL (torsion) | ~10⁻⁵⁶ | Consistent (|f_NL| < 5) |
| Oscillatory features | At k ~ k_b ~ GHz | No data at GHz |

### Indirect predictions (requiring pre-bounce specification)

| Observable | Prediction | Status |
|-----------|-----------|--------|
| Scalar amplitude A_s | Pre-bounce dependent | Cannot constrain bounce |
| Scalar tilt n_s | Pre-bounce dependent | Cannot constrain bounce |
| Running | Pre-bounce dependent | Cannot constrain bounce |

---

## Comparison with Observed CMB Scalar Spectrum

### Planck 2018 results (baseline ΛCDM)

```
A_s = (2.100 ± 0.030) × 10⁻⁹    at k_* = 0.05 Mpc⁻¹
n_s = 0.9649 ± 0.0042
r < 0.064 (95% CL)
dn_s/d ln k = -0.0045 ± 0.0067
```

### Bounce compatibility

The bounce predicts T(k) = 1 at CMB scales. This means:

```
A_s,observed = T² × A_s,pre-bounce = A_s,pre-bounce
n_s,observed = n_s,pre-bounce
```

**The bounce is TRIVIALLY compatible** with any observed scalar
spectrum, because it doesn't modify the spectrum at all.

This is simultaneously:
- **Good news:** The bounce doesn't conflict with CMB data.
- **Bad news:** The bounce makes no testable prediction.

---

## Could Features Be Detectable?

### At CMB scales (10⁻⁴ to 1 Mpc⁻¹)

The transfer function is T = 1 with corrections of order
(k/k_b)² ~ 10⁻⁵⁶. This is immeasurably small. No feature.

Current feature constraints from Planck: features with
amplitude ΔP_S/P_S > 10⁻² are detectable at specific scales.
The bounce correction is 10⁻⁵⁶. Undetectable.

### At large-scale structure scales (0.01 to 10 Mpc⁻¹)

Same conclusion. T = 1 with negligible corrections.

Future surveys (DESI, Euclid, Roman) will improve feature
sensitivity by ~10× relative to Planck. Still 10⁵⁴ away
from the bounce correction.

### At small scales (k > 10 Mpc⁻¹)

CMB spectral distortions (PIXIE, SuperPIXIE) probe scales
up to k ~ 10⁴ Mpc⁻¹. Even at this extreme:

```
k/k_b ~ 10⁴/10²⁵ = 10⁻²¹
```

Still deeply in the T = 1 regime. No bounce feature.

### At ultrashort scales (k ~ k_b)

The bounce features live at k ~ k_b ~ 10²⁵ Mpc⁻¹,
corresponding to wavelengths ~ cm and frequencies ~ GHz.

There is NO cosmological probe at these scales:
- CMB: k < 0.3 Mpc⁻¹
- LSS: k < 10 Mpc⁻¹
- Lyman-α: k < 100 Mpc⁻¹
- CMB distortions: k < 10⁴ Mpc⁻¹
- PBH constraints: k < 10⁶ Mpc⁻¹
- BBN: k ~ 10⁸ Mpc⁻¹

Gap to bounce features: 10¹⁷ orders of magnitude minimum.

---

## The r Prediction in Context

### Current and future r constraints

| Experiment | r sensitivity | Status |
|-----------|-------------|--------|
| Planck + BICEP/Keck (2021) | r < 0.03 | Current |
| BICEP Array (2025+) | r ~ 0.003 | In progress |
| LiteBIRD (2030s) | r ~ 0.001 | Planned |
| CMB-S4 (2030s) | r ~ 0.001 | Planned |
| Ultimate limit | r ~ 10⁻⁴ | Theoretical |

### Bounce prediction: r ~ 10⁻⁵⁵

The gap between the bounce prediction and even the most
optimistic future sensitivity is:

```
r_bounce / r_limit = 10⁻⁵⁵ / 10⁻⁴ = 10⁻⁵¹
```

**51 orders of magnitude** below any conceivable detection.

### What this means

The spin-torsion bounce predicts that primordial tensors at
CMB scales are ENTIRELY due to the pre-bounce mechanism (if any).
The bounce-generated tensors are negligible. If tensors are
detected at r ~ 0.01 (for example), they must come from a
pre-bounce inflationary or ekpyrotic phase, not the bounce.

---

## Comparison with Other Bounce Models

| Model | Scalar prediction | Tensor prediction | Distinctive? |
|-------|------------------|------------------|-------------|
| Spin-torsion | T(k) = 1 | P_T ~ 10⁻⁶⁴ | NO (at obs. scales) |
| LQC | T(k) ≈ 1 + corrections | P_T ~ 10⁻¹¹ (model-dep.) | Marginally |
| Matter bounce | Scale-invariant (built-in) | r ~ O(1) (problematic) | Yes (too much) |
| Ekpyrotic | Nearly scale-invariant | r ~ 0 | Marginally |

The spin-torsion bounce is LESS distinctive than LQC (which has
lower ρ_crit and potentially observable corrections) and less
distinctive than the matter bounce (which makes specific scalar
predictions).

The reason: ρ_crit ~ M_Pl⁴ pushes all bounce features to the
Planck scale (GHz frequencies), far beyond any cosmological
probe. LQC with ρ_crit ~ 0.41 ρ_Pl also has features at
high frequencies, but the specific LQC quantum corrections to
the perturbation equations can propagate to larger scales in
some quantization schemes.

---

## Could Anything Save the Observational Prospects?

### Option 1: Lower ρ_crit

If ρ_crit were much lower (e.g., 10⁻¹⁰ M_Pl⁴ instead of
0.21 M_Pl⁴), the bounce scale k_b would shift to potentially
observable frequencies. But ρ_crit in Einstein-Cartan theory
is fixed by the fundamental constants (G, ℏ) and the number
of fermion species. There is no free parameter to tune.

### Option 2: Pre-bounce mechanism with bounce-scale features

If the pre-bounce contraction produced a spectrum with features
at k ~ k_b, the bounce would modify those features in a
calculable, model-specific way. But this requires engineering
the pre-bounce mechanism to produce features at exactly the
bounce scale — a fine-tuning without physical justification.

### Option 3: Non-minimal extensions

Adding propagating torsion, extra fields, or higher-derivative
terms could modify the perturbation equations at lower scales.
But this leaves the MINIMAL model (which is the subject of
this analysis).

**None of these options apply to the minimal spin-torsion bounce.**

---

## Summary Assessment

| Question | Answer |
|----------|--------|
| Is the bounce already excluded? | **NO** (T = 1, trivially compatible) |
| Is the bounce weakly testable? | **NO** (features at GHz, gap of 10¹⁷+) |
| Is the bounce genuinely promising? | **NO** (no observable prediction) |
| Does the bounce improve on Λ+inflation? | **NO** (adds no testable content) |
| Is the result worth reporting? | **MARGINALLY** (consistency + growing mode resolution) |

**The spin-torsion bounce is observationally INERT in the
scalar perturbation sector. It neither conflicts with nor
contributes to the observed scalar power spectrum.**
