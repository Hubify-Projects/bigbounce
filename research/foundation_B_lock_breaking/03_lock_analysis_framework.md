# Foundation B — Lock Analysis Framework

**Date:** 2026-03-14

---

## Purpose

A general procedure to determine whether any candidate geometric
dark-energy model exhibits the mass-coupling lock.

Given a Lagrangian L[φ, g_μν, Γ, matter], the framework outputs one of:

- **LOCKED:** m → 0 implies g_eff → 0. No independent control.
- **PARTIALLY_UNLOCKED:** m and g_eff have independent parameters, but
  the tiny mass is not technically natural (no protecting symmetry).
- **FULLY_UNLOCKED:** m and g_eff are independent AND m is technically
  natural or symmetry-protected.

---

## Step 1: Field Normalization

### Input
The Lagrangian in the form:

```
L = -½ Z_ij(p) ∂φ^i ∂φ^j - ½ M²_ij(p) φ^i φ^j + g_i(p) φ^i J^i + ...
```

where p = {p₁, p₂, ...} are the fundamental parameters of the theory
(coupling constants in the gravitational action).

### Procedure
1. Identify the kinetic matrix Z_ij(p).
2. Diagonalize and canonically normalize: φ^i_can = (√Z)_ij φ^j.
3. Express everything in terms of canonical fields.

### Output
The canonical Lagrangian with:
- Physical masses m_i(p)
- Physical couplings g_eff,i(p)
- Explicit parameter dependence of each

---

## Step 2: Mass Scaling

### Procedure
1. Express m_i as functions of the fundamental parameters p.
2. Identify which parameters m_i depends on: M_i = {p_a, p_b, ...}
   such that ∂m_i/∂p_a ≠ 0.
3. Identify the parameter subspace where m_i → 0 (the "light-mass
   limit"): L_i = {p : m_i(p) = 0}.

### Output
- The set M_i of parameters controlling each mass.
- The light-mass limit L_i as a submanifold of parameter space.

---

## Step 3: Coupling Scaling

### Procedure
1. Express g_eff,i as functions of the fundamental parameters p.
2. Identify which parameters g_eff,i depends on: G_i = {p_c, p_d, ...}
   such that ∂g_eff,i/∂p_c ≠ 0.
3. Evaluate g_eff,i on the light-mass limit L_i.

### Output
- The set G_i of parameters controlling each coupling.
- The value of g_eff,i restricted to L_i.

---

## Step 4: Lock Detection

### The lock criterion

**LOCKED** if and only if:

```
For all points p ∈ L_i: g_eff,i(p) → 0.
```

Equivalently: the light-mass limit is a subset of the decoupling
limit. There is no path in parameter space to m_i → 0 with
g_eff,i remaining finite.

**UNLOCKED** if:

```
There exists p ∈ L_i such that g_eff,i(p) ≥ g_grav = 1/M_Pl.
```

There is at least one direction in parameter space where the mass
goes to zero while the coupling remains at observable strength.

### Formal test

Compute the parameter-space dimension:

```
d_lock = dim(M_i ∩ G_i) - dim(M_i ∪ G_i)
```

Wait — more precisely:

**Lock index:** Count the number of parameters that appear in BOTH
m_i and g_eff,i but in NO other independent combination.

If every parameter that controls m also controls g in the same
direction (i.e., m/g = const on L_i), the model is LOCKED.

If there exists at least one parameter in M_i that is NOT in G_i
(or vice versa), the model is potentially UNLOCKED.

### Practical test

The simplest diagnostic:

```
R(p) = m_i(p) / g_eff,i(p)
```

If R is a constant (independent of all parameters p), the model
is LOCKED. If R depends on at least one parameter, the model is
UNLOCKED (mass and coupling can be adjusted independently).

For PGT 0⁻ mode: R = m_B / g_eff ~ M_Pl². This is a constant —
LOCKED.

---

## Step 5: Radiative Stability

### Procedure (for UNLOCKED models only)
1. Identify the symmetry (if any) restored when m_i = 0.
   - Shift symmetry φ → φ + c?
   - Gauge symmetry?
   - Chiral symmetry?
   - Discrete symmetry?

2. If no symmetry is restored, compute the leading radiative
   correction:
   ```
   δm² ~ g_eff² Λ_UV² / (16π²)
   ```
   where Λ_UV is the UV cutoff (typically M_Pl for gravitational
   theories).

3. Assess the fine-tuning:
   ```
   FT = δm² / m_phys²
   ```
   If FT ≫ 1, the light mass is unnatural.

### Output
- Symmetry classification: PROTECTED, NATURAL, or UNPROTECTED
- Fine-tuning level if UNPROTECTED

---

## Step 6: Decoupling Behavior

### Procedure
1. Take the light-mass limit (m → 0 along the chosen path in
   parameter space).
2. In this limit, compute:
   - Does the mode thermalize? (rate ~ g_eff² T)
   - Does it produce detectable fifth forces? (range ~ 1/m,
     strength ~ g_eff²)
   - Does it generate birefringence? (rotation ~ g_eff × distance/m)

3. If ALL observational channels vanish in the light-mass limit,
   the model is observationally empty regardless of the lock status.

### Output
- List of surviving observational channels in the light-mass limit
- Observable strength estimates

---

## Summary: Decision Tree

```
START
  │
  ├── Step 1-3: Compute m(p), g_eff(p)
  │
  ├── Step 4: Is R = m/g_eff constant?
  │     │
  │     ├── YES → LOCKED (stop)
  │     │
  │     └── NO → potentially unlocked
  │           │
  │           ├── Step 5: Is m=0 symmetry-protected?
  │           │     │
  │           │     ├── YES → FULLY_UNLOCKED ✓
  │           │     │
  │           │     └── NO → PARTIALLY_UNLOCKED
  │           │           │
  │           │           └── Compute fine-tuning FT
  │           │                 │
  │           │                 ├── FT < 10⁵ → acceptable
  │           │                 └── FT > 10⁵ → problem transferred
  │           │
  │           └── Step 6: Any surviving observables?
  │                 │
  │                 ├── YES → viable candidate
  │                 └── NO → observationally empty (DR3 fail)
```

---

## Application to Known Cases

### PGT 0⁻ mode (Foundation A)

```
m = M_Pl / (4√(π|t₃|))
g_eff = c / (M_Pl √|t₃|)     [c = O(1) coefficient]

R = m/g_eff = M_Pl² × 4√π × c = const

→ LOCKED
```

### Brans-Dicke scalar

```
m_BD = 0 (massless in pure BD)
g_eff = 1/(M_Pl √(2ω_BD + 3))

Light mass limit: already m = 0
Coupling: g_eff → 0 as ω_BD → ∞ (GR limit)

→ LOCKED (the GR limit IS the decoupling limit)
```

### Standard Model W boson (counterexample)

```
m_W = g v / 2
g_W = g

m_W → 0 by v → 0, while g remains fixed.

R = m/g = v/2 → 0

R is NOT constant — it depends on v independently of g.

→ FULLY_UNLOCKED (mass protected by gauge symmetry)
```

### ALP with shift symmetry

```
m_a = Λ² / f     (from non-perturbative breaking)
g_a = 1 / f       (from derivative coupling)

R = m/g = Λ² → constant if only f varies

But: Λ is an independent parameter (instanton scale).
If we vary Λ while holding f fixed: m → 0 while g stays at 1/f.

→ FULLY_UNLOCKED (mass protected by shift symmetry, broken by instantons)
```

This is the ALP paradigm. The question is whether any geometric theory
naturally produces this structure.
