# Branch Q: Order-of-Magnitude Screening

**Date:** 2026-03-16

---

## Screening Protocol

For each surviving candidate: answer four cheap-kill questions.

1. Does the source term actually generate phi != 0?
2. Is the coupling strong enough for observable effects?
3. Is it already excluded by existing data?
4. Is it generic (any ALP does this) or distinctive (ECH-specific)?

Kill any candidate that fails on questions 1 or 2.
Flag any candidate that fails on question 4 (generic but viable).

---

## Candidate A: Gravitational Chern-Simons

### Q1: Does theta-dot != 0?

The Pontryagin density R R-tilde = 0 on exact FRW. So theta has no
gravitational source on the background. theta-dot must come from:
- A potential V(theta): theta rolls due to V'(theta)
- Initial conditions: theta starts displaced from the minimum

If we give theta a potential (e.g., cosine from instantons), then
theta-dot != 0 at late times if theta is ultralight (m_theta ~ H_0).

**Verdict: CONDITIONAL.** Requires a potential or initial conditions
that are not determined by the CS coupling. The gravitational coupling
alone does not generate theta-dot on FRW.

### Q2: Is the coupling strong enough?

The CS modification to GW propagation is:

```
v_L - v_R ~ k * theta-dot / M_CS^2
```

where M_CS is the CS mass scale. For detectable chirality in the CMB
tensor spectrum:

```
Delta chi ~ (k / M_CS^2) * integral theta-dot dt ~ (k * Delta theta) / M_CS^2
```

With Delta theta ~ f_CS and k ~ 10^{-3} Mpc^{-1} (CMB scales):

```
Delta chi ~ f_CS * k / M_CS^2
```

For Delta chi ~ 0.1 (marginally detectable by LiteBIRD if r ~ 0.01):

```
f_CS / M_CS^2 ~ 100 Mpc ~ 10^{29} eV^{-1}
```

This requires M_CS ~ 10^{-14.5} eV * sqrt(f_CS / M_Pl), which for
f_CS ~ M_Pl gives M_CS ~ 10^{-14.5} eV ~ meV scale. This is allowed
by current constraints (binary pulsar bounds are in the strong-field
regime, not directly comparable).

**Verdict: MARGINAL.** Could work with ultralight theta and low M_CS,
but requires r > 10^{-3} (LiteBIRD threshold) to see any tensor mode
at all. Not testable with birefringence data (wrong observable).

### Q3: Already excluded?

Solar system: M_CS > O(10 km) in the non-dynamical limit (weak).
Binary pulsars: constraints on the dynamical theory are model-dependent.
CMB: no direct constraint on chiral tensors beyond r < 0.032.

**Verdict: NOT EXCLUDED** but weakly constrained.

### Q4: ECH-specific?

**NO.** Dynamical CS gravity is a standalone theory studied since 2003.
The ECH framework provides a motivation for theta (promoted Immirzi
parameter) but the observable predictions are identical to any other
dCS theory. The cs coupling theta R R-tilde exists independently of
torsion.

### SCREENING RESULT: SURVIVES but NOT ECH-SPECIFIC

---

## Candidate B: Standard ALP (bounce-sourced)

### Q1: Does phi != 0?

The bounce modifies the axion angle by Delta theta ~ 10^{-96} (Branch N).
This is a 96-order-of-magnitude kill. The bounce does not source the ALP.

phi != 0 requires SEPARATE initial conditions (misalignment) unrelated
to the bounce.

**Verdict: FAILS Q1 as an ECH-sourced mechanism.** Works as standard
ALP with externally supplied initial conditions.

### Q2: Coupling strong enough?

Yes, by construction. f_a ~ 10^{8}-10^{12} GeV gives beta ~ 0.35 deg
for Delta phi / f_a ~ 0.012 rad. This is the standard ALP window.

### Q3: Already excluded?

No. The ALP birefringence window is open and matches the data.

### Q4: ECH-specific?

**NO.** Zero ECH content. The ALP exists independently. The bounce
contributes nothing.

### SCREENING RESULT: KILLED as ECH extension. Survives as generic ALP.

---

## Candidate C: Dynamical Barbero-Immirzi Field

This is the critical candidate. The screening must be done carefully.

### Q1: Does phi != 0?

If phi has a potential V(phi) = Lambda^4 [1 - cos(phi/f_phi)] from
instantons, then phi starts at a random initial angle and rolls to
the minimum. For ultralight m_phi ~ 10^{-33} eV (dark energy scale),
phi is still rolling today. phi-dot != 0: YES.

