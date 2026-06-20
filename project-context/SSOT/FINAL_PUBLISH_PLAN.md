# Final Publishing Plan — bigbounce 6-paper portfolio

**Date:** 2026-06-20 PST
**Status:** ✅ Science R-rounds + **D-round (visual)** + **P-round (packaging)** all complete. Tarballs built + standalone-compile-verified, site cohesive, external artifacts linked. Readiness **99** on 5 papers; **P1B held at 98** pending one HF flip (below). The final 1% → 100 is your sign-off.
**Bottom line:** Everything I can do is done. What remains is **4 actions, all yours**: flip P1B's 3 HF datasets public, flip ORCID public, sign off, submit. DOIs mint at the drop.

---

## 1. Final paper state (post R→D→P)

| # | Paper | Version | md5 (PDF) | pp | Readiness | arXiv (primary / cross) |
|---|-------|---------|-----------|----|-----------|----|
| P4 | Galaxy chirality catalog | v1.0.188 | `c47abc18` | 23 | **99** | astro-ph.GA / astro-ph.CO |
| P1A | ECH dark-energy no-go | v1A.0.79 | `fad68a47` | 29 | **99** | astro-ph.CO / gr-qc, hep-th |
| P1B | MCMC / ALP companion | v1B.0.75 | `b166f4c0` | 21 | **98** ⬅ HF gate | astro-ph.CO / hep-ph |
| P3 | Multi-survey anomaly catalog | v3.1.113 | `7c935f19` | 29 | **99** | astro-ph.CO / astro-ph.GA |
| P2 | f_NL sensitivity forecast | v1.7.71 | `4667e9e2` | 28 | **99** | astro-ph.CO / astro-ph.IM |
| P5 | DESI chirality environment | v0.1.83 | `b65b3ac4` | 33 | **99** | astro-ph.CO / astro-ph.GA |

Tarballs (standalone-compile-verified, in `project-context/SSOT/arxiv_tarballs/`):
`paper4_arxiv_v1.0.188.tar.gz` · `paper1a_arxiv_v1A.0.79.tar.gz` · `paper1b_arxiv_v1B.0.75.tar.gz` · `paper3_arxiv_v3.1.113.tar.gz` · `paper2_arxiv_v1.7.71.tar.gz` · `paper5_arxiv_v0.1.83-2026-06-13.tar.gz`

---

## 2. What the rounds did

- **R-round (science):** R40 internal 5-model + EXT20 external — all 6 ACCEPT, zero blockers.
- **D-round (visual):** D1 production-editor review + fixes (full-width tables/figures, new P1A 14-barrier schematic, P5 colorbar-overlap fix + pie→bar + panel labels + path-ID appendix, abstract splits) → **D2 confirmation CLEAN, 0 regressions**.
- **P-round (packaging):** tarballs rebuilt + standalone-verified; PDFs mirrored (md5-matched); `/site-cohesion-sweep` ran (site cohesive); public HF datasets/models wired into the site; external links (GitHub, repro) resolve.

---

## 3. ✅ Your final checklist (4 actions — everything else is done)

- [ ] **(A) Flip P1B's 3 HuggingFace datasets to public** — the only gate holding P1B at 98:
  `Hubify/p1b-alp-chains`, `Hubify/p1b-mcmc-diagnostics`, `Hubify/p1b-namaster-artifacts` (currently 401). Until public, P1B isn't byte-level reproducible by a referee. Once flipped, tell me and P1B climbs to 99 + I wire the links. (P3/P4/P5 datasets + the P4 model are already public and linked.)
- [ ] **(B) Flip ORCID `0009-0008-3617-8729` to public** — Settings → Visibility → Public. Verify:
  ```
  curl -s -o /dev/null -w "%{http_code}\n" https://pub.orcid.org/v3.0/0009-0008-3617-8729/person
  ```
  must return **200** (currently 404).
- [ ] **(C) Sign off** — record your sign-off in this file / `SIGNOFF_ACCEPT`; that awards the final 1% (99→100).
- [ ] **(D) Submit to arXiv** in order **P4 → P1A → P1B → P3 → P2 → P5** (P4 first — P5 cross-references P4's arXiv ID; wait ~60 min for P4's ID before P5). For each: upload tarball → paste abstract → set categories (§1) → link ORCID → submit. Steps in `ARXIV_SUBMISSION_RUNBOOK.md`.

**Submission-day (during D):** mint 6 Zenodo DOIs (one per paper; interim release-tag handles are in the sources); flip the HF anomaly/chirality dataset cards' visibility check at P3/P4 posting (already public).

---

## 4. Notes / final considerations

- **The 99 vs 98 split is intentional and honest** — P1B's reproducibility package is incomplete only because its 3 chains sit private on HF; that's a one-click fix on your end, not a paper defect.
- **No paper reads 100 until you sign off** — per `readiness-cap-99`. The DOIs are correctly deferred to submission and do not block readiness.
- **R→D→P is now an official, self-improving, globally-synced protocol** (`/paper-design-round`, `/paper-packaging-round`, `/site-cohesion-sweep`) — applies to all future papers.

## 5. Provenance
- Reviews: `project-context/peer-reviews/{R40,EXT20,D1,D2}_*` + truth-audits
- Patterns: `project-context/review-patterns/` (`pattern-*` / `dpattern-*` / `ppattern-*` / `spattern-*`)
- Dashboard: `SSOT/index.md` (top, 2026-06-20) · Site timeline: `reviewTimeline.ts`
