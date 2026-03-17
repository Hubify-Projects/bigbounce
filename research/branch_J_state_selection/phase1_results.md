# Branch J Phase 1 Results: Bounce-Triggered State Selection

**Date:** 2026-03-16

---

## Verdict: BRANCH_J_CLOSED

---

## What Was Tested

Whether the spin-torsion bounce can dynamically select, prepare,
or kick an independently existing dark-energy sector into a
specific late-time state — via vacuum branch selection,
misalignment setting, metastable trapping, symmetry re-breaking,
or nonadiabatic excitation.

Five candidate mechanisms were constructed, tested against five
structural criteria (J1–J5), and screened at order-of-magnitude
level.

---

## Results by Candidate

| Candidate | J1 Strength | J2 Not IC | J3 Natural | J4 Narrow | J5 Viable | Status |
|-----------|:-----------:|:---------:|:----------:|:---------:|:---------:|--------|
| A: pNGB misalignment | PASS | MARGINAL | FAIL | FAIL | PASS | DEAD |
| B: Multi-vacuum | PASS | FAIL | FAIL | MARGINAL | PASS | DEAD |
| C: Symmetry re-breaking | PASS | FAIL | FAIL | FAIL | PASS | DEAD |
| D: Metastable trapping | PASS | FAIL | FAIL | MARGINAL | PASS | DEAD |
| E: Nonadiabatic excitation | PASS | PASS (weak) | FAIL | FAIL | FAIL | DEAD |

**No candidate passes all five tests.**
**No candidate survives OOM screening.**

---

## The Three Structural Barriers That Close Branch J

### Barrier 9: Hamiltonian Phase-Space Conservation (Liouville)

The bounce is a Hamiltonian scattering event occurring near
H = 0 (negligible friction). Liouville's theorem guarantees
that the mapping from pre-bounce to post-bounce states preserves
phase-space volume. The bounce ROTATES dark-sector initial
conditions but cannot CONTRACT them to a predictive outcome.

For state selection to work, phase-space contraction is required
(many initial conditions → few outcomes). This needs dissipation
or irreversibility, both absent at the bounce instant.

### The Naturalness Dilemma (reinforcing Barriers 1–7)

Any curvature coupling strong enough to affect the dark sector
at the bounce (ξ ~ O(1)) generates Planck-scale radiative
corrections to the DE mass (δm² ~ ξM_Pl²), destroying the DE
potential structure. A coupling weak enough to preserve the DE
sector (ξ ~ 10⁻¹²⁴) is far too weak for state selection.

### Scale Separation (reinforcing Barrier 5)

The 10⁶¹ hierarchy between M_Pl and m_DE prevents:
- Parametric resonance (frequency mismatch)
- Meaningful field evolution during the bounce (t_Pl ≪ 1/m_DE)
- Nonadiabatic effects at DE frequencies (ω̇/ω² ~ 0 for DE modes)

---

## The Ninth Barrier

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  BARRIER 9: Hamiltonian phase-space conservation        │
│                                                         │
│  The bounce is a Hamiltonian scattering event at H ≈ 0. │
│  Liouville's theorem prevents phase-space contraction.  │
│  The bounce rotates dark-sector states but cannot       │
│  select them. Combined with the naturalness dilemma,    │
│  this closes ALL curvature-coupled state-selection      │
│  mechanisms for DE-scale dark sectors.                  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

This joins the eight previous barriers:

1. Mass-coupling lock (A) — propagating torsion
2. Topological-shift duality (B) — pseudoscalar protection
3. Scalar-tensor universality (C) — FRW reduction
4. Planck suppression (D) — connection coupling
5. Scale separation (E) — global integrals
6. Attractor-sensitivity dilemma (F) — initial conditions
7. Parameter immunity (G) — vacuum selection
8. Parity-even effective interaction (H) — tensor chirality
9. **Hamiltonian phase-space conservation (J) — state selection**

---

## Why the Verdict Is CLOSED, Not WEAK

### The closure is structural, not parametric

The Liouville barrier is a theorem of classical mechanics,
not an estimate. It holds for ANY Hamiltonian system regardless
of coupling strength, potential shape, or bounce profile. No
parameter choice evades it.

### The closure is comprehensive