But where does the potential come from? In the standard QCD axion,
instantons generate the potential. For the Immirzi field, the potential
would come from gravitational instantons (euclidean gravity path
integral). The scale would be:

```
Lambda_grav ~ M_Pl * exp(-S_inst) ~ M_Pl * exp(-M_Pl^2 / Lambda_UV^2)
```

For Lambda_UV ~ M_Pl: Lambda_grav ~ M_Pl * exp(-1) ~ 10^{18} GeV (too heavy).
For Lambda_UV ~ 10 TeV: Lambda_grav ~ M_Pl * exp(-10^{26}) ~ 0 (effectively zero).

Gravitational instantons give either an enormous mass (phi frozen at
minimum, no birefringence) or a negligible mass (phi effectively
massless, no late-time roll unless displaced).

The only way to get m_phi ~ H_0 ~ 10^{-33} eV is FINE-TUNING the
instanton scale: Lambda ~ (H_0 f_phi)^{1/2} ~ 10^{-12} eV for
f_phi ~ 10^{18} GeV. This requires a non-gravitational instanton
with an extremely specific scale.

**Verdict: CONDITIONAL.** phi != 0 requires a finely tuned potential
that the ECH framework does not predict. The existence of phi is
geometrically motivated, but the potential (and therefore phi-dot)
must be put in by hand.

### Q2: Is the induced coupling strong enough?

This is the KEY calculation. The Immirzi field phi couples to fermions
through torsion elimination:

```
L_phi-psi = -(1/f_phi) * partial_mu phi * J^{5,mu} * (correction factor)
```

The correction factor comes from the phi-dependent torsion elimination.
To leading order in phi/f_phi:

```
L = -(1/f_phi) * partial_mu phi * J^{5,mu} + O(phi^2/f_phi^2)
```

Through the standard ABJ anomaly, this generates the effective
phi-photon coupling:

```
L_{phi-gamma} = (alpha_EM / (4 pi f_phi)) * N_eff * phi * F F-tilde
```

where N_eff = sum_f Q_f^2 = 8 (three SM generations, same as Branch S).

The birefringence angle is:

```
beta = (alpha / (4 pi f_phi)) * N_eff * Delta phi / 2
     = (alpha * N_eff / (8 pi)) * (Delta phi / f_phi)
```

For Delta phi / f_phi ~ O(1) (order-one misalignment):

```
beta ~ (1/137) * 8 / (8 pi) ~ (8 / (137 * 25))
     ~ 0.0023 radians ~ 0.13 degrees
```

This is within a factor of 3 of the observed 0.35 degrees!

Wait -- this is a remarkable coincidence, but it is the SAME coincidence
for ANY ALP with derivative coupling to fermions. The coupling
alpha/(4 pi f_phi) with f_phi such that Delta phi/f_phi ~ O(1) gives
beta ~ alpha/(4 pi) ~ 10^{-3} radians ~ 0.06 degrees, order-of-magnitude
compatible with observation. This works for ANY ALP, not specifically
for the Immirzi field.

The key question is: what sets f_phi? In the Immirzi field interpretation,
f_phi is the scale at which gamma(x) = gamma_0 + phi/f_phi varies
significantly. If gamma is an O(1) parameter (as in LQG, gamma ~ 0.274),
then phi/f_phi ~ O(1) at the PLANCK SCALE, meaning f_phi ~ M_Pl ~ 10^{18} GeV.

With f_phi ~ M_Pl:

```
beta ~ alpha * N_eff * Delta phi / (8 pi M_Pl)
```

For Delta phi ~ M_Pl (Planckian field excursion):

```
beta ~ alpha * 8 / (8 pi) ~ alpha / pi ~ 0.0023 rad ~ 0.13 deg
```

This is numerically compatible! But note:
- It requires a Planckian field excursion (Delta phi ~ M_Pl)
- The coupling is alpha/(4 pi M_Pl) ~ 10^{-21} GeV^{-1}
- This is within the allowed ALP parameter space but NOT specific to ECH

For f_phi << M_Pl (sub-Planckian decay constant):

```
beta ~ (alpha * N_eff / (8 pi)) * (Delta phi / f_phi)
```

which can be made to fit for any f_phi with appropriate Delta phi.

**Verdict: COUPLING IS STRONG ENOUGH** with f_phi ~ M_Pl and O(1)
misalignment. But this is not an ECH prediction -- it is the standard
ALP result with the ABJ anomaly coefficient.

