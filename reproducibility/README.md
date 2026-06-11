# Reproducibility Bundle

**Paper:** Channel-Level Closure of Four Minimal Einstein--Cartan--Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter (Paper I A)
**Author:** Houston Golden
**Paper version:** v1A.0.61 (2026-06-11)
**Bundle version:** v1A.0.59-bundle

## Paper I(b) quick links

This repository is program-wide; companion Paper I(b) (the MCMC companion,
`arxiv/paper1b_mcmc_companion.tex`) is backed by the same bundle:

- **Frozen MCMC chains + diagnostics** (Paper I(b) Tables I/III–IV):
  `cosmology/frozen/full_tension_20260311_1728/` and
  `cosmology/frozen/planck_bao_sn_20260312_1954/` — use
  `diagnostics/parameter_summary_CORRECTED.json` in each (all seven
  Table I parameters incl. S₈), not the column-permuted
  `parameter_summary.json`.
- **Cobaya YAML configurations** (stock CAMB): `cosmology/`
- **NaMaster driver script** (Paper I(b) CMB EB pipeline): `cmb/`-level
  driver referenced in `IMPLEMENTATION_MAP.md`
- **HuggingFace datasets** (chain diagnostics, NaMaster artifacts, ALP
  chains): URLs in the repository root `CHANGELOG.md` under the Paper I(b)
  version entry
- **Sample-count conventions**: `cosmology/COUNT_EXPLANATION.md`

> **Note (2026-06-10):** This bundle was previously labelled "v0.9.0 / Geometric Dark Energy" while the manuscript moved to title "Channel-Level Closure of Four Minimal ECH Dark-Energy Routes and Perturbation Transparency for Scalar Matter" at v1A.0.56, then to v1A.0.57 after the EXT1 external-round textual-closure wave, then to v1A.0.58 after the R29 post-EXT1 internal-round closure wave, then to v1A.0.59 after the EXT2 external-round closure wave. Labels here now track the current manuscript title and version. The Cobaya YAMLs and Stan galaxy-spin code are unchanged from the v0.9.0 / v1A.0.56-bundle states (MCMC chains and convergence are documented in companion Paper I(b)); the v1A.0.56 → v1A.0.57 → v1A.0.58 bumps were README/BibTeX-metadata resyncs only, and the v1A.0.59 bump additionally corrects the "What This Bundle Reproduces" table to the frozen-chain values (EXT2 F2) — the bundles are otherwise byte-identical.

## Quick Start

```bash
# 1. Create environment
pip install cobaya==3.5.4 getdist cmdstanpy arviz pandas numpy matplotlib
cobaya-install cosmo -p ./packages
install_cmdstan

# 2. Reproduce cosmological fits (~4-12h per config)
cd cosmology && bash reproduce_cosmology.sh

# 3. Reproduce galaxy spin fit (~10-30min)
cd galaxy_spins && bash reproduce_spins.sh
```

## Repository Structure

```
reproducibility/
├── README.md                  # This file
├── cosmology/
│   ├── cobaya_planck.yaml           # Planck-only (Table IV row 1)
│   ├── cobaya_planck_bao.yaml       # Planck + BAO (Table IV row 2)
│   ├── cobaya_planck_bao_sn.yaml    # Planck + BAO + SN (Table IV row 3)
│   ├── cobaya_full_tension.yaml     # Full tension dataset (Tables III, IV row 4)
│   └── reproduce_cosmology.sh       # One-command reproduction
├── galaxy_spins/
│   ├── spin_fit_stan.py             # Hierarchical Bayesian model (Stan)
│   ├── reproduce_spins.sh           # One-command reproduction
│   ├── DEPRECATED.md                # Deprecation notice for old data file
│   └── galaxy_spin_data_DEPRECATED.csv  # DEPRECATED — do not use
├── cmb_eb/
│   └── (empty — CMB EB values are literature citations, not original analysis)
├── results/
│   └── (populated by running reproduce scripts)
├── docs/
│   ├── IMPLEMENTATION_MAP.md        # Paper claim → code → output mapping
│   └── KNOWN_GAPS.md               # Honest disclosure of gaps
└── figures/
    └── (populated by running reproduce scripts)
```

## What This Bundle Reproduces

Values quoted below track the frozen-chain results recorded in companion
Paper I(b) Table IV (full-tension configuration: Planck NPIPE + BAO + Pantheon+
+ DES-SN5YR + DESI DR2). Source of truth:
`reproducibility/cosmology/frozen/full_tension_20260311_1728/diagnostics/parameter_summary_CORRECTED.json`.

| Paper Result | Reproducible? | How |
|-------------|:---:|-----|
| H₀ = 67.68 ± 1.06 km s⁻¹ Mpc⁻¹ | YES | `cobaya_full_tension.yaml` with stock CAMB |
| σ₈ = 0.8034 ± 0.0084 | YES | `cobaya_full_tension.yaml` with stock CAMB |
| ΔN_eff = −0.020 ± 0.169 | YES | `cobaya_full_tension.yaml` with stock CAMB |
| Galaxy spin A₀, p, q | YES | `spin_fit_stan.py` + Shamir (2024) aggregate counts |
| χ²_eff, AIC, BIC | YES | From MCMC chain maximum likelihood |
| ln B (Bayes factors) | PARTIAL | Requires PolyChord (not included) |
| β ≈ 0.27° birefringence | N/A | Literature value (WMAP+Planck PR4) |
| Corner plots | YES | From chains using GetDist |

## What This Bundle Does NOT Reproduce

See `docs/KNOWN_GAPS.md` for full details:

1. **No custom CAMB modifications** — model uses standard ΛCDM + N_eff
2. **Frozen chains are committed; fresh proxy chains are not** — the
   `reproducibility/cosmology/frozen/full_tension_20260311_1728/` and
   `frozen/planck_bao_sn_20260312_1954/` directories contain the committed
   chains and diagnostics that back Paper I(b) Tables III–IV. Fresh ΛCDM+ΔN_eff
   proxy chains for re-verification must be generated locally via
   `reproduce_cosmology.sh` (~4–12 h per config).
3. **No CNN classifier** — uses published catalogs
4. **No CMB map analysis beyond the NaMaster driver** — Paper I(b)'s EB
   pipeline artifacts (mask, MC seeds, output spectra) are provided /
   linked via the HuggingFace datasets; published birefringence values
   (e.g. β=0.342°±0.094°) are literature-cited, not re-derived from maps
5. **No nested sampling** — Bayes factors require PolyChord

## Hardware Notes

- MCMC runs: 4+ CPU cores recommended, ~8 GB RAM
- Stan fit: Any modern laptop, ~1 GB RAM
- Disk: ~1 GB per MCMC chain set

## Known Issues

- The DES Y3 S8 constraint in `cobaya_full_tension.yaml` is approximated
  as a Gaussian prior, not the full 3x2pt likelihood.
- The Planck NPIPE likelihood (`CamSpec`) may produce slightly different
  results than the older `plikHM` likelihood used in some Planck papers.

## License

MIT License. See LICENSE file.

## Citation

```bibtex
@article{Golden2026P1A,
  author = {Golden, Houston},
  title = {Channel-Level Closure of Four Minimal Einstein--Cartan--Holst
           Dark-Energy Routes and Perturbation Transparency for Scalar Matter},
  year = {2026},
  note = {Paper I A, v1A.0.59},
  eprint = {XXXX.XXXXX},
  archivePrefix = {arXiv},
  primaryClass = {gr-qc}
}
```
