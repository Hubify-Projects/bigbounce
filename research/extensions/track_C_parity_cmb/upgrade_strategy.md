# Phase 0: Track C Upgrade — Executive Strategy Note

**Date:** 2026-03-13

---

## 1. What is the current Track C result?

Track C is a **phenomenological consistency check** that performs zero statistical inference. It answers one question: "Given α/M ~ 10⁻²¹ GeV⁻¹, what photon-torsion coupling f_photon is needed to match observed cosmic birefringence β ~ 0.24°?"

**Answer:** f_photon ≈ 1.7 ± 0.4 (for C₀ = 1 rad). This is O(1), meaning no fine-tuning is required.

The current implementation consists of three scripts totaling ~500 lines of Python that perform:
- Inverse-variance weighted combination of two published β measurements
- Algebraic mapping β → f_photon
- Forward-modeled EB spectrum (no data comparison)

Runtime: < 3 seconds. No likelihood is evaluated. No sampler is run. No posterior is computed.

## 2. Why is it only a consistency check right now?

Three reasons:

**a) No formal likelihood.** The inverse-variance combination is mathematically equivalent to a Gaussian likelihood evaluation, but is not framed or implemented as one. There is no explicit prior, no evidence computation, no model comparison.

**b) The photon-torsion coupling gap.** The framework derives the parity-odd gravitational operator (α/M)ε^{abcd}K_{ab}R_{cd} but does NOT derive its coupling to photons. The parameter f_photon is entirely undetermined by the theory. This means the "posterior on f_photon" is really just a reparameterization of the measured β, not a constraint on a fundamental quantity.

**c) No shape test.** The EB spectrum predicted by uniform birefringence (C_ℓ^{EB} ∝ C_ℓ^{EE} − C_ℓ^{BB}) has not been compared against published bandpowers. This would be the only test with real discriminating power.

## 3. What would be required to upgrade it into a real inference result?

To make Track C a defensible statistical result, we need:

1. **A proper Gaussian summary likelihood** on β using published measurements — this is the honest ceiling given available data.

2. **Explicit priors** on all parameters (β, f_photon, C₀).

3. **Bayesian evidence** for β ≠ 0 (Savage-Dickey density ratio or Bayes factor).

4. **A 2D joint analysis** on (f_photon, C₀) that properly marginalizes the degeneracy.

5. **An EB shape comparison** against published Eskilt (2022) bandpowers to test the uniform-rotation hypothesis.

What we explicitly CANNOT do:
- Full map-level CMB analysis (requires Planck NPIPE maps + dedicated pipeline)
- Full harmonic-space EB/TB likelihood (not publicly released)
- Derive f_photon from first principles (open theoretical problem)

## 4. What is the strongest honest Track C result for the current paper?

**Gaussian summary-likelihood inference on β, with derived constraints on f_photon(C₀).**

This upgrades from "algebraic consistency check" to "summary-likelihood inference" — a genuine statistical result, honestly labeled as using published summary statistics rather than raw data.

Concretely:
- Gaussian likelihood: L(β) = Π_i N(β; β_i, σ_i) for Eskilt + ACT
- Prior: uniform on β ∈ [−1°, 1°] (uninformative)
- Posterior: β = 0.242° ± 0.061° (unchanged numerically, but now formally a posterior)
- Bayes factor: BF(β≠0 vs β=0) ≈ exp(−χ²/2) ratio → quantifiable preference for nonzero β
- 2D: (f_photon, C₀) posterior showing the degeneracy explicitly
- EB shape: χ² against Eskilt bandpowers for uniform rotation

**This is a small but honest upgrade.** It does not change the central result (f_photon ~ 1.7) but wraps it in proper statistical language with explicit priors, evidence, and a shape test.

**A heavier MCMC (emcee, cobaya) is NOT justified.** With 2 Gaussian data points and 1-2 parameters, the posterior is analytically tractable. Running a sampler would be performative — the exact same answer falls out of textbook formulas.
