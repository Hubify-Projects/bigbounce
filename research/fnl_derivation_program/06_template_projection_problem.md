# 06: The Template Projection Problem

**Created:** 2026-03-17
**Status:** COMPLETE

---

## The Problem

Cai et al. (2009) themselves state that the matter bounce bispectrum shape is "loosely local." Planck constrains the LOCAL template specifically. The squeezed-limit amplitude and the template-projected amplitude are NOT the same thing unless the shape is exactly local.

**Question:** Does the template projection give f_NL^eff = -35/8, or something different?

---

## What "Local" Means Precisely

### The local template:

$$
B_\zeta^{\rm local}(k_1, k_2, k_3) = \frac{6}{5} f_{\rm NL} \left[ P(k_1)P(k_2) + P(k_2)P(k_3) + P(k_3)P(k_1) \right]
$$

For scale-invariant P(k) = A/k^3 (where A = 2pi^2 A_s):

$$
B_\zeta^{\rm local} = \frac{6}{5} f_{\rm NL} A^2 \left[ \frac{1}{k_1^3 k_2^3} + \frac{1}{k_2^3 k_3^3} + \frac{1}{k_3^3 k_1^3} \right]
$$

### The squeezed limit (k_1 -> 0):

$$
B_\zeta^{\rm local}(k_1, k, k) \to \frac{12}{5} f_{\rm NL} \frac{A^2}{k_1^3 k^3}
$$

(The 1/(k_2^3 k_3^3) = 1/k^6 term is subdominant when k_1 << k.)

### The equilateral limit (k_1 = k_2 = k_3 = k):

$$
B_\zeta^{\rm local}(k, k, k) = \frac{18}{5} f_{\rm NL} \frac{A^2}{k^6}
$$

---

## What Cai et al. Find for the Shape

### Their shape function A_T(k_1, k_2, k_3):

From their Eq. (37), the dominant terms in A_T are:

$$
A_T \propto \left[ \text{terms with various powers of } k_i \right]
$$

### In the squeezed limit:

They find A_T dominated by terms scaling as k_1^2 k^4 (i.e., the long mode enters at order k_1^2, not k_1^0). This is the characteristic signature of the local shape — the bispectrum diverges as 1/(k_1^3) in the squeezed limit (after dividing by the mode function normalizations).

### In the equilateral limit:

They give |B|_NL^equil = -255/64 = -3.984.

Compare: for a purely local shape, the equilateral-to-squeezed ratio is:

$$
\frac{|B|_{\rm NL}^{\rm equil}}{|B|_{\rm NL}^{\rm sq}} = \frac{B^{\rm equil}(k,k,k) \cdot (k_1^3 + 2k^3)/3k^3}{B^{\rm sq}(k_1,k,k) \cdot (k_1^3 + 2k^3)/(k_1^3 + 2k^3)}
$$

This ratio depends on the normalization convention. For Cai et al.'s |B|_NL = (10/3) A_T / (sum k_i^3):

- Squeezed: |B|_NL = -35/8 = -4.375
- Equilateral: |B|_NL = -255/64 = -3.984

The ratio is 3.984/4.375 = 0.911.

For a PURE local shape, the equilateral amplitude in the |B|_NL normalization would be:

$$
|B|_{\rm NL}^{\rm equil, pure local} = \frac{10}{3} \cdot \frac{3/(k^6) \cdot (2\pi^2 A_s)^2 / [(2\pi)^4 \cdot 1/(k^2)^3 \cdot A_s^2]}{3k^3}
$$

Actually, let me compute this more carefully. For a pure local shape:

B^local(k,k,k) = (6/5) f_NL * 3 * P(k)^2 = (18/5) f_NL * (2pi^2 A_s / k^3)^2

In Cai's A_T normalization: B = (2pi)^4 A_s^2 A_T / (k^2)^3

So A_T^{local}(k,k,k) = [(18/5) f_NL * (2pi^2)^2 / k^6] * k^6 / [(2pi)^4] = (18/5) f_NL * (2pi^2)^2 / (2pi)^4 = (18/5) f_NL / 4

And |B|_NL^{equil, local} = (10/3) * (18/5) f_NL / (4 * 3k^3) * ...

This is getting messy because the exact conversion requires knowing Cai's A_T normalization precisely. Let me take the cleaner approach.

---

## The Clean Approach: Cosine Estimator

### Template projection definition:

The effective f_NL that Planck would measure is:

$$
f_{\rm NL}^{\rm eff} = f_{\rm NL}^{\rm sq} \times \cos(\theta)
$$

where theta is the angle between the matter bounce shape S_MB and the local template S_local in the bispectrum inner product:

$$
\cos(\theta) = \frac{\langle S_{\rm MB}, S_{\rm local} \rangle}{\sqrt{\langle S_{\rm MB}, S_{\rm MB} \rangle \langle S_{\rm local}, S_{\rm local} \rangle}}
$$

and the inner product is:

$$
\langle S_1, S_2 \rangle = \sum_{\rm triangles} \frac{S_1(k_1, k_2, k_3) S_2(k_1, k_2, k_3)}{P(k_1) P(k_2) P(k_3)}
$$

(The exact form of the sum/integral depends on the survey, but this is the standard Fisher-matrix form.)

### What we know:

- f_NL^sq = -35/8 (Cai et al. squeezed-limit value, to be verified)
- cos(theta) = unknown, but Cai says the shape is "loosely local"

