# Theory Audit + Cosmology Results: Integration Note for Manuscript Editing

**Date:** 2026-03-12
**Purpose:** Guide for connecting the theory validation audit to the MCMC cosmology results when editing the manuscript.

---

## 1. Fine-Tuning Claim: State Carefully

The Monte Carlo scan (100K samples) demonstrates a reduction from 10^120 to 10^5 in fine-tuning. When writing this in the paper:

- **Do say:** "The residual fine-tuning is ~10^5, corresponding to specifying N_tot to within approximately 4 e-folds."
- **Do say:** "This is an initial-condition tuning (how long did inflation last?), not a fundamental-constant tuning (why is Lambda_bare small?)."
- **Do NOT say:** "The cosmological constant problem is solved." It is reparametrized, not solved.
- **Emphasize:** The improvement is 115 orders of magnitude, but the viable N_tot range (79-95 e-folds) is fitted, not predicted. The mechanism is moderately tuned, not natural.
- **Note:** The Spearman |rho_s| = 0.996 for N_tot means the other parameters (alpha/M, T_reh, M_GUT) are essentially irrelevant to the vacuum energy scale. The paper should state that the fine-tuning has been concentrated into a single initial condition, not distributed across multiple parameters.

## 2. Dimensional Consistency and Framework Credibility

The equation-by-equation audit (12 equations) provides concrete evidence for the paper's discussion section:

- **10/12 equations are fully dimensionally consistent** -- this can be cited as a systematic verification of the derivation chain from the ECH action through to rho_Lambda.
- **2/12 have noted gaps** -- both are already acknowledged in the manuscript:
  - The parity-odd Lagrangian density (Eq. 7) has mass dimension +1 rather than +4. The paper calls this a "scaling ansatz" requiring on-shell Planck-scale evaluation. This is honest but should be flagged as a limitation in the discussion, not buried.
  - The galaxy spin amplitude A_0 proportionality hides a required energy scale E_eff. This connects to the 9-12 OOM gap acknowledged elsewhere.
- **Manuscript implication:** The dimensional audit strengthens the claim that the derivation chain is internally consistent, while the two noted gaps provide natural places to state open problems.

## 3. Limit Behavior and Paper Claims

All 5 limit checks pass. This supports the following paper claims:

- **"The framework embeds within GR"** -- Torsion -> 0 recovers standard GR (Limit 1). This is the most important limit for referee credibility.
- **"Parity violation is a quantum effect"** -- alpha/M -> 0 removes all parity-violating signatures while preserving the bounce (Limit 2). This establishes that cosmic birefringence and galaxy spin asymmetry are predictions of the quantum correction, not artifacts of the classical theory.
- **"Inflation bridges the 120 orders of magnitude"** -- D_inf -> 1 reproduces the full cosmological constant problem (Limit 3). This is the strongest argument for the mechanism: without inflation, the theory naturally produces Planck-scale vacuum energy.
- **"The BI parameter is essential"** -- gamma -> 0 is singular and gamma -> infinity removes the bounce (Limits 4-5).

Recommend adding a brief paragraph in the discussion section: "The framework reduces to standard GR in all appropriate limits (Table X), ensuring that it modifies gravity only at the scales and regimes where modification is intended."

## 4. Connecting MCMC delta_neff to WP4 Theory Predictions

The two MCMC datasets give:

| Dataset | delta_neff | Interpretation |
|---------|-----------|----------------|
| full_tension | -0.020 +/- 0.16 | Consistent with zero |
| planck_bao_sn | +0.065 +/- 0.19 | Consistent with zero |

**How to connect to theory:**

- The spin-torsion framework predicts a small positive contribution to N_eff from the four-fermion contact interaction (WP4 microphysics). The planck_bao_sn result (+0.065) has the correct sign but is not statistically significant.
- **Do NOT claim:** "The MCMC confirms the model's delta_neff prediction." Both values are consistent with zero at well within 1-sigma.
- **Do claim:** "Current data do not exclude the predicted delta_neff contribution. The framework's prediction lies within the observational uncertainty."
- **Forward-looking:** CMB-S4 sensitivity (~0.03 on N_eff) will be able to test the predicted contribution at the relevant precision. This is a genuine future test.
- The full_tension dataset's slight negative value (-0.020) is a reminder that dataset-dependent systematics dominate at this precision level. Do not over-interpret sign differences between datasets.

## 5. The vacuum_scale_sensitivity Figure

The Monte Carlo scan produces a figure (`vacuum_scale_sensitivity`) showing how rho_Lambda depends on each parameter. This figure should be referenced in the Discussion section of the paper, specifically:

- It visually demonstrates that N_tot is the single controlling parameter (near-vertical correlation band).
- It shows that alpha/M, T_reh, and M_GUT produce horizontal scatter (no correlation with the vacuum energy scale).
- **Suggested placement:** Discussion section, subsection on naturalness/fine-tuning. Caption should note: "100,000-sample Monte Carlo scan. The viable region (shaded) corresponds to N_tot in [79, 95]. Other parameters have negligible impact on the predicted vacuum energy scale."

## 6. What the Monte Carlo Scan Adds Beyond the Paper

The existing paper derives the functional form rho_Lambda = [(alpha/M) * M_Pl] * D_inf * M_Pl^4 and notes that N_tot controls the result. The Monte Carlo scan adds:

1. **Quantitative fine-tuning measure:** 1 in 46 (2.2% of parameter space is viable), compared to 1 in 10^120 for LCDM. This is a publishable number.
2. **Formal sensitivity ranking:** Spearman correlations proving that N_tot dominates (|rho_s| = 0.996) while other parameters are negligible (|rho_s| < 0.08). This goes beyond the qualitative argument in the current draft.
3. **Viable N_tot range:** [79, 95] e-folds, which is physically reasonable (exceeds the minimum ~60 required by the CMB, and below the ~140 that some eternal inflation scenarios produce).
4. **Nature-of-tuning distinction:** The scan makes concrete the claim that residual tuning is initial-condition type, because the only parameter that matters (N_tot) is an initial condition of the inflationary epoch.

These results strengthen the paper's naturalness argument from qualitative to semi-quantitative. Recommend adding a short subsection (or expanding the existing naturalness discussion) with the scan results and the sensitivity figure.
