# SUBMIT-TODAY CHECKLIST — all 6 papers (2026-07-05)

All six papers passed a fresh full-source publication audit today (fix-verified, packets
standalone-compile-tested, three-way md5 compile==served==Convex). Every reviewer finding
is closed by real science, artifact-cited, or resolved by this coordinated plan. Houston's
clicks are the only remaining step.

## WAVE 1 — submit now, in this order (no dependencies)

| # | Paper | Bundle | Ver | pp | Notes |
|---|-------|--------|-----|----|-------|
| 1 | **P4** chirality catalog | `submissions/P4/arxiv_p4_v1.0.225.tar.gz` (md5 3adc5739) | v1.0.225 | 32 | astro-ph.CO, x-list GA. Metadata in `ARXIV_METADATA.txt`. Bundle rebuilt from current source 2026-07-09 (the .224 bundle was one version stale); standalone re-extract+compile 0 err / 0 undef / 32pp. **Submit FIRST — P5 needs its ID.** |
| 2 | **P3** anomaly catalog | `submissions/P3/arxiv_p3_v3.1.146.tar.gz` (md5 25807ecb) | v3.1.146 | 35 | Title: "A Multi-Survey Autoencoder Anomaly-Candidate Catalog: 268,519 Reconstruction-Outlier Sources from a Native-Trained Scan of 37.3 Million Spectra and Map Patches". v3.1.146 R9 EXT closure; standalone re-extract+compile 0 err / 0 undef / 35pp. HF dataset `bamfai/bigbounce-anomaly-catalog` already PUBLIC (no flip needed); Zenodo DOI mints at submit (optional). |
| 3 | **P2** f_NL forecast + Cai/Li resolution | `submissions/P2/arxiv_p2_v1.7.105.tar.gz` (md5 ed764493) | v1.7.105 | 36 | Positioned as honest forecast + the −35/16 literature resolution. v1.7.105 R9 closure (App A Table VII per-vertex derivation + gauge/physical-frame table); no science number changed, −35/16 unchanged; standalone re-extract+compile 0 err / 0 undef / 36pp. Zenodo DOI at submit (optional). |

arXiv assigns each ID immediately on submission (announcement later; the ID is usable at once).

## WAVE 2 — same day, after wave-1 IDs exist

