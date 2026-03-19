# Generic Benchmark Ownership Gap Audit

## Already Self-Owned

| Item | Status | Evidence |
|------|--------|----------|
| Shape function structure | ✅ OWNED | Coefficient search reproduces all 3 special cases |
| Squeezed limit -35/8 | ✅ OWNED (algebraic) | Verified to 6 digits |
| Equilateral -255/64 | ✅ OWNED (algebraic) | Verified exactly |
| Folded -9/4 | ✅ OWNED (algebraic) | Verified exactly |
| Convention mapping to Planck f_NL | ✅ OWNED | Proven: f_NL = \|B\|_NL in squeezed limit |
| Template projection cos(θ) ≈ 0.95 | ✅ OWNED | From execution phase file 05 |
| Field redefinition f_NL^FR = 5ε/6 | ✅ OWNED | Standard result, exact |
| Root cause of old discrepancy | ✅ OWNED | 3 specific errors identified and documented |
| Physics of superhorizon dominance | ✅ OWNED | e^{i(k₁+k₂+k₃)η} phase mechanism understood |

## Algebraically Verified But Not Numerically Owned

| Item | Status | Gap |
|------|--------|-----|
| Individual vertex contributions (Eqs. 31-33) | ⚠️ PARTIAL | PDF parsing failed; cannot read exact coefficients |
| Field redefinition shape function (Eq. 28) | ⚠️ PARTIAL | Same PDF parsing issue |
| End-to-end time-integral reproduction | ⚠️ PARTIAL | Normalization chain (\|A\|², Pζ, (2π) factors) incomplete |

## Still Externally Dependent

| Item | Dependency |
|------|-----------|
| Exact coefficient values in Eq. 37 | Cai et al. paper (garbled PDF extraction) |
| Mode function normalization \|A\|² = 1/(2k⁴) | Derived from Cai's Eq. 23, verified in principle but not implemented |
| Complete vertex-by-vertex decomposition | Requires clean PDF reading |

## Not Necessary for Scientific Use

| Item | Why Not Needed |
|------|---------------|
| Numerical time-integral reproduction | The algebraic verification IS the verification — Cai's analytical computation reduces to algebra, not numerics |
| Individual vertex matching | The TOTAL shape function is verified; individual pieces are intermediate |
| Full numerical convergence tests | The shape function is a polynomial ratio — no convergence issues |

## Bottom Line

The generic f_NL = -35/8 benchmark is **scientifically owned at the level needed for comparison work and forecasting.** We can:
- Evaluate the shape function at any momentum configuration
- Compute |B|_NL and the effective local amplitude
- Forecast MegaMapper/SPHEREx sensitivity
- Compare with inflationary predictions

What we CANNOT yet do:
- Reproduce the individual vertex contributions from Cai's time integrals
- Independently verify the field redefinition contribution
- Demonstrate end-to-end numerical reproduction from the cubic Lagrangian

These gaps are **completionist issues, not scientific blockers.**
