# P6 CMB EB Birefringence Pipeline

**BigBounce Paper 2 — Track D: Cosmic Birefringence from CMB EB Correlations**

## Objective

Compile a citation-verified registry of published cosmic birefringence (beta)
measurements and produce a defensible meta-analysis with systematic caveats.
Optionally, if Planck PR4 maps are available, run an independent map-level
EB estimator as a cross-check.

This is a literature-synthesis and pipeline-development project. We do NOT
claim an independent EB detection unless Tier 2 produces reproducible outputs.

## Two-Tier Structure

### Tier 1 (Required)

- Literature beta registry: all published isotropic beta measurements with
  full provenance (instrument, method, frequency, statistical + systematic errors)
- Inverse-variance weighted average with chi-squared consistency test
- Forest plot (publication-quality)
- Systematic caveats writeup: calibration-angle degeneracy, Galactic dust EB,
  instrumental leakage, frequency dependence as diagnostic

### Tier 2 (Optional — only if clean pipeline achieved)

- Download Planck PR4 (NPIPE) frequency maps from Planck Legacy Archive
- Compute EB cross-spectra with HEALPix/NaMaster
- Estimate beta via D_l^EB / D_l^EE rotation formula
- Apply Galactic masks and null tests (A-B detector split)
- Compare with Tier 1 literature values

**Tier 2 status: NOT ATTEMPTED in first run. Requires ~13 GB map data + healpy + NaMaster.**

## Success Criteria

| Deliverable             | Target                                           |
|-------------------------|--------------------------------------------------|
| Beta registry           | >= 5 independent measurements with full citations |
| Weighted average        | Consistent with published values (0.2-0.4 deg)   |
| Forest plot             | Publication-quality, PDF + PNG                    |
| Systematics writeup     | >= 3 systematic effects discussed with references |
| Tier 2 (if attempted)   | Reproducible EB spectrum from >= 2 frequency channels |

## Datasets

- **Tier 1**: Published beta values from literature (no downloads needed)
  - Minami & Komatsu (2020): Planck 2018, arXiv:2011.11254
  - Eskilt (2022): Planck PR4, arXiv:2205.13962
  - Diego-Palazuelos & Komatsu (2025): ACT DR6, arXiv:2509.13654
  - Zagatti et al. (2025): Planck PR4 map-space, arXiv:2502.07654
  - SPIDER Collaboration (2025): Combined 7sigma, arXiv:2510.25489
- **Tier 2**: Planck PR4/NPIPE maps from PLA (see dataset_registry.csv)

## Pipeline

```
beta_registry.py           -->  outputs/{beta_registry.json, forest_plot.pdf}
systematics_review.md      -->  (standalone writeup)
tier2_eb_estimator.py      -->  outputs/{eb_spectra.json, beta_estimate.json}  [optional]
tier2_download_maps.sh     -->  data/planck_pr4/  [optional, ~13 GB]
```

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run Tier 1 (always works, no external data needed)
python beta_registry.py --output outputs/

# Run full pipeline including Tier 2 (needs Planck maps + healpy)
bash reproduce_pipeline.sh
```

## File Manifest

| File                      | Purpose                                              |
|---------------------------|------------------------------------------------------|
| `README.md`               | This file                                            |
| `beta_registry.py`        | Tier 1: literature beta compilation + forest plot    |
| `systematics_review.md`   | Calibration angle, dust, instrumental systematics    |
| `tier2_eb_estimator.py`   | Tier 2: map-level EB estimator (optional)            |
| `tier2_download_maps.sh`  | Download Planck PR4 maps from PLA (optional)         |
| `requirements.txt`        | Python dependencies                                  |
| `reproduce_pipeline.sh`   | One-command reproducible pipeline                    |

## References

- Minami & Komatsu (2020), PRL 125, 221301, arXiv:2011.11254
- Eskilt (2022), A&A 662, A10, arXiv:2205.13962
- Eskilt et al. (2022), PRD 106, 063503, arXiv:2203.04830
- Zagatti et al. (2025), arXiv:2502.07654
- Diego-Palazuelos & Komatsu (2025), arXiv:2509.13654
- SPIDER Collaboration (2025), arXiv:2510.25489
