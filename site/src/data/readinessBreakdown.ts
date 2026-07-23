// Per-paper readiness BREAKDOWN — Houston's 2026-07-23 request: separate the
// mushy footnote language into named, scored dimensions so it is obvious per
// paper WHAT kind of work remains and WHO owns it. The single headline
// "publication readiness" number stays the canonical evidence-capped score
// (papers.ts / Convex readinessCap) — this file explains its composition; it
// never uplifts it.
//
// owner semantics:
//   agent    — executable by the loop right now or automatically on a trigger
//   houston  — needs a human decision, outreach, or click only Houston can do
//   external — depends on people outside the project (endorsers, referees)

export type GateOwner = "agent" | "houston" | "external" | "done";

export interface ReadinessGate {
  dimension: string;
  /** 0-100, honest, never aspirational */
  score: number;
  owner: GateOwner;
  status: string;
}

export interface PaperBreakdown {
  code: string;
  /** the canonical headline number (evidence cap) — mirrors papers.ts */
  publicationReadiness: number;
  gates: ReadinessGate[];
}

const COMMON_NOTE =
  "Science/evidence/packaging are agent-complete on every paper — no open gate " +
  "anywhere needs new math, new compute, new GPU/CPU runs, or new data. Every " +
  "remaining blocker is administrative or human: arXiv endorsement (Houston " +
  "outreach), submission clicks (Houston), and independent human peer review " +
  "(external — it BEGINS at submission; it cannot be completed before it).";

export const readinessBreakdownNote = COMMON_NOTE;

function gates(
  reviewNote: string,
  venueScore: number,
  venueOwner: GateOwner,
  venueNote: string,
): ReadinessGate[] {
  return [
    {
      dimension: "Science closure",
      score: 100,
      owner: "done",
      status:
        "0 genuinely-new-real findings outstanding; compute campaigns complete; disclosed scope limits are in-paper, not open work.",
    },
    {
      dimension: "Evidence & reproducibility",
      score: 100,
      owner: "done",
      status:
        "Published Zenodo DOI, commit-bound artifacts, public datasets/models, deterministic rebuild proofs.",
    },
    {
      dimension: "Automated review convergence",
      score: 90,
      owner: "agent",
      status: reviewNote,
    },
    {
      dimension: "Packaging & PDF hygiene",
      score: 100,
      owner: "done",
      status:
        "Commit-bound arXiv tarball standalone-compiles clean; directive-G mirrors byte-identical; submission kit paste-ready.",
    },
    {
      dimension: "Venue / submission",
      score: venueScore,
      owner: venueOwner,
      status: venueNote,
    },
    {
      dimension: "Independent human review",
      score: 0,
      owner: "external",
      status:
        "Starts when the paper is public (arXiv/journal). Not a pre-submission blocker — it is what submission buys.",
    },
  ];
}

const REVIEW_NOTE =
  "18-leg 2026-07-22 confirmation wave truth-audited to 0 genuinely-new-real; the same-day closure version awaits one routine re-sweep.";

const ENDORSE =
  "Blocked on arXiv endorsement (codes issued + emailed 2026-07-22; one qualified endorser clears it). Journal route open in parallel.";

export const readinessBreakdown: PaperBreakdown[] = [
  { code: "P1A", publicationReadiness: 62, gates: gates(REVIEW_NOTE, 20, "houston", ENDORSE + " Category: gr-qc (code HYEJ7S).") },
  { code: "P1B", publicationReadiness: 56, gates: gates(REVIEW_NOTE, 20, "houston", ENDORSE + " Category: astro-ph.IM (code L8TIPN). JORS journal route has no content blocker.") },
  { code: "P2", publicationReadiness: 80, gates: gates(REVIEW_NOTE, 20, "houston", ENDORSE + " Category: astro-ph.CO (code LRZHC4).") },
  { code: "P3", publicationReadiness: 56, gates: gates(REVIEW_NOTE, 20, "houston", ENDORSE + " Category: astro-ph.IM (code L8TIPN). ApJS route needs one abstract trim (agent, on go).") },
  { code: "P4", publicationReadiness: 80, gates: gates(REVIEW_NOTE, 20, "houston", ENDORSE + " Category: astro-ph.GA (code CLVMAQ).") },
  { code: "P5", publicationReadiness: 74, gates: gates(REVIEW_NOTE, 15, "agent", ENDORSE + " Category: astro-ph.GA (code CLVMAQ). Additionally waits on P4's arXiv ID back-patch — automatic (agent) the moment P4 submits.") },
];
