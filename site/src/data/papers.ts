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
  title: string;
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
  artifacts: Array<{
    label: string;
    href: string;
    kind: "primary" | "secondary";
    external?: boolean;
    download?: boolean;
  }>;
}

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
      note: "P1B v109/P4 v245 boards complete; closure artifacts still have open major gates",
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
    title: "Algebraic Cartan Elimination in Minimal Einstein–Cartan–Holst Gravity: Spin-Sourced Contact and Zero-Spin Scalar Branches",
    version: "v1A.0.123",
    lastUpdated: "2026-07-14",
    tldr: "A compact CQG Note deriving the minimal Einstein–Cartan–Holst axial contact interaction and the zero-spin canonical-scalar branch. It fixes conventions, separates coefficient-level statements from state-dependent observables, and provides a commit-pinned hard-cutoff NJL diagnostic. A subscription-backed exact-PDF reviewer returned ACCEPT with no tagged findings; human, release, and external-science gates remain.",
    path: publicationPath({}),
    pages: "7",
    refs: "11",
    readiness: 62,
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
    ],
    surveys: ["No survey likelihood — algebraic and field-theory Note"],
    predictions: ["Axial contact coefficient in the stated ECH convention", "Zero-spin scalar transparency under matched boundary data"],
    figures: ["Table I: hard-cutoff coefficient-to-threshold diagnostics"],
    remainingWork: [
      "Human CQG/editorial review — automated ACCEPT is not journal acceptance",
      "Authorize a manuscript/source license; exact bundle/proof pass but deposit metadata and any draft intentionally fail closed until then",
      "After license authorization, verify a reversible draft before any immutable archive/DOI action",
      "Alternate-regulator robustness beyond the declared hard-cutoff convention",
      "Matched Lorentzian state/stress observable and a state-specific renormalized axial expectation value",
    ],
    preprintId: "HUBIFY-2026-001",
    pdfMeta: "PDF · 7 pp · v1A.0.123 · updated Jul 14, 2026 · sha256 4c450a67 — exact ChatGPT-subscription Codex CLI confirmation: ACCEPT (0 MAJOR / 0 MINOR); no OpenAI API or Anthropic; readiness unchanged and human/external/release gates remain.",
    changelog: [
      "v1A.0.123: corrected the pinned NJL artifact to the manuscript's three-row M_Pl-only scope and replaced active mutable-main artifact URLs with commit-pinned links; exact subscription-backed Codex confirmation returned ACCEPT (0 MAJOR / 0 MINOR). Readiness unchanged.",
    ],
    artifacts: [
      { label: "Read PDF", href: "/papers/paper1a_ech_nogo_v1A.0.123.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper1a_ech_nogo_v1A.0.123.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/bdbb2242199a8eb50bdee825b98d42ea8a3de523/arxiv/paper1a_ech_nogo.tex",
        kind: "secondary",
        external: true,
      },
      {
        label: "Exact-PDF review evidence",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P1A-v1A.0.123-EXACTPDF-4c450a67-CQG-NOTE-CODEX-SUBSCRIPTION-CONFIRM/RESULT.md",
        kind: "secondary",
        external: true,
      },
    ],
  },
  {
    slug: "paper-1b",
    number: "1B",
    title: "namaster-proof: Exact pseudo-Cℓ Window Inference and Tamper-Evident Provenance for Reproducible Spin-2 Analyses",
    version: "v2B.0.6",
    lastUpdated: "2026-07-16",
    tldr: "P1B is a focused software metapaper around namaster-proof 0.1.4. v2B.0.6 closes two confirmation regressions: the sharded-validation paragraph is back in its technical section and the printed minimal API call now uses the real beta_rad interface. Archive, confirmation, and human review remain open; readiness holds 56.",
    path: publicationPath({}),
    pages: "5",
    refs: "4",
    readiness: 56,
    statusVariant: "amber",
    target: "Journal of Open Research Software — Software Metapaper",
    description: "A narrow, installable Python verification layer for exact NaMaster bandpower-window inference, deterministic multipole-support contracts, and tamper-evident JSON result receipts. The paper makes software and reproducibility claims only; it does not claim a cosmological detection or a novel physical model.",
    keyResults: [
      "Exact contraction of uniformly rotated EE/EB/BE/BB spectra through the complete NaMaster bandpower-window tensor",
      "Fixed-grid recovery and direct equivalence testing against the couple-cell/decouple-cell operator",
      "Atomic JSON publication with coherent-snapshot SHA-256 receipts and fail-closed metadata validation",
      "Deterministic field, bin, and harmonic-limit contracts whose final exclusive bin edge is ℓmax+1",
      "28 automated tests across Linux Python 3.10–3.13 plus Windows 3.12, including non-finite JSON and verifier/publisher concurrency regressions",
      "Associated 500-realization physical example recovers +0.270°, +0.342°, and the null at the declared 0.001° grid resolution",
      "Independent PyMaster 2.6 integration: injected/exact-recovered 0.250°, effective-ℓ shortcut 0.315°, exact operator residual 6.78×10⁻²¹",
    ],
    surveys: ["Synthetic linear workspace", "Synthetic CAMB/NaMaster validation"],
    predictions: ["Exact-window operator equivalence", "Tamper-evident result validation", "Deterministic multipole contracts"],
    figures: ["Software architecture", "Exact-window equations", "Executable worked examples"],
    remainingWork: [
      "Run an exact-PDF non-Anthropic confirmation review of v2B.0.6",
      "Obtain independent human software review and publish an immutable archive/DOI",
      "Optionally publish the package to an independent package index after release QA",
    ],
    preprintId: "HUBIFY-2026-001B",
    pdfMeta: "Software metapaper · 5 pp · v2B.0.6 · package 0.1.4 · 28 tests · sha256 33da2a70bd559766b0988de5885f12333ef02b86e8a45bcf0a8057dbd8f80c9a · executable API example + corrected section boundary · visual audit passed · exact confirmation pending · readiness holds 56",
    artifacts: [
      { label: "Read PDF", href: "/papers/paper1b_namaster_proof.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper1b_namaster_proof.pdf", kind: "secondary", download: true },
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
    ],
  },
  {
    slug: "paper-2",
    number: "2",
    title: "The Exact Matter-Contraction Non-Gaussian Amplitude: Four-Vertex Derivation and Conditional Large-Scale-Structure Mapping",
    version: "v1.7.122",
    lastUpdated: "2026-07-14",
    tldr: "Derives f_NL = −35/16 for the stated matter-contraction background and cubic action, then maps that result conditionally to published and in-house large-scale-structure sensitivity estimates. The observational forecasts are illustrative, not a completed detection claim.",
    path: publicationPath({}),
    pages: "10",
    refs: "39",
    readiness: 80,
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
      "REDSHIFT-SPACE (RSD) tree bispectrum Fisher (c14, v1.7.103): extends c13 with the Kaiser Z1=b+fμ² factor + SCF99/Sefusatti Z2 kernel, growth f(z)=fσ8/σ8 from the same CAMB Planck2018, orientation-integrated over full (μ1,φ) so ℓ=0,2,4 content is exact. σ(f_NL^local) tightens to 0.415 (b-fix)/0.449 (b-marg) vs real-space 0.687 (+34.7% tighter; RSD/Heinrich 0.64); σ(f_NL^bounce)=0.417/0.449; r_eff≈0.99 persists in redshift space; f→0 reproduces c13 to 6 sig-figs. Unmarginalized −35/16 significance rises to 4.9–5.2σ (before the systematic + GR-projection budget) — retires the 'real-space monopole only, ~18% offset' limitation with real computation",
      "Template mismatch quantification between bounce and local shapes",
      "Joint (f_NL, n_fNL) SDB Fisher rebuilt from committed code: subordinate channel at 1.4σ (fixed-bias) / 0.6σ (bias-marginalized); earlier ~9.9σ joint-Fisher claim withdrawn (not reproducible from documented inputs)",
      "Table III rebuilt from committed c9g recompute: BF/lnBF per config 3.5e8/7.0, 4.5e5/6.1, 6.4e2/4.7 (envelope ~9–14 under bounce-amplitude bookkeeping); Φ/ζ convention mapping proven exactly; 0.5000 ratio identified as the −2Im operator identity",
      "QSFI scaling endpoints corrected per Chen–Wang; −35/16 single-field result re-attributed to Li–Quintin–Wang–Cai at 17 sites",
      "Continuous-GR-recovery marginalization (c9k): bounce preference robust at BF = 6.0; GR-degradation calibration corrected ~15% → ~23% (c9k-verified)",
      "σ_theory continuous marginalization (c9l): configuration ranking stable under continuous theory-error treatment (R25conf wave)",
    ],
    surveys: ["DESI DR1 (current constraint σ ≈ 4.1 combined)"],
    predictions: ["f_NL = -35/16"],
    figures: ["Fisher forecast contours", "Template overlap matrix", "σ(f_NL) sensitivity curves"],
    remainingWork: [
      "Independent human scientific review and venue-specific scope/format check",
      "Exact reversible draft is remotely digest-verified; Houston still controls immutable archive/DOI publication",
      "Direct cubic bounce transfer, survey-native SPHEREx covariance/likelihood, and any model-specific torsion bound remain open",
      "Author arXiv endorsement and journal-submission decision",
    ],
    preprintId: "HUBIFY-2026-002",
    pdfMeta: "PDF · 10 pp · v1.7.122 · updated Jul 14, 2026 · sha256 4097bac5 — routing-corrected exact-PDF board: Codex via ChatGPT subscription ACCEPT · Gemini direct ACCEPT · Grok direct ACCEPT. M45 lifted the external cap to 80; no Anthropic, DOI, submission, or journal acceptance is claimed.",
    changelog: [
      "directive-M presentation restructure (v1.7.116, ZERO content change): consolidated the repeated scope/caveat/proxy/illustrative statements the REJECT/minor raws named (DP2-30 presentation-scope) to canonical homes + cross-refs, relegated the cosmic-birefringence auxiliary paragraph to a new Appendix (app:birefringence), tightened the Caveats→Scope-and-limitations register. Freeze held: every number byte-identical, −35/16 quadruple-certification untouched. INT re-test: OpenAI REJECT / Grok MAJOR / Gemini MAJOR / Claude ABSENT; 0 genuinely-new editable findings, 0 regressions — residual verdicts are the documented LLM harsh-referee floor. Nothing fabricated.",
      "c15 GR-leg basis-mismatch fix (v1.7.115, INT-Claude genuinely-new MAJOR): the channel-native Fisher built ∂B/∂A_GR = b·b·b·S_GR without the M123 transfer product the f_NL primordial leg carries, leaving the GR template in potential space vs the f_NL density basis — collapsing F[2,2]~1e-18 and faking ρ(f_NL,A_GR)≈−0.001 orthogonality. Fixed (M123 promotion) + re-ran: corrected ρ=−0.42 (2×2)/−0.49 (3×3), σ_marg=0.94→2.32σ. Channel-native floor still > proxy 1.30σ floor, so the retained proxy conclusion holds. −35/16 unchanged, nothing fabricated.",
      "Per-vertex term-by-term derivation table (v1.7.105, R9 Grok+ChatGPT MAJOR): added Appendix A Table VII walking each of Cai's four cubic vertices through the squeezed AND equilateral limits (field-redef -25/16, L_zzdd -5/32, mixed 0, highest-order -15/32 squeezed), both columns summing exact-fraction to -35/16 and -255/128; transcribed verbatim from the committed sympy cert script, no new math. Plus a consolidated gauge-vs-physical-frame f_NL table (Gemini minor). -35/16 unchanged.",
      "Appendix A vertex-algebra display (v1.7.104, deep-Grok MAJOR): added the collapsed exact vertex-sum degree-9 polynomial + the epsilon-order-grouped squeezed contributions (fNL|eps^1=-5/2, |eps^2=+5/16, |eps^3=0 -> -35/16), both transcribed verbatim from the committed sympy certification script; no new math, -35/16 unchanged.",
    ],
    artifacts: [
      { label: "Read PDF", href: "/papers/02_full_draft_v1.7.122.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/02_full_draft_v1.7.122.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/research/focused_paper_source_integration/02_full_draft.tex",
        kind: "secondary",
        external: true,
      },
    ],
  },
  {
    slug: "paper-3",
    number: "3",
    title: "Public-ID Recovery for a Historical DESI DR1 Anomaly List: 170 High-Coordinate-Consistency Core and 11 Lower-Confidence Positional Associations",
    version: "v3.2.0-r8",
    lastUpdated: "2026-07-14",
    tldr: "Recovers 181 public DESI DR1 TARGETIDs from a frozen historical anomaly list, split transparently into 170 high-coordinate-consistency core associations and 11 lower-confidence positional associations; this is an archive-recovery product, not a purity, novelty, or detection claim.",
    path: publicationPath({}),
    pages: "16",
    refs: "12",
    readiness: 56,
    statusVariant: "amber",
    target: "ApJS",
    description: "A focused, reproducible public-ID recovery of a frozen historical DESI anomaly list. The declared 1-arcsec positional join yields 181 warning-free global-primary DESI DR1 associations: 170 at or below 0.1 arcsec and 11 lower-confidence associations between 0.1 and 1 arcsec. The release carries exact source-row provenance, explicit quality tiers, warned-row auxiliary data, shift controls, checksums, and a clean-checkout validator while declining physical classification, purity, novelty, and anomaly-rate claims unsupported by the surviving historical lineage.",
    keyResults: [
      "181 unique warning-free global-primary DESI DR1 TARGETIDs, partitioned exactly into 170 core and 11 lower-confidence positional associations",
      "20,299,155 eligible DESI rows → 2,468 positional parents → 2,448 global-primary rows → 181 warning-free associations",
      "Every released row and all 18 carried DESI fields were re-read from the recorded FITS row and compared exactly",
      "Sixteen deterministic local shifts yield 86.7 ± 14.4 parent and 76.2 ± 13.3 warning-free-primary associations within 1 arcsec; the 11-row tail is not treated as secure identity",
      "A separately released 2,267-row warned auxiliary table preserves inspectability without admitting warned rows to the primary catalog",
      "Original-member sensitivity retains 180/181 rows; only P3-DESI-000030 fails the alternate 1-arcsec rule at 1.979009 arcsec",
      "The definitive bundle contains 41 tracked files and passes exact clean-tree validation of all 38 manifest payloads",
      "r7 board: Grok direct API ACCEPT, Gemini direct API MINOR, Codex ChatGPT-subscription MAJOR; exact r8 subscription confirmation: ACCEPT with zero in-scope blockers",
    ],
    surveys: ["DESI DR1"],
    predictions: ["Public-ID recovery", "Coordinate-association quality tiers", "Archive reproducibility"],
    figures: ["Selection waterfall", "Separation distribution", "Shift-control radius curves", "Catalog sky distribution"],
    remainingWork: [
      "Human ApJS/editorial review and submission decision; automated ACCEPT is not journal acceptance",
      "Resolve the recorded 1.82327 pt minor hbox warning during the next versioned edit; the current 16-page raster audit shows no clipping or overlap",
      "A reversible exact-commit draft is verified; Houston still controls immutable archive/DOI publication and arXiv/ApJS submission",
      "Object-level physical interpretation and any representative-control performance study remain separate new-science work",
    ],
    preprintId: "HUBIFY-2026-003",
    pdfMeta: "PDF · 16 pp · v3.2.0-r8 · updated Jul 14, 2026 · md5 8faac098",
    artifacts: [
      { label: "Read PDF", href: "/papers/paper3_apjs_v3.2.0-r8.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper3_apjs_v3.2.0-r8.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/d155eb27488b271be12942b1a1be8b3c39dd24f4/pipelines/p3_anomaly_engine/paper3_apjs.tex",
        kind: "secondary",
        external: true,
      },
      {
        label: "r8 review receipt",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/project-context/peer-reviews/INT_apjs/CONFIRM_2026-07-14_P3_v3.2.0-r8_b5f254f9/RUN_RECEIPT.json",
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
    title: "An Observed-Label Chirality-Dipole Null in 890,069 Quality-Controlled High-Confidence DESI Spirals and an 8.5-Million-Galaxy Catalog",
    version: "v1.0.260",
    lastUpdated: "2026-07-16",
    tldr: "Classifies 8.47M galaxies. The strict safe-sample observed-label statistic remains null-consistent (z=0.63465, p=0.23768), while exact-support harmonic results remain systematics diagnostics. Training, covariance, archive, exact re-review, and human gates remain; readiness holds 80.",
    path: publicationPath({}),
    pages: "25",
    refs: "18",
    readiness: 80,
    statusVariant: "amber",
    target: "The Astrophysical Journal Supplement Series",
    description: "The galaxy chirality catalog: 8.47M galaxies classified CW/CCW by a ViT-Small ensemble with flip-equivariant TTA. v1.0.260 binds the manuscript to a content-addressed strict-primary overlay while retaining the unchanged immutable public catalog revision. The primary is null-consistent; harmonic results are systematics diagnostics only. Publishing and verifying the immutable provider overlay, training replay, spatial covariance, complete metadata, a DOI-backed archive, exact re-review, and human review remain open.",
    keyResults: [
      "8.47M galaxies classified (1,592,107 CW / 1,609,053 CCW / 5,273,371 NOT_SPIRAL)",
      "Strict release-safe primary: N_selected=890,069, N_support=887,472, z_mom=+0.63465, one-sided empirical-rank p=0.23768",
      "Exact 24,087-pixel FSC support: fixed-occupancy harmonic z=6.923, p=0.001996; apodized z=7.033; 10,000-draw binomial z=7.207, p=0.00059994; systematics diagnostics only",
      "Corrected public ApJS bundle: immutable HF data commit db110233 contains the safe catalog, 249,066-row quarantine, fixed-occupancy primary array f6360f4b, distinct pixel-permutation diagnostic 62bb1c01, manifest, schema, checksums, and reproducer; receipt e535b262 verifies remote paths and byte sizes",
      "Release-integrity closure: HF dataset revision 43fc8a5b publishes the complete clean-bootstrap semantic contract; HF model revision 6f113097 publishes the production-accurate model card",
      "Catalog C semantic validation streams all 8,474,531 primary and 249,066 quarantine rows and proves exact object-ID/HC-flag equivalence with zero failed gates; Catalog B remains historical and unreleased",
      "Galaxy Zoo 1 human-vote cross-check: 46,017 matched inputs, exactly 4,963 on the 394-pixel N_pixel>10 support and 41,054 excluded; null-consistent at z=−0.539, p=0.666 under its legacy pixel-permutation convention",
      "ℓ=1 MASTER decoupling numerically stable: full coupling-matrix condition number 3.17 (3.11/3.25 at 1°/3° apodization)",
      "Bin-by-bin CW flatness audited across 4 morphology axes; residuals are classification correlations, orthogonal to dipole tests",
      "Finite injection pilots report score-pass fractions only; they do not establish calibrated A50/A95 recovery thresholds or physical bounds",
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
      "Freeze and validate full-catalog imaging-leg, depth, seeing, PSF, and redshift metadata; the exact morphology join is now public but these fields remain unavailable",
      "Publish and byte-verify the strict-primary overlay at an immutable provider revision, then run and truth-audit exact non-Anthropic confirmation on v1.0.260 before any DOI publication",
      "Prove the exact training split/seed/realization and propagate spatially varying confusion with covariance",
      "Author arXiv endorsement and journal-submission decision",
    ],
    preprintId: "HUBIFY-2026-004",
    pdfMeta: "PDF · 25 pp · v1.0.260 · sha256 2a747d6a · md5 2e2e1fa4 — strict-primary overlay locally synchronized; immutable provider publication, exact re-review, and external/human gates remain. Readiness holds 80.",
    changelog: [
      "End-to-end transfer-calibration scope statement (v1.0.229): the injection-recovery section now delineates which links of the classify→dipole chain the sweep traverses (map-making + dipole estimator + null calibration) versus which it does not (ViT classifier, NS triage, confidence cut, spatially-varying confusion), shows from the committed GZ1 confusion numbers that the asymmetric-confusion transfer slope g_eff = s_CW + s_CCW − 1 = 0.398 equals the symmetric g = 2a − 1 = 0.398 for the near-balanced parent (so CW/CCW asymmetry does not degrade the physical-amplitude conversion), and honest-flags the full image-level end-to-end injection through the classifier as requiring new simulation — operative claims held to the observed hard-label field. No number changed, nothing fabricated.",
      "R9 ACCEPT-track minor closure (v1.0.225): Grok = minor-revisions, Gemini = 'Accept with minor revisions'; both referees' concrete minors closed with real edits (no number changed). Abstract z≈−18 now explicitly labeled a model-dependent template-disfavor statistic (not a frequentist exclusion) with the injection-recovery A95∈(1.0,1.5]% cross-referenced as the primary real-space falsification; added a main-text downstream-user warning that raw p_eq scores are not frequentist likelihoods (cite Appendix-B ECE ≥0.25–0.36); abstract real-space p now names its isotropic-pixel-permutation null. ChatGPT major = presentation/consolidation of already-disclosed content.",
      "Deep-tier Gemini MAJOR closure (v1.0.224): added self-contained training-data provenance table + a probabilistic-calibration paragraph quantifying a real top-label ECE lower bound from the committed GZ1 confusion matrix (mean-conf 0.951 vs 3-class acc 0.5871 -> ECE>=0.36; chirality 0.6991 -> >=0.25), proven invariant to any monotone recalibration; surfaced existing committed data, no number changed.",
    ],
    artifacts: [
      { label: "Read PDF", href: "https://raw.githubusercontent.com/Hubify-Projects/bigbounce/b4593563591a0eb7aac4e68eafe302715377a439/site/public/papers/chirality_catalog_paper_v1.0.260.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "https://raw.githubusercontent.com/Hubify-Projects/bigbounce/b4593563591a0eb7aac4e68eafe302715377a439/site/public/papers/chirality_catalog_paper_v1.0.260.pdf", kind: "secondary", download: true },
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
    ],
  },
  {
    slug: "paper-5",
    number: "5",
    title: "Environmental Dependence of Spiral Chirality: A DESIVAST Catalog-Native Void Non-Detection with Secondary Cosmic-Web Cross-Checks",
    version: "v0.1.139-2026-07-16",
    lastUpdated: "2026-07-16",
    tldr: "On the released DESIVAST GALZONE parent, the focal exploratory analysis detects no void/non-void difference in classifier-labelled CW fraction; this bounded non-detection does not establish physical environment independence.",
    path: publicationPath({}),
    pages: "41",
    refs: "—",
    readiness: 74,
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
      "v0.1.139 is a retained local candidate, not an immutable public release; a public tag/archive/DOI and verified artifact links remain required before submission",
    ],
    surveys: ["P4 chirality catalog (HF bamfai/galaxy-chirality-catalog, 8.47M)", "DESI DR1 zall-pix-iron.fits (~22.5M rows; matched subset 16.4M after quality cuts)", "DESIVAST void catalogs (3 algorithms)"],
    predictions: ["LSS-environment-dependent chirality test (cosmic-web alignment)"],
    figures: ["Matched-catalog footprint", "Per-environment CW fractions", "DESIVAST void-spiral test", "z-shell robustness", "HEALPix coherence at three resolutions"],
    remainingWork: [
      "Finalize Paper IV labels, weights, and provenance, then reverify P5 against that independently reviewable release",
      "Publish an immutable P5 tag/archive/DOI and verify every A1–A44 link; local retention is not a public release",
      "Run exact-PDF confirmation review on v0.1.139 and keep the sparse interaction and secondary T-Web limitations explicit",
      "Resolve the human/editorial gate through actual AJ review; automated evidence is not journal acceptance",
    ],
    preprintId: "HUBIFY-2026-005",
    pdfMeta: "PDF · 41 pp · v0.1.139-2026-07-16 · sha256 948e0412 · md5 21a4a79f — unanimous-minor residual defects closed; release, exact re-review, editorial, and human AJ gates remain. Readiness holds 74.",
    artifacts: [
      { label: "Read PDF", href: "/papers/p5_desi_chirality_v0.1.139-2026-07-16.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/p5_desi_chirality_v0.1.139-2026-07-16.pdf", kind: "secondary", download: true },
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
