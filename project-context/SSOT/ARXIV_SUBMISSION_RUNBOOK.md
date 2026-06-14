# arXiv Submission Runbook — BigBounce 6-Paper Coordinated Drop
## Status: EXT16-CLOSURE-WAVE COMPLETE | EXT17 READY → HIGH CONFIDENCE 18/18 ACCEPT → arXiv
## Prepared: 2026-06-13 | Updated: EXT16-closure-wave (P1A v1A.0.77 / P1B v1B.0.72 FROZEN / P2 v1.7.68 / P3 v3.1.111 / P4 v1.0.188 FROZEN / P5 v0.1.80)

### EXT16-Closure-Wave Tarballs (REBUILT 2026-06-13, EXT16-closure — SHIP-READY)

| Paper | Tarball | Tarball MD5 | Source PDF MD5 (prefix 8) | Pages | Compile |
|-------|---------|-------------|--------------------------|-------|---------|
| P1A | `paper1a_arxiv_v1A.0.77.tar.gz` | `d051803c457a8a815fc3cff68f7b2290` | `f1eab008` | 29 | CLEAN (errors=0 undef=0) |
| P1B | `paper1b_arxiv_v1B.0.72.tar.gz` | `f0c354fe998aa540550e8bab100e184c` | `5a3c98e9` | 21 | CLEAN (errors=0 undef=0) — FROZEN |
| P2  | `paper2_arxiv_v1.7.68.tar.gz`   | `8d8b4da2adb00c7e873a9010646d50cf` | `5a8a1af4` | 29 | CLEAN (errors=0 undef=0) |
| P3  | `paper3_arxiv_v3.1.111.tar.gz`  | `2aa35ec526f33392e4263c85c63b9fe9` | `4a8c1172` | 30 | CLEAN (errors=0 undef=0) |
| P4  | `paper4_arxiv_v1.0.188.tar.gz`  | `9ec878204f68aa7fb3131fb1d52e284e` | `c47abc18` | 23 | CLEAN (errors=0 undef=0) — FROZEN |
| P5  | `paper5_arxiv_v0.1.80-2026-06-13.tar.gz` | `4d27ac490d36cf5d72c79ef275ef86e9` | `7bb73989` | 32 | CLEAN (errors=0 undef=0) |

---

## Executable 1-pager

For the zero-ambiguity action checklist, see:
**`project-context/SSOT/SHIP_DAY_BRIEFING.md`** — Houston-facing ship-day briefing with every click target and bash command.

This runbook is the full reference; SHIP_DAY_BRIEFING is the distilled executable.

---

## 0. TL;DR — When Houston says "go"

```
1. Apply Houston sign-off decisions (see §8 below)
2. Build updated tarballs for any papers that changed (see §3)
3. Submit all 6 to arXiv in ONE HOUR (see §4 — coordinated drop)
4. Harvest 6 arXiv IDs → back-patch cross-citations → resubmit as v2 within 24h window
5. All 6 go live next morning (20:00 UTC cutoff)
```

Estimated wall-clock from "go" to all 6 papers live: **~26 hours**
(submit in afternoon PST → IDs assigned same night → patch + v2 resubmit next morning → live by 20:00 UTC)

---

## 1. EXT16-Closure-Wave Tarballs — Canonical Location (REBUILT 2026-06-13, EXT16-closure)

All 6 submission-ready tarballs live at:
```
project-context/SSOT/arxiv_tarballs/
```

