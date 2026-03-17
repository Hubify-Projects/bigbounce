# Figure Plan

**Date:** 2026-03-17

---

## Figures for the Paper

### Figure 1: ECH Bounce Schematic
**Location:** Section 2.2
**Content:** H²(ρ) showing the modified Friedmann equation with bounce at ρ_crit. Standard GR curve vs ECH curve. Labels: ρ_crit ≈ 0.27 ρ_Pl, H = 0 at bounce.
**Source:** Existing `public/images/` or new matplotlib plot.
**Status:** EXISTS (adapt from current paper)

---

### Figure 2: Structural Barrier Summary
**Location:** Section 3.2
**Content:** Visual map of the 15 branches (A–O) with color-coded status (CLOSED/GENERIC/WEAK). Arrow diagram showing which barrier kills which route. Or: compact table rendered as figure.
**Format:** Flowchart or matrix diagram.
**Status:** NEW — needs creation

---

### Figure 3: ALP Rolling Efficiency η(m/H₀)
**Location:** Section 4.1
**Content:** η vs log₁₀(m/eV) for θ_i = 1.0. Shows transition from frozen (η → 0 for m ≪ H₀) to fully rolled (η → 1 for m ≫ H₀). Mark spectator regime and DE regime. Overlay: horizontal band for β_obs.
**Source:** Compute from `alp_ode.py` with mass scan.
**Status:** NEW — straightforward computation

---

### Figure 4: β Prediction vs Observation
**Location:** Section 4.3
**Content:** β vs θ_i showing the linear prediction β = 0.27° × θ_i (for η = 1, C = 8). Horizontal band: observed β = 0.342 ± 0.094°. Vertical band: inferred θ_i = 1.3 ± 0.4. Shaded natural region θ_i ∈ [0.5, 2.5].
**Source:** Simple analytic plot.
**Status:** NEW — straightforward

---

### Figure 5: MCMC Triangle Plot (Run 1)
**Location:** Section 5.2
**Content:** 2D posterior for (θ_i, log₁₀ m) with 68% and 95% contours. Marginal 1D histograms on diagonal. Derived β shown as color or separate panel.
**Source:** `chains/run1_full/triangle_plot.png` (exists)
**Status:** EXISTS — may need cosmetic cleanup for publication

---

### Figure 6: β Posterior Comparison (3 Models)
**Location:** Section 5.4
**Content:** Overlaid 1D posteriors for β from: (a) ALP C=8, (b) ALP C free, (c) free β. Shows they are indistinguishable. Vertical line at β = 0.
**Source:** `chains/run2_extended/beta_comparison_all_models.png` (exists)
**Status:** EXISTS — may need axis labels for publication

---

### Figure 7: C × θ_i Degeneracy
**Location:** Section 5.3
**Content:** 2D scatter plot of C_agamma vs θ_i colored by β value. Shows the hyperbolic degeneracy C × θ_i = const. SM value C = 8 marked.
**Source:** `chains/run2_extended/C_vs_theta_degeneracy.png` (exists)
**Status:** EXISTS

---

### Figure 8: Experimental Constraint Landscape
**Location:** Section 6.1
**Content:** ALP parameter space (g_aγ vs m_a) showing: CAST exclusion, SN1987A, superradiance, and the model prediction point. Standard "ALP landscape" plot with our model marked.
**Source:** Adapt from standard ALP constraint plots in literature; mark our point.
**Status:** NEW — standard format, well-defined

---

### Figure 9: LiteBIRD Forecast
**Location:** Section 6.2
**Content:** β posterior with current data (broad Gaussian) vs projected LiteBIRD posterior (narrow Gaussian at σ = 0.01°). If β = 0.27°: shows clear detection. If β = 0: shows clear exclusion.
**Source:** Simple Gaussian overlay.
**Status:** NEW — straightforward

---

## Figure Summary

| # | Title | Section | Status | Priority |
|---|-------|---------|--------|----------|
| 1 | Bounce schematic | 2.2 | EXISTS | Medium |
| 2 | Barrier map | 3.2 | NEW | High |
| 3 | Rolling efficiency | 4.1 | NEW | High |
| 4 | β vs θ_i prediction | 4.3 | NEW | High |
| 5 | Triangle plot | 5.2 | EXISTS | High |
| 6 | β comparison | 5.4 | EXISTS | Medium |
| 7 | C-θ degeneracy | 5.3 | EXISTS | Low (may move to appendix) |
| 8 | ALP constraints | 6.1 | NEW | Medium |
| 9 | LiteBIRD forecast | 6.2 | NEW | Medium |

**Total: 9 figures** (4 existing, 5 new)

---

## Production Notes

- All new figures: matplotlib, publication quality (fontsize 12, 300 dpi, PDF output)
- Color scheme: consistent across all figures (blue = ALP model, orange = data, green = forecast)
- Existing chain plots may need: axis relabeling, font size increase, legend cleanup
- Figure 2 (barrier map) is the most design-intensive; consider a clean table format if flowchart is too busy
- Figure 8 (ALP landscape) should cite the standard reference for the constraint compilation
