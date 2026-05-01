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
  lastUpdatedISO: "2026-05-02T02:00:00Z",
  lastUpdatedDisplay: "2026-05-01 19:00 PT",
  headline:
    "Wave 14-L LANDED — P3 v3.1.8 → v3.1.9 (Gemini P3 m-1 SIMBAD novelty headline downgrade: 58.8% SIMBAD-unmatched relabeled as a database-coverage measurement, not a discovery rate; 17.8% genuine novelty against 20 all-sky catalogs via CDS X-Match is now the primary catalog novelty figure cited in §V.A and Fig. 5 caption); 18 cross-model findings closed across 11 cheap-fast sub-waves while the Wave 14-B 1M SPARCL fetch continues; Wave 14-K's 'throughput declining' narrative corrected — full-window math at this commit shows ~204 spectra/min sustained, roughly stable",
  summary:
    "Wave 14-L closes one Gemini-3.1-Pro P3 MINOR (m-1) by demoting the misleading 58.8% SIMBAD-unmatched headline and elevating the 17.8% genuine novelty figure (178/1,000 DESI DR1 top-anomalies vs 20 all-sky catalogs via CDS X-Match) to primary metric. Gemini's adversarial review flagged that the paper was conflating two distinct quantities: (a) the SIMBAD-unmatched fraction (58.8% on DESI DR1 / 99.6% on LAMOST DR10 / 99.9% on SDSS DR18), which measures absence from a single curated synthesis database and substantially overstates true catalog novelty because SIMBAD does not individually index the majority of photometric detections from wide-field surveys (a 100% archival-identification rate is recovered in NED+VizieR for the SDSS DR18 top-20 SIMBAD-unmatched anomalies, already documented inline in §V.A); and (b) the genuine novelty fraction against a deep multi-catalog baseline (17.8% via CDS X-Match against 20 catalogs, paragraph 'Archival cross-match and genuine novelty floor'). Wave 14-L closes this cheap-fast: §V.A SIMBAD subsection now opens with a new R42 Wave 14-L peer-review reframe paragraph leading with 17.8% genuine novelty as the primary metric and demoting 58.8% to 'a database-coverage measurement, not a discovery rate'; existing 58.8% sentence retains its number but is explicitly tagged 'This is a database-coverage measurement, not a discovery rate.'; Fig. 5 (fig:novelty) caption expanded with bold 'R42 Wave 14-L:' framing — 58.8% explicitly tagged database-coverage; 17.8% is 'the primary catalog novelty figure'; ~5.6× reduction factor between SIMBAD-unmatched and genuine novelty explicitly cited; closing sentence 'readers should quote 17.8% (not 58.8%) when summarizing the catalog's discovery rate'. Cites the cross-model peer-review concern explicitly (R42 Gemini~3.1-Pro P3-CM-m1) for traceability. P3 .tex bumped v3.1.8 → v3.1.9, date May 1 11:15 PDT → 19:00 PDT, recompiled clean on Pod 3 H200 (pdflatex × 2 in /workspace/recompile_p3/, 28,299,132 bytes / 39 pp / 0 undef refs / 0 undef cites / 2 'Wave 14-L' occurrences confirmed), mirrored to pipelines/p3_anomaly_engine/ + public/papers/{paper3_draft.pdf, paper3_anomaly_catalog.pdf, anomaly-catalog-paper.pdf}. Eighteen cross-model findings (P3-CM-B4 14-A, P4-OA-B1+B2 14-C, P4-OA-B6 14-D, P4-OA-B4 14-E, Gemini P4 M-1+m-1 14-F, OpenAI P4 M-2+M-3 + OpenAI M-8 / Gemini m-2 documented 14-G, OpenAI minor-1+minor-3+minor-5+M-6 14-H, OpenAI B4 + B3+minor-2+minor-4 documented 14-I, OpenAI M-4 + minor-3-leftover + minor-1-leftover 14-J, Gemini P2 B-3 14-K, Gemini P3 m-1 14-L) now closed across eleven cheap-fast sub-waves inside the single multi-hour Wave 14-B 1M SPARCL fetch window. Pod 3 H200 SPARCL 1M fetch alive on PID 25860, ~3h25m elapsed at this commit, 82 shards / 116 MB written, throughput corrected to ~204 spectra/min sustained (Wave 14-K's single-window 'declining' read was over-narrow; full-window math 82 shards × ~500 spectra/shard / 205 minutes ≈ 204 spectra/min shows roughly stable). 100K sub-sample short-circuit (~8 h ETA from this commit) remains strongly recommended on cost/cadence grounds, not because throughput is dropping. $0 marginal H200 spend — recompile_p3 shares the same Pod 3 session running the fetch.",
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
      version: "v3.1.9",
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
    closed: 18, // +1 from Wave 14-L: Gemini P3 MINOR m-1 SIMBAD novelty headline downgrade (17.8% genuine novelty now primary metric; 58.8% SIMBAD-unmatched relabeled database-coverage)
    openBlockers: 2, // unchanged — Wave 14-L closes a MINOR not a BLOCKER
    openMajors: 19, // unchanged
    openMinors: 17, // -1 from Wave 14-L: Gemini P3 m-1 closed via cheap-fast precise-language reframe (§V.A SIMBAD subsection + Fig. 5 caption)
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~36-60 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-B 1M Jaccard fetch ~70 h on corrected ~204 spectra/min sustained throughput, 100K sub-sample short-circuit (~8 h from this commit) remains strongly recommended on cost/cadence grounds)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-B 1M SPARCL fetch in flight (PID 25860, ~3h25m elapsed at Wave 14-L commit, 82 shards / 116 MB written; throughput corrected to ~204 spectra/min sustained, roughly stable across full-window measurement — Wave 14-K's single-window 'declining' read was over-narrow. Recompile_p3 (39 pp / 28.30 MB / 0 undef refs / 0 undef cites) ran cleanly in same session, $0 marginal H200 spend. 100K sub-sample short-circuit (~8 h ETA from this commit) remains strongly recommended on cost/cadence grounds.)",
    },
  ],
};
