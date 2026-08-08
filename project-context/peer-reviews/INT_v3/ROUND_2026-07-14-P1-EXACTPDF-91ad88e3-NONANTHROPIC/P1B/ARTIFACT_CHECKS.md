# P1B exact-commit artifact checks

All checks below use objects from commit `91ad88e36121da128175415f55be44d5e458f9f1`, not the moving worktree.

## Prior-predictive fractions

`reproducibility/cosmology/alp_prior_predictive_result.json` records, for 100,000 draws per configuration and zero failed draws:

- fixed `C_agamma=8`: within-one-sigma fraction `0.11597` (11.597%); within two sigma `0.23867`;
- broad `C_agamma~U[4,60]`: within-one-sigma fraction `0.06137` (6.137%); within two sigma `0.12601`;
- maximum fast/reference-integrator disagreement `2.4935757014787896e-08 deg`.

The companion script declares the exact priors, deterministic RNG, observed band, ODE forward model, and count. This verifies the abstract's rounded 11.6% and 6.1% values. The rendered manuscript would still benefit from consolidating this protocol and output path in one paragraph.

## Spectator-subset fractions

The four exact `c5_continuous/c5.[1-4].txt` chains contain 8,955 rows and total Monte Carlo weight 82,754. Direct weighted integration of the committed `Omega_a` column gives:

| Cut | Raw rows | Weighted mass |
|---|---:|---:|
| `Omega_a < 0.1` | 4,286 | 0.4404741765 |
| `Omega_a < 0.01` | 1,099 | 0.1338183049 |
| `theta_i <= 0.1` | 42 | 0.0032747662 |

These reproduce the paper's rounded 44%, 13%, and 0.33%. The last value is independently frozen in `c10a_spectator_slice.json`. The larger two cuts are recomputable from the public chains but lack their own compact committed result JSON; that is a bounded provenance improvement, not evidence against the values.

The likelihood treats the ALP as a fixed-background spectator throughout and does not feed `Omega_a` back into the background. Therefore the `<0.01` subset can be used conditionally, but the 13.3818% ratio to the full surrogate chain is not a physical posterior probability: much of its denominator violates the likelihood's spectator approximation.

## Table IV beta and ESS audit

Direct exact-chain summaries are:

| Selection | Weighted mean | Weighted std | Weighted median | Paper |
|---|---:|---:|---:|---:|
| full | 0.32629 | 0.09899 | 0.33028 | 0.326 +/- 0.099 |
| `Omega_a<0.1` | 0.31471 | 0.10258 | 0.31909 | 0.328 +/- 0.100 |
| `Omega_a<0.01` | 0.27595 | 0.09880 | 0.28409 | 0.28 +/- 0.10 |

The middle row is stale/mixed. The caption also calls beta entries medians while the full value is the mean. A weight-expanded Sokal-style calculation gives roughly full beta/theta ESS 2937/812, `<0.1` beta ESS 1530 (but `w_a` about 1935), and `<0.01` beta ESS 491. The manuscript's 1989/461 values therefore mix unidentified markers/estimators; no committed script generates them.

## NaMaster bandpower-template audit

The recovered spectrum is a decoupled broad-bandpower vector. The fit template is formed by sampling the unbinned `C_ell^EE` array at each effective bin center rather than applying the identical NaMaster bandpower/window operator. This is not an optional alternative-binning request: it is an implementation mismatch capable of producing multiplicative recovery bias. A corrected rerun is required before attributing the ~12% bias or carrying 0.040 degrees as a pipeline floor.

## Figure 2 label

Visual inspection of exact rendered page 7 shows panel (a)'s horizontal axis labeled `Delta N_eff`; the caption uses the same symbol. The OpenAI claim that it is labeled `N_eff` is a raster/PDF-extraction error.

## Estimator normalization

Exact rendered page 7 and source lines 2152–2163 use

`C_b^EB = (1/2) sin(4 beta) C_b^EE`

in the negligible-`BB` template limit and identify it with `sin(2 beta) cos(2 beta)`. The Gemini `1/4` complaint is stale or misread.

## Frozen snapshot mismatch

At commit `b22f8cc9`, `paper1b_mcmc_companion.tex` declares v1B.0.47. The exact reviewed source at `91ad88e3` declares v1B.0.105, yet its Data Availability and claims table still call `b22f8cc9` the current matching snapshot. That provenance statement is false and must be repaired.

## Sample-count reconciliation

Frozen source lines 1790–1805 explicitly distinguishes:

- 309,189 total raw accepted samples across two frozen combinations;
- 216,432 nominal 30%-burn-in total;
- 123,368 nominal full-tension 30%-burn-in count;
- 123,129 actual chain-end-truncated count;
- 119,617 GetDist weight-thinned count used in Figure 1.

The apparent count contradiction is therefore already reconciled in the paper.
