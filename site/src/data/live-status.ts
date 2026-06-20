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
  lastUpdatedISO: "2026-06-20T12:00:00Z",
  lastUpdatedDisplay: "June 20, 2026 · 12:00 PM PT",
  headline:
    "R→D→P all complete; readiness 99 (P1B 98 pending its HF datasets going public); final 1% = Houston sign-off.",
  summary:
    "P-round (packaging) complete: all 6 tarballs standalone-verified (0 errors / 0 undef refs), site surfaces cohesive, public HF artifacts linked. Next gate: Houston sign-off (P1B also awaits HF datasets flip) → ORCID flip → arXiv drop (P4 → P1A → P1B → P3 → P2 → P5).",
  currentlyRunning: [
    "P-round COMPLETE — tarballs standalone-verified, site cohesive, HF artifacts linked.",
    "arXiv drop waits on Houston sign-off + ORCID flip (P1B also awaits HF datasets flip).",
  ],
  needsHouston: [
    {
      title: "ORCID public flip (only hard blocker)",
      blockedPaper: "all",
      why: "arXiv submission requires the author ORCID 0009-0008-3617-8729 to resolve publicly; pub.orcid.org currently returns 404, not 200.",
      ask: "At orcid.org set Names/Employment/Education to PUBLIC, then confirm `curl -s -o /dev/null -w '%{http_code}' https://pub.orcid.org/v3.0/0009-0008-3617-8729/person` returns 200.",
    },
    {
      title: "Resolve P5 title galaxy count",
      blockedPaper: "P5",
      why: "P5 title shows '791,635 DR1 Matched Spirals' vs the environment-matched '783,820' — a one-line Houston decision before P5's tarball is final.",
      ask: "Confirm the headline count (recommend 783,820 environment-matched); P5 tarball rebuilds in one command if changed.",
    },
    {
      title: "Authorize the coordinated arXiv drop",
      blockedPaper: "all",
      why: "Only Houston holds the arXiv account + astro-ph endorser relationships; all six tarballs are staged and drop-ready.",
      ask: "Give the go and submit in order P4 → P1A → P1B → P3 → P2 → P5 (P4 first; P5 needs P4's arXiv ID).",
    },
  ],
  papers: [
    {
      slug: "paper-1a",
      number: "1A",
      shortTitle: "ECH dark-energy closure + perturbation transparency",
      version: "v1A.0.79",
      readiness: 99,
      pendingWork: "P-round COMPLETE. Next: Houston sign-off → arXiv drop.",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.75",
      readiness: 98,
      pendingWork: "P-round COMPLETE. Next: HF chains flip (Houston) + sign-off → arXiv drop same-day as P1A.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.71",
      readiness: 99,
      pendingWork: "P-round COMPLETE. Next: Houston sign-off → arXiv drop.",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.113",
      readiness: 99,
      pendingWork: "P-round COMPLETE. Next: Houston sign-off + HF catalog flip → arXiv drop.",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.188",
      readiness: 99,
      pendingWork: "P-round COMPLETE (FROZEN v1.0.188). Next: Houston sign-off → arXiv drop (first in queue).",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.83-2026-06-19",
      readiness: 99,
      pendingWork: "P-round COMPLETE. Next: Houston sign-off → arXiv drop (last in queue; needs P4 arXiv ID).",
    },
  ],
  blockerTally: {
    closed: 864, // EXT17 closure wave — P1A + P2 + P3 + P5 EXT16-MINORs resolved to ACCEPT; P1B + P4 frozen universal ACCEPT
    openBlockers: 0,
    openMajors: 0,
    openMinors: 0,
  },
  cronStatus: "P-ROUND COMPLETE (2026-06-20). Tarballs standalone-verified, site cohesive, HF artifacts linked. Readiness 99 (P1B 98). Final gate: Houston sign-off.",
  etaToCompletion:
    "P-round DONE — readiness 99 (P1B 98). Remaining: Houston sign-off + ORCID flip + P1B HF chains flip → arXiv drop (order P4 → P1A → P1B → P3 → P2 → P5).",
  pods: [],
};
