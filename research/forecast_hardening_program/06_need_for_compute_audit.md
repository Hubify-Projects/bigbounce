# 06: Need-for-Compute Audit

## Current State: Everything Runs on a Laptop

All completed analysis (shape function evaluation, squeezed-limit verification, forecast significance estimates, decision thresholds) was done locally. No MCMC, no GPUs, no RunPod.

## Compute Level Assessment

### Level 0: Laptop Only (NO external compute)
**Scientific questions answered:**
- Shape function evaluation at any (k₁,k₂,k₃): YES (polynomial, milliseconds)
- Fisher forecast for SPHEREx/MegaMapper: YES (analytical, seconds)
- SDB estimator significance: YES (analytical)
- Decision threshold table: YES (arithmetic)
- Template projection (LSS/squeezed limit): YES (trivially cos(θ) = 1)

**Verdict: SUFFICIENT for the current science case.** All claims in this framework are laptop-computable.

### Level 1: Light CPU Scans (local machine, hours)
**Scientific questions answered:**
- Robustness scan over nuisance parameters (b₁, σ_z, k_min): would quantify sensitivity
- Fisher matrix with marginalization over bias/photo-z: would give degraded σ(f_NL) estimates
- Monte Carlo scan over survey assumptions: would map the full significance distribution

**Verdict: USEFUL but NOT ESSENTIAL now.** These would sharpen the forecast but don't change the qualitative picture. Worth doing if preparing a focused forecast paper.

### Level 2: Medium CPU (RunPod, 10-100 CPU-hours)
**Scientific questions answered:**
- Mock galaxy catalog generation: would validate the Fisher forecast with realistic survey geometry
- Multi-tracer simulation: would test whether cosmic variance cancellation actually works
- Full likelihood analysis on mocks: would test the estimator pipeline

**Verdict: PREMATURE. Only justified if committing to a detailed forecast publication with mock-based validation.**

### Level 3: Heavy CPU (RunPod, 100-1000 CPU-hours)
**Scientific questions answered:**
- Large mock suites for covariance estimation
- Full Bayesian inference on mock surveys
- Simulation-based prior calibration

**Verdict: NOT NEEDED. Way beyond current requirements.**

### Level 4: GPU (any scale)
**Scientific questions answered:**
- None identified. No neural network, emulator, or GPU-accelerated likelihood work is needed.

**Verdict: NOT NEEDED.**

## The Bottom Line

| Compute Level | Needed Now? | Needed for Paper? |
|--------------|-------------|------------------|
| Laptop only | **YES (sufficient)** | YES (sufficient for theory paper) |
| Light CPU scans | No (but useful) | YES (for forecast paper) |
| Medium RunPod CPU | No | Maybe (for mock-validated forecast) |
| Heavy RunPod CPU | No | No |
| GPU | No | No |
| New MCMC (Cobaya) | **NO** (f_NL is parameter-free) | NO |

## Recommendation

**Stay on the laptop.** The science case stands on analytical grounds. Escalate to RunPod CPU only if writing a mock-validated forecast paper targeted at SPHEREx or MegaMapper science teams.
