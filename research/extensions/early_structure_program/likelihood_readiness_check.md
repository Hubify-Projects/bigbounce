# Likelihood Readiness Check

**Date:** 2026-03-13
**Program:** Early Structure from Bounce Cosmology

---

## Question: Is a Lightweight MCMC Justified?

**NO.**

---

## Reasons

### 1. No model-to-observable chain exists

The framework does not predict any P(k) feature parameters. An MCMC would constrain purely phenomenological parameters (k_*, A_bump, Δ) that have no connection to the framework's equations. This is equivalent to "fitting a bump to nothing."

### 2. The window analysis is the honest stopping point

The forward-model grid scan has fully characterized the allowed parameter space. The result — a narrow 0.4-decade window at scales disconnected from the framework — does not benefit from MCMC refinement. An MCMC would produce prettier contour plots of the same conclusion.

### 3. The data situation does not support statistical inference

For SMBH seeds:
- < 20 high-z SMBH observations (insufficient for population MCMC)
- Individual growth-time arguments are deterministic, not statistical

For PBH constraints:
- PBH upper limits are one-sided bounds, not detections
- There is no positive detection to fit

For μ-distortions:
- FIRAS provides a single upper limit (μ < 9 × 10⁻⁵)
- This is a binary cut, not a likelihood surface

### 4. An MCMC would be misleading

Running an MCMC on phenomenological parameters and presenting contour plots would create the false impression that the framework constrains these parameters. It does not. The rigor would be performative, not scientific.

---

## When Would an MCMC Be Justified?

An MCMC becomes defensible when ALL of the following are satisfied:

1. ☐ The perturbation spectrum through the spin-torsion bounce has been calculated
2. ☐ The resulting P(k) has features at specific scales with derived amplitudes
3. ☐ The derived (k_*, A_bump) map onto observable predictions
4. ☐ Sufficient data exists to constrain the derived parameters
5. ☐ The P(k) feature is parameterized in terms of framework quantities (e.g., γ, ρ_crit, N_tot)

Currently: 0 of 5 conditions are met.

---

## Verdict

**The forward-model window analysis IS the honest stopping point.**

Do not launch any MCMC. The next scientifically productive step is the perturbation calculation through the spin-torsion bounce, which is a 1-2 year project requiring numerical LQC expertise outside the scope of the current paper.
