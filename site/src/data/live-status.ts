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
  lastUpdatedISO: "2026-08-04T03:23:00Z",
  lastUpdatedDisplay: "August 3, 2026 · 8:23 PM PT",
  headline:
    "All six manuscripts remain IN REVISION at 95% publication readiness under Directive P. That score records completed evidence, packaging, and review-disposition work; it is not submission, journal acceptance, or Houston sign-off.",
  summary:
    "All six exact source packages and journal portal kits now exist. P3, P4, and P5 were migrated to the current AASTeX 7.0.2 journal shell and mirrored at the versions below; final-hash bounded confirmation is running against these served bytes before Houston's visual review.",
  currentlyRunning: [
    "Deterministic preflight, clean-room package compiles, link checks, mirror checks, and all-page visual audits pass; bounded reviewer confirmation remains version-specific.",
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
      version: "v3.2.0-r16",
      readiness: 95,
      pendingWork: "Exact r16 bounded confirmation and Houston's visual review remain; annular-null, r2 payload, and viewer-evidence defects from r15 are closed in the served candidate.",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "Galaxy chirality null",
      version: "v1.0.273",
      readiness: 95,
      pendingWork: "Current-hash bounded confirmation and Houston's visual review remain; the ApJS package is clean and line-numbered.",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality",
      version: "v0.1.147-2026-08-03",
      readiness: 95,
      pendingWork: "Current-hash bounded confirmation and Houston review remain; after sign-off, mint the immutable tag/Zenodo snapshot and back-patch identifiers.",
    },
  ],
  blockerTally: {
    closed: 920,
    openBlockers: 0,
    openMajors: 0,
    openMinors: 0,
  },
  cronStatus:
    "No autonomous review wave is running. No recorded open BLOCKER, MAJOR, or MINOR; bounded current-hash confirmation plus Houston review are tracked separately.",
  etaToCompletion:
    "No automated completion estimate: the remaining readiness points require Houston's personal review. Submission and journal review proceed on their own publishing timeline.",
  pods: [],
};
