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
  lastUpdatedISO: "2026-05-01T22:25:00Z",
  lastUpdatedDisplay: "2026-05-01 15:25 PT",
  headline:
    "Live site is now Next.js (verified) — LiveStatus banner baked at top of every page",
  summary:
    "First flip-deploy errored on a missing prebuild script; second on Vercel installing root deps instead of site/ deps (geist/font/sans unresolved). Both fixed in 06d189d3 + 8cef036d. Live site now serving Next.js (deploy bigbounce-j1z736wk2 ● Ready, build 54s, title \"BigBounce — Spin-Torsion Cosmology\"). LiveStatus banner verified rendered at top of every page (homepage + /paper + /papers/paper-N + /figures + /glossary + /articles + /activity + ...). Wave 14-D LANDED earlier — P4 v1.0.9 + three GPT-5 BLOCKERs closed inside the single Wave 14-B fetch window. Pod 3 H200 SPARCL 1M fetch alive on PID 25860, ~60 min elapsed, 18 shards / 9K of 1M spectra written (~150 spectra/min observed — slower than the original 2,374/min projection; sub-sample short-circuit decision likely needed if throughput stays at this level).",
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
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~48-72 h at current Wave-cadence (3-4 BLOCKERs / day on cheap-fast queue + 1 compute-heavy / day on Pod 3 H200; Wave 14-B 1M Jaccard fetch now ~80 h on the observed ~200 spectra/min throughput, may need a sub-sample short-circuit)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-B 1M SPARCL fetch in flight (PID 25860, ~60 min elapsed, 18 shards / 9K of 1M spectra written, ~150 spectra/min — sub-sample short-circuit on the table)",
    },
  ],
};
