# Foundation B — Research Log

**Date:** 2026-03-14

---

## Session 1: Initial Survey and Symbolic Analysis

### What was done

1. Defined the mass-coupling lock problem precisely (01_problem_statement.md)
2. Identified five candidate model classes (02_candidate_model_classes.md)
3. Built a general lock analysis framework (03_lock_analysis_framework.md)
4. Implemented symbolic lock detection in SymPy (04_symbolic_model_exploration.ipynb)
5. Ran the lock diagnostic on four models: PGT baseline, Model A (Higgs portal),
   Model B (geometric ALP), Model C (two-field PGT)

### Symbolic results

**PGT 0⁻ baseline:**
```
R = m/g_eff = M_Pl² / (4√π)
dR/dt₃ = 0
```
R is independent of the only free parameter t₃. **LOCKED** (as expected).

Note: SymPy flags R as "depending on M_Pl" but M_Pl is fixed by observation
(Newton's constant), not a free parameter. So the lock holds.

**Model A (PGT + Higgs portal):**
```
R = M_Pl √(M_Pl² + 16πλv²) / (4√π)
dR/dλ ≠ 0, dR/dv ≠ 0
```
R depends on λ and v — parameters that g_eff does NOT depend on.
**UNLOCKED.** The mass can be adjusted via (λ, v) independently of the
coupling. BUT: making the mass small (m ~ meV) requires λv² ~ meV² —
a new hierarchy problem. No symmetry protects this scale.

Verdict: **PARTIALLY_UNLOCKED.**

**Model B (geometric ALP):**
```
R = Λ² / α
dR/dΛ ≠ 0, dR/dα ≠ 0
```
R depends on Λ (shift-symmetry-breaking scale) and α (Nieh-Yan coupling),
neither of which appears in the f-dependent coupling g_eff = α/f.
**UNLOCKED.** The mass m = Λ²/f → 0 as Λ → 0 while g = α/f stays finite.
At Λ = 0, the shift symmetry θ → θ + c is restored — **mass is technically
natural**.

Verdict: **FULLY_UNLOCKED** — IF the geometric theory produces this structure
with genuinely independent Λ and α.

**Model C (two-field PGT portal):**
```
R = M_Pl² √(16πλ_p + t₂) / (4√π √t₂)
dR/dt₂ ≠ 0, dR/dλ_p ≠ 0
```
R depends on t₂ and λ_p. **FORMALLY UNLOCKED.** But in PGT, λ_p is
determined by the same t_i couplings that set Z and μ. The ghost-free
conditions may impose relations that re-lock. Requires explicit ghost
analysis.

Verdict: **FORMALLY UNLOCKED, likely re-locked by PGT constraints.**

### Key findings

1. **The ALP architecture is the unique fully-unlocking structure.**
   Among the candidates tested, only the ALP-like structure
   (independent shift-symmetry-breaking scale + independent coupling
   constant) achieves m → 0 with g_eff finite AND mass technically
   natural. This is not a surprise — it is the QCD axion paradigm.

2. **The Higgs portal breaks the lock but transfers the hierarchy.**
   Model A is honest progress: the mass and coupling are independent.
   But the tiny mass requires a new small scale (λv²). This trades
   the t₃ ~ 10⁵⁸ hierarchy for a λv² ~ meV² hierarchy.

3. **The critical open question is geometric realization of the ALP structure.**
   Can a geometric theory (MAG, extended PGT, or other) produce a
   pseudoscalar with:
   - shift symmetry (protecting the mass)
   - geometric coupling to matter (independent of the symmetry-breaking scale)
   - non-topological content (surviving reduction, unlike Route T1)

   This is Foundation B's central question.

### What failed

Nothing failed in the sense of producing wrong results. The analysis
correctly identifies the landscape of possibilities.

### What survives

- **Model B (geometric ALP) is the primary candidate** for Phase 2.
  The mathematical first-check is: compute dN₄ in metric-affine gravity.
  If the Nieh-Yan form is non-topological (dN₄ ≠ 0 on shell), the
  pseudoscalar θ coupled to N₄ retains geometric content and the ALP
  structure is realized geometrically.

- **Model A (Higgs portal) is a backup** — it works structurally but
  requires additional input to solve the hierarchy.

### New ideas

1. **Composite geometric pseudoscalar.** Instead of a fundamental θ,
   consider a composite pseudoscalar formed from torsion bilinears
   (analogous to the η' in QCD). If torsion condensation produces
   a composite state, the mass could be set by the condensation
   scale (independent of the fundamental coupling). This connects
   to Track B (NJL) but in the propagating-torsion context rather
   than the algebraic-torsion context.

2. **Dimensional transmutation.** If the torsion sector has a
   non-trivial beta function, the running coupling could generate
   an exponentially small scale (like Λ_QCD from α_s). This would
   provide a natural small mass without a hierarchy. Requires
   computing the one-loop beta function for PGT torsion couplings.

3. **Environmental mass.** If the torsion mass depends on the
   cosmological background (e.g., through a coupling to the Ricci
   scalar R), the mass could be light today (R ~ H₀²) while heavy
   in the early universe. This is the chameleon/symmetron idea
   applied to torsion. The coupling would be independent of R,
   breaking the lock.

---

## Next steps (Phase 2)

1. **Compute dN₄ in MAG.** This is the first-check for Model B.
   Requires the definition of N₄ in the presence of non-metricity
   and the computation of its exterior derivative.

2. **Check PGT two-mode ghost constraints.** For Model C, determine
   whether the ghost-free parameter space allows independent control
   of two modes' masses and couplings.

3. **Evaluate the composite pseudoscalar idea.** Can torsion
   condensation in PGT produce a pseudo-Goldstone boson with the
   ALP structure?

4. **Check environmental mass mechanisms.** Can a torsion-curvature
   coupling m²(R) break the lock while avoiding fifth-force constraints?
