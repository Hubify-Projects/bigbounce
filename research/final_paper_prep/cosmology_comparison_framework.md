# Cosmology Comparison Framework — Paper 1

**Created:** 2026-03-11
**Status:** Structure ready; fill in values as datasets freeze

---

## Master Comparison Table

This table will become the central results table in the paper (likely Table 2 or 3).

| Parameter | full_tension | planck_bao_sn | planck_only | planck_bao | LCDM reference |
|-----------|-------------|---------------|-------------|------------|---------------|
| H0 [km/s/Mpc] | 67.68 +/- 1.06 | _pending_ | _pending_ | _pending_ | 67.36 +/- 0.54 (Planck 2018) |
| Delta_Neff | -0.019 +/- 0.169 | _pending_ | _pending_ | _pending_ | 0 (SM) |
| N_eff | 3.027 +/- 0.169 | _pending_ | _pending_ | _pending_ | 3.046 (SM) |
| tau | 0.054 +/- 0.007 | _pending_ | _pending_ | _pending_ | 0.054 +/- 0.007 (Planck 2018) |
| sigma8 | 0.803 +/- 0.008 | _pending_ | _pending_ | _pending_ | 0.811 +/- 0.006 (Planck 2018) |
| Omega_m | 0.308 +/- 0.005 | _pending_ | _pending_ | _pending_ | 0.315 +/- 0.007 (Planck 2018) |
| n_s | 0.965 +/- 0.006 | _pending_ | _pending_ | _pending_ | 0.965 +/- 0.004 (Planck 2018) |
| S8 | 0.814 +/- 0.008 | _pending_ | _pending_ | _pending_ | 0.832 +/- 0.013 (Planck 2018) |
| Age [Gyr] | 13.82 +/- 0.17 | _pending_ | _pending_ | _pending_ | 13.80 +/- 0.02 (Planck 2018) |
| Convergence | FROZEN (9/9 pass) | RUNNING | PAUSED | PAUSED | — |

## Dataset Definitions

### full_tension (ANCHOR — FROZEN)
- Planck NPIPE (TTTEEE + lowT + lowE + lensing) + BAO DR16 + Pantheon+ SN + Riess 2020 H0 + DES S8
- Maximum constraining power, includes both early and late-universe probes
- Includes the H0 and S8 priors that create "tension" pulls
- **Role:** Anchor result, most constrained Delta_Neff measurement

### planck_bao_sn (RUNNING)
- Planck NPIPE + BAO DR16 + Pantheon+ SN
- Drops the Riess H0 prior and DES S8 prior
- **Role:** Shows impact of removing the H0 and S8 tension anchors
- Expected: slightly wider Delta_Neff posterior, possibly shifted mean

### planck_only (PAUSED)
- Planck NPIPE only (TTTEEE + lowT + lowE + lensing)
- No BAO, no SN, no external priors
- **Role:** Pure CMB constraint on Delta_Neff
- Expected: wider Delta_Neff constraints, different degeneracy directions

### planck_bao (PAUSED — optional)
- Planck NPIPE + BAO DR16
- Adds geometric distance constraints but no luminosity/H0 priors
- **Role:** Intermediate between planck_only and planck_bao_sn
- Expected: tighter than planck_only but without SN pull

## Planned Figures

### Figure N: Triangle/Corner Plot Comparison
- Overlay posteriors from full_tension + planck_bao_sn + planck_only
- Focus on H0 vs Delta_Neff plane to show how different datasets constrain the degeneracy
- Use different colors per dataset
- **Script:** To be created after all datasets frozen
- **Output:** `paper/figures/multi_dataset_triangle.pdf`

### Figure N+1: Delta_Neff Posterior Comparison
- 1D posteriors of Delta_Neff from all datasets overlaid
- Mark SM value (Delta_Neff = 0) and any preferred ranges
- **Output:** `paper/figures/dneff_posterior_comparison.pdf`

### Figure N+2: H0-Delta_Neff Degeneracy
- 2D contour plot (68% and 95%) in H0 vs Delta_Neff plane
- All datasets overlaid
- Mark Planck LCDM H0 and SH0ES H0 bands
- **Output:** `paper/figures/h0_dneff_degeneracy.pdf`

### Figure N+3: Delta_Neff Physical Viability (Centerpiece)
- Panel A: Delta_Neff posteriors from MCMC
- Panel B: External constraints (BBN, CMB, ACT)
- Panel C: WP4 mechanism viability region
- **Output:** `paper/figures/fig_dneff_viability.pdf` (replaces draft)

## Planned Tables

### Table: MCMC Results Summary
- All parameters from all datasets
- Compare to Planck 2018 LCDM baseline
- Include convergence status per dataset
- **Template:** The master comparison table above

### Table: Model Comparison
- LCDM + Delta_Neff vs pure LCDM
- Delta chi-squared
- Bayesian evidence if computable
- **Requires:** LCDM control chains (not yet started)

## Supporting Text Updates Needed (after all freezes)

1. **Results section:** Quote full_tension values; discuss consistency with Planck LCDM
2. **Discussion:** Interpret Delta_Neff ~ 0 in context of spin-torsion predictions
3. **Dataset comparison:** Note any shifts between full_tension and planck_bao_sn
4. **H0 tension:** Discuss whether Delta_Neff helps or doesn't help resolve it
5. **S8 tension:** Note S8 = 0.814 compromise value

## Phased Schedule

| Phase | Dataset | Status | Expected Freeze |
|-------|---------|--------|----------------|
| 1 | full_tension | **FROZEN** | Done (2026-03-11) |
| 2 | planck_bao_sn | RUNNING | ~2026-03-12 14:00 UTC |
| 3 | planck_only | PAUSED | ~2026-03-14 (after planck_bao_sn) |
| 3 | planck_bao | PAUSED | ~2026-03-15 (with planck_only) |
| 4 | Manuscript edits | NOT STARTED | After Phase 3 |
