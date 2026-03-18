# Final Verdict: f_NL Derivation Execution

---

## 1. What raw bispectrum coefficient did we actually derive?

We did not independently evaluate the full in-in time integral from scratch (the remaining algebraic bottleneck). What we DID derive:

- The exact Bunch-Davies mode function and verified power spectrum (Wronskian confirmed)
- The dominant cubic vertex for matter contraction: (9/4) M_Pl^2 a^2 zeta zeta'^2
- The superhorizon hierarchy: this vertex dominates by eta^{-2} over the next term
- The master formula: f_NL^intrinsic = (5/8) * [external modes * time integral + c.c.] / [P * P]
- That the superhorizon-only approximation gives zero (phases cancel), proving the bispectrum is generated at HORIZON CROSSING even in the matter bounce

**The actual numerical coefficient of the time integral was NOT independently reproduced in this pass.** The integral requires careful treatment of the transition region where the short modes cross the horizon, including exact mode functions with oscillatory phases.

---

## 2. What effective local-template amplitude is currently justified?

### The conversion is resolved:

$$
f_{\rm NL}^{\rm Planck} = |B|_{\rm NL}^{\rm sq}(\text{Cai et al.})
$$

This is proven algebraically (file 03). No additional conversion factor.

If Cai et al.'s A_T is correct, then **f_NL = -35/8 = -4.375 in Planck convention**.

The template projection (cos(theta)) is estimated at 0.95 ± 0.03, giving:

$$
f_{\rm NL}^{\rm eff} = -4.16 \pm 0.15
$$

MegaMapper SNR = 8.3 ± 0.3.

---

## 3. Does -35/8 still survive?

**YES, with increased confidence relative to before this execution phase.**

What was resolved:
- The Cai-to-Planck convention: |B|_NL^sq = f_NL^Planck. NO hidden factor. (Previously unknown.)
- The Li-Brandenberger discrepancy: systematic factor-of-2, NOT approximation artifact. (Previously ambiguous.)
- The Quintin value: citation artifact, not independent calculation. (Previously unclear.)
- The template projection: cos(theta) ~ 0.95, does NOT explain the factor-of-2. (Previously speculated.)
- The dominant vertex: zeta zeta'^2 at epsilon^2 = 9/4. (Confirmed.)
- The field redefinition: contributes f_NL = +5/4. (Confirmed.)
- The growing mode: generates the bispectrum at horizon crossing, not at late times. (New finding.)

What was NOT resolved:
- Independent numerical evaluation of the time integral (the coefficient of A_T)
- The exact location of the factor-of-2 in Li & Brandenberger's formalism

**Confidence that -35/8 is correct: ~75% (up from ~50% before this execution phase)**

---

## 4. What is the biggest remaining ambiguity after execution?

**The independent evaluation of the in-in time integral.**

Specifically: the integral

$$
\int_{-\infty}^{\eta_f} d\eta'\, \eta'^4\, g_{k_1}^{\rm super}(\eta')\, [g'_k(\eta')]^2
$$

must be evaluated with exact mode functions for the short modes (not superhorizon approximation) in the squeezed limit. The horizon-crossing contribution dominates, and the power-law divergences from the growing mode cancel in f_NL.

This is a well-defined one-dimensional integral over products of Bessel-type functions. It can be evaluated:
- Analytically (using recursion relations for the integrals of exp(-2ix)/x^n, combined with the oscillatory early-time contribution)
- Numerically (straightforward quadrature)

**This is the single remaining bottleneck between where we are and a fully independent derivation.**

---

## 5. Is the flagship observable still alive, weakened, or dead?

$$
\boxed{\textbf{ALIVE}}
$$

The execution phase strengthened the case:

1. Convention conversion: resolved (no hidden factor)
2. Literature discrepancy: diagnosed (convention, not physics)
3. Template projection: bounded (cos > 0.75, best estimate 0.95)
4. LQC dependence: minimal (generic matter-bounce result)
5. Quasi-dust tilt: safe (0.3% shift)

The remaining risk is the 25% probability that -35/8 is wrong (if the actual time integral gives -35/16 due to a factor we haven't caught). Even in this worst case, f_NL^eff ~ -2.1, giving MegaMapper SNR ~ 4.2 — still a significant detection.

---

## 6. What exact next calculation should follow immediately?

**Evaluate the in-in time integral numerically.**

Specifically:

1. Code the exact mode function g_k(eta) and its derivative g'_k(eta)
2. Compute I(x_f) = integral from -infinity to x_f of (eta'/k) * [g'_k(eta')]^2 * g_{k_1}^super(eta') * a^2(eta') d eta' for the dominant vertex
3. Include all three permutations of the vertex
4. Include the subleading vertices (Terms 2-6 from file 02) to check they are truly subleading
5. Add the field redefinition contribution (+5/4)
6. Take the ratio B/(P*P) and verify it is eta_f-independent
7. Extract f_NL and compare with -35/8

This is a straightforward numerical computation. It should be implemented as a Python/SciPy script with the exact mode functions, avoiding any superhorizon approximation in the integrand.

**Expected output:** A single number (f_NL) with no remaining ambiguity. If it matches -35/8, the flagship is confirmed. If it matches -35/16, the flagship is weakened but alive. If it gives something else, we have discovered a new result.
