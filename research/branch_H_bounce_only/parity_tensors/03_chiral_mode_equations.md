# Chiral Tensor Mode Equations

**Date:** 2026-03-15

---

## Setup: Left and Right Circular Polarizations

The tensor perturbation h_ij can be decomposed into circular
polarizations:

```
h_ij(η, x⃗) = ∫ d³k/(2π)³ Σ_{s=L,R} h_s(η,k) e^s_ij(k̂) e^{ik⃗·x⃗}
```

where e^L_ij and e^R_ij are the left and right polarization
tensors. Under a parity transformation (x⃗ → -x⃗):

```
e^L_ij ↔ e^R_ij    (parity swaps handedness)
```

In a parity-symmetric theory: h_L and h_R obey the same equation.
In a parity-violating theory: they may differ.

---

## Standard GR on FRW (No Parity Violation)

The mode equation for both polarizations:

```
v_{k,s}'' + (k² - a''/a) v_{k,s} = 0     for s = L, R
```

Identical for L and R. The Bogoliubov coefficients are equal:

```
|β_{k,L}|² = |β_{k,R}|²
P_L(k) = P_R(k)
Δχ(k) = (P_L - P_R)/(P_L + P_R) = 0
```

No chirality.

---

## What a Parity-Odd Term Would Look Like

The general form of a chirality-splitting modification:

```
v_{k,L}'' + (k² - a''/a + μ(η)k) v_{k,L} = 0
v_{k,R}'' + (k² - a''/a - μ(η)k) v_{k,R} = 0
```

The key feature: the parity-odd term is LINEAR in k (not k²),
because it must change sign under parity (k → -k for one
circular polarization).

The coefficient μ(η) is a parity-odd background quantity with
dimensions of inverse conformal time.

### Known sources of μ(η):

1. **Chern-Simons gravity:** μ(η) = α_CS φ'(η) / M_Pl²
   where φ is a dynamical pseudoscalar.

2. **Gravitational leptogenesis:** μ(η) = (n_5/M_Pl²) × (...)
   from axial charge density coupling to curvature.

3. **Lorentz violation:** μ(η) from a background timelike
   pseudovector.

ALL of these require physics BEYOND the minimal EC theory.

---

## Does the Minimal EC Theory Produce μ(η) ≠ 0?

### Check 1: From the four-fermion interaction

The effective stress-energy from (J^5)² is:

```
T^{eff}_{μν} = (3κ⁴/16) [J^5_μ J^5_ν - (1/2)g_μν (J^5)²]
```

The TT spatial perturbation:

```
δT^{eff}_{ij}|^{TT} = (3κ⁴/16) [δ(J^5_i J^5_j)|^{TT}
                        - (1/2) h_ij (J^5)²]
```

On FRW background: ⟨J^5_i⟩ = 0 (isotropy). So:

```
⟨δ(J^5_i J^5_j)⟩ = ⟨J^5_i⟩ δJ^5_j + ⟨J^5_j⟩ δJ^5_i = 0
```

at linear order. The only surviving term is:

```
δT^{eff}_{ij}|^{TT} = -(3κ⁴/32) h_ij ⟨(J^5)²⟩
```

This is proportional to h_ij itself (a mass-like term, not a
chirality-splitting term). It modifies a''/a but does NOT split
L and R:

```
v_{k,s}'' + (k² - a''/a - Δm²(η)) v_{k,s} = 0
```

Same for L and R. **No chirality splitting from (J^5)².**

### Check 2: From Holst term perturbation

The Holst term:

```
S_H = (M_Pl²/2γ) ∫ e^I ∧ e^J ∧ F_{IJ}
```

At the perturbation level, this contributes to the tensor equation
through the variation of F_{IJ} with respect to the connection.
But on-shell, the Holst term is the Nieh-Yan topological invariant,
whose variation vanishes:

```
δN₄ / δg_{μν} = 0    (topological invariant)
```

On-shell and on FRW: **No contribution to tensor equations from
the Holst term.**

### Check 3: From torsion perturbation

In EC theory, torsion is algebraically determined:

```
T^λ_{μν} = -κ² ε^λ_{μνρ} J^{5ρ}
```

The perturbation of torsion from h_ij:

