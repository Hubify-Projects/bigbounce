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
  lastUpdatedISO: "2026-06-10T01:30:00Z",
  lastUpdatedDisplay: "June 9, 2026 · 6:30 PM PT",
  headline:
    "Provenance-audit day closed out: ~150+ findings closed across 5 closure waves. P4 v1.0.167 re-anchored on the real-space +0.43σ null + WLS template exclusion (the synthetic −0.122σ subsample null is withdrawn); P1B v1B.0.51 and P5 v0.1.52 review queues are EMPTY. All six papers at 85–92%.",
  summary:
    "Today's waves landed: P4 49 R-v166-c1 closures (2.98× corrected equivariance suppression, harmonic completeness anchor z≈68–218 vs +7.3); P1B w_pivot corrected to +2.5σ from −1 on the twice-verified DESI DR2 chain + NaMaster validation rescoped to synthetic ΛCDM skies; P2's withdrawn ~9.9σ SDB claim replaced by the committed-Fisher 1.4σ/0.6σ subordinate channel; P3 36+ closures incl. the descriptive eROSITA reframe; P5 duplicate-TARGETID join root-caused with omnibus χ² nulls (p=0.31/0.99) and covariate-robust Wald nulls (p=0.46/0.99).",
  currentlyRunning: [
    "Hourly native-PDF cross-vendor review autoloop on all 6 papers (Claude · GPT · Gemini · Grok · Perplexity + meta-reviewer)",
    "Persistence tracker fingerprinting findings across fires; load-bearing items escalate to Houston decision package",
    "Site + SSOT + Convex sync on every paper version bump",
  ],
  needsHouston: [
    {
      title: "Anthropic API credits exhausted (reviewer leg down)",
      blockedPaper: "all",
      why: "The Claude reviewer leg of every cross-vendor round has been failing with a billing 400 since ~1 PM PT; rounds are running 4-vendor (degraded).",
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
      version: "v1A.0.50",
      readiness: 92,
      pendingWork: "External round on v1A.0.50 → Houston sign-off → arXiv",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.51",
      readiness: 90,
      pendingWork: "v1B.0.51 — review queue EMPTY (c9f: sign-symmetric recovery, σ_β(0.32)=0.046° measured directly) → Claude-inclusive clean round → sign-off → arXiv (with P1A)",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.45",
      readiness: 92,
      pendingWork: "v1.7.45 R22prov2 mini-wave closed (Gemini/OpenAI/META zero findings; Claude leg failed on API credits — round DEGRADED, Claude-inclusive confirmation round needed post-top-up) → Houston sign-off → arXiv",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.80",
      readiness: 90,
      pendingWork: "v3.1.80 wave landed (36+ closures incl. measured dedup sweep 0.086%, eROSITA null reframe, Fig 12 regen) → Claude-inclusive clean round post-top-up → HF flip → arXiv",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.167",
      readiness: 85,
      pendingWork: "v1.0.167 wave landed (49 R-v166-c1 closures: clean abstract, 2.98× corrected suppression, Table II/III rebuilt) → two Claude-inclusive clean rounds → sign-off → arXiv (first in queue)",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.52-2026-06-09",
      readiness: 90,
      pendingWork: "v0.1.52 — review queue EMPTY (covariate regression closed: env null robust to size/mag/morphology/inclination, 100% GZ-DESI join) → Claude-inclusive clean round → arXiv (last, after P4)",
    },
  ],
  blockerTally: {
    closed: 367, // 217 pre-2026-06-09 + ~150 closed across today's 5 closure waves
    openBlockers: 0,
    openMajors: 0,
    openMinors: 0,
  },
  cronStatus: "autonomous review loop active — hourly fires",
  etaToCompletion:
    "All six papers targeted publishable ~June 12–13, 2026 (per SSOT/PUBLISH_PLAN.md). Gated on Houston external round + sign-off; the final 1% is Houston-only.",
  pods: [],
};
