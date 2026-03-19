# r Tension Assessment

## The Concern

The GENERIC matter bounce (pure dust, w = 0, standard GR) predicts r ~ O(1). Current data gives r < 0.036 (Planck + BICEP). This is a factor ~30 discrepancy.

## Resolution: ALREADY IN THE REPO

**The r tension was resolved in project_viable_bounce_model_pass2 (2026-03-17).**

The Wilson-Ewing LCDM Quasi-Dust model (Model B) achieves r ~ 10⁻⁴ through LQC quantum-geometry corrections. Specifically:

| Mechanism | What it fixes | Price |
|-----------|--------------|-------|
| LQC quantum bounce | r ~ 10⁻⁴ (tensor suppression) | Tensor sector becomes unmeasurable (r too small) |
| Quasi-dust w = -0.003 | n_s = 0.964 (red tilt) | One free parameter (ε, fitted to n_s) |
| Lambda (ΛCDM ingredient) | Physical motivation for w < 0 | Already in ΛCDM, not new |

**Critically:** LQC corrections suppress r WITHOUT affecting f_NL.

From the prior analysis: "LQC corrections affect r (tensor-to-scalar amplitude ratio) but NOT f_NL (scalar self-interaction). The EOS epsilon affects the tilt but NOT the nonlinear transfer function."

## Why LQC Suppresses r but Not f_NL

The LQC effective equations modify the tensor propagation through quantum-geometry corrections to the Mukhanov-Sasaki equation for tensor modes. These corrections preferentially affect the tensor sector because:

1. Tensor modes interact with the background geometry (through the scale factor evolution)
2. The LQC bounce modifies the scale factor evolution at high density
3. The tensor transfer through the bounce is modified by the quantum corrections
4. The scalar bispectrum f_NL is computed BEFORE the bounce (in the contracting phase) where LQC corrections are negligible

The separation of scales ensures: f_NL is set at k ~ H during contraction (sub-Planckian density), while r is modified at the bounce (Planck density). The two observables are controlled by different epochs.

## Current Best Model Parameters

| Observable | Prediction | Status |
|-----------|-----------|--------|
| n_s | 0.964 | ✅ Matches Planck |
| r | ~10⁻⁴ | ✅ Well below r < 0.036 |
| f_NL | -35/8 = -4.375 | ✅ Consistent with Planck (within 1σ) |
| α_s | ~10⁻⁴ | ✅ Consistent with Planck |

## Verdict

**The r tension is NOT an existential threat.** It was already resolved in the Wilson-Ewing quasi-dust model through LQC quantum corrections. The f_NL = -35/8 prediction survives intact.

The price is: r becomes unmeasurable (too small for LiteBIRD), and n_s requires one fitted parameter (ε = 0.003). But the FLAGSHIP discriminator (f_NL = -35/8, parameter-free) is preserved.

## My Error

I flagged the r tension as the "single highest-value calculation" without checking the existing repo. The viable bounce model work (Pass 2) had already identified and addressed this. The Wilson-Ewing model accommodates r < 0.036 naturally through LQC, while keeping f_NL = -35/8 untouched.

The actual highest-priority remaining work is completing the f_NL benchmark ownership (parsing Cai's equations cleanly) — not reassessing the r tension.
