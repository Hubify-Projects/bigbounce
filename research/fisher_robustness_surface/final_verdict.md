# Final Verdict: Fisher Robustness Surface

## 1. Robust SPHEREx Significance Range

| Scenario | σ(f_NL) | Significance |
|----------|---------|-------------|
| Published forecast (multi-z-bin angular) | 0.5-1.5 | 2.9-8.75σ |
| **Our simple SDB forecast (realistic k_min)** | **3-70** | **0.1-1.3σ** |
| Discrepancy factor | 5-50× | |

**Honest assessment: Our simple Fisher code gives SPHEREx σ ~ 3 at best (k_min = 10⁻⁴), which is MUCH weaker than the published σ ~ 0.5-1.5.** The discrepancy arises because SPHEREx's real constraint comes from multi-z-bin angular cross-correlations and multi-tracer techniques across redshift bins — NOT from a single-population 3D power spectrum. Our simple code doesn't capture this.

**Robust SPHEREx range:** σ(f_NL) ~ 1-5, significance ~ **1-4σ.** SPHEREx can provide a suggestive hint but is unlikely to be decisive on its own.

## 2. Robust MegaMapper Significance Range

| Scenario | σ(f_NL) | Significance | Key Condition |
|----------|---------|-------------|--------------|
| k_min = 10⁻⁴, multi-tracer | **0.5** | **8.3σ** | Ultra-large-scale modes accessible |
| k_min = 1.5×10⁻⁴, multi-tracer | 1.0 | 4.4σ | Modest large-scale degradation |
| k_min = 2×10⁻⁴, multi-tracer | 1.9 | 2.3σ | Significant large-scale loss |
| k_min = 5×10⁻⁴ (any config) | >30 | <0.1σ | Ultra-large scales lost → DEAD |

**The MegaMapper 8.3σ claim is REAL but requires k_min ≲ 10⁻⁴ h/Mpc.** This corresponds to angular modes ℓ ~ 2-10 on the sky. Whether these modes can be accessed cleanly is the SINGLE most important question for the forecast.

**Robust MegaMapper range:** σ(f_NL) ~ 0.5-2.0, significance ~ **2-9σ**, depending almost entirely on the effective k_min.

## 3. Most Fragile Assumptions (REVISED RANKING)

1. **Ultra-large-scale mode access (k_min)** — dominates EVERYTHING. Factor 100× in σ between k_min = 10⁻⁴ and 10⁻³.
2. **Multi-tracer performance** — factor 2-3× in σ. Important but secondary to k_min.
3. **Galaxy bias** — factor 2-5× depending on b₁. Higher bias at high-z helps significantly.
4. **Photo-z quality** — only matters for SPHEREx; negligible for spectroscopic MegaMapper.
5. **Number density** — factor 2× across realistic range. Moderate impact.

## 4. Is the Science Case Robust Enough Without Mocks?

**YES, conditionally.** The science case stands on Fisher grounds IF k_min ~ 10⁻⁴ is achievable. The question of whether k_min ~ 10⁻⁴ is achievable is an observational-methodology question that mocks COULD help answer — but it's really a foreground/systematics question, not a statistical one.

Mocks would be most useful for:
- Testing whether foreground subtraction preserves the ℓ ~ 2-10 modes
- Validating multi-tracer cosmic variance cancellation in realistic geometry
- Quantifying the GR projection effect residual after correction

These are medium-CPU tasks (RunPod-level), not laptop tasks. But they're also NOT essential for the science case — they would SHARPEN it, not make-or-break it.

## 5. Need for MCMC / RunPod / GPU

**MCMC: NO.** f_NL is parameter-free. No posterior to sample.

**RunPod CPU: NOT YET but potentially useful later** for mock catalog validation of ultra-large-scale mode access. This would be the single most valuable additional computation.

**GPU: NO.** No neural network or emulator tasks.

## 6. Exact Next Step

**The Fisher scan has identified the critical vulnerability: ultra-large-scale mode access.**

The two highest-value next actions are:

### Option A: Literature deep-dive on ultra-large-scale f_NL systematics
Read the recent literature (2022-2025) on whether k_min ~ 10⁻⁴ is achievable for local PNG. Key papers: Castorina & White (2020) on GR corrections, Barreira (2020) on bias + PNG Fisher, the MegaMapper white paper methodology sections. This would determine whether our 8.3σ headline is realistic WITHOUT needing mocks.

### Option B: Package the sensitivity surface as a deliverable
Write up the finding that "the MegaMapper test of matter-bounce non-Gaussianity is decisive IF ultra-large-scale modes are accessible, but collapses completely if they're not." This IS a novel, publishable finding — it quantifies exactly WHERE the observational discrimination lives or dies.

**RECOMMENDATION: Option A first** (literature deep-dive, no compute needed), **then Option B** (package the finding).
