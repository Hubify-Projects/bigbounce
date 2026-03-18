# 00: Execution Target Lock

**Status:** LOCKED

---

## Five Distinct Quantities

### Q1: Raw Bispectrum Coefficient

The full three-point function B_zeta(k_1, k_2, k_3) as a function of the three momenta, computed from the cubic action in matter-dominated contraction (w = 0, epsilon = 3/2, c_s = 1).

This is the shape function. It contains ALL information about the non-Gaussianity.

### Q2: Squeezed-Limit Coefficient

The limit of B_zeta as k_1 -> 0 with k_2 = k_3 = k:

$$
B_\zeta^{\rm sq}(k_1, k, k) = F_{\rm sq} \cdot P(k_1) P(k)
$$

where F_sq is a pure number (if scale-invariant). This is what Cai et al. call |B|_NL after their normalization.

### Q3: Exact Local-Template Amplitude (Squeezed-Limit f_NL)

$$
f_{\rm NL}^{\rm sq} = \frac{5}{12} F_{\rm sq}
$$

This is the f_NL extracted by applying our locked Planck-convention formula to the squeezed-limit bispectrum. It equals f_NL^local ONLY if the shape is exactly local.

### Q4: Template-Projected Effective Amplitude

$$
f_{\rm NL}^{\rm eff} = f_{\rm NL}^{\rm sq} \times \cos(\theta)
$$

where cos(theta) is the overlap between the full matter-bounce shape and the local template in the standard Fisher inner product. This is what a matched-filter analysis (Planck, MegaMapper) actually measures.

### Q5: Forecast-Relevant Observable

$$
\text{SNR} = \frac{|f_{\rm NL}^{\rm eff}|}{\sigma(f_{\rm NL}^{\rm local})}
$$

with sigma = 5.0 (Planck), sigma = 0.5 (MegaMapper).

---

## What Counts As

### CONFIRMED (strong success)
- Q3 gives f_NL^sq = -35/8 = -4.375
- Q4 gives |f_NL^eff| > 3 (cos(theta) > 0.7)
- Q5 gives MegaMapper SNR > 6

### WEAKENED (still usable)
- Q3 gives -4.4 < f_NL^sq < -1.5
- Q4 gives 1.0 < |f_NL^eff| < 3.0
- Q5 gives MegaMapper SNR = 2 to 6

### FATAL
- Q3 gives f_NL^sq > 0 (wrong sign)
- Q4 gives |f_NL^eff| < 0.5
- Q5 gives MegaMapper SNR < 1
- Or: f_NL depends on eta_f (not a prediction)

---

## This Execution Phase Targets Q1 through Q4

Q5 is a direct calculation from Q4 and requires no new physics.
