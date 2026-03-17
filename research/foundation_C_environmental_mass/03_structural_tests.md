# Foundation C — Structural Test Framework

**Date:** 2026-03-14

---

## Tests

Each candidate action must pass ALL five structural tests to receive
a SURVIVES_PHASE1 verdict. Failure on any single test produces the
corresponding failure verdict.

---

## Test 1: Lock Test

### Question

Are m_eff and g_eff independently adjustable?

### Procedure

1. Compute m_eff(params, environment) and g_eff(params).
2. Compute R_ratio = m_eff / g_eff.
3. If R_ratio is constant in all Lagrangian parameters: **FAIL_LOCK**.
4. If R_ratio depends on at least one parameter (or on the environment
   independently of all coupling parameters): **PASS**.

### Key insight from Foundation A

The lock is a property of the RATIO m/g, not of individual values.
Curvature-dependent kinetic normalization does NOT break the lock
(Candidate E). Only INDEPENDENT mass contributions (not through the
shared kinetic normalization Z) can break it.

### Application to environmental mass

If m²_eff = m₀² + ξR and g = α/M_Pl:

```
R_ratio = √(m₀² + ξR) × M_Pl/α
```

This depends on R (environment), ξ, m₀, M_Pl, α. Unless all of
these are locked to each other, the ratio is adjustable. **PASS**
for candidates where m₀, ξ, and α are independent parameters.

But for PGT modes: m₀² ~ M_Pl²/|t₃| and α ~ 1/M_Pl√|t₃| share
the parameter t₃. The ξR correction is negligible. **FAIL_LOCK** in
practice (even if formally unlocked by ξR).

---

## Test 2: Duality Test

### Question

Does the mechanism require a pseudoscalar coupled to a topological
density for mass protection?

### Procedure

1. Identify the field type: scalar, pseudoscalar, vector, tensor.
2. If pseudoscalar: check whether mass protection requires coupling
   to an exact form. If yes: **FAIL_DUALITY** (topological-shift
   duality applies — mass protection and geometric content are
   mutually exclusive).
3. If scalar: identify the mass protection mechanism.
   - Conformal symmetry → PASS (no topological structure needed)
   - Gauge symmetry → PASS
   - No symmetry → proceed to naturalness test
4. If vector/tensor: analyze on a case-by-case basis.

### Key insight from Foundation B

The duality is SPECIFIC to pseudoscalars with linear Ω₄ couplings.
Scalars with conformal or gauge mass protection are NOT affected.
This is the primary reason Foundation C focuses on scalar fields.

---

## Test 3: Cosmological Background (FRW) Test

### Question

Does the environmental mass mechanism produce a nonzero, dynamically
relevant mass on FRW backgrounds?

### Procedure

1. Evaluate m²_eff on flat FRW: ds² = -dt² + a²(t)dx².
2. Compute the Ricci scalar: R = 6(Ḣ + 2H²).
3. Substitute into m²_eff(R).
4. Check:
   - Is m²_eff = 0 on FRW? → **FAIL** (mechanism inactive in cosmology)
   - Is m²_eff ≠ 0 but negligible compared to H²? → **FAIL**
   - Is m²_eff ~ O(H²)? → **PASS** (cosmologically relevant)
   - Is m²_eff >> H²? → check if field is too heavy to be relevant

### FRW Ricci scalar values

```
Radiation (w = 1/3):  R = 0
Matter (w = 0):       R = 3H²        [from R = 8πGρ(1-3w), H² = 8πGρ/3]
de Sitter (w = -1):   R = 12H²
Current epoch:        R ≈ 3Ω_m H₀² + 12Ω_Λ H₀² ≈ several H₀²
```

### Critical check

If the environmental term involves torsion (T) or non-metricity (Q)
evaluated on the FRW background:
- Background torsion: T₀ = 0 (no macroscopic spin density in FRW).
  Any T-dependent term VANISHES.
- Background non-metricity: Q₀ = 0 in standard MAG cosmology
  (unless the theory specifically sources it). Usually vanishes.

**Terms that depend on T or Q are NOT cosmologically relevant.**
Only terms depending on the metric curvature R(g) survive on FRW.