| Paper | Tarball | Tarball MD5 | Source PDF MD5 (prefix 8) | Pages | Compile |
|-------|---------|-------------|--------------------------|-------|---------|
| P1A | `paper1a_arxiv_v1A.0.77.tar.gz` | `d051803c457a8a815fc3cff68f7b2290` | `f1eab008` | 29 | CLEAN (errors=0 undef=0) |
| P1B | `paper1b_arxiv_v1B.0.72.tar.gz` | `f0c354fe998aa540550e8bab100e184c` | `5a3c98e9` | 21 | CLEAN (errors=0 undef=0) — FROZEN |
| P2  | `paper2_arxiv_v1.7.68.tar.gz`   | `8d8b4da2adb00c7e873a9010646d50cf` | `5a8a1af4` | 29 | CLEAN (errors=0 undef=0) |
| P3  | `paper3_arxiv_v3.1.111.tar.gz`  | `2aa35ec526f33392e4263c85c63b9fe9` | `4a8c1172` | 30 | CLEAN (errors=0 undef=0) |
| P4  | `paper4_arxiv_v1.0.188.tar.gz`  | `9ec878204f68aa7fb3131fb1d52e284e` | `c47abc18` | 23 | CLEAN (errors=0 undef=0) — FROZEN |
| P5  | `paper5_arxiv_v0.1.80-2026-06-13.tar.gz` | `4d27ac490d36cf5d72c79ef275ef86e9` | `7bb73989` | 32 | CLEAN (errors=0 undef=0) |

All rebuilt via `tools/build_arxiv_tarball.sh` from EXT16-closure .tex sources.
Source PDF md5s verified against canonical source PDFs at each paper's directory (match SSOT/index.md EXT16-closure header).
EXT11 tarballs preserved as `*.ext11-backup` in same directory.
These tarballs are the v1 upload files — cross-citations are still placeholder `arXiv:XXXX.XXXXX`; the patching step is in §4 below.

---

## 2. Per-Paper arXiv Metadata

### P1A — ECH No-Go (v1A.0.77)
- **Primary:** `astro-ph.CO`
- **Cross-list:** `gr-qc`, `hep-th`
- **Title:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
- **Authors:** Houston Golden (ORCID: 0009-0008-3617-8729)
- **Comment:** 28 pages, 8 figures. Companion verification paper (P1B) submitted same day. Data at https://github.com/Hubify-Projects/bigbounce
- **License:** arXiv.org perpetual, non-exclusive license
- **Supplementary data:** Zenodo deposition — see `zenodo/P1A_zenodo_deposition.md`

### P1B — MCMC Companion (v1B.0.72)
- **Primary:** `astro-ph.CO`
- **Cross-list:** `hep-ph`  ← CMB birefringence / ALP context
- **Title:** Technical Verification Companion to the ECH Spin-Torsion Program: Lambda-CDM + Delta-N_eff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model
- **Authors:** Houston Golden (ORCID: 0009-0008-3617-8729)
- **Comment:** 21 pages, 4 figures. Companion to arXiv:XXXX.XXXXX (P1A). MCMC chains at https://github.com/Hubify-Projects/bigbounce
- **License:** arXiv.org perpetual, non-exclusive license
- **Supplementary data:** Zenodo deposition — see `zenodo/P1B_zenodo_deposition.md`

### P2 — f_NL Forecast / SPHEREx (v1.7.68)
- **Primary:** `astro-ph.CO`
- **Cross-list:** `astro-ph.IM`
- **Title:** Testing the Matter Bounce with Primordial Non-Gaussianity: Forecasts for SPHEREx and MegaMapper
- **Authors:** Houston Golden (ORCID: 0009-0008-3617-8729)
- **Comment:** 29 pages, 5 figures. Fisher code and configs at https://github.com/Hubify-Projects/bigbounce
- **License:** arXiv.org perpetual, non-exclusive license
- **Supplementary data:** Zenodo deposition — see `zenodo/P2_zenodo_deposition.md`

### P3 — Multi-Survey Anomaly Catalog (v3.1.111)
- **Primary:** `astro-ph.CO`
- **Cross-list:** `astro-ph.GA`
- **Title:** Multi-Survey Spectral Anomaly Detection: 378,280 Anomalous Sources from 37 Million Objects Across Eight Astronomical Archives
- **Authors:** Houston Golden (ORCID: 0009-0008-3617-8729)
- **Comment:** 29 pages, 17+ figures. Catalog at https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog (CC-BY-4.0, flip to public at time of posting). Code at https://github.com/Hubify-Projects/bigbounce
- **License:** arXiv.org perpetual, non-exclusive license
- **Supplementary data:** Zenodo deposition — see `zenodo/P3_zenodo_deposition.md`

