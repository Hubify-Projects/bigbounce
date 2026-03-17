# Observable Window Analysis Report

**Date:** 2026-03-13
**Program:** Early Structure from Bounce Cosmology — P(k) Feature Window

---

## 1. Analysis Performed

A forward-model grid scan over the (k_*, P_R) parameter space, computing three constraint/target layers:

1. **SMBH seed threshold:** Minimum P_R at each k_* needed to produce at least ~1 PBH seed per Gpc³ (matching observed high-z SMBH number density ~10⁻⁹ Mpc⁻³)
2. **PBH overproduction ceiling:** Maximum P_R at each k_* before f_PBH exceeds observational upper limits (compiled from Carr+ 2020, Green & Kavanagh 2021)
3. **FIRAS μ-distortion ceiling:** Maximum P_R at k < 10⁴ Mpc⁻¹ before violating FIRAS μ < 9 × 10⁻⁵

The P(k) feature model is a Gaussian bump:
P_R(k) = A_s(k/k_pivot)^{n_s-1} × [1 + A_bump × exp(−(ln k/k_*)²/(2Δ²))]

with Δ = 1 (one e-fold width, fiducial).

### Mapping: P_R → f_PBH

- σ²(M) ≈ (16/81) × 0.4 × P_R × Δ (calibrated effective smoothing)
- β(M) = erfc(δ_c/(√2 σ))/2 with δ_c = 0.45
- f_PBH = 1.3 × 10⁸ × (M/M_☉)^{-1/2} × β(M)
- M/M_☉ = 33 × (k/10⁶ Mpc⁻¹)^{-2}

---

## 2. Results

### Scale Mismatch

| Quantity | Framework value | SMBH-relevant value | Mismatch |
|----------|----------------|---------------------|----------|
| k_feature (Mpc⁻¹) | 5.86 × 10¹⁴ | 2 × 10⁴ to 6 × 10⁵ | **10⁹** |
| M_PBH (M_☉) | 10⁻¹⁶ | 10² to 10⁵ | **10¹⁸** |
| N_tot required | 92 (fitted) | ~70 (needed) | ΔN = 22 |

### Phenomenological Window (Ignoring Framework Scale Prediction)

A narrow allowed window EXISTS in the phenomenological parameter space:

| Parameter | Value |
|-----------|-------|
| Best scale | k_* ≈ 10^{5.7} Mpc⁻¹ (M ≈ 110 M_☉) |
| P_R floor (seed threshold) | 10^{-1.62} |
| P_R ceiling (PBH constraint) | 10^{-1.25} |
| **Window width** | **~0.37 decades** |

This window is **extremely narrow**: only a factor of ~2.3 in P_R amplitude separates "enough seeds" from "PBH overproduction."

The narrowness is a fundamental consequence of the erfc function's steep dependence on σ. The PBH formation rate transitions from negligible to order-unity over a very small range of P_R.

### μ-Distortion Constraint

The FIRAS μ-distortion constraint affects features at k < 10⁴ Mpc⁻¹. Since the SMBH seed window is at k > 10⁴ Mpc⁻¹, the μ constraint does not further restrict the SMBH window.

However, it would constrain any feature at intermediate scales (k ~ 10²–10⁴ Mpc⁻¹) to P_R < ~10⁻⁵ to 10⁻⁴, depending on the feature width.

### Framework-Predicted Scale

At k_bounce ≈ 6 × 10¹⁴ Mpc⁻¹ (M ≈ 10⁻¹⁶ M_☉):
- Falls in the **asteroid-mass PBH window** (weakly constrained)
- PBH constraint: f_PBH < 1 (essentially unconstrained)
- Potentially interesting for PBH dark matter but **completely irrelevant for SMBH seeds**

---

## 3. Figures Produced

1. **`pk_feature_window_analysis.pdf`** — Full (k, P_R) parameter space showing PBH constraints, SMBH seed threshold, μ-distortion bound, framework-predicted scale, and the scale mismatch. Also saved to `paper/figures/`.

2. **`pk_feature_smbh_zoom.pdf`** — Zoomed view of the SMBH-relevant scales showing the narrow phenomenological window between the seed threshold and PBH overproduction limit.

---

## 4. Key Physical Insight

The phenomenological window is narrow (~0.4 decades) because PBH formation is a threshold process. The collapse fraction β transitions from ~10⁻²⁰ to ~10⁻¹ over a factor of ~2 change in P_R. This means:

- **Any P(k) feature at SMBH scales is either negligible or immediately runs into PBH constraints**
- **There is no "comfortable" region** where abundant seeds form without overproducing PBHs
- **Fine-tuning in P_R at the ~0.3 dex level** would be required even in the phenomenological model

This narrowness is not specific to our framework — it affects ALL P(k)-based SMBH seed models.

---

## 5. Verdict

| Question | Answer |
|----------|--------|
| Does a phenomenological window exist? | YES, but very narrow (~0.4 dex in P_R) |
| Is it at the framework-predicted scale? | **NO — mismatch of 10⁹ in k** |
| Could the framework target this window? | **Only by abandoning N_tot = 92** (breaks dark energy constraint) |
| Is this useful for the current paper? | **Only as a future-work caveat** |
| Is this useful for a follow-up paper? | **Marginally** — the phenomenological window analysis is publishable but not connected to the framework |
