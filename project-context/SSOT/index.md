# BigBounce SSOT — cross-paper dashboard

**Read this first.** Every number here is sourced from the per-paper `status.md` files in this directory. If you catch a contradiction, the per-paper file wins — update this index.

Last authoritative update: 2026-04-17

---

## Program health at a glance

| # | Paper | One-line status | Ready for arXiv | Gap to 100 % | Canonical source | SSOT |
|---|---|---|---:|---|---|---|
| **1** | **Spin-Torsion Cosmology** | v2.3.0, 24 pp, 63+ refs, 10+ revision rounds. Most mature paper. β = 0.264° ALP already integrated (L391). Compiles clean, 0 undefined refs. Remaining: 1 TBD wordsmith (L299), corner plots from existing chains (L882 "companion data release" note), figure-embedding verify (510 KB PDF is low), tarball + site sync. | **99 %** | 7 queue tasks (P1-LINE-299, P1-FIGURES-VERIFY, P1-CORNER-PLOTS, P1-PDF-RECOMPILE, P1-SITE-SYNC, P1-WIKI-SYNC, P1-TARBALL) | `arxiv/main.tex` | [paper-1/status.md](paper-1/status.md) |
| **2** | **f_NL Forecast (SPHEREx / MegaMapper)** | v1.6.0, 375 lines, 6 figures. Science complete: σ(f_NL) forecasts, Bayes factors 8–17, bias validation 1.58× on Gold+Silver QSOs. **BLOCKER: document class is `article` + `natbib`, NOT revtex4-2.** Current PDF has `[?]` placeholder refs. 1–2 days of mechanical conversion. | **85 %** | 9 queue tasks (P2-REVTEX4-2-CONVERT, P2-BIB-RESOLVE, P2-COMPILE-POD, P2-XREF-AUDIT, P2-SITE-SYNC, P2-WIKI-POINTER, P2-CURRENT-STATUS-SYNC, P2-PDF-PUBLISH, P2-TARBALL) | `research/focused_paper_source_integration/02_full_draft.tex` | [paper-2/status.md](paper-2/status.md) |
| **3** | **Multi-Survey Anomaly Catalog** | Locked 2026-04-16. 8 surveys · 37.3 M sources · 319,443 anomalies · 58.8 % novel · σ(f_NL) +16.4 % · SPHEREx 4.38σ · NANOGrav γ = 3.20 ± 0.42. | **99 %** | 8 queue tasks (P3-A..H, PDF, site sync, HF upload) | `pipelines/p3_anomaly_engine/paper3_draft.tex` | [paper-3/status.md](paper-3/status.md) |
| **4** | **Galaxy Chirality Catalog** | Science-complete. 8.47 M galaxies · 8/8 bias tests · 0.43σ null dipole · Shamir refuted 7×. Dipole JSON gap closed 2026-04-17. | **97 %** | 7 queue tasks (JSON rebuild, PDF recompile, site sync, Paper 2 cross-ref) | `pipelines/p2_chirality/chirality_catalog_paper.tex` | [paper-4/status.md](paper-4/status.md) |

**Program-level arXiv ETA:** Papers 1, 3, 4 can submit within **1 week** after their respective queues complete (all are revtex4-2 compliant and 97 %+ ready). Paper 2 needs a mandatory revtex4-2 conversion (~4 h of work) before it can submit — add 1–2 days to its timeline. Recommended submission order: Paper 4 → Paper 3 → Paper 1 → Paper 2 (or Paper 1 + 2 together once Paper 2's conversion lands).

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
