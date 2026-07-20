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
    version: "v1A.0.124",
    lastUpdated: "2026-07-16",
    tldr: "A compact CQG Note deriving the minimal Einstein–Cartan–Holst axial contact interaction and the zero-spin canonical-scalar branch. It fixes conventions, separates coefficient-level statements from state-dependent observables, and provides a commit-pinned hard-cutoff NJL diagnostic. The exact v1A.0.124 confirmation board (Grok MINOR / Gemini MINOR / Claude MAJOR) truth-audited all 13 findings to 0 genuinely-new-real — P1A is CONVERGED to human gates. No version change; human CQG review, license/deposit authorization, and alternate-regulator robustness remain.",
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
    pdfMeta: "PDF · 7 pp · v1A.0.124 · updated Jul 16, 2026 · md5 11172191d176dc8fc0651a1af682312d · sha256 5689a5f8b4c6488b9fa1c4d2225d3c0211b830b028b0284299c00f912d0977aa — exact v1A.0.124 confirmation board (Grok MINOR / Gemini MINOR / Claude MAJOR) truth-audited to 0 genuinely-new-real; P1A CONVERGED to human gates. Readiness cap 62 HOLDS.",
    changelog: [
      "2026-07-16 confirmation board: exact v1A.0.124 board Grok MINOR / Gemini MINOR / Claude MAJOR (13 findings); truth audit found 0 genuinely-new-real — algebra verified a third time, all majors disclosed re-flags or Houston-gated venue items. P1A CONVERGED to human gates (CQG significance disposition, license/deposit authorization, alternate-regulator robustness). No version change.",
      "v1A.0.124: Claude Opus-tier subagent exact-PDF board on v1A.0.123 returned MAJOR (2 MAJOR / 4 MINOR); truth audit found 0 correctness errors (algebra hand-verified) — the majors are disclosed re-flags/tracked gates. Closed 3 sub-sentence editorial items: shows the torsion-lemma 4D contraction coefficients (derived from the manuscript's own identities), relabels Sec III.B \"mean-field NJL diagnostic\" with scope softening, and consolidates the relation-to-prior-work sentence. Readiness cap 62 unchanged.",
      "v1A.0.123: corrected the pinned NJL artifact to the manuscript's three-row M_Pl-only scope and replaced active mutable-main artifact URLs with commit-pinned links; exact subscription-backed Codex confirmation returned ACCEPT (0 MAJOR / 0 MINOR). Readiness unchanged.",
    ],
    artifacts: [
      { label: "Read PDF", href: "/papers/paper1a_ech_nogo_v1A.0.124.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper1a_ech_nogo_v1A.0.124.pdf", kind: "secondary", download: true },
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
    ],
  },
  {
    slug: "paper-1b",
    number: "1B",
    title: "namaster-proof: Exact pseudo-Cℓ Window Inference and Tamper-Evident Provenance for Reproducible Spin-2 Analyses",
    version: "v2B.0.11",
    lastUpdated: "2026-07-16",
    tldr: "P1B is a focused software metapaper around namaster-proof 0.1.7. The exact v2B.0.9 confirmation board (Grok REJECT / Gemini MINOR / Claude MAJOR) FALSIFIED the 'workspace tensor not reproducible' premise — it is deterministically regenerable from committed RNG-free code. v2B.0.10 closes 4 optional polish items: a new recheck script, real committed execution costs, a pip-install one-liner, and the retained macOS-untested label. Archive DOI, correspondence metadata, and human review remain open; readiness holds 56.",
    path: publicationPath({}),
    pages: "6",
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
      "Houston-gated: immutable archive DOI (Zenodo or PyPI+Zenodo), correspondence metadata, human software review — the exact v2B.0.10 board + truth audit found P1B science exhausted with the DOI as the only remaining major; v2B.0.11 adds the pytest command + non-affiliation sentences and no further board is owed on that two-sentence diff per the content-hash stop rule",
      "Obtain independent human software review and publish an immutable archive/DOI",
      "Publish package 0.1.7 to an independent package index once a PyPI token is available (Houston gate) after release QA",
    ],
    preprintId: "HUBIFY-2026-001B",
    pdfMeta: "Software metapaper · 6 pp · v2B.0.11 · package 0.1.7 · 41 tests · md5 7c14c2a1d4fb58ed652a2231bbd7e17a · exact v2B.0.10 board truth-audited (science exhausted; only the Houston-gated DOI/metadata/human gates remain); v2B.0.11 adds the pytest invocation + non-affiliation sentences · readiness holds 56",
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
    version: "v1.7.126",
    lastUpdated: "2026-07-20",
    tldr: "Derives f_NL = −35/16 for the stated matter-contraction background and cubic action, then maps that result conditionally to published and in-house large-scale-structure sensitivity estimates. v1.7.125 adds a computed model-specific Einstein-Cartan four-fermion torsion bound, converting assumption (f) from asserted to bounded. The observational forecasts are illustrative, not a completed detection claim.",
    path: publicationPath({}),
    pages: "11",
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
      "G3 model-specific torsion bound (v1.7.125, Eq. 5): |δf_NL^tor| ≲ (35/16)(3/16)[γ²/(1+γ²)] κ n_ψ,c²/ρ_c via a sympy Einstein-Cartan four-fermion estimate anchored to the companion P1A's convention-audited contact term (benchmark reproduced to 0.1%); within EFT validity (x_ψ<1) the bound saturates at prefactor 0.022 (γ=0.2375) to 0.21 (γ=1) — torsion never exceeds ~1-10% of the -35/16 amplitude, <<1e-3 for sub-Planckian n_ψ,c — converting assumption (f) from asserted to bounded",
    ],
    surveys: ["DESI DR1 (current constraint σ ≈ 4.1 combined)"],
    predictions: ["f_NL = -35/16"],
    figures: ["Fisher forecast contours", "Template overlap matrix", "σ(f_NL) sensitivity curves"],
    remainingWork: [
      "Independent human scientific review and venue-specific scope/format check",
      "Immutable archive/DOI is now published and embedded (v1.7.126, Zenodo 10.5281/zenodo.21461881); the record archives the reviewed v1.7.125 bytes and the concept DOI carries forward to future versions",
      "Direct cubic bounce transfer (dressed-metric intermediate now regulator-independent to <1%, IC-epoch placement + quantum-mass term remain) and survey-native SPHEREx covariance/likelihood remain open; the model-specific torsion bound is now computed and bounded (v1.7.125)",
      "Author arXiv endorsement and journal-submission decision",
    ],
    preprintId: "HUBIFY-2026-002",
    pdfMeta: "PDF · 11 pp · v1.7.126 · updated Jul 20, 2026 · md5 bd10fe4ab022485cf647c2fc2d5074a2 — DOI BACK-PATCH: embeds the minted Zenodo archival DOI 10.5281/zenodo.21461881 (concept 21461880) in the Data and Code Availability section, closing the archive/DOI Houston-gate. The record archives the exact bytes of the reviewed v1.7.125 release (md5 174d52d55719c5955f852d2365fdb9c8); no science number changed, −35/16 UNCHANGED. Readiness cap 80 HOLDS (no uplift claimed).",
    changelog: [
      "DOI back-patch (v1.7.126, Jul 20): embedded the minted Zenodo archival DOI 10.5281/zenodo.21461881 (concept 10.5281/zenodo.21461880) in the Data and Code Availability section, closing the standing 'archive/DOI remains a submission-time step' caveat. The record archives the exact bytes of the reviewed v1.7.125 release (11pp md5 174d52d55719c5955f852d2365fdb9c8; receipt project-context/SSOT/zenodo/P2_zenodo_receipt_2026-07-20.json). Only the version macros + availability sentence changed; no science number changed, −35/16 UNCHANGED.",
      "Dressed-metric transmission closure (v1.7.125, Jul 18): in the dressed-metric scheme the bounded bounce is TRANSPARENT to the conserved mode (T_c(k)=1); |δf_NL| ≤ 6.8e-8 at k·η_B=1e-2, more than 4 orders of magnitude below the prior order-of-magnitude reference. Effective-fluid scheme-specificity DEMONSTRATED (K-integral d_cut^-1/2 divergence, fitted -0.4998), so the transmission result is scheme-specific, not scheme-independent. Scheme label applied everywhere; AAN U(η)/deformed-algebra/third-order branch remain honestly disclosed open. Artifacts: research/cubic_bounce_transmission/g1_dressedmetric_ic_close.{py,json}. Headline −35/16 unchanged, nothing fabricated.",
      "G3 model-specific torsion bound (v1.7.123, Eq. 5): new Eq. 5 + bounded-disclosure paragraph converts assumption (f) (fermion-sourced torsion negligible) from asserted to bounded — |δf_NL^tor| ≲ (35/16)(3/16)[γ²/(1+γ²)] κ n_ψ,c²/ρ_c, sympy Einstein-Cartan four-fermion estimate anchored verbatim to the companion P1A's convention-audited axial contact term (benchmark reproduced to 0.1%). n_ψ,c carried as an explicit symbolic model parameter, never fixed. No headline number changed, −35/16 unchanged, nothing fabricated. Artifacts: research/cubic_bounce_transmission/g3_torsion_fourfermion_bound.{py,json}.",
      "directive-M presentation restructure (v1.7.116, ZERO content change): consolidated the repeated scope/caveat/proxy/illustrative statements the REJECT/minor raws named (DP2-30 presentation-scope) to canonical homes + cross-refs, relegated the cosmic-birefringence auxiliary paragraph to a new Appendix (app:birefringence), tightened the Caveats→Scope-and-limitations register. Freeze held: every number byte-identical, −35/16 quadruple-certification untouched. INT re-test: OpenAI REJECT / Grok MAJOR / Gemini MAJOR / Claude ABSENT; 0 genuinely-new editable findings, 0 regressions — residual verdicts are the documented LLM harsh-referee floor. Nothing fabricated.",
      "c15 GR-leg basis-mismatch fix (v1.7.115, INT-Claude genuinely-new MAJOR): the channel-native Fisher built ∂B/∂A_GR = b·b·b·S_GR without the M123 transfer product the f_NL primordial leg carries, leaving the GR template in potential space vs the f_NL density basis — collapsing F[2,2]~1e-18 and faking ρ(f_NL,A_GR)≈−0.001 orthogonality. Fixed (M123 promotion) + re-ran: corrected ρ=−0.42 (2×2)/−0.49 (3×3), σ_marg=0.94→2.32σ. Channel-native floor still > proxy 1.30σ floor, so the retained proxy conclusion holds. −35/16 unchanged, nothing fabricated.",
      "Per-vertex term-by-term derivation table (v1.7.105, R9 Grok+ChatGPT MAJOR): added Appendix A Table VII walking each of Cai's four cubic vertices through the squeezed AND equilateral limits (field-redef -25/16, L_zzdd -5/32, mixed 0, highest-order -15/32 squeezed), both columns summing exact-fraction to -35/16 and -255/128; transcribed verbatim from the committed sympy cert script, no new math. Plus a consolidated gauge-vs-physical-frame f_NL table (Gemini minor). -35/16 unchanged.",
      "Appendix A vertex-algebra display (v1.7.104, deep-Grok MAJOR): added the collapsed exact vertex-sum degree-9 polynomial + the epsilon-order-grouped squeezed contributions (fNL|eps^1=-5/2, |eps^2=+5/16, |eps^3=0 -> -35/16), both transcribed verbatim from the committed sympy certification script; no new math, -35/16 unchanged.",
    ],
    artifacts: [
      { label: "Read PDF", href: "/papers/02_full_draft_v1.7.126.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/02_full_draft_v1.7.126.pdf", kind: "secondary", download: true },
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
    slug: "paper-3",
    number: "3",
    title: "Public-ID Recovery for a Historical DESI DR1 Anomaly List: 170 High-Coordinate-Consistency Core and 11 Lower-Confidence Positional Associations",
    version: "v3.2.0-r11",
    lastUpdated: "2026-07-20",
    tldr: "Recovers 181 public DESI DR1 TARGETIDs from a frozen historical anomaly list, split transparently into 170 high-coordinate-consistency core associations and 11 lower-confidence positional associations. r10 adds an integrity reframe: the sub-0.1-arcsec core excess is by-construction expected seed self-recovery (single-member clusters whose centroid is the seed member's own coordinates) — NOT independent association evidence. This is an archive-recovery product, not a purity, novelty, or detection claim.",
    path: publicationPath({}),
    pages: "17",
    refs: "12",
    readiness: 56,
    statusVariant: "amber",
    target: "ApJS",
    description: "A focused, reproducible public-ID recovery of a frozen historical DESI anomaly list. The declared 1-arcsec positional join yields 181 warning-free global-primary DESI DR1 associations: 170 at or below 0.1 arcsec and 11 lower-confidence associations between 0.1 and 1 arcsec. As of v3.2.0-r10, every claim site (abstract, methods, figure caption, discussion) explicitly states that the sub-0.1-arcsec core excess is expected seed self-recovery — the cluster centroid equals the seed DESI member's own coordinates by construction, verified end-to-end rather than an independent association test. The release carries exact source-row provenance, explicit quality tiers, warned-row auxiliary data, shift controls (scoped to the 0.1-1 arcsec tail), checksums, and a clean-checkout validator while declining physical classification, purity, novelty, and anomaly-rate claims unsupported by the surviving historical lineage.",
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
      "v3.2.0-r10 integrity reframe: every claim site (abstract, Sec 3.5, Fig 1 caption, Sec 7, Sec 8) now states the core excess is expected seed self-recovery / end-to-end recovery verification, NOT independent association evidence; shift control scoped to the 0.1-1 arcsec tail; annulus deficit explained as nearest-neighbor shielding",
    ],
    surveys: ["DESI DR1"],
    predictions: ["Public-ID recovery", "Coordinate-association quality tiers", "Archive reproducibility"],
    figures: ["Selection waterfall", "Separation distribution", "Shift-control radius curves", "Catalog sky distribution"],
    remainingWork: [
      "Human ApJS/editorial review and submission decision; automated ACCEPT is not journal acceptance",
      "AAS journal digital-asset DOI: the Zenodo archival DOI is now published and embedded (v3.2.0-r11, 10.5281/zenodo.21461888); the distinct AAS journal digital-asset DOI remains an honestly open, journal-assigned gate",
      "Run the exact v3.2.0-r10 non-Anthropic + Claude-subagent confirmation review",
      "Rebuild the wave-2 submission tarball at v3.2.0-r11 (DOI-bearing) before submission; Houston still controls arXiv/ApJS submission",
      "Object-level physical interpretation and any representative-control performance study remain separate new-science work",
    ],
    preprintId: "HUBIFY-2026-003",
    pdfMeta: "PDF · 17 pp · v3.2.0-r11 · updated Jul 20, 2026 · md5 62e755678e28fb742d96f3daf5c81b93 — DOI BACK-PATCH: embeds the minted Zenodo archival DOI 10.5281/zenodo.21461888 (concept 21461887) in the Data Availability section, closing the archival-DOI Houston-gate; the distinct AAS journal digital-asset DOI stays honestly open. The record archives the exact bytes of the reviewed v3.2.0-r10 release (md5 9fb6e882068a4613132792633a9d7a60). Readiness cap 56 HOLDS (no uplift claimed).",
    artifacts: [
      { label: "Read PDF", href: "/papers/paper3_apjs_v3.2.0-r11.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper3_apjs_v3.2.0-r11.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/d155eb27488b271be12942b1a1be8b3c39dd24f4/pipelines/p3_anomaly_engine/paper3_apjs.tex",
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
    title: "An Observed-Label Chirality-Dipole Null in 890,069 Quality-Controlled High-Confidence DESI Spirals and an 8.5-Million-Galaxy Catalog",
    version: "v1.0.269",
    lastUpdated: "2026-07-20",
    tldr: "Classifies 8.47M galaxies. The strict safe-sample observed-label statistic remains null-consistent (z=0.63465, p=0.23768). v1.0.268 adjudicates the CE-ResNet catalog composition: re-provisioned via Zenodo, deterministic seeded assembly reproduces GZ1=6,637 and CE-spirals=17,153 exactly, with a reproducible CE non-spiral count of 819, resolving the historical 826-vs-846 conflict. The composition-faithful CE-included retrain collapses to chance on chirality (val 0.5617) — an honest-negative root-caused to systematically fainter/lower-confidence CE-only spirals — so the historical 93.69%/92.10% CE-included headline is not reproducible under honest same-composition ingestion; the GZ1-core manifest-retained realization (0.9931) stands and released Catalog C labels are unchanged. Exact v1.0.268 confirmation board CONVERGED: Grok ACCEPT (its first) / Gemini MINOR / Claude MAJOR (all re-flags), 0 genuinely-new-real. Transfer function, archive, and human gates remain; readiness holds 80.",
    path: publicationPath({}),
    pages: "32",
    refs: "18",
    readiness: 80,
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
      "Freeze and validate full-catalog imaging-leg, depth, seeing, PSF, and redshift metadata; the exact morphology join is now public but these fields remain unavailable",
      "Complete systematics-metadata sidecar: the DOI back-patch (v1.0.269) closed the archive/DOI gate itself, but the separate complete systematics-metadata sidecar remains honestly open",
      "Re-provision the Jia et al. 2023 CE-ResNet high-confidence spiral catalog (pre_desi.fits; external source, GitHub h3jia/galaxy_spin_classifier / NADC China-VO) to engage the CE-non-spiral 826-vs-846 sub-conflict and complete the full historical-realization training component; released Catalog C labels are unaffected",
      "Extend the computed 3x3 joint covariance to the MASTER-decoupled leg and full joint likelihood; run the G4 monopole-mechanism injection (H200, now unblocked by the completed G1 retrain); derive the morphology transfer function needed to convert A_95^obs into a physical parity-amplitude bound",
      "Author arXiv endorsement and journal-submission decision",
    ],
    preprintId: "HUBIFY-2026-004",
    pdfMeta: "PDF · 32 pp · v1.0.269 · md5 b266198157eef7f2feb590a3692e8004 — DOI BACK-PATCH: embeds the minted Zenodo archival DOI 10.5281/zenodo.21461899 (concept 21461898) in the abstract, Data Availability paragraph, and catalog itemize, closing the DOI Houston-gate; the complete systematics-metadata sidecar stays honestly open. The record archives the exact bytes of the reviewed v1.0.268 release (md5 4e139b56b0718c70b73ae7295e4ee7b1). Readiness holds 80 (no uplift claimed).",
    changelog: [
      "DOI back-patch (v1.0.269, Jul 20): embedded the minted Zenodo archival DOI 10.5281/zenodo.21461899 (concept 10.5281/zenodo.21461898) in the abstract, Data Availability paragraph (replacing the 'DOI ... will be inserted here ... at submission time' placeholder), and catalog itemize, closing the standing 'DOI-backed archive remain open' caveat. The record archives the exact bytes of the reviewed v1.0.268 release (32pp md5 4e139b56b0718c70b73ae7295e4ee7b1; git commit 397671bf; receipt project-context/SSOT/zenodo/P4_zenodo_receipt_2026-07-20.json). The separate complete systematics-metadata sidecar gate stays honestly open. No science number changed; the observed-label null is unchanged.",
      "CE-composition adjudication + honest-negative retrain (v1.0.268): the Jia CE-ResNet catalog is re-provisioned (Zenodo 10.5281/zenodo.7167388, sha 894dbe88; provenance committed). Deterministic seeded assembly reproduces GZ1=6,637 and CE-spirals=17,153 exactly; the reproducible CE non-spiral count is 819 (neither 826 nor 846) — isolating the entire historical conflict to the seeded 50k non-spiral subsample crossmatch. The composition-faithful CE-included retrain collapses to chance on chirality (val 0.5617 = NS-perfect + chirality-chance arithmetic; per-source GZ1 0.517 / CE 0.509; four alternate hypotheses ruled out, incl. 99.72% CE-GZ1 convention agreement on the 38,617-galaxy bright overlap) — root cause: the CE-only pool (72% of spirals) is systematically fainter/smaller with near-coin-flip supervision (median winner-prob 0.569 vs 0.899). The historical 93.69%/92.10% CE-included headline is NOT reproducible under honest same-composition ingestion, corroborating the paper's standing disclosures; the GZ1-core manifest-retained realization (0.9931) stands and released Catalog C labels are unchanged. All five CE caveat sites adjudicated in-paper. Exact v1.0.268 confirmation board CONVERGED with the softest board of the era: Grok ACCEPT (its first) / Gemini MINOR (0 major) / Claude MAJOR (all re-flags); 16 findings, 0 genuinely-new-real, 0 falsified.",
      "Two real-compute pod-campaign closures (v1.0.266): (1) G1 manifest-retained ViT retrain COMPLETE on RunPod A4000 (<$1 total) — 8,637 objects (6,637 GZ1-core + 2,000 synthetic; CE-ResNet component absent pending external re-provisioning from Jia 2023 / NADC China-VO, so the 826-vs-846 sub-conflict stayed open and released Catalog C labels are unchanged), every object ID/split/seed retained in the committed manifest, best_val_acc=0.9931 @ epoch 47, checkpoint backed up to 3 verified locations. (2) G2 training-disjoint validation: accuracy=0.9867 / Cohen's kappa=0.9733 on 3,000 GZ1 confident spirals disjoint from G1 training on both the object-ID and label-source axes (overlap counts 0), presented with an explicit like-for-like distinction vs the historical kappa=0.40 human-vote figure — a different measure, not a replacement. Caveat sites narrowed honestly at abstract/intro/discussion/conclusions/data-availability. No science number changed.",
      "Coverage-calibrated observed-label A_95^obs closure (v1.0.265): the exact v1.0.264 confirmation board (Claude MAJOR / Grok MAJOR / Gemini MINOR) truth-audited to 2 genuinely-new-real findings. Closed M3 with A_95^obs~=0.98% (linear-interp; logistic cross-check 0.955%) from 2,000 random-axis injections/amplitude through the exact committed primary estimator and exact fixed-occupancy null (headline z=+0.63465/p=0.23768 reproduced exactly as a hard gate first); integrated at 7 manuscript sites. Closed Ge1 with an editorial rephrase removing review-process narration from the new Sec 4.5. Explicitly an observed-label bound, not a physical one; no science number changed.",
      "End-to-end transfer-calibration scope statement (v1.0.229): the injection-recovery section now delineates which links of the classify→dipole chain the sweep traverses (map-making + dipole estimator + null calibration) versus which it does not (ViT classifier, NS triage, confidence cut, spatially-varying confusion), shows from the committed GZ1 confusion numbers that the asymmetric-confusion transfer slope g_eff = s_CW + s_CCW − 1 = 0.398 equals the symmetric g = 2a − 1 = 0.398 for the near-balanced parent (so CW/CCW asymmetry does not degrade the physical-amplitude conversion), and honest-flags the full image-level end-to-end injection through the classifier as requiring new simulation — operative claims held to the observed hard-label field. No number changed, nothing fabricated.",
      "R9 ACCEPT-track minor closure (v1.0.225): Grok = minor-revisions, Gemini = 'Accept with minor revisions'; both referees' concrete minors closed with real edits (no number changed). Abstract z≈−18 now explicitly labeled a model-dependent template-disfavor statistic (not a frequentist exclusion) with the injection-recovery A95∈(1.0,1.5]% cross-referenced as the primary real-space falsification; added a main-text downstream-user warning that raw p_eq scores are not frequentist likelihoods (cite Appendix-B ECE ≥0.25–0.36); abstract real-space p now names its isotropic-pixel-permutation null. ChatGPT major = presentation/consolidation of already-disclosed content.",
      "Deep-tier Gemini MAJOR closure (v1.0.224): added self-contained training-data provenance table + a probabilistic-calibration paragraph quantifying a real top-label ECE lower bound from the committed GZ1 confusion matrix (mean-conf 0.951 vs 3-class acc 0.5871 -> ECE>=0.36; chirality 0.6991 -> >=0.25), proven invariant to any monotone recalibration; surfaced existing committed data, no number changed.",
    ],
    artifacts: [
      { label: "Read PDF", href: "/papers/chirality_catalog_paper_v1.0.269.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/chirality_catalog_paper_v1.0.269.pdf", kind: "secondary", download: true },
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
    title: "Environmental Dependence of Spiral Chirality: A DESIVAST Catalog-Native Void Non-Detection with Secondary Cosmic-Web Cross-Checks",
    version: "v0.1.141-2026-07-16",
    lastUpdated: "2026-07-16",
    tldr: "On the released DESIVAST GALZONE parent, the focal exploratory analysis detects no void/non-void difference in classifier-labelled CW fraction; this bounded non-detection does not establish physical environment independence.",
    path: publicationPath({}),
    pages: "42",
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
      "Run exact-PDF confirmation review on v0.1.141 and keep the sparse interaction and secondary T-Web limitations explicit",
      "Finalize Paper IV labels, weights, and provenance, then reverify P5 against that independently reviewable release",
      "Publish an immutable P5 tag/archive/DOI and verify every A1–A48 link; local retention is not a public release",
      "Resolve the human/editorial gate through actual AJ review; automated evidence is not journal acceptance",
    ],
    preprintId: "HUBIFY-2026-005",
    pdfMeta: "PDF · 42 pp · v0.1.141-2026-07-16 · sha256 4cca09d0 · md5 6a4e79b4 — semi-analytic forward-leakage injection closure (78–88% of large raw deviations reproduced from committed leakage components, every residual non-significant); release, exact re-review, editorial, and human AJ gates remain. Readiness holds 74.",
    artifacts: [
      { label: "Read PDF", href: "/papers/p5_desi_chirality_v0.1.141-2026-07-16.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/p5_desi_chirality_v0.1.141-2026-07-16.pdf", kind: "secondary", download: true },
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
