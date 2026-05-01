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
  lastUpdatedISO: "2026-05-02T06:00:00Z",
  lastUpdatedDisplay: "2026-05-01 23:00 PT",
  headline:
    "Wave 14-R LANDED — P3 v3.1.11 → v3.1.12 (Gemini-3.1-Pro P3 MAJOR M-1 quantitative systematics marginalization OR explicit zero-systematic caveat in f_NL Fisher per Gemini's literal 'OR' clause: cheap-fast caveat path chosen — abstract appended bold sentence after the existing Wave 14-O α-calibration limitation flag explicitly stating the forecast assumes zero observational systematics (no fiber-assignment correction, no photometric-redshift uncertainty, no PSF-induced selection effects, no foreground contamination, no spectroscopic-completeness variation across the footprint); §V.A opener at L547 prepended a bold R42 Wave 14-R peer-review reframe block after the existing Wave 14-O reframe block, decomposing each unmodelled systematic, citing Heinrich+2023 as the realistic ~1-3% σ(f_NL) systematic floor in DESI-class surveys, and explicitly framing the quoted 6.1%/α=0.15 central improvement as a zero-systematic upper bound on the achievable improvement, not a marginalized realistic forecast; compute-medium quantitative recompute formally queued as Wave 14-S follow-up); 24 cross-model findings closed across 17 cheap-fast sub-waves while the Wave 14-B 1M SPARCL fetch continues; Pod 3 throughput full-window ~195 spectra/min sustained at ~5h44m elapsed",
  summary:
    "Wave 14-R closes one Gemini-3.1-Pro P3 MAJOR M-1 on the cheap-fast caveat axis. Gemini's literal ask was: 'Quantitative systematics marginalization in f_NL Fisher OR explicit zero-systematic caveat'. The OR clause permits two closure paths: (Path A) compute-medium quantitative recompute with nuisance parameters per systematic marginalized at the Fisher level following Heinrich et al. 2023 recipe (~2 h on H200 once Pod 3 frees up), or (Path B) cheap-fast explicit zero-systematic caveat in abstract + §V (text-only, $0 marginal H200 spend). Wave 14-R chose Path B because Pod 3 is currently committed to the active Wave 14-B 1M SPARCL fetch; the quantitative recompute is formally queued as Wave 14-S follow-up to dispatch on Pod 3 once the fetch finishes (~74 h projected, or sooner via 100K sub-sample short-circuit). Wave 14-R closes this cheap-fast: (1) abstract appended a bold sentence after the existing Wave 14-O α-calibration limitation flag stating the forecast assumes zero observational systematics (no fiber-assignment correction, no photometric-redshift uncertainty, no PSF-induced selection effects, no foreground contamination, no spectroscopic-completeness variation across the footprint), and queueing a quantitative systematics-marginalization Fisher recompute as the second-most-important follow-up after empirical α calibration; (2) §V.A opener at L547 prepended a bold 'R42 Wave 14-R peer-review reframe (cross-model Gemini~3.1-Pro P3 M-1)' italic block placed after the existing Wave 14-O reframe block, decomposing each unmodelled systematic, citing Heinrich+2023 as the realistic ~1-3% σ(f_NL) systematic floor in DESI-class surveys (subdominant to but not negligible compared to the α-axis sensitivity range), and explicitly framing the quoted 6.1%/α=0.15 central improvement as a zero-systematic upper bound on the achievable improvement, not a marginalized realistic forecast — until the Wave 14-S quantitative recompute is performed; (3) no equations or numbers were modified — text-only caveat insertion. P3 .tex bumped v3.1.11 → v3.1.12, date May 1 20:30 PDT → 23:00 PDT, recompiled clean on Pod 3 H200 (pdflatex × 2 in /workspace/recompile_p3/, 28,305,540 bytes / 39 pp / 0 errors / 0 undef refs / 0 undef cites / 1 'Wave 14-R' occurrence), mirrored to public/papers/{paper3_draft.pdf, paper3_anomaly_catalog.pdf, anomaly-catalog-paper.pdf}. Twenty-four cross-model findings (P3-CM-B4 14-A, P4-OA-B1+B2 14-C, P4-OA-B6 14-D, P4-OA-B4 14-E, Gemini P4 M-1+m-1 14-F, OpenAI P4 M-2+M-3 + OpenAI M-8 / Gemini m-2 documented 14-G, OpenAI minor-1+minor-3+minor-5+M-6 14-H, OpenAI B4 + B3+minor-2+minor-4 documented 14-I, OpenAI M-4 + minor-3-leftover + minor-1-leftover 14-J, Gemini P2 B-3 14-K, Gemini P3 m-1 14-L, OpenAI P1 B-4 14-M, Gemini P3 m-2 14-N, Gemini P3 M-2 14-O, Gemini P1 M-2 14-P, Gemini P1 m-1 14-Q, Gemini P3 M-1 14-R) now closed across seventeen cheap-fast sub-waves inside the single multi-hour Wave 14-B 1M SPARCL fetch window. Pod 3 H200 SPARCL 1M fetch alive on PID 25860, ~5h44m elapsed at this commit, throughput full-window ~195 spectra/min sustained — consistent with Wave 14-Q's reading. 100K sub-sample short-circuit (~5 h ETA from this commit) remains strongly recommended on cost/cadence grounds. $0 marginal H200 spend — recompile_p3 shares the same Pod 3 session running the fetch.",
  papers: [
    {
      slug: "spin-torsion",
      number: 1,
      shortTitle: "Spin-Torsion Cosmology",
      version: "v2.3.8",
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
    closed: 24, // +1 from Wave 14-R: Gemini P3 M-1 quantitative systematics marginalization OR explicit zero-systematic caveat in f_NL Fisher (cheap-fast caveat path; quantitative recompute queued as Wave 14-S follow-up)
    openBlockers: 1, // unchanged from Wave 14-Q
    openMajors: 16, // -1 from Wave 14-R: Gemini P3 M-1 closed (was a MAJOR)
    openMinors: 15, // unchanged from Wave 14-R (Gemini P3 M-1 was a MAJOR, not a MINOR)
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~28-52 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-B 1M Jaccard fetch ~74 h on sustained ~195 spectra/min full-window throughput, 100K sub-sample short-circuit (~5 h from this commit) remains strongly recommended on cost/cadence grounds; Wave 14-S quantitative systematics-marginalization Fisher recompute queued ~2h H200 once Pod 3 frees up)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-B 1M SPARCL fetch in flight (PID 25860, ~5h44m elapsed at Wave 14-R commit; throughput full-window ~195 spectra/min sustained, consistent with Wave 14-Q reading. Recompile_p3 (39 pp / 28,305,540 bytes / 0 errors / 0 undef refs / 0 undef cites / 1 'Wave 14-R' occurrence) ran cleanly in same session, $0 marginal H200 spend. 100K sub-sample short-circuit (~5 h ETA from this commit) remains strongly recommended on cost/cadence grounds. Wave 14-S quantitative systematics-marginalization Fisher recompute (~2h H200) queued to dispatch once fetch completes.)",
    },
  ],
};
