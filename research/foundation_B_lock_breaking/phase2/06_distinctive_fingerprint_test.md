# Foundation B Phase 2 — Distinctive Fingerprint Test (DR3)

**Date:** 2026-03-14

---

## Purpose

Determine whether any of the Phase 2 toy actions produce predictions
that distinguish them from a generic (non-geometric) ALP. This is
Decision Rule 3 (DR3): a viable geometric dark-energy model must
predict at least one observable that a generic scalar/pseudoscalar
model cannot.

---

## What Counts as a Distinctive Fingerprint

A "geometric fingerprint" must be:

1. **Derived from geometry:** The prediction must follow from the
   geometric origin of the coupling (torsion, non-metricity, curvature),
   not from ad hoc parameter choices.

2. **Not reproducible by parameter tuning:** A generic ALP with freely
   chosen couplings must not be able to match the prediction by simply
   adjusting its parameters.

3. **In principle observable:** The prediction must be testable
   (at least in principle) by existing or planned experiments.

---

## Fingerprint Analysis by Toy Action

### Toy I/II: theta-N_4 coupling (direct or + instanton)

**Candidate fingerprint: Environment-dependent mass**

In these actions, the non-topological piece alpha theta Q wedge e wedge T
generates an environment-dependent mass for theta:

```
m^2(x) = m_0^2 + delta m^2(x)

where delta m^2(x) ~ alpha^2 Q(x) T(x) / (a_1 a_2)
```

In regions with torsion (spin-polarized matter, neutron star interiors),
theta acquires additional mass. In vacuum, delta m = 0.

**Is this distinctive?**

NO — for two reasons:

1. **Chameleon/symmetron mechanisms** produce the same qualitative
   effect (environment-dependent mass) from a scalar potential with
   matter coupling. The geometric origin is not uniquely diagnostic.

2. **The specific form** delta m^2 ~ Q * T requires both non-metricity
   and torsion to be present. In practice, both are sourced by matter
   (spin density for T, hypermomentum for Q), so delta m^2 ~ (matter)^2.
   A generic scalar with a rho^2-dependent potential gives the same
   scaling.

**Verdict: NOT DISTINCTIVE.** The qualitative effect exists but is
phenomenologically identical to non-geometric chameleon mechanisms.

### Toy III: Derivative coupling with dual channels

**Candidate fingerprint: Correlated axial + conformal couplings**

Toy III has two independent couplings:
- g_axial ~ alpha / (a_1 sqrt(Z)): coupling to fermion axial current
- g_conf ~ beta / (a_2 sqrt(Z)): coupling to trace of stress-energy

A generic ALP typically couples to EITHER the axial current (via
theta F F-tilde in gauge theory) OR to the trace of T_mu_nu (via
conformal coupling). Having BOTH couplings is uncommon but not
impossible in generic ALPs.

**Is this distinctive?**

WEAK — for these reasons:

1. **A generic ALP CAN have both couplings.** There is no symmetry
   principle forbidding both. String theory compactifications routinely
   produce ALPs with multiple couplings.

2. **The ratio g_axial/g_conf = (alpha a_2)/(beta a_1) is a free parameter**
   in MAG (alpha and beta are independent coupling constants). So MAG
   does not predict a SPECIFIC ratio — it only predicts the existence
   of both couplings.

3. **The distinctive claim** would be that MAG REQUIRES both couplings
   to be present (if the gravitational action has both T^2 and Q^2
   terms). But the coupling constants alpha and beta could independently
   be zero, so this is not a robust prediction.

**Verdict: MARGINALLY DISTINCTIVE.** The coexistence of both couplings
is suggestive but not uniquely geometric. A generic ALP with two coupling
constants can mimic this exactly.

### Possible stronger fingerprint: Coupling universality

In MAG, the torsion and non-metricity couple to ALL matter fields
through the covariant derivative. This means the ALP-matter coupling
is UNIVERSAL (same coupling to all fermions), not flavor-dependent.

A generic ALP can have different couplings to different fermion
species. The geometric origin enforces universality.

**Is this distinctive?**

POTENTIALLY — but:

1. **Universality is testable** (e.g., by comparing ALP-electron and
   ALP-nucleon couplings in different experiments).

2. **But** the QCD axion ALSO has approximately universal couplings
   (from its coupling to QCD instantons). So universality alone does
   not uniquely point to geometry.

3. **The prediction is conditional** on the ALP being detected AND its
   couplings to multiple fermion species being measured — a very
   challenging experimental program.

