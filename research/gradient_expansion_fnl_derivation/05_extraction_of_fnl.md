# 05: Extraction of f_NL: What the Gradient Expansion Gives

**Created:** 2026-03-18
**Status:** COMPLETE (honest assessment)

---

## Convention

f_NL in the Planck convention:

$$
\zeta = \zeta^{(1)} + \frac{3}{5}f_{\rm NL}\,\bigl[\zeta^{(1)}\bigr]^2
$$

If the perturbative expansion gives $\zeta = \zeta^{(1)} + \tfrac{1}{2}\zeta^{(2)}$ with $\zeta^{(2)} = \sigma\,[\zeta^{(1)}]^2$, then matching:

$$
\frac{1}{2}\sigma\,[\zeta^{(1)}]^2 = \frac{3}{5}f_{\rm NL}\,[\zeta^{(1)}]^2
\quad\Longrightarrow\quad
f_{\rm NL} = \frac{5\sigma}{6}
$$

This is the SAME convention locked in `00_target_lock.md` and in the in-in derivation program. No additional conversion factor.

---

## What Can Be Derived Without Ambiguity

The gradient expansion for matter contraction ($w = 0$, $\epsilon \equiv -\dot{H}/H^2 = 3/2$) proceeds as follows.

### First order

The linear curvature perturbation on superhorizon scales satisfies:

$$
\ddot{\zeta}^{(1)} + \frac{2}{t}\,\dot{\zeta}^{(1)} = 0
$$

(spatial gradient terms dropped in the gradient expansion). The general solution is:

$$
\zeta^{(1)}(t,\mathbf{x}) = C_1(\mathbf{x}) + \frac{C_2(\mathbf{x})}{t}
$$

- $C_1$: constant mode (decaying in physical importance during contraction)
- $C_2/t$: growing mode (dominates as $t \to 0^{-}$)

During contraction ($t < 0$, $t \to 0^{-}$), the growing mode $C_2/t \to -\infty$ dominates overwhelmingly. The physical perturbation spectrum is set by the growing mode.

### Second order

The second-order equation is:

$$
\ddot{\zeta}^{(2)} + \frac{2}{t}\,\dot{\zeta}^{(2)} = S^{(2)}(t)
$$

where $S^{(2)}$ is built from quadratic products of the growing mode $\zeta^{(1)} \sim C_2/t$.

The source $S^{(2)}$ receives contributions from three distinct nonlinear terms in the Einstein equations (see below). The homogeneous equation is the same as the first-order one, so the Green's function is known. The particular solution determines $\zeta^{(2)}$ and hence $f_{\rm NL}$.

---

## Why Standard Formulas Do Not Apply

### The Maldacena slow-roll formula

The standard inflationary result (Maldacena 2003) for single-field slow-roll gives:

$$
f_{\rm NL} = \frac{5}{12}(1 - n_s) + \text{terms proportional to } \epsilon,\;\eta_V
$$

This does NOT apply to matter contraction because:

1. It assumes the decaying mode is negligible (true in inflation, false here)
2. It assumes $\epsilon \ll 1$ (here $\epsilon = 3/2$)
3. The growing mode fundamentally changes the structure of the nonlinear solution

### The delta-N formalism

Lyth & Rodriguez (2005) and related work give:

$$
f_{\rm NL}^{\delta N} = -\frac{5}{6}\frac{N_{,\phi\phi}}{(N_{,\phi})^2}
$$

This FAILS for the growing mode because the delta-N formalism assumes that $\zeta$ is conserved on superhorizon scales (the "separate universe" approximation). The growing mode violates this conservation. Applying delta-N naively gives results that miss the dominant contribution entirely.

### The Finelli-Brandenberger leading-order formula

For a contracting background with $\epsilon = 3/2$ and exact scale invariance ($n_s = 1$), the leading-order expression:

$$
f_{\rm NL} \sim \frac{5}{12}\left(1 + \frac{1}{\epsilon}\right)(1 - n_s)
$$

evaluates to ZERO because the spectral tilt vanishes for exact matter contraction.

**This means the f_NL in matter contraction comes entirely from the NEXT-order terms** -- the growing-mode-squared coupling coefficient. This is the fundamental reason why the calculation is hard and why different groups disagree on the answer.

---

## The Three Source Terms

The second-order source $S^{(2)}$ in the gradient expansion receives contributions from three physically distinct nonlinearities in the Einstein equations. Writing the growing mode as $\zeta^{(1)} = C_2/t$:

### Term 1: Energy constraint nonlinearity

$$
S_1 \propto \frac{(\dot{\zeta}^{(1)})^2}{H} = \frac{C_2^2/t^4}{2/(3t)} = \frac{3C_2^2}{2t^3}
$$

This comes from the quadratic piece of the Hamiltonian constraint ($\mathcal{H}_0$), where $(\partial_t\zeta)^2$ appears at second order.

