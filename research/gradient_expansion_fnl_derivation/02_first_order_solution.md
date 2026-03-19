# First-Order Long-Wavelength Solution

**Created:** 2026-03-18
**Status:** COMPLETE

---

## 1. The First-Order Equation

From file 01, the linearized superhorizon equation for zeta is:

$$
\ddot{\zeta}^{(1)} + \frac{2}{t}\dot{\zeta}^{(1)} = 0
$$

This is a second-order linear ODE in cosmic time t.

---

## 2. General Solution

This is an Euler-type equation. Try zeta^(1) = t^alpha:

alpha(alpha - 1) t^{alpha-2} + (2/t) alpha t^{alpha-1} = 0

alpha(alpha - 1) + 2 alpha = 0

alpha^2 + alpha = 0

alpha(alpha + 1) = 0

alpha = 0 or alpha = -1

**General solution:**

$$
\boxed{\zeta^{(1)}(t) = C_1 + \frac{C_2}{t}}
$$

### Mode identification:

- **C_1 mode (constant):** This is the standard adiabatic superhorizon mode. In expanding matter domination, this is the dominant (growing) mode. In contracting matter domination, it is the DECAYING mode (it is eventually overwhelmed by the C_2 mode).

- **C_2/t mode (growing in contraction):** Since t < 0 and t -> 0^-, we have |1/t| -> infinity. This mode GROWS during contraction. It is the mode responsible for the large non-Gaussianity.

### Time derivative:

$$
\dot{\zeta}^{(1)} = -\frac{C_2}{t^2}
$$

---

## 3. Verification Against the Conformal-Time Result

From the in-in program (file 01_power_spectrum_derivation), the superhorizon zeta in conformal time is:

$$
\zeta_k^{\rm super}(\eta) \propto \frac{1}{\eta^3}
$$

The relation between cosmic time and conformal time for matter contraction:

$$
dt = a\,d\eta = a_0(\eta/\eta_0)^2 d\eta
$$

$$
t = a_0\int\frac{\eta^2}{\eta_0^2}d\eta = \frac{a_0}{3\eta_0^2}\eta^3
$$

So eta^3 proportional to t, hence eta proportional to t^{1/3}.

Then zeta ~ 1/eta^3 ~ 1/t. **CONFIRMED:** The growing mode 1/t in cosmic time corresponds to 1/eta^3 in conformal time.

Also: the constant mode C_1 in cosmic time corresponds to a constant mode in conformal time. **Both modes match.**

---

## 4. The Growing Mode Dominance

During matter contraction, starting from some initial time t_i < 0 (with |t_i| >> |t_f|, i.e., the initial time is far from the bounce):

$$
\frac{\zeta^{(1)}_{\rm growing}(t_f)}{\zeta^{(1)}_{\rm constant}} = \frac{C_2/t_f}{C_1} = \frac{C_2}{C_1 t_f}
$$

As t_f -> 0^- (approaching the bounce), this ratio diverges. **The growing mode dominates.**

For modes that exit the Hubble radius during contraction, both C_1 and C_2 are set at horizon crossing. The ratio at a later time is:

$$
\frac{C_2/t}{C_1} \sim \frac{t_{\rm exit}}{t}
$$

where t_exit is the cosmic time at Hubble exit. Since |t| < |t_exit| during contraction (time moves from large negative to zero), this ratio exceeds unity and grows.

**For the bispectrum calculation, we work in the regime where the growing mode dominates: C_2/t >> C_1.** We set C_1 = 0 (or equivalently, C_1 is absorbed into a redefinition of the background). The relevant first-order solution is:

$$
\boxed{\zeta^{(1)}(t,\mathbf{x}) = \frac{C(\mathbf{x})}{t}}
$$

where C(x) is a spatially-varying amplitude set by the initial conditions at horizon crossing.

---

## 5. Physical Interpretation of the Growing Mode

### Why does zeta grow?

In the separate-universe picture, each patch evolves as an independent FRW universe. For dust (w = 0), the Friedmann equation gives:

$$
a_{\rm loc}(t) \propto (-t)^{2/3} \quad \text{(same power for all patches)}
$$

But different patches have different SPATIAL CURVATURE K. The Friedmann equation with curvature is:

$$
H_{\rm loc}^2 = \frac{\rho}{3M_{\rm Pl}^2} - \frac{K}{a_{\rm loc}^2}
$$

During contraction, a_loc shrinks, so the K/a^2 term GROWS relative to rho/(3 M_Pl^2). The spatial curvature becomes increasingly important. The growing zeta mode tracks this growing importance of spatial curvature.

Explicitly: zeta ~ K/(a^2 H^2) ~ K * t^2 / (t^{-4/3} * t^{-2}) = K * t^{4/3+2-2} ... let me compute this more carefully.

For a = a_0(-t/t_0)^{2/3}, H = 2/(3t):

K/(a^2 H^2) = K t_0^{4/3} / (a_0^2 (-t)^{4/3} * 4/(9t^2)) = 9K t_0^{4/3} / (4 a_0^2 (-t)^{4/3} * t^{-2})

