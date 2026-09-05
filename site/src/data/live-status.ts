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
  lastUpdatedISO: "2026-09-02T20:00:00Z",
  lastUpdatedDisplay: "September 2, 2026",
  headline:
    "Portfolio restructured to Track A (bounce vs. inflation, flagship) / Track B (the ECH Note) / Track C (DESI data products), replacing the retired three-research-programs framing (directive R3). P1N and P4′ are freshly merged/folded drafts, not yet scored — P1A, P1C, P4, and P5 remain listed as their archived lineage.",
  summary:
    "P1N (Track B) merges P1A into P1C as one closed-line ECH Note. P4′ (Track C1) folds P5 into P4 and adds the Poplawski black-hole-universe spin-axis exclusion. Both are fresh drafts (readiness cap 20, no review board run yet). P2 remains gated toward P2′ pending the ledger #1 independent re-derivation. P3 is provenance support for the redirected early-universe anomaly map.",
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
      slug: "paper-1n",
      number: "1N",
      shortTitle: "The ECH Note (P1A + P1C merged, grown to CQG Paper form)",
      version: "v1N.0.5",
      readiness: 95,
      pendingWork: "REVISE (abstract cap) executed 2026-09-02 → v1N.0.5 (abstract trimmed to 298 words). R3 verification closed; automated review converged; final author review APPROVE; Houston sign-off (95→100) not yet sought.",
    },
    {
      slug: "paper-1a",
      number: "1A",
      shortTitle: "ECH channel-level closure (archived — see P1N)",
      version: "v1A.0.127",
      readiness: 95,
      pendingWork: "Archived lineage: merged into P1N (Track B ECH Note) 2026-09-02. Frozen on disk, not an independent submission target.",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "NaMaster verification companion",
      version: "v2B.0.23",
      readiness: 95,
      pendingWork: "All deferred text items from the v2B.0.20 R3 truth audit now closed (batch-3 commit-ordered audit trail, frozen rule-file sha256 digests, Table 1 third trust category). ROUNDS STOPPED under directive R2 — next: Zenodo corpus deposit + venue decision (Houston-gated).",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "Matter-contraction f_NL forecast (archived — see P2′)",
      version: "v1.7.130",
      readiness: 95,
      pendingWork: "Archived lineage: rescoped into P2′ (Track A A1 Letter) 2026-09-02 after ledger #1 closed. Unedited on disk, not an independent submission target.",
    },
    {
      slug: "paper-2l",
      number: "2L",
      shortTitle: "Exact f_NL Letter (archived theory record — folded into A3)",
      version: "v2L.0.2",
      readiness: 20,
      pendingWork: "R1 (Fable major / Grok reject / Gemini major) truth-audited; scope decision recorded — archived theory record, content folded into the A3 multi-channel paper.",
    },
    {
      slug: "paper-a3m",
      number: "A3",
      shortTitle: "Multi-channel consistency (Track A flagship submission candidate)",
      version: "v3M.0.22",
      readiness: 75,
      pendingWork: "S9b derivation-statement correction: the intrinsic flat-slice term vanishes in the growing-mode limit that defines -55/16, so it does not close the gap to -5/2 (residual 5(6-eps)/24); the residual now attributed to the super-Hubble evolution step between slices -- open item, not reconciled. Only the comoving-slice delta N (-5) is fully reconciled; flagship -35/16 unaffected. ROUNDS STOPPED (R2). Houston final review pending.",
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
      slug: "paper-4p",
      number: "4P",
      shortTitle: "Chirality test + black-hole-universe exclusion (P4 + P5 folded)",
      version: "v4P.0.7",
      readiness: 95,
      pendingWork: "Row-16 (iv-b) DESI DR1 BGS external environment result integrated 2026-09-05 → v4P.0.7 (genuine external tracer field, spec-z 3D N=121,417 + projected N=949,584, null; no science-conclusion change). R3 verification closed; automated review converged; final author review APPROVE; readiness 95. 100 requires Houston's explicit per-paper sign-off (directive P), which should read v4P.0.7.",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "Galaxy chirality null (archived — see P4′)",
      version: "v1.0.274",
      readiness: 95,
      pendingWork: "Archived lineage: folded into P4′ (Track C1) 2026-09-02. Frozen on disk, not an independent submission target.",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality (archived — see P4′)",
      version: "v0.1.147-2026-08-03",
      readiness: 95,
      pendingWork: "Archived lineage: folded into P4′ (Track C1) 2026-09-02. Frozen on disk, not an independent submission target.",
    },
    {
      slug: "paper-su",
      number: "SU",
      shortTitle: "Separate-universe failure criterion (short note)",
      version: "v1S.0.6",
      readiness: 65,
      pendingWork: "S9b: the intrinsic flat-slice term does not close the -55/16 gap (vanishes in the growing-mode limit); residual attributed to the super-Hubble evolution step between slices -- open item, not reconciled. ROUNDS STOPPED (R2) pending a science or venue decision.",
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
