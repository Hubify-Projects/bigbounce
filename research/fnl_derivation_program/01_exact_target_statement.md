# 01: Exact Target Statement

**Created:** 2026-03-17
**Status:** COMPLETE

---

## What We Are Deriving

We are computing the **squeezed-limit bispectrum amplitude** of the comoving curvature perturbation zeta during matter-dominated contraction (w = 0, epsilon = 3/2), in the **local-type non-Gaussianity convention used by Planck**.

---

## Precise Definition of the Target Quantity

### The bispectrum:

$$
\langle \zeta_{\mathbf{k}_1} \zeta_{\mathbf{k}_2} \zeta_{\mathbf{k}_3} \rangle = (2\pi)^3 \delta^{(3)}(\mathbf{k}_1 + \mathbf{k}_2 + \mathbf{k}_3) \, B_\zeta(k_1, k_2, k_3)
$$

### The local-template parametrization (Planck convention):

The LOCAL non-Gaussianity parameter f_NL^local is defined by the ansatz:

$$
\zeta(\mathbf{x}) = \zeta_G(\mathbf{x}) + \frac{3}{5} f_{\rm NL}^{\rm local} \left[ \zeta_G^2(\mathbf{x}) - \langle \zeta_G^2 \rangle \right]
$$

which generates the bispectrum:

$$
B_\zeta^{\rm local}(k_1, k_2, k_3) = \frac{6}{5} f_{\rm NL}^{\rm local} \left[ P_\zeta(k_1) P_\zeta(k_2) + P_\zeta(k_2) P_\zeta(k_3) + P_\zeta(k_3) P_\zeta(k_1) \right]
$$

where P_zeta(k) is the dimensionless power spectrum defined by:

$$
\langle \zeta_{\mathbf{k}} \zeta_{\mathbf{k}'} \rangle = (2\pi)^3 \delta^{(3)}(\mathbf{k} + \mathbf{k}') \frac{2\pi^2}{k^3} P_\zeta(k)
$$

### The squeezed limit:

In the squeezed limit k_1 -> 0 with k_2 = k_3 = k:

$$
B_\zeta(k_1, k, k) \to \frac{12}{5} f_{\rm NL}^{\rm local} \cdot P_\zeta(k_1) P_\zeta(k) \cdot \frac{(2\pi^2)^2}{k_1^3 k^3}
$$

Wait — we need to be more careful about dimensional conventions. Let me use the DIMENSIONAL power spectrum P(k) = (2pi^2/k^3) P_zeta(k) where P_zeta is dimensionless. Then:

$$
\langle \zeta_{\mathbf{k}} \zeta_{\mathbf{k}'} \rangle = (2\pi)^3 \delta^{(3)}(\mathbf{k} + \mathbf{k}') P(k)
$$

and the local bispectrum is:

$$
B_\zeta^{\rm local}(k_1, k_2, k_3) = \frac{6}{5} f_{\rm NL}^{\rm local} \left[ P(k_1) P(k_2) + \text{cyc.} \right]
$$

### The exact target:

**Compute B_zeta(k_1, k_2, k_3) for the matter bounce (w = 0, c_s = 1), then extract f_NL^local from:**

$$
f_{\rm NL}^{\rm local} = \frac{5}{6} \lim_{k_1 \to 0} \frac{B_\zeta(k_1, k, k)}{2 P(k_1) P(k)}
$$

This is the quantity Planck constrains at f_NL = -0.9 +/- 5.1.

---

## What This Is NOT

1. **NOT |B|_NL from Cai et al.** Their quantity |B|_NL is defined differently (Eq. 20-21 in their paper). We must convert to the Planck convention above.

2. **NOT the equilateral or folded amplitude.** We want the local (squeezed) limit specifically.

3. **NOT the full shape function.** We want the squeezed-limit coefficient, which is the leading contribution to the Planck local template.

4. **NOT f_NL^Phi.** We work directly with zeta, using the relation Phi = (3/5) zeta to verify conventions.

---

## What Must Equal What for the Flagship Claim to Be Valid

### The claim is: f_NL^local = -35/8 in the Planck convention.

This requires ALL of the following:

1. The matter-bounce bispectrum B_zeta, computed from the third-order action (or gradient expansion), gives a squeezed-limit amplitude with:

$$
\frac{5}{6} \frac{B_\zeta(k_1, k, k)}{2 P(k_1) P(k)} \bigg|_{k_1 \to 0} = -\frac{35}{8}
$$

2. The quantity on the left is the SAME f_NL^local that Planck reports.

3. The shape of B_zeta in non-squeezed configurations is sufficiently local-like that the template projection gives an effective f_NL close to the squeezed-limit value.

---

## Success Conditions

### Minimum success condition:
The squeezed-limit amplitude f_NL^local is NEGATIVE and O(1). The exact value may be -35/8 or -35/16 or -2.2 or something else, but it must be:
- Negative (opposite sign from standard inflation)
- |f_NL| > 1 (detectable by MegaMapper at sigma ~ 0.5)

If this holds, the matter bounce retains a hard-to-mimic discriminator.

### Strong success condition:
f_NL^local = -35/8 = -4.375 in the Planck convention, with the Li-Brandenberger discrepancy explained as a convention artifact or approximation error.

If this holds, MegaMapper detection at 8.75 sigma. The flagship claim is fully validated.

### Fatal failure condition:
Any of:
- f_NL^local is POSITIVE (same sign as inflation) -> no discrimination
- |f_NL| < 0.5 (undetectable by MegaMapper) -> no test
- The squeezed limit is not well-defined (IR divergence or pathology) -> no clean prediction
- The calculation reveals an error in Cai et al. that flips the sign

---

## The Four Quantities That Must Be Carefully Distinguished

| Quantity | What it is | What it's NOT |
|----------|-----------|---------------|
| Squeezed-limit B_zeta coefficient | The raw analytic amplitude at k_1 << k_2 ~ k_3 | Not the full shape |
| f_NL^local (Planck convention) | The coefficient in zeta = zeta_G + (3/5) f_NL zeta_G^2 | Not |B|_NL from Cai |
| Template-projected f_NL | What a survey actually measures by fitting the local template | May differ from squeezed-limit value |
| Shape function S(k_1,k_2,k_3) | The full k-dependent bispectrum shape | Contains more info than f_NL alone |

**Our primary target is #2.** We derive #1 and convert to #2. If the shape is sufficiently local, #3 approximately equals #2 and the prediction is sharp. If the shape deviates substantially from local, we need to also compute #3.