All five candidate mechanisms fail. The three barriers
(Liouville, naturalness, scale separation) cover the entire
space of curvature-coupled state-selection mechanisms. No
candidate was found that even partially survives.

### The closure is not evadable within the minimal model

The only escapes from Liouville (dissipation, decoherence,
non-perturbative topology change) require physics BEYOND the
minimal EC model:
- Dissipation: requires additional light fields or a thermal bath
  coupled to the dark sector (not in minimal model)
- Decoherence: requires environmental coupling (suppressed by
  10⁻¹²⁰ for gravitationally coupled sectors)
- Topology change: requires non-perturbative quantum gravity
  (beyond semiclassical EC)

---

## Assessment Against Success Criteria

| Criterion | Met? |
|-----------|------|
| S1: Bounce changes dark-sector state | YES (curvature kick) |
| S2: Not arbitrary initial conditions | **NO** (Liouville) |
| S3: Technically natural | **NO** (ξ dilemma) |
| S4: Predictive narrowing | **NO** (rotation, not contraction) |
| S5: Late-time DE viability | YES (for A, B, C, D) |

Two of five criteria met. The two that pass (S1, S5) are the
easy ones. The three hard criteria (S2, S3, S4) all fail.

---

## What Branch J Adds to the Program

### New barrier identified

Barrier 9 (Hamiltonian phase-space conservation) is a genuinely
new obstacle, distinct from previous barriers. It applies
specifically to state-selection mechanisms and complements the
scale-separation barrier (which applies to energy-budget
mechanisms).

### Deeper understanding of why bounce→DE fails

The nine barriers now cover THREE distinct failure modes:

1. **Energy-budget failure** (Barriers 1–7): The bounce cannot
   produce or energetically constrain DE.

2. **Signature failure** (Barrier 8): The bounce cannot produce
   distinctive observable imprints.

3. **State-selection failure** (Barrier 9): The bounce cannot
   select or narrow DE initial conditions.

These three modes exhaust the logical space of bounce→DE
connections:
- Direct derivation: closed (A–G)
- Observable signatures: closed (H)
- Compatibility constraints: weak (I)
- State selection: closed (J)

### Mildly interesting negative results

1. **Metastable vacuum anti-trapping:** For ξ < 0, the bounce
   DESTROYS metastable DE vacua (Toy 3). This means bouncing
   cosmologies with ξ < 0 are incompatible with metastable
   vacuum DE. This is a mild negative constraint (not on the
   bounce, but on DE models in bouncing cosmologies).

2. **H = 0 causal connection:** The infinite Hubble radius at
   the bounce means perfect causal connection, which PREVENTS
   topological defect formation (Kibble mechanism requires
   causal disconnection). Bouncing cosmologies naturally
   suppress monopoles, domain walls, and cosmic strings formed
   at the bounce.

---

## Overall Program Status

| Branch | Route | Verdict |
|--------|-------|---------|
| A–G | Direct bounce → DE derivation | CLOSED (7 barriers) |
| H | Observable tensor signatures | CLOSED (amplitude + parity) |
| I | DE compatibility constraints | WEAK (scale separation) |
| J | State selection | CLOSED (Liouville + naturalness) |

**All four logical routes from bounce to dark energy are now
closed or negligible for the minimal spin-torsion bounce.**

The conclusion is comprehensive: the minimal Einstein-Cartan
bounce and dark energy are INDEPENDENT phenomena. The bounce
cannot produce, constrain, imprint, or select dark energy.
Nine structural barriers, spanning three failure modes, prevent
any nontrivial bounce→DE connection.

---

## Summary Table

| Item | Result |
|------|--------|
| Candidates tested | 5 (pNGB, multi-vacuum, symmetry, metastable, nonadiabatic) |
| Candidates surviving screening | **0** |
| New barrier identified | YES: Barrier 9 (Hamiltonian phase-space conservation) |
| Strongest candidate | A (pNGB misalignment) — still fails J2, J3, J4 |
| Weakest candidate | C (symmetry re-breaking) — fails J2, J3, J4 |
| Bounce capable of nontrivial state selection? | **NO** |
| Genuinely different from closed IC branch? | Partially (Liouville argument is new) but same conclusion |
| Phase 2 recommended? | **NO** |
| Overall verdict | **BRANCH_J_CLOSED** |
| Recommended next move | Write comprehensive closure paper |
