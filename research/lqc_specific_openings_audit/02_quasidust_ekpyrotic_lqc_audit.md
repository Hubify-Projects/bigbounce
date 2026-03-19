# Quasi-Dust Ekpyrotic LQC: Worth Pursuing?

**Created:** 2026-03-18
**Status:** ASSESSED
**Priority:** #4 (after formalism audit, third-order transfer, PBH channel)

---

## What Problem Does It Solve?

The current Wilson-Ewing model has two structural weaknesses:

1. **n_s = 0.964 is FITTED, not predicted.** It comes from epsilon = 0.003 (the Lambda contribution to the EOS during contraction). This is physically motivated but not derived -- epsilon is a free parameter set to match Planck. Compare with Starobinsky inflation, which predicts n_s = 1 - 2/N ~ 0.964 from the number of e-folds N ~ 55, with no fitting.

2. **BKL instability during contraction requires an ekpyrotic pre-phase.** Anisotropies grow as a^-6 during matter contraction. Without an ekpyrotic phase (w >> 1), anisotropies dominate before the bounce, destroying the homogeneous FRW geometry. The Wilson-Ewing model postulates ~10 e-folds of ekpyrosis before the bounce but does not derive the ekpyrotic sector from first principles.

The quasi-dust ekpyrotic model (arXiv:2509.06148, 2025) claims to address both weaknesses by combining:
- A matter-like contraction phase (for a near-scale-invariant base spectrum)
- An ekpyrotic phase (w >> 1) before the bounce (for BKL suppression)
- Two fields (adiabatic + entropy) with a conversion mechanism

---

## Does It Genuinely Extend the Viable Model Space?

**Partially.** It addresses the BKL problem more naturally than postulating "~10 e-folds of ekpyrosis." The two-field dynamics provide a self-consistent realization of the matter-to-ekpyrotic transition.

**But it introduces significant new ingredients:**
- A second scalar field (the entropy field)
- A conversion mechanism (entropy perturbations -> adiabatic perturbations)
- Multiple new parameters (potential shape for both fields, field-space curvature, coupling strength)
- A specific trajectory in field space during the bounce

**Comparison with Wilson-Ewing:**

| Feature | Wilson-Ewing (Model B) | Quasi-Dust Ekpyrotic |
|---------|----------------------|---------------------|
| Extra fields | 0 | 1 (entropy scalar) |
| Free parameters | 1 (epsilon) | 4+ (potential shapes, coupling) |
| BKL resolution | Postulated ekpyrotic pre-phase | Self-consistent two-field dynamics |
| n_s origin | Fitted from epsilon | Potentially predicted from field dynamics |
| f_NL | -35/8 (parameter-free) | UNKNOWN (likely model-dependent) |
| Complexity | Minimal | Moderate |

---

## Does It Add New Predictive Observables?

### Potentially:
- **Correlated n_s, r, f_NL:** Two-field dynamics can produce non-trivial relationships between observables that single-field models cannot. If the model predicts a specific f_NL as a function of n_s (not fitted independently), that is more predictive than Wilson-Ewing.
- **Entropy perturbation residual:** If the entropy-to-adiabatic conversion is incomplete, a residual isocurvature component could be detectable in the CMB.
- **Running alpha_s:** Two-field dynamics typically produce different spectral running than single-field, potentially distinguishable by Planck + future data.

### But:
- The specific f_NL from two-field ekpyrotic models is highly model-dependent. It depends on the potential shape, the field-space trajectory, and the conversion efficiency.
- Ekpyrotic models typically produce large EQUILATERAL non-Gaussianity (from the fast-roll dynamics with c_s < 1 effective sound speed), not local type. The local f_NL may be small.
- The matter-contraction f_NL (-35/8) would be diluted or modified by the entropy-to-adiabatic conversion. The conversion generically mixes the single-field bispectrum with the entropy-field bispectrum.

---

## Does It Threaten or Enrich the f_NL Story?

### POTENTIALLY THREATENS IT.

The strength of the Wilson-Ewing model is precisely that f_NL = -35/8 is parameter-free. It comes from single-field matter contraction dynamics with no additional ingredients. This is the model's key virtue: maximum prediction from minimum input.

Adding two-field dynamics introduces several risks:

1. **f_NL becomes model-dependent.** The conversion mechanism has free parameters that enter the bispectrum. Even if the model predicts a specific f_NL, that prediction depends on the field-space geometry and coupling.

