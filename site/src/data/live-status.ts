// Live build status surfaced at the top of every page. This is a concise
// display model; the review timeline and Convex remain the detailed record.

export interface PaperProgress {
  slug: string;
  number: string;
  shortTitle: string;
  version: string;
  readiness: number;
  pendingWork: string;
}

export interface NeedsHoustonItem {
  title: string;
  why: string;
  blockedPaper?: string;
  ask: string;
}

export interface LiveStatus {
  lastUpdatedISO: string;
  lastUpdatedDisplay: string;
  headline: string;
  summary: string;
  currentlyRunning: string[];
  needsHouston: NeedsHoustonItem[];
  papers: PaperProgress[];
  blockerTally: {
    closed: number;
    openBlockers: number;
    openMajors: number;
    openMinors: number;
  };
  cronStatus: string;
  etaToCompletion: string;
  pods: Array<{
    name: string;
    state: "active" | "idle" | "queued";
    note: string;
  }>;
}

export const liveStatus: LiveStatus = {
  lastUpdatedISO: "2026-08-03T21:30:00Z",
  lastUpdatedDisplay: "August 3, 2026 · 2:30 PM PT",
  headline:
    "All six manuscripts remain IN REVISION at 95% publication readiness under Directive P. That score records completed evidence, packaging, and review-disposition work; it is not submission, journal acceptance, or Houston sign-off.",
  summary:
    "The July 24 directive-G bundles set the current served versions below. Earlier exact-PDF evidence is version-specific; final-hash bounded confirmation remains an explicit coverage check where it has not yet read the current artifact.",
  currentlyRunning: [
    "Bounded confirmation coverage is tracked against the exact current PDF; no older review label is presented as a verdict on a newer hash.",
    "Houston's final per-paper review is the remaining five readiness points and is not implied by an automated review result.",
    "Publishing is a separate phase: endorsement, submission clicks, and independent human review do not convert a 95% paper into 100% automatically.",
  ],
  needsHouston: [
    {
      title: "Final personal review",
      why: "Directive P reserves the final five percentage points for Houston's per-paper review.",
      ask: "Review each current PDF and record sign-off only when personally satisfied.",
    },
    {
      title: "arXiv endorsement and submission",
      why: "Endorsement and submission actions belong to the separate publishing phase.",
      ask: "Complete the required endorsement and submission actions when the publication decision is made.",
    },
  ],
  papers: [
    {
      slug: "paper-1a",
      number: "1A",
      shortTitle: "ECH channel-level closure",
      version: "v1A.0.127",
      readiness: 95,
      pendingWork: "Current-hash bounded confirmation and Houston's CQG review remain distinct from prior review evidence.",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "NaMaster verification companion",
      version: "v2B.0.16",
      readiness: 95,
      pendingWork: "Current-hash bounded confirmation, correspondence metadata, and human software review remain open.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "Matter-contraction f_NL forecast",
      version: "v1.7.130",
      readiness: 95,
      pendingWork: "Current-hash bounded confirmation and Houston's PRD review remain open; the published archive is not journal acceptance.",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "DESI anomaly-list recovery",
      version: "v3.2.0-r14",
      readiness: 95,
      pendingWork: "One recorded minor and current-hash bounded confirmation remain under review; human ApJS review is separate.",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "Galaxy chirality null",
      version: "v1.0.272",
      readiness: 95,
      pendingWork: "Current-hash bounded confirmation, systematics metadata, and human ApJS review remain open.",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality",
      version: "v0.1.146-2026-07-24",
      readiness: 95,
      pendingWork: "Current-hash bounded confirmation and independent human review remain open; the limitations remain in the paper.",
    },
  ],
  blockerTally: {
    closed: 920,
    openBlockers: 0,
    openMajors: 0,
    openMinors: 1,
  },
  cronStatus:
    "No recorded open BLOCKER or MAJOR. P3 retains one recorded MINOR; current-hash confirmation and Houston review are tracked separately.",
  etaToCompletion:
    "No automated completion estimate: the remaining readiness points require Houston's personal review. Submission and journal review proceed on their own publishing timeline.",
  pods: [],
};
