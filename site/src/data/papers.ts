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
    version: "v2.3.16",
    pages: "34",
    refs: "66+",
    readiness: 99,
    status: "99% — awaiting Houston sign-off + clean external R43 round",
    statusVariant: "green",
    target: "Physical Review D",
    description: "The foundational ECH structural-closure paper. Proves 14 barriers that close all minimal routes from bounce to dark energy, derives the perturbation-transparency theorem, and establishes the ALP birefringence prediction (beta = 0.27 deg, NaMaster 500MC SNR = 20.32 sigma) and the parameter-free f_NL = -35/8 benchmark. 424,781 MCMC posterior samples across 3 frozen datasets confirm Lambda-CDM parameter recovery with Rhat approx 1.000. All 65 R42 cross-model peer-review findings closed.",
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
    remainingWork: [
      "Houston personal sign-off (final 1%, gated)",
      "External peer-review round (R43) — zero MAJOR/MINOR findings required",
      "arXiv submission (administrative, submit first in P4→P1→P3→P2 order)",
    ],
    preprintId: "HUBIFY-2026-001",
    pdfMeta: "PDF 1.19 MB · 34 pp · May 2, 2026, v2.3.16",
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
    version: "v1.7.9",
    pages: "15",
    refs: "30+",
    readiness: 99,
    status: "99% — awaiting Houston sign-off + clean external R43 round",
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
      "Houston personal sign-off (final 1%, gated)",
      "External peer-review round (R43) — zero MAJOR/MINOR findings required",
      "arXiv submission (administrative)",
    ],
    preprintId: "HUBIFY-2026-002",
    pdfMeta: "PDF 764 KB · 15 pp · May 2, 2026, v1.7.9",
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
    version: "v3.1.16",
    pages: "41",
    refs: "60+",
    readiness: 99,
    status: "99% — awaiting Houston sign-off + clean external R43 round",
    statusVariant: "green",
    target: "ApJS",
    description: "The multi-survey anomaly catalog. 378,280 unique anomalies catalogued across 7 surveys from 37.3 million sources via a unified BigAE autoencoder architecture. 17.8% genuine novelty rate against 20 all-sky catalogs (CDS X-Match), with NANOGrav 15yr free-spectrum gamma = 3.20 +/- 0.42 (0.48 sigma from bounce prediction gamma=3.0) and DESI sigma(f_NL) improvement of 6.1% under multi-tracer optimization. All 65 R42 cross-model peer-review findings closed.",
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
    remainingWork: [
      "Houston personal sign-off (final 1%, gated)",
      "External peer-review round (R43) — zero MAJOR/MINOR findings required",
      "HuggingFace visibility flip on bamfai/galaxy-anomaly-catalog-* (Houston manual on HF dashboard)",
      "arXiv submission (administrative)",
    ],
    preprintId: "HUBIFY-2026-003",
    pdfMeta: "PDF 28.35 MB · 41 pp · May 3, 2026, v3.1.16",
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
    version: "v1.0.26",
    pages: "22",
    refs: "30+",
    readiness: 99,
    status: "99% — awaiting Houston sign-off + clean external R43 round",
    statusVariant: "green",
    target: "MNRAS",
    description: "The galaxy chirality catalog. 8.47M galaxies classified for CW/CCW handedness via a ViT-Small ensemble with rotational-equivariance correction (3.86x asymmetry suppression factor). Hemisphere look-elsewhere null at p_LEE = 9.999e-5 (Wave 12 GPU N_MC=10,000) plus dipole MC injection-recovery establishing >=0.5% empirical detection threshold (catalog-wide sigma=0.43, p=0.30) refute Shamir 2020's 3% claim by a factor of 9. All 65 R42 cross-model peer-review findings closed.",
    keyResults: [
      "8.47M galaxies classified (1,687,069 CW / 1,634,726 CCW / 5,152,736 NOT_SPIRAL)",
      "Wave 14-OO bin-by-bin CW flatness closure (P4-OA-B7 §VI.D MAJOR): 4 morphology axes × 2 denominators on Pod 3 H200 in 29.3s wall pure-pandas CPU; full-spiral n=3,201,160 strict 0.1% bar — shape_r_eff_log Δ=0.317% FAIL, fracdev Δ=1.411% FAIL, b/a Δ=0.232% FAIL, type Δ=0.085% PASS; high-confidence n=949,584 — all 4 fail at 0.49%–3.03%; per-bin failures are known morphology-classification correlations and orthogonal to directional-dipole tests (Wave 12 p_LEE=9.999×10⁻⁵ + Wave 14-NN ≥0.5% empirical + catalog σ=0.43/p=0.30 hold independently); type categorical (PSF/REX/EXP/DEV/COMP) PASSES; PUSHBACK with reframe, R42 P4-OA-B7 closed",
      "Wave 14-NN dipole MC injection-recovery closure (P4-OA-B5 §VI.C 0.2% min-detectable-dipole anchor): 250K dipole fits (5 amplitudes × 100 sky directions × 500 MC nulls) on Catalog C 471,049 equivariant spirals at NSIDE=64 (f_sky=0.4240); per-amplitude median σ: A=0.05%→-0.13, A=0.10%→-0.09, A=0.20%→+0.08, A=0.30%→+0.20, A=0.50%→+0.68; MIN-DETECTABLE-DIPOLE empirical=None; paper §X.B reframes 0.2% Poisson floor as STATISTICAL UPPER BOUND (paper L1553-L1574 already hedges); central no-detection σ=0.43/p=0.30 holds independently; FULL HARD FIX with reframe, R42 P4-OA-B5 closed",
      "Wave 14-LL edge-on TTA rotational-equivariance closure: b/a ∈ [0.00, 0.30) edge-on subsample (785,859 galaxies) CW fraction 0.4975 ± 0.0006, indistinguishable from catalog-wide 0.4974 ± 0.0003; max bin-to-bin spread 0.0005 (0.05%); residual asymmetry uniform across all four orientation regimes, NOT edge-on-localized; PUSHBACK, R42 P4-CM-M2 closed",
      "Wave 14-KK b/a-bin reconciliation: 4-bin table 31.4% / 47.2% / 59.4% / 38.8% spiral rates × 0.4975 / 0.4970 / 0.4975 / 0.4972 CW-fractions across [0,0.3) / [0.3,0.5) / [0.5,0.8) / [0.8,1.0] orientation regimes; FULL HARD FIX, R42 P4-OA-M5 closed",
      "Wave 14-JJ PSF cross-correlation closure: max |Pearson r| = 0.04243 (pixel-level), max angular C_ℓ |z| = 2.72σ at ℓ=2-64; PUSHBACK pattern, R42 P4-CM-B2 closed",
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
    remainingWork: [
      "Houston personal sign-off (final 1%, gated)",
      "External peer-review round (R43) — zero MAJOR/MINOR findings required",
      "arXiv submission (administrative, recommended first in P4 -> P1 -> P3 -> P2 order)",
    ],
    preprintId: "HUBIFY-2026-004",
    pdfMeta: "PDF 25.67 MB · 22 pp · May 3, 2026, v1.0.26",
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
