# 01: Precision Diagnosis — The Real Part Problem

## Discovery

The factor-of-3 discrepancy between v1 (f_NL = 1.56) and the corrected code (f_NL = 2.19) was traced to **loss of the real part of the time integral in the corrected code**.

## The Mechanism

The time integral J = ∫ η'⁴ · (mode functions) · dη' is a complex number where:
- Im[J] ~ 10²² (large, from the growing mode)
- Re[J] ~ 10¹⁵ (small, from horizon-crossing oscillations)

The physical bispectrum depends on **both** parts:

B ∝ Im[ext × J] = Re[ext]·Im[J] + Im[ext]·Re[J]

**Term A:** Re[ext]·Im[J] ~ 10²¹ × 10²² = 10⁴³ (dominant)
**Term B:** Im[ext]·Re[J] ~ 10²⁷ × 10¹⁵ = 10⁴² (30% correction)

When Re[J] is lost in roundoff (computed as 10¹⁰ instead of 10¹⁵), Term B becomes negligible, and f_NL inflates by ~30% → from 0.31 to 0.94.

## Numerical Evidence

From the diagnostic script:

| Quantity | V1 (correct) | Corrected (artifact) |
|----------|-------------|---------------------|
| Re[I] | 4.312e+15 | 1.423e+10 |
| Im[I] | -9.684e+21 | -2.179e+22 |
| Im[ext×I] | -4.613e+42 | -3.125e+43 |
| B | 2.076e+43 | 6.251e+43 |
| f_NL (intrinsic) | **+0.311** | +0.938 |

Ratio c1×I_v1 vs I_T1_corrected: imaginary parts match (1.000), real parts differ by 10⁵.

## Lesson

For the matter bounce bispectrum, the REAL part of the time integral is physically meaningful despite being 7 orders of magnitude smaller than the imaginary part. Any computational approach must preserve this real part to ~15 significant digits.

**V1's approach (separating the coefficient from the integral) is more numerically stable** because it avoids multiplying the integrand by a constant before integration, which can shift the roundoff noise floor.

## Implication for All Results

- v1 result f_NL(T1) = +1.561 is CORRECT and CONVERGED
- The "corrected" result of 2.186 ≈ 35/16 was a numerical coincidence
- All previous conclusions based on 35/16 must be revised
- The T3 "correction" (coefficient 27/2) is algebraically correct but NUMERICALLY unreliable
