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
  lastUpdatedISO: "2026-06-14T08:00:00Z",
  lastUpdatedDisplay: "June 13, 2026 · 11:00 PM PT",
  headline:
    "EXT13-closure-wave complete: 5 papers updated (P4 frozen at universal 3/3 ACCEPT). EXT14 launched — 18 chats submitted with Gemini pattern-058 fix (MNRAS referee-format first-line). Target: 18/18 ACCEPT → arXiv coordinated drop.",
  summary:
    "EXT13-closure: P1A v1A.0.75 (dim bookkeeping) · P1B v1B.0.72 (release-pairing harmonized) · P2 v1.7.66 (BF self-check 3-sentence rewrite) · P3 v3.1.109 (DESI gate explicit + Savage-Dickey tablenote) · P5 v0.1.78 (pattern-057 V-Web body residuals closed). P4 FROZEN at v1.0.188 — universal 3/3 ACCEPT (ChatGPT first-ever ACCEPT in campaign). EXT14: 18 chats submitted — Gemini fresh chats with pattern-058 verdict-format first-line applied. HIGH CONFIDENCE 18/18 ACCEPT.",
  currentlyRunning: [
    "EXT14 harvesting — 18 chats submitted across ChatGPT (in-thread delta) · Grok (in-thread delta) · Gemini (fresh chats, pattern-058 MNRAS first-line applied)",
    "Native-PDF cross-vendor review autoloop on all 6 papers (Claude · GPT · Gemini · Grok · Perplexity + meta-reviewer)",
    "Site + SSOT + Convex sync on every paper version bump",
  ],
  needsHouston: [
    {
      title: "Personal sign-off — all six papers at the post-EXT6 gate",
      blockedPaper: "all",
      why: "Six external browser-tier rounds complete; Grok 4× consecutive 6/6 ACCEPT; P1B fully cleared by Gemini; EXT6 truth-audits in progress; the final 1% is Houston-only.",
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
      version: "v1A.0.75",
      readiness: 95,
      pendingWork: "v1A.0.75 — EXT13-closure: Sec IV/App B dim bookkeeping + reheating residual clarified. EXT14 submitted with Gemini pattern-058 fix. Awaiting harvest (≥30 min).",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.72",
      readiness: 94,
      pendingWork: "v1B.0.72 — EXT13-closure: release-pairing harmonized Sec III+V.B+Conclusion (c15 yaml names; 0.04σ ΔNeff bound). EXT14 submitted. Awaiting harvest.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.66",
      readiness: 94,
      pendingWork: "v1.7.66 — EXT13-closure: BF self-check 3-sentence rewrite (delta-prior vs bounce-prior vs required equation disentangled). EXT14 submitted. Awaiting harvest.",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.109",
      readiness: 95,
      pendingWork: "v3.1.109 — EXT13-closure: abstract DESI gate type explicit + Table IX BF Savage-Dickey tablenote (8 sites). EXT14 submitted. Awaiting harvest.",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.188",
      readiness: 95,
      pendingWork: "v1.0.188 FROZEN — universal 3/3 ACCEPT at EXT12 (ChatGPT first-ever ACCEPT in campaign). EXT14 courtesy re-prompt only. Queue for arXiv submission.",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.78-2026-06-13",
      readiness: 95,
      pendingWork: "v0.1.78 — EXT13-closure: pattern-057 V-Web body residuals closed (4 sites) + Verdict.→Result. + Fig 8 clean. EXT14 submitted with Gemini pattern-058 fix. Awaiting harvest.",
    },
  ],
  blockerTally: {
    closed: 844, // +10 EXT13-closure wave — P1A:2 + P1B:2 + P2:2 + P3:2 + P5:4 VERIFIED findings closed (P4 frozen universal ACCEPT)
    openBlockers: 0,
    openMajors: 0,
    openMinors: 0,
  },
  cronStatus: "EXT13-closure-wave COMPLETE: 5 papers bumped (P4 frozen universal ACCEPT) · EXT14 LAUNCHED: 18 chats submitted · Gemini pattern-058 fix applied (MNRAS first-line)",
  etaToCompletion:
    "EXT14 in flight: 18 chats submitted (ChatGPT in-thread · Grok in-thread · Gemini fresh-chat with pattern-058 MNRAS verdict-format first-line). Harvest ETA ≥30 min from last submission. Target: 18/18 ACCEPT → arXiv coordinated drop. Confidence: HIGH.",
  pods: [],
};
