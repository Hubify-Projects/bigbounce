# WP5 Spin Amplitude Derivation — Run Manifest

## Track
Paper 2, Track B (WP5)

## Framing
Phenomenological parity-odd tidal torque mapping: A₀ as a function of ε_PO.
This is a scaling estimate, NOT a torsion derivation. The required ε_PO to
match A₀ ~ 0.003 is the main result.

## Run Environment
- Pod: paper2-wp5-spin (RunPod, RTX 3070 community)
- Image: runpod/pytorch:2.2.0-py3.10-cuda12.1.1-devel-ubuntu22.04
- Python: 3.10
- Dependencies: numpy, scipy, matplotlib (see requirements.txt)

## Datasets Used
| Dataset | Source | Access |
|---------|--------|--------|
| Galaxy spin counts (Shamir 2024) | arXiv:2401.09450 | Reconstructed from tables |
| TTT parameters (Porciani+2002) | MNRAS 332, 325 | Literature |

## Commands
```bash
python monte_carlo_sensitivity.py --n_samples 100000 --output runs/mc_001/
```

## Outputs
- runs/mc_001/: MC samples CSV, summary statistics, 3 figures

## Key Result
A₀ ~ ε_PO × 0.015 (for standard TTT parameters)
For A₀ = 0.003: ε_PO ~ 0.2 (median), with uncertainty from MC sampling.

## Limitations
- Phenomenological extension to TTT, not derived from a specific Lagrangian
- The ε_PO coupling is postulated, not calculated from torsion dynamics
- Standard TTT parameters (λ_mean, σ_lnλ, δ_rms) have scatter from simulations
- Galaxy spin CW/CCW asymmetry itself is contested (Patel & Desmond 2024 find null)
- The mapping assumes a simple dipolar pattern; higher multipoles are ignored
