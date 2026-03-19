# 02: Systematics Threat Matrix

## Ranked Threats

| Rank | Threat | Impact Type | SPHEREx | MegaMapper | Mitigable? |
|------|--------|------------|---------|------------|-----------|
| **1** | **Relativistic projection effects** | **Biases f_NL by ~20σ** (MegaMapper) | Moderate (3σ at low-z) | **CRITICAL (20σ)** | Yes but requires accurate modeling |
| **2** | **b_φ (PNG bias) uncertainty** | **Degrades σ by up to 14×** | HIGH | HIGH | Needs theoretical priors or simulations |
| **3** | **Ultra-large-scale mode access (k_min)** | **Degrades σ by 100-1000×** if lost | HIGH (for P(k) only) | HIGH (for P(k) only) | Partially mitigated by bispectrum |
| 4 | Foregrounds / imaging systematics | Biases + degrades at ℓ < 10 | Moderate (IR) | Lower (spectroscopic) | Survey-dependent |
| 5 | Multi-tracer implementation | Degrades σ by 2-4× if fails | Moderate | HIGH | Requires 2+ well-characterized populations |
| 6 | Photo-z quality | Degrades by 3-18% | Moderate | LOW (spectroscopic) | Mitigated by best-z sample dominance |
| 7 | Survey geometry / window function | Degrades by 10-30% | LOW (all-sky) | Moderate (partial sky) | Standard correction |
| 8 | Non-Gaussian covariance | < 1% effect | NEGLIGIBLE | NEGLIGIBLE | N/A |

## The Two NEW Threats (Not in Our Previous Assessment)

### Threat 1: Relativistic Projection Effects
**Previous assessment:** "Moderate, ~20% signal contamination, computable and subtractable"
**Updated assessment:** **CRITICAL for MegaMapper.** The bias is ~20σ, not ~20%. This means a 20× larger effect than the signal itself. It IS computable and subtractable in principle, but requires:
- Accurate magnification bias (s parameter)
- Accurate evolution bias (f_evo)
- Accurate luminosity function at z > 2
- These quantities are NOT well-constrained for Lyman-break galaxies

### Threat 2: b_φ Uncertainty
**Previous assessment:** Not identified as a separate threat.
**Updated assessment:** **HIGH.** Barreira (2022) shows that b_φ uncertainty can degrade constraints by up to 14×. The standard assumption b_φ = 2δ_c(b₁-1) (universality relation) may not hold to the precision needed. If b_φ is uncertain by 30%, σ(f_NL) degrades by ~30% (linear). If b_φ is uncertain by a factor of 2, σ degrades by ~2×.

## The Game-Changer: Bispectrum Channel

The SPHEREx bispectrum forecast (arXiv:2311.13082) shows σ(f_NL) = 0.7 from the bispectrum ALONE. This is important because:

1. The bispectrum measures the three-point function DIRECTLY, not via scale-dependent bias
2. It accesses information at higher k (not just the ultra-large scales)
3. It has DIFFERENT systematic dependencies from the power spectrum
4. It is less sensitive to b_φ uncertainty (the bispectrum has its own bias parameters)
5. It partially mitigates the k_min fragility

**If both power spectrum (SDB) and bispectrum channels are used, the combined constraint is more robust than either alone.** The SPHEREx σ = 0.5 (combined) is more credible than our power-spectrum-only Fisher scan suggested.

## Updated Fragility Assessment

| Assumption | Previous Assessment | Updated Assessment |
|-----------|-------------------|-------------------|
| k_min access | DOMINANT | Still important for P(k), but mitigated by bispectrum channel |
| Multi-tracer | Important | Secondary (15-20% improvement) |
| Photo-z | Important for SPHEREx | Moderate (3-18%, not fatal) |
| **Relativistic effects** | **Moderate** | **CRITICAL for MegaMapper (20σ bias)** |
| **b_φ uncertainty** | **Not identified** | **HIGH (up to 14× degradation)** |
| **Bispectrum channel** | **Not considered** | **MAJOR rescue path** |