2. **Ekpyrotic dynamics can suppress local f_NL.** In many ekpyrotic models, the local-type bispectrum is suppressed because the fast-roll dynamics produce equilateral rather than local non-Gaussianity. If the quasi-dust ekpyrotic model gives |f_NL^local| << 1, the primary discriminator is lost.

3. **Entropy-to-adiabatic conversion modifies the shape.** The total bispectrum is a sum of the adiabatic (matter-contraction) and converted (entropy) contributions. The sum need not be local-type. The template projection onto the Planck local template could be poor.

### When it ENRICHES:
- If the two-field model predicts f_NL close to -35/8 despite the additional dynamics, it confirms robustness.
- If it predicts a specific, different f_NL that is also testable (say, f_NL = -6 or f_NL = -3), it provides a competing model that the same survey can distinguish.
- If it predicts a correlated (n_s, f_NL) relation, it adds discriminating power.

---

## What Does the Existing Literature Say About f_NL in Matter-Ekpyrotic Models?

### Haro et al. (arXiv:1703.03710):
- Studied matter-ekpyrotic transition in LQC.
- Found near-scale-invariant spectrum but n_s outside Planck bounds for some parameter choices.
- **Did NOT compute f_NL.**

### Lehners (arXiv:1001.3125, review):
- General ekpyrotic non-Gaussianity: large equilateral f_NL ~ -O(c_s^{-2}) in the fast-roll phase.
- Local f_NL from ekpyrotic conversion: can be O(1) but is model-dependent (depends on the bending of the field-space trajectory).
- Two-field ekpyrotic: f_NL^local ~ -(5/12) kappa^2 where kappa is the field-space curvature at the bend. Typically |f_NL^local| ~ 1-10.

### Qiu, Gao, Saridakis (arXiv:1306.3927):
- Matter bounce with curvaton-like conversion.
- Found that the conversion can produce large local f_NL but with model-dependent sign and magnitude.

### Fertig, Lehners, Mallwitz (arXiv:1901.01218):
- Two-field ekpyrotic models: local f_NL depends sensitively on the conversion surface geometry.
- Can range from f_NL ~ 0 to f_NL ~ -50, depending on parameters.

### Key finding from literature survey:
**Two-field ekpyrotic models do NOT predict a specific f_NL.** The value depends on multiple parameters (field-space curvature, potential shape, conversion timing). This is the opposite of the Wilson-Ewing single-field model, which gives f_NL = -35/8 with zero free parameters.

---

## Verdict

### WORTH CHECKING but NOT worth full investment now.

**Reasons to check:**
- The 2025 paper (arXiv:2509.06148) claims a viable model with specific parameters. If those parameters give a definite f_NL, it is worth comparing.
- If the matter-ekpyrotic model gives f_NL close to -35/8, it confirms robustness (the matter-contraction contribution dominates regardless of the ekpyrotic pre-phase).
- If it gives a very different f_NL, these are competing models, and surveys can distinguish them.

**Reasons NOT to invest heavily now:**
- The model is more complex (2 fields, 4+ parameters) and less predictive than Wilson-Ewing.
- The f_NL prediction is almost certainly model-dependent, reducing the science case.
- It does not address the core vulnerability (single-point-of-failure on f_NL), it just adds a competing model with a DIFFERENT f_NL.
- The BKL resolution it provides can be postulated more simply in the Wilson-Ewing framework.

### Quick-check protocol:
1. Read arXiv:2509.06148 for specific parameter values and any n_s, r predictions.
2. Check if they compute f_NL (probably not -- it is a 2025 paper on background + linear perturbations).
3. If they give specific potential parameters, estimate f_NL from the Lehners formula: f_NL^local ~ -(5/12) kappa^2.
4. Compare with -35/8 = -4.375.
5. If |difference| < 1: robustness confirmed, document and move on.
6. If |difference| > 2: competing model, note for future survey comparison paper.
7. If f_NL is indeterminate: model is less predictive, Wilson-Ewing remains preferred.

**Estimated effort: 1 session for the quick check. No further investment unless the quick check reveals something surprising.**

---

## Summary

| Question | Answer |
|----------|--------|
| Does it solve a real problem? | Yes (BKL, partially n_s) |
| Does it add predictive power? | Unlikely (f_NL becomes model-dependent) |
| Does it threaten f_NL = -35/8? | Possibly (conversion could modify or suppress) |
| Is it simpler than Wilson-Ewing? | No (more fields, more parameters) |
| Priority? | #4 (after formalism audit, transfer, PBH) |
| Investment? | 1 session quick check, then decision gate |
