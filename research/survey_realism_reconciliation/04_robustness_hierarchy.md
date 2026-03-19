# 04: Robustness Hierarchy

## Head-to-Head Comparison

| Dimension | SPHEREx | MegaMapper |
|-----------|---------|------------|
| **Timeline** | ~2028 (funded, building) | ~2032+ (concept, not funded) |
| **Primary f_NL channel** | Bispectrum + power spectrum | Scale-dependent bias (power spectrum) |
| **Fiducial σ(f_NL)** | 0.5 (P+B) / 0.7 (B only) | 0.5 (P multi-tracer) |
| **Significance for -4.375** | 6.3-8.75σ | 8.75σ (ideal) / 3-7σ (realistic) |
| **k_min dependence** | LOW (bispectrum accesses shorter scales) | HIGH (SDB signal concentrated at lowest k) |
| **GR projection risk** | LOW (~3σ raw bias at z~1.5) | HIGH (~20σ raw bias at z~3) |
| **b_φ sensitivity** | MODERATE (enters differently in bispectrum) | HIGH (enters linearly in SDB) |
| **Photo-z risk** | MODERATE (3-18% degradation) | LOW (spectroscopic) |
| **Multi-tracer dependence** | MODERATE (uses multi-z bins) | HIGH (essential for σ=0.5) |
| **Foreground risk** | MODERATE (IR sky) | LOW (spectroscopic at z>2) |
| **Survey existence risk** | LOW (funded, launching soon) | HIGH (concept only) |

## Robustness Rankings

### Most Robust Near-Term Test: **SPHEREx**

Why:
1. FUNDED and BUILDING — will actually produce data (~2028)
2. Bispectrum channel is inherently less sensitive to ultra-large-scale systematics
3. Lower redshift means smaller GR projection contamination (3σ vs 20σ raw)
4. Dedicated multi-tracer bispectrum analysis already published (arXiv:2311.13082)
5. σ(f_NL) = 0.7 (bispectrum only) is achievable without heroic assumptions

Caveats:
- Photo-z quality won't be known until after launch
- The bispectrum estimator is more complex than SDB
- The 0.5 target requires combining bispectrum + power spectrum

### Most Powerful (But Fragile) Long-Term Test: **MegaMapper**

Why:
1. Spectroscopic redshifts give the best radial resolution
2. Multi-tracer with high-bias LBGs gives the best potential σ(f_NL)
3. If all systematics are handled, it's the most decisive single experiment

But:
1. Not funded — may never be built
2. 20σ raw GR contamination must be modeled and subtracted
3. b_φ for LBGs at z > 2 is poorly constrained
4. Multi-tracer implementation is untested
5. The 8.75σ headline requires EVERYTHING to work perfectly

### Verdict: **SPHEREx First, MegaMapper If Available**

The science strategy should be:

**Stage 1 (~2028):** SPHEREx provides the first test at 4-7σ via the galaxy bispectrum. If f_NL < -2, this is strong evidence for the bounce. If f_NL ≈ 0, the bounce is in serious trouble.

**Stage 2 (~2032+):** MegaMapper (if funded) provides the follow-up at 3-9σ via SDB + multi-tracer. If SPHEREx sees a hint, MegaMapper confirms. If SPHEREx is inconclusive, MegaMapper settles it.

**The robust story is STAGED, not single-experiment.**
