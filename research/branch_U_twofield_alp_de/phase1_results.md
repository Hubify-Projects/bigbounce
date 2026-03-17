# Branch U Phase 1 Results: Two-Field ALP + DE

**Date:** 2026-03-17
**Verdict:** BRANCH_U_DEFERRED — No ECH-specific content; reduces to standard axiverse.

---

## What Was Investigated

Five candidate two-field models were assessed for their ability to simultaneously explain cosmic birefringence (β ~ 0.35°) and dark energy (Ω_DE ~ 0.68):

| Model | Description | Verdict |
|-------|-------------|---------|
| U1 | Independent two-ALP | WORKS BUT TRIVIAL |
| U2 | Kinetic mixing | KILLED (doesn't help) |
| U3 | Aligned axions (KNP) | OVERBUILT |
| U4 | Quintessence + spectator | REDUNDANT (= existing model) |
| U5 | Vacuum decay | KILLED (CC problem + Branch J) |

Six possible bounce contributions were tested against the thirteen barriers:

| Bounce mechanism | Blocking barrier | Status |
|-----------------|-----------------|--------|
| Initial conditions | #9 (Liouville) | CLOSED |
| Mass generation | #5 (scale separation) | CLOSED |
| Coupling generation | UV-determined | CLOSED |
| Symmetry breaking | #13 (bounce-vacuum decoupling) | CLOSED |
| Isocurvature | Branch K (T=1) | CLOSED |
| Alignment | Lagrangian-level | CLOSED |

Five dynamical screening mechanisms were assessed:

| Mechanism | Verdict |
|-----------|---------|
| Monodromy | OUT OF SCOPE (string theory) |
| Tracker coupling | OVERTUNED (7 params) |
| EDE + birefringence | TANGENTIAL (different mass scale) |
| Anti-screening | KILLED (instability) |
| Dissipative | KILLED (fine-tuning + constraints) |

---

## Key Findings

### 1. The rolling-vs-freezing tension is fundamental

It follows from energy conservation for a single scalar with a bounded potential: large field displacement (birefringence) requires decreased potential energy (not DE). This is not a model-building accident.

### 2. Two fields resolve the tension trivially

Model U1 (independent ALPs) works by giving each field a separate job. But this is equivalent to spectator ALP + quintessence — a known model class. No ECH-specific physics enters.

### 3. The bounce adds nothing to any two-field model

All six possible bounce contributions are blocked by barriers #5, #9, #13, or the generic transfer function. The thirteen barriers from Branches A–O completely isolate the bounce from the late-time ALP sector.

### 4. No dynamical screening works within ECH

All mechanisms that could make a single field do both jobs either require string-theoretic constructions, introduce more parameters than they explain, or are killed by stability constraints.

---

## Implication for the Paper

**Branch U does not warrant inclusion in Paper 1.** The investigation confirms that:

1. **The spectator ALP is the correct model.** Birefringence and DE are separate phenomena; the spectator model correctly treats them separately.
2. **The two-field extension adds parameters without predictions.** AIC/BIC would penalize it relative to spectator + Λ.
3. **The bounce is background.** No ECH-specific prediction emerges from two-field models.

**Paper treatment:** A brief paragraph in the Discussion noting that the rolling-vs-freezing tension motivates separate treatment of birefringence and DE, and that a two-field axiverse extension is deferred to future work with DESI DR2 w(z) constraints.

---

## Branch U Status: DEFERRED

- Theory investigation: COMPLETE
- MCMC analysis: NOT WARRANTED
- Bounce connection: CLOSED (all routes blocked)
- Paper inclusion: ONE PARAGRAPH in Discussion
- Trigger for reopening: DESI DR2 w_0 ≠ -1 at > 3σ AND/OR LiteBIRD β > 0 at > 10σ

---

## Files

| File | Content |
|------|---------|
| `01_problem_statement.md` | Rolling-vs-freezing tension definition |
| `02_candidate_models.md` | 5 models screened |
| `03_bounce_connection_map.md` | 6 bounce mechanisms tested |
| `04_dynamical_screening.md` | 5 screening mechanisms tested |
| `05_background_equations.md` | Model U1 equations and parameter count |
| `06_first_calculation_target.md` | Calculation plan + go/no-go (NO-GO) |
| `phase1_results.md` | This file |
