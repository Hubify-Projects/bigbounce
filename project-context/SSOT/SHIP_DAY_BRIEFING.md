# SHIP DAY BRIEFING — bigbounce coordinated arXiv drop

**Status**: Awaiting (a) EXT16 verdict ladder (HIGH confidence 18/18 ACCEPT), (b) Houston ORCID public flip, (c) Houston drop authorization.

**Tarballs ready**: `project-context/SSOT/arxiv_tarballs/` — EXT16-closure versions (2026-06-13). P1A v1A.0.77 / P1B v1B.0.72 / P2 v1.7.68 / P3 v3.1.111 / P4 v1.0.188 / P5 v0.1.80.

**Full reference**: `project-context/SSOT/ARXIV_SUBMISSION_RUNBOOK.md`

---

## PRE-FLIGHT HOUSTON ACTIONS (do these BEFORE step 1)

### A. ORCID public flip (ONLY true blocker)

1. Log in at https://orcid.org with Houston's credentials
2. Profile settings → "Visibility" → set Names, Employment, Education to **PUBLIC**
3. Verify externally:
   ```bash
   curl -s -o /dev/null -w "%{http_code}" https://pub.orcid.org/v3.0/0009-0008-3617-8729/person
   ```
   - Expected: `200`
   - Current: `404` (blocker — do not proceed until 200)

### B. Resolve 1 open Houston-decision (P5 only)

- **P5-NM1 (blocking)**: Title count — "791,635 DR1 Matched Spirals" vs "783,820 Environment-Matched DR1 Spirals". Recommend 783,820. If changed, rebuild P5 tarball:
  ```bash
  bash tools/build_arxiv_tarball.sh pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex paper5_arxiv_v0.1.80
  ```

### C. Authorize the drop

Once EXT16 reports 18/18 ACCEPT, review SIGNOFF_PACKAGE_2026-06-13.md §2 (6 paper checkboxes).

---

## THE 5-STEP COORDINATED DROP (when authorized)

### Step 1 — Submit ALL 6 to arXiv in ONE HOUR (P4 first)

Submit in this order at https://arxiv.org/submit:

| Order | Paper | Tarball | Primary | Cross-list |
|-------|-------|---------|---------|------------|
| 1 | **P4** | `paper4_arxiv_v1.0.188.tar.gz` | `astro-ph.GA` | `astro-ph.CO` |
| 2 | **P1A** | `paper1a_arxiv_v1A.0.77.tar.gz` | `astro-ph.CO` | `gr-qc`, `hep-th` |
| 3 | **P1B** | `paper1b_arxiv_v1B.0.72.tar.gz` | `astro-ph.CO` | `hep-ph` |
| 4 | **P3** | `paper3_arxiv_v3.1.111.tar.gz` | `astro-ph.CO` | `astro-ph.GA` |
| 5 | **P2** | `paper2_arxiv_v1.7.68.tar.gz` | `astro-ph.CO` | `astro-ph.IM` |
| 6 | **P5** | `paper5_arxiv_v0.1.80-2026-06-13.tar.gz` | `astro-ph.CO` | `astro-ph.GA` |

For each: upload tarball → copy abstract from `abstract_for_webform.txt` → link ORCID `0009-0008-3617-8729` → submit. P4 must upload FIRST because P5 needs P4's arXiv ID. Wait ~60 min for P4's ID before submitting P5.

Pre-submission per-paper: Zenodo one-click publish (see zenodo/ below) → tag HF repos → get live Zenodo DOI → insert into paper before uploading tarball.

### Step 2 — Collect all 6 arXiv IDs (same night, confirmation emails)

IDs arrive via email within ~2 hours of submission (format `2506.NNNNN`). Record here:

```
project-context/SSOT/arxiv_ids_assigned.md   ← create this file, paste all 6
```

