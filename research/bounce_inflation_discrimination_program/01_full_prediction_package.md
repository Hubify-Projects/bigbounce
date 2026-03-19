# 01: Full Prediction Package

## Primary Observables

### 1. Scalar Non-Gaussianity f_NL
**Value:** f_NL^local = -35/8 = -4.375
**Classification:** SHARP_PREDICTION
**Why:** Parameter-free. Depends only on ε = 3/2 (matter contraction) and standard GR cubic action. No adjustable inputs.
**Template overlap:** cos(θ) ≈ 0.95 with local template → effective amplitude f_NL^eff ≈ -4.16

### 2. Spectral Index n_s
**Value:** n_s = 1 - 12ε = 0.964 (for ε = 0.003)
**Classification:** MODEL_DEPENDENT
**Why:** ε is the one free parameter, fitted to Planck n_s. The FORMULA n_s = 1 - 12ε is fixed, but the VALUE depends on ε.

### 3. Tensor-to-Scalar Ratio r
**Value:** r ~ 10⁻⁴
**Classification:** SHARP_PREDICTION (within LQC framework)
**Why:** Set by LQC quantum-geometry corrections. Not continuously adjustable — it's determined by the Immirzi parameter γ = 0.274 and ρ_crit.

## Secondary Observables

### 4. Bispectrum Shape Ratios
**Values:** |B|_NL^equil / |B|_NL^squeezed = (-255/64)/(-35/8) = 0.911
           |B|_NL^folded / |B|_NL^squeezed = (-9/4)/(-35/8) = 0.514
**Classification:** SHARP_PREDICTION (but hard to measure precisely)
**Why:** Determined by the same shape function. Would require shape decomposition beyond local template.

### 5. Sign of f_NL
**Value:** NEGATIVE
**Classification:** SHARP_PREDICTION
**Why:** The growing-mode mechanism in contraction generically produces negative f_NL. Standard slow-roll inflation gives f_NL ≈ 0 (tiny positive). The SIGN is the single cleanest discriminator.

### 6. Consistency Relation Violation
**Value:** f_NL ≠ (5/12)(1-n_s) by a large amount
**Classification:** SHARP_PREDICTION (but requires precise simultaneous measurement of f_NL and n_s)
**Why:** The Maldacena consistency relation f_NL = (5/12)(1-n_s) ≈ 0.015 holds for single-field inflation. The matter bounce gives f_NL = -4.375 — a violation by a factor of ~300.

### 7. Running of Spectral Index α_s
**Value:** α_s ~ +10⁻⁴ (positive, very small)
**Classification:** NOT_USEFUL_FOR_DISCRIMINATION
**Why:** Too small to measure. Current σ(α_s) ~ 0.007.

### 8. Tensor Spectral Tilt n_T
**Value:** n_T > 0 (blue)
**Classification:** NOT_USEFUL_FOR_DISCRIMINATION
**Why:** r ~ 10⁻⁴ makes the tensor spectrum unmeasurable. Blue tilt is a theoretical prediction but observationally inaccessible.

## Summary Table

| Observable | Value | Classification | Detectable? |
|-----------|-------|---------------|------------|
| f_NL^local | **-4.375** | SHARP_PREDICTION | **YES (MegaMapper 8.3σ)** |
| Sign(f_NL) | **negative** | SHARP_PREDICTION | **YES** |
| n_s | 0.964 | MODEL_DEPENDENT | Already measured |
| r | ~10⁻⁴ | SHARP_PREDICTION | Below LiteBIRD threshold |
| Shape ratios | 0.91, 0.51 | SHARP_PREDICTION | Requires future shape analysis |
| Consistency violation | f_NL >> (5/12)(1-n_s) | SHARP_PREDICTION | **YES (if f_NL detected)** |
| α_s | ~10⁻⁴ | NOT_USEFUL | No |
| n_T | >0 | NOT_USEFUL | No |
