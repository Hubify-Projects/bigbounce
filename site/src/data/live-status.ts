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
      version: "v3M.0.28",
      readiness: 75,
      pendingWork: "R11 INT board (Grok REJECT, Gemini MAJOR REVISIONS, Claude opus verdict-blind referee MAJOR REVISIONS) ran on the exact v3M.0.27 PDF -- the one board directive R2 permitted after the row-9 (D-A3-9) Bardeen-potential science decision. Truth-audit found 16 genuinely-new-real finding-classes: a recurrence of the internal-audit-language leak, two ESSENTIAL items on the new Bardeen material (regularity proof, evaluation-window convention -- both closed using material already in the cited artifact, no new derivation), five MAJOR scheme-labelling/reasoning defects, and a minor cluster incl. a leaked internal figure-title label. No physics error found; no headline number changed. Directive R2 budget SPENT AGAIN -- rounds stopped. Readiness 75 COMPUTED, no cap-95 claim. Open for the director: push origin/main so the reproducibility branch pointers resolve, mint the frozen-release DOI, and authorize either a scope decision or a confirmation board on v3M.0.28."
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
      version: "v4P.0.10",
      readiness: 95,
      pendingWork: "Row-16(ii-b) science propagation 2026-09-21 → v4P.0.10: withdrew the invalid pixel-injection tension claim (comparisons between statistics that didn't share a normalization) and adopted a direct, assumption-light dilution bound instead (D≤0.717±0.005, A₉₅ᵖʰʸˢ≥1.37%, consistent with the illustrative g=0.398 bridge); primary null unchanged. Not a review round — a fresh INT confirmation board is now due (directive R2 round budget refreshed by this science decision). Readiness 95. 100 requires Houston's explicit per-paper sign-off (directive P), which should read v4P.0.10.",
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
      version: "v1S.0.12",
      readiness: 72,
      pendingWork: "R4 board COMPLETE (2026-09-19): Claude-opus leg (v1S.0.10) + Grok/Gemini API legs (v1S.0.11) all run and truth-audited -> v1S.0.12. 4 genuinely-real findings closed: S14's Cai-2009 citation (now backed by a new equation-level appendix), 3 App.~A2->A3 cross-reference errors, a Fig.1 caption clarity note, a Table I citation. S13 (initial-slice convention) and S15 (Appendix A5 lambda_g derivation) remain open real science gates needing a from-scratch derivation, not an edit. Per directive R2, paper-su's review-round budget is now spent -- no further board without a new science/scope decision.",
    },
    {
      slug: "paper-af",
      number: "AF",
      shortTitle: "DESI anomaly-score catalogue (Track C2 flagship draft)",
      version: "vAF.0.5",
      readiness: 77,
      pendingWork: "vAF.0.5 (lane LAF2, non-review directive-G bundle, no board run): DAF-16 fully closed -- released-column schema now documents all 192/192 columns (was 183/192), the 9 remaining derived colours/flags/join-tags reconstructed and documented from the committed assembly/enrichment scripts. Full bibliography ADS-verified (26 remaining entries beyond the 4 LR1 already checked; all match, no text changed). OT-1 selection function and the Zenodo DOI reconfirmed genuinely not agent-closable (GPU compute / Houston-only) -- left as already honestly specified. Prior: R1 INT board closed 2026-09-19 (Claude opus 6 BLOCKER/16 MAJOR, Grok REJECT, Gemini MAJOR REVISIONS, all convergent): 17/20 canonical findings closed with real edits or new committed computation, most consequentially downgrading the abstract's 'supports one' z~4.3 quasar candidate to Undecidable. 3 findings remain honestly disclosed as open (training corpus, dedup near-threshold, taxonomy RA-wrap). Directive R2: round 1 of 2 spent. Readiness 77 COMPUTED.",
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
