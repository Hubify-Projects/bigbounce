# 04: Forecast Downgrade / Survival Update

## Pre-Audit vs Post-Audit Significance

### SPHEREx

| Scenario | Pre-Audit σ(f_NL) | Pre-Audit Significance | Post-Audit Assessment |
|----------|-------------------|----------------------|---------------------|
| Optimistic | 0.5 | 8.75σ | **PLAUSIBLE** — requires P(k) + bispectrum combined |
| **Central** | **0.7** | **6.3σ** | **PLAUSIBLE** — bispectrum alone (arXiv:2311.13082) |
| Conservative | 1.5 | 2.9σ | Plausible with degraded photo-z |
| With b_φ uncertainty (~30%) | ~0.9 | ~4.9σ | Plausible if universality holds approximately |
| With b_φ uncertainty (~2×) | ~1.4 | ~3.1σ | Still suggestive |

**Post-audit SPHEREx verdict: σ(f_NL) = 0.5-1.0, significance 4-9σ.** The bispectrum channel (arXiv:2311.13082) makes SPHEREx MORE robust than our Fisher-only analysis suggested. The published σ = 0.5 (P+B combined) is **PLAUSIBLE** based on the dedicated forecast paper.

**Upgrade from previous assessment: SPHEREx significance upgraded from "1-4σ" to "4-9σ" once the bispectrum channel is included.**

### MegaMapper

| Scenario | Pre-Audit σ(f_NL) | Post-Audit Assessment |
|----------|-------------------|--------------------|
| Published (P(k) + multi-tracer, k_min=10⁻⁴) | 0.5 | **FRAGILE** — requires GR corrections modeled to ~0.1σ precision |
| After GR bias risk | — | If not corrected: measurement is BIASED by ~20σ → useless |
| After GR correction + residual | ~0.6-0.8 | **PLAUSIBLE** if GR effects modeled to few-% accuracy |
| After b_φ marginalisation | ~0.8-2.0 | **PLAUSIBLE_BUT_FRAGILE** |
| Conservative (all degradations) | ~1.5-3.0 | 1.5-3σ range |

**Post-audit MegaMapper verdict: The headline 8.75σ is FRAGILE because:**
1. GR projection effects create a 20σ bias that must be modeled and subtracted
2. b_φ uncertainty can degrade σ by up to 14×
3. The residual after correction depends on how accurately the luminosity function and magnification bias of LBGs are known at z > 2

**Downgrade: MegaMapper from "definitive" to "plausible-but-fragile" until GR modeling and b_φ priors are demonstrated.**

## Combined Assessment

| Survey | Pre-Audit | Post-Audit | Change |
|--------|-----------|-----------|--------|
| **SPHEREx** | **1-4σ** | **4-9σ** | **UPGRADED** (bispectrum channel) |
| **MegaMapper** | **2-9σ** | **1.5-9σ** | **WIDENED** (GR + b_φ risks) |

The SURPRISING result: **SPHEREx may be MORE reliable than MegaMapper** for this specific measurement, because:
1. SPHEREx's bispectrum channel avoids the ultra-large-scale mode dependence
2. SPHEREx operates at lower redshift (z ~ 1.5), where GR projection effects are smaller (3σ bias vs 20σ)
3. SPHEREx has a dedicated multi-tracer bispectrum analysis (arXiv:2311.13082)

MegaMapper's advantage (spectroscopic, multi-tracer) is real but is OFFSET by its disadvantage (high-z LBGs where GR effects are largest and b_φ is most uncertain).

## Overall Science Case Status

**PLAUSIBLE_BUT_FRAGILE**

The science case survives the systematics audit — the signal (f_NL = -4.375) is large enough to be detectable even with degradation. But:
- The "definitive 8.75σ" headline is too optimistic for MegaMapper (GR + b_φ risks)
- SPHEREx is more robust than previously thought (bispectrum channel)
- The realistic detection significance is 3-7σ (combining SPHEREx + MegaMapper with degradations)
- This is STILL strong evidence, just not the clean "discovery" we initially claimed
