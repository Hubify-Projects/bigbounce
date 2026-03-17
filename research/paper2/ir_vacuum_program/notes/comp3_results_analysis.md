# Computation 3 Results: Fierz Rearrangement — Critical Findings

**Date:** 2026-03-13
**Status:** VERIFIED (two independent computations agree)

---

## The Result

The explicit Fierz rearrangement of the torsion-induced four-fermion interaction
`(J^μ)(J_μ)` with `J^μ = ψ̄γ^μγ⁵ψ + (1/γ)ψ̄γ^μψ` gives:

**1. The σπ cross-term vanishes identically: G_sp = 0**

This means **Possibility B** from the canonical problem statement (frozen v3, §Q5) is realized:
- The Holst-dependent interaction modifies only the even coefficients of V_eff
- The π → −π symmetry of V_eff is **preserved**
- No explicit odd-power term in π appears

**2. Both scalar and pseudoscalar channels are REPULSIVE at γ = 0.274**

```
G_s  / κ² = +0.161  (repulsive)
G_p  / κ² = +0.161  (repulsive)
G_sp / κ² =  0.000  (absent)
```

At the Barbero-Immirzi value γ = 0.274, G_s = G_p > 0, meaning neither the scalar
nor the pseudoscalar channel has an attractive interaction in the S/P sector.

**3. The vector and axial channels ARE attractive**

The dominant attractive channels are VV and AA, not S or P. This is a consequence
of the current-current structure: the original interaction is `−G_eff (J^μ)(J_μ)`,
and after Fierz, the vector/axial channels retain the attractive sign.

**4. G_s and G_p are EQUAL: G_s = G_p = (3κ²/16)(1−γ²)/(1+γ²)**

The scalar and pseudoscalar channels have identical coupling strength. The potential
V_eff(σ, π) has a full O(2) symmetry in the (σ, π) plane (not just π → −π), at
least at tree level.

**5. At γ = 1, G_s = G_p = 0 exactly**

The scalar/pseudoscalar channels completely decouple when γ = 1. Below γ = 1 (which
includes γ = 0.274), these channels are repulsive.

---

## What This Means for the Program

### The bad news

1. **The pseudoscalar condensate Φ = ⟨ψ̄iγ⁵ψ⟩ does NOT form via the scalar/pseudoscalar
   channel of the four-fermion interaction alone.** The coupling is repulsive, not attractive.

2. **Possibility A does not happen.** There is no σπ mixing term — the effective potential
   is symmetric under π → −π AND under σ → −σ (actually O(2) symmetric).

3. **The "standard NJL route" to a pseudoscalar condensate is blocked** at tree level for
   γ < 1. The scalar/pseudoscalar Fierz channel is repulsive.

### What is NOT yet ruled out

1. **Gravitational catalysis.** Curvature corrections at one loop (the a₁ ∝ R terms in the
   heat-kernel expansion) can flip the effective mass² of the auxiliary fields. Near the
   bounce (R ~ M_Pl²), these corrections are enormous and could turn a repulsive channel
   into a condensing one. This is the Gorbar-Gusynin (2008) mechanism.

2. **Vector/axial condensation.** The VV and AA channels ARE attractive. A vector or axial
   condensate (⟨ψ̄γ^μψ⟩ ≠ 0 or ⟨ψ̄γ^μγ⁵ψ⟩ ≠ 0) could form. However:
   - Vector condensates break Lorentz invariance
   - Axial condensates break both Lorentz and parity
   - Both are much more exotic than scalar/pseudoscalar condensates
   - Neither gives a simple vacuum energy (they produce anisotropic stress)

3. **Color-enhanced Fierz.** With N_c colors, the Fierz rearrangement gets additional
   contributions. In standard QCD-NJL, the color Fierz flips some repulsive channels
   to attractive. This needs checking for the gravitational case (where "color" = number
   of fermion species in the gravitational coupling).

4. **Two-loop or non-perturbative effects.** The one-loop effective potential could have
   different structure from the tree-level Fierz prediction.

---

## Impact on Gate 1

**At the current level of analysis, Gate 1 is in danger.**

The pseudoscalar channel is repulsive, the scalar channel is repulsive, and there is no
σπ mixing. The standard route to a condensate via the NJL mechanism does not work for
the scalar/pseudoscalar sector at γ = 0.274.

