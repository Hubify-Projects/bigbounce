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
  lastUpdatedISO: "2026-05-01T23:10:00Z",
  lastUpdatedDisplay: "2026-05-01 16:10 PT",
  headline:
    "Wave 14-F LANDED — P4 v1.0.11 (Gemini M-1 Catalog~B GZ1-deprecation caveat + Gemini m-1 statistical-only sensitivity caveat); 5 cross-model findings closed inside the Wave 14-B 1M SPARCL fetch window",
  summary:
    "Wave 14-F closes two more cheap-fast Gemini-3.1-Pro P4 findings. Gemini M-1 (Catalog~B Platt-circularity → GZ1-deprecation): §III.F Catalog~B bullet expanded with explicit \"not recommended for cosmological parity tests\" caveat (Platt is fit against CE-ResNet consensus rather than independent ground truth, so any residual CE-ResNet bias propagates into a Catalog~B parity statistic; canonical recalibration would require the GZ1 cross-match restricted to the 117,205 GZ1 spirals where the model also predicts spiral; Catalog~C equivariant production remains the canonical tier for parity analyses). Gemini m-1 (statistical-only sensitivity): new \\paragraph{Statistical-only sensitivity, not systematic-inclusive.} in §sec:sensitivity clarifies that the 0.2% statistical Poisson dipole floor sits below the catalog's 0.26% raw-classifier systematic monopole — therefore 0.2% is a statistical upper bound under the zero-systematic-dipole-projection assumption, not a systematic-inclusive sensitivity (PSF-ellipticity / scan-angle cross-correlation against the equivariant CW-fraction map queued as downstream extension). P4 .tex bumped v1.0.10 → v1.0.11, date 15:45 PDT → 16:10 PDT, recompiled clean on Pod 3 (pdflatex × 2 in /workspace/recompile_p4/, 25.79 MB / 18 pp / 0 undef refs, page count unchanged because both edits flow within existing column blocks), mirrored to pipelines/p2_chirality/ + public/papers/. Five cross-model cheap-fast findings (P3-CM-B4 14-A, P4-OA-B1+B2 14-C, P4-OA-B6 14-D, P4-OA-B4 14-E, Gemini P4 M-1+m-1 14-F) now closed inside the single multi-hour Wave 14-B 1M SPARCL fetch window — exactly the cheap-fast text-edit while compute runs discipline feedback_more_not_less.md + feedback_default_hardest_path.md codify. Pod 3 H200 SPARCL 1M fetch alive on PID 25860, ~1h24m elapsed at this commit, 34 shards / ~120 MB written, throughput improved to ~275 spectra/min from earlier ~150 spectra/min — at the new rate the 1M ETA is ~60 hours; sub-sample short-circuit (e.g., 100K, ~6 hours at the new rate) remains the likely operational call.",
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
      version: "v1.0.11",
      readiness: 95,
    },
  ],
  blockerTally: {
    closed: 14, // 14 cross-model BLOCKERs closed across Waves 11-14 (Gemini M-1 + m-1 closed in 14-F are MAJOR + minor, not BLOCKER)
    openBlockers: 4, // remaining cross-model BLOCKERs (P3-OA-M1 1M Jaccard pending fetch)
    openMajors: 24, // -1: Gemini P4 M-1 (Catalog~B GZ1-deprecation caveat) closed in 14-F
    openMinors: 24, // -1: Gemini P4 m-1 (statistical-only sensitivity caveat) closed in 14-F
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~48-72 h at current Wave-cadence (3-5 cross-model findings / day on cheap-fast queue + 1 compute-heavy / day on Pod 3 H200; Wave 14-B 1M Jaccard fetch now ~60 h on the improved ~275 spectra/min throughput, sub-sample short-circuit (e.g., 100K, ~6 h) remains the likely operational call)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-B 1M SPARCL fetch in flight (PID 25860, ~1h24m elapsed, 34 shards / ~120 MB written, throughput improved to ~275 spectra/min from earlier ~150 spectra/min — at the new rate the 1M ETA is ~60 h, sub-sample short-circuit (e.g., 100K, ~6 h) remains the likely operational call)",
    },
  ],
};