### P4 — Galaxy Chirality Catalog (v1.0.188)
- **Primary:** `astro-ph.GA`
- **Cross-list:** `astro-ph.CO`
- **Title:** Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)
- **Authors:** Houston Golden (ORCID: 0009-0008-3617-8729)
- **Comment:** 23 pages, 15 figures. Catalog (3.2M spirals) and model weights at https://huggingface.co/bamfai/galaxy-chirality-v2 (tag v2026.04). Code at https://github.com/Hubify-Projects/bigbounce
- **License:** arXiv.org perpetual, non-exclusive license
- **Supplementary data:** Zenodo deposition — see `zenodo/P4_zenodo_deposition.md`

### P5 — DESI Environmental Chirality (v0.1.80-2026-06-13)
- **Primary:** `astro-ph.CO`
- **Cross-list:** `astro-ph.GA`
- **Title:** Environmental Dependence of Galaxy Chirality in DESI DR1: No Significant Handedness Preference Across Cosmic Web Environments
- **Authors:** Houston Golden (ORCID: 0009-0008-3617-8729)
- **Comment:** 32 pages. Companion to P4 (arXiv:XXXX.XXXXX). Data at https://github.com/Hubify-Projects/bigbounce
- **License:** arXiv.org perpetual, non-exclusive license
- **Supplementary data:** Zenodo deposition — see `zenodo/P5_zenodo_deposition.md`

---

## 3. Pre-Submission Checklist (per paper)

Run this checklist for each paper before uploading tarball to arXiv:

- [ ] revtex4-2 class confirmed (check `\documentclass` line)
- [ ] `\paperVersion` in .tex matches tarball filename version
- [ ] All `\includegraphics` figures present in tarball (verified by build script)
- [ ] `.bbl` present in tarball (build script copies from source dir)
- [ ] No `.aux`, `.log`, `.out`, `.toc`, `.bbl` auxiliary files in tarball root (build script strips them)
- [ ] Hyperlinks resolve: no `\href{TODO}` or `TODO-SUBMISSION` placeholders **except** `arXiv:XXXX.XXXXX` cross-citations (those get back-patched in §4)
- [ ] Zenodo DOI reserved (see `zenodo/INDEX.md`) and inserted in paper where noted
- [ ] ORCID `0009-0008-3617-8729` linked in author field on arXiv webform
- [ ] `abstract_for_webform.txt` present alongside tarball for copy-paste

---

## 4. Coordinated Drop Sequence (CRITICAL — resolves companion ESSENTIAL)

The P1A/P1B/P5 cross-citation ESSENTIAL requires all 6 papers live simultaneously with real IDs. The protocol:

### Step 1 — Submit all 6 in one sitting (target: same 1-hour window)

Submit order (P4 first because P5 hard-depends on P4 arXiv ID for final citation, but all 6 go up before any go live):

```
P4  → arXiv  (submit first)
P1A → arXiv  (submit second, same session)
P1B → arXiv  (submit third)
P3  → arXiv  (submit fourth)
P2  → arXiv  (submit fifth)
P5  → arXiv  (submit sixth)
```

arXiv assigns IDs in submission order. After all 6 are submitted, you receive 6 submission confirmation emails with IDs (format `2506.NNNNN`). Do NOT wait for papers to go live before collecting IDs.

### Step 2 — Collect all 6 arXiv IDs (same night, within ~1-2 hours of submission)

Log assigned IDs here once known:

| Paper | arXiv ID | Assigned |
|-------|---------|----------|
| P4    | `arXiv:XXXX.XXXXX` | [ ] |
| P1A   | `arXiv:XXXX.XXXXX` | [ ] |
| P1B   | `arXiv:XXXX.XXXXX` | [ ] |
| P3    | `arXiv:XXXX.XXXXX` | [ ] |
| P2    | `arXiv:XXXX.XXXXX` | [ ] |
| P5    | `arXiv:XXXX.XXXXX` | [ ] |

### Step 3 — Back-patch cross-citations in each .tex AND .bbl

> **Pre-flight 2026-06-13 fix**: prior runbook revision missed .bbl bibitems. Both .tex AND .bbl must be patched in v2 re-tarball.

