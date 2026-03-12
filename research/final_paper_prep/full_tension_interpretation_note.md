# full_tension Interpretation Note

**Date:** 2026-03-11
**Status:** Preliminary — do NOT edit manuscript yet

---

## What This Result Is

The full_tension dataset combines all available cosmological probes:
- **CMB:** Planck NPIPE high-ell (CamSpec TTTEEE) + 2018 low-ell TT + low-ell EE + lensing
- **BAO:** SDSS DR16 (LRG, Lya auto, Lya x QSO, QSO, MGS) + 6dF 2011
- **Supernovae:** Pantheon+
- **Local H0:** Riess 2020 (Mb prior)
- **Large-scale structure:** DES S8

This is the "kitchen sink" combination — maximum constraining power. It serves as the **anchor result** for Paper 1.

## Parameter Interpretation Caveats

**IMPORTANT:** The parameter values reported from the chains use Cobaya's internal parameterization, which may differ from standard cosmological conventions. Before quoting any values in the paper:

1. **H0:** The chain reports `H0 = 0.8035 +/- 0.0084`. Verify whether this is H0 in km/s/Mpc or H0/100. If the latter, then H0 = 80.35 +/- 0.84 km/s/Mpc.

2. **delta_neff / nnu:** The chain reports `nnu = 13.82 +/- 0.17`. Standard Neff = 3.044 for the SM. The `nnu` parameter in the Cobaya config may be mapped differently depending on the theory code setup. Check the YAML config for the exact definition. Delta_Neff = nnu - 3.044 only if nnu is literally Neff.

3. **tau:** The chain reports `tau = 1.04092 +/- 0.00038`. Standard tau (optical depth to reionization) is typically ~0.054 +/- 0.007. The value 1.04 suggests this may be theta_MC_100 or another scaled parameter mislabeled, OR the model's spin-torsion modifications genuinely shift tau. **Must verify against the Cobaya config.**

4. **ns:** The chain reports `ns = 0.02227 +/- 0.00016`. Standard ns ~ 0.965. This value (0.022) is far from standard, suggesting it may be a derived or rescaled parameter. **Must verify.**

5. **omegam:** `omegam = 0.814 +/- 0.009`. Standard Omega_m ~ 0.315. This high value may reflect the model's modified expansion history or a different parameterization. **Must verify.**

## What to Verify Before Paper Edits

1. Cross-reference every parameter name against the Cobaya YAML config (`cobaya_config.yaml` in each chain directory)
2. Check the `params:` block for any `renames`, `derived`, or scaling definitions
3. Verify units by comparing one chain point against a manual CAMB call
4. Confirm that "delta_neff" as reported corresponds to Delta_Neff as defined in the paper
5. Run getdist with proper .paramnames file for correct labels

## Comparison to Previous Runs

The GPU run (snapshot 20260305_0824) and previous CPU runs were terminated before convergence. This is the first fully converged result. Previous runs can be used as consistency checks but not as primary results.

## Next Steps (do NOT execute yet)

1. Map chain parameters to paper parameters
2. Generate publication-quality figures with correct axis labels and units
3. Update Table 2 (or equivalent) in the manuscript
4. Write the Results section text
5. Wait for planck_bao_sn, planck_only, planck_bao to freeze for the comparison table
