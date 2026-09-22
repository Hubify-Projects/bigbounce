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
    "P1N (Track B) merges P1A into P1C as one closed-line ECH Note; its D-round and P-round packaging are complete, but a 2026-09-22 exact-version CONFIRM board's cold-read referee leg surfaced two ESSENTIAL open science findings (DP1N-60, DP1N-61) targeting the paper's title claims — readiness held at 95 pending real science closure, not Houston sign-off. P4′ (Track C1) folds P5 into P4 and adds the Poplawski black-hole-universe spin-axis exclusion; an exact-version INT confirmation board closed 7 genuinely-new-real MAJOR + 12 MINOR findings on its post-R3 disclosure content (readiness 95, Houston sign-off next). P2 remains gated toward P2′ pending the ledger #1 independent re-derivation. P3 is provenance support for the redirected early-universe anomaly map.",
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
      shortTitle: "The ECH Note (P1A + P1C merged, grown to CQG Paper form) — SIGN-OFF HOLD",
      version: "v1N.0.7",
      readiness: 95,
      pendingWork: "SIGN-OFF HOLD (2026-09-22): exact-version CONFIRM board closed a wording-only item (DP1N-59, v1N.0.7) but a verdict-blind Claude opus cold-read referee surfaced two ESSENTIAL, previously-unexamined findings targeting the title claims directly — the contact-term equation-of-state assumption contradicts its own density parametrization (DP1N-60), and the Popławski dark-energy rebuttal evaluates the wrong physical scale by ~74 orders of magnitude against a misdescribed source (DP1N-61). Neither closeable by a text edit; readiness held at 95 pending real science closure via a dedicated science lane, not another review board.",
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
      version: "v2B.0.24",
      readiness: 95,
      pendingWork: "R-CONFIRM exact-version board (2026-09-22) found real items and closed most by real edit (see DISPOSITIONS/P1B.md); NOT yet a confirmed/converged board. Open by design: venue split Sec.13-vs-JORS (Houston-gated), archive re-mint (Houston-gated, both Zenodo deposits predate batches 2-4), full batch-4 commit trail + appendix, deferred related-work items.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "Matter-contraction f_NL forecast",
      version: "v1.7.131",
      readiness: 95,
      pendingWork: "R-CONFIRM exact-version board (2026-09-22) found real items and closed most by real edit (see DISPOSITIONS/P2.md); NOT yet a confirmed/converged board. Open by design: whether -35/16 is an independent derivation vs. a re-summation of trusted inputs, the Cai/Li convention-mismatch question (Houston-gated re-flag of DP2-25), and the inflation-vs-bounce projection-argument asymmetry. Standalone PRD submission target; its theory content also echoes inside A3M but P2 itself was not retired.",
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
      version: "v3M.0.30",
      readiness: 75,
      pendingWork: "R12 (the one confirmation board the row-9b science decision authorized) found 6 genuinely-new-real items on the exact v3M.0.29 PDF -- Grok/Gemini API FAILED-INFRA (shared-checkout contention, not faked/back-filled), Claude opus verdict-blind referee MAJOR REVISIONS. 5 closed by real edit (two caused by this lane's own row-9b propagation: LQC's two irreconcilable transfers 0.409/0.500 distinguished; rho+p notation and undefined x fixed); 1 ESSENTIAL closed only by honest disclosure -- the PBH channel's headline ratio sits entirely inside the paper's own non-perturbative-branch window, the next concrete unlock. No physics error found; no headline number changed. Readiness 75 COMPUTED, no cap-95 claim. Open for the director: push origin/main so the reproducibility branch pointers resolve, mint the frozen-release DOI, and run the PBH perturbativity pointwise check that would authorize a further board."
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
      version: "v4P.0.12",
      readiness: 95,
      pendingWork: "HOLD LIFTED 2026-09-22 → v4P.0.12: the v4P.0.11 hold on the PA-restoring dilution bound is lifted by an in-domain re-measurement on the classifier's own Smith42/galaxies imaging (N=40,000, streamed by HTTP range read, 320,000 forward passes, $0), gated by 99.936% in-domain catalogue-scale agreement (43.9% out-of-domain) and a measured 3.41× field-of-view gap. Result D≤0.5998±0.0065 (primary_hc), A₉₅ᵖʰʸˢ≥1.63%, superseding — not averaged with — the withdrawn D≤0.717±0.005/A₉₅ᵖʰʸˢ≥1.37%; the in-domain classifier is less rotation-stable, so the correction is conservative. The sky-dependence dipole systematic (23% of A₉₅) remains out-of-domain, unchanged. A fresh INT confirmation board on the exact v4P.0.12 PDF is due (directive R2 round budget refreshed twice). Readiness 95. 100 requires Houston's explicit per-paper sign-off (directive P), which should read v4P.0.12. The prior co-director SIGN-OFF HOLD is recommended RELEASED.",
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
      version: "vAF.0.6",
      readiness: 80,
      pendingWork: "vAF.0.6 (lane LAF3, R2 confirmation board, 2026-09-22): ran on the exact vAF.0.5 PDF (never before reviewed -- LAF2 closed real items and bumped twice after R1 without an intervening board). Grok API + Gemini API (ApJS-CATALOG profile) + Claude-opus verdict-blind referee, all independently converging on a flux-to-magnitude arithmetic error and missing LoVerde/Eisenstein-Hu/Planck citations; opus alone caught the round's most consequential finding, a headline R^2=0.78 attribution error conflating a full-model regression with a univariate one (independently recomputed at R^2=0.20). 9 real findings closed with edits/new computation; several reviewer claims independently FALSIFIED against source; 2 new items honestly left open (blue-arm cut quantification, a Gunn-Peterson citation) alongside the 3 pre-existing disclosed-open items. Directive-G clean: 4-pass, 0 errors/undef refs/overfull, 18pp, 6/6 artifact links, standalone tarball compile byte-identical. NOT CONFIRMED -- directive R2: round 2 of 2 spent, no further board without an intervening science/scope decision. Prior: R1 INT board closed 2026-09-19, 17/20 canonical findings, most consequentially downgrading the abstract's 'supports one' z~4.3 quasar candidate to Undecidable. Readiness 80 COMPUTED.",
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
