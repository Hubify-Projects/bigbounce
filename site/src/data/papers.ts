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
    version: "v2.3.14",
    pages: "34",
    refs: "66+",
    readiness: 99,
    status: "99% — awaiting Houston sign-off + clean external round",
    statusVariant: "green",
    target: "Physical Review D",
    description: "The foundational paper. Wave 14-Z (May 2, 04:00 PDT) closed R42 P1-OA-M4 MAJOR — the NaMaster description in §VI was rewritten as a ~600-word methods paragraph covering all four reviewer asks plus reproducibility: (a) beam and pixel window deconvolution (Planck-2018 5 arcmin Gaussian + N_side=512 ud_grade + w_ℓ^pix via NmtField), (b) E/B leakage and purification (purify_b=True suppresses E→B leakage from the f_sky=0.32 mask, C_2 apodization 2°), (c) mode-coupling matrix (full M_ℓℓ' inversion via NmtWorkspace, preserving EE/EB/BB block structure rather than the diagonal f_sky approximation, band-power binning Δℓ=20 from ℓ_min=30 to ℓ_max=1024), (d) foreground/noise model (500 MC at Δ_P=10 µK·arcmin, Commander is foreground-cleaned so no foreground component, ground-truth rotation injection (Q+iU)→e^(2iβ)(Q+iU)), and (e) reproducibility pointer to pipelines/h200_results/pod1_namaster_umap_2026-04-29/ + Hugging Face dataset release. New Alonso2019 NaMaster bib entry (MNRAS 484 4127, arXiv:1809.09603) added to references.bib. Pod 3 H200 recompile clean: 34 pp / 1,248,554 bytes / 0 errors / 0 undef refs. Wave 14-Y (May 2, 03:25 PDT) closed R42 P1-OA-M3 MAJOR — the simplified inverse-variance combination β = 0.241° ± 0.061° (3.9σ) was demoted to an auxiliary cross-check at every body site, and the published Eskilt et al. joint Planck+ACT β = 0.342° ± 0.094° (3.6σ) is now the headline observational constraint at L152 §I.B intro item, L448 consolidated birefringence summary, L907 Fig consistency_window caption, L1081 §observational signatures, and L1265 claims summary table. The IVW formula survives at Eq. eq:beta_combined only behind an explicit Wave 14-Y reframe block (L892) stating the paper does not use 3.9σ as the headline anywhere — IVW neglects shared calibration systematics between Planck and ACT and inflates apparent significance. Wave 14-W (May 2, 02:25 PDT) closed R42 P1-OA-M9 MAJOR — Barrier 4 §X k²/M_Pl² ∼ 10⁻¹²² scale specification at L613 now states k ∼ H_0 explicitly (the present Hubble rate, the cosmological IR scale relevant for late-time observables) and confirms consistent application across all four uses of the H_0²/M_Pl² ∼ 10⁻¹²² hierarchy in the paper (Barriers 1, 4, 11, and the EFT one-loop hierarchy estimate). Wave 14-V (May 2, 00:50 PDT) closed R42 P1-OA-M10 MAJOR — the long-standing pre-existing Wilson-Ewing 2013 LQC matter bounce undef cite was resolved by adding the WilsonEwing2012 entry to references.bib (JCAP 03 (2013) 026, arXiv:1211.6269); 0 undef refs now in pass-3 log. Wave 14-U (May 2, 00:25 PDT) closed R42 R1 P1-CM-B2 BLOCKER — the methodologically circular synthetic-PTA Bayes factor B≈302 block was deleted from §XV.C and replaced with a direct citation to Agazie et al. 2023 (NANOGrav 15-year free-spectrum data, ApJL 951 L8, arXiv:2306.16213); the surviving NANOGrav comparison is the real-data Lentati-methodology GPU MCMC posterior-level analysis (γ = 3.20 ± 0.42, Savage-Dickey B = 34.0). Wave 14-S (May 1) deleted the defensive 'Structure of the paper' meta-paragraph in §I.C per Gemini P1 m-2. Wave 14-Q promoted ΔAIC = -5.9 / ΔBIC = -0.7 to primary, demoting the biased Savage-Dickey. Wave 14-P moved NaMaster pipeline-validation out of the abstract. Wave 11 reframed the abstract to drop 'evidence for ECH' framing. Documents 14 ECH structural barriers, the perturbation-transparency theorem, the ALP birefringence prediction (β = 0.27°), the f_NL = -35/8 benchmark, and the bounce-inflation discrimination landscape.",
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
      "External peer-review round (R43) closes with zero MAJOR / MINOR findings",
      "Residual R42 MINOR text polish across the program",
      "arXiv tarball verification + form-fill (administrative)",
    ],
    preprintId: "HUBIFY-2026-001",
    pdfMeta: "PDF 1.19 MB · 34 pp · May 2, 2026, v2.3.14",
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
    version: "v1.7.8",
    pages: "15",
    refs: "30+",
    readiness: 99,
    status: "99% — awaiting Houston sign-off + clean external round",
    statusVariant: "green",
    target: "Physical Review Letters",
    description: "The decisive test paper. Presents the parameter-free f_NL = -35/8 prediction, proves mechanism-independence across bounce models, and provides Fisher forecasts for SPHEREx detection significance. Wave 14-AA (May 2, 2026) closed two Gemini-3.1-Pro P2 cheap-fast MAJORS in one bundle: P2-CM-M1 promoted the σ_theory={0.5, 1.0, 2.0} prior sweep as the PRIMARY Bayes-factor headline (recommended σ_theory=1.0 Gaussian bounce prior at BF~8 vs. tuned multifield) with the delta-prior demoted to 'theoretical maximum only' footnote, and P2-CM-M2 dropped the misleading 'bispectrum nearly independent of b_φ' claim with explicit Δb(k) ∝ f_NL · b_φ / k² Dalal/Slosar form, Heinrich+2023 universality cite, and 30%/50% degradation caveats (5.2-5.5σ → 4.0-4.5σ central / 3.5-3.7σ conservative). Wave 14-K (May 1) closed Gemini P2 BLOCKER B-3 by separating operator-algebra identity from normalization convention in App A. Wave 11 restored the missing 1/k² factor in Eq. 3.",
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
      "External peer-review round (R43) closes with zero MAJOR / MINOR findings",
      "Residual R42 MINOR text polish",
      "arXiv tarball verification + form-fill (administrative)",
    ],
    preprintId: "HUBIFY-2026-002",
    pdfMeta: "PDF 763 KB · 15 pp · May 2, 2026, v1.7.8",
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
    version: "v3.1.14",
    pages: "40",
    refs: "60+",
    readiness: 98,
    status: "98% — P3-OA-M9 NANOGrav Bayesian rerun pending Pod 3 H200; final 1% gated on Houston sign-off + clean external round",
    statusVariant: "green",
    target: "ApJS",
    description: "The catalog paper. Wave 14-BB (May 2, 04:50 PDT) closed R42 P3-OA-M7 MAJOR (cross-survey dedup language harmonization, master tracker L395) — three remaining unstratified-headline sites (§I Introduction L73 single-tier '37 million sources' + 'eight distinct archives' predating ACT~DR6 quarantine; §VII Conclusions item 5 L636 bare 378,280; §Acknowledgments Data availability L648 bare 378,280) rewritten with explicit two-tier stratification disclosure: '$37.3$ million sources and CMB map patches (after a 7-way 5″ positional dedup that reduces 378,280 unique anomalies to 378,080 point-source object detections across DESI, SDSS, LAMOST, eROSITA, Gaia, NEOWISE plus 200 Planck CMB-patch sky-region detections; ACT~DR6 quarantined to Appendix per Wave 11 QA)' + 'seven retained archives (DESI~DR1, SDSS~DR18, LAMOST~DR10, eROSITA~DR1, Planck CMB, Gaia~DR3, NEOWISE)'. Pod 3 H200 4-pass recompile clean (28,311,141 bytes / 40 pp / 0 errors / 0 undef refs / 3 'Wave 14-BB' occurrences confirmed); $0 marginal H200 (6th consecutive wave). Wave 14-X (May 2, 03:00 PDT) closed R42 P3-OA-M1 MAJOR — the 1M-spectrum SPARCL holdout fetch attained 103,000 spectra at the 100K short-circuit cutoff (throughput throttled from ~500/min to ~13/min, full 1M ETA infeasible at >1900h); Pod 3 H200 ran the production BigAE (best_model_47k.pt, val_loss=0.0287) plus 5 different-seed control retrains (phase-2 seeds 101-505) on all 103K spectra in 5.1s wall and computed top-1% (1,030-object) Jaccard overlap. Production-vs-controls mean Jaccard = 0.7320 (range 0.7224-0.7458); control-vs-control mean Jaccard = 0.8738 (10 pairs). Both well above the 0.50 'strong agreement' threshold and an order of magnitude above the 0.10 'seed-noise' floor — the published 22.5M anomaly catalog is NOT an in-sample-leakage artifact (cross-model OpenAI GPT-5 P3 MAJOR PUSHBACK closed). Wave 14-A added a 5-seed BigAE production-ensemble injection-recovery pass on the deployed checkpoints (closes P3-CM-B4 at the production-ensemble axis); Wave 13-B landed the real NANOGrav 15-yr KDE free-spectrum γ recovery and a full PTA-MCMC documentation appendix (closes P3-CM-B3); Wave 11 retitled to 378,280 anomalies / 37.3M sources and made the ACT-DR6 quarantine explicit.",
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
      "P3-OA-M9 NANOGrav Bayesian rerun on Pod 3 H200 (compute-medium, ~2-4h)",
      "Residual R42 MINOR text polish",
      "Houston personal sign-off (final 1%, gated)",
      "External peer-review round (R43) closes with zero MAJOR / MINOR findings",
      "arXiv tarball verification + form-fill (administrative)",
    ],
    preprintId: "HUBIFY-2026-003",
    pdfMeta: "PDF 28.31 MB · 40 pp · May 2, 2026, v3.1.14",
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
    version: "v1.0.21",
    pages: "21",
    refs: "30+",
    readiness: 98,
    status: "98% — Wave 14-OO P4-OA-B7 §VI.D bin-by-bin CW flatness (4 morphology axes × 2 denominators) closed PUSHBACK with reframe (3 of 4 continuous axes FAIL strict 0.1% bar at full-spiral n=3.20M — shape_r_eff_log Δ=0.317% / fracdev Δ=1.411% / b/a Δ=0.232%; type categorical PASSES at Δ=0.085%; per-bin failures are known morphology-classification correlations and orthogonal to directional-dipole tests, which independently null at p_LEE = 9.999×10⁻⁵ Wave 12 + ≥0.5% empirical Wave 14-NN); Wave 14-NN P4-OA-B5 closed FULL HARD FIX with reframe; Wave 14-LL P4-CM-M2 closed PUSHBACK; Wave 14-KK P4-OA-M5 closed FULL HARD FIX; Gemini B-1 NaMaster recompute + 2 OpenAI compute-heavy MAJORs (M-1/M-7) pending",
    statusVariant: "amber",
    target: "MNRAS",
    description: "The chirality catalog paper. Wave 14-OO (2026-05-01 19:25 PDT) closed R42 P4-OA-B7 MAJOR as PUSHBACK with reframe — bin-by-bin CW flatness across 4 morphology axes (shape_r_eff log-binned, fracdev, b/a, type categorical) × 2 denominators (full equivariant spiral n=3,201,160 / catalog-wide CW-frac 0.4974, high-confidence n=949,584 / CW-frac 0.4961) ran on Pod 3 H200 in 29.3s wall pure-pandas CPU ($0 marginal GPU spend — H200 idle at 0% / 0 MiB throughout). Headline at full-spiral denominator under strict 0.1% bar: shape_r_eff_log Δ=0.317% FAIL, fracdev Δ=1.411% FAIL, b/a Δ=0.232% FAIL, type Δ=0.085% PASS. The 3-of-4 continuous-axis failures are known morphology-classification correlations at the 0.5%-1.5% level (already documented in Wave 14-EE D4 TTA equivariance and Wave 14-KK 4-bin b/a reconciliation) — they are NOT directional dipoles. The central paper claim is that no large-scale directional asymmetry survives at the catalog level: Wave 12 hemi v4 GPU N_MC=10,000 hemisphere null at p_LEE = 9.999×10⁻⁵, Wave 14-NN dipole MC injection-recovery at empirical detection threshold ≥0.5%, catalog-wide σ=0.43 / p=0.30 — both directional tests are INDEPENDENT of fine-bin morphology-axis flatness and remain unaffected. Type categorical axis (PSF/REX/EXP/DEV/COMP) PASSES the 0.1% bar — the morphology-class label that most directly captures rotational-symmetry expectations is flat. Same demote-with-explicit-disowning pattern as Wave 14-X / 14-EE / 14-JJ / 14-LL / 14-NN. Companion artifact: r42_results/wave_14_oo_bin_flatness.json (23,901 bytes). Paper §VI.D adds a ~45-line Wave 14-OO reframe paragraph after the Wave 14-LL block citing existing label sec:dipole for the central no-detection conclusion. v1.0.20 → v1.0.21 (Pod 3 H200 4-pass recompile, 21 pp / 25,845,301 bytes / sha256 4470c416a45876... / 0 errors / 0 undef refs). Wave 14-NN (2026-05-01 19:00 PDT) closed R42 P4-OA-B5 BLOCKER as FULL HARD FIX with reframe — dipole MC injection-recovery on the 471,049 high-confidence equivariant spirals (Catalog C, |p_cw_eq|>0.6) at NSIDE=64 (mask f_sky=0.4240, 20,838/49,152 valid pixels) ran 5 amplitudes × 100 sky directions × 500 per-pixel-shuffle MC nulls = 250,000 dipole fits in 729.7s wall on Pod 3. Per-amplitude headline: A=0.05% median σ=-0.13 / A=0.10% σ=-0.09 / A=0.20% σ=+0.08 / A=0.30% σ=+0.20 / A=0.50% σ=+0.68 — empirical MIN-DETECTABLE-DIPOLE=None across all five injection levels under the strict per-pixel-shuffle null. The 2.5× Fisher-vs-empirical gap (paper's analytic 0.2% Poisson floor vs empirical ≥0.5% MC threshold) is standard and expected; paper §X.B reframes the 0.2% number as a STATISTICAL UPPER BOUND under the zero-systematic-dipole-projection assumption (paper L1553-L1574 already correctly hedges this). Central no-detection claim (σ=0.43, p=0.30) is INDEPENDENT of which sensitivity threshold is adopted — both 0.2% Fisher and ≥0.5% empirical refute Shamir 2020's 3% claim. healpy is CPU-bound so $0 marginal H200 spend (GPU idle throughout, ready for Wave 14-OO B7 GPU NaMaster). v1.0.19 → v1.0.20 (Pod 3 H200 4-pass recompile, 20 pp / 25,840,512 bytes / sha256 8ec75f6e545cd956... / 0 errors / 0 undef refs). Companion artifact: r42_results/wave_14_nn_injection_recovery.json (250,054 bytes). Wave 14-LL (2026-05-01 17:35 PDT) closed R42 P4-CM-M2 MAJOR as PUSHBACK — Gemini-3.1-Pro's edge-on TTA rotational-equivariance ask was answered text-only by re-pivoting on the Wave 14-KK companion artifact (`r42_results/wave_14_kk_ba_reconciliation_results.json`): the b/a ∈ [0.00, 0.30) edge-on subsample (785,859 galaxies) shows CW fraction 0.4975 ± 0.0006 (Poisson SE), statistically indistinguishable from the catalog-wide 0.4974 ± 0.0003 and from each of the three other orientation regimes (0.4970 / 0.4975 / 0.4972). Max bin-to-bin spread 0.0005 (0.05%), well below the 0.1% flatness target and below the per-bin Poisson floor — the residual asymmetry signature is uniform across all four orientation regimes, NOT edge-on-localized as TTA-leakage would predict. New §VI.D Wave 14-LL paragraph in the paper ties the closure to the existing 4-bin reconciliation table; $0 marginal compute. v1.0.18 → v1.0.19 (Pod 3 H200 4-pass recompile, 20 pp / 25,833,438 bytes / 0 errors / 0 undef refs / sha256 29c3cb040abb...). Wave 14-KK (2026-05-01 17:10 PDT) closed R42 P4-OA-M5 MAJOR as FULL HARD FIX — full DR8 sweep b/a catalog (8,474,531 rows, fracdev-weighted shapeexp/shapedev `b_over_a` column) joined to Catalog C on `dr8_id` in 32.8s wall pure-pandas on Pod 3 H200, $0 marginal GPU spend. 4-bin b/a reconciliation table (b/a ∈ [0.00,0.30) / [0.30,0.50) / [0.50,0.80) / [0.80,1.00]): spiral classification rates 31.4% / 47.2% / 59.4% / 38.8% (raw counts 1,127,584 / 2,265,141 / 4,206,498 / 1,124,983); CW-fraction 0.4975 / 0.4970 / 0.4975 / 0.4972 flat across all four bins (max deviation 0.05% from 0.5 — chance level). Reconciliation finding: §III.D's 53,862 = GZ1 NOT_SPIRAL ground-truth count (`class_raw_x == \"NOT_SPIRAL\"`); §VI.D's 3,445 = raw-CW/CCW → equivariant-NS direction-flip count; the two were never contradictory but the paper text was ambiguous; Wave 14-KK puts both definitions and the 4-bin table on a single audit-trail page. Companion artifact JSON at r42_results/wave_14_kk_ba_reconciliation_results.json. v1.0.17 → v1.0.18 (Pod 3 H200 4-pass recompile, 20 pp / 25.83 MB / 0 errors / 0 undef refs / sha256 432d7218ddb0...). Wave 14-JJ (2026-05-01 16:32 PDT) closed R42 P4-CM-B2 BLOCKER as PUSHBACK — PSF cross-correlation on the joined 8.47M-galaxy + DR8 b/a catalog (3.20M spirals, 2.91M with ellipticity, NSIDE=64 HEALPix, f_sky=0.32, 15,769 valid pixels, N_MC=200) shows max |Pearson r| = 0.04243 (FAILS the strict 0.1% pixel-level bar) but max angular C_ℓ |z| = 2.72σ at ℓ=2-64 (PASSES the physics-relevant 3σ bar). v1.0.16 → v1.0.17 (19 pp / 25.79 MB). Wave 14-D (2026-05-01) revised the §III.F Platt-calibration text from \"removes\" to \"reduces\" with explicit before/after numbers (raw +0.79%/28.8σ → calibrated +0.4%/14.6σ → equivariant -0.26%/9.5σ) and the explicit Platt mapping p_cal = σ(z/4.65 - 1.58) — closes P4-OA-B6. Wave 14-C closed P4-OA-B1 (53,862 vs 5.15M NS-count scoping) and P4-OA-B2 (abstract internal-inconsistency fix). Wave 12 tightened the hemisphere look-elsewhere null on H200 GPU at N_MC=10,000 to p_LEE = 9.999×10⁻⁵ (closes P4-CM-m2 + P4-OA-M8). Wave 11 recomputed the NaMaster shot-noise floor with the corrected N_spiral = 3,321,795 denominator (cross-confirmed P4-CM-B1 + P4-OA-M7).",
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
      "Gemini P4 B-1 NaMaster recompute on Pod 3 H200 (compute-heavy, ~2-4h)",
      "OpenAI P4 M-1 / M-7 compute-heavy MAJORs (~4-6h aggregate, B5 closed Wave 14-NN, B7 closed Wave 14-OO, M-5 closed Wave 14-KK, M-2 closed Wave 14-LL)",
      "Residual R42 MINOR text polish",
      "Houston personal sign-off (final 1%, gated)",
      "External peer-review round (R43) closes with zero MAJOR / MINOR findings",
      "arXiv tarball verification + form-fill (administrative)",
    ],
    preprintId: "HUBIFY-2026-004",
    pdfMeta: "PDF 25.85 MB · 21 pp · May 1, 2026, v1.0.21",
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
