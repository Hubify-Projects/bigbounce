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
      note: "Houston external round queued on current version",
    },
    overrides.signoff ?? {
      label: "Houston sign-off",
      state: "blocked",
      note: "The final 1% — Houston only",
    },
    overrides.arxiv ?? {
      label: "arXiv submission",
      state: "pending",
      note: "Needs endorsement · order P4 → P1A+P1B → P3 → P2 → P5",
    },
  ];
}

export const papers: Paper[] = [
  {
    slug: "paper-1a",
    number: "1A",
    title: "Structural Closure of Einstein–Cartan–Holst Dark Energy: Perturbation Transparency, Inflation–f_NL Tension, and Surviving Matter-Bounce Tests",
    version: "v1A.0.50",
    lastUpdated: "2026-06-09",
    tldr: "Closes all four minimal Einstein–Cartan–Holst routes from a quantum bounce to dark energy and proves the Holst sector is invisible to scalar/tensor perturbations — leaving two clean observational kill-tests (LiteBIRD birefringence, SPHEREx f_NL).",
    path: publicationPath({
      external: {
        label: "External journal-style review",
        state: "active",
        note: "Round 1 (Grok/Gemini/ChatGPT) closed in v1A.0.40 · next Houston round queued",
      },
    }),
    pages: "23",
    refs: "72",
    readiness: 92,
    statusVariant: "green",
    target: "Physical Review D",
    description: "The theory foundation of the program (PRD target). Proves a perturbation-transparency theorem — for canonical scalar matter, torsion vanishes at all perturbation orders and the Holst sector decouples from every scalar/tensor observable — and closes all four minimal Einstein–Cartan–Holst routes from the quantum bounce to late-time dark energy. The structural-tension argument shows the dark-energy mechanism (N_tot ≈ 92 post-bounce e-folds) is incompatible with the f_NL = -35/8 matter-bounce signature; technical verification lives in Paper 1B.",
    keyResults: [
      "14 ECH structural barriers close all minimal routes from bounce to dark energy",
      "Perturbation-transparency theorem: torsion vanishes at all perturbation orders for canonical scalars",
      "Structural-tension argument (§III): N_tot ≈ 92 post-bounce e-folds is incompatible with f_NL = -35/8",
      "Bounce-model discrimination table: matter-bounce vs Cuscuton vs ekpyrotic vs quintom vs slow-roll",
      "f_NL = -35/8 parameter-free, mechanism-independent across all matter-bounce variants",
      "Matter-bounce SPHEREx detection forecast: 4.7-12σ by 2027 (cross-references Paper 2)",
    ],
    surveys: ["Planck CMB", "ACT DR6", "DESI DR1", "DESI DR2 (referenced)", "NANOGrav 15yr"],
    predictions: ["f_NL = -35/8", "Birefringence β = 0.27°", "NANOGrav γ = 3.0", "Quintom w-crossing falsification path"],
    figures: ["LQG-Holst derivation", "14 barriers diagram", "Theory map (mechanisms × observables)", "Model discrimination table"],
    remainingWork: [
      "Houston external review round on v1A.0.50",
      "Houston personal sign-off (final 1%, gated)",
      "arXiv endorsement + submission (astro-ph.CO)",
    ],
    preprintId: "HUBIFY-2026-001A",
    pdfMeta: "PDF 1.5 MB · 23 pp · updated Jun 9, 2026",
    artifacts: [
      { label: "Read PDF", href: "/papers/paper1a_ech_nogo_v1A.0.50.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper1a_ech_nogo_v1A.0.50.pdf", kind: "secondary", download: true },
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
    title: "Technical Verification Companion: ΛCDM+ΔN_eff MCMC Proxy, NaMaster Pipeline Recovery, and Spectator-ALP Consistency Check for the ECH Spin-Torsion Program",
    version: "v1B.0.50",
    lastUpdated: "2026-06-09",
    tldr: "Technical companion to Paper 1A: a 424K-sample ΛCDM+ΔN_eff MCMC null test (ΔN_eff consistent with zero), a NaMaster birefringence pipeline-recovery exercise, and a spectator-ALP consistency check against the Planck+ACT β = 0.342° measurement.",
    path: publicationPath({}),
    pages: "12",
    refs: "32",
    readiness: 90,
    statusVariant: "green",
    target: "Physical Review D (companion)",
    description: "Technical verification companion to Paper 1A, documenting three analyses: a 424,781-sample Cobaya ΛCDM+ΔN_eff MCMC that recovers ΛCDM (H0 = 67.68 ± 1.06 km/s/Mpc, ΔN_eff consistent with zero); a NaMaster pipeline-recovery test on the Planck Commander map (inject β=0.27°, recover 0.238°); and a spectator-ALP consistency check against the published Planck+ACT β = 0.342° ± 0.094° (3.6σ).",
    keyResults: [
      "309,789 frozen MCMC samples across 2 converged dataset combinations (176,840 full-tension + 132,949 Planck+BAO+SN); third Planck-only ongoing",
      "ΔN_eff consistent with zero (-0.020 ± 0.169 full-tension; +0.065 ± 0.17 Planck+BAO+SN); H0 = 67.68 ± 1.06",
      "NaMaster 500MC: β=0.27° → recover 0.238° at SNR=20.32; β=0.342° → recover 0.302° at SNR=25.71",
      "Spectator-ALP f_a ~ M_Pl, m ~ H_0 consistent with Eskilt+ joint Planck+ACT 0.342°±0.094° (3.6σ)",
      "Pipeline-recovery bias 0.032° well below the published observational σ_β = 0.094°",
      "DESI DR2 w0wa free chain (Planck NPIPE + DESI DR2 + Pantheon+ + DES-SN5YR) in progress",
    ],
    surveys: ["Planck NPIPE", "Planck Commander (CMB pol)", "ACT DR6", "DESI DR2 BAO (running)", "Pantheon+ SN", "DES-SN5YR (running)", "NANOGrav 15yr"],
    predictions: ["ΔN_eff null", "Birefringence β = 0.27° (recovery test)", "w0-wa quintom-B test (DESI DR2)"],
    figures: ["Δχ² and ΔAIC summary table", "Corner plots", "NaMaster recovery posteriors", "Cross-paper status table"],
    remainingWork: [
      "Houston external review round on v1B.0.49",
      "Houston personal sign-off (final 1%, gated)",
      "arXiv submission (administrative, alongside P1A)",
    ],
    preprintId: "HUBIFY-2026-001B",
    pdfMeta: "PDF 920 KB · 12 pp · updated Jun 9, 2026",
    artifacts: [
      { label: "Read PDF", href: "/papers/paper1b_mcmc_companion_v1B.0.50.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper1b_mcmc_companion_v1B.0.50.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/arxiv/paper1b_mcmc_companion.tex",
        kind: "secondary",
        external: true,
      },
      { label: "Theory paper (1A)", href: "/papers/paper-1a", kind: "secondary" },
      { label: "Corner plot", href: "/images/paper1_corner_full_tension.png", kind: "secondary", external: true },
    ],
  },
  {
    slug: "paper-2",
    number: "2",
    title: "f_NL = -35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation",
    version: "v1.7.45",
    lastUpdated: "2026-06-03",
    tldr: "Shows f_NL = −35/8 is a parameter-free, mechanism-independent prediction of all matter-bounce models, and forecasts SPHEREx will detect or kill it at 4.7–12σ by ~2028 — the decisive bounce-vs-inflation discriminator.",
    path: publicationPath({}),
    pages: "23",
    refs: "39",
    readiness: 95,
    statusVariant: "green",
    target: "Physical Review Letters",
    description: "The decisive SPHEREx discrimination paper. Proves f_NL = -35/8 is parameter-free and mechanism-independent across all matter-bounce variants, then delivers Fisher forecasts showing 4.7-12 sigma SPHEREx detection significance by 2027. Multi-tracer sigma(f_NL) marginalized floor of 0.067-0.116 across 6 configurations, with magnification-bias identified as the dominant systematic axis. All 65 R42 cross-model peer-review findings closed.",
    keyResults: [
      "f_NL = -35/8 = -4.375 (parameter-free, mechanism-independent)",
      "Verified across 3 bounce models (matter bounce, LQC, Cuscuton)",
      "Eq. 3 1/k² shape function fix (Wave 11) restores claim-derivation consistency",
      "Normalization audit: 92% confidence via vertex-by-vertex Cai action",
      "SPHEREx Fisher forecast: σ(f_NL) ≈ 0.36 (Fisher) / 0.93 (Munchmeyer+2019 conservative) → 4.7–12σ detection",
      "Heinrich+2023 σ(f_NL) ≈ 0.5–0.7 SPHEREx anchor (R35 polish)",
      "Template mismatch quantification between bounce and local shapes",
    ],
    surveys: ["DESI DR1 (current constraint σ ≈ 4.1 combined)"],
    predictions: ["f_NL = -35/8"],
    figures: ["Fisher forecast contours", "Template overlap matrix", "σ(f_NL) sensitivity curves"],
    remainingWork: [
      "R22prov2 near-clean (3/5 vendors zero findings) → mini-wave closed in v1.7.45 → next round",
      "Houston personal sign-off (final 1%, gated)",
      "arXiv submission (administrative)",
    ],
    preprintId: "HUBIFY-2026-002",
    pdfMeta: "PDF 808 KB · 23 pp · updated Jun 3, 2026",
    artifacts: [
      { label: "Read PDF", href: "/papers/paper2_fnl_forecast_v1.7.45.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper2_fnl_forecast_v1.7.45.pdf", kind: "secondary", download: true },
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
    title: "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Anomalies and Native-Trained Novelty Rates from 37.3 Million Sources",
    version: "v3.1.80",
    lastUpdated: "2026-06-09",
    tldr: "A 378,280-object anomaly catalog mined from 37.3M sources across 7 surveys with one autoencoder architecture — 17.8% of top-ranked objects are new to existing catalogs, plus a NANOGrav free-spectrum fit consistent with matter-bounce γ = 3.0.",
    path: publicationPath({}),
    pages: "22",
    refs: "71",
    readiness: 90,
    statusVariant: "green",
    target: "ApJS",
    description: "The multi-survey anomaly catalog: 378,280 unique anomalies from 37.3 million sources across 7 surveys via one BigAE autoencoder architecture, with a 17.8% novelty rate at the top-1,000 stratum against 20 all-sky catalogs. A NANOGrav 15-yr free-spectrum re-fit gives γ = 2.567 ± 0.382 — matter-bounce γ=3.0 is consistent (+1.13σ) while SMBHB γ=4.33 is excluded (+4.61σ). Multi-tracer forecast: σ(f_NL) = 8.27 ± 2.37.",
    keyResults: [
      "378,280 unique anomalies across 7 non-quarantined surveys from 37.3M sources (Wave 11 retitle)",
      "Catalog-grade tier: 264,938 anomalies (DESI + SDSS native + eROSITA + Planck native + Gaia + NEOWISE); point-source tier 378,080; Planck CMB-patch tier 200",
      "LAMOST 113,342 reclassified as exploratory tier (FAIL: ~56% B-dominant cross-transfer empirical; native retrain 21.4x reduction to 2,054 at S>5)",
      "100k OOD validation (Wave 5 B10): median MSE 0.178, p99 = 44.85, 0.87% DESI anomaly rate preserved",
      "5-fold OOS Jaccard J̄ = 0.862 PASS on real DESI 47k-spectra retrain (Path-C exit criterion)",
      "NANOGrav 15-yr KDE free-spectrum γ = 2.567 ± 0.382 — bounce γ=3.0 consistent (+1.13σ), SMBHB γ=4.33 excluded (+4.61σ)",
      "Empirical α_jk = 0.19 ± 0.65 (consistent with zero at 0.29σ); σ(f_NL) = 8.27 ± 2.37 multi-tracer forecast; SPHEREx 4.38σ for f_NL = -35/8",
      "58.8% novel objects (not in SIMBAD); injection/recovery 0% false positive at 10–1,377× enrichment",
    ],
    surveys: ["DESI DR1", "SDSS DR18", "LAMOST DR10 (exploratory)", "eROSITA DR1", "Planck CMB", "ACT DR6 (quarantined)", "NEOWISE", "Gaia DR3"],
    predictions: ["f_NL improvement", "Multi-survey validation", "NANOGrav γ (real free-spectrum)"],
    figures: ["Multi-survey sky map", "Score distributions", "Taxonomy UMAP", "f_NL improvement plot", "γ posterior (real KDE vs synth)"],
    remainingWork: [
      "Houston external review round on v3.1.79",
      "Houston personal sign-off (final 1%, gated)",
      "HuggingFace visibility flip on bamfai/galaxy-anomaly-catalog-* (Houston manual on HF dashboard)",
      "arXiv submission (administrative)",
    ],
    preprintId: "HUBIFY-2026-003",
    pdfMeta: "PDF 4.3 MB · 22 pp · updated Jun 9, 2026",
    artifacts: [
      { label: "Read PDF", href: "/papers/paper3_anomaly_catalog_v3.1.80.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper3_anomaly_catalog_v3.1.80.pdf", kind: "secondary", download: true },
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
    ],
  },
  {
    slug: "paper-4",
    number: "4",
    title: "Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)",
    version: "v1.0.167",
    lastUpdated: "2026-06-09",
    tldr: "Classifies 8.47M galaxies for spiral handedness with a rotation-equivariant ViT ensemble and finds a null real-space chirality dipole (+0.43σ, p=0.30) — the earlier −0.122σ subsample-mask null was withdrawn in v1.0.166 after a provenance audit.",
    path: [
      { label: "Draft complete", state: "done" },
      {
        label: "Internal multi-model review",
        state: "done",
        note: "Native-PDF autoloop: Claude · GPT · Gemini · Grok · Perplexity",
      },
      {
        label: "Cross-vendor rounds clean",
        state: "active",
        note: "Re-opened by the v1.0.166 headline retraction — two clean rounds required",
      },
      {
        label: "External journal-style review",
        state: "active",
        note: "3-vendor round closed in v1.0.151 · next Houston round queued on v1.0.166",
      },
      {
        label: "Houston sign-off",
        state: "blocked",
        note: "The final 1% — Houston only",
      },
      {
        label: "arXiv submission",
        state: "pending",
        note: "First in queue once clean rounds + sign-off land",
      },
    ],
    pages: "17",
    refs: "46",
    readiness: 85,
    statusVariant: "amber",
    target: "MNRAS",
    description: "The galaxy chirality catalog: 8.47M galaxies classified CW/CCW by a ViT-Small ensemble with rotational-equivariance correction (3.86× asymmetry suppression). The parity test is the dipole — the real-space fit at +0.43σ (p=0.30) plus a template-fit exclusion of a clean 1.7% dipole (z≈−18) and a ≥0.5% empirical detection threshold refute Shamir 2020's 3% claim. v1.0.166 withdraws the earlier −0.122σ subsample-mask MASTER null after a provenance audit showed it was computed on a synthetic-footprint catalog; the MASTER channel is now presented as a systematics diagnostic (+7.28σ on the real apodized footprint, unchanged under depth-stratified nulls — survey systematics, not cosmology). The 0.4974 CW monopole (9.5σ) traces to GZ1 training-label bias: spatially uniform, not parity violation.",
    keyResults: [
      "8.47M galaxies classified (1,687,069 CW / 1,634,726 CCW / 5,152,736 NOT_SPIRAL)",
      "Real-space ℓ=1 dipole at +0.43σ (p=0.30) + template-fit exclusion of a clean 1.7% dipole at z≈−18 (raw pseudo-C_ℓ 6.48σ was a mask-coupling artifact; earlier −0.12σ subsample-mask null withdrawn in v1.0.166 — synthetic-footprint provenance)",
      "Bin-by-bin CW flatness audited across 4 morphology axes; residuals are classification correlations, orthogonal to dipole tests",
      "Dipole MC injection-recovery (250K fits): ≥0.5% empirical detection threshold; catalog-wide σ=0.43, p=0.30 — no detection",
      "Edge-on TTA equivariance check: CW fraction 0.4975 ± 0.0006 on 785,859 edge-on galaxies, indistinguishable from catalog-wide",
      "Platt calibration: raw +0.79%/28.8σ → calibrated +0.4%/14.6σ → equivariant -0.26%/9.5σ",
      "Equivariance suppression factor 3.86× (raw asym +2.05% → eq asym -0.53%)",
      "Hemisphere look-elsewhere null: p_LEE < 10⁻⁴ (0/10,000 MC nulls reach data)",
      "100,000-bootstrap CW/CCW asymmetry: A_obs=1.5757%, 95%CI=[1.471%, 1.685%], σ_stat = 28.80σ",
      "8/8 bias hardening tests pass (flip-equivariance, rotation stability, etc.)",
      "Definitively refutes Shamir 2020 3% cosmic parity violation claim",
    ],
    surveys: ["DECaLS / DESI Legacy DR9 (8.47M galaxies)"],
    predictions: ["Parity test (indirect bounce test)"],
    figures: ["Chirality sky map", "Hemisphere null", "Bias audit results", "Class pie (canonical text counts)"],
    remainingWork: [
      "TWO clean cross-vendor R-rounds on v1.0.166 (post-retraction rule, >5pp backward step)",
      "Houston personal sign-off (final 1%, gated)",
      "GitHub release PDF asset upload (tag + commit already pushed)",
      "arXiv endorsement + submission (astro-ph.GA + astro-ph.CO, first in queue)",
    ],
    preprintId: "HUBIFY-2026-004",
    pdfMeta: "PDF 25 MB · 17 pp · updated Jun 9, 2026",
    artifacts: [
      { label: "Read PDF", href: "/papers/chirality_catalog_paper_v167.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/chirality_catalog_paper_v167.pdf", kind: "secondary", download: true },
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
    ],
  },
  {
    slug: "paper-5",
    number: "5",
    title: "Environmental Dependence of Spiral Chirality Across DESI Large-Scale Structure: A Cross-Matched Test of Local Coherence and Cosmic-Web Alignment",
    version: "v0.1.51-2026-06-09",
    lastUpdated: "2026-06-09",
    tldr: "Cross-matches P4's spiral handedness with DESI large-scale structure (791,635 matched spirals + 56,981 void spirals) and finds galaxy chirality is statistically independent of cosmic-web environment — constraining environment-coupled parity models.",
    path: publicationPath({}),
    pages: "21",
    refs: "—",
    readiness: 90,
    statusVariant: "green",
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
    ],
    surveys: ["P4 chirality catalog (HF bamfai/galaxy-chirality-catalog, 8.47M)", "DESI DR1 zall-pix-iron.fits (~22.5M rows; matched subset 16.4M after quality cuts)", "DESIVAST void catalogs (3 algorithms)"],
    predictions: ["LSS-environment-dependent chirality test (cosmic-web alignment)"],
    figures: ["Matched-catalog footprint", "Per-environment CW fractions", "DESIVAST void-spiral test", "z-shell robustness", "HEALPix coherence at three resolutions"],
    remainingWork: [
      "Houston external review round on v0.1.50",
      "Houston personal sign-off (final 1%, gated)",
      "arXiv endorsement + submission (last in queue)",
    ],
    preprintId: "HUBIFY-2026-005",
    pdfMeta: "PDF 1.0 MB · 21 pp · updated Jun 9, 2026",
    artifacts: [
      { label: "Read PDF", href: "/papers/p5_desi_chirality_v0.1.51.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/p5_desi_chirality_v0.1.51.pdf", kind: "secondary", download: true },
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
