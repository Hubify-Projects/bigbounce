# Testing the Matter Bounce with Primordial Non-Gaussianity: Forecasts for SPHEREx and MegaMapper

**Houston Golden**

---

## Abstract

A matter-dominated contracting phase preceding a nonsingular bounce produces a specific, parameter-free prediction for local-type primordial non-Gaussianity: f_NL^local = -35/8 = -4.375 (Cai et al. 2009). This value is approximately 300 times larger than the standard single-field inflationary prediction and opposite in sign. We present forecasts for testing this prediction with the SPHEREx and MegaMapper galaxy surveys via the scale-dependent bias effect and the galaxy bispectrum. In the squeezed limit relevant for large-scale structure estimators, the matter-bounce bispectrum shape projects exactly onto the local template with no projection penalty. The SPHEREx multi-tracer galaxy bispectrum achieves σ(f_NL) ≈ 0.7, giving approximately 4-6σ sensitivity to the bounce signal after accounting for photometric redshift degradation and PNG bias uncertainty. MegaMapper's spectroscopic multi-tracer capability could reach σ(f_NL) ≈ 0.5 under ideal conditions (3-7σ realistic, conditional on ultra-large-scale systematics modeling). We perform a Bayesian model comparison using 800,000 Monte Carlo realizations across analytic, mock-based, and GR-aware frameworks, finding that a detection near f_NL = -4.375 would favor the bounce over standard single-field inflation at Bayes factor > 300 and over tuned multifield competitors at Bayes factor > 7, with these conclusions robust to conservative treatment of relativistic projection effects and PNG bias uncertainty. A null result from SPHEREx would disfavor the quasi-dust matter bounce at > 4σ significance. We identify GR projection contamination as the dominant systematic requiring careful modeling, but show that once marginalized, the model comparison remains strongly favorable for the bounce.

---

## 1. Introduction

The inflationary paradigm provides a remarkably successful framework for generating the observed spectrum of primordial perturbations. Standard single-field slow-roll inflation predicts a nearly scale-invariant, nearly Gaussian spectrum with a small, positive local-type non-Gaussianity f_NL ≈ (5/12)(1-n_s) ≈ 0.015, set by the Maldacena consistency relation [Maldacena 2003].

Bouncing cosmology offers an alternative origin for primordial perturbations: modes exit the Hubble radius during a contracting phase and re-enter after a nonsingular bounce. In particular, a matter-dominated contraction (w ≈ 0) produces a scale-invariant scalar spectrum through the growth of the curvature perturbation ζ on superhorizon scales [Wands 1999, Finelli & Brandenberger 2002].

A distinctive prediction of the matter bounce is a large, negative, parameter-free local-type non-Gaussianity f_NL = -35/8 = -4.375 [Cai et al. 2009]. This value is determined entirely by the equation of state during contraction (ε = 3/2 for matter) and the structure of the Maldacena cubic action, with no free parameters.

This prediction is mechanism-independent: it holds regardless of whether the bounce is realized by loop quantum cosmology [Wilson-Ewing 2013], Einstein-Cartan-Holst gravity, or other nonsingular completions. In minimal Einstein-Cartan-Holst gravity, scalar perturbations reduce exactly to the standard Mukhanov-Sasaki sector because the Holst term becomes a topological invariant (the Pontryagin density) when torsion vanishes for canonical scalar field matter. This perturbation-transparency, observed across multiple bounce mechanisms, motivates treating the f_NL prediction as a generic matter-bounce observable rather than a framework-specific result.

The next generation of galaxy surveys — SPHEREx [Doré et al. 2014] and MegaMapper [Schlegel et al. 2022] — will constrain local-type f_NL at unprecedented precision through the scale-dependent bias effect [Dalal et al. 2008] and the galaxy bispectrum [Heinrich et al. 2023]. In this paper, we present hardened forecasts for testing f_NL = -35/8 with these surveys, including a systematic assessment of the dominant observational fragilities and a Bayesian model comparison quantifying the discrimination power against inflationary alternatives.

---

## 2. The Matter-Bounce Bispectrum Benchmark

### 2.1 The Prediction

In a matter-dominated contracting universe with standard GR perturbation theory and Bunch-Davies vacuum, the curvature perturbation ζ grows as |η|^{-3} on superhorizon scales during contraction. The cubic interactions, governed by the Maldacena action [Maldacena 2003] specialized to ε = 3/2, produce a bispectrum with shape function [Cai et al. 2009]:

A_T(k_1, k_2, k_3) = (3/(256 k_1^2 k_2^2 k_3^2)) × P(k_1, k_2, k_3)

where P is a degree-9 homogeneous polynomial in the wavenumbers, and the nonlinearity parameter in the squeezed limit is:

|B|_NL = (10/3) A_T / Σk_i^3 → -35/8  as  k_1/k → 0

