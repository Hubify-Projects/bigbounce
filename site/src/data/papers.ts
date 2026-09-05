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
      "P1N (v1N.0.1) merges P1A and P1C into one \u226412 pp gr-qc/CQG Note: the derived axial spin-spin contact term is identified with Po\u0142awski's torsion-bounce repulsion mechanism (the positive result), while the same algebraic elimination closes four candidate dark-energy routes (the negative result).",
    limitation:
      "P1N has not yet been through any INT/EXT review board. P1A and P1C remain on disk, frozen and unedited, as this Note's archived lineage \u2014 not separate live submission targets.",
    leadSlug: "paper-1n",
    supportSlugs: [],
    status: "One closed-line Note. P1A + P1C review churn stopped after R13; single INT board runs on the merged Note before submission.",
  },
  {
    id: "track-c-desi-data-products",
    title: "Track C \u2014 DESI data products (on-vision)",
    question:
      "What do DESI's public galaxy and spectral data show when tested directly against the rotating-black-hole-universe spin-axis prediction and scanned for early-universe anomalies \u2014 and what does that say about bounce vs. inflation?",
    result:
      "C1 \u00b7 P4\u2032 (v4P.0.1) folds P5 into P4 as the largest test of Po\u0142awski's galaxy-spin-axis prediction: a null so far, excluding alignment fractions \u03b7 > 0.98% at \u226595% coverage, a factor of 2\u201320\u00d7 below literature claims. C2 (early-universe anomaly map) redirects the anomaly line from a bare data product to an explicit bounce-vs-inflation discriminator; P3 stands as its provenance/public-ID release until the map's autoencoder catalogue is earned. C3 (namaster-proof) is an optional software note.",
    limitation:
      "P4\u2032's exclusion bears on the black-hole-universe model's spin-axis claim only \u2014 it is not itself a bounce-cosmology detection. C2's catalogue is contingent on ledger #8 (known-object recovery benchmark) passing before it is drafted.",
    leadSlug: "paper-4p",
    supportSlugs: ["paper-3", "paper-1b"],
    status: "P4\u2032 fresh draft, review board not yet run. P3 is provenance support for the redirected anomaly map. P1B (namaster-proof) is an optional JOSS note.",
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
    version: "v2B.0.21",
    lastUpdated: "2026-09-05",
    tldr: "R3 truth-audit found R7's row draw is prover-predictable, not unpredictable, and fails open if its checked intermediate is omitted. Batch 4 (54 sealed runs, seal verified, seed committed before the seal) answers both with R8, a post-commitment verifier challenge: the rule-aware evasion (S7) and the omission (S8) are each caught 6/6 with zero honest false positives, while metadata forgery (S5) still escapes by construction. Batch 3's 24/24 miscount corrected to 30/30; all four batches now report class-level counts only. Prior art (Freivalds 1977, Fiat-Shamir 1986) cited.",
    path: publicationPath({}),
    pages: "16",
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
    pdfMeta: "Software metapaper · 16 pp · v2B.0.21 · package 0.1.7 · 41 tests · updated Sep 5, 2026 · md5 92df731d69859c74285a3c099a7aab1f — R3 closure plan (i): batch-4 R8 post-commitment verifier challenge integrated, R7 restated honestly, batch-3 stats corrected. ROUNDS STOPPED under R2; venue decision next.",
    changelog: [
      "v2B.0.21: R3 truth-audit closure (project-context/peer-reviews/INT_v3/P1B_v2B.0.20_R3_TRUTH_AUDIT_2026-09-05.md, 33 canonical findings, 27 genuinely-new-real). Batch 4 (RULES_v4_FROZEN.md, 54 runs sealed dbe6a713..., seed committed before the seal and revealed after) integrated: S7 (R7-aware effective multipole) 6/6 flagged, R7 fired 0/6 exactly as predicted, R8 fired 6/6; S8 (omit pseudo_cl) 6/6 flagged, R7 fails open 0/6 as predicted, R8 catches it 6/6; honest 0/6; S5 still escapes 0/6. R7 restated honestly as receipt-bound but prover-predictable, not unpredictable. Batch-3 '24/24' corrected to 30/30; all four batches now report class-level counts only, never run-level Clopper-Pearson intervals. Protocol rewritten for four batches. New prior-art paragraph (Freivalds 1977, Fiat-Shamir 1986, Klein & Roodman 2005). Dangling cross-references repointed; pymaster 3.0.1 corrected to 3.0; abstract shortened and rescoped for R7/R8; venue statement added (ACM REP primary, JOSS/JORS software companion). 16 pp, md5 92df731d69859c74285a3c099a7aab1f, tarball sha256 b8136d02fd9152a90909d8234c73ff6f40beabf35fb7a1e81b540682d1a0cdc3, Convex bump k5784xam4eaqav7dwc1end373d8dvtka. ROUNDS STOPPED under directive R2; next step is the venue decision + ASCL/Zenodo kit (Houston-gated).",
      "v2B.0.20: Batch 3 pre-registered blind round (pipelines/namaster_proof/VERIFICATION_PRIMITIVE_2026-09-04.md) adds R7 — recomputes 6 receipt-selected coupling-matrix rows against the declared pseudo-spectrum, fires iff the residual exceeds 1e-6*||p||. 48 sealed runs (8 arms x 6, seal abfe2793..., seal_verified true): honest 0/6 (FP upper bound 0.393); S1-S4 6/6 each; new S4b cross-run cache variant 6/6 (cross-run disjunct fired 4/6, first time it has fired); S6 effective-multipole 6/6 by R7 alone (lower bound 0.607, closes the batch-2 open item); S5 metadata forgery still escapes 6/6 by forging p := M C. Attempt 1 aborted before unsealing (seed-handling defect), preserved under public3_aborted/. Separately, a PyMaster (NaMaster 3.0.1) cross-check (pipelines/namaster_proof/PYMASTER_CROSSCHECK_2026-09-05.md) validates the in-house spin-0 MASTER estimator to floating-point round-off (coupling matrix 4.25e-13, bandpowers 1.54e-12 max relative diff). Abstract, blind-test section, limitations, and reproducibility statement updated. 15 pp, md5 c22158448310861711838e3544a0e04b, tarball sha256 01c6c1a6bad158aa5b02303727ef29011 9607c86b635d8308a3ff9db86c8d584. ROUNDS STOPPED under directive R2; one verification board now permitted following this science change.",
      "v2B.0.19: R2 closure (commits af7f2b18, a7cbd82e, 7a7f98f9) — statistics presentation corrected (class-level detection, no run-level intervals, 90% interval labelled correctly), estimator description fixed, traceability + reproducibility recipe added. 13 pp, md5 b1c68336fdd183918dcb677fddb9fd72, tarball sha256 9a695757d0ee5a493bcf6177fa53fcd1eda6d88a7ac76767b0d046df5ce57370, Convex bump k5753kmsvg9bp644qwt03vrrex8dv0v8. ROUNDS STOPPED under directive R2 pending a science/venue decision; batch 3, OTS confirmation, and PyMaster cross-check remain open.",
      "v2B.0.18: R1 truth-audit closure (project-context/peer-reviews/INT_v3/P1B_v2B.0.17_R1_TRUTH_AUDIT_2026-09-04.md, 23 canonical findings, 21 genuinely-new-real, 8 answered by integrating the pre-registered batch-2 blind test). Batch 2 (35 sealed runs, 7 arms x 5, rules frozen+committed before the seal) is now the PRIMARY result: S1-S4 20/20 (one-sided 95% Clopper-Pearson lower bound 0.861), honest 0/5 (FPR upper bound 0.451), S5 metadata-forgery escaped 5/5 (pre-declared), S6 effective-multipole escaped 5/5 with no rule added post hoc (independence caveat pre-declared and stated). Batch 1 (18 runs) relabelled the pilot/rule-development round; its post-hoc wall-clock and M-hash rule changes disclosed, not defended. New 'Relation to Provenance and Attestation Tooling' section (in-toto/SLSA/Sigstore-Rekor/ReproZip/Snakemake/Nextflow/RO-Crate/MLflow). SEM added to 500-realization recovery numbers; exact (not rounded) recovered values reported. Sealed digests of both batches OpenTimestamps-anchored (pending Bitcoin confirmation, disclosed as in-progress). Appendix table of all 35 batch-2 per-run verdicts added. 12 pp, md5 89cbca0fc922f9c1c63f1afaf35f8517, tarball sha256 00bb9c78c25882537bd295d48d7adb8ba8041c3a11a5e82e413539ba0654c652, Convex bump k571wkyj4scvf02q553tyq9r8d8dtnsx. R1 CLOSED; per directive R2 at most one further verification round permitted before an intervening science/scope decision.",
      "v2B.0.17: novelty lift #3 (project-context/NOVELTY_AUDIT_2026-09-04.md #3) — reframed from an N2 NaMaster-specific validation layer to a general verification primitive tested against a pre-declared, sealed BLIND shortcut-detection protocol (18 runs, 3 per arm, local CPU, ~1 min, $0). Detected all 4 receipt-visible shortcut classes (operator-skip, operator-truncate, grid-reduce+interpolate, cache-substitute) 12/12 with 0/3 false positives; metadata-forgery arm escaped 3/3, reported as the limitation. Two corrections found while running it: wall-clock is not a usable rule (would false-fire on 3/3 honest runs); an M-hash collision across honest runs is not cache-substitution evidence. New 'Blind Shortcut-Detection Test' section + 'What the receipt binds' table; title reframed to 'Content-bound execution receipts as a shortcut detector for pseudo-C_l computations'. 8 pp, md5 7bc21cbe7a1dfb837f08cae2c8b0f2b3.",
      "v2B.0.16: closed the 2026-07-23 Grok MAJOR ('irreconcilable internal contradiction' claim FALSIFIED — pyproject.toml, codemeta.json, CITATION.cff, __init__.py, Zenodo all read 0.1.7); title-page stamp labelled a manuscript revision; new Software version section states the document-vs-software namespace split.",
    ],
    artifacts: [
      { label: "Read PDF", href: "/papers/paper1b_namaster_proof_v2B.0.21.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper1b_namaster_proof_v2B.0.21.pdf", kind: "secondary", download: true },
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
    version: "v1N.0.5",
    lastUpdated: "2026-09-02",
    tldr: "Merges P1A and P1C into a single gr-qc/CQG paper. The derived axial spin-spin contact term is identified with Popławski's torsion-bounce repulsion mechanism (the positive result) while the same algebraic elimination closes four candidate dark-energy routes (the negative result). R3 verification pass closed (Claude major-revisions, Grok reject, Gemini major-revisions) with machine-checked regressions; automated review convergence criterion met and final author review recorded APPROVE — readiness 95. v1N.0.5: abstract trimmed to the CQG venue word cap (298 words); no science change.",
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
      "R3 verification pass closed — automated review converged (Claude major-revisions, Grok reject, Gemini major-revisions) with machine-checked regressions — v1N.0.4; final author review APPROVE; readiness 95",
      "Readiness composition (directive P): science closure + evidence & reproducibility + automated review convergence + packaging & PDF hygiene = 95; the remaining 5 requires Houston's explicit per-paper sign-off (quote recorded in SSOT) and is tracked separately from publishing-phase steps (arXiv endorsement, venue submission, independent human review)",
      "arXiv tarball assembled: SSOT/arxiv_tarballs/paper1bc_ech_note_arxiv_v1N.0.5.tar.gz",
      "Houston sign-off (readiness 95→100) has not been sought",
    ],
    preprintId: "HUBIFY-2026-001N",
    pdfMeta: "PDF · 11 pp · v1N.0.5 · created Sep 2, 2026 · md5 6836eb995effef298cca6830b1beda7c — abstract trimmed to CQG's word cap (298 words); no science change; REVISE (abstract cap) executed 2026-09-02.",
    changelog: [
      "v1N.0.5: REVISE (abstract cap) executed — abstract trimmed to venue word cap (298 words), no science change; tarball rebuilt.",
      "v1N.0.4: R3 verification pass closed — automated review converged (Claude major-revisions, Grok reject, Gemini major-revisions) with machine-checked regressions; final author review APPROVE; readiness 95; arXiv tarball assembled.",
      "v1N.0.3: R2 closure — 23/23 findings closed, including two errors inherited from P1C (8π coefficient, O5 parity). R2 verdicts: Claude major-revisions, Grok reject, Gemini major-revisions. R3 verification pass dispatched, verdicts pending.",
      "v1N.0.2: R1 closure — 42 finding-rows audited (Claude INT major-revisions, Grok API REJECT, Gemini API REJECT), 19 canonical real items closed via real edits (operator definitions, derivations, citations, bib pruned 113→26). Grown from Note to Paper form (10pp/7725 words). Compiled 4-pass, 0 undef refs, 0 overfull hboxes >10pt, 4/4 consistency-check rules PASS.",
      "v1N.0.1: first merged draft. Compiled 4-pass, 0 undef refs, 0 overfull hboxes, 4/4 consistency-check rules PASS. Superseded P1A (v1A.0.127, archived, Zenodo 10.5281/zenodo.21481838) and P1C (v1C.0.16, frozen, not independently submitted).",
    ],
    artifacts: [
      { label: "Read PDF", href: "/papers/paper1bc_ech_note_v1N.0.5.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper1bc_ech_note_v1N.0.5.pdf", kind: "secondary", download: true },
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
    archivedInto: {
      note: "Rescoped into P2′, the Track A A1 Letter (v2L.0.1) — 2026-09-02 portfolio decision, directive R3, ledger #1 CLOSED. P2 itself is unedited and stays listed as the archived full-length source (Zenodo DOI below); the Letter carries only the exact matter-contraction result plus the ledger-#1 closure and Cai(2009) factor-2 resolution.",
      successorSlug: "paper-2l",
      zenodoDoi: "https://doi.org/10.5281/zenodo.21461881",
    },
    title: "The Exact Matter-Contraction Non-Gaussian Amplitude: Four-Vertex Derivation and Conditional Large-Scale-Structure Mapping",
    plainTitle: "The bounce program's core prediction: an exact primordial non-Gaussianity amplitude (f_NL = −35/16)",
    version: "v1.7.130",
    lastUpdated: "2026-08-03",
    tldr: "Derives f_NL = −35/16 for the stated matter-contraction background and cubic action, then maps that result conditionally to published and in-house large-scale-structure sensitivity estimates. v1.7.130 adds the APS AI-use disclosure and a drift-proof deposit reference; its final-hash bounded confirmation and Houston review remain separate from the earlier evidence.",
    path: publicationPath({}),
    pages: "13",
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
    pdfMeta: "PDF · 12 pp · v1.7.130 · updated Jul 24, 2026 · md5 f7116fe3e2541d6f649876f2ec7789ee — v1.7.130 closes two PRD submission gates in one directive-G bundle: the APS-required AI-usage disclosure, which P2 carried none of, written full rather than minimised and naming only the models actually on this paper's record; and a drift-proof deposit reference that can no longer go stale against the deposited bytes. No readiness change.",
    changelog: [
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
      { label: "Read PDF", href: "/papers/02_full_draft_v1.7.130.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/02_full_draft_v1.7.130.pdf", kind: "secondary", download: true },
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
    title: "Multi-channel tests of the matter-bounce prediction f_NL = \u221235/16 and a joint (r, f_NL) no-go for single-field matter bounces",
    plainTitle: "A joint tensor-and-non-Gaussianity no-go for single-field matter bounces, with a viable curvaton route",
    version: "v3M.0.20",
    lastUpdated: "2026-09-05",
    tldr: "D-A3-14 (ledger row 19): the joint (r,f_NL) no-go generalizes to the full P(X) k-essence class \u2014 r=24c_s and the bounce's own cubic term are exactly independent of the cubic-action coefficient lambda (it cancels by parity in the bounce window), so no lambda opens the window; the best case (DBI line) gives r_min=12.57 (349\u00d7 BICEP/Keck). The lambda=s=0 scope qualifier is dropped. Single-field matter bounce (canonical or k-essence, any lambda) remains jointly excluded by r and f_NL; the curvaton route survives. Readiness 75.",
    path: publicationPath({}),
    pages: "18",
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
      "v3M.0.9: R3 truth-audit closure C1-C10 - transmitted-amplitude Table IV, delta N_c derivation appendix, induced-GW IR-slope correction, 8 numeric/definitional fixes, abstract restores PBH perturbativity/non-monotonicity caveats. Readiness 75.",
      "v3M.0.6: final-review REVISE executed (abstract 307 words).",
      "See project-context/PAPER_LINEAGE_2026-08-05.md for the recorded scope decision folding P2\u2032 theory into A3",
    ],
    preprintId: "HUBIFY-2026-A3M",
    pdfMeta: "PDF \u00b7 18 pp \u00b7 v3M.0.20 \u00b7 created Sep 5, 2026 \u00b7 md5 541a6b8a76c9cb2875c13dc15246bcce \u2014 S7 literature correction: Cai factor-of-2 span widened to Eqs. (38)-(41)+Fig. 5. Readiness 75 \u2014 ROUNDS STOPPED (R2).",
    changelog: [
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
      { label: "Read PDF", href: "/papers/a3_multichannel_arxiv_v3M.0.20.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/a3_multichannel_arxiv_v3M.0.20.pdf", kind: "secondary", download: true },
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
    version: "v4P.0.7",
    lastUpdated: "2026-09-05",
    tldr: "Folds P4 (8.47M-galaxy chirality catalog, observed-label dipole null) and P5 (DESIVAST void/non-void environment contrast) into one ≤15 pp ApJS paper, adding a new section reading Popławski's rotating-black-hole-universe papers for a computed dipole prediction. Under the minimal closure needed to make the claim testable, the catalog's own A₉₅ᵒᵇˢ≈0.98% sensitivity floor excludes alignment fractions η>0.98% at ≥95% coverage — a factor of 2–20× below the ~7–33% amplitudes reported by Longo (2011) and Shamir (2012–2025). Confirms the independent reanalyses of Iye, Yagi & Fukumoto (2021) and Patel & Desmond (2024). v4P.0.7: row-16 (iv-b) DESI DR1 BGS external environment result added — spec-z 3D N=121,417 and projected N=949,584 parity-fraction-by-density-contrast table, null verdict (largest excursion projected node-like f_CW z=+2.96, p=0.084 corrected); no science-conclusion change.",
    path: publicationPath({}),
    pages: "13",
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
      "R3 verification pass closed — automated review converged (Claude minor, Grok reject, Gemini minor) — v4P.0.4; final author review APPROVE; readiness 95",
      "arXiv tarball assembled: SSOT/arxiv_tarballs/paper4prime_chirality_test_arxiv_v4P.0.7.tar.gz",
      "Whether/when P5's standalone 42-pp paper is formally retired (vs. kept as an archived companion) is a Houston-gated decision",
      "Houston sign-off (readiness 95→100) has not been sought",
    ],
    preprintId: "HUBIFY-2026-004P",
    pdfMeta: "PDF · 13 pp · v4P.0.7 · created Sep 5, 2026 · md5 1fc6b21ae07accb0b2a3441e4a31ebc1 — row-16 (iv-b) BGS external environment result added; no science-conclusion change.",
    changelog: [
      "v4P.0.7: row-16 (iv-b) DESI DR1 BGS_BRIGHT-21.5 external environment result added — genuine external tracer field (300,043 galaxies), spec-z 3D N=121,417 + projected N=949,584 parity-by-density table, null (largest excursion projected node-like z=+2.96, p=0.084 corrected); recompiled to 13 pp; no science-conclusion change.",
      "v4P.0.6: row-16 disclosure integrated — pixel-level injection calibration (N=20k), full-parent selection systematic (confidence-cut/DES-leg), 15-statistic chirality x structure cross-correlation nulls; recompiled to 12 pp; no science-conclusion change.",
      "v4P.0.5: REVISE (abstract cap) executed — abstract trimmed to 246 words, no science change; tarball rebuilt.",
      "v4P.0.4: R3 verification pass closed — automated review converged (Claude minor / Grok reject / Gemini minor); final author review APPROVE; readiness 95; arXiv tarball assembled.",
      "v4P.0.3: R2 closure — 21/21 findings closed; monopole disclosed; genuine 95% CL limit ≈0.75% by Neyman inversion. R2 verdicts: Claude major-revisions, Grok reject, Gemini major-revisions.",
      "v4P.0.2: R1 board closed; recompiled to 10 pp. Compiled 4-pass, 0 undef refs, 0 overfull hboxes.",
      "v4P.0.1: first folded draft (P4 catalog + P5 environment section + new black-hole-universe exclusion section). Compiled 4-pass, 0 undef refs, 0 overfull hboxes. Superseded P4 (v1.0.274, archived, Zenodo 10.5281/zenodo.21461899) and P5 (v0.1.147, archived, not independently DOI'd).",
    ],
    artifacts: [
      { label: "Read PDF", href: "/papers/paper4prime_chirality_test_v4P.0.7.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper4prime_chirality_test_v4P.0.7.pdf", kind: "secondary", download: true },
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
    version: "v1S.0.4",
    lastUpdated: "2026-09-05",
    tldr: "R2 truth-audit closure (20 genuinely-new-real findings): abstract precision fixes, Eq. (4) sign flip, Cai 2009 counterfactual ratio corrected to 4/3, reference splits, gradient-order term folded into the bracket, Table I relabeled, and a required new Appendix A transcribing the second-order lapse/shift setup. Readiness 65 — ROUNDS STOPPED (R2) pending a science/venue decision.",
    path: publicationPath({}),
    pages: "6",
    refs: "—",
    readiness: 65,
    statusVariant: "amber",
    target: "gr-qc / astro-ph.CO (candidate; cross-list astro-ph.CO)",
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
      "R2 CLOSED (2026-09-04): 20 genuinely-new-real findings closed in v1S.0.3. Per directive R2's convergence budget (R1+R2 exhaust it), rounds STOP here pending a science or venue decision.",
      "Venue/arXiv-category selection not yet finalized (candidate: gr-qc or astro-ph.CO, cross-list astro-ph.CO given the P2/P2L family)",
      "See project-context/SSOT/paper-su/status.md for the full close-the-gap section",
    ],
    preprintId: "HUBIFY-2026-SU",
    pdfMeta: "PDF · 6 pp · v1S.0.4 · created Sep 5, 2026 · md5 32ef7a73c509eeb5cf4383f2e3ee00fe — S7 literature correction: Cai (2009) Eq. (37) confirmed correct, Eqs. (38)-(41)/Fig. 5 uniformly 2x. Readiness 65 — ROUNDS STOPPED (R2).",
    changelog: [
      "v1S.0.3: R2 truth-audit closure (project-context/peer-reviews/INT_v3/PSU_v1S.0.2_R2_TRUTH_AUDIT_2026-09-04.md, 20 genuinely-new-real findings across Grok/Gemini/Fable INT legs). All 11 editorial items closed: abstract precision, Eq. (4) sign flip (sympy-verified), algebra statement corrected (1-lambda=I/3), Cai 2009 counterfactual ratio corrected to 4/3 (was a wrong 8/7 transcribed unverified from R1), references split/fixed, gradient-expansion order term folded into the [1-I/3+O(.)] bracket, Eq. (1) caveats stated, Table I relabeled, reproducibility paths switched to \\url{}, and a required new self-contained Appendix A transcribing the second-order lapse/shift setup + five kernel contributions + two-label translation. 4-pass, 0 undef refs, 0 overfull hboxes >10pt, 6 pp (up from 4), md5 afeda89e03a7e0bc688d84c423d164fb, tarball paper_su_arxiv_v1S.0.3.tar.gz, Convex bump k572q3ewgfsmjb02ets0jyh9b58dvghn. Readiness 65 (up from 55) -- ROUNDS STOPPED (R2) pending a science or venue decision.",
      "v1S.0.2: D-PSU-1 reframe + R1 truth-audit closure (project-context/peer-reviews/INT_v3/PSU_v1S.0.1_R1_TRUTH_AUDIT_2026-09-04.md, 21 genuinely-new-real findings, 5 falsified, 1 opinion, 1 out-of-scope). Title/abstract reframed: the isotropic separate universe computes an exact, invertible change of variable, delta N_c = zeta_L,f[1 - I/3] + O(k_L^2/a^2H^2) with I the ratio of the neglected (eps/c_s^2)-weighted integral to zeta_L,f; the O(1) error arises only when delta N_c is identified with zeta, i.e. iff I=O(1) (I=0 on attractor/ekpyrotic rows; reduces to sqrt(eps_s eps_f)-eps_f in USR; to eps in the dust contraction). Label-resolved compositions: initial label reproduces -5 exactly for all constant eps; final label gives -25/4+(15/4)mu^2 at eps=3/2. Eq. (2) restores the dropped O(k_L^2/a^2H^2) gradient term; Table I gains an f^in-in_mono=-15/8 column; Cai et al. 2009 cited with the located factor-of-2. All three science gates (S1/S2/S3) resolved (research/theory_audit/psu_gates_S1_S2_2026_09_04.{md,py,json}). 4-pass, 0 undef refs, 0 overfull hboxes >10pt, 4 pp, md5 fcbecd03679fdc4ecae3956c35b9b08c, tarball a3_su/paper_su_arxiv_v1S.0.2.tar.gz. Readiness 55 (up from 40) — one further verification round permitted under directive R2.",
      "v1S.0.1: first draft, spun out of A3M Appendix A per PAPER_LINEAGE_2026-08-05.md's disposition trail (original claim vs new claim). 4-pass pdflatex, 0 undef refs, 0 overfull hboxes >10pt, md5 b974dc018e0f5a9f62aa92ea8cef697b. Readiness 40.",
    ],
    artifacts: [
      { label: "Read PDF", href: "/papers/paper_su_criterion_v1S.0.4.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper_su_criterion_v1S.0.4.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/arxiv/paper_su_criterion",
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
