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
  lastUpdatedISO: "2026-05-02T06:50:00Z",
  lastUpdatedDisplay: "2026-05-01 23:50 PT",
  headline:
    "Wave 14-T LANDED · P4 v1.0.16 · 26 cross-model findings closed · ETA all-4 → 100%: ~28-50 h",
  summary:
    "P4 v1.0.16: R42 R1 m5 Shamir refs given years (2022) + (2020, 2022). 19 pp / 25.79 MB recompile clean on Pod 3 (0 undef refs). SPARCL 1M fetch ~7h in at ~195 spectra/min (~82,500 spectra so far); 100K sub-sample short-circuit imminent. Cron */20 armed; banner refreshes every 15 min.",
  papers: [
    {
      slug: "spin-torsion",
      number: 1,
      shortTitle: "Spin-Torsion Cosmology",
      version: "v2.3.9",
      readiness: 95,
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
      version: "v3.1.12",
      readiness: 94,
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
    closed: 26, // +1 from Wave 14-T: R42 m5 P4 Shamir-refs-need-years (cheap-fast precise-citation path)
    openBlockers: 1, // unchanged from Wave 14-S
    openMajors: 16, // unchanged from Wave 14-T (m5 was a MINOR, not a MAJOR)
    openMinors: 13, // -1 from Wave 14-T: m5 P4 Shamir years closed (was a MINOR)
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~28-52 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-B 1M Jaccard fetch ~74 h on sustained ~195 spectra/min full-window throughput, 100K sub-sample short-circuit (~5 h from this commit) remains strongly recommended on cost/cadence grounds; quantitative systematics-marginalization Fisher recompute for P3 queued ~2h H200 once Pod 3 frees up)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-B 1M SPARCL fetch in flight (PID 25860, ~6h47m elapsed at Wave 14-T commit; ~82,500 spectra fetched, throughput full-window ~195 spectra/min sustained. Recompile_p4 (19 pp / 25,794,489 bytes / 0 errors / 0 undef refs / Shamir-refs-now-with-years per R42 m5) ran cleanly in /workspace/recompile_p4 in same session, $0 marginal H200 spend. 100K sub-sample short-circuit imminent. Quantitative systematics-marginalization Fisher recompute for P3 (~2h H200) queued to dispatch once fetch completes.)",
    },
  ],
};
