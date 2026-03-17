# Branch Q: Best Model Selection

**Date:** 2026-03-16

---

## Winner: Candidate C — Dynamical Barbero-Immirzi Field

### Why it is best

Among the seven candidates screened, Candidate C is the only one that
satisfies ALL of:
- Survives OOM screening (coupling strong enough, not excluded)
- Has genuine geometric motivation from ECH (promoted Immirzi parameter)
- Opens a birefringence channel that matches current data

No other candidate achieves all three simultaneously:
- A (Grav CS): no birefringence, not ECH-specific
- B, D (standard ALP): no geometric motivation
- E (explicit PV): killed on source and strength
- F (Nieh-Yan): reduces to C
- G (PGT parity-odd): killed on coupling strength

### The model

**Field content:** gamma(x) = gamma_0 + phi(x)/f_phi, where gamma is the
Barbero-Immirzi parameter and phi is a pseudoscalar field.

**Action:**
```
S = (1/2 kappa) integral [e^I wedge e^J wedge F_{IJ}
                          + (1/gamma(x)) e^I wedge e^J wedge (*F_{IJ})]
    + integral [(1/2)(partial phi)^2 - V(phi)] sqrt(-g) d^4x
    + S_matter[psi, e, omega]
```

**New parameters:** f_phi (decay constant), m_phi (from V(phi))

**Key couplings after torsion elimination:**
1. Derivative coupling: (1/f_phi) partial_mu phi J^{5,mu}
2. Induced photon coupling: [alpha N_eff / (4 pi f_phi)] phi F F-tilde
3. Modified four-fermion: C(gamma_0, phi/f_phi) * (kappa/4) * (J^5)^2

**Birefringence prediction:**
```
beta = [alpha * N_eff / (8 pi)] * (Delta phi / f_phi) * (180/pi)

For N_eff = 8, Delta phi / f_phi ~ 1:
beta ~ 0.13 degrees (within factor 3 of 0.35 deg observed)
```

---

## The honest assessment

### What is ECH-specific

1. **The ORIGIN of phi.** The Immirzi parameter is unique to the Palatini
   formulation of gravity with the Holst term. Promoting it to a field
   is the minimal dynamical extension of the ECH framework. No other
   theory has this specific field.

2. **f_phi ~ M_Pl.** The identification phi = (gamma - gamma_0) * f_phi
   with gamma an O(1) parameter implies f_phi is at the Planck scale.
   This is a (soft) prediction: f_phi is not a free parameter but is
   theoretically bounded to the Planck scale by the geometric origin.

3. **No direct phi F F-tilde.** The geometric embedding FORBIDS a direct
   phi-photon coupling at tree level. All photon coupling goes through
   the fermion ABJ triangle. This is a restriction that constrains the
   parameter space.

4. **phi-dependent (J^5)^2.** The four-fermion interaction strength depends
   on phi/f_phi. This is a genuinely new operator, but Planck-suppressed
   (kappa ~ 1/M_Pl^2) and parity-EVEN (modifies the coefficient of (J^5)^2,
   not its symmetry).

### What is NOT ECH-specific

1. **The phi F F-tilde coupling.** The induced coupling alpha/(4 pi f_phi)
   is the standard ABJ anomaly coefficient. Any ALP with a derivative
   fermion coupling produces the same operator with the same coefficient
   (up to group theory factors).

2. **The birefringence prediction.** beta depends on Delta phi / f_phi and
   alpha, both of which are available to any ALP model. The predicted
   beta ~ 0.1 deg for O(1) misalignment is a dimensional-analysis
   coincidence that works for any ALP with f_a ~ M_Pl.

3. **The mass m_phi.** The Immirzi field has no natural mass from the
   ECH framework. A potential must be added by hand (from instantons
   or some other mechanism). The mass is a free parameter.

4. **The late-time dynamics.** phi rolls in its potential identically
   to any other ultralight pseudoscalar. The ECH origin is invisible
   in the late-universe evolution.

### Bottom line

**The dynamical Immirzi field is a geometrically motivated ALP, but its
observable predictions are indistinguishable from a generic ALP with
f_a ~ M_Pl.**

The ECH framework provides a MOTIVATION for the field's existence and
constrains f_phi to the Planck scale, but does not produce any distinctive
observable signature.

---

## What to calculate next

### Calculation 1: Exact torsion elimination with dynamical gamma

Solve the torsion equation of motion with gamma = gamma_0 + phi/f_phi
to all orders in phi/f_phi. Determine:
- The exact form of the derivative coupling (any corrections to 1/f_phi?)
- The exact phi-dependence of the four-fermion term
- Whether any NEW operators appear beyond leading order

This is a clean algebraic calculation (no loops, no numerics needed).

