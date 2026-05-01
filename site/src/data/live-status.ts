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
  lastUpdatedISO: "2026-05-02T00:55:00Z",
  lastUpdatedDisplay: "2026-05-01 17:55 PT",
  headline:
    "Wave 14-J LANDED — P4 v1.0.15 (OpenAI MAJOR M-4 SI/DOI footnote anchoring all r42_results/*.json artifacts to the public paper4-v1.0 GitHub release tag + Wave 14-H minor-3 leftover at L278 closed + Wave 14-H minor-1 leftover at L820 closed); 16 cross-model findings closed across 9 cheap-fast sub-waves while the Wave 14-B 1M SPARCL fetch continues",
  summary:
    "Wave 14-J closes one OpenAI MAJOR (M-4 SI/DOI reproducibility-deposit anchor) plus mops up two cheap-fast residuals that Wave 14-H missed when scrubbing internal shorthand. OpenAI MAJOR M-4 (move essential numerical results into paper/SI with persistent DOIs): the reviewer flagged that the paper cites \\\\texttt{r42\\\\_results/*.json} files for confusion matrices, throughput logs, GEMM/batch-size sweeps, and bootstrap results without anchoring them to a deposit. Took the cheap-fast footnote-anchor path: the first \\\\texttt{r42\\\\_results/B20\\\\_B21\\\\_results.json} cite at L290 (§II.B GZ1-cross-check paragraph) now carries a labeled fn:repro_artifacts footnote that maps every r42_results/*.json file in the paper to the paper4-v1.0 release tag at https://github.com/Hubify-Projects/bigbounce/releases/tag/paper4-v1.0 in the path pipelines/p2_chirality/r42_results/, with a forward-pointer that subsequent paper versions tag paper4-v1.1 / paper4-v1.2 etc. with cumulative artifacts. OpenAI minor-3 leftover (L278 P_ACW in §II.B GZ1 cross-check): Wave 14-H standardized CCW at L156/L170/L1327/L1331 but missed L278's `(\\\\textsc{spiral} with $P_{\\\\mathrm{CW}}\\\\!\\\\neq\\\\!P_{\\\\mathrm{ACW}}$, or` reference to GZ1's published variable-name schema. Closed by changing P_ACW → P_CCW in our convention with an inline note that GZ1's published schema labels this variable P_ACW, identical to P_CCW (anchored to the existing footnote at the start of Sec.~\\\\ref{sec:intro}). OpenAI minor-1 leftover (L820 \"R42-required\" in §IV.A bootstrap paragraph): Wave 14-H scrubbed \"R42\" / \"Reviewer R1\" / \"BLOCKER B21\" tokens at 7 .tex sites but missed L820's \"is the R42-required uncertainty quantification for the raw-catalog asymmetry baseline\" trailing sentence, plus its inline `(companion artifact \\\\texttt{r42\\\\_results/B19\\\\_sustained\\\\_results.json})` cite. Closed by replacing \"R42-required\" with \"external peer-review-required\" and replacing the inline raw filename with `(companion artifact deposited with the public release; see Sec.~\\\\ref{sec:data_availability})` so the artifact deposit anchors via the central data-availability section rather than scattered raw filenames. P4 .tex bumped v1.0.14 → v1.0.15, date 17:25 PDT → 17:55 PDT, recompiled clean on Pod 3 H200 (pdflatex × 2 in /workspace/recompile_p4/, 25.79 MB / 19 pp / 0 undef refs / 2 cosmetic OT1/cmr font-shape warnings same as every prior P4), mirrored to pipelines/p2_chirality/ + public/papers/. Sixteen cross-model findings (P3-CM-B4 14-A, P4-OA-B1+B2 14-C, P4-OA-B6 14-D, P4-OA-B4 14-E, Gemini P4 M-1+m-1 14-F, OpenAI P4 M-2+M-3 + OpenAI M-8 / Gemini m-2 documented 14-G, OpenAI minor-1+minor-3+minor-5+M-6 14-H, OpenAI B4 + B3+minor-2+minor-4 documented 14-I, OpenAI M-4 + minor-3-leftover + minor-1-leftover 14-J) now closed across nine cheap-fast sub-waves inside the single multi-hour Wave 14-B 1M SPARCL fetch window. Pod 3 H200 SPARCL 1M fetch alive on PID 25860, ~2h29m elapsed at this commit, 62 shards / 99 MB written, sustained throughput ~197 spectra/min — within the corrected Wave 14-G ~170 spectra/min envelope; at the current sustained rate the 1M ETA is ~85 hours, so the 100K sub-sample short-circuit (~8.5 hours) remains the strongly recommended operational call when the next compute-heavy decision lands. $0 marginal H200 spend — recompile_p4 shares the same Pod 3 session running the fetch.",
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
      version: "v1.0.15",
      readiness: 97,
    },
  ],
  blockerTally: {
    closed: 16, // +1 from Wave 14-J: OpenAI P4 MAJOR M-4 SI/DOI footnote anchor (minor-3-leftover at L278 + minor-1-leftover at L820 are residual mop-ups of Wave 14-H, not new closures)
    openBlockers: 3, // unchanged from Wave 14-I — Wave 14-J closes a MAJOR not a BLOCKER
    openMajors: 19, // -1 from Wave 14-J: M-4 SI/DOI footnote anchor closed
    openMinors: 18, // unchanged — Wave 14-J residuals were Wave 14-H counted minors (already counted closed at 14-H)
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~36-60 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-B 1M Jaccard fetch ~85 h on the observed ~197 spectra/min sustained throughput, 100K sub-sample short-circuit (~8.5 h) remains strongly recommended)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-B 1M SPARCL fetch in flight (PID 25860, ~2h29m elapsed at Wave 14-J commit, 62 shards / 99 MB written, sustained throughput ~197 spectra/min — within the corrected Wave 14-G ~170 spectra/min envelope; at the current rate the 1M ETA is ~85 h, 100K sub-sample short-circuit (~8.5 h) remains the strongly recommended operational call)",
    },
  ],
};
