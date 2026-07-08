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
      label: "Internal multi-model review",
      state: "done",
      note: "Native-PDF autoloop: Claude · GPT · Gemini · Grok · Perplexity",
    },
    {
      label: "Cross-vendor rounds clean",
      state: "done",
      note: "3+ consecutive clean 5-vendor rounds (§4.4.1)",
    },
    overrides.external ?? {
      label: "External journal-style review",
      state: "active",
      note: "NOT passed — verified EXT board (Jul 6) shows a real ChatGPT REJECT + Grok/Gemini MINOR-to-MAJOR; closing findings with real science",
    },
    overrides.signoff ?? {
      label: "Reviewer ACCEPT",
      state: "pending",
      note: "The bar — no paper is reviewer-accepted yet",
    },
    overrides.arxiv ?? {
      label: "arXiv submission",
      state: "pending",
      note: "Gated behind a reviewer ACCEPT · endorsement Houston-only",
    },
  ];
}

export const papers: Paper[] = [
  {
    slug: "paper-1a",
    number: "1A",
    title: "Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter",
    version: "v1A.0.115",
    lastUpdated: "2026-07-08",
    tldr: "Closes all four minimal Einstein–Cartan–Holst routes from a quantum bounce to dark energy and proves the Holst sector is invisible to scalar/tensor perturbations — leaving two clean observational kill-tests (LiteBIRD birefringence, SPHEREx f_NL).",
    path: publicationPath({}),
    pages: "37",
    refs: "72",
    readiness: 62,
    statusVariant: "amber",
    target: "Physical Review D",
    description: "The theory foundation of the program (PRD target). Proves a perturbation-transparency theorem — for canonical scalar matter, torsion vanishes at all perturbation orders and the Holst sector decouples from every scalar/tensor observable — and closes all four minimal Einstein–Cartan–Holst routes from the quantum bounce to late-time dark energy. The structural-tension argument shows the dark-energy mechanism (N_tot ≈ 92 post-bounce e-folds) is incompatible with the f_NL = -35/16 matter-bounce signature; technical verification lives in Paper 1B.",
    keyResults: [
      "14 ECH structural barriers close all minimal routes from bounce to dark energy",
      "Perturbation-transparency theorem: torsion vanishes at all perturbation orders for canonical scalars",
      "Structural-tension argument (§III): N_tot ≈ 92 post-bounce e-folds is incompatible with f_NL = -35/16",
      "Bounce-model discrimination table: matter-bounce vs Cuscuton vs ekpyrotic vs quintom vs slow-roll",
      "f_NL = -35/16 parameter-free, mechanism-independent across all matter-bounce variants",
      "Matter-bounce SPHEREx detection forecast: ~1.3-2.75σ realistic (cross-references Paper 2)",
      "MCS line-of-sight derivation appendix (App C): helicity dispersion → β = (α/2M)Δθ — closes the last analytic gate",
      "R26conf: App C derivation verified step-by-step clean; Cartan factor-2 normalization inconsistency disclosed (single-convention re-derivation queued, analytic); dimensionally inconsistent thermal clause removed (v1A.0.56)",
    ],
    surveys: ["Planck CMB", "ACT DR6", "DESI DR1", "DESI DR2 (referenced)", "NANOGrav 15yr"],
    predictions: ["f_NL = -35/16", "Birefringence β = 0.27°", "NANOGrav γ = 3.0", "Quintom w-crossing falsification path"],
    figures: ["LQG-Holst derivation", "14 barriers diagram", "Theory map (mechanisms × observables)", "Model discrimination table"],
    remainingWork: [
      "Close remaining reviewer findings with real science (NOT reviewer-accepted — verified EXT board shows a real ChatGPT REJECT + Grok/Gemini MINOR-to-MAJOR)",
      "arXiv endorsement + submission — gated behind a reviewer ACCEPT (packets are ready; reviews are not passed)",
    ],
    preprintId: "HUBIFY-2026-001A",
    pdfMeta: "PDF · 39 pp · v1A.0.115 · updated Jul 8, 2026 · md5 68b133c7",
    artifacts: [
      { label: "Read PDF", href: "/papers/paper1a_ech_nogo_v1A.0.115.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper1a_ech_nogo_v1A.0.115.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/arxiv/paper1a_ech_nogo.tex",
        kind: "secondary",
        external: true,
      },
      {
        label: "Companion (Paper 1B)",
        href: "/papers/paper-1b",
        kind: "secondary",
      },
    ],
  },
  {
    slug: "paper-1b",
    number: "1B",
    title: "Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔN_eff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model",
    version: "v1B.0.104",
    lastUpdated: "2026-07-08",
    tldr: "Technical companion to Paper 1A: a 309K-sample ΛCDM+ΔN_eff MCMC null test (ΔN_eff consistent with zero), a NaMaster pipeline validation on synthetic ΛCDM skies, a DESI DR2 w0wa chain (w_pivot +2.5σ from −1), and a spectator-ALP consistency check against the Planck+ACT β = 0.342° measurement.",
    path: publicationPath({}),
    pages: "22",
    refs: "32",
    readiness: 62,
    statusVariant: "amber",
    target: "Physical Review D (companion)",
    description: "Technical verification companion to Paper 1A, documenting three analyses: a 309,189-sample Cobaya ΛCDM+ΔN_eff MCMC that recovers ΛCDM (H0 = 67.68 ± 1.06 km/s/Mpc, ΔN_eff consistent with zero); a NaMaster pipeline validation on synthetic ΛCDM polarization skies with an ACT-like mask (inject β=0.27°, recover 0.238°, bias −0.032° — a pipeline-validation figure, not a sky measurement); and a spectator-ALP consistency check against the published Planck+ACT β = 0.342° ± 0.094° (3.6σ).",
    keyResults: [
      "309,189 frozen MCMC samples across 2 converged dataset combinations (176,240 full-tension + 132,949 Planck+BAO+SN); third Planck-only ongoing",
      "ΔN_eff consistent with zero (-0.020 ± 0.169 full-tension; +0.058 ± 0.179 Planck+BAO+SN); H0 = 67.68 ± 1.06",
      "NaMaster 500MC on synthetic ΛCDM skies (f_sky=0.32, ACT-level noise): β=0.27° recovered as 0.238°, bias −0.032°, sign-symmetric, σ_β(0.32)=0.046° measured directly — pipeline validation, not a sky detection",
      "Spectator-ALP f_a ~ M_Pl, m ~ H_0 consistent with Eskilt+ joint Planck+ACT 0.342°±0.094° (3.6σ)",
      "Pipeline-recovery bias 0.032° well below the published observational σ_β = 0.094°",
      "DESI DR2 w0wa chain (Planck NPIPE + DESI DR2 BAO + DES-Y5 + Pantheon+): w_pivot = −0.952 ± 0.019, i.e. +2.5σ from −1 (twice-verified direct chain readout)",
      "S8 marginal corrected 0.831 ± 0.018 → 0.827 ± 0.010 (chain-recomputed, in-text correction note); 2.6σ vs DES-Y3 with posterior overlap 0.05 (overlay artifact)",
      "cosθ-prior robustness on the spectator-ALP fit (c14): C_aγ median 17.1, 16–84% [6.8, 43.4] — essentially unchanged vs flat-θ",
      "R26conf ROUND CLEAN: lone substantive accusation (CPL crossing) falsified by shown arithmetic (z* = +0.39 inside range); every committed number chain-reproduced; M-tier traceability closures applied (v1B.0.54)",
    ],
    surveys: ["Planck NPIPE", "Synthetic ΛCDM skies (NaMaster validation)", "ACT DR6", "DESI DR2 BAO", "Pantheon+ SN", "DES-SN5YR", "NANOGrav 15yr"],
    predictions: ["ΔN_eff null", "Birefringence β = 0.27° (recovery test)", "w0-wa quintom-B test (DESI DR2)"],
    figures: ["Δχ² and ΔAIC summary table", "Corner plots", "NaMaster recovery posteriors", "Cross-paper status table"],
    remainingWork: [
      "Close remaining reviewer findings with real science (NOT reviewer-accepted — verified EXT board shows a real ChatGPT REJECT + Grok/Gemini MINOR-to-MAJOR)",
      "Release-pairing swap MCMC (queue #29) — running on pod; PR4-consistent low-ℓ/lensing stack vs current pairing, ΔNeff/H0/S8 shift check (non-gating)",
      "arXiv endorsement + submission — gated behind a reviewer ACCEPT (packets are ready; reviews are not passed)",
    ],
    preprintId: "HUBIFY-2026-001B",
    pdfMeta: "PDF · 22 pp · v1B.0.104 · updated Jul 8, 2026 · md5 76dce947",
    artifacts: [
      { label: "Read PDF", href: "/papers/paper1b_mcmc_companion_v1B.0.104.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper1b_mcmc_companion_v1B.0.104.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/arxiv/paper1b_mcmc_companion.tex",
        kind: "secondary",
        external: true,
      },
      { label: "Theory paper (1A)", href: "/papers/paper-1a", kind: "secondary" },
      { label: "Corner plot", href: "/images/paper1_corner_full_tension.png", kind: "secondary", external: true },
      {
        label: "ALP chains (HuggingFace)",
        href: "https://huggingface.co/datasets/bamfai/p1b-alp-chains",
        kind: "secondary",
        external: true,
      },
      {
        label: "MCMC diagnostics (HuggingFace)",
        href: "https://huggingface.co/datasets/bamfai/p1b-mcmc-diagnostics",
        kind: "secondary",
        external: true,
      },
      {
        label: "NaMaster artifacts (HuggingFace)",
        href: "https://huggingface.co/datasets/bamfai/p1b-namaster-artifacts",
        kind: "secondary",
        external: true,
      },
    ],
  },
  {
    slug: "paper-2",
    number: "2",
    title: "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook",
    version: "v1.7.104",
    lastUpdated: "2026-07-08",
    tldr: "Resolves the long-standing Cai–Li factor-of-two: the matter-bounce squeezed local non-Gaussianity is f_NL = −35/16 = −2.1875 (not −35/8), and recasts published SPHEREx forecasting power onto it — ~2.6–2.75σ optimistic, ~1.3–2.75σ realistic — as a bounce-vs-inflation discriminator. An independent in-house tree-level multi-tracer bispectrum Fisher validates the recast (reproduces Heinrich σ≈0.7 to 2–11%, r_eff≈0.99 for the bounce template), now extended to the full redshift-space (RSD) tree bispectrum: σ tightens to 0.42–0.45 (+34.7% vs real-space), r_eff≈0.99 persists, and the unmarginalized −35/16 significance rises to 4.9–5.2σ — retiring the 'real-space monopole only' limitation.",
    path: publicationPath({}),
    pages: "36",
    refs: "39",
    readiness: 74,
    statusVariant: "amber",
    target: "Physical Review Letters",
    description: "The decisive SPHEREx discrimination paper. Proves f_NL = -35/16 is parameter-free and mechanism-independent across all matter-bounce variants, then delivers Fisher forecasts showing ~1.3-2.75σ realistic SPHEREx detection significance by 2027. Multi-tracer sigma(f_NL) marginalized floor of 0.067-0.116 across 6 configurations, with magnification-bias identified as the dominant systematic axis. All 65 R42 cross-model peer-review findings closed.",
    keyResults: [
      "f_NL = -35/16 = -2.1875 (parameter-free, mechanism-independent)",
      "Verified across 3 bounce models (matter bounce, LQC, Cuscuton)",
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
      "Close remaining reviewer findings with real science (NOT reviewer-accepted — verified EXT board shows a real ChatGPT REJECT + Grok/Gemini MINOR-to-MAJOR)",
      "arXiv endorsement + submission — gated behind a reviewer ACCEPT (packets are ready; reviews are not passed)",
    ],
    preprintId: "HUBIFY-2026-002",
    pdfMeta: "PDF · 36 pp · v1.7.104 · updated Jul 8, 2026 · md5 c5d4523a",
    changelog: [
      "Appendix A vertex-algebra display (v1.7.104, deep-Grok MAJOR): added the collapsed exact vertex-sum degree-9 polynomial + the epsilon-order-grouped squeezed contributions (fNL|eps^1=-5/2, |eps^2=+5/16, |eps^3=0 -> -35/16), both transcribed verbatim from the committed sympy certification script; no new math, -35/16 unchanged.",
    ],
    artifacts: [
      { label: "Read PDF", href: "/papers/02_full_draft_v1.7.104.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/02_full_draft_v1.7.104.pdf", kind: "secondary", download: true },
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
    title: "Spectrally Unusual Sources at Scale: A Multi-Survey Anomaly-Candidate Catalog of 378,280 Path-C Reconstruction-Outlier Sources and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches",
    version: "v3.1.144",
    lastUpdated: "2026-07-08",
    tldr: "A 378,280-object anomaly catalog mined from 37.3M sources across 7 surveys with one autoencoder architecture — 17.8% of top-ranked objects are new to existing catalogs, plus a NANOGrav free-spectrum fit consistent with matter-bounce γ = 3.0.",
    path: publicationPath({}),
    pages: "33",
    refs: "71",
    readiness: 62,
    statusVariant: "amber",
    target: "ApJS",
    description: "The multi-survey anomaly catalog: 378,280 unique anomalies from 37.3 million sources across 7 surveys via one BigAE autoencoder architecture, with a 17.8% novelty rate at the top-1,000 stratum against 20 all-sky catalogs. A NANOGrav 15-yr free-spectrum re-fit gives γ = 2.567 ± 0.382 — matter-bounce γ=3.0 is consistent (+1.13σ) while SMBHB γ=4.33 is excluded (+4.61σ). Multi-tracer forecast: σ(f_NL) = 8.27 ± 2.37.",
    keyResults: [
      "378,280 unique anomalies across 7 non-quarantined surveys from 37.3M sources (Wave 11 retitle)",
      "Catalog-grade tier: 269,317 unique entries (point-source subset 269,117; DESI + SDSS native + eROSITA + Planck native + Gaia + NEOWISE); point-source tier 378,080; Planck CMB-patch tier 200",
      "LAMOST 113,342 reclassified as exploratory tier (FAIL: ~56% B-dominant cross-transfer empirical; native retrain 21.4x reduction to 2,054 at S>5)",
      "100k OOD validation (Wave 5 B10): median MSE 0.178, p99 = 44.85, 0.87% DESI anomaly rate preserved",
      "5-fold OOS Jaccard J̄ = 0.862 PASS on real DESI 47k-spectra retrain (Path-C exit criterion)",
      "NANOGrav 15-yr KDE free-spectrum γ = 2.567 ± 0.382 — bounce γ=3.0 consistent (+1.13σ), SMBHB γ=4.33 excluded (+4.61σ)",
      "Empirical α_jk = 0.19 ± 0.65 (consistent with zero at 0.29σ); σ(f_NL) = 8.27 ± 2.37 multi-tracer forecast; SPHEREx 4.38σ for f_NL = -35/16",
      "58.8% novel objects (not in SIMBAD); injection/recovery 0% false positive at 10–1,377× enrichment",
      "eROSITA enrichment statistic reframed as descriptive (selection-coupled), not an inferential significance (v3.1.80 wave)",
      "Abstract novelty rate arithmetic-anchored 7.9% → 9.4%; gold/silver novelty tiers defined (116 + 1,006 = 1,122); FoF dedup audit artifact committed (v3.1.81 R23conf wave)",
      "eROSITA 0.259 threshold-axis irreproducibility disclosed in-text; abstract framing upgraded with Wilson CI, prior qualifiers, and de-biased ordering (v3.1.82 R24conf wave)",
      "eROSITA axis definitively resolved: monotone-rescaling class ruled out (Spearman ρ = −0.10); membership-is-canonical framing adopted (v3.1.83 wave)",
      "Catalog-grade count corrected 264,938 → 269,317 (prior count double-removed 4,379 LAMOST-overlap objects; independent 6-way dedup verified); HEALPix 38,330px unrecoverable confirmed → reproducible rerun 24,049px χ²_ν=15.7; SMICA preprocessing documented, 200/200 top-200 reproduction (v3.1.84 pod wave)",
      "R26conf: zero arithmetic errors across the round; 12 textual closures — cluster accounting made exact from the dedup artifact, NANOGrav Eq. E1 claim falsified by rederivation (v3.1.87)",
      "TARGETTYPE-restricted recount completed: 2,468 DESI anomaly clusters (1.3%) sit on main-survey science-class spectra — ≈0.9× the Liang 2023 benchmark restricted, not 73×; ~98.7% of DESI anomalies fall on sky/secondary/filler spectra (v3.1.93 EXT3-B2 closure)",
      "R32conf closure wave: recount-at-a-glance table added (3-vendor convergent ask), irreproducible S_BigAE column stripped from the eROSITA table, title moved to singular novelty fraction, SMBHB abstract framing tightened to 'not a cosmological detection' (v3.1.94)",
      "R33conf confirmation CLEAN-after-audit: zero closure-introduced regressions across all 12 closures, 2nd consecutive zero-arithmetic round; abstract envelope clause + auditable numeric Fisher mapping landed; EXT4-eligible (v3.1.95)",
      "FM1 eROSITA scaler-refit computed (was queued): scaler effect ≤ model-retrain reproducibility floor — top-298 overlap 257/298, Spearman 0.94; rates/rankings robust, ~15% quantified extreme-tail membership churn (v3.1.96)",
    ],
    surveys: ["DESI DR1", "SDSS DR18", "LAMOST DR10 (exploratory)", "eROSITA DR1", "Planck CMB", "ACT DR6 (quarantined)", "NEOWISE", "Gaia DR3"],
    predictions: ["f_NL improvement", "Multi-survey validation", "NANOGrav γ (real free-spectrum)"],
    figures: ["Multi-survey sky map", "Score distributions", "Taxonomy UMAP", "f_NL improvement plot", "γ posterior (real KDE vs synth)"],
    remainingWork: [
      "Close remaining reviewer findings with real science (NOT reviewer-accepted — verified EXT board shows a real ChatGPT REJECT + Grok/Gemini MINOR-to-MAJOR)",
      "HuggingFace visibility flip on bamfai/bigbounce-anomaly-catalog (Houston manual on HF dashboard)",
      "arXiv endorsement + submission — gated behind a reviewer ACCEPT (packets are ready; reviews are not passed)",
    ],
    preprintId: "HUBIFY-2026-003",
    pdfMeta: "PDF · 34 pp · v3.1.144 · updated Jul 8, 2026 · md5 0dc4c23c",
    artifacts: [
      { label: "Read PDF", href: "/papers/paper3_draft_v3.1.144.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper3_draft_v3.1.144.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p3_anomaly_engine/paper3_draft.tex",
        kind: "secondary",
        external: true,
      },
      {
        label: "Science highlights",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/project-context/paper3_science_highlights.md",
        kind: "secondary",
        external: true,
      },
      { label: "Anomaly catalog (HuggingFace)", href: "https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog", kind: "secondary", external: true },
    ],
  },
  {
    slug: "paper-4",
    number: "4",
    title: "A Null Chirality Dipole in 8.5 Million DESI Galaxies from Equivariant Deep Learning",
    version: "v1.0.224",
    lastUpdated: "2026-07-08",
    tldr: "Classifies 8.47M galaxies for spiral handedness with a rotation-equivariant ViT ensemble and finds a null real-space chirality dipole (+0.41σ, rank-p=0.31; A_dip < 6.8×10⁻³ at 95% UL) — the earlier −0.122σ subsample-mask null was withdrawn in v1.0.166 after a provenance audit.",
    path: [
      { label: "Draft complete", state: "done" },
      {
        label: "Internal multi-model review",
        state: "done",
        note: "Native-PDF autoloop: Claude · GPT · Gemini · Grok · Perplexity",
      },
      {
        label: "Cross-vendor rounds clean",
        state: "done",
        note: "R25conf CLEAN — round 2-of-2 post-retraction requirement met",
      },
      {
        label: "External journal-style review",
        state: "active",
        note: "NOT passed — verified EXT board (Jul 6): ChatGPT REJECT · Grok MINOR · Gemini MAJOR; closing findings with real science",
      },
      {
        label: "Reviewer ACCEPT",
        state: "pending",
        note: "The bar — not reviewer-accepted yet",
      },
      {
        label: "arXiv submission",
        state: "pending",
        note: "Gated behind a reviewer ACCEPT · endorsement Houston-only",
      },
    ],
    pages: "32",
    refs: "46",
    readiness: 80,
    statusVariant: "amber",
    target: "MNRAS",
    description: "The galaxy chirality catalog: 8.47M galaxies classified CW/CCW by a ViT-Small ensemble with rotational-equivariance correction (2.98× asymmetry suppression). The parity test is the dipole — the real-space fit at +0.41σ (empirical-rank p=0.31, regenerated from the fixed null generator in v1.0.168) plus a template-fit exclusion of a clean 1.7% dipole (z≈−18), with injection-recovery sensitivity A50 ≈ 0.75% and A95 bracketed in (1.0%, 1.5%]. The earlier −0.122σ subsample-mask MASTER null was withdrawn after a provenance audit traced it to a synthetic-footprint catalog; the MASTER channel is presented as a systematics diagnostic (+7.28σ on the real apodized footprint, unchanged under depth-stratified nulls — survey systematics, not cosmology). The 0.4974 CW monopole (−9.5σ) traces to GZ1 training-label bias: spatially uniform, not parity violation.",
    keyResults: [
      "8.47M galaxies classified (1,687,069 CW / 1,634,726 CCW / 5,152,736 NOT_SPIRAL)",
      "Real-space ℓ=1 dipole at +0.41σ (empirical-rank p=0.31, 10⁴ isotropic-null realizations from the fixed generator) with a formal A_dip < 6.8×10⁻³ 95% UL + template-fit exclusion of a clean 1.7% dipole at z≈−18; earlier −0.12σ subsample-mask null withdrawn (synthetic-footprint provenance)",
      "Confidence-cut profile: full-sample z=+4.27 collapses to +0.41 at p_eq ≥ 0.6 — confirms the low-confidence-tail attribution of the 4.2σ diagnostic; per-galaxy label-shuffle null 0.58σ; HC selection explicit (N=949,584)",
      "ℓ=1 MASTER decoupling numerically stable: full coupling-matrix condition number 3.17 (3.11/3.25 at 1°/3° apodization)",
      "Bin-by-bin CW flatness audited across 4 morphology axes; residuals are classification correlations, orthogonal to dipole tests",
      "Injection-recovery sensitivity: A50 ≈ 0.75% (50%-recovery at 3σ); A95 bracketed in (1.0%, 1.5%] — honest falsification window",
      "Edge-on TTA equivariance check: CW fraction 0.4975 ± 0.0006 on 785,859 edge-on galaxies, indistinguishable from catalog-wide",
      "Platt calibration: raw +0.79%/28.8σ → calibrated +0.4%/14.6σ → equivariant -0.26%/9.5σ",
      "Equivariance suppression factor 2.98× (raw +1.58% → equivariant −0.53% in asymmetry-A units; +0.79% → −0.26% in f_CW units)",
      "Harmonic-channel completeness anchor: an injected Shamir-class A_p=1.7% dipole would recover at z≈68–218 in the apodized MASTER channel (A_p=3%: z≈209–685) vs the observed +7.3 — incompatible in amplitude by over an order of magnitude",
      "Hemisphere look-elsewhere null: p_LEE < 10⁻⁴ (0/10,000 MC nulls reach data)",
      "100,000-bootstrap CW/CCW asymmetry: A_obs=1.5757%, 95%CI=[1.471%, 1.685%], σ_stat = 28.80σ",
      "8/8 bias hardening tests pass (flip-equivariance, rotation stability, etc.)",
      "Shamir 2020 3% parity-violation claim not reproduced: clean 1.7% dipole excluded at >99% confidence under the adopted error model",
      "R25conf round 2-of-2 CLEAN (93 findings audited); one substantive catch — App A field-convention description corrected from artifacts, no number changed (v1.0.170)",
      "Pod recompute wave: unthresholded-sample injection floors A50=0.36% / A95=0.63% (the 0.57% excess sits between — honest disclosure); area-uniform axis curve P3σ=0.59 @ 0.75%; threshold sweep reproduces canonical exactly; T7 quantified by confidence (0.267 vs 0.383); training-acc semantics corrected — 93.7% = 3-class val, 94.9% = CW per-class (v1.0.171)",
    ],
    surveys: ["DECaLS / DESI Legacy DR9 (8.47M galaxies)"],
    predictions: ["Parity test (indirect bounce test)"],
    figures: ["Chirality sky map", "Hemisphere null", "Bias audit results", "Class pie (canonical text counts)"],
    remainingWork: [
      "Close remaining reviewer findings with real science (NOT reviewer-accepted — verified EXT board shows a real ChatGPT REJECT + Grok/Gemini MINOR-to-MAJOR)",
      "Pod recompute: multi-null 10⁴ rerun (generator not committed; non-gating)",
      "GitHub release PDF asset upload (tag + commit already pushed)",
      "arXiv endorsement + submission — gated behind a reviewer ACCEPT (packets are ready; reviews are not passed)",
    ],
    preprintId: "HUBIFY-2026-004",
    pdfMeta: "PDF · 32 pp · v1.0.224 · updated Jul 8, 2026 · md5 521b5bbb · 34 MB",
    changelog: [
      "Deep-tier Gemini MAJOR closure (v1.0.224): added self-contained training-data provenance table + a probabilistic-calibration paragraph quantifying a real top-label ECE lower bound from the committed GZ1 confusion matrix (mean-conf 0.951 vs 3-class acc 0.5871 -> ECE>=0.36; chirality 0.6991 -> >=0.25), proven invariant to any monotone recalibration; surfaced existing committed data, no number changed.",
    ],
    artifacts: [
      { label: "Read PDF", href: "/papers/chirality_catalog_paper_v1.0.224.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/chirality_catalog_paper_v1.0.224.pdf", kind: "secondary", download: true },
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
    title: "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Void Null Test on 56,981 DESI DR1 Spirals, with a Secondary Tidal-Tensor Cross-Check",
    version: "v0.1.107",
    lastUpdated: "2026-07-07",
    tldr: "Cross-matches P4's spiral handedness with DESI large-scale structure (791,635 matched spirals + 56,981 void spirals) and finds galaxy chirality is statistically independent of cosmic-web environment — constraining environment-coupled parity models.",
    path: publicationPath({}),
    pages: "37",
    refs: "—",
    readiness: 74,
    statusVariant: "amber",
    target: "MNRAS (or A&A)",
    description: "Separate from P4. P5 inherits P4's chirality labels and asks an environment-dependent question P4 is not designed to answer: is galaxy chirality statistically independent of DESI-derived large-scale-structure environment after controlling for sky position, redshift, imaging systematics, morphology confidence, and selection effects?",
    keyResults: [
      "Matched chirality × DESI DR1 catalog: 2,232,212 deduped rows, 791,635 spirals (DECaLS 1,538,880 / BASS+MzLS 688,608 / DES 4,724)",
      "Headline: chirality is statistically independent of LSS environment within DESI DR1 — no class clears Bonferroni-corrected significance under any classifier",
      "DESIVAST three-algorithm void test on 56,981 void spirals: controlled-sample non-detection across all void-finding algorithms",
      "T-Web (Hahn 2007) tidal-tensor cross-check on 14.6M DESI DR1 spectro galaxies: per-environment CW fractions consistent with parity",
      "z-shell selection-corrected rebuild (21 shells): environmental-independence headline robust to survey-shell systematics",
      "Redshift analysis: permutation null p=0.372 — no z-dependence; HEALPix spatial scan p=0.61/0.14/0.41 — no spatial structure",
      "ASTRA-DESI EDR per-object cross-validation (25,186 spirals with all three labels): independence holds under independent classifiers",
      "Duplicate-TARGETID join root-caused and rebuilt (100% GZ–DESI join after fix); omnibus χ² environment nulls p=0.31/0.99; covariate-robust regression (size/mag/morphology/inclination) Wald p=0.46/0.99",
      "Count ledger unified (812,793 rows / 783,820 unique / 7,815 dropouts); unique-TARGETID omnibus χ²=3.00 (p=0.39); Bonferroni threshold corrected 3.02→2.77 with the Z3=−3.14 crossing disclosed + monopole-subtracted residuals (v0.1.53 R23conf wave)",
      "ZONEVOID zone-offset join bug found + fixed: GALZONE void counts 86,276/64,514 → 104,912/74,111 (σ −0.52/−1.50), conclusion unchanged; earlier-draft disclosure in §VIII.D (v0.1.54 R24conf wave)",
      "Unique-TARGETID parent rebuild closed the gating item: headline statistics rebuilt on the deduped parent, Δ ≤ 0.70pp, conclusions unchanged (v0.1.55 wave)",
      "Stratified Phase-2 LEE: global max-stat p=0.36/0.27; maximal-sphere vs any-hole void membership both null; z-tail clamp a no-op (zero galaxies above z=1.6979); #16 randoms-data-missing documented (v0.1.56 pod wave)",
      "R26conf: zero arithmetic errors across the round; 9 closures including code-verified tidal-tensor sign documentation (v0.1.60)",
    ],
    surveys: ["P4 chirality catalog (HF bamfai/galaxy-chirality-catalog, 8.47M)", "DESI DR1 zall-pix-iron.fits (~22.5M rows; matched subset 16.4M after quality cuts)", "DESIVAST void catalogs (3 algorithms)"],
    predictions: ["LSS-environment-dependent chirality test (cosmic-web alignment)"],
    figures: ["Matched-catalog footprint", "Per-environment CW fractions", "DESIVAST void-spiral test", "z-shell robustness", "HEALPix coherence at three resolutions"],
    remainingWork: [
      "Close remaining reviewer findings with real science (NOT reviewer-accepted — verified EXT board shows a real ChatGPT REJECT + Grok/Gemini MINOR-to-MAJOR)",
      "Compute-class queue: mask-dilation/randoms rebuilds + footprint re-tabulation (pod-side); #16 completeness-weighted δ still blocked on DESI LSS randoms, documented in-text",
      "arXiv endorsement + submission — gated behind a reviewer ACCEPT (packets are ready; reviews are not passed)",
    ],
    preprintId: "HUBIFY-2026-005",
    pdfMeta: "PDF · 39 pp · v0.1.107 · updated Jul 7, 2026 · md5 1b569055",
    artifacts: [
      { label: "Read PDF", href: "/papers/p5_desi_chirality_v0.1.107.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/p5_desi_chirality_v0.1.107.pdf", kind: "secondary", download: true },
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
