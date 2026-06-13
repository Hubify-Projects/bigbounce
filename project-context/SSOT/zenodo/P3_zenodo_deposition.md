# Zenodo Deposition Record — P3
## Paper: Spectrally Unusual Sources at Scale — Multi-Survey Anomaly Catalog

**Version:** v3.1.103
**Prepared:** 2026-06-13 (HD-11 DO-NOW directive)

---

## 1. Title

Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches

---

## 2. Authors

| Name | Email | Affiliation |
|------|-------|-------------|
| Houston Golden | houston@hubify.com | Independent Researcher, Los Angeles, California, USA |

---

## 3. Description (Abstract)

We present the largest-scale application of autoencoder anomaly detection across multiple astronomical archives (applying the BigAE autoencoder framework to 37.3 million sources and CMB map patches across DESI DR1, SDSS DR18, LAMOST DR10, eROSITA DR1, Planck, Gaia DR3, and NEOWISE). After per-survey native retraining and 7-way positional deduplication at 5 arcseconds, the recommended catalog-grade tier contains 269,317 unique entries drawn from a full Path-C unique catalog of 378,280 anomalies: 378,080 point-source object detections from six photometric/spectroscopic surveys plus 200 Planck CMB map-patch sky regions. Extended archival cross-matching of the top-1,000 DESI anomalies against 18 curated all-sky catalogs yields a genuine novelty fraction of 178/1,000 ~ 17.8% (Wilson 68% CI +/- 1.2%). A Path-C rebuild protocol resolves cross-transfer artifacts: 21.5x LAMOST anomaly-rate reduction after native retraining and ~6500x SDSS rate compression after native retraining. DESI 5-fold cross-validation Jaccard J_CV = 0.862 (>= 0.70 gate, PASS). Six injection-recovery gates: 3 PASS (SDSS 64%, Planck 100%, NEOWISE mask-geometry 100%) and 3 FAIL-with-diagnostic at 5 sigma (LAMOST 5.8%, Gaia 5.2%, eROSITA 1.2%). Three DESI x SDSS cross-matches include a time-variable source and an uncataloged BAL QSO at z ~ 0.86. An empirical Landy-Szalay bias measurement on the 5,384 QSO-candidate sample yields alpha_jk = 0.19 +/- 0.65 (0.29 sigma from null). A NANOGrav 15-yr KDE free-spectrum MCMC yields gamma = 2.567 +/- 0.382; the matter-bounce prediction gamma = 3.0 sits at +1.13 sigma (marginally consistent) and SMBHB gamma = 4.33 at +4.61 sigma (Savage-Dickey B_MB/SMBHB = 7.14 x 10^3 under the flat gamma in [0,7] prior). The catalog, model weights, and reproducibility scripts are publicly released with the arXiv posting.

---

## 4. Keywords

- anomaly detection
- machine learning
- spectroscopic surveys
- multi-survey catalogs
- autoencoder
- DESI DR1
- SDSS DR18
- LAMOST DR10
- eROSITA
- Planck CMB
- Gaia DR3
- NEOWISE
- primordial non-Gaussianity
- NANOGrav
- bouncing cosmology

---

## 5. License

**CC-BY-4.0** (Creative Commons Attribution 4.0 International)

---

## 6. Related Identifiers

| Relation | Identifier | Note |
|----------|-----------|------|
| isSupplementedBy | arXiv:XXXX.XXXXX | **PLACEHOLDER — insert real P3 arXiv ID after submission** |
| isPartOf | arXiv:XXXX.XXXXX (P1A) | ECH no-go companion |
| isPartOf | arXiv:XXXX.XXXXX (P1B) | MCMC companion |
| isPartOf | arXiv:XXXX.XXXXX (P2) | fnl forecast companion |
| isPartOf | arXiv:XXXX.XXXXX (P4) | Galaxy chirality catalog |
| hasVersion | https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog | **HuggingFace dataset (primary catalog parquets)** — flip to public on arXiv posting |

**HuggingFace Dataset URLs (from DATA_RELEASE_MANIFEST.md):**