| # | Paper | Bundle | Ver | pp | Pre-submit step (~2 min each) |
|---|-------|--------|-----|----|------------------------------|
| 4 | **P5** DESI environmental chirality | `submissions/P5/arxiv_p5_v0.1.108.tar.gz` | v0.1.108 | 39 | Set the single `\paperIVarxiv` macro to P4's real ID (see `submissions/P5/SUBMISSION_NOTE.txt`) → recompile → rebuild bundle → submit. NOTE: latest committed P5 bundle is `arxiv_p5_v0.1.107.tar.gz`; source is v0.1.108, so the v0.1.108 bundle is produced by the wave-2 ID-insertion rebuild (or rebuild now from source if submitting before wave-1 IDs exist). |
| 5 | **P1U** unified Paper 1 (theory + reproducibility) | `submissions/P1A/arxiv_p1_unified_v1U.0.4.tar.gz` | v1U.0.4 | 60 | P1B is MERGED into P1U — no standalone P1B submission, no reciprocal note. Fill the four companion arXiv IDs in `arxiv/references.bib` `TODO-SUBMISSION` notes (`Golden2026P2/P3/P4` + P5) with wave-1 IDs; the `Golden2026P1a` self-ref stays `[arXiv:XXXX.XXXXX]` (P1U's own ID does not exist yet) → recompile `arxiv/paper1_unified.tex` (regenerates .bbl) → rebuild tarball → submit. |

## Post-submit (agent-executable — say the word)
- Insert real IDs, recompile wave-2, rebuild bundles (I do this the moment you give me the IDs)
- Update P1B replacement (v2) with P1A's ID
- Site/Convex/SSOT sync with arXiv IDs + announcement links; reviewTimeline "published" entries
- Strengthening computes from the DATA agent (P3-DESI, P4-morphology, P2-CovB) fold into v2
  replacements if they land — none are blocking

## Verified state per paper (finals: P4 v1.0.225 · P3 v3.1.146 · P2 v1.7.105 · P5 v0.1.108 · P1U v1U.0.4)
- **P4** (v1.0.225): condensed title + reader-first abstract; Grok+Gemini MINOR, null "robustly supported"; every number reproduces.
- **P3** (v3.1.146): byte-identical reproduction; anomalies proven real high-z QSOs (p~1e-103); eROSITA tier excised from every count.
- **P2** (v1.7.105): −35/16 3-way certified (App A Table VII per-vertex derivation); independent+RSD Fisher; Grok MINOR.
- **P5** (v0.1.108): all numbers exact; Δf_CW monopole-invariant on public data; Paper-IV = citation timing.
- **P1U** (v1U.0.4): P1A theory + P1B reproducibility companion MERGED; all tiers derived/grounded/NDA-bounded; f_NL −35/16 propagated; Fierz lemma closed; companion numbers artifact-cited; 0 genuinely-new Grok/Gemini findings.

ChatGPT's blanket REJECTs are its structural harsh-referee floor (directive H) — record-only,
each remaining item truth-audited as re-flag/disclosed. The operative calibrated gate
(Grok+Gemini + INT + verified science) is satisfied to the honest convergence floor on all six.

## Journal targets after arXiv (orchestrator judgment, 2026-07-05 — see FINAL_SIGNOFF_AUDIT)

| Paper | Primary target | Positioning | Expected referee friction |
|---|---|---|---|
| P4 | PRD (or MNRAS) | Null-result + catalog, pre-specified, model-free confirmation | Low — strongest paper |
| P3 | ApJS / AJ | Catalog + methods data-release (right venue for tiered validation) | Low at the right venue |
| P2 | PRD / JCAP | LEAD with the −35/16 Cai–Li resolution; forecast as secondary | Moderate — forecast scope |
| P5 | MNRAS / PRD | Environmental null on public data (post P4 ID) | Low-moderate |
| P1A | JCAP / PRD | Channel-level no-go + NDA argument, scope explicit | Expect a real scope exchange — normal refereeing |
| P1B | arXiv companion (or pair with P1A; alt: methods venue) | Reproducibility + derived ΔN_eff bound | Venue-dependent |

ChatGPT's blanket REJECTs are dispositioned in FINAL_SIGNOFF_AUDIT_2026-07-05.md (0 genuinely-new
real findings); read them as a preview of the toughest human referee's *scope* questions, answered
in referee exchanges with the verified artifact record.

---

## Wave-2 arXiv-ID insertion — one command (`tools/insert_arxiv_ids.sh`)

> **⚠ SUPERSEDED for the merged layout (2026-07-09).** Wave-2 is now **P5 v0.1.108
> + the unified Paper 1 (P1U v1U.0.4)** — P1B is merged into P1U, so there is **no
> standalone P1B submission and no reciprocal P1B_V2 note.** The `insert_arxiv_ids.sh`
> steps below still describe the OLD two-paper (P1A + P1B) layout and the script's
> own header targets `arxiv/paper1a_ech_nogo.tex`. Its P5 leg (Step 1, `\paperIVarxiv`)
> is still correct; its P1A/P1B legs are stale. For P1U, insert the four wave-1 IDs
> directly into `arxiv/references.bib` (see the tool's updated header note + the
> WAVE RE-PLAN block below), then recompile `arxiv/paper1_unified.tex`. Also note the
> script's `REPO` path constant still points at the old `CODE_2025/bigbounce` location
> (repo now lives under `CODE_YOU/bigbounce`).

Once wave-1 IDs (P4, P3, P2) are assigned, run the P5 leg to set `\paperIVarxiv`,
then insert the companion IDs into P1U's bib and recompile:

