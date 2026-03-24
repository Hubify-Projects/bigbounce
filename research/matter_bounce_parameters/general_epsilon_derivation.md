# Phase 2: General-ε Derivation — Progress Report

**Date:** 2026-03-23
**Status:** MODE FUNCTIONS COMPUTED, BISPECTRUM PENDING

---

## Key Finding: ε = 3/2 is a Singular Point

The Hankel function index for the mode functions is:

$$\nu(\varepsilon) = \frac{1 - 3p}{2(1-p)} \quad \text{where} \quad p = \frac{2}{2\varepsilon - 1}$$

At ε = 3/2: p = 1 and ν → ∞ (pole). The mode functions at exact matter domination are NOT standard Bessel/Hankel functions — they are the DEGENERATE case where the Bessel index diverges and the solutions reduce to polynomials × exponentials.

This means:
- Taylor expansion of f_NL(ε) around ε = 3/2 via ν-perturbation is NOT valid
- The numerical ODE approach (solving the Mukhanov-Sasaki equation directly) is required
- The ε-correction coefficient c₁ cannot be obtained from simple Hankel-order perturbation theory

## Mode Function Results

Successfully computed mode functions via direct ODE integration for ε ∈ [1.48, 1.52]:

| ε | p | |ζ|²/|ζ|²_ref | Comment |
|---|---|---------------|---------|
| 1.480 | 1.0204 | 1.387 | |
| 1.490 | 1.0101 | 1.175 | |
| 1.4955 | 1.0045 | 1.075 | Wilson-Ewing |
| 1.500 | 1.0000 | 1.000 | Reference (exact dust) |
| 1.505 | 0.9950 | 0.924 | |
| 1.510 | 0.9901 | 0.854 | |
| 1.520 | 0.9804 | 0.733 | |

The power spectrum varies smoothly (~8% per 0.01 in ε) despite the ν singularity. The ODE solver handles the singularity correctly because it doesn't use the Hankel representation.

## What's Needed for f_NL(ε)

To compute f_NL as a function of ε, we need to:

1. **For each ε value:** solve the ODE for two mode functions (k and k₁) at multiple momenta
2. **Evaluate the cubic action integrals:** products of mode functions integrated over conformal time
3. **Extract A_T:** the shape function at squeezed, equilateral, and folded configurations
4. **Compute |B|_NL:** and map to f_NL via the Planck convention

This is a 2D numerical integration (over time and momentum ratios) for each ε value. For a scan over ~20 ε values with 3 momentum configurations each, this is ~60 numerical integrations.

**Estimated compute:**
- Each integration: ~10 seconds with scipy adaptive quadrature
- Total: ~10 minutes locally, or ~2 minutes on RunPod CPU with parallelization
- Not GPU-worthy

## Impact on the Consistency Relation

The current estimate uses:
$$f_{\rm NL}(\varepsilon) \approx -\frac{35}{8} \times (1 + 2\delta\varepsilon/\varepsilon)$$

with coefficient c ≈ 2 from scaling. The ν-singularity means this scaling argument may be inaccurate near ε = 3/2. The numerical computation will determine whether the linear approximation is valid and what the actual coefficient is.

Possible outcomes:
1. **Linear approximation holds:** c ≈ 2 is confirmed, consistency relation survives
2. **Nonlinear near singularity:** f_NL(ε) has non-trivial curvature near ε = 3/2
3. **Weak dependence:** f_NL barely changes with ε (making the consistency relation trivial)

All outcomes are scientifically informative.

## Next Steps

1. **Implement general_epsilon_bispectrum.py:** cubic action integrals with ODE-computed mode functions
2. **Run ε scan:** f_NL at 20 ε values
3. **Extract derivative:** df_NL/dε at ε = 3/2 (numerically, avoiding the singularity analytically)
4. **Validate consistency relation:** compare against current approximate coefficient

### RunPod needed?
Probably not — the computation is ~10 minutes locally. But if we want a fine-grained scan with convergence testing, RunPod CPU would be faster.
