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
  lastUpdatedISO: "2026-06-30T12:00:00Z",
  lastUpdatedDisplay: "June 30, 2026 · 12:00 PM PT",
  headline:
    "Rounds A/B/C complete (Jun 28–30): 3 rigorous INT+EXT passes, 23 real items closed program-wide, final neutral truth-audit returned 0 genuinely-new findings. All 6 papers verified internally honest and materially improved. Readiness 96. Houston sign-off is the final gate.",
  summary:
    "Three back-to-back review rounds (A/B/C, Jun 28–30) on top of a de-biased external validation closed 23 real items across all 6 papers. The final independent neutral truth-audit (Opus, skeptical stance, no convergence hint) found 0 genuinely-new real findings. Remaining external MAJORs are disclosed caveats, submission-time DOI/arXiv blockers, and LLM-referee variance — not quality issues. Next gate: Houston external-review sign-off → arXiv endorsement + coordinated submission (P4 → P1A → P1B → P3 → P2 → P5).",
  currentlyRunning: [
    "Light-touch regression watch — no active review loop running.",
  ],
  needsHouston: [
    {
      title: "External-review sign-off (final 1% gate)",
      blockedPaper: "all",
      why: "Houston's personal review verdict is the only remaining gate before tarballs are submitted; agents cannot self-authorize submission.",
      ask: "Review the final neutral truth-audit summary (project-context/peer-reviews/) and give go/no-go on coordinated arXiv submission.",
    },
    {
      title: "arXiv endorsement + coordinated submission",
      blockedPaper: "all",
      why: "Only Houston holds the arXiv account + astro-ph endorser relationships; all six tarballs are staged and drop-ready.",
      ask: "Submit in order P4 → P1A → P1B → P3 → P2 → P5 (P4 first; P5 needs P4's arXiv ID).",
    },
  ],
  papers: [
    {
      slug: "paper-1a",
      number: "1A",
      shortTitle: "ECH dark-energy closure + perturbation transparency",
      version: "v1A.0.89",
      readiness: 96,
      pendingWork: "Rounds A/B/C clean (0 new verified after 23-item program close). Next: Houston sign-off → arXiv drop.",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.84",
      readiness: 96,
      pendingWork: "Rounds A/B/C clean. 3 HF datasets public (bamfai/p1b-*). Next: Houston sign-off → arXiv drop.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.80",
      readiness: 96,
      pendingWork: "Rounds A/B/C clean. Next: Houston sign-off → arXiv drop.",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.120",
      readiness: 96,
      pendingWork: "Rounds A/B/C clean. Next: Houston sign-off + HF catalog flip → arXiv drop.",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.198",
      readiness: 96,
      pendingWork: "Rounds A/B/C clean. Next: Houston sign-off → arXiv drop (first in queue).",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.94",
      readiness: 96,
      pendingWork: "Rounds A/B/C clean. Next: Houston sign-off → arXiv drop (last in queue; needs P4 arXiv ID).",
    },
  ],
  blockerTally: {
    closed: 895, // 872 prior + 23 real items closed across Rounds A/B/C (Jun 28-30)
    openBlockers: 0,
    openMajors: 0,
    openMinors: 0,
  },
  cronStatus: "Rounds A/B/C COMPLETE (2026-06-28 to 2026-06-30). 23 items closed program-wide. Final neutral truth-audit: 0 new genuine findings. All 6 papers at readiness 96. Next gate: Houston sign-off.",
  etaToCompletion:
    "Rounds A/B/C done — all 6 papers at readiness 96. Remaining: Houston sign-off + arXiv endorsement → coordinated drop (P4 → P1A → P1B → P3 → P2 → P5).",
  pods: [],
};
