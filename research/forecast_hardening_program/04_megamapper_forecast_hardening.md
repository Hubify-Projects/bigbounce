# 04: MegaMapper Forecast Hardening

## MegaMapper f_NL Capability — Hardened Assessment

### Survey Concept

MegaMapper is a proposed Stage-V spectroscopic galaxy survey:
- ~10 million Lyman-break galaxies at z = 2-5
- Full multi-tracer capability (multiple galaxy populations with different biases)
- Spectroscopic redshifts (high radial resolution)
- ~14,000 deg² sky coverage
- Primary science target: primordial non-Gaussianity via scale-dependent bias

### Published Forecasts

Schlegel et al. (2022) MegaMapper white paper: σ(f_NL) ~ 0.3-0.5 (multi-tracer, optimistic).
Sailer et al. (2021, arXiv:2106.09713): σ(f_NL) ~ 0.5-1.0 depending on tracer assumptions.
Ferraro et al. (2022, Snowmass): σ(f_NL) ~ 0.3 (aggressive multi-tracer).

The key: MegaMapper's advantage over SPHEREx is SPECTROSCOPIC redshifts (much better radial resolution) and MULTI-TRACER capability (cancels cosmic variance).

### Hardened Significance for f_NL = -4.375

| Scenario | σ(f_NL) | Significance | Assessment |
|----------|---------|-------------|-----------|
| Aggressive multi-tracer | 0.3 | 14.6σ | Likely too optimistic — assumes perfect bias characterization |
| **Design goal** | **0.5** | **8.75σ** | **Plausible if multi-tracer works well** |
| Moderate degradation | 0.8 | 5.5σ | Multi-tracer with modest systematics |
| Conservative (bias uncertainty) | 1.0 | 4.4σ | Still strong evidence |
| Single-tracer fallback | 2.0-3.0 | 1.5-2.2σ | Multi-tracer failure — not decisive |

### MegaMapper-Specific Fragilities

1. **Multi-tracer requirement:** The σ = 0.5 claim is fundamentally built on having 2+ galaxy populations with different biases. If only one well-characterized population is available, cosmic variance limits σ to ~2-3.

2. **Galaxy bias characterization at z > 2:** The bias properties of Lyman-break galaxies at z = 2-5 are not well-measured. Bias uncertainty propagates directly to f_NL uncertainty.

3. **Scale-dependent stochasticity:** At high redshift, the relationship between galaxies and dark matter may have scale-dependent scatter that mimics the f_NL 1/k² signal.

4. **Survey not yet funded:** MegaMapper is a concept, not an approved project. Timeline is uncertain (earliest science: ~2032-2035).

### Minimum Viable Detection

For a 5σ detection of f_NL = -4.375:
σ(f_NL) ≤ 4.375/5 = 0.875

This requires at least moderate multi-tracer performance. Single-tracer (σ ~ 2-3) cannot reach 5σ.

For a 3σ detection (evidence-level):
σ(f_NL) ≤ 4.375/3 = 1.46

This is achievable even without perfect multi-tracer — conservative single-tracer plus some cosmic variance cancellation could reach this.

### Does the ~8.75σ Central Claim Remain Robust?

**CONDITIONALLY YES.** The 8.75σ claim requires:
- Multi-tracer with 2+ populations: YES (design spec)
- σ(f_NL) = 0.5: achievable if bias modeling is adequate
- No catastrophic systematics: reasonable for a spectroscopic survey

The claim FAILS if:
- Multi-tracer capability degrades to single-tracer → 1.5-2.2σ
- Aggressive scale cuts are needed (k_min > 0.005 h/Mpc) → lose ~50% constraining power
- Bias modeling breaks down at z > 3 → σ degrades by factor 2+

### MegaMapper Decision Thresholds

| MegaMapper measures | Verdict | Confidence |
|-------------------|---------|-----------|
| f_NL = -4.4 ± 0.5 | **STRONGLY_FAVORS_BOUNCE** | 8.75σ from zero, perfect match |
| -6 < f_NL < -3 | **STRONGLY_FAVORS_BOUNCE** | Correct sign and magnitude, >5σ |
| -3 < f_NL < -1 | **SUPPORTS_BOUNCE** | Correct sign, smaller than predicted |
| -1 < f_NL < +1 | **KILLS_LIVE_LANE** | Excludes -4.375 at >6σ |
| f_NL > +2 | **KILLS** bounce, **supports** exotic inflation | Wrong sign entirely |

### Honest Bottom Line for MegaMapper

**MegaMapper at σ(f_NL) = 0.5 gives the definitive test: 8.75σ if bounce is real, >8σ exclusion if f_NL = 0.** This is the gold-standard experiment. The main risk is survey existence (not yet funded) and multi-tracer performance.

Even the conservative scenario (σ = 1.0) gives 4.4σ — strong evidence. MegaMapper is robust against moderate degradation.
