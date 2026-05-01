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
  lastUpdatedISO: "2026-05-02T09:25:00Z",
  lastUpdatedDisplay: "2026-05-02 02:25 PT",
  headline:
    "Wave 14-W LANDED · P1 v2.3.12 · 29 cross-model findings closed · ETA all-4 → 100%: ~22-44 h",
  summary:
    "P1 v2.3.12: R42 P1-OA-M9 MAJOR closed — Barrier 4 §X k²/M_Pl² ∼ 10⁻¹²² scale specification now states k ∼ H_0 (the present Hubble rate, IR scale relevant for late-time observables) explicitly and confirms consistent application across all four uses of the H_0²/M_Pl² ∼ 10⁻¹²² hierarchy in the paper. 33 pp / 1.23 MB recompile clean on Pod 3 — 0 undef refs. Wave 14-V Wilson-Ewing 2013 LQC bib entry preserved. SPARCL 1M fetch ~7.7 h elapsed (~96K spectra fetched), 100K short-circuit ~8 min away. Cron */20 armed.",
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
    closed: 29, // +1 from Wave 14-W: P1-OA-M9 MAJOR (Barrier 4 §X k²/M_Pl² scale-specification at L613 now states k ~ H_0 explicitly + cross-references all four 10⁻¹²² hierarchy uses)
    openBlockers: 0, // unchanged from Wave 14-V
    openMajors: 14, // -1 from Wave 14-V: P1-OA-M9 closed
    openMinors: 13, // unchanged from Wave 14-V
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~22-44 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-B 1M Jaccard fetch ~96K spectra now disk-resident at ~500 spectra/min sustained recent rate, 100K short-circuit ~8 min away on cost/cadence grounds; quantitative systematics-marginalization Fisher recompute for P3 queued ~2h H200 once Pod 3 frees up)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-B 1M SPARCL fetch in flight (PID 25860, ~7h45m elapsed; ~96K spectra fetched, 192 shards / 222 MB on disk, throughput recent ~500 spectra/min, 100K short-circuit imminent within ~8 min. Recompile_p1 ran cleanly in /workspace/recompile_p1 in same session for the second consecutive wave ($0 marginal H200 spend) — 33 pp / 1,232,611 bytes / 0 errors / Wave 14-W k~H_0 scale specification at Barrier 4 now anchors all four 10⁻¹²² hierarchy uses. Quantitative systematics-marginalization Fisher recompute for P3 (~2h H200) queued for dispatch once fetch completes.)",
    },
  ],
};
