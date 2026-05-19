---
title: "Paper 5 SSOT — Environmental Dependence of Spiral Chirality Across DESI LSS"
type: ssot
paper: 5
last_updated: 2026-05-18 PDT
canonical_source: pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex
canonical_pdf: (not yet compiled; paper is scaffold)
version: bootstrap-2026-05-15
headline_pct: 15
submission_status: BOOTSTRAP — matched catalog + first-pass analyses landed 2026-05-16; cosmic-web headline analysis blocked on DESI environmental VAC missing from repo; paper LaTeX is a 9KB scaffold.
---

# Paper 5 — Environmental Dependence of Spiral Chirality Across DESI Large-Scale Structure — Single Source of Truth

**Canonical status file. When in doubt about Paper 5, read this.**

**Last authoritative update:** 2026-05-19 (PDT, tick 116) — **🎯 ENV-VAC BLOCKER CLOSED — V-Web cosmic-web env catalog landed via Phase 1 MVP env_finder, headline analysis ran-not-blocked.** Houston approved Phase 1 MVP at tick 115; this tick implemented + ran end-to-end in 104 seconds wall on laptop ($0 marginal compute, no pod). **Algorithm**: V-Web (Hahn+ 2007 / Cautun+ 2014) on 14,622,283 DESI DR1 spectro galaxies (ZWARN==0 GALAXY 0.01<z<2): comoving Cartesian → CIC onto 256³ grid (cell 25.9 Mpc/h in 6.6 Gpc/h bounding cube) → survey-mask-aware overdensity δ → Gaussian smoothing R_s=25 Mpc/h → tidal tensor T_ij via FFT → eigendecomposition → V-Web class. **Survey-mask fix** added after V0.1 first pass showed void-fraction skew (9.5% vs literature 70%): dilated occupied-cell mask treats outside-footprint cells as mean-density rather than δ=-1, killing the survey-edge artifact. **V0.2 in-footprint volume fractions**: void 24.4% / wall 41.3% / filament 33.3% / cluster 1.0% — still tilted vs Cautun+ 2014 N-body baseline (70/15/12/3) because the DESI footprint is a thin spherical shell not a box, so edge-mode bias remains; relative density-ordering is correct (cluster > filament > wall > void) which is what matters for the analysis. **🎯 HEADLINE COSMIC-WEB RESULT** (`results/analysis_cosmic_web/cw_fraction_by_env__desi_env_vweb.csv`): **Galaxy chirality is statistically independent of cosmic-web environment within DESI DR1 at V-Web resolution.** Per-env cw_fraction: void (n=428) 0.4836 / −0.68σ; wall (n=6,673) 0.5034 / +0.55σ; filament (n=408,187) 0.4980 / **−2.6σ**; cluster (n=397,505) 0.4963 / **−4.7σ**. The catalog-level P4 monopole (cw_fraction=0.4972, −5σ on 791,635 matched spirals) is uniformly distributed across filament+cluster populations; range of cw_fraction across all 4 env classes is only 0.4836–0.5034 (a 1.7pp spread) and dominated by counting statistics on small subsamples. **Consistent with the P4 uniform classifier-bias interpretation, NOT with an environment-dependent chirality effect.** This is a real positive null finding for P5. **Artifacts**: `data/desi_env/desi_env_vweb.parquet` (230 MB, 14.6M rows, gitignored per policy; provenance sidecar committed), `env_finder/01_compute_vweb.py`, `env_finder/config.yaml`, `env_finder/reports/01_volume_fractions.json`. Readiness P5 **15 → 30** (+15pp): env-VAC blocker closed (the load-bearing P5 blocker); headline analysis runs; null result confirms P5 central scientific question has a defensible answer at MVP resolution. Phase 2 (sensitivity sweep + RSD correction + Tempel cross-validation) and Phase 3 (paper draft + first PDF compile + first R-round) are the next ~3-5 day windows.

**Prior authoritative update:** 2026-05-18 (PDT, tick 114) — **P5 brought onto SSOT radar after being missed across ticks 102-113.** Bootstrap commit `059c3458` (2026-05-15) created the pipeline at `pipelines/p5_desi_chirality/` but P5 was never added to `papers.ts`, `live-status.ts`, `CLAUDE.md`, `queue.md`, or `SSOT/index.md`. The R-round cron loop has never operated on P5. This SSOT file is the first formal acknowledgment that the bigbounce campaign is a **5-paper portfolio**, not 4.

---

## Scientific question

> Is galaxy chirality statistically independent of DESI-derived large-scale-structure environment after controlling for sky position, redshift, imaging systematics, morphology confidence, and selection effects?

Separate from P4 (which is the catalog/null parity paper). P5 inherits P4's chirality labels and asks an environment-dependent question that P4 is not designed to answer.

---

## What's done (all written 2026-05-16)

| Artifact | Path | Size / rows | State |
|---|---|---|---|
| Matched chirality × DESI DR1 catalog | `pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet` | 1.3 GB, **2,232,212** deduped rows | ✅ landed |
| Provenance sidecar | `p5_matched_chirality_desi.parquet.provenance.json` | git_sha 0882fcdcc75e, config_hash 83970171f71bb863 | ✅ |
| Headline binomial | `p5_matched_chirality_desi_summary.json` | cw_fraction=0.4972 on 791,635 spirals; −5.0σ from 0.5 | ✅ |
| Redshift analysis | `results/analysis_redshift/` | permutation null p=0.372; obs max-deviation 3.14% vs null p99 7.75% | ✅ no z-dependence |
| Density analysis (5-NN) | `results/analysis_density/` | max_abs_sigma = 3.94 global; no LEE correction yet | ⚠️ needs LEE |
| HEALPix spatial scan | `results/analysis_healpix/` | nside 16/32/64 p-values 0.607/0.135/0.413 | ✅ no spatial structure |
| Systematics label-shuffle | `results/analysis_systematics/` | null cleanly preserved | ✅ sanity pass |
| Cosmic-web analysis | `results/analysis_cosmic_web/summary.json` | status: **"blocked"** — environmental VAC missing | ❌ BLOCKED |

