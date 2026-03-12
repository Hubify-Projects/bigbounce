# Theory Claims: Supported vs. Not Supported

**Date:** 2026-03-12
**Purpose:** Clear reference for manuscript editing -- what the theory audit and MCMC results do and do not support.

---

## SUPPORTED CLAIMS (with evidence)

| Claim | Evidence |
|-------|----------|
| Derivation chain from ECH action to rho_Lambda is dimensionally consistent | Dimensional audit: 10/12 equations fully consistent; 2/12 have acknowledged scaling ansatze (Eqs. 7 and A_0) |
| Fine-tuning reduced from 10^120 to 10^5 | Monte Carlo scan, 100K samples; viable fraction 2.2% (1 in 46); residual tuning = specification of N_tot to within ~4 e-folds |
| Framework correctly reduces to GR in all physical limits | 5/5 limit checks pass: torsion->0, alpha/M->0, D_inf->1, gamma->0 (singular, correctly excluded), gamma->infinity |
| N_tot is the single controlling parameter for rho_Lambda | Spearman |rho_s| = 0.996 for N_tot; all other parameters |rho_s| < 0.08 |
| Viable N_tot range is physically reasonable | [79, 95] e-folds -- exceeds CMB minimum (~60), below eternal inflation scenarios (~140) |
| Residual tuning is initial-condition type, not fundamental-constant type | The only parameter that matters (N_tot) is an initial condition of inflation, not a fundamental coupling constant |
| Four-fermion contact interaction survives when parity violation is turned off | Limit 2 check: alpha/M -> 0 removes DE and birefringence but preserves the bounce and spin-torsion contact term |
| Without inflation, the mechanism reproduces the standard CC problem | Limit 3 check: D_inf -> 1 gives rho_Lambda ~ 10^{-2} M_Pl^4, which is 10^121 times too large |
| MCMC results are consistent with SM (no tension with standard N_eff) | delta_neff = -0.020 +/- 0.16 (full_tension) and +0.065 +/- 0.19 (planck_bao_sn); both consistent with zero within 1-sigma |
| Parity-odd coefficient alpha/M has one-loop motivation | Multiple independent analyses (Freidel et al., Mercuri, Shapiro & Teixeira) establish existence; order of magnitude [(alpha/M)*M_Pl ~ 10^{-2}] is generic one-loop prediction |

---

## NOT SUPPORTED / MUST BE STATED AS ASSUMPTIONS

| Claim that must NOT be presented as derived | Actual status |
|---------------------------------------------|---------------|
| N_tot ~ 92 is predicted by the theory | **Fitted, not predicted.** N_tot is adjusted to match the observed rho_Lambda. The mechanism reparametrizes the CC problem as a duration-of-inflation problem. |
| w = -1 at late times is derived from the framework | **Assumed, not derived.** The persistence of the vacuum energy term after the spin source vanishes is an input assumption. The paper identifies deriving the late-time IR effective action as an open problem. |
| Galaxy spin amplitude A_0 ~ 0.003 follows from the theory | **Fitted, with a 9-12 OOM gap.** The naive parity-odd tidal torque estimate falls 9-12 orders of magnitude short of the observed amplitude. A_0 is a fit parameter, and the proportionality hides a required energy scale E_eff. |
| The exact value of alpha/M is first-principles determined | **Scheme-dependent.** Its existence is established at one loop, but the exact value depends on the gamma_5 prescription and Nieh-Yan counterterm ambiguity (delta_NY is unknown). |
| The dimensional bridge from dim +1 to dim +4 is a controlled EFT calculation | **Scaling ansatz.** The parity-odd Lagrangian density has mass dimension +1; the paper invokes on-shell Planck-scale evaluation to reach dim +4. This is physically motivated but not a rigorous derivation. |
| delta_neff = +0.065 confirms the model | **Not confirmed.** The value is consistent with zero at well within 1-sigma. It has the predicted sign but is not statistically significant. CMB-S4 (~0.03 sensitivity) is needed for a meaningful test. |
| The bounce-to-inflation transition selects N_tot dynamically | **Conjectured, not demonstrated.** This is stated as a potential dynamical escape route from the residual fine-tuning, but no calculation exists showing that bounce dynamics select N_tot ~ 92. |
| T_reh ~ 10^15 GeV and M_GUT ~ 10^16 GeV are derived | **Standard GUT-scale assumptions.** These are inputs, though the Monte Carlo scan shows they have negligible impact on the result (|rho_s| < 0.08). |

---

## EDITORIAL GUIDANCE

1. **Language precision:** Use "the mechanism reduces fine-tuning from 10^120 to 10^5" rather than "solves the cosmological constant problem."
2. **Attribution:** When citing the 10^5 number, attribute it to the Monte Carlo scan (100K samples) with the viable N_tot range [79, 95].
3. **Honesty about N_tot:** Every mention of the fine-tuning improvement should be accompanied (at least once in the paper) by the caveat that N_tot is fitted.
4. **delta_neff:** Present as "consistent with standard model expectations" and note that the framework's prediction lies within current uncertainties. Do not present as evidence for or against the model.
5. **Galaxy spins:** Present as a qualitative prediction (correct sign of parity violation) with a quantitative gap that requires further theoretical work.
6. **Two scaling ansatze:** Both the dimensional bridge (Eq. 7) and the galaxy spin amplitude (A_0) should be explicitly flagged in the discussion as open theoretical problems, not swept into footnotes.
