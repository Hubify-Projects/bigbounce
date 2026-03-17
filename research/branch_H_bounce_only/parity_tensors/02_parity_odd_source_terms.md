# Parity-Odd Source Term Analysis

**Date:** 2026-03-15

---

## The Minimal Model

Einstein-Cartan gravity with Dirac fermions:

```
S = ∫ d⁴x √g [M_Pl²/2 R(ω) + iψ̄ γ^μ D_μ(ω) ψ - mψ̄ψ]
```

where ω is the full spin connection (Levi-Civita + contortion)
and D_μ(ω) is the covariant derivative acting on spinors.

Torsion is algebraically determined by the spin density:

```
T^λ_{μν} = -κ² ε^λ_{μνρ} J^{5ρ}  (+ trace terms)
```

where J^5_μ = ψ̄ γ_μ γ^5 ψ is the axial current.

After integrating out torsion, the effective action is:

```
S_eff = ∫ d⁴x √g̊ [M_Pl²/2 R̊ + iψ̄ γ^μ D̊_μ ψ - mψ̄ψ
                     + (3κ⁴/32) J^5_μ J^{5μ}]
```

The four-fermion interaction is **(J^5)² = J^5_μ J^{5μ}**.

---

## Candidate Parity-Odd Structures

### Candidate 1: The four-fermion interaction (J^5)²

```
(J^5)² = J^5_μ J^{5μ} = -(J^5_0)² + (J⃗^5)²
```

J^5_μ is a PSEUDOVECTOR. The product of two pseudovectors is
a SCALAR (parity-even).

```
┌────────────────────────────────────────────────────┐
│                                                    │
│  (J^5)² is PARITY-EVEN. It does NOT distinguish    │
│  left from right.                                  │
│                                                    │
└────────────────────────────────────────────────────┘
```

**VERDICT: Does not produce parity-odd tensor source.**

### Candidate 2: Background axial charge n_5 = ⟨J^5_0⟩

In thermal equilibrium at the bounce, is there a net axial charge?

For a CP-symmetric thermal bath: **n_5 = 0** (equal numbers of
left-handed and right-handed fermions).

For a CP-asymmetric bath (e.g., from CKM-type phases): n_5
could be nonzero, but:

1. The CKM CP violation is parametrically small (J_CKM ~ 10⁻⁵)
2. At Planck temperature, all flavors are relativistic and CP
   violation is thermally averaged
3. No known mechanism generates a large n_5 at Planck density

Even IF n_5 ≠ 0: n_5 is a pseudoscalar (parity-odd), but does it
couple to tensor modes?

The perturbation of (J^5)² at linear order:

```
δ(J^5)² = 2 J^5_μ δJ^{5μ} = 2 n_5 δJ^{5,0} + 0  (isotropy)
```

Now, δJ^{5,0} from tensor perturbations h_ij:

Tensor perturbations modify only the spatial metric: g_ij → a²(δ_ij + h_ij).
They do NOT modify g_00 or g_0i at linear order.

The J^{5,0} component depends on the temporal vierbein e^a_0,
which is UNPERTURBED by tensor modes:

```
δe^a_0 = 0    for tensor perturbations
```

Therefore:

```
┌────────────────────────────────────────────────────┐
│                                                    │
│  δJ^{5,0} = 0 from tensor perturbations.           │
│  Even with n_5 ≠ 0, there is no coupling to        │
│  tensor modes at linear order.                     │
│                                                    │
└────────────────────────────────────────────────────┘
```

**VERDICT: n_5 does not produce parity-odd tensor source at
linear order.**

### Candidate 3: The Holst term / Immirzi parameter

The Holst modification of the EC action:

```
S_Holst = (M_Pl²/2γ) ∫ e^I ∧ e^J ∧ F_{IJ}(ω)
```

where γ is the Barbero-Immirzi parameter. This term IS parity-odd
in the action (it lacks the ε tensor compared to the Einstein-
Hilbert term).

**Effect on the effective action:**

With the Holst term, the torsion equation is modified. The
solution for torsion changes, and the effective four-fermion
coefficient becomes:

```
L_4f = -(3κ⁴/32) × [γ²/(1+γ²)] × J^5_μ J^{5μ}
```

The Immirzi parameter RESCALES the coefficient of (J^5)². It does
NOT introduce any new terms. The interaction remains (J^5)²,
which is parity-even.

**Why?** On-shell (after solving for torsion), the Holst term
reduces to the Nieh-Yan topological invariant:

```
S_Holst → (M_Pl²/2γ) ∫ N₄ + (four-fermion terms)
```

The Nieh-Yan integral ∫ N₄ is a boundary term and does not
contribute to the equations of motion. The four-fermion part
is (J^5)², just with a γ-dependent coefficient.

```
┌────────────────────────────────────────────────────┐
│                                                    │
│  The Holst term / Immirzi parameter does NOT        │
│  generate new parity-odd terms. It only rescales   │
│  the coefficient of the parity-even (J^5)².        │
│                                                    │
└────────────────────────────────────────────────────┘
```

**VERDICT: No new parity-odd tensor source from Holst/Immirzi.**

### Candidate 4: Nieh-Yan term coupled to a pseudoscalar

If the Immirzi parameter is PROMOTED to a dynamical field β(x):

```
S_NY = ∫ β(x) N₄
```

