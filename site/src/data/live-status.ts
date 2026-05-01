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
  lastUpdatedISO: "2026-05-02T06:30:00Z",
  lastUpdatedDisplay: "2026-05-01 23:30 PT",
  headline:
    "Wave 14-S LANDED — P1 v2.3.8 → v2.3.9 (Gemini-3.1-Pro P1 MINOR m-2 defensive Scope-note delete in §I.C per Gemini's literal 'Let the physics justify the structure. Delete the meta-commentary.' ask: deleted the standalone '*Structure of the paper.*---The paper has two parts. Part I... Part II...' paragraph at L155 between §I.B 'Original Contributions' and §I.C 'Paper Organization' entirely; the deleted paragraph duplicated content already present in §I.B item-2 (proxy MCMC framed as 'null-consistency test, not an ECH module') and item-3 (ALP framed as '*not* a distinctive ECH prediction'), plus the §I.C 'Paper Organization' subsection that immediately follows already provides the structural map of the paper without the defensive Part-I/Part-II framing; the §I.B 'Original Contributions' scope claims and the §I.C structural map both survive untouched — only the redundant defensive meta-paragraph between them was removed; no equations, figures, numbers, or substantive claims were modified — text-only deletion); 25 cross-model findings closed across 18 cheap-fast sub-waves while the Wave 14-B 1M SPARCL fetch continues; Pod 3 throughput full-window ~195 spectra/min sustained at ~6h elapsed",
  summary:
    "Wave 14-S closes one Gemini-3.1-Pro P1 MINOR m-2 on the cheap-fast precise-language axis. Gemini's literal ask was: 'Telling the reader This paper intentionally spans three threads... The hybrid scope is a scientific necessity reads as highly defensive and signals structural bloat. ... Let the physics justify the structure. Delete the meta-commentary.' Wave 14-S closes this cheap-fast: deleted the entire L155 'Structure of the paper.---The paper has two parts. Part I... Part II...' paragraph between §I.B 'Original Contributions' and §I.C 'Paper Organization' entirely. The deleted paragraph duplicated content already present in §I.B item-2 (proxy MCMC framed as 'null-consistency test, not an ECH module') and item-3 (ALP framed as '*not* a distinctive ECH prediction'), so deleting L155 loses no information; it only removes the defensive structural framing that Gemini flagged. The §I.C 'Paper Organization' subsection at L157-L159 (now L156-L158 post-delete) provides the proper organizational map of the paper without defensiveness. No equations, figures, numbers, or substantive claims were modified — text-only deletion. P1 .tex bumped v2.3.8 → v2.3.9, date May 1 22:30 PDT → 23:30 PDT, recompiled clean on Pod 3 H200 (pdflatex × 2 in /workspace/recompile_p1/, 1,231,939 bytes / 33 pp / 0 errors / 0 undef refs / 0 'Wave 14-S' occurrences (expected — delete-only) / 1 pre-existing WilsonEwing2012 undef cite), mirrored to public/papers/{paper1_spin_torsion.pdf, spin_torsion_paper1.pdf, spin-torsion-paper.pdf}. Twenty-five cross-model findings (P3-CM-B4 14-A, P4-OA-B1+B2 14-C, P4-OA-B6 14-D, P4-OA-B4 14-E, Gemini P4 M-1+m-1 14-F, OpenAI P4 M-2+M-3 + OpenAI M-8 / Gemini m-2 documented 14-G, OpenAI minor-1+minor-3+minor-5+M-6 14-H, OpenAI B4 + B3+minor-2+minor-4 documented 14-I, OpenAI M-4 + minor-3-leftover + minor-1-leftover 14-J, Gemini P2 B-3 14-K, Gemini P3 m-1 14-L, OpenAI P1 B-4 14-M, Gemini P3 m-2 14-N, Gemini P3 M-2 14-O, Gemini P1 M-2 14-P, Gemini P1 m-1 14-Q, Gemini P3 M-1 14-R, Gemini P1 m-2 14-S) now closed across eighteen cheap-fast sub-waves inside the single multi-hour Wave 14-B 1M SPARCL fetch window. Pod 3 H200 SPARCL 1M fetch alive on PID 25860, ~6h elapsed at this commit, throughput full-window ~195 spectra/min sustained — consistent with Wave 14-R's reading. 100K sub-sample short-circuit (~5 h ETA from this commit) remains strongly recommended on cost/cadence grounds. $0 marginal H200 spend — recompile_p1 shares the same Pod 3 session running the fetch.",
  papers: [
    {
      slug: "spin-torsion",
      number: 1,
      shortTitle: "Spin-Torsion Cosmology",
      version: "v2.3.9",
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
    closed: 25, // +1 from Wave 14-S: Gemini P1 m-2 defensive Scope-note delete in §I.C (cheap-fast precise-language path)
    openBlockers: 1, // unchanged from Wave 14-R
    openMajors: 16, // unchanged from Wave 14-S (Gemini P1 m-2 was a MINOR, not a MAJOR)
    openMinors: 14, // -1 from Wave 14-S: Gemini P1 m-2 closed (was a MINOR)
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~28-52 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-B 1M Jaccard fetch ~74 h on sustained ~195 spectra/min full-window throughput, 100K sub-sample short-circuit (~5 h from this commit) remains strongly recommended on cost/cadence grounds; quantitative systematics-marginalization Fisher recompute for P3 queued ~2h H200 once Pod 3 frees up)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-B 1M SPARCL fetch in flight (PID 25860, ~6h elapsed at Wave 14-S commit; throughput full-window ~195 spectra/min sustained, consistent with Wave 14-R reading. Recompile_p1 (33 pp / 1,231,939 bytes / 0 errors / 0 undef refs / 0 'Wave 14-S' occurrences (expected — delete-only) / 1 pre-existing WilsonEwing2012 undef cite) ran cleanly in same session, $0 marginal H200 spend. 100K sub-sample short-circuit (~5 h ETA from this commit) remains strongly recommended on cost/cadence grounds. Quantitative systematics-marginalization Fisher recompute for P3 (~2h H200) queued to dispatch once fetch completes.)",
    },
  ],
};
