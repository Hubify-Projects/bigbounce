# Foundation C — Problem Statement

**Date:** 2026-03-14

---

## Why Previous Foundations Failed

### Foundation A: PGT propagating torsion (MASS-COUPLING LOCK)

The ghost-free PGT 0⁻ pseudoscalar mode has:

```
m = M_Pl / (4√(π|t₃|))
g = c / (M_Pl √|t₃|)

R = m/g = M_Pl² / (4√π) = constant
```

The ratio R is independent of all free parameters. Making the mode
light (m → 0 by |t₃| → ∞) simultaneously kills the coupling (g → 0).
The mass and coupling are structurally locked by sharing a single
normalization parameter.

### Foundation B: MAG Nieh-Yan pseudoscalar (TOPOLOGICAL-SHIFT DUALITY)

The mass-coupling lock CAN be broken by the ALP architecture
(m = Λ²/f, g = α/f), and the Nieh-Yan form IS non-topological
in metric-affine gravity. But a structural obstruction was discovered:

**Topological-Shift Duality:** For a pseudoscalar θ linearly coupled
to a geometric 4-form Ω₄:

- If Ω₄ is exact (topological): shift symmetry θ → θ + c preserved,
  mass protected, BUT no local geometric content survives → Route T1
- If Ω₄ is non-exact (non-topological): local geometric content
  present, BUT shift symmetry broken → mass unprotected

Furthermore: in cosmological FRW backgrounds (torsion T₀ = 0), the
non-topological correction Q∧e∧T vanishes. Model B = Route T1 in
cosmology.

After field elimination, all couplings reduce to generic ALP-matter
couplings. DR3 fails.

### The pattern of failure

Both failures share a common structure: the protection mechanism
for the mass (shift symmetry for pseudoscalars, kinetic normalization
in PGT) is entangled with the coupling mechanism. Breaking this
entanglement destroys the protection or the coupling.

---

## Why Environmental Mass Is a Logically Different Route

The environmental mass idea changes the question:

**Old question:** Can we find a globally tiny mass that is protected
by a symmetry AND has an independent coupling?

**New question:** Can we avoid needing a globally tiny mass at all,
by making the effective mass depend on the gravitational environment?

```
m²_eff(x) = m₀² + ξR(x) + (higher curvature terms)
```

On cosmological backgrounds: R ~ H₀² ~ (10⁻³³ eV)². If ξ ~ O(1)
and m₀ = 0 (protected by some symmetry), then m_eff ~ H₀ — the
dark energy scale emerges from the cosmological background itself.

In the solar system: R ~ GM_sun/r³ >> H₀², so the field is heavy
and decoupled from fifth-force experiments.

This is logically distinct from Foundations A and B because:

1. **No globally tiny mass is needed.** The mass is O(H), which is
   set by the cosmological background, not by a Lagrangian parameter.

2. **The protection question changes.** Instead of "why is m tiny?",
   the question becomes "why is m₀ = 0?" — which may have a
   symmetry-based answer (conformal symmetry, gauge symmetry).

3. **The topological-shift duality does not apply** if the field is
   a scalar (not pseudoscalar). Scalars do not need shift symmetry
   for mass protection — conformal or gauge symmetry suffices.

4. **The mass-coupling lock may be evaded** because the mass depends
   on the environment (R), not on the same Lagrangian parameters that
   control the coupling.

---

## Success Criteria

A successful Foundation C candidate must satisfy ALL of:

1. **LOCK_BROKEN:** m_eff and g_eff depend on independent parameters
   (or m_eff depends on the environment while g_eff does not).

2. **DUALITY_EVADED:** The mechanism does not require a pseudoscalar
   with shift symmetry coupled to a topological density. Either the
   field is a scalar (no shift symmetry needed) or the mass protection
   comes from a different symmetry.

3. **FRW_NONTRIVIAL:** The environmental mass term survives on FRW
   backgrounds and produces m_eff ~ O(H). If the environmental term
   vanishes on FRW (as the Q∧e∧T term does in Foundation B), the
   mechanism is NOT cosmologically relevant.

4. **NO_BARE_MASS_DOMINANCE:** The environmental mass ξR must not be
   negligible compared to a locked bare mass. If the bare mass is
   ~M_Pl (as in PGT), the correction ξR ~ H² is irrelevant. Either
   m₀ = 0 must be protected, or the bare mass must be independently
   small.

5. **NOT_GENERIC_SCALAR_TENSOR:** After field elimination, the theory
   must produce something beyond standard quintessence / Brans-Dicke /
   f(R) / chameleon models. If the geometric origin is invisible in
   the low-energy EFT, the mechanism fails DR3 (no distinctive
   geometric fingerprint).

6. **NO_GHOSTS:** The candidate must not obviously introduce ghost
   instabilities, tachyonic directions in field space, or violations
   of unitarity bounds.

---

## The Central Tension

There is an inherent tension in the success criteria:

- Criteria 1-4 are achievable by STANDARD scalar-tensor theories
  (conformally coupled scalar, quintessence with ξRφ²). These are
  well-studied and known to work.

- Criterion 5 requires something BEYOND standard scalar-tensor theory.
  This is where the geometric origin must matter.

The question is whether any geometric theory produces an environmental
mass mechanism that is structurally richer than the standard ξRφ²
coupling. If not, Foundation C reduces to "geometry gives you
quintessence" — which is true but not a new result.

---

## Candidate Field Types

| Field type | Mass protection | Lock? | Duality? | FRW? |
|------------|----------------|-------|----------|------|
| PGT 0⁻ pseudoscalar | Shift symmetry | LOCKED | APPLIES | Correction irrelevant |
| PGT 0⁺ scalar | None (bare mass ~M_Pl) | LOCKED | N/A | Correction irrelevant |
| Conformal scalar | Conformal symmetry | BROKEN | EVADED | R ≠ 0 on FRW |
| Scalaron (from R²) | R² origin | BROKEN | N/A | R ≠ 0 on FRW |
| Weyl vector trace | Weyl gauge symmetry | BROKEN | EVADED | R ≠ 0 on FRW |
| Torsion-curvature mixed | Unknown | Unknown | Unknown | Unknown |

The most promising candidates are the conformal scalar, scalaron, and
Weyl vector — all of which have symmetry-protected m₀ = 0 and survive
on FRW. But all three are variants of known scalar-tensor theories.
