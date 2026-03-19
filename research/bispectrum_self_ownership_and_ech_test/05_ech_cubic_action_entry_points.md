# 05: ECH Cubic Action Entry Points

## The Question

Can Einstein-Cartan-Holst (ECH) gravity modify the matter-bounce bispectrum?

## Classification of Entry Points

### 1. Background modification only
**Status: LIKELY REAL but IRRELEVANT to f_NL**

ECH modifies the Friedmann equations at high density (near the bounce) through spin-torsion coupling. This changes:
- The bounce mechanism (curvature-induced bounce vs quantum bounce)
- The maximum density at the bounce (ρ_crit)
- The matching conditions for perturbations through the bounce

But the f_NL = -35/8 is computed ENTIRELY in the contracting phase, far from the bounce. The background during matter contraction is the SAME in ECH as in standard GR (torsion vanishes for dust matter on FRW backgrounds: T₀ = Q₀ = 0 by symmetry).

**Verdict: ECH background modification does NOT affect f_NL.**

### 2. Quadratic action modification
**Status: LIKELY ABSENT**

The Mukhanov-Sasaki equation for scalar perturbations derives from the quadratic action. In ECH, torsion could in principle modify the effective mass term (z''/z) or the sound speed.

However, on FRW backgrounds with scalar field matter, the torsion perturbations decouple at quadratic order from the scalar sector (this is the "perturbation transparency" finding from our earlier work). The Mukhanov-Sasaki equation is UNCHANGED.

This means the mode functions, power spectrum, and spectral index are the SAME as in GR.

**Verdict: ECH does NOT modify the quadratic action for scalar perturbations.**

### 3. Cubic action modification (DIRECT)
**Status: POSSIBLE BUT UNPROVEN — the key question**

The cubic action for ζ derives from expanding the Einstein-Hilbert action to third order. In ECH, the action is:

S = (M²_Pl/2) ∫ √(-g) [R(Γ) + (1/γ)·R̃(Γ)] d⁴x + S_matter

where Γ is the full connection (with torsion) and R̃ is the Holst dual of the Ricci scalar.

At SECOND order, the Holst term doesn't contribute new degrees of freedom (it's topological on-shell for FRW). But at THIRD order, the contorsion tensor K^α_βγ could generate NEW cubic vertices that are NOT present in the standard Maldacena action.

Specifically:
- The Christoffel connection Γ̊ gives the standard Maldacena vertices
- The contorsion K adds correction vertices proportional to (torsion)×(curvature perturbation)²
- These corrections are suppressed by the torsion mass scale but could be enhanced by the Barbero-Immirzi parameter γ

**The correction would look like:**
δL₃^{ECH} ~ (1/γ) × (torsion coupling) × ζ × ζ' × (something)

**Verdict: POSSIBLE but requires explicit computation of the ECH cubic action. This is the highest-priority ECH calculation.**

### 4. Constraint equation modification
**Status: POSSIBLE**

In the ADM decomposition with torsion, the Hamiltonian and momentum constraints receive torsion corrections. These modify the solution for the lapse N and shift N^i at second order, which feeds back into the cubic action for ζ.

If the constraint equations change, the χ variable (which encodes the shift) also changes, modifying the χ-dependent vertices in the cubic action.

This is closely related to entry point #3 and would be part of the same calculation.

**Verdict: Possible, included in #3.**

### 5. Bounce transfer modification
**Status: LIKELY REAL but SEPARATE from f_NL**

ECH provides a specific bounce mechanism (curvature-induced bounce from the ∝ ρ² term in the modified Friedmann equation). The perturbation transfer through this bounce differs from LQC or other bounce mechanisms.

However, the f_NL = -35/8 is computed BEFORE the bounce. The bounce transfer can modify the AMPLITUDE of the perturbations (and hence the power spectrum) but the SHAPE function A_T (which determines f_NL) is independent of the bounce transfer (it's a ratio that cancels the amplitude).

EXCEPTION: if the bounce generates ADDITIONAL non-Gaussianity (beyond what was produced in the contracting phase), this would add to f_NL. This is possible but requires a separate computation of the bispectrum generated AT the bounce, not just during contraction.

**Verdict: Bounce-generated non-Gaussianity is possible but separate from the Cai calculation. Would require a dedicated study of perturbation theory at the ECH bounce.**

### 6. Non-minimal coupling effects
**Status: ALREADY RULED OUT**

Our earlier work (Foundations A-G) showed that non-minimal coupling of the scalar field to torsion either:
- Reduces to standard scalar-tensor theory (no geometric fingerprint on FRW)
- Has couplings that are Planck-suppressed (unobservable)
- Faces the mass-coupling lock (can't be both light and strongly coupled)

**Verdict: Ruled out by previous work.**

## Summary Table

| Entry Point | Status | Priority |
|------------|--------|----------|
| Background modification | Real but irrelevant to f_NL | LOW |
| Quadratic action | Absent (perturbation transparency) | NONE |
| **Cubic action (direct)** | **Possible, unproven** | **HIGH** |
| Constraint equations | Part of cubic action | HIGH |
| Bounce transfer | Possible, separate calculation | MEDIUM |
| Non-minimal coupling | Ruled out | NONE |

## The One Credible ECH Entry Point

**The ECH cubic action might differ from the standard Maldacena action** if the contorsion tensor generates new cubic vertices for ζ.

To test this, one would need to:
1. Expand the ECH action S[g, Γ] = S_EH[g] + S_Holst[g, Γ] to THIRD order in perturbations
2. Solve the torsion equation of motion to the relevant order
3. Substitute back to get the effective cubic action for ζ
4. Compare with the standard Maldacena action (Cai's Eq. 15)
5. Identify any NEW vertices and compute their contribution to the shape function

If the Holst term produces new vertices, they would be proportional to 1/γ (Barbero-Immirzi parameter), giving an ECH-SPECIFIC correction:

f_NL^{ECH} = f_NL^{generic} + δf_NL(γ)

This would make the bispectrum ECH-specific and potentially distinguishable from the pure GR matter bounce.
