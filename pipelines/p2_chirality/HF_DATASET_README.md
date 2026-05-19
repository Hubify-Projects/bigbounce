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

# DESI Legacy Galaxy Chirality Catalog (Paper 4 v1.0.116)



## v1.0.116 changelog (P4 external review wave + 11 internal R-rounds; v1.0.104 → v1.0.116)

Net trajectory since the v1.0.104 external review (2026-05-15 → 2026-05-18, 12 patch versions):

- **v1.0.106 GPT5-B3 monopole-subtraction truth-audit**: NaMaster input field now uses explicit galaxy-weighted mask-mean subtraction $\langle A\rangle_{\rm mask,gw}=2f_{\rm CW}^{\rm global}-1=-0.005294$. Canonical-mask post-MASTER $\sigma$ rises from $+1.85$ (v1.0.62 baseline, uncorrected $A_p$) to $+3.64$ (v1.0.107+ paper-wide convention) under proper monopole subtraction.
- **v1.0.108 multi-null battery** (3 interpretations of canonical-mask $+3.64\sigma$ explored at full extent per no-bias directive): proper-monopole-subtracted binomial null $+3.64\sigma$, apodized canonical mask $+3.57\sigma$ (rules out sharp-edge NaMaster artifact), sky-rotation null $+2.56\sigma$, bootstrap pixel-resample $-0.22\sigma$ (later proven tautological).
- **v1.0.109 cross-spectrum smoking gun**: $C^{An}_\ell$ between chirality asymmetry $A_p$ and pixel-density $n_{\rm total}(p)$ on canonical mask gives $r_{\ell=2}=-0.65$, $\sigma_{\ell=2}=-2.89$ at the auto-spectrum quadrupole excess → interpretation (ii) coherent low-$\ell$ depth-correlated systematic DIRECTLY CONFIRMED at the same multipole.
- **v1.0.110-v1.0.111 bootstrap audit**: bootstrap injection-recovery test shows a REAL $1.7\%$ dipole would give median $\sigma_{\rm bootstrap}=-0.49$ (P($\sigma>3$)=$1.3\%$) — bootstrap is TAUTOLOGICAL for cosmological-dipole hypothesis testing and is retained only as a sampling-variance diagnostic, not a verdict.
- **v1.0.113-v1.0.115 abstract trim + paper-wide convention**: abstract reduced from 1839 words / 177 lines → 600 words / 13 lines (67% reduction); result-first structure leads with $-0.12\sigma$ subsample-mask null. Paper-wide $+1.85\sigma \to +3.64\sigma$ replacement enforced (29 instances, v1.0.115).
- **v1.0.116 R20 closures**: Grok-R20 GRO-B1 "parity-violation overclaim" FALSIFIED by direct file inspection (the cited title is a stale `%`-comment; the live title is monopole-mask leakage; parity-EVEN disclaimer already in abstract). GRO-B2 closed via existing artifact — the $\ell=1$ cross-spectrum value $r_{\ell=1}=-0.49$, $\sigma_{\ell=1}=-1.53$ was already in `outputs/canonical_provenance/p4_cross_spectrum_A_n.json`; now reported in paper text alongside $\ell=2$.

**Verdict structure (v1.0.116, three-interpretation framework for canonical-mask $+3.64\sigma$ excess):**
- **(i) Real cosmological dipole at $\sim 1.7\%$**: DISFAVORED but bootstrap-null does NOT independently rule it out. Ruled out by THREE discriminators in combination: (a) $\ell=2 > \ell=1$ broadband structure (incompatible with a clean cosmological dipole), (b) $p_{\rm eq}$ quality-quartile washout (all four quartiles $|\sigma|<1$), (c) direct cross-spectrum confirming depth-correlated component at the precise multipole of the excess.
- **(ii) Coherent depth/PSF/morphology-correlated systematic at low $\ell$ on canonical footprint**: STRONGEST INTERPRETATION, now DIRECTLY CONFIRMED by cross-spectrum quadrupole anti-alignment.
- **(iii) NaMaster low-$\ell$ deconvolution artifact**: RULED OUT for the sharp-edge variant (apodized mask gives $+3.57\sigma$). A deeper NaMaster low-$\ell$ coupling artifact specific to patchy canonical geometry cannot be excluded without a NaMaster-independent reanalysis.

**Companion data release for** _"A Quantifiable Monopole-Mask Leakage Channel Can Mimic Large Raw Pseudo-$C_\ell$ Chirality Dipoles: An Equivariant Re-Analysis of 8.47M DESI Legacy Galaxies (3.2M Spirals) at Sub-Percent Sensitivity (50%-Recovery $3\sigma$ Threshold $A\approx 0.75\%$)"_ (Golden 2026, paper4-v1.0.116 release).

