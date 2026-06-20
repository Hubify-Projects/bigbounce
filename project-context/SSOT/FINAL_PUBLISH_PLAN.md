# Final Publishing Plan — bigbounce 6-paper portfolio

**Date:** 2026-06-20 PST
**Status:** ✅ R→D→P all complete. **All six papers at readiness 99.** Tarballs standalone-verified, PDFs mirrored, site cohesive, every external artifact (HuggingFace datasets+models, GitHub source, reproducibility) resolving. The final 1% → 100 is your sign-off.
**Bottom line:** Everything autonomously doable is done — including publishing P1B's 3 reproducibility datasets to HuggingFace and fixing its dead links. **Only 3 actions remain, all genuinely yours: flip ORCID public, sign off, submit.** DOIs mint at the drop.

---

## 1. Final paper state (post R→D→P, all 99)

| # | Paper | Version | md5 (PDF) | pp | Readiness | arXiv (primary / cross) |
|---|-------|---------|-----------|----|-----------|----|
| P4 | Galaxy chirality catalog | v1.0.188 | `c47abc18` | 23 | **99** | astro-ph.GA / astro-ph.CO |
| P1A | ECH dark-energy no-go | v1A.0.79 | `fad68a47` | 29 | **99** | astro-ph.CO / gr-qc, hep-th |
| P1B | MCMC / ALP companion | v1B.0.76 | `9d2974c2` | 21 | **99** ✓ reproducible | astro-ph.CO / hep-ph |
| P3 | Multi-survey anomaly catalog | v3.1.113 | `7c935f19` | 29 | **99** | astro-ph.CO / astro-ph.GA |
| P2 | f_NL sensitivity forecast | v1.7.71 | `4667e9e2` | 28 | **99** | astro-ph.CO / astro-ph.IM |
| P5 | DESI chirality environment | v0.1.83 | `b65b3ac4` | 33 | **99** | astro-ph.CO / astro-ph.GA |

Tarballs (standalone-compile-verified, in `project-context/SSOT/arxiv_tarballs/`):
`paper4_arxiv_v1.0.188` · `paper1a_arxiv_v1A.0.79` · `paper1b_arxiv_v1B.0.76` · `paper3_arxiv_v3.1.113` · `paper2_arxiv_v1.7.71` · `paper5_arxiv_v0.1.83-2026-06-13` (.tar.gz).

---

## 2. Reproducibility / artifacts — COMPLETE
- **Datasets (HuggingFace, all public + linked from the site):** P3 `bamfai/bigbounce-anomaly-catalog`; P4 `bamfai/galaxy-chirality-catalog`; P5 reuses P4's; **P1B `bamfai/p1b-alp-chains` + `p1b-mcmc-diagnostics` + `p1b-namaster-artifacts` (published this session; Appendix A links corrected Hubify→bamfai in v1B.0.76).**
- **Model (HuggingFace, public + linked):** P4 `bamfai/galaxy-chirality-v2`.
- **Code + reproducibility:** GitHub `Hubify-Projects/bigbounce` + the cited chains/configs/notebooks all resolve.
- **DOIs:** mint at submission (interim release-tag handles in the sources) — the only deferred item, by design.

---

## 3. ✅ Your final checklist — 3 actions

- [ ] **(A) Flip ORCID `0009-0008-3617-8729` to public** — Settings → Visibility → Public. Verify:
  ```
  curl -s -o /dev/null -w "%{http_code}\n" https://pub.orcid.org/v3.0/0009-0008-3617-8729/person
  ```
  must return **200** (currently 404). *I've re-armed a 30-min watcher that pings the moment it flips.*
- [ ] **(B) Sign off** — record your sign-off here / in `SIGNOFF_ACCEPT`; that awards the final 1% (99→100).
- [ ] **(C) Submit to arXiv** in order **P4 → P1A → P1B → P3 → P2 → P5** (P4 first — P5 cross-refs P4's ID; wait ~60 min for P4's ID before P5). Per paper: upload tarball → paste abstract → set categories (§1) → link ORCID → submit. Full steps: `ARXIV_SUBMISSION_RUNBOOK.md`.
  - **Submission-day:** mint the 6 Zenodo DOIs as part of the drop.

---

## 4. Notes
- **No paper reads 100 until you sign off** (per `readiness-cap-99`). I cannot self-award the final 1% — that's the design.
- **R→D→P is an official, self-improving, globally-synced protocol** (`/paper-design-round`, `/paper-packaging-round`, `/site-cohesion-sweep`) for all future papers.

## 5. Provenance
- Reviews: `project-context/peer-reviews/{R40,EXT20,D1,D2}_*` + truth-audits
- Patterns: `project-context/review-patterns/` (`pattern-*` / `dpattern-*` / `ppattern-*` / `spattern-*`)
- Dashboard: `SSOT/index.md` · Site: `reviewTimeline.ts` · Runbook: `ARXIV_SUBMISSION_RUNBOOK.md`
