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
  lastUpdatedISO: "2026-05-02T03:30:00Z",
  lastUpdatedDisplay: "2026-05-01 20:30 PT",
  headline:
    "Wave 14-O LANDED — P3 v3.1.10 → v3.1.11 (Gemini-3.1-Pro P3 MAJOR M-2 α-bias-enhancement abstract flag: headline 6.1% σ(f_NL) improvement was contingent on uncalibrated fiducial α=0.15 with no abstract-level uncertainty framing; abstract now states σ(f_NL) improvement as a function of α with explicit [2%, 20%] range for α ∈ [0.05, 0.50] and bold 'absence of empirical calibration of α is the primary limitation of the cosmological forecast' sentence; §V opener prepended with bold Wave 14-O peer-review reframe block + explicit instruction that the α-dependent table is the primary forecast deliverable, not a single-point quote at α=0.15); 21 cross-model findings closed across 14 cheap-fast sub-waves while the Wave 14-B 1M SPARCL fetch continues; Pod 3 throughput full-window ~195 spectra/min sustained at ~98 shards / ~132 MB / ~4h11m elapsed",
  summary:
    "Wave 14-O closes one Gemini-3.1-Pro P3 MAJOR (M-2) on the cheap-fast precise-language axis. Gemini flagged that the abstract's headline '6.1% improvement in σ(f_NL)' was a single-point quote at fiducial α=0.15 without any abstract-level acknowledgment that (a) α is uncalibrated empirically against the anomaly subsample, (b) the σ(f_NL) improvement scales approximately linearly with α across the plausible range, and (c) the absence of empirical α calibration is the primary limitation of the cosmological forecast. The on-disk numerics already documented this α-dependence in Appendix sensitivity tables (~2% improvement at α=0.05, ~20% at α=0.50), and the in-paper Pipeline-1 1.58× clustering bias result (Landy-Szalay on N=1,122 Gold+Silver QSO candidates from the 5,384-candidate population, broadly consistent with α~0.15 but too small a sample to be definitive) was already cited inline. What was missing was the abstract-level reframe that prevents downstream forecasts and headline quotes from cementing the 6.1%/α=0.15 figure as the cosmological deliverable. Wave 14-O closes this cheap-fast: (1) abstract close (after 'Cosmological applications ... primary-source methodology.') appended bold two-sentence flag stating σ(f_NL) improvement as a function of α (6.1% at α=0.15 fiducial, ~2% at α=0.05, ~20% at α=0.50, citing Appendix sensitivity table), the in-paper 1.58× Pipeline-1 bias result (N=1,122) as broadly consistent but too small to be definitive, and bold sentence 'The absence of empirical calibration of α is the primary limitation of the cosmological forecast'; (2) §V opener prepended with bold 'R42 Wave 14-O peer-review reframe (cross-model Gemini 3.1-Pro P3 M-2)' italic block stating the headline σ(f_NL) improvement quoted below is contingent on fiducial α=0.15 + range [2%, 20%] for α ∈ [0.05, 0.50] + explicit instruction that the α-dependent table is the primary forecast deliverable, not the single-point α=0.15 quote. P3 .tex bumped v3.1.10 → v3.1.11, date May 1 19:45 PDT → 20:30 PDT, recompiled clean on Pod 3 H200 (pdflatex × 2 in /workspace/recompile_p3/, 28,301,481 bytes / 39 pp / 0 errors / 0 undef refs / 0 undef cites / 1 'Wave 14-O' occurrence), mirrored to public/papers/{paper3_draft.pdf, paper3_anomaly_catalog.pdf, anomaly-catalog-paper.pdf}. Twenty-one cross-model findings (P3-CM-B4 14-A, P4-OA-B1+B2 14-C, P4-OA-B6 14-D, P4-OA-B4 14-E, Gemini P4 M-1+m-1 14-F, OpenAI P4 M-2+M-3 + OpenAI M-8 / Gemini m-2 documented 14-G, OpenAI minor-1+minor-3+minor-5+M-6 14-H, OpenAI B4 + B3+minor-2+minor-4 documented 14-I, OpenAI M-4 + minor-3-leftover + minor-1-leftover 14-J, Gemini P2 B-3 14-K, Gemini P3 m-1 14-L, OpenAI P1 B-4 14-M, Gemini P3 m-2 14-N, Gemini P3 M-2 14-O) now closed across fourteen cheap-fast sub-waves inside the single multi-hour Wave 14-B 1M SPARCL fetch window. Pod 3 H200 SPARCL 1M fetch alive on PID 25860, ~4h11m elapsed at this commit, ~98 shards / ~132 MB written, throughput full-window ~195 spectra/min sustained — consistent with Wave 14-N's reading. 100K sub-sample short-circuit (~5 h ETA from this commit) remains strongly recommended on cost/cadence grounds. $0 marginal H200 spend — recompile_p3 shares the same Pod 3 session running the fetch.",
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
      version: "v3.1.11",
      readiness: 93,
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
    closed: 21, // +1 from Wave 14-O: Gemini P3 M-2 α-bias-enhancement abstract flag (state σ(f_NL) as function of α + flag empirical-calibration absence as primary limitation in abstract; §V opener reframed)
    openBlockers: 1, // unchanged from Wave 14-N
    openMajors: 18, // -1 from Wave 14-O: Gemini P3 M-2 closed
    openMinors: 16, // unchanged from Wave 14-N
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~32-56 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-B 1M Jaccard fetch ~85 h on sustained ~195 spectra/min full-window throughput, 100K sub-sample short-circuit (~5 h from this commit) remains strongly recommended on cost/cadence grounds)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-B 1M SPARCL fetch in flight (PID 25860, ~4h11m elapsed at Wave 14-O commit, ~98 shards / ~132 MB written; throughput full-window ~195 spectra/min sustained, consistent with Wave 14-N reading. Recompile_p3 (39 pp / 28.30 MB / 0 errors / 0 undef refs / 0 undef cites / 1 'Wave 14-O' occurrence) ran cleanly in same session, $0 marginal H200 spend. 100K sub-sample short-circuit (~5 h ETA from this commit) remains strongly recommended on cost/cadence grounds.)",
    },
  ],
};
