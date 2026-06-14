# Zenodo Deposition Record — P5
## Paper: Environmental Dependence of Spiral Chirality (DESI + DESIVAST)

**Version:** v0.1.77-2026-06-13 (EXT11-closure submission version | PDF md5: e5a3999a | 32pp)
**Prepared:** 2026-06-13 (HD-11 DO-NOW directive) | **Updated:** EXT11-closure-wave 2026-06-13
**Submission order:** LAST (after P4 arXiv ID is minted; P5 inserts it into the manuscript)

---

## 1. Title

Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample

*Note: The NM1 ruling (P5-NM1 open Houston-decision) may update the title count from "791,635" to "783,820 Environment-Matched DR1 Spirals". Confirm with Houston before finalizing the Zenodo title — whichever version is in the submitted manuscript is the correct one to use here.*

---

## 2. Authors

| Name | Email | Affiliation |
|------|-------|-------------|
| Houston Golden | houston@hubify.com | Independent Researcher, Los Angeles, California, USA |

---

## 3. Description (Abstract)

We cross-match the 8,474,531-galaxy chirality catalog of Paper IV with the DESI Data Release 1 redshift catalog (16.36 million ZWARN=0 input rows) to test whether spiral galaxy handedness is statistically independent of large-scale structure environment. The primary path is the DESIVAST-anchored void cross-check using three algorithms (VoidFinder sphere-growing, V2-REVOLVER, and V2-VIDE watershed); the V-Web tidal classification on 14,622,283 DR1 spectroscopic galaxies is the supporting cross-check across the full matched sample. The 1-arcsecond matched catalog contains 2,232,212 unique galaxies; of these, 791,635 carry an unambiguous post-TTA equivariant CW or CCW label. We classify each matched spiral into one of four cosmic-web classes {void, wall, filament, cluster} using a tidal-tensor cosmic-web classifier (Hahn et al. 2007; Cautun et al. 2014) on a 256^3 comoving grid with 25 Mpc/h Gaussian smoothing. Sample ledger: (1) DESIVAST primary: 56,981 k=20 VoidFinder void spirals drawn from 678,945 z <= 0.24 matched spirals; (2) V-Web secondary: 783,820 unique chirality-relevant matched spirals with an environment row. Headline result: the CW fraction shows no environment dependence beyond the known Paper IV catalog-wide classifier-monopole systematic of ~0.26 percentage points and the counting-statistics floor. Per-class CW fractions are 0.4980 (filament, n=408,187), 0.4963 (cluster, n=397,505), 0.5034 (wall, n=6,673), and 0.4836 (void, n=428). An omnibus 4x2 homogeneity test is null (chi^2=3.55, 3 d.o.f., p=0.31). A Phase 2 sensitivity sweep across nine cells confirms the result. Additional null tests in redshift (p=0.372), projected density (|sigma|_max=3.94 pre-monopole-subtraction), and sky-position (HEALPix scans at NSIDE in {16,32,64}, p=0.607/0.135/0.413) support the null. The galaxy catalog, model weights, and analysis scripts are released with the companion Paper IV; this paper's environment-classification code and DESIVAST cross-match scripts are released with the arXiv posting.

---

## 4. Keywords

- spiral galaxy chirality
- large-scale structure
- DESI DR1
- cosmic web
- void galaxies
- DESIVAST
- T-Web
- tidal tensor
- environmental dependence
- galaxy handedness
- parity
- bouncing cosmology
- VoidFinder

---

## 5. License

**CC-BY-4.0** (Creative Commons Attribution 4.0 International)

---

## 6. Related Identifiers

| Relation | Identifier | Note |
|----------|-----------|------|
| isSupplementedBy | arXiv:XXXX.XXXXX | **PLACEHOLDER — insert real P5 arXiv ID after submission** |
| isPartOf | arXiv:XXXX.XXXXX (P4) | **BLOCKING — insert P4 arXiv ID before P5 upload** |
| isPartOf | arXiv:XXXX.XXXXX (P1A) | ECH no-go companion |
| isReferencedBy | https://huggingface.co/bamfai/galaxy-chirality-v2 | Parent catalog model weights (Paper IV) |
| isReferencedBy | https://zenodo.org/record/10.5281/zenodo.19358024 | ASTRA-DESI EDR (Zenodo 19358024, 4.4 GB) used in per-object cross-validation |

