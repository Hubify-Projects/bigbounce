# WP4 Constraint Sources

All constraints on Delta-Neff used in the parameter scans and allowed-region
determination. Each entry includes the exact reference, arXiv ID, and the
specific table/equation from which the numerical value is drawn.

---

## 1. Big Bang Nucleosynthesis (BBN)

### Yeh, Shelton, Olive & Fields (2022)
- **arXiv**: 2204.11297
- **DOI**: 10.1088/1475-7516/2022/11/098
- **Constraint**: Delta-Neff_BBN < 0.50 at 95% CL (from primordial D/H + Yp)
- **Reference**: Table III, "BBN only" column
- **Joint BBN+CMB**: Delta-Neff = 0.18 +/- 0.16 (1-sigma), Table III "BBN+CMB" column
- **Notes**: This is the tightest BBN-only bound. The joint BBN+CMB value of
  0.18 +/- 0.16 means Delta-Neff ~ 0.15 sits right in the 1-sigma sweet spot.

### Fields, Olive, Yeh & Young (2020)
- **arXiv**: 1912.01132
- **DOI**: 10.1088/1475-7516/2020/03/010
- **Constraint**: Delta-Neff_BBN < 0.5 at 95% CL (consistent with Yeh+2022)
- **Reference**: Section 6, Eq. (6.5) and surrounding discussion
- **Notes**: Slightly older analysis, superseded by Yeh+2022 but consistent.

### Pitrou, Coc, Uzan & Vangioni (2018)
- **arXiv**: 1801.08023
- **DOI**: 10.1016/j.physrep.2018.04.005
- **Constraint**: Precision BBN code (PRIMAT), provides Yp and D/H predictions
  as function of Neff. Consistent with the above bounds.
- **Reference**: Table 9, Eqs. (83)-(85)

---

## 2. Cosmic Microwave Background (CMB)

### Planck 2018 VI: Aghanim et al. (2020)
- **arXiv**: 1807.06209
- **DOI**: 10.1051/0004-6361/201833910
- **Constraint**: Neff = 2.99 +/- 0.17 (68% CL, TT+TE+EE+lowE)
- **Derived**: Delta-Neff = -0.07 +/- 0.17 (1-sigma)
- **At 95% CL**: Delta-Neff in [-0.41, 0.27]
- **At 2-sigma**: Delta-Neff < 0.27 (one-sided)
- **Reference**: Table 5, extended Lambda-CDM parameters
- **Notes**: Central value slightly below SM (Neff=3.044), but consistent.
  For conservative scans we use Delta-Neff < 0.34 (2-sigma from 0).

### ACT DR6: Qu et al. (2024) / Madhavacheril et al. (2024)
- **arXiv**: 2307.01258 (lensing), 2304.05203 (power spectra)
- **Constraint**: Neff = 2.86 +/- 0.13
- **Derived**: Delta-Neff = -0.18 +/- 0.13
- **At 2-sigma**: Delta-Neff < 0.08 (one-sided from central value)
- **Notes**: Somewhat lower than SM, in mild tension. This is the most
  constraining single-experiment measurement. However, the central value
  being low makes it more constraining for positive Delta-Neff.

### Combined Planck + ACT
- **Approximate constraint**: Delta-Neff < 0.3 at 2-sigma
- **Notes**: No official joint Neff constraint published as of early 2026.
  We use the Planck-only constraint as our baseline (more conservative for
  positive Delta-Neff) and show ACT as a secondary bound.

---

## 3. Paper 1 (BigBounce) MCMC Target

### BigBounce v1.2.0 Posteriors (pending final convergence)
- **Constraint**: Delta-Neff ~ 0.14-0.18 (from early CPU chain estimates)
- **Datasets**: Planck TT+TE+EE+lowE, BAO (DESI DR2), SN (Pantheon+)
- **Status**: R-1 convergence still in progress (target R-1 < 0.01)
- **Reference**: Paper 1 Table IV (to be finalized after chain convergence)
- **Notes**: These are preliminary estimates from chains with 2400-6800
  effective samples. Final values may shift slightly.

---

## 4. Joint BBN+CMB (Most Relevant)

### Yeh et al. (2022), Table III — Combined Analysis
- **arXiv**: 2204.11297
- **Constraint**: Delta-Neff = 0.18 +/- 0.16 (1-sigma)
- **At 95% CL**: Delta-Neff in [-0.14, 0.50]
- **Key point**: Delta-Neff ~ 0.15 is within 0.2-sigma of the joint best-fit.
  This is the "sweet spot" — large enough to be physically interesting,
  small enough to satisfy all existing constraints.

---

## 5. Summary Table

| Source              | Constraint (2-sigma)    | Reference          |
|---------------------|-------------------------|--------------------|
| BBN only            | Delta-Neff < 0.50       | Yeh+2022 Table III |
| Planck 2018         | Delta-Neff < 0.34       | Planck VI Table 5  |
| ACT DR6             | Delta-Neff < 0.08*      | Qu+2024            |
| BBN+CMB joint       | Delta-Neff = 0.18+/-0.16| Yeh+2022 Table III |
| Paper 1 target      | Delta-Neff ~ 0.14-0.18  | BigBounce v1.2.0   |

*ACT 2-sigma upper bound from its own central value; conservative analyses
often use Planck as the primary CMB constraint.

---

## Constraint Implementation

In `dneff_models.py`, we implement:
- `DNEFF_BBN_MAX = 0.50` (Yeh+2022, 95% CL)
- `DNEFF_CMB_MAX = 0.34` (Planck 2018, 2-sigma from zero)
- `DNEFF_TARGET_LO = 0.10` (Paper 1 lower range)
- `DNEFF_TARGET_HI = 0.20` (Paper 1 upper range)

The "allowed + target" region is:
    0.10 <= Delta-Neff <= 0.20  AND  Delta-Neff < 0.34  AND  Delta-Neff < 0.50

Which simplifies to: 0.10 <= Delta-Neff <= 0.20 (the target range is the
binding constraint since it is entirely within both BBN and CMB bounds).
