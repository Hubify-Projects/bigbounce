# Branch O: Structural Tests

**Date:** 2026-03-16

---

## Test O1 — Irreversibility Test

**Question:** Is there a genuinely non-Hamiltonian or hysteretic
ingredient in the mechanism?

**What passes:**
- Bubble nucleation with Γ > 0 and entropy production ΔS > 0
- Particle production with |β_k|² > 0 for relevant modes
- Thermalization converting coherent → thermal DOF
- Quantum tunneling through a barrier
- Hysteretic first-order transition with latent heat

**What fails:**
- Classical field evolution on a potential (Hamiltonian)
- Adiabatic evolution (reversible by definition)
- "Phase-space rotation" (Liouville-preserving maps)
- Scattering with deterministic outcome
- Any process where time-reversal returns to the initial state

**Verdict labels:**
- PASS_O1: genuinely irreversible step identified and quantified
- FAIL_NO_IRREVERSIBILITY: mechanism is secretly Hamiltonian

**Relationship to Branch J:**
Branch J failed precisely because all five candidates were
Hamiltonian. Test O1 is the FIRST filter: anything that fails
O1 is Branch J recycled and immediately dead.

---

## Test O2 — Bounce-Essential Test

**Question:** Would the same irreversible transition occur without
the bounce? Specifically: in a standard inflationary cosmology
with reheating, does the same hidden-sector phase transition
happen with comparable or better predictivity?

**What passes:**
- A transition that REQUIRES curvature R > R_crit where R_crit
  is achieved at the bounce but not during inflation or radiation era
- A process that depends on the SPECIFIC time profile of R(t) at
  the bounce (e.g., the rapid rise and fall, H passing through zero)
- A coupling to the spin density S ~ M_Pl³ or (J⁵)² that has no
  analog in standard cosmology
- A transition that depends on the CONTRACTING phase preceding
  the bounce (no analog in inflation)

**What fails:**
- A transition triggered by high temperature T > T_c, since
  T_reheat after inflation can exceed T_c for any reasonable T_c
- A transition triggered by Hubble friction H > H_c, since
  H_inf > H_c for most scales
- A transition that depends only on the expansion rate (generic
  to any FRW cosmology)
- Gravitational particle production that occurs equally during
  inflation

**Verdict labels:**
- PASS_O2: bounce provides qualitatively different transition
  dynamics
- MARGINAL_O2: bounce modifies timing/rate but doesn't change
  qualitative outcome
- FAIL_NOT_BOUNCE_SPECIFIC: any hot cosmology does the same

**The standard comparison:**
For the bounce at ρ_crit ~ M_Pl⁴ (ECH), the comparison is with
inflation at H_inf ~ 10¹⁴ GeV (energy density ρ_inf ~ 10⁻¹⁰ M_Pl⁴).
The bounce wins by 10¹⁰ in energy density but loses in DURATION
(t_Pl vs 10⁻³⁴ s for 60 e-folds, a factor of 10⁹). The total
energy-time product:

```
(ρ × t)_bounce ~ M_Pl⁴ × t_Pl = M_Pl³ ~ 10⁵⁴ GeV³
(ρ × t)_inflation ~ 10⁻¹⁰ M_Pl⁴ × 10⁹ t_Pl = 10⁻¹ M_Pl³ ~ 10⁵³ GeV³
```

Comparable. The bounce has higher peak energy but shorter duration.
For processes that depend on PEAK energy (tunneling), the bounce
may win. For processes that depend on DURATION (thermalization),
inflation wins.

---

## Test O3 — Arbitrary-Branch Collapse Test

**Question:** Does the mechanism actually select a specific vacuum,
or does it leave multiple vacua equally accessible?

**What passes:**
- A mechanism where the bounce biases nucleation rates such that
  one vacuum is exponentially preferred (Γ_1/Γ_2 ~ exp(ΔS_E) ≫ 1)
- A trapping mechanism where the field is locked in a specific
  minimum with tunneling rate Γ_escape ≪ H₀⁴
- A thermal selection where one vacuum is the unique thermal
  ground state at T_h

**What fails:**
- Z_N symmetric vacua with equal nucleation rates (each equally
  likely → no selection)
- Random thermal fluctuations determining the vacuum (stochastic,
  unpredictive)
- Multiple nearly-degenerate vacua with no mechanism to prefer one
- Metastable trapping where the specific minimum depends on initial
  conditions (Liouville recycled)

**Verdict labels:**
- PASS_O3: specific vacuum exponentially preferred or uniquely
  selected
- MARGINAL_O3: modest preference (factor of few) for one vacuum
- FAIL_ARBITRARY_BRANCH: multiple vacua equally accessible

---

## Test O4 — Naturalness/Protection Test

**Question:** Is the late-time vacuum energy technically natural?
Does the mechanism avoid introducing new fine-tuning?

**What passes:**
- Vacuum energy protected by a symmetry (supersymmetry, shift
  symmetry, sequestering)
- Vacuum energy set by dimensional transmutation (exponentially
  small from O(1) couplings)
- Vacuum energy in a landscape where the selected branch
  AUTOMATICALLY has small ρ_DE (e.g., nearly-degenerate vacua
  with ΔV ~ (meV)⁴ protected by approximate symmetry)

