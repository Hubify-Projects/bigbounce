# 04: Local-Template Translation

---

## The Central Result of File 03

The conversion between Cai et al.'s |B|_NL and our Planck-convention f_NL has been derived:

$$
f_{\rm NL}^{\rm local}(\text{Planck}) = |B|_{\rm NL}^{\rm squeezed}(\text{Cai})
$$

**These are algebraically identical in the squeezed limit.** The proof:

1. Cai's definition: |B|_NL = (10/3) A_T / (sum k_i^3)
2. Cai's bispectrum: B_zeta = (2pi)^4 P_zeta^2 A_T / (k_1 k_2 k_3)^3
3. Our extraction: f_NL = (5/12) B_zeta / (P(k_1) P(k)) in squeezed limit
4. Using P(k) = (2pi^2/k^3) P_zeta:

f_NL = (5/3) A_T^sq / k^3

And Cai's |B|_NL^sq = (10/3) A_T^sq / (2k^3) = (5/3) A_T^sq / k^3.

Therefore f_NL = |B|_NL^sq. QED.

---

## What This Means

### The raw squeezed-limit coefficient IS the local-template f_NL

Unlike the equilateral or folded limits (where |B|_NL ≠ f_NL^local), in the squeezed limit the Cai normalization and the Planck normalization agree exactly. This is because:

- The squeezed limit is dominated by the local-type contribution
- The factor (k_1^3 + 2k^3) -> 2k^3 in the squeezed limit
- The factor P(k_1) P(k) = (2pi^2)^2 P_zeta^2 / (k_1^3 k^3)
- These combine to give the same numerical coefficient

### No additional "template projection" is needed for the squeezed-limit value

If f_NL^sq = -35/8, then this IS the Planck-convention f_NL extracted from the squeezed limit. There is no hidden factor.

---

## But: Template Projection Is Still Needed for Survey Forecasts

### The subtlety:

Surveys like Planck and MegaMapper do NOT measure the squeezed limit alone. They fit the ENTIRE bispectrum to the local template across ALL triangle configurations. The effective f_NL measured by a survey is:

$$
f_{\rm NL}^{\rm eff} = f_{\rm NL}^{\rm sq}\cdot\cos(\theta)
$$

where cos(theta) is the overlap between the full matter-bounce shape and the local template.

### When does cos(theta) ≈ 1?

If the matter bounce bispectrum is dominated by the squeezed configurations (which carry the most signal-to-noise for the local template), then cos(theta) ≈ 1 even if the shape deviates from local at equilateral or folded configurations.

For the local template, the Fisher information is concentrated in squeezed triangles (k_1/k << 1). This means cos(theta) is weighted toward the squeezed limit.

### Estimate:

From Cai et al.'s equilateral vs squeezed comparison:
- |B|_NL^sq = -35/8 = -4.375
- |B|_NL^equil = -255/64 = -3.984

The ratio |B|_NL^equil / |B|_NL^sq = 0.91.

For a pure local shape: |B|_NL^equil / |B|_NL^sq = 3/2 * P(k)^2 / (2 P(k_1) P(k)) evaluated at equilateral vs squeezed. In the Cai normalization, this ratio is (18/5)/(12/5) * (normalization factors). For a pure local template, |B|_NL is constant over ALL triangles (that's the definition of |B|_NL for a local shape).

Actually — |B|_NL for a pure local shape is NOT constant. The factor (sum k_i^3) in the denominator changes across triangle configurations.

For equilateral (k,k,k): sum k_i^3 = 3k^3
For squeezed (k_1->0, k,k): sum k_i^3 = 2k^3

So |B|_NL^equil / |B|_NL^sq = (A_T^equil / 3k^3) / (A_T^sq / 2k^3) = (2/3)(A_T^equil / A_T^sq)

For a pure local shape: A_T^local ~ 1/k_1 in squeezed limit and A_T^local ~ k^0 at equilateral. The ratio A_T^equil / A_T^sq ~ (k_1/k)^1 -> 0 in the squeezed limit. So |B|_NL^equil / |B|_NL^sq -> 0 for a pure local shape.

But Cai finds the ratio is 0.91, NOT zero. This means the matter bounce shape has SIGNIFICANT equilateral contamination relative to a pure local shape.

### What this implies for cos(theta):

The matter bounce shape is not purely local. It has equilateral-type contributions (from the contact vertices in the cubic action) that are O(1) because epsilon = 3/2.

However, for the Fisher-weighted overlap, the squeezed configurations dominate. An order-of-magnitude estimate:

cos(theta) ~ 0.85 to 0.95

This is based on the fact that:
1. The squeezed limit matches exactly (by construction)
2. The equilateral amplitude is within 10% of the squeezed value
3. The Fisher weight is concentrated at squeezed configurations

**Conservative estimate: cos(theta) > 0.75**

---

## Summary of Translation

| Quantity | Value | Status |
|----------|-------|--------|
| Raw squeezed coefficient f_NL^sq | -35/8 = -4.375 (if Cai correct) | EQUALS Planck f_NL |
| Cai-to-Planck conversion factor | 1.0 (exact in squeezed limit) | PROVEN |
| Template projection cos(theta) | 0.85 - 0.95 (estimated) | NEEDS COMPUTATION |
| Effective observable f_NL^eff | -3.7 to -4.2 (estimated) | NEEDS CONFIRMATION |
| MegaMapper SNR | 7.4 to 8.4 | ROBUST if above holds |

---

## The Li-Brandenberger Discrepancy Revisited

Since f_NL = |B|_NL^sq exactly, the factor-of-2 between Cai (-35/8) and Li-Brandenberger (-35/16) cannot be a normalization artifact in the squeezed limit. It must be:

1. A factor of 2 in the cubic action prefactor or the in-in commutator factor
2. A different definition of their "f_NL" (without the 3/5 factor, or with a different convention)
3. An algebraic error in one of the calculations

The systematic nature of the factor (numerator 35 preserved) strongly suggests option 1 or 2.
