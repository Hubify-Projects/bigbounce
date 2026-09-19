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
  lastUpdatedISO: "2026-09-19T06:52:00Z",
  lastUpdatedDisplay: "September 18, 2026",
  headline:
    "Portfolio restructured to Track A (bounce vs. inflation, flagship) / Track B (the ECH Note) / Track C (DESI data products), replacing the retired three-research-programs framing (directive R3). The 2026-09-18 publication-push campaign closed P1N's D-round + P-round (95→99) and ran a fresh exact-version confirmation board on P4′ (→v4P.0.8, still 95) — P1A, P1C, P4, and P5 remain listed as their archived lineage.",
  summary:
    "P1N (Track B) merges P1A into P1C as one closed-line ECH Note; its D-round and P-round are now complete (readiness 99, Houston sign-off next). P4′ (Track C1) folds P5 into P4 and adds the Poplawski black-hole-universe spin-axis exclusion; an exact-version INT confirmation board closed 7 genuinely-new-real MAJOR + 12 MINOR findings on its post-R3 disclosure content (readiness 95, Houston sign-off next). P2 remains gated toward P2′ pending the ledger #1 independent re-derivation. P3 is provenance support for the redirected early-universe anomaly map.",
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
      version: "v1N.0.6",
      readiness: 99,
      pendingWork: "D-round (visual) + P-round (packaging) complete 2026-09-18 → v1N.0.6 (0 broken artifact links; unused bib entry pruned; arXiv tarball rebuilt + standalone-smoke-tested; CQG submission kit assembled). arXiv gr-qc endorsement (D4) remains Houston-only, not a CQG-submission blocker. Houston sign-off (99→100) not yet sought.",
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
      version: "v3M.0.25",
      readiness: 75,
      pendingWork: "R9 INT board (first since the directive-R2 stop was lifted by ledger row 19 / D-A3-14): Grok REJECT, Gemini minor-revisions, Claude Fable 5.1 major-revisions on exact v3M.0.24. Truth-audit: 24 genuinely-new-real (3 MAJOR + 1 MAJOR-lite), 14 falsified with source citations. All closed in v3M.0.25 -- reproducibility pin resolved to a commit holding none of the cited artifacts; Eq. (15) misattributed and double-counting lambda; the 10^11 f_NL figure printed without noting tree-level control expires 6.9 decades earlier (new committed computation r9_perturbativity supplies the floor). Readiness 75 COMPUTED; the one confirmation board permitted by R2 is the remaining gate before the convergence gate can be claimed."
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
      version: "v4P.0.9",
      readiness: 95,
      pendingWork: "Exact-v4P.0.8 re-verification board (Grok + Gemini + a Claude opus sub-agent not shown the prior round's closures) independently checked lane L4's own closures and closed 6 further genuinely-new-real MAJOR + 4 MINOR findings 2026-09-19 → v4P.0.9 (mislabeled monopole comparator, a false near-antipodal-axis claim, two disclosures with no forward reference from the headline sections, a mislabeled quintile split, a misattributed correlation); primary null unchanged. Directive R2: no further consecutive round without a scope decision. Readiness 95. 100 requires Houston's explicit per-paper sign-off (directive P), which should read v4P.0.9.",
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
      version: "v1S.0.9",
      readiness: 72,
      pendingWork: "R3VERIFY (2026-09-18) closed 2 ESSENTIAL + 3 MAJOR genuinely-new-real defects: the v1S.0.8 A2 closing amendment had landed in the Appendix only, contradicting Sec. III's stale value in the served PDF for 11 days; a LaTeX unicode error also dropped text. New open item S12 (translation-term monopole generality) gates the next review round.",
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
