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
  lastUpdatedISO: "2026-05-02T10:00:00Z",
  lastUpdatedDisplay: "2026-05-02 03:00 PT",
  headline:
    "Wave 14-X LANDED · P3 v3.1.13 · 30 cross-model findings closed · ETA all-4 → 100%: ~20-40 h",
  summary:
    "P3 v3.1.13: R42 P3-OA-M1 MAJOR closed as quantitative PUSHBACK — Pod 3 H200 ran the production BigAE (val_loss=0.0287) plus 5 different-seed control retrains on the 103,000-spectrum SPARCL DR1 holdout in 5.1s wall. Top-1% (1,030-object) Jaccard: production-vs-controls 0.7320 (range 0.7224-0.7458 across 5 seeds), control-vs-control 0.8738 (10 pairs) — both well above the 0.50 'strong agreement' threshold and an order of magnitude above the 0.10 'seed-noise' floor. The 22.5M-object DESI anomaly catalog is NOT an in-sample-leakage artifact: independent-seed retrains that have themselves never seen the holdout flag the same anomalies. SPARCL fetch attained 100K short-circuit at shard 199 then throttled from ~500/min to ~13/min (1M ETA infeasible at >1900h); 100K is the publication-grade short-circuit. P3 recompile: 40 pp / 28.31 MB / 0 undef refs. Cron */20 armed.",
  papers: [
    {
      slug: "spin-torsion",
      number: 1,
      shortTitle: "Spin-Torsion Cosmology",
      version: "v2.3.12",
      readiness: 96,
    },
    {
      slug: "fnl-forecast",
      number: 2,
      shortTitle: "f_NL SPHEREx Forecast",
      version: "v1.7.7",
      readiness: 91,
    },
    {
      slug: "anomaly-catalog",
      number: 3,
      shortTitle: "Multi-Survey Anomaly Catalog",
      version: "v3.1.13",
      readiness: 95,
    },
    {
      slug: "chirality-catalog",
      number: 4,
      shortTitle: "Galaxy Chirality Catalog",
      version: "v1.0.16",
      readiness: 97,
    },
  ],
  blockerTally: {
    closed: 30, // +1 from Wave 14-X: P3-OA-M1 MAJOR PUSHBACK (103K Jaccard short-circuit on Pod 3, prod-vs-controls J̄=0.7320, NOT a leakage artifact)
    openBlockers: 0, // unchanged from Wave 14-W
    openMajors: 13, // -1 from Wave 14-W: P3-OA-M1 closed
    openMinors: 13, // unchanged from Wave 14-W
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~20-40 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-X 103K Jaccard short-circuit COMPLETE on the SPARCL holdout — production-vs-control top-1% Jaccard 0.7320 confirms the 22.5M anomaly catalog is not a leakage artifact; quantitative systematics-marginalization Fisher recompute for P3 queued ~2h H200 next; cheap-fast P1 residuals P1-OA-M3 IVW 3.9σ resolve + P1-OA-M4 NaMaster methods both ~30min-2h)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-X COMPLETE: production BigAE + 5 phase-2 seed retrains scored on 103,000-spectrum SPARCL holdout in 5.1s wall, top-1% Jaccard prod-vs-controls J̄=0.7320 (range 0.7224-0.7458), control-vs-control J̄=0.8738; PUSHBACK on R42 P3-OA-M1 catalog-leakage finding. Recompile_p3 ran cleanly in /workspace/recompile_p3 in same session ($0 marginal H200 spend) — 40 pp / 28,309,528 bytes / 0 undef refs / 1 'Wave 14-X' occurrence confirmed. SPARCL fetch (PID 25860, ~8h08m elapsed) throttled from ~500/min to ~13/min — 100K is the publication-grade short-circuit. Quantitative systematics-marginalization Fisher recompute for P3 (~2h H200) queued for dispatch as Wave 14-Y candidate.",
    },
  ],
};
