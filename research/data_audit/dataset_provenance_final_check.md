# Dataset Provenance Final Check

**Date:** 2026-03-13
**Scope:** All datasets referenced in arxiv/main.tex

---

## 1. MCMC Chain Data

| Dataset | Source | License | Reproducible? | Checksum? |
|---------|--------|---------|---------------|-----------|
| full_tension | Cobaya 3.6.1 + Planck NPIPE + BAO + SN + SH0ES + DES | Planck: ESA PSI; BAO: public; SN: CC-BY | YES (configs in frozen pack) | YES (SHA256SUMS.txt) |
| planck_bao_sn | Cobaya 3.6.1 + Planck NPIPE + BAO + Pantheon SN | Same as above minus SH0ES/DES | YES (configs in frozen pack) | YES (SHA256SUMS.txt) |
| planck_only | IN PROGRESS | — | — | — |
| planck_bao | NOT YET STARTED | — | — | — |

**Status:** First two frozen and checksummed. Last two pending.

---

## 2. CMB Likelihood Data

| Dataset | Source URL | DOI/Citation | License | Download? |
|---------|-----------|-------------|---------|-----------|
| Planck 2018 (TTTEEE+lowl+lensing) | pla.esac.esa.int | Planck 2018 VI | ESA PSI | Via Cobaya auto-download |
| Planck NPIPE CamSpec | GitHub/cmbant | Rosenberg+ 2022 | Public | Via Cobaya auto-download |

**Status:** GOOD — standard public likelihoods, automatically downloaded by Cobaya.

---

## 3. BAO Data

| Dataset | Source | Citation | License |
|---------|--------|----------|---------|
| SDSS DR7 (6dFGS) | sdss.org | Beutler+ 2011 | Public |
| SDSS DR12 (BOSS) | sdss.org | Alam+ 2017 | Public |
| DESI BAO (if used) | desi.lbl.gov | DESI 2024 | Public |

**Status:** GOOD — all public. Exact BAO dataset combination documented in Cobaya YAML configs.

---

## 4. Supernova Data

| Dataset | Source | Citation | License |
|---------|--------|----------|---------|
| Pantheon+ | pantheonplussh0es.github.io | Brout+ 2022 | CC-BY 4.0 |

**Status:** GOOD — public, DOI available, CC-BY licensed.

---

## 5. H₀ Prior

| Dataset | Source | Citation | License |
|---------|--------|----------|---------|
| SH0ES | Riess+ 2022 | arXiv:2112.04510 | Public measurement |

**Status:** GOOD — published value used as Gaussian prior.

---

## 6. Galaxy Spin Data

| Dataset | Source | Citation | Status |
|---------|--------|----------|--------|
| galaxy_spin_data.csv | UNKNOWN provenance | Claims Shamir+ surveys | **DEPRECATED** |
| Shamir 2024 aggregate counts | Shamir 2024 (arXiv) | Table reconstruction | ADEQUATE — honest provenance |
| Galaxy Zoo DECaLS | Zenodo (doi:10.5281/zenodo.4573248) | Walmsley+ 2022 | On RunPod only |

**CRITICAL WARNING:** `reproducibility/galaxy_spins/galaxy_spin_data.csv` has unverified provenance. Round-number counts and JWST entries that contradict the cited paper. This file is DEPRECATED and should NOT be referenced in the paper. The current manuscript uses published aggregate counts from Shamir (2024), which is adequate.

---

## 7. Birefringence Measurements

| Source | Value | Citation | arXiv | Status |
|--------|-------|----------|-------|--------|
| Eskilt 2022 (Planck NPIPE) | β = 0.30° ± 0.11° | Eskilt 2022 | 2205.13962 | **USED** ✓ |
| ACT DR6 | β = 0.215° ± 0.074° | Diego-Palazuelos & Komatsu 2025 | 2503.14452 | **USED** ✓ |
| SPIDER 2025 | β_total = 0.50° ± 0.07° | SPIDER collab 2025 | 2510.25489 | CITE ONLY |
| Minami & Komatsu 2020 | β = 0.35° ± 0.14° | Minami & Komatsu 2020 | 2011.11254 | DO NOT USE (superseded) |

**Status:** GOOD — two independent measurements properly cited and used.

---

## 8. Bibliography Provenance

| Issue | Details | Severity |
|-------|---------|----------|
| Missing journal field | `Shamir2024` in references.bib | LOW |
| Empty author field | `ECTorsionDESI2025` in references.bib | LOW |
| Uncited entries | CMBS4_2019, Euclid2024, LSST2019, PantosS82026 | LOW (may be future use) |
| Missing citation? | DiegoPalazuelos2025 — verify in .bib | CHECK |
| Missing citation? | SPIDER 2025 — verify in .bib if cited | CHECK |

---

## 9. Data & Code Availability

The manuscript (Sec. 12, line 1218+) references a GitHub repository:
`https://github.com/Hubify-Projects/bigbounce/tree/v1.6.0/reproducibility`

Items listed as available:
- Cobaya YAML configs ✓ (in frozen packs)
- reproduce_cosmology.sh ✓
- galaxy_spins/spin_fit_stan.py ✓
- data_build/build_galaxy_spin_dataset.py ✓
- docs/IMPLEMENTATION_MAP.md ✓
- docs/KNOWN_GAPS.md ✓
- results/mcmc_posterior_summary.txt — auto-generated, verify exists
- **figures/corner_H0_sigma8_Neff.pdf** — **FILE DOES NOT EXIST** in arxiv/figures/ or paper/figures/

**Action needed:** Generate or update corner_H0_sigma8_Neff.pdf for the reproducibility package.

---

## 10. Summary

| Category | Status |
|----------|--------|
| MCMC chains | GOOD (2/4 frozen, 2 pending) |
| CMB likelihoods | GOOD (public, auto-downloaded) |
| BAO + SN data | GOOD (public, documented) |
| Galaxy spin data | CAUTION (deprecated file exists; current analysis uses honest Shamir 2024 reconstruction) |
| Birefringence data | GOOD (2 independent published measurements) |
| Bibliography | GOOD (0 undefined refs; 2 minor BibTeX warnings) |
| Reproducibility package | 1 MISSING FILE (corner plot) |
