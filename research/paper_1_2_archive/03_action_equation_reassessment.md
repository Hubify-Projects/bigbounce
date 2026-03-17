# Action and Equation Reassessment Note

**Date:** 2026-03-13
**Author:** Houston Golden
**Purpose:** Technical inventory of which equations, operators, and actions
from Paper 1.01 survive, which are retired, and what next-generation
templates are worth considering.

---

## 1. Equations and Actions: Survival Classification

### Category A: Survive as Useful Reference Phenomenology

These equations are mathematically correct, observationally useful, and do
not overclaim. They survive in Paper 1.2 but are relabeled as
phenomenological or background material.

| Equation | Description | Paper 1.01 Role | Paper 1.2 Role |
|----------|-------------|-----------------|----------------|
| ECH action (eq:ECH) | S_grav + S_ferm with Holst term | Foundation | Background starting point |
| Barbero-Immirzi (eq:gamma) | gamma = 0.274 from LQG | Key parameter | Background parameter |
| Torsion definition (eq:torsion) | T^I = de^I + omega^I_J wedge e^J | Definition | Definition |
| Reduced action (eq:Sreduced) | S_EH + S_Dirac + S_4f after torsion elimination | Derived result | Derived, but context of "this is as far as the minimal model goes" |
| Four-fermion term (eq:Sfour) | L_4f = -G_eff (J^mu)^2, perfect square | Key derived result | Key derived result, now with context: "this is where all gamma-dependence lives, and it is insufficient for dark energy" |
| Modified Friedmann (eq:modfriedmann) | H^2 = (8piG/3)(rho + rho_Lambda) | Framework | Standard + ansatz (rho_Lambda from phenomenological scaling) |
| MCMC parameters (eq:H0, eq:s8, eq:S8result) | H_0 = 69.2, sigma_8 = 0.785, etc. | Key results | Phenomenological LCDM-extension fits (survive) |

### Category B: Retired as Central Foundation

These equations were presented or implied as foundational to the
dark-energy mechanism. They are no longer defensible in that role.

| Equation | Description | Why Retired |
|----------|-------------|-------------|
| L_eff = Xi M_Pl^2 + c_omega omega^2 (eq:Leff) | Effective dark-energy Lagrangian | The scaling story is not a derivation; w=-1 is assumed; the source operator vanishes at late times. Survives only as a phenomenological ansatz with heavy caveats. |
| rho_Lambda = Xi M_Pl^4 (eq:gdp) | Inflationary dilution | Same: motivated scaling, not a mechanism. Does not address scale naturalness. |
| E-B cross-correlation (eq:ClEB) | CMB birefringence from parity-odd operator | No derived photon coupling. The formula is standard birefringence theory, not a prediction of the framework. |
| One-loop effective action Gamma[e] (eq:Gam) | Fermion determinant | gamma-independent after torsion elimination. No novel content at this order. |
| Condensate order parameter (implicit in Sec 4) | VEV of psi-bar i gamma^5 psi | S/P channel repulsive at gamma=0.274. Route closed. |

### Category C: Candidates to Generalize into Next-Generation Models

These equations or structures contain ideas worth carrying forward, but
they need to be embedded in a richer theoretical context.

| Structure | What to Generalize | Direction |
|-----------|-------------------|-----------|
| ECH action with Holst term | The connection sector is too constrained (algebraic torsion). Generalize to propagating torsion/connection. | Foundation A |
| Nieh-Yan 4-form coupling | Topological in 4D, so washes out. Generalize to non-topological parity-odd invariants, or move to D != 4. | Foundation B |
| Four-fermion perfect-square structure | Constrained channel structure is real physics. Could become more interesting with non-minimal couplings or in a propagating-torsion background. | Foundation A or D |
| Parity-odd vacuum operator | The operator itself is real. The problem is that its source vanishes and no mechanism preserves the VEV. Generalize to a framework where the VEV is protected. | Foundation C |

---

## 2. Three Next-Generation Action Templates

### Template 1: Propagating Torsion / Poincare Gauge Theory

**Action:**
```
S = integral [ (1/2kappa^2) * (a_0 R + sum_I a_I R_I^2 + sum_J b_J T_J^2)
               + S_matter ]
```

