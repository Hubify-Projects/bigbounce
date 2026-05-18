# P4_v1_0_109_R_INTERNAL R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1715pt
**Wall time**: 85.1s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=89253, completion=9871, reasoning=8805, total=99124

---

## BLOCKER: Contradiction in Canonical-Mask $\sigma$ and Null Variance
**ID:** PAPER-GEM-B1
**Location:** Abstract (v1.0.107 Grok-B1 closure) vs. Sec VIII (Monopole-subtraction note)
**Concrete Issue:** The abstract reports the canonical-mask data with proper monopole subtraction yields $+3.64\sigma$ ($C_1=1.51\times 10^{-5}$, null std $3.31\times 10^{-6}$). Section VIII reports the same proper-monopole-subtracted data yields $+1.77\sigma$ ($C_1=1.79\times 10^{-5}$, null std $\sim 8.09\times 10^{-6}$). The null variances differ by a factor of $\sim 2.5$ for the same mask and data, indicating a severe normalization or mode-coupling bug in one of the two scripts.
**Fix:** Reconcile the injection-sweep null variance with the direct-MC null variance, identify the bugged script, and unify the reported canonical-mask $\sigma$ throughout the text.

## BLOCKER: Tautological Bootstrap Null
**ID:** PAPER-GEM-B2
**Location:** Abstract (v1.0.108 multi-null battery)
**Concrete Issue:** The text states "each pixel's per-galaxy chirality contribution is resampled with replacement". Resampling galaxies *within* a fixed pixel preserves the observed pixel mean $A_p$, meaning the bootstrap distribution perfectly retains the observed spatial dipole. Yielding $-0.22\sigma$ against this distribution is a mathematical tautology, not evidence of "consistency with null" or absence of spatial covariance.
**Fix:** If the intent is to break spatial covariance, the bootstrap must resample pixel values $A_p$ *across different sky locations*. Correct the methodology or the text description to ensure the null actually destroys the spatial dipole.

## MAJOR: Incorrect Real-Space Interpretation of $\ell=2$ Cross-Spectrum
**ID:** PAPER-GEM-M1
**Location:** Abstract (Direct cross-spectrum smoking gun)
**Concrete Issue:** A negative cross-spectrum at $\ell=2$ ($r_{\ell=2}=-0.65$) means the quadrupole moments of the asymmetry and density maps are anti-aligned. It does not mathematically imply the global real-space zero-lag correlation stated ("where there are MORE galaxies per pixel... there is LOWER CW asymmetry"), which would require a negative $\ell=0$ cross-power or a broadband real-space Pearson $r$.
**Fix:** Change the interpretation to "the quadrupole moment of the chirality asymmetry is anti-aligned with the quadrupole moment of the survey depth/density map."

## MAJOR: Missing GR Lightcone Projection Effects
**ID:** PAPER-GEM-M2
**Location:** Sec VI.H (Late-universe to primordial)
**Concrete Issue:** The list of steps required to compute the transfer function from primordial chiral tensors to observed 2D morphology omits general-relativistic lightcone projection effects. Mapping a local 3D spin vector to a 2D sky projection over cosmological distances ($z \sim 0.5$) strictly requires accounting for lensing rotation and frame-dragging corrections.
**Fix:** Add "(iv) general-relativistic lightcone projection effects (e.g., lensing rotation) mapping the local 3D frame to the observer frame" to the transfer-function requirements.

## minor: Stale $+1.85\sigma$ References
**ID:** PAPER-GEM-m1
**Location:** Table III, Sec VIII, Sec IV.D
**Concrete Issue:** Despite the abstract updating the canonical-mask residual to $+3.64\sigma$ (binomial) and $-0.22\sigma$ (bootstrap) via the v1.0.108 battery, Table III and Sec VIII still prominently feature the stale $+1.85\sigma$ result which is explicitly acknowledged to have improper monopole subtraction.
**Fix:** Update Table III and Sec VIII to report the $+3.64\sigma$ binomial / $-0.22\sigma$ bootstrap results, deprecating the $+1.85\sigma$ value entirely.

## minor: Imprecise EFT Operator Sourcing Claim
**ID:** PAPER-GEM-m2
**Location:** Sec VI.H (Parity-odd galaxy-trispectrum amplitude)
**Concrete Issue:** The text states the $\ell=1$ dipole "would require a background vector or tensor source rather than a scalar EFT operator." While true at tree-level in an isotropic background, scalar EFT operators (like the dimension-7 $\dot{\pi} W \tilde{W}$) can source vector observables at loop level or in the presence of background anisotropies.
**Fix:** Clarify to "would require a background vector or tensor source rather than a scalar EFT operator at tree-level in an isotropic background."