| Paper | arXiv ID | Assigned |
|-------|---------|----------|
| P4    | `arXiv:XXXX.XXXXX` | [ ] |
| P1A   | `arXiv:XXXX.XXXXX` | [ ] |
| P1B   | `arXiv:XXXX.XXXXX` | [ ] |
| P3    | `arXiv:XXXX.XXXXX` | [ ] |
| P2    | `arXiv:XXXX.XXXXX` | [ ] |
| P5    | `arXiv:XXXX.XXXXX` | [ ] |

### Step 3 — Back-patch cross-citations in .tex AND .bbl (load-bearing — preflight 2026-06-13)

> **CRITICAL**: .bbl files contain "companion paper, posted concurrently on arXiv" bibitems that are NOT caught by the `XXXX.XXXXX` grep. Both .tex and .bbl must be patched.

> **P2 and P3: SKIP companion-ID patches entirely.** Both papers have ZERO Golden202\* cite-keys in their .tex source AND zero companion-phrase hits in their .bbl files. Confirmed by `arxiv_companion_citation_map.md`. Only their self-preprint `%\preprint` uncomment is needed.
> **P4: SKIP entirely** — zero placeholders, zero companion cites, no v2 needed.
> **Net: only ~3 papers (P1A, P1B, P5) need companion arXiv ID patches.** All 5 papers with `%\preprint` markers need self-preprint uncomment.

**3a. Grep for .tex placeholders (P2/P3 will show 1 hit each — self-preprint only; P4 will show 0):**
```bash
grep -n "XXXX\.XXXXX\|TODO-SUBMISSION" \
  arxiv/paper1a_ech_nogo.tex \
  arxiv/paper1b_mcmc_companion.tex \
  research/focused_paper_source_integration/02_full_draft.tex \
  pipelines/p3_anomaly_engine/paper3_draft.tex \
  pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex
# P4 (pipelines/p2_chirality/chirality_catalog_paper.tex): SKIP — zero markers confirmed
```

**3b. Grep for .bbl companion bibitems (expect hits in P1A and P1B only — P2/P3/P4/P5 have zero):**
```bash
grep -rn "companion paper, posted concurrently on arXiv" arxiv/ pipelines/
# Expected: 4 lines total — paper1a_ech_nogo.bbl:112, :305 and paper1b_mcmc_companion.bbl:60, :137
```

**3c. Run sed patches** (fill in real IDs, then execute):

> **PRE-FLIGHT DRY-RUN VERIFIED 2026-06-13**: The .bbl sed inserts the arXiv ID INSIDE the closing `}` brace of the `\bibinfo {note}` block. The pattern `s/companion paper, posted concurrently on arXiv}/companion paper, posted concurrently on arXiv, arXiv:ID}/g` was dry-run tested against both P1A and P1B .bbl files — both line variants matched correctly. See ARXIV_SUBMISSION_RUNBOOK.md §4 Step 3 for full diff evidence.

