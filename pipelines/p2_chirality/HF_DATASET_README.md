---
license: cc-by-4.0
language:
- en
pretty_name: "DESI Legacy Galaxy Chirality Catalog (8.47M)"
size_categories:
- 1M<n<10M
task_categories:
- image-classification
- tabular-classification
tags:
- astronomy
- cosmology
- galaxy-morphology
- spin-direction
- chirality
- desi-legacy
- vit
- group-equivariance
- isotropy
- cosmological-principle
configs:
- config_name: catalog_c_production
  data_files:
  - split: catalog_c
    path: "catalog_c_production.parquet"
- config_name: catalog_c_high_confidence_spiral
  data_files:
  - split: hc_spiral
    path: "catalog_c_hc_spiral_p_cw_gt_0p6.parquet"
- config_name: dipole_results
  data_files:
  - split: dipole
    path: "dipole_catalog_c.json"
---

# DESI Legacy Galaxy Chirality Catalog (Paper 4 v1.0)

**Companion data release for** _"Constraints on the Cosmological-Principle Spin-Direction Dipole from 8.47M DESI Legacy Galaxies: A Null Result with Quantified Mask-Coupling Floor"_ (Golden 2026, arXiv:2526.XXXXX).

**Headline result.** A null dipole detection at the cosmological-principle test wavelength after MASTER mode-coupling deconvolution: canonical-N (N_spiral = 3,201,160, f_sky = 0.491) $\ell=1$ direct-MC significance = **+1.85σ** (not detected; consistent with the mask-coupling leakage floor). The +5.88σ pre-MASTER pseudo-$C_1$ excess is shown to be ~70% removed by MASTER decoupling, with the residual +1.85σ identified as the irreducible mask-coupling leakage floor under the patchy DESI Legacy footprint, NOT a detected cosmological dipole.

## Quick links

