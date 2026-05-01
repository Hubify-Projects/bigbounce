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
  lastUpdatedISO: "2026-05-01T21:30:00Z",
  lastUpdatedDisplay: "2026-05-01 14:30 PT",
  headline:
    "R42 Wave 14-D LANDED — Paper 4 v1.0.9 (P4-OA-B6 Platt calibration close)",
  summary:
    "Closed GPT-5 OpenAI BLOCKER #6 in §III.F: \"removes\" → \"reduces\" + explicit residual offset (raw +0.79% / 28.8σ → calibrated +0.4% / 14.6σ → equivariant −0.26% / 9.5σ from Table III) + explicit Platt mapping with A=1/4.65, B=−1.58, L-BFGS on held-out 20% validation. Three GPT-5 BLOCKERs closed inside the single multi-hour Wave 14-B fetch window on Pod 3 H200. PDF recompiled clean (25.79 MB / 18 pp / 0 undef refs).",
  papers: [
    {
      slug: "spin-torsion",
      number: 1,
      shortTitle: "Spin-Torsion Cosmology",
      version: "v2.3.5",
      readiness: 92,
    },
    {
      slug: "fnl-forecast",
      number: 2,
      shortTitle: "f_NL SPHEREx Forecast",
      version: "v1.7.6",
      readiness: 90,
    },
    {
      slug: "anomaly-catalog",
      number: 3,
      shortTitle: "Multi-Survey Anomaly Catalog",
      version: "v3.1.8",
      readiness: 91,
    },
    {
      slug: "chirality-catalog",
      number: 4,
      shortTitle: "Galaxy Chirality Catalog",
      version: "v1.0.9",
      readiness: 93,
    },
  ],
  blockerTally: {
    closed: 14, // 14 cross-model BLOCKERs closed across Waves 11-14
    openBlockers: 4, // remaining cross-model BLOCKERs (P3-OA-M1 1M Jaccard pending fetch)
    openMajors: 25,
    openMinors: 25,
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b)",
  etaToCompletion:
    "ETA all-4 → 100%: ~36-48 h at current Wave-cadence (4 BLOCKERs / day on cheap-fast queue + 1 compute-heavy / day on Pod 3 H200)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-B 1M SPARCL fetch in flight (PID 25860, ~25 min elapsed, ~7 h wall)",
    },
  ],
};
