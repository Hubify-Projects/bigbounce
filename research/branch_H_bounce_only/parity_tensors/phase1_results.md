# Parity-Violating Tensors Phase 1 — Results

**Date:** 2026-03-15

---

## Verdict: PARITY_SIGNATURE_CLOSED

---

## What Was Tested

Whether the minimal spin-torsion bounce (Einstein-Cartan gravity
+ Dirac fermions on FRW) produces a distinctive parity-violating
signature in the tensor perturbation spectrum.

Specifically tested:
1. All parity-odd structures in the effective action
2. Whether any produce a left/right tensor mode splitting
3. Whether FRW symmetry permits parity-odd tensor backgrounds
4. Whether the bounce itself breaks parity
5. Numerical verification of chirality = 0

---

## Key Results

### 1. No parity-odd tensor source exists in the minimal model

Six candidate mechanisms were analyzed:

| Candidate | Parity-odd? | In minimal EC? | Couples to tensors? |
|-----------|------------|---------------|-------------------|
| (J^5)² interaction | NO | YES | — |
| n_5 background | YES | Conditional | NO |
| Holst/Immirzi | Rescales only | YES | NO |
| Dynamical Nieh-Yan | YES | NO (new field) | Yes (generic ALP) |
| Chern-Simons R̃R | YES | NO (new field) | Yes (not EC) |
| Chiral anomaly | YES | NO (quantum) | NO (R̃R = 0 on FRW) |

**None provide a parity-odd tensor source within the minimal
theory.**

### 2. The four-fermion interaction (J^5)² is parity-EVEN

The spin-torsion effective interaction is the product of two
pseudovectors, giving a scalar. This is the ONLY non-standard
term in the effective action, and it is parity-symmetric.

### 3. FRW isotropy kills all spatial parity-odd backgrounds

On a homogeneous, isotropic FRW background:
- ⟨J^5_i⟩ = 0 (isotropy eliminates spatial pseudovectors)
- The only pseudoscalar (n_5) does not couple to tensor modes
  because δJ^{5,0} = 0 from tensor perturbations

### 4. The bounce does not break parity

The bounce breaks TIME-REVERSAL symmetry (T), not spatial
PARITY (P). Tensor chirality requires P violation, which the
isotropic bounce does not provide.

### 5. Left and right tensor modes are identical

Numerically confirmed:

```
Δχ(k) = (P_L - P_R)/(P_L + P_R) = 0    (to machine precision)
```

Verified at k/k_b = 0.1, 0.2, 0.3, 0.5, 1.0.

For comparison, a toy Chern-Simons model (NOT in EC) produces
Δχ ~ 0.1–0.3, showing that the code correctly detects chirality
when present.

### 6. The Pontryagin density vanishes on FRW

```
R̃^{μν}_{ρσ} R^{ρσ}_{μν} = 0    on exact FRW
```

This eliminates gravitational leptogenesis from the bounce and
removes the gravitational chiral anomaly as a source of n_5.

### 7. All parity-related observables are zero

TB/EB correlations, chiral GW background, frequency-dependent
chirality, gravitational leptogenesis — all zero in the minimal
model.

---

## Why the Verdict is CLOSED (Not WEAK)

The parity signature is CLOSED, not merely WEAK, because:

1. The null result is STRUCTURAL, not parametric. It does not
   depend on the value of ρ_crit, γ, or any coupling constant.

2. The null result follows from three independent structural
   facts:
   - (J^5)² is parity-even (algebraic)
   - FRW isotropy kills spatial parity-odd quantities (geometric)
   - Tensor perturbations don't perturb J^{5,0} (kinematic)

3. There is no parameter regime or limiting case where the
   chirality becomes nonzero within the minimal model.

4. Every extension that WOULD produce chirality requires
   NEW PHYSICS beyond EC gravity, and the most natural extension
   (dynamical Immirzi field) was already closed by Foundation B.

---

## The Eighth Barrier

This result establishes a new structural barrier:

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│  BARRIER 8: Parity-even effective interaction           │
│                                                        │
│  The spin-torsion four-fermion interaction (J^5)² is   │
│  parity-EVEN despite arising from parity-odd torsion.  │
│  Squaring a pseudovector gives a scalar.               │
│  FRW isotropy eliminates all remaining parity-odd      │
│  backgrounds. No chirality in tensor observables.      │
│                                                        │
└────────────────────────────────────────────────────────┘
```

This joins the seven barriers from Foundations A–G:

1. Mass-coupling lock (A)
2. Topological-shift duality (B)
3. Scalar-tensor universality (C)
4. Planck suppression (D)
5. Scale separation (E)
6. Attractor-sensitivity dilemma (F)
7. Parameter immunity (G)
8. **Parity-even effective interaction (H-parity)**

---

## Implications for Branch H

### Tensor sector is now fully explored

| Route | Result | Barrier |
|-------|--------|---------|
| Tensor amplitude | P_T ~ 10⁻⁶⁴, n_T ≈ 0 | Scale separation |
| Tensor chirality | Δχ = 0 exactly | Parity-even interaction |

**Both the amplitude and the chirality routes are closed for the
tensor sector.**

### Remaining Branch H directions

| Direction | Status | Assessment |
|-----------|--------|-----------|
| Tensor amplitude | CLOSED | Unobservable |
| Tensor chirality | CLOSED | Zero in minimal model |
| Scalar perturbations | LIKELY CLOSED | Same amplitude problem + requires pre-bounce model |
| Non-Gaussianity | LIKELY WEAK | Same amplitude problem |

**Branch H is running out of directions.** The bounce is a
brief Planck-scale event on an isotropic background. Both
amplitude (scale separation) and symmetry (parity-even, FRW
isotropy) conspire against observable signatures.

### What remains potentially viable

The ONLY remaining possibility that has not been explicitly
closed is whether the bounce leaves an imprint through
SCALAR perturbation initial conditions (requiring a pre-bounce
contraction phase that IS NOT part of the minimal model). This
is outside the scope of the minimal spin-torsion bounce.

---

## Assessment Against Success Criteria

| Criterion | Met? |
|-----------|------|
| Parity-odd term in tensor equation | **NO** |
| Nonzero chirality asymmetry | **NO** |
| Effect not generic to radiation bounces | N/A (no effect) |
| Structurally distinctive signal | **NO** |

**Zero of four criteria met. Clean closure.**

---

## Summary

| Item | Result |
|------|--------|
| Parity-odd tensor source in EC? | **NO** |
| Left/right splitting? | **NO** (identical equations) |
| Chirality Δχ? | **0 (exact)** |
| Pontryagin density on FRW? | **0** |
| Gravitational leptogenesis? | **NO** |
| Any parity observable? | **ALL ZERO** |
| Requires new physics for chirality? | **YES** |
| Already-closed extension (Foundation B)? | YES (Nieh-Yan) |
| Verdict | **PARITY_SIGNATURE_CLOSED** |
