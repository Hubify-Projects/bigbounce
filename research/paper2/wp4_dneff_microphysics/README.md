# WP4: Delta-Neff Microphysics

## Objective

Produce explicit post-inflation mechanisms that yield Delta-Neff ~ 0.1-0.2,
with BBN and CMB constraint checks. This work package provides the microphysical
foundation for the effective Delta-Neff measured in Paper 1 MCMC posteriors.

## Success Criteria

At least one mechanism with an allowed parameter region producing
Delta-Neff in the target range 0.10-0.20, consistent with:
- BBN constraints (Yeh+2022: Delta-Neff_BBN < 0.5 at 95% CL)
- CMB constraints (Planck 2018: Neff = 2.99 +/- 0.17 at 68%)
- Paper 1 MCMC posteriors (Delta-Neff ~ 0.14-0.18)

## Models

### Model A: Dark Radiation from Reheating Branching
A fraction Br_dr of the reheating energy density goes into a hidden sector
with g_star_hidden relativistic degrees of freedom. The hidden sector
temperature ratio (T_dr/T_gamma) is set by entropy conservation after
decoupling. Standard Kolb & Turner (1990) thermodynamics.

### Model B: Out-of-Equilibrium Heavy Particle Decay
A heavy particle X (mass m_X, lifetime tau_X) decays with branching
fraction Br_dark into dark radiation. The decay temperature is set by
the Hubble rate matching 1/tau_X. Following Brust et al. (2013).

## Datasets

- Planck 2018 parameters (Aghanim et al. 2020, arXiv:1807.06209)
- BBN constraints (Fields et al. 2020, arXiv:1912.01132; Yeh et al. 2022, arXiv:2204.11297)
- Paper 1 MCMC posteriors (BigBounce v1.2.0, pending convergence)

## Outputs

- Delta-Neff contour figures (PDF + PNG at 300 dpi)
- Constraint overlap plots showing allowed parameter regions
- Parameter tables with best-fit values
- 1-2 page writeup summarizing viable mechanisms

## Usage

### Requirements

```bash
pip install -r requirements.txt
```

### Run Parameter Scans

```bash
# Reheating model scan
python scan.py --model reheating --output runs/RUN_ID/

# Decay model scan
python scan.py --model decay --output runs/RUN_ID/

# Both models
python scan.py --model reheating --output runs/reheat_001/
python scan.py --model decay --output runs/decay_001/
```

### Generate Figures

```bash
# From reheating scan results
python plots.py --input runs/reheat_001/ --output figures/

# From decay scan results
python plots.py --input runs/decay_001/ --output figures/

# Comparison plot (needs both)
python plots.py --input runs/reheat_001/ --input-decay runs/decay_001/ --output figures/
```

## File Structure

```
wp4_dneff_microphysics/
  README.md              -- this file
  requirements.txt       -- Python dependencies
  dneff_models.py        -- Model A (reheating) and Model B (decay) classes
  scan.py                -- Parameter scan driver
  plots.py               -- Publication-quality figure generation
  constraints.md         -- Constraint sources with full citations
  runs/                  -- Scan output directories (gitignored)
  figures/               -- Generated figures
```

## References

- Kolb & Turner, "The Early Universe" (1990), Ch. 3-5
- Brust, Kaplan, Walters & Zurek (2013), arXiv:1303.5379
- Yeh, Shelton, Olive & Fields (2022), arXiv:2204.11297
- Fields, Olive, Yeh & Young (2020), arXiv:1912.01132
- Planck 2018 VI: Aghanim et al. (2020), arXiv:1807.06209
