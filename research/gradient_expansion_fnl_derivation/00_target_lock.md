# Target Lock: Independent f_NL Derivation via Gradient Expansion

**Created:** 2026-03-18
**Status:** LOCKED

---

## Observable Target

f_NL^local in the Planck convention:

$$
\Phi(\mathbf{x}) = \Phi_G(\mathbf{x}) + f_{\rm NL}\left[\Phi_G(\mathbf{x})^2 - \langle\Phi_G^2\rangle\right]
$$

where Phi = (3/5)zeta on superhorizon scales (matter domination), giving:

$$
\zeta = \zeta^{(1)} + \frac{3}{5}f_{\rm NL}\left[\zeta^{(1)}\right]^2
$$

or equivalently:

$$
f_{\rm NL} = \frac{5}{6}\frac{\zeta^{(2)}}{\left[\zeta^{(1)}\right]^2}
$$

where ζ = ζ^(1) + (1/2)ζ^(2) + ... is the perturbative expansion, so ζ = ζ^(1) + (3/5)f_NL [ζ^(1)]^2 implies (1/2)ζ^(2) = (3/5)f_NL [ζ^(1)]^2, hence f_NL = (5/6) ζ^(2)/[ζ^(1)]^2.

**Convention check:** This is the SAME f_NL locked in the in-in derivation program (file 02_notation_and_convention_lock.md). No additional conversion factor.

---

## Model Assumptions

- **Background:** Matter contraction, w = 0 exactly (dust)
- **Scale factor:** a(t) = a_0(-t/t_0)^{2/3} for t < 0 (contraction toward t = 0)
- **Hubble:** H = 2/(3t) < 0 during contraction
- **Slow-roll parameter:** epsilon = -H_dot/H^2 = 3/2 (NOT small; this is matter domination)
- **Scalar field:** Canonical massive scalar phi with V = (1/2)m^2 phi^2 providing the matter content
- **Perturbation variable:** Comoving curvature perturbation zeta (gauge-invariant)
- **Regime:** Long-wavelength (gradient expansion), superhorizon modes k << aH

These are identical to the assumptions in the in-in program. The ONLY difference is the method of calculating f_NL.

---

## What Counts As Success

| Outcome | Interpretation | Impact |
|---------|---------------|--------|
| f_NL = -35/8 = -4.375 | Confirms Cai et al. (2009) | Full validation; MegaMapper 8.75-sigma detection |
| f_NL = -35/16 = -2.1875 | Supports Li & Brandenberger (2016) | Factor-of-2 discrepancy in Cai et al.; MegaMapper ~4.4-sigma |
| f_NL negative, O(1), but neither value | New result | Requires reconciliation between all three methods |
| Calculation bottlenecks at coefficient | Partial result | Confirms structural features (sign, order, shape) but not exact value |

**Minimum success condition:** The gradient expansion independently confirms that f_NL is (i) negative, (ii) O(1) not O(epsilon), (iii) parameter-free (depends only on w = 0), and (iv) local-type. All four structural features are independently testable even if the exact coefficient remains ambiguous.

**Strong success condition:** The exact numerical coefficient is determined, resolving the -35/8 vs -35/16 discrepancy.

---

## Why This Is a Genuinely Independent Derivation

### The in-in / cubic-action approach (Cai et al.):
1. Expands the action S[zeta] to third order in zeta
2. Identifies cubic interaction vertices (6 terms at epsilon = 3/2)
3. Computes the three-point function via the Schwinger-Keldysh (in-in) path integral
4. Takes the squeezed limit and extracts f_NL from B/(P*P)
5. **Key objects:** Cubic Lagrangian L_3, in-in time integral, mode functions v_k(eta)

### The gradient-expansion / Salopek-Bond approach (this derivation):
1. Writes the FULL nonlinear Einstein equations (no action expansion)
2. Applies the gradient expansion: drop spatial derivatives (long-wavelength limit)
3. Solves the resulting nonlinear ODE order by order in perturbation theory
4. First order: recovers the linear growing mode zeta^(1) ~ 1/t
5. Second order: solves the SOURCED equation for zeta^(2), where the source is quadratic in zeta^(1)
6. Extracts f_NL directly from zeta^(2)/[zeta^(1)]^2
7. **Key objects:** Nonlinear constraint equations, second-order source terms, Green's function

### What is shared:
- The same background (w = 0 matter contraction)
- The same perturbation variable (comoving curvature perturbation zeta)
- The same physical regime (superhorizon)
- The same f_NL convention

### What is NOT shared:
- The cubic action is never constructed in the gradient expansion
- No in-in time integrals are needed
- No mode functions in Fourier space are needed (the calculation is purely in real/coordinate space)
- The gradient expansion works directly with the nonlinear Einstein equations

**Agreement between the two methods would constitute a strong cross-check.** Disagreement would indicate an error in one or both approaches.

---

## The Physical Origin of Large f_NL in Matter Contraction

The standard delta-N formalism gives f_NL ~ O(epsilon) ~ O(1) for matter domination, but this misses the growing mode. The correct story:

1. During matter contraction, zeta has a GROWING mode: zeta ~ 1/t ~ a^{-3/2}
2. This growing mode dominates over the constant mode by a factor (a_exit/a_eval)^{3/2} >> 1
3. The growing mode self-interacts nonlinearly: zeta^(2) ~ (zeta^(1))^2 with an O(1) coefficient
4. The coefficient is NOT slow-roll-suppressed because epsilon = 3/2 (not small)
5. The resulting f_NL is O(1), negative, and parameter-free

The delta-N formalism FAILS here because it assumes zeta is constant on superhorizon scales (the "separate universe conservation"). This is violated by the growing mode.

The gradient expansion SUCCEEDS because it tracks the full nonlinear superhorizon evolution, including the growing mode, without assuming conservation of zeta.

---

## Relationship to Existing Literature

| Reference | Method | Result |
|-----------|--------|--------|
| Cai, Xue, Brandenberger, Zhang (2009) | In-in / cubic action | f_NL = -35/8 |
| Li & Brandenberger (2016) | In-in / cubic action (general c_s) | f_NL ~ -2.19 at c_s = 1 |
| Salopek & Bond (1990) | Gradient expansion (inflation) | f_NL ~ O(epsilon) for slow-roll |
| Wands et al. (2000); Lyth & Rodriguez (2005) | delta-N formalism | f_NL = -(5/6)(n_s - 1) for single-field |
| **This derivation** | Gradient expansion (matter contraction) | **To be determined** |

No one has applied the Salopek-Bond gradient expansion to matter contraction with the growing mode. This is genuinely new.
