# Computation Sequence: What to Derive, in Order

**Status:** NOT STARTED
**Purpose:** Concrete checklist of derivations, each building on the previous

---

## Computation 1: Canonical Action Memo

**Input:** Hehl 1976, Freidel+ 2005, Mercuri 2006
**Output:** Explicit S_total in first-order variables

Equations to write down:
- Full action with all terms and coupling constants
- Torsion decomposition into irreducible parts
- Identification of which parts couple to fermions

**Estimated effort:** 1 week (mostly literature synthesis)

---

## Computation 2: Torsion Elimination

**Input:** Computation 1
**Output:** Reduced action S_reduced[g, ψ] with no torsion variables

Equations to derive:
- Torsion EOM with Holst term
- Explicit solution T^I_{μν}[ψ̄, ψ, γ]
- Substitution back into action
- Four-fermion coupling constants G_V(γ), G_A(γ), G_VA(γ)

Key check: When γ → ∞, must recover standard EC result (G_VA → 0).

**Estimated effort:** 1–2 weeks
**Tools:** By hand or xAct (Mathematica)

---

## Computation 3: Fierz Rearrangement + Auxiliary Fields

**Input:** Computation 2
**Output:** Action with auxiliary scalar σ and pseudoscalar π

Equations to derive:
- Fierz identity for (ψ̄ γ^μ γ⁵ ψ)² in terms of (ψ̄ψ)², (ψ̄ iγ⁵ψ)², etc.
- Same for the parity-odd cross-term
- Hubbard-Stratonovich transformation introducing σ, π
- Tree-level potential V_tree(σ, π) = σ²/(4G_s) + π²/(4G_p) + (cross terms from G_VA)

Key result: The parity-odd coupling G_VA introduces a σ-π mixing term that breaks the Z₂ symmetry π → −π. This is what could generate ⟨π⟩ ≠ 0.

**Estimated effort:** 1 week

---

## Computation 4: One-Loop Effective Potential

**Input:** Computation 3 + choice of background spacetime
**Output:** V_eff(σ, π; R, H) at one loop

### 4a: Flat spacetime first (warm-up)

Fermion determinant:
```
V_1-loop = -i Tr ln [iγ^μ ∂_μ - m - σ - iγ⁵ π]
```

Standard result (NJL model):
```
V_1-loop = -N_c N_f / (8π²) × [(m+σ)² + π²]² × [ln((m+σ)² + π²)/Λ² - 1/2]
```

Check: does the gap equation have a nontrivial solution?

### 4b: Curved spacetime (the real calculation)

Use Schwinger-DeWitt / heat-kernel expansion:

```
V_1-loop = -(1/2)(4π)^{-2} Σ_n a_n(D) × Λ^{4-2n}
```

where a_n are the Seeley-DeWitt coefficients of the Dirac operator:
```
D = iγ^μ D_μ - M_eff(σ, π)
```

The curvature corrections enter through:
- a₁ ∝ R (Ricci scalar)
- a₂ ∝ R², R_μν R^μν, R_μνρσ R^μνρσ

**Critical:** The curvature R near the bounce is ~ M_Pl². This means the curvature-dependent terms in V_eff could be enormous at early times and catalyze symmetry breaking.

**Estimated effort:** 3–4 weeks (the hardest single computation)

---

## Computation 5: Gap Equation and Condensate

**Input:** Computation 4
**Output:** (σ*, π*) = solution of ∂V_eff/∂σ = ∂V_eff/∂π = 0

Solve numerically (or analytically in limiting cases):
```
σ* = 2G_s × ⟨ψ̄ψ⟩|_{σ*, π*}
π* = 2G_p × ⟨ψ̄ iγ⁵ψ⟩|_{σ*, π*}
```

**Key question:** Is π* ≠ 0? (pseudoscalar condensate)

If π* ≠ 0 AND σ* ≠ 0: both chiral and parity symmetry spontaneously broken. Maximum vacuum energy contribution.

