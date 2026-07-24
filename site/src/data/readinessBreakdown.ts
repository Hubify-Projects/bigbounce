// Per-paper PUBLICATION-READINESS breakdown — directive P (Houston 2026-07-23).
//
// The headline % is composed ONLY of the five gates below (weights in
// parentheses). Venue/submission/endorsement and independent human peer
// review are the NEXT PHASE ("Publishing") — tracked separately, never
// subtracted from readiness. A paper with all four agent gates complete sits
// at 95; Houston's explicit per-paper sign-off is the final 5 → 100.
//
// Convergence criterion (directive M-AMENDED + H-refined): 0 genuinely-new-real
// findings outstanding across ACTIVE legs (Grok API, Gemini API, Claude INT;
// paused legs excluded) on the current exact PDFs. Verdict words are feedback,
// never the gate.

export type GateOwner = "agent" | "houston" | "external" | "done";

export interface ReadinessGate {
  dimension: string;
  weight: number;
  /** 0-100 within the gate */
  score: number;
  owner: GateOwner;
  status: string;
}

export interface PublishingStep {
  step: string;
  owner: GateOwner;
  status: string;
}

export interface PaperBreakdown {
  code: string;
  /** headline publication readiness, directive-P composition */
  publicationReadiness: number;
  gates: ReadinessGate[];
}

export const readinessBreakdownNote =
  "Directive P (2026-07-23): publication readiness = the five gates below only. " +
  "No gate on any paper needs new math, compute, GPU/CPU runs, or data — the " +
  "four agent gates are complete on all six papers, so every paper sits at 95%. " +
  "The last 5% is Houston's final personal review, per paper: mark it good and " +
  "that paper is 100% ready and moves to the Publishing phase (endorsement → " +
  "submission → journal/human review), which is tracked below but never " +
  "subtracts from readiness.";

const RESWEEP =
  "2026-07-23 re-sweep (18 exact-PDF legs, active legs per directive M-AMENDED) truth-audited to 0 genuinely-new-real outstanding — the one real item (version-stamp drift) closed same-day, drift-proofed via the \\paperVersion macro.";

function gates(convergenceNote: string): ReadinessGate[] {
  return [
    { dimension: "Science closure", weight: 25, score: 100, owner: "done", status: "0 genuinely-new-real findings outstanding; compute campaigns complete; disclosed scope limits are in-paper, not open work." },
    { dimension: "Evidence & reproducibility", weight: 25, score: 100, owner: "done", status: "Published Zenodo DOI, commit-bound artifacts, public datasets/models, deterministic rebuild proofs." },
    { dimension: "Automated review convergence", weight: 25, score: 100, owner: "done", status: convergenceNote },
    { dimension: "Packaging & PDF hygiene", weight: 20, score: 100, owner: "done", status: "Commit-bound arXiv tarball standalone-compiles clean; directive-G mirrors byte-identical; submission kit paste-ready." },
    { dimension: "Houston final personal review", weight: 5, score: 0, owner: "houston", status: "The last 5%: read the paper, flag anything visual/formatting/wording — or mark it good and this paper is 100% publication-ready." },
  ];
}

export const publishingPhase: PublishingStep[] = [
  { step: "arXiv endorsement", owner: "houston", status: "Codes issued + emailed 2026-07-22 (gr-qc HYEJ7S; astro-ph.IM L8TIPN; astro-ph.CO LRZHC4; astro-ph.GA CLVMAQ). One qualified endorser clears the astro-ph trio; shortlist verified on /publish." },
  { step: "Submission clicks", owner: "houston", status: "Wave 1 (P1B → P1A → P3), wave 2 (P2 + P4), then P5 after the automatic Paper-IV back-patch. Draft 7859751 parked at Start, ready." },
  { step: "P5 Paper-IV back-patch", owner: "agent", status: "Automatic the moment P4 has an arXiv ID." },
  { step: "Journal / independent human review", owner: "external", status: "Begins when the papers are public — it is what publishing buys, not a precondition for it." },
];

export const readinessBreakdown: PaperBreakdown[] = [
  { code: "P1A", publicationReadiness: 95, gates: gates("2026-07-23 re-sweep: Grok ACCEPT · Gemini minor (dispositioned) · Claude ACCEPT, zero findings. " + RESWEEP) },
  { code: "P1B", publicationReadiness: 95, gates: gates("2026-07-23 re-sweep: Claude ACCEPT with zero findings; Grok/Gemini minors dispositioned (re-flags of deliberate honesty disclosures). " + RESWEEP) },
  { code: "P2", publicationReadiness: 95, gates: gates("2026-07-23 re-sweep: Grok ACCEPT — its first on P2. Stamp-drift closed in v1.7.128. " + RESWEEP) },
  { code: "P3", publicationReadiness: 95, gates: gates("2026-07-23 re-sweep: Grok ACCEPT. Stamp-drift closed in v3.2.0-r13. " + RESWEEP) },
  { code: "P4", publicationReadiness: 95, gates: gates("2026-07-23 re-sweep: all-minor board; re-flags falsified with citations (DOI renders 3×). Stamp-drift closed in v1.0.271. " + RESWEEP) },
  { code: "P5", publicationReadiness: 95, gates: gates("2026-07-23 re-sweep: Gemini MAJORs = the tracked Paper-IV/DOI gates + a disclosed limitation (audited, non-real); Hamaus re-flag falsified twice (cite at tex:2943). " + RESWEEP) },
];
