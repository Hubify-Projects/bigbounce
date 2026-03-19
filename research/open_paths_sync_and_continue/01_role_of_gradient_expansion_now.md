# Role of the Gradient Expansion Now

**Created:** 2026-03-19
**Status:** CLOSED
**Classification:** SUPPORTING_CROSS_CHECK

---

## Decision

The gradient expansion is a **SUPPORTING_CROSS_CHECK**. It independently derives f_NL^GE ~ -5/4 (the superhorizon piece, corresponding to the Hamiltonian-constraint nonlinearity) and confirms sign, magnitude, shape, and parameter-free nature. But the full coefficient is now settled by the Cai action audit (-35/8 verified through three independent methods). The gradient expansion adds a pedagogical and theoretical cross-check but is NOT the frontier.

**No further work on this line is justified.**

---

## What the Gradient Expansion Established

1. **Sign:** Negative. The growing-mode-squared coupling through the energy constraint generates an anti-correlated contribution. This matches the sign from the in-in calculation (after the convention resolution from the Cai audit).

2. **Magnitude:** O(epsilon) = O(1) for matter contraction (epsilon = 3/2). Not slow-roll-suppressed. The gradient expansion makes this manifest: the nonlinearity is a BACKGROUND-LEVEL effect amplified by the growing mode, not a loop correction.

3. **Shape:** Local. The gradient expansion operates in position space on superhorizon scales. There are no k-dependent vertices. The resulting bispectrum is purely squeezed/local by construction. This confirms the local-shape result from the in-in calculation without any Fourier-space manipulation.

4. **Parameter-freedom:** The f_NL depends only on w = 0 (the equation of state during contraction). All other parameters -- the scalar field mass, the scalar field VEV, the bounce energy density -- cancel in the ratio B/P^2. The gradient expansion makes this particularly transparent because the calculation never introduces these parameters.

---

## What the Gradient Expansion Did NOT Resolve

The exact numerical coefficient. The gradient expansion reaches the same mathematical bottleneck as the in-in approach: evaluating the growing-mode-squared coupling through the full second-order Einstein equations. The superhorizon piece gives f_NL^GE = -5/4, but the complete coefficient requires the horizon-crossing contribution, which is the same object in both formalisms expressed in different variables.

This was the last open quantitative question, and it has been resolved by the Cai action audit (not by the gradient expansion). The Cai audit identified three specific differences between our in-in calculation and Cai's, explained the sign flip (mode-function conjugation) and the magnitude difference (superhorizon-dominated vs horizon-crossing-dominated regime), and concluded f_NL = -35/8 from the correct starting point.

---

## How It Should Appear in the Paper

The gradient expansion deserves 3-4 sentences in the paper, or at most a 1-page appendix:

> "As an independent consistency check, we verify the structural features of f_NL using the Salopek-Bond gradient expansion [refs]. Working entirely in position space on superhorizon scales, the gradient expansion confirms that f_NL is negative, O(1), local-shape, and parameter-free for w = 0 contraction. The superhorizon piece alone gives f_NL^GE = -5/4, consistent with the superhorizon sector of the full in-in result. This formalism-independent confirmation strengthens confidence in the robustness of the prediction."

This is the appropriate level of treatment: credit the cross-check, cite the structural confirmation, do not overstate the contribution.

---

## Why No Further Extension Is Warranted

1. **The coefficient is resolved.** Extending the gradient expansion to capture the horizon-crossing contribution would reproduce what the Cai audit + SymPy cancellation already established (-35/8). The marginal information gain is zero.

2. **The formalism bottleneck is identical.** The growing-mode-squared coupling is the same mathematical object in the gradient expansion and the in-in approach. Completing the calculation in the gradient expansion variables is not "independent" -- it is the same computation expressed differently.

3. **Opportunity cost.** Every session spent extending the gradient expansion is a session NOT spent on the PBH+GW feasibility assessment, the formalism sensitivity audit, or paper preparation. The gradient expansion has diminishing returns; the other paths have not been touched.

4. **The science case does not depend on it.** The paper can be (and has been) drafted using the in-in result from Cai et al., verified by SymPy and the gradient-expansion structural check. Adding a full gradient-expansion reproduction of -35/8 would make the theory section slightly stronger but would not change any forecast, any Bayes factor, or any observational prediction.

---

## Final Status

```
Gradient expansion f_NL derivation: CLOSED (SUPPORTING_CROSS_CHECK)
  - Structural features confirmed: YES (sign, magnitude, shape, parameter-freedom)
  - Exact coefficient resolved: NO (but resolved by Cai audit)
  - Further work justified: NO
  - Paper treatment: 3-4 sentences or 1-page appendix
  - Priority for extension: ZERO
```