**Expected outcome:** Leading-order result confirmed. Corrections are
O(phi^2/f_phi^2) and Planck-suppressed. No surprises.

**Time estimate:** 2-4 hours.

### Calculation 2: Birefringence MCMC fit

Use the existing Cobaya + CAMB infrastructure to fit:
- f_phi (with the prior f_phi ~ M_Pl from the geometric identification)
- m_phi (free, ultralight)
- Delta phi / f_phi (misalignment, ~ O(1))

to the Planck + ACT birefringence data.

**Expected outcome:** Posterior on f_phi peaked near M_Pl, consistent
with observation. But this is IDENTICAL to an ALP MCMC fit with f_a
as a free parameter. The geometric prior f_phi ~ M_Pl can be tested:
if data prefer f_a << M_Pl, the Immirzi interpretation is disfavored.

**Time estimate:** 1-2 days (reusing existing MCMC chains with modified
likelihood for birefringence).

### Calculation 3: Consistency check — ABJ coefficient

Verify that the ABJ anomaly coefficient in the torsion-eliminated theory
matches the standard QED result. This was done in Branch S for the
minimal (non-dynamical gamma) case. Repeat with dynamical gamma to check
for modifications.

**Expected outcome:** No modification. The anomaly is universal
(Adler-Bardeen theorem). The dynamical gamma does not change the
anomaly coefficient, only the external coupling.

**Time estimate:** 1-2 hours.

---

## What kills it quickly

### Kill 1: f_phi << M_Pl required by data

If the birefringence data require f_a << M_Pl (e.g., f_a ~ 10^{10} GeV),
the Immirzi field interpretation fails. The geometric identification
phi = delta gamma * f_phi requires f_phi ~ M_Pl, and sub-Planckian f_phi
would mean gamma(x) varies by enormous amounts, which is inconsistent
with the perturbative expansion.

**How to check:** Run the MCMC fit with and without the f_phi ~ M_Pl
prior. If the likelihood strongly prefers f_a << M_Pl, the Immirzi
interpretation is killed.

### Kill 2: Frequency-dependent birefringence detected

The Immirzi field model predicts frequency-INDEPENDENT birefringence
(phi F F-tilde coupling). If future data detect frequency dependence,
the model is excluded (along with all phi F F-tilde models).

**Timeline:** Simons Observatory, CMB-S4 (multi-frequency data ~2027-2030).

### Kill 3: Anisotropic birefringence pattern inconsistent with ultralight ALP

If the anisotropic birefringence pattern (multipole structure of beta(n-hat))
is detected and is inconsistent with an ultralight scalar field (e.g.,
requires spin-2 or vector source), the model is killed.

**Timeline:** LiteBIRD (~2032).

### Kill 4: No new operators found in Calculation 1

If the exact torsion elimination with dynamical gamma produces NO new
operators beyond the standard ALP terms, the model is confirmed as
phenomenologically identical to a generic ALP. This does not kill the
model but kills the claim of ECH-specific observables.

This is the most likely outcome.

---

## Decision tree

```
Start: Candidate C (dynamical Immirzi field)
  |
  v
Calculation 1: Exact torsion elimination
  |
  +-- New operators found? ---> BRANCH Q PROMISING
  |                              (proceed to phenomenology)
  |
  +-- No new operators -------> Phenomenologically generic ALP
       |
       v
  Calculation 2: MCMC fit
       |
       +-- f_phi ~ M_Pl consistent? ---> WEAKLY ECH-SPECIFIC
       |                                  (publishable as "Immirzi ALP")
       |
       +-- f_phi << M_Pl required? ----> IMMIRZI INTERPRETATION KILLED
                                          (publish as generic ALP constraints)
```

---

## Comparison to the alternatives

If Candidate C fails (Immirzi interpretation killed), the options are:

1. **Generic ALP birefringence paper.** Use existing MCMC infrastructure
   to constrain ALP parameters from birefringence + CMB + BAO. Publishable
   but not novel (many groups doing this).

2. **Dynamical CS gravity (Candidate A) for chiral GWs.** Requires r > 10^{-3}
   (LiteBIRD era). Long timeline, not ECH-specific. Could be combined with
   generic ALP (same field theta couples to both R R-tilde and F F-tilde
   through fermion loops).

3. **Close the parity program.** Add this result to Paper 1.2 as the final
   nail: even the most natural parity-violating extension (dynamical Immirzi)
   reduces to generic ALP phenomenology. The ECH framework is phenomenologically
   closed at all levels.

**My recommendation:** Pursue Calculation 1 (2-4 hours). If no new operators
appear, proceed directly to option 3 (close the parity program) and reframe
Paper 2 as either a generic ALP constraints paper or a comprehensive ECH
closure paper that includes the dynamical Immirzi result.