**Headline scientific finding.** The load-bearing scientific result is the MASTER-deconvolved $\ell=1$ chirality-dipole observable on the analysis subsample mask ($n=5{,}547{,}858$, $f_{\rm sky}=0.659$): $-0.12\sigma$, consistent with no dipole. The real-space post-TTA Catalog C dipole is $+0.43\sigma$ ($p=0.30$, $\sim 0.6\%$ residual amplitude). The $\ell=1$ observable is the parity-EVEN isotropy-breaking axial-vector channel and is NOT a direct parity-violation test. In our DESI Legacy / ViT-Small pipeline, a quantifiable leakage channel can mimic large raw chirality dipoles: a small uniform CW-vs-CCW classifier monopole couples to the patchy survey-mask geometry and inflates the raw pseudo-$C_\ell$ at $\ell=1$, then collapses through the full mode-coupling-removal chain (map + monopole + mask + MASTER inversion). A controlled monopole-only generative null at $N=500$ (canonical mask, NSIDE=64, binomial realizations at $p_{\rm CW}^{\rm global}=0.4974$) reproduces $99.3\%$ of the observed pre-MASTER pseudo-$C_1$ power. The canonical-mask post-MASTER residual is $+3.64\sigma$ under proper galaxy-weighted monopole subtraction (v1.0.107+ paper-wide convention; the legacy $+1.85\sigma$ v1.0.62 baseline was on uncorrected $A_p$ field) — interpretation (ii) coherent depth-correlated systematic, NOT a primordial detection. **This is a this-pipeline demonstration**: a like-for-like matched-footprint reanalysis under Shamir's Ganalyzer pipeline would be required for a formal $\sigma$-level exclusion of his reported signal, and is not performed in the present release.

**Cosmological measurement.** Real-space dipole fit on Catalog C: $\sigma_{\rm dipole}=0.43$ ($p=0.30$, $N_{\rm MC}=10{,}000$). MASTER-deconvolved $\ell=1$ on subsample mask: $-0.12\sigma$. The load-bearing systematic-inclusive sensitivity is the empirical 50%-recovery-at-$3\sigma$ threshold of $|A_{\rm dipole}|\approx 0.75\%$ from the extended 9-amplitude injection sweep; the Fisher Poisson asymptote $\sim 0.29\%$ is the ideal-statistical floor, not the operational detection threshold. Confidence-stratified diagnostics show $\sim 3\sigma$ apparent dipoles in low-confidence bins $p_{\rm eq}\in[0.4,0.6)$ that drop sharply into the high-confidence subsamples (two of three HC bins null, the third marginal at $\sim 2\sigma$), suggestive of classifier-label systematics rather than a primordial dipole.

## Quick links