```
δT^λ_{μν} = -κ² ε^λ_{μνρ} δJ^{5ρ}
```

Now, δJ^{5ρ} from tensor perturbations. The axial current:

```
J^{5μ} = ψ̄ γ^μ γ^5 ψ
```

In curved spacetime: J^{5μ} = e^μ_a ψ̄ γ^a γ^5 ψ. The tensor
perturbation modifies the spatial vierbein:

```
δe^a_i = (1/2) h_ij e^{aj}    (spatial)
δe^a_0 = 0                    (temporal, unperturbed by tensors)
```

So the perturbation of the spatial components of J^5:

```
δJ^{5i} = (1/2) h^{ij} ψ̄ γ_j γ^5 ψ
```

On FRW background: ⟨ψ̄ γ_j γ^5 ψ⟩ = ⟨J^5_j⟩ = 0 (isotropy).

Therefore: **⟨δJ^{5i}⟩ = 0** and the torsion perturbation
vanishes at the expectation value level.

The torsion perturbation only contributes at SECOND order
(fluctuation × fluctuation), not at linear order.

### Check 4: Could spin-torsion produce a PROPAGATION asymmetry?

The gravitational wave propagation equation includes corrections
from the effective stress-energy. For a parity-odd propagation
effect (birefringence), we need a term of the form:

```
ε^{ij}_k ∂_j h_{kl}' × (parity-odd background)
```

This requires a background pseudovector V^i with ⟨V^i⟩ ≠ 0.

On FRW: ALL spatial vectors vanish by isotropy:

```
⟨V^i⟩ = 0    for any spatial vector V^i
```

The only surviving pseudoscalar (n_5 = ⟨J^{5,0}⟩) does not
have a spatial index to contract with ε^{ij}_k.

**No propagation birefringence on FRW.**

---

## The Complete Result

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│  In the minimal Einstein-Cartan theory on FRW:         │
│                                                        │
│  v_{k,L}'' + (k² - a''/a) v_{k,L} = 0                │
│  v_{k,R}'' + (k² - a''/a) v_{k,R} = 0                │
│                                                        │
│  The equations are IDENTICAL.                          │
│  μ(η) = 0 exactly.                                    │
│  No chirality splitting. No parity violation.          │
│                                                        │
└────────────────────────────────────────────────────────┘
```

This holds for:
- Any value of ρ_crit (any spin-torsion coupling strength)
- Any value of the Immirzi parameter γ
- Any composition of the fermion bath (any n_5)
- Any time during or after the bounce

---

## What WOULD Produce Chirality

For reference, the modifications that WOULD split L and R:

### Model A: Chern-Simons gravity

```
S_CS = (α/4) ∫ φ ε^{μνρσ} R_{μνab} R_{ρσ}^{ab} √g d⁴x
```

Produces: μ(η) = α φ'/(M_Pl²)

**Not in EC theory.** Requires a new pseudoscalar field φ.

### Model B: Dynamical Immirzi field

```
S = (M_Pl²/2) ∫ [R + (1/β(x)) Holst]
```

Produces: μ(η) ∝ β'(η) through the non-topological part of
the Nieh-Yan variation.

**Not in EC theory.** Requires promoting γ to a dynamical field.
Already explored and closed by Foundation B.

### Model C: Lorentz-violating background

```
S_LV = ∫ b_μ ε^{μνρσ} e^a_ν T_{ρσa}
```

Produces: μ(η) ∝ b_0(η) (temporal component of background
pseudovector).

**Not in EC theory.** Requires explicit Lorentz violation.

**Every known mechanism for tensor chirality requires physics
BEYOND the minimal spin-torsion bounce model.**

---

## Structural Theorem

**In Einstein-Cartan gravity with Dirac fermions on FRW:**

1. Torsion is algebraically determined by the spin density
2. The effective interaction is (J^5)², which is parity-EVEN
3. FRW isotropy forces all spatial parity-odd backgrounds to zero
4. The temporal pseudoscalar n_5 does not couple to tensor modes
5. Therefore: left and right tensor modes are IDENTICAL

This is a NO-GO result for parity-violating tensor signatures
in the minimal model. It holds independent of:
- The bounce dynamics (symmetric or asymmetric)
- The matter content (as long as it's isotropic)
- The value of any coupling constants
