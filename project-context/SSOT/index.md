# BigBounce SSOT — cross-paper dashboard

**Read this first.** Every number here is sourced from the per-paper `status.md` files in this directory. If you catch a contradiction, the per-paper file wins — update this index.

Last authoritative update: 2026-04-17

---

## Program health at a glance

| # | Paper | One-line status | Ready for arXiv | Gap to 100 % | Canonical source | SSOT |
|---|---|---|---:|---|---|---|
| **1** | **Spin-Torsion Cosmology** | v2.3.0, 24 pp, 63+ refs, 10+ revision rounds. Likely the most mature paper but SSOT sweep pending. Known todo: integrate real β = 0.264° birefringence result. | **TBD** (est. 90-95 %) | sweep pending → see `paper-1/status.md` | `arxiv/main.tex` | [paper-1/status.md](paper-1/status.md) |
| **2** | **f_NL Forecast (SPHEREx / MegaMapper)** | v1.3.0, 12 pp. Matter-bounce f_NL = −35/8 detectable at 4.7–12σ by 2027. SSOT sweep pending. | **TBD** (est. 90-95 %) | sweep pending → see `paper-2/status.md` | believed: `research/focused_paper_source_integration/02_full_draft.tex` | [paper-2/status.md](paper-2/status.md) |
| **3** | **Multi-Survey Anomaly Catalog** | Locked 2026-04-16. 8 surveys · 37.3 M sources · 319,443 anomalies · 58.8 % novel · σ(f_NL) +16.4 % · SPHEREx 4.38σ · NANOGrav γ = 3.20 ± 0.42. | **99 %** | 8 queue tasks (P3-A..H, PDF, site sync, HF upload) | `pipelines/p3_anomaly_engine/paper3_draft.tex` | [paper-3/status.md](paper-3/status.md) |
| **4** | **Galaxy Chirality Catalog** | Science-complete. 8.47 M galaxies · 8/8 bias tests · 0.43σ null dipole · Shamir refuted 7×. Dipole JSON gap closed 2026-04-17. | **97 %** | 7 queue tasks (JSON rebuild, PDF recompile, site sync, Paper 2 cross-ref) | `pipelines/p2_chirality/chirality_catalog_paper.tex` | [paper-4/status.md](paper-4/status.md) |

**Program-level arXiv ETA:** Papers 3 and 4 can submit within **1 week** after queue completion. Papers 1 and 2 need forensic sweeps first to set honest timelines.

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
