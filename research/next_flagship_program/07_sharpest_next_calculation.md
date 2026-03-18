# 07: Sharpest Next Calculation

**Created:** 2026-03-17
**Status:** COMPLETE

---

## The Decision Space

| Candidate | What it resolves | Risk of wasted effort | Value if successful |
|-----------|-----------------|----------------------|-------------------|
| A: Gradient-expansion f_NL derivation | The -35/8 vs -2.2 discrepancy | LOW (clean algebra) | CRITICAL (confirms or corrects flagship) |
| B: In-in f_NL reproduction | Same, but reproducing Cai et al. directly | MEDIUM (complex integrals) | CRITICAL (same) |
| C: LQC bounce transfer for f_NL | Whether bounce preserves/enhances f_NL | HIGH (requires third-order LQC, likely needs numerics) | HIGH (answers Quintin no-go) |
| D: Exact r in dressed-metric | Pinning down r for w = -0.003 | LOW (but low value — r is untestable) | LOW |
| E: Template projection of bispectrum | How "loosely local" maps to observed f_NL^local | MEDIUM | MEDIUM |
| F: Quintin no-go test for LQC | Whether r suppression forces f_NL enhancement | MEDIUM (analytic argument possible) | HIGH |

---

## Selection: **A — Gradient-Expansion f_NL Derivation**

### Why This Dominates All Alternatives

**1. It resolves the foundation crisis.** Three discrepant values exist (-35/8, -35/16, -2.2). Until we know which is correct, every downstream calculation (bounce transfer, detection forecasts, inflation comparison) is built on uncertain ground. This is the highest-leverage resolution.

**2. It is the fastest path to a definitive answer.** The gradient expansion requires:
- Background: a(eta) = a_0 eta^2 (known)
- First-order perturbation: zeta^(1) proportional to a^{-3/2} (known)
- Second-order: solve the local Friedmann equation to second order (algebra)
- Extract coefficient ratio: f_NL = (5/6) * zeta^(2) / (zeta^(1))^2

This is a paper-and-pencil calculation. No numerical codes, no bounce transfer, no LQC machinery required.

**3. It immediately clarifies the program trajectory.** Three possible outcomes:

| Outcome | Implication |
|---------|------------|
| f_NL = -35/8 confirmed | Foundation solid. Proceed to bounce transfer (Calc C) |
| f_NL = -2.2 (Li-Brandenberger) | Foundation weakened but not dead. MegaMapper detection drops to 4.4 sigma. Still interesting. Need to understand why Cai et al. got a different value |
| f_NL = something else | Major discovery — literature has errors. Complete recalibration needed |

Every outcome is informative. No outcome is wasted effort.

**4. It has the lowest risk of failure.** The gradient expansion is well-understood formalism. The calculation is finite and completable. The only risk is computational error, which can be checked algebraically.

**5. It directly addresses the mistake that produced 5/12.** By using the gradient expansion CORRECTLY (tracking the growing mode), we demonstrate exactly where the earlier delta-N attempt went wrong and establish the correct procedure.

---

## Exact Specification

### Input Assumptions
- Background: matter-dominated contraction, a(t) = a_0 (-t/t_0)^{2/3}
- Matter: canonical scalar field with V = (1/2) m^2 phi^2, dust-like EOS (w = 0)
- Perturbations: adiabatic, single-field
- Gauge: comoving gauge (zeta definition)
- Initial conditions: Bunch-Davies vacuum in the asymptotic past
- Spatial topology: flat (K = 0 background, perturbative K from gradients)

### Output Quantity
f_NL^local in the squeezed limit, defined as:
zeta(x) = zeta_G(x) + (3/5) f_NL [zeta_G^2(x) - <zeta_G^2>]

This is the Planck convention.

### Method
1. Write the perturbed FRW equations to second order in the gradient expansion
2. Solve for the growing mode at first order: zeta^(1)(t,x) = C(x) * g(t) with g(t) proportional to (-t)^{-1} (or a^{-3/2})
3. Identify the second-order source: quadratic in zeta^(1)
4. Solve for zeta^(2)(t,x) as a particular solution sourced by (zeta^(1))^2
5. Extract f_NL = (5/6) * [zeta^(2) / (zeta^(1))^2] in the superhorizon limit

### Intermediate Checkpoints

| Checkpoint | How to verify |
|-----------|--------------|
| First-order growing mode: zeta^(1) proportional to (-t)^{-1} | Compare with known Mukhanov-Sasaki solution |
| Power spectrum: P_zeta proportional to k^0 | Must be scale-invariant at leading order |
| Second-order source proportional to (zeta^(1))^2 | Dimensional analysis + consistency with Einstein equations |
| f_NL is a pure number (no time or scale dependence) | Required for a well-defined local f_NL |
| Sign is negative | Expected from the growing mode physics (anti-correlation) |

### What Result Would Strengthen the Program
- f_NL = -35/8 exactly (or within 10%): the Cai et al. value is confirmed, foundation is solid, proceed to bounce transfer
- f_NL between -2.2 and -4.4: the truth is somewhere in the discrepancy range, but the prediction is still negative and O(1), which is the key discriminating feature

### What Result Would Seriously Damage the Current Lane
- f_NL = 0 or positive: the matter bounce does NOT produce negative local non-Gaussianity. The entire discriminator program is dead.
- |f_NL| > 10: the prediction already violates Planck bounds. The model is excluded.
- f_NL is scale-dependent or time-dependent: the prediction is not a clean number, making it less sharp as a discriminator

---

## After This Calculation

If f_NL is confirmed at O(1) and negative:

**Next calculation:** The Quintin no-go test for the LQC dressed-metric bounce (Calculation F from the decision space). This determines whether the r suppression mechanism (dressed-metric scalar amplification) also amplifies f_NL. If f_NL is preserved through the bounce, the prediction is solid. If enhanced, we need to check whether the enhanced value still satisfies Planck bounds.

If f_NL is different from expected:

**Next calculation:** Detailed comparison of Cai et al., Li & Brandenberger, and our result. Identify exactly which terms in the cubic action produce the discrepancy. This would be a significant technical contribution to the bounce cosmology literature regardless of the outcome for our program.
