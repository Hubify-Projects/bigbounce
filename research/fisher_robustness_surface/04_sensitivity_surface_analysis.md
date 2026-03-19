# 04: Sensitivity Surface Analysis

## The Dominant Failure Surface

There is ONE dominant failure axis: **k_min** (the minimum accessible wavenumber).

Everything else — multi-tracer, photo-z, galaxy bias, number density — is SECONDARY. The k_min dependence is:

σ(f_NL) ∝ k_min^α where α ≈ 2-3

A factor of 2 in k_min → factor 4-8 in σ(f_NL) → factor 4-8 in significance.

## Why k_min Dominates

The Fisher information for local f_NL from SDB scales as:
dF/d(ln k) ∝ [Δb(k)]² × N_modes / P_g² ∝ (1/k²)² × k³ / ... ∝ 1/k

This is DIVERGENT toward low k (in the ideal case). The total Fisher information is:
F ∝ ∫_{k_min}^{k_max} dk/k ∝ ln(k_max/k_min)

But in practice, shot noise and the finite 1/k² growth make this steeper than logarithmic. The result: ~80% of the Fisher information comes from the lowest octave of k-modes.

## Minimum Viable Survey Performance

### For MegaMapper to be DECISIVE (≥ 5σ):
- Required: k_min ≲ 1.5×10⁻⁴ h/Mpc AND (multi-tracer OR b₁ > 4)
- This corresponds to angular modes ℓ ≲ 5 at z ~ 3
- The survey MUST access these ultra-large-scale modes cleanly

### For MegaMapper to provide STRONG EVIDENCE (≥ 3σ):
- Required: k_min ≲ 2×10⁻⁴ h/Mpc WITH multi-tracer (contrast ≥ 3) OR b₁ ≥ 5
- OR: k_min ≲ 1.5×10⁻⁴ with single tracer and b₁ ≥ 3

### For SPHEREx to provide a MEANINGFUL HINT (≥ 2σ):
- Required: k_min ≲ 1×10⁻⁴ h/Mpc (in the angular analysis) AND high-quality multi-z-bin cross-correlations
- Simple single-population SDB is NOT sufficient for SPHEREx

### For ANY survey to fail completely:
- k_min > 5×10⁻⁴ h/Mpc → σ(f_NL) > 30 → no useful constraint regardless of other assumptions

## The Ultra-Large-Scale Mode Access Question

The CRITICAL unknown: can future surveys access ℓ ~ 2-10 modes cleanly?

**Challenges:**
1. **Galactic foregrounds:** At ℓ ~ 2-10, Galactic dust, stars, and systematics dominate the observed signal. Careful foreground modeling is essential.
2. **Survey geometry:** Partial sky coverage (f_sky < 1) couples low-ℓ modes and degrades their measurement.
3. **Relativistic/wide-angle effects:** At ℓ ~ 2-10, general-relativistic corrections to the galaxy number counts become important. The Doppler, lensing, and ISW contributions create an effective f_NL^GR ~ 1-5 that must be modeled and subtracted.
4. **Integral constraint:** Galaxy surveys with finite volume have a mean density offset that creates large-scale artifacts.

**Mitigations:**
- All-sky surveys (SPHEREx) avoid some geometry issues
- Spectroscopic surveys (MegaMapper) can separate angular and radial modes
- GR effects are COMPUTABLE (Bonvin & Durrer 2011) — they shift f_NL by a known amount, not a random systematic
- Multi-tracer cancels some systematics along with cosmic variance

## Where the Science Case Lives

The science case LIVES in this region:
- k_min ≲ 1.5×10⁻⁴ h/Mpc (ultra-large-scale modes accessible)
- Multi-tracer with contrast ≥ 1.5 (cosmic variance partially cancelled)
- b₁ ≥ 2.5 (adequate SDB amplitude)
- GR projection effects properly modeled and subtracted

The science case DIES if:
- k_min > 3×10⁻⁴ h/Mpc (ultra-large-scale modes lost to systematics)
- OR foreground contamination at ℓ ~ 2-10 is unmanageable
- OR integral-constraint bias is unresolvable

## The Single Most Important Research Question

**Is k_min ~ 10⁻⁴ h/Mpc achievable in practice for MegaMapper and SPHEREx?**

This is NOT a theoretical question. It is an observational-methodology question that depends on:
- Foreground subtraction quality
- Survey window deconvolution
- GR correction modeling
- Integral constraint treatment

The published forecasts ASSUME these are handled. Whether they CAN be handled is the dominant uncertainty.
