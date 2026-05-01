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
  lastUpdatedISO: "2026-05-02T07:50:00Z",
  lastUpdatedDisplay: "2026-05-02 00:50 PT",
  headline:
    "Wave 14-V LANDED · P1 v2.3.11 · 28 cross-model findings closed · ETA all-4 → 100%: ~24-46 h",
  summary:
    "P1 v2.3.11: R42 P1-OA-M10 MAJOR closed — long-standing pre-existing Wilson-Ewing 2013 (LQC matter bounce) undef cite resolved by adding WilsonEwing2012 entry to references.bib (JCAP 03 (2013) 026, arXiv:1211.6269). 33 pp / 1.23 MB recompile clean on Pod 3 — bbl now shows resolved Wilson-Ewing entry, 0 undef refs in pass 3 log. Wave 14-U synthetic-PTA Bayes deletion + Agazie 2023 cite preserved. SPARCL 1M fetch ~8h elapsed (~91.5K spectra fetched), 100K short-circuit ~44 min away. Cron */20 armed.",
  papers: [
    {
      slug: "spin-torsion",
      number: 1,
      shortTitle: "Spin-Torsion Cosmology",
      version: "v2.3.11",
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
    closed: 28, // +1 from Wave 14-V: P1-OA-M10 MAJOR (Wilson-Ewing 2013 LQC matter bounce undef cite resolved via references.bib entry add)
    openBlockers: 0, // unchanged from Wave 14-U
    openMajors: 15, // -1 from Wave 14-U: P1-OA-M10 closed
    openMinors: 13, // unchanged from Wave 14-U
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~24-46 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-B 1M Jaccard fetch ~91.5K spectra now disk-resident at ~195 spectra/min sustained, 100K short-circuit ~44 min away on cost/cadence grounds; quantitative systematics-marginalization Fisher recompute for P3 queued ~2h H200 once Pod 3 frees up)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-B 1M SPARCL fetch in flight (PID 25860, ~7h35m elapsed at Wave 14-U commit; ~89K spectra fetched, ~178 shards / 207 MB on disk, throughput full-window ~195 spectra/min sustained, 100K short-circuit imminent within ~5-10 min. Recompile_p1 ran cleanly in /workspace/recompile_p1 in same session ($0 marginal H200 spend) — 33 pp / 1,230,946 bytes / 0 errors / new Agazie:2023ng15 cite resolved / synthetic-PTA Bayes B≈302 block deleted from §XV.C per R1 P1-CM-B2. Quantitative systematics-marginalization Fisher recompute for P3 (~2h H200) queued for dispatch once fetch completes.)",
    },
  ],
};
