# planck_bao_sn parameter_summary — Units + Column Diagnosis

**Status (EXT2 P1B F2 closure, 2026-06-10):** the
`Parameter summary:` block at the bottom of `convergence_report.txt`
is **column-permuted** in the same off-by-one extraction class that
EXT1-P1B F1 root-caused for the `full_tension` frozen directory. The
`convergence_report.txt` block is preserved for audit-trail purposes
only; the authoritative parameter values for this dataset combination
are in `parameter_summary_CORRECTED.json` in this directory.

## Symptom

In `convergence_report.txt` the entries read e.g.
`nnu : 0.96644` (which is plainly the spectral index n_s) and
`H0 : 11.93680` (which is plainly logA-class). Cross-checking against
the chain header in `chains/chain_01/spin_torsion.1.txt` shows the
column order is

```
weight minuslogpost  logA  nnu  ns  ombh2  omch2  tau  theta_MC_100
A_planck  amp_143  amp_217  amp_143x217  n_143  n_217  n_143x217
calTE  calEE  As  H0  sigma8  omegam  S8  delta_neff  age  …
```

Compared to that header, the report's "Parameter summary" labels are
shifted by one (the report skipped the `#` header token), so each
quoted statistic is paired with the value of the *next* chain column.

## Resolution

`parameter_summary_CORRECTED.json` was regenerated 2026-06-10 by
directly loading the six chain files

```
chains/chain_0[1-6]/spin_torsion.1.txt
```

dropping the first 30 % of each chain as burn-in (matching the
`burn_fraction = 0.3` used for the `full_tension` frozen directory),
and computing weighted means + standard deviations (the chain weight
sits in column 0). Verifying counts:

| metric | value |
|---|---|
| chains | 6 |
| raw rows (all chains) | 132,949 |
| burn-in fraction | 0.3 (30 %) |
| post-burn-in samples | 93,066 |

The 93,066 figure agrees with the manuscript's "93,064" up to
per-chain integer rounding of the 30 % cut, which matches the
companion note in `convergence_report.txt` (`Post-burnin samples:
106361 [at 20% burn-in; paper reports 93,064 at 30%]`).

## Units

All values in `parameter_summary_CORRECTED.json` are in the same
physical units used in Paper I(b) Tables III–IV:

| key | unit |
|---|---|
| `H0` | km s⁻¹ Mpc⁻¹ |
| `delta_neff` | dimensionless |
| `tau` | dimensionless |
| `sigma8` | dimensionless |
| `omegam` | dimensionless |
| `ns` | dimensionless |
| `S8` | dimensionless |
| `age` | Gyr |

This matches the units schema used for the `full_tension` frozen
directory (`parameter_summary_units_README.md` in the sibling
diagnostics folder).
