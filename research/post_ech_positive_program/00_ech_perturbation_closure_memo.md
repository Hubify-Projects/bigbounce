# ECH Perturbation Closure Memo

## Status: PERMANENTLY CLOSED

## What Was Tested

### Scalar Sector
- Does the Holst term modify the scalar cubic action? → **NO** (Holst is topological when T=0)
- Does torsion appear in scalar perturbations? → **NO** (canonical scalar: S^λ_μν = 0 → T = 0 at all orders)
- Does γ (Barbero-Immirzi) enter any scalar equation? → **NO**
- Does ECH modify f_NL? → **NO** (f_NL = -35/8 is purely generic)
- Tested in: ech_bispectrum_gate/, fnl_symbolic_cancellation/, fnl_combined_integrand/

### Tensor Sector
- Does the Holst term modify tensor mode equations? → **NO** (same T=0 kill chain)
- Does ECH produce tensor parity violation? → **NO** (Barrier 8: parity-even effective interaction)
- Does ECH produce GW birefringence? → **NO** (Δv_R - v_L = 0 exactly)
- Is any tensor signal detectable? → **NO** (P_T ~ 10⁻⁶⁴; frequency gate failed at GHz)
- Tested in: branch_H/, branch_M/, project_chiral_bounce_GW/, ech_tensor_gate/

### Non-Minimal Extensions
- Dynamical Immirzi field? → Reduces to generic ALP (Branch Q: comprehensively closed)
- Nieh-Yan coupling? → Same ALP reduction after torsion elimination
- Fermionic spin density? → Parity-even interaction, Planck-suppressed
- PGT propagating torsion? → Generic GW spectrum, detector gap 10¹⁷

## Why the Closure Is Structural

The closure follows from a chain of mathematical identities, not approximations:

1. Canonical scalar field → zero spin density (definition of "canonical")
2. Zero spin → zero torsion (algebraic EC torsion equation, exact)
3. Zero torsion → connection = Levi-Civita (definition)
4. Levi-Civita → Holst term = Pontryagin density (algebraic identity in 4D)
5. Pontryagin density = total derivative (topological, exact)
6. Total derivative → zero variation → no equations of motion (variational calculus, exact)

No approximation was used. No loophole exists within the minimal ECH + canonical scalar framework.

## What Role ECH Still Plays

ECH provides the BACKGROUND bounce mechanism through the spin-torsion modification of the Friedmann equation at high density (ρ ~ M⁴_Pl). This:
- Resolves the Big Bang singularity
- Provides a specific ρ_crit and bounce dynamics
- Transfers perturbations from contracting to expanding phase

ECH is a **bounce mechanism framework** — it provides the engine that makes the bounce happen.

## What Role ECH No Longer Plays

ECH does NOT:
- Generate distinctive perturbation-level observables
- Modify f_NL, n_s, r, or any CMB/LSS observable
- Produce parity violation, birefringence, or chiral GW signals
- Leave any γ-dependent fingerprint in observations

ECH is NOT a **perturbation-level observable framework**.

## Do Not Reopen Unless

The only circumstances under which ECH perturbation novelty should be reconsidered:
1. A genuinely NEW non-minimal theory is introduced (not a relabeling of Branch Q/H/M)
2. Fermion spin density at cosmological scales is shown to be relevant (currently Planck-suppressed)
3. A higher-derivative extension (R² + torsion) is explicitly constructed with propagating torsion modes

None of these are currently on the table.

**Minimal ECH is a bounce mechanism framework, not a perturbation-level observable framework. This conclusion is structural and permanent.**
