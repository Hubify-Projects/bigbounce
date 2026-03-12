# full_tension Physical Parameters (CORRECTED)

**Frozen:** 2026-03-11 17:28 UTC
**Extracted:** 2026-03-11T17:58:04.587498+00:00
**Column mapping:** Validated (off-by-one bug fixed)

## Paper-Ready Values

| Parameter | Mean | Std (68%) | 68% CI | Unit | R-1 | ESS |
|-----------|------|-----------|--------|------|-----|-----|
| H0 | 67.684019 | 1.060648 | [66.6311, 68.7509] | km/s/Mpc | 0.0006 | 5078 |
| delta_neff | -0.019594 | 0.169207 | [-0.1879, 0.1485] | dimensionless | 0.0006 | 4744 |
| tau | 0.053592 | 0.006957 | [0.0469, 0.0604] | dimensionless | 0.0010 | 6507 |
| sigma8 | 0.803395 | 0.008400 | [0.7950, 0.8119] | dimensionless | 0.0008 | 5531 |
| omegam | 0.308090 | 0.005456 | [0.3027, 0.3136] | dimensionless | 0.0006 | 6227 |
| ns | 0.965482 | 0.006184 | [0.9593, 0.9716] | dimensionless | 0.0010 | 5624 |
| S8 | 0.814091 | 0.008456 | [0.8056, 0.8225] | dimensionless | 0.0004 | 6697 |
| nnu | 3.026406 | 0.169207 | [2.8581, 3.1945] | dimensionless | 0.0006 | 4744 |
| ombh2 | 0.022264 | 0.000156 | [0.0221, 0.0224] | dimensionless | 0.0001 | 6432 |
| omch2 | 0.118215 | 0.002754 | [0.1155, 0.1210] | dimensionless | 0.0005 | 4706 |
| logA | 3.036367 | 0.014656 | [3.0219, 3.0508] | dimensionless | 0.0007 | 6229 |
| age | 13.822290 | 0.166896 | [13.6559, 13.9884] | Gyr | 0.0006 | 4852 |

## Key Results for Paper

- **H0 = 67.68 +/- 1.06 km/s/Mpc** (consistent with Planck LCDM; Hubble tension not resolved by Delta_Neff alone)
- **Delta_Neff = -0.020 +/- 0.169** (consistent with zero; SM N_eff = 3.046)
- **tau = 0.0536 +/- 0.0070** (consistent with Planck 2018)
- **sigma8 = 0.8034 +/- 0.0084** (standard)
- **Omega_m = 0.3081 +/- 0.0055** (consistent with Planck LCDM)
- **S8 = 0.8141 +/- 0.0085** (compromise between Planck and DES)

## Convergence (all 9/9 gates PASS)

| Metric | H0 | delta_neff | tau |
|--------|-----|------------|-----|
| R-1 | 0.0006 | 0.0006 | 0.0010 |
| ESS | 5078 | 4744 | 6507 |

## Source

- Frozen pack: reproducibility/cosmology/frozen/full_tension_20260311_1728/
- Extraction script: research/final_paper_prep/extract_physical_parameters.py
- Raw JSON: research/final_paper_prep/full_tension_physical_parameters.json
