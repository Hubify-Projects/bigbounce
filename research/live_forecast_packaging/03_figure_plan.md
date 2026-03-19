# 03: Figure Plan

## Figure 1: Matter-Bounce Shape Function
**Purpose:** Show the bispectrum shape and squeezed-limit convergence.
**Content:** Plot |B|_NL(k₁, 1, 1) as a function of k₁/k for k₁ from 0 to 1. Mark the three benchmark values (squeezed, equilateral, folded).
**Source:** 02_compute_shape_projection.py (shape function code exists) + the coefficient-verified AT function.
**Status:** CODE EXISTS. Need to generate the actual plot.

## Figure 2: Survey Significance Comparison
**Purpose:** Compare SPHEREx and MegaMapper significance across scenarios.
**Content:** Bar chart or table-style figure showing significance ranges:
- SPHEREx: bispectrum-only (6.3σ), combined (8.75σ), degraded (4-5σ)
- MegaMapper: ideal (8.75σ), realistic (5σ), conservative (3σ), single-tracer (1.75σ)
**Source:** Hardened forecast numbers from the audit.
**Status:** Numbers exist. Need to generate figure.

## Figure 3: Fisher Sensitivity to k_min
**Purpose:** Show the dramatic k_min dependence of SDB-based f_NL constraints.
**Content:** Plot σ(f_NL) vs k_min for MegaMapper (with and without multi-tracer) and SPHEREx.
**Source:** 02_compute_fisher_robustness.py (code exists, ran successfully).
**Status:** CODE EXISTS AND RAN. Need to extract plot data and generate figure.

## Figure 4: Decision Threshold Diagram
**Purpose:** Show the confirm/weaken/kill regions as a function of measured f_NL.
**Content:** Number line or colored region showing:
- f_NL < -3: STRONGLY_FAVORS_BOUNCE
- -3 to -1: SUPPORTS_BOUNCE
- -1 to +1: KILLS_LIVE_LANE
- > +1: KILLS bounce, supports exotic inflation
With error bars for SPHEREx and MegaMapper overlaid.
**Source:** Decision threshold table from the discrimination program.
**Status:** Numbers exist. Need to generate figure.

## Figure 5: Inflation Comparison Schematic
**Purpose:** Show where f_NL = -4.375 sits relative to inflationary predictions.
**Content:** Plot or diagram showing:
- Single-field inflation: f_NL ≈ 0
- Standard curvaton: f_NL > -1.25
- Matter bounce: f_NL = -4.375 (marked, with error bands from SPHEREx/MegaMapper)
- Exotic multi-field: broad range (illustrating that it CAN reach -4 but with free parameters)
**Source:** Inflation mimicry audit numbers.
**Status:** Numbers exist. Need to generate figure.

## Summary

| Figure | Status | Effort |
|--------|--------|--------|
| 1. Shape function | Code exists, need plot | LOW (matplotlib) |
| 2. Survey comparison | Numbers exist, need bar chart | LOW |
| 3. Fisher k_min sensitivity | Code ran, need plot extraction | LOW |
| 4. Decision thresholds | Numbers exist, need diagram | LOW |
| 5. Inflation comparison | Numbers exist, need schematic | LOW |

**All figures are laptop-generatable with existing code/data.** No new computation needed.
