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
  lastUpdatedISO: "2026-06-10T04:30:00Z",
  lastUpdatedDisplay: "June 9, 2026 · 9:30 PM PT",
  headline:
    "R23conf full 5-vendor confirmation round closed on all six papers: ~200 findings truth-audited, all VERIFIED findings closed same-day, all six papers bumped (P1A v1A.0.51 · P1B v1B.0.52 · P2 v1.7.46 · P3 v3.1.81 · P4 v1.0.168 · P5 v0.1.53) — next gate is a clean R24conf round (P4 needs two).",
  summary:
    "R23conf closures: P1A cleanest round (E:0/M:0, birefringence factor-of-2 fixed); P1B §VI ALP provenance rewritten to committed-chain truth (run1-3, 9,720 samples) + c10 robustness battery; P2 Table III rebuilt from committed c9g recompute + null-space scatter 4.4–6.2σ propagated; P3 abstract 7.9%→9.4% anchored + gold/silver tiers (1,122); P4 headline null regenerated from the fixed generator 0.43σ→0.41σ (p=0.31, verdict unchanged); P5 Bonferroni misstatement fixed + count ledger unified (783,820 unique).",
  currentlyRunning: [
    "Hourly native-PDF cross-vendor review autoloop on all 6 papers (Claude · GPT · Gemini · Grok · Perplexity + meta-reviewer)",
    "Persistence tracker fingerprinting findings across fires; load-bearing items escalate to Houston decision package",
    "Site + SSOT + Convex sync on every paper version bump",
  ],
  needsHouston: [
    {
      title: "Anthropic API credits exhausted (reviewer leg down)",
      blockedPaper: "all",
      why: "The Claude API reviewer leg is still down on billing 400s; R23conf ran its Claude leg in-session on subscription as a workaround, but the autoloop needs API credits for R24conf.",
      ask: "Top up API credits at console.anthropic.com → Plans & Billing, then say 'credits topped up' so full 5-vendor rounds restart.",
    },
    {
      title: "External review round on current versions",
      blockedPaper: "all",
      why: "The agent-side review loop has run; the orthogonal external pass is Houston's per his 2026-06-08 plan.",
      ask: "Run your external round on the current PDFs and send back findings for truth-audit.",
    },
    {
      title: "Personal sign-off, paper by paper",
      blockedPaper: "all",
      why: "The final 1% of readiness is reserved for Houston's judgment — no agent can award it.",
      ask: "Read each paper end-to-end and reply 'sign off PN' or send blocking findings.",
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
      version: "v1A.0.51",
      readiness: 92,
      pendingWork: "v1A.0.51 — R23conf cleanest round (E:0/M:0) closed → R24conf on v1A.0.51 must come back clean → Houston external round + sign-off → arXiv",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.52",
      readiness: 90,
      pendingWork: "v1B.0.52 — R23conf closed (§VI ALP provenance rewrite to committed-chain truth + c10 battery) → R24conf must come back clean → sign-off → arXiv (with P1A)",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.46",
      readiness: 92,
      pendingWork: "v1.7.46 — R23conf closed (methods paragraph repaired, Table III rebuilt from c9g, null-space scatter propagated) → R24conf must come back clean → Houston sign-off → arXiv",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.81",
      readiness: 90,
      pendingWork: "v3.1.81 — R23conf closed (abstract 7.9%→9.4%, 4 figure contradictions, gold/silver tiers 1,122) → R24conf must come back clean → HF flip → arXiv",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.168",
      readiness: 85,
      pendingWork: "v1.0.168 — R23conf closed (headline null regenerated from fixed generator: 0.41σ, p=0.31) → TWO clean R24conf+ rounds (post-retraction rule) → sign-off → arXiv (first in queue)",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.53-2026-06-09",
      readiness: 90,
      pendingWork: "v0.1.53 — R23conf closed (Bonferroni fix, count ledger unified 783,820 unique, χ²=3.00 p=0.39) → R24conf must come back clean → arXiv (last, after P4)",
    },
  ],
  blockerTally: {
    closed: 567, // 367 through the 2026-06-09 closure waves + ~200 R23conf findings truth-audited and closed
    openBlockers: 0,
    openMajors: 0,
    openMinors: 0,
  },
  cronStatus: "autonomous review loop active — hourly fires",
  etaToCompletion:
    "All six papers targeted publishable ~June 12–13, 2026 (per SSOT/PUBLISH_PLAN.md). Gated on Houston external round + sign-off; the final 1% is Houston-only.",
  pods: [],
};