### Q3: Already excluded?

For f_phi ~ M_Pl and m_phi ~ 10^{-33} eV:
- Not excluded by laboratory axion searches (coupling too weak)
- Not excluded by astrophysics (Planck-suppressed)
- Consistent with birefringence data
- Consistent with BBN (Delta N_eff < 0.03 for Planck-mass ALP)

**Verdict: NOT EXCLUDED.**

### Q4: ECH-specific?

**The coupling strength is NOT ECH-specific.** The induced phi F F-tilde
coupling is the standard ABJ anomaly result, alpha/(4 pi f_phi), which
is the same for any ALP with derivative fermion coupling.

However, there are potentially distinctive features:

1. **phi = Immirzi field implies f_phi ~ M_Pl.** This is the ONLY case
   where the decay constant is theoretically determined (not a free
   parameter). f_phi ~ M_Pl is a prediction of the identification
   phi = delta gamma * M_Pl / gamma_0. This constrains beta through:
   ```
   beta ~ alpha * N_eff / (8 pi) * (Delta phi / M_Pl)
   ```
   For O(1) misalignment: beta ~ 0.1 degrees. Observable and close to data.

2. **Gravitational coupling correlation.** If the same field couples to
   R R-tilde (Pontryagin) and to F F-tilde (through fermion loops), the
   ratio of birefringence to GW chirality is fixed (no free parameter).
   But the GW chirality is undetectable with current r limits.

3. **No additional ALP-photon coupling.** In a generic ALP model, the
   phi F F-tilde coupling can be arbitrary. In the Immirzi field model,
   the ONLY phi-photon coupling comes through the fermion ABJ triangle.
   There is no direct phi F F-tilde term. This is a RESTRICTION, not
   an additional prediction.

**Verdict: WEAKLY ECH-SPECIFIC.** The identification f_phi ~ M_Pl is
the only potentially distinctive prediction. Everything else is standard
ALP phenomenology.

### SCREENING RESULT: SURVIVES. Best geometric motivation. Phenomenologically
equivalent to a standard ALP with f_a ~ 4 pi M_Pl / (alpha * N_eff) ~ 10^{21} GeV.

---

## Candidate D: Explicit phi F F-tilde

### Q1-Q4: All identical to Candidate B.

**SCREENING RESULT: KILLED as ECH extension (zero geometric content).**

---

## Candidate E: Explicit Parity-Breaking Mass Term

### Q1: Does S_0 != 0?

The linear coupling lambda S * J^5 sources S_0 from the fermion chiral
current. But:
- On FRW, J^5_spatial = 0 (isotropy)
- J^5_0 = n_5 = 0 at late times (no chiral asymmetry)
- Even at the bounce: J^5_0 ~ n_5 which is either zero (parity-even
  state) or free (undetermined initial condition)

After torsion elimination with the modified equation:
```
S_mu = -(kappa/4) C(gamma) J^5_mu + (lambda/m_T^2) J^5_mu
```
this just rescales the (J^5)^2 coefficient. No new physics.

**Verdict: FAILS Q1.** Does not generate S_0 != 0 from dynamics.

### SCREENING RESULT: KILLED.

---

## Candidate F: Nieh-Yan + Instanton

Reduces to Candidate C after field elimination. The non-topological
Nieh-Yan correction vanishes on FRW (T_0 = 0 in cosmological background,
Foundation B Phase 2).

**SCREENING RESULT: MERGED WITH C.** Same phenomenology.

---

## Candidate G: PGT Parity-Odd Bilinear

### Q1: Does this produce a nonzero parity-odd background?

The parity-odd torsion bilinear epsilon T T modifies the torsion
propagator and can split left/right modes of propagating torsion.
But it does NOT generate a nonzero torsion background. On FRW,
the background torsion is still determined by the (parity-even)
equations. The parity-odd term affects PERTURBATIONS only.

For torsion perturbations: yes, left/right splitting occurs.
But torsion perturbations must be sourced (need propagating torsion
with detectable amplitude), and the GW observable requires the
torsion mass to be accessible.

**Verdict: CONDITIONAL.** Requires propagating torsion at accessible
mass scale (not Planck mass). Subject to Branch L/M constraints.

### Q2: Strong enough?

For the GW chirality parameter:
```
Delta chi ~ c_PO * (m_T / M_Pl) * (k / m_T)
```
This is model-dependent. For m_T ~ meV (PTA band) and c_PO ~ O(1):
Delta chi ~ 10^{-30}. Undetectable.

