# Branch U: First Calculation Target Assessment

**Date:** 2026-03-17

---

## What Would a Branch U Calculation Look Like?

If we were to proceed with a full Branch U analysis, the first calculation would be:

### Target: Joint (β, w_0, w_a) Posterior for Two-ALP Model

**Inputs:**
1. Birefringence: β_obs = 0.342 ± 0.094° (Planck PR4 + ACT DR6)
2. Background expansion: Planck 2018 + DESI DR1 BAO + Pantheon+ SNe
3. CMB power spectra: Planck TT+TE+EE+lowE

**Sampled parameters:** θ_{i,1}, log10(m_1), θ_{i,2}, log10(m_2), Ω_b h², Ω_c h², h, τ, n_s, A_s

**Derived:** β, w_0, w_a, Ω_DE, H_0, σ_8

**Computational cost estimate:**
- 10 parameters → need ~10⁴ samples per chain × 8 chains
- Each evaluation: ALP ODE (~20 ms) + CAMB (~3 s) + likelihoods (~0.1 s) ≈ 3.1 s
- Total: ~70 hours on 8-core machine (or ~9 hours on 64 chains on RunPod)
- Cost: ~$30-50 RunPod

---

## Should We Do This Calculation?

### Arguments FOR:
1. Demonstrates compatibility of ALP birefringence with standard cosmology
2. Produces a publishable triangle plot (θ_i vs H_0 vs w_0)
3. May constrain θ_{i,2} and m_2 from expansion data
4. Shows explicitly that birefringence and expansion decouple (spectator confirmation)

### Arguments AGAINST:
1. **Already known outcome.** The spectator ALP decouples from expansion by construction. The joint posterior will show zero correlation between θ_{i,1} and cosmological parameters. This is a non-result that we already know.
2. **The DE field is unconstrained.** With f_a = M_Pl and m_2 ~ H_0, the w(z) deviation is ~ 0.01-0.1, below current sensitivity. The MCMC will return a prior-dominated posterior for θ_{i,2} and m_2.
3. **Not ECH-specific.** The calculation would be standard axiverse cosmology. It tests the ALP-photon coupling and ultralight quintessence, not ECH.
4. **Overparameterization.** 4 ALP parameters + 6 cosmological = 10 free parameters. With effectively one birefringence data point constraining θ_{i,1}, the rest of the ALP sector is unconstrained.
5. **Marginal publication value.** A 10-parameter model constrained by 1 new data point beyond standard cosmology does not strengthen the paper. It weakens it by suggesting overclaiming.

### Verdict: **DO NOT PROCEED.**

The right first calculation for this paper was Run 1 (spectator ALP birefringence-only), which is already done. A full cosmology joint fit would be Run 4 from the Phase 2 plan — useful for a figure but not scientifically necessary, and specifically for the spectator model (2 ALP params), not the two-field model (4 ALP params).

---

## What to Say in the Paper Instead

Rather than running a two-field MCMC, the paper should:

1. **State the rolling-vs-freezing tension explicitly** (Section on model comparison or Discussion)
2. **Note that ALP-as-DE is disfavored** by factor-2 tension on Ω_DE contour
3. **Adopt the spectator model** as the physically consistent choice
4. **Mention in Discussion:** "A two-field axiverse model (separate ALP for birefringence and ultralight quintessence for DE) resolves the rolling-vs-freezing tension but introduces additional parameters without ECH-specific predictions. We defer this to future work with improved w(z) constraints from DESI DR2."

This is honest, complete, and does not overcommit.

---

## If We Wanted to Revisit Branch U Later

Trigger conditions:
1. DESI DR2 reports w_0 ≠ -1 at > 3σ → ultralight quintessence becomes interesting
2. LiteBIRD confirms β > 0.2° at > 10σ → ALP is real, worth extending model
3. Anisotropic birefringence detected → tests ALP spatial structure
4. Both (1) and (2) simultaneously → two-field model becomes the obvious test

Until then, Branch U is **theory-complete and calculation-deferred.**
