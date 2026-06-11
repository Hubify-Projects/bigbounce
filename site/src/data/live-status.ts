// Live build status surfaced at the top of every page.
// Updated each cron fire / wave-close commit. Renders into <LiveStatus />.
// Timestamp is baked in at build time — bump on every commit that ships
// research progress so Vercel rebuilds put the new value live.
//
// KEEP EVERY STRING SHORT. headline <= 2 sentences, summary <= 3 sentences,
// pendingWork/why/ask one line each. The audit trail lives in
// project-context/SSOT/, never here.

export interface PaperProgress {
  slug: string;
  number: string;
  shortTitle: string;
  version: string;
  readiness: number; // percent 0-100
  pendingWork: string; // ONE LINE: what is still pending for this paper
}

export interface NeedsHoustonItem {
  title: string;       // short label (e.g. "arXiv submission credentials")
  why: string;         // ONE SENTENCE: why ONLY Houston can unblock this
  blockedPaper?: string; // e.g. "P1A", "P4", "P5" — which paper this gates
  ask: string;         // ONE SENTENCE: exact action Houston needs to take
}

export interface LiveStatus {
  lastUpdatedISO: string; // ISO 8601 UTC, baked at build time
  lastUpdatedDisplay: string; // human-readable PT timestamp for the banner
  headline: string; // 1-2 sentences, current state
  summary: string; // 1-3 sentences, what just shipped
  currentlyRunning: string[]; // short bullets of what is actively running RIGHT NOW
  needsHouston: NeedsHoustonItem[]; // ONLY items truly blocked on Houston
  papers: PaperProgress[]; // 6 papers, sorted by display order
  blockerTally: {
    closed: number;
    openBlockers: number;
    openMajors: number;
    openMinors: number;
  };
  cronStatus: string;
  etaToCompletion: string; // human-readable ETA to all-papers @ 100%
  pods: Array<{
    name: string;
    state: "active" | "idle" | "queued";
    note: string;
  }>;
}

export const liveStatus: LiveStatus = {
  lastUpdatedISO: "2026-06-11T06:40:00Z",
  lastUpdatedDisplay: "June 10, 2026 · 11:40 PM PT",
  headline:
    "EXT2 external cycle complete — closure wave restamped all six; gap metric 60 → ~32 vs EXT1 baseline; EXT3 pending.",
  summary:
    "EXT2 closure wave restamped all six papers same-day; readiness 95/94/94/95/95/95 (P1A/P1B/P2/P3/P4/P5); EXT3 pending. Per-paper versions live in the table below; changelog detail lives in SSOT/git.",
  currentlyRunning: [
    "Hourly native-PDF cross-vendor review autoloop on all 6 papers (Claude · GPT · Gemini · Grok · Perplexity + meta-reviewer)",
    "Persistence tracker fingerprinting findings across fires; load-bearing items escalate to Houston decision package",
    "Site + SSOT + Convex sync on every paper version bump",
  ],
  needsHouston: [
    {
      title: "Personal sign-off — all six papers at the post-EXT2 gate",
      blockedPaper: "all",
      why: "EXT1 + EXT2 browser-tier external rounds ran 2026-06-10 and every VERIFIED finding is closed; readiness sits at 94-95% and the final 1% is Houston-only.",
      ask: "Read the current PDFs end-to-end and reply 'sign off PX' per paper, or send blocking findings for truth-audit (recommended order P4 → P1A+P1B → P3 → P2 → P5).",
    },
    {
      title: "arXiv endorsement + submission credentials",
      blockedPaper: "all",
      why: "Only Houston has the arXiv account and astro-ph endorser relationships.",
      ask: "Submit each signed-off paper (recommended order P4 → P1A+P1B → P3 → P2 → P5); tarballs are prepared.",
    },
  ],
  papers: [
    {
      slug: "paper-1a",
      number: "1A",
      shortTitle: "ECH dark-energy closure + perturbation transparency",
      version: "v1A.0.59",
      readiness: 95,
      pendingWork: "v1A.0.59 — EXT2: confabulated Ref[22] replaced with Shapiro-Teixeira 2014, R29 pair-exchange sign-error chain deleted, WKB 60→30 orders recomputed; EXT3 pending; 95-cap until clean external round + Houston sign-off",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.57",
      readiness: 94,
      pendingWork: "v1B.0.57 — EXT2: 176,240 chain-confirmed, planck_bao_sn CORRECTED diagnostics added (ΔN_eff +0.058±0.179 / H0 67.78±1.09 rebooked), root CHANGELOG pin created; EXT3 pending; 95-cap until clean external round + Houston sign-off",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.51",
      readiness: 94,
      pendingWork: "v1.7.51 — EXT2: headline realistic range honestly rebooked 3-5σ → 2.6-5σ at all sites, Li -35/16 demoted to single-ordering intermediate; EXT3 pending",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.90",
      readiness: 95,
      pendingWork: "v3.1.90 — EXT2: 203-novel demoted to SIMBAD-unmatched, caveats caption honest, fixed-α grid reference-only; EXT3 pending; 95-cap until clean external round + Houston sign-off",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.174",
      readiness: 95,
      pendingWork: "v1.0.174 — EXT2: HC real-space dipole mislabel fixed, A95 falsification boundary honest, hash re-pinned; EXT3 pending; 95-cap until clean external round + Houston sign-off",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.63",
      readiness: 95,
      pendingWork: "v0.1.63 — EXT2: dual-parent sample ledger split (DESIVAST 678,945 vs V-Web 783,820), conditional-permutation framing corrected; EXT3 pending; 95-cap until clean external round + Houston sign-off",
    },
  ],
  blockerTally: {
    closed: 701, // 678 through the pod wave + 23 R26conf closures (P1A 2 catches + P3 12 textual + P5 9; P1B M-tier traceability closures + CPL falsification not separately tallied); P1B R26conf CLEAN
    openBlockers: 0,
    openMajors: 0,
    openMinors: 0,
  },
  cronStatus: "autonomous review loop active — hourly fires",
  etaToCompletion:
    "All six papers targeted publishable ~June 12–13, 2026 (per SSOT/PUBLISH_PLAN.md). Gated on Houston external round + sign-off; the final 1% is Houston-only.",
  pods: [],
};