| Dataset file | HF URL | Description |
|---|---|---|
| `pathc_unique_objects_no_act.parquet` | https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog | PRIMARY: 378,280 unique anomalies (7-way 5" dedup, ACT excluded); SHA-256 e0b57f25... |
| `pathc_unique_objects.parquet` | https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog | Sensitivity check: 378,480 anomalies (8-way with ACT); SHA-256 b14deb02... |
| `pathc_multi_survey_matches_no_act.parquet` | https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog | 637 multi-survey coincidence clusters (canonical); SHA-256 3605b16a... |
| `cmb_native_anomalies.parquet` | https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog | Planck CMB native retrain: 200 anomaly patches; SHA-256 ec1464cd... |
| `sdss_dr18_pathc_native.parquet` | https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog | SDSS DR18 native continuity slice: 77,905 objects; SHA-256 5139c663... |
| `neowise_pathc_masked_anomalies.parquet` | https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog | NEOWISE Path-C masked: 419 objects; SHA-256 fdee011e... |
| `gaia_dr3_anomalies.parquet` | https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog | Gaia DR3: 500 objects (exploratory); SHA-256 819c5978... |
| `lamost_dr10_pathc_native.parquet` | https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog | LAMOST DR10 native: 113,342 objects (exploratory tier); SHA-256 48c0e2f5... |
| `erosita_dr1_anomalies.parquet` | https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog | eROSITA DR1: 298 anomalies (membership-only; score axis irreproducible — use n=298 membership list only); SHA-256 4ea1b032... |

*Note: All parquet files are STAGED and not yet public on HuggingFace. They flip to public on arXiv posting.*

---

## 7. File Manifest

Files Houston should upload to Zenodo:

**Paper source files:**

| File | Path | Description |
|------|------|-------------|
| `paper3_arxiv_v3.1.103.tar.gz` | `pipelines/p3_anomaly_engine/paper3_arxiv_v3.1.103.tar.gz` | **PRIMARY — arXiv submission tarball** |
| `paper3_draft.pdf` | `pipelines/p3_anomaly_engine/paper3_draft.pdf` | Compiled PDF (27pp) |
| `paper3_draft.tex` | `pipelines/p3_anomaly_engine/paper3_draft.tex` | LaTeX source |

**Data artifacts (upload these to HuggingFace, link from Zenodo as related identifiers):**

All catalog parquet files live at: https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog (STAGED — flip to public on arXiv posting)

**Reproducibility scripts and JSON artifacts:**

| File | Path | Description |
|------|------|-------------|
| `pathc_positional_dedup.py` | `pipelines/p3_anomaly_engine/pathc_positional_dedup.py` | 7-way dedup script |
| `wave_14_rr_nanograv_bayesian.py` | `pipelines/p3_anomaly_engine/wave_14_rr_nanograv_bayesian.py` | NANOGrav MCMC script |
| `jaccard_100k_results.json` | `pipelines/p3_anomaly_engine/jaccard_100k_results.json` | Jaccard 100k validation |
| `r24conf_erosita_axis_sweep.json` | `pipelines/p3_anomaly_engine/r24conf_erosita_axis_sweep.json` | eROSITA score-axis audit artifact |
| `umap_stability.json` | `pipelines/p3_anomaly_engine/umap_stability.json` | UMAP stability results |

**Manifest count: 3 paper files + 5 reproducibility scripts/JSONs = 8 files** (catalog parquets hosted on HuggingFace, linked via related identifiers)

**FLAG for Houston attention:** The DESI DR1 native-retrained anomalies (195,829 objects) are noted in DATA_RELEASE_MANIFEST.md as hosted in the companion GitHub repo (https://github.com/Hubify-Projects/bigbounce), not under `pipelines/p3_anomaly_engine/`. These are large and were likely generated on RunPod pods — confirm they are accessible and backed up before submission day.

---

## 8. Communities

- `astrophysics`
- `cosmology-and-nongalactic-astrophysics`

---

## 9. Funding

**None** — Independent research, no grant funding.

---

## 10. Version

`v3.1.103`

---

## 11. Click-Publish Steps

1. **Log into zenodo.org** → click "New upload".
2. **Drop files:** drag in `paper3_arxiv_v3.1.103.tar.gz` + `paper3_draft.pdf` + the reproducibility scripts/JSONs (zip them as `p3_reproducibility.zip`). Do NOT upload the full catalog parquets to Zenodo — they live on HuggingFace; just add the HF dataset URL as a related identifier.
3. **Paste metadata:** Title, Description, Keywords, License (CC-BY-4.0), Authors, Communities, and Related Identifiers (including the HF dataset URL) from sections 1-9 above.
4. **Reserve DOI:** click "Reserve DOI" — copy the DOI and insert it into `DATA_RELEASE_MANIFEST.md` header `## Zenodo DOI: [TO BE MINTED AT SUBMISSION — insert here before arxiv upload]` and into the paper's Data Availability statement (tex L44 marker per the submission runbook).
5. **Publish:** click "Publish". Simultaneously flip the HuggingFace dataset `bamfai/bigbounce-anomaly-catalog` from STAGED to public at the moment of arXiv posting.
