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
  lastUpdatedISO: "2026-05-02T06:30:00Z",
  lastUpdatedDisplay: "2026-05-01 23:30 PT",
  headline:
    "Wave 14-S LANDED · P1 v2.3.9 · 25 cross-model findings closed · ETA all-4 → 100%: ~28-52 h",
  summary:
    "P1 v2.3.9: Gemini m-2 defensive Scope-note deleted in §I.C. 33 pp / 1.23 MB recompile clean on Pod 3. SPARCL 1M fetch ~6h in (PID 25860, ~195 spectra/min); 100K sub-sample short-circuit (~5 h) recommended. Cron */20 armed; banner refreshes every 15 min.",
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
      version: "v1.0.15",
      readiness: 97,
    },
  ],
  blockerTally: {
    closed: 25, // +1 from Wave 14-S: Gemini P1 m-2 defensive Scope-note delete in §I.C (cheap-fast precise-language path)
    openBlockers: 1, // unchanged from Wave 14-R
    openMajors: 16, // unchanged from Wave 14-S (Gemini P1 m-2 was a MINOR, not a MAJOR)
    openMinors: 14, // -1 from Wave 14-S: Gemini P1 m-2 closed (was a MINOR)
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~28-52 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-B 1M Jaccard fetch ~74 h on sustained ~195 spectra/min full-window throughput, 100K sub-sample short-circuit (~5 h from this commit) remains strongly recommended on cost/cadence grounds; quantitative systematics-marginalization Fisher recompute for P3 queued ~2h H200 once Pod 3 frees up)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-B 1M SPARCL fetch in flight (PID 25860, ~6h elapsed at Wave 14-S commit; throughput full-window ~195 spectra/min sustained, consistent with Wave 14-R reading. Recompile_p1 (33 pp / 1,231,939 bytes / 0 errors / 0 undef refs / 0 'Wave 14-S' occurrences (expected — delete-only) / 1 pre-existing WilsonEwing2012 undef cite) ran cleanly in same session, $0 marginal H200 spend. 100K sub-sample short-circuit (~5 h ETA from this commit) remains strongly recommended on cost/cadence grounds. Quantitative systematics-marginalization Fisher recompute for P3 (~2h H200) queued to dispatch once fetch completes.)",
    },
  ],
};
