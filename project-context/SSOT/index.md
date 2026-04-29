<!-- last_updated: 2026-04-29 -->

# BigBounce SSOT — cross-paper dashboard

**Last authoritative update:** 2026-04-29 (PDT) — R34 closed across all 4 papers + site; 5/8 originally-GPU-blocked items DONE; 3 P4 GPU items currently RUNNING on Pod 2; expected 100 % across all 4 papers within ~14 h.

**Read this first.** Every number here is sourced from the per-paper `status.md` files in this directory. If you catch a contradiction, the per-paper file wins — update this index.

---

## Current state — 2026-04-29 PDT

### Adversarial review

34 rounds complete (R31–R34 closed overnight in 12+ commits to `main`). R34 closed for all 4 papers + site. P1/P2/P3 submission-ready; P4 submission-ready with 3 deferrable nice-to-haves (currently running on Pod 2). Full review log: [`adversarial_peer_review_2026-04-27.md`](../adversarial_peer_review_2026-04-27.md).

### GPU work — 5/8 originally-blocked items DONE, 3 RUNNING

| # | Item | Status | Result location |
|---|---|---|---|
| 1 | **P1-M3** NaMaster 500MC birefringence | ✅ DONE (Pod 1, 2026-04-29 05:31 PDT) | `pipelines/h200_results/pod1_namaster_umap_2026-04-29/results/namaster-birefringence/summary.json` — β=0.27° → 0.238° (bias 0.032°), SNR=20.32σ, 0.77σ vs observed |
| 2 | **P2-C2** noise-weighted r template overlap | ✅ DONE pre-overnight | r=0.84-0.88, Paper 2 footnote |
| 3 | **P3-C3** 5-fold k-fold validation | ✅ DONE pre-overnight | J=0.862 PASS, Paper 3 |
| 4 | **P3-M1** UMAP multi-seed stability | ✅ DONE (Pod 1, 50K × 16D × 20 seeds) | 1-of-3 PASS framing integrated in Paper 3; `pipelines/h200_results/pod1_namaster_umap_2026-04-29/results/umap/umap_stability.json` |
| 5 | **P4-M6** MASTER deconvolution | ✅ DONE (Pod 2 prior session) | `pipelines/h200_results/pod2_priorsession_2026-04-29/master_power_spectrum.json` |
| 6 | **P4-M3** mag/color/SB/PSF bias tests | 🟡 RUNNING on Pod 2 (HF + chirality model unblocked 2026-04-29 ~10:30 PDT) | — |
| 7 | **P4-M4** Catalog C redshift re-analysis | 🟡 RUNNING on Pod 2 | — |
| 8 | **P4-m4** Edge-on contamination | 🟡 RUNNING on Pod 2 | — |

### Pod status

| Pod | Status | Notes |
|---|---|---|
| **Pod 1** (frail_tomato_koi) | ⏹ STOPPED | NaMaster 500MC + UMAP 20-seed stability completed overnight; results committed (5d54fbc) |
| **Pod 2** (regular_green_pig) | 🟢 RUNNING | P4 chirality suite: M3 + M4 + m4. Expected complete within ~12-14 h. |

### Paper readiness

| # | Paper | Readiness | State |
|---|---|---:|---|
| **1** | Spin-Torsion Cosmology | **~99 %+** | NaMaster 500MC integrated; submission-ready. PDF recompile pending. |
| **2** | f_NL Forecast (SPHEREx / MegaMapper) | **~99 %+** | R34 abstract clean (22/23 → 23/23 numbers supported in body); submission-ready. |
| **3** | Multi-Survey Anomaly Catalog | **~98 %+** | UMAP 1-of-3 PASS honest framing integrated; submission-ready. |
| **4** | Galaxy Chirality Catalog | **~96 %** → 100 % when Pod 2 lands | 3 GPU items running; will hit 100 % after Pod 2 completes. |

**Program-level arXiv ETA:** Papers 1, 2, 3 can submit today (PDF recompile only). Paper 4 submits after Pod 2 closes the 3 nice-to-haves (~14 h) — not running them risks an R1 referee request, not a rejection.

