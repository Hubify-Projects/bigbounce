# 03: MegaMapper Forecast Robustness Audit

## The Claimed Significance

f_NL^eff / σ(f_NL) = 4.16 / 0.5 = **8.3σ**

This assumes:
1. The true f_NL is -4.375 (matter-bounce prediction)
2. Template overlap cos(θ) ≈ 0.95 → f_NL^eff ≈ -4.16
3. MegaMapper achieves σ(f_NL^local) = 0.5

## Assumption Audit

### A1: True f_NL = -4.375

**Status: CONDITIONED ON THE BOUNCE ACTUALLY HAPPENING.**
This is the prediction, not a measurement. If the universe didn't bounce, f_NL ≈ 0.
**Risk to forecast: NONE** (this is what we're testing, not an assumption in the test)

### A2: Template Overlap cos(θ) ≈ 0.95

**Status: LIKELY ROBUST but with uncertainty.**
The matter-bounce shape is "loosely local" — dominated by the squeezed limit but with non-negligible equilateral and folded contributions.

- Our estimate: cos(θ) ≈ 0.95 ± 0.03
- Conservative lower bound: cos(θ) ≳ 0.75 (from file 05 of the execution phase)
- This means f_NL^eff ranges from -4.16 (central) to -3.28 (conservative)

**Impact on significance:**
- Central: 4.16/0.5 = 8.3σ
- Conservative: 3.28/0.5 = **6.6σ**
- Both still very strong detections.

### A3: σ(f_NL^local) = 0.5

**Status: THIS IS THE KEY ASSUMPTION. It comes from the MegaMapper design specification.**

MegaMapper is a proposed Stage-V spectroscopic survey. The σ(f_NL) = 0.5 forecast assumes:
- Multi-tracer technique with 2+ galaxy populations (cancels cosmic variance on large scales)
- Full sky coverage (~14,000 deg²)
- High-z galaxies at z = 2-5 (where non-Gaussianity signal is strongest)
- Scale-dependent bias: Δb(k) ∝ f_NL / k² on large scales

**Potential issues:**
1. **Multi-tracer efficiency:** If only ONE tracer is available (not two), cosmic variance limits σ(f_NL) to ~2-3. Significance drops to 1.4-2.1σ.
2. **Scale cuts:** If systematic uncertainties require cutting k < 0.001 h/Mpc, the large-scale modes carrying the f_NL signal are lost. Could degrade σ by factor 2-3.
3. **Photo-z vs spec-z:** MegaMapper is spectroscopic (good). But interlopers and redshift errors could reduce effective volume.
4. **Galaxy bias modeling:** The scale-dependent bias signal requires accurate modeling of the intrinsic bias b₁. Uncertainty in b₁ propagates to f_NL constraints.

**Realistic range for σ(f_NL):**
- Optimistic: 0.3 (perfect multi-tracer, full sky, no systematics)
- Central: 0.5 (design specification)
- Conservative: 1.0-2.0 (single tracer, limited k-range, or significant systematics)
- Pessimistic: 3.0 (if multi-tracer fails entirely)

### A4: Local template is the right observable

**Status: YES, with caveat.**
The matter-bounce shape projects 95% onto the local template. MegaMapper's f_NL^local constraint IS the right test. But the 5% non-local component could shift the best-fit by ~0.2, which is small compared to the signal.

## Significance Scenarios

| Scenario | σ(f_NL) | cos(θ) | f_NL^eff | Significance |
|----------|---------|--------|----------|-------------|
| Optimistic | 0.3 | 0.95 | 4.16 | **13.9σ** |
| Central | 0.5 | 0.95 | 4.16 | **8.3σ** |
| Conservative | 1.0 | 0.85 | 3.72 | **3.7σ** |
| Pessimistic (single tracer) | 2.5 | 0.75 | 3.28 | **1.3σ** |

## Intermediate Experiments

| Experiment | σ(f_NL) | Significance | Verdict |
|-----------|---------|-------------|---------|
| Planck (current) | 5.0 | 0.8σ | Not decisive |
| SPHEREx (~2028) | 1.0-1.5 | 2.8-4.2σ | **Interesting hint** |
| DESI + Euclid combined | ~2.0 | ~2.1σ | Marginal |
| CMB-S4 | ~2.5 | ~1.7σ | Not decisive |
| **MegaMapper (~2032+)** | **0.5** | **8.3σ** | **Definitive** |

## Honest Assessment

The **central forecast (8.3σ) is credible** but depends on MegaMapper achieving its design sensitivity. The key risk is multi-tracer performance — if MegaMapper can deploy two well-characterized galaxy populations at z > 2, σ(f_NL) = 0.5 is achievable based on Fisher-matrix forecasts in the literature.

The **conservative scenario (3.7σ at σ=1.0)** is still a strong signal, providing evidence-level detection even without perfect multi-tracer performance.

The **pessimistic scenario (1.3σ)** would fail to discriminate. This requires multi-tracer to fail completely, which seems unlikely for a dedicated Stage-V survey.

**Bottom line: the discrimination is robust under central assumptions and survives reasonable degradation. It fails only in the pessimistic single-tracer scenario.**