> **2026-06-13 accuracy fix**: earlier drafts of the runbook stated P2 and P3 need P1A/P1B arXiv ID insertion. This is WRONG. `arxiv_companion_citation_map.md` confirms P2 and P3 have ZERO Golden202\* cite-keys. **Skip P2 and P3 for companion-ID patches.**

#### PAPERS REQUIRING V2 BACK-PATCH (authoritative — from citation map)

| Paper | Self-preprint uncomment | Companion bibitem patches | .bbl companion phrase patches | Skip reason |
|-------|------------------------|--------------------------|-------------------------------|-------------|
| P1A   | YES (L663 commented) | YES — 4 bibitems (P1B, P2, P3, P4 IDs in .tex) | YES — 2 instances in paper1a_ech_nogo.bbl | — |
| P1B   | YES (L1064 commented) | YES — 4 bibitems (P1A, P2, P3, P4 IDs in .tex) | YES — 2 instances in paper1b_mcmc_companion.bbl | — |
| P2    | YES (L17 commented)  | **SKIP — no Golden202\* cite-keys in .tex** | **SKIP — 0 instances in .bbl** | No cross-cites |
| P3    | YES (L45 commented)  | **SKIP — no Golden202\* cite-keys in .tex** | **SKIP — 0 instances in .bbl** | No cross-cites |
| P4    | NONE (no preprint marker in .tex) | **SKIP — fully independent** | **SKIP** | Zero placeholders |
| P5    | NONE (no preprint marker in .tex) | YES — golden_chirality_2026 bibitem ("in preparation" → arXiv:P4_ID) + 2 free-text companion bibitems (L3634, L3639) | 0 instances in .bbl | No preprint marker |

**Net: only 3 papers need companion arXiv ID insertion (P1A, P1B, P5). All 5 papers with `%\preprint` markers need self-preprint uncomment. P4 needs zero v2 patches.**

For each paper, find all `arXiv:XXXX.XXXXX` placeholders and replace with real IDs.
Quick grep to locate them in .tex files (P2 and P3 will show ONLY the self-preprint line, confirming no cross-cites):

```bash
grep -n "XXXX\.XXXXX\|TODO-SUBMISSION" arxiv/paper1a_ech_nogo.tex
grep -n "XXXX\.XXXXX\|TODO-SUBMISSION" arxiv/paper1b_mcmc_companion.tex
grep -n "XXXX\.XXXXX\|TODO-SUBMISSION" research/focused_paper_source_integration/02_full_draft.tex   # P2: expect 1 hit (self-preprint only)
grep -n "XXXX\.XXXXX\|TODO-SUBMISSION" pipelines/p3_anomaly_engine/paper3_draft.tex                  # P3: expect 1 hit (self-preprint only)
# P4: skip — confirmed zero XXXX.XXXXX markers
grep -n "XXXX\.XXXXX\|TODO-SUBMISSION" pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex
```

**Also patch .bbl files** — the Golden202* bibitems use the phrase "companion paper, posted
concurrently on arXiv" inside a `\bibinfo {note} {...}` block (no `XXXX.XXXXX` token).
These will NOT be caught by the grep above and must be patched separately.

**IMPORTANT: the phrase ends with `}` (closing the `\bibinfo` brace) immediately before `\BibitemShut`. The correct insertion point is INSIDE the closing brace, not after it.**

Quick grep to locate them (expect hits in P1A and P1B only — P2/P3/P4 have zero):

```bash
grep -rn "companion paper, posted concurrently on arXiv" arxiv/ pipelines/
# Expected output:
#   arxiv/paper1a_ech_nogo.bbl:112:  \bibinfo {note} {companion paper, posted concurrently on arXiv}\BibitemShut
#   arxiv/paper1a_ech_nogo.bbl:305:  \bibinfo {note} {companion paper, posted concurrently on arXiv}\BibitemShut
#   arxiv/paper1b_mcmc_companion.bbl:60:  {companion paper, posted concurrently on arXiv}\BibitemShut {NoStop}%
#   arxiv/paper1b_mcmc_companion.bbl:137:  \bibinfo {note} {companion paper, posted concurrently on arXiv}\BibitemShut
# P2/P3/P4/P5 .bbl files: ZERO hits — skip
```

