# Track B Closure: Minimal Single-Flavor NJL Condensate Route

**Date:** 2026-03-13
**Status:** CLOSED
**Decision:** The minimal condensate route to first-principles dark energy fails at γ = 0.274

---

## What Was Tested

Whether the torsion-induced four-fermion interaction in Einstein-Cartan-Holst gravity,
at the Barbero-Immirzi value γ = 0.274, generates a pseudoscalar fermion condensate
Φ = ⟨ψ̄iγ⁵ψ⟩ that persists as late-time vacuum energy with w ≈ −1.

This was the "most credible route" identified in the program's executive summary
and the central mechanism of Track B (Condensate).

## Four Load-Bearing Negative Results

### 1. The scalar/pseudoscalar channel is repulsive at γ = 0.274

The Fierz rearrangement of the torsion-induced interaction gives an effective
coupling in the scalar/pseudoscalar sector:

```
G_SP = (3κ²/16) × (γ² − 1)/(γ² + 1)
```

This is an exact algebraic result (no approximation). The sign changes at γ = 1:
- γ > 1: attractive
- γ < 1: **repulsive**

At γ = 0.274: G_SP < 0. The NJL gap equation has no nontrivial solution for any
repulsive coupling, regardless of curvature or fermion content.

**Computation:** `comp2_fierz_rearrangement.py`, verified by `comp2b_fierz_verification.py`

### 2. Even with the correct sign, the coupling is ~175× too weak

The NJL critical coupling for condensation is G_crit = 2π²/(N_c Λ²). With
gravitational coupling G ~ κ² ~ 1/M_Pl² and cutoff Λ ~ M_Pl:

```
G_SP / G_crit ≈ 0.006  (at γ = 2.0, where the sign IS correct)
```

The gravitational four-fermion coupling is subcritical by two orders of magnitude.
This was identified as Failure Mode 1 in the honest failure modes document
(likelihood rated "Medium" — in retrospect, it was virtually certain).

**Computation:** `comp3b_gap_equation_check.py`

### 3. Curvature catalysis is exponentially suppressed

Gravitational catalysis (Gorbar & Gusynin 2008) lowers the threshold for
already-attractive channels. It cannot flip the sign of a repulsive channel.

For the attractive case (γ > 1), catalysis at Planck curvature R ~ M_Pl² produces:

```
M* ~ Λ exp(−const/(G_SP × R)) ~ exp(−2100) ≈ 10⁻⁹¹⁴ M_Pl
V_vac ~ M*⁴ ~ 10⁻³⁶⁵⁸ M_Pl⁴
```

The observed dark energy is ρ_Λ ~ 10⁻¹²² M_Pl⁴. The gap is ~3500 orders of
magnitude. Even at R = 100 M_Pl², the condensate scale is M* ~ 3×10⁻⁵ M_Pl,
far below what is needed.

**Computation:** `comp3b_gap_equation_check.py`, `comp3_one_loop_veff.py`

### 4. Multi-flavor and vector/axial alternatives do not rescue the mechanism

- **Multi-flavor:** Inter-flavor contributions to S/P channels vanish because
  tr(γ^μ) = 0 and tr(γ^μγ⁵) = 0 (traces factorize for different species).
- **Vector/axial condensation:** The VV and AA channels are attractive, but a
  vector condensate breaks Lorentz invariance and does not produce isotropic
  vacuum energy compatible with dark energy.
- **σπ mixing (Possibility A):** The VA cross-term vanishes identically for
  identical single-flavor fermions. V_eff has O(2) symmetry in (σ, π).
  Possibility B is realized, not Possibility A.

**Computation:** `comp2b_fierz_verification.py`, `comp3_one_loop_veff.py`

---

## Additional Finding: Perfect-Square Structure

The torsion-induced four-fermion interaction has the form:

```
L_4f = −G_eff [ψ̄γ^μγ⁵ψ + (1/γ)ψ̄γ^μψ]²
```

with G_eff = (3κ²/16) γ²/(γ²+1). This is a perfect square of a single combined
current J^μ = axial + (1/γ)×vector. The couplings G_V, G_A, G_VA in the
canonical problem statement are NOT independent parameters — they are constrained
by this squared-current structure.

At γ = 0.274, the vector admixture 1/γ ≈ 3.65 is O(1), not a small perturbation.
The vector sector dominates over the axial sector.

---

## What the Canonical Problem Statement Got Right

- Identified the pseudoscalar channel as the first to check (correct)
- Separated Possibility A vs B for the symmetry question (B realized)
- Defined three quantitative gates (Gate 1 failed cleanly)
- Listed "What this memo does not assume" (none of those assumptions were needed)
- The gate structure prevented wasted effort on Gates 2 and 3

## What Could Have Been Caught Earlier

- The γ = 1 sign flip is derivable from the Fierz identity without any numerics.
  It could have been identified at the Fierz stage of the computation sequence
  (Computation 3) as a program-threatening result.
- The 175× subcriticality of the gravitational coupling is well-known in the
  literature (Failure Mode 1). A more careful pre-computation literature review
  would have flagged this as the dominant risk.

---

## Impact on Paper 1

**None.** Paper 1 already labels w = −1 as an assumption. The paper explicitly states:

> "For the residual to persist as a true vacuum energy, one must show that integrating
> out the spin degrees of freedom in the early universe generates an IR-constant term
> in the effective action."

The Track B closure means that specific showing has not been achieved via the
condensate mechanism. The paper's phenomenological framing is correct and does not
need revision beyond optionally noting that the minimal condensate route was tested
and failed.

## Impact on the IR Vacuum Program

Track B (Condensate) is closed. The program's three-track structure remains:

- **Track A (EFT):** Unexplored. Requires its own canonical problem statement.
- **Track B (Condensate):** CLOSED at Gate 1.
- **Track C (Cosmological Matching):** Depends on A or B succeeding first.

Whether to pursue Track A (Branch G: gravitational effective action) is a separate
strategic decision that should not be made as an automatic continuation of Track B.

---

## Artifacts

| File | Content |
|------|---------|
| `comp1_torsion_elimination.py` | Torsion elimination, perfect-square structure, coupling constants |
| `comp2_fierz_rearrangement.py` | Full 16×16 Fierz rearrangement, channel decomposition |
| `comp2b_fierz_verification.py` | Verification of VA vanishing, sign analysis |
| `comp3_one_loop_veff.py` | One-loop V_eff, curvature corrections, multi-flavor analysis |
| `comp3b_gap_equation_check.py` | Gap equation, critical coupling, catalysis suppression |
| `figures/veff_repulsive_vs_attractive.png` | V_eff comparison plot |
| `figures/G_SP_vs_gamma.png` | Coupling vs γ plot |
| `notes/comp3_results_analysis.md` | Detailed Fierz result analysis |
| `notes/gate1_status_20260313.md` | Gate 1 failure report |

All computations are reproducible with Python 3.14 + SymPy 1.14 + NumPy + SciPy.
