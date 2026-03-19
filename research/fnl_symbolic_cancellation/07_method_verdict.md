# 07: Method Verdict

## Was the numerical failure expected?

**YES.** The failure of direct float64 integration for χ-dependent terms was the expected behavior. The growing-mode divergences create O(10⁴⁹) backgrounds from which the O(10²⁷) physical signal must be extracted. Float64's 16 digits are insufficient.

The SymPy phase proof confirms this: the divergences are in Re[ext×I], the physics is in Im[ext×I]. Separating them requires either algebraic insight (our approach) or arbitrary precision arithmetic.

## Was symbolic cancellation the right method?

**PARTIALLY.** The symbolic analysis provided the crucial insight (phase structure proof), but the full numerical extraction still required integrating the corrected finite terms (T1-T4). The symbolic work was necessary but not sufficient on its own.

## What should the next step be?

**Option B: High-precision arbitrary-precision integration on the complete combined integrand.**

Specifically:
1. Combine ALL 6 terms into a SINGLE integrand function
2. The early-time (UV) divergences from individual terms (T3, T5, T6) should cancel in the sum
3. Integrate the combined integrand with mpmath at 50+ digits
4. This should give the COMPLETE f_NL including all contributions

The combined-integrand approach avoids:
- The k₁⁻² divergence (cancels in Im[ext×I])
- The UV divergence from individual χ-terms (cancels in the sum)
- The iε sensitivity of individual terms

## Alternative: Convention verification

An equally valuable next step would be to carefully trace the sign conventions between our computation and Cai et al.'s paper. If the sign can be resolved, the answer is locked at f_NL = ±35/16 = ±2.1875.