For m_T in the CMB tensor band (k ~ 10^{-3} Mpc^{-1} ~ 10^{-29} eV):
this requires m_T ~ 10^{-29} eV (absurdly light torsion). The PGT
ghost-free conditions forbid this (minimum viable m_T is set by
stability).

**Verdict: FAILS Q2.** The coupling is too weak for any accessible
observation.

### SCREENING RESULT: KILLED.

---

## The Critical Question for Candidate C

### What is the INDUCED phi F F-tilde coupling from the Nieh-Yan vertex?

There are TWO routes to phi-photon coupling:

**Route 1: Through the derivative fermion coupling (standard ABJ)**

After torsion elimination, phi couples to J^5 through the derivative
coupling (1/f_phi) partial_mu phi * J^{5,mu}. The ABJ anomaly triangle
then gives:

```
g_{phi gamma gamma} = alpha * N_eff / (4 pi f_phi) = alpha * 8 / (4 pi f_phi)
                    = 2 alpha / (pi f_phi)
```

This is the STANDARD result. No ECH modification.

For f_phi = M_Pl: g_{phi gamma gamma} ~ 2 * (1/137) / (pi * 10^{18} GeV)
                                       ~ 5 * 10^{-21} GeV^{-1}

This gives birefringence:
```
beta = g_{phi gamma gamma} * Delta phi / 2
     = [alpha * N_eff / (4 pi f_phi)] * Delta phi / 2
```

For Delta phi ~ f_phi: beta ~ alpha * N_eff / (8 pi) ~ 0.002 rad ~ 0.1 deg

**This matches the observed 0.35 deg to within a factor of 3.**

**Route 2: Through the Nieh-Yan vertex at two loops**

The phi * N_4 coupling gives phi * T^I wedge T_I at the non-topological
level. After torsion elimination, this becomes phi * (J^5)^2, which is a
phi-dependent four-fermion operator. The two-loop diagram with TWO ABJ
triangles (one for each J^5 vertex connecting to photon lines) gives:

```
g_{phi gamma gamma}^{(2-loop)} ~ (alpha / pi)^2 * kappa * N_eff^2 / f_phi
                                ~ (alpha / pi)^2 * (1/M_Pl^2) / f_phi
```

This is DOUBLY suppressed: by (alpha/pi)^2 from two loops AND by 1/M_Pl^2
from the torsion elimination. For f_phi = M_Pl:

```
g^{(2-loop)} ~ (1/137)^2 * (1/pi^2) * (1/M_Pl^3) ~ 10^{-59} GeV^{-1}
```

This is 38 orders of magnitude weaker than Route 1.

**Conclusion: The Nieh-Yan vertex contributes NOTHING to the phi-photon
coupling. The entire effect comes from the standard derivative coupling
(Route 1), which is not ECH-specific.**

---

## Kill Summary

| Candidate | Q1 (source) | Q2 (strength) | Q3 (excluded?) | Q4 (distinctive?) | Verdict |
|-----------|-------------|---------------|----------------|-------------------|---------|
| A: Grav CS | Conditional | Marginal | No | NO | SURVIVES (non-ECH) |
| B: Standard ALP | FAILS (bounce irrelevant) | Yes | No | NO | KILLED as ECH |
| C: Dynamical Immirzi | Conditional (needs V) | YES | No | WEAKLY | **BEST SURVIVOR** |
| D: Explicit phi FF-tilde | Same as B | Yes | No | NO | KILLED as ECH |
| E: Explicit PV | FAILS | -- | -- | NO | KILLED |
| F: Nieh-Yan + inst. | = C | = C | = C | = C | MERGED with C |
| G: PGT parity-odd | Conditional | FAILS | -- | Partially | KILLED |

---

## Surviving Candidates After Screening

1. **Candidate C (dynamical Immirzi field):** Geometrically motivated,
   coupling strong enough, not excluded. BUT: phenomenologically equivalent
   to a standard ALP with f_a ~ 10^{21} GeV. The only ECH-specific feature
   is the theoretical identification f_phi ~ M_Pl and the restriction that
   phi-photon coupling MUST go through the ABJ anomaly (no direct phi F F-tilde
   allowed by the geometric embedding).

2. **Candidate A (gravitational CS):** Works for chiral GWs but requires
   r > 10^{-3} to detect. Not ECH-specific. Could be combined with C for
   a multi-messenger program.

**No candidate produces an observable that is BOTH accessible and
DISTINCTIVELY ECH.**
