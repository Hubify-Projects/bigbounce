# External Catalogs — Provenance

## `pre_desi.fits` — Jia CE-ResNet DESI chirality catalog

The CE-ResNet (Chirality Equivariant Residual Network) galaxy-spin classification
catalog. This is the external component that supplied ~67.5% of P4's historical
training composition (17,153 spirals + 826 non-spirals of the 26,616-row historical
realization; see `chirality_catalog_paper.tex` L871 and the P4 compute campaign G1
section). Re-provisioned to unblock the G1 regenerable-retrain gate.

| Field | Value |
|-------|-------|
| **Filename** | `pre_desi.fits` |
| **Source (canonical DOI)** | https://doi.org/10.5281/zenodo.7167388 |
| **Direct download URL** | https://zenodo.org/records/7167388/files/pre_desi.fits?download=1 |
| **Zenodo record** | `galaxy-spin-zs-catalog` (record 7167388, published 2022-10-08) |
| **Retrieval date** | 2026-07-19 (UTC) |
| **Size** | 380,897,280 bytes (363 MiB) |
| **sha256** | `894dbe887140c165488a0f6053e2cd21f4ab72be9b06ece733e6ce177c0e304b` |
| **License** | CC-BY-4.0 |
| **FITS validity** | VALID — verified with astropy 6.0.1 |

### Lineage
- **Paper:** He Jia, Hong-Ming Zhu, Ue-Li Pen, *"Galaxy Spin Classification I:
  Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network"*,
  ApJ (accepted); arXiv:2210.04168.
- **Code:** GitHub `h3jia/galaxy_spin_classifier` (README references arXiv 2210.04168;
  repo has no data assets/releases — the catalog lives only on Zenodo).
- **Data host:** Zenodo DOI 10.5281/zenodo.7167388. (China-VO / NADC was cited in the
  campaign-doc lineage as a possible host, but the actual public, no-login artifact is
  on Zenodo — used directly; no registration required.)

### File structure (verified 2026-07-19 with astropy)
- HDU 0: `PRIMARY` (empty)
- HDU 1: `SWEEP` BinTableHDU — **1,953,246 rows × 40 columns**
- Key columns: `P_CW`, `P_ACW` (CE-ResNet DESI-image chirality probabilities,
  float64, range ~[0.006, 0.972]), `RA`, `DEC` (float64, degrees), plus DESI sweep
  photometry (`FLUX_G/R/Z`, `SHAPE_*`, `Z_PHOT_*`, `Z_SPEC`, `MASKBITS`, `TRAINING`, ...).
- Matches the schema the G1 wrapper `train_g1_manifest.py` expects (RA/DEC/P_CW/P_ACW):
  drop this file into `external_catalogs/` and the wrapper auto-includes CE spirals /
  non-spirals and records the file sha256.

### Companion file (not downloaded this session, same record)
- `reduced_gz1.csv` (70.1 MB) — 173,097 GZ1 galaxies with GZ vote fractions +
  CE-ResNet SDSS/DESI predictions. Available from the same Zenodo record if needed
  for the 26,616-vs-26,626 crossmatch reconciliation.

### Reproduce this download
```bash
curl -L --fail --retry 3 \
  -o pre_desi.fits \
  "https://zenodo.org/records/7167388/files/pre_desi.fits?download=1"
shasum -a 256 pre_desi.fits
# expect: 894dbe887140c165488a0f6053e2cd21f4ab72be9b06ece733e6ce177c0e304b
```

**Note:** the FITS itself is gitignored (363 MB > 100 MB); this provenance file is
tracked. Re-fetch from the Zenodo DOI above on any fresh machine or pod.