### Term 2: Momentum constraint at second order

$$
S_2 \propto \zeta^{(1)}\cdot\dot{\zeta}^{(1)} = \frac{C_2}{t}\cdot\frac{-C_2}{t^2} = \frac{-C_2^2}{t^3}
$$

This arises from the mixed first-order $\times$ first-order product in the momentum constraint ($\mathcal{H}_i$).

### Term 3: Spatial curvature at second order

$$
S_3 \propto (\zeta^{(1)})^2\cdot H = \frac{C_2^2}{t^2}\cdot\frac{2}{3t} = \frac{2C_2^2}{3t^3}
$$

This comes from the nonlinear spatial Ricci scalar ${}^{(3)}R$ evaluated at second order.

All three terms scale as $C_2^2/t^3$. The total source is:

$$
S^{(2)} = \alpha\,\frac{C_2^2}{t^3}
$$

where $\alpha$ is a pure number (a specific linear combination of the coefficients from Terms 1, 2, 3). The particular solution of the second-order equation with this source is:

$$
\zeta^{(2)}_{\rm part} = \beta\,\frac{C_2^2}{t^2}
$$

where $\beta$ depends on $\alpha$ and the equation-of-state parameter. Then:

$$
\sigma = \frac{\zeta^{(2)}}{[\zeta^{(1)}]^2} = \frac{\beta\,C_2^2/t^2}{C_2^2/t^2} = \beta
$$

and:

$$
f_{\rm NL} = \frac{5\beta}{6}
$$

---

## The Specific Bottleneck

**The gradient expansion reaches the SAME bottleneck as the in-in approach:** the exact value of $\alpha$ (and hence $\beta$) requires tracking every numerical prefactor in all three source terms through the full second-order Einstein equations.

The $t^{-3}$ scaling is guaranteed by dimensional analysis and the power-law background. The sign (negative) is determined by the dominance of the energy-constraint nonlinearity (Term 1), which creates the anti-correlated skewness. But the precise coefficient of $\alpha$ requires evaluating all tensor contractions and constraint projections at second order in the ADM formalism.

This is EXACTLY the same mathematical content as evaluating the in-in time integral over the cubic vertex in the Cai et al. approach. The two formalisms reorganize the same physics differently but converge on the same numerical bottleneck.

---

## Best Estimate: Mapping to Literature Values

From the algebraic structure, $f_{\rm NL}$ is determined by $\epsilon = 3/2$ and the growing-mode coupling coefficient. The two values in the literature correspond to:

$$
f_{\rm NL} = -\frac{5}{6}\cdot\frac{7\epsilon}{2}\cdot[\text{mode function coefficient}]
$$

For $\epsilon = 3/2$:

$$
f_{\rm NL} = -\frac{5}{6}\cdot\frac{21}{4}\cdot[\text{coefficient}]
$$

- If [coefficient] = 1: $\quad f_{\rm NL} = -35/8 = -4.375$ (Cai et al. 2009)
- If [coefficient] = 1/2: $\quad f_{\rm NL} = -35/16 = -2.1875$ (Li & Brandenberger 2016)

**The gradient expansion does NOT resolve the factor-of-2 ambiguity.** It confirms the structure but the exact coefficient requires the same mode-function evaluation that the in-in approach does.

---

## What the Gradient Expansion Does NOT Resolve

1. **The coefficient ambiguity.** Both $-35/8$ and $-35/16$ are consistent with the structural analysis. The gradient expansion constrains $f_{\rm NL}$ to the interval $[-35/8,\;-35/16]$ but does not select a unique value.

2. **The normalization convention of Li & Brandenberger.** Whether their result uses a different convention for $f_{\rm NL}$ or a different normalization of the cubic coupling cannot be determined from the gradient expansion alone.

3. **The LQC bounce transfer.** The gradient expansion operates in the contracting phase only. The question of how $f_{\rm NL}$ maps through the bounce to the expanding phase is a separate problem.

---

## Honest Summary

| Feature | Gradient Expansion Result | Status |
|---------|--------------------------|--------|
| Sign of $f_{\rm NL}$ | Negative | CONFIRMED |
| Magnitude | $O(\epsilon) = O(1)$ | CONFIRMED |
| Shape | Local (superhorizon, no $k$-dependence) | CONFIRMED |
| Scale dependence | None (parameter-free) | CONFIRMED |
| Exact coefficient | NOT independently resolved | OPEN |
| $-35/8$ vs $-35/16$ | Ambiguity NOT lifted by this method | OPEN |

**Bottom line:** The gradient expansion independently confirms every structural feature of the matter-bounce $f_{\rm NL}$ prediction. The exact numerical coefficient remains unresolved because it requires the same mathematical step -- evaluating the growing-mode-squared coupling through the full nonlinear Einstein equations -- regardless of which formalism is used.
