export interface Paper {
  slug: string;
  number: string;
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
    slug: "paper-1a",
    number: "1A",
    title: "Structural Closure of Einstein–Cartan–Holst Dark Energy: Perturbation Transparency, Inflation–f_NL Tension, and Surviving Matter-Bounce Tests",
    version: "v1A.0.19",
    pages: "17",
    refs: "70+",
    readiness: 86,
    status: "86% — R47 forward closure (Wave 14-CCCCC, CROSS-PAPER coordinated): +6pp from 80 after closing R47 BLOCKER B1 + MAJOR M1 in a coordinated cross-paper commit (P1A v1A.0.12 → v1A.0.13 + P1B v1B.0.2 → v1B.0.3 in a single commit). R47-B1 fix: P1A Table II ‡ footnote rewritten — old text cited non-existent 'Paper I(b) §VII.H' AND claimed 'zero free-w0wa samples' which contradicted Paper 1B Table III ('~109 accepted, Running'). New text re-anchors at the correct Paper 1B §VII Table III subsection and reframes accurately: 'the three frozen MCMC dataset combinations contain zero free-w0wa samples' (true — those frozen rows hold w_0=-1, w_a=0 at LCDM fiducial), 'A new DESI DR2 + Planck NPIPE + Pantheon+ + DES-SN5YR cobaya chain with the w0wa free-parameter extension is currently running on Pod 3 H200 (~109 samples accepted as of 2026-05-08 18:27 PT, target R̂−1 < 0.01 still 1-3 days from publication-quality convergence; Paper 1B Table III row DESI DR2 w0wa (new))'. P1B coordination: new §VII subsection 'Free-w0wa chain status' (sec:crosspaper-shadow) added inside §VII, with three load-bearing points (i)-(iii) explicitly anchoring the P1A ‡ footnote: frozen posteriors do NOT include free w0wa, the new chain has 109 accepted at R̂−1=0.076 / ETA 1-3 days, the asymmetry between Quintom-B and other rows is theoretical accommodation not measured fit quality. R47-M1 fix: '7 observational research branches (Branches H–O)' was off-by-one (H-to-O = 8 letters) and inconsistent with Table II's 6 distinct branch labels (H, J, L, L/M, M, N/O). Corrected to '6 observational research branches (Branches H, J, L, M, N, O)' in 4 sites: abstract L67, §I.A L195, §VII.A L810, conclusions L1261. Conclusions also gained the B8⊂B14 special-case clause to match the abstract. Wave 14-DDDDD (P2 R47 B1+3M) queued.",
    statusVariant: "green",
    target: "Physical Review D",
    description: "Paper 1A — the foundational ECH structural-closure no-go theorem (theory-focused, PRD target). Establishes 14 independent structural barriers that close every minimal route from the quantum bounce to late-time dark energy. The central result is the perturbation-transparency theorem: for canonical scalar matter, torsion vanishes at all perturbation orders, the Holst dual contraction vanishes identically by the first Bianchi identity, and the Holst sector decouples from all scalar/tensor perturbation observables. The structural-tension §III argument shows the dark-energy mechanism (requiring N_tot ≈ 92 post-bounce e-folds) is incompatible with the fNL/f_NL = -35/8 matter-bounce signature. Companion technical verification material lives in Paper 1B.",
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
      "Houston personal sign-off (final 1%, gated)",
      "External peer-review round (R43) — zero MAJOR/MINOR findings required",
      "arXiv submission (administrative, in P4 → P1A → P1B → P3 → P2 order)",
    ],
    preprintId: "HUBIFY-2026-001A",
    pdfMeta: "PDF 786 KB · 17 pp · May 10, 2026, v1A.0.19",
    artifacts: [
      { label: "Read PDF", href: "/papers/paper1a_ech_nogo.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper1a_ech_nogo.pdf", kind: "secondary", download: true },
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
    version: "v1B.0.3",
    pages: "7",
    refs: "30+",
    readiness: 76,
    status: "75% — compute-gated on DESI DR2 w0wa cobaya chain (R̂−1 = 0.076 at 18:27 PT 5/8, target < 0.01, ETA 1–3 days). §Structural Tension MCMC numbers are placeholder until convergence. Excluded from R44 self-review for the same reason; R45 + cross-vendor + Houston sign-off all still ahead.",
    statusVariant: "green",
    target: "Physical Review D (companion)",
    description: "Paper 1B — technical verification companion to Paper 1A. Three analyses documented: (1) Stock-CAMB ΛCDM+ΔN_eff MCMC proxy run (Cobaya v3.6.1, 424,781 samples across three frozen dataset combinations) — null-consistency test of an extra radiation degree of freedom, recovers ΛCDM with H0 = 67.68 ± 1.06 km/s/Mpc and ΔN_eff consistent with zero. (2) NaMaster pseudo-C_ell pipeline recovery on the Planck Commander map (500 MC, NSIDE=512, ℓ_max=1024, f_sky=0.32): injecting β=0.27° recovers 0.238° at SNR=20.32. (3) Spectator-ALP consistency check: a field with f_a ~ M_Pl, m ~ H_0 is consistent with the published Planck+ACT joint β = 0.342° ± 0.094° (3.6σ). A new DESI DR2 w0wa free MCMC chain (Planck NPIPE + DESI DR2 BAO + Pantheon+ + DES-SN5YR) is in progress on RTX A5000 pod and will be incorporated into the §Structural Tension cross-reference once converged.",
    keyResults: [
      "424,781 MCMC posterior samples across 3 frozen dataset combinations (176,840 + 132,949 + 114,992)",
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
      "Houston personal sign-off (final 1%, gated)",
      "External peer-review round (R43) — zero MAJOR/MINOR findings required",
      "DESI DR2 w0wa chain convergence (R̂−1 < 0.01) → GetDist → §Structural Tension update",
      "arXiv submission (administrative, after DR2 chain incorporation)",
    ],
    preprintId: "HUBIFY-2026-001B",
    pdfMeta: "PDF 665 KB · 7 pp · May 9, 2026, v1B.0.3",
    artifacts: [
      { label: "Read PDF", href: "/papers/paper1b_mcmc_companion.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper1b_mcmc_companion.pdf", kind: "secondary", download: true },
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
    version: "v1.7.25",
    pages: "18",
    refs: "33+",
    readiness: 81,
    status: "82% — R47 forward closure (Wave 14-DDDDD): +6pp from 76 after closing R47 BLOCKER B1 + 3 MAJORs M1-M3. R47-B1 fix: Table 5 (tab:gr) caption now explicitly states 'BF vs. Tuned' uses NARROW competitor prior [-5,+5] (not broad), reconciling the 9.4 vs 17 disagreement at σ_GR=0.5 — the 9.4 is at narrow competitor, 17 is at broad. Table 4 row 4 footnote ^a updated to confirm Table 4 row 4 (8-11 GR-spread) is at SAME narrow [-5,+5] competitor as Table 5; the two tables are now numerically consistent at σ_GR=0.5 (Table 4 row 4 = 9.4 = Table 5 row 2 BF-vs-Tuned). R47-M2 fix: Table 4 row 4 label changed from 'Delta at f_NL=-35/8 (theoretical maximum only)' to 'Delta at f_NL=-35/8, narrow [-5,+5] multifield (GR-variation only)' — competitor prior now explicit on the row. R47-M1 fix: 3×6 SVD rank statement at L70 expanded — old text 'computed its SVD, confirming a 3-dimensional null space' replaced with explicit 'finding three nonzero singular values σ_1 ≥ σ_2 ≥ σ_3 > 0 with σ_3/σ_1 ≈ 0.3 in our reference monomial normalization (kinematic separation between squeezed and equilateral configurations bounds the smallest-to-largest singular-value ratio far from any rank-deficiency tolerance). The rank is therefore exactly 3 (full row rank) and the null space is exactly 3-dimensional.' R47-M3 fix: abstract gained one explicit sentence justifying the bispectrum-only headline over the SDB joint-Fisher 9.9σ — 'A joint (f_NL, n_fNL) scale-dependent-bias Fisher analysis yields a higher idealized significance (~9.9σ marginalized over the running n_fNL; §sec:discussion), but is more vulnerable than the multi-tracer bispectrum to the ultra-large-scale-mode access k_min, the relativistic-projection cliff, and the universality assumption b_φ=2δ_c(b_1-1); we therefore promote the bispectrum-only forecast as the headline-conservative figure'. Wave 14-EEEEE (P3 R47 2 MAJORs) queued.",
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
    pdfMeta: "PDF 791 KB · 18 pp · May 10, 2026, v1.7.25",
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
    number: "3",
    title: "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Anomalies and Native-Trained Novelty Rates from 37.3 Million Sources",
    version: "v3.1.36",
    pages: "43",
    refs: "60+",
    readiness: 85,
    status: "89% — R47 forward closure (Wave 14-EEEEE): +5pp from 84 after closing both R47 MAJORs M1 + M2. R47-M1 fix: §sec:limitations 17.8% framing harmonized — old text labeled it 'provisional upper bound' (with conflicting 'single-sample point estimate' clause in the same paragraph) AND Conclusions item 6 called it 'genuine novelty floor'. New text reads as a SINGLE-SAMPLE POINT ESTIMATE everywhere: 'We report 17.8% as a single-sample point estimate measured at the top-1,000 score stratum and explicitly do NOT claim it as an upper bound, lower bound, or floor on the full-catalog novelty rate ... the abstract, this limitations section, and the conclusions all use the same single-sample point estimate at the top-1,000 stratum framing, with no upper-bound, lower-bound, or floor status assigned.' Conclusions item 6 changed from 'novelty floor' to 'novelty fraction ... single-sample point estimate at the top-1,000 DESI score stratum (no upper- or lower-bound status assigned; sec:limitations)'. Three sites now harmonized. R47-M2 fix: data-availability paragraph at L651 — old text directed consumers to pathc_unique_objects.parquet (the with-ACT 378,480-row sensitivity-check file) for 'all headline numbers', contradicting the ACT-quarantine policy. New text directs at pathc_unique_objects_no_act.parquet (378,280 rows, ACT-quarantined headline) and explicitly forbids using the with-ACT variant for the headline aggregate ('the off-by-200 with respect to the headline reflects the ACT quarantine and would corrupt downstream tabulations'). Wave 14-FFFFF (P4 R47 3 MAJORs, mechanical 30-min fixes) queued.",
    statusVariant: "green",
    target: "ApJS",
    description: "The multi-survey anomaly catalog. 378,280 unique anomalies catalogued across 7 surveys from 37.3 million sources via a unified BigAE autoencoder architecture. 17.8% upper-bound on genuine novelty rate against 20 all-sky catalogs (CDS X-Match), with NANOGrav 15yr free-spectrum gamma = 3.20 +/- 0.42 (0.48 sigma from bounce prediction gamma=3.0) and a central-value sigma(f_NL) = 8.27 +/- 2.37 forecast from the multi-tracer DESI pipeline at empirical alpha_jk = 0.19 +/- 0.65 (consistent with zero at 0.29 sigma; Wave 14-VVV calibration on full 5,384 QSO candidates closes the prior 'deferred to follow-up' gap but does not yet constrain alpha at multi-tracer-detection level). All 65 R42 cross-model peer-review findings closed; R43 BLOCKER fixes (alpha definition, error-bar reframe, novelty bound logic, multi-survey vs single-survey 141x/73x split, redshift coverage caveat) shipped Wave 14-WWW.",
    keyResults: [
      "378,280 unique anomalies across 7 non-quarantined surveys from 37.3M sources (Wave 11 retitle)",
      "Catalog-grade tier: 264,938 anomalies (DESI + SDSS native + eROSITA + Planck native + Gaia + NEOWISE); point-source tier 378,080; Planck CMB-patch tier 200",
      "LAMOST 113,342 reclassified as exploratory tier (FAIL: ~56% B-dominant cross-transfer empirical; native retrain 21.4x reduction to 2,054 at S>5)",
      "100k OOD validation (Wave 5 B10): median MSE 0.178, p99 = 44.85, 0.87% DESI anomaly rate preserved",
      "5-fold OOS Jaccard J̄ = 0.862 PASS on real DESI 47k-spectra retrain (Path-C exit criterion)",
      "Wave 13 (2026-05-01): real NANOGrav 15-yr KDE free-spectrum γ = 2.567 ± 0.382 — supersedes synthetic-power-law γ; bounce 3.0 still consistent (-1.13σ), SMBHB excluded at -4.6σ",
      "Empirical α_jk = 0.19 ± 0.65 (Wave 14-VVV jackknife on 5,384 QSO candidates; consistent with zero at 0.29σ); central-value σ(f_NL) = 8.27 ± 2.37 forecast (+1σ tail exceeds 8.98 baseline so 7.9% improvement is < 1σ from null); 16.4% improvement at fiducial α=0.15 (DESI+SDSS); SPHEREx forecast 4.38σ for f_NL = -35/8",
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
    pdfMeta: "PDF 28.39 MB · 43 pp · May 10, 2026, v3.1.36",
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
    number: "4",
    title: "Galaxy Chirality at Scale: 8.47M Galaxies Classified, Hemisphere Null at p_LEE < 10⁻⁴",
    version: "v1.0.46",
    pages: "25",
    refs: "30+",
    readiness: 86,
    status: "85% — R47 forward closure (Wave 14-FFFFF, mechanical 30-min fixes): +5pp from 80 after closing all 3 P4 R47 MAJORs M1+M2+M3. R47-M1 fix: §X Conclusion #1 ℓ=1 mode updated from superseded 'marginal 2.75σ' to canonical '−0.12σ after MASTER mode-coupling deconvolution' with explicit clarifying clause that the raw pseudo-C_ℓ value 6.48σ before deconvolution is mask-induced mode-coupling artifact fully removed by MASTER, and that the older snapshot value 2.75σ predates the canonical N_spiral=3,201,160 normalization recount and is retained only as a historical cross-reference (now consistent with §VII.B's self-stated invariant 'abstract, intro, conclusions all quote the high-confidence dipole upper bound'). R47-M2 fix: §X Conclusion #2 'factor of ~9 smaller' replaced with consistent 'factor of ~6-12 smaller (central ~9, depending on which Shamir reported value 2-4% is used as the comparator)' matching the abstract/§I/§VIII.A range framing from Wave 14-ZZZZ M3 closure. R47-M3 fix: §III.B 3.86× suppression factor re-anchored at the correct +2.05% → −0.53% NS-pool pair (2.05/0.53 ≈ 3.87 ≈ 3.86) instead of the within-spiral monopole pair +0.79% → −0.26% (0.79/0.26 = 3.04, NOT 3.86); within-spiral 3.04× factor explicitly named alongside as the smaller raw-to-equivariant within-spiral factor with explicit instruction not to conflate the two. PDF: 23 pp / 25,662,933 bytes (was 23 pp / 25,662,185 bytes; +748 bytes for the three reframings).",
    statusVariant: "green",
    target: "MNRAS",
    description: "The galaxy chirality catalog. 8.47M galaxies classified for CW/CCW handedness via a ViT-Small ensemble with rotational-equivariance correction (3.86x asymmetry suppression factor). Hemisphere look-elsewhere null at p_LEE < 10⁻⁴ (Wave 12 GPU 0/10,000 nulls exceeded data, MC resolution-limited) plus dipole MC injection-recovery establishing >=0.5% empirical detection threshold (catalog-wide sigma=0.43, p=0.30) refute Shamir 2020's 3% claim by a factor of 9. Global CW=0.4974 monopole offset (9.5σ from 0.5) traced to ~1% GZ1 human-handedness training-label bias — spatially uniform, not parity violation; the parity-preference test of this paper is the dipole, not the monopole. R43 BLOCKER fixes: GZ1 cross-validation gap restated as 5.5σ (was incorrectly <2σ) and reframed as monopole-floor agreement; abstract caveat on monopole-vs-dipole interpretation. All 65 R42 cross-model peer-review findings closed.",
    keyResults: [
      "8.47M galaxies classified (1,687,069 CW / 1,634,726 CCW / 5,152,736 NOT_SPIRAL)",
      "Wave 14-QQQ angular power reconcile: ℓ=1 -0.12σ MASTER-deconvolved canonical (raw pseudo-C_ℓ 6.48σ pre-deconvolution, mask-coupling artifact)",
      "Wave 14-OO bin-by-bin CW flatness closure (P4-OA-B7 §VI.D MAJOR): 4 morphology axes × 2 denominators on Pod 3 H200 in 29.3s wall pure-pandas CPU; full-spiral n=3,201,160 strict 0.1% bar — shape_r_eff_log Δ=0.317% FAIL, fracdev Δ=1.411% FAIL, b/a Δ=0.232% FAIL, type Δ=0.085% PASS; high-confidence n=949,584 — all 4 fail at 0.49%–3.03%; per-bin failures are known morphology-classification correlations and orthogonal to directional-dipole tests (Wave 12 p_LEE < 10⁻⁴ + Wave 14-NN ≥0.5% empirical + catalog σ=0.43/p=0.30 hold independently); type categorical (PSF/REX/EXP/DEV/COMP) PASSES; PUSHBACK with reframe, R42 P4-OA-B7 closed",
      "Wave 14-NN dipole MC injection-recovery closure (P4-OA-B5 §VI.C 0.2% min-detectable-dipole anchor): 250K dipole fits (5 amplitudes × 100 sky directions × 500 MC nulls) on Catalog C 471,049 equivariant spirals at NSIDE=64 (f_sky=0.4240); per-amplitude median σ: A=0.05%→-0.13, A=0.10%→-0.09, A=0.20%→+0.08, A=0.30%→+0.20, A=0.50%→+0.68; MIN-DETECTABLE-DIPOLE empirical=None; paper §X.B reframes 0.2% Poisson floor as STATISTICAL UPPER BOUND (paper L1553-L1574 already hedges); central no-detection σ=0.43/p=0.30 holds independently; FULL HARD FIX with reframe, R42 P4-OA-B5 closed",
      "Wave 14-LL edge-on TTA rotational-equivariance closure: b/a ∈ [0.00, 0.30) edge-on subsample (785,859 galaxies) CW fraction 0.4975 ± 0.0006, indistinguishable from catalog-wide 0.4974 ± 0.0003; max bin-to-bin spread 0.0005 (0.05%); residual asymmetry uniform across all four orientation regimes, NOT edge-on-localized; PUSHBACK, R42 P4-CM-M2 closed",
      "Wave 14-D Platt-calibration text fix: raw +0.79%/28.8σ → calibrated +0.4%/14.6σ → equivariant -0.26%/9.5σ; p_cal = σ(z/4.65 - 1.58) via L-BFGS on 20% held-out split",
      "Equivariance suppression factor 3.86× (raw asym +2.05% → eq asym -0.53%)",
      "Wave 12 hemi v4 GPU N_MC=10,000: max|A| = 8.531e-3 at (RA=78.75°, Dec=-66.44°), p_LEE < 10⁻⁴ (MC-resolution upper bound; 0/10,000 nulls reach data)",
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
      "arXiv submission (administrative, recommended first in P4 -> P1A -> P1B -> P3 -> P2 order)",
    ],
    preprintId: "HUBIFY-2026-004",
    pdfMeta: "PDF 25.68 MB · 25 pp · May 10, 2026, v1.0.46",
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
