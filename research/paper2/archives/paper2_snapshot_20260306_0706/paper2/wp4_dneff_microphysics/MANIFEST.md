# WP4 ΔNeff Microphysics — Run Manifest

## Track
Paper 2, Track A (WP4)

## Framing
Candidate microphysics realizations of ΔNeff ~ 0.1-0.2 from post-inflation physics.
These are allowed parameter regions and benchmark mechanisms, NOT first-principles
derivations from the bounce.

## Run Environment
- Pod: paper2-wp4-dneff (RunPod, RTX 3070 community)
- Image: runpod/pytorch:2.2.0-py3.10-cuda12.1.1-devel-ubuntu22.04
- Python: 3.10
- Dependencies: numpy, scipy, matplotlib (see requirements.txt)

## Datasets Used
| Dataset | Source | Access |
|---------|--------|--------|
| Planck 2018 parameters | arXiv:1807.06209 | Literature (no download) |
| BBN constraints (Yeh+2022) | arXiv:2204.11297 | Literature |
| BBN update (Burns+2024) | arXiv:2401.15054 | Literature |
| Paper 1 MCMC posteriors | Internal (RunPod) | NOT PUBLIC |

## Commands
```bash
python scan.py --model reheating --output runs/reheat_001/
python scan.py --model decay --output runs/decay_001/
python plots.py --input runs/reheat_001/ --output figures/
python plots.py --input runs/decay_001/ --output figures/
```

## Outputs
- runs/reheat_001/: scan_results.csv, summary.json, .npy grids
- runs/decay_001/: scan_results.csv, summary.json, .npy grids
- figures/: 4 publication figures (PDF + PNG)

## Limitations
- Toy models, not full quantum field theory calculations
- Reheating model assumes instantaneous thermalization
- Decay model uses simplified Hubble rate matching for decay temperature
- Parameter regions are necessary conditions, not sufficient for a complete model
- Connection to bounce physics provides theoretical motivation only
