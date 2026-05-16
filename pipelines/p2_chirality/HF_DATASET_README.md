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
    path: "catalog_production.parquet"
- config_name: catalog_c_high_confidence_spiral
  data_files:
  - split: hc_spiral
    path: "catalog_c_hc_spiral_p_cw_gt_0p6.parquet"
- config_name: dipole_results
  data_files:
  - split: dipole
    path: "dipole_catalog_c.json"
---

# DESI Legacy Galaxy Chirality Catalog (Paper 4 v1.0.88)

**Companion data release for** _"A Quantifiable Monopole-Mask Leakage Channel Can Mimic Large Raw Pseudo-$C_\ell$ Chirality Dipoles: An Equivariant Re-Analysis of 8.47M DESI Legacy Galaxies (3.2M Spirals) at Sub-Percent Sensitivity (50%-Recovery $3\sigma$ Threshold $A\approx 0.75\%$)"_ (Golden 2026, paper4-v1.0.88 release).

**Headline scientific finding.** In our DESI Legacy / ViT-Small classifier pipeline, a quantifiable leakage channel can mimic large raw chirality dipoles: a small uniform CW-vs-CCW classifier monopole couples to the patchy survey-mask geometry and inflates the raw pseudo-$C_\ell$ at $\ell=1$, then **collapses to $-0.12\sigma$ once the MASTER mode-coupling matrix is applied** on the same data. A controlled monopole-only generative null at $N=500$ (canonical mask, NSIDE=64, binomial realizations at $p_{\rm CW}^{\rm global}=0.4974$) **reproduces 99.3% of the observed pre-MASTER pseudo-$C_1$ power** (observed $1.696\times10^{-2}$ vs null mean $1.6846\times10^{-2}\pm 6.8\times10^{-5}$; residual $+1.69\sigma$). The residual canonical-mask post-MASTER excursion of $+1.85\sigma$ is reported transparently as a sub-detection-threshold unresolved systematic (NOT a calibrated leakage floor or primordial signal). **This is a this-pipeline demonstration**: a like-for-like matched-footprint reanalysis under Shamir's Ganalyzer pipeline would be required for a formal $\sigma$-level exclusion of his reported signal, and is not performed in the present release.

**Cosmological measurement.** Real-space dipole fit on Catalog C: $\sigma_{\rm dipole}=0.43$ ($p=0.30$, $N_{\rm MC}=10{,}000$). MASTER-deconvolved $\ell=1$ on subsample mask: $-0.12\sigma$. The load-bearing systematic-inclusive sensitivity is the empirical 50%-recovery-at-$3\sigma$ threshold of $|A_{\rm dipole}|\approx 0.75\%$ from the extended 9-amplitude injection sweep; the Fisher Poisson asymptote $\sim 0.29\%$ is the ideal-statistical floor, not the operational detection threshold. Confidence-stratified diagnostics show $\sim 3\sigma$ apparent dipoles in low-confidence bins $p_{\rm eq}\in[0.4,0.6)$ that drop sharply into the high-confidence subsamples (two of three HC bins null, the third marginal at $\sim 2\sigma$), suggestive of classifier-label systematics rather than a primordial dipole.

## Quick links

- **Paper PDF (v1.0.88, latest):** https://github.com/Hubify-Projects/bigbounce/releases/download/paper4-v1.0.88/chirality_catalog_paper.pdf
- **Source LaTeX + canonical pipeline:** https://github.com/Hubify-Projects/bigbounce/tree/main/pipelines/p2_chirality
- **Immutable release (PDF + artifacts):** https://github.com/Hubify-Projects/bigbounce/releases/tag/paper4-v1.0.88
- **Zenodo DOI (release-pinned snapshot):** _minted via GitHub-Zenodo webhook on the_ [`paper4-v1.0.88` _release_](https://github.com/Hubify-Projects/bigbounce/releases/tag/paper4-v1.0.88)
- **One-shot reproduction:** `bash pipelines/p2_chirality/reproduce_paper4.sh`

## Schema

### `catalog_production.parquet` (8,474,531 rows total; 3,201,160 spirals)

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
  "version": "v1.0.88",
  "config": {"N_spiral": 3201160, "f_sky": 0.4938, "nside": 64, "lmax": 191, "N_MC": 500},
  "global_cw_fraction": 0.497353,
  "dipole_l1": {"C1_decoupled": 2.298e-05, "null_mean": 8.00e-06, "null_std": 8.10e-06, "sigma_canonical_direct": 1.850},
  "monopole_mask_leakage_null_N500": {
    "pre_master_pseudo_C1_sigma_vs_monopole_null": 1.69,
    "pre_master_reproduction_pct": 99.3,
    "post_master_canonical_sigma": 1.85,
    "post_master_subsample_sigma": -0.12,
    "hemisphere_maxabs_sigma_vs_monopole_null": 4.42,
    "hemisphere_reproduction_pct": 48.6,
    "interpretation": "At N=500 the monopole-only null reproduces 99.3% of the observed pre-MASTER pseudo-Cl power; the residual +1.85sigma post-MASTER canonical-mask value is reported as an unresolved sub-detection-threshold systematic, NOT a calibrated leakage floor. The hemisphere residual at +4.42sigma indicates additional depth/PSF/morphology coupling not captured by the monopole-only null."
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
    repo_id="bamfai/galaxy-chirality-catalog",
    filename="catalog_production.parquet",
    repo_type="dataset",
)
df = pd.read_parquet(path)
print(df.shape, df.columns.tolist())
```

## Quality gates

The catalog passed the following gates in v1.0.88 of the paper. Per-leg systematics, face-on robustness, monopole+mask leakage null, D4-TTA rotation-equivariance hold-out, and confidence-stratified signal-hunt diagnostics are all consistent with the no-cosmological-dipole verdict.

| Gate | Verdict | Source |
|---|---|---|
| Per-imaging-leg dipole significance (BASS+MzLS, DECaLS, DES) | All \|σ\| < 2 individually | §IV.E + Table per_leg |
| Face-on HC-spiral robustness | +0.62σ (Catalog C +4.31σ → HC +0.62σ) | §VI.D + Table face_on |
| MASTER post-deconvolution canonical $\ell=1$ | +1.85σ | §VI.A + Table multipoles |
| PSF-ellipticity 2D scatter calibration | $\langle\Delta p_{\rm CW}\rangle$ vs PSF \|e\| < 0.1% across all bins | Fig. PSF correlation |

## Versioning

This release corresponds to the paper at version **v1.0.88** (commit `4b867b0f...`, 2026-05-15) and tracks the methods-paper reframe + Path-A signal-hunt + N=500 monopole+mask null + extended injection sweep + external-review-3 closures. Future revisions will tag matching versions in both the paper LaTeX `\version{}` macro and the `paper4-v1.X` GitHub release; the Parquet schema will not break across patch versions (v1.0.x). Minor or major version bumps (v1.1.x, v2.x) may introduce schema changes and will be announced in a CHANGELOG section here.

## Citation

```bibtex
@article{Golden2026Chirality,
  author = {Golden, Houston},
  title = {Galaxy-Chirality Dipole Claims Are Explained by Monopole-Mask Leakage: An Equivariant Re-Analysis of 8.47M DESI Legacy Galaxies},
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
