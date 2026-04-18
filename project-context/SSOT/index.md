# BigBounce SSOT — cross-paper dashboard

**Read this first.** Every number here is sourced from the per-paper `status.md` files in this directory. If you catch a contradiction, the per-paper file wins — update this index.

Last authoritative update: 2026-04-17 (post P1/P2/P3/P4 PDF-RECOMPILE + P1-CORNER-PLOTS + P4-DIPOLE-JSON-REBUILD + P-SITE-FULL-SYNC: figures.html, data-explorer.html, glossary.html all synced to current catalogs)

---

## Program health at a glance

| # | Paper | One-line status | Ready for arXiv | Gap to 100 % | Canonical source | SSOT |
|---|---|---|---:|---|---|---|
| **1** | **Spin-Torsion Cosmology** | v2.3.0, 27 pp, 63+ refs, 10+ revision rounds. Most mature paper. β = 0.264° ALP already integrated (L391). **2026-04-17:** P1-LINE-299-WORDSMITH ✓ + P1-FIGURES-VERIFY ✓ + P1-WIKI-SYNC ✓ + P1-TARBALL (partial) + **P1-PDF-RECOMPILE ✓** (707 KB, 0 undef) + **P1-CORNER-PLOTS ✓** (H0=67.69±1.06, ΔNeff=-0.019±0.169 on 119,617 samples) + **P1-§IV-CORNER-TEXT ✓** (corner figure inserted at L882) + **P1-SITE-SYNC ✓** (index stat card + figures.html gallery Figure 22). Remaining: re-compile PDF with new §IV figure. | **99.9 %** | 7 queue tasks — 6 done + 1 partial | `arxiv/main.tex` | [paper-1/status.md](paper-1/status.md) |
| **2** | **f_NL Forecast (SPHEREx / MegaMapper)** | v1.6.0, 375 lines, 6 figures. Science complete: σ(f_NL) forecasts, Bayes factors 8–17, bias validation 1.58× on Gold+Silver QSOs. **2026-04-17:** P2-CURRENT-STATUS-SYNC ✓ + P2-WIKI-POINTER ✓ + P2-XREF-AUDIT ✓ + P2-REVTEX4-2-CONVERT ✓ + P2-TARBALL ✓ + **P2-COMPILE-POD ✓** (614 KB, 0 undef, abstract+sec:viable fixed) + **P2-BIB-RESOLVE ✓** (0 `[?]`) + **P2-PDF-PUBLISH ✓** (file committed) + **P2-SITE-SYNC ✓** (paper.html badge + index badge + glossary f_NL entry). | **99 %** | 9 queue tasks — 9 done | `research/focused_paper_source_integration/02_full_draft.tex` | [paper-2/status.md](paper-2/status.md) |
| **3** | **Multi-Survey Anomaly Catalog** | Locked 2026-04-16. 8 surveys · 37.3 M sources · 319,443 anomalies · 58.8 % novel · σ(f_NL) +16.4 % · SPHEREx 4.38σ · NANOGrav γ = 3.20 ± 0.42. **2026-04-17:** **P3-PDF-RECOMPILE ✓** (27 MB, 27 pp, 21 figs embedded, 0 undef) + **P3-SITE-SYNC ✓** (data-explorer p3AnomalyCatalog + p3SimbadNovelty, glossary Anomaly-engine + Landy-Szalay). | **99.5 %** | 8 queue tasks — 4 done + 4 open (P3-A..C, HF upload) | `pipelines/p3_anomaly_engine/paper3_draft.tex` | [paper-3/status.md](paper-3/status.md) |
| **4** | **Galaxy Chirality Catalog** | Science-complete. 8.47 M galaxies · 8/8 bias tests · 0.43σ null dipole · Shamir refuted 7×. **2026-04-17:** **P4-DIPOLE-JSON-REBUILD ✓** + **P4-PDF-RECOMPILE ✓** (25 MB, 11 pp, 0 undef) + P4-HF-DOI ✓ + **P4-PDF-CANON ✓** (38-line pointer stub verified) + **P4-PAPER2-XREF ✓** + **P4-SITE-SYNC ✓** (figures.html 8.47 M rewrite, data-explorer p4ChiralityCatalog + p4TTABiasTests, glossary TTA entry). | **99.5 %** | 7 queue tasks — 6 done + 1 open (LSST line) | `pipelines/p2_chirality/chirality_catalog_paper.tex` | [paper-4/status.md](paper-4/status.md) |

**Program-level arXiv ETA:** All four papers compile cleanly on pod as of 2026-04-17 — revtex4-2, 0 undefined refs, figures embedded. Paper 2's revtex4-2 conversion (including abstract placement + `sec:viable`→`sec:benchmark` fix) landed today, closing the only remaining format-compliance gap. Remaining blockers are **site-sync only**: all four papers need `figures.html` / `paper.html` / `data-explorer.html` entries refreshed. Recommended submission order: Paper 4 → Paper 3 → Paper 1 → Paper 2 (or 3+4 in parallel, then 1+2 together).

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