- **Paper PDF (v1.0):** https://github.com/Hubify-Projects/bigbounce/releases/download/paper4-v1.0/chirality_catalog_paper.pdf
- **Source LaTeX + canonical pipeline:** https://github.com/Hubify-Projects/bigbounce/tree/main/pipelines/p2_chirality
- **Zenodo DOI (release-pinned snapshot):** _minted via GitHub-Zenodo webhook on the_ [`paper4-v1.0` _release_](https://github.com/Hubify-Projects/bigbounce/releases/tag/paper4-v1.0)
- **One-shot reproduction:** `bash pipelines/p2_chirality/reproduce_paper4.sh`

## Schema

### `catalog_c_production.parquet` (8,470,332 rows)

Production catalog with all DESI Legacy galaxies that passed the chirality-pipeline quality gates. Includes both spirals (CW/CCW) and non-spirals (NS).

| Column | Type | Description |
|---|---|---|
| `objid` | int64 | DESI Legacy Survey DR8 object ID (Tractor catalog) |
| `ra` | float64 | Right ascension, J2000 (decimal degrees, 0–360) |
| `dec` | float64 | Declination, J2000 (decimal degrees, −90 to +90) |
| `mag_r` | float32 | DESI Legacy DR8 SDSS-r-band Tractor magnitude |
| `redshift` | float32 | Photometric redshift (if available; NaN otherwise) |
| `imaging_leg` | category | One of `{BASS+MzLS, DECaLS, DES}` — per-imaging-leg assignment from the per-leg systematics audit |
| `class_eq` | category | Equivariant-TTA argmax class: `{CW, CCW, NS}` |
| `p_cw_eq` | float32 | Z2-flip-equivariant ViT-Small posterior probability of clockwise spin |
| `p_ccw_eq` | float32 | Z2-flip-equivariant ViT-Small posterior probability of counter-clockwise spin |
| `p_ns_eq` | float32 | Z2-flip-equivariant ViT-Small posterior probability of non-spiral |
| `axial_ratio_ba` | float32 | Tractor b/a axial ratio (b/a → 1 = face-on, b/a → 0 = edge-on) |
| `psf_e1` | float32 | PSF ellipticity component 1 at the source location (Tractor/legacypipe) |
| `psf_e2` | float32 | PSF ellipticity component 2 at the source location |
| `image_url` | string | DESI Legacy Sky Viewer cutout URL (256x256 jpg cutout, layer=ls-dr8, pixscale=0.262) |

### `catalog_c_hc_spiral_p_cw_gt_0p6.parquet` (subset; 2,107,494 rows)

High-confidence-spiral subsample used for the face-on robustness check (HC-spiral cut: $\max(p_{\rm CW}, p_{\rm CCW}) > 0.6$). Same schema as above.

### `dipole_catalog_c.json`

Headline dipole / multipole numbers from the canonical pipeline. Schema (see `chirality_catalog_paper.tex` §VI and §IV.E for full definitions):

```json
{
  "version": "v1.0.69",
  "config": {"N_spiral": 3201160, "f_sky": 0.4938, "nside": 64, "lmax": 191, "N_MC": 500},
  "global_cw_fraction": 0.49982,
  "dipole_l1": {"C1_decoupled": 2.298e-05, "null_mean": 8.00e-06, "null_std": 8.10e-06, "sigma_canonical_direct": 1.850},
  "monopole_mask_leakage_null": {
    "pre_master_pseudo_C1_sigma_vs_monopole_null": 5.88,
    "post_master_canonical_sigma": 1.85,
    "post_master_subsample_sigma": -0.12,
    "hemisphere_maxabs_dipole_amplitude_sigma": 6.62,
    "interpretation": "Pre-MASTER excess +5.88sigma is mask+monopole leakage; MASTER decoupling removes ~70%; residual +1.85sigma is the irreducible leakage floor."
  },
  "per_imaging_leg": {
    "BASS+MzLS": {"N": 934551, "delta_cw_pct": 0.178, "dipole_sigma": 1.08, "p_value": 0.137},
    "DECaLS":    {"N": 1413958, "delta_cw_pct": -0.21, "dipole_sigma": -1.63, "p_value": 0.974},
    "DES":       {"N": 852651, "delta_cw_pct": 0.094, "dipole_sigma": 0.66, "p_value": 0.247}
  },
  "face_on_robustness": {
    "catalog_c_full": {"N_spirals": 3201160, "dipole_sigma": 4.31, "p_value": 0.001},
    "hc_spiral_p_gt_0p6": {"N_spirals": 2107494, "dipole_sigma": 0.62, "p_value": 0.243},
    "hc_strict_p_gt_0p8": {"N_spirals": 1402115, "dipole_sigma": 0.87, "p_value": 0.187},
    "null_used": "monopole-preserving (binomial draw at global p_CW); NOT isotropic-p=0.5"
  }
}
```

## How to load

```python
import pandas as pd
from huggingface_hub import hf_hub_download

path = hf_hub_download(
    repo_id="bamfai/galaxy-chirality-paper4",
    filename="catalog_c_production.parquet",
    repo_type="dataset",
)
df = pd.read_parquet(path)
print(df.shape, df.columns.tolist())
```

## Quality gates

The catalog passed the following gates in v1.0.69 of the paper. Per-leg systematics, face-on robustness, and the monopole+mask leakage null are all consistent with the no-cosmological-dipole verdict.

| Gate | Verdict | Source |
|---|---|---|
| Per-imaging-leg dipole significance (BASS+MzLS, DECaLS, DES) | All \|σ\| < 2 individually | §IV.E + Table per_leg |
| Face-on HC-spiral robustness | +0.62σ (Catalog C +4.31σ → HC +0.62σ) | §VI.D + Table face_on |
| MASTER post-deconvolution canonical $\ell=1$ | +1.85σ | §VI.A + Table multipoles |
| PSF-ellipticity 2D scatter calibration | $\langle\Delta p_{\rm CW}\rangle$ vs PSF \|e\| < 0.1% across all bins | Fig. PSF correlation |

## Versioning

This release corresponds to the paper at version **v1.0.69** (commit `5772535e2f24...`, 2026-05-15). Future revisions will tag matching versions in both the paper LaTeX `\version{}` macro and the `paper4-v1.X` GitHub release; the Parquet schema will not break across patch versions (v1.0.x). Minor or major version bumps (v1.1.x, v2.x) may introduce schema changes and will be announced in a CHANGELOG section here.

## Citation

```bibtex
@article{Golden2026Chirality,
  author = {Golden, Houston},
  title = {Constraints on the Cosmological-Principle Spin-Direction Dipole from 8.47M DESI Legacy Galaxies},
  year = {2026},
  journal = {arXiv preprint},
  eprint = {2526.XXXXX},
  doi = {10.XXXX/zenodo.XXXXXXX},
  url = {https://github.com/Hubify-Projects/bigbounce/releases/tag/paper4-v1.0}
}
```

## License

Catalog data: CC-BY-4.0. The paper PDF and source LaTeX are also CC-BY-4.0 on the public release. Underlying DESI Legacy Survey imagery is © DESI Legacy Imaging Surveys (NSF NOIRLab) and follows their standard CC-BY release terms.

## Contact

Houston Golden — `houston@bamf.ai` — https://hubify.com
