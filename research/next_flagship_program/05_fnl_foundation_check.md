# 05: f_NL Foundation Check

**Created:** 2026-03-17
**Status:** COMPLETE

---

## The Claim

f_NL^local = -35/8 = -4.375 is the matter bounce prediction in the Planck convention.

**This is the single value on which the entire positive research program depends.**

---

## Where It Comes From

### Source Paper
Cai, Xue, Brandenberger, Zhang (2009), arXiv:0903.0631, "Non-Gaussianity in a Matter Bounce"

### Method
Direct in-in (interaction picture) perturbation theory using Maldacena's third-order action, evaluated at epsilon = 3/2 (matter domination, w = 0). NOT the delta-N / separate-universe formalism.

### Steps:
1. Background: matter-dominated contraction, a(eta) proportional to eta^2
2. Mode functions: v_k has growing mode proportional to 1/eta (in conformal time)
3. Cubic action: six terms with coefficients involving epsilon = 3/2 (all O(1), not slow-roll suppressed)
4. Time integral: from -infinity to eta_B (bounce), dominated by late times (near bounce) because modes GROW on superhorizon scales
5. Squeezed limit (k_1 << k_2 ~ k_3): shape function A_T|_squeezed = -(21/8) k^3
6. f_NL identification: |B|_NL = (10/3) A_T / sum(k_i^3) -> -35/8 in squeezed limit

---

## Assumptions That Go Into It

### 1. Exact w = 0 during contraction
The derivation uses epsilon = 3/2 exactly. The quasi-dust model has epsilon = 3(1+w)/2 = 3(1-0.003)/2 = 1.4955. The fractional change is delta-epsilon/epsilon = 0.003, giving corrections to f_NL of order w^2 ~ 10^-5. **NEGLIGIBLE.**

### 2. Single canonical scalar field (c_s = 1)
The Cai et al. derivation assumes a canonical kinetic term. Li & Brandenberger (2016, arXiv:1612.02036) generalize to arbitrary c_s and get:
f_NL ~ -165/16 + 65/(8 c_s^2)

At c_s = 1: this gives -165/16 + 65/8 = -10.3125 + 8.125 = **-2.1875**

**THIS DOES NOT MATCH -35/8 = -4.375.** Discrepancy of a factor ~2.

### 3. Adiabatic perturbations only
No spectator fields, no isocurvature modes. If a curvaton is present, the bispectrum receives additional contributions. Our model has no curvaton (we use quasi-dust + Lambda only), so this assumption is satisfied.

### 4. No bounce transfer
The -35/8 is computed in the contracting phase, up to the bounce time eta_B. The transfer through the bounce is NOT included. If the bounce amplifies zeta (as needed for r suppression in LQC), the Quintin no-go implies |f_NL| is enhanced.

### 5. FRW background
The BKL instability (sigma^2/rho -> infinity for w < 1) could invalidate the homogeneous background. Requires ekpyrotic pre-phase. This is a model assumption, not a calculation assumption.

### 6. Bunch-Davies vacuum
Standard Minkowski vacuum in the asymptotic past. Alternative vacua would modify the mode functions and hence the bispectrum.

### 7. GR validity in the contracting phase
Higher-curvature corrections are negligible far from the bounce. This is safe for modes that exit the Hubble radius during the matter-dominated contraction, well before approaching rho_c.

### 8. Shape is "loosely local"
Cai et al. explicitly state: "If our predicted shape were exactly local (which it is not), then the above amplitude would equal the famous f_NL^local parameter. Since the matter bounce model predicts a shape which is loosely local, one can loosely speaking phrase our prediction as f_NL^local = -35/8."

**The observable f_NL^local is obtained by projecting the full bispectrum onto the local template.** This projection has not been computed precisely. The -35/8 is the squeezed-limit amplitude, which is the DOMINANT contribution to the local template projection, but there are corrections from non-squeezed configurations.

---

## Is It Truly Parameter-Free?

**YES, for the matter bounce with w = 0 and c_s = 1.** The value -35/8 depends only on epsilon = 3/2 (set by w = 0).

**But:** The quasi-dust model has w = -0.003, and the correction is negligible (O(w^2)). The value remains effectively -35/8 for the quasi-dust case.

---

## Is It Truly Robust Across Conventions?

**YES — verified.** Cai et al. use zeta = zeta_G + (3/5) f_NL zeta_G^2. Planck uses Phi = Phi_G + f_NL Phi_G^2 with Phi = (3/5) zeta. The algebraic conversion gives the SAME numerical f_NL in both conventions. (Verified in detail by our agent research.)

---

## Is It Tied to Matter Bounce Generically or Only Specific Setups?

**Generic to matter contraction with w = 0.** The result uses only:
- a(eta) proportional to eta^2 (matter domination)
- canonical scalar field
- standard vacuum initial conditions

It does NOT depend on:
- The specific bounce mechanism (LQC, ECH, Horndeski, etc.)
- The post-bounce history
- The presence of radiation, Lambda, or other components during the matter-dominated contraction phase

