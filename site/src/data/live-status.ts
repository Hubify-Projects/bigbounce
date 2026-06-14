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
  lastUpdatedISO: "2026-06-13T23:59:00Z",
  lastUpdatedDisplay: "June 13, 2026 · 11:59 PM PT",
  headline:
    "EXT16-closure sync complete: P1A v1A.0.77 · P2 v1.7.68 · P3 v3.1.111 · P5 v0.1.80 (P1B+P4 FROZEN universal 3/3 ACCEPT). Pattern-060 encoded (\\mbox{-} math subscript escape extends 057/059). EXT17 launched — 18 chats submitted. Target: 18/18 ACCEPT → arXiv coordinated drop.",
  summary:
    "EXT16-closure: P1A v1A.0.77 (Sec XII.A C/P-violating thermal-scattering propagation miss) · P2 v1.7.68 (CDF-tail 'reduces→raises' Sec VI.C direction) · P3 v3.1.111 (Table IX prior density footnote per-row denominator) · P5 v0.1.80 (V\\mbox{-}Web→T\\mbox{-}Web l.2864 + nomenclature + dup T-Web; pattern-060 first catch). P1B v1B.0.72 + P4 v1.0.188 FROZEN — universal 3/3 ACCEPT confirmed 4 consecutive rounds. EXT17: 18 chats submitted — ChatGPT in-thread delta × 6 + Grok in-thread delta × 6 + Gemini fresh chats pattern-058 MNRAS first-line × 6. P1B+P4 courtesy re-confirmation. HIGH CONFIDENCE 18/18 ACCEPT.",
  currentlyRunning: [
    "EXT17 harvesting — 18 chats submitted: ChatGPT 6 in-thread · Grok 6 in-thread · Gemini 6 fresh chats (pattern-058 MNRAS first-line). P1B+P4 courtesy re-confirmation prompts included.",
    "EXT16-closure post-bump full sync: mirrors + tarballs + Convex + SSOT + pattern-060 encoded",
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
      version: "v1A.0.77",
      readiness: 95,
      pendingWork: "v1A.0.77 — EXT16-closure: Sec XII.A C/P-violating thermal-scattering propagation miss fixed. EXT17 submitted. Awaiting harvest.",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.72",
      readiness: 95,
      pendingWork: "v1B.0.72 FROZEN — universal 3/3 ACCEPT confirmed EXT14+EXT16 (3 consecutive rounds). EXT17 courtesy re-confirmation. Queue for arXiv submission.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.68",
      readiness: 95,
      pendingWork: "v1.7.68 — EXT16-closure: CDF-tail direction 'reduces→raises' in Sec VI.C corrected. EXT17 submitted. Awaiting harvest.",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.111",
      readiness: 95,
      pendingWork: "v3.1.111 — EXT16-closure: Table IX prior density footnote per-row denominator clarified. EXT17 submitted. Awaiting harvest.",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.188",
      readiness: 95,
      pendingWork: "v1.0.188 FROZEN — universal 3/3 ACCEPT confirmed EXT12+EXT14+EXT16 (4 consecutive rounds). EXT17 courtesy re-confirmation. Queue for arXiv submission (first in order).",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.80-2026-06-13",
      readiness: 95,
      pendingWork: "v0.1.80 — EXT16-closure: V\\mbox{-}Web→T\\mbox{-}Web l.2864 (pattern-060 first catch) + nomenclature + dup T-Web. EXT17 submitted. Awaiting harvest.",
    },
  ],
  blockerTally: {
    closed: 860, // +4 EXT16-closure wave — P1A:1 + P2:1 + P3:1 + P5:1 VERIFIED findings closed (P1B+P4 frozen universal ACCEPT 4 rounds)
    openBlockers: 0,
    openMajors: 0,
    openMinors: 0,
  },
  cronStatus: "EXT16-closure-sync COMPLETE: 4 papers bumped (P1B+P4 frozen 4× universal ACCEPT) · pattern-060 encoded · EXT17 LAUNCHED: 18 chats submitted",
  etaToCompletion:
    "EXT17 in flight: 18 chats submitted (ChatGPT in-thread · Grok in-thread · Gemini fresh-chat pattern-058 MNRAS first-line; P1B+P4 courtesy re-confirmation). Harvest ETA ≥30 min from last submission. Target: 18/18 ACCEPT → arXiv coordinated drop. Confidence: HIGH.",
  pods: [],
};
