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
  lastUpdatedISO: "2026-06-14T00:45:00Z",
  lastUpdatedDisplay: "June 13, 2026 · 5:45 PM PT",
  headline:
    "EXT11 = 10/18 ACCEPT · Grok unanimous 6/6 · P4 first universal 3/3 across all providers. EXT11-closure-wave addressed all residuals. EXT12 submitted — expected 18/18 ACCEPT loop terminator.",
  summary:
    "EXT11: 10/18 ACCEPT (Grok 6/6, P4 3/3 universal, ChatGPT 1/6, Gemini 3/6). EXT11-closure lands: P1A v1A.0.74 / P1B v1B.0.71 / P2 v1.7.65 / P3 v3.1.108 / P4 v1.0.188 / P5 v0.1.77. P5 Figs 2/3/9 regenerated from generation scripts (T-Web plot titles fixed). P1A Eq.15 ChatGPT misread vindicated (false-positive; source correct). EXT12 18-chat delta-prompts submitted.",
  currentlyRunning: [
    "Hourly native-PDF cross-vendor review autoloop on all 6 papers (Claude · GPT · Gemini · Grok · Perplexity + meta-reviewer)",
    "Persistence tracker fingerprinting findings across fires; load-bearing items escalate to Houston decision package",
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
      version: "v1A.0.74",
      readiness: 95,
      pendingWork: "v1A.0.74 — EXT11-closure: Eq.15 inv-denom rewrite + αW⁵ sphaleron wording + App C softened; EXT12 submitted — Eq.15 ChatGPT misread vindicated (false-positive)",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.71",
      readiness: 94,
      pendingWork: "v1B.0.71 — EXT11-closure: release-pairing desc aligned to c15.input.yaml names; audit labels (E3/E4)(E8) stripped from journal prose; EXT12 submitted",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.65",
      readiness: 94,
      pendingWork: "v1.7.65 — EXT11-closure: r=0.84 canonical central confirmed; r=0.75 labeled r_{16th}; BF delta-prior vs bounce-prior rows disentangled; EXT12 submitted",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.108",
      readiness: 95,
      pendingWork: "v3.1.108 — EXT11-closure: abstract scope corrected (4 of 6 surveys pass 5σ gate); eROSITA/Gaia flagged exploratory; Table IX BF clarified; EXT12 submitted",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.188",
      readiness: 95,
      pendingWork: "v1.0.188 — EXT11=3/3 ACCEPT (first universal ACCEPT); EXT11-closure: Shamir [2] title+DOI+arXiv verified; (B1) stripped; EXT12 submitted",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.77-2026-06-13",
      readiness: 95,
      pendingWork: "v0.1.77 — EXT11-closure: Figs 2/3/9 regenerated (T-Web plot titles); §IX C T-Web ambiguity resolved; Table I MS=pdftotext artifact vindicated; EXT12 submitted",
    },
  ],
  blockerTally: {
    closed: 834, // +16 EXT11-closure wave — all residuals from EXT11_BATCH_TRUTH_AUDIT.md closed (P1A:5 + P1B:2 + P2:2 + P3:2 + P4:1 + P5:4 VERIFIED findings)
    openBlockers: 0,
    openMajors: 0,
    openMinors: 0,
  },
  cronStatus: "EXT12 submitted (18/18 chats) — harvest pending ≥30 min from submission",
  etaToCompletion:
    "EXT11=10/18 ACCEPT (Grok 6/6, P4 3/3 universal). EXT11-closure-wave: all residuals closed, figures regenerated. EXT12 expected 18/18 ACCEPT loop terminator. HIGH confidence.",
  pods: [],
};
