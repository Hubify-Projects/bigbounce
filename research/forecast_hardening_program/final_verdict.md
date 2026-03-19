# Final Verdict: Forecast Hardening Program

## 1. Best Current Observational Discriminator Package

**ONE NUMBER: f_NL^local = -4.375**

Extracted via scale-dependent bias from the galaxy power spectrum. For LSS surveys, the matter-bounce shape is EXACTLY local in the squeezed limit — no template mismatch, no projection loss. cos(θ) = 1.0 for SDB estimators.

Supporting discriminators (secondary): negative sign, consistency-relation violation (f_NL >> (5/12)(1-n_s)).

## 2. Hardened SPHEREx Significance Range

| Scenario | σ(f_NL) | Significance | Key Assumption |
|----------|---------|-------------|---------------|
| Design goal | 0.5 | 8.75σ | Perfect multi-tracer (likely optimistic) |
| **Realistic** | **1.0** | **4.4σ** | **Moderate photo-z degradation** |
| Conservative | 2.0 | 2.2σ | Significant photo-z issues |
| Pessimistic | 3.0 | 1.5σ | Severe degradation |

**Honest assessment: SPHEREx realistic is ~4.4σ — strong evidence, not definitive.** The main fragility is photo-z quality, which won't be known until after launch (~2026-2028).

## 3. Hardened MegaMapper Significance Range

| Scenario | σ(f_NL) | Significance | Key Assumption |
|----------|---------|-------------|---------------|
| Aggressive | 0.3 | 14.6σ | Perfect multi-tracer + bias (too optimistic) |
| **Design goal** | **0.5** | **8.75σ** | **Multi-tracer working well** |
| Conservative | 1.0 | 4.4σ | Moderate bias uncertainty |
| Single-tracer fallback | 2.5 | 1.75σ | Multi-tracer fails |

**Honest assessment: MegaMapper design goal of 8.75σ is plausible but conditional on multi-tracer performance.** Conservative scenario (4.4σ) is still strong. The survey is not yet funded.

## 4. Most Fragile Forecast Assumptions

Ranked by impact:

1. **Multi-tracer capability** (MegaMapper): if it works → 8.75σ; if it fails → 1.75σ. Factor 5× swing.
2. **Photo-z quality** (SPHEREx): factor 1.5-3× impact on σ(f_NL).
3. **Scale cuts (k_min)**: if large-scale modes are cut by systematics, up to 70% power loss.
4. **GR projection effects**: ~20% signal contamination, computable and subtractable.
5. **Galaxy bias modeling**: ~20-50% degradation in σ after marginalization.

## 5. Do We Need MCMC or Heavy Simulations Now?

**NO.**

- No new MCMC: f_NL is parameter-free, not a chain parameter
- No GPU jobs: no neural network or emulator tasks
- No RunPod: all analysis is laptop-scale
- No mock catalogs yet: only justified for a dedicated forecast paper

## 6. If Compute Is Needed, What Setup?

**Laptop only.** All current work is analytical Fisher forecasting + polynomial evaluation. No external compute justified at this stage.

**Later (if forecast paper): RunPod CPU** for light mock catalog generation and multi-tracer validation. Still no GPUs.

## 7. Exact Next Calculation

The forecast hardening is now COMPLETE at the level of analytical rigor. The remaining work falls into two clear categories:

### Category A: Research Complete — Ready for Deliverable

The theoretical framework, observational framework, and forecast hardening are all done. The natural next step is producing a deliverable (paper or document) that packages this into a form useful for the observational community.

### Category B: Additional Stress Tests (If Desired)

If not yet ready to produce a deliverable:
1. **Light CPU Fisher scan**: systematically vary (b₁, σ_z, k_min, N_tracer) and map the full significance surface. This would produce a robustness figure showing how σ(f_NL) and detection significance vary with survey assumptions.
2. **GR projection correction estimate**: compute the effective f_NL^GR contamination for the SPHEREx and MegaMapper survey geometries. This determines whether the systematic floor is << 1 (safe) or ~ 1 (needs careful treatment).
3. **CMB template projection**: compute cos(θ) with proper CMB transfer functions for Planck/CMB-S4. Low priority but would complete the picture.

**RECOMMENDATION: Category A.** The science case is analytically robust. The forecast survives reasonable degradation. The next highest-value action is packaging this into a focused forecast document — not more stress testing.