This is the lesson from Foundation B: the Q∧e∧T correction to N₄
vanishes on FRW because T₀ = 0.

---

## Test 4: Reduction Test

### Question

After all non-metric fields (torsion, non-metricity, auxiliary fields)
are eliminated via their field equations, does the effective action
for the remaining dynamical scalar reduce to a known scalar-tensor
theory?

### Procedure

1. Solve the algebraic field equations for torsion T and non-metricity Q
   (both are typically algebraic in quadratic gravity theories).
2. Substitute back into the action to obtain S_eff[g_μν, φ, matter].
3. Compare with known classes:
   - Brans-Dicke (ω parameter)
   - f(R) gravity (specific potential)
   - Quintessence (canonical scalar + potential)
   - Horndeski / beyond-Horndeski (higher derivative couplings)
   - Chameleon / symmetron (environment-dependent potential)

4. If S_eff matches a known class exactly: **FAIL_GENERIC_COLLAPSE**
   (the geometric origin is invisible in the EFT).
5. If S_eff has novel structure not captured by existing classes:
   **PASS** (potential for distinctive predictions).

### Why this matters

The universality of scalar EFT means that at low energies, all
weakly coupled scalars look similar regardless of their UV origin.
A geometric origin is a UV completion, not an IR signature. For the
geometric origin to matter observationally, the reduction must
produce specific parameter relations or novel coupling structures
that a generic scalar-tensor theory cannot reproduce.

---

## Test 5: Naturalness Test

### Question

Is the small effective mass (m_eff ~ H₀) technically natural?

### Procedure

1. Identify the symmetry (if any) restored when m₀ = 0:
   - Conformal symmetry? → natural (ξ is fixed, m₀ protected)
   - Gauge symmetry? → natural (m₀ = 0 by gauge invariance)
   - Shift symmetry? → need to check compatibility with ξRφ²
   - No symmetry? → compute radiative corrections

2. If no protecting symmetry: compute the leading radiative correction:
   ```
   δm₀² ~ g² Λ_UV² / (16π²)
   ```
   If δm₀² >> ξR ~ H², the mechanism is fine-tuned.

3. Check for hidden fine-tunings:
   - Does any Lagrangian parameter need to be ~H₀ ~ 10⁻³³ eV?
   - Is a large hierarchy (> 10¹⁰) required in any coupling?
   - Is the mechanism stable under small perturbations of parameters?

4. If fine-tuning FT > 10¹⁰: **FAIL_NATURALNESS**.
5. If FT < 10¹⁰ with symmetry protection: **PASS**.

---

## Verdict Categories

| Verdict | Meaning |
|---------|---------|
| **FAIL_LOCK** | Mass and coupling remain tied. Environmental correction negligible. |
| **FAIL_DUALITY** | Mechanism relies on pseudoscalar + topological coupling. Foundation B obstruction applies. |
| **FAIL_FRW** | Environmental term vanishes or is negligible on FRW. Not cosmologically relevant. |
| **FAIL_GENERIC_COLLAPSE** | Reduces to known scalar-tensor EFT after elimination. No geometric fingerprint. |
| **FAIL_NATURALNESS** | Small mass requires tuning a parameter to ~H₀ with no symmetry protection. |
| **SURVIVES_PHASE1** | Passes all five tests. Proceeds to Phase 2 detailed analysis. |

### Combined verdict logic

```
FAIL on Test 1 → FAIL_LOCK (stop)
FAIL on Test 2 → FAIL_DUALITY (stop)
FAIL on Test 3 → FAIL_FRW (stop)
PASS on Tests 1-3 + FAIL on Test 4 → FAIL_GENERIC_COLLAPSE
PASS on Tests 1-4 + FAIL on Test 5 → FAIL_NATURALNESS
PASS on all 5 → SURVIVES_PHASE1
```

Note: FAIL_GENERIC_COLLAPSE is not a hard stop — the mechanism works
as dark energy, it just doesn't provide anything new beyond known
scalar-tensor models. This is a "success as physics, failure as novelty"
outcome.
