# IR Vacuum Persistence Program — Executive Summary

**Date:** 2026-03-13
**Status:** TRACK B CLOSED + BRANCH G v1 CLOSED — Both first-principles routes to dark energy have failed at the tested approximation orders
**Goal:** Derive (or rigorously disprove) that the spin-torsion parity-odd sector produces a persistent IR vacuum term with w ≈ −1

---

## The Gap

The paper (Sec. III.B.1, line 308 of `arxiv/main.tex`) states the exact issue:

> "The operator ⟨ε^{abcd} K_{ab} R_{cd}⟩ is sourced by the fermion spin density, which vanishes at late times (K_{ab} → 0). For the residual to persist as a true vacuum energy, one must show that integrating out the spin degrees of freedom in the early universe generates an IR-constant term in the effective action."

This is **the** central open problem. Everything else in the framework — cosmological fits, birefringence, fine-tuning reduction — rests on the assumption that such a term exists.

## Track B Result: GATE 1 FAILED (2026-03-13)

The condensate route was tested via explicit computation (Fierz rearrangement, gap equation analysis, one-loop effective potential with curvature corrections). Four independent results close this route:

1. **Wrong sign:** G_SP ∝ (γ²−1)/(γ²+1) is repulsive at γ = 0.274 < 1
2. **Too weak:** G_SP/G_crit ≈ 0.006 even when attractive (γ > 1)
3. **Catalysis suppressed:** M* ~ exp(−2100) at Planck curvature
4. **No multi-flavor rescue:** Inter-flavor S/P traces vanish

See `07_track_b_closure.md` for the full negative-result package.

**Path 3 of the decision tree is realized: no residual survives via the condensate mechanism. The framework remains phenomenological.**

## What Was Learned

- The four-fermion interaction has a perfect-square form: L = −G_eff(J^μ)² with J = axial + (1/γ)×vector. The couplings G_V, G_A, G_VA are constrained, not independent.
- The VA cross-term vanishes for identical fermions (Possibility B, not A). V_eff has O(2) symmetry in (σ, π).
- The critical γ for S/P attractiveness is γ = 1 exactly.
- The gate structure worked as designed: clean failure at Gate 1, no wasted effort on Gates 2–3.

## Decision Tree (Outcome)

| Path | Outcome | Implication |
|------|---------|-------------|
| **1** | Direct residual vacuum term survives | ~~Major upgrade~~ |
| **2** | Residual survives but is time-dependent | ~~Evolving dark sector~~ |
| **3** ← | **No residual survives via condensate** | **Framework remains phenomenological** |

**Path 3 is not failure. It is good science.**

## Branch G v1 Result: FM-G6 FIRES (2026-03-13)

The strict one-loop effective-action route was tested by systematic analysis of whether the Barbero-Immirzi parameter γ enters the one-loop fermion determinant after torsion elimination. Three candidate channels were checked:

1. **Modified background:** γ enters the background solution, not the effective action functional. Excluded per canonical statement.
2. **Parity-odd sector / η-invariant:** Uses the Levi-Civita Dirac operator, which is γ-independent. P₄ = 0 on homogeneous backgrounds. Curvature-local, not vacuum-like.
3. **Measure corrections:** Torsion elimination is classical substitution. No Jacobian in the fermion sector.

**Literature confirmation:**
- Chattopadhyay (2023) [2310.10405]: Computes the graviton (not fermion) loop. No γ, no fermions. Different computation.
- Shapiro & Teixeira (2014) [1402.4854]: γ-dependent one-loop divergences DO appear — but in the **graviton** loop with **external** fermion currents. Fermions are classical backgrounds, not quantum fields. Confirms γ enters through graviton vertices, not the fermion operator.

**The fermion determinant at strict one-loop is the standard Seeley-DeWitt expansion for a Dirac field on a Riemannian background. All coefficients are γ-independent.**

See `notes/branchG_phase1_closure.md` for the full analysis.

## Track Status

- **Track A — EFT derivation (Branch G v1):** **CLOSED.** FM-G6 at Phase 1. The strict one-loop fermion determinant has no novel γ-dependent content.
- **Track B — Condensate mechanism:** **CLOSED.** Gate 1 failed.
- **Track C — Cosmological matching:** Both prerequisite routes (A, B) have failed.

## Impact on Paper 1

None. Paper 1 already labels w = −1 as an assumption. The condensate failure reinforces the phenomenological framing. The paper is correct as written.

## What Was Learned (Combined)

- Track B showed the NJL condensate mechanism fails: wrong sign, too weak, no rescue
- Branch G v1 showed the strict one-loop effective action has no novel Holst content: γ enters only through S_4f, which doesn't contribute at one loop
- Shapiro & Teixeira (2014) shows γ CAN enter through graviton loops — but that's a different (harder) computation
- The framework remains phenomenological at all tested approximation orders
- **Both negative results are clean, publishable, and scientifically valuable**

## What Is NOT Ruled Out

- Graviton one-loop with fermion currents (Shapiro-Teixeira approach — γ enters)
- Two-loop / Approach A (S_4f vertices contribute)
- Non-perturbative effects
- Non-minimal couplings

Each would require its own branch definition. None is automatically authorized.

## What NOT to Do

- Do NOT reframe the failures as "preliminary" — they are definitive at the stated approximation orders
- Do NOT patch Paper 1 with verbal arguments about alternative mechanisms
- Do NOT treat the negative results as wasted work — they map the theory landscape
- Do NOT start new routes without frozen canonical problem statements

## Key Documents

| Document | Status |
|----------|--------|
| `06_canonical_problem_statement.md` | Frozen v3 — defined the test |
| `06a_frozen_assumptions_and_change_log.md` | Freeze log |
| `07_track_b_closure.md` | Negative-result package |
| `notes/gate1_status_20260313.md` | Detailed Gate 1 failure report |
| `derivations/comp1_torsion_elimination.py` | Torsion elimination + perfect-square |
| `derivations/comp2_fierz_rearrangement.py` | Fierz decomposition |
| `derivations/comp2b_fierz_verification.py` | VA vanishing verification |
| `derivations/comp3_one_loop_veff.py` | One-loop V_eff + catalysis |
| `derivations/comp3b_gap_equation_check.py` | Gap equation + subcriticality |
| `08_branchG_canonical_problem_statement.md` | Branch G definition (v2 frozen) |
| `08a_branchG_freeze_log.md` | Branch G freeze log + Track B comparison |
| `notes/branchG_phase1_closure.md` | Branch G Phase 1 closure (FM-G6) |
| `derivations/branchG_phase1_operator_analysis.py` | Three-channel operator analysis |
