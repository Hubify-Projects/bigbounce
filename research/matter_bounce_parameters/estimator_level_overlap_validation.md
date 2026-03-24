# Phase 3: Estimator-Level Overlap Validation — Plan

**Date:** 2026-03-23
**Status:** PUBLIC ESTIMATOR FOUND, IMPLEMENTATION PLANNED

---

## Public Estimator: PolySpec (Philcox)

**Repository:** https://github.com/oliverphilcox/PolySpec
**Author:** Oliver Philcox (Columbia/Simons Foundation)
**Capability:** Full-sky binned and template bispectrum estimators for HEALPix maps

### Key features for our validation

1. **Binned bispectrum estimator:** Measures the bispectrum in triangle bins, providing a model-independent measurement that can be projected onto ANY template
2. **Template amplitude estimator:** Directly estimates f_NL for local, equilateral, orthogonal templates with mask/beam correction
3. **Works on Planck maps:** Example scripts for Planck data included
4. **Public and well-documented:** Jupyter tutorials available

### Our validation strategy

**Step 1: Install PolySpec on RunPod**
- Clone the repo, install dependencies, compile Cython modules
- Verify with the provided tutorial notebooks

**Step 2: Run the local template estimator on SMICA**
- Reproduce the Planck 2018 local f_NL = -0.9 ± 5.1
- This is the BASELINE_REPRODUCED gate
- If this fails, we cannot proceed

**Step 3: Measure the binned bispectrum**
- Extract model-independent binned bispectrum from SMICA
- This gives us the actual data in triangle space

**Step 4: Project onto bounce template**
- Construct the bounce template B_NL(k1, k2, k3) from the verified polynomial
- Project the binned bispectrum onto both local and bounce templates
- Compute the ratio of recovered amplitudes
- THIS gives the estimator-level r

**Step 5: Compare to our shape-inner-product r**
- Our current r = 0.84 ± 0.02 is from shape inner products
- The PolySpec-based r includes ℓ-space projection, beam effects, mask correction
- If they agree: our r is validated at estimator level (upgrade to Level A)
- If they disagree: the difference quantifies the estimator-specific effects

### Dependencies on RunPod

- PolySpec requires: healpy, fitsio, tqdm, pywigxjpf, Cython, ducc0
- SMICA maps already downloaded
- Estimated additional disk: ~500 MB for PolySpec + outputs
- Estimated compute: ~30-60 min for binned bispectrum at lmax=1000

### Expected outcomes

**Optimistic:** r from PolySpec agrees with 0.84 ± 0.02 within errors. The template mismatch is validated at the estimator level. The paper can say "estimator-validated."

**Neutral:** r from PolySpec differs by ~0.05 from our shape calculation, indicating ℓ-space effects. We update r with the estimator-level value and note the correction.

**Pessimistic:** PolySpec cannot run on our data (compatibility issues, missing products). We document the attempt and keep the shape-inner-product r with explicit caveats.

---

## Alternative: CMB-BEST (Wuhyun Sohn)

**Repository:** https://github.com/Wuhyun/CMB-BEST
**Capability:** CMB bispectrum estimator specifically designed for constraining primordial non-Gaussianity

This is an alternative if PolySpec has issues. CMB-BEST may support more flexible template definitions.

---

## Phase 3 Deliverables (planned)

- `planck_like_overlap_test.py` — PolySpec-based validation script
- `template_overlap_estimator_comparison.md` — comparison of shape vs estimator r
- Updated r value with estimator-level validation or explicit caveat

Sources:
- [PolySpec (GitHub)](https://github.com/oliverphilcox/PolySpec)
- [PolyBin3D (for LSS)](https://github.com/oliverphilcox/PolyBin3D)
- [CMB-BEST](https://github.com/Wuhyun/CMB-BEST)
