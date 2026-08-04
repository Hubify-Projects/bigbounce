// Per-paper PUBLICATION-READINESS breakdown — directive P (Houston 2026-07-23).
//
// The headline % is composed ONLY of the five gates below (weights in
// parentheses). Venue/submission/endorsement and independent human peer
// review are the NEXT PHASE ("Publishing") — tracked separately, never
// subtracted from readiness. A selected standalone manuscript with all four
// agent gates complete sits at 95; Houston's explicit per-paper sign-off is
// the final 5 → 100. P3 retains a 95 technical-package evidence record, but
// it is an integrated supporting release rather than an approval target.
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
  "Selected standalone manuscripts have final-hash confirmation evidence, with uneven provider coverage recorded in the review packets. " +
  "P3's 95% is technical-package evidence only: it is an integrated support release for the rebuilt DESI anomaly flagship, not a Houston approval target or standalone submission. " +
  "For the selected standalone manuscripts, the last 5% is Houston's final personal review; approval moves that manuscript to 100% and then into the separate Publishing phase (endorsement → submission → journal/human review).";

function gates(convergenceNote: string, finalReviewStatus?: string): ReadinessGate[] {
  return [
    { dimension: "Science closure", weight: 25, score: 100, owner: "done", status: "0 genuinely-new-real findings outstanding; compute campaigns complete; disclosed scope limits are in-paper, not open work." },
    { dimension: "Evidence & reproducibility", weight: 25, score: 100, owner: "done", status: "Published Zenodo DOI, commit-bound artifacts, public datasets/models, deterministic rebuild proofs." },
    { dimension: "Automated review convergence", weight: 25, score: 100, owner: "done", status: convergenceNote },
    { dimension: "Packaging & PDF hygiene", weight: 20, score: 100, owner: "done", status: "Commit-bound arXiv tarball standalone-compiles clean; directive-G mirrors byte-identical; submission kit paste-ready." },
    { dimension: "Houston final personal review", weight: 5, score: 0, owner: "houston", status: finalReviewStatus ?? "The last 5%: read the paper, flag anything visual/formatting/wording — or mark it good and this paper is 100% publication-ready." },
  ];
}

export const publishingPhase: PublishingStep[] = [
  { step: "arXiv endorsement", owner: "houston", status: "Codes issued + emailed 2026-07-22 (gr-qc HYEJ7S; astro-ph.IM L8TIPN; astro-ph.CO LRZHC4; astro-ph.GA CLVMAQ). One qualified endorser clears the astro-ph trio; shortlist verified on /publish." },
  { step: "Submission clicks", owner: "houston", status: "Selected manuscript order: P2 → P1A → P4 → P1B → P5 after final author approval and venue-specific checks. P3 remains attached support for the rebuilt anomaly flagship, not a standalone submission." },
  { step: "P5 Paper-IV back-patch", owner: "agent", status: "Automatic the moment P4 has an arXiv ID." },
  { step: "Journal / independent human review", owner: "external", status: "Begins when the papers are public — it is what publishing buys, not a precondition for it." },
];

export const readinessBreakdown: PaperBreakdown[] = [
  { code: "P1A", publicationReadiness: 95, gates: gates("Current v1A.0.127 final-hash audit: no genuinely-new-real finding; usable provider coverage is recorded in the review packet.") },
  { code: "P1B", publicationReadiness: 95, gates: gates("Current v2B.0.16 final-hash audit: no genuinely-new-real finding; usable provider coverage is recorded in the review packet.") },
  { code: "P2", publicationReadiness: 95, gates: gates("Current v1.7.130 final-hash audit: no genuinely-new-real finding; usable provider coverage is recorded in the review packet.") },
  { code: "P3", publicationReadiness: 95, gates: gates("Current r17 package audit preserves technical provenance evidence; this is not a standalone-science or flagship claim.", "Not applicable: P3 is an integrated supporting data/provenance release. Its 95% is technical-package evidence, not a Houston sign-off gate and cannot become a standalone submission score.") },
  { code: "P4", publicationReadiness: 95, gates: gates("Current v1.0.274 final-hash audit: the v1.0.273 editorial finding was closed; provider coverage is recorded in the review packet.") },
  { code: "P5", publicationReadiness: 95, gates: gates("Current v0.1.147 final-hash audit: no genuinely-new-real finding; usable provider coverage is recorded in the review packet.") },
];
