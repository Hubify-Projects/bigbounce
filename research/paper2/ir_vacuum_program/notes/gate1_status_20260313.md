# Gate 1 Status Report: Single-Flavor Pseudoscalar Condensate

**Date:** 2026-03-13
**Verdict:** FAILED (minimal single-flavor NJL route)
**Confidence:** HIGH — three independent lines of evidence converge

---

## What Was Tested

The canonical problem statement (v3, frozen) asked whether the pseudoscalar
condensate Φ = ⟨ψ̄iγ⁵ψ⟩ forms via the NJL mechanism from torsion-induced
four-fermion interactions at the Barbero-Immirzi value γ = 0.274.

## Three Results That Kill This Route

### Result 1: The S/P channel is repulsive at γ < 1

The Fierz rearrangement of the torsion-induced four-fermion interaction gives
an effective S/P coupling:

```
G_SP = G_eff × (1 - 1/γ²) = (3κ²/16) × (γ² - 1)/(γ² + 1)
```

This changes sign at γ = 1:
- γ > 1: attractive (condensation possible in principle)
- γ = 1: decoupled
- γ < 1: REPULSIVE (condensation impossible via NJL)

At γ = 0.274: G_SP < 0. The scalar/pseudoscalar channel is repulsive.

### Result 2: Even with the correct sign, the coupling is 175× too weak

The NJL critical coupling for condensation is G_crit = 2π²/(N_c Λ²).
The gravitational four-fermion coupling is G ~ κ² ~ 1/M_Pl². With Λ ~ M_Pl:

```
G_SP / G_crit ≈ 0.006
```

The coupling is ~175 times too weak for NJL condensation, **even when attractive**.
This is the standard result in the literature (Failure Mode 1 in 05_honest_failure_modes.md).

### Result 3: Gravitational catalysis is exponentially suppressed

With curvature R = M_Pl² (Planck-scale, i.e., the bounce):

```
M* ~ Λ exp(-const/(G_SP × R)) ~ exp(-2100) ≈ 10⁻⁹¹⁴ M_Pl
V_vac ~ M*⁴ ~ 10⁻³⁶⁵⁸ M_Pl⁴
```

Compared to the observed dark energy ρ_Λ ~ 10⁻¹²² M_Pl⁴, the catalyzed
condensate vacuum energy is smaller by ~3500 orders of magnitude.

Even at R = 100 M_Pl² (far above Planck curvature), M* ≈ 3×10⁻⁵ M_Pl —
still producing vacuum energy far below observational scales.

## What Is Now Ruled Out

- Single-flavor pseudoscalar condensate via NJL at γ = 0.274 ✗
- Multi-flavor rescue of the S/P channel (inter-flavor traces vanish) ✗
- Gravitational catalysis rescue (wrong sign + too weak) ✗
- Vector/axial condensation as dark energy (breaks Lorentz invariance) ✗

## What Survived

### Possibility A vs B (Q5 from canonical statement)

**Possibility B is realized.** The VA cross-term vanishes for identical fermions.
The effective potential has O(2) symmetry in (σ, π). No explicit π → −π breaking.

However, this is somewhat moot because the channel is repulsive regardless.

### The perfect-square structure

The four-fermion interaction is L_4f = -G_eff (J^μ)² with a single combined current.
G_V, G_A, G_VA are NOT independent — they are constrained by this structure.
This is a clean result that should be stated in any future publication.

## What the Canonical Problem Statement Got Right

- The honest failure modes document (05) listed "No Nontrivial Minimum" as
  Failure Mode 1 with "Medium" likelihood. The likelihood was underestimated
  but the mode was correctly identified.
- The canonical statement's "What This Memo Does Not Assume" box correctly
  listed that it does not assume Φ ≠ 0.
- The gate structure worked as designed: Gate 1 failed cleanly, before
  wasting effort on Gates 2 and 3.

## Remaining Active Branches

### Branch S: Single-flavor curvature rescue — CLOSED

Tree-level repulsion + exponential catalysis suppression = no viable route.

### Branch F: Multi-flavor extension — NEEDS INVESTIGATION

The inter-flavor S/P channel vanishes at the trace level for current-current
interactions. However, this analysis assumed the torsion-induced interaction
couples universally to all fermion species. If different species have different
effective couplings (e.g., through mass-dependent corrections), the inter-flavor
structure may be richer.

**Status:** Not yet ruled out but not obviously viable. Low priority.

### Branch G: Gravitational effective action (non-NJL)

The vacuum energy may not come from a fermion condensate at all. It could arise
from the gravitational effective action Γ[g] after integrating out ALL matter,
not from a specific condensate channel. The Holst term's contribution to the
one-loop gravitational effective action is a separate computation (closer to
Track A of the original program, not Track B).

**Status:** Unexplored. This bypasses the NJL framework entirely.
Reference: Chattopadhyay (2023) [2310.10405] computed the one-loop effective
action in chiral EC gravity — this is the most directly relevant paper.

### Branch E: Different value of γ

If γ > 1 (which some approaches beyond LQG black hole entropy allow), the S/P
channel becomes attractive. However, the coupling remains ~175× too weak for
NJL condensation even then, unless Λ ≫ M_Pl (which requires new physics).

**Status:** Technically alive but requires abandoning the LQG value γ = 0.274.

---

## Impact on Paper 1

None. Paper 1 already labels w = −1 as an assumption. The paper explicitly states
that "one must show that integrating out the spin degrees of freedom generates an
IR-constant term." This computation is the beginning of that showing, and the
first-pass answer is: the NJL condensate route does not work.

The framework remains phenomenological. **This is a perfectly acceptable
scientific outcome** (as stated in the canonical problem statement).

---

## Recommended Program Update

Per the branching protocol in 06a_frozen_assumptions_and_change_log.md:

1. Record Gate 1 failure for the pseudoscalar condensate order parameter
2. Do NOT reopen the canonical problem statement for casual edits
3. If pursuing Branch G (gravitational effective action), create a new
   versioned problem statement (06_canonical_problem_statement_v4.md)
   with a different order parameter or mechanism
4. The honest failure is itself a publishable result
