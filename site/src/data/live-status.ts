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
  lastUpdatedISO: "2026-05-01T22:45:00Z",
  lastUpdatedDisplay: "2026-05-01 15:45 PT",
  headline:
    "Wave 14-E LANDED — P4 v1.0.10 (Table V N_spiral footnote anchor); 4 cheap-fast GPT-5 BLOCKERs closed inside the Wave 14-B 1M SPARCL fetch window",
  summary:
    "Wave 14-E closes P4-OA-B4: Table V (tab:sky_balance) bold \"All sky\" row N_spiral=3,321,795 cell anchored with $^{\\mathrm{a}}$ superscript pointing within the same float to the caption disambiguation between Table V's snapshot total (3,321,795) and the paper-canonical equivariant N_spiral=3,201,160 (Wave 11-C verdict, used everywhere else in the paper for dipole + NaMaster shot-noise normalization). Standard revtex4-2 ruledtabular-safe table-caption anchor pattern. P4 .tex bumped v1.0.9 → v1.0.10, date 14:30 PDT → 15:45 PDT, recompiled clean on Pod 3 (pdflatex × 2 in /workspace/recompile_p4/, 25.79 MB / 18 pp / 0 undef refs, page count unchanged because cell+caption mod is in-place within existing table float), mirrored to pipelines/p2_chirality/ + public/papers/. Four GPT-5 cheap-fast P4 BLOCKERs (P3-CM-B4 14-A, P4-OA-B1+B2 14-C, P4-OA-B6 14-D, P4-OA-B4 14-E) now closed inside the single multi-hour Wave 14-B 1M SPARCL fetch window — exactly the cheap-fast text-edit while compute runs discipline feedback_more_not_less.md + feedback_default_hardest_path.md codify. Pod 3 H200 SPARCL 1M fetch alive on PID 25860, ~1h15m elapsed at this commit, 29 shards / ~9K of 1M spectra written, ~150 spectra/min steady — slower than the original 2,374/min projection; sub-sample short-circuit (e.g., 100K) likely needed if throughput stays at this level (1M ETA at observed rate is ~111 hours).",
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
      version: "v1.0.10",
      readiness: 94,
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
      note: "Wave 14-B 1M SPARCL fetch in flight (PID 25860, ~1h15m elapsed, 29 shards / ~9K of 1M spectra written, ~150 spectra/min steady — sub-sample short-circuit (e.g., 100K) likely needed; 1M ETA at observed rate is ~111h)",
    },
  ],
};
