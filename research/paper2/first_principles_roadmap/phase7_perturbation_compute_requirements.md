# Phase 7: Compute Requirements and Feasibility

**Date:** 2026-03-13
**Status:** COST ESTIMATE — based on Phase 4 algorithm design

---

## 1. Compute Tasks

| Task | Description | Dependencies |
|------|------------|--------------|
| T1 | Background ODE solve (single point) | None |
| T2 | z''/z + c_s computation | T1 |
| T3 | Mode evolution (all k, single parameter point) | T2 |
| T4 | Power spectrum extraction | T3 |
| T5 | Condensate parameter grid scan | T1–T4 repeated |
| T6 | Vacuum state comparison | T5 × 3 vacuum choices |
| T7 | Inflaton potential comparison | T5 × 3 potentials |
| T8 | Transfer function fitting | T5–T7 |
| T9 | Observable mapping (PBH, μ, GW) | T4 |
| T10 | MCMC chains with fast template | T8 |

---

## 2. Per-Task Cost Estimates

### T1: Background ODE (single parameter point)

```
Dimension: 5 ODEs
Integration range: ~200 e-folds in conformal time
Steps: ~10⁵ (adaptive RK8)
Time per step: ~0.5 μs
Total: ~0.05 seconds
Memory: ~10 MB (solution stored on grid)
```

### T2: z''/z Computation

```
Spectral differentiation on N = 10⁵ grid points
FFT-based: ~0.01 seconds
Memory: ~5 MB
```

### T3: Mode Evolution (all k, single parameter point)

```
N_k = 5,200 modes
Per mode:
  - Integration: ~10⁴ steps × 2 complex ODEs
  - Time: ~0.05 seconds (DOP853 with rtol=10⁻¹⁰)
Total (serial): 5200 × 0.05 = 260 seconds ≈ 4.3 minutes
Total (8-core): ~33 seconds
Total (GPU, 1024 threads): ~0.3 seconds
Memory per mode: ~1 MB (temporary)
Total memory: ~50 MB (mode-parallel on CPU) or ~5 GB (all modes on GPU)
```

### T4: Power Spectrum Extraction

```
Time: ~0.01 seconds (post-processing of mode solutions)
```

### T5: Condensate Parameter Grid

```
Grid: 20 × 20 × 20 × 5 × 5 = 200,000 points
  (Δρ: 20, α: 20, n_★: 20, ξ_s: 5, m: 5)
Time per point (8-core): 33 seconds
Total: 200,000 × 33s ≈ 1,830 CPU-hours
With 8-core machine: 229 hours ≈ 9.5 days
```

**OPTIMIZATION:** Most of the 200,000 points will be uninteresting (no PBH production). Use coarse initial grid (5⁵ = 3125 points), then refine around interesting regions.

Estimated optimized cost:
```
Coarse: 3,125 × 33s ≈ 29 hours (8-core)
Refined: 10,000 × 33s ≈ 92 hours (8-core)
Total: ~121 hours ≈ 5 days (single 8-core machine)
```

### T6: Vacuum State Comparison

```
3 × T5 (one for each vacuum choice)
Estimated: 15 days (single 8-core machine)
```

### T7: Inflaton Potential Comparison

```
3 × T5 (one for each potential)
Estimated: 15 days (single 8-core machine)
```

### T8: Transfer Function Fitting

```
Regression from ~30,000 (P_R, params) pairs
Standard fitting: ~1 hour
```

### T9: Observable Mapping

```
Per P_R(k): PBH integral (~0.1s), μ-distortion (~0.01s), GW (~0.1s)
Total for 30,000 spectra: ~1 hour
```

### T10: MCMC with Fast Template

```
Chain length: 10⁵ samples per chain
Template evaluation: ~1 ms per sample
Total per chain: ~100 seconds
4 chains × 3 vacuum × 3 potential = 36 chains
Total: ~1 hour
```

---

## 3. Total Compute Budget

### Minimal Program (proof of concept)

| Task | CPU-hours | Wall time (8-core) |
|------|-----------|-------------------|
| T5 (coarse grid, 1 vacuum, 1 potential) | 29 | 3.6 hours |
| T9 (observable mapping) | 0.1 | 6 minutes |
| T10 (MCMC) | 0.03 | 2 minutes |
| **Total** | **~30** | **~4 hours** |

### Standard Program (3 vacuum × 1 potential)

| Task | CPU-hours | Wall time (8-core) |
|------|-----------|-------------------|
| T5 (grid, 3 vacuum choices) | 360 | 45 hours |
| T8 (fitting) | 1 | 1 hour |
| T9 (observables) | 1 | 1 hour |
| T10 (MCMC, 12 chains) | 0.3 | 20 minutes |
| **Total** | **~362** | **~47 hours (2 days)** |

