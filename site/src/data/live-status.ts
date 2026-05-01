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
  lastUpdatedISO: "2026-05-02T07:25:00Z",
  lastUpdatedDisplay: "2026-05-02 00:25 PT",
  headline:
    "Wave 14-U LANDED · P1 v2.3.10 · 27 cross-model findings closed · ETA all-4 → 100%: ~26-48 h",
  summary:
    "P1 v2.3.10: R42 R1 P1-CM-B2 BLOCKER closed — synthetic-PTA Bayes factor B≈302 deleted from §XV.C, replaced with direct Agazie 2023 NG15 free-spectrum cite + Lentati methodology GPU MCMC posterior-level B=34.0 (only real data now). 33 pp / 1.23 MB recompile clean on Pod 3 (Agazie:2023ng15 bib entry added; only pre-existing WilsonEwing2012 undef remains, unrelated). SPARCL 1M fetch ~7h35m in (~89K spectra fetched), 100K short-circuit imminent. Cron */20 armed.",
  papers: [
    {
      slug: "spin-torsion",
      number: 1,
      shortTitle: "Spin-Torsion Cosmology",
      version: "v2.3.10",
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
    closed: 27, // +1 from Wave 14-U: P1-CM-B2 BLOCKER (synthetic-PTA Bayes deleted, Agazie 2023 cited directly)
    openBlockers: 0, // -1 from Wave 14-T: P1-CM-B2 was the last open BLOCKER. Compute-heavy items remain in MAJORS/quantitative items, but BLOCKER queue clear after Wave 14-U.
    openMajors: 16, // unchanged from Wave 14-T
    openMinors: 13, // unchanged from Wave 14-T
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~28-52 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-B 1M Jaccard fetch ~74 h on sustained ~195 spectra/min full-window throughput, 100K sub-sample short-circuit (~5 h from this commit) remains strongly recommended on cost/cadence grounds; quantitative systematics-marginalization Fisher recompute for P3 queued ~2h H200 once Pod 3 frees up)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-B 1M SPARCL fetch in flight (PID 25860, ~7h35m elapsed at Wave 14-U commit; ~89K spectra fetched, ~178 shards / 207 MB on disk, throughput full-window ~195 spectra/min sustained, 100K short-circuit imminent within ~5-10 min. Recompile_p1 ran cleanly in /workspace/recompile_p1 in same session ($0 marginal H200 spend) — 33 pp / 1,230,946 bytes / 0 errors / new Agazie:2023ng15 cite resolved / synthetic-PTA Bayes B≈302 block deleted from §XV.C per R1 P1-CM-B2. Quantitative systematics-marginalization Fisher recompute for P3 (~2h H200) queued for dispatch once fetch completes.)",
    },
  ],
};
