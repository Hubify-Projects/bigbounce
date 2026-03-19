# 07: Compute Strategy Recommendation

## Do We Need New MCMC?

**NO.** The existing 236k MCMC posterior samples (from the Cobaya runs) already constrain the ΛCDM parameters. The matter-bounce prediction (f_NL = -4.375) is parameter-free — it doesn't enter the MCMC at all. Running more chains would constrain ΔN_eff or other derived parameters, which is irrelevant to the f_NL discrimination question.

## Do We Need GPU Jobs?

**NO.** There are no neural network, emulator, or large N-body simulation tasks needed at this stage. GPU compute is not justified.

## Do We Need Heavy CPU Jobs (RunPod)?

**NOT YET.** The current analysis is all Fisher-matrix / analytical forecasting, which runs in seconds on a laptop. RunPod CPU would be justified only for:
- Large Monte Carlo forecast suites (varying survey parameters, bias models, etc.)
- Mock catalog generation for multi-tracer validation
- Full likelihood analysis with realistic survey window functions

None of these are needed RIGHT NOW. They would become relevant if we decide to write a detailed forecast paper.

## What Can Be Done Locally (Laptop/Desktop)

| Task | Compute | Status |
|------|---------|--------|
| Shape function evaluation | Trivial (polynomial) | **DONE** |
| Squeezed-limit convergence | Trivial | **DONE** |
| Fisher forecast for SPHEREx/MegaMapper | Light CPU (seconds) | Doable now |
| Scale-dependent bias forecast | Light CPU | Doable now |
| Template projection (CMB-proper) | Medium CPU (needs bispectrum transfer functions) | Deferred |
| Robustness scans over nuisance parameters | Medium CPU | Doable now |

## What Should Be Done on RunPod (If Later Justified)

| Task | Compute | When |
|------|---------|------|
| Mock galaxy catalog generation | Medium CPU (hours) | If writing a forecast paper |
| Multi-tracer validation with mocks | Medium CPU (hours) | If writing a forecast paper |
| Full Bayesian f_NL inference pipeline test | Medium CPU (hours) | If writing a forecast paper |

## What Is Premature

| Task | Why Premature |
|------|--------------|
| New Cobaya MCMC | f_NL is parameter-free; MCMC adds nothing |
| N-body simulations | No simulation-based observable yet identified |
| GPU emulators | No high-dimensional parameter space to emulate |
| Simulation-based priors | Only needed for detailed systematic modeling |

## Recommendation

**Stay on the laptop for now.** All remaining analysis is analytical or light-CPU. Escalate to RunPod ONLY if we commit to a detailed forecast paper with mock-based validation.
