# Phase 3: PolySpec Assessment — Honest Status

**Date:** 2026-03-23

---

## What PolySpec Can Do

PolySpec (Philcox 2025) is the state-of-the-art public CMB bispectrum estimator. It:
- Computes binned bispectra from Planck maps
- Estimates template amplitudes (local, equilateral, orthogonal f_NL)
- Includes mask deconvolution, beam correction, Monte Carlo Fisher matrices
- Has been validated on Planck data

## What We Would Need to Run It

1. **CAMB:** Generate fiducial Cℓ (we can do this)
2. **Smooth analysis mask:** Apodized mask specific to the analysis (NOT the raw PLA mask)
3. **Beam file:** Planck beam transfer functions at the analysis resolution
4. **Noise power spectrum:** Planck noise Nℓ at the analysis resolution
5. **Monte Carlo simulations:** 50-100 FFP10 or equivalent simulations for Fisher matrix
6. **Data maps:** Downgraded to analysis NSIDE (256 in the example)

Items 2-5 are specific to the Philcox preprocessing pipeline and are NOT standard PLA products. Reproducing them requires either:
- Access to Philcox's preprocessed files (not public)
- Building our own preprocessing pipeline (multi-day project)

## What We Can Do Now

### Option A: Use PolySpec's Fisher framework for TEMPLATE COMPARISON

We don't need the full data pipeline to answer our core question. PolySpec's Fisher matrix computation tells us the optimal f_NL sensitivity for ANY template. We can:

1. Generate a fiducial Cℓ from CAMB
2. Compute the Fisher information for the local template
3. Compute the Fisher information for the bounce template
4. The ratio gives the relative sensitivity → equivalent to r²

This does NOT use actual Planck data, but it gives us the **ℓ-space-corrected** template overlap, which accounts for:
- CMB transfer functions
- Noise weighting
- Beam effects
- Multipole-dependent weighting

This is strictly better than our current shape-inner-product r.

### Option B: Build simplified estimator surrogate

Build a KSW-like optimal estimator from scratch (without PolySpec) using:
- Cℓ^fid from CAMB
- Known bispectrum templates (local + bounce)
- Planck noise model (approximate from published values)

This is more tractable and gives us direct control.

## Decision

**Option A is the priority.** It directly answers "what is the ℓ-space-corrected template overlap?" without requiring the full Planck pipeline.

**Option B is the fallback** if Option A fails.

## Impact on r = 0.84 ± 0.02

Our current r is from a k-space shape inner product. The ℓ-space result may differ because:
- The CMB transfer function modifies the k-space shape before it reaches the estimator
- Noise is ℓ-dependent, changing the weighting
- The beam suppresses high-ℓ modes

These effects could move r by ~0.02-0.05 in either direction. The shape-inner-product result (0.84) should be treated as correct to ~5% until the ℓ-space calculation is done.
