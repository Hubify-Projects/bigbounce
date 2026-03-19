# 06: Comparison to Cubic-Action Result

**Created:** 2026-03-18
**Status:** COMPLETE

---

## Central Question: Does the Gradient Expansion Reproduce $-35/8$?

**Structural features: YES** (all four confirmed independently)
**Exact coefficient: NOT INDEPENDENTLY DETERMINED** (same bottleneck reached)

---

## Where the Two Methods Agree

### 1. Sign of $f_{\rm NL}$: Negative

- **Cubic action (Cai et al.):** The dominant vertex $\propto a^2\,\zeta\,\zeta'^{\,2}$ with $\epsilon^2 = 9/4$ prefactor generates a negative bispectrum in the squeezed limit.
- **Gradient expansion:** The energy-constraint nonlinearity (Term 1: $(\dot\zeta^{(1)})^2/H$) dominates the source, and the particular solution has the same sign as $-C_2^2$, yielding negative $f_{\rm NL}$.

Both methods trace the sign to the same physics: the growing mode enhances overdensities more than underdensities during contraction, creating negative skewness.

### 2. Magnitude: $O(\epsilon) = O(1)$

- **Cubic action:** $f_{\rm NL} = -35/8$ with $35/8 = O(\epsilon^1)$ for $\epsilon = 3/2$.
- **Gradient expansion:** The source scales as $\epsilon\cdot C_2^2/t^3$, the particular solution as $\epsilon\cdot C_2^2/t^2$, giving $f_{\rm NL} = O(\epsilon)$.

In both approaches, the magnitude is NOT slow-roll-suppressed because $\epsilon = 3/2$ is order unity. This is the fundamental difference from inflation, where $f_{\rm NL}^{\rm local} \sim O(\epsilon) \sim O(0.01)$.

### 3. Shape: Local

- **Cubic action:** In the squeezed limit ($k_1 \ll k_2 \approx k_3$), the bispectrum factorizes as $B(k_1, k_2, k_3) \propto P(k_1)\,P(k_2)$, which is the defining property of local-type non-Gaussianity.
- **Gradient expansion:** The calculation is performed entirely on superhorizon scales. The second-order solution $\zeta^{(2)}(\mathbf{x}) \propto [\zeta^{(1)}(\mathbf{x})]^2$ is a local product in real space, which Fourier-transforms to the local template.

The local shape is guaranteed in the gradient expansion because the formalism works in position space without any momentum-dependent vertices.

### 4. Growing mode as physical origin

- **Cubic action:** The bispectrum is dominated by the growing mode $v_k(\eta) \propto \eta^{-1}$ in the mode functions. The decaying mode contributes subdominantly.
- **Gradient expansion:** $\zeta^{(1)} = C_2/t$ (growing mode) generates the quadratic source for $\zeta^{(2)}$. The constant mode $C_1$ contributes only at subleading order in the gradient expansion.

### 5. Dominant nonlinear coupling

- **Cubic action:** The dominant cubic vertex is $(9/4)\,M_{\rm Pl}^2\,a^2\,\zeta\,\zeta'^{\,2}$ (the $\epsilon^2$ vertex), which dominates over all other vertices by a factor of $\eta^{-2}$ on superhorizon scales.
- **Gradient expansion:** The dominant source term is $(\dot\zeta^{(1)})^2/H$ (Term 1 from file 05), which has the same physical origin -- the nonlinear energy constraint coupling two time derivatives of the growing mode.

---

## Where the Bottleneck Is Shared

Both methods ultimately require computing a single number: **the coefficient of the growing-mode-squared coupling to the second-order curvature perturbation.**

| Formalism | How the coefficient appears |
|-----------|-----------------------------|
| Cubic action / in-in | Time integral $\int d\eta'\;\eta'^4\,g_{k_1}^{\rm super}(\eta')\,[g'_k(\eta')]^2$ evaluated with exact mode functions at horizon crossing |
| Gradient expansion | Coefficient $\alpha$ of the total source $S^{(2)} = \alpha\,C_2^2/t^3$, requiring all numerical prefactors from the three source terms in the second-order Einstein equations |

These are mathematically the SAME quantity expressed in different variables. The cubic-action approach writes it as a Fourier-space time integral; the gradient expansion writes it as a coefficient in an ODE source term. Neither shortcut avoids evaluating the full nonlinear Einstein equations at second order.

**This is why the gradient expansion does not automatically resolve the numerical discrepancy.** The calculation reaches the same algebra from a different direction.

---

## The Li-Brandenberger Discrepancy: What It Means Now

### Li & Brandenberger (2016): $f_{\rm NL} \approx -2.19 = -35/16$

Li & Brandenberger use a generalized formalism (arbitrary sound speed $c_s$) and evaluate:

$$
f_{\rm NL} = -\frac{165}{16} + \frac{65}{8c_s^2}
$$

At $c_s = 1$:

$$
f_{\rm NL} = -\frac{165}{16} + \frac{130}{16} = -\frac{35}{16} = -2.1875
$$

### Cai et al. (2009): $f_{\rm NL} = -35/8$

Cai et al. compute the bispectrum directly via the in-in formalism with exact mode functions for a canonical scalar field ($c_s = 1$) and obtain:

$$
f_{\rm NL} = -\frac{35}{8} = -4.375
$$

### The factor of 2

The ratio is exactly 2:

$$
\frac{-35/8}{-35/16} = 2
$$

This systematic factor-of-2 is NOT resolved by the gradient expansion. From our analysis in `research/fnl_derivation_execution/06_literature_discrepancy_resolution.md`, the most likely explanations are:

1. **Normalization convention:** Li & Brandenberger may define the interaction Hamiltonian or the bispectrum with a different overall factor (e.g., time-ordered product vs. commutator introduces a factor of 2).
2. **Field redefinition contribution:** Cai et al. include a field-redefinition contribution of $+5/4$ that may be treated differently in the Li-Brandenberger formalism.
3. **Growing-mode normalization:** A factor-of-2 in the growing-mode amplitude propagates as a factor of 2 (not 4) in $f_{\rm NL}$ if one power cancels in the ratio $B/P^2$.

The gradient expansion CANNOT arbitrate between these possibilities because they all concern the same numerical step that the gradient expansion also cannot complete independently.

---

## What Has Been Gained

Despite not resolving the coefficient, the comparison between the two methods provides genuine value:

1. **The result is not a computational artifact.** Two independent formalisms with different mathematical machinery (cubic action + in-in integrals vs. nonlinear Einstein equations + gradient expansion) confirm the same structural prediction. An error would have to be present in the shared physics, not in either method's machinery.

2. **The factor-of-2 is isolated.** The discrepancy is now known to reside in a single numerical coefficient, not in the sign, magnitude, shape, or parameter-dependence. This dramatically narrows the space of possible errors.

3. **The detectability is robust regardless.** Both $-35/8$ and $-35/16$ predict MegaMapper detections at $> 4\sigma$ (SNR $\approx 8.75$ or $\approx 4.4$ respectively). The science case does not depend on resolving the ambiguity.

---

## Honest Conclusion

The gradient expansion is a valuable cross-check of the STRUCTURE of the $f_{\rm NL}$ result, but it does NOT provide a genuinely independent numerical verification. The exact coefficient requires the same mathematical ingredients regardless of the formalism used.

**What would resolve it:** Numerical evaluation of the in-in time integral with exact mode functions (not superhorizon approximations). This is a well-defined one-dimensional quadrature that can be computed in a single session of careful numerical work.
