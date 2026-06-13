# Zenodo Deposition Record — P1B
## Paper: Technical Verification Companion to the ECH Spin-Torsion Program

**Version:** v1B.0.65
**Prepared:** 2026-06-13 (HD-11 DO-NOW directive)

---

## 1. Title

Technical Verification Companion to the ECH Spin-Torsion Program: Lambda-CDM + Delta-N_eff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model

---

## 2. Authors

| Name | Email | Affiliation |
|------|-------|-------------|
| Houston Golden | houston@hubify.com | Independent Researcher, Los Angeles, California, USA |

---

## 3. Description (Abstract)

We report the technical verification material for the Einstein-Cartan-Holst (ECH) spin-torsion cosmology no-go program of Paper I(a). Three analyses are documented. (1) Stock-CAMB Lambda-CDM + Delta-N_eff MCMC proxy (Cobaya v3.6.1, 309,189 frozen samples across two converged dataset combinations): this run uses stock CAMB with Delta-N_eff as a free parameter and carries no torsion modifications to the Boltzmann equations; it is reported as a null-consistency test of an extra radiation-like degree of freedom, not as evidence for or against the ECH spin-torsion framework. Both frozen dataset combinations find Delta-N_eff consistent with zero (-0.020 +/- 0.169 full-tension; +0.058 +/- 0.179 Planck+BAO+SN) and H0 consistent with the standard Planck-Lambda-CDM value. (2) NaMaster pseudo-C_ell pipeline validation on synthetic Lambda-CDM CMB polarization skies with an ACT-like footprint mask (N_side=512, ell_max=1024, f_sky=0.32, 10 uK-arcmin white noise, 500 Monte Carlo realizations): injecting the spectator-ALP fiducial value beta=0.27 deg recovers beta_hat=0.238 deg. The scope of this validation is the algebraic pseudo-C_ell E->B deconvolution under MASTER mode coupling; it is not a physical separation of cosmic-rotation from instrumental-miscalibration angle. (3) Spectator-ALP consistency check: for a field with f_a ~M_Pl, the scan-prior m~H_0 region brackets the published joint WMAP+Planck signal beta=0.342 +/- 0.094 deg (3.6 sigma), but the posterior-supported fixed-coupling accommodation shifts to m >> H_0. The same birefringence arises in standard GR with an identical ALP; it is not a distinctive ECH prediction. A reproducibility manifest is included in Appendix A.

---

## 4. Keywords

- MCMC
- Cobaya
- NaMaster
- cosmic birefringence
- axion-like particle
- spin-torsion cosmology
- Lambda-CDM
- dark energy
- bouncing cosmology
- CMB polarization
- reproducibility
- Einstein-Cartan-Holst gravity

---

## 5. License

**CC-BY-4.0** (Creative Commons Attribution 4.0 International)

---

## 6. Related Identifiers

| Relation | Identifier | Note |
|----------|-----------|------|
| isSupplementedBy | arXiv:XXXX.XXXXX | **PLACEHOLDER — insert real arXiv ID after submission** |
| isPartOf | arXiv:XXXX.XXXXX (P1A) | Primary ECH no-go paper — insert P1A arXiv ID (minted first) |
| isReferencedBy | arXiv:XXXX.XXXXX (P2) | fnl forecast companion |

---

## 7. File Manifest

Files Houston should upload to Zenodo:

| File | Path | Description |
|------|------|-------------|
| `paper1b_arxiv_v1B.0.65.tar.gz` | `arxiv/paper1b_arxiv_v1B.0.65.tar.gz` | **PRIMARY — arXiv submission tarball** |
| `paper1b_mcmc_companion.pdf` | `arxiv/paper1b_mcmc_companion.pdf` | Compiled PDF (22pp) |
| `paper1b_mcmc_companion.tex` | `arxiv/paper1b_mcmc_companion.tex` | LaTeX source |

**MCMC chain data** (in `reproducibility/`):

| File | Path | Description |
|------|------|-------------|
| `p1_namaster_500mc/` | `reproducibility/p1_namaster_500mc/` | 500-MC NaMaster pipeline validation realizations |
| `cosmology/` | `reproducibility/cosmology/` | Cobaya MCMC chains (Planck+BAO+SN; full-tension) |

**Manifest count: 3 paper files + 2 reproducibility directories**

*Note: The planck_bao_sn parameter_summary_CORRECTED.json and units README were added at v1B.0.57 and live under `reproducibility/`. Check `reproducibility/cosmology/` for the canonical chain artifacts before uploading.*

---

## 8. Communities

- `astrophysics`
- `cosmology-and-nongalactic-astrophysics`

---

## 9. Funding

**None** — Independent research, no grant funding.

---

## 10. Version

`v1B.0.65`

---

## 11. Click-Publish Steps

1. **Log into zenodo.org** → click "New upload".
2. **Drop files:** drag in `paper1b_arxiv_v1B.0.65.tar.gz` + `paper1b_mcmc_companion.pdf` + the `reproducibility/cosmology/` and `reproducibility/p1_namaster_500mc/` chain bundles (zip them first if needed: `zip -r p1b_chains.zip reproducibility/cosmology/ reproducibility/p1_namaster_500mc/`).
3. **Paste metadata:** Title, Description, Keywords, License (CC-BY-4.0), Authors, Communities from sections 1-9 above. Set Upload type = "Publication" → "Preprint".
4. **Reserve DOI:** click "Reserve DOI" — copy and insert the minted DOI into P1B's App A "pending DOI assignment" placeholder before final compile. Also insert P1A's arXiv ID (minted before P1B) into the companion reference `\cite{Golden2026P1a}`.
5. **Publish:** click "Publish". Copy DOI → update DATA_RELEASE_MANIFEST.md (if referenced from P3) and insert into subsequent papers (P3, P2, P5) at their companion-reference markers.
