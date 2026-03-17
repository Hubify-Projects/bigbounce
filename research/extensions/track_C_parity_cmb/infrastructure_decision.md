# Phase 6: Infrastructure Decision

**Date:** 2026-03-13

---

## Question: Does Track C v2 require RunPod or any GPU infrastructure?

### Answer: **NO.**

---

## Justification

| Criterion | Assessment |
|-----------|-----------|
| Runtime | < 3 seconds on any laptop |
| Dependencies | numpy, scipy, matplotlib (standard) |
| Memory | < 50 MB |
| Computation | Analytic Gaussian posterior (no sampling) |
| Data volume | 2 scalar measurements |
| Output | 4 PDF/PNG figures + 2 tables |

The entire Track C v2 analysis is analytically tractable. The posterior is a product of two Gaussians, which is itself Gaussian with known mean and variance. No MCMC, no numerical integration, no parallelism needed.

### What would require infrastructure:

1. **Full map-level EB likelihood** (Planck NPIPE maps + ACT DR6 maps) — would require ~100 GB data download and HEALPix/NaMaster pipelines. NOT justified for this paper (data partially non-public).
2. **Joint fit with Paper 1 MCMC parameters** — would require cobaya + CosmoMC chains on RunPod. NOT justified (beta is measured independently of cosmological parameters; no non-trivial correlation to explore).
3. **Monte Carlo validation** (e.g., simulating 10^5 mock datasets to verify coverage) — useful but ~1 minute on a laptop, no GPU needed.

### Interaction with Paper 1 chains:

Track C v2 has **zero interaction** with the planck_only chains currently running on RunPod. Different parameters, different data, different likelihood. No risk of interference.

---

## Decision: Run locally. No infrastructure needed.