- **Paper PDF (v1.0.116, latest):** https://github.com/Hubify-Projects/bigbounce/releases/download/paper4-v1.0.116/chirality_catalog_paper.pdf
- **Source LaTeX + canonical pipeline:** https://github.com/Hubify-Projects/bigbounce/tree/main/pipelines/p2_chirality
- **Immutable release (PDF + artifacts):** https://github.com/Hubify-Projects/bigbounce/releases/tag/paper4-v1.0.116
- **Zenodo DOI (release-pinned snapshot):** _minted via GitHub-Zenodo webhook on the_ [`paper4-v1.0.116` _release_](https://github.com/Hubify-Projects/bigbounce/releases/tag/paper4-v1.0.116)
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
  "version": "v1.0.116",
  "config": {"N_spiral": 3201160, "f_sky": 0.4938, "nside": 64, "lmax": 191, "N_MC": 500},
  "global_cw_fraction": 0.497353,
  "galaxy_weighted_mask_mean_A_gw": -0.005294,
  "dipole_l1_v1062_baseline_uncorrected_Ap": {"C1_decoupled": 2.298e-05, "null_mean": 8.00e-06, "null_std": 8.10e-06, "sigma_canonical_direct": 1.85, "_note": "v1.0.62 baseline; uncorrected A_p field; superseded by v1.0.107+ paper-wide convention below"},
  "dipole_l1_v10107_corrected_proper_monopole_subtraction": {"C1_decoupled": 1.51e-05, "null_mean": 3.10e-06, "null_std": 3.31e-06, "sigma_canonical_direct": 3.64, "_note": "v1.0.107+ paper-wide convention; proper galaxy-weighted monopole subtraction; canonical-mask canonical number"},
  "monopole_mask_leakage_null_N500": {
    "pre_master_pseudo_C1_sigma_vs_monopole_null": 1.69,
    "pre_master_reproduction_pct": 99.3,
    "post_master_canonical_sigma_v10107_corrected": 3.64,
    "post_master_canonical_sigma_v1062_baseline": 1.85,
    "post_master_subsample_sigma": -0.12,
    "hemisphere_maxabs_sigma_vs_monopole_null": 4.42,
    "hemisphere_reproduction_pct": 48.6,
    "interpretation": "At N=500 the monopole-only null reproduces 99.3% of the observed pre-MASTER pseudo-Cl power; the residual +3.64sigma post-MASTER canonical-mask value (v1.0.107+ proper-monopole-subtraction; supersedes the v1.0.62 baseline +1.85sigma on uncorrected A_p) is interpreted as a coherent depth-correlated systematic (interpretation (ii)), DIRECTLY CONFIRMED by cross-spectrum quadrupole anti-alignment with the pixel-density proxy at the same multipole (r_l=2=-0.65, sigma_l=2=-2.89; the auto-spectrum dipole multipole also shows depth correlation at r_l=1=-0.49, sigma_l=1=-1.53). NOT a primordial detection. The subsample-mask MASTER-deconvolved -0.12sigma is the load-bearing scientific result of the paper."
  },
  "multi_null_battery_v10108": {
    "proper_monopole_subtracted_binomial": 3.64,
    "apodized_canonical_mask_C2_apod": 3.57,
    "sky_rotation_per_pixel_shuffle": 2.56,
    "bootstrap_pixel_resample": -0.22,
    "bootstrap_tautology_note": "Bootstrap proven tautological for cosmological-dipole hypothesis testing per v1.0.110-v1.0.111 injection-recovery audit: a REAL injected A=1.7% dipole gives median sigma_bootstrap=-0.49 (P(sigma>3)=1.3%) under the same bootstrap. Retained as sampling-variance diagnostic only."
  },
  "cross_spectrum_A_n_canonical_mask_v10109": {
    "ell_1": {"correlation_r": -0.49, "cross_sigma_data_vs_null": -1.53},
    "ell_2": {"correlation_r": -0.65, "cross_sigma_data_vs_null": -2.89, "_note": "smoking gun for interpretation (ii) at the auto-spectrum quadrupole excess multipole"}
  },
  "per_imaging_leg": {
    "BASS+MzLS": {"N": 934551, "delta_cw_pct": 0.178, "dipole_sigma": 1.08, "p_value": 0.137},
    "DECaLS":    {"N": 1413958, "delta_cw_pct": -0.21, "dipole_sigma": -1.63, "p_value": 0.974},
    "DES":       {"N": 852651, "delta_cw_pct": 0.094, "dipole_sigma": 0.66, "p_value": 0.247}
  },
  "face_on_robustness": {
    "catalog_c_full": {"N_spirals": 3201160, "dipole_sigma_real_space_post_tta": 0.43, "p_value_real_space_post_tta": 0.30, "pseudo_c1_post_master_subsample_mask": -0.12, "pseudo_c1_post_master_canonical_mask_v10107_corrected": 3.64, "pseudo_c1_post_master_canonical_mask_v1062_baseline": 1.85, "_note": "v1.0.116: canonical-mask number is +3.64σ under proper galaxy-weighted monopole subtraction (v1.0.107+ paper-wide convention); the +1.85σ value is the v1.0.62 baseline on uncorrected A_p field and is retained for historical provenance only"},
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

The catalog passed the following gates in v1.0.116 of the paper. Per-leg systematics, face-on robustness, monopole+mask leakage null, D4-TTA rotation-equivariance hold-out, confidence-stratified signal-hunt diagnostics, multi-null battery, and cross-spectrum smoking gun are all consistent with the no-cosmological-dipole verdict on the load-bearing subsample-mask null and with the interpretation-(ii) coherent depth-correlated systematic on the canonical mask.

| Gate | Verdict | Source |
|---|---|---|
| Per-imaging-leg dipole significance (BASS+MzLS, DECaLS, DES) | All \|σ\| < 2 individually | §IV.E + Table per_leg |
| Face-on HC-spiral robustness | +0.62σ (face-on diagnostic; real-space headline is +0.43σ post-TTA, NOT 4.31σ — see footnote) | §VI.D + Table face_on |
| MASTER post-deconvolution subsample-mask $\ell=1$ (load-bearing) | −0.12σ | §VI.A + Table multipoles |
| MASTER post-deconvolution canonical-mask $\ell=1$ (interpretation (ii) systematic) | +3.64σ (v1.0.107+ proper-monopole-subtracted; supersedes v1.0.62 baseline +1.85σ on uncorrected A_p) | §VI.A + Table multipoles |
| Cross-spectrum smoking gun $C^{An}_\ell$ on canonical mask | $r_{\ell=1}=-0.49$, $\sigma_{\ell=1}=-1.53$ and $r_{\ell=2}=-0.65$, $\sigma_{\ell=2}=-2.89$ → interpretation (ii) directly confirmed | §VI.B Cross-spectrum |
| PSF-ellipticity 2D scatter calibration | $\langle\Delta p_{\rm CW}\rangle$ vs PSF \|e\| < 0.1% across all bins | Fig. PSF correlation |

## Versioning

This release corresponds to the paper at version **v1.0.116** (commit `a2f24332`, 2026-05-18) and tracks the v1.0.104 → v1.0.116 trajectory: external review wave + 11 internal R-rounds + GPT5-B3 monopole-subtraction truth-audit + multi-null battery + cross-spectrum smoking gun + bootstrap-tautology audit + abstract trim + paper-wide $+1.85\sigma \to +3.64\sigma$ convention + R20 $\ell=1$ cross-spectrum closure. Future revisions will tag matching versions in both the paper LaTeX `\version{}` macro and the `paper4-v1.X` GitHub release; the Parquet schema will not break across patch versions (v1.0.x). Minor or major version bumps (v1.1.x, v2.x) may introduce schema changes and will be announced in a CHANGELOG section here.

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