We have independently verified this result by evaluating the shape function at three distinct momentum configurations:
- Squeezed (k_1 → 0, k_2 = k_3): |B|_NL = -35/8 = -4.375
- Equilateral (k_1 = k_2 = k_3): |B|_NL = -255/64 = -3.984
- Folded (k_1 = 2k_2 = 2k_3): |B|_NL = -9/4 = -2.250

All three values match the published results exactly.

### 2.2 Mechanism Independence

The prediction depends only on: (a) matter-dominated contraction (w ≈ 0, ε ≈ 3/2), (b) standard GR perturbation theory during contraction, and (c) Bunch-Davies vacuum initial conditions. It does not depend on the specific bounce mechanism. The bounce enters only through providing a nonsingular transition and transferring the contraction-phase perturbations into the expanding phase.

### 2.3 The Viable Model

The Wilson-Ewing ΛCDM quasi-dust model [Wilson-Ewing 2013] provides a complete observational package: n_s = 0.964 (from w = -0.003, one free parameter), r ≈ 10^{-4} (from LQC quantum-geometry tensor suppression), and f_NL = -35/8 (parameter-free). This model has no current observational tensions.

---

## 3. Observable Mapping to LSS

### 3.1 Scale-Dependent Bias

Primordial local non-Gaussianity induces a scale-dependent correction to galaxy bias [Dalal et al. 2008]:

Δb(k) = 2(b_1 - 1) f_NL δ_c / [D(z) T(k) α(k)]

where α(k) encodes the Poisson equation normalization. The signal grows as 1/k^2 on the largest scales, making it detectable in the galaxy power spectrum.

### 3.2 Template Projection

For LSS surveys using the scale-dependent bias estimator, the relevant bispectrum configurations are in the squeezed limit (k_long << k_short). In this limit, the matter-bounce bispectrum converges to exactly -35/8 — the local template value. There is no template-projection penalty: the matter-bounce shape IS the local template in the squeezed limit.

### 3.3 Galaxy Bispectrum

The galaxy bispectrum provides an independent measurement channel that accesses information at shorter wavelengths, reducing the dependence on ultra-large-scale modes [Heinrich et al. 2023]. This makes bispectrum-based constraints more robust to large-scale systematics than power-spectrum-based scale-dependent bias alone.

---

## 4. SPHEREx Forecast

### 4.1 Survey Parameters

SPHEREx is an all-sky spectrophotometric survey (0.75-5 μm) with spectral resolution R ≈ 40-130 and approximately 450 million galaxies. A dedicated multi-tracer bispectrum analysis [Heinrich et al. 2023] forecasts σ(f_NL) = 0.7 from the bispectrum alone, with σ(f_NL) = 0.5 when combined with the power spectrum.

### 4.2 Significance for f_NL = -4.375

| Scenario | σ(f_NL) | Significance |
|----------|---------|-------------|
| Bispectrum only (fiducial) | 0.7 | 6.3σ |
| Combined P+B | 0.5 | 8.75σ |
| With GR marginalization (σ_GR = 0.5) | ~0.9 | ~4.9σ |
| Conservative (σ_GR = 1.0) | ~1.3 | ~3.4σ |

### 4.3 Assessment

SPHEREx provides the most robust near-term test because: (a) the bispectrum channel avoids ultra-large-scale mode dependence, (b) lower redshift (z ≈ 1.5) reduces GR projection contamination, (c) multi-tracer across redshift bins provides effective cosmic variance cancellation despite photometric redshifts.

---

## 5. MegaMapper Forecast

### 5.1 Survey Parameters

MegaMapper is a proposed Stage-V spectroscopic survey targeting ~10 million Lyman-break galaxies at z = 2-5 with multi-tracer capability [Schlegel et al. 2022]. Published forecasts give σ(f_NL) ≈ 0.5 under ideal conditions.

### 5.2 Significance Range

| Scenario | σ(f_NL) | Significance |
|----------|---------|-------------|
| Design goal (multi-tracer) | 0.5 | 8.75σ |
| Moderate degradation | 0.8 | 5.5σ |
| Conservative | 1.0-1.5 | 2.9-4.4σ |
| Single-tracer fallback | 2.0-3.0 | 1.5-2.2σ |

### 5.3 Key Fragilities

MegaMapper's forecast is more sensitive to: (a) relativistic projection effects, which create ~5-20× the signal magnitude in GR-induced bias at z > 2 [arXiv:2511.09466]; (b) PNG bias parameter b_φ uncertainty, which can degrade constraints by up to 14× if uncalibrated [Barreira 2022]; (c) multi-tracer implementation quality. These effects are modelable but make MegaMapper's forecast more conditional than SPHEREx's.

---

## 6. Inflation Mimicry and Bayesian Comparison

### 6.1 Can Inflation Reproduce f_NL = -4.375?

Standard single-field slow-roll inflation predicts f_NL = (5/12)(1-n_s) ≈ +0.015 — wrong by a factor of 300 and opposite in sign. Non-canonical single-field models (DBI, etc.) produce equilateral-shape f_NL, not local.

