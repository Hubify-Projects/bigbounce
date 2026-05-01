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
  lastUpdatedISO: "2026-05-02T10:25:00Z",
  lastUpdatedDisplay: "2026-05-02 03:25 PT",
  headline:
    "Wave 14-Y LANDED · P1 v2.3.13 · 31 cross-model findings closed · ETA all-4 → 100%: ~20-40 h",
  summary:
    "P1 v2.3.13: R42 P1-OA-M3 MAJOR closed via the Wave 14-Q 'demote-with-explicit-disowning' pattern. The published Eskilt et al. joint Planck+ACT β=0.342°±0.094° (3.6σ) is now the headline observational constraint at every body site (L152 §I.B intro item, L448 consolidated birefringence summary, L907 Fig consistency_window caption, L1081 §observational signatures, L1265 claims summary table). The simplified IVW combination β=0.241°±0.061° (3.9σ) survives at Eq. eq:beta_combined only as an auxiliary cross-check, prefaced by an explicit Wave 14-Y reframe block (L892) stating the paper does not use 3.9σ as the headline anywhere — IVW neglects shared calibration systematics and inflates significance. Pod 3 4-pass recompile clean: 33 pp / 1,235,593 bytes / 0 errors / 0 undef refs. Mirrored to all 7 P1 surfaces. Cron */20 armed.",
  papers: [
    {
      slug: "spin-torsion",
      number: 1,
      shortTitle: "Spin-Torsion Cosmology",
      version: "v2.3.13",
      readiness: 96,
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
      version: "v3.1.13",
      readiness: 95,
    },
    {
      slug: "chirality-catalog",
      number: 4,
      shortTitle: "Galaxy Chirality Catalog",
      version: "v1.0.16",
      readiness: 97,
    },
  ],
  blockerTally: {
    closed: 31, // +1 from Wave 14-Y: P1-OA-M3 MAJOR closed (IVW 3.9σ → Eskilt 0.342°/3.6σ headline reframe across 5 body sites + Eq. 18 auxiliary-only label)
    openBlockers: 0, // unchanged from Wave 14-X
    openMajors: 12, // -1 from Wave 14-X: P1-OA-M3 closed
    openMinors: 13, // unchanged from Wave 14-X
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~18-36 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-Y P1-OA-M3 IVW 3.9σ → Eskilt 0.342°/3.6σ headline reframe COMPLETE across 5 body sites + Eq. 18 auxiliary-only label, 4-pass recompile clean on Pod 3 H200, mirrored to all 7 P1 surfaces, $0 marginal H200 spend; Wave 14-Z candidates queued: (a) Wave 14-S quantitative systematics-marginalization Fisher recompute for P3 ~2h H200, (b) P1-OA-M4 NaMaster methods paragraph ~30min-2h cheap-fast, (c) Gemini P4 B-1 NaMaster recompute + B-2 PSF cross-correlation ~2-4h, (d) OpenAI P4 B5/B7/M-1/M-5/M-7/M-9 leftover MAJORS cheap-fast)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-Y COMPLETE: P1 v2.3.13 4-pass recompile in /workspace/recompile_p1 — 33 pp / 1,235,593 bytes / 0 errors / 0 undef refs / R42 P1-OA-M3 MAJOR IVW 3.9σ → Eskilt 0.342°/3.6σ headline reframe applied at 5 body sites (L152 §I.B intro, L448 consolidated birefringence summary, L907 Fig consistency_window caption, L1081 §observational signatures, L1265 claims summary table) + Eq. 18 IVW formula labeled `eq:beta_combined` and bracketed by an explicit Wave 14-Y reframe block (L892) stating the paper does not use 3.9σ as the headline anywhere. PDF mirrored byte-identical (1,235,593) to all 7 P1 site surfaces (arxiv/main.pdf + public/papers/{paper1_spin_torsion,spin_torsion_paper1,spin-torsion-paper}.pdf + site/public/arxiv_v2/main.pdf + site/public/papers/{paper1_spin_torsion,spin_torsion_paper1,spin-torsion-paper}.pdf). $0 marginal H200 spend (existing Pod 3 session). Wave 14-Z candidates queued for dispatch: Wave 14-S quantitative systematics-marginalization Fisher recompute for P3 (~2h H200), P1-OA-M4 NaMaster methods paragraph (~30min-2h cheap-fast), Gemini P4 B-1 NaMaster recompute + B-2 PSF cross-correlation (~2-4h), OpenAI P4 B5/B7/M-1/M-5/M-7/M-9 leftover MAJORS (cheap-fast).",
    },
  ],
};
