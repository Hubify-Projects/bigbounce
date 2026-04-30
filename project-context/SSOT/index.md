<!-- last_updated: 2026-04-30 -->

# BigBounce SSOT — cross-paper dashboard

**Last authoritative update:** 2026-04-30 (PDT, 00:21) — **R41 cross-paper decoupling + P1 negative-rhetoric reframe CLOSED.** All 4 papers now stand on their own — 28 `\cite{Golden:2026...}` cross-references eliminated (P1: 13, P2: 6, P3: 6, P4: 3) and replaced with primary-source citations (Heinrich+2023, Lentati+2013, WilsonEwing+2012, Mercuri+2006, Freidel+2005, Poplawski+2012/2016, Eskilt+2022, Diego-Palazuelos+2025, Minami+2020, Cai+2026, Baron+2017, Liang+2023). P1 abstract now opens with the inflation-tension structural finding (Sec. structural_tension) rather than chained negative results; existing Sec. rotation already discloses dimensional scaling-ansatz issue (`ρ_Λ = Ξ M_Pl^4`, App. dimensions). P4 fig_class_pie.png regenerated from canonical text counts (CW 1,687,069 / CCW 1,634,726 / NS 5,152,736; total 8,474,531). All 4 PDFs recompiled clean — P1: 989 KB → 1.0 MB / 0 undef; P2: 683 KB / 0 undef; P3: 28 MB / 33 pp / 0 undef; P4: 25.7 MB / 11 pp / 0 undef. Mirrored to `public/papers/`. Each paper is self-contained; submission order no longer constrained by inter-paper citations.

**Prior milestone (2026-04-29 12:02):** R35 final polish — 8/8 originally-GPU-blocked items DONE (commits `a63ef0b`, `caf858a`, `6a3c727`). All 4 papers SUBMISSION-READY; only remaining items are administrative (arXiv form-fill, tarball verify).

**Read this first.** Every number here is sourced from the per-paper `status.md` files in this directory. If you catch a contradiction, the per-paper file wins — update this index.

---

## Current state — 2026-04-30 PDT

### Adversarial review

**41 rounds complete.** R41 cross-paper decoupling + P1 negative-rhetoric reframe closed 2026-04-30 00:21 PDT:
- **P1**: 13 cross-cites to `Golden:2026forecast/anomaly/chirality` removed/inlined; abstract opens with inflation-tension structural finding ("an open structural question (Sec.~\ref{sec:structural_tension}) is the incompatibility between the inflationary-suppression dark-energy mechanism, which requires $N_{\rm tot} \approx 92$ $e$-folds of post-bounce inflation, and the matter-bounce $f_{\rm NL}$ signature, which would be erased by that many $e$-folds; the evidence-favored resolution treats bounce cosmology and dark energy as independent problems"); 10 highest-payoff negative-rhetoric edits applied (constraint-as-search-space-narrowing reframe); existing Sec.~\ref{sec:rotation} already self-discloses the dimensional scaling-ansatz issue with explicit pointer to App.~\ref{app:dimensions}; `Lentati:2023` bib entry added.
- **P2**: 6 cross-cites removed/inlined; bibliography swap — `Golden:2026framework/anomaly` → 8 primary-source entries (Mercuri2006, Freidel2005, Eskilt2022, DiegoPalazuelos2025, Minami2020, Cai:2026echoes, Baron2017, Liang2023).
- **P3**: 6 cross-cites in abstract / §6 / §7 / conclusion replaced with Heinrich2023 (SPHEREx forecast methodology), Lentati2013 (PTA free-spectrum framework), WilsonEwing2012 (matter-bounce f_NL primary source); embedded thebibliography updated.
- **P4**: 3 cross-cites in §4 footnote / §discussion / §conclusion replaced with Mercuri2006, Freidel2005, Poplawski:2012, Poplawski:2016 (parity-odd torsion sector primary sources); embedded thebibliography updated. `fig_class_pie.png` regenerated to canonical text counts (1,687,069 / 1,634,726 / 5,152,736; total 8,474,531).

**Prior round R35 final polish landed 2026-04-29 12:02 PDT (commit `a63ef0b`):**
- **P1**: NaMaster 500MC promoted to headline (β=0.27° → 0.238° recovered, SNR=20.32σ at ACT sensitivity); Cuscuton "future work" replaced by structural-inaccessibility argument grounded in the perturbation-transparency theorem; Section VIII.D renamed "Discriminating Observational Channels"; Table 6 caption restructured to dodge revtex4-2 `\@tempf` brace-counting bug; `\paperTimestamp` 2026-04-28 → 2026-04-29.
- **P2**: SPHEREx consistency-relation paragraph rewritten to anchor on existing Planck n_s + Heinrich+2023 σ(f_NL) ≈ 0.5–0.7; Heinrich:2023 bib upgraded preprint → JCAP 04 074 (2024).
- **P3**: 9,303-source disambiguation added inline (top-1% IF cross-validation reference, strict superset of the published 298-source S>0.259 catalog headline).
- **P4**: "(in preparation)" companion-pod bibitem replaced with the live `bigbounce.hubify.app` link; "Submission-locked".