**Verdict: CONDITIONALLY DISTINCTIVE.** Universality is a prediction
but not a smoking gun.

---

## The Real Problem: Generic ALP Coupling After Field Elimination

The fundamental issue across all toy actions is:

**After torsion and non-metricity are eliminated from the MAG field
equations, the geometric couplings reduce to standard ALP-matter
couplings.**

Specifically:
- d(theta) wedge e wedge T -> (after T elimination) -> d(theta) * (psi-bar gamma_5 psi)
  This is a standard ALP-fermion derivative coupling.
- d(theta) wedge Q wedge e wedge e -> (after Q elimination) -> d(theta) * T_mu^mu
  This is a standard conformal coupling.

Neither retains a signature of its geometric origin. The geometry
determines the EXISTENCE and relative STRUCTURE of the couplings
but not their absolute values or any uniquely geometric observable.

---

## Comparison: What Would a Genuine Geometric Fingerprint Look Like?

A truly distinctive geometric dark-energy mechanism would predict:

1. **A specific mass-coupling relation** (not just that they're
   independent, but a precise functional relationship derived from
   geometry). Model B does not provide this — alpha, beta, a_1, a_2
   are all free parameters.

2. **A coupling that does NOT reduce to standard ALP form** after
   field elimination. For example, a coupling to spacetime curvature
   that persists as a non-minimal gravitational coupling (like f(R)
   theories). Model B's couplings DO reduce to standard form.

3. **Violation of the equivalence principle** at a level set by the
   geometric sector. In MAG, the non-metricity can produce WEP
   violations through the hypermomentum coupling. But these effects
   are generically tiny (suppressed by M_Pl) and not specific to the
   ALP sector.

4. **CMB birefringence with a specific spectral shape** determined
   by the geometric coupling structure (not just an overall rotation
   angle). Model B's birefringence is standard ALP birefringence
   (frequency-independent rotation) — not distinctive.

---

## DR3 Verdict

| Fingerprint candidate | Distinctive? | Reason |
|----------------------|-------------|--------|
| Environment-dependent mass | No | Mimicked by chameleon |
| Dual axial + conformal coupling | Marginal | Generic ALP can have both |
| Coupling universality | Conditional | QCD axion also universal |
| Specific mass-coupling relation | No | Too many free parameters |
| Non-standard coupling form | No | Reduces to standard ALP |
| WEP violation | No | Generic to non-metricity, not ALP-specific |
| CMB birefringence shape | No | Standard ALP birefringence |

**Overall DR3 assessment: FAILS.**

No distinctive geometric fingerprint survives field elimination.
The toy actions produce viable ALP dark-energy candidates, but their
predictions are indistinguishable from a non-geometric ALP with
appropriately chosen parameters.

---

## Implication for Foundation B

The DR3 failure means that even though the mass-coupling lock IS
broken in Model B (confirmed by the symbolic analysis), and the
Nieh-Yan form IS non-topological in MAG (confirmed by the algebraic
calculation), the resulting theory does not produce a DISTINCTIVE
geometric dark-energy mechanism.

The physics works. The lock breaks. The mass can be natural. But the
output — after all geometric fields are eliminated — is a generic ALP.
The geometric origin is invisible at low energies.

This is not a failure of the MAG framework. It is a consequence of
the universality of the ALP effective field theory: at low energies,
ALL weakly coupled pseudoscalars look like ALPs, regardless of their
UV origin. The geometric origin is a UV completion, not an IR signature.

---

## Is There Any Way Forward?

Three possibilities for future investigation (not pursued here):

1. **Non-perturbative geometric effects:** If torsion condensation
   produces topological defects (domain walls, strings) with specific
   geometric properties, these could provide distinctive signatures.
   But this requires strong-coupling dynamics beyond current tools.

2. **Gravitational-wave signatures:** The MAG corrections to the
   gravitational wave equation (from non-metricity) could produce
   distinctive propagation effects (birefringence, anomalous dispersion)
   that correlate with the ALP sector. But these are generically tiny.

3. **Multi-messenger correlations:** If the ALP mass is truly
   environment-dependent (from the Q*T term), there could be
   correlations between ALP phenomenology and the local gravitational
   environment that a generic ALP would not predict. But measuring
   this requires detecting the ALP AND mapping the local torsion/
   non-metricity field — currently impossible.

None of these rise to the level of a near-term distinctive prediction.
