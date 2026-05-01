// Live build status surfaced at the top of every page.
// Updated each cron fire / wave-close commit. Renders into <LiveStatus />.
// Timestamp is baked in at build time — bump on every commit that ships
// research progress so Vercel rebuilds put the new value live.

export interface PaperProgress {
  slug: string;
  number: number;
  shortTitle: string;
  version: string;
  readiness: number; // percent 0-100
}

export interface LiveStatus {
  lastUpdatedISO: string; // ISO 8601 UTC, baked at build time
  lastUpdatedDisplay: string; // human-readable PT timestamp for the banner
  headline: string; // "Wave 14-D LANDED — P4 v1.0.9 ..."
  summary: string; // 1-2 sentences, what just shipped
  papers: PaperProgress[]; // 4 papers, sorted by number
  blockerTally: {
    closed: number;
    openBlockers: number;
    openMajors: number;
    openMinors: number;
  };
  cronStatus: string; // "*/20 cron firing — autonomous loop active"
  etaToCompletion: string; // human-readable ETA to all-4 papers @ 100%
  pods: Array<{
    name: string;
    state: "active" | "idle" | "queued";
    note: string;
  }>;
}

export const liveStatus: LiveStatus = {
  lastUpdatedISO: "2026-05-02T14:15:00Z",
  lastUpdatedDisplay: "May 2, 2026 · 7:15 AM PT",
  headline:
    "Readiness rule clarified · 99% is the cap until Houston signs off + an external peer-review round closes with zero MAJOR/MINOR findings · the final 1% is reserved for that sign-off, not awarded by the cron · per-paper now reads: P1 99% · P2 99% · P3 98% · P4 96% (Wave 14-JJ P4-CM-B2 PSF cross-correlation BLOCKER in flight on Pod 3 H200) · 39 R42 cross-model findings closed · 1 conditional BLOCKER + 6 open MAJORs + 13 open MINORs across all 4 papers · Wave 14-II LANDED earlier (P3 v3.1.14 → v3.1.15 quantitative systematics-marginalization Fisher recompute, FULL HARD FIX of P3-CM-M1) · Wave 14-FF/EE/DD chirality grid + DR8 b/a fetch carried forward",
  summary:
    "Readiness model corrected per Houston directive (2026-05-02 07:15 PT): no paper reads 100% until two gates close — (1) Houston personally signs off and (2) the next external peer-review round closes with zero MAJOR / MINOR findings. The cron alone cannot award the final 1%; that is reserved for the human + adversarial-review sign-off. Per-paper today: **P1 = 99%** (Spin-Torsion — all R42 BLOCKERs closed, all known cross-model MAJORs closed Wave 14-Z; residual is the 13 open MINORs across the program plus the standing arXiv tarball / form-fill admin step), **P2 = 99%** (f_NL Forecast — Wave 14-AA closed both Gemini-3.1-Pro MAJORs M-1 / M-2; Wave 14-K closed BLOCKER B-3; residual is text-polish MINORs), **P3 = 98%** (Anomaly Catalog — Wave 14-II FULL HARD FIX of P3-CM-M1 just landed; P3-OA-M9 NANOGrav Bayesian rerun on Pod 3 H200 still pending compute; some MINORs open), **P4 = 96%** (Chirality Catalog — Wave 14-JJ P4-CM-B2 PSF cross-correlation BLOCKER in flight on Pod 3 H200, NOT yet confirmed closed; Gemini P4 B-1 NaMaster recompute pending; OpenAI P4 B5 / B7 / M-1 / M-5 / M-7 / M-9 compute-heavy MAJORs queued). Average readiness across the four papers: ~98%. Banner / paper.html / SSOT all aligned to these numbers in the same commit. The cron will continue closing R42 residuals, but a paper progressing past 99% requires Houston's sign-off plus a clean external round; that is now the load-bearing gate, not a wave-cadence calculation. Wave 14-II carried forward: Pod 3 H200 6.0s wall pure-NumPy multi-tracer Fisher with (4n+1)-dim nuisance block per tracer × (k,z) cell, σ(f_NL)_marg ∈ [0.067, 0.116] floor across 6 SPHEREx/DESI/anomaly configs, δs dominant, δb broken by multi-tracer cross-correlations. Wave 14-FF/EE/DD carried forward: 2D morphology grid + D4 TTA + DR8 b/a fetch confirm chirality asymmetry is morphology-flat. SPARCL fetch (PID 25860) still alive at ~13% / ETA ~80h on separate CPU core. Wave 14-JJ continues on Pod 3 (patch 3 = pre-bin NaN-row filter applied). Bundled UI/design carries forward: banner homepage-only, compact-by-default with toggle, LA 12-hr timestamp, paper PDF UX, mirror-effect favicon, galaxy/anomaly-explorer Next routes, 45 routes 0 errors.",
  papers: [
    {
      slug: "spin-torsion",
      number: 1,
      shortTitle: "Spin-Torsion Cosmology",
      version: "v2.3.14",
      readiness: 99, // R42 BLOCKERs all closed (Wave 14-U last); MAJORs all closed (Wave 14-Z last). Final 1% gated on Houston sign-off + clean external peer-review round.
    },
    {
      slug: "fnl-forecast",
      number: 2,
      shortTitle: "f_NL SPHEREx Forecast",
      version: "v1.7.8",
      readiness: 99, // P2-CM-B3 closed Wave 14-K; P2-CM-M1+M2 closed Wave 14-AA. Final 1% gated on Houston sign-off + clean external peer-review round.
    },
    {
      slug: "anomaly-catalog",
      number: 3,
      shortTitle: "Multi-Survey Anomaly Catalog",
      version: "v3.1.15",
      readiness: 98, // Wave 14-II FULL HARD FIX of P3-CM-M1 just landed; P3-OA-M9 NANOGrav Bayesian rerun still pending Pod 3 H200 compute; residual MINORs open.
    },
    {
      slug: "chirality-catalog",
      number: 4,
      shortTitle: "Galaxy Chirality Catalog",
      version: "v1.0.16",
      readiness: 96, // Wave 14-JJ P4-CM-B2 PSF cross-correlation BLOCKER in flight on Pod 3 (patch 3 NaN-row filter applied, not yet confirmed closed); Gemini P4 B-1 NaMaster recompute pending; OpenAI P4 B5/B7/M-1/M-5/M-7/M-9 compute-heavy MAJORs queued.
    },
  ],
  blockerTally: {
    closed: 39, // R42 cross-model findings closed cumulative
    openBlockers: 1, // Wave 14-JJ P4-CM-B2 PSF cross-correlation in flight on Pod 3, conditional close on patch-3 success
    openMajors: 6,
    openMinors: 13,
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA per paper to 99% (cron-driven, Houston sign-off + clean external peer-review round still required for the final 1%): P1 99% NOW (residual MINORs only — text polish, ~2-4 h cron-driven); P2 99% NOW (residual MINORs only — ~1-2 h cron-driven); P3 → 99% in ~6-12 h (P3-OA-M9 NANOGrav Bayesian rerun on Pod 3 H200 ~2-4 h GPU + cheap-fast residual MINORs ~1-2 h); P4 → 99% in ~12-24 h (Wave 14-JJ P4-CM-B2 PSF cross-correlation must confirm close ~1-2 h on Pod 3 + Gemini P4 B-1 NaMaster recompute ~2-4 h + OpenAI P4 B5/B7/M-1/M-5/M-7/M-9 compute-heavy MAJORs ~6-12 h aggregate). After all four hit 99%, the next external peer-review round (R43) gets the current PDFs; if R43 closes with zero MAJOR / MINOR findings AND Houston signs off, papers move to 100%. The cron does not award the final 1%. SPARCL fetch (PID 25860) at ~13% / ETA ~80h on separate CPU core, does not block GPU dispatch.",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-FF LANDED 14:35 PDT (3-min pandas-only 2D morphology grid on the in-memory 8.47M joined catalog): 4-quadrant cw_fraction stratification (DEV-edge / disk-edge / DEV-face / disk-face) shows cross-bin range 0.00142 < 2× max bin SE 0.00185 → morphology-flat verdict. Tightest cuts (fracdev>0.7 ∩ b/a<0.3 and fracdev<0.3 ∩ b/a<0.3) STILL hold the asymmetry, locking P4-CM-M2 PUSHBACK closure with a 2D-stratified second-pass test. Wave 14-DD LANDED 14:21 PDT (run time ~30 min, 8-thread parallel ThreadPoolExecutor, 4400+ chunks/hr sustained, 0 failed chunks): 8,474,531 unique dr8_ids fetched and merged from ls_dr8.tractor via NOIRLab Astro Data Lab Datalab queryClient. fracdev-weighted effective shape parameters materialized with b/a = (1-|e|)/(1+|e|), e_mag = sqrt(e1²+e2²). Output parquet 860.8 MB at /workspace/dr8_sweep_fetch/catalog_production_with_ba.parquet. Coverage: b/a non-null 7,728,567 (91.2% recovery — 8.8% PSF/REX rows have undefined shape by design); b/a<0.3 edge-on candidates 785,859; b/a<0.5 mostly-edge 2,447,858; b/a>0.7 face-on 2,855,862. Wave 14-EE LANDED 14:27 PDT (4-min pandas-only join + binomial Wald z-stat, 0 GPU usage): JOINED b/a parquet with existing chirality catalog catalog_production.parquet on dr8_id → CW-fraction binomial z-stat confirmed morphology-FLAT asymmetry: full 0.49735±0.00028 z=-9.5σ ≡ b/a<0.3 edge-on 0.49753±0.00073 z=-3.4σ ≡ b/a>0.7 face-on 0.49734±0.00056 z=-4.7σ ≡ fracdev<0.1 disk 0.49702±0.00038 z=-7.8σ ≡ fracdev>0.9 DEV 0.49772±0.00044 z=-5.1σ — all eight subsamples agree to 4-5 decimal places on cw_fraction. R42 P4-CM-M2 D4 closes as PUSHBACK: the residual ~-0.265% offset survives in equivariant Catalog C and is NOT b/a-dependent → D4 TTA equivariance is preserved on rotated edge-ons; offset is consistent with the post-Platt-calibration residual disclosed at L815 of chirality_catalog_paper.tex. Result JSON saved to pipelines/p3_anomaly_engine/r42_results/wave_14_ee_d4_tta_results.json. Pod 3 H200 GPU still genuinely idle (Waves 14-EE and 14-FF were both pandas-only) and ready for next compute-medium dispatch — natural candidates: (a) Wave 14-GG P3 systematics-marginalization Fisher recompute (~1-2h dev + ~30-60min run, GPU-bound linear algebra, P3 96 → 100 lever), (b) Wave 14-HH P3-OA-M9 NANOGrav Bayesian rerun on Pod 3 H200, (c) Wave 14-II BigAE retraining on the joined 8.47M-row catalog with morphology features. SPARCL fetch (PID 25860, alive 12h+) still on separate CPU core at ~13% / ETA ~80h, does not contend with GPU. $0 marginal H200 spend on Wave 14-DD + Wave 14-EE + Wave 14-FF bundled close (DD was IO/network-bound, EE+FF were pandas-only).",
    },
  ],
};
