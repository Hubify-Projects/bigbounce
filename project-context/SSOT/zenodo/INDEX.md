# Zenodo Deposition Index — BigBounce 6-Paper Portfolio
## Prepared: 2026-06-13 | HD-11 DO-NOW | UPDATED: EXT11-closure versions staged

All six deposition records are ready for one-click publish. Houston's action on submission day is: open each PX_zenodo_deposition.md → follow the 5-step "Click-Publish Steps" → done.

**EXT11-closure version bump (2026-06-13):** All tarballs updated to EXT11-closure versions. Canonical tarballs staged at `project-context/SSOT/arxiv_tarballs/`.

---

## Deposition Summary

| Paper | Short Title | Version | PDF MD5 | Pages | Status |
|-------|-------------|---------|---------|-------|--------|
| **P4** (first) | Galaxy Chirality Catalog | v1.0.188 | `c47abc18` | 23 | READY — EXT11-closure |
| **P1A** | ECH No-Go | v1A.0.74 | `3871b587` | 28 | READY — EXT11-closure |
| **P1B** | MCMC Companion | v1B.0.71 | `aa1a694e` | 21 | READY — EXT11-closure |
| **P3** | Multi-Survey Anomaly Catalog | v3.1.108 | `72bd3e5b` | 29 | READY — EXT11-closure (HF flip needed at posting) |
| **P2** | fnl Forecast / SPHEREx | v1.7.65 | `fc42f393` | 28 | READY — EXT11-closure |
| **P5** (last) | DESI Chirality Environment | v0.1.77-2026-06-13 | `e5a3999a` | 32 | READY (awaits P4 arXiv ID + NM1 ruling) |

All 6 tarballs standalone-compile verified (errors=0, undef=0) from EXT11-closure .tex sources. git SHA at build: EXT11-closure-wave commit.

---

## Submission Order (per PUBLISH_PLAN.md)

```
P4 → P1A + P1B (same day) → P3 → P2 → P5
```

**Inter-paper DOI/arXiv dependencies:**
- P1A needs P4's arXiv ID (companion anchor) → insert after P4 posts
- P1B needs P1A's arXiv ID (App A "pending DOI" placeholder) → insert after P1A posts
- P3 needs P1A/P1B arXiv IDs (companion refs) + Zenodo DOI in DATA_RELEASE_MANIFEST.md
- P2 needs P1A/P1B arXiv IDs ("DOI inserted at submission" placeholders)
- P5 needs P4's arXiv ID (BLOCKING — wait ~1 hour after P4 upload before uploading P5)

---

## HuggingFace Dataset Flip (P3 only)

At the moment of P3 arXiv posting:
- Flip `bamfai/bigbounce-anomaly-catalog` from STAGED → public
- URL: https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog
- Contains 9 parquet files (SHA-256 hashes in `DATA_RELEASE_MANIFEST.md`)

---

## HuggingFace Model Tag (P4)

At P4 submission:
- Tag `bamfai/galaxy-chirality-v2` → `v2026.04`
- URL: https://huggingface.co/bamfai/galaxy-chirality-v2
- 5-minute task requiring HF write token (see `.env.local` for `HF_TOKEN`)

---

## Master Submission-Day Runbook

### Morning prep (before any uploads)

- [ ] Resolve P5 NM1 title ruling (791,635 vs 783,820) → if changed, regen Fig 3 → bump from v0.1.77 accordingly
- [ ] Resolve P3 S_BigAE column strip ruling → apply if YES (already at v3.1.108)
- [ ] Resolve P1B SN-overlap chain decision → ship with current framing (recommended)

### P4 upload (Step 1 — first in queue)

- [ ] Open `P4_zenodo_deposition.md`
- [ ] Create GitHub release tag `paper4-v1.0.188` on the submission commit
- [ ] Mint Zenodo deposition → Reserve DOI → re-point `\artifact{}` blob/main links → recompile → upload tarball + PDF + provenance JSONs → Publish
- [ ] Tag HuggingFace model `bamfai/galaxy-chirality-v2` → `v2026.04`
- [ ] Upload P4 tarball to arXiv → wait ~60 min for arXiv ID assignment
- [ ] Note P4 arXiv ID: `arXiv:XXXX.XXXXX`

