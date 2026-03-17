# Branch S2 — Canonical Problem Statement: Localized Early-Structure Signatures

**Version:** v1 (DRAFT — NOT FROZEN)
**Date:** 2026-03-13
**Status:** Awaiting parameterization study before freeze
**Prerequisite:** None (signal branch, independent of theory branches)

---

## Motivation

The main paper's framework modifies early-universe physics through the bounce-to-inflation transition and the spin-torsion sector. These modifications could leave narrow, localized signatures in the primordial power spectrum, transfer function, or growth history — features more specific and testable than the broad ΔN_eff shift already tested (and found null).

The key physical mechanisms that could produce features:

1. **Bounce-to-inflation transition:** The transition from contraction to expansion produces specific initial conditions for perturbations. If these differ from standard Bunch-Davies vacuum, they could leave features in P(k) at specific k-scales.
2. **Torsion-modified transfer function:** The four-fermion interaction modifies the equation of state at very early times (near the bounce), which could produce a localized step or oscillation in the matter transfer function.
3. **Parity-odd perturbation sector:** The parity-odd operator could introduce helicity-dependent modifications to the primordial spectrum, visible as TB or EB correlations at specific ℓ ranges.

**This is a signal branch.** It asks: "Does the framework predict narrow features, and are they detectable?"

---

## The Central Question

> Does the spin-torsion dark energy framework predict localized (narrow in k-space or ℓ-space) modifications to the primordial power spectrum, transfer function, or CMB correlation functions that are:
> (a) derivable from the framework's specific physics (not generic feature templates),
> (b) distinguishable from noise or generic feature models,
> (c) testable with existing or near-future data?

---

## Candidate Feature Types

### Type A: Bounce-induced oscillations in P(k)
- **Mechanism:** Non-Bunch-Davies initial conditions from the bounce produce oscillations in P(k) at trans-Planckian or near-bounce scales.
- **Scale:** k ~ k_bounce (the comoving scale that exits the horizon at the bounce-to-inflation transition). This scale is determined by the bounce dynamics and could correspond to ℓ ~ 10–100 in the CMB or to small-scale structure probes.
- **Expected form:** P(k) = P_standard(k) × [1 + A_osc × sin(ω ln(k/k_*) + φ)]
- **Distinguishing feature:** The oscillation frequency ω is set by the bounce dynamics, not a free parameter.

### Type B: Step in the transfer function
- **Mechanism:** The four-fermion interaction modifies the equation of state near the bounce (w ≠ 1/3 for a brief period), producing a step-like feature in the transfer function.
- **Scale:** The step scale is set by the Hubble radius at the time the equation of state changes.
- **Expected form:** T(k) = T_standard(k) × [1 + A_step × tanh((ln k - ln k_step)/Δ)]
- **Distinguishing feature:** The step amplitude A_step and width Δ are determined by the four-fermion coupling strength and duration.

### Type C: Parity-odd primordial features
- **Mechanism:** The parity-odd operator introduces helicity-dependent modifications to primordial tensor perturbations, producing features in TB or EB at specific ℓ.
- **Scale:** Determined by the time evolution of the parity-odd operator during inflation.
- **Expected form:** C_ℓ^{TB} or C_ℓ^{EB} with a specific ℓ-shape
- **Connection to S1:** This overlaps with S1 but focuses on localized features rather than uniform birefringence.

### Type D: Enhanced small-scale power
- **Mechanism:** The bounce could produce enhanced power at small scales (high k), potentially observable through PBH constraints, spectral distortions (μ, y), or 21cm.
- **Scale:** k > 1 Mpc⁻¹ (sub-CMB scales)
- **Expected form:** P(k) enhancement at specific k range

---

## Gate Structure

### Gate S2-1: Clean and minimally defensible parameterization
At least one candidate feature type (A–D) has:
- a parameterization with ≤ 3 free parameters,
- parameters that are connected to the framework's physics (not arbitrary),
- a specific k or ℓ range prediction.

**Kill criterion:** If all feature types require > 3 arbitrary parameters with no connection to framework physics, Gate S2-1 fails. The features are too ad hoc.

### Gate S2-2: Propagation into observables
The parameterized feature can be:
- propagated through CAMB or CLASS into CMB C_ℓ or matter P(k),
- compared with existing data (Planck, ACT, BOSS/DESI BAO),
- without requiring a custom Boltzmann solver.