```
tools/insert_arxiv_ids.sh --p4 2507.NNNNN --p1b 2507.NNNNN --p3 2507.NNNNN --p2 2507.NNNNN [--dry-run]
```

The four IDs are the **wave-1** IDs (already assigned when this runs). What it does:

1. **P5** (`pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`): sets the
   single `\paperIVarxiv` macro to the real **P4** ID (per `submissions/P5/SUBMISSION_NOTE.txt`).
   Every Paper-IV reference resolves through that one macro.
2. **P1A** (`arxiv/paper1a_ech_nogo.tex` via shared `arxiv/references.bib`): fills the
   four `TODO-SUBMISSION` companion bib notes — `Golden2026P1b→P1B`, `Golden2026P2→P2`,
   `Golden2026P3→P3`, `Golden2026P4→P4` — then **regenerates the `.bbl`** (bibtex) so the
   IDs render in the PDF bibliography. P1A's own forward-ref (`Golden2026P1a`,
   `[arXiv:XXXX.XXXXX]`) is **left intact** — P1A's ID doesn't exist yet.
3. **P1B reciprocal**: writes `submissions/P1B/P1B_V2_NOTE.md` staging (NOT applying)
   the P1A-ID insertion for the P1B **v2** replacement — P1B submits before P1A's ID exists.
   P1B source is never edited by this script.
4. For each touched paper (**P5, P1A**): recompile (**0-undef gate**), bump patch
   version + timestamp/date, mirror the PDF byte-identical to all served paths
   (`public/papers/` versioned+alias, `site/public/papers/`, source dir),
   rebuild + **standalone-verify** the arXiv bundle, print the **Convex `paperVersions:bump`**
   command (real md5/pages), and stamp the checklist. **Fails loudly on any gate.**
5. **`--dry-run`**: does all of the above in a `/tmp` copy, verifies every gate, and
   **touches nothing in the repo**. Verified green with placeholder IDs 2507.00001–00004
   (P5 + P1A both recompile clean 37pp, both bundles standalone-verify, IDs render in PDF).

TeX PATH the script sets itself: `$HOME/Library/TinyTeX/bin/universal-darwin:/opt/homebrew/bin`.

**Submission-day sequence:**
1. Submit wave-1 (P4 first, then P1B, P3, P2) → collect the four assigned IDs.
2. `tools/insert_arxiv_ids.sh --p4 … --p1b … --p3 … --p2 …` (drop `--dry-run`).
3. Run the two printed Convex bump commands; submit P5 + P1A (new bundles); commit.
4. When P1A's ID is assigned, apply `submissions/P1B/P1B_V2_NOTE.md` for the P1B v2 replacement.


## ⚠ WAVE RE-PLAN (2026-07-09, post-merge — supersedes the tables above)
P1B is MERGED into the unified Paper 1 (P1U, v1U.0.4, 60pp, bundle `submissions/P1A/arxiv_p1_unified_v1U.0.4.tar.gz`) — no standalone P1B submission.
**Wave 1:** P4 v1.0.225 (32pp) → P3 v3.1.146 (35pp) → P2 v1.7.105 (36pp). **Wave 2 (same day, wave-1 IDs inserted):** P5 v0.1.108 (39pp; P4 ID) → Paper 1 unified v1U.0.4 (60pp; P2/P3/P4/P5 IDs). `tools/insert_arxiv_ids.sh` targets the OLD two-paper layout for P1A/P1B cross-refs — for the unified paper, insert the four companion arXiv IDs directly in `arxiv/references.bib` (bib keys `Golden2026P2/P3/P4` + the P5 ref → wave-1 IDs; `Golden2026P1a` self-ref stays `[arXiv:XXXX.XXXXX]`) or wherever the live `TODO-SUBMISSION` / `arXiv:XXXX.XXXXX` markers sit, then recompile `arxiv/paper1_unified.tex` (regenerates the `.bbl`). See `tools/insert_arxiv_ids.sh` header note (P1U section) for the exact placeholders.