If π* = 0: parity-odd sector does not condense. Theory lacks the "memory" mechanism.

**Estimated effort:** 1–2 weeks (numerical)

---

## Computation 6: IR Persistence Test (THE CRITICAL TEST)

**Input:** Computation 5
**Output:** Does V_eff(σ*, π*) survive when the fermion spin density → 0?

**Procedure:**
1. Solve gap equation at high curvature (R ~ M_Pl²) — this is the bounce epoch
2. Track the solution as R → 0 (matter/radiation era)
3. At late times, set the explicit spin source to zero
4. Check: does (σ*, π*) ≠ 0 persist?

The condensate is self-sustaining if V_eff(σ, π) has a local minimum at (σ*, π*) ≠ 0 even in flat spacetime, **provided** the system was prepared in that minimum by early-universe dynamics. This is the standard "quench" mechanism in condensed matter.

**Three possible outcomes:**
1. **Minimum persists:** Condensate is metastable or absolutely stable. Vacuum energy survives. **SUCCESS.**
2. **Minimum exists but system tunnels out:** Condensate has finite lifetime. Could still work if lifetime > age of universe.
3. **No minimum in flat spacetime:** Condensate relaxes to zero. **FAILURE** of the condensate route.

**Estimated effort:** 2–3 weeks

---

## Computation 7: Vacuum Stress Tensor

**Input:** Computations 5–6 (assuming success)
**Output:** T_μν^eff and w(a)

Derive:
```
T_μν = (2/√-g) δΓ_eff/δg^μν
     = -V_eff(σ*, π*) g_μν + (kinetic corrections)
```

For a frozen condensate: w = −1 exactly.
For a slowly varying condensate: w = −1 + ε(a), compute ε.

**Estimated effort:** 1 week

---

## Computation 8: Radiative Stability

**Input:** Computation 7
**Output:** Is V_eff(σ*, π*) stable under higher-order corrections?

Checks:
- Two-loop correction to V_eff
- RG running of G_s, G_p, G_VA
- Naturalness: is ρ_vac protected by a symmetry? (e.g., if the condensate spontaneously breaks a symmetry, the Goldstone theorem constrains radiative corrections)

**Estimated effort:** 3–4 weeks

---

## Total Computation Timeline

| # | Computation | Weeks | Cumulative |
|---|-------------|-------|-----------|
| 1 | Canonical action | 1 | 1 |
| 2 | Torsion elimination | 1–2 | 3 |
| 3 | Fierz + auxiliary fields | 1 | 4 |
| 4 | One-loop V_eff | 3–4 | 8 |
| 5 | Gap equation | 1–2 | 10 |
| 6 | IR persistence test | 2–3 | 13 |
| 7 | Stress tensor | 1 | 14 |
| 8 | Radiative stability | 3–4 | 18 |

**Total: ~18 weeks of focused computation** (not counting writing, iteration, or getting stuck)

---

## Decision Points (Mapped to Three Gates)

| After Computation | Gate | Question | If YES | If NO |
|-------------------|------|----------|--------|-------|
| 4–5 | **Gate 1** | Does V_eff have a minimum with π* ≠ 0? | Condensate exists; proceed to Gate 2 | Try gravitational catalysis, multiple species; if still no, STOP — condensate mechanism fails |
| 6 | **Gate 2** | Does the minimum survive when R → 0, spin source → 0? | Vacuum persists; proceed to Gate 3 | Framework is phenomenological — publish as transient condensate if interesting |
| 7 | **Gate 3** | Is V_eff(σ*, π*) > 0, cutoff-independent, w ≈ −1? | **GREEN LIGHT** — first-principles dark energy | Partial results may still be publishable (see `06_canonical_problem_statement.md`) |
| 8 | (stability) | Is the result radiatively stable? | Full program success | Result exists but may be fine-tuned |

See `06_canonical_problem_statement.md` for precise success/failure criteria at each gate.
