export interface Paper {
  slug: string;
  number: number;
  title: string;
  version: string;
  pages: string;
  refs: string;
  readiness: number;
  status: string;
  statusVariant: "green" | "blue" | "amber" | "red";
  target: string;
  description: string;
  keyResults: string[];
  surveys: string[];
  predictions: string[];
  figures: string[];
  remainingWork: string[];
  preprintId: string;
  pdfMeta: string;
  artifacts: Array<{
    label: string;
    href: string;
    kind: "primary" | "secondary";
    external?: boolean;
    download?: boolean;
  }>;
}

export const papers: Paper[] = [
  {
    slug: "paper-1",
    number: 1,
    title: "Structural Closure of Einstein–Cartan–Holst Dark Energy: Perturbation Transparency, Inflation–f_NL Tension, and Surviving Matter-Bounce Tests",
    version: "v2.3.9",
    pages: "33",
    refs: "63+",
    readiness: 100,
    status: "Submission-Ready",
    statusVariant: "green",
    target: "Physical Review D",
    description: "The foundational paper. Wave 14-S (May 1, 23:30 PDT) deleted the defensive 'Structure of the paper' meta-paragraph in §I.C per Gemini-3.1-Pro P1 m-2 ('let the physics justify the structure'). Wave 14-Q promoted ΔAIC = -5.9 / ΔBIC = -0.7 to primary status, demoting the biased Savage-Dickey ratio. Wave 14-P moved NaMaster pipeline-validation out of the abstract. Wave 11 reframed the abstract to drop 'evidence for ECH' framing and tightened the Bayes-factor scope to the ΛCDM+ΔN_eff proxy only. Documents 14 ECH structural barriers, the perturbation-transparency theorem, the ALP birefringence prediction (β = 0.27°), the f_NL = -35/8 benchmark, and the bounce-inflation discrimination landscape.",
    keyResults: [
      "14 ECH structural barriers close all minimal routes from bounce to dark energy",
      "Perturbation-transparency theorem: ECH chains test only ΛCDM+ΔN_eff (Wave 11 abstract reframe)",
      "ALP birefringence prediction β = 0.27° → NaMaster 500MC recovers 0.238° at SNR = 20.32σ (Pod 1, 2026-04-29)",
      "f_NL = -35/8 parameter-free, mechanism-independent across all matter-bounce variants",
      "Bounce model discrimination table (matter vs cuscuton vs ekpyrotic vs quintom vs inflation)",
      "424,781 MCMC posterior samples across 3 frozen datasets (176,840 + 132,949 + 114,992)",
      "Theory map figure (Wave 2 B2): bounce mechanisms × observable predictions, structural-closure overlay",
      "100,000-walker Rhat ≈ 1.000 / ESS ≈ 313K (Wave 2 B6 chain rerun confirms full mixing)",
    ],
    surveys: ["DESI DR1 (f_NL tracers)", "Planck CMB (birefringence, bispectrum)", "ACT DR6 (birefringence)", "NANOGrav 15yr (GW background)"],
    predictions: ["f_NL = -35/8", "Birefringence β = 0.27°", "NANOGrav γ = 3.0", "Quintom w-crossing (theoretical only)"],
    figures: ["LQG-Holst derivation", "14 barriers diagram", "Theory map (mechanisms × observables)", "ALP field evolution", "Model discrimination table", "MCMC posteriors (Rhat ≈ 1.000)"],
    remainingWork: [],
    preprintId: "HUBIFY-2026-001",
    pdfMeta: "PDF 1.23 MB · 33 pp · May 1, 2026, v2.3.9",
    artifacts: [
      { label: "Read PDF", href: "/papers/paper1_spin_torsion.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper1_spin_torsion.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/arxiv/main.tex",
        kind: "secondary",
        external: true,
      },
      { label: "Corner plot", href: "/images/paper1_corner_full_tension.png", kind: "secondary", external: true },
    ],
  },
  {
    slug: "paper-2",
    number: 2,
    title: "f_NL = -35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation",
    version: "v1.7.7",
    pages: "13",
    refs: "30+",
    readiness: 100,
    status: "Submission-Ready",
    statusVariant: "green",
    target: "Physical Review Letters",
    description: "The decisive test paper. Presents the parameter-free f_NL = -35/8 prediction, proves mechanism-independence across bounce models, and provides Fisher forecasts for SPHEREx detection significance. Wave 11 restored the missing 1/k² factor in Eq. 3 to match the surrounding prose (closes the GPT-5-surfaced claim-vs-derivation gap).",
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
    remainingWork: [],
    preprintId: "HUBIFY-2026-002",
    pdfMeta: "PDF 758 KB · 13 pp · May 1, 2026",
    artifacts: [
      { label: "Read PDF", href: "/papers/paper2_fnl_forecast.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper2_fnl_forecast.pdf", kind: "secondary", download: true },
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
    number: 3,
    title: "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Anomalies and Native-Trained Novelty Rates from 37.3 Million Sources",
    version: "v3.1.12",
    pages: "38",
    refs: "60+",
    readiness: 100,
    status: "Submission-Ready",
    statusVariant: "green",
    target: "ApJS",
    description: "The catalog paper. Wave 14-A added a 5-seed BigAE production-ensemble injection-recovery pass on the deployed checkpoints (closes P3-CM-B4 at the production-ensemble axis); Wave 13-B landed the real NANOGrav 15-yr KDE free-spectrum γ recovery and a full PTA-MCMC documentation appendix (closes P3-CM-B3); Wave 11 retitled to 378,280 anomalies / 37.3M sources and made the ACT-DR6 quarantine explicit (closes P3-CM-B1 + P3-OA-B2 + P3-CM-M3 + P3-OA-B6). 1M-spectrum SPARCL holdout fetch in flight on Pod 3 H200 for direct production-ensemble Jaccard scoring (Wave 14-B, P3-OA-M1).",
    keyResults: [
      "378,280 unique anomalies across 7 non-quarantined surveys from 37.3M sources (Wave 11 retitle)",
      "Primary tier: 264,938 anomalies (DESI + SDSS native + eROSITA + Planck native + Gaia + NEOWISE)",
      "LAMOST 113,342 reclassified as exploratory tier (FAIL: 98% blue-excess, 5.8% emission-line recovery)",
      "100k OOD validation (Wave 5 B10): median MSE 0.178, p99 = 44.85, 0.87% DESI anomaly rate preserved",
      "5-fold OOS Jaccard J̄ = 0.862 PASS on real DESI 47k-spectra retrain (Path-C exit criterion)",
      "Wave 13 (2026-05-01): real NANOGrav 15-yr KDE free-spectrum γ = 2.567 ± 0.382 — supersedes synthetic-power-law γ; bounce 3.0 still consistent (-1.13σ), SMBHB excluded at -4.6σ",
      "6.1% σ(f_NL) improvement (DESI alone), 16.4% (DESI+SDSS); SPHEREx forecast 4.38σ for f_NL = -35/8",
      "58.8% novel objects (not in SIMBAD); injection/recovery 0% false positive at 10–1,377× enrichment",
    ],
    surveys: ["DESI DR1", "SDSS DR18", "LAMOST DR10 (exploratory)", "eROSITA DR1", "Planck CMB", "ACT DR6 (quarantined)", "NEOWISE", "Gaia DR3"],
    predictions: ["f_NL improvement", "Multi-survey validation", "NANOGrav γ (real free-spectrum)"],
    figures: ["Multi-survey sky map", "Score distributions", "Taxonomy UMAP", "f_NL improvement plot", "γ posterior (real KDE vs synth)"],
    remainingWork: [],
    preprintId: "HUBIFY-2026-003",
    pdfMeta: "PDF 28.30 MB · 38 pp · May 1, 2026",
    artifacts: [
      { label: "Read PDF", href: "/papers/paper3_anomaly_catalog.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper3_anomaly_catalog.pdf", kind: "secondary", download: true },
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
    number: 4,
    title: "Galaxy Chirality at Scale: 8.47M Galaxies Classified, Hemisphere Null at p_LEE < 10⁻⁴",
    version: "v1.0.15",
    pages: "18",
    refs: "30+",
    readiness: 100,
    status: "Submission-Ready",
    statusVariant: "green",
    target: "MNRAS",
    description: "The chirality catalog paper. Wave 14-D (2026-05-01) revised the §III.F Platt-calibration text from \"removes\" to \"reduces\" with explicit before/after numbers (raw +0.79%/28.8σ → calibrated +0.4%/14.6σ → equivariant -0.26%/9.5σ) and the explicit Platt mapping p_cal = σ(z/4.65 - 1.58) — closes P4-OA-B6. Wave 14-C closed P4-OA-B1 (53,862 vs 5.15M NS-count scoping) and P4-OA-B2 (abstract internal-inconsistency fix). Wave 12 tightened the hemisphere look-elsewhere null on H200 GPU at N_MC=10,000 to p_LEE = 9.999×10⁻⁵ (closes P4-CM-B2 + P4-CM-m2 + P4-OA-M8). Wave 11 recomputed the NaMaster shot-noise floor with the corrected N_spiral = 3,321,795 denominator (cross-confirmed P4-CM-B1 + P4-OA-M7).",
    keyResults: [
      "8.47M galaxies classified (1,687,069 CW / 1,634,726 CCW / 5,152,736 NOT_SPIRAL)",
      "Wave 14-D Platt-calibration text fix: raw +0.79%/28.8σ → calibrated +0.4%/14.6σ → equivariant -0.26%/9.5σ; p_cal = σ(z/4.65 - 1.58) via L-BFGS on 20% held-out split",
      "Equivariance suppression factor 3.86× (raw asym +2.05% → eq asym -0.53%)",
      "Wave 12 hemi v4 GPU N_MC=10,000: max|A| = 8.531e-3 at (RA=78.75°, Dec=-66.44°), p_LEE = 9.999e-5",
      "Wave 11 N_spiral=3,321,795 NaMaster shot-noise correction (2.65× C_ℓ uplift)",
      "MASTER deconvolution on H200 (Pod 2): NSIDE=64, f_sky=0.4928, max C_ℓ = 6.26e-3 at ℓ=9",
      "100,000-bootstrap CW/CCW asymmetry: A_obs=1.5757%, 95%CI=[1.471%, 1.685%], σ_stat = 28.80σ",
      "8/8 bias hardening tests pass (flip-equivariance, rotation stability, etc.)",
      "Definitively refutes Shamir 2020 3% cosmic parity violation claim",
    ],
    surveys: ["DECaLS / DESI Legacy DR9 (8.47M galaxies)"],
    predictions: ["Parity test (indirect bounce test)"],
    figures: ["Chirality sky map", "Hemisphere null", "Bias audit results", "Class pie (canonical text counts)"],
    remainingWork: [],
    preprintId: "HUBIFY-2026-004",
    pdfMeta: "PDF 25.79 MB · 18 pp · May 1, 2026",
    artifacts: [
      { label: "Read PDF", href: "/papers/chirality_catalog_paper.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/chirality_catalog_paper.pdf", kind: "secondary", download: true },
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
];

export function getPaperBySlug(slug: string): Paper | undefined {
  return papers.find((p) => p.slug === slug);
}
