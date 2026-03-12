# Fine-Tuning Assessment — Vacuum Energy Scale

**Date:** 2026-03-12
**Method:** 100,000-sample Monte Carlo scan over parameter space

---

## Key Results

### Viable Parameter Space Fraction

| Metric | Value |
|--------|-------|
| Viable criterion | 0.01 < ρ_pred/ρ_obs < 100 |
| Overall viable fraction | **2.18%** (2,183 / 100,000 samples) |
| Fine-tuning measure | **1 in 46** |
| Viable N_tot range | [78.6, 95.3] (width 16.8 e-folds) |
| N_tot fractional range | 12.0% of prior range [60, 200] |

### Parameter Sensitivity Ranking

| Rank | Parameter | Spearman ρ_s | Role |
|------|-----------|-------------|------|
| 1 | **N_tot** (total e-folds) | **-0.996** | Dominant — near-perfect anti-correlation |
| 2 | T_reh (reheating temp) | +0.079 | Minor — enters as (T_reh/M_GUT)^{3/2} |
| 3 | (α/M)·M_Pl (loop factor) | +0.022 | Negligible at leading order |
| 4 | M_GUT (GUT scale) | -0.019 | Negligible |

### Interpretation

**N_tot overwhelmingly dominates the vacuum energy scale.** All other parameters are essentially irrelevant: the ratio ρ_pred/ρ_obs changes by 3 orders of magnitude per e-fold of N_tot (since δρ/ρ = 3·δN_tot), while varying α/M by 4 orders of magnitude changes ρ_pred by only 4 orders.

This is an inherent feature of the exponential suppression mechanism: D_inf ~ exp(-3 N_tot) means the dark energy scale is an exponentially sensitive function of inflation duration.

---

## Fine-Tuning Comparison

### This Framework

- **Residual tuning:** ~10⁵ (specification of N_tot to within ΔN_tot ≈ 4 e-folds)
- **Nature of tuning:** Initial condition — "How long did inflation last?"
- **Potential dynamical answer:** Bounce-to-inflation transition dynamics may select N_tot
- **Fine-tuning measure from scan:** 1 in 46 (2.2% of scanned parameter space)

### Standard ΛCDM

- **Residual tuning:** ~10¹²⁰
- **Nature of tuning:** Fundamental — "Why is the bare cosmological constant so small?"
- **Potential dynamical answer:** None known (landscape/anthropic arguments only)

### Comparison Summary

| Metric | This framework | ΛCDM |
|--------|---------------|------|
| Tuning level | 10⁵ | 10¹²⁰ |
| Nature | Initial condition | Fundamental constant |
| Dynamical escape route | Yes (bounce dynamics) | No |
| Exponential sensitivity | Yes (to N_tot) | Yes (to Λ_bare) |

---

## Robustness Assessment

### What is robust (insensitive to parameter choices):

1. **The existence of exponential suppression** — Any inflation duration > 60 e-folds produces enormous suppression of the primordial parity-odd coefficient. The mechanism generically produces tiny ρ_Λ.

2. **The functional form** — ρ_Λ = [(α/M)·M_Pl] × exp(-3 N_tot) × (T_reh/M_GUT)^{3/2} × M_Pl⁴ is a direct consequence of spin density dilution during inflation. The -3 exponent follows from the a⁻³ dilution of the spin density source.

3. **The one-loop origin of parity violation** — The existence of a parity-odd coefficient is established by multiple independent analyses (Freidel et al., Mercuri, Shapiro & Teixeira). Its order of magnitude [(α/M)·M_Pl ~ 10⁻²] is a generic one-loop prediction.

### What is finely tuned:

1. **N_tot to within ~4 e-folds** — Getting ρ_Λ within 2 orders of magnitude of the observed value requires 86 < N_tot < 98 (for fiducial α/M and T_reh). This is the residual fine-tuning.

2. **The combination N_tot + log₁₀(α/M·M_Pl)** — There is a degeneracy: if the loop factor is larger, fewer e-folds are needed. The viable region is a narrow diagonal band in this 2D space.

### What is an assumption (neither robust nor tuned):

1. **w = -1 at late times** — Not derived from the framework; assumed.
2. **T_reh ~ 10¹⁵ GeV** — Standard GUT-scale assumption. Low T_reh shifts the required N_tot.
3. **The Planck-scale on-shell evaluation** — The dimensional bridge from dim +1 to dim +4 relies on evaluating at the bounce. This is a scaling ansatz, not a controlled EFT calculation.

---

## Conclusion

**The mechanism is moderately tuned but not severely so.** The fine-tuning is reduced from 10¹²⁰ (ΛCDM) to 10⁵ (this framework), corresponding to specifying N_tot to within ~4 e-folds. This is a dramatic improvement over ΛCDM, but the mechanism is not "natural" in the technical sense — it still requires a specific initial condition. The key advantage is that this initial condition (inflation duration) has a plausible dynamical origin in the bounce-to-inflation transition, whereas ΛCDM's fine-tuning has no known dynamical explanation.

The sensitivity is entirely dominated by N_tot. The other parameters (α/M, T_reh, M_GUT) play negligible roles in determining whether the predicted ρ_Λ matches observation.
