# 05: Power Spectrum Results

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Result

$$
\boxed{n_s = 1.000 \quad \text{(Harrison-Zel'dovich, scale-invariant)}}
$$

The dust contraction → ECH bounce → radiation expansion scenario produces an **exactly scale-invariant** primordial scalar power spectrum, with corrections of order (k/k_b)² ~ 10⁻⁵⁶ at CMB scales.

This is **8.3σ discrepant** with the Planck 2018 measurement of n_s = 0.9649 ± 0.0042.

---

## Derivation

### Analytic argument

1. **Dust contraction phase:** The Mukhanov-Sasaki equation with z''/z = 2/η² (matter domination) gives a scale-invariant spectrum of the curvature perturbation ζ. The growing mode amplitude at freeze-out is |ζ_k|² ∝ k⁻³, which gives P_ζ = k³/(2π²)|ζ_k|² ∝ k⁰. This is the standard result from Finelli & Brandenberger (2002).

2. **EOS transition (dust → radiation):** The curvature perturbation ζ is conserved on super-Hubble scales for adiabatic perturbations, regardless of the equation of state. The transition from w = 0 to w = 1/3 preserves ζ for modes with k/aH ≪ 1. Since all observable modes satisfy k/k_b ~ 10⁻²⁸ ≪ 1, the transition does not modify the spectrum.

3. **ECH bounce:** Branch K established that the symmetric radiation bounce has transfer function T(k) = 1 for k ≪ k_b. Our numerical computation confirms this: the constant mode of the Bardeen potential passes through the bounce unmodified for super-Hubble modes.

4. **Result:** P_ζ,output = T² × P_ζ,input. With T = 1 and P_ζ,input ∝ k⁰, we get P_ζ,output ∝ k⁰, i.e., n_s = 1.

### Numerical verification

We computed the transfer function T(k) = Φ_out(k)/Φ_out(k_ref) for the constant Bardeen potential mode through the full dust → transition → ECH bounce → radiation evolution:

| k/k_b | T(k) | Deviation from T = 1 |
|--------|------|---------------------|
| 10⁻⁴ | 1.000000 | reference |
| 3.6 × 10⁻⁴ | 1.008 | 0.8% |
| 10⁻³ | 1.061 | 6.1% |
| 3.3 × 10⁻³ | 1.740 | 74% |
| 10⁻² | 5.69 | 469% |

The transfer function deviates from unity only when k/k_b approaches O(10⁻³) or larger. For actual CMB modes (k/k_b ~ 10⁻²⁸), the deviation is of order (k/k_b)² ~ 10⁻⁵⁶ — completely negligible.

**The spectral index correction from the bounce:**

$$
\delta n_s \sim 2 \frac{d \ln T}{d \ln k} \sim \left(\frac{k}{k_b}\right)^2 \sim 10^{-56}
$$

This is zero to any measurable precision.

---

## Amplitude

The amplitude normalization P_ζ = A_s ≈ 2.1 × 10⁻⁹ is set by the duration of the dust contraction phase. Specifically:

$$
A_s \propto \frac{\rho_{\rm bounce}}{M_{\rm Pl}^4} \times \left(\frac{a_{\rm bounce}}{a_{\rm initial}}\right)^3
$$

where the second factor is the growth factor of the curvature perturbation during contraction. This depends on a_initial (i.e., how early the contraction began), which is a free parameter analogous to the height of the inflationary potential.

**One free parameter** (the contraction duration or equivalently a_initial/a_bounce) is needed to match A_s. This is comparable to inflation, which also has one free parameter for the amplitude (V₀ or the Hubble scale during inflation).

---

## Spectral running

The running of the spectral index is:

$$
\alpha_s = \frac{d n_s}{d \ln k} = 0
$$

to the same precision as n_s = 1. The spectrum is exactly power-law (with no running) in the matter bounce.

Observed: α_s = −0.0045 ± 0.0067 (Planck 2018) — consistent with zero.

---

## Tensor spectrum

From the same analysis:

- **Tensor spectral index:** n_T = 0 (flat, same as the scalar spectrum)
- **Tensor-to-scalar ratio:** r ~ (k/k_b)² ~ 10⁻⁵⁵ (unobservable)

The consistency relation for the matter bounce differs from inflation:

| Model | Consistency relation |
|-------|---------------------|
| Slow-roll inflation | r = −8n_T |
| Matter bounce (ECH) | r ≈ 0, n_T ≈ 0 (both vanishing) |

This is not useful as a discriminator because both r and n_T are too small to measure.

---

## Comparison with observations

| Observable | Matter bounce + ECH | Planck 2018 | Compatible? |
|-----------|--------------------|-----------|----|
| n_s | 1.000 | 0.9649 ± 0.0042 | **NO (8.3σ)** |
| α_s | 0 | −0.005 ± 0.007 | YES |
| r | ~10⁻⁵⁵ | < 0.036 | YES (trivially) |
| A_s | tunable (1 param) | 2.1 × 10⁻⁹ | YES (with tuning) |

**The n_s = 1 prediction is the showstopper.** The spectrum is 8.3σ from the observed value. The matter bounce + ECH model is excluded by Planck data unless an additional mechanism provides the red tilt.

---

## The n_s = 1 problem: known in the literature

This is a well-known problem of the matter bounce scenario, not specific to the ECH framework:

- Finelli & Brandenberger (2002) established n_s = 1 for the symmetric matter bounce
- Cai & Wilson-Ewing (2014) confirmed n_s = 1 for the LQC matter bounce
- The ECH bounce gives the same result because the bounce is transparent to super-Hubble modes

### Proposed resolutions in the literature

1. **Entropy-to-curvature conversion** (Cai et al. 2009): A second field converts isocurvature perturbations to curvature at the bounce, with a k-dependent transfer. Can produce n_s < 1 but requires fine-tuning.

2. **Nearly dust-dominated contraction** (Quintin et al. 2015): If w is slightly different from 0 (e.g., w = 10⁻³), the spectrum acquires a tilt proportional to w. But matching n_s = 0.965 requires w ≈ 0.02, which is not dust.

3. **Curvaton mechanism** (Cai et al. 2011): A subdominant scalar field (curvaton) generates the perturbations. The tilt comes from the curvaton mass. Can work but adds a free parameter.

4. **ALP as curvaton** (our framework): The spectator ALP already present in the ECH framework could act as a curvaton, providing the red tilt. This is the most natural resolution within the ECH context but requires a specific mass and coupling. To be investigated in Phase 1b.

---

## Bottom line

The dust contraction + ECH bounce produces a **calculable, well-defined, and scale-invariant** power spectrum. The calculation is clean, the numerics converge, and the result matches the analytic prediction. But the spectrum is wrong: n_s = 1 instead of 0.965.

The ECH bounce is not the problem — it faithfully transmits the pre-bounce spectrum. The problem is the dust contraction itself, which produces n_s = 1 by construction.
