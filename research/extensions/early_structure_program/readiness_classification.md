# Readiness Classification

**Date:** 2026-03-13
**Program:** Early Structure from Bounce Cosmology

---

## Classification Decisions

| Track | Status | Rationale |
|-------|--------|-----------|
| A — SMBH Seeds | **READY FOR FORWARD-MODEL CONSTRAINT PLOT** | Minimum seed mass calculations are standard astrophysics. Can be done with published (M_BH, z) data points. No MCMC needed or justified — too few data points for population inference on seed parameters. The bounce connection is motivational only. |
| B — PBH-like Seeds | **READY FOR FORWARD-MODEL CONSTRAINT PLOT** | PBHbounds provides machine-readable constraint curves. Mapping P(k) → f_PBH(M) is standard Press-Schechter. No MCMC needed — this is a constraint overlay, not a fit. |
| C — Joint Synthesis | **READY FOR FORWARD-MODEL CONSTRAINT PLOT** | Combines A and B on shared A_bump(k_bump) parameter space. The "allowed window" where seeds help but PBH constraints are satisfied is a well-posed question. |

**No track is READY FOR REAL LIKELIHOOD / MCMC.** The reasons:
1. Track A has too few high-z SMBH data points (< 20) for meaningful population MCMC
2. Track B has no forward model from framework parameters to f_PBH(M) — the P(k) is a free parameterization
3. The framework does not predict the P(k) feature, so any MCMC would constrain a phenomenological parameter disconnected from the theory

---

## Rankings

### By scientific defensibility

1. **Track B (PBH constraints)** — The PBHbounds data is gold standard, the mapping is standard, the output (excluded P(k) regions) is model-independent
2. **Track C (joint synthesis)** — Inherits defensibility from B, adds the SMBH requirement as a target
3. **Track A (SMBH seeds)** — Individual high-z SMBH observations are solid, but the connection to our framework is purely motivational

### By likely usefulness for the current paper

1. **None.** The perturbation spectrum through the bounce has not been calculated. Including P(k) phenomenology in the current paper would be:
   - Disconnected from the paper's equations
   - Potentially misleading (suggesting the framework predicts something it doesn't)
   - Better suited as a future-work discussion paragraph

2. If forced to include something: a **2-3 sentence paragraph** in the Future Directions section noting that "the bounce-to-inflation transition may imprint features on P(k) at small scales, with implications for early SMBH seed formation and PBH constraints; a full perturbation calculation is needed to determine whether such features arise in the spin-torsion variant."

### By likely usefulness for a separate follow-up paper

1. **Track C (joint synthesis)** — Best paper potential: "Primordial Perturbation Features from Bouncing Cosmologies: Implications for SMBH Seeds and PBH Constraints." This is a legitimate 15-20 page paper regardless of the spin-torsion framework.
2. **Track B** — Strong standalone section
3. **Track A** — Useful context but not novel on its own (minimum seed mass calculations are well-studied)

---

## The N_tot Problem

A critical issue for the framework connection:

With N_tot = 92 (as required by the dark energy constraint), bounce features are pushed to comoving scales k ~ 10^{13} Mpc^{-1}, corresponding to PBH masses M ~ 10^{-18} M_☉ (sub-planetary). This is:
- **Irrelevant for SMBH seeds** (need M ~ 10^3-10^6 M_☉, k ~ 10^5-10^6 Mpc^{-1})
- **In the asteroid-mass PBH window** where constraints are weakest
- **Potentially interesting for dark matter** if the bounce produces sufficient enhancement

For bounce features to appear at SMBH-relevant scales, one would need N_tot ≈ 70, which contradicts the dark energy constraint. This tension should be stated clearly in any publication.

**However:** The N_tot constraint applies to the TOTAL number of e-folds. The bounce-to-inflation transition dynamics might produce broader spectral features that extend beyond the naive single-scale estimate. This is unknown without the full perturbation calculation.

---

## Compute Requirements

| Track | Compute | Infrastructure |
|-------|---------|----------------|
| A | <1 min, local Python | None needed |
| B | <5 min, local Python | PBHbounds repo (git clone) |
| C | <5 min, local Python | Same as A + B |

**No RunPod pods needed. No MCMC infrastructure needed.**
