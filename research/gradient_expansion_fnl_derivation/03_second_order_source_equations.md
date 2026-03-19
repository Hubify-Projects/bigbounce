# Second-Order Source Equations

**Created:** 2026-03-18
**Status:** COMPLETE

---

## 1. The Second-Order Equation (Recap)

From files 01-02, the perturbative expansion of the nonlinear superhorizon equation

$$
\ddot{\zeta} + \frac{2}{t}\dot{\zeta} + \frac{3}{2}\dot{\zeta}^2 = 0
$$

gives at second order:

$$
\ddot{\zeta}^{(2)} + \frac{2}{t}\dot{\zeta}^{(2)} = -3\left(\dot{\zeta}^{(1)}\right)^2
$$

with the first-order growing mode:

$$
\zeta^{(1)} = \frac{C(\mathbf{x})}{t}, \quad \dot{\zeta}^{(1)} = -\frac{C(\mathbf{x})}{t^2}
$$

**Source:**

$$
S^{(2)}(t) = -3\frac{C^2}{t^4}
$$

---

## 2. Are There Additional Source Terms from Spatial Gradients?

The derivation in file 01 used the ZEROTH-ORDER gradient expansion: the nonlinear evolution equation ddot{zeta} + (2/t)dot{zeta} + (3/2)dot{zeta}^2 = 0 was obtained by dropping ALL spatial gradient terms from the Einstein equations.

**Question:** Do spatial gradient terms contribute to f_NL at the same order as the (3/2)dot{zeta}^2 source?

### Analysis:

The full nonlinear equation including leading gradient terms is (from file 01, Section 6):

$$
\ddot{\zeta} + \frac{2}{t}\dot{\zeta} + \frac{3}{2}\dot{\zeta}^2 = \frac{1}{3a^2}e^{-2\zeta}\nabla^2\zeta + O((\nabla\zeta)^2, \zeta\nabla^2\zeta)
$$

At FIRST order, the gradient term (1/(3a^2))nabla^2 zeta^(1) is the term that allows zeta^(1) to have spatial dependence. It enters the energy constraint and determines the spatial profile of zeta through the initial conditions. But in the EVOLUTION equation, this term is what allows the growing mode to be spatially varying.

At SECOND order, the gradient terms contribute:

$$
S_{\rm grad}^{(2)} = \frac{1}{3a^2}\nabla^2\zeta^{(2)} - \frac{2}{3a^2}\zeta^{(1)}\nabla^2\zeta^{(1)} + \frac{1}{3a^2}(\nabla\zeta^{(1)})^2 + ...
$$

### Comparison of source terms:

For a mode with comoving wavenumber k:

- **The dot{zeta}^2 source:** ~ C^2/t^4. Since C ~ zeta^(1) * t ~ zeta_k * t, this goes as zeta_k^2 / t^2.

- **The gradient source terms:** ~ k^2/(a^2) * zeta^{(1)2}. For the growing mode zeta^(1) = C/t:

  k^2/(a^2) * (C/t)^2 = k^2 C^2 / (a^2 t^2)

  With a^2 = a_0^2 (-t/t_0)^{4/3}:

  ~ k^2 C^2 / (a_0^2 (-t)^{4/3} t^2) = k^2 C^2 / (a_0^2 (-t)^{10/3})

  Meanwhile, the dot{zeta}^2 source is C^2/t^4 = C^2/(-t)^4.

  **Ratio:** gradient source / dot{zeta}^2 source ~ k^2 (-t)^{4-10/3} / a_0^2 = k^2 (-t)^{2/3} / a_0^2.

  Now, (-t)^{2/3} ~ a(t)/a_0 (up to constants). And k/(aH) = k * 3t/(2a) = 3kt/(2a_0(-t/t_0)^{2/3}).

  For SUPERHORIZON modes, k/(aH) << 1, which means k(-t)/a << 1 (up to numerical factors). So k^2(-t)^{2/3}/a_0^2 ~ (k/(aH))^2 << 1.

**CONCLUSION: The spatial gradient contributions to the second-order source are suppressed by (k/(aH))^2 relative to the dot{zeta}^2 source.**

For superhorizon modes, these corrections are negligible. The zeroth-order gradient expansion is SELF-CONSISTENT at second order: the dominant source for f_NL is the (3/2)dot{zeta}^2 term, and gradient corrections are small.

**This is a key result.** It means the simple nonlinear ODE captures the full physics of f_NL for superhorizon modes.

---

## 3. The Complete Source at Zeroth Order in Gradients

Having established that gradient corrections are suppressed, the second-order source is simply:

$$
\boxed{S^{(2)}(t,\mathbf{x}) = -3\left(\dot{\zeta}^{(1)}\right)^2 = -\frac{3\,C(\mathbf{x})^2}{t^4}}
$$

**There are no other source terms at this order.**

---

## 4. Possible Additional Sources: Lapse and Shift Perturbations

In the full ADM formalism, the lapse N and shift N^i are determined by the constraint equations. Could nonlinear corrections to N and N^i contribute additional sources at second order?

### The lapse perturbation:

