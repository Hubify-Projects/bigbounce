export type StageState = "done" | "active" | "blocked" | "pending";

/**
 * One step on a paper's path to publication. Notes must stay short
 * (<= ~90 chars) — the audit trail lives in project-context/SSOT/, not here.
 */
export interface PublicationStage {
  label: string;
  state: StageState;
  note?: string;
}

export interface Paper {
  slug: string;
  number: string;
  /** Editorial role in the approved question-first publication portfolio. */
  publicationRole: string;
  /** Whether this artifact is currently selected for its own submission. */
  standaloneSubmission: boolean;
  title: string;
  /** One-line plain-English purpose label — what this work is FOR, no jargon. A non-specialist gets it instantly. */
  plainTitle: string;
  version: string;
  /** ISO 8601 date of the paper's last substantive update — set per-paper, NOT a uniform "today" stamp. */
  lastUpdated: string;
  pages: string;
  refs: string;
  readiness: number;
  /** One plain-English sentence: what the paper shows. <= ~250 chars, no version changelog. */
  tldr: string;
  /** Path to publication — the canonical 6-stage pipeline, current state per stage. */
  path: PublicationStage[];
  statusVariant: "green" | "blue" | "amber" | "red";
  target: string;
  description: string;
  keyResults: string[];
  surveys: string[];
  predictions: string[];
  figures: string[];
  remainingWork: string[];
  preprintId: string;
  /** Short artifact line: size · pages · date. No changelog. */
  pdfMeta: string;
  /** Ordered list of per-version change notes, most recent first. */
  changelog?: string[];
  /**
   * Set when this paper has been superseded/merged/folded into a successor
   * paper (directive R3, 2026-09-02 portfolio restructure). The original
   * entry stays listed (never deleted) with a pointer to its successor slug
   * and, where published, its own Zenodo DOI for the archived version.
   */
  archivedInto?: {
    note: string;
    successorSlug: string;
    zenodoDoi?: string;
  };
  artifacts: Array<{
    label: string;
    href: string;
    kind: "primary" | "secondary";
    external?: boolean;
    download?: boolean;
  }>;
}

export type ResearchProgramId =
  | "track-a-bounce-vs-inflation"
  | "track-b-ech-note"
  | "track-c-desi-data-products";

/**
 * A program-level supporting link — for real, registered manuscripts that
 * back a program's science but do NOT carry the campaign-paper machinery
 * (versioned PDF-mirror path, publication-path ladder, DOI/artifact record)
 * that every entry in `papers` implies. Use this instead of adding a
 * lightweight companion to `papers` when it would wrongly pick up that
 * machinery on /paper, /papers, /publish, and /status.
 */
export interface ProgramSupportingLink {
  /** Full manuscript title, as written in its own .tex \title. */
  title: string;
  /** One-line plain-English purpose label — what this work is FOR, no jargon. */
  plainTitle: string;
  /** Editorial role relative to the program's lead/support papers. */
  role: string;
  /** One plain-English sentence: what this work validates or checks. */
  description: string;
  href: string;
  external?: boolean;
}

export interface ResearchProgram {
  id: ResearchProgramId;
  title: string;
  question: string;
  result: string;
  limitation: string;
  leadSlug?: string;
  supportSlugs: string[];
  /** Registered companion manuscripts surfaced at the program level (see ProgramSupportingLink). */
  supportingLinks?: ProgramSupportingLink[];
  status: string;
}

/**
 * Public-facing portfolio structure (2026-09-02 restructure, directive R3;
 * see project-context/PORTFOLIO_DECISION_2026-09-02.md and
 * project-context/PAPER_LINEAGE_2026-08-05.md). Three tracks replace the
 * retired "three research programs" framing: Track A is the flagship
 * bounce-vs-inflation line, Track B is one closed-line Note, Track C is
 * DESI data products framed on-vision. Archived-lineage papers (P1A, P1C,
 * P4, P5) stay listed on the flat /papers page with an "archived into"
 * label — never deleted.
 */
export const researchPrograms: ResearchProgram[] = [
  {
    id: "track-a-bounce-vs-inflation",
    title: "Track A \u2014 Bounce vs. inflation (flagship)",
    question:
      "Does a nonsingular matter-bounce produce a distinctive, reproducible, and observationally testable primordial non-Gaussian signature that beats inflation-from-a-singularity as the origin of structure?",
    result:
      "A1 \u00b7 P2\u2032 derives the exact matter-contraction amplitude f_NL = \u221235/16, confirmed by an independent from-scratch in-in computation; Cai et al. 2009's \u221235/8 located as a uniform factor 2 (ledger #1 CLOSED, 2026-09-02). A3 (paper-a3m, v3M.0.4) is now the flagship submission candidate: it folds the P2\u2032 exact-amplitude theory together with the multi-channel consistency checks (NANOGrav \u03b3, PBH abundance, SPHEREx/MegaMapper reach) into one manuscript. A2 (nonlinear transmission through an explicit bounce) remains a research brief in progress.",
    limitation:
      "A3 is at readiness 70 (R2 verification closed; final author review pending, per directive P's readiness composition). A2 is not yet a complete manuscript. The archived P2\u2032 Letter (paper-2l) is kept as a theory record, not a separate live submission target.",
    leadSlug: "paper-2l",
    supportSlugs: ["paper-a3m"],
    supportingLinks: [
      {
        title: "Nonlinear transmission of f_NL through an explicit nonsingular bounce",
        plainTitle: "A2 \u2014 does the bounce itself distort the predicted non-Gaussian amplitude? (research brief in progress)",
        role: "Track A2 \u00b7 research brief in progress",
        description:
          "Turns the matter-contraction coefficient into an observable prediction by tracing f_NL through an explicit nonsingular bounce completion (LQC dressed-metric/hybrid, plus one non-LQC bounce), rather than assuming lossless transmission. The dressed-metric scheme-specific transparency result already computed for P2\u2032 (|\u03b4f_NL| \u2264 6.8e-8 at k\u00b7\u03b7_B=1e-2) is the seed of this line; the full paper is not yet drafted.",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/research/cubic_bounce_transmission",
        external: true,
      },
    ],
    status: "Flagship line \u2014 A3 (paper-a3m) is the flagship submission candidate in draft; A2 the remaining new-science work.",
  },
  {
    id: "track-b-ech-note",
    title: "Track B \u2014 The ECH Note (closed line)",
    question:
      "What does minimal Einstein\u2013Cartan\u2013Holst spin-torsion gravity do for the bounce, and what can it not do for dark energy?",
    result:
      "P1N (v1N.0.7) merges P1A and P1C into one gr-qc/CQG paper: the derived axial spin-spin contact term is identified with Po\u0142awski's torsion-bounce repulsion mechanism (the positive result), while the same algebraic elimination closes four candidate dark-energy routes (the negative result). \u2014 SIGN-OFF HOLD: a 2026-09-22 exact-version CONFIRM board's verdict-blind cold-read referee leg surfaced two ESSENTIAL findings targeting these title claims directly, still open.",
    limitation:
      "P1N's R1\u2013R3 INT review board closed with automated review convergence declared 2026-09-02; D-round + P-round packaging complete 2026-09-18 \u2014 but the 2026-09-22 exact-version CONFIRM board (Grok API, Gemini API, Claude opus cold-read referee) found the contact term's equation-of-state assumption inconsistent with its own density parametrization (DP1N-60), and the Po\u0142awski dark-energy rebuttal evaluated at the wrong physical scale by ~74 orders of magnitude against a misdescribed source (DP1N-61). Neither is closeable by a text edit. P1A and P1C remain on disk, frozen and unedited, as this paper's archived lineage \u2014 not separate live submission targets.",
    leadSlug: "paper-1n",
    supportSlugs: [],
    status: "One closed-line paper, readiness 99 on SIGN-OFF HOLD (2026-09-22) pending DP1N-60/61 science closure. P1A + P1C review churn stopped after R13; the merged paper's D-round+P-round packaging is closed; CQG submission kit assembled but venue-click decision pending the hold.",
  },
  {
    id: "track-c-desi-data-products",
    title: "Track C \u2014 DESI data products (on-vision)",
    question:
      "What do DESI's public galaxy and spectral data show when tested directly against the rotating-black-hole-universe spin-axis prediction and scanned for early-universe anomalies \u2014 and what does that say about bounce vs. inflation?",
    result:
      "C1 \u00b7 P4\u2032 (v4P.0.11) folds P5 into P4 as the largest test of Po\u0142awski's galaxy-spin-axis prediction: a null so far, excluding alignment fractions \u03b7 > 0.98% at \u226595% coverage, a factor of 2\u201320\u00d7 below literature claims. C2 (paper-af, vAF.0.5) is the early-universe anomaly map's first full manuscript: a 1,244-object DESI DR1 anomaly-score catalogue whose R1 INT board closed 17/20 findings, reported honestly as a data release \u2014 ledger #8's pre-declared discovery condition is NOT met (no reference class clears the recovery bar). P3 remains its provenance/public-ID supporting release. C3 (namaster-proof) is an optional software note.",
    limitation:
      "P4\u2032's exclusion bears on the black-hole-universe model's spin-axis claim only \u2014 it is not itself a bounce-cosmology detection. C2 (paper-af) is a validated data release, not a discovery: its taxonomy carries no material latent-space structure and the recovery benchmark clears no reference class at the pre-declared bar; R1's board downgraded its one 'supports' quasar candidate to undecidable after finding it inside a disclosed photometric-join defect.",
    leadSlug: "paper-4p",
    supportSlugs: ["paper-af", "paper-3", "paper-1b"],
    status: "P4\u2032 at readiness 95, fresh exact-version confirmation in hand. Paper-af (anomaly-score catalogue) at vAF.0.5, readiness 77, R1 INT board closed (directive R2 round 1 of 2 spent). P3 is provenance support for paper-af. P1B (namaster-proof) is an optional JOSS note.",
  },
];

/** Shared pipeline stages — every paper walks the same six gates. */
function publicationPath(overrides: {
  external?: PublicationStage;
  signoff?: PublicationStage;
  arxiv?: PublicationStage;
}): PublicationStage[] {
  return [
    { label: "Draft complete", state: "done" },
    {
      label: "Historical automated review",
      state: "done",
      note: "Receipt-backed evidence retained; labels are version-specific",
    },
    {
      label: "Latest-version review coverage",
      state: "active",
      note: "Version-specific evidence retained; final-hash bounded confirmation may still be pending",
    },
    overrides.external ?? {
      label: "Independent human review",
      state: "active",
      note: "Required; automated-model labels are not journal decisions",
    },
    overrides.signoff ?? {
      label: "Archive and venue checks",
      state: "pending",
      note: "Immutable archive/DOI plus journal-specific scope and format checks",
    },
    overrides.arxiv ?? {
      label: "Author submission decision",
      state: "pending",
      note: "arXiv endorsement and journal submission remain author-controlled",
    },
  ];
}

