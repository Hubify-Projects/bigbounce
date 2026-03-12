# full_tension Result Validation Report

**Date:** 2026-03-11
**Status:** VALIDATED — all checks pass

---

## 1. Recomputation from Frozen Chain Files

Ran `extract_physical_parameters.py` directly on frozen chain files at:
`reproducibility/cosmology/frozen/full_tension_20260311_1728/chains/`

### Recomputed Values

| Parameter | Mean | Std (68%) | 68% CI | R-1 | ESS |
|-----------|------|-----------|--------|-----|-----|
| H0 | 67.684019 | 1.060648 | [66.6311, 68.7509] | 0.0006 | 5078 |
| delta_neff | -0.019594 | 0.169207 | [-0.1879, 0.1485] | 0.0006 | 4744 |
| tau | 0.053592 | 0.006957 | [0.0469, 0.0604] | 0.0010 | 6507 |
| sigma8 | 0.803395 | 0.008400 | [0.7950, 0.8119] | 0.0008 | 5531 |
| omegam | 0.308090 | 0.005456 | [0.3027, 0.3136] | 0.0006 | 6227 |
| ns | 0.965482 | 0.006184 | [0.9593, 0.9716] | 0.0010 | 5624 |
| S8 | 0.814091 | 0.008456 | [0.8056, 0.8225] | 0.0004 | 6697 |

## 2. Cross-Check Against Stored Values

Compared recomputed values against `research/final_paper_prep/full_tension_physical_parameters.md`:

| Parameter | Recomputed | Stored | Match? |
|-----------|-----------|--------|--------|
| H0 | 67.684019 ± 1.060648 | 67.684019 ± 1.060648 | EXACT |
| delta_neff | -0.019594 ± 0.169207 | -0.019594 ± 0.169207 | EXACT |
| tau | 0.053592 ± 0.006957 | 0.053592 ± 0.006957 | EXACT |
| sigma8 | 0.803395 ± 0.008400 | 0.803395 ± 0.008400 | EXACT |
| omegam | 0.308090 ± 0.005456 | 0.308090 ± 0.005456 | EXACT |
| ns | 0.965482 ± 0.006184 | 0.965482 ± 0.006184 | EXACT |
| S8 | 0.814091 ± 0.008456 | 0.814091 ± 0.008456 | EXACT |

**Result: 7/7 parameters match exactly.**

## 3. Plot Verification

### Triangle Plot (`paper/figures/full_tension_triangle.png`)
- Visually confirmed: diagonal panels show 1D posteriors with correct means
- H0 annotation: "67.7 ± 1.1" — matches
- dNeff annotation: "-0.02 ± 0.17" — matches
- tau annotation: "0.054 ± 0.007" — matches
- sigma8 annotation: "0.803 ± 0.008" — matches
- Omega_m annotation: "0.308 ± 0.006" — matches
- ns annotation: "0.965 ± 0.006" — matches
- Off-diagonal: 2D contours show expected degeneracy structure (H0-dNeff positive correlation)

### 1D Posteriors (`paper/figures/full_tension_posteriors.png`)
- Title: "CORRECTED 1D Marginalized Posteriors"
- All 6 panels show correct parameter ranges and means
- Red dashed lines mark posterior means — consistent with table values
- Well-behaved unimodal posteriors for all parameters

## 4. Convergence Confirmation

All 9 freeze gates passed:
- R-1 (H0, delta_neff): 0.0006 < 0.01
- R-1 (tau): 0.0010 < 0.02
- ESS (H0): 5078 > 2000
- ESS (delta_neff): 4744 > 2000
- ESS (tau): 6507 > 1000
- Drift (all): < 0.1σ (confirmed in freeze report)
- GetDist worst R-1: 0.004470 < 0.01

## 5. Column Mapping Verification

The off-by-one column mapping bug was fixed in `extract_physical_parameters.py`.
Validation checks confirm all parameters fall within expected physical ranges:
- H0 ∈ [60, 80] km/s/Mpc
- delta_neff ∈ [-2, 2]
- tau ∈ [0.01, 0.15]
- sigma8 ∈ [0.5, 1.2]
- omegam ∈ [0.1, 0.6]
- ns ∈ [0.8, 1.1]

## Conclusion

**The full_tension frozen result is validated and ready for publication use.**
All values are internally consistent, match stored records exactly, and all plots reflect the corrected parameter mapping.