This is NOT a total derivative when β varies in spacetime.
It would produce a Chern-Simons-like coupling:

```
β(x) [T^a ∧ T_a - R_{ab} ∧ e^a ∧ e^b]
```

This IS parity-odd and WOULD produce chirality in tensor modes.

**However:** this requires a NEW DYNAMICAL FIELD β(x) that is
NOT present in the minimal EC theory. This was explored in
Foundation B:

- Foundation B found: the Nieh-Yan form breaks into a non-
  topological piece in MAG (metric-affine gravity)
- But the topological-shift duality blocks mass protection +
  geometric content simultaneously
- The resulting coupling is a GENERIC ALP (axion-like particle),
  not a spin-torsion-specific effect

```
┌────────────────────────────────────────────────────┐
│                                                    │
│  A dynamical Nieh-Yan coupling WOULD produce       │
│  parity-odd tensors, but it requires ADDITIONAL    │
│  physics beyond minimal EC. Already closed by      │
│  Foundation B (topological-shift duality).          │
│                                                    │
└────────────────────────────────────────────────────┘
```

**VERDICT: Requires new physics; already closed as a distinctive
mechanism (Foundation B).**

### Candidate 5: Gravitational Chern-Simons term

The Pontryagin density:

```
P = R̃^{μν}_{ρσ} R^{ρσ}_{μν} = ε^{μνκλ} R_{μνab} R_{κλ}^{ab}
```

Coupled to a pseudoscalar: φ × P (dynamical Chern-Simons gravity).

This IS parity-odd and DOES produce chiral gravitational waves.

**But:** the Pontryagin term is NOT part of the minimal EC theory.
It is a separate modification of gravity.

In EC theory: the Pontryagin density IS modified by torsion
(P acquires torsion-dependent terms). But it remains topological
(a total derivative) even with torsion. Only when coupled to a
DYNAMICAL pseudoscalar does it contribute to equations of motion.

**VERDICT: Not in minimal EC. Requires additional fields/couplings.**

### Candidate 6: Gravitational chiral anomaly

The quantum anomaly:

```
∂_μ J^{5μ} = (1/192π²) R̃^{μν}_{ρσ} R^{ρσ}_{μν} + ...
```

At the bounce (R ~ M_Pl²):

```
∂_μ J^{5μ} ~ M_Pl⁴ / (192π²) ~ 10⁻³ M_Pl⁴
```

This could generate n_5 ~ M_Pl³ during the bounce, which is
significant. BUT:

1. This is a ONE-LOOP quantum gravity effect, not captured by
   the classical EC theory
2. Even if n_5 is generated, it does not couple to tensor modes
   at linear order (Candidate 2 analysis applies)
3. The anomaly itself does not produce a classical parity-odd
   term in the tensor equation

**VERDICT: Quantum effect beyond classical EC; even if present,
does not couple to tensor modes.**

---

## Summary of All Candidates

| # | Candidate | Parity-odd? | In minimal EC? | Couples to tensors? |
|---|-----------|------------|---------------|-------------------|
| 1 | (J^5)² interaction | NO (scalar) | YES | — |
| 2 | n_5 background | YES (pseudo) | IF CP asymmetry | **NO** (δJ^{5,0} = 0) |
| 3 | Holst/Immirzi | Rescales only | YES | NO (still (J^5)²) |
| 4 | Dynamical Nieh-Yan | YES | **NO** (new field) | YES (but generic ALP) |
| 5 | Chern-Simons R̃R | YES | **NO** (new field) | YES (but not EC) |
| 6 | Chiral anomaly | YES | **NO** (quantum) | NO (doesn't couple) |

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│  NONE of the candidates provide a parity-odd tensor    │
│  source within the MINIMAL Einstein-Cartan theory      │
│  on an FRW background.                                 │
│                                                        │
│  Every parity-odd possibility either:                  │
│  (a) is parity-even when properly evaluated, or        │
│  (b) requires physics beyond minimal EC, or            │
│  (c) does not couple to tensor modes at linear order.  │
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

## The Structural Reason

### Why the four-fermion interaction is parity-even

The spin-torsion coupling is:

```
Torsion ~ J^5    (pseudovector)
```

The back-reaction on the metric goes through the stress-energy,
which involves torsion SQUARED:

```
T_μν^{torsion} ~ T² ~ (J^5)²    (scalar)
```

Squaring a parity-odd quantity gives a parity-even result.
This is STRUCTURAL — it follows from the algebraic nature of
torsion in EC theory.

### Why FRW isotropy eliminates parity violation

Even if the theory contained parity-odd terms, spatial isotropy
on FRW forces:

```
⟨J^5_i⟩ = 0        (no preferred spatial direction)
⟨ε_{ijk} A^{jk}⟩ = 0   (no preferred handedness)
```

The only surviving parity-odd background is the pseudoscalar n_5,
which (as shown) does not couple to tensor modes.

### Why the bounce does not break parity

The bounce is a TIME-symmetric or time-ASYMMETRIC event:
- H goes from negative (contraction) to positive (expansion)
- Ḣ > 0 at the bounce
- This breaks T (time-reversal), not P (spatial parity)

Tensor chirality requires P violation. The bounce provides T
violation. These are DIFFERENT symmetries.

(In CPT-invariant theories, T violation → CP violation. But
C has no effect on gravity, and P violation requires a spatial
handedness that the isotropic bounce does not provide.)
