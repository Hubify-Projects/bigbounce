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
  lastUpdatedISO: "2026-05-02T00:25:00Z",
  lastUpdatedDisplay: "2026-05-01 17:25 PT",
  headline:
    "Wave 14-I LANDED — P4 v1.0.14 (OpenAI BLOCKER B4 Fig 1 caption note disambiguating embedded panel total 3,201,160 vs Table V snapshot 3,321,795 + B3/minor-2/minor-4 documented as already-closed); 13 cross-model findings closed across 8 cheap-fast sub-waves while the Wave 14-B 1M SPARCL fetch continues",
  summary:
    "Wave 14-I closes one OpenAI BLOCKER + documents three additional already-closed findings inside the Wave 14-B compute-idle window. OpenAI BLOCKER B4 (Fig 1 caption note): the reviewer flagged a ~120,000-object discrepancy between the embedded fig:spiral_density panel title (3,201,160 spirals) and §IV.A + Table V (3,321,795 spirals) and asked for either a Fig 1 regenerate or a caption note explaining the mask difference. Took the cheap-fast caption-note path (mirroring the Wave 14-E table-caption pattern): Fig 1 caption at L218-237 expanded with explicit disambiguation — the 3,201,160 panel total is the canonical equivariant production catalog (Wave 11-C verdict; §sec:cw_frac, Table III) used consistently for the dipole, multipole, and NaMaster analyses, and the Table V \"All sky\" 3,321,795 row is the prior sky-balance verification snapshot total disambiguated via the existing $^{\\mathrm{a}}$ footnote in that table from Wave 14-E. Three additional OpenAI P4 findings documented as already-closed without redundant .tex edits: (1) BLOCKER B3 (T7 37.9%>0.9 vs Fig 6 62.1%>0.99 dataset scoping) — the live fig:confidence_dist caption at L774-783 already states explicitly that 37.9% is the qualitative T7-only stat at the >0.9 threshold and that the older 62.1%>0.99 figure was from a different catalog snapshot superseded by the canonical T7 + sec:confidence stratification; (2) minor-2 (typo \"equivarianta\") — repo-wide grep returns zero matches in the current .tex source, the typo was either fixed in an earlier wave or was a reviewer OCR error against a prior PDF revision; (3) minor-4 (Platt equation explicit) — already closed in Wave 14-D at L672-678 with the explicit equation p_cal = σ(Az + B) with A=1/T=1/4.65, B=−1.58, L-BFGS NLL on held-out 20% validation split. P4 .tex bumped v1.0.13 → v1.0.14, date 17:00 PDT → 17:25 PDT, recompiled clean on Pod 3 (pdflatex × 2 in /workspace/recompile_p4/, 25.79 MB / 19 pp / 0 undef refs — page count 18 → 19 pp because the new Fig 1 caption note added ~6 lines triggering one more column break in the figure float; same 2 cosmetic OT1/cmr font-shape warnings every prior P4 carries), mirrored to pipelines/p2_chirality/ + public/papers/. Thirteen cross-model findings (P3-CM-B4 14-A, P4-OA-B1+B2 14-C, P4-OA-B6 14-D, P4-OA-B4 14-E, Gemini P4 M-1+m-1 14-F, OpenAI P4 M-2+M-3 + OpenAI M-8 / Gemini m-2 documented 14-G, OpenAI minor-1+minor-3+minor-5+M-6 14-H, OpenAI B4 + B3+minor-2+minor-4 documented 14-I) now closed across eight cheap-fast sub-waves inside the single multi-hour Wave 14-B 1M SPARCL fetch window. Pod 3 H200 SPARCL 1M fetch alive on PID 25860, ~2h7m elapsed at this commit, 50 shards / 86 MB written, sustained throughput ~197 spectra/min — within the corrected Wave 14-G ~170 spectra/min envelope; at the current sustained rate the 1M ETA is ~85 hours, so the 100K sub-sample short-circuit (~8.5 hours) remains the strongly recommended operational call when the next compute-heavy decision lands.",
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
      version: "v1.0.14",
      readiness: 97,
    },
  ],
  blockerTally: {
    closed: 15, // +1 from Wave 14-I: OpenAI P4 BLOCKER B4 Fig 1 caption note (B3 documented as already-closed in fig:confidence_dist caption text, not a new closure)
    openBlockers: 3, // -1 from Wave 14-I: B4 + B3 already-closed; remaining P3-OA-M1 1M Jaccard pending fetch / sub-sample short-circuit + P4-OA-B5 + P4-OA-B7
    openMajors: 20, // unchanged — Wave 14-I closes 1 BLOCKER not a MAJOR
    openMinors: 18, // -2 from Wave 14-I: minor-2 (already-closed; typo absent) + minor-4 (already-closed in 14-D)
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~36-60 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-B 1M Jaccard fetch ~85 h on the observed ~197 spectra/min sustained throughput, 100K sub-sample short-circuit (~8.5 h) remains strongly recommended)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-B 1M SPARCL fetch in flight (PID 25860, ~2h7m elapsed at Wave 14-I commit, 50 shards / 86 MB written, sustained throughput ~197 spectra/min — within the corrected Wave 14-G ~170 spectra/min envelope; at the current rate the 1M ETA is ~85 h, 100K sub-sample short-circuit (~8.5 h) remains the strongly recommended operational call)",
    },
  ],
};