**Kill criterion:** If the feature requires modifications to the perturbation equations that cannot be implemented as a CAMB modification (and would need a from-scratch solver), Gate S2-2 fails for resource reasons.

### Gate S2-3: Interesting parameter space survives
After data confrontation, the framework-preferred feature amplitude:
- is not already excluded by data (A_feature > A_excluded), AND
- is not so small that it's undetectable even with next-generation experiments.

**Kill criterion:** If the entire framework-preferred parameter range is either excluded or undetectable, Gate S2-3 fails.

---

## Predeclared Failure Modes

| Code | Failure mode | Likelihood |
|------|-------------|-----------|
| FM-S2-1 | Too ad hoc (> 3 free parameters, no physics connection) | 30% |
| FM-S2-2 | Not distinguishable from generic feature templates | 25% |
| FM-S2-3 | All parameter space excluded by Planck | 15% |
| FM-S2-4 | Feature amplitude far below detection threshold | 20% |
| FM-S2-5 | Requires custom Boltzmann solver (resource barrier) | 15% |
| FM-S2-6 | Feature scale falls outside observable range | 10% |

---

## Computation Sequence

### Phase 1: Parameterization Study (2 weeks)

| Step | Task | Output |
|------|------|--------|
| 1.1 | Review bounce-to-inflation perturbation literature | Reading notes |
| 1.2 | Derive expected feature scales from bounce parameters | k_bounce, k_step formulas |
| 1.3 | Propose minimal parameterizations for Types A–D | Explicit templates |
| 1.4 | Assess Gate S2-1 | Go/no-go for each type |
| 1.5 | Select most promising type(s) for Phase 2 | Selection document |

**Deliverable:** `notes/S2_parameterization_study.md`

### Phase 2: Boltzmann Implementation (2–3 weeks, conditional on S2-1)

| Step | Task | Output |
|------|------|--------|
| 2.1 | Implement feature template as CAMB modification | Python script |
| 2.2 | Generate C_ℓ with and without feature | Template spectra |
| 2.3 | Compare with Planck/ACT residuals | Preliminary constraint |
| 2.4 | Test Gate S2-2 | Pipeline verdict |

**Deliverable:** `derivations/S2_feature_boltzmann.py`

### Phase 3: Data Confrontation (1–2 weeks, conditional on S2-2)

| Step | Task | Output |
|------|------|--------|
| 3.1 | Run MCMC with feature parameters | Posteriors |
| 3.2 | Compute Bayesian evidence for feature vs no-feature | Bayes factor |
| 3.3 | Test Gate S2-3 | Final verdict |

**Deliverable:** `derivations/S2_mcmc_feature.py`

---

## Expected Figures / Tables

| Figure | Description |
|--------|-------------|
| S2_feature_templates | P(k) with each candidate feature type overlaid |
| S2_Cl_comparison | C_ℓ^{TT} residuals with and without feature |
| S2_parameter_posterior | Posterior on feature amplitude and scale |
| S2_detection_forecast | Fisher forecast for CMB-S4 / LiteBIRD detection threshold |

---

## Compute Requirements

| Phase | Compute | Duration |
|-------|---------|----------|
| Phase 1 | Local CPU only | 2 weeks |
| Phase 2 | Local CPU (CAMB runs) | 2–3 weeks |
| Phase 3 | Cloud CPU for MCMC (Cobaya) | 1–2 weeks |

No GPU required.

---

## Honest Assessment

The most likely outcome is that **no feature is derivable from the framework with fewer than 3 free parameters** (FM-S2-1). The bounce-to-inflation transition is not modeled in enough detail to predict specific feature shapes. The perturbation roadmap (`first_principles_roadmap/`) was designed to eventually address this, but it requires its own multi-phase program.

If a feature IS derivable, the most likely result is an **exclusion or uninformative bound** — existing CMB data already constrain features in P(k) quite tightly at CMB scales.

The strongest publishable outcome would be showing that the bounce-to-inflation transition predicts features at specific scales that are **not yet constrained** (e.g., sub-CMB scales probed by μ-distortions or 21cm), providing targets for future observations.

---

## Connection to Perturbation Roadmap

The existing `first_principles_roadmap/` (phases 1–8) is the long-term program for deriving perturbation predictions from the bounce. S2 is a shorter-term phenomenological effort that uses parameterized templates rather than first-principles derivations. If the perturbation roadmap eventually produces concrete predictions, they would supersede S2's templates.