#### PRE-FLIGHT DRY-RUN VERIFIED (2026-06-13)

The .bbl sed pattern was dry-run tested against `arxiv/paper1a_ech_nogo.bbl` and `arxiv/paper1b_mcmc_companion.bbl` with fake ID `2606.99999`.

**Original runbook pattern (BROKEN — failed to match due to backslash escaping):**
```bash
sed -i.bak 's/\(companion paper, posted concurrently on arXiv\)\([^,]\)/\1, arXiv:2606.99999\2/' file.bbl
```

**Verified working pattern (INSERT INSIDE CLOSING BRACE):**
```bash
# Replace "arXiv}" with "arXiv, arXiv:<ID>}" — inserts ID inside the \bibinfo brace
sed -i.bak 's/companion paper, posted concurrently on arXiv}/companion paper, posted concurrently on arXiv, arXiv:REAL_ID}/g' file.bbl
```

Verified diff output from dry-run (P1A .bbl, 2 matching lines):
```diff
112c112
<   \bibinfo {note} {companion paper, posted concurrently on arXiv}\BibitemShut
---
>   \bibinfo {note} {companion paper, posted concurrently on arXiv, arXiv:2606.99999}\BibitemShut
305c305
<   \bibinfo {note} {companion paper, posted concurrently on arXiv}\BibitemShut
---
>   \bibinfo {note} {companion paper, posted concurrently on arXiv, arXiv:2606.99999}\BibitemShut
```

Both line variants (inline `{...}\BibitemShut {NoStop}%` and newline `\bibinfo {note} {...}\BibitemShut`) matched correctly in P1B dry-run. Pattern is confirmed correct.

Authoritative per-paper-per-cite-key target map (51 cite-instances total):
`project-context/SSOT/arxiv_companion_citation_map.md`

### Step 4 — Rebuild tarballs with patched .tex

```bash
REPO=/path/to/bigbounce
bash tools/build_arxiv_tarball.sh arxiv/paper1a_ech_nogo.tex paper1a_arxiv_v1A.0.77b
bash tools/build_arxiv_tarball.sh arxiv/paper1b_mcmc_companion.tex paper1b_arxiv_v1B.0.72b
bash tools/build_arxiv_tarball.sh research/focused_paper_source_integration/02_full_draft.tex paper2_arxiv_v1.7.68b
bash tools/build_arxiv_tarball.sh pipelines/p3_anomaly_engine/paper3_draft.tex paper3_arxiv_v3.1.111b
# P4: no v2 needed (zero patches, zero XXXX.XXXXX markers)
bash tools/build_arxiv_tarball.sh pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex paper5_arxiv_v0.1.80b
```

### Step 5 — Resubmit as v2 within 24h window

arXiv allows free re-upload before the paper goes live (before 14:00 ET / 11:00 PT cutoff).
Upload the `*b` tarballs as v2 replacements. All 6 go live next morning with live cross-IDs.

**arXiv submission cutoff: 14:00 ET (11:00 PT) for same-day announcement.**
**Target: submit Step 1 by 10:00 PT → IDs by midnight → patch + v2 by 09:00 PT next morning.**

---

## 5. Zenodo One-Click Publish (Submission Day)

Follow `zenodo/INDEX.md` → open each `zenodo/PX_zenodo_deposition.md` → 5-step click-publish.
Mint DOIs in submission order: P4 → P1A → P1B → P3 → P2 → P5.

Key DOI insertion dependencies:
- P4 Zenodo DOI → re-point `\artifact{}` blob/main links before final P4 compile
- P1A Zenodo DOI → insert in P1B App A "pending DOI" placeholder
- P3 Zenodo DOI → insert in `DATA_RELEASE_MANIFEST.md` header + tex L44 marker
- P2 Zenodo DOI → insert at "DOI inserted at submission" placeholders

---

## 6. HuggingFace Actions (Submission Day)

