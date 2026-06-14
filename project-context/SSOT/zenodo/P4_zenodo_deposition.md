# Zenodo Deposition Record — P4
## Paper: Survey-Scale Galaxy Chirality with Equivariant TTA

**Version:** v1.0.188 (EXT11-closure submission version | PDF md5: c47abc18 | 23pp)
**Prepared:** 2026-06-13 (HD-11 DO-NOW directive) | **Updated:** EXT11-closure-wave 2026-06-13
**Submission order:** FIRST (P4 → P1A+P1B → P3 → P2 → P5 per PUBLISH_PLAN.md)

---

## 1. Title

Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)

---

## 2. Authors

| Name | Email | Affiliation |
|------|-------|-------------|
| Houston Golden | houston@hubify.com | Independent Researcher, Los Angeles, California, USA |

---

## 3. Description (Abstract)

We present, to our knowledge, the largest chirality-labeled galaxy catalog to date: 8,474,531 DESI Legacy DR8 galaxies classified by a flip-equivariant Vision Transformer pipeline into clockwise (CW), counter-clockwise (CCW), and non-spiral classes, with N_spiral = 3,201,160 spirals, publicly released with model weights and reproducibility scripts. The primary scientific result is a real-space chirality dipole consistent with null: the equivariant-catalog high-confidence dipole fit (confidence > 0.6; N ~ 9.5 x 10^5 spirals) gives +0.41 sigma (moment-z against the isotropic-bootstrap null; empirical-rank p = 0.31, 10^4 isotropic-null realizations), and a block-bootstrap WLS template fit disfavors a clean cosmological dipole at the 1.7% reference amplitude at z ~ -18. This l=1 observable is parity-even (isotropy-breaking axial-vector channel), not a direct parity-violation test. The MASTER pseudo-C_ell channel on the patchy footprint is a systematics diagnostic, not an independent cosmological null: a monopole-only generative null reproduces 99.32% of the raw pre-MASTER l=1 power (monopole-mask leakage), and MASTER deconvolution substantially reduces but does not remove this leakage — the post-MASTER harmonic diagnostics carry systematics-attributed residuals (+3.64 sigma moment-z, ~1.9 sigma Gaussian-equivalent, canonical mask; +7.28 sigma, apodized footprint), characterized by an eight-anchor systematic battery. Falsification criterion: a future >= 5 sigma real-space dipole detection at amplitude A >= A_95, where injection-recovery brackets A_95 between 1.0% and 1.5% (A_50 ~ 0.75%), would be in tension with the present null.

---

## 4. Keywords

- galaxies: spiral
- galaxies: statistics
- methods: data analysis
- cosmology: observations
- large-scale structure of universe
- galaxy chirality
- handedness
- Vision Transformer
- equivariant neural network
- DESI Legacy Survey
- parity violation
- dipole asymmetry
- machine learning

---

## 5. License

**CC-BY-4.0** (Creative Commons Attribution 4.0 International)

---

## 6. Related Identifiers

| Relation | Identifier | Note |
|----------|-----------|------|
| isSupplementedBy | arXiv:XXXX.XXXXX | **PLACEHOLDER — insert real P4 arXiv ID after submission (minted first)** |
| isReferencedBy | arXiv:XXXX.XXXXX (P5) | DESI environment follow-up paper; P5 cites P4 |
| hasVersion | https://huggingface.co/bamfai/galaxy-chirality-v2 | Model weights (HuggingFace) — tag v2026.04 on submission day |

*Note: The Gemini EXT7 MAJOR finding was entirely driven by the absence of this Zenodo DOI placeholder (HD-11). Minting this Zenodo record resolves that finding and satisfies the release-bundle gate.*

---

## 7. File Manifest

Files Houston should upload to Zenodo:

**Paper source files:**

| File | Path | Description |
|------|------|-------------|
| `paper4_arxiv_v1.0.188.tar.gz` | `project-context/SSOT/arxiv_tarballs/paper4_arxiv_v1.0.188.tar.gz` | **PRIMARY — arXiv submission tarball (EXT11-closure; PDF md5 c47abc18)** |
| `chirality_catalog_paper.pdf` | `pipelines/p2_chirality/chirality_catalog_paper.pdf` | Compiled PDF (23pp; v1.0.188) |
| `chirality_catalog_paper.tex` | `pipelines/p2_chirality/chirality_catalog_paper.tex` | LaTeX source |

**Canonical provenance JSON artifacts:**

| File | Path | Description |
|------|------|-------------|
| `boundary_distance_variance.json` | `pipelines/p2_chirality/outputs/canonical_provenance/boundary_distance_variance.json` | Boundary-distance variance (Gemini-Major1 closure) |
| `block_bootstrap_nside_sensitivity.json` | `pipelines/p2_chirality/outputs/canonical_provenance/block_bootstrap_nside_sensitivity.json` | Block-bootstrap NSIDE sensitivity |
| `c11b_hc_dipole_nulls.json` | `pipelines/p2_chirality/outputs/canonical_provenance/c11b_hc_dipole_nulls.json` | HC dipole nulls |
| `c12_queue2_null_amps_10k.npy` | `pipelines/p2_chirality/outputs/canonical_provenance/c12_queue2_null_amps_10k.npy` | 10k null amplitude distribution |
| `c12b_wls_conditioning.json` | `pipelines/p2_chirality/outputs/canonical_provenance/c12b_wls_conditioning.json` | WLS conditioning |
| `c12_r24conf_local_batch.json` | `pipelines/p2_chirality/outputs/canonical_provenance/c12_r24conf_local_batch.json` | R24conf local batch |
| `c16_r24conf_pod_batch.json` | `pipelines/p2_chirality/outputs/canonical_provenance/c16_r24conf_pod_batch.json` | R24conf pod batch |

*Additional canonical provenance files exist in `outputs/canonical_provenance/`; see `README_CANONICAL.md` for the full provenance index.*

**Model weights:**

| Resource | URL | Description |
|----------|-----|-------------|
| Galaxy chirality ViT model | https://huggingface.co/bamfai/galaxy-chirality-v2 | Tag v2026.04 on submission day (5-min task) |

**Manifest count: 3 paper files + 7 canonical JSON/npy artifacts + HF model link = 10 local files**

---

## 8. Communities

- `astrophysics`
- `cosmology-and-nongalactic-astrophysics`

---

## 9. Funding

**None** — Independent research, no grant funding.

---

## 10. Version

`v1.0.188` (EXT11-closure | PDF md5: c47abc18 | 23pp)

---

## 11. Click-Publish Steps

1. **Log into zenodo.org** → click "New upload". (P4 is submitted FIRST; all other papers wait for P4's arXiv ID.)
2. **Drop files:** drag in `paper4_arxiv_v1.0.188.tar.gz` + `chirality_catalog_paper.pdf` + the canonical provenance JSONs (zip as `p4_provenance.zip`).
3. **Paste metadata:** Title, Description, Keywords, License (CC-BY-4.0), Authors, Communities, and Related Identifiers from sections 1-9 above. Set Upload type = "Publication" → "Preprint".
4. **Reserve DOI:** click "Reserve DOI" — copy the DOI and re-point all `\artifact{}` blob/main links in the paper to this Zenodo DOI before the final compile. Also tag the HuggingFace model repo `bamfai/galaxy-chirality-v2` with `v2026.04`.
5. **Publish:** click "Publish". The Zenodo DOI and the P4 arXiv ID (assigned ~1 hour after upload) are what P5 depends on for its companion-reference insertion. Hold the P5 upload until P4's arXiv ID is in hand.