### What "loosely local" implies:

For reference:
- cos(theta) = 1: shape is exactly local. f_NL^eff = f_NL^sq.
- cos(theta) = 0.95: shape is ~95% local. f_NL^eff = 0.95 * f_NL^sq.
- cos(theta) = 0.5: shape is half local. f_NL^eff = 0.5 * f_NL^sq. The MegaMapper significance drops from 8.75 sigma to 4.4 sigma.

### Literature data on the shape:

Cai et al. compute |B|_NL at two configurations:
- Squeezed: -35/8 = -4.375
- Equilateral: -255/64 = -3.984

The ratio equilateral/squeezed = 0.911.

For a PURE local shape:
B^local(k,k,k) / B^local(k_1->0, k, k) = (18/5) f_NL P^2 / [(12/5) f_NL P(k_1)P(k)]
= (3/2) * P(k)/P(k_1) * (k_1/k)^...

Hmm, this ratio depends on the specific k_1 used in the squeezed limit, making direct comparison difficult.

---

## Why This Matters for the Flagship Claim

### The optimistic case (cos(theta) > 0.9):

If the matter bounce shape is >90% local, then:
- f_NL^eff > 0.9 * (-35/8) = -3.94
- MegaMapper detection: |f_NL^eff| / 0.5 > 7.9 sigma
- The flagship claim is barely affected

### The pessimistic case (cos(theta) ~ 0.5-0.7):

If the shape has significant non-local components:
- f_NL^eff ~ 0.5 to 0.7 * (-35/8) = -2.2 to -3.1
- MegaMapper detection: 4.4 to 6.1 sigma
- Still detectable, but the claim "8.75 sigma" is overstated
- **This might also explain the Li-Brandenberger value of -2.19** — if their approximate formula effectively performs a template projection rather than a squeezed-limit extraction

### The fatal case (cos(theta) < 0.3):

If the shape is mostly non-local:
- f_NL^eff < 1.3
- Detection marginal or impossible
- The flagship claim collapses

---

## How to Compute the Template Projection

### Method 1: Analytic (approximate)

Use the full Cai et al. shape function A_T and compute the inner product analytically. This requires knowing A_T as a closed-form function of (k_1, k_2, k_3), which Cai et al. provide.

**Difficulty: MEDIUM.** The integrals over triangle space are non-trivial but standard.

### Method 2: Numerical (exact)

Numerically evaluate A_T on a grid of triangles and compute the inner product by numerical integration.

**Difficulty: LOW.** This is a straightforward numerical computation once A_T is coded.

### Method 3: Literature extraction

Find if anyone has computed the cosine between the matter bounce shape and the local template.

**Preliminary assessment:** No paper in the literature has done this explicitly. The closest is Fergusson & Shellard (2009, arXiv:0812.3413) who developed general decomposition methods, but they did not apply them to the matter bounce.

---

## The Specific Concern

### The matter bounce shape differs from local in two ways:

**1. Equilateral contamination.**

The cubic action has contact vertices (all three modes interacting at the same time) that produce equilateral-type contributions. These are NOT present in the local template. In inflation, these are slow-roll suppressed. In the matter bounce (epsilon = 3/2), they are O(1).

**2. Growing mode evolution.**

The growing mode causes the bispectrum to evolve after horizon crossing. This evolution may change the relative weights of different triangle configurations, shifting the shape.

### The saving grace:

In the squeezed limit, the bispectrum is dominated by the local-type contribution regardless of the full shape. This is because the squeezed limit probes the correlation between short and long modes, which is always local-type (consistency relation / separate-universe physics). The equilateral contamination is important only for non-squeezed configurations.

Since MegaMapper's f_NL sensitivity comes primarily from squeezed triangles, the effective f_NL may be close to the squeezed-limit value even if the full shape is not purely local.

---

## Priority Assessment

### For the derivation program:

The template projection is SECONDARY to getting the squeezed-limit value right. If the squeezed limit gives -35/8, the template projection can only REDUCE |f_NL^eff|, not increase it. The cosine factor is bounded: 0 < cos(theta) <= 1.

### Order of operations:

1. **FIRST:** Derive the squeezed-limit f_NL from scratch (Paths A and B)
2. **SECOND:** Compute the template projection to get f_NL^eff
3. **THIRD:** Assess MegaMapper significance using f_NL^eff

### Minimum requirement for the flagship claim:

The squeezed-limit f_NL must be |f_NL| > 2 (to survive a cosine factor of ~0.5 and still give MegaMapper detection above 2 sigma). If the squeezed-limit value is -35/8 = -4.375, there is ample margin.

---

## Connection to the Li-Brandenberger Discrepancy

### A speculative resolution:

Could the Li-Brandenberger value of -2.19 be the TEMPLATE-PROJECTED f_NL rather than the squeezed-limit value?

If cos(theta) ~ 0.5, then f_NL^eff = 0.5 * (-35/8) = -2.19.

This would mean:
- Cai et al. computed the squeezed-limit amplitude: -35/8
- Li & Brandenberger (effectively) computed the template-projected amplitude: -2.19
- Both are correct, but they measure different things

**This hypothesis is testable:** compute the template projection from the Cai et al. shape and check if it gives -2.19.

**Status:** SPECULATIVE. Must not bias the derivation.
