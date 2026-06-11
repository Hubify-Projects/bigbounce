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
      "Central 9.4% multi-tracer f_NL forecast (consistent with no improvement at <1σ)",
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
    qcNote: "Cross-transfer baseline (77,905 at S>=0.1060). Path-C native retrain (gate-PASS val_loss=0.0311) yields only 12 sources at S>5 — a ~6500x reduction confirming domain shift. Use 77,905 for cross-survey rate comparison; use 12 for purity; use 19,253 (top-1% native, S>=0.2051) for SIMBAD novelty pool.",
    description: "Sloan Digital Sky Survey Data Release 18. Three-threshold disclosure: 77,905 (cross-transfer top-1% continuity baseline), 19,253 (native top-1% S>=0.2051), 12 (native S>5 field-defining threshold). Domain shift confirmed: DESI-trained autoencoder sees SDSS-specific spectral types (ultra-cool dwarfs, M7/T2/L3) as anomalous.",
    wavelength: "Optical spectroscopy (3800-9200 Å)",
    cost: "~$10",
    runtime: "~2.8h",
    pipeline: "DESI BigAE transfer (cross-transfer baseline) + native BigAE retrain (val_loss=0.0311)",
    paperRefs: ["Paper 3 — cross-survey validation"],
    figures: ["SDSS score distribution", "SDSS × DESI cross-match"],
    keyFindings: [
      "77,905 cross-transfer anomalies (domain-shift inflation vs DESI)",
      "Path-C native retrain: only 12 sources at S>5 (~6500x reduction)",
      "Native top-1% (19,253 at S>=0.2051) is SIMBAD novelty pool",
      "Ultra-cool dwarfs (M7, T2, L3) dominate cross-transfer catalog",
      "3 SDSS × DESI 5-arcsec positional coincidences",
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
    qcNote: "~56% B-dominant cross-transfer (empirical; the 98% figure was a synthetic schematic not a measurement). Native retrain reduces anomaly count 21.4x (43,915 -> 2,054 at S>5). Path-C native model in progress.",
    description: "Large Sky Area Multi-Object Fiber Spectroscopic Telescope Data Release 10. Largest spectroscopic survey before DESI. Transfer-learning run exposed training set bias.",
    wavelength: "Optical spectroscopy (3700-9100 Å)",
    cost: "~$40",
    runtime: "~18.3h",
    pipeline: "DESI BigAE transfer",
    paperRefs: ["Paper 3 — multi-survey"],
    figures: ["LAMOST UMAP clusters"],
    keyFindings: [
      "44,075 anomalies from 11.4M spectra (0.39%)",
      "~56% B-dominant (empirical cross-transfer; 98% was synthetic schematic, not measured)",
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
    anomalies: 298,
    anomalyRate: "0.03%",
    qcStatus: "pass",
    qcNote: "298 canonical sources (score-knee top-cut S>0.259, IsolationForest). 73% novel (not in SIMBAD). Note: 9,303 is the top-1% IF cross-validation reference pool, not the published catalog headline.",
    description: "Extended Roentgen Survey with an Imaging Telescope Array first data release. First all-sky X-ray survey since the 1990s. Published catalog: 298 sources at S>0.259 (IsolationForest score knee, ~top 0.03%). LMC/Galactic-plane concentration.",
    wavelength: "X-ray (0.2-8 keV)",
    cost: "~$1",
    runtime: "~8 seconds",
    pipeline: "16-dim autoencoder latent + IsolationForest (100 trees)",
    paperRefs: ["Paper 3 — X-ray anomalies"],
    figures: ["eROSITA sky map"],
    keyFindings: [
      "298 anomalies from 930K sources (0.03% canonical top-cut)",
      "73% novel (not in SIMBAD)",
      "203 SIMBAD-unmatched X-ray sources near LMC (not independently confirmed discoveries)",
      "Cross-validation stability 81.5% — highest of all Path-C surveys",
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
    anomalies: 200,
    anomalyRate: "1%",
    qcStatus: "pass",
    qcNote: "Path-C native retrain: QC PASS. val_loss=0.4437. 500/500=100% injection-recovery at 5sigma. Note: 200 patches are CMB sky-region detections, not point sources — exclude from cross-matching against object catalogs.",
    description: "Planck 2018 CMB temperature + polarization map, analyzed as image patches. Native convolutional autoencoder with GAL080 galactic mask (|b|>=20 deg). Sky-region tier of the Path-C catalog (not point sources).",
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
    anomalies: 0,
    anomalyRate: "—",
    qcStatus: "fail",
    qcNote: "FORMALLY QUARANTINED (Paper 3 Appendix). Cross-transfer val_loss=22,420 (~7x10^4 above the 0.30 gate). Injection-recovery <1% at 5sigma. No native retrain executed. Excluded from all headline numbers.",
    description: "Atacama Cosmology Telescope Data Release 6. Formally quarantined under Path-C protocol: cross-transfer autoencoder gate-FAILED both criteria (val_loss 22,420 vs 0.30 threshold; <1% injection-recovery at 5sigma). No native retrain has been run. The 200-patch cross-transfer block is preserved in Paper 3 Appendix as a methodological lessons-learned artifact only.",
    wavelength: "Microwave (90-220 GHz)",
    cost: "~$2",
    runtime: "~5 min",
    pipeline: "Cross-transfer (quarantined — no native retrain)",
    paperRefs: ["Paper 3 — Appendix (quarantined, lessons-learned only)"],
    figures: [],
    keyFindings: [
      "QUARANTINED: cross-transfer val_loss=22,420 (gate threshold: 0.30)",
      "Injection-recovery <1% at 5sigma (gate threshold: 50%)",
      "Contributes 0 objects to Path-C catalog headline",
      "200-patch cross-transfer block documented in Appendix for audit only",
    ],
    followUpTasks: [
      "Native retrain (future work — requires ACT IQU maps and custom patch pipeline)",
      "Birefringence measurement with NaMaster on ACT IQU maps (separate from anomaly catalog)",
    ],
    topAnomalies: [],
    connections: [
      { label: "Planck CMB", href: "/surveys/planck-cmb" },
      { label: "Birefringence", href: "/predictions/birefringence" },
    ],
  },
  {
    slug: "neowise",
    name: "NEOWISE",
    shortName: "NEOWISE",
    sources: "43.5K sources",
    anomalies: 419,
    anomalyRate: "0.96%",
    qcStatus: "pass",
    qcNote: "Path-C masked: 419/436 retained after |b_ecl|<80deg cut. 2.6x polar-cap excess vs uniform-null. Ecliptic systematic eliminated.",
    description: "Wide-field Infrared Survey Explorer NEOWISE reactivation. Path-C applies ecliptic-pole mask (|b_ecl|<80 deg), retaining 419/436 sources (96.1%). Mask injection-recovery: 100% specificity and sensitivity.",
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
    sources: "50K variables",
    anomalies: 500,
    anomalyRate: "1%",
    qcStatus: "caution",
    qcNote: "Exploratory tier. Cross-validation stability only 41% (training-sample-conditioned selection). 10x expansion to 500K run internally for CV diagnostics; published catalog uses original 50K scope. Dedicated Gaia-optimized detector needed.",
    description: "ESA Gaia Data Release 3 variable star catalog. 50K-source subset with top-1% IsolationForest on 22-dimensional variability features. Cross-validation stability (41%) indicates the selection is training-sample-conditioned; treat as exploratory, not catalog-grade.",
    wavelength: "Optical astrometry + photometry",
    cost: "~$1",
    runtime: "~3 min",
    pipeline: "IsolationForest (100 trees, 22-dim variability features)",
    paperRefs: ["Paper 3 — stellar anomalies"],
    figures: [],
    keyFindings: [
      "500 anomalies from 50K sources (1% top-cut)",
      "Cross-validation stability 41% — training-sample-conditioned",
      "22 features including period, amplitude, Stetson J, chi-squared",
      "Extreme variable stars, high proper motion objects",
      "Exploratory tier only — dedicated Gaia-optimized detector needed",
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