**What fails:**
- ρ_DE depends on a hidden-sector parameter that must be tuned
  to 10⁻¹²² (tuning moved, not eliminated)
- ρ_DE depends on the number of vacua N with N ~ 10¹²² required
  (anthropic landscape recycled, not a bounce prediction)
- The hidden-sector potential has a flat direction that must be
  lifted to exactly (2.3 meV)⁴ (quintessence tuning recycled)
- Radiative corrections from the bounce coupling destabilize the
  DE vacuum (Branch J naturalness dilemma recycled)

**The key diagnostic:** Write ρ_DE in terms of fundamental
parameters. If ρ_DE ~ f(g_i, m_i, M_Pl) where f requires ANY
argument to be tuned to ≪ 1, the test fails. If ρ_DE ~ Λ⁴_h
with Λ_h a dynamically generated scale (like Λ_QCD), the test
passes — but then Λ_h must be explained.

**Verdict labels:**
- PASS_O4: vacuum energy protected or naturally small
- MARGINAL_O4: modest tuning required (10⁻¹⁰ or less)
- FAIL_NO_PROTECTION: tuning of 10⁻⁶⁰ or worse required

---

## Test O5 — Predictive Narrowing Test

**Question:** Does the bounce significantly narrow the late-time
vacuum state compared to "anything goes"?

**What passes:**
- A quantitative relation: ρ_DE = f(ρ_crit, m_T, ...) with f
  determined by the mechanism
- A discrete selection: out of N vacua, exactly one is selected
  by the bounce, with the vacuum energy of that one computable
- A strong correlation: bounce parameters → hidden-sector reheat
  temperature → specific transition → specific vacuum

**What fails:**
- The vacuum is selected but its energy is unconstrained
- Multiple vacua survive and the relative occupancy is unknown
- The prediction is ρ_DE ∈ [0, M_Pl⁴] (trivially satisfied)
- The prediction depends on unknown hidden-sector parameters
  with equal or greater uncertainty than ρ_DE itself

**Quantitative criterion:** The mechanism must reduce the
uncertainty in ρ_DE by at least a factor of 10⁶⁰ compared to
the naive range [0, M_Pl⁴]. This means the predicted ρ_DE must
be within a factor of 10⁶² of (2.3 meV)⁴. Even this modest
criterion is extremely difficult to meet.

**Verdict labels:**
- PASS_O5: ρ_DE predicted to within a few orders of magnitude
  of the observed value
- MARGINAL_O5: vacuum branch selected but ρ_DE within branch
  uncertain by > 10 orders of magnitude
- FAIL_NO_NARROWING: no quantitative narrowing achieved

---

## Test O6 — Late-Time Viability Test

**Question:** Does the resulting vacuum state produce acceptable
dark energy?

**Requirements:**
- w ≈ -1 (within current bounds: -1.03 < w < -0.97 at 95% CL)
- ρ_DE ~ (2.3 meV)⁴
- No ghost instability (kinetic term positive)
- No gradient instability (sound speed c_s² ≥ 0)
- Stable on cosmological timescales (Γ_decay ≪ H₀)
- Compatible with fifth-force constraints
- Compatible with BBN/CMB constraints on additional radiation

**What passes:**
- A true vacuum with V > 0 and no light propagating DOF (pure CC)
- A metastable vacuum with lifetime ≫ t_universe
- A slowly-rolling field with w ≈ -1 (quintessence-like)

**What fails:**
- A vacuum with V < 0 (AdS, collapse)
- A vacuum with V ≫ (2.3 meV)⁴ (wrong energy scale)
- A metastable vacuum with lifetime < t_universe (catastrophic decay)
- A field with w ≠ -1 ruled out by data
- Light hidden-sector states that conflict with BBN/CMB N_eff bounds

**Verdict labels:**
- PASS_O6: viable DE with all constraints satisfied
- MARGINAL_O6: some constraints satisfied, others unchecked
- FAIL_LATE_TIME: clear conflict with observations

---

## Combined Verdict Logic

```
IF any test gives FAIL → candidate is DEAD at that test

Possible combined verdicts:
- SURVIVES_PHASE1: passes O1–O3, at least MARGINAL on O4–O6
- MIXED: passes O1–O2, fails or marginal on O3–O6
- DEAD: fails O1 or O2 (fundamental, non-negotiable)

For Branch O overall:
- BRANCH_O_PROMISING: ≥ 2 candidates SURVIVE_PHASE1
- BRANCH_O_MIXED: 1 candidate SURVIVES_PHASE1
- BRANCH_O_WEAK_BUT_WORTH_ONE_TEST: 0 survive but 1 is MIXED with
  a clear calculation that could promote or kill it
- BRANCH_O_CLOSED: all candidates DEAD at O1 or O2
```

---

## The Hard Truth About These Tests

Tests O1 and O2 are the existential ones. O1 separates Branch O
from Branch J (which failed Liouville). O2 separates bounce
cosmology from generic cosmology.

A mechanism that passes O1 but fails O2 is a valid cosmological
mechanism — it's just not a BOUNCE mechanism. It works in
inflation too. This is useful physics but not useful for the
spin-torsion program.

A mechanism that passes O1 and O2 but fails O4 has reproduced
the CC problem in a hidden sector. This is not progress; it's
relabeling.

The combination O1 + O2 + O4 is the real killer. History suggests
that almost nothing passes all three simultaneously.