Write N = 1 + alpha, where alpha is the lapse perturbation. The constraint equations determine alpha in terms of zeta:

At first order:
$$
\alpha^{(1)} = -\frac{\dot{\zeta}^{(1)}}{H} = -\frac{(-C/t^2)}{2/(3t)} = \frac{3C}{2t}
$$

So alpha^(1) = (3/2) zeta^(1). This is an O(1) relation (not slow-roll suppressed), consistent with epsilon = 3/2.

At second order, alpha^(2) receives contributions quadratic in zeta^(1). These modify the evolution equation for zeta through terms like dot{alpha}^(1) * dot{zeta}^(1).

### The critical question:

Does the lapse perturbation contribute additional terms to the second-order evolution equation beyond what we already have?

**The answer is: the equation ddot{zeta} + (2/t)dot{zeta} + (3/2)dot{zeta}^2 = 0 was derived from the EXACT nonlinear Raychaudhuri equation in the separate-universe framework.** In this framework, the lapse is set to N = 1 (cosmic time slicing), and all nonlinear effects are captured by the local Hubble rate H_loc = H + dot{zeta}.

The (3/2)dot{zeta}^2 term is the COMPLETE nonlinear correction at zeroth order in gradients. No additional lapse or shift corrections are needed because we are working in the uniform-field gauge with cosmic time, where the lapse is identically 1 and the shift vanishes (to zeroth order in gradients).

**To verify:** The nonlinear Raychaudhuri equation for dust is:

$$
\dot{H}_{\rm loc} = -\frac{3}{2}H_{\rm loc}^2
$$

With H_loc = H + dot{zeta}:

$$
\dot{H} + \ddot{\zeta} = -\frac{3}{2}(H + \dot{\zeta})^2 = -\frac{3}{2}H^2 - 3H\dot{\zeta} - \frac{3}{2}\dot{\zeta}^2
$$

Using dot{H} = -(3/2)H^2:

$$
\ddot{\zeta} = -3H\dot{\zeta} - \frac{3}{2}\dot{\zeta}^2
$$

$$
\ddot{\zeta} + 3H\dot{\zeta} + \frac{3}{2}\dot{\zeta}^2 = 0
$$

With 3H = 2/t:

$$
\ddot{\zeta} + \frac{2}{t}\dot{\zeta} + \frac{3}{2}\dot{\zeta}^2 = 0
$$

**Confirmed.** This is the EXACT nonlinear equation (at zeroth order in spatial gradients) for the local expansion rate perturbation in dust-dominated contraction. The lapse is N = 1 by construction, and the shift is zero at zeroth order. No additional corrections.

---

## 5. Fourier-Space Structure of the Source

In Fourier space, the source S^(2) = -3(dot{zeta}^(1))^2 becomes a CONVOLUTION:

$$
S_{\mathbf{k}}^{(2)} = -3\int\frac{d^3q}{(2\pi)^3}\,\dot{\zeta}^{(1)}_{\mathbf{q}}\,\dot{\zeta}^{(1)}_{\mathbf{k}-\mathbf{q}}
$$

For the growing mode: dot{zeta}^(1)_q = -C_q / t^2, so:

$$
S_{\mathbf{k}}^{(2)} = -\frac{3}{t^4}\int\frac{d^3q}{(2\pi)^3}\,C_{\mathbf{q}}\,C_{\mathbf{k}-\mathbf{q}}
$$

The time dependence (1/t^4) factors out of the convolution. This is because both modes have the SAME time dependence (the growing mode).

**This factorization is key:** it means the second-order equation in Fourier space is:

$$
\ddot{\zeta}^{(2)}_{\mathbf{k}} + \frac{2}{t}\dot{\zeta}^{(2)}_{\mathbf{k}} = -\frac{3}{t^4}\int\frac{d^3q}{(2\pi)^3}\,C_{\mathbf{q}}\,C_{\mathbf{k}-\mathbf{q}}
$$

The spatial (k) dependence sits entirely in the convolution integral, while the time dependence is universal (1/t^4).

---

## 6. Connection to the Bispectrum

The bispectrum is related to zeta^(2) by:

$$
\langle\zeta_{\mathbf{k}_1}\zeta_{\mathbf{k}_2}\zeta_{\mathbf{k}_3}\rangle = \langle\zeta^{(1)}_{\mathbf{k}_1}\zeta^{(1)}_{\mathbf{k}_2}\zeta^{(2)}_{\mathbf{k}_3}\rangle + \text{2 perms} + O(\text{4th order})
$$

In the squeezed limit k_3 -> 0 with k_1 = k_2 = k:

$$
B_\zeta(k_1,k_2,k_3) \supset P(k_1)\cdot\frac{\zeta^{(2)}_{k_3}}{\zeta^{(1)}_{k_3}} + \text{(perms)}
$$

Since zeta^(2) proportional to [zeta^(1)]^2, the ratio zeta^(2)/zeta^(1) is proportional to zeta^(1), giving the local-shape B ~ P * P structure.

The local f_NL is then determined by the coefficient:

$$
f_{\rm NL} = \frac{5}{6}\frac{\zeta^{(2)}(t,\mathbf{x})}{\left[\zeta^{(1)}(t,\mathbf{x})\right]^2}
$$

