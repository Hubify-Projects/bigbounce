# Final Verdict: Gradient-Expansion f_NL Derivation

**Created:** 2026-03-18
**Status:** CLOSED

---

## 1. Did the gradient expansion reproduce $-35/8$?

**Structurally yes, numerically not resolved.**

The gradient expansion independently confirms:

- $f_{\rm NL}$ is **negative** (anti-correlated growing-mode coupling; energy-constraint nonlinearity dominates)
- $f_{\rm NL}$ is **$O(\epsilon) = O(1)$** for matter contraction ($\epsilon = 3/2$, not slow-roll-suppressed)
- $f_{\rm NL}$ has **local shape** (superhorizon calculation in position space; no $k$-dependent vertices)
- $f_{\rm NL}$ is **parameter-free** (depends only on $w = 0$; all other parameters cancel in $B/P^2$)

The exact coefficient ($-35/8$ vs $-35/16$) was NOT independently determined because the gradient expansion reaches the same numerical bottleneck as the cubic-action approach: evaluating the growing-mode-squared coupling through the full second-order Einstein equations.

---

## 2. What coefficient was obtained?

$$
f_{\rm NL} \in \left[-\frac{35}{8},\;-\frac{35}{16}\right] = [-4.375,\;-2.188]
$$

The structural analysis constrains $f_{\rm NL}$ to this interval (bounded by the two literature values) but does not select a unique value. The gradient expansion confirms the algebraic form:

$$
f_{\rm NL} = -\frac{5}{6}\cdot\frac{7\epsilon}{2}\cdot[\text{coupling coefficient}]
$$

with $\epsilon = 3/2$ and the coupling coefficient $\in [1/2, 1]$.

---

## 3. Is the result genuinely independent?

**Partially.**

| Aspect | Independent? | Explanation |
|--------|-------------|-------------|
| Formalism | Yes | Gradient expansion uses nonlinear Einstein equations directly; no cubic action, no in-in integrals, no Fourier-space mode functions |
| Structural features | Yes | Sign, magnitude, shape, parameter-freedom all confirmed independently |
| Exact coefficient | No | Both formalisms require evaluating the same growing-mode-squared coupling, which is the same mathematical step expressed in different variables |

The gradient expansion is a genuinely different mathematical route that independently confirms all qualitative and semi-quantitative features. But the single numerical quantity in dispute (the coupling coefficient) is the same object in both formalisms, so neither can resolve the other's value without completing the same calculation.

---

## 4. Does this materially strengthen the theory case?

**Yes.** Confidence raised from $\sim 75\%$ to $\sim 80\%$.

The prediction is now confirmed as structurally robust from two independent formalisms. The remaining uncertainty is a factor-of-2 in one coefficient, and both possible values predict detectable signals:

| Value | Source | MegaMapper SNR ($\sigma_{f_{\rm NL}} = 0.5$) |
|-------|--------|----------------------------------------------|
| $f_{\rm NL} = -4.375$ | Cai et al. (2009) | $\approx 8.75\sigma$ |
| $f_{\rm NL} = -2.19$ | Li & Brandenberger (2016) | $\approx 4.4\sigma$ |

The science case -- a parameter-free, falsifiable prediction testable by next-generation LSS surveys -- is NOT dependent on resolving the factor-of-2.

---

## 5. What exact next step should follow immediately?

### Option A (theory): Numerical evaluation of the in-in time integral

- **What:** Code the exact Bessel-type mode functions for the short modes in the squeezed limit. Evaluate the one-dimensional time integral that determines the coupling coefficient. This is the integral identified in `research/fnl_derivation_execution/final_verdict.md` (Sec. 6).
- **Why:** Resolves $-35/8$ vs $-35/16$ definitively. Closes the last open question in the $f_{\rm NL}$ prediction.
- **Effort:** 1-2 sessions of careful numerical work (Python/SciPy).
- **Risk:** Low. The integral is well-defined and convergent. The only question is its numerical value.

### Option B (survey): Move to the PBH + induced GW second observable channel

- **What:** Assess whether the matter-bounce power spectrum at small scales ($k \gg k_{\rm CMB}$) produces primordial black holes (PBH) or induced gravitational waves (GW) at detectable amplitudes.
- **Why:** Breaks the single-point-of-failure architecture. Currently, $f_{\rm NL}$ is the only sharp discriminator. A second independent channel would make the program resilient to a null $f_{\rm NL}$ result.
- **Effort:** 1 session for order-of-magnitude estimate (Wilson-Ewing bounce sharpness). More if viable.
- **Risk:** Moderate. The small-scale spectrum depends on bounce details (LQC, ECH, etc.) that are not constrained by the large-scale analysis.

**Recommendation:** Option A if the goal is theoretical completeness (pin down the exact prediction before writing). Option B if the goal is observational resilience (ensure the program survives even if MegaMapper's $f_{\rm NL}$ measurement is ambiguous).

---

## Program Status After This Derivation

```
f_NL structural features:   CONFIRMED (2 formalisms)         [DONE]
f_NL exact coefficient:     [-35/8, -35/16] (bounded)        [OPEN]
f_NL detectability:         >4-sigma at MegaMapper (either)   [DONE]
Second observable channel:  NOT YET ASSESSED                  [TODO]
LQC bounce transfer:        NOT YET CHECKED                  [TODO]
Numerical time integral:    NOT YET EVALUATED                 [TODO]
Paper readiness:            ~70% (f_NL confirmed enough to write; coefficient ambiguity must be acknowledged)
```

### What is needed before publication

1. **Resolve $-35/8$ vs $-35/16$** (Option A above) OR explicitly acknowledge the ambiguity and quote the range
2. **Assess bounce transfer** (does $f_{\rm NL}$ pass through the bounce unchanged?)
3. **Write the paper** with honest error budget: quote $f_{\rm NL} = -4.4 \pm 2.2$ (spanning the range) or the resolved value

### What is NOT needed before publication

- The gradient expansion derivation itself (it is a cross-check, not a primary result)
- Resolution of every literature discrepancy (the Quintin citation artifact is documented but not publishable)
- A second observable channel (desirable but not required for the first paper)
