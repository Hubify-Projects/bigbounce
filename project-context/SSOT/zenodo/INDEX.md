# Deposit readiness — BigBounce six-paper portfolio

**Audited:** 2026-07-15. All six papers remain **IN REVISION**. This directory previously claimed that obsolete June versions were “one-click ready”; that claim was false for the current manuscripts and is withdrawn.

| Paper | Current version | Readiness | Current PDF | Deposit state |
|---|---:|---:|---|---|
| P1A | v1A.0.123 | 62 | 7 pp; SHA-256 `4c450a67…3f71` | Current-version deposit package not yet prepared; DOI and human CQG gates open |
| P1B | v1B.0.109 | 56 | 20 pp; SHA-256 `36b8fc98…4a78` | Corrected 500-MC physical-spectrum result still absent; current-version deposit package not prepared |
| P2 | v1.7.122 | 74 | 10 pp; SHA-256 `4097bac5…25c9` | Current-version package not prepared; direct transfer/covariance, DOI, and human PRD gates open |
| P3 | v3.2.0-r8 | 56 | 16 pp; MD5 `8faac098b5f4cde3133937460b8df4c5` | Current-version package not prepared; DOI/archive and human ApJS gates open |
| P4 | v1.0.252 | 80 | 28 pp; SHA-256 `a109f3d1…3292` | **Verified exact-commit candidate in reversible GitHub draft; no DOI reserved or archive published** |
| P5 | v0.1.133-2026-07-14 | 74 | 39 pp; SHA-256 `db18dd93…764` | Current-version package not prepared; Paper-IV provenance, selection products, DOI, and human AJ gates open |

## P4 evidence

- Exact science target: `8cb975c37ac27bea5c1c7fda2a10274b80623128`.
- Draft-release receipt: [`../github-releases/P4_v1.0.252_draft_release_receipt.json`](../github-releases/P4_v1.0.252_draft_release_receipt.json).
- Deposit specification: [`P4_zenodo_deposition.md`](P4_zenodo_deposition.md).
- Standalone source proof: [`../arxiv_tarballs/paper4_arxiv_v1.0.252.proof.json`](../arxiv_tarballs/paper4_arxiv_v1.0.252.proof.json).
- The 90-file tracked-provenance archive excludes ignored/untracked large shards and is content-addressed in the receipt.

## Accelerated, fail-closed workflow

`tools/prepare_paper_deposit.py` now binds a package to a full Git commit and manuscript version; requires byte-identical tracked TeX, PDF, source bundle, proof, and provenance inputs; validates the PDF and standalone compile; generates a deterministic provenance archive, manifest, checksums, and placeholder-free Zenodo metadata; writes only to ignored staging unless `--write` is explicit; and never mutates GitHub, Zenodo, arXiv, or journal state.

Next, add current paper-specific configurations for archive-unblocked P1A and P3 and prepare reversible drafts. Final Zenodo publication remains confirmation-gated because it is immutable.
