# 03: Literature Discrepancy Map

**Created:** 2026-03-17
**Status:** COMPLETE

---

## The Three Discrepant Values

| Source | Claimed f_NL | Year | Method |
|--------|-------------|------|--------|
| Cai, Xue, Brandenberger, Zhang | -35/8 = -4.375 | 2009 | In-in (Maldacena cubic action) |
| Quintin, Sherkatghanad, Cai, Brandenberger (citing Cai 2009) | -35/16 = -2.1875 | 2015 | Citation of Cai et al. |
| Li & Brandenberger (generalized formula at c_s = 1) | ~-2.19 | 2016 | In-in with general c_s |

---

## Source 1: Cai et al. (2009), arXiv:0903.0631

### What they compute:
A shape function A_T(k_1, k_2, k_3) from the Maldacena cubic action, evaluated for a canonical scalar field in matter-dominated contraction (epsilon = 3/2, c_s = 1).

### Their normalization:
They define |B|_NL via:
$$
|B|_{\rm NL}(k_1, k_2, k_3) = \frac{10}{3} \frac{A_T(k_1, k_2, k_3)}{\sum_i k_i^3}
$$

### Their result in the squeezed limit:
|B|_NL^local = -35/8 (their Eq. 38-39)

### Their statement about relationship to f_NL^local:
"If our predicted shape were exactly local (which it is not), then the above amplitude would equal the famous f_NL^local parameter. Since the matter bounce model predicts a shape which is loosely local, one can loosely speaking phrase our prediction as f_NL^local = -35/8."

### Critical observation:
**|B|_NL is NOT necessarily f_NL^local in the Planck convention.** The normalization by sum(k_i^3) is different from the standard local template normalization by P(k_1)P(k_2) + cyc. These COINCIDE only if the shape is exactly local.

### Gauge:
Comoving gauge (zeta as the perturbation variable).

### Background:
Exact w = 0, a(eta) proportional to eta^2, epsilon = 3/2.

### What could produce the discrepancy:
The identification |B|_NL = f_NL^local assumes the shape is purely local. If the matter bounce shape has non-local components (which Cai et al. acknowledge), |B|_NL in the squeezed limit and the template-projected f_NL^local could differ. However, for a genuinely squeezed configuration (k_1 << k_2 ~ k_3), the local template dominates and the identification should be approximately correct.

---

## Source 2: Quintin et al. (2015), arXiv:1508.04141

### What they cite:
They cite Cai et al. (2009) for the pre-bounce f_NL value. Their quoted value appears to be -35/16 (based on agent research), but this needs direct verification.

### Possible explanation for factor-of-2:
1. **Confusion between |B|_NL and a differently-normalized f_NL.** If Quintin uses a convention where f_NL is defined without the (3/5) factor [i.e., zeta = zeta_G + f_NL zeta_G^2 instead of zeta = zeta_G + (3/5) f_NL zeta_G^2], then f_NL^Quintin = (3/5) * (-35/8) = -21/8 = -2.625. This doesn't match -35/16 = -2.1875 either.

2. **Confusion between local and equilateral amplitudes.** Cai et al. give the equilateral amplitude as -255/64 = -3.984. Half of -35/8 = -35/16 = -2.1875. This exact factor-of-2 relationship suggests Quintin might have taken the ratio in a different triangle configuration.

3. **Typo or citation error.** The simplest explanation: -35/16 is a misprint of -35/8 (16 vs 8 — easy to confuse in handwritten notes).

### Resolution needed:
**Read the actual Quintin et al. paper and find the exact quoted value and context.** The factor-of-2 may be a citation error rather than a physics disagreement.

### Priority: MEDIUM
If this is a citation error, it does not affect the physics. It only matters if Quintin actually rederived the result and got a different answer.

---

## Source 3: Li & Brandenberger (2016), arXiv:1612.02036

### What they compute:
The bispectrum for a GENERALIZED matter bounce with arbitrary sound speed c_s, using the Maldacena cubic action with the DBI/k-essence modification.

### Their formula:
$$
f_{\rm NL} \sim -\frac{165}{16} + \frac{65}{8 c_s^2}
$$

### At c_s = 1:
$$
f_{\rm NL} \sim -\frac{165}{16} + \frac{65}{8} = -10.3125 + 8.125 = -2.1875
$$

### Critical observations:

