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
  lastUpdatedISO: "2026-05-02T01:30:00Z",
  lastUpdatedDisplay: "2026-05-01 18:30 PT",
  headline:
    "Wave 14-K LANDED — P2 v1.7.6 → v1.7.7 (Gemini P2 BLOCKER B-3 Appendix-A framing fix: factor-of-two between Cai and Li-Brandenberger now explicitly decomposed as a normalization-convention difference plus an in-in commutator operator-algebra identity, not two interchangeable conventions); 17 cross-model findings closed across 10 cheap-fast sub-waves while the Wave 14-B 1M SPARCL fetch continues",
  summary:
    "Wave 14-K closes one Gemini-3.1-Pro P2 BLOCKER (B-3) by sharpening the Appendix-A framing of the factor-of-two between Cai et al.~2009 (f_NL = -35/8) and Li & Brandenberger~2014 (f_NL = -35/16). Gemini's adversarial review flagged that the paper's prior framing called this a 'dual-normalization convention difference', which conflated two independent factors of two with very different epistemic status: the Komatsu-Spergel constant c (genuine normalization convention), and the missing second time-ordering of the in-in commutator (an operator-algebra identity, fixed by Hermiticity of the cubic interaction Hamiltonian and convention-independent). The substantive resolution (explicit Wick-contraction derivation of the commutator doubling identity i<[zeta^3, H_int]> = -2 Im <zeta^3 H_int>, with the four-vertex shape-function decomposition and the empirical 0.5000-ratio cross-check at the three benchmark configurations) was already shipped in Wave 11-D at L399-446 (App A.1, R42 B8). What was missing was the explicit framing in the appendix title and intro paragraph that distinguished operator-algebra identity from normalization convention. Wave 14-K closes this cheap-fast: appendix title v1.7.6 'Bispectrum Convention: Cai vs. Li-Brandenberger' → v1.7.7 'Bispectrum Convention vs. Operator-Algebra Identity: Cai vs. Li-Brandenberger'; intro paragraph rewritten to explicitly decompose the factor-of-two into (a) genuine normalization convention difference (the c constant) plus (b) the missing in-in time-ordering, which is an operator-algebra identity not a convention; and added a one-sentence note that treating both as conventions would be misleading because the in-in commutator factor is fixed by Hermiticity and is the same in any normalization. Cites the cross-model peer-review concern explicitly (R42 Gemini~3.1-Pro P2 BLOCKER B-3) for traceability. P2 .tex bumped v1.7.6 → v1.7.7, date May 1 07:30 PDT → 18:30 PDT, recompiled clean on Pod 3 H200 (pdflatex × 2 in /workspace/recompile_p2/, 759,783 bytes / 15 pp / 1 pre-existing Maldacena:2003 undef cite unrelated to this edit / cosmetic font-shape warnings same as every prior P2), mirrored to research/focused_paper_source_integration/ + public/papers/. Seventeen cross-model findings (P3-CM-B4 14-A, P4-OA-B1+B2 14-C, P4-OA-B6 14-D, P4-OA-B4 14-E, Gemini P4 M-1+m-1 14-F, OpenAI P4 M-2+M-3 + OpenAI M-8 / Gemini m-2 documented 14-G, OpenAI minor-1+minor-3+minor-5+M-6 14-H, OpenAI B4 + B3+minor-2+minor-4 documented 14-I, OpenAI M-4 + minor-3-leftover + minor-1-leftover 14-J, Gemini P2 B-3 14-K) now closed across ten cheap-fast sub-waves inside the single multi-hour Wave 14-B 1M SPARCL fetch window. Pod 3 H200 SPARCL 1M fetch alive on PID 25860, ~3h05m elapsed at this commit, 75 shards / 112 MB written, throughput steadily declining (Wave 14-J observed 197 spectra/min, Wave 14-K observed lower); 100K sub-sample short-circuit remains strongly recommended. $0 marginal H200 spend — recompile_p2 shares the same Pod 3 session running the fetch.",
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
      version: "v1.7.7",
      readiness: 91,
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
      version: "v1.0.15",
      readiness: 97,
    },
  ],
  blockerTally: {
    closed: 17, // +1 from Wave 14-K: Gemini P2 BLOCKER B-3 Appendix-A framing fix (operator-algebra identity vs normalization convention now explicitly separated)
    openBlockers: 2, // -1 from Wave 14-K: Gemini P2 B-3 closed via cheap-fast Appendix-A title + intro clarification; substantive resolution already at L399-446 (Wick contraction derivation, Wave 11-D)
    openMajors: 19, // unchanged — Wave 14-K closes a BLOCKER not a MAJOR
    openMinors: 18, // unchanged
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~36-60 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-B 1M Jaccard fetch ~85 h on the observed ~197 spectra/min sustained throughput, 100K sub-sample short-circuit (~8.5 h) remains strongly recommended)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-B 1M SPARCL fetch in flight (PID 25860, ~3h05m elapsed at Wave 14-K commit, 75 shards / 112 MB written; throughput now declining vs Wave 14-J's 197 spectra/min — possibly NOIRLab SPARCL load shedding or rate limiting. Recompile_p2 (15 pp / 759 KB / 1 pre-existing undef cite) ran cleanly in same session, $0 marginal H200 spend. 100K sub-sample short-circuit remains strongly recommended.)",
    },
  ],
};