export const papers: Paper[] = [
  {
    slug: "paper-1a",
    number: "1",
    publicationRole: "Focused Theory Note · ECH Boundary Result",
    standaloneSubmission: true,
    archivedInto: {
      note: "Merged into P1N, the Track B ECH Note (v1N.0.1) — 2026-09-02 portfolio restructure, directive R3. Frozen on disk unedited; no longer an independent submission target.",
      successorSlug: "paper-1n",
      zenodoDoi: "https://doi.org/10.5281/zenodo.21481838",
    },
    title: "Algebraic Cartan Elimination in Minimal Einstein–Cartan–Holst Gravity: Spin-Sourced Contact and Zero-Spin Scalar Branches",
    plainTitle: "What minimal spin-torsion gravity can and cannot change — a boundary-setting theory note",
    version: "v1A.0.127",
    lastUpdated: "2026-08-03",
    tldr: "A compact CQG Note deriving the minimal Einstein–Cartan–Holst axial contact interaction and the zero-spin canonical-scalar branch. v1A.0.127 adds the mandatory declarations and availability section; earlier exact-PDF findings were truth-audited to zero genuinely-new-real. Final-hash bounded confirmation and Houston's own review remain distinct open gates.",
    path: publicationPath({}),
    pages: "9",
    refs: "11",
    readiness: 95,
    statusVariant: "amber",
    target: "Classical and Quantum Gravity — Note",
    description: "A narrow algebraic Note. Eliminating the Cartan connection gives the convention-pinned axial four-fermion contact term; on a canonical scalar branch with zero spin current, torsion vanishes and the Holst density reduces pointwise by the torsion-free Bianchi identity. The included density and NJL calculations are dimensional/regulator diagnostics, not observational constraints or state-independent phenomenology.",
    keyResults: [
      "Minimal ECH Cartan elimination yields −(3κ/16)[γ²/(1+γ²)] J₅² in the stated convention",
      "Canonical zero-spin scalar matter gives a torsion-free branch; the Holst density then vanishes pointwise by the Bianchi identity",
      "Finite-density benchmark κnψ²/ρΛ ≈ 3.6×10⁻⁶⁹ (nψ/100 cm⁻³)² is explicitly dimensional and non-observational",
      "The direct scalar Fierz channel has Gs = −3κ/16 and no nonzero real homogeneous scalar gap in the stated hard-cutoff convention",
      "The v1A.0.123 artifact contains exactly the three M_Pl cutoff rows described by the Note and all active links are commit-pinned",
      "Exact seven-page subscription review: ACCEPT, 0 MAJOR, 0 MINOR; central contact/transparency claims preserved",
      "Exact v1A.0.124 confirmation board (Grok MINOR / Gemini MINOR / Claude MAJOR, 13 findings): truth-audited to 0 genuinely-new-real — algebra verified a third time, all majors disclosed re-flags or Houston-gated venue items. P1A CONVERGED to human gates.",
    ],
    surveys: ["No survey likelihood — algebraic and field-theory Note"],
    predictions: ["Axial contact coefficient in the stated ECH convention", "Zero-spin scalar transparency under matched boundary data"],
    figures: ["Table I: hard-cutoff coefficient-to-threshold diagnostics"],
    remainingWork: [
      "Human CQG significance disposition — the automated confirmation board is not journal acceptance",
      "Authorize a manuscript/source license; exact bundle/proof pass but deposit metadata and any draft intentionally fail closed until then",
      "After license authorization, verify a reversible draft before any immutable archive/DOI action",
      "Alternate-regulator robustness beyond the declared hard-cutoff convention",
      "Matched Lorentzian state/stress observable and a state-specific renormalized axial expectation value",
    ],
    preprintId: "HUBIFY-2026-001",
    pdfMeta: "PDF · 8 pp · v1A.0.127 · updated Jul 24, 2026 · md5 0bc1ee72836c867114118521cf86e1c2 — v1A.0.127 makes the IOP-mandatory declarations actually compile: the whole acknowledgements block sat inside a commented-out region with the cut cosmology material, so the Note had shipped with no competing-interests, funding, or AI-usage statement. A new Note-scoped block was written rather than un-commenting the old one, and Data and Code Availability was promoted to its own section. Archival deposit PUBLISHED (Houston go): DOI 10.5281/zenodo.21481838 (CC-BY-4.0). No readiness change.",
    changelog: [
      "v3M.0.19: D-A3-14 (ledger row 19) -- the joint (r,f_NL) no-go generalizes to the full P(X) k-essence class. r=24c_s and the bounce's own cubic term Delta f_NL^bounce(c_s) are exactly independent of the cubic-action coefficient lambda (d(c_s^2)/d(P_XXX)=d(Sigma)/d(P_XXX)=0; the lambda vertex is odd about a symmetric bounce and cancels in the S1 in-in integral, verified to 2.8e-7). f_NL^pre(c_s,L)=-245/16+105/(8c_s^2)-30L (L=lambda/Sigma, squeezed) reproduces Li+2016 on their line and -35/16 at c_s=1,L=0; no L in the physical range opens the window -- cancelling the divergence needs lambda/Sigma=7/(16c_s^2) (s=39/16, far outside |s|<<1). DBI best case r_min=12.57 at c_s=0.524 (349x BICEP/Keck). The lambda=s=0 scope qualifier dropped from abstract/Sec. VIII/Next steps (v3M.0.18's D-A3-13 first restricted the no-go to lambda=s=0 pending this computation). 4-pass, 0 undef refs, 0 overfull hboxes >10pt, 18 pp, md5 fdbf93bfacc6cc644e103ff522d15381, Convex bump k57axjh0ap83rgnmgd6qtdk3qh8dtsaz. Readiness held at 75 -- ROUNDS STOPPED (R2); row 19 answered, no lambda opens the window.",
      "v1A.0.127: IOP-mandatory declarations now compile — the acknowledgements block had been commented out together with the cut cosmology material, so the Note shipped with no competing-interests, funding, or AI-usage statement; a new Note-scoped block replaces it and Data and Code Availability is now its own section. No readiness change.",
      "2026-07-16 confirmation board: exact v1A.0.124 board Grok MINOR / Gemini MINOR / Claude MAJOR (13 findings); truth audit found 0 genuinely-new-real — algebra verified a third time, all majors disclosed re-flags or Houston-gated venue items. P1A CONVERGED to human gates (CQG significance disposition, license/deposit authorization, alternate-regulator robustness). No version change.",
      "v1A.0.124: Claude Opus-tier subagent exact-PDF board on v1A.0.123 returned MAJOR (2 MAJOR / 4 MINOR); truth audit found 0 correctness errors (algebra hand-verified) — the majors are disclosed re-flags/tracked gates. Closed 3 sub-sentence editorial items: shows the torsion-lemma 4D contraction coefficients (derived from the manuscript's own identities), relabels Sec III.B \"mean-field NJL diagnostic\" with scope softening, and consolidates the relation-to-prior-work sentence. Readiness cap 62 unchanged.",
      "v1A.0.123: corrected the pinned NJL artifact to the manuscript's three-row M_Pl-only scope and replaced active mutable-main artifact URLs with commit-pinned links; exact subscription-backed Codex confirmation returned ACCEPT (0 MAJOR / 0 MINOR). Readiness unchanged.",
    ],
    artifacts: [
      { label: "Read PDF", href: "/papers/paper1a_ech_nogo_v1A.0.127.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper1a_ech_nogo_v1A.0.127.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/bdbb2242199a8eb50bdee825b98d42ea8a3de523/arxiv/paper1a_ech_nogo.tex",
        kind: "secondary",
        external: true,
      },
      {
        label: "Exact-PDF review evidence",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/project-context/peer-reviews/INT_v3/ROUND_2026-07-16-P1A-v1A.0.123-EXACTPDF-4c450a67-CLAUDESTACK/P1A_v1A.0.123_truth_audit.md",
        kind: "secondary",
        external: true,
      },
      { label: "Zenodo DOI (manuscript archive)", href: "https://doi.org/10.5281/zenodo.21481838", kind: "secondary", external: true },
    ],
  },
  {
    slug: "paper-1b",
    number: "1B",
    publicationRole: "Research Software · Exact-Window Verification",
    standaloneSubmission: true,
    title: "namaster-proof: Content-bound execution receipts as a shortcut detector for pseudo-Cℓ computations",
    plainTitle: "Software that catches skipped or faked steps in a common CMB/LSS analysis — a general verification primitive, tested blind",
    version: "v2B.0.24",
    lastUpdated: "2026-09-22",
    tldr: "R3 truth-audit found R7's row draw is prover-predictable, not unpredictable, and fails open if its checked intermediate is omitted. Batch 4 (54 sealed runs, seal verified, seed committed before the seal) answers both with R8, a post-commitment verifier challenge: the rule-aware evasion (S7) and the omission (S8) are each caught 6/6 with zero honest false positives, while metadata forgery (S5) still escapes by construction. Batch 3's 24/24 miscount corrected to 30/30; all four batches now report class-level counts only. Prior art (Freivalds 1977, Fiat-Shamir 1986) cited.",
    path: publicationPath({}),
    pages: "18",
    refs: "4",
    readiness: 95,
    statusVariant: "amber",
    target: "Journal of Open Research Software — Software Metapaper",
    description: "A narrow, installable Python verification layer for exact NaMaster bandpower-window inference, deterministic multipole-support contracts, and tamper-evident JSON result receipts. The paper makes software and reproducibility claims only; it does not claim a cosmological detection or a novel physical model.",
    keyResults: [
      "Exact contraction of uniformly rotated EE/EB/BE/BB spectra through the complete NaMaster bandpower-window tensor",
      "Fixed-grid recovery and direct equivalence testing against the couple-cell/decouple-cell operator",
      "Atomic JSON publication with coherent-snapshot SHA-256 receipts and fail-closed metadata validation",
      "Deterministic field, bin, and harmonic-limit contracts whose final exclusive bin edge is ℓmax+1",
      "41 automated tests across Linux Python 3.10–3.13 plus Windows 3.12, including strict JSON metadata types, exact operator shapes, integer harmonic inputs, and concurrency regressions",
      "A REAL standalone wheel-build test verified the honest test contract: 41/41 pass inside the monorepo; 39/41 pass standalone with the 2 monorepo-coupled tests skip-guarded (verified both ways)",
      "Associated 500-realization physical example recovers +0.270°, +0.342°, and the null at the declared 0.001° grid resolution",
      "Independent PyMaster 2.6 integration: injected/exact-recovered 0.250°, effective-ℓ shortcut 0.315°, exact operator residual 6.78×10⁻²¹",
      "Exact v2B.0.9 confirmation board (Grok REJECT / Gemini MINOR / Claude MAJOR): truth audit found no new executable defect and FALSIFIED the 'workspace tensor not reproducible' premise (deterministically regenerable from committed RNG-free code, verified)",
      "v2B.0.10 closure: new examples/rebuild_workspace_check.py recheck script (skip-safe without PyMaster), real committed execution costs (701.5 s / 8 workers), pip-install one-liner in Sec 11, macOS-untested label retained; 41/41 tests",
    ],
    surveys: ["Synthetic linear workspace", "Synthetic CAMB/NaMaster validation"],
    predictions: ["Exact-window operator equivalence", "Tamper-evident result validation", "Deterministic multipole contracts"],
    figures: ["Software architecture", "Exact-window equations", "Executable worked examples"],
    remainingWork: [
      "Houston-gated: immutable archive DOI (Zenodo or PyPI+Zenodo), correspondence metadata, human software review — the DOI major is fully CLOSED 2026-07-21 (software DOI 10.5281/zenodo.21481753 + manuscript deposit DOI 10.5281/zenodo.21481842, both published on Houston's go and cited in the v2B.0.13 Archive paragraph); remaining Houston gates: correspondence metadata + human software review",
      "Obtain independent human software review and publish an immutable archive/DOI",
      "Publish package 0.1.7 to an independent package index once a PyPI token is available (Houston gate) after release QA",
    ],
    preprintId: "HUBIFY-2026-001B",
    pdfMeta: "Software metapaper · 18 pp · v2B.0.24 · package 0.1.7 · 41 tests · updated Sep 22, 2026 · md5 b94a18fbfbdece5949999354d6833864 — R-CONFIRM exact-version board (Grok REJECT / Gemini REJECT / Claude opus MAJOR-REVISIONS) closed most genuinely-new-real findings by real edit; NOT yet a confirmed/converged board. Venue split (Sec.13 vs JORS) remains a standing Houston-gated decision.",
    changelog: [
      "v2B.0.24: R-CONFIRM exact-version board on v2B.0.23 (sha256 c7cac6c9f16c..., Grok REJECT / Gemini REJECT / Claude opus verdict-blind MAJOR-REVISIONS, 43 findings) truth-audited against DISPOSITIONS/P1B.md. NOT a clean wave. Closed by real edit: abstract's stale 'not of value-level shortcuts' claim brought in line with Sec.11 (recurrence of D-R3-13, whose remedy was never applied to the abstract); the absolute 'never run-level' claim scoped to exclude batch-1's own disclosed pilot numbers; every Clopper-Pearson interval removed from batches 1-4 (honest runs are deterministic replicas of one fixed reference configuration, not an i.i.d. sample); a new batch-4 confusion table (Table 5) transcribed from the committed public4/scorecard.json plus an explicit f^K R8-soundness bound (N~63, K=6); 'Protocol, two batches' heading fixed; Sec.11 L1-L3 reworded out of reviewer-response-style status tags into prose (no disclosed content removed) plus new L5 disclosing R0/R1/R5 never fire across 137 tabulated runs; Sigstore/Rekor and 'Fiat-Shamir-correct' mislabeling corrected (a transparency log witnesses publication time, not truth; R8 is an interactive verifier-committed challenge, not a Fiat-Shamir instance) with Freivalds/Fiat-Shamir/Klein-Roodman promoted to numbered bibliography entries; Archive paragraph now discloses both Zenodo deposits (July 21) predate batches 2-4 by 6-7 weeks; ~15 further editorial fixes. Left open by design (Houston-gated or explicitly deferred, logged as D-CONF-04/09/10/12): the venue-split scope decision, the archive re-mint, a full batch-4 commit trail + 54-run appendix, and several related-work/derivation items. 18 pp (was 16), sha256 eec6e6d4792b2d8ecb17b05a4ee97d4ec2b5bd1c1f579f41b92bfc8746dc5bbd, md5 b94a18fbfbdece5949999354d6833864, tarball paper1b_namaster_proof_arxiv_v2B.0.24.tar.gz rebuilt from the single .tex and standalone-recompiled clean. Convex disabled (spending limit) -- paperVersions:bump queued to CONVEX_BACKFILL_QUEUE_2026-09-21.md. Readiness holds 95 (computed).",
      "v2B.0.23: closed the three remaining deferred text-only items from the v2B.0.20 R3 truth audit. D-R3-06: added the commit-ordered batch-3 audit trail (dcf96696 rules-frozen -> d03fe376 pre-registration -> b19b72fc attempt-1 seal -> 60917635 attempt-1 aborted -> cd9ab366 artifacts preserved -> 56ef3fd2 harness fix -> c7fb5e38 fresh-key reseal -> 4a7f9f82 runs published -> 5b643fc2 reveal+scorecard -> bf7d26e3 OpenTimestamps anchor), disclosed that no abort criterion was pre-registered before attempt 1, and added the fresh-key non-contamination + attempt-1-assignment-unpublished sentences. D-R3-15: quoted the frozen rule-file sha256 digests as committed (RULES_v2_FROZEN.md 169b3690..., RULES_v3_FROZEN.md 856f4c50..., RULES_v4_FROZEN.md a59caaf8...). D-R3-20: Table 1 gets a third trust category for intermediates.pseudo_cl, whose absence fails R7 open. 16 pp, md5 60d1a18ab3ea499398106d6a92bc8a35, tarball sha256 495c4bde5404e8080d1f81d9d0bf0ad952df485b076f070f61d1400e8cc85579, Convex bump k57044fvt6tf1thg4fkpb10bbd8dt2gf. All deferred text items now closed; remaining: Zenodo corpus deposit + venue decision (Houston).",
      "v2B.0.22: closed deferred D-R3-21 (Section IX recompute of the two remaining injected-angle sigmas). Recomputed all three injected-angle recovery statistics (0.270deg, 0.342deg, 0.000deg-null) directly from the committed physical_spectrum_v2/bandpowers.npz per-realization EB bandpowers (N=500 each), using the same windowed chi-squared grid-search estimator as scripts/namaster_500mc.py; the theory response was reconstructed exactly from the three stored theory vectors and cross-validated bit-for-bit against the script's own recorded beta_paper1 SD/SEM. Result: 0.270deg -> 0.2699+-0.0006deg (SD 0.0128deg), 0.342deg -> 0.3419+-0.0006deg (SD 0.0128deg), 0.000deg (null) -> -0.0001+-0.0006deg (SD 0.0127deg), all N=500. 16 pp, md5 843755dc1931e6e469b88150b7de4fc9, tarball sha256 350e95439cf8b1db4d3da482a1574a8477c14a791d32b2d1177716dac42ff0eb, Convex bump k57bp9zcmh1efx8y83jgx72bcn8dtga5. Remaining deferred: Zenodo deposit (Houston), venue decision (Houston), §6 subsectioning/appendix tables, batch-3 audit-trail sentences, rule-file digest quoting, Table 1 third trust category.",
      "v2B.0.21: R3 truth-audit closure (project-context/peer-reviews/INT_v3/P1B_v2B.0.20_R3_TRUTH_AUDIT_2026-09-05.md, 33 canonical findings, 27 genuinely-new-real). Batch 4 (RULES_v4_FROZEN.md, 54 runs sealed dbe6a713..., seed committed before the seal and revealed after) integrated: S7 (R7-aware effective multipole) 6/6 flagged, R7 fired 0/6 exactly as predicted, R8 fired 6/6; S8 (omit pseudo_cl) 6/6 flagged, R7 fails open 0/6 as predicted, R8 catches it 6/6; honest 0/6; S5 still escapes 0/6. R7 restated honestly as receipt-bound but prover-predictable, not unpredictable. Batch-3 '24/24' corrected to 30/30; all four batches now report class-level counts only, never run-level Clopper-Pearson intervals. Protocol rewritten for four batches. New prior-art paragraph (Freivalds 1977, Fiat-Shamir 1986, Klein & Roodman 2005). Dangling cross-references repointed; pymaster 3.0.1 corrected to 3.0; abstract shortened and rescoped for R7/R8; venue statement added (ACM REP primary, JOSS/JORS software companion). 16 pp, md5 92df731d69859c74285a3c099a7aab1f, tarball sha256 b8136d02fd9152a90909d8234c73ff6f40beabf35fb7a1e81b540682d1a0cdc3, Convex bump k5784xam4eaqav7dwc1end373d8dvtka. ROUNDS STOPPED under directive R2; next step is the venue decision + ASCL/Zenodo kit (Houston-gated).",
      "v2B.0.20: Batch 3 pre-registered blind round (pipelines/namaster_proof/VERIFICATION_PRIMITIVE_2026-09-04.md) adds R7 — recomputes 6 receipt-selected coupling-matrix rows against the declared pseudo-spectrum, fires iff the residual exceeds 1e-6*||p||. 48 sealed runs (8 arms x 6, seal abfe2793..., seal_verified true): honest 0/6 (FP upper bound 0.393); S1-S4 6/6 each; new S4b cross-run cache variant 6/6 (cross-run disjunct fired 4/6, first time it has fired); S6 effective-multipole 6/6 by R7 alone (lower bound 0.607, closes the batch-2 open item); S5 metadata forgery still escapes 6/6 by forging p := M C. Attempt 1 aborted before unsealing (seed-handling defect), preserved under public3_aborted/. Separately, a PyMaster (NaMaster 3.0.1) cross-check (pipelines/namaster_proof/PYMASTER_CROSSCHECK_2026-09-05.md) validates the in-house spin-0 MASTER estimator to floating-point round-off (coupling matrix 4.25e-13, bandpowers 1.54e-12 max relative diff). Abstract, blind-test section, limitations, and reproducibility statement updated. 15 pp, md5 c22158448310861711838e3544a0e04b, tarball sha256 01c6c1a6bad158aa5b02303727ef29011 9607c86b635d8308a3ff9db86c8d584. ROUNDS STOPPED under directive R2; one verification board now permitted following this science change.",
      "v2B.0.19: R2 closure (commits af7f2b18, a7cbd82e, 7a7f98f9) — statistics presentation corrected (class-level detection, no run-level intervals, 90% interval labelled correctly), estimator description fixed, traceability + reproducibility recipe added. 13 pp, md5 b1c68336fdd183918dcb677fddb9fd72, tarball sha256 9a695757d0ee5a493bcf6177fa53fcd1eda6d88a7ac76767b0d046df5ce57370, Convex bump k5753kmsvg9bp644qwt03vrrex8dv0v8. ROUNDS STOPPED under directive R2 pending a science/venue decision; batch 3, OTS confirmation, and PyMaster cross-check remain open.",
      "v2B.0.18: R1 truth-audit closure (project-context/peer-reviews/INT_v3/P1B_v2B.0.17_R1_TRUTH_AUDIT_2026-09-04.md, 23 canonical findings, 21 genuinely-new-real, 8 answered by integrating the pre-registered batch-2 blind test). Batch 2 (35 sealed runs, 7 arms x 5, rules frozen+committed before the seal) is now the PRIMARY result: S1-S4 20/20 (one-sided 95% Clopper-Pearson lower bound 0.861), honest 0/5 (FPR upper bound 0.451), S5 metadata-forgery escaped 5/5 (pre-declared), S6 effective-multipole escaped 5/5 with no rule added post hoc (independence caveat pre-declared and stated). Batch 1 (18 runs) relabelled the pilot/rule-development round; its post-hoc wall-clock and M-hash rule changes disclosed, not defended. New 'Relation to Provenance and Attestation Tooling' section (in-toto/SLSA/Sigstore-Rekor/ReproZip/Snakemake/Nextflow/RO-Crate/MLflow). SEM added to 500-realization recovery numbers; exact (not rounded) recovered values reported. Sealed digests of both batches OpenTimestamps-anchored (pending Bitcoin confirmation, disclosed as in-progress). Appendix table of all 35 batch-2 per-run verdicts added. 12 pp, md5 89cbca0fc922f9c1c63f1afaf35f8517, tarball sha256 00bb9c78c25882537bd295d48d7adb8ba8041c3a11a5e82e413539ba0654c652, Convex bump k571wkyj4scvf02q553tyq9r8d8dtnsx. R1 CLOSED; per directive R2 at most one further verification round permitted before an intervening science/scope decision.",
      "v2B.0.17: novelty lift #3 (project-context/NOVELTY_AUDIT_2026-09-04.md #3) — reframed from an N2 NaMaster-specific validation layer to a general verification primitive tested against a pre-declared, sealed BLIND shortcut-detection protocol (18 runs, 3 per arm, local CPU, ~1 min, $0). Detected all 4 receipt-visible shortcut classes (operator-skip, operator-truncate, grid-reduce+interpolate, cache-substitute) 12/12 with 0/3 false positives; metadata-forgery arm escaped 3/3, reported as the limitation. Two corrections found while running it: wall-clock is not a usable rule (would false-fire on 3/3 honest runs); an M-hash collision across honest runs is not cache-substitution evidence. New 'Blind Shortcut-Detection Test' section + 'What the receipt binds' table; title reframed to 'Content-bound execution receipts as a shortcut detector for pseudo-C_l computations'. 8 pp, md5 7bc21cbe7a1dfb837f08cae2c8b0f2b3.",
      "v2B.0.16: closed the 2026-07-23 Grok MAJOR ('irreconcilable internal contradiction' claim FALSIFIED — pyproject.toml, codemeta.json, CITATION.cff, __init__.py, Zenodo all read 0.1.7); title-page stamp labelled a manuscript revision; new Software version section states the document-vs-software namespace split.",
    ],
    artifacts: [
      { label: "Read PDF", href: "/papers/paper1b_namaster_proof_v2B.0.24.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper1b_namaster_proof_v2B.0.24.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/arxiv/paper1b_namaster_proof.tex",
        kind: "secondary",
        external: true,
      },
      {
        label: "Software package",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/packages/namaster-proof",
        kind: "secondary",
        external: true,
      },
      {
        label: "Physical validation artifacts",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/reproducibility/p1_namaster_500mc",
        kind: "secondary",
        external: true,
      },
      {
        label: "Legacy validation dossier",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/arxiv/paper1b_mcmc_companion.pdf",
        kind: "secondary",
        external: true,
      },
      { label: "Zenodo DOI (manuscript archive)", href: "https://doi.org/10.5281/zenodo.21481842", kind: "secondary", external: true },
      { label: "Zenodo DOI (namaster-proof 0.1.7 software)", href: "https://doi.org/10.5281/zenodo.21481753", kind: "secondary", external: true },
    ],
  },
  {
    slug: "paper-1n",
    number: "1N",
    publicationRole: "Track B · The ECH Note (closed line)",
    standaloneSubmission: true,
    title: "What Minimal Einstein–Cartan–Holst Torsion Does for the Bounce and Cannot Do for Dark Energy",
    plainTitle: "One closed-line Note: spin-torsion gravity's contact repulsion powers a bounce mechanism, but not dark energy",
    version: "v1N.0.7",
    lastUpdated: "2026-09-22",
    tldr: "Merges P1A and P1C into a single gr-qc/CQG paper. The derived axial spin-spin contact term is identified with Popławski's torsion-bounce repulsion mechanism (the positive result) while the same algebraic elimination closes four candidate dark-energy routes (the negative result). SIGN-OFF HOLD (2026-09-22): an exact-version CONFIRM board's verdict-blind Claude opus cold-read referee — after independently re-verifying nearly every other quantitative claim in the paper as correct, including falsifying an adversarial 57-order-of-magnitude unit-error claim — surfaced two ESSENTIAL findings targeting the title claims directly: the contact term's equation-of-state assumption contradicts its own density parametrization and the standard torsion-cosmology literature result (DP1N-60), and the 'direct quantitative rebuttal' of Popławski's own dark-energy proposal evaluates the wrong physical quantity by ~74 orders of magnitude against a misdescribed source (DP1N-61). Neither is closeable by a text edit; readiness held pending real science closure.",
    path: publicationPath({}),
    pages: "13",
    refs: "—",
    readiness: 95,
    statusVariant: "amber",
    target: "Classical and Quantum Gravity — Paper",
    description:
      "Track B of the 2026-09-02 portfolio restructure (directive R3): P1A's algebraic Cartan elimination (spin-sourced axial contact term, zero-spin scalar branch) merged with P1C's 14-entry structural no-go survey (Route-2/Route-3 amplitude-budget closures, six-member dimension-4 parity-odd operator list) into one Note that states both readings of the same result — what minimal ECH gravity does for the bounce, and what it cannot do for dark energy. The Introduction and Discussion explicitly identify the derived contact term with Popławski's spin-spin repulsion mechanism (arXiv:1007.0587; arXiv:1102.5667).",
    keyResults: [
      "Minimal ECH Cartan elimination yields the axial contact term −(3κ/16)[γ²/(1+γ²)]J₅² in the stated convention",
      "The derived contact term is identified with Popławski's torsion-bounce spin-spin repulsion mechanism — the positive result",
      "14-entry barrier catalog across 7 foundation mechanism classes and 6 observational branches closes four candidate dark-energy routes (R1–R4) — the negative result",
      "Six-member dimension-4 parity-odd operator list corrected to a rank-4 spanning/generating list (rank 2 modulo total derivatives), matching the settled theory-audit record",
      "On-shell ECH torsion at finite Barbero–Immirzi γ carries both an axial and a trace-vector irrep (β/α = 1/2γ); pure axiality holds only in the strict γ→∞ Einstein–Cartan limit",
      "4-pass compile: 0 undefined references, 0 undefined citations; overflow audit 0 overfull hboxes >10pt after two fixes; every page visually rendered and checked",
      "tools/p1c_consistency_check.py: 4/4 rules PASS (constraint-count agreement, Tier-I count agreement, assert-vs-disclaim pairs, universal-closure claim vs self-declared non-closures)",
    ],
    surveys: ["No survey likelihood — algebraic and field-theory Note"],
    predictions: ["Axial contact coefficient in the stated ECH convention", "Identification of the contact term with the Popławski torsion-bounce mechanism"],
    figures: ["Table I: 14-entry barrier catalog", "Table II: six-member operator list with rank-4 spanning status"],
    remainingWork: [
      "SIGN-OFF HOLD (2026-09-22): DP1N-60 (contact-term equation-of-state inconsistent with its own density parametrization) and DP1N-61 (Popławski dark-energy rebuttal evaluated at the wrong physical scale, ~74 orders off, against a misdescribed source) are OPEN, ESSENTIAL, and target the paper's title claims directly — not closeable by a text edit; a dedicated science-closure lane is needed",
      "D-round (visual) + P-round (packaging) remain complete on their own packaging-gate terms — v1N.0.7, readiness ladder R(96, now reopened)→D(98)→P(99)",
      "arXiv gr-qc endorsement (D4) remains open — Houston-only action (forward/regenerate endorsement code); not a blocker for the CQG journal submission, which needs no arXiv prerequisite",
      "CQG submission kit assembled: SSOT/CQG_SUBMISSION_KIT_P1N_2026-09-18.md (abstract, categories, cover letter, DAS) — do not submit until the sign-off hold lifts",
      "arXiv tarball rebuilt + standalone-smoke-tested: SSOT/arxiv_tarballs/paper1bc_ech_note_arxiv_v1N.0.6.tar.gz",
      "Houston sign-off has not been sought and should not be until DP1N-60/61 close",
    ],
    preprintId: "HUBIFY-2026-001N",
    pdfMeta: "PDF · 11 pp · v1N.0.7 · created Sep 22, 2026 · md5 8f073078c95ff587825e0a78397b13a3 — SIGN-OFF HOLD: 2 ESSENTIAL open science findings (DP1N-60, DP1N-61).",
    changelog: [
      "v1N.0.7: exact-version CONFIRM board (Grok API, Gemini API, Claude opus verdict-blind cold-read referee) closed one wording-only item (DP1N-59, abstract-body operator-classification drift) and independently re-verified nearly every quantitative claim in the paper correct — but the cold-read referee surfaced two ESSENTIAL findings never examined by any prior round: the contact-term equation-of-state assumption contradicts its own density parametrization (DP1N-60), and the Popławski dark-energy rebuttal evaluates the wrong physical scale by ~74 orders of magnitude against a misdescribed source (DP1N-61). SIGN-OFF HOLD placed; readiness 99→95 pending real science closure.",
      "v1N.0.6: D-round (visual audit clean, 0 fixes needed beyond pre-existing sub-gate residual) + P-round (0 broken artifact links; bib-tarball-rebuild pruned one orphaned unused entry; arXiv tarball rebuilt + standalone-smoke-tested; CQG submission kit assembled). No science change. Readiness 95→99.",
      "v1N.0.5: REVISE (abstract cap) executed — abstract trimmed to venue word cap (298 words), no science change; tarball rebuilt.",
      "v1N.0.4: R3 verification pass closed — automated review converged (Claude major-revisions, Grok reject, Gemini major-revisions) with machine-checked regressions; final author review APPROVE; readiness 95; arXiv tarball assembled.",
      "v1N.0.3: R2 closure — 23/23 findings closed, including two errors inherited from P1C (8π coefficient, O5 parity). R2 verdicts: Claude major-revisions, Grok reject, Gemini major-revisions. R3 verification pass dispatched, verdicts pending.",
      "v1N.0.2: R1 closure — 42 finding-rows audited (Claude INT major-revisions, Grok API REJECT, Gemini API REJECT), 19 canonical real items closed via real edits (operator definitions, derivations, citations, bib pruned 113→26). Grown from Note to Paper form (10pp/7725 words). Compiled 4-pass, 0 undef refs, 0 overfull hboxes >10pt, 4/4 consistency-check rules PASS.",
      "v1N.0.1: first merged draft. Compiled 4-pass, 0 undef refs, 0 overfull hboxes, 4/4 consistency-check rules PASS. Superseded P1A (v1A.0.127, archived, Zenodo 10.5281/zenodo.21481838) and P1C (v1C.0.16, frozen, not independently submitted).",
    ],
    artifacts: [
      { label: "Read PDF", href: "/papers/paper1bc_ech_note_v1N.0.7.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper1bc_ech_note_v1N.0.7.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/arxiv/paper1bc_ech_note",
        kind: "secondary",
        external: true,
      },
      {
        label: "Archived lineage: P1A (Zenodo DOI)",
        href: "https://doi.org/10.5281/zenodo.21481838",
        kind: "secondary",
        external: true,
      },
      {
        label: "Archived lineage: P1C (LaTeX source, frozen v1C.0.16)",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/arxiv/paper1c_nogo_survey/main.tex",
        kind: "secondary",
        external: true,
      },
    ],
  },
  {
    slug: "paper-2",
    number: "2",
    publicationRole: "Lead Theory Paper · Matter-Contraction Non-Gaussianity",
    standaloneSubmission: true,
    title: "The Exact Matter-Contraction Non-Gaussian Amplitude: Four-Vertex Derivation and Conditional Large-Scale-Structure Mapping",
    plainTitle: "The bounce program's core prediction: an exact primordial non-Gaussianity amplitude (f_NL = −35/16)",
    version: "v1.7.131",
    lastUpdated: "2026-09-22",
    tldr: "Derives f_NL = −35/16 for the stated matter-contraction background and cubic action, then maps that result conditionally to published and in-house large-scale-structure sensitivity estimates. v1.7.131 closes an exact-version confirmation board (Grok REJECT / Gemini MINOR / Claude opus MAJOR): most editorial/citation findings closed by real edit, three deep scientific-framing findings honestly logged as open rather than resolved or hidden.",
    path: publicationPath({}),
    pages: "12",
    refs: "39",
    readiness: 95,
    statusVariant: "amber",
    target: "Physical Review D",
    description: "A four-vertex derivation of the matter-contraction non-Gaussian amplitude under the manuscript's stated assumptions, followed by conditional large-scale-structure mappings. Published SPHEREx sensitivities and an in-house Fisher calculation are used as bounded forecasting diagnostics; they are not treated as mechanism-independent predictions or detections.",
    keyResults: [
      "f_NL = -35/16 = -2.1875 under the stated background, gauge, and cubic-action assumptions",
      "Four-vertex squeezed-limit derivation and committed symbolic cross-check agree",
      "Eq. 3 1/k² shape function fix (Wave 11) restores claim-derivation consistency",
      "Normalization audit: 92% confidence via vertex-by-vertex Cai action",
      "SPHEREx Fisher forecast: σ(f_NL) ≈ 0.36 (Fisher) / 0.93 (Munchmeyer+2019 conservative) → ~1.3-2.75σ realistic detection",
      "Heinrich+2023 σ(f_NL) ≈ 0.5–0.7 SPHEREx anchor (R35 polish)",
      "INDEPENDENT bispectrum Fisher (c13, v1.7.100): from-scratch tree-level multi-tracer Fisher on the same public SPHEREx table reproduces Heinrich σ(f_NL^local)=0.63–0.69 (within 2–11%), recovers σ(f_NL^bounce)=0.63–0.69 → r_eff≈0.99 and an unmarginalized ~3.2–3.5σ for −35/16 — validates the recast, retires the 'no independent Fisher' concession (GR-projection bracket 0.8–1.3σ still applies on top)",
      "REDSHIFT-SPACE (RSD) tree bispectrum Fisher (c14, v1.7.103): extends c13 with the Kaiser Z1=b+fμ² factor + SCF99/Sefusatti Z2 kernel, growth f(z)=fσ8/σ8 from the same CAMB Planck2018, orientation-integrated over full (μ1,φ) so ℓ=0,2,4 content is exact. σ(f_NL^local) tightens to 0.415 (b-fix)/0.449 (b-marg) vs real-space 0.688 (+34.7% tighter; bounce-template bias-marginalized baseline; RSD/Heinrich 0.64); σ(f_NL^bounce)=0.417/0.449; r_eff≈0.99 persists in redshift space; f→0 reproduces c13 to 6 sig-figs. Unmarginalized −35/16 significance rises to 4.9–5.2σ (before the systematic + GR-projection budget) — retires the 'real-space monopole only, ~18% offset' limitation with real computation",
      "Template mismatch quantification between bounce and local shapes",
      "Joint (f_NL, n_fNL) SDB Fisher rebuilt from committed code: subordinate channel at 1.4σ (fixed-bias) / 0.6σ (bias-marginalized); earlier ~9.9σ joint-Fisher claim withdrawn (not reproducible from documented inputs)",
      "Table III rebuilt from committed c9g recompute: BF/lnBF per config 3.5e8/7.0, 4.5e5/6.1, 6.4e2/4.7 (envelope ~9–14 under bounce-amplitude bookkeeping); Φ/ζ convention mapping proven exactly; 0.5000 ratio identified as the −2Im operator identity",
      "QSFI scaling endpoints corrected per Chen–Wang; −35/16 single-field result re-attributed to Li–Quintin–Wang–Cai at 17 sites",
      "Continuous-GR-recovery marginalization (c9k): bounce preference robust at BF = 6.0; GR-degradation calibration corrected ~15% → ~23% (c9k-verified)",
      "σ_theory continuous marginalization (c9l): configuration ranking stable under continuous theory-error treatment (R25conf wave)",
      "G3 model-specific torsion bound (v1.7.125, Eq. 5): |δf_NL^tor| ≲ (35/16)(3/16)[γ²/(1+γ²)] κ n_ψ,c²/ρ_c via a sympy Einstein-Cartan four-fermion estimate anchored to the companion P1A's convention-audited contact term (benchmark reproduced to 0.1%); within EFT validity (x_ψ<1) the bound saturates at prefactor 0.022 (γ=0.2375) to 0.21 (γ=1) — torsion never exceeds ~1-10% of the -35/16 amplitude, <<1e-3 for sub-Planckian n_ψ,c — converting assumption (f) from asserted to bounded",
    ],
    surveys: ["DESI DR1 (current constraint σ ≈ 4.1 combined)"],
    predictions: ["f_NL = -35/16"],
    figures: ["Fisher forecast contours", "Template overlap matrix", "σ(f_NL) sensitivity curves"],
    remainingWork: [
      "Run the bounded confirmation against the exact v1.7.130 PDF; earlier review evidence is not a verdict on this hash",
      "Independent human scientific review and venue-specific scope/format check",
      "Immutable archive/DOI is now published and embedded (v1.7.126, Zenodo 10.5281/zenodo.21461881); the record archives the reviewed v1.7.125 bytes and the concept DOI carries forward to future versions",
      "Direct cubic bounce transfer (dressed-metric intermediate now regulator-independent to <1%, IC-epoch placement + quantum-mass term remain) and survey-native SPHEREx covariance/likelihood remain open; the model-specific torsion bound is now computed and bounded (v1.7.125)",
      "Author arXiv endorsement and journal-submission decision",
    ],
    preprintId: "HUBIFY-2026-002",
    pdfMeta: "PDF · 12 pp · v1.7.131 · updated Sep 22, 2026 · md5 b7ba55724042883ce6c27a29b5b56436 — R-CONFIRM exact-version board (Grok REJECT / Gemini MINOR / Claude opus MAJOR-REVISIONS) closed most genuinely-new-real findings by real edit; NOT yet a confirmed/converged board. Three ESSENTIAL scientific-framing findings remain open by design (see DISPOSITIONS/P2.md).",
    changelog: [
      "v1.7.131: R-CONFIRM exact-version board on v1.7.130 (sha256 d3afe79fe70c..., Grok REJECT / Gemini MINOR-REVISIONS / Claude opus verdict-blind MAJOR-REVISIONS, 36 findings from the opus leg) truth-audited against DISPOSITIONS/P2.md. NOT a clean wave. Closed by real edit: missing citations (the '18% gain' RSD comparison traced to Heinrich et al. via the committed c14 script; an uncited 'existing scaling arguments' claim reworded); the r=0.8354/r_cos=0.9817 grid, weight, and formulas defined explicitly, transcribed from and verified against the committed exact_shape_analysis.py (23,098 triangles, k1=1, k2,k3 in [0.01,1], 300x300 mesh, weight S_local^2); the r=0.876 'signal-only endpoint' vs 'CMB-weighted recovery' naming harmonized; a text/code fidelity gap on the growth-factor kernel clarified (the Fisher code evaluates CAMB's P_m(k,z) directly, sidestepping the D(z)-normalization convention opus worried about); a misattributed citation for -35/16 (was citing Cai et al., whose own paper states -35/8) restricted to Li et al.; an inconsistent 'two/three/four independent certifications' count harmonized to one honest count, with Li et al.'s own internal Eq.4.19-vs-Eq.5.1 tension disclosed rather than resolved; a leaked script-name ('C14') replaced with descriptive text; Table II's 'quasi-dust' caption corrected to 'exact matter-limit (w=0)'; the +-0.02 spread on r propagated into a 2.56-2.69sigma range; the AI Usage Disclosure trimmed from two paragraphs to one; several bibliography-capitalization and wording fixes. Left open by design, not silently dropped, logged in DISPOSITIONS/P2.md: whether the -35/16 result is an independent derivation or a re-summation of trusted transcribed inputs (title/abstract framing question); whether a convention mismatch explains the discrepancy with Cai/Li's own printed polynomials (re-flag of the already-disclosed, Houston-gated DP2-25); whether the squeezed-limit projection argument applied to inflation also applies to matter-contraction; a full Fisher-ladder specification table; several smaller deferred items. 12 pp (unchanged), sha256 0e7aaf3fc46cad71f63f1d804d4993ad17a95d432076523927ff4afd3fa3dd90, md5 b7ba55724042883ce6c27a29b5b56436, tarball paper2_arxiv_v1.7.131.tar.gz rebuilt and standalone-recompiled clean. Convex disabled (spending limit) -- paperVersions:bump queued to CONVEX_BACKFILL_QUEUE_2026-09-21.md. Readiness holds 95 (computed).",
      "v1.7.130: APS-required AI-usage disclosure (P2 carried none) plus a drift-proof deposit reference — both PRD submission gates closed in one directive-G bundle. No readiness change.",
      "DOI back-patch (v1.7.126, Jul 20): embedded the minted Zenodo archival DOI 10.5281/zenodo.21461881 (concept 10.5281/zenodo.21461880) in the Data and Code Availability section, closing the standing 'archive/DOI remains a submission-time step' caveat. The record archives the exact bytes of the reviewed v1.7.125 release (11pp md5 174d52d55719c5955f852d2365fdb9c8; receipt project-context/SSOT/zenodo/P2_zenodo_receipt_2026-07-20.json). Only the version macros + availability sentence changed; no science number changed, −35/16 UNCHANGED.",
      "Dressed-metric transmission closure (v1.7.125, Jul 18): in the dressed-metric scheme the bounded bounce is TRANSPARENT to the conserved mode (T_c(k)=1); |δf_NL| ≤ 6.8e-8 at k·η_B=1e-2, more than 4 orders of magnitude below the prior order-of-magnitude reference. Effective-fluid scheme-specificity DEMONSTRATED (K-integral d_cut^-1/2 divergence, fitted -0.4998), so the transmission result is scheme-specific, not scheme-independent. Scheme label applied everywhere; AAN U(η)/deformed-algebra/third-order branch remain honestly disclosed open. Artifacts: research/cubic_bounce_transmission/g1_dressedmetric_ic_close.{py,json}. Headline −35/16 unchanged, nothing fabricated.",
      "G3 model-specific torsion bound (v1.7.123, Eq. 5): new Eq. 5 + bounded-disclosure paragraph converts assumption (f) (fermion-sourced torsion negligible) from asserted to bounded — |δf_NL^tor| ≲ (35/16)(3/16)[γ²/(1+γ²)] κ n_ψ,c²/ρ_c, sympy Einstein-Cartan four-fermion estimate anchored verbatim to the companion P1A's convention-audited axial contact term (benchmark reproduced to 0.1%). n_ψ,c carried as an explicit symbolic model parameter, never fixed. No headline number changed, −35/16 unchanged, nothing fabricated. Artifacts: research/cubic_bounce_transmission/g3_torsion_fourfermion_bound.{py,json}.",
      "directive-M presentation restructure (v1.7.116, ZERO content change): consolidated the repeated scope/caveat/proxy/illustrative statements the REJECT/minor raws named (DP2-30 presentation-scope) to canonical homes + cross-refs, relegated the cosmic-birefringence auxiliary paragraph to a new Appendix (app:birefringence), tightened the Caveats→Scope-and-limitations register. Freeze held: every number byte-identical, −35/16 quadruple-certification untouched. INT re-test: OpenAI REJECT / Grok MAJOR / Gemini MAJOR / Claude ABSENT; 0 genuinely-new editable findings, 0 regressions — residual verdicts are the documented LLM harsh-referee floor. Nothing fabricated.",
      "c15 GR-leg basis-mismatch fix (v1.7.115, INT-Claude genuinely-new MAJOR): the channel-native Fisher built ∂B/∂A_GR = b·b·b·S_GR without the M123 transfer product the f_NL primordial leg carries, leaving the GR template in potential space vs the f_NL density basis — collapsing F[2,2]~1e-18 and faking ρ(f_NL,A_GR)≈−0.001 orthogonality. Fixed (M123 promotion) + re-ran: corrected ρ=−0.42 (2×2)/−0.49 (3×3), σ_marg=0.94→2.32σ. Channel-native floor still > proxy 1.30σ floor, so the retained proxy conclusion holds. −35/16 unchanged, nothing fabricated.",
      "Per-vertex term-by-term derivation table (v1.7.105, R9 Grok+ChatGPT MAJOR): added Appendix A Table VII walking each of Cai's four cubic vertices through the squeezed AND equilateral limits (field-redef -25/16, L_zzdd -5/32, mixed 0, highest-order -15/32 squeezed), both columns summing exact-fraction to -35/16 and -255/128; transcribed verbatim from the committed sympy cert script, no new math. Plus a consolidated gauge-vs-physical-frame f_NL table (Gemini minor). -35/16 unchanged.",
      "Appendix A vertex-algebra display (v1.7.104, deep-Grok MAJOR): added the collapsed exact vertex-sum degree-9 polynomial + the epsilon-order-grouped squeezed contributions (fNL|eps^1=-5/2, |eps^2=+5/16, |eps^3=0 -> -35/16), both transcribed verbatim from the committed sympy certification script; no new math, -35/16 unchanged.",
    ],
    artifacts: [
      { label: "Read PDF", href: "/papers/02_full_draft_v1.7.131.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/02_full_draft_v1.7.131.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/research/focused_paper_source_integration/02_full_draft.tex",
        kind: "secondary",
        external: true,
      },
      { label: "Zenodo DOI", href: "https://doi.org/10.5281/zenodo.21461881", kind: "secondary", external: true },
    ],
  },
  {
    slug: "paper-2l",
    number: "2L",
    publicationRole: "Track A · A1 Letter (flagship) · Exact Non-Gaussianity",
    standaloneSubmission: true,
    title: "An Independent Confirmation of f_NL = −35/16 for Matter-Dominated Contraction",
    plainTitle: "An independent confirmation of f_NL = −35/16 for matter-dominated contraction",
    version: "v2L.0.2",
    lastUpdated: "2026-09-02",
    tldr: "Archived theory record; content folded into the A3 multi-channel paper. Retains the flagship result — f_NL = −35/16 for a matter-dominated contraction, confirmed by an independent from-scratch in-in computation that also locates Cai et al. (2009)'s −35/8 as a uniform factor-2 discrepancy (ledger #1 CLOSED, 2026-09-02) — plus the orientation-dependent squeezed limit and δN cross-check, now carried forward as a component of Track A's A3 multi-channel consistency paper rather than as a standalone submission.",
    path: publicationPath({}),
    pages: "4",
    refs: "—",
    readiness: 20,
    statusVariant: "blue",
    target: "PRD Letters (JCAP alternate)",
    description:
      "Track A's A1 Letter (2026-09-02 portfolio decision, directive R3 §3, unblocked by NEXT_SCIENCE_LEDGER.md item 1): the exact matter-contraction non-Gaussianity amplitude f_NL = −35/16, carried alone rather than inside P2's full forecast-machinery manuscript. The ledger-#1 gate — an independent second, from-scratch in-in derivation — is closed: it reproduces −35/16 and identifies Cai et al. (2009)'s published −35/8 as the same physics under a uniform missing factor of 2, not a competing result. The Letter adds a new orientation-dependent squeezed-limit calculation and a δN-formalism cross-check, and states the bounce-transmission question honestly (not assumed lossless, T=1) rather than asserting it. P2's full forecast machinery (b_φ nuisance ladder, torsion bound, dressed-metric transmission closure) stays in P2/A2, not duplicated here.",
    keyResults: [
      "f_NL = −35/16 = −2.1875 for the stated matter-dominated-contraction background and cubic action",
      "Ledger #1 CLOSED: independent from-scratch in-in re-derivation reproduces −35/16 by a second method",
      "Cai et al. (2009)'s −35/8 located as the same physics under a uniform missing factor of 2, not a competing derivation",
      "New orientation-dependent squeezed-limit result not carried in P2's original manuscript",
      "δN-formalism cross-check against the in-in result",
      "Bounce-transmission stated honestly as an open question (T=1 not assumed), consistent with A2's in-progress transmission work",
    ],
    surveys: ["DESI DR1 (current constraint σ ≈ 4.1 combined)"],
    predictions: ["f_NL = -35/16"],
    figures: ["Squeezed-limit orientation dependence"],
    remainingWork: [
      "R1 board (Fable major / Grok reject / Gemini major) truth-audited — scope decision: content folded into the A3 multi-channel paper rather than closed round-by-round as a standalone Letter",
      "Archived theory record; no further standalone submission track for this Letter",
      "See project-context/SSOT/paper-2l/status.md and PAPER_LINEAGE_2026-08-05.md for the recorded scope decision",
    ],
    preprintId: "HUBIFY-2026-002L",
    pdfMeta: "PDF · 4 pp · v2L.0.2 · created Sep 2, 2026 · md5 718521c10032511339b334ff6f277629 — archived theory record; content folded into the A3 multi-channel paper.",
    changelog: [
      "v2L.0.2: R1 (Fable major / Grok reject / Gemini major) truth-audited; scope decision recorded — archived as a theory record, content folded into the A3 multi-channel paper.",
      "v2L.0.1: first draft. Rescoped from P2 v1.7.130 (research/focused_paper_source_integration/02_full_draft.tex, 11pp) per PORTFOLIO_DECISION_2026-09-02.md §3 Track A A1, unblocked by NEXT_SCIENCE_LEDGER.md #1 (CLOSED 2026-09-02). Carries only the exact matter-contraction result, the ledger-#1 closure, the Cai(2009) factor-2 resolution, the new orientation-dependent squeezed limit, the δN cross-check, and an honest bounce-transmission statement.",
    ],
    artifacts: [
      { label: "Read PDF", href: "/papers/paper2prime_fnl_letter_v2L.0.2.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper2prime_fnl_letter_v2L.0.2.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/arxiv/paper2prime_fnl_letter",
        kind: "secondary",
        external: true,
      },
      {
        label: "Archived lineage: P2 full-length source (Zenodo DOI)",
        href: "https://doi.org/10.5281/zenodo.21461881",
        kind: "secondary",
        external: true,
      },
    ],
  },
  {
    slug: "paper-a3m",
    number: "A3",
    publicationRole: "Track A · A3 Multi-Channel Consistency (flagship submission candidate)",
    standaloneSubmission: true,
    title: "Multi-channel tests of the matter-bounce prediction f_NL = \u221235/16 and a joint (r, f_NL) no-go for single-field matter bounces at constant sound speed",
    plainTitle: "A joint tensor-and-non-Gaussianity no-go for single-field matter bounces, with a viable curvaton route",
    version: "v3M.0.30",
    lastUpdated: "2026-09-22",
    tldr: "R12 -- the one confirmation board the row-9b (LQC/poly Bardeen extension) science decision authorized -- ran on the exact v3M.0.29 PDF. Grok/Gemini API FAILED-INFRA (shared-checkout contention on a concurrent lane's files, never faked or back-filled); a Claude opus verdict-blind INT referee (no repository access outside the exact PDF) returned MAJOR REVISIONS after independently reproducing roughly forty displayed equations, all exact. 5 of 6 genuinely-new-real findings closed by real edit (two caused by this lane's own row-9b propagation: LQC's two irreconcilable linear transfers, 0.409 vs 0.500, now distinguished; 'rho+p' notation and undefined x in Sec. III A fixed); one ESSENTIAL item -- the PBH channel's headline ratio sits entirely inside the paper's own non-perturbative-branch window -- closed only by honest disclosure, not computation, and named as the next unlock. No physics error found; no headline number changed.",
    path: publicationPath({}),
    pages: "23",
    refs: "\u2014",
    readiness: 75,
    statusVariant: "blue",
    target: "PRD (regular article)",
    description:
      "Track A's flagship line (2026-09-02 portfolio decision): the A3 skeleton (research/track_a3_multichannel/) folds in the P2\u2032 v2L.0.2 exact-amplitude theory per PAPER_LINEAGE_2026-08-05.md's 2026-09-02 decision record, so the exact matter-contraction derivation and its multi-channel observational consistency checks live in one submission-track manuscript rather than split across a Letter and a research brief. v3M.0.5: R2 CLOSED (real 30-bin injection-recovery validation, Eq. (8) sigma^2 term, Omega_DM label fix, precision/label fixes, five carried R1 minors); per directive R2, rounds STOP \u2014 residue is genre/length/venue.",
    keyResults: [
      "f_NL = \u221235/16 = \u22122.1875 for the stated matter-dominated-contraction background and cubic action (c_s\u21921 limit), folded in from P2\u2032 v2L.0.2",
      "Ledger #1 CLOSED: independent from-scratch in-in re-derivation reproduces \u221235/16 by a second method; Cai et al. (2009)'s \u221235/8 located as a uniform factor-2 discrepancy, not a competing derivation",
      "New Sec. VII/VIII (D-A3-10/11): r=16\u03b5=24 exactly, ~670\u00d7 above BICEP/Keck r<0.036; joint (r, f_NL) no-go excludes single-field matter bounces jointly on r and f_NL (windows disjoint 296\u00d7 in c_s, strengthening Li et al. 2016's own no-go 3.8\u00d7); curvaton-type spectator route is the surviving (r, n_s)-viable path",
      "NANOGrav 15-yr free-spectrum MCMC: \u03b3 = 2.57 \u00b1 0.38 vs. the matter-bounce prediction 3, Savage\u2013Dickey B \u2248 3.2 for matter bounce over free spectrum",
      "New orientation-dependent squeezed-limit result and \u03b4N-formalism cross-check, folded in from P2\u2032",
      "SPHEREx/MegaMapper survey-reach channel",
      "PBH abundance channel: real compaction-function result integrated (v3M.0.3), replacing the Press-Schechter placeholder — f_PBH(−35/16) < f_PBH(−35/8) at every grid point (ratio-level result, ordering reverses relative to the first pass)",
    ],
    surveys: ["NANOGrav 15-yr free-spectrum posterior", "DESI DR1 (current constraint \u03c3 \u2248 4.1 combined)"],
    predictions: ["f_NL = -35/16, conditional on c_s->1 -- the joint (r, f_NL) no-go excludes the single-field matter bounce that would realize it unconditionally", "NANOGrav channel: null for the lab's own spectrum (gamma_pred 5.07, amplitude 14.3 dex below the signal)"],
    figures: ["NANOGrav free-spectrum \u03b3 posterior vs. matter-bounce prediction", "Squeezed-limit orientation dependence"],
    remainingWork: [
      "v3M.0.15: D-A3-10/11 science reframe (not a review round) closing ledger rows 10 and 14 -- new Sec. VII shows r=16eps=24 exactly for the modelled dust contraction, bounce-invariant to 8e-5, ~670x above BICEP/Keck r<0.036 (n_s=1 exactly, n_T=n_s-1=-0.035 the falsifiable tilt; earlier tensor-sense 'r=0.84' withdrawn as a bispectrum shape-overlap coefficient, not a tensor ratio). New Sec. VIII: r=24c_s and f_NL^pre=-165/16+65/(8c_s^2) (reproduces Li, Quintin, Wang & Cai 2016 Eq. 3.18/4.19; c_s->1 matches this paper's own -35/16 exactly); r<0.036 needs c_s<1.5e-3 (f_NL^after 6e5-9e5); |f_NL|<=5.1 needs c_s>=0.444 (r>=10.7); windows disjoint 296x -- single-field matter bounce (canonical or k-essence) excluded jointly by r and f_NL, confirming and strengthening Li+2016's no-go 3.8x. Curvaton route (Cai-Xue-Brandenberger 2011) named as the surviving (r,n_s)-viable path, but dilutes -35/16 into the bispectrum by (r/24)^2, detectable only for r>~23; CXB11's own -320/pi^4 flagged as arithmetic on their estimate, not derived. Appendix A wording fixed (pure-translation coefficient match is a numerical coincidence, not a mechanism -- a rigid isotropic translation cannot supply the monopole). Sec. V (D-A3-11): PBH sign disagreement with Choudhury et al. resolved as an IR-divergent O(eps^2) artefact, not physical; in-coverage amplitude ratio corrected to 1.84+-0.03 (was 1.732+-0.050, no longer quoted as universal). 4-pass, 0 undef refs, 0 overfull hboxes >10pt (largest 3.9pt), 17 pp, md5 4f2bf5e8204021bf06cbe27e3b8932c9, Convex bump k570ykr8ywyxmbqxpkhc630ys58dvztk. Readiness held at 75 -- one verification board (R7) permitted under directive R2's convergence budget.",
      "v3M.0.14: R6 closure -- 16 genuinely-new-real findings (0 physics errors) truth-audited and closed. Sec V C/IV D: bounce-temperature condition recomputed from the committed k_B~1.71e7*T_B[GeV] mapping (was 10^8-10^10 GeV/eleven decades, now 6e9-6e10 GeV/thirteen decades -- error made the null stronger, not weaker). Channel I: NANOGrav amplitude re-paired to the free-gamma posterior (A~6.46e-15 vs the mismatched gamma=13/3-fixed 2.4e-15); shortfall moves 10^14.3->10^15.2; Fig. 1 regenerated. Abstract calibrated to body: P+B candidate separation (0.5-1.1sigma) stated distinct from bare significance (1.0-1.3sigma); SMBH-seed FIRAS exclusion (3 dex, model-independent) separated from this model's own ~7-dex shortfall; S1/S2 stated as two distinct scheme values, not a band; PBH ratio carries its gamma_cr-grid conditionality instead of 'shape-robust'. PTA sigmas (5.1/4.9/etc.) labelled Gaussian-equivalent z-distances throughout. Sec VI gains the DESI DR1 v3 reproduction sentence (lab's own likelihood on official DESI window/covariance products: f_NL=-2.2+-25, p=1.6, 0.06sigma from the published -3.6, too weak by ~10x to separate -35/16 from -35/8 or zero; near-coincidence flagged as coincidence, not evidence; wide-angle/systematics-split caveat included). Minor fixes: DESI sign-of-comparison inversion, version-history prose removed, S2 f_NL^after clarified as cubic-order-only (linear S2/LQC transfer exists, T=0.409), sentence fragment after Eq. (7) repaired, Table VI captioned as upper bounds. Rounds stopped under directive R2; remaining open items (A3-4 r-derivation vs r<0.036, Choudhury sign disagreement, n_s shift, delta-N mechanism, DESI wide-angle corrections) moved to NEXT_SCIENCE_LEDGER.md as science decisions, not review findings. 4-pass, 0 undef refs, overfull hboxes 2.7pt/2.2pt (both <10pt), 15 pp, md5 de167ede0c3aa1ea31ded3fe9437fd82, Convex bump k57571ypt0a7rz8zx3pfj0evk58dt0pd. Readiness held at 75.",
      "v3M.0.13: abstract to cap, 15 pp -- rewritten to <=307 words (PRD-regular convention, cap used since v3M.0.6); every claim kept at its evidential strength (-35/16 in-in confirmation + located x2, S1 linear transfer bound, two-scheme transmitted band [-1.25,-0.50], three honest nulls with their numbers, LSS reach). 4-pass, 0 undef refs, 0 overfull hboxes >10pt, md5 02251c80882da4eda5fa07c92917c86d. Readiness 75.",
      "v3M.0.12: R5 truth-audit closure C1-C7 (18 genuinely-new findings closed) -- S1/S2 transfer-bound scoped to scheme S1 + assumption (A4), S2 raw-ADM T_fNL~1.03 stated; exact-mode LQC bispectrum deficit (2.1-4.4 dex) scoped to squeezed configuration at and below k_LQC eta_B~1.06 (was overstated across the full validated band); NANOGrav Omega_GW h^2(f_yr) corrected 6.3e-10 -> 3.6235e-9; editorial MINORs (sigma qualifiers, novelty claim narrowed, f_NL normalization defined, vertex-count reconciled, typography); Fig. 1 regenerated with publication labels (directive I6) + Omega_DM footnote closed; 'this lab's' neutralized; both >10pt overfull hboxes eliminated. Plus DA3M-R5-15 (first-order tensor Omega_GW at nHz -- dominates the induced background by ~6 decades but stays 8-9 decades below NANOGrav, still a null) and DA3M-R5-18 (gamma_cr grid coverage: 9/27 points below the 0.85 sign-flip scale). 15 pp, md5 6c9a16d50efe17e16ac683fdb96807ca. One verification round remains under the R2 convergence budget. Readiness held at 75.",
      "v3M.0.11: science decision D-A3-9 (ledger row 9) integrated -- transmitted amplitude restated as a two-scheme band f_NL^after in [-1.25,-0.50] (S1 geometric vs S2 fluid MS variable; S2 finite on the raw ADM Lagrangian, resolving the earlier 'S2 does not regulate' claim); Table IV gains an S2 row block (SPHEREx bispectrum-only 1.78 sigma, P+B 2.49 sigma, MegaMapper 1.25 sigma; -35/8 S2 row not computed); exact-mode LQC-dust bispectrum shows no enhancement (PBH null unchanged); velocity-dip amplification shown to equal exactly 1 on all backgrounds; an O(1) sign-indefinite transfer feature at k*eta_B~0.6-0.8 disclosed as next-steps. 14 pp, md5 56ca90f1202595c8b7ee2f91932b3c65. Readiness held at 75.",
      "v3M.0.10: R4 verification board (Fable major-revisions 5M/11m, Grok REJECT, Gemini major-revisions) truth-audited (15 real, 13 genuinely-new) and closed; science decision D-A3-3: PTA channel restated as a null (gamma_pred 5.07, Omega_GW 14.3 dex below NANOGrav). Rounds STOPPED under R2 pending a science decision. Readiness 75.",
      "v3M.0.7: real-KDE injection validation closed (Zenodo 8060824). Readiness 75.",
      "v3M.0.8: method-independent f_NL cross-check closed, bounce cubic term computed (f_NL^after in [-0.65,-0.50]), lab-own-spectrum PBH channel null. Readiness 75.",
      "v3M.0.22: S9b derivation-statement correction (research/theory_audit/psu_gate_S9b_intrinsic_term_2026_09_05.md) \u2014 Sec. II and Appendix A corrected: the intrinsic flat-slice initial-data term f^intr_NL = 5\u221a(3\u03b5)(3-\u03b5)/18 \u00b7 r_i/(W-1) vanishes in the growing-mode-dominated limit that defines -55/16, so it cannot close that gap as previously stated; the residual 5(6-\u03b5)/24 is now attributed to the super-Hubble evolution step between slices, not the initial data, and is stated as an open item. Flagship in-in monopole -35/16 unaffected. Rounds still stopped under R2.",
      "v3M.0.9: R3 truth-audit closure C1-C10 - transmitted-amplitude Table IV, delta N_c derivation appendix, induced-GW IR-slope correction, 8 numeric/definitional fixes, abstract restores PBH perturbativity/non-monotonicity caveats. Readiness 75.",
      "v3M.0.6: final-review REVISE executed (abstract 307 words).",
      "See project-context/PAPER_LINEAGE_2026-08-05.md for the recorded scope decision folding P2\u2032 theory into A3",
    ],
    preprintId: "HUBIFY-2026-A3M",
    pdfMeta: "PDF \u00b7 23 pp \u00b7 v3M.0.30 \u00b7 created Sep 22, 2026 \u00b7 md5 a1bcf35a2789ce14091e43c80f4b5b9e \u2014 R12 confirmation board (Grok/Gemini FAILED-INFRA, Claude opus verdict-blind referee MAJOR REVISIONS) found 6 genuinely-new-real items; 5 closed by real edit, 1 ESSENTIAL closed only by honest disclosure (the PBH Channel-II headline sits entirely inside the paper's own non-perturbative-branch window \u2014 named as the next unlock). No physics error found; no headline number changed. Readiness 75 COMPUTED \u2014 rounds STOPPED under directive R2 (R12 budget spent).",
    changelog: [
      "v3M.0.30: R12 (the one confirmation board the row-9b science decision authorized) ran on the exact v3M.0.29 PDF. Grok API and Gemini API FAILED-INFRA: tools/v3_native_pdf_review.py's preflight receipt generation requires every registered draft paper's inputs clean, and pipelines/p4prime_chirality_test/paper/{main.tex,main.pdf} were dirty under a concurrent, legitimately active P4P lane this lane does not own -- an attempted reversible git-stash-and-restore was blocked by the harness's own safety classifier, so no receipt was generated and no leg was faked or back-filled (same class of contention already recorded for the P-SU R4 board). Per directive I2 this did not stop the independently valuable Claude opus verdict-blind INT referee (no access to this repository outside the exact PDF), which returned MAJOR REVISIONS after independently reproducing roughly forty displayed equations and table entries, all exact. Truth-audit found 6 genuinely-new-real items. Two caused by this lane's own row-9b propagation, closed with real edits: LQC's two non-S1 linear transfers (0.409 vs 0.500) were never reconciled -- closed by distinguishing the fluid-variable handoff-at-eta_B construction from the geometric Bardeen dust-handoff construction; 'rho+p' denoted two different quantities in Sec. III A with x left undefined -- closed by writing the NEC crossing as rho+p (equiv) -2Hdot=0 with x=rho/rho_c defined at first use. Three pre-existing items closed with real edits: the T_fNL<1/2 disclaimer, scoped only to Quintin-type, extended to cover LQC/poly's new Bardeen transfers outside [0,1/2); a sign-sharing sentence given an S1 scheme qualifier; the PBH channel's 144-point/27-point ratio reconciliation arithmetic added (an aggregation of already-committed per-point data, no new computation: gamma_cr means 0.430/0.853, OLS slope -0.20 => 1.84 to 3 s.f.). One ESSENTIAL pre-existing item -- the PBH Channel-II headline 1.84+-0.03 is measured entirely inside the region the paper's own caption calls the non-perturbative branch, and the stated mechanism (large positive gamma_cr 0.766-0.968) does not apply to the headline window (gamma_cr 0.267-0.630), a materially deeper claim than any prior leg raised -- was closed only by honest disclosure (the paper now states the perturbativity diagnostic has not been pointwise-checked on the 144-point set) rather than by computation, since the proper close needs a new per-point run this lane's row-9b mandate and budget did not cover, and /never-fabricate-derivation forbids estimating it; this is the concrete next unlock. One referee claim FALSIFIED (a bracket-endpoint rounding artifact from printed vs. exact inputs). No physics error found; no headline number changed. Directive G: 4-pass, 0 errors, 0 undef refs/citations, 23 pp (unchanged), max overfull hbox 3.9pt (unchanged), /latex-audit visual PASS (pages 4, 6, 7, 8, 11, 12 rendered and inspected). Three-way md5 a1bcf35a2789ce14091e43c80f4b5b9e, sha256 0f4c5f606dc8dabf6cf08eed58d5a3b10d128f44608ef8dd8eb0b7db1603fbae. Convex paperVersions:bump + externalReviews:upsertByLabelDate QUEUED to CONVEX_BACKFILL_QUEUE_2026-09-21.md (Convex disabled, spending limit). Directive R2: budget SPENT -- rounds STOPPED; the PBH perturbativity pointwise check is the next intervening science decision candidate.",
      "v3M.0.29: row-9b (LQC/poly Bardeen extension) propagated from research/cubic_bounce_transmission/row9b_bardeen_lqc_2026_09_22/ (lane LS9-bardeen-lqc; ledger row 9b CLOSED 2026-09-19->2026-09-22, the directive-R2 intervening science decision authorizing one confirmation board, R12). The Bardeen route extends to the LQC and poly backgrounds, which cross rho+p=0 smoothly (unlike Quintin-type's jump): Phi/Phi' stay continuous, the divergence is a logarithm in the momentum sector with closed-form amplitude, and the continuation is the time-symmetric (principal-value) member of a one-parameter self-adjoint-extension family -- NOT unique (an earlier draft of the source note wrongly claimed uniqueness; retracted after an independent cross-check, given neither the construction nor its numbers, found the same non-essential-self-adjointness and confirmed both rationals by an unrelated route). Transmitted amplitude differs from S1 on all three backgrounds (background-independent in direction) but by 6.25x (Quintin, unchanged) / 2.00x (LQC) / 2.67x (poly) -- NOT a universal 6.25x, and row 9's factor must not be carried to the other two. On LQC a second, prescription-free anchor (matter-kinetic weight has no zero) gives R=1/2 independent of prescription; on poly no such anchor exists and R=3/8 is principal-value-only (an extension parameter theta=3.02 would return R to 1 and erase the effect). Table III gains two new rows: LQC and poly Bardeen linear-transfer T_fNL=0.500/0.521, cubic term not computed, f_NL^after reported ONLY as a bracket ([-1.20,-0.09] and [-1.27,-0.13]) per directive F (never a single value). AGAINST the paper (same prominence, directive F): row 18's tensor gap for LQC/poly now closes with r_after=24/R^2=96.0 (LQC) and 170.6 (poly) against S1's common 24.0 -- 2.7e3x and 4.7e3x BICEP/Keck (was 6.7e2x); the no-go strengthens on every background evaluated. Sec. VII, abstract, Discussion, and Next-steps swept for every downstream S1-range/'not yet computed' reference (the R11 lesson: a propagation that isn't swept through the whole manuscript leaves scheme-labelling MAJORs). Separately, A3M's R11 ESSENTIAL 2 (undisclosed evaluation-window convention) now closes by COMPUTATION rather than disclosure: a 12-point eta_*/eta_B scan at all three k-points (row9b_window.py) shows a stationary region common to all three, and the uniform convention eta_*/eta_B=15 sits inside it at every k, giving f_NL^after[S2]=-1.2492/-1.2490/-1.2464 (0.22% spread) -- the headline -1.25 survives to 3 sig figs with a stated 0.3% systematic; the paper's per-k f_NL^after[S2] triple updated from -1.249,-1.246,-1.244 (old non-uniform convention) to -1.249,-1.249,-1.246 (uniform convention). Symbol audit: the extension parameter is named theta, not nu, to avoid colliding with the pre-existing general-nu Hankel-limit symbol in Sec. VIII; no other collisions found. Directive G: 4-pass, 0 errors, 0 undef refs/citations, 23 pp (grew from 21), max overfull hbox 3.9pt (unchanged; one new 74pt table overflow from the added Table III rows caught by /latex-audit and fixed with \\scriptsize + shortened row labels before this commit), /latex-audit visual PASS (pages 1, 6-9, 13-15, 17-18 rendered and inspected, no column overflow). Three-way md5 8ee1f13bd4e596c87655a9347c0c0918, sha256 0c8c318e184577b614251d9d517f1cdf7d5bb9c667a6b731ca130a26b47d4a60. Convex paperVersions:bump QUEUED to CONVEX_BACKFILL_QUEUE_2026-09-21.md (Convex disabled, spending limit). R12 confirmation board (the one board R2's 'confirmation after real closure' clause permits) dispatched on this exact PDF next.",
      "v3M.0.28: R11 INT board (the one board directive R2 permitted after the row-9 (D-A3-9) intervening science decision) ran on the exact v3M.0.27 PDF (sha256 3e49f29b, md5 ea6ebd91, 21pp, three-way verified before dispatch). Legs: Grok grok-4.3 REJECT, Gemini gemini-3.1-pro-preview MAJOR REVISIONS, Claude opus INT referee (verdict-blind, no access to prior review history) MAJOR REVISIONS (2 ESSENTIAL / 6 MAJOR / 14 minor / 12 nit). No leg FAILED. Truth-audit: 16 genuinely-new-real finding-classes, all closed. (1) A recurrence of the internal-audit-language-leak defect class (directive Q1; closed twice before, DA3M-R9-04/R10-01) -- the row-9 propagation had copied working-note phrasing ('superseded', 'blind adjudication', 'committed grid/chain', 'this lab's own', 'ledger row N', 'D-A3-9') verbatim into main.tex; full scrub applied. (2) ESSENTIAL: the Bardeen-potential regularity/scheme-selection argument was asserted not derived, and inconsistent with the paper's own LQC/poly-exclusion reasoning -- closed using material the cited artifact already contains (indicial exponents {0,2} at the NEC crossing, the H=0 friction-term vanishing, and the smoothed-NEC-crossing numerical control reproducing the sharp result to 6e-5/7e-6/5e-6, gate G4 PASS), no new derivation. (3) ESSENTIAL: f_NL^after[S2]=-1.25 was quoted to three sig figs with an undisclosed, non-uniform evaluation-window convention -- closed by stating the actual eta*/eta_B convention read directly from the committed JSON (50 at the first two k-points, converged to 0.1%; 20 at the third, disclosed as less-converged), not by new computation. (4) Five MAJOR scheme-labelling/reasoning defects: abstract misattributed the S1 three-background range [-0.65,-0.50] as the LQC/poly-only retained range (actually [-0.65,-0.55]); Sec. III's 'not supported by any of these calculations' directly contradicted the paper's own S2 selection; four passages quoted S1 numbers as 'the model's own' without a label or S2 counterpart (now both added, S2 values by simple linear scaling of already-printed numbers); Sec. VI A's DESI-comparison reasoning was backwards relative to Sec. III's own framing (fixed, S2-value comparison 0.26sigma/0.64sigma added). (5) A pre-existing sign error in the PBH artefact term, Sec. V B (propto -(6 gamma_cr^2-1) not +(...), confirmed against the committed script's own verdict string) -- sign fixed, no conclusion change. (6) A symbol collision self-caught during verification: the new Bardeen-system coefficient reused mu, already the squeezed-angle cosine used throughout -- renamed to varpi. (7) Minor cluster: Table III S2-row clarified, six wrong internal cross-references repaired, Fig. 1's in-image title carried the leaked internal label 'A3-3' (regenerated from the committed generator script, re-mirrored, only the title changed -- directive I6), Fig. 1 caption now describes all four curves, abstract's ambiguous dual attribution for -35/16 dropped. FALSIFIED (source-cited): Grok's 'Bardeen construction asserted not derived' claim (the equations are printed in body text, independently re-derived and certified equivalent to the standard Mukhanov-Feldman-Brandenberger form by the Claude opus leg) and its Cai-factor-of-two claim (Sec. II C already gives the methodology in prose, independently re-evaluated from the arXiv e-print, exact match). No physics error found: the Claude opus leg independently re-derived or cross-checked ~40 numerical claims against primary literature and committed JSONs, all reproduced. No headline number changed. Directive G: 4-pass, 0 errors, 0 undef refs/citations, 21 pp (unchanged), max overfull hbox 3.9pt (unchanged), three-way md5 e4a2ca93564bc566a52e68252865c460. Directive R2: budget SPENT AGAIN -- rounds STOPPED; a further science/scope decision or Houston's authorization of a confirmation board is required. Readiness held at 75 COMPUTED; no cap-95 recommendation made.",
      "v3M.0.27: ledger row 9 (D-A3-9) science decision propagated (the intervening decision directive R2 required after the R9+R10 rounds-stop). research/cubic_bounce_transmission/row9_scheme_independence_2026_09_19/ closes the S1/S2 scalar-continuation residual: the Bardeen potential Phi obeys a z-free, 1/H-free second-order equation, regular at both H=0 and the NEC crossing rho+p=0; written as the delta-function-free first-order (Phi,Xi) system, its automatic continuity across the NEC boundaries is identically S2's junction condition. Propagated across the Quintin-type bounce it gives |lambda_zeta|=0.9699 (agrees with S2 to 7e-8, differs from S1's 6.06 by 84%); S1's z=a is exact iff eps=-Hdot/H^2 is constant (true in the matter contraction, false in the bounce window). An independent blind adjudication (different construction: the (Psi,D) system with Israel-matching junctions) confirmed S2, lambda_zeta=0.970, by a different route. Consequence, both directions propagated together per directive F: f_NL^after on the Quintin-type background is now the single value -1.25 (favorable -- was the band [-1.25,-0.50]), while r_after takes row-18a's S2 value ~9.4e2 rather than the S1 24.0 (unfavorable -- tensor no-go strengthens from 670x to 2.6e4x BICEP/Keck). Sec. III/Table III/Table VI/Sec. VII/Sec. VIII/Discussion/Next-steps updated to state S2 as selected on Quintin-type and retain S1 only where LQC/poly lack an S2 computation. Same bundle: gate-S12 general-tilt correction (research/theory_audit/psu_gate_S12_translation_trace_2026_09_19.md) to Appendix A -- the printed Appendix-A2 monopole -5eps/6 and the general-eps in-in bispectrum formula are labelled as their n_s=1 values (exact at this paper's own eps=3/2 dust construction), with the general-n_s expressions given; a general-tilt gate proves the correction cancels identically in the composed f_delta-N^init=-5 result, so no number in Sec. II or Appendix A changes. Directive I6: both figures (sigw_nhz_from_lab_spectrum, pbh_compaction_fnl) checked -- neither carries f_NL^after, r_after, or lambda_zeta, so no regeneration needed. Directive G: 4-pass, 0 errors, 0 undef refs/citations, 21 pp (grew from 20), max overfull hbox 3.9pt (unchanged), three-way md5 ea6ebd918399650702ee5a9c81182ab2. Readiness held at 75 COMPUTED. R11 INT board dispatched on this exact PDF (the one board unlocked by this decision, per directive R2).",
      "v3M.0.26: R10 CONFIRMATION board (the one permitted by directive R2 after R9 closed real items) on the exact v3M.0.25 PDF (sha256 c5fe8889, md5 d46166cb, 20pp, three-way verified before dispatch). The Gemini and Fable legs had no raw on disk from the prior session and were RE-RUN, not back-filled. Legs: Grok grok-4.3 REJECT, Gemini gemini-3.1-pro-preview MAJOR REVISIONS, Claude Fable 5.1 INT referee (verdict-blind cold read) MAJOR REVISIONS with 0 ESSENTIAL / 4 MAJOR / 9 minor / 5 nit. It did NOT confirm: 17 genuinely-new-real (4 MAJOR + 1 MAJOR-lite + 12 minor/nit), 15 FALSIFIED each with a source citation, 5 re-flags, 4 opinion/genre. MAJOR 1: Table V's two f_PBH columns were not evaluated at the rows' own (Delta, r_p k_p, C_th) labels -- rows 4-5 carried C_th=0.5 values under C_th=0.6/0.4 labels because pbh_compaction_fnl.py computes that block at C_TH_BASE=0.5, and row 1 carried the (0.5,1.0,0.4) baseline pair; re-evaluated at the labeled points with the committed functions unchanged (new artifact r10_tableV_recompute), ratio column and n=27 footer unaffected and every qualitative claim intact. MAJOR 2: the DBI 'best case r_min=12.6' was computed under |f_NL^after|<=5.1 on the Quintin background alone while the adjacent Planck-95% number uses 9.3 across three backgrounds -- two criteria colliding at 12.6; recomputed on a common criterion (new artifact r10_window_criterion) the DBI minimum is r_min=10.3 (LQC, 286x BICEP/Keck), a correction AGAINST the paper, now printed that way with the criterion and background set named. MAJOR 3: p.8 called the r=24 first-order tensor '8-9 orders' below NANOGrav while p.13 said 10^6.2 for the same pair; the arithmetic is 6.19 and the 8-9 was the tensor-vs-induced ratio -- fixed. MAJOR 4: two reproducibility citations cannot resolve (r9_perturbativity.log is gitignored and never committed; outputs/r11_pbh_residuals.json exists on no branch) -- both corrected; a third sub-finding, that origin/main does not yet carry this manuscript, is a PUSH GATE for the director, recorded open. Also closed: the title now carries the constant-sound-speed scope; seven pieces of drafting-history prose removed (directive Q1); seven raw artifact paths cleared from body text; the DOI self-instruction rewritten as a data-availability sentence; the Li Eq. (A.19) citation added for s=39/16; the printed ratio slope 0.13 corrected to the measured OLS -0.20; the 144-point composition stated; the false 'under 6 s total' wall-clock claim replaced with real per-channel times; the factor-of-two attribution softened to what print can decide. NO physics error found: every number re-checked reproduced, including a byte-identical re-run of the four sympy derivations and an independent re-derivation of Cai et al. Eq. (37) from the e-print. Directive G: 4-pass, 0 errors, 0 undef refs, 20 pp, max overfull hbox 3.9pt, three-way md5 4dcb996e0a1252e9dca3c9414a33a213. Directive R2: budget SPENT (R9+R10) -- rounds STOPPED, a scope decision is required before any further board. Readiness 75 COMPUTED; no cap-95 recommendation made.",
      "v3M.0.25: R9 INT board + closure -- the first review round since the directive-R2 stop was lifted by NEXT_SCIENCE_LEDGER row 19 (D-A3-14, 'DONE 2026-09-04 -- NO-GO GENERALISED'). Legs on the exact v3M.0.24 PDF (sha256 e0e923d6, 19pp, three-way md5-verified before dispatch): Grok grok-4.3 REJECT, Gemini gemini-3.1-pro-preview MINOR REVISIONS, Claude Fable 5.1 INT referee MAJOR REVISIONS; no leg FAILED. Truth-audit: 24 genuinely-new-real (3 MAJOR + 1 MAJOR-lite + 17 minor + 3 nit), 14 FALSIFIED each with a source citation, 2 re-flags, 2 opinion/genre; not a clean wave. MAJOR 1: the reproducibility statement pinned to commit 68309c8, and git cat-file shows NONE of the ~12 artifacts it names exists there -- both published tree URLs returned 200 only because the parent directories do -- re-pointed to the main-branch trees with the frozen-release DOI named as a required packaging action. MAJOR 2: Eq. (15) was attributed to Li+2016 Eq. (4.19) but is their Eq. (5.1), the P-propto-X^n specialization that already carries lambda, so the Sec. VIII lambda-scan double-counted lambda on the matter-contraction line; the general-lambda amplitude f_NL^pre = -245/16 + 105/(8c_s^2) - 30*Lambda is now the primary equation and every scan number is stated as measured from the Lambda=0 baseline (D-A3-14's conclusion is unchanged). MAJOR 3: f_NL^after = 1.0-1.4e11 appeared in the abstract, Sec. VIII and Table VII with no statement that tree-level control is lost 6.9 decades earlier; a new committed computation (r9_perturbativity) applies the paper's own Sec. V B criterion to give a floor c_s >~ 0.073-0.079 where r >~ 1.8 is already 49x BICEP/Keck, and independently reproduces the paper's 68% boundary as a gate. MAJOR-lite: v3M.0.19 had dropped the whole 'lambda = s = 0' qualifier when only lambda-independence was proved; the constant-sound-speed restriction is restored to the abstract and the claim sentence. Also: Planck 95% edge added as the headline (c_s >= 0.525, r >= 12.6, disjointness 350x); squeezed LQC deficit corrected 2.1-4.4 -> 3.1-4.4 dex; Sec. IV D T_B/k-eta_B pairing corrected; PTA injection test disclosed as testing bias not coverage; gamma-marginal left skew (-1.10) noted; Table V re-cited to row11_pbh_residuals; bispectrum amplitude A, T_3/T_4, s, and p all defined; drafting-history parenthetical removed (Q1); four internal ledger/lane labels and nine raw artifact paths removed from prose; abstract re-trimmed 341 -> 307 words; four disclosed limitations added to Sec. IX. Found during closure, not by any leg: the committed v3M.0.24 .tex did not compile at all on a clean toolchain (raw Unicode rho), so the served PDF was not reproducible from its own source -- fixed. Directive G: 4-pass, 0 errors, 0 undef refs/citations, 20 pp, max overfull hbox 3.9pt, three-way md5 d46166cb88b32009cdc6be59bb620547, tarball standalone-compiled clean (sha256 403f6b1f). Readiness 75 COMPUTED -- the one confirmation board permitted by R2 is the remaining gate.",
      "v3M.0.24: A2 lapse-monopole gap reconciled (research/theory_audit/a2_lapse_monopole_adjudication_2026_09_07.md). Sec. II and Appendix A: the earlier 'not reconciled / open item' wording on the uniform-density f_NL^rho gap is replaced. A2=eps(3-eps)^2/3 stands as the correct constraint-solve value (not 2(3-eps)^2). The uniform-density delta N value is f_NL^rho=5(eps-7)/8=-55/16 at dust, obtained by correcting the composition weight on the second-order curvature perturbation from lambda'=2lambda to 3lambda; this closes the 15/16 gap to the earlier initial-label figure -5/2 exactly. The in-in monopole -15/8, the comoving-slice delta N value -5, and the uniform-density delta N value -55/16 are now stated as three well-defined variables related by exact threading maps, not competing claims. Flagship in-in monopole -35/16 unaffected; no new math. 4-pass, 0 undef refs, max overfull hbox 3.9pt, 19 pp, md5 b29ebb90be09f8d0bbc3875647bb150a. Readiness held at 75 \u2014 rounds still stopped under R2.",
      "v3M.0.23: S9c derivation-statement update (research/theory_audit/psu_gate_S9c_evolution_residual_2026_09_05.md) \u2014 the v3M.0.22 hypothesis that the -55/16 gap arises from a dropped super-Hubble evolution term is NOT supported: an independent exact separate-universe solution reproduces both -55/16 (uniform-density) and -5 (comoving) for all \u03b5, so both delta N values are well-defined variables. Sec. II and Appendix A corrected: the 15/16 gap is relocated to the second-order threading map's long\u00d7short lapse monopole coefficient A2=\u03b5(3-\u03b5)^2/3 versus the separate universe's required 2(3-\u03b5)^2; which coefficient is correct is under independent adjudication, not yet resolved. Flagship in-in monopole -35/16 unaffected. Rounds still stopped under R2.",
      "v3M.0.22: S9b derivation-statement correction (research/theory_audit/psu_gates_S9_S10_2026_09_05.md). Sec. II cross-check paragraph and Appendix A (Bianchi-I subsection) no longer state the uniform-density delta N value -55/16 is reconciled by the threading-map identity: a direct second-order continuation of the uniform-density (rho-slice) variable itself gives f_NL^rho=5(2eps-15)/24=-5/2 at dust (isotropic), which does NOT reproduce -55/16 (gap 15/16); the residual is attributed to an intrinsic flat-slice initial-data bispectrum omitted from that delta N integration (Namjoo-Firouzjahi-Sasaki non-attractor caveat), not to a slice-labelling error. Only the comoving-slice delta N value (-5) is fully reconciled by the map; the flagship in-in monopole -35/16 is unaffected. Rounds still stopped under R2. 4-pass, 0 undef refs, 0 overfull hboxes >10pt, 18 pp, md5 91d5a6511eb0169054855b5fae85960e. Readiness held at 75.",
      "v3M.0.17: D-A3-12 (ledger row 18) -- SVII: the tensor mode has no 1/H, eps, c_s, or scalar constraint variables, so the S1/S2 scalar-continuation ambiguity cannot touch it; because the S1 scalar equation with z=a IS the tensor equation, lambda_T = lambda_zeta^S1 identically (1.4e-14 on Quintin-type, 8.5e-9 on poly/LQC) -- r_after^S1=24.0 is an identity, r_after^S2~9.4e2 (39x bounce amplification), both excluded (670x, 2.6e4x), scheme-independent conclusion. SVIII: the bounce's own cubic term generalizes to Delta f_NL^bounce(c_s) = -(5/24) rho_B (6c_s^2-5)/c_s^4 (99.97% from the zeta-zetadot^2 vertex, reproduces c_s=1 to 4e-6), sign flip at c_s=sqrt(5/6)=0.913, diverging as 1/c_s^4 vs the transmitted term's 1/c_s^2; evaluated at the same c_s the Planck-viable boundary moves from c_s>=0.444 (r>=10.7) to c_s>=0.600 (r>=14.4), windows now disjoint by ~400x (was 296x); at the tensor-viable c_s=1.5e-3, f_NL^after rises from ~7e5 to ~1e11. Abstract updated (302 words). 4-pass, 0 undef refs, 0 overfull >10pt (largest 3.9pt), 18 pp, md5 b18aafd1288ffddeea2c3a1ee074a23b, tarball sha256 f37ff2e050c6b03349fe0e22c5871caeb2f5f05b3620bed5029fe5ba4c47eba4 (standalone smoke test PASS), Convex bump k5773fexyjhsy11m8gpd4j01xn8dt1fj. Readiness held at 75 -- D-A3-12 taken, one verification board (R8) permitted.",
      "v3M.0.16: R7 truth-audit closure -- 16 genuinely-new-real findings (0 physics errors beyond scoping + one stale figure). R7-01 scoped r=16eps=24 to scheme S1 (S2 raw-ADM gives r_after~9.4e2, worse not cured); R7-02 regenerated Fig. 1 (stale NANOGrav amplitude A=2.4e-15 -> current A=6.46e-15) + fixed an x-axis tick collision; R7-03 disclosed the c_s=0.8876 sign flip (k-essence branch positive on [0.444,0.888)); R7-04 disclosed the quoted window used T*f_NL^pre(c_s) only, without Delta f_NL^bounce's own c_s-dependence (ledger item A3-cs-bounce, closed in v3M.0.17 above); R7-05 rebuilt the CaiXue2011 bib entry + added 3 refs; R7-06/07 label/scope fixes; R7-08 Table V non-perturbative-branch labelling; R7-09 reconciled a stale tensor-nHz shortfall (10^5.3 -> 10^6.2); R7-10/11 removed repo-path framing + residual version-history prose (directive Q1); R7-13/14/15 dropped a false QCD-scale claim, marked the Cai conversion as 'effectively' exact, restated the six-permutation alternative; Appendix A replaced 'translation coincidence' wording with the label-resolved exact-change-of-variable statement. 4-pass, 0 undef refs, 0 overfull hboxes >10pt, 17 pp, md5 5544bea1dba2db64f25e85d476489ce4, tarball sha256 69d9178f24b6b8a3a292e3d579ec6c8a1c7834de574d31d9499b15c7e375914e, Convex bump k57421pb671psc0vbbxm8zkc698dt1ga. Readiness held at 75.",
      "v3M.0.15: D-A3-10/11 science reframe -- see remainingWork above for full detail. Joint (r, f_NL) no-go for single-field matter bounces integrated; curvaton route named; PBH sign resolved. md5 4f2bf5e8204021bf06cbe27e3b8932c9, Convex bump k570ykr8ywyxmbqxpkhc630ys58dvztk. Readiness held at 75.",
      "v3M.0.14: R6 closure -- see remainingWork above for full detail. 16 genuinely-new-real findings closed, 0 physics errors. md5 de167ede0c3aa1ea31ded3fe9437fd82, Convex bump k57571ypt0a7rz8zx3pfj0evk58dt0pd. Readiness held at 75.",
      "v3M.0.13: abstract to cap, 15 pp. Abstract rewritten from ~415 words to exactly 307 words (PRD-regular convention). No science changes; every quantitative claim retained (-35/16 in-in confirmation + located Cai x2, S1 linear handoff bound, two-scheme transmitted band f_NL^after in [-1.25,-0.50], three honest nulls: PTA gamma_pred=5.07 at ~10^14 below NANOGrav + first-order tensor 8-9 decades below, PBH ratio 1.7-1.9 / 6.7-7.0 dex short, SMBH-seed high-z 3 dex short; LSS reach S1 0.7-0.9sigma / S2 1.78sigma SPHEREx bispectrum-only). 4-pass, 0 undef refs, 0 overfull hboxes >10pt, md5 02251c80882da4eda5fa07c92917c86d, Convex bump k57akjqq9tz75xh8kd16tq6t058ds6m7. Readiness held at 75.",
      "v3M.0.12: R5 truth-audit closure C1-C7 (18 genuinely-new findings: 3 MAJOR + 15 MINOR) on the exact v3M.0.11 PDF (Grok REJECT 3E/3M/2m/2N, Gemini major-revisions 4E/3M/1m/1N, Claude Fable INT major-revisions 5M/16m). Abstract + Sec. III: S1 transfer bound tagged (scheme S1, assumption (A4)); S2's raw-ADM continuation stated (T_fNL~1.03, |lambda_zeta|=0.97); 'S2 has no computable f_NL^after' scoped to the LQC background specifically (S2 IS computed on Quintin-type); per-background table gains a caption+label+S2 row. Sec. III: exact-mode LQC bispectrum deficit (2.1-4.4 dex) scoped to squeezed configuration at and below k_LQC eta_B~1.06 (was advertised across the full validated k*eta_B in [0.1,10]); new Table sourced directly from lane9c2_lqc_modes/results.json. Sec. IV: NANOGrav Omega_GW h^2(f_yr) corrected 6.3e-10 -> 3.6235e-9 (matches the committed JSON exactly); first-order tensor result DA3M-R5-15 inserted (dominates the induced background by ~6 decades at the CMB bound r<0.036, but stays 8-9 decades below NANOGrav either way -- Channel I remains a null). Sec. V: DA3M-R5-18 inserted into Table V's caption (27-point grid's 9 distinct gamma_cr span [0.766,0.968], 9/27 points below the 0.85 sign-flip scale; the model's own spectrum shape sits outside that coverage). 13 editorial MINORs closed (body sigma qualifiers unified to 0.5-1.1sigma, novelty claim narrowed to per-vertex attribution, f_NL^rho/f_NL^c normalization defined, 'all five' vs 'all six' vertex-count reconciled, O(1)->0.06-2.2 reworded, 'apparent tension'->'forecast detection significance', typography fixes, Table II 'not directly comparable' qualifier added). Fig. 1 regenerated with publication-quality labels per directive I6 (no internal 'A3-3'/branch-name labels), numerically verified identical to the committed JSON; Omega_DM=0.674 footnote residual closed with a quantified factor-2.55 statement. 7 in-body 'this lab's' occurrences neutralized to 'this model's'/'this program's'. Both >10pt overfull hboxes eliminated (Eq. gammapred split into a gathered display; App. A.2 table columns narrowed). 4-pass, 0 undef refs, 15 pp (grew from 14), md5 6c9a16d50efe17e16ac683fdb96807ca, sha256 ad63d5ee0d67946c34c610a0e9985fe10973f798bc344800c8de2241e58605af, tarball sha256 931c3afd6bbebb8aaf6a927bff388cbc440a726ec68813677789fcb70f0a3622, Convex bump k5727mwmdrc3rdv2w89fx4j3jx8drnh0. One verification round remains under directive R2's convergence budget. Readiness held at 75.",
      "v3M.0.11: science decision D-A3-9 (ledger row 9, recorded in PAPER_LINEAGE before editing). Sec. III: the S2 apparent divergence is shown to be a total-derivative artefact of the Maldacena/Chen integrated-by-parts cubic form; on the raw ADM cubic Lagrangian exact S2 modes give a finite bounce-window integral (residue cancellation, no cutoff needed) -- f_NL^after[S2] = -1.249,-1.246,-1.244 vs S1's -0.501 (factor ~2.5, dominated by the linear MS-variable choice). The Agullo-Bolliet-Sreenath LQC cubic-operator claim is corrected (all nine operators map onto S1's vertex table); exact LQC-dust modes show no enhancement counterpart (2.1-4.4 dex below their plateau). Table IV gains an S2 row block (SPHEREx bispectrum-only 1.78 sigma, P+B 2.49 sigma, MegaMapper 1.25 sigma; -35/8 S2 row not computed). Velocity-dip amplification shown to equal exactly 1 on all three backgrounds. Abstract restates the transmitted amplitude as the two-scheme band. 4-pass, 0 undef refs, 14 pp (grew from 13), md5 56ca90f1202595c8b7ee2f91932b3c65, tarball sha256 da60e774..., Convex bump k57ag2aq3hs95mvqdkfp3jv9k18dszee. Readiness held at 75.",
      "v3M.0.10: R4 verification board on the exact v3M.0.9 PDF; truth-audit 30 raw -> 15 outstanding real (13 genuinely-new), all editorial items closed (S2-scheme exclusion stated beside the transmitted range; Eq. (6) defined; ref. title fixed; abstract reach consistent with Table IV; gamma=2 causal-floor row; Q1 sweep; Omega_DM footnote). Science decision D-A3-3 (ledger A3-3): the lab's own spectrum propagated to nHz through the validated Kohri-Terada kernel gives gamma_pred = 5.07 and Omega_GW h^2(f_yr) = 1.45e-23, 14.3 decades below NANOGrav -- Channel I restated as a null, gamma=3 attribution withdrawn; SIGW null-panel figure added; Discussion: three honest nulls (PTA, PBH, PNG high-z abundance) + one reachable-but-unseparable channel. 13 pp, md5 d3981d8b5ed2cbf6b02bd771f784ee1c. Rounds stopped under R2.",
      "v3M.0.9: R3 truth-audit closure (C1-C10). C1(a) PROPAGATE: k*eta_B<=1e-2 stated as an upper bound on k, satisfied most easily at the LSS/CMB pivot; Table IV gains f_NL^after rows (0.7-0.9sigma / 1.2-1.7sigma at SPHEREx bispectrum-only, under 1sigma separation between -35/16 and -35/8); abstract/Discussion/Sec. VI-VII rewritten to headline the transmitted amplitude. New Appendix A transcribes the delta N_c-zeta_Mald derivation (no new science). Induced-GW IR-slope corrected: causal floor is Omega_GW~f^3 (gamma=2, Cai-Pi-Sasaki PRD 102, 083528 (2020)), not f^2; gamma=3 here follows from the bounce's broad near-scale-invariant source (Papanikolaou Eq. 30+8). Numeric fixes: 19-39% (was 28-39%), n_s-1=12w/(1+3w) (was inverted), 0<=T_fNL<1/2 (was inverted). Eight definitional/labelling fixes; directive-Q1 revision-history sweep; Cai-bookkeeping equation numbers added (Li Eq. 4.19/5.1). Abstract restores the PBH perturbativity and non-monotonicity caveats dropped in v3M.0.8 (304 words). Readiness held at 75.",
      "v3M.0.7: real NANOGrav 15-yr KDE grids fetched from the public Zenodo record 10.5281/zenodo.8060824 (30f_fs{hd}_ceffyl, sha256-verified) and mirrored to HuggingFace (bamfai/bigbounce-aug-011-clean-rerun, external/nanograv15yr_kde/); Sec. IV C injection-recovery re-run with real per-bin KDE curves re-centered on the injected truth: \u03b3=13/3 mean pull +0.016\u03c3, \u03b3=3 control mean pull +0.033\u03c3 (5 realizations each), superseding the synthetic-density placeholder (retained as secondary cross-check). Readiness 75.",
      "v3M.0.8: Sec. II closed by a method-independent (classical O(k^0) super-Hubble / Bianchi-I shift-decomposition) confirmation of f_NL=-35/16; Sec. III adds the bounce's own computed cubic term, giving f_NL^after in [-0.65,-0.50] (scheme S1, three backgrounds); Sec. IV adds a new subsection feeding the lab's own predicted Delta^2_zeta spectrum into the PBH compaction channel — a clean null, 7.0 dex short of the required amplitude at every mass scale, with the required-amplitude ratio widened to 1.7-1.9 and a FIRAS check on the early-SMBH-seed channel. Abstract and Discussion updated to match; the LSS reach table (Sec. VI) intentionally not recomputed at f_NL^after since the CMB/LSS pivot scale lies outside the established k*eta_B<=1e-2 transmission-validity band. Readiness held at 75.",
      "v3M.0.5: R2 CLOSED \u2014 real injection-recovery test at gamma=13/3 and gamma=3 through the same 30-bin free-spectrum likelihood/priors replaces the misdescribed prior injection claim (mean pull -0.026sigma / +0.068sigma over 5 realizations each); Eq. (8) sigma^2 term restored; Omega_DM=0.674 footnoted as Planck h (cancels in the ratio); precision/label fixes; five carried R1 minors closed. Rounds stop per directive R2 (convergence budget 2/2 consumed); residue is genre/length/venue only.",
      "v3M.0.4: R1 closed (official NANOGrav posterior primary; handoff-conditional transmission bound; PBH ratio with regime disclosed). R2 verification pass dispatched (Fable + Grok + Gemini) \u2014 verdicts pending.",
      "v3M.0.3: PBH compaction-function channel (item A3-1) integrated, replacing the Press-Schechter placeholder row; ordering reverses (f_PBH(\u221235/16) < f_PBH(\u221235/8) at every grid point). R1 INT board dispatched (Fable + Grok + Gemini) \u2014 verdicts pending.",
      "v3M.0.2: A3 skeleton + P2\u2032 v2L.0.2 exact-amplitude theory folded in per PAPER_LINEAGE_2026-08-05.md; ledger #1 stated as closed.",
      "v3M.0.1 and earlier: A3 multi-channel first-pass skeleton (research/track_a3_multichannel/) \u2014 NANOGrav \u03b3, PBH abundance, SPHEREx/MegaMapper reach; not yet registered as a site paper.",
    ],
    artifacts: [
      { label: "Read PDF", href: "/papers/a3_multichannel_arxiv_v3M.0.30.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/a3_multichannel_arxiv_v3M.0.30.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/research/track_a3_multichannel/paper",
        kind: "secondary",
        external: true,
      },
      {
        label: "Folded-in theory: P2\u2032 Letter (archived theory record)",
        href: "/papers/paper-2l",
        kind: "secondary",
      },
    ],
  },
  {
    slug: "paper-3",
    number: "3",
    publicationRole: "Supporting Data Release · DESI Public-ID Recovery",
    standaloneSubmission: false,
    title: "Public-ID Recovery for a Historical DESI DR1 Anomaly List: 170 High-Coordinate-Consistency Core and 11 Lower-Confidence Positional Associations",
    plainTitle: "Supporting data release: public DESI IDs for the anomaly program's follow-up list",
    version: "v3.2.0-r17",
    lastUpdated: "2026-08-03",
    tldr: "Publishes 181 public DESI DR1 TARGETID associations for the anomaly program's candidate list, split transparently into 170 high-coordinate-consistency core associations and 11 lower-confidence positional associations. v3.2.0-r17 binds the viewer captures, documents the exact 2,468-row positional-parent denominator, publishes the two-pass deduplication order, and content-hashes every resumable scan input — deterministic public-identifier and join/checkpoint machinery enabling auditable follow-up. This is a public-identifier and provenance data release, not a detection claim.",
    path: publicationPath({}),
    pages: "17",
    refs: "12",
    readiness: 95,
    statusVariant: "amber",
    target: "Integrated supporting release for the rebuilt DESI anomaly flagship",
    description: "A focused, reproducible public-identifier and provenance data release for the anomaly program's historical candidate list. Deterministic join and checkpoint machinery ties each candidate to a public DESI DR1 TARGETID, enabling auditable independent follow-up. The declared 1-arcsec positional join yields 181 warning-free global-primary DESI DR1 associations: 170 at or below 0.1 arcsec and 11 lower-confidence associations between 0.1 and 1 arcsec. The sub-0.1-arcsec core is expected seed self-recovery — the cluster centroid equals the seed DESI member's own coordinates by construction, verified end-to-end rather than an independent association test. The aggregate annular shift comparison is descriptive, not a conditional false-association null or purity estimate. The release carries exact source-row provenance, explicit quality tiers, warned-row auxiliary data, checksums, and a clean-checkout validator while declining physical classification, purity, novelty, and anomaly-rate claims unsupported by the underlying historical candidate list.",
    keyResults: [
      "181 unique warning-free global-primary DESI DR1 TARGETIDs, partitioned exactly into 170 core and 11 lower-confidence positional associations",
      "20,299,155 eligible DESI rows → 2,468 positional parents → 2,448 global-primary rows → 181 warning-free associations",
      "Every released row and all 18 carried DESI fields were re-read from the recorded FITS row and compared exactly",
      "Sixteen deterministic local shifts yield 86.7 ± 14.4 parent and 76.2 ± 13.3 warning-free-primary associations within 1 arcsec; the 11-row tail is not treated as secure identity",
      "A separately released 2,267-row warned auxiliary table preserves inspectability without admitting warned rows to the primary catalog",
      "Original-member sensitivity retains 180/181 rows; only P3-DESI-000030 fails the alternate 1-arcsec rule at 1.979009 arcsec",
      "The definitive bundle contains 41 tracked files and passes exact clean-tree validation of all 38 manifest payloads",
      "r7 board: Grok direct API ACCEPT, Gemini direct API MINOR, Codex ChatGPT-subscription MAJOR; exact r8 subscription confirmation: ACCEPT with zero in-scope blockers",
      "Claude-leg exact-PDF board on r8: MINOR (1 MAJOR / 7 MINOR); truth audit: 0 falsified, 4 bounded editorial items, closed same-day in r9",
      "Exact v3.2.0-r9 confirmation board: Grok ACCEPT (its first) / Gemini MINOR / Claude MAJOR; truth audit CONFIRMED the Claude circularity finding as genuinely-new-real — the sub-0.1-arcsec core excess is by-construction seed self-recovery (median match sep 0.00127 arcsec, target-to-member sep zero)",
      "v3.2.0-r16 exact core-conditioned audit: all 18,134,821 strict FITS rows scanned; 0/170 core clusters contain an additional 0.1-1 arcsec target, 0 hidden-nearest cases, and 0 annular matches across all 16 shifted core controls; the aggregate deficit has no assigned causal mechanism",
      "v3.2.0-r17 exact-final closure: 20 viewer captures are path/hash/status-bound; 2,287 exclusions are explicitly from the 2,468-row positional parent; the two deduplication key orders are exact; checkpoint resume binds all three input SHA-256 digests",
    ],
    surveys: ["DESI DR1"],
    predictions: ["Public-ID recovery", "Coordinate-association quality tiers", "Archive reproducibility"],
    figures: ["Selection waterfall", "Separation distribution", "Shift-control radius curves", "Catalog sky distribution"],
    remainingWork: [
      "Run bounded confirmation against the exact v3.2.0-r17 PDF after the denominator, deduplication-specification, checkpoint-digest, and viewer-binding closures",
      "Bind this release and its immutable archive lineage into the rebuilt anomaly flagship; it is not selected for a standalone journal submission",
      "Reconcile the published Zenodo lineage (10.5281/zenodo.21461888) with the rebuilt flagship's archive; any future journal data DOI belongs to that integrated release path",
      "Revalidate the source/data bundle when it is incorporated into the rebuilt flagship; no standalone P3 portal submission is planned",
      "Object-level physical interpretation and any representative-control performance study remain separate new-science work",
    ],
    preprintId: "HUBIFY-2026-003",
    pdfMeta: "PDF · 17 pp · v3.2.0-r17 · updated Aug 3, 2026 · md5 477b0d83ca31f6ace3273bb19bcfcf34 · sha256 9a3769269ada4d2a5371aa447e6ce93aa55518ae2a3b13fdc3d83f0b8b779a0b — exact denominator, deduplication-order, checkpoint-digest, and viewer-binding closures included; exact r17 confirmation remains pending.",
    artifacts: [
      { label: "Read PDF", href: "/papers/paper3_apjs_v3.2.0-r17.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper3_apjs_v3.2.0-r17.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p3_anomaly_engine/paper3_apjs.tex",
        kind: "secondary",
        external: true,
      },
      { label: "Zenodo DOI", href: "https://doi.org/10.5281/zenodo.21461888", kind: "secondary", external: true },
      {
        label: "r9 confirmation board truth audit",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/project-context/peer-reviews/INT_v3/ROUND_2026-07-16-P3-v3.2.0-r9-EXACTPDF-7526e685-CLAUDESTACK-CONFIRM/P3_v3.2.0-r9_truth_audit.md",
        kind: "secondary",
        external: true,
      },
      {
        label: "Checksum-bound release bundle",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/d155eb27488b271be12942b1a1be8b3c39dd24f4/pipelines/p3_anomaly_engine/desi_science_catalog_v3.2.0-r2",
        kind: "secondary",
        external: true,
      },
    ],
  },
  {
    slug: "paper-4",
    number: "4",
    publicationRole: "Lead Catalog Paper · Observed-Label Chirality Null",
    standaloneSubmission: true,
    archivedInto: {
      note: "Folded into P4′, the Track C1 chirality test (v4P.0.1), with P5 folded in as one section — 2026-09-02 portfolio restructure, directive R3. Every P4′ number is quoted verbatim from this reviewed v1.0.274 source; the catalog pipeline was not re-run.",
      successorSlug: "paper-4p",
      zenodoDoi: "https://doi.org/10.5281/zenodo.21461899",
    },
    title: "An Observed-Label Chirality-Dipole Null in 890,069 Quality-Controlled High-Confidence DESI Spirals and an 8.5-Million-Galaxy Catalog",
    plainTitle: "Do spiral galaxies' apparent handedness directions cluster? An 8.5M-galaxy test (result: no dipole)",
    version: "v1.0.274",
    lastUpdated: "2026-08-03",
    tldr: "Classifies 8.47M galaxies. The strict safe-sample observed-label statistic remains null-consistent (z=0.63465, p=0.23768), and the v1.0.268 CE-composition audit retained the GZ1-core realization while documenting the honest-negative CE-inclusive retrain. v1.0.274 expands Expected Calibration Error (ECE) at first use without changing the science; exact confirmation and Houston review remain separate gates.",
    path: publicationPath({}),
    pages: "32",
    refs: "18",
    readiness: 95,
    statusVariant: "amber",
    target: "The Astrophysical Journal Supplement Series",
    description: "The galaxy chirality catalog: 8.47M galaxies classified CW/CCW by a ViT-Small ensemble with flip-equivariant TTA. Two real-compute pod-campaign closures land in v1.0.268. (1) G1 manifest-retained ViT retrain COMPLETE on RunPod A4000 (<$1 total): trained on 8,637 objects (6,637 GZ1-core + 2,000 synthetic; ce_resnet_present=false — the Jia CE-ResNet catalog still needs external re-provisioning, so the 826-vs-846 sub-conflict stays open and released Catalog C labels are UNCHANGED), every object ID/split/seed retained in the committed manifest, best_val_acc=0.9931 at epoch 47, checkpoint backed up to 3 verified locations. (2) G2 training-disjoint validation: accuracy=0.9867 / Cohen's kappa=0.9733 on 3,000 GZ1 confident spirals disjoint on both the object-ID and label-source axes (overlap counts 0), presented with an explicit like-for-like distinction vs the historical kappa=0.40 human-vote figure — a genuinely different measure, not a replacement for it. Caveat sites narrowed honestly at abstract/intro/discussion/conclusions/data-availability. No science number changed; the primary remains null-consistent and harmonic results remain systematics diagnostics only. CE-ResNet re-provisioning, the MASTER-decoupled/full-likelihood covariance legs, complete metadata, a DOI-backed archive, exact v1.0.268 confirmation, and human review remain open.",
    keyResults: [
      "8.47M galaxies classified (1,592,107 CW / 1,609,053 CCW / 5,273,371 NOT_SPIRAL)",
      "Strict release-safe primary: N_selected=890,069, N_support=887,472, z_mom=+0.63465, one-sided empirical-rank p=0.23768",
      "G1 manifest-retained ViT retrain: 8,637 objects (6,637 GZ1-core + 2,000 synthetic; CE-ResNet component absent pending external re-provisioning), every object ID/split/seed retained, best_val_acc=0.9931 @ epoch 47, checkpoint backed up to 3 verified locations — proves the exact training realization is regenerable",
      "G2 training-disjoint validation: accuracy=0.9867 / Cohen's kappa=0.9733 on 3,000 GZ1 confident spirals disjoint from G1 training on both the object-ID and label-source axes (overlap counts 0); presented like-for-like against, and explicitly NOT as a replacement for, the historical kappa=0.40 GZ1 human-vote inter-rater figure — a different measure (model-vs-independent-labels agreement, not human-vote agreement)",
      "Coverage-calibrated OBSERVED-LABEL 95% sensitivity upper limit on the primary dipole: A_95^obs~=0.98% (linear-interp; logistic cross-check 0.955%), from 2,000 random-axis injections/amplitude through the exact primary estimator + exact fixed-occupancy null; NOT a physical parity-amplitude bound (that remains gated on the morphology transfer function)",
      "Exact 24,087-pixel FSC support: fixed-occupancy harmonic z=6.923, p=0.001996; apodized z=7.033; 10,000-draw binomial z=7.207, p=0.00059994; systematics diagnostics only",
      "Corrected public ApJS bundle: immutable HF data commit db110233 contains the safe catalog, 249,066-row quarantine, fixed-occupancy primary array f6360f4b, distinct pixel-permutation diagnostic 62bb1c01, manifest, schema, checksums, and reproducer; receipt e535b262 verifies remote paths and byte sizes",
      "Release-integrity closure: HF dataset revision 43fc8a5b publishes the complete clean-bootstrap semantic contract; HF model revision 6f113097 publishes the production-accurate model card",
      "Catalog C semantic validation streams all 8,474,531 primary and 249,066 quarantine rows and proves exact object-ID/HC-flag equivalence with zero failed gates; Catalog B remains historical and unreleased",
      "Galaxy Zoo 1 human-vote cross-check: 46,017 matched inputs, exactly 4,963 on the 394-pixel N_pixel>10 support and 41,054 excluded; null-consistent at z=−0.539, p=0.666 under its legacy pixel-permutation convention",
      "ℓ=1 MASTER decoupling numerically stable: full coupling-matrix condition number 3.17 (3.11/3.25 at 1°/3° apodization)",
      "Bin-by-bin CW flatness audited across 4 morphology axes; residuals are classification correlations, orthogonal to dipole tests",
      "Finite-grid injection pilots (20 axes, 100 injections/amplitude) report score-pass fractions only and do not themselves establish calibrated recovery thresholds; the separately-computed 2,000-axis A_95^obs upper limit above supersedes them for the observed-label sensitivity floor, but establishes no physical bound",
      "Edge-on TTA equivariance check: CW fraction 0.4975 ± 0.0006 on 785,859 edge-on galaxies, indistinguishable from catalog-wide",
      "Platt calibration: raw +0.79%/28.8σ → calibrated +0.4%/14.6σ → equivariant -0.26%/9.5σ",
      "Equivariance suppression factor 2.98× (raw +1.58% → equivariant −0.53% in asymmetry-A units; +0.79% → −0.26% in f_CW units)",
      "Harmonic injection scores are pipeline-response diagnostics on a different field, support, and null; they are not calibrated completeness or physical exclusions",
      "Hemisphere look-elsewhere null: p_LEE < 10⁻⁴ (0/10,000 MC nulls reach data)",
      "100,000-bootstrap CW/CCW asymmetry: A_obs=1.5757%, 95%CI=[1.471%, 1.685%], σ_stat = 28.80σ",
      "Two support-bound FS-C diagnostics show apodization robustness and broadband low-ℓ structure; six different-support or support-unproven calculations are excluded from the strict synthesis",
      "No physical or primordial amplitude bound is claimed; matched-footprint independent-estimator analysis and a spatial transfer model remain open",
      "R25conf round 2-of-2 CLEAN (93 findings audited); one substantive catch — App A field-convention description corrected from artifacts, no number changed (v1.0.170)",
      "Pod recompute wave: unthresholded-sample injection floors A50=0.36% / A95=0.63% (the 0.57% excess sits between — honest disclosure); area-uniform axis curve P3σ=0.59 @ 0.75%; threshold sweep reproduces canonical exactly; T7 quantified by confidence (0.267 vs 0.383); training-acc semantics corrected — 93.7% = 3-class val, 94.9% = CW per-class (v1.0.171)",
    ],
    surveys: ["DECaLS / DESI Legacy DR8 (8.47M galaxies)"],
    predictions: ["Parity test (indirect bounce test)"],
    figures: ["Chirality sky map", "Hemisphere null", "Bias audit results", "Class pie (canonical text counts)"],
    remainingWork: [
      "Run bounded confirmation against the exact v1.0.274 PDF; earlier review evidence is not a verdict on this hash",
      "Freeze and validate full-catalog imaging-leg, depth, seeing, PSF, and redshift metadata; the exact morphology join is now public but these fields remain unavailable",
      "Complete systematics-metadata sidecar: the DOI back-patch (v1.0.269) closed the archive/DOI gate itself, but the separate complete systematics-metadata sidecar remains honestly open",
      "Re-provision the Jia et al. 2023 CE-ResNet high-confidence spiral catalog (pre_desi.fits; external source, GitHub h3jia/galaxy_spin_classifier / NADC China-VO) to engage the CE-non-spiral 826-vs-846 sub-conflict and complete the full historical-realization training component; released Catalog C labels are unaffected",
      "Extend the computed 3x3 joint covariance to the MASTER-decoupled leg and full joint likelihood; run the G4 monopole-mechanism injection (H200, now unblocked by the completed G1 retrain); derive the morphology transfer function needed to convert A_95^obs into a physical parity-amplitude bound",
      "Author arXiv endorsement and journal-submission decision",
    ],
    preprintId: "HUBIFY-2026-004",
    pdfMeta: "PDF · 32 pp · v1.0.274 · updated Aug 3, 2026 · md5 6c7de2b81dfa3d7af2a7414214d57cfc · sha256 2641a228af1e3decf17d18341570c4e779483a823267421fe041aade1375e0d7 — Expected Calibration Error (ECE) expanded at first use; no scientific claim, number, or caveat changed.",
    changelog: [
      "v1.0.274: expanded Expected Calibration Error (ECE) at first use. Copy edit only; no scientific claim, number, or caveat changed.",
      "v1.0.273: current AASTeX 7.0.2 class bundled and the out-of-page raw artifact-path link replaced with a short Data Availability pointer. No science change.",
      "v1.0.272: abstract cut to the AAS 250-word cap (339 → 236, no number re-rounded and no caveat cut) and raw provenance identifiers relocated from the narrative into a new artifact provenance register A1–A12 — closing a MAJOR that had been dismissed twice as a PROCESS-NIT. No readiness change.",
      "DOI back-patch (v1.0.269, Jul 20): embedded the minted Zenodo archival DOI 10.5281/zenodo.21461899 (concept 10.5281/zenodo.21461898) in the abstract, Data Availability paragraph (replacing the 'DOI ... will be inserted here ... at submission time' placeholder), and catalog itemize, closing the standing 'DOI-backed archive remain open' caveat. The record archives the exact bytes of the reviewed v1.0.268 release (32pp md5 4e139b56b0718c70b73ae7295e4ee7b1; git commit 397671bf; receipt project-context/SSOT/zenodo/P4_zenodo_receipt_2026-07-20.json). The separate complete systematics-metadata sidecar gate stays honestly open. No science number changed; the observed-label null is unchanged.",
      "CE-composition adjudication + honest-negative retrain (v1.0.268): the Jia CE-ResNet catalog is re-provisioned (Zenodo 10.5281/zenodo.7167388, sha 894dbe88; provenance committed). Deterministic seeded assembly reproduces GZ1=6,637 and CE-spirals=17,153 exactly; the reproducible CE non-spiral count is 819 (neither 826 nor 846) — isolating the entire historical conflict to the seeded 50k non-spiral subsample crossmatch. The composition-faithful CE-included retrain collapses to chance on chirality (val 0.5617 = NS-perfect + chirality-chance arithmetic; per-source GZ1 0.517 / CE 0.509; four alternate hypotheses ruled out, incl. 99.72% CE-GZ1 convention agreement on the 38,617-galaxy bright overlap) — root cause: the CE-only pool (72% of spirals) is systematically fainter/smaller with near-coin-flip supervision (median winner-prob 0.569 vs 0.899). The historical 93.69%/92.10% CE-included headline is NOT reproducible under honest same-composition ingestion, corroborating the paper's standing disclosures; the GZ1-core manifest-retained realization (0.9931) stands and released Catalog C labels are unchanged. All five CE caveat sites adjudicated in-paper. Exact v1.0.268 confirmation board CONVERGED with the softest board of the era: Grok ACCEPT (its first) / Gemini MINOR (0 major) / Claude MAJOR (all re-flags); 16 findings, 0 genuinely-new-real, 0 falsified.",
      "Two real-compute pod-campaign closures (v1.0.266): (1) G1 manifest-retained ViT retrain COMPLETE on RunPod A4000 (<$1 total) — 8,637 objects (6,637 GZ1-core + 2,000 synthetic; CE-ResNet component absent pending external re-provisioning from Jia 2023 / NADC China-VO, so the 826-vs-846 sub-conflict stayed open and released Catalog C labels are unchanged), every object ID/split/seed retained in the committed manifest, best_val_acc=0.9931 @ epoch 47, checkpoint backed up to 3 verified locations. (2) G2 training-disjoint validation: accuracy=0.9867 / Cohen's kappa=0.9733 on 3,000 GZ1 confident spirals disjoint from G1 training on both the object-ID and label-source axes (overlap counts 0), presented with an explicit like-for-like distinction vs the historical kappa=0.40 human-vote figure — a different measure, not a replacement. Caveat sites narrowed honestly at abstract/intro/discussion/conclusions/data-availability. No science number changed.",
      "Coverage-calibrated observed-label A_95^obs closure (v1.0.265): the exact v1.0.264 confirmation board (Claude MAJOR / Grok MAJOR / Gemini MINOR) truth-audited to 2 genuinely-new-real findings. Closed M3 with A_95^obs~=0.98% (linear-interp; logistic cross-check 0.955%) from 2,000 random-axis injections/amplitude through the exact committed primary estimator and exact fixed-occupancy null (headline z=+0.63465/p=0.23768 reproduced exactly as a hard gate first); integrated at 7 manuscript sites. Closed Ge1 with an editorial rephrase removing review-process narration from the new Sec 4.5. Explicitly an observed-label bound, not a physical one; no science number changed.",
      "End-to-end transfer-calibration scope statement (v1.0.229): the injection-recovery section now delineates which links of the classify→dipole chain the sweep traverses (map-making + dipole estimator + null calibration) versus which it does not (ViT classifier, NS triage, confidence cut, spatially-varying confusion), shows from the committed GZ1 confusion numbers that the asymmetric-confusion transfer slope g_eff = s_CW + s_CCW − 1 = 0.398 equals the symmetric g = 2a − 1 = 0.398 for the near-balanced parent (so CW/CCW asymmetry does not degrade the physical-amplitude conversion), and honest-flags the full image-level end-to-end injection through the classifier as requiring new simulation — operative claims held to the observed hard-label field. No number changed, nothing fabricated.",
      "R9 ACCEPT-track minor closure (v1.0.225): Grok = minor-revisions, Gemini = 'Accept with minor revisions'; both referees' concrete minors closed with real edits (no number changed). Abstract z≈−18 now explicitly labeled a model-dependent template-disfavor statistic (not a frequentist exclusion) with the injection-recovery A95∈(1.0,1.5]% cross-referenced as the primary real-space falsification; added a main-text downstream-user warning that raw p_eq scores are not frequentist likelihoods (cite Appendix-B ECE ≥0.25–0.36); abstract real-space p now names its isotropic-pixel-permutation null. ChatGPT major = presentation/consolidation of already-disclosed content.",
      "Deep-tier Gemini MAJOR closure (v1.0.224): added self-contained training-data provenance table + a probabilistic-calibration paragraph quantifying a real top-label ECE lower bound from the committed GZ1 confusion matrix (mean-conf 0.951 vs 3-class acc 0.5871 -> ECE>=0.36; chirality 0.6991 -> >=0.25), proven invariant to any monotone recalibration; surfaced existing committed data, no number changed.",
    ],
    artifacts: [
      { label: "Read PDF", href: "/papers/chirality_catalog_paper_v1.0.274.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/chirality_catalog_paper_v1.0.274.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p2_chirality/chirality_catalog_paper.tex",
        kind: "secondary",
        external: true,
      },
      {
        label: "Science highlights",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/project-context/paper4_science_highlights.md",
        kind: "secondary",
        external: true,
      },
      { label: "Chirality catalog (HuggingFace)", href: "https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog", kind: "secondary", external: true },
      { label: "Classifier model (HuggingFace)", href: "https://huggingface.co/bamfai/galaxy-chirality-v2", kind: "secondary", external: true },
      { label: "Zenodo DOI", href: "https://doi.org/10.5281/zenodo.21461899", kind: "secondary", external: true },
    ],
  },
  {
    slug: "paper-5",
    number: "5",
    publicationRole: "Standalone Companion · Chirality–Environment Null Test",
    standaloneSubmission: true,
    archivedInto: {
      note: "Folded into P4′ (v4P.0.1) as one condensed section rather than kept as a standalone 46-pp paper — 2026-09-02 portfolio restructure, directive R3. Every quoted number is verbatim from this reviewed v0.1.147 source.",
      successorSlug: "paper-4p",
    },
    title: "Environmental Dependence of Spiral Chirality: A DESIVAST Catalog-Native Void Non-Detection with Secondary Cosmic-Web Cross-Checks",
    plainTitle: "Does galaxy handedness differ inside cosmic voids? A null test companion to P4",
    version: "v0.1.147-2026-08-03",
    lastUpdated: "2026-08-03",
    tldr: "On the released DESIVAST GALZONE parent, the focal exploratory analysis detects no void/non-void difference in classifier-labelled CW fraction; this bounded non-detection does not establish physical environment independence.",
    path: publicationPath({}),
    pages: "46",
    refs: "—",
    readiness: 95,
    statusVariant: "amber",
    target: "The Astronomical Journal",
    description: "Separate from P4. P5 tests whether a DESIVAST catalog-native void/non-void contrast is detectable in Paper IV classifier labels. The focal estimator is explicitly exploratory, and the manuscript does not claim physical environment independence or complete removal of selection leakage.",
    keyResults: [
      "Focal released-parent flow: 694,642 GALZONE-valid rows → 145,789 chirality matches → 145,766 OUT=0 analysis rows (31,937 void / 113,829 non-void)",
      "Focal K=13 adjusted non-void-minus-void contrast Δf_CW=+0.00145442; NSIDE=4 cluster-sandwich SE=0.00331502, 95% CI [−0.00504290,+0.00795174], p=0.66085",
      "The identical focal estimate remains null across NSIDE=2/4/8 and 3,750 nearest-VoidFinder-MAXIMALS clusters; every 95% interval spans zero",
      "The older 78-column spline/fixed-effect model is retained only as a rank-fragile flexible sensitivity (Δf_CW=+0.00125636, p=0.71277)",
      "The released DESIVAST GALZONE OUT=0 parent and nearest-VoidFinder-MAXIMALS membership are distinguished explicitly; any-hole, T-Web, Tempel, and ASTRA analyses are secondary checks",
      "A 21-shell radial selection correction and multiple grid/denominator checks retain no detected classifier-label association, but do not establish that selection leakage is absent",
      "The environment-specific Paper IV label-bias check is underpowered, so final Paper IV labels/weights/provenance and a P5 rerun remain external science gates",
      "Program-by-void interaction strata are sparse and not tightly bounded; there is no robust interaction evidence, but no-leakage or physical-independence claims are not made",
      "v0.1.147 is the current clean AJ candidate and source package; an immutable public tag/archive/DOI and identifier back-patch intentionally follow Houston sign-off",
    ],
    surveys: ["P4 chirality catalog (HF bamfai/galaxy-chirality-catalog, 8.47M)", "DESI DR1 zall-pix-iron.fits (~22.5M rows; matched subset 16.4M after quality cuts)", "DESIVAST void catalogs (3 algorithms)"],
    predictions: ["LSS-environment-dependent chirality test (cosmic-web alignment)"],
    figures: ["Matched-catalog footprint", "Per-environment CW fractions", "DESIVAST void-spiral test", "z-shell robustness", "HEALPix coherence at three resolutions"],
    remainingWork: [
      "Run bounded confirmation against the exact v0.1.147-2026-08-03 PDF and keep the sparse interaction and secondary T-Web limitations explicit",
      "After Houston sign-off, refresh the companion P4 archive and mint the P5 immutable tag/Zenodo snapshot",
      "Back-patch the final identifiers, rebuild, and verify every A1–A48 link before submission",
      "Resolve the human/editorial gate through actual AJ review; automated evidence is not journal acceptance",
    ],
    preprintId: "HUBIFY-2026-005",
    pdfMeta: "PDF · 46 pp · v0.1.147-2026-08-03 · updated Aug 3, 2026 · md5 8b9365ff762e0baed12ad9963d9aea1d — migrated from the PRD shell to the selected AJ route's current line-numbered AASTeX 7.0.2 shell. All nine figures, scientific claims, numbers, caveats, references, and disclosure text are unchanged. No readiness change.",
    artifacts: [
      { label: "Read PDF", href: "/papers/p5_desi_chirality_v0.1.147-2026-08-03.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/p5_desi_chirality_v0.1.147-2026-08-03.pdf", kind: "secondary", download: true },
      {
        label: "Pipeline + scripts",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/pipelines/p5_desi_chirality",
        kind: "secondary",
        external: true,
      },
      {
        label: "Audit report",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p5_desi_chirality/reports/00_audit.md",
        kind: "secondary",
        external: true,
      },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex",
        kind: "secondary",
        external: true,
      },
      { label: "Chirality catalog (HuggingFace)", href: "https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog", kind: "secondary", external: true },
    ],
  },
  {
    slug: "paper-4p",
    number: "4P",
    publicationRole: "Track C1 · DESI Data Products (on-vision)",
    standaloneSubmission: true,
    title: "The Largest Test of the Rotating-Black-Hole-Universe Galaxy-Spin-Axis Prediction: A Chirality-Dipole Null in 8.47M DESI Spirals with Void-Environment Cross-Check",
    plainTitle: "Testing the 'universe born inside a rotating black hole' prediction against 8.5M DESI galaxies (result: null, excludes the literature amplitudes)",
    version: "v4P.0.12",
    lastUpdated: "2026-09-22",
    tldr: "Folds P4 (8.47M-galaxy chirality catalog, observed-label dipole null) and P5 (DESIVAST void/non-void environment contrast) into one ApJS paper, adding a new section reading Popławski's rotating-black-hole-universe papers for a computed dipole prediction. Under the minimal closure needed to make the claim testable, the catalog's own A₉₅ᵒᵇˢ≈0.98% sensitivity floor excludes alignment fractions η>0.98% at ≥95% coverage — a factor of 2–20× below the ~7–33% amplitudes reported by Longo (2011) and Shamir (2012–2025). Confirms the independent reanalyses of Iye, Yagi & Fukumoto (2021) and Patel & Desmond (2024). v4P.0.12: the v4P.0.11 hold is LIFTED — the PA-restoring dilution bound, re-measured directly on the classifier's own Smith42/galaxies imaging (not the out-of-domain viewer cutouts the withdrawn v4P.0.10/11 measurement used), gives D≤0.5998±0.0065 (primary_hc) / A₉₅ᵖʰʸˢ≥1.63%, in the conservative direction relative to the withdrawn out-of-domain bound. The sky-dependence dipole systematic (23% of A₉₅) remains out-of-domain and unchanged. Primary null result unchanged; readiness unchanged at 95.",
    path: publicationPath({}),
    pages: "16",
    refs: "—",
    readiness: 95,
    statusVariant: "amber",
    target: "ApJS (candidate; matches P4's venue fit)",
    description:
      "Track C1 of the 2026-09-02 portfolio restructure (directive R3): P4′ is the largest test to date of Popławski's galaxy-spin-axis prediction (the observational claim the black-hole-universe / torsion-bounce model is invoked to explain), not a detached data product. Every quantitative result is quoted verbatim from the reviewed P4 v1.0.274 and P5 v0.1.147 sources, or is a deterministic output of the new committed exclusion script; the catalog pipeline was not re-run.",
    keyResults: [
      "8,474,531 DESI Legacy DR8 galaxies catalogued; primary real-space chirality-dipole null on 890,069 quality-controlled high-confidence rows (887,472 support the fit): z_mom=+0.635, one-sided rank p=0.238",
      "New Sec. 5 — 'The black-hole-universe prediction and its exclusion': Popławski's papers (arXiv:1007.0587, 1111.4595, 1410.3881, 1910.10819) state only a qualitative preferred-axis alignment tendency, not a computed dipole amplitude",
      "Under the minimal closure A_pred≈η, the catalog's A₉₅ᵒᵇˢ≈0.98% sensitivity floor excludes η>0.98% at ≥95% coverage — 2–20× below the ~7–33% amplitudes reported by Longo (2011) and Shamir (2012, 2020, 2022, 2025)",
      "Confirms the independent reanalyses of Iye, Yagi & Fukumoto (2021, arXiv:2011.00662) and Patel & Desmond (2024, arXiv:2404.06617)",
      "DESIVAST void/non-void environment contrast (145,766 classifier-labelled galaxies, folded in from P5): Δf_CW=+0.00145, p=0.66 — null across NSIDE=2/4/8 and 3,750 nearest-VoidFinder-MAXIMALS clusters",
      "No bounce-cosmology claim is made beyond this test — Sec. 6 is explicit this bears on the black-hole-universe model's spin-axis claim only",
      "4-pass compile: 0 undefined references/citations, 0 overfull hboxes, 0 LaTeX warnings; every page visually rendered and checked",
    ],
    surveys: ["DESI Legacy DR8 (8.47M galaxies)", "DESI DR1 zall-pix-iron.fits (matched subset)", "DESIVAST void catalogs (3 algorithms)"],
    predictions: ["Chirality-dipole null (real-space, harmonic, WLS)", "Black-hole-universe spin-axis alignment exclusion η>0.98%", "Void/non-void chirality-environment null"],
    figures: ["Fig. 1: per-pixel HC CW-fraction sky map", "Fig. 2: T-Web secondary cosmic-web diagnostic", "Table 1: literature amplitude vs. A₉₅ᵒᵇˢ comparison"],
    remainingWork: [
      "A fresh INT confirmation board on the exact v4P.0.12 PDF is due (directive R2 round budget refreshed twice by the v4P.0.10/11 corrections) — not run in this lane",
      "The sky-dependence dipole systematic (11σ, 23% of A₉₅ on the strict-887,472 support) remains measured out-of-domain and is not yet re-measured on the classifier's own imaging",
      "arXiv tarball assembled: SSOT/arxiv_tarballs/paper4prime_chirality_test_arxiv_v4P.0.12.tar.gz",
      "Whether/when P5's standalone 42-pp paper is formally retired (vs. kept as an archived companion) is a Houston-gated decision",
      "Houston sign-off (readiness 95→100) has not been sought — the prior co-director SIGN-OFF HOLD is now recommended released, since the in-domain re-measurement it was waiting on is done",
    ],
    preprintId: "HUBIFY-2026-004P",
    pdfMeta: "PDF · 16 pp · v4P.0.12 · created Sep 22, 2026 · md5 afff6bec7b78bac271104d89a3582bf9 — hold LIFTED: in-domain dilution bound adopted, superseding the withdrawn out-of-domain one; primary null result unchanged.",
    changelog: [
      "v4P.0.12: HOLD LIFTED (not a review round) — lane bb-LS10-indomain-d180 re-ran the identical PA-restoring rotation test directly on the classifier's own Smith42/galaxies imaging (N=40,000, streamed by HTTP range read, 320,000 forward passes, zero image bytes to disk, local MPS, 47 min, $0), after two gates passed: catalogue-scale in-domain agreement 99.936% (100.000% on primary_hc) vs. 43.9% out-of-domain; and a measured 3.41× field-of-view gap (in-domain 512×512 px at 0.262″/px = 134.1″ field, vs. the withdrawn measurement's 39.3″ viewer-cutout field). Result: primary_hc (N=4,579) D≤0.5998±0.0065 (61σ below unity; θ=180°-only D≤0.6599±0.0075), all spirals (N=15,219) D≤0.5237±0.0038, A₉₅ᵖʰʸˢ≥1.63% (primary_hc) — superseding, not averaged with, the withdrawn D≤0.717±0.005/A₉₅ᵖʰʸˢ≥1.37%. The in-domain classifier is LESS rotation-stable than the withdrawn measurement suggested (θ=180° self-disagreement rose 21.1%→34.0%), so the correction moves the floor upward, in the conservative direction. Applied to 9 prose locations + tab:pixel_calib, each recording the withdrawal explicitly (never a silent substitution); the ε̄ (PA-restoring transfer efficiency) and TTA-recovery-fraction clauses are cut, not re-quoted, since they remain out-of-domain. Also fixed a documentation error: main.tex:171 said the Smith42/galaxies parent cutouts are 224×224 px; they are 512×512 px at 0.262″/pixel (a 134″ field), resampled to the 224×224 network input — corrected at 3 prose locations. The sky-dependence dipole systematic is unchanged (still out-of-domain, now stated explicitly as such). No new numbers introduced outside the lane's committed JSON. Recompiled 15→16 pp; primary null unchanged; readiness unchanged at 95 (no review board run this round). Co-director sign-off hold recommended RELEASED.",
      "v4P.0.11: HOLD CORRECTION (not a review round) — lane bb-LS6-row16-tta found the v4P.0.10 dilution bound was measured on out-of-domain images: a pre-registered positive control required the released preprocessing, run at the identity transform, to reproduce the released catalog's own labels on ≥99.9% of galaxies; on the images that measurement used it reproduces them for only 43.9% of 19,800 galaxies (42.4%/44.7% on two further draws), against 99.99% agreement with an in-domain forward pass — the classifier code and preprocessing are correct, the images were Legacy Survey display cutouts (39.3″, upsampled to 224 px) rather than the Smith42/galaxies images the released classifier ran inference on. Withdrew D≤0.717±0.005 and A₉₅ᵖʰʸˢ≥1.37% everywhere they appeared (7 prose locations + 2 table rows), replacing each with a named, lifted-by-a-specific-test hold — never a silent deletion. Added the pre-registered sky-dependence systematic: the classifier's parity-transfer efficiency carries an 11σ sky dipole (fractional amplitude 0.090±0.010, permutation-null p≤0.001) that, propagated through the paper's own exact estimator, imprints a spurious 0.23% dipole on the strict-887,472 support — 23% of the quoted A₉₅=0.98% limit. Recompiled to 15 pp; primary null unchanged; readiness unchanged at 95. NOTE (2026-09-22): the hold this version stated was lifted in v4P.0.12 — see above.",
      "v4P.0.10: science-content propagation (not a review round) — applied lane bb-LS-ledger16/bb-LS5-row16-finalize's exact PROPAGATION_NOTE.md sentences verbatim. Withdrew the pixel-injection naive-identity tension claim (+0.434/47σ comparison, 0.038 response ratio, ≈26% propagated floor — all comparisons between statistics that do not share a normalization) and adopted the measured direct dilution bound instead: presenting the released pipeline with a PA-restoring handedness reversal registers it in ε̄=0.754±0.005 of high-confidence spirals (51σ below unity); since handedness cannot depend on presentation orientation, the pipeline's self-contradiction rate across orientations bounds the dilution D≤0.717±0.005 (60σ from D=1), raising the physical-parity floor to A₉₅ᵖʰʸˢ≥1.37% — consistent with, not in tension with, the illustrative g=0.398 bridge. Propagated consistently to the §2.3 forward-reference, Discussion, and Conclusions (previously all three repeated the withdrawn claim), reusing only already-cited numbers. Recompiled to 15 pp; primary null unchanged; readiness unchanged at 95 (no review board run this round). NOTE (2026-09-22): this dilution bound was subsequently found to be measured on out-of-domain images and was withdrawn in v4P.0.11, then re-measured in-domain and reinstated in v4P.0.12 — see above.",
      "v4P.0.9: exact-v4P.0.8 re-verification board (Grok API ACCEPT-with-minor-corrections + Gemini API accept + a Claude opus sub-agent verdict-blind and not shown the prior round's closures, major-revisions) independently re-checked lane L4's own v4P.0.8 closures and found 6 genuinely-new-real MAJOR + 4 MINOR: a pixel-injection baseline compared against the wrong (catalog-wide vs. HC-selected) monopole sample and convention; a 'near-antipodal axis' claim quantitatively false (max recomputed pairwise separation 119.9°, not ~180°), with the closest axis pair (19.3°) previously omitted; two headline-qualifying §A.1 disclosures (the pixel-transfer tension, the primary channel's own leg-instability) with zero forward reference from the Abstract/§3/§5/§6/§7, fixed with four targeted pointers; a 'tercile' split that is actually a 20/60/20 quintile split; and a correlation figure misattributed to the wrong channel pair. All independently re-derived by the orchestrator from the underlying committed JSON/scripts before closure, not accepted from reviewer text alone; recompiled to 14 pp; primary null unchanged. Directive R2: no further consecutive review round on this content without an intervening science/scope decision.",
      "v4P.0.8: exact-v4P.0.7 INT confirmation board (Grok API + Gemini API + Claude opus sub-agent) closed 7 genuinely-new-real MAJOR + 12 MINOR findings in the v4P.0.5-v4P.0.7 disclosure content — inverted QC-cut attribution, omitted primary-channel leg-instability disclosure, undisclosed sample contamination in two new channels, void-catalog self-contradiction, misattributed literature claim, two wrong reproducibility-manifest pointers, and an explicit disclosure of the tension between the new pixel-level calibration and the exclusion's g=0.398 bridge factor (not resolved, stated honestly); recompiled to 14 pp; primary null unchanged.",
      "v4P.0.7: row-16 (iv-b) DESI DR1 BGS_BRIGHT-21.5 external environment result added — genuine external tracer field (300,043 galaxies), spec-z 3D N=121,417 + projected N=949,584 parity-by-density table, null (largest excursion projected node-like z=+2.96, p=0.084 corrected); recompiled to 13 pp; no science-conclusion change.",
      "v4P.0.6: row-16 disclosure integrated — pixel-level injection calibration (N=20k), full-parent selection systematic (confidence-cut/DES-leg), 15-statistic chirality x structure cross-correlation nulls; recompiled to 12 pp; no science-conclusion change.",
      "v4P.0.5: REVISE (abstract cap) executed — abstract trimmed to 246 words, no science change; tarball rebuilt.",
      "v4P.0.4: R3 verification pass closed — automated review converged (Claude minor / Grok reject / Gemini minor); final author review APPROVE; readiness 95; arXiv tarball assembled.",
      "v4P.0.3: R2 closure — 21/21 findings closed; monopole disclosed; genuine 95% CL limit ≈0.75% by Neyman inversion. R2 verdicts: Claude major-revisions, Grok reject, Gemini major-revisions.",
      "v4P.0.2: R1 board closed; recompiled to 10 pp. Compiled 4-pass, 0 undef refs, 0 overfull hboxes.",
      "v4P.0.1: first folded draft (P4 catalog + P5 environment section + new black-hole-universe exclusion section). Compiled 4-pass, 0 undef refs, 0 overfull hboxes. Superseded P4 (v1.0.274, archived, Zenodo 10.5281/zenodo.21461899) and P5 (v0.1.147, archived, not independently DOI'd).",
    ],
    artifacts: [
      { label: "Read PDF", href: "/papers/paper4prime_chirality_test_v4P.0.12.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper4prime_chirality_test_v4P.0.12.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/pipelines/p4prime_chirality_test/paper",
        kind: "secondary",
        external: true,
      },
      {
        label: "Exclusion computation script",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py",
        kind: "secondary",
        external: true,
      },
      {
        label: "Archived lineage: P4 (Zenodo DOI)",
        href: "https://doi.org/10.5281/zenodo.21461899",
        kind: "secondary",
        external: true,
      },
      {
        label: "Archived lineage: P5 (LaTeX source, v0.1.147)",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex",
        kind: "secondary",
        external: true,
      },
      { label: "Chirality catalog (HuggingFace)", href: "https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog", kind: "secondary", external: true },
    ],
  },
  {
    slug: "paper-su",
    number: "SU",
    publicationRole: "Short note · Separate-universe failure criterion",
    standaloneSubmission: true,
    title: "The separate universe computes a different variable: an exact criterion for δN = ζ in non-attractor phases",
    plainTitle: "When the separate-universe shortcut computes a different variable from ζ",
    version: "v1S.0.12",
    lastUpdated: "2026-09-19",
    tldr: "R4 board COMPLETE: Claude-opus leg (v1S.0.10) closed an internal-consistency gap from the S12 fix; Grok+Gemini API legs (v1S.0.11) then closed 4 more genuinely-real items (a wrong Cai-2009 citation now backed by a new equation-level appendix, 3 App.~A2->A3 cross-ref errors, a Fig.1 caption clarity note, a Table I citation) -> v1S.0.12. Two real science gates remain open (S13 initial-slice convention, S15 Appendix A5 derivation) -- both need a from-scratch derivation, not an edit. Per directive R2, paper-su's review-round budget is now spent; no further board without a new science/scope decision. Readiness holds at 72 (COMPUTED).",
    path: publicationPath({}),
    pages: "8",
    refs: "—",
    readiness: 72,
    statusVariant: "amber",
    target: "gr-qc / astro-ph.CO (candidate; cross-list astro-ph.CO) -- 2026-09-19 recommendation: primary astro-ph.CO, cross-list gr-qc (Houston-gated final choice, see SSOT)",
    description: "A standalone short note transcribing the separate-universe failure criterion, spun out of A3M's Appendix A (no new math introduced beyond the source theory-audit note). It derives the exact threading identity between the comoving curvature perturbation and the separate universe's zero-shift variable, and states when the separate-universe method reproduces the squeezed-limit bispectrum and when it does not.",
    keyResults: [
      "Exact threading identity between Maldacena's comoving ζ and the separate universe's zero-shift variable δN_c",
      "Criterion: δN (isotropic, N(φ,π)) reproduces the squeezed bispectrum of ζ iff the ζ-growth-weighted mean ⟨ε/c_s²⟩_ζ vanishes",
      "Dust contraction: O(1) failure, monopole gap 25/8",
      "Ultra-slow-roll inflation: agreement to O(ε), reproduces Namjoo-Firouzjahi-Sasaki 2013",
      "Attractor slow roll: identity map, Maldacena consistency relation untouched",
      "Ekpyrotic contraction: passes because ζ sits on its constant mode, consistent with Creminelli-Nicolis-Zaldarriaga 2004",
    ],
    surveys: ["No survey likelihood — analytic criterion + four background checks"],
    predictions: ["Separate-universe validity criterion ⟨ε/c_s²⟩_ζ = 0", "O(1) separate-universe failure for matter-dominated contraction"],
    figures: ["λ vs. f_map general-w closed forms"],
    remainingWork: [
      "R4 board COMPLETE (2026-09-19): all 3 legs run + truth-audited (Claude-opus on v1S.0.10, Grok+Gemini API on v1S.0.11) -> v1S.0.12. 4 genuinely-real findings closed: S14's Cai-2009 citation (now backed by a new equation-level Appendix A6), 3 App.~A2->A3 cross-reference errors, a Fig.1 caption clarity note, a Table I USR-row citation. Per directive R2, the round budget for paper-su is now spent -- no further board without a new science/scope decision.",
      "S13/S15 (real science gates, NOT closable by editing): initial-slice/zeta_L(t_i)=0 convention inconsistency across Eq.1-2/USR-lambda/ekpyrosis row; Appendix A5's lambda_g asserted not derived (linked to S13). Both need a from-scratch derivation. S16 (cosmetic minors) carried, non-blocking. None touch S12 or the headline -5. See SSOT.",
      "S12 RESOLVED + APPLIED (2026-09-19): translation-term monopole generality — the trace carries a nonzero (n_s-1) monopole, exactly cancelled by a compensating in-in tilt term, so f_deltaN^init=-5 for every constant eps and n_s. No longer gating.",
      "Venue/arXiv-category: 2026-09-19 recommendation is primary astro-ph.CO / cross-list gr-qc (Houston-gated final choice); note is 8 pp., over a strict PRD-Letter limit — Letter vs. Brief Report form also undecided.",
      "S4 (self-containedness, ADM constraint solve not fully reproduced in-paper), S8 (numerical USR validation), S11 (Zenodo DOI) remain open, non-blocking, carried.",
      "See project-context/SSOT/paper-su/status.md for the full close-the-gap section",
    ],
    preprintId: "HUBIFY-2026-SU",
    pdfMeta: "PDF · 8 pp · v1S.0.12 · created Sep 19, 2026 · md5 7bae5b35c4ee1456557a8c74f57a3692 — R4 board complete (all 3 legs); 4 genuinely-real findings closed (Cai citation + appendix, 3 cross-refs, Fig.1 caption, Table I citation). S13/S15 remain open science gates. No science number changed. Readiness holds at 72.",
    changelog: [
      "v1S.0.12: R4COMPLETE (campaign lane bb-L2c-psu-r4-complete, 2026-09-19) — Grok API (grok-4.3, REJECT) + Gemini API (gemini-3.1-pro-preview, MAJOR REVISIONS) run on the exact v1S.0.11 PDF (sha8 0fc47bd5), completing R4 (the Claude-opus leg had reviewed v1S.0.10 — two different exact PDFs, recorded separately, never blended). 4 genuinely-new-real findings truth-audited and CLOSED: (1) S14's citation half — Sec. I's Cai et al. 2009 factor-of-2 claim was cited only to an unpublished note that does not even contain the comparison; fixed with a new citation (Golden2026CaiFactor) plus a new Appendix A6 transcribing the actual equation-level derivation (fetches the real Cai 2009 + Li-Quintin-Wang-Cai 2017 arXiv e-prints) verbatim from research/theory_audit/psu_gate_S7_cai_factor_2026_09_05.md; (2) three '(App.~A2)' cross-references corrected to '(App.~A3)' (the cited formulas are actually in A3); (3) Fig.1 caption gains a sentence explaining the two curves are deliberately dual-axis-scaled to coincide exactly; (4) Table I's USR row gains a footnote citing Namjoo et al. 2013 for its 5/2 values (previously uncited in-row, read as internally derived). Most of Grok's other findings were FALSIFIED on direct/independent re-derivation (a hallucinated contradictory clause, a mis-derived +25/4, a footnote-miscount defect already fixed pre-round, a wrong-formula quadrupole claim) or are re-flags of already-tracked genre items (S4, S11, venue/length, reproducibility-hash/AI-disclosure/version-tag complaints). Full per-finding disposition in DISPOSITIONS/PSU.md. Directive-G: v1S.0.11->v1S.0.12, 4-pass, 0 undef refs, a transient 179pt table overfull from an over-long USR-row parenthetical fixed by moving the citation to a caption footnote (final 12.6pt, matching the pre-existing ~8pt Table I class, /latex-audit visual PASS all touched pages), 8pp (up from 7, new appendix), md5 7bae5b35c4ee1456557a8c74f57a3692, three-way matched. Readiness holds 72 (COMPUTED). Per directive R2, paper-su's review-round budget is now spent.",
      "v1S.0.11: R4 board (campaign lane bb-L2b-psu-s12-apply, 2026-09-19), Claude-opus verdict-blind referee leg on exact v1S.0.10 (sha8 1015f442): MAJOR REVISIONS. Independently re-derived and confirmed correct essentially all of Appendix A2's kernel totals, Eq.(4)'s identity, the -5 composition, and byte-verified all 10 cited SHA-256 prefixes. Truth-audited findings: MAJOR 2 genuinely-new-real and CLOSED -- Sec. II's Eqs.(3)-(5), the 'label-independent monopole -5eps/6' claim, Fig.1's caption, and the abstract's 'translation term with zero monopole' printed the n_s=1 special case as general, contradicting the Appendix A2/A3 fix this lane had just applied (the S12 fix touched only the Appendix, not the main text restating the same formulas) -- fixed with matching n_s qualifiers + strengthened -5 statement in Sec. II/abstract/Fig.1. Two real wording slips in the S12 addition itself also closed: the A3/A4 cancellation identity needed an explicit 1/lambda factor (was stated as an unqualified equality); the Reproducibility Statement mis-attributed the in-in tilt term to the linearised ADM constraints alone (needs the in-in vertex assembly too). MAJOR 1 (initial-slice convention), MAJOR 3 (Appendix A5 lambda_g), MAJOR 4 (Cai 2009 citation) are real but pre-existing, out of this closure's scope -- carried as new gates S13/S14/S15, non-blocking, not touching S12 or the headline -5. Directive-G: v1S.0.10->v1S.0.11, 4-pass, 0 undef refs, one new 26.77pt overfull hbox from the added n_s bracket fixed by wrapping into a two-line align (0 overfull >10pt after), /latex-audit visual PASS all 7 pages, 7pp, md5 c5b0ea962c5b9f965c22bc6d08d93250, three-way matched incl. Convex. Grok/Gemini API legs of R4 still not run (preflight gate now blocked on a different concurrent lane's A3M files). Readiness holds 72 (COMPUTED). Lane budget spent here per task stop condition.",
      "v1S.0.10: S12 presentation fix (campaign lane bb-L2b-psu-s12-apply, 2026-09-19) applying research/theory_audit/psu_gate_S12_translation_trace_2026_09_19.md's Printable P1-P5 verbatim. Appendix A3: replaced the wrong 'trace part vanishes at n_s=1' / 'monopole 0 (all eps)' with T(eps,mu,n_s)=5eps/(4(3-eps))[1-3mu^2+(n_s-1)mu^2], monopole 5eps(n_s-1)/(12(3-eps)). Appendix A2 'Totals': final-label monopole -5eps/6 holds for any n_s (tilt-independent, no 1/k_L pole); initial-label monopole corrected to 5eps(2eps-7+n_s)/(12(3-eps)), reducing to -5eps/6 only at n_s=1. Appendix A4: printed in-in shape labelled n_s=1; general-n_s shape added with its extra tilt term identified as exactly -deltaT (cancels the A3 correction term-by-term in mu). f_deltaN^init=-5 statement strengthened: holds for every constant eps AND every n_s (a constant-eps background is not scale-invariant; n_s-1=2(2eps-3)/(eps-1) vanishes only at eps=3/2). One sentence added to 'What is new' (the two labels are n_s-independent for different reasons). Reproducibility Statement cites the S12 script/json with real SHA-256 prefixes. No science number changed -- /never-fabricate-derivation clean, every sentence traces to the source note. 4-pass recompile, 0 undef refs, 0 raw Unicode, 0 overfull hboxes >10pt except the pre-existing 8.31pt Table I row, /latex-audit visual PASS on all 7 pages, 7 pp (unchanged), md5 c6457c37f51a8ba0a92f57f1aed5d650. R4 (the one directive-R2-permitted board) dispatched on the exact PDF: Claude-opus verdict-blind referee leg running; Grok+Gemini API legs blocked on bigbounce_preflight.py's clean-tree requirement for site/src/data/{live-status,papers}.ts, mid-edit by concurrent campaign lanes in this shared checkout -- retry once clear. Readiness holds 72 (COMPUTED) pending R4's completion.",
      "v1S.0.9: R3VERIFY (campaign lane L2, 2026-09-18) — the review round directive R2's intervening S7-A2-adjudication science decisions unlocked, run on the exact v1S.0.8 artifact (Claude Opus 5 INT, Grok API, Gemini API; OpenAI/ChatGPT absent per directive N). Closed 2 ESSENTIAL genuinely-new-real defects: Sec. III still printed the pre-adjudication f^rho_NL=-5/2 while Appendix A5 printed the corrected -55/16 for the same quantity (the v1S.0.8 closing amendment landed in the Appendix only, never propagated to the main text, for 11 days); a raw UTF-8 rho character threw a hard LaTeX error and was silently dropped from the served PDF. Closed 3 MAJOR: Appendix A5's amendment paragraph narrated internal review/adjudication process and used undefined symbols lambda'/A_2 (directive-G leak-gate violation, rewritten to state the physics directly with both symbols defined and the f^rho_NL normalization stated); footnote 1 miscounted f_map^fin's contributions (fixed to four, with the initial-label translation named as the separate fifth term for f_map^init); Reproducibility Statement was missing the two newest scripts and manifests (added with SHA-256 prefixes). New open science item S12 (NOT closed, NOT dismissed): Gemini's finding that the translation term's exact zero monopole was derived assuming n_s=1, unverified at general constant-eps -- gates the next review round. 4-pass, 0 undef refs, leak-gate grep clean, 0 overfull hboxes >10pt except the pre-existing 8.31pt Table I overflow, 7 pp (up from 6), md5 fcc3383afa72efebd7e4cf888c5851e0. Readiness 70 -> 72 -- ROUNDS STOPPED again pending S12.",
      "v1S.0.8: A2 lapse-monopole gap reconciled (research/theory_audit/a2_lapse_monopole_adjudication_2026_09_07.md). S9's constraint solve A2=eps(3-eps)^2/3 stands as correct (not 2(3-eps)^2). The uniform-density-surface squeezed monopole is f^rho_NL=5(eps-7)/8=-55/16 at eps=3/2 — the earlier initial-label figure -5/2 came from composing the threading map with the linear-mode weight lambda'=2lambda where the rho-surface time shift, acting on the second-order curvature perturbation, instead carries weight 3lambda; correcting the weight closes the gap 5(6-eps)/24 exactly. In-in monopole -15/8, comoving delta N -5, and uniform-density delta N -55/16 are three well-defined variables related by exact threading maps, not competing claims. No new math; Appendix A composition step corrected in place. 4-pass, 0 undef refs, max overfull hbox 8.3pt, 6 pp, md5 87bda8d5faf08102b621a3ea1755d233. Readiness 65 -> 70 — ROUNDS STOPPED (R2); all S9 science gates closed, next step is venue selection.",
      "v1S.0.7: S9c derivation-statement update (research/theory_audit/psu_gate_S9c_evolution_residual_2026_09_05.md) — the v1S.0.6 hypothesis that the -55/16 gap arises from a dropped super-Hubble evolution term is NOT supported: an independent exact separate-universe solution reproduces both -55/16 (uniform-density) and -5 (comoving) for all ε, so both delta N values are well-defined variables. The 15/16 gap is relocated to the second-order threading map's long×short lapse monopole coefficient A2=ε(3-ε)^2/3 versus the separate universe's required 2(3-ε)^2; which coefficient is correct is under independent adjudication, not yet resolved. Readiness 65 (unchanged) — ROUNDS STOPPED (R2).",
      "v1S.0.6: S9b derivation-statement correction (research/theory_audit/psu_gate_S9b_intrinsic_term_2026_09_05.md) \u2014 the sentence attributing the -55/16 gap to the omitted intrinsic flat-slice initial-data term is replaced: that term, f^intr_NL = 5\u221a(3\u03b5)(3-\u03b5)/18 \u00b7 r_i/(W-1), vanishes in the growing-mode limit that defines -55/16, so it cannot close the gap; the residual 5(6-\u03b5)/24 is stated to arise in the super-Hubble evolution step between the flat and uniform-density slices instead, and remains an open item, not reconciled. Readiness 65 (unchanged) \u2014 ROUNDS STOPPED (R2).",
      "v1S.0.5: S9/S10 second-order closure (research/theory_audit/psu_gates_S9_S10_2026_09_05.md). Appendix A gains the general-admixture constant-mode kernel: K_c derived in closed form by re-solving the ADM constraints at (m_L,m_S)=(0,3/eps-1), squeezed value K_c to -2eps/3 (cancels the constant-mode zlap term exactly, so a constant long mode has a null O(k^0) map), and the corrected bispectrum normalisation f_map(g) = (g lambda_1/lambda_g) f_map(1) with prefactor 1/(lambda_g lambda_1); g=1 reproduces -5 (initial label) and -25/4+(15/4)mu^2 (final label). Section II gains the uniform-density (rho-slice) result: continuing the fluid-congruence field to second order on rho=rho-bar(t_f) gives f^rho_NL=5(2eps-15)/24=-5/2 at dust (isotropic) -- this does NOT reproduce the separate-universe -55/16 value quoted elsewhere in this program (gap 15/16), attributed to an omitted intrinsic flat-slice initial-data bispectrum (Namjoo-Firouzjahi-Sasaki non-attractor caveat), not to an error in the map. 4-pass, 0 undef refs, 0 overfull hboxes >10pt, 6 pp, md5 780b079e88e4ade112b35517edece020. Readiness 65 (unchanged) -- ROUNDS STOPPED (R2).",
      "v1S.0.3: R2 truth-audit closure (project-context/peer-reviews/INT_v3/PSU_v1S.0.2_R2_TRUTH_AUDIT_2026-09-04.md, 20 genuinely-new-real findings across Grok/Gemini/Fable INT legs). All 11 editorial items closed: abstract precision, Eq. (4) sign flip (sympy-verified), algebra statement corrected (1-lambda=I/3), Cai 2009 counterfactual ratio corrected to 4/3 (was a wrong 8/7 transcribed unverified from R1), references split/fixed, gradient-expansion order term folded into the [1-I/3+O(.)] bracket, Eq. (1) caveats stated, Table I relabeled, reproducibility paths switched to \\url{}, and a required new self-contained Appendix A transcribing the second-order lapse/shift setup + five kernel contributions + two-label translation. 4-pass, 0 undef refs, 0 overfull hboxes >10pt, 6 pp (up from 4), md5 afeda89e03a7e0bc688d84c423d164fb, tarball paper_su_arxiv_v1S.0.3.tar.gz, Convex bump k572q3ewgfsmjb02ets0jyh9b58dvghn. Readiness 65 (up from 55) -- ROUNDS STOPPED (R2) pending a science or venue decision.",
      "v1S.0.2: D-PSU-1 reframe + R1 truth-audit closure (project-context/peer-reviews/INT_v3/PSU_v1S.0.1_R1_TRUTH_AUDIT_2026-09-04.md, 21 genuinely-new-real findings, 5 falsified, 1 opinion, 1 out-of-scope). Title/abstract reframed: the isotropic separate universe computes an exact, invertible change of variable, delta N_c = zeta_L,f[1 - I/3] + O(k_L^2/a^2H^2) with I the ratio of the neglected (eps/c_s^2)-weighted integral to zeta_L,f; the O(1) error arises only when delta N_c is identified with zeta, i.e. iff I=O(1) (I=0 on attractor/ekpyrotic rows; reduces to sqrt(eps_s eps_f)-eps_f in USR; to eps in the dust contraction). Label-resolved compositions: initial label reproduces -5 exactly for all constant eps; final label gives -25/4+(15/4)mu^2 at eps=3/2. Eq. (2) restores the dropped O(k_L^2/a^2H^2) gradient term; Table I gains an f^in-in_mono=-15/8 column; Cai et al. 2009 cited with the located factor-of-2. All three science gates (S1/S2/S3) resolved (research/theory_audit/psu_gates_S1_S2_2026_09_04.{md,py,json}). 4-pass, 0 undef refs, 0 overfull hboxes >10pt, 4 pp, md5 fcbecd03679fdc4ecae3956c35b9b08c, tarball a3_su/paper_su_arxiv_v1S.0.2.tar.gz. Readiness 55 (up from 40) — one further verification round permitted under directive R2.",
      "v1S.0.1: first draft, spun out of A3M Appendix A per PAPER_LINEAGE_2026-08-05.md's disposition trail (original claim vs new claim). 4-pass pdflatex, 0 undef refs, 0 overfull hboxes >10pt, md5 b974dc018e0f5a9f62aa92ea8cef697b. Readiness 40.",
    ],
    artifacts: [
      { label: "Read PDF", href: "/papers/paper_su_criterion_v1S.0.12.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper_su_criterion_v1S.0.12.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/arxiv/paper_su_criterion",
        kind: "secondary",
        external: true,
      },
    ],
  },
  {
    slug: "paper-af",
    number: "AF",
    publicationRole: "Track C2 · DESI Data Products (on-vision)",
    standaloneSubmission: true,
    title:
      "A Provenance-Sealed DESI DR1 Anomaly-Score Candidate Catalogue: Selection, Validation, and a Null Known-Object Recovery Benchmark",
    plainTitle:
      "The DESI anomaly-map catalogue: a public list of the strangest-looking spectra, with an honest test of whether that tail is actually anomalous (result: a validated data release, not a discovery)",
    version: "vAF.0.5",
    lastUpdated: "2026-09-21",
    tldr:
      "Publishes a provenance-sealed candidate catalogue of 1,244 spectroscopically unusual DESI DR1 objects (the top 5.7×10⁻⁵ of 21,793,550 science-target spectra), now retitled to carry the null result explicitly. The anomaly score is uncorrelated with exposure quality/brightness, and a new variance-decomposition script shows it is almost entirely explained by the blue spectrograph arm's own residual (R²=0.78 with it, R²=0.01 without). A known-object recovery benchmark clears no reference class at its pre-declared bar. R1's INT board (Claude opus + Grok + Gemini, all convergent) closed 17 of 20 findings with real edits or new committed computation — most consequentially downgrading a 'supports one' z≈4.3 quasar candidate to 'undecidable' after independent re-verification found it inside the paper's own disclosed photometric-join defect — leaving the honest verdict as 'refutes one of four, cannot decide the other three.'",
    path: publicationPath({}),
    pages: "18",
    refs: "—",
    readiness: 77,
    statusVariant: "amber",
    target: "ApJS (candidate; catalogue + method paper with a large public data product)",
    description:
      "Track C2 of the 2026-09-02 portfolio restructure (directive R3): the early-universe anomaly map's first full manuscript, redirecting the anomaly line from a bare data product (P3) to an explicit, honestly-scoped catalogue release. An archived convolutional autoencoder, SHA-256-bound to a sealed run contract, scores every DESI DR1 iron science-target spectrum; 21,793,550 unique TARGETIDs pass the science-target provenance gate, and a pre-declared threshold yields the released 1,244-object catalogue. Every quoted number traces to a committed generator script and outputs/draft_numbers.json (directive Q2 reproducibility); ledger row 8's pre-declared discovery condition is stated as NOT met, per directive Q1/R6 (nulls stay nulls). R1's INT board (Claude opus 6 BLOCKER/16 MAJOR, Grok REJECT, Gemini MAJOR REVISIONS, all independently convergent) closed 17 of 20 canonical findings with real edits or new, independently re-derived computation; 3 remain honestly disclosed as open (undocumented training corpus/architecture, unquantified dedup near-threshold effect, taxonomy RA-wrap).",
    keyResults: [
      "28,425,963 raw rows deduplicate to 27,547,223 unique TARGETIDs; 21,793,550 pass the science-target provenance gate — the released 1,244 objects are the top 5.7×10⁻⁵ of that science-target population, not the all-fibre denominator",
      "Above S=3, >99.5% of raw fibres in every score bin are sky/non-science fibres, rising with score up to S=10; a score cut alone does not select astrophysical objects — the provenance gate must be applied first",
      "Anomaly score uncorrelated with exposure quality/brightness (Spearman |ρₛ|≤0.10 against 5 independent measures); a new committed variance-decomposition script shows the blue spectrograph arm's own residual explains R²=0.78 of the score's variance, falling to R²=0.01 without it (94.9% of released objects have it as their worst-fit camera) — evidence favoring a fixed-wavelength calibration origin, not yet closed",
      "25-cluster/8-family descriptive taxonomy (built over 675 no-SIMBAD/NED-counterpart objects) is structured but not separated in the model's own latent space — a stratification of the candidate list, not physical classes",
      "Known-object recovery benchmark against 5 reference classes clears no class at the pre-declared bar — reported as a validated data release, not a discovery (ledger #8 condition NOT met)",
      "R1 board independently re-verified the abstract's 'supports one' z≈4.3 quasar candidate and found it sits inside the paper's own disclosed 406-row photometric-join defect (empty morphtype, exact-zero WISE/shape columns, a physically backwards r/z flux ratio) — downgraded Supported → Undecidable; honest verdict is now 'refutes one of four, cannot decide the other three'",
      "R1 closed 17/20 canonical findings with real edits/computation, no science number changed without a committed computation: validation pass count corrected 13→11, enrichment denominator fixed at the generator (4.2×→3.3×), title now states the null result directly; 3 items honestly disclosed as open (training corpus, dedup near-threshold effect, taxonomy RA-wrap)",
      "4-pass compile: 0 undefined refs, 0 overfull hboxes >10pt, 17 pages (up from 15, real new content)",
    ],
    surveys: ["DESI DR1 iron spectral release (science-target population)"],
    predictions: ["Anomaly-score candidate catalogue (data release, not a detection claim)", "Descriptive taxonomy stratification", "Named follow-up target tiers"],
    figures: [
      "Score distribution + survival curve",
      "Mollweide sky map",
      "Per-camera residual diagnostics + blue-arm variance decomposition (R²=0.78→0.01)",
      "V12 latent-space silhouette vs. permutation null",
    ],
    remainingWork: [
      "3 findings honestly disclosed as open, not closed: the archived autoencoder's undocumented training corpus/architecture, the deduplication rule's unquantified near-threshold effect, the taxonomy's RA-wrap and missing clustering hyperparameters",
      "2 genuinely open TODOs remain, correctly not agent-closable: the absent selection function (OT-1, needs GPU injection-recovery compute — fully specified in-paper, not run) and a Zenodo DOI (Houston-only, minting step)",
      "Directive R2: round 1 of 2 spent; readiness 77 COMPUTED — no further board without an intervening science/scope decision",
    ],
    preprintId: "HUBIFY-2026-AF",
    pdfMeta: "PDF · 18 pp · vAF.0.5 · created Sep 21, 2026 · md5 60de7e9dbfbcc77336b3050ee788e68e — non-review TODO-closure bundle: schema table completed to 192/192 columns, full bibliography ADS-verified; primary null result unchanged.",
    changelog: [
      "vAF.0.5: non-review directive-G bundle (lane LAF2, no review board run — R2 stays at round 1 of 2). Closed DAF-16 fully: identified and documented the real 9 remaining released columns (mean_fiber_ra/dec, gr/rz/w1w2_color, is_point_source, is_star_candidate, crossmatch, snr_med) by reconstructing the actual 192-column master frame from the committed assembly script and reading their exact definitions out of the committed enrich/assemble scripts — schema table now accounts for all 192/192 released columns (was 183/192). Completed the bibliography verification LR1 started: all 26 remaining \\bibitem entries (beyond the 4 already ADS-verified) checked against ADS/journal records — every journal/volume/page matches exactly, including the three hardest-to-verify (Nicolaou2026's MNRAS page-ID stag010, DESI DR1's AJ 171/285, Guy et al.'s AJ 165/144); no bibliography text changed. Re-confirmed OT-1 (selection function) and the Zenodo DOI remain genuinely not agent-closable (GPU compute / Houston-only respectively) — left as already honestly specified, not touched. 4-pass compile clean: 0 errors, 0 undefined refs/cites, 0 overfull hboxes >10pt, 18 pages (up from 17, real new schema-documentation content). Readiness 75→77.",
      "vAF.0.4: R1 INT board closed (Claude opus verdict-blind 6 BLOCKER/16 MAJOR/16 MINOR/9 NIT, Grok API REJECT, Gemini API MAJOR REVISIONS, all three independently convergent on the same core defects; every BLOCKER + highest-impact MAJOR independently re-derived from committed artifacts before closure, 10/10 spot-checks matched). Most consequential: the abstract's 'supports one' z≈4.3 quasar candidate sits inside the paper's own disclosed 406-row photometric-join defect — downgraded Supported→Undecidable. 17/20 canonical findings closed with real edits or new committed computation (validation pass count 13→11, new blue_arm_diagnostics_2026-09-19.py variance-decomposition script, Table VII denominator fixed at the generator, title/abstract/conclusions rewritten to state the null directly); 3 honestly disclosed as open. 4-pass compile clean, 17pp (up from 15). Convex readinessCap 60→75. Directive R2: round 1 of 2 spent.",
      "vAF.0.3: registered in Convex (papers:upsert slug paper-af, paperVersions:bump vAF.0.2→vAF.0.3, byte-identical mirrors to site/public/papers + public/papers). Closed 2 of LA's 4 open TODOs: ADS-verified the 4 uncommitted-artifact bibliography citations (all already correct, no bibliography text changed) and replaced the acknowledgements placeholder with the DESI DR1 standard funding/land acknowledgement, SIMBAD/NED/VizieR service acknowledgements, a compute-cost acknowledgement, and the lab's AI-assisted-methodology disclosure paragraph. 4-pass compile clean: 0 errors, 0 undefined refs/cites, 0 overfull hboxes >10pt, 15 pages (unchanged). Zenodo DOI and OT-1 selection function remain open.",
      "vAF.0.2: full first draft (from the vAF.0.1 skeleton): 15pp, 9 figures, 11 tables, 0 undef refs, 0 overfull hboxes, all 7 artifact links resolve. Corrected the science-target parent to 21,793,550 unique TARGETIDs (not the 27,547,223 all-fibre figure); found 36 ZWARN=0 objects at z≥4 (16 at z≥6); executed the cheapest named follow-up test (FT-A Lyman-break check refutes one z=5.19 candidate, supports one z=4.33 candidate, 2 undecidable on a released-schema flux-inverse-variance gap — a fourth release defect recorded). Corrected the benchmark enrichment against the fairer science-target denominator (4.2× → 3.3×; still short of the 10× bar, conclusion unchanged). No review board run yet; not registered as a Convex-tracked paper slug at this version.",
      "vAF.0.1: manuscript skeleton assembled from the phase-3-v2 landing (7pp, revtex4-2). Provenance gate re-run clean on both released tables (9/9 artifact sha256 match); 16-item validation contract built (13 PASS, 2 disclosed defects); 8-family/25-cluster per-family evidence table; 32 named follow-up targets in 5 tiers; directive-Q2 reproducibility manifest.",
    ],
    artifacts: [
      { label: "Read PDF", href: "/papers/anomaly_flagship_vAF.0.5.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/anomaly_flagship_vAF.0.5.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/pipelines/p1_highz_tracers/anomaly_flagship_draft",
        kind: "secondary",
        external: true,
      },
      {
        label: "Figure/table generator",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/pipelines/p1_highz_tracers/flagship_assembly_2026-09-18/scripts/make_draft_figures.py",
        kind: "secondary",
        external: true,
      },
      {
        label: "Supporting release: DESI public-ID recovery (P3)",
        href: "https://doi.org/10.5281/zenodo.21461888",
        kind: "secondary",
        external: true,
      },
    ],
  },
];

export function getPaperBySlug(slug: string): Paper | undefined {
  return papers.find((p) => p.slug === slug);
}

/** Count of completed stages + the current gating stage, for compact widgets. */
export function pathSummary(paper: Paper): {
  done: number;
  total: number;
  current: PublicationStage | undefined;
} {
  const done = paper.path.filter((s) => s.state === "done").length;
  const current =
    paper.path.find((s) => s.state === "active") ??
    paper.path.find((s) => s.state === "blocked") ??
    paper.path.find((s) => s.state === "pending");
  return { done, total: paper.path.length, current };
}