where R_I^2 are the six independent quadratic curvature invariants of the
Lorentz connection (3 parity-even, 3 parity-odd), and T_J^2 are the three
independent torsion-squared invariants.

**Motivation:**
In Poincare gauge theory (PGT), the most general gravitational Lagrangian
quadratic in torsion and curvature has 10 free parameters. The spin
connection is dynamical — torsion propagates. The spectrum generically
contains massive spin-2 and spin-0 torsion modes in addition to the
massless graviton.

**Why it avoids at least one old failure mode:**
Algebraic torsion (Lesson 1) is eliminated by construction. Torsion is a
genuine dynamical field with its own equation of motion, propagator, and
spectrum. It does not wash out after "elimination" because there is nothing
to eliminate — the connection is an independent dynamical variable.

**Biggest risk:**
Ghost instabilities. The PGT spectrum analysis (Sezgin-van Nieuwenhuizen
1980, Yo-Nester 1999, 2002, Karananas 2015, Blagojevic-Cvetkovic 2018)
shows that most parameter choices lead to ghosts or tachyons. The ghost-free
parameter subspace is small and not fully mapped. A propagating torsion mode
that is ghost-free, massive, light, and cosmologically relevant may not
exist.

**Concrete next step:**
Map the ghost-free parameter subspace of the PGT action. For each ghost-free
point, compute the torsion mass spectrum. Check whether any ghost-free
massive torsion mode has a mass light enough (m ~ H_0 ~ 10^{-33} eV) to
be cosmologically relevant. This is a well-defined technical problem.

**Key references:**
- Blagojevic & Hehl (2013): Gauge Theories of Gravitation (textbook)
- Yo & Nester (1999, 2002): Hamiltonian analysis of PGT
- Nikiforova, Randjbar-Daemi, Rubakov (2009): massive torsion modes
- Karananas (2015): unitarity constraints on PGT

---

### Template 2: Symmetry-Protected Geometric Pseudoscalar

**Action:**
```
S = S_EH + integral [ -(1/2) f^2 (partial theta)^2
                       - lambda_NY theta N_4[T]
                       - lambda_P  theta P_4[R]
                       + V_NP(theta) ]
    + S_matter[g, psi, theta]
```

where theta is a pseudoscalar with a discrete Z_N or continuous shift
symmetry, N_4 is the Nieh-Yan density (modified to be non-topological,
e.g., through boundary-term-breaking or dimensional construction), P_4 is
the Pontryagin density, V_NP is a non-perturbatively generated potential,
and the matter coupling is constrained by the symmetry.

**Motivation:**
The dynamical Immirzi field (Route T1) failed because the Nieh-Yan density
is exact in 4D, so the coupling washes out. But a pseudoscalar with a
*different* coupling structure — or one where the Nieh-Yan coupling is made
non-topological by going beyond 4D or beyond the metric-compatible case —
could retain non-trivial geometric content.

The shift symmetry theta -> theta + const protects the pseudoscalar mass.
V_NP is generated non-perturbatively (analogous to QCD instantons for the
axion) and breaks the shift symmetry weakly, giving theta a naturally small
mass.

**Why it avoids at least one old failure mode:**
ALP collapse (Lesson 3) is avoided IF the coupling to N_4 or P_4 is
non-topological and retains geometric information after reduction. The shift
symmetry addresses scale protection (Lesson 5). The key question is whether
the coupling structure can be made genuinely non-generic.

**Biggest risk:**
This may be the dynamical Immirzi route in better clothing. The burden is
entirely on the claim that the modified N_4 coupling is non-topological
and retains geometric fingerprints. If it doesn't, the model reduces to
a generic ALP and Route T1's closure applies.

**Concrete next step:**
Investigate whether the Nieh-Yan density can be made non-topological in
metric-affine gravity (where the connection is not metric-compatible). In
the metric-affine case, the Nieh-Yan form is NOT an exact differential, and
its coupling to a pseudoscalar does not reduce to a boundary term. This is
a precise mathematical question with a checkable answer.

