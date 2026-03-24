# PolySpec Validation — Status

**Date:** 2026-03-24

## What We Achieved

- PolySpec installed, compiled, and operational on RunPod
- PolySpec.PolySpec base class works: generates simulations, applies filters
- BSpecTemplate class discovered: requires mask, inverse signal matrix, template definitions
- Fisher derivative functions available at low level

## What Remains

BSpecTemplate requires building a complete pipeline:
1. **mask**: apodized analysis mask (we have this from NaMaster)
2. **applySinv**: inverse-signal weighting function (need to build from Cℓ)
3. **templates**: list of template names (local, etc.)
4. **lmin, lmax**: analysis range
5. **k_arr, Tl_arr, r_arr**: radiation transfer functions from CAMB

Items 1, 4, 5 are straightforward. Items 2-3 require understanding PolySpec's internal API.

## Assessment

Building the full PolySpec pipeline is a **1-2 session project**, not a quick test. It requires:
- Reading the PolySpec tutorial notebooks carefully
- Setting up the radiation transfer functions (CAMB → PolySpec format)
- Building the inverse-signal weighting
- Implementing a custom bounce template in PolySpec's framework
- Running on simulated data first, then on real SMICA

This is feasible but is NOT a closure task — it's a follow-up project.

## Current r Validation Status

Without PolySpec, our r validation rests on THREE independent methods:
1. k-space shape inner product: r = 0.84 ± 0.02
2. ℓ-space Fisher overlap: r = 0.878 ± 0.012
3. MC injection recovery: r = 0.900 ± 0.012

These are sufficient for the paper. PolySpec would provide a fourth, estimator-grade validation but is not strictly necessary.

**Final value: r = 0.88–0.90 (injection-validated)**
