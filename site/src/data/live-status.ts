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
  lastUpdatedISO: "2026-06-26T12:00:00Z",
  lastUpdatedDisplay: "June 26, 2026 · 12:00 PM PT",
  headline:
    "EXT22 confirm round complete: 18/18 legs MINOR or ACCEPT, 0 MAJORs/BLOCKERs — polish-tier convergence reached. 2 edits closed (P1A §XII.B closure-mechanism alignment + P4 σ rounding). Readiness 97→98. Houston sign-off is the final gate.",
  summary:
    "Three-pass review (INT R52 + EXT21 + EXT22) closed with 0 MAJORs/BLOCKERs across all 6 papers. EXT22 surfaces only 2 verified polish edits (P1A NV-P1A-1 MINOR: §XII.B attribution corrected to amplitude suppression; P4 NV-P4-1 POLISH: +3.3σ→+3.29σ consistency fix). Both edits applied, both papers recompiled clean (P1A 29pp md5 06c3b525 · P4 23pp md5 f2902399). Readiness advances 97→98 (D-round convergence). Final gate: Houston sign-off → ORCID flip → arXiv drop (P4 → P1A → P1B → P3 → P2 → P5).",
  currentlyRunning: [
    "EXT22 COMPLETE — 18/18 legs MINOR or ACCEPT, 0 MAJORs/BLOCKERs. Polish-tier convergence reached. Readiness 97→98.",
    "Awaiting Houston sign-off + ORCID flip → arXiv drop.",
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
      readiness: 98,
      pendingWork: "EXT22 CLOSED (NV-P1A-1 §XII.B closure-mechanism edit applied, recompiled md5 06c3b525). Next: Houston sign-off → arXiv drop.",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.76",
      readiness: 98,
      pendingWork: "EXT22 CLEAN (0 new verified). 3 HF datasets public (bamfai/p1b-*). Next: Houston sign-off → arXiv drop.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.71",
      readiness: 98,
      pendingWork: "EXT22 CLEAN (0 new verified). Next: Houston sign-off → arXiv drop.",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.113",
      readiness: 98,
      pendingWork: "EXT22 CLEAN (0 new verified). Next: Houston sign-off + HF catalog flip → arXiv drop.",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.188",
      readiness: 98,
      pendingWork: "EXT22 CLOSED (NV-P4-1 +3.3σ→+3.29σ applied, recompiled md5 f2902399). Next: Houston sign-off → arXiv drop (first in queue).",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.83-2026-06-19",
      readiness: 98,
      pendingWork: "EXT22 CLEAN (0 new verified). Next: Houston sign-off → arXiv drop (last in queue; needs P4 arXiv ID).",
    },
  ],
  blockerTally: {
    closed: 872, // EXT22 closure: NV-P1A-1 (MINOR §XII.B) + NV-P4-1 (POLISH σ rounding); 0 open across 3-pass portfolio review
    openBlockers: 0,
    openMajors: 0,
    openMinors: 0,
  },
  cronStatus: "EXT22 COMPLETE (2026-06-26). Polish-tier convergence: 0 MAJORs/BLOCKERs across 3 passes. All 6 papers at readiness 98. Next gate: Houston sign-off.",
  etaToCompletion:
    "EXT22 DONE — all 6 papers at readiness 98. Remaining: Houston sign-off + ORCID flip → arXiv drop (order P4 → P1A → P1B → P3 → P2 → P5).",
  pods: [],
};
