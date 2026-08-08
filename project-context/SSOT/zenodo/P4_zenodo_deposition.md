# P4 deposit record — v1.0.252

> **SUPERSEDED DRAFT — DO NOT PUBLISH AS CURRENT.** The reversible GitHub draft
> below remains bound to v1.0.252. The current v1.0.255 source bundle and isolated
> 29-page proof are recorded in
> [`../arxiv_tarballs/paper4_arxiv_v1.0.255.proof.json`](../arxiv_tarballs/paper4_arxiv_v1.0.255.proof.json).
> No current-version Zenodo draft, DOI, arXiv submission, or journal submission
> exists.

**State:** verified deposit candidate in a reversible GitHub draft. **No DOI has been reserved, no Zenodo record has been published, and no arXiv or journal submission has occurred.** Publication readiness remains 80.

## Exact release identity

| Field | Verified value |
|---|---|
| Version | `v1.0.252` |
| Science commit | `8cb975c37ac27bea5c1c7fda2a10274b80623128` |
| PDF | 28 pages; 25,168,862 bytes |
| PDF SHA-256 | `a109f3d150ff02107bc10bc7dec576ad28b0157081b3e521da86e7c06ade3292` |
| PDF MD5 | `7231d1d1e773b48c37718d7636303f00` |
| arXiv bundle SHA-256 | `1fe38151c4f096846b68c0c3de77c4a9f18a640241d7f52f360f1b87312ae2f1` |
| Standalone compile | Tectonic 0.16.9; 28 pages; 0 errors; 0 undefined references |
| Draft release | database ID `354600688`; tag intent `paper4-v1.0.252`; exact science target above |

The machine-readable draft-release receipt is [`../github-releases/P4_v1.0.252_draft_release_receipt.json`](../github-releases/P4_v1.0.252_draft_release_receipt.json). The standalone proof is [`../arxiv_tarballs/paper4_arxiv_v1.0.252.proof.json`](../arxiv_tarballs/paper4_arxiv_v1.0.252.proof.json).

## Deposit metadata

**Title:** An Observed-Label Chirality-Dipole Null in 949,584 High-Confidence DESI Spirals and an 8.5-Million-Galaxy Catalog

**Creator:** Houston Golden, Independent Researcher, Los Angeles, California, USA (`houston@hubify.com`)

The previously listed ORCID is deliberately omitted: the public ORCID API did not verify that record on 2026-07-15. It may be added only after a public-registry check succeeds.

**Abstract:** We release observed chirality labels for 8,474,531 DESI Legacy DR8 galaxies and test one primary high-confidence observed-label dipole. Of 949,584 selected spirals, 947,326 enter the supported-pixel fit and fixed-occupancy label-randomization null; the result is consistent with zero (`z=+0.71`, one-sided rank `p=0.225`). The content-addressed release includes the science catalog, unsafe-row quarantine, retained primary-null array, schema, checksums, and reproducer. WLS and harmonic analyses use different supports or nulls and are retained only as systematics diagnostics. Spatial transfer calibration, joint covariance, an independent matched-footprint estimator, a complete systematics-metadata sidecar, and a DOI-backed archive remain open. The parity-even morphology observable supports no primordial-parity bound.

**Upload type:** publication / article. **Access:** open. **License:** CC BY 4.0.

No placeholder DOI, arXiv identifier, or unverified related identifier is present in the generated metadata.

## Verified draft assets

| Asset | SHA-256 |
|---|---|
| `chirality_catalog_paper.pdf` | `a109f3d150ff02107bc10bc7dec576ad28b0157081b3e521da86e7c06ade3292` |
| `chirality_catalog_paper.tex` | `384bdf938fdce91b7bdc42422d8a0c9f4d56c6ed2abca113df9880d0f4fcd646` |
| `paper4_arxiv_v1.0.252.tar.gz` | `1fe38151c4f096846b68c0c3de77c4a9f18a640241d7f52f360f1b87312ae2f1` |
| `paper4_arxiv_v1.0.252.proof.json` | `d30af5f7af4b2c5482b1a814696fbb760b13e0a44ac60e1dda5d5f9e37d09594` |
| `P4_v1.0.252_tracked_provenance.tar.gz` (90 tracked files) | `72e1f56edf7962eb329f91eaa1459cacbf60d5deaa6369be2118abc05e956e0e` |
| `manifest.json` | `f73a70a503ac05ba59bb97d50767c2eeb3488b10a74cbf8d8ff944df3d657dc5` |
| `SHA256SUMS` | `9dfb2ed87739cd677a155cf97c2cf89741002339cd301313aec4956c9524726c` |
| `default.zenodo.json` | `5e9422edf15a3645f1d4873823e9093f8275ff29a64dd6c132ec26799c61a194` |

## Remaining irreversible/external steps

1. Houston authenticates Zenodo or supplies a narrowly scoped deposit token.
2. Create a Zenodo **draft** and reserve (but do not publish) a DOI.
3. Insert the real reserved DOI into the manuscript and artifact links, bump the paper, recompile, run the full LaTeX/PDF visual audit, rebuild the source bundle, and repeat exact multi-model confirmation.
4. After Houston's explicit publish decision, publish the immutable archive and only then update public DOI/arXiv links.

The GitHub draft is a reversible preparation artifact. It is not evidence that the scientific, DOI, human-review, arXiv, or journal-acceptance gates are closed.
