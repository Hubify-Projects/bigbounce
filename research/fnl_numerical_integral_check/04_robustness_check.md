# 04: Robustness Check

---

## What Was Tested

### Term 1 (converged — full robustness battery):

| Test | Variation | f_NL range | Verdict |
|------|-----------|------------|---------|
| Late-time cutoff η_f | -0.1 to -0.001 | 1.560–1.562 | PASS |
| Squeeze ratio k₁/k | 0.1 to 0.0001 | 1.561–1.562 | PASS |
| iε regulator | 1e-2 to 1e-6 | 1.561 | PASS |
| UV cutoff x_early | -100 to -5000 | 1.561–1.563 | PASS |
| Subleading perms | with/without | 1.561/1.562 | PASS (0.1% effect) |
| Gradient term (Term 2) | included | 0.002% of Term 1 | NEGLIGIBLE |

**Term 1 is rock-solid.** The numerical evaluation converges to f_NL = 1.5613 ± 0.001 across all parameter variations.

### Full cubic action (NOT converged):

| Test | Variation | f_NL range | Verdict |
|------|-----------|------------|---------|
| Late-time cutoff η_f | -0.1 to -0.001 | 0.94 to 1816 | **FAIL** |
| Squeeze ratio k₁/k | 0.001 to 0.0001 | 3.5 to 188 | **FAIL** |
| UV cutoff | -100 to -5000 | 2.6 to 3.5 | **FAIL** |
| iε regulator | 1e-2 to 1e-5 | 3.2 to 3.5 | marginal |

**The full calculation fails robustness checks** because Terms 4 and 6 introduce divergences that don't cancel within individual terms.

---

## Numerical Stability Analysis

### Float64 precision:
- Term 1 integrands: max ~10²¹, but the RATIO B/PP has all divergences cancelled, giving a stable O(1) result.
- Term 6 integrands: max ~10⁴⁹ (from χ² factors), with the divergent part NOT cancelling within Term 6 alone.
- The inter-term cancellation (between Terms 4, 6, and possibly 3) would require computing individual B_i to ~30 significant digits — far beyond float64's 16 digits.

### Quadrature accuracy:
- scipy.integrate.quad with limit=5000 achieves absolute error ~10⁻¹⁴ for Term 1.
- For Terms involving χ, the integrand oscillations combined with power-law growth overwhelm the adaptive quadrature.

---

## Verdict

The numerical integration approach is RELIABLE for the single-vertex contribution but INSUFFICIENT for the complete bispectrum. This is not a code bug — it's a fundamental limitation of numerical evaluation for growing-mode cosmologies. The analytical approach used by Cai et al. avoids this problem by cancelling divergences symbolically.