**Key references:**
- Mercuri (2009): Peccei-Quinn for Barbero-Immirzi
- Bombacigno, Boudet, Montani (2023): non-topological Nieh-Yan in
  metric-affine gravity
- Chatzistavrakidis, Karagiannis, Manousselis (2022): torsion in
  metric-affine gravity

---

### Template 3: Vacuum Sequestering via Geometric Constraint

**Action:**
```
S = integral [ (M_Pl^2/2) R sqrt(-g) d^4x
               + L_matter sqrt(-g) d^4x ]
    subject to: integral sqrt(-g) d^4x = fixed (unimodular constraint)
    or subject to: Lambda = (1/V_4) integral L_vac sqrt(-g) d^4x
                   (global sequestering)
```

More concretely, in the Kaloper-Padilla framework extended to include
torsion:
```
S = integral [ sigma_1 (epsilon_IJKL e^I e^J F^KL + Lambda_1 epsilon_IJKL e^I e^J e^K e^L)
               + sigma_2 mu^4 ]
    + S_matter[g, psi]
```
where sigma_1, sigma_2 are global (non-dynamical, spacetime-constant)
variables that enforce a sequestering constraint: the vacuum energy
contributions from matter loops are absorbed into sigma_1 and do not
gravitate.

**Motivation:**
The fundamental problem is not generating a vacuum energy — it is
explaining why it is small. Sequestering mechanisms enforce, at the level
of the action's global structure, that radiative corrections to the
cosmological constant do not gravitate. The effective cosmological constant
is determined by the boundary conditions of the universe, not by local
QFT contributions.

The geometric/torsion content enters through the first-order formulation:
the sequestering constraint naturally fits into the Palatini/first-order
framework where the connection and tetrad are independent variables.

**Why it avoids at least one old failure mode:**
Scale naturalness (Lesson 5) is addressed directly. The small scale is not
generated by a dynamical mechanism but is protected by a global structural
constraint. The mechanism does not require a propagating degree of freedom
that might wash out (partially addressing Lesson 1, though the mechanism
is fundamentally different in character from the propagating-mode route).

**Biggest risk:**
1. Weinberg's no-go theorem (1989): any local, Lorentz-invariant adjustment
   mechanism for Lambda fails. Sequestering evades this by being global
   (non-local), but this non-locality is itself controversial.
2. Fine-tuning of initial conditions: Kaloper-Padilla sequestering has been
   criticized (Burgess, Padilla debates) for requiring specific initial
   conditions.
3. Observational content: pure sequestering sets Lambda to a small value
   but may not predict any distinctive observable beyond "Lambda is small."
   This would satisfy DR2 but may fail DR3.

**Concrete next step:**
Review the Kaloper-Padilla sequestering mechanism in its first-order
(Palatini/EC) formulation. Determine whether the torsion sector modifies
the sequestering constraint in a non-trivial way. This is a specific
calculation: write down the sequestering action in first-order EC gravity,
solve the global constraint equations, and check whether torsion
contributes.

**Key references:**
- Kaloper & Padilla (2014, 2016): vacuum energy sequestering
- Kaloper, Padilla, Stefanyszyn, Zahariade (2016): sequestering in
  first-order gravity
- Weinberg (1989): the cosmological constant problem (no-go)
- Padilla (2015): review of approaches to the cosmological constant

---

## 3. Summary Table

| Template | Avoids Which Failure | Biggest Risk | First Check |
|----------|---------------------|-------------|-------------|
| 1. Propagating torsion (PGT) | Wash-out (L1), ALP collapse (L3) | Ghosts | Ghost-free mass spectrum |
| 2. Symmetry-protected pseudoscalar | ALP collapse (L3), scale (L5) | ALP disguise | Is non-metric N_Y non-topological? |
| 3. Vacuum sequestering | Scale naturalness (L5) | Weinberg no-go, no observable | Torsion-modified sequestering constraint |

---

## 4. What This Note Does NOT Do

- It does not claim any template is correct
- It does not propose a new model
- It does not contain new calculations
- It identifies concrete, checkable questions for each template
- It provides a starting point for Phase 1 assessments of next-generation
  foundations, using the same disciplined methodology (canonical problem
  statements, gates, failure modes) that produced the four clean closures