```bash
P1A_ID="2506.NNNNN"   P1B_ID="2506.NNNNN"   P2_ID="2506.NNNNN"
P3_ID="2506.NNNNN"    P4_ID="2506.NNNNN"     P5_ID="2506.NNNNN"

# P1A: uncomment self-preprint + patch 4 companion bibitems in .tex
sed -i.bak "s|%\\\\preprint{arXiv:XXXX\\.XXXXX}|\\\\preprint{arXiv:${P1A_ID}}|" arxiv/paper1a_ech_nogo.tex
sed -i.bak "/\\\\bibitem{Golden2026P1b}/,/^$/ s|arXiv:XXXX\\.XXXXX|arXiv:${P1B_ID}|" arxiv/paper1a_ech_nogo.tex
sed -i.bak "/\\\\bibitem{Golden2026P2}/,/^$/  s|arXiv:XXXX\\.XXXXX|arXiv:${P2_ID}|"  arxiv/paper1a_ech_nogo.tex
sed -i.bak "/\\\\bibitem{Golden2026P3}/,/^$/  s|arXiv:XXXX\\.XXXXX|arXiv:${P3_ID}|"  arxiv/paper1a_ech_nogo.tex
sed -i.bak "/\\\\bibitem{Golden2026P4}/,/^$/  s|arXiv:XXXX\\.XXXXX|arXiv:${P4_ID}|"  arxiv/paper1a_ech_nogo.tex
# P1A .bbl: patch companion bibitems (2 instances at lines 112, 305)
sed -i.bak "s/companion paper, posted concurrently on arXiv}/companion paper, posted concurrently on arXiv, arXiv:${P1B_ID}}/g" arxiv/paper1a_ech_nogo.bbl

# P1B: same structure
sed -i.bak "s|%\\\\preprint{arXiv:XXXX\\.XXXXX}|\\\\preprint{arXiv:${P1B_ID}}|" arxiv/paper1b_mcmc_companion.tex
sed -i.bak "/\\\\bibitem{Golden2026P1a}/,/^$/ s|arXiv:XXXX\\.XXXXX|arXiv:${P1A_ID}|" arxiv/paper1b_mcmc_companion.tex
sed -i.bak "/\\\\bibitem{Golden2026P2}/,/^$/  s|arXiv:XXXX\\.XXXXX|arXiv:${P2_ID}|"  arxiv/paper1b_mcmc_companion.tex
sed -i.bak "/\\\\bibitem{Golden2026P3}/,/^$/  s|arXiv:XXXX\\.XXXXX|arXiv:${P3_ID}|"  arxiv/paper1b_mcmc_companion.tex
sed -i.bak "/\\\\bibitem{Golden2026P4}/,/^$/  s|arXiv:XXXX\\.XXXXX|arXiv:${P4_ID}|"  arxiv/paper1b_mcmc_companion.tex
# P1B .bbl: patch companion bibitems (2 instances at lines 60, 137) — note P1A.bbl has P1B companion; P1B.bbl has P1A companion
sed -i.bak "s/companion paper, posted concurrently on arXiv}/companion paper, posted concurrently on arXiv, arXiv:${P1A_ID}}/g" arxiv/paper1b_mcmc_companion.bbl

# P2: self-preprint only — NO companion patches (zero Golden202* cite-keys confirmed)
sed -i.bak "s|%\\\\preprint{arXiv:XXXX\\.XXXXX}|\\\\preprint{arXiv:${P2_ID}}|" research/focused_paper_source_integration/02_full_draft.tex

# P3: self-preprint only — NO companion patches (zero Golden202* cite-keys confirmed)
sed -i.bak "s|%\\\\preprint{arXiv:XXXX\\.XXXXX}|\\\\preprint{arXiv:${P3_ID}}|" pipelines/p3_anomaly_engine/paper3_draft.tex

# P4: SKIP ENTIRELY — zero placeholders, no v2 needed

# P5: golden_chirality_2026 bibitem (free-text "in preparation" → real ID)
sed -i.bak "/\\\\bibitem{golden_chirality_2026}/,/^$/ s|in preparation|arXiv:${P4_ID}|" pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex
# Also patch free-text companion bibitems at L3634, L3639 manually (Paper IV → arXiv:P4_ID; Paper II → arXiv:P2_ID)
```

Authoritative 51-instance map: `project-context/SSOT/arxiv_companion_citation_map.md`

### Step 4 — Recompile + rebuild tarballs + re-upload as v2 (within 24h window)

**arXiv v2 deadline: 14:00 ET / 11:00 PT** — submit v1 by 10:00 PT, patch overnight, v2 by 09:00 PT next morning.