### P1A + P1B upload (Step 2 — same day as P4)

- [ ] Insert P4 arXiv ID at companion anchors in P1A source
- [ ] Compile P1A → rebuild `paper1a_arxiv_v1A.0.74.tar.gz`
- [ ] Mint P1A Zenodo → Reserve DOI → insert DOI in P1B App A placeholder → Publish
- [ ] Upload P1A to arXiv → note arXiv ID: `arXiv:XXXX.XXXXX`
- [ ] Insert P1A arXiv ID into P1B source → compile → rebuild `paper1b_arxiv_v1B.0.71.tar.gz`
- [ ] Mint P1B Zenodo → Reserve DOI → Publish
- [ ] Upload P1B to arXiv → note arXiv ID: `arXiv:XXXX.XXXXX`

### P3 upload (Step 3)

- [ ] Insert P1A/P1B arXiv IDs into P3 source
- [ ] Insert Zenodo DOI into `DATA_RELEASE_MANIFEST.md` header + tex L44 marker
- [ ] Compile P3 → rebuild `paper3_arxiv_v3.1.108.tar.gz`
- [ ] Mint P3 Zenodo → Reserve DOI → Publish
- [ ] Flip HuggingFace dataset `bamfai/bigbounce-anomaly-catalog` to public
- [ ] Upload P3 to arXiv → note arXiv ID

### P2 upload (Step 4)

- [ ] Insert P1A/P1B arXiv IDs at "DOI inserted at submission" placeholders in P2
- [ ] Optional: targeted in-thread ChatGPT delta-confirm on regenerated figures
- [ ] Create GitHub release tag `paper2-v1.7.65` → Zenodo auto-import → edit metadata → Publish
- [ ] Upload P2 to arXiv → note arXiv ID

### P5 upload (Step 5 — last)

- [ ] Insert P4 arXiv ID into P5 source at `TODO-SUBMISSION` companion-reference markers
- [ ] If NM1 ruled + Fig 3 regenned → bump from v0.1.77-2026-06-13 accordingly; otherwise use v0.1.77-2026-06-13
- [ ] Compile P5 → rebuild tarball
- [ ] Mint P5 Zenodo → Reserve DOI → Publish
- [ ] Upload P5 to arXiv

### Post-all-six

- [ ] Run `v3_bundled_paper_bump.mjs` for final Convex sync with all 6 arXiv IDs
- [ ] Update `SSOT/index.md` with all arXiv IDs
- [ ] Update `site/src/data/papers.ts` with arXiv links
- [ ] Update `DATA_RELEASE_MANIFEST.md` with final Zenodo DOI

---

## Flags for Houston Attention

| Flag | Paper | Detail |
|------|-------|--------|
| DESI DR1 native anomalies (195,829 objects) | P3 | Noted in DATA_RELEASE_MANIFEST.md as hosted in companion GitHub repo, not under pipelines/p3_anomaly_engine/. Confirm accessible and backed up. |
| P1B MCMC chains | P1B | Live in `reproducibility/cosmology/` — confirm these are the `planck_bao_sn parameter_summary_CORRECTED.json` files from v1B.0.57 and are complete (176,240 chain-confirmed samples). |
| P2 phase3_fisher_overlap.json | P2 | Listed in ZENODO_RELEASE_CHECKLIST.md but not confirmed in initial directory listing. Check `research/focused_paper_source_integration/outputs/` before submission. |
| P4 `\artifact{}` links | P4 | All blob/main artifact links must be re-pointed to the minted Zenodo DOI before final compile. Do NOT upload the old tarball with blob/main paths. |
| P5 NM1 title ruling | P5 | Blocking open Houston-decision. "791,635 DR1 Matched Spirals" vs "783,820 Environment-Matched DR1 Spirals". If changed, triggers Fig 3 regen + v0.1.73 bump. |
