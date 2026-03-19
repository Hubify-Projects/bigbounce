# 05: Holst Power-Counting and Symmetry Gate

## The Question

Does the Holst term S_Holst = (M²_Pl/(2γ)) ∫ e^I ∧ e^J ∧ F_IJ generate any cubic scalar perturbation vertex on an FRW + scalar field background?

## Gate Test 1: Does torsion exist on the background?

**NO.** On an FRW background with a canonical scalar field (no spin), the torsion equation of motion gives:

T^λ_μν = 0 (identically)

This is because:
- Torsion is sourced by the spin density tensor S^λ_μν
- A canonical scalar field has S^λ_μν = 0
- Therefore T^λ_μν = 0 on the background

**Implication:** The background is IDENTICAL to GR. The Holst term contributes nothing at zeroth order. ✓ (consistent with known results)

## Gate Test 2: Does torsion appear at first order in scalar perturbations?

The scalar perturbation δφ of the scalar field still has zero spin density:
δS^λ_μν[δφ] = 0

The torsion equation of motion (algebraic in Einstein-Cartan theory) gives:
T^λ_μν ∝ S^λ_μν = 0

at ALL orders in scalar perturbations.

**CRITICAL RESULT: Torsion remains ZERO for scalar perturbations of a canonical scalar field, to ALL orders.**

This is because torsion in Einstein-Cartan theory is NOT dynamical — it's an algebraic function of the spin density. Since a scalar field has no spin density, torsion is identically zero regardless of the scalar field configuration.

**Implication:** At first, second, AND third order in scalar perturbations, T^λ_μν = 0. The full connection reduces to the Levi-Civita connection: Γ^λ_μν = Γ̊^λ_μν (Christoffel symbols only).

## Gate Test 3: Does the Holst term contribute when torsion = 0?

The Holst term is:
S_Holst = (M²_Pl/(2γ)) ∫ ε^IJ_KL e^K ∧ e^L ∧ F^IJ

When torsion = 0, the connection reduces to the Levi-Civita connection, and:

F^IJ = R^IJ(Γ̊) + K-dependent terms

where K is the contorsion. With K = 0:

F^IJ = R^IJ(Γ̊) = (Levi-Civita Riemann tensor in tetrad form)

The Holst term becomes:
S_Holst|_{T=0} = (M²_Pl/(2γ)) ∫ ε^IJ_KL e^K ∧ e^L ∧ R^IJ(Γ̊)

This is the **Holst dual of the Riemann tensor** evaluated with the Levi-Civita connection. In 4D, this is related to the **Pontryagin density**:

ε^IJ_KL R^KL ∝ *R^IJ (dual Riemann)

And the integral ∫ e ∧ e ∧ *R is the **Gauss-Bonnet-like topological term** (specifically, the Nieh-Yan or Euler class contribution).

**In 4 dimensions, with zero torsion:**
∫ ε^IJ_KL e^K ∧ e^L ∧ R^IJ(Γ̊) = ∫ √(-g) ε^μνρσ R_μνρσ d⁴x = topological invariant

This is the **Pontryagin density** (or more precisely, the Euler density), which is a TOTAL DERIVATIVE in 4D. It does not contribute to the equations of motion at ANY order in perturbation theory.

**GATE RESULT: The Holst term with zero torsion is topological and contributes NO dynamics — including NO cubic vertices.**

## Gate Test 4: Could fermion matter reintroduce torsion?

If the matter sector includes FERMIONS (e.g., neutrinos, electrons), then:
- S^λ_μν ≠ 0 (fermions carry spin)
- T^λ_μν ≠ 0 (sourced by spin density)
- The Holst term becomes non-topological

This would generate:
1. Four-fermion contact interactions (from integrating out torsion): ∝ (ψ̄γ⁵γψ)²/M²_Pl
2. Parity-violating corrections to gravitational dynamics
3. Potential modifications to the cubic action for ζ through fermion loops

**However:** These effects are:
- Suppressed by M²_Pl (Planck-scale coupling)
- Relevant only at densities near the Planck density
- Completely negligible during the matter contraction phase (which occurs at sub-Planckian densities)
- Only possibly relevant AT the bounce (if the bounce density approaches M⁴_Pl)

For the bispectrum computed during matter contraction (which is where f_NL = -35/8 comes from), fermion-induced torsion is utterly negligible.

## Gate Test 5: Does the Barbero-Immirzi parameter appear in any scalar observable?

For a canonical scalar field on FRW:
- Torsion = 0 (Gate Test 2)
- Holst term = topological (Gate Test 3)
- γ drops out of ALL equations of motion
- γ appears NOWHERE in the perturbation equations at any order

**The Barbero-Immirzi parameter is unobservable in the scalar sector of ECH with canonical scalar field matter.**

This is a well-known result (see e.g., the original Holst 1996 paper, and the discussion in Perez & Rovelli 2006). The parameter γ affects:
- The LQG area/volume spectra (quantum level)
- The coupling to fermions (if present)
- Parity-violating gravitational waves (through graviton propagation, if the Holst term becomes dynamical via higher-derivative corrections)

But it does NOT affect scalar perturbations in the classical Einstein-Cartan theory.

## GATE VERDICT

**THE ECH BISPECTRUM PATH IS DEAD.**

The argument is simple and rigorous:

1. A canonical scalar field has zero spin density
2. Zero spin density → zero torsion (algebraic equation in EC theory)
3. Zero torsion → Holst term reduces to a topological invariant
4. Topological invariant → no dynamics at any order in perturbation theory
5. Therefore: NO new cubic vertices, NO modification to the mode functions, NO change to the constraint equations, NO ECH-specific bispectrum correction

The Barbero-Immirzi parameter γ is completely invisible in the scalar bispectrum.

**f_NL = -35/8 is PURELY GENERIC. ECH adds nothing.**
