# Next-Stage Research Program — Master Summary

**Date:** 2026-03-13
**Status:** PLANNING — No branch is authorized for heavy computation until its canonical statement is frozen
**Prerequisite:** Track B (condensate) and Branch G v1 (strict one-loop) are both closed with clean negative results

---

## Context

The minimal EC+Holst+Dirac model, at the tested approximation orders, does not generate novel vacuum physics from the Holst sector. Two routes were tested and failed:

| Route | Result | What was learned |
|-------|--------|-----------------|
| Track B (NJL condensate) | Gate 1 failed | S/P repulsive at γ=0.274; coupling 175× subcritical |
| Branch G v1 (strict 1-loop) | FM-G6 fired | Fermion determinant is γ-independent after torsion elimination |

The framework remains phenomenological. Paper 1 is correct as written. The question now is: what next?

---

## Four New Branches

| Branch | Type | Target | Key question |
|--------|------|--------|-------------|
| **T1** | Theory | Dynamical Immirzi / pseudoscalar extension | Does promoting γ to a field open a genuinely new first-principles route? |
| **T2** | Theory | Non-minimal effective-action route | Does a controlled non-minimal extension generate nontrivial finite-γ vacuum content? |
| **S1** | Signal | Parity-sensitive CMB phenomenology | Can we constrain/detect parity-odd CMB observables more native to the framework than ΔN_eff? |
| **S2** | Signal | Localized early-structure signatures | Does the framework predict narrow feature-like perturbation signatures? |

---

## Recommended Pursuit Order

```
Phase 1 (immediate, parallel):
  S1 — Gate S1-1 only (theory-to-observable mapping assessment)
  T1 — Literature review + canonical statement draft

Phase 2 (after Phase 1 gates):
  S1 — If S1-1 survives: pipeline work (Gate S1-2)
  T1 — If literature review survives: Gate T1-1 computation
  S2 — Begin parameterization study (Gate S2-1)

Phase 3 (after Phase 2 gates):
  T2 — Open only if T1 provides structural insight about what non-minimal terms to target
  S1/S2 — If gates survive: data confrontation (Gates S1-3, S2-3)
```

### Rationale

1. **S1 first** because it requires no new theory — just mapping existing framework content to existing data pipelines. Fastest path to a publishable result (even if null).
2. **T1 next** because the dynamical Immirzi / pseudoscalar extension is the most structurally motivated theory direction (Mercuri 2009, Taveras-Yunes 2009 axion analogy). Literature is well-developed.
3. **S2 in parallel with T1** because feature parameterization is independent of the theory branches and can proceed with Boltzmann code work.
4. **T2 last** because "non-minimal effective action" is currently too vague — it needs input from T1 to know which non-minimal terms are worth computing.

---

## Decision Tree

```
START
  │
  ├── S1: Is there a defensible theory-to-observable mapping?
  │     ├── YES → S1-2: Can it be constrained with available data?
  │     │          ├── YES → S1-3: Nonzero allowed region or just bounds?
  │     │          │          ├── Signal → PUBLISH (detection/preference claim)
  │     │          │          └── Null → PUBLISH (constraint paper)
  │     │          └── NO → CLOSE S1 (document why)
  │     └── NO → CLOSE S1 (no mapping = no signal branch)
  │
  ├── T1: Does dynamical γ produce genuinely new finite low-energy structure?
  │     ├── YES → T1-2: Stable vacuum-like contribution?
  │     │          ├── YES → T1-3: Viable cosmological signal?
  │     │          │          ├── YES → MAJOR UPGRADE (first-principles route opens)
  │     │          │          └── NO → PUBLISH (positive but non-viable result)
  │     │          └── NO → CLOSE T1 (transient only)
  │     └── NO → CLOSE T1 (equivalent to field redefinition / no new content)
  │               │
  │               └── Opens T2? Only if T1 closure reveals a specific
  │                   non-minimal term worth testing. Otherwise T2 stays closed.
  │
  ├── S2: Is there a clean feature parameterization?
  │     ├── YES → S2-2: Propagates into observables?
  │     │          ├── YES → S2-3: Interesting window survives?
  │     │          │          ├── YES → PUBLISH (feature search)
  │     │          │          └── NO → PUBLISH (exclusion)
  │     │          └── NO → CLOSE S2
  │     └── NO → CLOSE S2
  │
  └── T2: (Conditional on T1 results)
        └── Only opened if T1 provides structural guidance
```

---

## Estimated Effort / Likelihood / Value

| Branch | Effort | P(success) | Best realistic outcome | Worst realistic outcome |
|--------|--------|-----------|----------------------|----------------------|
| S1 | Low–Medium (2–4 weeks) | 40% for constraint, 5% for weak preference | Published EB/TB constraint within framework | Null; no defensible mapping |
| T1 | Medium (4–8 weeks) | 15% for new mechanism | New first-principles route with canonical statement | Clean closure (field redefinition, no new content) |
| S2 | Medium (3–6 weeks) | 20% for interesting constraint | Constrained feature window from framework | Too ad hoc to publish |
| T2 | High (6–12 weeks) | 10% for new mechanism | Controlled non-minimal vacuum term | Closure like Branch G v1 but at higher order |

---

## Compute Requirements

| Branch | Local CPU | Cloud CPU | GPU |
|--------|-----------|-----------|-----|
| S1 | Literature + mapping phase | Boltzmann runs if Gate S1-2 survives | None |
| T1 | Symbolic (SymPy), literature | None expected | None |
| S2 | Boltzmann parameter studies | MCMC if Gate S2-2 survives | None |
| T2 | Symbolic + one-loop heat kernel | None expected | None |

---

## Publication Pathways

| Outcome | Publication |
|---------|------------|
| S1 constraint (even null) | Short letter: "Parity-odd CMB constraints on spin-torsion dark energy" |
| T1 new mechanism | Full paper or supplement to Paper 1 |
| T1 closure | Add to existing negative-result note |
| S2 feature constraint | Short letter or section in Paper 2 |
| T2 closure | Add to negative-result note |
| All branches close | Updated negative-result note with expanded scope |

---

## What NOT to Do

- Do NOT silently reopen Track B or Branch G v1 under new names
- Do NOT start heavy computation before the canonical statement is frozen
- Do NOT overclaim observational prospects
- Do NOT modify Paper 1 claims based on speculative new branches
- Do NOT pursue T2 before T1 results are available
- Do NOT treat the signal branches (S1, S2) as validating the theory branches (T1, T2)

---

## Key Documents

| Document | Location |
|----------|----------|
| This master summary | `next_branches/00_master_program_summary.md` |
| T1 planning package | `next_branches/T1_dynamical_immirzi/` |
| T2 planning package | `next_branches/T2_nonminimal_effective_action/` |
| S1 planning package | `next_branches/S1_parity_cmb/` |
| S2 planning package | `next_branches/S2_early_structure/` |
| Track B closure | `ir_vacuum_program/07_track_b_closure.md` |
| Branch G v1 closure | `ir_vacuum_program/notes/branchG_phase1_closure.md` |
| Negative-result supplement | `ir_vacuum_program/supplement_negative_results.tex` |
