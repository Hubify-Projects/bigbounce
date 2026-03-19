# 00: Scope Lock

## What Is Already Established
- f_NL = -35/8 prediction (verified)
- SPHEREx ~6σ, MegaMapper 3-7σ (hardened forecasts)
- Anti-mimicry argument (kinematic vs parametric)
- Point Bayes factors: bounce favored 17-24:1 vs best exotic inflation

## What This Computation Adds
A DISTRIBUTION of Bayes factors sampled over realistic uncertainty in:
- survey performance (σ(f_NL) varies due to photo-z, multi-tracer, systematics)
- nuisance parameters (b_φ uncertainty, GR residual)
- mock measured values (what nature actually gives us)

Instead of one number, we get: "Under X% of plausible survey realizations, the bounce is favored at Y:1 or better."

## Why This Is NOT Cosmology MCMC
- We are NOT sampling cosmological parameters (H₀, Ω_m, etc.)
- We are NOT running CAMB/Cobaya/CLASS
- We ARE sampling survey-assumption uncertainty and mock outcomes
- The parameter space is ~5-dimensional, not 30+
- Each evaluation takes microseconds, not minutes
- The full ensemble runs in seconds on a laptop

## Target Outputs
1. Distribution of Bayes factors over mock survey realizations
2. Probability that bounce is favored at >10:1 under realistic assumptions
3. Which nuisance assumptions dominate the support variation
4. Combined SPHEREx + MegaMapper inference