### Full Program (3 vacuum × 3 potential)

| Task | CPU-hours | Wall time (8-core) |
|------|-----------|-------------------|
| T5–T7 (full grid) | 1,100 | 137 hours |
| T8 (fitting) | 3 | 3 hours |
| T9 (observables) | 3 | 3 hours |
| T10 (MCMC, 36 chains) | 1 | 1 hour |
| **Total** | **~1,107** | **~144 hours (6 days)** |

### With GPU Acceleration

Replace T3 (mode evolution) with GPU kernel:
- Speedup factor: ~100× for mode evolution
- Background solve remains on CPU

| Program | GPU-hours | Wall time |
|---------|-----------|-----------|
| Minimal | 0.3 | 20 minutes |
| Standard | 4 | 4 hours |
| Full | 12 | 12 hours |

---

## 4. Infrastructure Assessment

### Current RunPod Infrastructure

```
Available: CPU pods (8-16 cores, 32-64 GB RAM)
GPU pods: A100 (80 GB), A40 (48 GB)
Cost: ~$0.40/hr (CPU), ~$1.50/hr (A100)
```

| Program | Platform | Cost | Duration |
|---------|---------|------|----------|
| Minimal | CPU (8-core) | ~$12 | 4 hours |
| Standard | CPU (8-core) | ~$19 | 47 hours |
| Standard | A100 GPU | ~$6 | 4 hours |
| Full | CPU (8-core) | ~$58 | 144 hours |
| Full | A100 GPU | ~$18 | 12 hours |

**VERDICT: Fully feasible on current RunPod infrastructure.**
Even the full program costs less than $60 and takes under a week on CPU.

### Local Machine (MacBook)

```
M-series: 8-10 cores, no NVIDIA GPU
Can run CPU programs at ~80% of RunPod speed
Minimal: ~5 hours
Standard: ~60 hours (2.5 days)
Full: ~180 hours (7.5 days)
```

**VERDICT: Feasible for minimal/standard. Full program better on RunPod.**

### Cluster-Scale (if needed)

Only needed if:
- Grid is much finer than estimated (>10⁶ points)
- Full solver is used inside MCMC loop (instead of fast template)
- Multiple perturbation prescriptions tested (adds another ×3-5)

In that case:
```
Full solver MCMC: 10⁵ samples × 4 min/sample = 6,700 CPU-hours
With 100-core cluster: 67 hours
With GPU (1000 modes parallel): ~670 hours on A100
```

**VERDICT: Not needed for the research program as designed. The fast-template approach avoids the need for cluster-scale compute.**

---

## 5. Software Development Time

| Component | Estimated dev time | Difficulty |
|-----------|-------------------|-----------|
| Background ODE solver | 1 week | Low (standard scipy/Julia) |
| z''/z spectral differentiator | 2 days | Medium (need high accuracy) |
| Mode evolution solver (CPU) | 1 week | Medium (validation against LQC) |
| Mode evolution solver (GPU) | 2 weeks | High (JAX/CUDA implementation) |
| Power spectrum extractor | 2 days | Low |
| PBH + μ-distortion mapping | 3 days | Low (exists from Chain 1A) |
| Transfer function fitter | 3 days | Low |
| MCMC integration (Cobaya) | 1 week | Medium |
| Validation against published LQC | 2 weeks | High (requires careful comparison) |
| **Total** | **~8 weeks** | |

---

## 6. Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Numerical instability at bounce | Medium | High | Use regularized z''/z; Radau solver |
| z''/z computation inaccurate | Medium | High | Spectral differentiation; convergence tests |
| GPU implementation takes longer | High | Low | CPU fallback is fast enough |
| Condensate model has no PBH production | Medium | Medium | Report null result honestly |
| Vacuum choice dominates uncertainty | High | Medium | Report all three; identify discriminators |
| Published LQC codes unavailable | Low | Medium | Implement from scratch using published equations |

---

## 7. Recommended Execution Plan

### Week 1-2: Background Solver
- Implement modified Friedmann + Klein-Gordon + condensate
- Validate against known LQC solutions (V_s = 0)
- Test with three inflaton potentials

### Week 3-4: Perturbation Solver
- Implement Mukhanov-Sasaki mode integration
- Three vacuum state initializations
- Validate z''/z computation against published LQC results
- Run minimal program (1 vacuum, 1 potential)

### Week 5-6: Standard Program
- Grid scan over condensate parameters (3 vacuum choices)
- Extract P_R(k) library
- Fit fast templates

### Week 7-8: Observable Mapping + MCMC
- PBH abundance, μ-distortion, GW mapping
- MCMC chains with fast template
- Paper 2 figures and tables

### Buffer: Week 9-10
- GPU acceleration if needed
- Additional perturbation prescriptions
- Paper writing