---

## Cross-paper dependencies

```
Paper 1 (Spin-Torsion) ──┬─> theoretical f_NL = −35/8 ─> Paper 2 (Fisher forecast)
                         │                               │
                         └─> 14 structural barriers      ├─> multi-tracer bias α ─> uses Paper 3 anomalies
                                                         │
Paper 3 (Anomaly Catalog) ─┬─> AI-selected tracers ─────┘
                           │
                           └─> Shares dipole infrastructure (Landy-Szalay w(θ)) ─> Paper 4 dipole code
Paper 4 (Chirality Catalog) ─> dipole/TTA code ─> available for Paper 3 limitation G
```

**Submission order** (per arXiv production editor 2026-04-18, minimizes bibitem rewiring): Paper 4 → Paper 1 → Paper 3 → Paper 2.

---

## Quick-verify commands

```bash
# SSOT freshness
grep -H "Last authoritative update\|last_updated" project-context/SSOT/paper-*/status.md \
  project-context/SSOT/index.md project-context/SSOT/queue.md

# Principle-10 grep across all four papers (no future-work phrasing)
for t in arxiv/main.tex \
         research/focused_paper_source_integration/02_full_draft.tex \
         pipelines/p3_anomaly_engine/paper3_draft.tex \
         pipelines/p2_chirality/chirality_catalog_paper.tex; do
  echo "=== $t ==="
  grep -niE "future work|in preparation|will be presented|follow-up|we plan to|merits|continued monitoring|is needed" "$t" | head -5
done
```

---

## Where this SSOT does NOT live

- ❌ `project-context/CURRENT_STATUS.md` — legacy; downstream mirror only.
- ❌ `wiki/entities/paper-*.md` — pointer-only entries.
- ❌ `research/project_master_dossier/` — read-only historical record.
- ❌ Any `plan*.md` under `project-context/` — forward-looking proposals, not status.

---

# 📦 Archive — completed milestones

