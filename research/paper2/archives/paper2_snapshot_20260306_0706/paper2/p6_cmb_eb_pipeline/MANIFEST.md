# P6 CMB EB Pipeline — Run Manifest

## Track
Paper 2, Track D (P6)

## Framing
Literature synthesis + pipeline development for cosmic birefringence.
Tier 1 (required): Citation-verified beta registry with systematic caveats.
Tier 2 (optional): Map-level EB estimator — only if clean pipeline achieved.
We do NOT claim an independent EB detection unless Tier 2 produces
reproducible outputs.

## Run Environment
- Pod: paper2-p6-eb (RunPod, RTX 3070 community)
- Image: runpod/pytorch:2.2.0-py3.10-cuda12.1.1-devel-ubuntu22.04
- Python: 3.10
- Dependencies: numpy, scipy, matplotlib (Tier 1); healpy, NaMaster (Tier 2)

## Datasets Used
| Dataset | Source | Access |
|---------|--------|--------|
| Minami & Komatsu (2020) | arXiv:2011.11254 | Literature |
| Eskilt (2022) | arXiv:2205.13962 | Literature |
| Eskilt et al. (2022) | arXiv:2203.04830 | Literature |
| Zagatti et al. (2025) | arXiv:2502.07654 | Literature |
| Diego-Palazuelos & Komatsu (2025) | arXiv:2509.13654 | Literature |
| SPIDER Collaboration (2025) | arXiv:2510.25489 | Literature |
| Planck PR4/NPIPE maps (Tier 2) | PLA | ESA-PSL, ~13 GB |

## Commands
```bash
# Tier 1 (always works)
python beta_registry.py --output outputs/

# Tier 2 (optional, needs Planck maps)
bash tier2_download_maps.sh
python tier2_eb_estimator.py --data_dir data/ --output_dir outputs/tier2/
```

## Outputs
- outputs/beta_registry.json: Full measurement compilation
- outputs/beta_summary.json: Weighted averages with caveats
- outputs/forest_plot.{pdf,png}: Publication-quality forest plot
- systematics_review.md: Calibration angle, dust, instrumental caveats

## Tier 2 Status
NOT ATTEMPTED in first run. Requires ~13 GB Planck map download +
healpy + NaMaster installation.

## Limitations
- Tier 1 is a literature compilation, not independent analysis
- Weighted average uses stat errors only (systematic errors are correlated)
- The SPIDER combined 7σ uses Planck + ACT data (not fully independent)
- Map-level vs spectrum-level analyses show mild tension (unresolved)
- Tier 2 simplified estimator does NOT include self-calibration method
