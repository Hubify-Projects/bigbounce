# Branch H: Priority Ranking

**Date:** 2026-03-15

---

## Top 3 Directions

### Priority 1: Tensor Perturbation Spectrum Through the Bounce

**Why this is #1:**
- Blue-tilted gravitational wave spectrum is THE signature that
  distinguishes bounce from inflation
- Inflationary consistency relation n_T = -r/8 predicts RED tilt
- Any detection of BLUE tilt immediately favors bounce models
- The computation is well-defined: solve tensor perturbation
  equations through the modified Friedmann background

**What to compute:**
1. Tensor perturbation equation with ρ² correction:
   ```
   h̄'' + 2(a'/a)h̄' + k²h̄ = 0
   ```
   where a(η) solves the modified Friedmann equation through bounce
2. Bogoliubov coefficients: amplification factor for each mode k
3. Power spectrum P_T(k) and spectral tilt n_T(k)
4. Energy density Ω_GW(f) today after redshifting

**Required inputs:**
- Equation of state during contraction (radiation? matter? ekpyrotic?)
- Bounce profile a(t) from modified Friedmann equation
- Matching conditions at the bounce

**Timeline:** 2–4 weeks for analytic + numerical computation

**Risk:** If pre-bounce equation of state is unconstrained, the
prediction is model-dependent. The BOUNCE ITSELF always gives blue
tilt at the bounce scale, but the LOW-k behavior depends on
pre-bounce history.

---

### Priority 2: Parity Violation and Gravitational Leptogenesis

**Why this is #2:**
- Spin-torsion coupling is intrinsically parity-violating
- This is SPECIFIC to Einstein-Cartan (not shared by generic
  bouncing cosmologies like LQC or ekpyrotic)
- The 2.4σ hint of cosmic birefringence (Planck EB) is tantalizing
- Connection to leptogenesis gives additional testable prediction

**What to compute:**
1. Parity-violating action at the bounce:
   ```
   S_PV ~ ∫ √g  ε^{μνρσ} T_μ T_ν R_ρσ  (or similar)
   ```
2. Gravitational leptogenesis rate from torsion at bounce
3. Resulting baryon asymmetry η_B
4. Propagation of parity violation to CMB observables

**Required inputs:**
- Fermion content at the bounce (Standard Model + possible BSM)
- Torsion profile T^μ(t) through the bounce
- Sphaleron rate in the radiation era

**Timeline:** 4–6 weeks (more complex, involves particle physics)

**Risk:** The signal may be too small after propagation from Planck
to CMB scale. The connection between bounce-era torsion and
recombination-era birefringence is indirect.

---

### Priority 3: Full Perturbation Theory Through the Bounce

**Why this is #3:**
- Necessary for ANY comparison with CMB data
- Scalar spectrum determines n_s, A_s predictions
- Non-Gaussianity shape is a discriminator between bounce models
- Requires solving the coupled scalar-tensor perturbation system

**What to compute:**
1. Scalar perturbation equation with ρ² correction
2. Mukhanov-Sasaki variable through the bounce
3. Power spectrum P_S(k), spectral index n_s(k), running α_s(k)
4. Bispectrum B(k₁, k₂, k₃) and f_NL shape function

**Required inputs:**
- Full pre-bounce + bounce + post-bounce background
- Equation of state transitions
- Matching conditions for perturbations

**Timeline:** 6–10 weeks (most technically demanding)

**Risk:** High model-dependence on pre-bounce phase. May not
produce distinctive signature without specifying full cosmological
history.

---

## Recommended Execution Order

```
IMMEDIATE (next 2 weeks):
  Priority 1 — Tensor perturbations through the bounce
  Deliverable: P_T(k), n_T, Ω_GW(f)

SECOND (weeks 3–6):
  Priority 2 — Parity violation / leptogenesis
  Deliverable: η_B prediction, birefringence angle estimate

THIRD (weeks 7–12):
  Priority 3 — Full scalar perturbation theory
  Deliverable: n_s, A_s predictions with bounce
```

## What NOT to Do

- Do NOT reopen any DE connection (A–G closed)
- Do NOT attempt to constrain Λ from the bounce
- Do NOT add new fields or symmetries — study the MINIMAL EC bounce
- Do NOT run MCMC until analytic predictions are in hand

## Decision Point After Priority 1

If the tensor spectrum computation shows:
- **Blue tilt detectable by LISA/ET/BBO:** Branch H is promising → proceed
- **Blue tilt only at f > 10¹⁰ Hz:** Unobservable → Branch H is
  theoretical only → shift resources to Branch I
- **Spectrum degenerate with inflation for all pre-bounce models:**
  Branch H has no distinctive observational program → close

---

## Relationship to Existing MCMC Infrastructure

The MCMC pipeline (236,622 samples, 64 chains, R̂−1 < 0.005)
constrained the PHENOMENOLOGICAL parameters of Paper 1. These
constraints remain valid as generic scalar-tensor bounds.

New MCMC is NOT needed until:
1. A specific bounce prediction (e.g., n_T) is computed
2. That prediction maps onto an observable with existing data
3. The parameter space is large enough to require sampling

For Priority 1, the computation is ANALYTIC + NUMERICAL ODE, not
statistical. MCMC comes later, if at all.