| Action | Paper | When |
|--------|-------|------|
| Tag `bamfai/galaxy-chirality-v2` → `v2026.04` | P4 | Before P4 arXiv upload |
| Flip `bamfai/bigbounce-anomaly-catalog` → public | P3 | At P3 arXiv posting |

HF token: `HF_TOKEN` in `bigbounce/.env.local`

---

## 7. Post-All-Six Sync

After all 6 arXiv IDs are in hand:

```bash
node tools/v3_bundled_paper_bump.mjs  # Convex sync with all 6 arXiv IDs
```

Then update:
- `project-context/SSOT/index.md` — add arXiv IDs under each paper
- `site/src/data/papers.ts` — add arXiv links (triggers Vercel auto-deploy)
- `pipelines/p3_anomaly_engine/DATA_RELEASE_MANIFEST.md` — final Zenodo DOI

---

## 8. Open Houston-Decision Items (Block or No-Block)

| Item | Paper | Blocking | Default |
|------|-------|----------|---------|
| **P5-NM1 title count** — "791,635" vs "783,820 Environment-Matched DR1 Spirals" | P5 | YES (requires Fig 3 regen if changed; bump to v0.1.81) | 783,820 recommended |
| **P3 S_BigAE column strip** — strip irreproducible scores from Table III per 3-reviewer/2-round consensus | P3 | Soft (won't break submission but recommended before upload) | YES, strip |
| **P3 title count framing** — "Novelty Fractions" + 378,280 lead number | P3 | No | Already at v3.1.111 |
| **P1B SN-overlap chains** — ship with "Exploratory w₀wₐ" framing vs hold | P1B | No | Ship now |
| **P4 companion arXiv ID** — P5 must wait ~1h after P4 upload for P4's ID | P4/P5 | Sequence dependency, not a decision | Hold P5 upload until P4 ID confirmed |

**Status: 1 hard blocker (P5-NM1). All others are soft or have standing defaults.**

If Houston rules P5-NM1 = "783,820" before go day, rebuild P5 tarball:
```bash
bash tools/build_arxiv_tarball.sh pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex paper5_arxiv_v0.1.81
```

---

## 9. EXT10 Verdict Summary

| Paper | EXT10 Verdict | Path to ACCEPT |
|-------|-------------|----------------|
| P1A   | MINOR REVISIONS × 3/3 | 18/18 MINOR → ACCEPT ≤1 cycle |
| P1B   | MINOR REVISIONS × 3/3 | 18/18 MINOR → ACCEPT ≤1 cycle |
| P2    | MINOR REVISIONS × 3/3 | 18/18 MINOR → ACCEPT ≤1 cycle |
| P3    | MINOR REVISIONS × 3/3 | 18/18 MINOR → ACCEPT ≤1 cycle |
| P4    | MINOR REVISIONS × 3/3 | 18/18 MINOR → ACCEPT ≤1 cycle |
| P5    | MINOR REVISIONS × 3/3 | 18/18 MINOR → ACCEPT ≤1 cycle |

Zero MAJORs across all 6 papers in EXT10. 5/5 vendor consensus on MINOR tier.
Prior round: Grok ACCEPT on all 6 through EXT3–EXT7 (stable calibration anchor).

---

## 10. Submission Readiness Gate

| Gate | Status |
|------|--------|
| All 6 tarballs built from EXT16-closure .tex sources | DONE (919fd7cd) |
| Standalone pdflatex (errors=0, undef=0) on all 6 | DONE |
| md5 checksums recorded | DONE |
| Zenodo deposition records prepared (one-click publish ready) | DONE |
| Coordinated-drop sequence documented | DONE |
| ORCID confirmed (0009-0008-3617-8729) | PENDING Houston (currently 404) |
| P5-NM1 title ruling | PENDING Houston |
| Houston 6-paper sign-off | PENDING |

---

*Runbook updated 2026-06-13 (SHIP_READINESS_FINAL QA sweep) — all version refs advanced to EXT16-closure (919fd7cd). Tarballs staged at `project-context/SSOT/arxiv_tarballs/`. All 6 cross-citation placeholders (`arXiv:XXXX.XXXXX`) will be back-patched on submission day per §4.*