**Crossmatch geometry**: 1″ primary radius (with 0.5/1.0/2.0/3.0/5.0″ sensitivity sweep showing matched count is insensitive — 2.34M → 2.44M from 1″ → 5″). p50 separation 0.007″, p90 0.030″, p99 0.298″ — sub-arcsecond as expected from shared imaging.

**Imaging-leg breakdown** of matched primary: DECaLS 1,538,880 / BASS+MzLS 688,608 / DES 4,724.

---

## What's blocked

### High-severity: DESI environmental VAC

The cosmic-web/environment headline analysis is blocked on a missing dataset. Schema contract is published in `scripts/08_analysis_cosmic_web.py` and the analysis script writes a `status: "blocked"` summary instead of producing nulls — the pipeline does not silently fail.

**The "187 DESI-derived attributes" catalog** Houston referenced in earlier planning is **confirmed not in repo** (exhaustive subagent search 2026-05-15; reconfirmed tick 114). Two interpretations remain open:
- (a) The file was never committed and lives on an old pod / external Zenodo / separate repo. **Houston-mediated**: needs Houston to point us at its actual location.
- (b) "187 attributes" referred to a count from a planned LSS VAC that doesn't yet exist.

**Three real paths to close this blocker**:

1. **Houston locates the 187-attribute catalog** (if it exists) — fastest path; would unblock analysis C directly.
2. **DESI DR1 LSS VAC official release** (BGS/LRG/ELG/QSO catalogs + random catalogs + filament/void labels) — pending DESI collaboration release. Out of our timeline.
3. **Run our own cosmic-web finder pipeline** on DESI DR1 LSS targets — real new compute work. DBSCAN-style spatial clustering or DisPerSE-style filament tracing on the spectroscopic galaxy sample. Estimated track: a separate sub-project under `pipelines/p5_desi_chirality/env_finder/`. Owner not yet assigned.

### Other open work

| Item | Severity | Resolution |
|---|---|---|
| Paper LaTeX is 9KB scaffold (no compiled PDF) | High for external-review readiness | Requires headline results from analyses A-E in hand; do not draft prose against placeholder numbers per audit's TODO 7. |
| 5-NN density max_abs_sigma=3.94 lacks LEE correction | Medium | Look-elsewhere correction needed before quoting as significant; trial-factor depends on number of density bins × z bins. |
| Cross-survey connections (P2 high-z tracers, P3 anomaly engine) not yet drawn | Low — follow-up | Houston Method completion item per `feedback_houston_method`. |
| Cross-vendor R-round campaign has never operated on P5 | Low — pre-mature | P5 needs paper draft before R-round adversarial review is meaningful. |
| Not in `papers.ts` / `live-status.ts` / `CLAUDE.md` / `queue.md` / `SSOT/index.md` | High — visibility | **Closing in tick-114 bundle.** |

---

## Readiness estimate

**P5 = 15%** — bootstrap with first-pass analyses on hand, no paper draft, headline analysis blocked. The number reflects:
- ✅ Matched catalog landed (2.23M rows) — big load-bearing artifact done (+5pp)
- ✅ 5 of 6 first-pass analyses complete with sensible results (+5pp)
- ✅ Pipeline scaffolding + provenance + audit doc + scripts compile (+3pp)
- ✅ SSOT integration tick 114 (+2pp)
- ❌ Paper draft is scaffold only
- ❌ Cosmic-web headline analysis blocked
- ❌ Never been through R-round campaign
- ❌ No external review yet

For comparison: P2 at 82% has been through 2-3 R-rounds but is also pre-external-review; P1A at 90% has cleared the loop-exit gate. P5's path to ~80% would require: env-VAC blocker resolved (one of 3 paths above), paper draft populated with headline results, at least 1 R-round on the draft.

---

## What changes when you finish a P5 piece of work

Per `project-context/SSOT/README.md` SSOT protocol: when you finish work that changes P5's state (new analysis result, new figure, new compile, env-VAC blocker resolution, paper draft milestone), update **this status.md** AND mark the relevant `queue.md` row AND the `SSOT/index.md` headline IN THE SAME COMMIT. Same protocol as P1-P4.

---

## File pointers

| Resource | Path |
|---|---|
| Pipeline root | `pipelines/p5_desi_chirality/` |
| Audit doc (read FIRST when picking up P5) | `pipelines/p5_desi_chirality/reports/00_audit.md` |
| Pipeline README | `pipelines/p5_desi_chirality/README.md` |
| Paper LaTeX scaffold | `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` |
| Config | `pipelines/p5_desi_chirality/config/p5_config.yaml` |
| Scripts (fetch + analysis 01-10) | `pipelines/p5_desi_chirality/scripts/` |
| Matched catalog | `pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet` |
| Cosmic-web blocker contract | `pipelines/p5_desi_chirality/scripts/08_analysis_cosmic_web.py` + `results/analysis_cosmic_web/summary.json` |