```bash
REPO=/Users/houstongolden/Desktop/CODE_2025/bigbounce
bash tools/build_arxiv_tarball.sh arxiv/paper1a_ech_nogo.tex          paper1a_arxiv_v1A.0.77b
bash tools/build_arxiv_tarball.sh arxiv/paper1b_mcmc_companion.tex     paper1b_arxiv_v1B.0.72b
bash tools/build_arxiv_tarball.sh research/focused_paper_source_integration/02_full_draft.tex paper2_arxiv_v1.7.68b
bash tools/build_arxiv_tarball.sh pipelines/p3_anomaly_engine/paper3_draft.tex paper3_arxiv_v3.1.111b
# P4: no v2 needed (zero patches)
bash tools/build_arxiv_tarball.sh pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex paper5_arxiv_v0.1.80b
```

Upload `*b` tarballs as v2 replacements on each paper's arXiv submission page.

### Step 5 — Verify live (next morning after 20:00 UTC mailing, ~13:00 PT)

```bash
# Check each paper live
for ID in XXXX XXXX XXXX XXXX XXXX XXXX; do
  curl -s -o /dev/null -w "arXiv:${ID} — %{http_code}\n" https://arxiv.org/abs/$ID
done
```

- Verify cross-citations are clickable on each abstract page
- Flip HF dataset `bamfai/bigbounce-anomaly-catalog` to public at P3 posting time
- Zenodo DOIs live and linking correctly

---

## ZENODO ONE-CLICK PUBLISH (before uploading each tarball to arXiv)

Mint DOIs in submission order: P4 → P1A → P1B → P3 → P2 → P5.

1. Open https://zenodo.org/deposit (logged-in Houston)
2. Open per-paper record: `project-context/SSOT/zenodo/PX_zenodo_deposition.md`
3. Follow the 5-step "Click-Publish Steps" in each deposition file
4. Copy live DOI → insert into paper .tex (re-point `\artifact{}` blob/main links for P4; "pending DOI" placeholder for P1B App A; L44 marker for P3; "DOI inserted at submission" for P2)
5. Recompile before uploading the tarball

Master: `project-context/SSOT/zenodo/INDEX.md`

---

## HF ACTIONS (submission day)

| Action | Paper | When |
|--------|-------|------|
| Tag `bamfai/galaxy-chirality-v2` → `v2026.04` | P4 | Before P4 arXiv upload |
| Flip `bamfai/bigbounce-anomaly-catalog` → public | P3 | At P3 arXiv posting |

HF token: `HF_TOKEN` in `bigbounce/.env.local`

---

## POST-ALL-SIX SYNC

```bash
node tools/v3_bundled_paper_bump.mjs   # Convex sync with all 6 arXiv IDs
```

Then update:
- `project-context/SSOT/index.md` — add arXiv IDs under each paper
- `site/src/data/papers.ts` — add arXiv links (triggers Vercel auto-deploy)
- `pipelines/p3_anomaly_engine/DATA_RELEASE_MANIFEST.md` — final Zenodo DOI

---

## ROLLBACK PROTOCOL

If Step 3 patch introduces a regression caught in Step 5:
1. arXiv allows free v3 within submission week
2. EXT11 tarball backups at `arxiv_tarballs/*.ext11-backup` preserve last-known-good
3. Worst case: email arxiv-admin support for "withdraw" within 7 days

**Emergency contacts**: help@arxiv.org · info@zenodo.org

---

## WALL-CLOCK PLAN

| Time (PT) | Action |
|-----------|--------|
| 10:00 PT Day 1 | Submit all 6 to arXiv in one hour (P4 first, wait 60 min for P4 ID before P5) |
| 11:00–midnight | Collect 6 IDs from confirmation emails; run Step 3 patches; recompile |
| 09:00 PT Day 2 | Upload v2 tarballs for P1A, P1B, P2, P3, P5 (P4 needs no v2) |
| 13:00 PT Day 2 | Papers live — verify all 6, verify cross-citations clickable |

Estimated wall-clock from "go" to all 6 live: **~26 hours**

---

**Closure-loop**: when all 6 papers live + cross-citations resolve, update `project-context/SSOT/index.md` with the 6 arXiv IDs + Zenodo DOIs as the canonical "shipped" state. Campaign complete.