evaluated at any superhorizon time (the ratio must be time-independent if f_NL is a well-defined quantity).

---

## 7. Why the Source Coefficient Matters

The second-order equation is:

$$
\ddot{\zeta}^{(2)} + \frac{2}{t}\dot{\zeta}^{(2)} = -\frac{3C^2}{t^4}
$$

The source coefficient is **-3**. This number comes ENTIRELY from the coefficient (3/2) in the nonlinear Raychaudhuri equation dot{H}_loc = -(3/2) H_loc^2, which in turn comes from epsilon = 3/2 (matter domination).

**For general epsilon (general w):**

The Raychaudhuri equation is dot{H}_loc = -epsilon H_loc^2 (for constant epsilon).

Expanding to second order:

ddot{zeta} + (1 + epsilon/(epsilon))... Actually let me derive this properly.

For general constant epsilon: H = p/t where p = 1/(1+epsilon-1)... this is getting complicated. Let me just note that for matter (epsilon = 3/2), the source coefficient is -3, and for general epsilon:

The nonlinear equation is ddot{zeta} + (epsilon + 1)H dot{zeta} + epsilon dot{zeta}^2 = 0 (this is the general form of the Raychaudhuri equation for constant epsilon).

Wait -- let me rederive. For general constant epsilon: dot{H} = -epsilon H^2, so H = 1/(epsilon t) (choosing conventions). Actually, for a(t) ~ (-t)^{1/epsilon} (contraction), H = 1/(epsilon t). Then 3H = 3/(epsilon t).

The Raychaudhuri equation dot{H}_loc = -epsilon H_loc^2 gives:

ddot{zeta} + (1 + epsilon)H dot{zeta} + epsilon dot{zeta}^2 = 0

Hmm, let me just verify for epsilon = 3/2. H = 2/(3t), so (1 + 3/2)(2/(3t)) = (5/2)(2/(3t)) = 5/(3t). But we have 2/t = 3H. And (1+epsilon)H = (5/2)(2/(3t)) = 5/(3t) which is NOT 2/t.

I think the issue is that the general form for a ~ (-t)^p with p = 2/(3(1+w)) gives H = p/t. For matter: p = 2/3, H = 2/(3t). Then dot{H} = -p/t^2 and epsilon = p/t^2 / (p/t)^2 = 1/p. So for p = 2/3: epsilon = 3/2. Good.

The Raychaudhuri equation: dot{H}_loc = -(1/p)H_loc^2. Wait: dot{H} = -epsilon H^2 = -(3/2)(4/(9t^2)) = -2/(3t^2). Check: -p/t^2 = -2/(3t^2). Yes.

But dot{H} = -epsilon H^2 = -(1/p)(p/t)^2 = -p/t^2. Confirmed.

Now: dot{H}_loc = -epsilon H_loc^2 means:

dot{H} + ddot{zeta} = -epsilon(H + dot{zeta})^2 = -epsilon H^2 - 2 epsilon H dot{zeta} - epsilon dot{zeta}^2

Since dot{H} = -epsilon H^2:

ddot{zeta} = -2 epsilon H dot{zeta} - epsilon dot{zeta}^2

For epsilon = 3/2, H = 2/(3t): 2 epsilon H = 2(3/2)(2/(3t)) = 2/t. **CONFIRMED.**

And the dot{zeta}^2 coefficient is epsilon = 3/2. **CONFIRMED.**

So the general form is:

$$
\ddot{\zeta} + 2\epsilon H\dot{\zeta} + \epsilon\dot{\zeta}^2 = 0
$$

At second order:

$$
\ddot{\zeta}^{(2)} + 2\epsilon H\dot{\zeta}^{(2)} = -2\epsilon\left(\dot{\zeta}^{(1)}\right)^2
$$

For epsilon = 3/2: source coefficient = -2 * 3/2 = -3. **CONFIRMED.**

**The source coefficient -3 is DERIVED from epsilon = 3/2 (w = 0). For general w: the coefficient is -2 epsilon = -(3(1+w))/(1)... = -3(1+w).** For w = 0: -3. For slow-roll inflation (epsilon << 1): -2 epsilon, which is tiny. This confirms that large f_NL is specific to matter domination (large epsilon).

---

## 8. Summary

The second-order source equation is fully determined:

$$
\boxed{\ddot{\zeta}^{(2)} + \frac{2}{t}\dot{\zeta}^{(2)} = -\frac{3\,C^2(\mathbf{x})}{t^4}}
$$

with:
- Source coefficient: **-3** (derived from epsilon = 3/2)
- Source time dependence: **t^{-4}** (from the square of the growing mode's time derivative)
- Spatial dependence: **C(x)^2** (convolution of first-order modes in Fourier space)
- Gradient corrections: **suppressed by (k/aH)^2** (negligible for superhorizon modes)
- Lapse/shift corrections: **none at zeroth order in gradients** (verified)

**Everything needed for the solution is in hand. No assumptions remain beyond w = 0 and the superhorizon (gradient expansion) approximation.**