---

## 7. File Manifest

Files Houston should upload to Zenodo:

**Paper source files:**

| File | Path | Description |
|------|------|-------------|
| `paper5_arxiv_v0.1.77-2026-06-13.tar.gz` | `project-context/SSOT/arxiv_tarballs/paper5_arxiv_v0.1.77-2026-06-13.tar.gz` | **PRIMARY — arXiv submission tarball (EXT11-closure; PDF md5 e5a3999a)** |
| `p5_desi_chirality.pdf` | `pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` | Compiled PDF (32pp; v0.1.77-2026-06-13) |
| `p5_desi_chirality.tex` | `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` | LaTeX source |

**Analysis output artifacts:**

| File | Path | Description |
|------|------|-------------|
| `16_cosmic_web_zshell_corrected.json` | `pipelines/p5_desi_chirality/outputs/16_cosmic_web_zshell_corrected.json` | z-shell corrected cosmic-web results |
| `29_ext3_desivast_footprint_retabulation.json` | `pipelines/p5_desi_chirality/outputs/29_ext3_desivast_footprint_retabulation.json` | DESIVAST footprint retabulation |
| `30_ext4_galzone_complement_contrasts.json` | `pipelines/p5_desi_chirality/outputs/30_ext4_galzone_complement_contrasts.json` | Galzone complement contrasts |
| `31_ext5_appendixB_tables.json` | `pipelines/p5_desi_chirality/outputs/31_ext5_appendixB_tables.json` | Appendix B tables |

**Environment-classification scripts:**

| File | Path | Description |
|------|------|-------------|
| `env_finder/` | `pipelines/p5_desi_chirality/env_finder/` | T-Web tidal-tensor classifier (DESI DR1 V-Web recipe) |
| `scripts/` | `pipelines/p5_desi_chirality/scripts/` | DESIVAST cross-match and analysis scripts (incl. script 15: ASTRA-DESI per-object cross-validation) |

**Manifest count: 3 paper files + 4 output JSONs + 2 script directories = 9 local file entries**

*Note: The NM1 title ruling (open Houston-decision) may trigger a Fig 3 regen before final submission. If so, rebuild a post-NM1-ruling tarball and upload that version instead of v0.1.77-2026-06-13.*

---

## 8. Communities

- `astrophysics`
- `cosmology-and-nongalactic-astrophysics`

---

## 9. Funding

**None** — Independent research, no grant funding.

---

## 10. Version

`v0.1.77-2026-06-13` (EXT11-closure | PDF md5: e5a3999a | 32pp)

*NM1 ruling may still force a bump; use this version unless Houston rules otherwise.*

---

## 11. Click-Publish Steps

1. **Log into zenodo.org** → click "New upload". **Wait until P4's arXiv ID is in hand** (~1 hour after P4 upload) before proceeding with P5.
2. **Drop files:** drag in `paper5_arxiv_v0.1.77-2026-06-13.tar.gz` + `p5_desi_chirality.pdf` + the output JSONs (zip as `p5_analysis.zip`) + zip the `env_finder/` and `scripts/` directories as `p5_code.zip`.
3. **Paste metadata:** Title (with NM1-ruled count), Description, Keywords, License (CC-BY-4.0), Authors, Communities, and Related Identifiers (including P4's real arXiv ID) from sections 1-9 above.
4. **Reserve DOI:** click "Reserve DOI" — copy and insert the DOI into P5's companion-reference markers. Also insert P4's real arXiv ID at the `TODO-SUBMISSION` companion-reference markers in the P5 source before the final compile (BLOCKING dependency).
5. **Publish:** click "Publish". After arXiv assigns P5's ID, run `v3_bundled_paper_bump.mjs` for the final Convex sync of all 6 arXiv IDs.
