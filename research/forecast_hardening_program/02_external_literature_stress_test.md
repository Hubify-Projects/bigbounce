# 02: External Literature Stress Test

## Known Forecast Fragilities for Local f_NL from LSS

### 1. Relativistic Projection Effects
**Issue:** General-relativistic corrections to the observed galaxy number counts create an effective "fake" f_NL of order f_NL^GR ~ 1-5 on the largest scales (Bruni et al. 2012, Yoo 2010, Bonvin & Durrer 2011).

**Impact on our signal:** f_NL^GR ~ O(1) vs our signal |f_NL| = 4.375. The contamination is ~20-100% of the signal in the worst case.

**Mitigation:** These effects are COMPUTABLE and can be subtracted. They depend on the observer's velocity, lensing, and the metric at the survey boundary. Modern forecasts include these corrections explicitly. The residual after correction is expected to be << 1.

**Severity for us:** MODERATE. Must be accounted for but does not kill the signal. The SIGN of f_NL^GR is typically positive, while our signal is negative — the contamination would REDUCE the measured |f_NL| but not flip its sign.

### 2. Galaxy Bias Modeling
**Issue:** The SDB signal Δb ∝ f_NL(b₁-1)/k² requires accurate knowledge of b₁ (linear bias). Uncertainty in b₁ propagates linearly to f_NL uncertainty.

**Impact:** If b₁ is uncertain at 5%, σ(f_NL) degrades by ~5%. This is relatively benign.

**But:** Non-linear bias (b₂, etc.) and scale-dependent stochasticity can mimic the 1/k² signal. These are harder to model and could contribute systematic floors.

**Severity:** LOW-MODERATE. Standard Fisher forecasts include bias marginalization. The degradation is typically 20-50% in σ(f_NL).

### 3. Multi-Tracer Assumptions
**Issue:** The MegaMapper σ(f_NL) = 0.5 forecast assumes multi-tracer technique with 2+ well-separated galaxy populations. If only one tracer is available:
- σ(f_NL) degrades from 0.5 to ~2-3 (cosmic variance limited)
- Detection significance drops from 8.75σ to 1.5-2.2σ

**Severity:** HIGH for MegaMapper. The multi-tracer capability is ESSENTIAL for the claimed significance. For SPHEREx (primarily single-tracer with photo-z), the multi-tracer enhancement is smaller.

### 4. Photo-z Quality (SPHEREx-Specific)
**Issue:** SPHEREx uses photometric redshifts at R ~ 40-130. Photo-z scatter and catastrophic outliers degrade the radial power spectrum measurement, reducing the number of independent k-modes at large scales.

**Impact:** Photo-z degradation increases σ(f_NL) by a factor of 1.5-3× compared to spectroscopic quality (Doré et al. 2014 vs later assessments).

**Severity:** HIGH for SPHEREx. The σ(f_NL) = 1.0 central estimate already accounts for moderate photo-z degradation, but pessimistic scenarios could push σ to 2-3.

### 5. Scale Cuts (k_min)
**Issue:** The f_NL signal grows as 1/k² — the LARGEST scales carry the most information. If systematic uncertainties require cutting k < k_min:
- Cutting modes below k = 0.001 h/Mpc loses ~30% of the f_NL constraining power
- Cutting below k = 0.005 h/Mpc loses ~70%

**Severity:** HIGH if aggressive scale cuts are needed. The largest scales are also where survey geometry effects, stellar contamination, and wide-angle corrections are worst.

### 6. Survey Geometry / Window Function
**Issue:** Realistic survey footprints are not full-sky. The convolution of the survey window with the large-scale power spectrum couples modes and degrades the effective volume for f_NL.

**Impact:** Typically 10-30% degradation in σ(f_NL) compared to ideal full-sky forecasts.

**Severity:** LOW-MODERATE. Accounted for in realistic forecasts.

### 7. Non-Gaussian Covariance (Trispectrum)
**Issue:** If f_NL is large, the trispectrum (connected 4-point function) contributes to the covariance of the power spectrum, modifying the Fisher forecast.

**Impact:** For |f_NL| ~ 4, the trispectrum correction to the covariance is ~(f_NL)² × O(10⁻⁴) ~ 10⁻³ — negligible compared to the Gaussian covariance.

**Severity:** NEGLIGIBLE.

### 8. Foregrounds / Systematics Floor
**Issue:** Galactic dust, stellar contamination, and calibration errors create large-scale power that can mimic the f_NL signal.

**Impact:** Depends strongly on the survey. SPHEREx (infrared) has different systematics from optical surveys. MegaMapper (spectroscopic) is less affected by photometric systematics.

**Severity:** MODERATE. Requires careful characterization but does not fundamentally limit the measurement.

## Summary: Fragility Rankings

| Effect | Severity | Impact on σ(f_NL) | Addressed in Standard Forecasts? |
|--------|---------|-------------------|--------------------------------|
| Multi-tracer requirement | **HIGH** | Factor 4-6× if fails | Yes (but optimistic) |
| Photo-z quality (SPHEREx) | **HIGH** | Factor 1.5-3× | Partially |
| Scale cuts (k_min) | **HIGH** | Up to 70% power loss | Partially |
| GR projection effects | **MODERATE** | ~20% signal contamination | Yes (computable) |
| Galaxy bias modeling | **LOW-MODERATE** | ~20-50% in σ | Yes |
| Survey geometry | **LOW** | ~10-30% | Yes |
| Non-Gaussian covariance | **NEGLIGIBLE** | ~0.1% | N/A |
| Foregrounds | **MODERATE** | Survey-dependent | Partially |

## The Three Most Fragile Assumptions

1. **Multi-tracer performance** (MegaMapper): if multi-tracer fails, significance drops from 8.75σ to ~1.5-2.2σ
2. **Photo-z quality** (SPHEREx): if photo-z degrades, σ increases by 1.5-3×
3. **Scale cuts**: if large-scale modes are lost to systematics, constraining power drops sharply
