# arXiv submission tarballs

Standalone-tested arXiv-ready submission bundles. Each tarball was
smoke-tested by extracting into an empty temp directory and running
`pdflatex -interaction=nonstopmode` twice (P1A) or three times (P4)
to confirm a clean compile with **0 undef refs / 0 undef cites** before
being archived here.

Built 2026-05-22 PDT (cron fire #28, tick 149).

## P1A — `p1a_v1A.0.35_arxiv.tar.gz`

- **Source**: `arxiv/paper1a_ech_nogo.tex` @ v1A.0.35 (cron fire #24
  Holst-dual widetext fix, first fully-clean compile in campaign).
- **Bundle contents** (5 files):
  - `paper1a_ech_nogo.tex`
  - `references.bib`
  - `paper1a_ech_nogo.bbl` (pre-resolved bibliography; arXiv prefers
    the `.bbl` over re-running BibTeX server-side)
  - `fig_theory_map.png`
  - `figures/figure1_lqg_holst_derivation_enhanced.png`
- **Smoke test result**: 20 pp / 832 KB / 0 undef refs / 0 undef cites.
- **Tarball size**: 433 KB.

## P4 — `p4_v1.0.128_arxiv.tar.gz`

- **Source**: `pipelines/p2_chirality/chirality_catalog_paper.tex`
  @ v1.0.128 (R22 5-vendor 3-of-5 0/0 + R23 verification 5/5 0/0;
  bibliography is inline `thebibliography` so no external .bib needed).
- **Bundle contents** (15 files):
  - `chirality_catalog_paper.tex`
  - 14 `fig_*.png` figures (spiral density, gallery CW/CCW, equivariance
    demo, class pie, confidence dist, sky map, multipoles, 2pt
    chirality, hemisphere, sky regions, raw-vs-eq, PSF correlation,
    binned CW fraction)
- **Smoke test result**: 51 pp / 26 MB / 0 undef refs / 0 undef cites
  after 3-pass `pdflatex` (cross-references resolve on pass 3).
- **Tarball size**: 20 MB.

## Submission workflow (Houston, when ready)

1. Sign off the relevant paper (commit message containing `sign off P1A`
   or `sign off P4`).
2. Upload the corresponding tarball to https://arxiv.org/submit
3. Verify arXiv preview matches the local PDF.
4. Submit; the announcement schedule is the next 20:00 UTC.

If you want a re-bundle at a newer version after sign-off (e.g., to
include a sign-off-day Author Note), drop a one-liner and the cron will
rebuild and replace the tarball in the same single-purpose commit.

## What's NOT yet packaged

- **P1B v1B.0.22** — clean compile but R-round campaign less mature than
  P1A; arXiv-tarball deferred until at least one more clean R-round.
- **P2 v1.7.33** — same reasoning.
- **P3 v3.1.62** — same.
- **P5 v0.1.7** — never been through R-round; not arXiv-ready by definition.
