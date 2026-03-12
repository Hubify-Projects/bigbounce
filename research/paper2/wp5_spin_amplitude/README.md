# WP5: Spin Amplitude Derivation

## Objective

Produce a defensible first-principles-ish scaling estimate for the galaxy spin dipole
amplitude A_0 from a parity-odd tidal torque correction, plus a conservative upper bound.

## Success Criteria

- A_0(epsilon_PO) scaling relationship with uncertainty bands
- Required epsilon_PO range for A_0 ~ 0.003 (the observed value from Shamir 2024)

## Datasets

- Paper 1 CW/CCW counts (Shamir 2024)
- Standard TTT references: White (1984), Porciani, Dekel & Hoffman (2002)
- Halo formation parameters from N-body simulation literature

## Key Result

A_0 ~ epsilon_PO * (2/3) * lambda / delta_rms * <|cos theta|>
    ~ epsilon_PO * (2/3) * 0.035 * (2/pi)
    ~ epsilon_PO * 0.015

For A_0 = 0.003: epsilon_PO ~ 0.2 (a ~20% parity-odd correction to TTT).

## File Structure

| File                        | Description                                          |
|-----------------------------|------------------------------------------------------|
| `ttt_baseline.py`           | Standard Tidal Torque Theory baseline                |
| `parity_bias_model.py`      | Parity-odd bias extension: A_0(epsilon_PO)           |
| `monte_carlo_sensitivity.py`| Monte Carlo sensitivity analysis (argparse CLI)      |
| `writeup.md`                | Technical note (1-2 pages)                           |
| `requirements.txt`          | Python dependencies                                  |
| `runs/`                     | Output directory for MC runs                         |

## Commands

```bash
# Run full Monte Carlo sensitivity analysis
python monte_carlo_sensitivity.py --n_samples 100000 --output runs/RUN_ID/

# Quick test run
python monte_carlo_sensitivity.py --n_samples 1000 --output runs/test/

# Individual module tests
python ttt_baseline.py
python parity_bias_model.py
```

## Dependencies

```
numpy
scipy
matplotlib
```

Install: `pip install -r requirements.txt`

## References

- White, S. D. M. (1984). Angular momentum growth in protogalaxies. ApJ, 286, 38.
- Porciani, C., Dekel, A., & Hoffman, Y. (2002). Testing tidal-torque theory.
  I. Spin amplitude and direction. MNRAS, 332, 325.
- Shamir, L. (2024). Asymmetry between galaxy spin directions.
- Philcox, O. & Ereza, J. (2022). Testing parity symmetry with BOSS.
- Patel, P. & Desmond, H. (2024). Tests of isotropy with galaxy surveys.
