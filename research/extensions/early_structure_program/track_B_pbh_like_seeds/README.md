# Track B: PBH Constraint Overlay

## Scope

Forward-model analysis overlaying primordial black hole (PBH) observational
constraints with the SMBH seed mass window. This identifies where in PBH
parameter space seeds for high-z SMBHs could form without violating existing
bounds.

Two scripts:
1. **pbh_constraint_overlay.py** -- Plots approximate upper limits on the PBH
   dark matter fraction f_PBH(M) from six major constraint channels, with the
   SMBH seed window highlighted.
2. **pk_to_fpbh.py** -- Maps primordial power spectrum enhancements P(k)
   through the Press-Schechter collapse fraction to f_PBH, showing the
   required amplitude A_bump to produce various PBH abundances.

Constraint curves are ILLUSTRATIVE (approximate piecewise/power-law fits to
published bounds), not exact digitizations.

## Inputs

All constraint boundaries and cosmological parameters are hardcoded from
the literature.

## Outputs

Saved to `outputs/`:
- `pbh_constraint_overlay.pdf` -- f_PBH upper limits with SMBH seed window
- `pk_to_fpbh_mapping.pdf` -- Required A_bump vs M_PBH

## How to Run

```bash
pip install -r requirements.txt
python scripts/pbh_constraint_overlay.py
python scripts/pk_to_fpbh.py
```
