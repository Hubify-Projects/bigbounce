export interface SurveyAnomaly {
  rank: number;
  ra: number;
  dec: number;
  score: number;
  type?: string;
}

export interface Survey {
  slug: string;
  name: string;
  shortName: string;
  sources: string;
  anomalies: number;
  anomalyRate: string;
  qcStatus: "pass" | "caution" | "fail" | "needs-expansion";
  qcNote: string;
  description: string;
  wavelength: string;
  cost: string;
  runtime: string;
  pipeline: string;
  paperRefs: string[];
  figures: string[];
  keyFindings: string[];
  followUpTasks: string[];
  topAnomalies: SurveyAnomaly[];
  connections: { label: string; href: string }[];
}

export const surveys: Survey[] = [
  {
    slug: "desi-dr1",
    name: "DESI DR1",
    shortName: "DESI",
    sources: "22.5M spectra",
    anomalies: 195829,
    anomalyRate: "0.87%",
    qcStatus: "pass",
    qcNote: "Gold standard. 2,145 SNR-filtered, 1,127 uncataloged, 10 taxonomy families.",
    description: "The Dark Energy Spectroscopic Instrument first data release. Our flagship anomaly catalog — the first full-DR1-scale autoencoder search (~90x prior EDR work).",
    wavelength: "Optical spectroscopy (3600-9800 Å)",
    cost: "~$200",
    runtime: "~24h",
    pipeline: "BigAE autoencoder (660K params, 128-dim latent)",
    paperRefs: ["Paper 3 — primary dataset", "Paper 2 — f_NL tracers"],
    figures: ["DESI anomaly sky map", "Score distribution", "Taxonomy UMAP", "Latent space t-SNE"],
    keyFindings: [
      "195,829 anomalies from 22.5M spectra (0.87%)",
      "2,145 pass SNR filter, 120 gold (>5σ)",
      "1,127 not in SIMBAD or NED (52.5% uncataloged)",
      "10 taxonomy families: 76 AGN, 27 post-starburst, 363 blue compact",
      "16 NEOWISE IR-variable anomalies incl. z=5.65 QSO",
      "9.5% f_NL improvement via latent-space multi-tracer",
      "Injection/recovery: 0% false positive, 10–1,377x enrichment",
    ],
    followUpTasks: [
      "Pipeline 1 Steps 2-6: cross-match, classify, validate bias, re-measure σ(f_NL)",
      "Download all 195K spectra for full spectral analysis",
      "DESI × eROSITA cross-match (optical × X-ray)",
      "Re-run with Vision Transformer architecture",
      "Full 18M structured catalog (band-ratio classification on ALL spectra)",
    ],
    topAnomalies: [
      { rank: 1, ra: 213.31, dec: 37.34, score: 3.01, type: "QSO (z=1.68)" },
      { rank: 2, ra: 69.85, dec: 0.32, score: 4.44, type: "Galaxy (z=0.96)" },
      { rank: 3, ra: 294.01, dec: 66.05, score: 5.35, type: "Galaxy (z=0.98)" },
    ],
    connections: [
      { label: "f_NL Prediction", href: "/predictions/fnl" },
      { label: "Paper 3", href: "/papers/paper-3" },
      { label: "SDSS cross-match", href: "/surveys/sdss-dr18" },
    ],
  },
  {
    slug: "sdss-dr18",
    name: "SDSS DR18",
    shortName: "SDSS",
    sources: "2.3M spectra",
    anomalies: 77905,
    anomalyRate: "3.4%",
    qcStatus: "caution",
    qcNote: "Transfer-learning from DESI. Scores up to 10¹¹ indicate domain shift — flags SDSS-specific spectral types as 'anomalous relative to DESI'.",
    description: "Sloan Digital Sky Survey Data Release 18. Transfer-learning run using DESI-trained autoencoder. Higher anomaly rate reflects domain shift, not necessarily more real anomalies.",
    wavelength: "Optical spectroscopy (3800-9200 Å)",
    cost: "~$10",
    runtime: "~2.8h",
    pipeline: "DESI BigAE transfer (no retraining)",
    paperRefs: ["Paper 3 — cross-survey validation"],
    figures: ["SDSS score distribution", "SDSS × DESI cross-match"],
    keyFindings: [
      "77,905 anomalies from 2.3M spectra (3.4%)",
      "14 UMAP clusters identified",
      "4,117 high-z candidates, 585 QSO candidates",
      "3 SDSS × DESI cross-matches including z≈5.27 QSO",
      "Domain shift: scores span 5 to 1.9×10¹¹ (model confusion, not physics)",
    ],
    followUpTasks: [
      "Train SDSS-native autoencoder (not transfer from DESI)",
      "Classify top 1000 by spectral type",
      "Cross-match with LAMOST for independent validation",
      "Add as 2nd tracer population for f_NL multi-tracer",
    ],
    topAnomalies: [
      { rank: 1, ra: 0.0, dec: 0.0, score: 194532737024.0, type: "Score explosion (domain shift)" },
    ],
    connections: [
      { label: "DESI (source model)", href: "/surveys/desi-dr1" },
      { label: "LAMOST overlap", href: "/surveys/lamost-dr10" },
      { label: "Paper 3", href: "/papers/paper-3" },
    ],
  },
  {
    slug: "lamost-dr10",
    name: "LAMOST DR10",
    shortName: "LAMOST",
    sources: "11.4M spectra",
    anomalies: 44075,
    anomalyRate: "0.39%",
    qcStatus: "caution",
    qcNote: "98% blue-excess artifacts from training set bias. Needs LAMOST-native autoencoder.",
    description: "Large Sky Area Multi-Object Fiber Spectroscopic Telescope Data Release 10. Largest spectroscopic survey before DESI. Transfer-learning run exposed training set bias.",
    wavelength: "Optical spectroscopy (3700-9100 Å)",
    cost: "~$40",
    runtime: "~18.3h",
    pipeline: "DESI BigAE transfer",
    paperRefs: ["Paper 3 — multi-survey"],
    figures: ["LAMOST UMAP clusters"],
    keyFindings: [
      "44,075 anomalies from 11.4M spectra (0.39%)",
      "98% are blue-excess objects (training bias artifact)",
      "8 UMAP clusters, mostly single population",
      "Rankings are model-dependent — LAMOST-native model needed",
    ],
    followUpTasks: [
      "Train LAMOST-native autoencoder",
      "Add as 3rd tracer for f_NL multi-tracer",
      "Cross-match with SDSS and DESI",
    ],
    topAnomalies: [],
    connections: [
      { label: "DESI (source model)", href: "/surveys/desi-dr1" },
      { label: "SDSS overlap", href: "/surveys/sdss-dr18" },
      { label: "f_NL tracers", href: "/predictions/fnl" },
    ],
  },
  {
    slug: "erosita-dr1",
    name: "eROSITA DR1",
    shortName: "eROSITA",
    sources: "930K X-ray sources",
    anomalies: 9303,
    anomalyRate: "1%",
    qcStatus: "pass",
    qcNote: "73% novel (not in SIMBAD). Solid X-ray anomaly catalog.",
    description: "Extended Roentgen Survey with an Imaging Telescope Array first data release. First all-sky X-ray survey since the 1990s. X-ray sources are almost always astrophysically interesting.",
    wavelength: "X-ray (0.2-8 keV)",
    cost: "~$1",
    runtime: "~8 seconds",
    pipeline: "Tabular autoencoder on source properties",
    paperRefs: ["Paper 3 — X-ray anomalies"],
    figures: ["eROSITA sky map"],
    keyFindings: [
      "9,303 anomalies from 930K sources (1%)",
      "73% novel (not in SIMBAD)",
      "Fast processing (8 seconds) due to tabular data",
    ],
    followUpTasks: [
      "eROSITA × DESI cross-match (X-ray × optical)",
      "eROSITA × NEOWISE cross-match (X-ray × IR — AGN hunting)",
      "Classify X-ray anomalies by hardness ratio",
    ],
    topAnomalies: [],
    connections: [
      { label: "DESI optical", href: "/surveys/desi-dr1" },
      { label: "NEOWISE IR", href: "/surveys/neowise" },
      { label: "Multi-messenger", href: "/predictions/fnl" },
    ],
  },
  {
    slug: "planck-cmb",
    name: "Planck CMB",
    shortName: "Planck",
    sources: "20K patches",
    anomalies: 193,
    anomalyRate: "1%",
    qcStatus: "pass",
    qcNote: "v2 re-run with galactic mask: QC PASS. val_loss=0.138 (was 0.831). Anomalies now at mid-sky, not galactic poles.",
    description: "Planck 2018 CMB temperature map, analyzed as image patches. V1 failed QC (galactic contamination). V2 applies GAL080 galactic mask before patch extraction.",
    wavelength: "Microwave (30-857 GHz)",
    cost: "~$1",
    runtime: "~3 min",
    pipeline: "Patch autoencoder with galactic mask",
    paperRefs: ["Paper 3 — CMB anomalies", "Paper 1 — bounce predictions"],
    figures: ["Planck anomaly patches"],
    keyFindings: [
      "v2: 193 anomalies from 19,296 masked patches",
      "val_loss=0.138 (v1 was 0.831 without mask)",
      "Top anomaly: RA=208.5°, Dec=-21.2° (mid-sky, not poles)",
      "Galactic mask successfully eliminated contamination",
    ],
    followUpTasks: [
      "Cross-match with ACT anomalies (after ACT re-run)",
      "Check correlation with known CMB Cold Spot",
      "Multipole-by-multipole analysis",
      "Birefringence measurement with NaMaster",
    ],
    topAnomalies: [
      { rank: 1, ra: 208.5, dec: -21.2, score: 63.0 },
      { rank: 2, ra: 210.1, dec: -21.1, score: 42.3 },
      { rank: 3, ra: 279.7, dec: -33.2, score: 15.3 },
    ],
    connections: [
      { label: "ACT DR6", href: "/surveys/act-dr6" },
      { label: "Birefringence", href: "/predictions/birefringence" },
      { label: "Paper 1", href: "/papers/paper-1" },
    ],
  },
  {
    slug: "act-dr6",
    name: "ACT DR6",
    shortName: "ACT",
    sources: "20K patches",
    anomalies: 200,
    anomalyRate: "1%",
    qcStatus: "pass",
    qcNote: "v2 re-run with proper training: QC PASS. val_loss=0.610 (was 22,420). Early stopping at epoch 40.",
    description: "Atacama Cosmology Telescope Data Release 6. V1 failed QC (undertrained). V2 uses proper normalization, 100 epochs, and early stopping.",
    wavelength: "Microwave (90-220 GHz)",
    cost: "~$2",
    runtime: "~5 min",
    pipeline: "Patch autoencoder with per-patch normalization",
    paperRefs: ["Paper 3 — CMB anomalies"],
    figures: [],
    keyFindings: [
      "v2: 200 anomalies, val_loss=0.610 (v1 was 22,420)",
      "Trained 40 epochs before early stopping (patience=20)",
      "Top anomaly: RA=97°, Dec=43° (spread across sky)",
    ],
    followUpTasks: [
      "Cross-match with Planck anomalies (both now QC PASS)",
      "Birefringence measurement with NaMaster on ACT IQU maps",
      "Null tests (half-mission splits, frequency splits)",
    ],
    topAnomalies: [
      { rank: 1, ra: 97.0, dec: 43.0, score: 0.854 },
      { rank: 2, ra: 280.0, dec: 13.2, score: 0.851 },
    ],
    connections: [
      { label: "Planck CMB", href: "/surveys/planck-cmb" },
      { label: "Birefringence", href: "/predictions/birefringence" },
    ],
  },
  {
    slug: "neowise",
    name: "NEOWISE",
    shortName: "NEOWISE",
    sources: "44.3K sources",
    anomalies: 444,
    anomalyRate: "1%",
    qcStatus: "pass",
    qcNote: "v2 re-run with ecliptic masking: top anomaly at Dec=80° (high latitude). Ecliptic systematic eliminated.",
    description: "Wide-field Infrared Survey Explorer NEOWISE reactivation. V1 failed QC (all top anomalies at ecliptic plane). V2 excludes |ecliptic lat| < 10°.",
    wavelength: "Infrared (3.4-4.6 μm)",
    cost: "~$2",
    runtime: "~5 min",
    pipeline: "Variability autoencoder with ecliptic mask",
    paperRefs: ["Paper 3 — IR variability"],
    figures: [],
    keyFindings: [
      "v2: 444 anomalies from 44,341 sources (after ecliptic mask)",
      "Top anomaly at Dec=80° (high galactic latitude — real, not systematic)",
      "Variability features: Stetson J, chi-squared, amplitude",
    ],
    followUpTasks: [
      "Cross-match with ZTF alerts",
      "Cross-match with AGN catalogs (Milliquas)",
      "Full-sky run via AWS S3 Parquet (170B rows — Phase 9)",
    ],
    topAnomalies: [
      { rank: 1, ra: 271.8, dec: 80.2, score: 244413.0 },
    ],
    connections: [
      { label: "eROSITA (X-ray×IR)", href: "/surveys/erosita-dr1" },
      { label: "ZTF time-domain", href: "/surveys/desi-dr1" },
    ],
  },
  {
    slug: "gaia-dr3",
    name: "Gaia DR3",
    shortName: "Gaia",
    sources: "500K variables",
    anomalies: 5000,
    anomalyRate: "1%",
    qcStatus: "pass",
    qcNote: "v2 expanded from 50K to 500K sources. val_loss=0.004. 10x more anomalies than v1.",
    description: "ESA Gaia Data Release 3 variable star catalog. V1 was only 50K sources (too small). V2 expanded to 500K with proper period folding and 18 features.",
    wavelength: "Optical astrometry + photometry",
    cost: "~$1",
    runtime: "~3 min",
    pipeline: "Tabular autoencoder on variability features",
    paperRefs: ["Paper 3 — stellar anomalies"],
    figures: [],
    keyFindings: [
      "v2: 5,000 anomalies from 500K variables (10x expansion)",
      "val_loss=0.004 (excellent training)",
      "18 features including period, amplitude, Stetson J",
      "Full epoch photometry run planned (1.8B sources — Phase 9)",
    ],
    followUpTasks: [
      "Cross-match with known variable star catalogs (AAVSO, GCVS)",
      "Dyson sphere search (Gaia × AllWISE IR excess)",
      "Full 1.8B epoch photometry run (Phase 9)",
    ],
    topAnomalies: [],
    connections: [
      { label: "Dyson sphere search", href: "/predictions/fnl" },
      { label: "AllWISE IR", href: "/surveys/neowise" },
    ],
  },
];

export function getSurveyBySlug(slug: string): Survey | undefined {
  return surveys.find((s) => s.slug === slug);
}