= 9K t_0^{4/3} / (4 a_0^2) * t^2 / (-t)^{4/3} = 9K t_0^{4/3} / (4 a_0^2) * |t|^{2-4/3} = ... * |t|^{2/3}

So K/(a^2 H^2) ~ |t|^{2/3}, which GROWS as |t| -> infinity during contraction? That doesn't match.

Actually wait: during contraction, t < 0 and t goes from -infinity toward 0. So |t| DECREASES. Then K/(a^2 H^2) ~ |t|^{2/3} DECREASES during contraction. This contradicts the growing mode.

**Let me reconsider.** The spatial curvature contribution to the Friedmann equation is:

H^2 = rho/(3 M_Pl^2) - K/a^2

The fractional importance of curvature is |K|/(a^2 H^2). For matter domination: rho ~ a^{-3}, H^2 ~ a^{-3}, so a^2 H^2 ~ a^{-1} ~ (-t)^{-2/3}. Then:

K/(a^2 H^2) ~ K * (-t)^{2/3}

As t -> 0^- (contraction), (-t)^{2/3} -> 0. So curvature becomes LESS important as we approach the bounce? That contradicts the growing mode zeta ~ 1/t.

**The resolution:** zeta is NOT simply K/(a^2 H^2). The comoving curvature perturbation zeta measures the perturbation in the NUMBER OF E-FOLDS, not the fractional curvature. The growing zeta mode corresponds to the fact that patches with different spatial curvature reach a given density at DIFFERENT TIMES. As contraction proceeds, this time offset accumulates.

More precisely: consider two patches, one with curvature K and one without. They reach the same density rho at times t_1 and t_2, with t_2 - t_1 growing as contraction proceeds. The number of e-folds difference is:

delta N = H * delta t ~ (2/3t) * delta t

As t -> 0, H diverges, so even a small delta t gives a large delta N, hence a large zeta.

**This is the physical mechanism behind the growing mode.** It is specific to contraction and does not occur in expansion (where H decreases and time offsets shrink in significance).

---

## 6. Normalization from Quantum Vacuum

The amplitude C(x) is set by matching to the quantum vacuum at horizon crossing. For a mode with comoving wavenumber k:

At horizon crossing (k = aH), t_k satisfies k = a(t_k) * |H(t_k)| = a_0 (-t_k/t_0)^{2/3} * 2/(3|t_k|).

The quantum vacuum gives:

$$
C_k = \frac{i}{A\sqrt{2k^3}} \cdot t_k
$$

where A = a_0 sqrt(3)/eta_0^2 is the normalization from the Mukhanov-Sasaki variable (from the in-in program, file 01).

This normalization will cancel in the ratio f_NL = (5/6) zeta^(2)/[zeta^(1)]^2, so we do not need its explicit form.

---

## 7. Power Spectrum of the Growing Mode

$$
P_\zeta^{(1)}(k, t) = \frac{k^3}{2\pi^2}|C_k|^2 / t^2
$$

This is:
- Scale-invariant (n_s = 1) because |C_k|^2 ~ 1/k^3 from the quantum vacuum normalization
- Time-dependent: grows as 1/t^2 (the growing mode squared)

This matches the in-in result: P_zeta ~ 1/eta^6 ~ 1/t^2. **CONFIRMED.**

---

## 8. Key Result for the Second-Order Calculation

The first-order solution and its time derivative:

$$
\zeta^{(1)}(t,\mathbf{x}) = \frac{C(\mathbf{x})}{t}
$$

$$
\dot{\zeta}^{(1)}(t,\mathbf{x}) = -\frac{C(\mathbf{x})}{t^2}
$$

The second-order source:

$$
S^{(2)}(t,\mathbf{x}) = -3\left(\dot{\zeta}^{(1)}\right)^2 = -3\frac{C(\mathbf{x})^2}{t^4}
$$

The second-order equation to solve is:

$$
\boxed{\ddot{\zeta}^{(2)} + \frac{2}{t}\dot{\zeta}^{(2)} = -\frac{3\,C(\mathbf{x})^2}{t^4}}
$$

This is a second-order inhomogeneous ODE with a known source. The solution is obtained in the next file.

---

## 9. Assumption Inventory at This Stage

| Item | Status | Note |
|------|--------|------|
| First-order equation from gradient expansion | DERIVED | From Einstein equations + w=0 + superhorizon |
| Growing mode zeta ~ 1/t | DERIVED | Exact analytic solution |
| Consistency with conformal-time result (1/eta^3) | VERIFIED | t proportional to eta^3 |
| Consistency with power spectrum (scale-invariant) | VERIFIED | Matches in-in program |
| Growing mode dominance over constant mode | DERIVED | Follows from t -> 0^- during contraction |
| Source term -3(dot{zeta}^(1))^2 for second order | DERIVED | From perturbative expansion of nonlinear equation |
| Spatial gradient contributions to source | NOT YET ASSESSED | See file 03 |

**The first-order solution is rigorous and independently confirmed against the in-in approach. The second-order source is algebraically determined. What remains is solving the second-order equation and assessing whether spatial gradient terms contribute additional sources.**