The verbose fire-by-fire history (fires #150–#189, Path-C rebuild, R20–R30 review rounds) lives below. Everything here is verified-completed and reflected in the current-state block above. Collapsed for scannability.

<details>
<summary><b>Phase 2 → Path C Paper 3 rebuild — CLOSED 2026-04-22 (fire #189, 12 / 12 criteria green, weighted sum 100.000 %)</b></summary>

**Closed 2026-04-22 (fire #189).** Houston greenlit autonomous completion ("bro why do you need my ack to finish this? just do it?"), removing fire-#170's ack gate. Final fire executed on pod `o76k3jfzbfh25e`: rewrote `fetch_desi_47k_training.py` to live SPARCL retrieval (`ThreadPoolExecutor` max_workers=12, `rec_get()` safe accessor), 47,000 DESI DR1 spectra in 19.8 min, 0 dropped, deterministic checksum **1812395110**. 5-fold BigAE training < 30 s on A100. Jaccard aggregation **GATE PASS**: mean pairwise $\bar J = 0.862$ (min $0.777$) vs required $\bar J \geq 0.70$. Paper 3 §pathc_caveats updated, recompiled to 28 MB PDF / 33 pp / 0 undef, mirrored to `public/papers/paper3_anomaly_catalog.pdf`. Cron `9f44c29e` self-terminated. Cumulative Path-C spend ~$71 / $400 cap.

**Path-C exit criteria — all 12 CLOSED:**
- #1 SDSS native re-score (fire #164, 1,925,279 scored, ~6500× reduction)
- #2 LAMOST native re-score (fire #133, 21.4× reduction)
- #3 CMB native retrain (val_loss 0.4437, 100 % injection-recovery @5σ)
- #4 DESI 5-fold OOS k-fold (fire #189, $\bar J = 0.862$ PASS)
- #5 NEOWISE ecliptic mask (fire #139)
- #6 Injection-recovery (all surveys, fire #122)
- #7 8-way positional dedup (fire #164, 378,480 unique + 637 multi-survey)
- #8 Paper 3 integration (fire #142, all 4 reader-entry points)
- #9 Paper 3 PDF recompile (fire #168, 28 MB / 33 pp / 0 undef)
- #10 HF rebuild (fire #166, 5-file 15.2 MB bundle)
- #11 P1-PDF-V3 carryover (fire #144)
- #12 Site-sync (fires #125–#187, 13 site surfaces)

</details>

<details>
<summary><b>Adversarial peer review — Rounds 1–34 closed (2026-04-27 → 2026-04-29)</b></summary>

5 parallel Opus agents — 4 hostile per-paper referees + 1 cross-paper consistency checker. 34 rounds across all 4 papers + site. ~280 findings total, ~273 fixed.

**Recent rounds (overnight 2026-04-28 ~22:00 → 2026-04-29 10:19 PDT):**

| Round | Scope | Result |
|---|---|---|
| R31 | Deep paper-by-paper re-reads | P1: 1 MAJOR + 3 MINOR; P2: 3 MINOR; P3: 1 MAJOR + 3 MINOR; P4: 2 MINOR + N_gal=5,547,858 closure |
| R32 | Round-32 sweep | P1: Reproducibility note → 500MC; P2: bib hygiene + xref; P3: UMAP "1-of-3 PASS" honest framing; P4: units + ℓ_max + N_gal arithmetic + Dosovitskiy bib |
| R33 | Single-check micro-tasks | P2: MC count >6e5 abstract↔conclusion alignment; P4: % units in confusion-matrix headers; P1: 20 sections + 43 subsections CLEAN; P3: 21/21 figure files resolve CLEAN; SITE: activity-feed entry added |
| R34 | Single-narrow-check round | P4: cites all 28/28 resolve CLEAN; P2: 22/23 abstract numbers supported in body, orphan ">4σ SPHEREx null disfavor" added to body §VIII.A |

**Strategy lesson:** Single-check 1-scope micro-tasks finished in 15-230s. Broad 3-check sub-agents stalled at 600s with zero edits. R33+R34 used the focused pattern exclusively — zero stalls.

</details>

<details>
<summary><b>Site-sync sweep — fires #171–#188 (13 site surfaces brought to Path-C state)</b></summary>

Opportunistic secondary-surface sweep landed Path-C state across:
- `paper.html` (Paper 3 card refreshed fire #171)
- `ssot.html` (10 surgical edits fire #172)
- `articles/technical-evaluation.html`, `figures.html`, `glossary.html` (fire #173)
- `paper-3/status.md` Path-C banner (fire #174)
- `reproducibility/docs/KNOWN_GAPS.md` (fire #175)
- `status.html` two-surface drift-close (fire #176)
- `explained.html` (fire #177)
- `index.html` stat-sub (fire #178)
- `contributions.html` + `projects.html` (fire #179)
- `anomaly-explorer.html` + `figures.html` + `data-explorer.html` (fire #180)
- `paper.html` title caveat (fire #181)
- `ssot.html` Paper-3 tab badge + `projects.html` SDSS-rescore (fire #182)
- `speculations.html` (fire #183)
- `sitemap.html` (fire #184)
- `anomaly-explorer.html` dual-anchor (fire #185)
- `index.html` Paper 3 subtitle (fire #186)
- `ssot.html` banner header + `projects.html` DESI-card (fire #187)
- `activity.html` timeline feed gap (fire #188)

</details>

<details>
<summary><b>Pre-Path-C historical state — preserved for §7 before/after baseline</b></summary>

Pre-rebuild state (2026-04-16): 319,443 anomalies aggregate / 37.3 M sources scored / 58.8 % SIMBAD-novel / NANOGrav γ = 3.20 ± 0.42 (0.48σ from bounce prediction γ=3.0) / σ(f_NL) 6.1 % / 16.4 % improvements / SPHEREx projection 4.38σ.

These numbers are preserved as the Paper 3 §7 before-after baseline against the Path-C native-retrain results.

</details>