**1. The "~" (approximately equal) sign.** Li & Brandenberger explicitly use an approximation symbol, not an equality. This means their formula may drop terms that are important at c_s = 1.

**2. Their formula may be optimized for c_s << 1.** In the DBI/k-essence context, the interesting regime is c_s << 1 where the 65/(8 c_s^2) term dominates. The -165/16 constant may be an approximate fit to the c_s = 1 limit rather than an exact evaluation.

**3. The structure of the formula.** The terms -165/16 and +65/8 must come from different vertices in the cubic action. At c_s = 1, these two terms nearly cancel (-10.31 + 8.13 = -2.19), so the result is sensitive to the exact coefficient of each term. Even a small approximation error in either coefficient could shift the answer significantly.

**4. At c_s = 1, the k-essence cubic action should reduce to the canonical cubic action.** If Li & Brandenberger's calculation is exact, it must reproduce Cai et al. at c_s = 1. The fact that it doesn't (-2.19 vs -4.375) means either:
   - (a) One of the two calculations has an error
   - (b) The approximation in Li & Brandenberger's formula is significant at c_s = 1
   - (c) They compute different quantities

### Gauge:
Comoving gauge (same as Cai et al.).

### Background:
Power-law contraction with epsilon = 3(1+w)/2 and general c_s.

### What could produce the discrepancy:

**Hypothesis A (approximation):** The Li-Brandenberger formula is derived in the limit c_s << 1 and extrapolated to c_s = 1. Terms that are subleading at small c_s may be O(1) at c_s = 1. In this case, Cai et al. -35/8 is the correct c_s = 1 value and the discrepancy is explained.

**Hypothesis B (error in Cai):** Li & Brandenberger's full calculation is correct at c_s = 1, and Cai et al. made an error in their cubic action or time integrals. In this case, -2.19 is the correct value.

**Hypothesis C (different quantities):** The two papers extract f_NL using different normalizations. If |B|_NL from Cai is NOT the same as f_NL from Li-Brandenberger, the discrepancy is a normalization mismatch, not a physics disagreement.

### Resolution strategy:
Compute f_NL directly from the locked conventions (file 02), bypassing both intermediate notations. If the direct computation gives -35/8, Hypothesis A is correct. If it gives -2.19, Hypothesis B is correct. If it gives something else, both have issues.

### Priority: HIGH
This is the main discrepancy that must be resolved by our derivation.

---

## Secondary References

### Brandenberger & Peter (2017), arXiv:1603.05834 (review)
Quotes f_NL = -35/8 from Cai et al. without independent verification. Not helpful for resolving the discrepancy.

### Wilson-Ewing (2013), arXiv:1211.6269
Does NOT compute f_NL. Focuses on the power spectrum only. States that extension to higher-order perturbation theory is needed.

### Our own earlier calculation (branch_V files)
Got f_NL = 5/12. This is WRONG — used inflationary delta-N formulas that don't apply to the matter bounce because zeta grows on superhorizon scales.

---

## Discrepancy Summary

| Source | Value | Method | Convention clear? | Independent calc? |
|--------|-------|--------|------------------|------------------|
| Cai et al. | -35/8 | In-in, direct | Custom |B|_NL, approximately = f_NL | YES (original) |
| Quintin et al. | -35/16 (?) | Citation | Unclear | NO (citation only) |
| Li & Brandenberger | ~-2.19 | In-in, general c_s | Approximate ("~") | YES (independent) |
| Our branch_V | 5/12 | Delta-N | Wrong method | YES but WRONG |

**There are only TWO independent calculations: Cai et al. and Li & Brandenberger. They disagree by a factor of 2. The Quintin value is likely a citation artifact. Our branch_V value was a methodological error.**

---

## Most Likely Resolution

Based on the structure of the discrepancy:

**Working hypothesis: Li & Brandenberger's formula is approximate at c_s = 1, and the true value is closer to Cai et al.'s -35/8.**

Reasoning:
1. The Li-Brandenberger formula uses "~", signaling approximation
2. At c_s = 1, two large terms nearly cancel (-10.31 + 8.13), making the result sensitive to small errors
3. Cai et al. compute at c_s = 1 directly, with no c_s-dependent approximation
4. The Cai et al. paper has been cited hundreds of times with the -35/8 value and no published correction

**But this is a HYPOTHESIS, not a conclusion. The derivation must determine the truth.**
