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
  lastUpdatedISO: "2026-05-02T02:45:00Z",
  lastUpdatedDisplay: "2026-05-01 19:45 PT",
  headline:
    "Wave 14-N LANDED — P3 v3.1.9 → v3.1.10 (Gemini-3.1-Pro P3 m-2 S>5 anomaly-threshold scope clarification at §II.A L116: rewrote contradictory paragraph that simultaneously claimed a fixed canonical-S cut S>5.0 AND 'all surveys use a per-survey percentile-based anomaly threshold' into a precise per-survey policy — DESI/SDSS use absolute MSE-anchored cuts MSE≈0.143 for DESI, LAMOST/Gaia use 99th-percentile, eROSITA uses isolation-forest score); 20 cross-model findings closed across 13 cheap-fast sub-waves while the Wave 14-B 1M SPARCL fetch continues; Pod 3 throughput full-window ~199 spectra/min sustained at ~89 shards / ~123 MB / ~3h47m elapsed",
  summary:
    "Wave 14-N closes one Gemini-3.1-Pro P3 MINOR (m-2) on the cheap-fast precise-language axis. Gemini flagged that §II.A's anomaly-threshold paragraph at L116 was internally inconsistent: the paragraph opened by stating 'the threshold is a fixed canonical-S cut (S>5.0 for DESI and SDSS) ... or 99th percentile' for LAMOST/Gaia, then closed with 'all surveys use a per-survey percentile-based anomaly threshold'. The two sentences cannot both be true simultaneously and the contradiction was visible to any careful reader. The on-disk reality (verified from the Paper 3 catalog code) is that DESI/SDSS use absolute MSE-anchored cuts (MSE≈0.143 for DESI on the rescaled scale, with the analogous fixed MSE for SDSS, anchored by each survey's (μ_val, σ_val) on its own 20% held-out validation split), LAMOST/Gaia use 99th-percentile cuts, and eROSITA uses an isolation-forest score with its own threshold — three different policies, chosen by survey rather than uniformly applied. The realized anomaly rates (0.87% on DESI, 3.4% on SDSS, etc.) are emergent properties of the absolute cut applied to the full survey, not designed-in percentiles. Wave 14-N closes this cheap-fast: rewrote the entire L116 paragraph to lead with 'The anomaly catalog threshold is set per survey, with the policy chosen by survey rather than uniformly applied.' followed by an explicit per-survey breakdown that distinguishes absolute (DESI/SDSS, MSE-anchored) from percentile-based (LAMOST/Gaia 99th) from isolation-forest (eROSITA). Added bold 'R42 Wave 14-N peer-review reframe (cross-model Gemini 3.1-Pro P3 m-2)' trailer for traceability. P3 .tex bumped v3.1.9 → v3.1.10, date May 1 19:00 PDT → 19:45 PDT, recompiled clean on Pod 3 H200 (pdflatex × 2 in /workspace/recompile_p3/, 28,299,586 bytes / 39 pp / 0 errors / 0 undef refs / 0 undef cites / 1 'Wave 14-N' occurrence), mirrored to public/papers/{paper3_draft.pdf, paper3_anomaly_catalog.pdf, anomaly-catalog-paper.pdf}. Twenty cross-model findings (P3-CM-B4 14-A, P4-OA-B1+B2 14-C, P4-OA-B6 14-D, P4-OA-B4 14-E, Gemini P4 M-1+m-1 14-F, OpenAI P4 M-2+M-3 + OpenAI M-8 / Gemini m-2 documented 14-G, OpenAI minor-1+minor-3+minor-5+M-6 14-H, OpenAI B4 + B3+minor-2+minor-4 documented 14-I, OpenAI M-4 + minor-3-leftover + minor-1-leftover 14-J, Gemini P2 B-3 14-K, Gemini P3 m-1 14-L, OpenAI P1 B-4 14-M, Gemini P3 m-2 14-N) now closed across thirteen cheap-fast sub-waves inside the single multi-hour Wave 14-B 1M SPARCL fetch window. Pod 3 H200 SPARCL 1M fetch alive on PID 25860, ~3h47m elapsed at this commit, ~89 shards / ~123 MB written, throughput full-window ~199 spectra/min sustained — consistent with Wave 14-M's reading. 100K sub-sample short-circuit (~5 h ETA from this commit) remains strongly recommended on cost/cadence grounds. $0 marginal H200 spend — recompile_p3 shares the same Pod 3 session running the fetch.",
  papers: [
    {
      slug: "spin-torsion",
      number: 1,
      shortTitle: "Spin-Torsion Cosmology",
      version: "v2.3.6",
      readiness: 93,
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
      version: "v3.1.10",
      readiness: 92,
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
    closed: 20, // +1 from Wave 14-N: Gemini P3 m-2 S>5 anomaly-threshold scope clarification at §II.A L116 (rewrote contradictory percentile/absolute framing into precise per-survey policy)
    openBlockers: 1, // unchanged from Wave 14-M
    openMajors: 19, // unchanged
    openMinors: 16, // -1 from Wave 14-N: Gemini P3 m-2 closed
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~34-58 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-B 1M Jaccard fetch ~85 h on sustained ~199 spectra/min full-window throughput, 100K sub-sample short-circuit (~5 h from this commit) remains strongly recommended on cost/cadence grounds)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-B 1M SPARCL fetch in flight (PID 25860, ~3h47m elapsed at Wave 14-N commit, ~89 shards / ~123 MB written; throughput full-window ~199 spectra/min sustained, consistent with Wave 14-M reading. Recompile_p3 (39 pp / 28.30 MB / 0 errors / 0 undef refs / 0 undef cites / 1 'Wave 14-N' occurrence) ran cleanly in same session, $0 marginal H200 spend. 100K sub-sample short-circuit (~5 h ETA from this commit) remains strongly recommended on cost/cadence grounds.)",
    },
  ],
};
