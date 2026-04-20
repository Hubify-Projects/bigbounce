# BigBounce SSOT — cross-paper dashboard

**Read this first.** Every number here is sourced from the per-paper `status.md` files in this directory. If you catch a contradiction, the per-paper file wins — update this index.

Last authoritative update: 2026-04-20 (drive-to-100 fire #111 — Paper 3 Path-C index.md catchup: per-criterion percentages refreshed from fire #100 → fire #110 state, overall Paper 3 % bumped 55 → 59, integration criterion #8 70 → 90 reflecting abstract + §1 + §3 intro + §Conclusions + §Data-availability + Table 1 ‡-footnote Path-C narrative landed, site-sync criterion #12 70 → 85 reflecting 5/5 explorer pages + activity.html + SSOT index in Path-C state, injection-recovery #6 60 → 70 reflecting continuum-dip SDSS gate PASS + LAMOST + CMB closed, SDSS+LAMOST re-scores now 26 % / 29 % done on top of gate PASS)

---

## 🟠 Phase 2 → Path C full Paper 3 rebuild — scope widened 2026-04-19

**Papers 1, 2, 4 are at 100 % on .tex + compile axes** (content stable; Houston-owned scientific decisions remain self-paced).

**Paper 3 is being rebuilt to Path C scope** after Houston novelty-integrity pushback 2026-04-19. Root cause: the BigAE model was trained on 47K DESI spectra and then *cross-applied* to SDSS + LAMOST (inflating those anomaly rates via catalog-cross-calibration artifacts), while the CMB autoencoder was catastrophically undertrained (0.33 % injection-recovery). The "58.8 % novel" headline is bookkeeping against SIMBAD at 5-arcsec, not true astrophysical novelty, and the 319,443 total is sum-over-surveys, not unique physical objects.

**Path C scope** (Houston chose over Path A "ship with caveats" and Path B "native retrain only"): native BigAE retrain for SDSS + LAMOST, CMB autoencoder retrain with proper galactic mask, DESI 5-fold out-of-sample validation, NEOWISE ecliptic mask, injection-recovery on every retained survey, 8-way positional dedup at 5 arcsec. Current cross-transfer (DESI-trained on SDSS/LAMOST) scans preserved as Paper 3 §7 "before / after native retrain" comparison baseline. Paper 3 gets a new §2.X methodology subsection + rewritten abstract + Table 1 with unique-object counts alongside sum-over-surveys.

**Scope + budget:** ~10–14 days, ~$300–500 pod (Houston's prior $140 cap exceeded via Path C choice). See `SSOT/drive-to-100.md` "🟡 RE-OPENED Phase 2" banner + Path C exit criteria (12 gates). 7 new `P3-PATHC-*` queue rows filed.

**Papers 1, 2, 4 carryover:** `P1-PDF-RECOMPILE-V3` (14 bundled non-scientific Paper 1 edits) folds into Phase 2 as a single pod recompile session. Houston-owned decisions (`P1-RHAT-NUMBER-RECONCILE`, `P1-BETA-EQ38-CHECK`, `P4-D4-VS-Z2-RENAME`) remain self-paced.

**"Peer review" caveat:** the 6 review files at `project-context/peer-reviews/autonomous-2026-04-18/` (1,434 lines total) are adversarial reviewer personas I generated, NOT external academic review. Real peer review happens post-arXiv.

**Do NOT submit arXiv forms yet.** Review site at https://bigbounce.hubify.app.

---

## Program health at a glance

| # | Paper | One-line status | Ready for arXiv | Gap to 100 % | Canonical source | SSOT |
|---|---|---|---:|---|---|---|
| **1** | **Spin-Torsion Cosmology** | v2.3.0, 27 pp, 63+ refs, 10+ revision rounds. β = 0.264° ALP integrated (L391). **2026-04-17 fire #9:** fresh `pdflatex + bibtex + pdflatex x2` via Docker TeX Live — **945 KB PDF, 0 undefined refs, fresh `main.bbl` (58 bibitems)**, §IV corner figure rendered, tarball rebuilt clean (440 KB, 3 figures, smoke-tested → 945 KB self-compile). | **100 %** | all queue tasks closed — P1-PDF-RECOMPILE-V2 ✓ + P1-BBL-REGEN ✓ + P1-TARBALL ✓ | `arxiv/main.tex` | [paper-1/status.md](paper-1/status.md) |
| **2** | **f_NL Forecast (SPHEREx / MegaMapper)** | v1.6.0, 375 lines, 6 figures. σ(f_NL) forecasts, Bayes factors 8–17, bias validation 1.58× on Gold+Silver QSOs. **2026-04-17 fire #9:** fresh compile via Docker TeX Live — **632 KB PDF, 0 undefined refs**, mirrored to `public/papers/paper2_fnl_forecast.pdf`. | **100 %** | 9 queue tasks — 9 done | `research/focused_paper_source_integration/02_full_draft.tex` | [paper-2/status.md](paper-2/status.md) |
| **3** | **Multi-Survey Anomaly Catalog** | 🟠 **PATH-C REBUILD IN FLIGHT (≈59 %)** post-2026-04-19 novelty-integrity pushback. Prior 2026-04-16 lock (319,443 anomalies / 58.8 % novel / NANOGrav γ = 3.20 ± 0.42) preserved as §7 before-after baseline. Path-C progress (fire #110, 2026-04-20): criterion #3 CMB native retrain **CLOSED** (val_loss 0.4437 gate PASS, 500/500 = 100 % injection-recovery at 5× noise, 200K-patch full re-score complete); criteria #1/#2 SDSS+LAMOST native re-scores gate-PASS (val_loss 0.0311 + 0.0329) and partially rescored (SDSS batch 120/471 = 25.5 %, LAMOST 340/1177 nights = 28.9 %, ETA 30-37 h, 80 %); #5 NEOWISE ecliptic mask 85 % (mask applied, paper §3.3 annotated, Table 1 † footnote landed); #6 injection-recovery 70 % (continuum-dip variant SDSS native **gate PASS 64 % at 5σ** vs 7.2 % emission-line, LAMOST continuum-dip 5.8 % = 9.7× over emission-line, CMB 100 % @5σ); #7 8-way dedup 70 % (5/8 surveys loaded, 197,246 detections → 191,432 unique physical objects, 0 multi-survey matches); #8 paper integration **90 %** — Path-C disclosed at every reader-entry point (abstract fire #102 + §1 Intro #107 + §2.4 methodology #87 + §3 intro #106 + §3.2 SDSS + §3.3 LAMOST + §3.5 CMB + §3.3 NEOWISE + Table 1 ‡-footnote #110 + §7.4 caveats + §Conclusions bullet #8 #108 + §Data-availability manifest #109); #10 HF-REBUILD 45 % (README staged, native artifact manifest specified in §Data-availability, push gated on natives); #12 site-sync 85 % (all 5 explorer pages + index.md + activity.html top-of-feed timeline entry in Path-C state). Pre-Path-C compile state: 28 MB PDF / 0 undef refs at `public/papers/paper3_anomaly_catalog.pdf`; post-Path-C recompile (criterion #9) gated on natives. | **Rebuild ≈59 %** | 12 Path-C exit criteria — 1 CLOSED (#3 CMB) + 8 in progress (#1/#2/#5-8/#10/#12) + 3 not-started (#4 DESI k-fold, #9 recompile, #11 P1-PDF-V3). See `SSOT/drive-to-100.md` Phase-2 Path-C block + fire-by-fire Loop log. | `pipelines/p3_anomaly_engine/paper3_draft.tex` | [paper-3/status.md](paper-3/status.md) |
| **4** | **Galaxy Chirality Catalog** | 8.47 M galaxies · 8/8 bias tests · 0.43σ null dipole · Shamir refuted 7×. **2026-04-17 fire #9:** fresh compile via Docker TeX Live — **25.7 MB PDF, 0 undefined refs**, LSST 10-yr projection line rendered, mirrored to `public/papers/chirality_catalog_paper.pdf`. | **100 %** | 7 queue tasks — 6 done + 1 Houston-review (P4-LSST-LINE-REVIEW, non-blocking for arXiv acceptance) | `pipelines/p2_chirality/chirality_catalog_paper.tex` | [paper-4/status.md](paper-4/status.md) |

**Program-level arXiv ETA:** Papers 1, 2, 4 compiled cleanly via Docker TeX Live as of 2026-04-17 — revtex4-2, **0 undefined refs**, figures embedded (945 KB / 632 KB / 25.7 MB), PDFs mirrored to `public/papers/`. Paper 1 tarball rebuilt clean (440 KB, 3 figures, smoke-tested). **Papers 1, 2, 4 are at 100 % on the content + compile axes.** Paper 3 is in Path-C rebuild (~59 %, fire #110 state) — the 28 MB pre-Path-C PDF is preserved as §7 before/after baseline but will be superseded by the native-retrain-based recompile (criterion #9) once SDSS + LAMOST native re-scores complete (ETA 30-37 h at current pod cadence). Paper 3 integration is now at 90 % — all reader-entry points carry Path-C framing (abstract / §1 / §2.4 / §3 intro / §3.2-§3.3-§3.5 per-survey / Table 1 / §7.4 caveats / §Conclusions / §Data-availability). The only remaining non-rescore-gated open items for the other three papers are (a) Houston's one-line review of the LSST projection line in Paper 4 (P4-LSST-LINE-REVIEW) and (b) Houston-owned arXiv submission (fill the arXiv form for each paper). Recommended submission order once Paper 3 Path-C closes: Paper 4 → Paper 3 → Paper 1 → Paper 2.

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
Paper 4 (Chirality Catalog) ─> dipole/TTA code ─> available for Paper 3 limitation G (empirical α calibration)
```

- **Paper 2 depends on Paper 3's tracer catalog** — if Paper 3 data-availability link changes, Paper 2 citations update.
- **Paper 3 depends on Paper 1's f_NL theory** — if Paper 1 revises the −35/8 derivation, Paper 3 forecast equation updates.
- **Paper 3 can reuse Paper 4's dipole infrastructure** for limitation-G (empirical bias calibration), which matters for both papers' Fisher claims.
- **Submission order should be:** Paper 4 (most self-contained) → Paper 3 → Paper 2 (depends on both) → Paper 1 (citation root). Or 3+4 in parallel, then 2, then 1.

---

## Aggregate surface-sync checklist

Every paper's "Close the gap to 100 %" section lists its own site-sync tasks. Aggregated here so the site-agent can execute them in one pass:

| Site file | Currently reflects | Should reflect |
|---|---|---|
| `index.html` stat cards | mixed / outdated | Paper 3: 37.3 M / 319,443 / 58.8 % / 4.38σ. Paper 4: 8.47 M / 0.43σ. Paper 1: 14 barriers / β = 0.27°. Paper 2: σ(f_NL) triple. |
| `paper.html` readiness table | 35 % / 85 % / 95 % / 20 % | 99 % / 97 % / TBD / TBD (match SSOT) |
| `activity.html` latest entries | — | SSOT creation + dipole-JSON gap closed (2026-04-17) |
| `data-explorer.html` datasets | core MCMC chains | + chirality catalog preview · + anomaly catalog preview |
| `figures.html` gallery | v2.2 figure set | + 11 chirality figures · + 21 paper-3 gallery figures |
| `glossary.html` | current | add: `f_NL triple role`, `TTA equivariance`, `latent dim 67`, `Landy-Szalay α` |

**One-shot sync task:** after all four SSOTs are green, run the `P-SITE-FULL-SYNC` queue item (in `queue.md`).

---

## Quick-verify commands

```bash
# Confirm nothing claims stale % outside SSOT
grep -rHn "35%\|85%\|95%\|20%" project-context wiki | grep -v SSOT/

# SSOT freshness
grep -H "Last authoritative update" project-context/SSOT/paper-*/status.md \
  project-context/SSOT/index.md project-context/SSOT/queue.md

# Principle-10 grep across all four papers
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

- ❌ `project-context/CURRENT_STATUS.md` — legacy; treat as downstream mirror. Rows there should be refreshed to match this index.
- ❌ `wiki/entities/paper-*.md` — each is now a pointer-only entry.
- ❌ `research/project_master_dossier/` — read-only historical record; do not update.
- ❌ Any `plan*.md` under `project-context/` — those are forward-looking proposals, not status.