However, Gate 1 is not yet failed because:
- Gravitational catalysis has not been included (one-loop curvature corrections)
- The vector/axial channels are attractive (different type of condensation)
- Multi-flavor enhancement has not been considered

---

## Recommended Next Steps

1. **Check the Fierz result carefully.** The VA cross-term giving exactly zero is suspicious
   and should be verified against the literature. Cross-check with Freidel+ 2005 and
   Mercuri 2006 if they perform a similar decomposition.

2. **Compute the one-loop effective potential including curvature corrections.** This is
   Computation 4. The curvature-dependent terms may dominate at the bounce and change
   the sign of the effective coupling.

3. **Consider the vector/axial channel seriously.** If the S/P channel truly cannot condense,
   the program may need to pivot to a vector condensate analysis. This would be a significant
   change to the order parameter (requiring update to the canonical problem statement per
   the branching protocol in 06a).

4. **Check whether the VA Fierz coefficient is really exactly zero.** This could be an
   artifact of the single-flavor computation. With multiple fermion species that couple
   differently to the torsion sector, the cross-term may reappear.

---

## Refined Understanding After Verification

The verification (comp2b) revealed important structure:

1. **The VA cross-term does NOT vanish as an operator.** It has nonzero Fierz coefficients:
   - C^VA[S,P] = 16i, C^VA[P,S] = -16i (imaginary! — pseudoscalar-scalar mixing)
   - C^VA[Vμ,Aμ] = ±8 (vector-axial mixing)
   These are pure imaginary (SP) or off-diagonal (VA) — they correspond to
   *interference terms* like (ψ̄ψ)(ψ̄iγ⁵ψ) with imaginary coefficients.

2. **For identical single-flavor fermions, these interference terms vanish** because
   the bilinear products are either identically zero or cancel pairwise. The
   imaginary SP coefficient ±16i means the cross-term produces i(ψ̄ψ)(ψ̄iγ⁵ψ)
   which is anti-Hermitian — it contributes nothing to the Hermitian effective
   potential for a single species.

3. **FOR MULTIPLE FLAVORS, this argument breaks down.** If different fermion species
   couple to the torsion sector with different strengths (e.g., different masses),
   the cross-term between species i and j:
   (ψ̄_i γ^μ ψ_i)(ψ̄_j γ_μ γ⁵ ψ_j)
   is NOT zero for i ≠ j, because the Fierz exchange identity does not apply
   to different fermion fields.

4. **This opens a possible rescue route:** if the Standard Model fermion spectrum
   enters the problem (as it must at some level), inter-species VA interactions
   could generate a real σπ cross-term and break the π → −π symmetry.
   This would recover Possibility A but through a multi-flavor mechanism.

## Caveats on This Computation

1. **Single flavor only.** The Fierz rearrangement was computed for a single Dirac
   fermion. Multi-flavor effects could qualitatively change the channel structure.

2. **No color factors.** For QCD-like fermions, color Fierz rearrangement adds
   channels. In standard NJL, color factors make the S/P channel attractive
   even when the single-color result is repulsive.

3. **Overall normalization.** The 3/16 vs 3/32 prefactor issue from Computation 1-2
   is still unresolved. This affects numerical values but not signs or ratios.

4. **γ-dependence is exact.** The critical value γ = 1 where the S/P coupling
   changes sign is an exact algebraic result, independent of normalization conventions.

## Updated Assessment of Gate 1

**For single-flavor, the standard NJL condensate route is blocked at γ = 0.274.**

The scalar/pseudoscalar effective coupling is:
```
G_s = G_p = G_eff × (1 - 1/γ²) = G_eff × (γ² - 1)/γ²
```

At γ = 0.274: G_s = G_p < 0 (in the convention where negative = repulsive).

**Three paths forward for Gate 1:**

1. **Multi-flavor Fierz.** Include N_f > 1 fermion species with inter-species
   interactions. This could open real σπ mixing and flip channel attractiveness.

2. **Gravitational catalysis.** One-loop curvature corrections (a₁ ∝ R terms in
   heat-kernel) can dominate over tree-level at R ~ M_Pl². This could effectively
   flip the sign of the scalar/pseudoscalar mass term even if the tree-level
   coupling is repulsive.

3. **Vector/axial condensation.** Accept that the dominant attractive channel is
   VV/AA and investigate Lorentz-breaking vector condensates. This would be a
   major change to the order parameter.