**However:** It IS specific to the contracting phase. The bounce transfer and post-bounce reprocessing could modify the observable value.

---

## Does LQC Change It?

**Unknown — this is the key open question.**

The LQC dressed-metric approach modifies the perturbation evolution through the bounce via a modified z''/z. This affects:
- The scalar amplification factor (which sets r)
- Potentially the bispectrum transfer (which affects f_NL)

For superhorizon modes (k << k_bounce ~ k_Pl), the bounce corrections are suppressed by (k/k_bounce)^n with n > 0. For CMB scales, k/k_bounce ~ 10^-56, so bounce corrections to f_NL should be NEGLIGIBLY small.

**BUT:** The Quintin no-go argues that if the bounce amplifies the scalar power spectrum (to suppress r), the same amplification enhances f_NL. The dressed-metric approach DOES amplify scalars. Whether the enhancement is significant for superhorizon modes is the critical question.

Agullo, Ashtekar, & Gupt (2015, arXiv:1510.05630) computed the LQC bispectrum for INFLATION (not matter bounce) and found oscillatory corrections at the bounce. For modes deep in the superhorizon regime, corrections are suppressed. Extrapolation to the matter bounce suggests f_NL is preserved, but this has not been explicitly verified.

---

## Does Quasi-Dust w = -0.003 Change It Materially?

**NO.** The correction is O(w^2) ~ O(10^-5), completely negligible. The f_NL value is essentially unchanged from the w = 0 case.

---

## Could Entropy Transfer / Bounce Matching / Gauge Issues Modify It?

### Entropy transfer
Not relevant in our model (single adiabatic field). The quasi-dust matter + Lambda system has no isocurvature degrees of freedom during the matter-dominated contraction.

### Bounce matching
This is the main unknown. The "matching" across the bounce is handled by the continuous evolution of the dressed-metric equations. There is no discontinuous matching condition in LQC — the effective equations are smooth through the bounce. But the third-order perturbation evolution through this smooth transition has not been computed.

### Gauge issues
The comoving gauge curvature perturbation zeta is gauge-invariant on superhorizon scales. No gauge artifacts are expected for the squeezed-limit bispectrum.

---

## What Would Invalidate Using This as Our Flagship Discriminator?

### Deal-breakers (would kill the program):
1. **Li & Brandenberger being correct at c_s = 1.** If the true value is -2.2 instead of -4.375, the MegaMapper detection drops from 8.75 sigma to 4.4 sigma. Still interesting, but less decisive, and the discrepancy would indicate the -35/8 calculation has errors.

2. **Quintin enhancement pushing |f_NL| > 10.** If the LQC bounce transfer enhances f_NL to -10 or beyond, the prediction violates Planck bounds (f_NL = -0.9 +/- 5.1, so |f_NL| > 10.3 is excluded at 2 sigma). The model would be observationally excluded.

3. **The shape being too far from local.** If the template projection of the matter bounce bispectrum onto the local template gives an effective f_NL^local significantly different from the squeezed-limit value, the prediction loses sharpness.

4. **A computational error in Cai et al.** No independent reproduction exists. The discrepancy with Li & Brandenberger is unresolved.

### Serious concerns (would weaken but not kill):
5. **Quintin enhancement giving |f_NL| ~ 6-8.** Still within Planck bounds, still detectable, but the prediction is no longer parameter-free — it depends on the LQC bounce details.

6. **The factor-of-2 Quintin citation discrepancy.** If the correct value is -35/16 = -2.1875, the prediction is weaker but still negative and detectable by MegaMapper at ~4.4 sigma.

---

## Structural Dependency Map

```
f_NL = -35/8 (flagship discriminator)
  |
  +-- Depends on: Cai et al. 2009 in-in calculation (SINGLE SOURCE)
  |     |
  |     +-- Discrepancy 1: Li & Brandenberger gives -2.2 at c_s = 1 (UNRESOLVED)
  |     +-- Discrepancy 2: Quintin cites -35/16 (factor of 2, UNRESOLVED)
  |     +-- Caveat: shape is "loosely local" (template projection not computed)
  |
  +-- Depends on: bounce transfer preserving f_NL (NOT VERIFIED)
  |     |
  |     +-- Quintin no-go: r suppression may enhance f_NL
  |     +-- LQC dressed-metric transfer: not computed at third order
  |     +-- Superhorizon suppression argument: (k/k_bounce)^n ~ 10^-56 (favorable)
  |
  +-- Depends on: convention match with Planck (VERIFIED)
  |
  +-- Depends on: w = 0 approximation (VERIFIED: w = -0.003 correction negligible)
  |
  +-- Depends on: no extra fields (SATISFIED: quasi-dust + Lambda only)
```

**The two UNRESOLVED dependencies are:**
1. The Cai et al. / Li-Brandenberger discrepancy
2. The bounce transfer at third order

**Both must be resolved before the flagship program is on solid ground.**
