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
    version: "v1A.0.22",
    pages: "18",
    refs: "72",
    readiness: 73,
    status: "73% — v1A.0.22 (1st NEW real cross-vendor R-round on v1A.0.21 closed in single bundled wave; substantive findings — 3 of 5 prior 'closed' BLOCKERs re-surfaced + new convergent dimensional-bug findings + scope-narrowing for f_NL claim). Per-vendor verdicts: **GPT-5.5 3 BLOCKERs** (Appendix B dim+2 vs dim+4 inconsistency STILL PRESENT in v1A.0.21 [convergent with Gemini-B1 + DeepSeek-M2]; deferral paragraph + Route 2 still dimensionally inconsistent; 13/14 barrier merge not propagated across 6+ sites) + 3 MAJORs (B8 parity-even closure undermined by admitted parity-odd Holst partner; f_NL=-35/8 over-scoped beyond P2 Assumption (f); SPHEREx 3-5σ not supported in P1A); **Gemini-2.5-Pro 2 BLOCKERs** (same dim+2 vs dim+4 + Route 2 dimensionful ratio) + 1 MAJOR (v1A.0.21 deferral note describes axial-axial as 'pseudoscalar parity-odd' contradicting main-text correct 'parity-even') + 1 minor (13/14 barrier); **DeepSeek-V3.2 1 BLOCKER** (f_NL=-35/8 mechanism-independence not aligned with P2 scalar-only w=0 scoping) + 3 MAJORs + 1 minor + 1 nit; **Perplexity 1 FALSE-POSITIVE BLOCKER** (Freidel-Minic-Takeuchi bib already has correct arXiv hep-th/0507253; Perplexity inferred wrong from context) + 1 MAJOR + 3 minors; Grok-4 502 FAIL (5th consecutive). **Closed in v1A.0.22**: (a) **Dimensional bookkeeping fix** in Appendix B — explicit dim-reduction factors written out: ρ_Λ^bounce ∼ (α/M)·K·R·M_Pl^2 = (α/M) M_Pl^5 ∼ 10^-2 M_Pl^4 with [ρ_Λ]=+4 by construction; the missing volume-integration M_Pl^2 placeholder is flagged as a scaling-ansatz item for future iteration; (b) **Hehl-Datta parity-character clarification**: deferral note's incorrect 'pseudoscalar parity-odd' replaced with explicit 'parity-even (axial-vector × axial-vector → scalar, each parity-odd component squared = +1)' — main text Sec.~r1_njl was always correct; (c) **13-barrier propagation across 7 sites**: abstract, Sec 1, Sec 2.4, Sec 9, Sec 14.2, Sec 15, Table II caption — all now consistently read '13 logically-independent (14 historical catalog entries; B8 subsumed by B14)'; (d) **f_NL=-35/8 scoped to scalar-only w=0 matter-bounce class under Assumption (f) of Paper II**; abstract Table reframed, Sec 13 rewritten with explicit ekpyrotic/Cuscuton/quintom/fermion-bound exclusions; (e) **SPHEREx 3-5σ downgraded** to 'forecasted in Paper II' cross-reference. **Route 2 dimensional re-derivation remains on-record deferred** to v1A.0.23 (requires explicit photon-Chern-Simons coupling derivation; channel-level closure at >30 orders of magnitude is preserved at OOM level). PDF 18pp / 798 KB / 0 undef refs / sha256 d2503424... 3 mirrors byte-identical. **Readiness 73 unchanged** — substantive narrative-actionable closures preserved baseline; the dimensional bookkeeping fix is significant theoretical work but the Route 2 deferral keeps gate (a) of 99% cap unmet. +1pp to 74 expected after v1A.0.23 closure of Route 2.",
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
    pdfMeta: "PDF 798 KB · 18 pp · May 15, 2026, v1A.0.22",
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
    version: "v1B.0.5v1B.0.6",
    pages: "8",
    refs: "32",
    readiness: 64,
    status: "64% — v1B.0.6 (1st real cross-vendor R-round on v1B.0.5 closed in single bundled wave). **Per-vendor**: DeepSeek-V3.2 3 BLOCKERs (sample-count provenance; Δχ²_eff=-7.9 incompatibility with ΔNeff posterior; Savage-Dickey ln B provenance) + 2 MAJORs + 1 minor; GPT-5.5 2 BLOCKERs (model-comparison stats still printed despite deferral; (ω/H)_0 parameter scope inconsistent) + 4 MAJORs (DESI DR2 chain status stale; NaMaster bias 0.032° vs 0.040° inconsistent; cross-paper 14-barrier inconsistency with P1A v1A.0.22; Table 3 stale versions/readiness; bib not provided to reviewer); Gemini-2.5-Pro 2 MAJORs (parameter scope; Savage-Dickey spurious ±0.5 uncertainty) + 4 minors/nit; Grok-4 2 BLOCKERs (same model-comparison stats + DESI chain stale) + 2 MAJORs + 2 minors/nits; Perplexity 1 FALSE-POSITIVE BLOCKER (Liu 2025 ECTorsionDESI2025 IS in bib with arXiv:2507.04265; Perplexity inferred wrong from manuscript-only) + 2 MAJORs + 3 minors/nits. **Closed in v1B.0.6**: (a) **DESI DR2 chain stall status update** across 4 sites (cross-paper Table 1 caption, MCMC inventory Table 2 caption, §Cosmological-Fits §5 paragraph, §Forward paragraph) — all now report 'stalled at R̂−1=0.01775 / 53,736 samples / last checkpoint flush 15:43 UTC / no advance ~12+h / 16-rank mpirun alive (slow-mode-dominated, not crashed)' replacing the prior 'running ~3 days ETA / monotonically descending' framing; calendar ETA removed and replaced with honest 'do not commit to a calendar-date convergence ETA' language; (b) **Cross-paper Table 1 refreshed** to current versions and readinesses (P1A v1A.0.22 73% / P1B v1B.0.6 64% / P2 v1.7.29 81% / P3 v3.1.40 84% / P4 v1.0.64 95%); 14-barrier text → '13 logically-independent (14 historical catalog entries)' aligned with P1A v1A.0.22; (c) **14→13 barrier propagation** at §intro 'What is NOT in this paper' site. **Deferred on-record to v1B.0.7 (compute-bound)**: Δχ²_eff/AIC/BIC/ln B Table 2 + Conclusions recompute from frozen-thinned chain (3-vendor convergent BLOCKER; the v1B.0.5 deferral paragraph stays in place since the underlying chain artifact recompute is a separate task); (ω/H)_0 parameter-scope removal/sample (Gemini-M1 + GPT-B2); NaMaster per-injection bias table (GPT-B4); Savage-Dickey provenance script (DeepSeek-B3 + Gemini-M2); sample-count provenance script (DeepSeek-B1). PDF 8pp / 682 KB / 0 undef refs / sha256 b35d95a1... 3 mirrors byte-identical. **Readiness P1B 64 unchanged** — DESI DR2 chain stall transparency closure preserves baseline but the compute-bound recompute deferrals keep gate (a) unmet.",
    statusVariant: "green",
    target: "Physical Review D (companion)",
    description: "Paper 1B — technical verification companion to Paper 1A. Three analyses documented: (1) Stock-CAMB ΛCDM+ΔN_eff MCMC proxy run (Cobaya v3.6.1, 424,781 samples across three frozen dataset combinations) — null-consistency test of an extra radiation degree of freedom, recovers ΛCDM with H0 = 67.68 ± 1.06 km/s/Mpc and ΔN_eff consistent with zero. (2) NaMaster pseudo-C_ell pipeline recovery on the Planck Commander map (500 MC, NSIDE=512, ℓ_max=1024, f_sky=0.32): injecting β=0.27° recovers 0.238° at SNR=20.32. (3) Spectator-ALP consistency check: a field with f_a ~ M_Pl, m ~ H_0 is consistent with the published Planck+ACT joint β = 0.342° ± 0.094° (3.6σ). A new DESI DR2 w0wa free MCMC chain (Planck NPIPE + DESI DR2 BAO + Pantheon+ + DES-SN5YR) is in progress on RTX A5000 pod and will be incorporated into the §Structural Tension cross-reference once converged.",
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
      "Houston personal sign-off (final 1%, gated)",
      "External peer-review round (R43) — zero MAJOR/MINOR findings required",
      "DESI DR2 w0wa chain convergence (R̂−1 < 0.01) → GetDist → §Structural Tension update",
      "arXiv submission (administrative, after DR2 chain incorporation)",
    ],
    preprintId: "HUBIFY-2026-001B",
    pdfMeta: "PDF 682 KB · 8 pp · May 15, 2026, v1B.0.6",
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
    version: "v1.7.30",
    pages: "19",
    refs: "39",
    readiness: 82,
    status: "82% — v1.7.30 (cycle-2 2nd real cross-vendor R-round on v1.7.29 closed on the upgraded model stack: Gemini-3.1-Pro-preview / Grok-4.3 / DeepSeek-V4-Pro / GPT-5.5 / Sonar Pro Search, all reasoning_effort=high). **Per-vendor on the upgraded stack** (higher-effort reasoning produced substantively more nuanced findings): Gemini-3.1-Pro 1 BLOCKER (B1: **DBI inflation category error** — DBI is equilateral, vanishes in squeezed limit, cannot be tested via SDB n_fNL) + 2 MAJORs (Assumption (e)/(f) conflation; r-range Sec 8.3 still [0.821, 0.879]) + 2 minors + 1 nit; GPT-5.5 1 BLOCKER (Appendix A convention unresolved — deferred from v1.7.29) + 4 MAJORs (5.2-5.5σ doesn't propagate ε-range f_NL=[-4.35,-4.02]; CFC dual-pronged inconsistent across abstract/conclusion; Assumption (a)-(e) → (a)-(f) propagation; reproducibility code-tag still v1.7.26) + 1 minor; Grok-4.3 0 BLOCKERs + 3 MAJORs framed as Bs (r-range propagation; 9.9σ still in body; CFC framing not uniform) + 3 confirmation items (Assumption (f), Suyama-Yamaguchi, κ_1 sign all confirmed correct); DeepSeek-V4-Pro 0 BLOCKERs + 6 MAJORs/minors (template-mismatch provenance miscounted 'four' values when only 3+1=4 shown; 3-5σ post-systematic not from single Fisher matrix; injection-recovery validates only CMB-Fisher weighting; 3×10^5 vs 6×10^5 realization-count inconsistency; ℓ-space Fisher methodology insufficient; Heinrich σ(f_NL)=0.7 no uncertainty propagation); **Perplexity Sonar Pro: FIRST CLEAN BIB AUDIT PASS THIS SESSION** (all citations check out — CaiBrandenberger:2014 fix is clean, Wands/Finelli/Maldacena/Mercuri/Freidel/Suyama-Yamaguchi all verified; no fused-ID issues found). **Closed in v1.7.30**: (a) Gemini-B1 DBI category error — DBI is equilateral not local; can't measure via SDB n_fNL; replaced with explicit explanation; (b) Gemini-M1 abstract Assumption (e)/(f) conflation — abstract now correctly attributes Assumption (e)=post-bounce inflation, Assumption (f)=fermion-sourced torsion; (c) 3-vendor convergent r-range propagation [0.821, 0.879] → [0.829, 0.876] in Sec 8.3 decision-thresholds; (d) GPT-M5 (a)-(e) → (a)-(f) propagated across 4 sites (assumption-list cross-refs in §sensitivity, §forecast, §conclusion, §abstract); (e) Cai et al. → Cai & Brandenberger for the 2-author 2014 paper; (f) β=0.27° 'bounce ALP prediction' → 'bounce-motivated ALP accommodation' (observational fit, not first-principles derivation); (g) 'four noise-weighted values {0.829, 0.830, 0.835}' miscount fixed — now reads 'three noise-weighted values (SDB/SPHEREx/flat) plus signal-only CMB-Fisher 0.876, four total'; (h) 3×10^5 vs 6×10^5 realization-count reconciliation — canonical 3×10^5 across 3 framework ensembles; 6×10^5 was aggregation error in older draft. **Deferred on-record to v1.7.31 (compute-bound)**: GPT-B1 Appendix A convention split (already deferred from v1.7.29); GPT-M3 single unified error-budget table; DeepSeek-B2 unified Fisher matrix for 3-5σ derivation; CFC physical-frame matter-bounce bispectrum CFC-transform calculation (GPT-M4); Heinrich σ(f_NL)=0.7 uncertainty propagation. PDF 19pp / 816,025 bytes / 0 undef refs / sha256 76108e62... 4 mirrors byte-identical. **Readiness 81 → 82 (+1pp)** per feedback_readiness_oscillation — substantive narrative-actionable closures + first clean bib audit (Perplexity) + Grok-4.3 confirming v1.7.29 kappa_1/Assumption(f)/Suyama-Yamaguchi closures held. Cap 95% pending Houston sign-off + clean external R-round (Appendix A + error-budget items still pending v1.7.31).",
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
    pdfMeta: "PDF 816 KB · 19 pp · May 15, 2026, v1.7.30",
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
    version: "v3.1.40",
    pages: "44",
    refs: "67",
    readiness: 84,
    status: "84% — v3.1.40 (1st real cross-vendor R-round on v3.1.39 closed in single bundled wave). **Per-vendor verdicts**: GPT-5.5 2 BLOCKERs (378,280 dedup arithmetic; DESI OOD MSE normalization) + 4 MAJORs (tier-mixing in headline; 37.3M denominator; σ(f_NL) propagation; NANOGrav per-bin KDE independence + bib metadata) — both BLOCKERs require recompute, NOT narrative work; DeepSeek-V3.2 1 BLOCKER (378,280 tier arithmetic traceability — same as GPT-B1) + 3 MAJORs (17.8% novelty caveat already in v3.1.39 text; SDSS 77,905 reporting; α heterogeneous z) + 2 minors; Gemini-2.5-Pro 1 BLOCKER (f_NL=-35/8 / γ=3.0 'not independent observables' overstates rigidity beyond w=0 single-field) + 1 MAJOR (bib audit) + 3 minors/nit; Grok-4 3 MAJORs (378,280 narrative inflation; NANOGrav asymmetric framing; f_NL forecast <1σ from null emphasis); Perplexity Sonar Pro 2 FALSE-POSITIVE BLOCKERs (Heinrich2023 already has arXiv:2311.13082 in bib state; ACT_DR6 bib correctly cites Qu et al. ApJ 962, 112 (2024) without conflicting arXiv ID) + 4 minor bib audit items. **Closed in v3.1.40**: (Gemini-B1) mechanism-rigidity scoping — f_NL/γ tight coupling explicitly scoped to scalar-only w=0 matter-bounce class, with explicit clarification that ekpyrotic/Cuscuton/quintom/non-scalar-only models decouple the predictions; (Gemini-m2) deleted self-referential '>4σ-equivalent framing dropped in earlier drafts' sentence; (Gemini-n1 + Grok-B2) SMBHB '+4.61σ (excluded)' reframed at 3 sites as 'strongly disfavored as parameter-shift; full marginalized model-comparison required for model-level exclusion'; (GPT-B1 + GPT-B2 + GPT-M3 + GPT-M4 deferred-items paragraph) added to §Path-C Caveats explicitly flagging (a) 378,280 dedup-arithmetic 637-vs-10,213 reconciliation, (b) DESI OOD MSE normalization, (c) σ(f_NL) zero-systematics vs propagated forecast distinction, (d) NANOGrav per-bin KDE covariance — all 4 are recompute-bound and on-record for v3.1.41. Several MAJORs already addressed in v3.1.39 text from prior R-rounds (17.8% point-estimate caveat at L455/L498/L629; α heterogeneous-z 'Note on redshift coverage' at L552; σ(f_NL) 'central-value forecast pending higher-S/N' framing at L552/L635). **Deferred to v3.1.41 (recompute-bound)**: 378,280 union-find dedup manifest recompute; DESI OOD MSE-in-standardized-units validation; full multi-parameter Fisher recompute with photo-z/fiber-assignment/selection nuisance blocks; NANOGrav Savage-Dickey full marginalization on chain; comprehensive bib audit for missing arXiv IDs across all entries. PDF 44pp / 28.40 MB / 0 undef refs / sha256 69a7afb5... 5 mirrors byte-identical. **Readiness 84 unchanged** — substantive findings closed where narrative-actionable; recompute-bound items on-record for v3.1.41.",
    statusVariant: "green",
    target: "ApJS",
    description: "The multi-survey anomaly catalog. 378,280 unique anomalies (378,080 point-source tier + 200 Planck CMB-patch tier) across 7 surveys from 37.3 million sources via a unified BigAE autoencoder architecture. 17.8% novelty rate at the top-1,000 stratum against 20 all-sky catalogs (CDS X-Match), with NANOGrav 15yr HD-correlated KDE free-spectrum fit (Zenodo 8060824, emcee 32x10k+2.5k burn-in) recovering gamma = 2.567 +/- 0.382 — matter-bounce gamma=3.0 sits at +1.13 sigma above posterior mean (marginally consistent), SMBHB gamma=4.33 at +4.61 sigma above mean (excluded). The prior gamma = 3.20 +/- 0.42 figure was from the synthetic-from-power-law summary-statistic fit superseded by the real-KDE result. Central-value sigma(f_NL) = 8.27 +/- 2.37 forecast from the multi-tracer DESI pipeline at empirical alpha_jk = 0.19 +/- 0.65 (consistent with zero at 0.29 sigma; Wave 14-VVV calibration on full 5,384 QSO candidates closes the prior 'deferred to follow-up' gap but does not yet constrain alpha at multi-tracer-detection level).",
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
    pdfMeta: "PDF 28.40 MB · 44 pp · May 14, 2026, v3.1.40",
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
    title: "A Survey-Scale Chirality Catalog of 8.47M Galaxies (3.2M Spirals): A Null Detection of Large-Scale Parity Violation at Sub-Percent Sensitivity",
    version: "v1.0.65",
    pages: "32",
    refs: "46",
    readiness: 95,
    status: "95% — v1.0.65 (cycle-2 2nd real cross-vendor R-round on v1.0.64 closed in single bundled wave). **Gemini-2.5-Pro: 0 BLOCKERs — 8th-CONSECUTIVE ENDORSEMENT-CLASS VERDICT** (exact quote: 'The paper\u2019s theoretical framing and interpretation of its null result are sound and appropriately cautious. The v1.0.64 revisions have successfully addressed the substantive findings from the previous round.'). GPT-5.5 'No BLOCKER-grade findings' + 5 MAJORs; DeepSeek-V3.2 1 BLOCKER (per-pixel-null contradiction abstract↔§Hemisphere — convergent with GPT-M1 and Grok-B1) + 3 MAJORs + 2 minor/nit; Grok-4 1 MAJOR + 3 minor/nit (2nd consecutive landing after 5-round 502 streak); Perplexity 2 MAJORs (Shamir 2022 + Jia 2023 bib: prior wrong arXiv IDs correctly removed but no replacement/no-arXiv-preprint notes given — minor metadata polish for v1.0.66). **Closed in v1.0.65**: (a) **3-vendor convergent per-pixel-null language precision fix** — abstract + §Hemisphere § Conclusions (i)/(ii)/(iii) now uniformly use the global-permutation-at-fixed-positions characterization: shuffle destroys per-galaxy depth-vs-label and per-galaxy mask-edge-vs-label correlations, but does NOT destroy the geometric leakage of the global monopole into the patchy canonical mask; the abstract's prior 'preserves per-pixel mask-edge positions' phrasing (which sounded like 'preserves mask-edge-label correlations') is replaced with 'destroys per-galaxy depth/edge × label correlations but does not destroy monopole-mask geometric leakage'; (b) **dangling 0.2% reference removed** from abstract Fisher-floor sentence (DeepSeek-M1); (c) **'all higher multipoles consistent with null' contradiction fixed** in §Dipole — replaced with explicit attribution to monopole-leakage channel for $+2$ to $+6\sigma$ bandpowers $\ell\in[2,26]$; parity observable lives at $\ell=1$ specifically. **Deferred on-record to v1.0.66 (smaller polish items)**: DeepSeek-M2 Table III caption row-1-vs-rows-2-5 explicit separation; DeepSeek-M3 'canonical mask' vs 'subsample mask' definitions in §IX; GPT-M2 Fig 7 caption hemisphere statistic separation; GPT-M3 LEE accounting 3.05σ-local vs p_LEE≤10⁻⁴ consistency; GPT-M4 0.5% empirical → 'lower bound only' framing; Gemini-T1 TTT 'cleaner probe' rephrase; Gemini-T2 uncited Mercuri/Freidel/Holst bib entries; Perplexity-B1/B2 Shamir + Jia 'no-arXiv-preprint' notes. **PDF 33pp / 25,905,151 bytes / 0 undef refs / sha256 `2a1435cc0e40...`** (was 32pp / 25,900,495 / 7a7f9f01; +4,656 bytes for precision-fix rewording + +1 page from abstract Fisher-floor cleanup). 4 mirrors byte-identical. **Readiness P4 95 unchanged — at cap; gate (a) of feedback_99_pct_readiness_cap re-confirmed for 3rd consecutive cycle-level satisfaction** (v1.0.61 R-rounds 10+11; v1.0.64 R-round 13; v1.0.65 R-round 14 = this round). Gemini-2.5-Pro endorsement streak now **8 consecutive rounds**. **P4 REMAINS PUBLISH-READY pending only Houston manual sign-off** (gate b) to lift 95→99; final 1pp 99→100 Houston-only.",
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
    pdfMeta: "PDF 25.90 MB · 33 pp · May 15, 2026, v1.0.65",
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