Non-attractor single-field inflation naturally gives f_NL = +5/2 (wrong sign). Reaching -4.375 requires engineering the attractor-to-slow-roll transition.

Multifield / curvaton models: the standard quadratic curvaton gives minimum f_NL ≈ -1.25 (insufficient). Self-interacting curvatons or curved field-space models can reach -4.375 but require ≥2 tuned parameters.

### 6.2 The Kinematic vs Parametric Asymmetry

The bounce predicts f_NL = -35/8 kinematically, with zero free parameters in the cubic sector. Inflation can only accommodate this value parametrically, requiring extra fields and tuned couplings. This asymmetry drives a natural Bayesian preference for the bounce.

### 6.3 Quantitative Bayesian Comparison

We performed model comparison using 800,000 Monte Carlo realizations across three frameworks (analytic, mock-based, and GR-aware).

For a detection at f_NL = -4.375 by SPHEREx (σ = 0.7):

| Comparison | Median Bayes Factor | P(BF > 3) |
|-----------|-------------------|-----------|
| Bounce vs standard single-field | > 10^5 | 97% |
| Bounce vs tuned multifield [-15,+15] | 10-23 | 87-96% |

These results are robust to prior sensitivity: the Bayes factor vs tuned multifield ranges from 7 (narrow prior) to 57 (broad prior) under all reasonable prior choices.

---

## 7. Systematics and GR-Aware Robustness

### 7.1 Dominant Fragilities

Our Fisher robustness scan identified three dominant threats:
1. Ultra-large-scale mode access (k_min): the SDB signal is concentrated in the lowest k-modes
2. Relativistic projection effects: create a fake f_NL signal at large scales
3. PNG bias (b_φ) uncertainty: degrades the SDB calibration

### 7.2 GR-Aware Analysis

We performed GR-aware Bayesian comparison across five scenarios:

| GR Treatment | Median BF vs SSFSR | P(BF > 3) vs SSFSR | BF vs Tuned |
|-------------|-------------------|-------------------|----|
| Ideal (no GR) | 3.3 × 10^6 | 98% | 10.9 |
| Unmodeled (worst) | 2.6 × 10^6 | 97% | 9.9 |
| Marginalized (σ_GR=0.5) | 4.1 × 10^4 | 97% | 9.4 |
| Marginalized (σ_GR=1.0) | 329 | 96% | 7.9 |
| Corrected (10% residual) | 3.3 × 10^6 | 98% | 10.9 |

The bounce-vs-inflation comparison survives ALL GR treatment scenarios. Even under conservative GR marginalization (σ_GR = 1.0), the bounce is favored at 329:1 over standard inflation and 7.9:1 over tuned multifield.

---

## 8. Discussion

### 8.1 The Staged Observational Strategy

SPHEREx (~2028) provides the first real test via the galaxy bispectrum at ~4-6σ significance. MegaMapper (~2032+, if funded) provides the more powerful but fragile follow-up at 3-7σ via scale-dependent bias. The staged strategy leverages SPHEREx's robustness for the initial test and MegaMapper's statistical power for confirmation.

### 8.2 Decision Thresholds

A measurement of f_NL = -4 ± 1 by SPHEREx would provide strong evidence favoring a contracting/bounce origin over standard single-field inflation. A null result (f_NL consistent with zero at the 2σ level) would strongly disfavor the quasi-dust matter bounce.

### 8.3 Caveats

We emphasize that a detection of f_NL ≈ -4 would constitute strong evidence FAVORING the bounce over standard inflation, not unique proof that the universe underwent a contraction. Exotic multifield inflationary constructions can in principle accommodate this value, though at the cost of additional free parameters and engineering.

The detection significance is conditional on the quality of GR projection modeling at ultra-large scales, the PNG bias parameter calibration, and (for MegaMapper) the multi-tracer implementation quality.

---

## 9. Conclusion

The quasi-dust matter bounce makes a specific, parameter-free, falsifiable prediction: f_NL^local = -35/8. This value is mechanism-independent, 300× larger than the standard inflationary prediction, and opposite in sign. We have shown that SPHEREx can test this prediction at 4-6σ significance through the multi-tracer galaxy bispectrum, with MegaMapper providing a more powerful but systematics-sensitive follow-up.

Our Bayesian model comparison, based on 800,000 Monte Carlo realizations across multiple frameworks including realistic GR contamination treatment, demonstrates that a detection near f_NL = -4.375 would robustly favor the bounce over standard single-field inflation (Bayes factor > 300 even under conservative systematics) and over tuned multifield competitors (Bayes factor > 7). These conclusions are robust to prior sensitivity and survive conservative treatment of all identified systematic effects.

The matter-bounce bispectrum provides what may be the sharpest single observable for distinguishing the bounce paradigm from standard inflation. SPHEREx data, expected around 2028, will provide the first meaningful test.
