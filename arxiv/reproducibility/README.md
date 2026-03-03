# Reproducibility Materials

**Paper:** Geometric Dark Energy from Spin-Torsion Cosmology (Golden 2026)
**Version:** v0.7.0

## Contents

- `cobaya_config.yaml` — Complete Cobaya v3.3 configuration
- `camb_modifications.diff` — Patch for CAMB v1.5 theory module
- `params_bestfit.ini` — Best-fit parameters with 68% CI

## Requirements

- Python 3.9+
- Cobaya v3.3 (`pip install cobaya==3.3`)
- CAMB v1.5 (`pip install camb==1.5`)
- PolyChord (for nested sampling / Bayesian evidence)

## Quick Start

1. Install Cobaya and CAMB:
   ```bash
   pip install cobaya==3.3 camb==1.5
   cobaya-install cosmo -p /path/to/packages
   ```

2. Apply the CAMB modifications:
   ```bash
   cd /path/to/packages/code/CAMB
   git apply /path/to/camb_modifications.diff
   ```

3. Run the MCMC:
   ```bash
   cobaya-run cobaya_config.yaml
   ```

4. Convergence is monitored via the Gelman-Rubin diagnostic (R-1 < 0.01).

## Notes

- The CAMB patch adds: (i) an early dark energy component Lambda_eff(z) following the spin-torsion dilution history, and (ii) modified perturbation initial conditions reflecting the bounce epoch.
- MCMC chain files and full convergence diagnostics will be released in a companion data package.
- Contact: houston@hubify.com
