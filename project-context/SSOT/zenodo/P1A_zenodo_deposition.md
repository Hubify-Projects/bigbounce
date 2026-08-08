# P1A deposit specification — v1A.0.123

**State:** exact source package verified; deposit metadata intentionally blocked on license authorization. No DOI is reserved, no archive is published, and no submission or acceptance is claimed.

## Exact release identity

- Target commit: `05746dc56fb09f0800c13db56905af570eee2cfe`
- Manuscript: `arxiv/paper1a_ech_nogo.tex`; SHA-256 `e08323215579b843a43d6288643f339442560da45bd3ffd91a762dcfb1702233`
- PDF: `arxiv/paper1a_ech_nogo.pdf`; 7 pages; SHA-256 `4c450a6706b2f4e53faac5ffbc6ec720f21e45c7406aa7186ef830f3fef33f71`
- Source bundle: `project-context/SSOT/arxiv_tarballs/paper1a_arxiv_v1A.0.123.tar.gz`; SHA-256 `c147269c37359247bd5cbb34648783b6056f81a5c7cd4f66f55b291a4b0d1662`
- Standalone proof: `project-context/SSOT/arxiv_tarballs/paper1a_arxiv_v1A.0.123.proof.json`

The deterministic bundle contains the exact TeX, the closure-round BBL, and `references.bib`. Isolated Tectonic 0.16.9 compilation produced 7 pages with zero errors, undefined references, or overfull boxes; all 7 rendered pages passed visual inspection.

## Metadata blocker

The live P1A manuscript does not declare a license. The obsolete deposition note asserted CC BY 4.0 without evidence; that assertion is withdrawn. `tools/prepare_paper_deposit.py` therefore fails closed until Houston chooses and authorizes the manuscript/source license. No reversible GitHub draft or Zenodo-ready metadata is created before that decision.

## Remaining publication gates

1. Houston authorizes the license.
2. Regenerate validated metadata and a checksummed staging package.
3. Optionally create a reversible draft and verify every remote digest.
4. Reserve/publish a DOI only with explicit confirmation.
5. Complete human CQG/editorial submission and review.

Readiness remains **62**.
