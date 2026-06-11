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
  lastUpdatedISO: "2026-06-11T01:55:00Z",
  lastUpdatedDisplay: "June 10, 2026 · 6:55 PM PT",
  headline:
    "R29 internal round complete — upgraded reviewer sweeps caught closure-introduced regressions, same-day patch wave restamped all six; R30conf pending, then EXT2.",
  summary:
    "R29 post-EXT1 internal round restamped all six — P1A v1A.0.58 · P1B v1B.0.56 · P2 v1.7.50 · P3 v3.1.89 · P4 v1.0.173 · P5 v0.1.62. P1A 94 (regressions fixed), P1B 94 (E1 artifact bug found+fixed), P2 94 (dimensional regressions found+fixed), P3 94, P4 95, P5 95. R30conf pending, then EXT2.",
  currentlyRunning: [
    "Hourly native-PDF cross-vendor review autoloop on all 6 papers (Claude · GPT · Gemini · Grok · Perplexity + meta-reviewer)",
    "Persistence tracker fingerprinting findings across fires; load-bearing items escalate to Houston decision package",
    "Site + SSOT + Convex sync on every paper version bump",
  ],
  needsHouston: [
    {
      title: "Anthropic API credits exhausted (reviewer leg down)",
      blockedPaper: "all",
      why: "The Claude API reviewer leg is still down on billing 400s; R23conf–R26conf ran their Claude legs in-session on subscription as a workaround, but the autoloop needs API credits for R27conf.",
      ask: "Top up API credits at console.anthropic.com → Plans & Billing, then say 'credits topped up' so full 5-vendor rounds restart.",
    },
    {
      title: "External review round on current versions",
      blockedPaper: "all",
      why: "The agent-side review loop has run; the orthogonal external pass is Houston's per his 2026-06-08 plan.",
      ask: "Run your external round on the current PDFs and send back findings for truth-audit.",
    },
    {
      title: "Personal sign-off — P4 + P2 + P1B are SIGN-OFF-READY now",
      blockedPaper: "P4, P2, P1B",
      why: "P4 completed its 2-of-2 post-retraction clean rounds, P2 came back R25conf-clean, and P1B came back R26conf-clean (third paper at the gate) — only Houston's read stands between them and arXiv.",
      ask: "Read P4 + P2 + P1B end-to-end and reply 'sign off P4'/'sign off P2'/'sign off P1B' or send blocking findings; P1A/P3/P5 follow after R27conf.",
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
      version: "v1A.0.58",
      readiness: 94,
      pendingWork: "v1A.0.58 — R29: N_tot differential restated, Cartan footnote honest substitution, bundle desync resynced; R30conf pending, then EXT2; 95-cap until clean external round + Houston sign-off",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.56",
      readiness: 94,
      pendingWork: "v1B.0.56 — R29: export-script off-by-one root-caused from chains (E1 artifact bug found+fixed); R30conf pending, then EXT2; 95-cap until clean external round + Houston sign-off",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.50",
      readiness: 94,
      pendingWork: "v1.7.50 — R29: title recast + 5-paragraph abstract + OOM dimensional regressions found+fixed, BF rebooked ~9-14 (readiness 95→94); R30conf pending, then EXT2",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.89",
      readiness: 94,
      pendingWork: "v3.1.89 — R29: half-applied eROSITA de-scope completed, manifest byte-identical pair documented; R30conf pending, then EXT2; 95-cap until clean external round + Houston sign-off",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.173",
      readiness: 95,
      pendingWork: "v1.0.173 — R29: NSIDE sensitivity computed (z stable 16.9–19.4), missing NS gallery panel restored, hash re-pinned; R30conf pending, then EXT2; 95-cap until clean external round + Houston sign-off",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.62-2026-06-10",
      readiness: 95,
      pendingWork: "v0.1.62 — R29: Wald-shift bound corrected to ≤0.12 SE, void-fraction denominators disambiguated; R30conf pending, then EXT2; 95-cap until clean external round + Houston sign-off",
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
