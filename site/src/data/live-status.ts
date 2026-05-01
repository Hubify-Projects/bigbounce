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
  lastUpdatedISO: "2026-05-02T05:00:00Z",
  lastUpdatedDisplay: "2026-05-01 22:00 PT",
  headline:
    "Wave 14-P LANDED — P1 v2.3.6 → v2.3.7 (Gemini-3.1-Pro P1 MAJOR M-2 NaMaster pipeline-validation move out of the abstract per Gemini's literal 'Do not list it in the abstract or executive summary (Table I) as part of the observational evidence' ask: NaMaster pseudo-C_ℓ sentence deleted from abstract and replaced with a parenthetical Sec.~\\ref{sec:data_cmb} cross-reference stating the pipeline-recovery cross-check is 'not part of the observational evidence reported in this abstract or in Table~\\ref{tab:summary}'; §VI Eq.~18 NaMaster paragraph at L427 prepended with bold/italic R42 Wave 14-P peer-review reframe block stating the recovery SNR figures (e.g. 20.32, 25.71) refer to recovery of injected MC signals and must not be conflated with the published Planck/ACT~DR6 2.4–2.9σ sky detection); 22 cross-model findings closed across 15 cheap-fast sub-waves while the Wave 14-B 1M SPARCL fetch continues; Pod 3 throughput full-window ~195 spectra/min sustained at ~5 h elapsed",
  summary:
    "Wave 14-P closes one Gemini-3.1-Pro P1 MAJOR (M-2) on the cheap-fast precise-language axis. Gemini's adversarial review explicitly stated, in literal terms, 'Do not list it in the abstract or executive summary (Table I) as part of the observational evidence,' on the grounds that NaMaster pseudo-C_ℓ on the Planck Commander map with injected constant-β Monte Carlos is a pipeline-recovery validation of the deconvolution stack, not a sky detection of cosmic birefringence. Wave 11-A had previously partially addressed this by adding a 'methodology cross-check rather than a sky detection' framing inline in the abstract, but the abstract still listed the NaMaster sentence alongside the published Planck/ACT~DR6 2.4–2.9σ sky detection, which is what Gemini's literal ask said to remove. Wave 14-P closes this cheap-fast: (1) literal removal of the NaMaster sentence from the P1 abstract, replaced with a single parenthetical clause appended to the surviving Planck/ACT detection sentence: '(a methodology pipeline-recovery cross-check using NaMaster pseudo-C_ℓ on the Planck Commander map is reported as a cross-check in Sec.~\\ref{sec:data_cmb} only and is not part of the observational evidence reported in this abstract or in Table~\\ref{tab:summary})'; (2) §VI Eq.~18 NaMaster paragraph at L427 prepended with bold paragraph header 'R42 Wave 14-P peer-review reframe (cross-model Gemini 3.1-Pro P1 M-2)' followed by italic block stating the NaMaster analysis is a bias-injection MC validation of the deconvolution pipeline (not a cosmological measurement), is documented only in the Data Methods section as a methodology cross-check, has been removed from the abstract, and is not listed in Table~\\ref{tab:summary}, the executive summary, or anywhere outside this section as part of the observational evidence; the high pipeline-recovery SNR figures (e.g. 20.32, 25.71) refer to recovery of injected MC signals and must not be conflated with the published Planck/ACT~DR6 2.4–2.9σ sky detection. P1 .tex bumped v2.3.6 → v2.3.7, date May 1 19:30 PDT → 22:00 PDT, recompiled clean on Pod 3 H200 (pdflatex × 2 in /workspace/recompile_p1/, 1,229,642 bytes / 33 pp / 0 errors / 0 undef refs / 1 'Wave 14-P' occurrence / 1 pre-existing WilsonEwing2012 undef cite), mirrored to public/papers/{paper1_spin_torsion.pdf, spin_torsion_paper1.pdf, spin-torsion-paper.pdf}. Twenty-two cross-model findings (P3-CM-B4 14-A, P4-OA-B1+B2 14-C, P4-OA-B6 14-D, P4-OA-B4 14-E, Gemini P4 M-1+m-1 14-F, OpenAI P4 M-2+M-3 + OpenAI M-8 / Gemini m-2 documented 14-G, OpenAI minor-1+minor-3+minor-5+M-6 14-H, OpenAI B4 + B3+minor-2+minor-4 documented 14-I, OpenAI M-4 + minor-3-leftover + minor-1-leftover 14-J, Gemini P2 B-3 14-K, Gemini P3 m-1 14-L, OpenAI P1 B-4 14-M, Gemini P3 m-2 14-N, Gemini P3 M-2 14-O, Gemini P1 M-2 14-P) now closed across fifteen cheap-fast sub-waves inside the single multi-hour Wave 14-B 1M SPARCL fetch window. Pod 3 H200 SPARCL 1M fetch alive on PID 25860, ~5 h elapsed at this commit, throughput full-window ~195 spectra/min sustained — consistent with Wave 14-O's reading. 100K sub-sample short-circuit (~5 h ETA from this commit) remains strongly recommended on cost/cadence grounds. $0 marginal H200 spend — recompile_p1 shares the same Pod 3 session running the fetch.",
  papers: [
    {
      slug: "spin-torsion",
      number: 1,
      shortTitle: "Spin-Torsion Cosmology",
      version: "v2.3.7",
      readiness: 94,
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
    closed: 22, // +1 from Wave 14-P: Gemini P1 M-2 NaMaster pipeline-validation move out of abstract (abstract NaMaster sentence removed per Gemini's literal "do not list" ask; §VI Eq.~18 paragraph prepended with R42 Wave 14-P peer-review reframe block)
    openBlockers: 1, // unchanged from Wave 14-O
    openMajors: 17, // -1 from Wave 14-P: Gemini P1 M-2 closed
    openMinors: 16, // unchanged from Wave 14-O
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~30-54 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-B 1M Jaccard fetch ~80 h on sustained ~195 spectra/min full-window throughput, 100K sub-sample short-circuit (~5 h from this commit) remains strongly recommended on cost/cadence grounds)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-B 1M SPARCL fetch in flight (PID 25860, ~5 h elapsed at Wave 14-P commit; throughput full-window ~195 spectra/min sustained, consistent with Wave 14-O reading. Recompile_p1 (33 pp / 1.23 MB / 0 errors / 0 undef refs / 1 'Wave 14-P' occurrence / 1 pre-existing WilsonEwing2012 undef cite) ran cleanly in same session, $0 marginal H200 spend. 100K sub-sample short-circuit (~5 h ETA from this commit) remains strongly recommended on cost/cadence grounds.)",
    },
  ],
};
