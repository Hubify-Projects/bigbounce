# Phase 3: Upgrade Readiness Decision

**Date:** 2026-03-13

---

## Decision: **B — Upgrade to Gaussian summary-likelihood inference**

---

## Evidence-Based Assessment

### Option A: Keep as consistency check only
- **Against:** The current analysis already performs the mathematical operations of a Gaussian likelihood (inverse-variance weighting = maximum-likelihood estimation for Gaussians). Calling it "just a consistency check" undersells what it actually computes.

### Option B: Upgrade to Gaussian summary-likelihood inference ← **SELECTED**
- **For:** Two independent published measurements, each with well-characterized Gaussian errors. The likelihood L(β) = Π_i N(β; β_i, σ_i) is exactly the right tool. The posterior is analytically tractable. Adding explicit priors, Bayes factor for β≠0, and 2D (f_photon, C₀) mapping is straightforward and honest.
- **Against:** None. This is the correct statistical framing of what the data support.

### Option C: Upgrade to lightweight MCMC
- **Against:** With 2 Gaussian data points and at most 2 parameters (β, or equivalently f_photon with fixed C₀), the posterior is analytically known. Running emcee or cobaya would produce identical results at higher computational cost with no additional information. This would be performative rigor, not real rigor.
- **Exception:** If we were jointly fitting β alongside Paper 1 MCMC parameters (H₀, ΔN_eff, etc.), a sampler would be justified. But β is measured independently of the cosmological parameters — the only connection is through f_photon, which is undetermined. There is no non-trivial parameter correlation to explore.

### Option D: Future work only
- **Against:** The data exist and are public. The analysis is trivial. There is no reason to defer.

---

## What the Upgrade Includes

### Required components:
1. **Explicit Gaussian likelihood** on β using Eskilt (2022) and ACT DR6 (2025)
2. **Explicit prior** on β: uniform [−1°, 1°]
3. **Posterior** P(β | data) — analytically computed
4. **Bayes factor** for H₁: β ≠ 0 vs H₀: β = 0 — Savage-Dickey density ratio
5. **Derived posterior** on f_photon for fixed C₀ values (C₀ = 0.3, 1.0, 3.0)
6. **2D degeneracy plot** showing f_photon vs C₀ at fixed β_obs
7. **EB shape comparison** against Eskilt (2022) Table 1 bandpowers — χ² for uniform rotation

### NOT included (would be dishonest):
- Full map-level likelihood (data not public)
- MCMC sampler (analytically tractable problem)
- Joint fit with Paper 1 parameters (no non-trivial coupling)
- Prediction of f_photon from first principles (open problem)

---

## Justification Summary

| Criterion | Assessment |
|-----------|-----------|
| Data available? | YES — 2 independent published β measurements |
| Data quality sufficient? | YES — 2.7σ and 2.9σ individual, 3.9σ combined |
| Likelihood well-defined? | YES — Gaussian, analytically tractable |
| Parameters identifiable? | PARTIALLY — β is identified; (f_photon, C₀) are degenerate |
| Prior specification clear? | YES — uninformative on β; log-uniform on coupling |
| Computational cost justified? | YES — runs in < 1 second on any machine |
| Scientific value? | MODERATE — quantifies naturalness of coupling scale |
| Overclaiming risk? | LOW if labeled correctly as "summary-likelihood inference using published β measurements" |

---

## Risk Mitigation

The main risk is readers interpreting "likelihood inference" as implying more statistical power than exists. Mitigations:

1. **Label explicitly** as "Gaussian summary-likelihood inference using published isotropic birefringence measurements"
2. **State explicitly** that no map-level or harmonic-space data are used
3. **State explicitly** that the (f_photon, C₀) degeneracy is not broken by the data
4. **State explicitly** that the EB shape test is a forward-model comparison, not a likelihood fit