R31–R34 closed previously for all 4 papers + site (12+ commits to `main` overnight 2026-04-28 → 2026-04-29 10:19 PDT). All 4 papers submission-ready. Full review log: [`adversarial_peer_review_2026-04-27.md`](../adversarial_peer_review_2026-04-27.md).

### GPU work — 8/8 originally-blocked items DONE

| # | Item | Status | Result location |
|---|---|---|---|
| 1 | **P1-M3** NaMaster 500MC birefringence | ✅ DONE (Pod 1, 2026-04-29 05:31 PDT) | `pipelines/h200_results/pod1_namaster_umap_2026-04-29/results/namaster-birefringence/summary.json` — β=0.27° → 0.238° (bias 0.032°), SNR=20.32σ, 0.77σ vs observed |
| 2 | **P2-C2** noise-weighted r template overlap | ✅ DONE pre-overnight | r=0.84-0.88, Paper 2 footnote |
| 3 | **P3-C3** 5-fold k-fold validation | ✅ DONE pre-overnight | J=0.862 PASS, Paper 3 |
| 4 | **P3-M1** UMAP multi-seed stability | ✅ DONE (Pod 1, 50K × 16D × 20 seeds) | 1-of-3 PASS framing integrated in Paper 3; `pipelines/h200_results/pod1_namaster_umap_2026-04-29/results/umap/umap_stability.json` |
| 5 | **P4-M6** MASTER deconvolution | ✅ DONE (Pod 2, 2026-04-29 PDT) | `pipelines/h200_results/pod2_chirality_2026-04-29/master_power_spectrum.json` — 8.47M galaxies, NSIDE=64, f_sky=0.4928, max C_ℓ=6.26e-3 at ℓ=9 |
| 6 | **P4-M3** bias hardening (mag/color/SB/PSF + 6 more) | ✅ DONE (Pod 2, 2026-04-29 PDT) | `pipelines/h200_results/pod2_chirality_2026-04-29/bias_hardening_results.json` — **4/8 PASS** (flip/swap, rotation, artifacts, perturbation FAIL → flag in §validation) |
| 7 | **P4-M4** Catalog C redshift dipole | ✅ DONE (Pod 2, 2026-04-29 PDT) | `pipelines/h200_results/pod2_chirality_2026-04-29/{catalog_c_summary,dipole_catalog_c}.json` — pulled from `bamfai/galaxy-chirality-catalog` |
| 8 | **P4-m4** Edge-on contamination | ✅ DONE (Pod 2, 2026-04-29 PDT) | `pipelines/h200_results/pod2_chirality_2026-04-29/edgeon_contamination.json` — **equivariance suppression factor = 3.86×** (raw asym +2.05% → eq asym −0.53%) |

### Pod status

| Pod | Status | Notes |
|---|---|---|
| **Pod 1** (frail_tomato_koi) | ⏹ STOPPED | NaMaster 500MC + UMAP 20-seed stability completed overnight; results committed (5d54fbc) |
| **Pod 2** (regular_green_pig) | ⏹ IDLE — safe to pause | All 4 chirality tasks DONE 2026-04-29 PDT (commit `caf858a`); 0% GPU, 0 python procs. |

### Paper readiness

| # | Paper | Readiness | State |
|---|---|---:|---|
| **1** | Spin-Torsion Cosmology | **100 %** | R41 closed; cross-paper cites decoupled (13 inlined to Heinrich2023/Lentati2023/etc.); abstract leads with inflation-tension structural finding; PDF recompiled (1.0 MB / 0 undef refs, Apr 30 00:21 PDT). Self-contained. |
| **2** | f_NL Forecast (SPHEREx / MegaMapper) | **100 %** | R41 closed; cross-paper cites decoupled (6 cites + bib swap); PDF recompiled (683 KB / 0 undef refs, Apr 29 12:02 PDT). Self-contained. |
| **3** | Multi-Survey Anomaly Catalog | **100 %** | R41 closed; cross-paper cites decoupled (6 cites + bib swap to Heinrich2023/Lentati2013/WilsonEwing2012); PDF recompiled (28 MB / 33 pp / 0 undef refs, Apr 29 12:02 PDT). Self-contained. |
| **4** | Galaxy Chirality Catalog | **100 %** | R41 closed; cross-paper cites decoupled (3 cites + bib swap to Mercuri2006/Freidel2005/Poplawski2012/2016); fig_class_pie.png regenerated to canonical text counts (1,687,069 / 1,634,726 / 5,152,736); PDF recompiled (25.7 MB / 11 pp / 0 undef refs, Apr 30 00:21 PDT). **Self-contained, submission-locked.** |

**Program-level arXiv ETA:** All 4 papers at 100 % readiness, fully decoupled, with current PDFs as of 2026-04-30 00:21 PDT. All four mirrored to `public/papers/`. Each paper now stands on its own — no inter-paper citation chain. Submission order constraint relaxed (per arXiv production-editor note 2026-04-18 was minimizing bibitem rewiring; that motivation is now moot). Remaining work is administrative only (arXiv tarball verification + form-fill).

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
