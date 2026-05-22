# arXiv submission tarballs — full portfolio (all 6 papers)

Standalone-tested arXiv-ready submission bundles. Every tarball was
smoke-tested by extracting into an empty temp directory and running
`pdflatex -interaction=nonstopmode` 2–3 times to confirm clean compilation
with **0 undef refs / 0 undef cites** before being archived here.

Built across cron fires #28 + #29 + #36 (2026-05-22 PDT, ticks 149–157). P5 tarball rebuilt at fire #36 after v0.1.7 → v0.1.10 added §sec:tweb_compare with T-Web + ASTRA + DESIVAST cross-citations.

| Paper | Tarball | Size | Files | Smoke-test PDF | Refs/cites |
|---|---|---:|---:|---|:---:|
| **P1A** v1A.0.35 | `p1a_v1A.0.35_arxiv.tar.gz` | 433 KB | 5 | 20 pp / 832 KB | 0 / 0 |
| **P1B** v1B.0.22 | `p1b_v1B.0.22_arxiv.tar.gz` | 255 KB | 4 | 11 pp / 694 KB | 0 / 0 |
| **P2** v1.7.33 | `p2_v1.7.33_arxiv.tar.gz` | 346 KB | 9 | 21 pp / 817 KB | 0 / 0 |
| **P3** v3.1.62 | `p3_v3.1.62_arxiv.tar.gz` | 27 MB | 23 | 47 pp / 28.4 MB | 0 / 0 |
| **P4** v1.0.128 | `p4_v1.0.128_arxiv.tar.gz` | 20 MB | 15 | 51 pp / 26 MB | 0 / 0 |
| **P5** v0.1.13 | `p5_v0.1.13_arxiv.tar.gz` | 443 KB | 8 | 23 pp / 759 KB | 0 / 0 |

Bibliography mechanisms:
- **P1A / P1B / P2 / P5** ship `.tex` + `.bib` + pre-resolved `.bbl` (arXiv
  prefers `.bbl` over re-running BibTeX server-side).
- **P3 / P4** use inline `\begin{thebibliography}` blocks; no `.bib` needed.

## Submission workflow (Houston, when ready)

1. Sign off the relevant paper (commit message containing `sign off P1A`,
   `sign off P1B`, `sign off P2`, `sign off P3`, `sign off P4`, or
   `sign off P5`).
2. Upload the corresponding tarball to https://arxiv.org/submit
3. Verify arXiv preview matches the local PDF in `public/papers/`.
4. Submit; the announcement schedule is the next 20:00 UTC.

If you want a re-bundle at a newer version after sign-off (e.g., to
include a sign-off-day Author Note), drop a one-liner and the cron will
rebuild and replace the tarball in the same single-purpose commit.

## Maturity at time of packaging

| Paper | R-round campaign maturity | arXiv-ready stance |
|---|---|---|
| P1A | Cascaded-loop exit (R15+R16+R24 3-consec 5/5 clean) | **READY** |
| P1B | First fully-clean compile (cron fire #23); new R-round blocked on OR cap | Sign-off prep — defer arXiv submission until OR-blocked R-round can fire |
| P2 | First fully-clean compile (cron fire #21); new R-round blocked on OR cap | Sign-off prep — defer arXiv submission until OR-blocked R-round can fire |
| P3 | First fully-clean compile (cron fire #24); new R-round blocked on OR cap | Sign-off prep — defer arXiv submission until OR-blocked R-round can fire |
| P4 | R22 3-of-5 + R23 5-of-5 clean | **READY** |
| P5 | Never been through R-round (paper just drafted) | Tarball is for future reference; not yet review-mature |

P1A and P4 are the two that can ship the moment Houston signs off.
P1B / P2 / P3 / P5 are pre-packaged so the path from sign-off to upload
stays a single step once their R-round campaigns close.

## Tarball provenance

Each tarball was built from the canonical source path documented in
`project-context/SSOT/paper-N/status.md` and smoke-tested in an empty
`/tmp/arxiv_*_submit/` working directory. No live-repo aux-state leakage.

`.tar.gz` files are gitignored (size); this README is tracked.
