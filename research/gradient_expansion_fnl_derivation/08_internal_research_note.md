# 08: Internal Research Note: Gradient-Expansion f_NL Derivation

**Created:** 2026-03-18
**Status:** COMPLETE
**Audience:** Internal (research program tracking)

---

## Why This Derivation Was Worth Doing

### 1. Confirmed the structural features from an independent formalism

The gradient expansion (Salopek-Bond approach applied to matter contraction) independently confirms all four structural features of the $f_{\rm NL}$ prediction:

| Feature | Confirmed? | Method of confirmation |
|---------|------------|------------------------|
| Sign: negative | Yes | Energy-constraint nonlinearity dominates; growing mode creates negative skewness |
| Magnitude: $O(1)$ | Yes | $f_{\rm NL} = O(\epsilon)$ with $\epsilon = 3/2$; not slow-roll-suppressed |
| Shape: local | Yes | Calculation is purely in position space on superhorizon scales; Fourier transform gives local template |
| Parameter-free | Yes | All model parameters ($m$, $M_{\rm Pl}$, initial amplitude) cancel in the ratio $B/P^2$; only $w = 0$ enters |

These confirmations are genuinely independent: the gradient expansion never constructs the cubic action, never evaluates an in-in time integral, and never uses Fourier-space mode functions.

### 2. Identified the shared bottleneck

The exact numerical coefficient ($-35/8$ or $-35/16$) requires evaluating the same mathematical quantity in every formalism:

- **In-in approach:** Time integral $\int d\eta'\;\eta'^4\,g_{k_1}^{\rm super}\,[g_k']^2$ at horizon crossing
- **Gradient expansion:** Total coefficient $\alpha$ of the source $S^{(2)} = \alpha\,C_2^2/t^3$ from three nonlinear Einstein-equation terms

These are the same algebra expressed in different variables. The discrepancy between Cai et al. ($-35/8$) and Li & Brandenberger ($-35/16$) is a disagreement about this single number, not about formalism or conventions (though a convention offset may be the root cause).

**This is a crucial finding:** the $-35/8$ vs $-35/16$ question is NOT "cubic action vs. gradient expansion." It is a question about one numerical coefficient that appears identically in both approaches. Resolving it requires evaluating that coefficient carefully, which can be done numerically.

### 3. Provided physical transparency

The gradient expansion makes the physics of matter-bounce non-Gaussianity transparent in a way the cubic-action approach does not:

- The growing mode $\zeta^{(1)} = C_2/t$ is an explicit function of time
- The second-order source is a sum of three identifiable physical contributions (energy constraint, momentum constraint, spatial curvature)
- The particular solution $\zeta^{(2)} \propto C_2^2/t^2$ shows directly that $f_{\rm NL}$ is the ratio of two time-independent quantities
- The cancellation at leading order (the Finelli-Brandenberger formula gives zero for $n_s = 1$) reveals WHY the coefficient is hard: it comes from the next-order terms

### 4. Narrowed the path to resolution

Before this derivation: "We need to redo the Cai et al. calculation from scratch to check $-35/8$."

After this derivation: "We need to evaluate one specific numerical coefficient. Everything else is confirmed. The coefficient can be computed by numerical quadrature of a one-dimensional integral with known integrand."

This is a much sharper target.

---

## Does This Strengthen the Theory Case?

### YES, partially

The structural confirmation from an independent formalism raises confidence that the matter-bounce $f_{\rm NL}$ prediction is:
- Definitely negative (robust across formalisms)
- Definitely $O(1)$ (not an artifact of the cubic-action approximation)
- Definitely detectable if MegaMapper achieves $\sigma(f_{\rm NL}) \sim 0.5$
- Definitely parameter-free (no model-dependent knobs)

### NO, not fully

The exact coefficient remains unresolved. The gradient expansion hits the same algebraic wall as the in-in approach. We cannot claim to have independently verified "$f_{\rm NL} = -35/8$" because we have not independently computed the coefficient.

---

## How It Changes the Live Science Case

### Before this derivation

"Cai et al. computed $f_{\rm NL} = -35/8$ using the cubic action. Li & Brandenberger got $-35/16$ using a generalized formalism. The discrepancy is unresolved. We trust $-35/8$ at $\sim 75\%$ based on convention analysis."

### After this derivation

"Two independent formalisms (cubic action and gradient expansion) confirm the sign, magnitude, shape, and parameter-free nature of the prediction. The remaining ambiguity is a factor-of-2 in the coefficient, residing in a single numerical step. Both values ($-4.375$ and $-2.19$) predict MegaMapper detections at $> 4\sigma$. The science case is robust regardless of which value is correct."

### Confidence update

$75\% \to 80\%$ (structural features confirmed; coefficient still open)

The 5% increase reflects the genuine value of structural confirmation from an independent formalism, tempered by the fact that the coefficient -- the piece most in question -- was not resolved.

---

## What Has Not Changed

1. **The single-point-of-failure architecture.** $f_{\rm NL}$ is still the only sharp numerical discriminator between the matter bounce and single-field inflation. A second independent observable channel (PBH spectrum, induced gravitational waves, spectral tilt running) would dramatically strengthen the program.

2. **The need for numerical verification.** The in-in time integral must be evaluated numerically with exact mode functions. This is a well-defined calculation that has not been done in this program.

3. **The LQC bounce transfer question.** The gradient expansion operates entirely in the contracting phase. How $f_{\rm NL}$ maps through the bounce (LQC or otherwise) to the expanding phase is a separate, unresolved question. Generic arguments suggest it passes through unchanged for superhorizon modes, but this has not been rigorously demonstrated.

4. **The quasi-dust sensitivity.** If the contracting phase is not exactly $w = 0$ but $w = 0 + \delta w$ with $|\delta w| \ll 1$, the $f_{\rm NL}$ prediction shifts by $O(\delta w)$, which is small ($\sim 0.3\%$ for realistic deviations) but not exactly zero.

---

## Immediate Next Step

**Numerical evaluation of the in-in time integral** using exact mode functions.

This is now the ONLY remaining bottleneck for resolving the coefficient. Everything else has been checked. The calculation is:

1. Code the exact mode function $g_k(\eta) = \frac{1}{\sqrt{2k}}\left(1 - \frac{i}{k\eta}\right)e^{-ik\eta}$ and its derivative
2. Evaluate $I(x_f) = \int_{-\infty}^{x_f} dx\;\frac{1}{x^2}\left[\frac{d}{dx}\left(\frac{e^{-ix}}{x}\right)\right]^2$ (schematic; exact integrand from Cai et al. Eq. (15))
3. Verify convergence and extract the real part
4. Compute $f_{\rm NL} = (5/6) \times [\text{vertex coefficient}] \times I + [\text{field redefinition}]$
5. Compare with $-35/8$ and $-35/16$

Expected effort: 1-2 sessions of careful numerical work with Python/SciPy.

Expected output: a definite number with no remaining ambiguity.
