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
}

export const papers: Paper[] = [
  {
    slug: "paper-1",
    number: 1,
    title: "Spin-Torsion Cosmology: Structural Barriers, Falsifiable Predictions, and the Bounce-Inflation Landscape",
    version: "v2.2.0",
    pages: "~24",
    refs: "63+",
    readiness: 99,
    status: "Needs TIER 1 edits",
    statusVariant: "amber",
    target: "Physical Review D",
    description: "The foundational paper. Documents 14 ECH structural barriers, derives the ALP birefringence prediction (β = 0.27°), presents the f_NL = -35/8 benchmark, and maps the bounce-inflation landscape with model discrimination tables.",
    keyResults: [
      "14 ECH structural barriers close all minimal routes from bounce to dark energy",
      "ALP birefringence prediction β = 0.27° matches 3.6σ observed signal",
      "f_NL = -35/8 parameter-free prediction benchmarked",
      "Bounce model discrimination table (matter vs cuscuton vs ekpyrotic vs quintom vs inflation)",
      "424,181+ MCMC posterior samples across 3 frozen datasets",
      "Quintom-B w-crossing at 98.6% (50.9K samples)",
      "NANOGrav γ = 3.0 consistency (0.33σ from observed 3.2 ± 0.6)",
    ],
    surveys: ["DESI DR1 (f_NL tracers)", "Planck CMB (birefringence, bispectrum)", "ACT DR6 (birefringence)", "NANOGrav 15yr (GW background)"],
    predictions: ["f_NL = -35/8", "Birefringence β = 0.27°", "NANOGrav γ = 3.0", "Quintom w-crossing"],
    figures: ["LQG-Holst derivation", "14 barriers diagram", "ALP field evolution", "Model discrimination table", "MCMC posteriors"],
    remainingWork: [
      "TIER 1: Rename 'Golden Parameter' to 'Geometric Dilution Parameter (ξ)'",
      "TIER 1: Delete 'Peer Review Gallery' section (violates arXiv standards)",
      "TIER 1: Rewrite 'FAQ: Addressing Referee Concerns' as Discussion subsection",
      "TIER 1: Tone down conclusions ('paradigm shift' → conditional language)",
      "TIER 1: Strengthen Popławski attribution",
      "TIER 2: Add Data Availability statement with DOI",
      "TIER 2: Restructure from 23 → ~9 main sections",
    ],
  },
  {
    slug: "paper-2",
    number: 2,
    title: "f_NL = -35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation",
    version: "v1.3.0",
    pages: "~12",
    refs: "30+",
    readiness: 100,
    status: "Submission-Ready",
    statusVariant: "green",
    target: "Physical Review Letters",
    description: "The decisive test paper. Presents the parameter-free f_NL = -35/8 prediction, proves mechanism-independence across bounce models, and provides Fisher forecasts for SPHEREx detection significance.",
    keyResults: [
      "f_NL = -35/8 = -4.375 (parameter-free, mechanism-independent)",
      "Verified across 3 bounce models (matter bounce, LQC, Cuscuton)",
      "Normalization audit: 92% confidence via vertex-by-vertex Cai action",
      "Fisher forecast: SPHEREx σ(f_NL) ≈ 0.7–1.0 → 4.4–6.3σ detection",
      "Template mismatch quantification between bounce and local shapes",
    ],
    surveys: ["DESI DR1 (current constraint σ ≈ 4.1 combined)"],
    predictions: ["f_NL = -35/8"],
    figures: ["Fisher forecast contours", "Template overlap matrix", "σ(f_NL) sensitivity curves"],
    remainingWork: [],
  },
  {
    slug: "paper-3",
    number: 3,
    title: "Multi-Survey Anomaly Catalog: 328K Anomalies from 33.5M Sources Across 8 Surveys",
    version: "v0.5",
    pages: "~18",
    refs: "TBD",
    readiness: 95,
    status: "Draft (~95%)",
    statusVariant: "blue",
    target: "ApJS",
    description: "The catalog paper. Documents the first multi-survey AI anomaly sweep across 8 astronomical archives. 33.5M sources scored, 328K anomalies found. Demonstrates 6.1% f_NL improvement via latent-space multi-tracer selection.",
    keyResults: [
      "328,448 anomalies across 8 surveys from 33.5M sources",
      "6.1% f_NL σ improvement (DESI alone), 16.4% (DESI+SDSS)",
      "SPHEREx forecast: 4.38σ detection of f_NL = -35/8",
      "58.8% novel objects (not in SIMBAD) across all surveys",
      "10 taxonomy families: 76 AGN, 27 post-starburst, 363 blue compact",
      "16 NEOWISE IR-variable anomalies incl. z=5.65 QSO",
      "Injection/recovery: 0% false positive, 10–1,377x enrichment",
    ],
    surveys: ["DESI DR1", "SDSS DR18", "LAMOST DR10", "eROSITA DR1", "Planck CMB", "ACT DR6", "NEOWISE", "Gaia DR3"],
    predictions: ["f_NL improvement", "Multi-survey validation"],
    figures: ["Multi-survey sky map", "Score distributions", "Taxonomy UMAP", "f_NL improvement plot"],
    remainingWork: [
      "Compile LaTeX → PDF (needs texlive-publishers on pod)",
      "Integrate birefringence β result (or defer as systematic-dominated)",
      "Peer review round 1",
      "Add Phase 1 re-run results (improved QC)",
    ],
  },
  {
    slug: "paper-4",
    number: 4,
    title: "Galaxy Chirality at Scale: 8.47M Galaxies Classified, Dipole 0.43σ Null",
    version: "v0.8",
    pages: "~11",
    refs: "TBD",
    readiness: 85,
    status: "Draft (~85%)",
    statusVariant: "blue",
    target: "MNRAS",
    description: "The chirality catalog paper. Presents the largest bias-audited galaxy handedness catalog (8.47M galaxies, 40x prior work). Definitively refutes Shamir's 3% cosmic parity violation claim.",
    keyResults: [
      "8.47M galaxies classified (CW/CCW/NOT_SPIRAL)",
      "93.7% three-class validation accuracy",
      "8/8 bias hardening tests pass (flip-equivariance, rotation stability, etc.)",
      "CW/(CW+CCW) = 0.4974 (perfectly balanced after equivariant post-processing)",
      "Dipole 0.43σ (null — definitively refutes Shamir 3% claim)",
      "40x larger than any prior bias-audited chirality catalog",
    ],
    surveys: [],
    predictions: ["Parity test (indirect bounce test)"],
    figures: ["Chirality sky map", "Dipole fit", "Bias audit results"],
    remainingWork: [
      "Add confusion matrix figure",
      "Add training loss curves",
      "Add redshift distribution histogram",
      "Add NSIDE dependence table",
      "Peer review round 1",
    ],
  },
];

export function getPaperBySlug(slug: string): Paper | undefined {
  return papers.find((p) => p.slug === slug);
}
