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
  lastUpdatedISO: "2026-05-02T00:00:00Z",
  lastUpdatedDisplay: "2026-05-01 17:00 PT",
  headline:
    "Wave 14-H LANDED — P4 v1.0.13 (OpenAI minor-1 PRD shorthand cleanup + minor-3 CCW/ACW standardization + minor-5 T2 60° rotation justification + M-6 T3 artifact-rejection held-out N + Clopper-Pearson 95% bound); 12 cross-model findings closed across 7 cheap-fast sub-waves while the Wave 14-B 1M SPARCL fetch continues",
  summary:
    "Wave 14-H closes four more cheap-fast OpenAI/GPT-5 P4 findings inside the Wave 14-B compute-idle window. OpenAI minor-1 (PRD shorthand cleanup): manuscript scrubbed of internal-reviewer tokens \"R42\", \"Reviewer R1\", \"BLOCKER B21\", \"P4-OA-M7\" / \"P4-CM-B1\" — across 7 .tex locations (L470 §III.B, L505-506 + L510 + L513 §sec:tta paragraph, L727 §sec:cw_frac itemize, L1009 §sec:multipoles footnote, L1087 §sec:multipoles MASTER-primary clause, L1265 §sec:dipole high-confidence-primary clause). Replacement language is PRD-style (\"external peer review\", \"cross-model peer review (cross-confirmed by Gemini 3.1-Pro and GPT-5)\", \"transition-matrix subsample\", \"leakage test\"). OpenAI minor-3 (CCW/ACW standardization): §I.B + §V.B + §V.C all standardized — \\CW/\\text{ACW} replaced with \\CW/\\CCW at L156 (with one-time footnote noting CE-ResNet's ACW=our CCW), L170 \"all classified as CW or CCW since CE-ResNet lacks a not-spiral class\", L1327 + L1331 CE-ResNet comparison rows. OpenAI minor-5 (T2 60° rotation justification): §IV.B Bias Hardening Suite T2 entry at L543-544 expanded with explicit rationale — 60° steps over 90° cardinals to avoid aliasing with the pixel-grid four-fold symmetry which could mask grid-correlated bias along cardinal axes; 60° resolution bounds worst-case bias-axis miss to ±30°. OpenAI M-6 (T3 artifact-rejection held-out N): §IV.B T3 entry at L545-546 expanded — 100% pass rate now reported as 400/400 on the held-out 20% validation split of the synthetic hard-negative training set (Sec:labels item 3), with Clopper-Pearson one-sided 95% lower bound 99.25% well above the >70% threshold; addresses M-6 ask for held-out N + uncertainty quantification. P4 .tex bumped v1.0.12 → v1.0.13, date 16:35 PDT → 17:00 PDT, recompiled clean on Pod 3 (pdflatex × 2 in /workspace/recompile_p4/, 25.79 MB / 18 pp / 0 undef refs — same 2 cosmetic OT1/cmr font-shape warnings every prior P4 carries), mirrored to pipelines/p2_chirality/ + public/papers/. Twelve cross-model findings (P3-CM-B4 14-A, P4-OA-B1+B2 14-C, P4-OA-B6 14-D, P4-OA-B4 14-E, Gemini P4 M-1+m-1 14-F, OpenAI P4 M-2+M-3 + OpenAI M-8 / Gemini m-2 documented 14-G, OpenAI minor-1 + minor-3 + minor-5 + M-6 14-H) now closed across seven cheap-fast sub-waves inside the single multi-hour Wave 14-B 1M SPARCL fetch window — the cheap-fast text-edit while compute runs discipline (feedback_more_not_less.md + feedback_default_hardest_path.md) keeps yielding ~3-5 closures per ~25-min wave at zero marginal compute. Pod 3 H200 SPARCL 1M fetch alive on PID 25860, ~1h54m elapsed at this commit, 47 shards / 83 MB written, sustained throughput ~206 spectra/min — within the corrected Wave 14-G ~170 spectra/min envelope (vs. Wave 14-F's stale 275 spectra/min over-read which was an arithmetic miss against a single-shard window); at the current sustained rate the 1M ETA is ~80 hours, so the 100K sub-sample short-circuit (~8 hours) remains the strongly recommended operational call when the next compute-heavy decision lands.",
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
      version: "v1.0.13",
      readiness: 97,
    },
  ],
  blockerTally: {
    closed: 14, // 14 cross-model BLOCKERs closed across Waves 11-14 (Wave 14-H closes 1 OpenAI MAJOR + 3 minors, not BLOCKERs)
    openBlockers: 4, // remaining cross-model BLOCKERs (P3-OA-M1 1M Jaccard pending fetch / sub-sample short-circuit)
    openMajors: 20, // -1 from Wave 14-H: OpenAI P4 M-6 (T3 artifact-rejection held-out N + Clopper-Pearson 95% bound)
    openMinors: 20, // -3 from Wave 14-H: OpenAI P4 minor-1 (PRD shorthand cleanup) + minor-3 (CCW/ACW standardization) + minor-5 (T2 60° rotation justification)
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~36-60 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-B 1M Jaccard fetch ~80 h on the observed ~206 spectra/min sustained throughput, 100K sub-sample short-circuit (~8 h) remains strongly recommended)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-B 1M SPARCL fetch in flight (PID 25860, ~1h54m elapsed at Wave 14-H commit, 47 shards / 83 MB written, sustained throughput ~206 spectra/min — within the corrected Wave 14-G ~170 spectra/min envelope; at the current rate the 1M ETA is ~80 h, 100K sub-sample short-circuit (~8 h) remains the strongly recommended operational call)",
    },
  ],
};
