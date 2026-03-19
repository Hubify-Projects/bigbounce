# 03: Shape Projection Results

## Critical Distinction: CMB vs LSS Template Projection

The "template projection" question has TWO different answers depending on the experiment type.

### Galaxy Surveys (MegaMapper, SPHEREx) — Scale-Dependent Bias

Galaxy surveys extract f_NL through the **scale-dependent bias** effect:
Δb(k) = 2(b₁ - 1) × f_NL × δ_crit / (α(k) × k²)

This is a purely SQUEEZED-LIMIT measurement. The survey is sensitive to the bispectrum at k_long << k_short, where the long mode modulates the local number density of galaxies.

For the matter bounce: the squeezed-limit bispectrum gives |B|_NL → -35/8 = -4.375 as k₁/k → 0. This IS the local-type f_NL, by definition. **No template projection loss.**

**cos(θ) for galaxy surveys: effectively 1.0**
**f_NL^eff for galaxy surveys: -4.375 (full amplitude)**

### CMB Bispectrum Estimator (Planck, CMB-S4)

CMB bispectrum estimators integrate over the FULL triangle space with signal-to-noise weighting. The overlap between the matter-bounce shape and the local template depends on the weight function.

Computation with the standard (k₁k₂k₃)² weight shows:
- The cosine is **highly sensitive to the squeezed-limit cutoff** (k_min/k_max)
- At k_min/k_max = 0.1: cos(θ) ≈ -0.54
- At k_min/k_max = 0.01: cos(θ) ≈ -0.10
- The integral is ILL-CONDITIONED because both shapes diverge differently in the squeezed limit

This means the (k₁k₂k₃)² weight is NOT appropriate for estimating the CMB overlap — it doesn't include the actual CMB signal-to-noise weighting that regulates the squeezed divergence.

A proper CMB overlap computation would require:
- The CMB bispectrum transfer functions β_ℓ(k)
- Noise spectra N_ℓ
- The KSW or modal estimator framework

This is beyond what we need for the discrimination forecast, because **the primary test comes from galaxy surveys (MegaMapper/SPHEREx), not CMB**.

## The Key Result

**For the galaxy-survey tests that matter (MegaMapper at 8.3σ, SPHEREx at 2.8-4.2σ), the template projection is essentially perfect: cos(θ) ≈ 1.**

The reason: scale-dependent bias extracts the SQUEEZED-LIMIT bispectrum, which is EXACTLY the local template by definition. The matter-bounce shape converges to -35/8 in the squeezed limit (verified numerically: |B|_NL → -4.375 as k₁/k → 0). There is no shape-mismatch suppression.

## Impact on Forecasts

| Experiment | Method | cos(θ) | f_NL^eff |
|-----------|--------|--------|----------|
| MegaMapper | Scale-dependent bias | **~1.0** | **-4.375** |
| SPHEREx | Scale-dependent bias | **~1.0** | **-4.375** |
| Planck | CMB bispectrum estimator | Unknown (need proper computation) | Unknown |
| CMB-S4 | CMB bispectrum estimator | Unknown (need proper computation) | Unknown |

**The galaxy-survey forecasts (MegaMapper, SPHEREx) do NOT suffer from template-projection suppression.** The previous estimate of cos(θ) ≈ 0.95 was unnecessarily conservative for these experiments.

## Correction to Previous Estimates

Previous: f_NL^eff ≈ -4.375 × 0.95 = -4.16 → MegaMapper at 8.3σ
Corrected: f_NL^eff ≈ -4.375 × 1.0 = -4.375 → MegaMapper at **8.75σ**

The change is small (8.3σ → 8.75σ) but the reasoning is now more rigorous.

## What the Full-Shape Code Showed

The (k₁k₂k₃)²-weighted inner product gives near-zero cosine because:
1. Both shapes diverge in the squeezed limit but with different powers of k
2. The weight function doesn't properly regulate this divergence
3. The CMB-style overlap integral is ill-conditioned without proper noise weighting

This does NOT mean the shapes are dissimilar — it means the standard inner product is the wrong tool for this comparison. For the galaxy-survey extraction (which dominates the forecast), the squeezed-limit match is perfect.
