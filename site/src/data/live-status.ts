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
    "Candidate-package evidence is recorded at 95% under Directive P. The portfolio is organized around three research programs; this score records evidence, packaging, and review disposition, not a decision to submit every package.",
  summary:
    "The exact candidate packages remain available as versioned evidence. P3 is the supporting DESI public-ID recovery release while its discovery-focused flagship is rebuilt; P5 is the selected standalone AJ chirality–environment companion.",
  currentlyRunning: [
    "Deterministic preflight, clean-room package compiles, link checks, mirror checks, and all-page visual audits pass; bounded reviewer confirmation remains version-specific.",
    "Houston's final review applies only after a program-level scientific and editorial decision; it is not implied by an automated review result.",
    "Publishing is a separate phase: endorsement, submission clicks, and independent human review do not convert a 95% paper into 100% automatically.",
  ],
  needsHouston: [
    {
      title: "Final visual and scientific review",
      why: "The portfolio roles are approved, but Houston's manuscript-by-manuscript sign-off remains the final five-point gate.",
      ask: "Review the selected standalone manuscripts in journal order and record approve, revise, or defer for each.",
    },
    {
      title: "arXiv endorsement and submission",
      why: "Endorsement and submission actions belong to the separate publishing phase after a specific manuscript is selected.",
      ask: "Complete the required endorsement and submission actions only for a selected submission target.",
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
      version: "v3.2.0-r17",
      readiness: 95,
      pendingWork: "Exact r17 bounded confirmation and integration review remain; the served package is supporting provenance for the anomaly flagship, not a standalone submission.",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "Galaxy chirality null",
      version: "v1.0.274",
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
