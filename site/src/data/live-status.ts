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
    "P1N (Track B) merges P1A into P1C as one closed-line ECH Note; its D-round and P-round packaging are complete, and the two ESSENTIAL findings a 2026-09-22 exact-version CONFIRM board surfaced (DP1N-60, DP1N-61) are now CLOSED-BY-WITHDRAWAL at v1N.0.8 — the repulsive-sign bridge and the Popławski-rebuttal claim were withdrawn, not restored, so readiness dropped 95→85 COMPUTED and sign-off hold is retained pending a fresh confirmation board. P4′ (Track C1) folds P5 into P4 and adds the Poplawski black-hole-universe spin-axis exclusion; an exact-version INT confirmation board closed 7 genuinely-new-real MAJOR + 12 MINOR findings on its post-R3 disclosure content (readiness 95, Houston sign-off next). P2 remains gated toward P2′ pending the ledger #1 independent re-derivation. P3 is provenance support for the redirected early-universe anomaly map.",
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
      version: "v1N.0.8",
      readiness: 85,
      pendingWork: "SIGN-OFF HOLD RETAINED (2026-09-22, v1N.0.8): a dedicated derivation lane confirmed both v1N.0.7 ESSENTIAL findings as REAL and closed them by WITHDRAWAL, not restoration. DP1N-60: the corrected equation of state (w=+1, stiff) taken with the manuscript's own stated configuration makes the contact term gravitationally ATTRACTIVE — the published Kerlick (1975)/O'Connell (1977) ECSK result for the Dirac field — so the independent repulsive-sign argument is withdrawn (the γ→∞ operator identification survives untouched). DP1N-61: the 'direct, quantitative rebuttal' of Popławski's dark-energy proposal is withdrawn from §VII.D and the abstract with no replacement manufactured. Readiness dropped 95→85 COMPUTED. New flagged item: the Fierz-row scalar-channel sign (drives G_s) is unchecked, separate lane bb-LS15-fierz-sign in progress.",
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
      version: "v3M.0.32",
      readiness: 75,
      pendingWork: "DA3M-VI-01 (2026-09-22): two now-false Sec. VI statements (wide-angle 'not applied', '2 of 5' splits) corrected against the lab's own LEDGER4_RESULT_v4/v5 -- wide-angle is a genuine null, all five splits were run. Real reasons for the QSO reproduction's sigma=25 vs. published 9.0: response lever b1-p=0.649 (p=1.6) vs 1.249 (p=1.0), the published number combines LRG+QSO vs. this fit's QSO-only, and n_shot fixed at 0 vs. DESI's full nuisance marginalisation. Ledger row 4 (LRG channel) opened: f_NL^loc=-3.4+-5.7 (p=1.0), AGREES with QSO at T=-0.159, all 15 systematics rows null, still cannot separate -35/16 from -35/8 (0.38 sigma). D-A3-15's authorized confirmation board runs on this exact PDF next in the same lane. Open for the director: push origin/main so the reproducibility branch pointers resolve, mint the frozen-release DOI."
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
      version: "vAF.0.7",
      readiness: 80,
      pendingWork: "vAF.0.7 (lane LAF5, 2026-09-22): DAF-19 CLOSED -- adopted the corrected spherical-embedding re-clustering (lane LAF4) as the paper's taxonomy, replacing Table VIII/IX. 25->23 clusters, 8->9 families, ARI 0.60/AMI 0.63 vs. published (moderate restructuring, no family reproduced unchanged), ARI/AMI 0.26/0.26 vs. a survey/programme-only baseline (not a relabelling), largest wrap-aware R.A. span 350.4->331.6 deg (not-a-compact-sky-region conclusion reinforced). Every downstream number re-derived by rerunning the real pipeline: family evidence, family-sky spans, V6 (now dynamic), V12 latent silhouette recomputed on corrected labels (-0.0162->-0.0183, still structured-but-weak), the two-families narrative, FT-B/FT-C/FT-E references. Two propagation defects caught and fixed before adoption (naive-vs-wrap-aware RA span reuse; a marginal-mode-vs-joint-mode dominant-cell labelling bug). Directive-G clean: 4-pass, 0 errors/undef refs/overfull, 18pp, 5-way md5-verified mirror, standalone tarball text-identical. Board (Grok API + Gemini API + one opus verdict-blind referee) authorized next on this exact PDF -- directive R2's intervening-science-decision exception. Prior: vAF.0.6 R2 confirmation board (lane LAF3, 2026-09-22) closed 9 real findings on the exact vAF.0.5 PDF, most consequentially a headline R^2=0.78 attribution error (recomputed at R^2=0.20). Readiness 80 COMPUTED.",
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
