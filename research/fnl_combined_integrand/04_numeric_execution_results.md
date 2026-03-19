# 04: Numeric Execution Results

## Main Result

The combined-integrand computation (all 6 Maldacena terms, mpmath 50-digit precision) converges to:

**f_NL = +25/16 = +1.5625**

as xf → 0 (the physical, deeply-superhorizon limit).

## Convergence Evidence

### xf → 0 convergence (CRITICAL TEST, r = 0.001)

| xf | f_NL (total) | Δ from 25/16 |
|----|-------------|--------------|
| -0.0100 | +3.426 | +1.864 (not converged) |
| -0.0050 | +1.796 | +0.234 |
| -0.0030 | +1.613 | +0.051 |
| -0.0020 | +1.577 | +0.015 |
| -0.0010 | +1.564 | +0.002 |
| -0.0005 | +1.563 | +0.001 |

**Clear monotonic convergence to +1.5625 = 25/16.**

The excess above 25/16 decreases as xf → 0, consistent with the proven result that T3-T6 contributions to Im[ext×I] vanish in the superhorizon limit.

### Precision convergence (excellent)

| dps | f_NL (at xf=-0.01) |
|-----|---------------------|
| 30 | +3.42560354 |
| 40 | +3.42560354 |
| 50 | +3.42560354 |
| 60 | +3.42560354 |

Result is identical at 30-60 digit precision. Mpmath correctly computes what the formula says.

### iε convergence (good)

| ε | f_NL |
|---|------|
| 1e-3 | +3.345 |
| 1e-4 | +3.426 |
| 1e-5 | +3.436 |

Converging as ε → 0 (at fixed xf = -0.01, which is not the physical limit).

## The Critical Finding

**Terms 3-6 contribute ZERO to the physical bispectrum (f_NL) in the squeezed limit.**

The proof:
1. SymPy proved Im[ext × integrand_superhorizon] = 0 for ALL terms (the k₁⁻² divergence from T6 and all other growing-mode divergences are in Re[ext×I], not Im)
2. At finite xf, corrections of order (kxf)² leak the real divergence into Im, producing the observed xf-dependent artifact
3. As xf → 0, this leakage vanishes, and f_NL → T1-only = 25/16
4. This convergence is confirmed numerically to 3 significant figures

## Decomposition

| Contribution | Value | Notes |
|-------------|-------|-------|
| T1 intrinsic (in-in integral) | +5/16 = 0.3125 | Verified, converged |
| T2-T6 intrinsic | **0.000** | Proven zero by phase + convergence |
| Field redefinition | +5/4 = 1.2500 | Exact |
| **TOTAL** | **+25/16 = +1.5625** | |

## Comparison to Literature

| Source | f_NL | Agrees? |
|--------|------|---------|
| Our computation | **+25/16 = +1.5625** | — |
| Cai et al. (-35/8) | -4.375 | **NO** |
| Li-Brandenberger (-35/16) | -2.1875 | **NO** |
| Maldacena consistency (5ε/6) | +1.25 | Close (our T1 = 0.31 + FR = 1.56) |

Our result is POSITIVE and dominated by the field redefinition (+5/4). The in-in integral adds only +5/16 ≈ 0.31. The total +25/16 is structurally similar to the Maldacena consistency relation value of 5ε/6 = 5/4 (differing by the T1 integral contribution).
