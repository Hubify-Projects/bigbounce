# P3 deposit specification — v3.2.0-r8

**State:** verified exact-commit candidate retained in a reversible GitHub draft. No DOI is reserved, no immutable archive is published, and no arXiv or journal submission/acceptance is claimed.

## Exact release identity

- Target commit: `05746dc56fb09f0800c13db56905af570eee2cfe`
- Title: *Public-ID Recovery for a Historical DESI DR1 Anomaly List: 170 High-Coordinate-Consistency Core and 11 Lower-Confidence Positional Associations*
- Manuscript: `pipelines/p3_anomaly_engine/paper3_apjs.tex`; SHA-256 `2b9a5fd356e49ae7a9939cbf8e9197379bef71b1f66a0e364e0de41ae416d10b`
- PDF: `pipelines/p3_anomaly_engine/paper3_apjs.pdf`; 16 pages; SHA-256 `b5f254f92b10bda43b687f07c5f58b828a6f7dc70d98c08f9e9b609edbba08b0`
- Source bundle: `project-context/SSOT/arxiv_tarballs/paper3_apjs_arxiv_v3.2.0-r8.tar.gz`; SHA-256 `8354213e1d674af9662ee438db1c2d00ad333d40cf7f007c997f8f0632f4ebd2`
- Standalone proof: `project-context/SSOT/arxiv_tarballs/paper3_apjs_arxiv_v3.2.0-r8.proof.json`
- Draft receipt: `project-context/SSOT/github-releases/P3_v3.2.0-r8_draft_release_receipt.json`

The deterministic bundle contains the exact manuscript, three exact figures, and the hash-pinned AASTeX class. Isolated Tectonic 0.16.9 compilation produced 16 pages with zero errors and zero undefined references. One 1.82327 pt overfull hbox is retained as an explicit minor typesetting warning; all 16 rendered pages show no clipping or column overlap.

## Draft assets

The draft contains the TeX, PDF, source tarball, standalone proof, deterministic 75-file tracked-provenance archive, manifest, `SHA256SUMS`, and validated Zenodo metadata. All eight GitHub asset digests match local bytes exactly. The local hidden `.zenodo.json` asset is normalized by GitHub CLI to `default.zenodo.json`.

Data and documentation metadata use CC BY 4.0; code retains the repository license. Placeholder related identifiers are omitted rather than fabricated.

## Remaining publication gates

1. Resolve the minor overfull line during the next versioned manuscript edit, if it can be done without destabilizing the exact release.
2. Houston decides when to reserve/publish the DOI and submit to arXiv/ApJS.
3. Re-run exact checks after any DOI or manuscript edit.
4. Complete human ApJS/editorial review.

Readiness remains **56**.
