# 03: Robustness Scan Results

## Critical Finding

**The forecast is DOMINATED by k_min, not multi-tracer.** The constraining power for f_NL from scale-dependent bias is almost entirely concentrated in the 2-3 LARGEST-SCALE modes. Everything else is secondary.

## Baseline Results

| Survey | σ(f_NL) | Significance | Assessment |
|--------|---------|-------------|-----------|
| SPHEREx (k_min=5e-4) | 66.2 | 0.1σ | USELESS at this k_min |
| MegaMapper (k_min=2e-4) | 1.93 | 2.3σ | Marginal hint only |

These are MUCH weaker than published forecasts (which give σ ~ 0.5). The reason: published forecasts use k_min ~ 10⁻⁴ h/Mpc (corresponding to ultra-large-scale angular modes ℓ ~ 2-10), while my defaults are more conservative.

## The k_min Dependence (THE DOMINANT EFFECT)

| k_min (h/Mpc) | σ(f_NL) MegaMapper | Significance | Assessment |
|---------------|-------------------|-------------|-----------|
| **1×10⁻⁴** | **0.53** | **8.3σ** | **DECISIVE** — matches published claims |
| 2×10⁻⁴ | 1.93 | 2.3σ | Marginal — factor 4× worse |
| 5×10⁻⁴ | 36.3 | 0.1σ | USELESS |
| 1×10⁻³ | 500 | 0.0σ | Dead |

**Going from k_min = 10⁻⁴ to 2×10⁻⁴ — a factor of 2 in k_min — degrades significance by 4×.**

This is because the SDB signal grows as 1/k² and the number of modes grows as k³. The Fisher information per log-k bin scales as (1/k²)² × k³ = 1/k, which is STEEPLY increasing toward low k. Nearly ALL the information is in the lowest 2-3 k-bins.

## Why Published Forecasts Get σ ~ 0.5

Published forecasts (Schlegel et al. 2022, Ferraro et al. 2022) use:
1. **Angular power spectra C_ℓ**, not 3D P(k). The angular approach accesses modes down to ℓ ~ 2 (corresponding to k_eff ~ 3×10⁻⁴ to 5×10⁻⁴ h/Mpc for z ~ 3).
2. **Ultra-large-scale angular modes (ℓ = 2-10)** that are much larger than the 3D k_fundamental.
3. **Multi-redshift binning** that creates effective multi-tracer configurations.
4. **Cross-correlations** between redshift bins that provide additional information.

At k_min = 10⁻⁴, my Fisher code DOES reproduce σ ≈ 0.5 for MegaMapper. So the published claims are self-consistent — they just require accessing the ultra-large-scale modes.

## Multi-Tracer Effect (SECONDARY)

| Configuration | σ(f_NL) | Significance |
|--------------|---------|-------------|
| 1 tracer | 3.86 | 1.1σ |
| 2 tracers, contrast 1.5 | 2.44 | 1.8σ |
| 2 tracers, contrast 2.0 | 1.93 | 2.3σ |
| 2 tracers, contrast 3.0 | 1.22 | 3.6σ |
| 3 tracers, contrast 2.0 | 1.58 | 2.8σ |

Multi-tracer improves σ by a factor of 1.6-3.2× (at fixed k_min = 2×10⁻⁴). Important but NOT the dominant factor.

## Galaxy Bias Effect

Higher bias = better (the SDB signal scales as (b₁-1)·f_NL/k²):

| b₁ | σ(f_NL) | Significance |
|----|---------|-------------|
| 1.5 | 11.4 | 0.4σ |
| 3.0 | 1.93 | 2.3σ |
| 5.0 | 0.91 | 4.8σ |

High-z galaxies with b₁ ~ 3-5 provide much better f_NL constraints. This favors MegaMapper (z ~ 3, b₁ ~ 3) over SPHEREx (z ~ 1.5, b₁ ~ 1.8).

## SPHEREx: Much Weaker Than Claimed

| Scenario | σ(f_NL) | Significance |
|----------|---------|-------------|
| BEST (k_min=2e-4, σ_z=0.003) | 7.25 | 0.6σ |
| CENTRAL (k_min=5e-4, σ_z=0.03) | 66.2 | 0.1σ |
| With k_min=1e-4 | 3.30 | 1.3σ |

SPHEREx is much weaker than the published σ ~ 0.5 claim because:
1. My simple single-population SDB forecast doesn't capture multi-z-bin angular cross-correlations
2. The published SPHEREx forecast uses a much more sophisticated analysis
3. SPHEREx's real power comes from cross-correlating multiple galaxy populations across redshift bins — not from a single power spectrum measurement

**Honest assessment: SPHEREx's f_NL constraint from a single-population SDB analysis is weak (σ > 3). The published σ ~ 0.5 requires the full multi-tracer angular analysis, which our simple Fisher code doesn't capture.**

## Combined Scenarios

| Scenario | σ(f_NL) | Significance | Verdict |
|----------|---------|-------------|---------|
| MegaMapper BEST (k_min=1e-4, 3 tracers) | 0.34 | 13.0σ | DECISIVE |
| MegaMapper with k_min=1e-4, 2 tracers | 0.53 | 8.3σ | DECISIVE |
| MegaMapper CENTRAL (k_min=2e-4) | 1.93 | 2.3σ | HINT |
| MegaMapper CONSERVATIVE (k_min=1e-3) | 677 | 0.0σ | DEAD |

## THE REAL BOTTOM LINE

**The MegaMapper 8.3σ claim is REAL but conditional on ONE assumption: that the survey can cleanly measure ultra-large-scale modes at k ~ 10⁻⁴ h/Mpc (ℓ ~ 2-10 on the sky).** If those modes are accessible, σ(f_NL) ~ 0.5 and the detection is decisive. If those modes are lost to foreground contamination, survey geometry, or systematic effects, the constraint degrades catastrophically.

The multi-tracer enhancement, photo-z quality, and galaxy bias are all SECONDARY compared to the ultra-large-scale mode access.
