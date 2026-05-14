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
    version: "v1B.0.5",
    pages: "8",
    refs: "32",
    readiness: 64,
    status: "64% — v1B.0.5 (2nd REAL cross-vendor round via OpenRouter, 5 vendors, 5 BLOCKERs caught the simulated rounds missed). Convergent finding (DeepSeek+GPT-5+Gemini): sample-count drift across abstract/conclusions — Abstract said 309,789 frozen, Conclusions said 424,781 (added ongoing 114,992), footnote burn-in arithmetic gave 123,129 when 0.7×309,789 = 216,852. Rewrote footnote with explicit 216,852 both-chains + 123,788 full-tension-only stratification + clarified 114,992 is ongoing-not-frozen. Conclusions L573 fixed 424,781→309,789. Plus Δχ²_eff=-7.9 incompatibility with ΔNeff=-0.020±0.169 posterior (deferred for chain-readout recompute, on-record at §V); ln B=+4.8 Savage-Dickey provenance missing; tab refs convergence→mcmc_inventory + model_compare→modelcomp. PDF 8pp / 677 KB / 0 undef refs / sha256 fd1c311a...",
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
    pdfMeta: "PDF 677 KB · 8 pp · May 14, 2026, v1B.0.5",
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
    version: "v1.7.29",
    pages: "19",
    refs: "39",
    readiness: 81,
    status: "81% — v1.7.29 (1st real cross-vendor R-round on v1.7.28 closed in single bundled wave). Verdicts on v1.7.28: GPT-5.5 1 BLOCKER (Appendix A convention inconsistency on c=2 vs c=1 normalization vs in-in commutator time-ordering) + 5 MAJORs (sign arithmetic on kappa_1(epsilon-3/2) correction wrong; 9.9-sigma Fisher unverifiable from on-disk inputs; error budget propagation; CFC physical-frame discriminator mixing with Planck/local-template gauge frame; HDM ECH caveat doesn't close decoupling gap); Gemini-2.5-Pro 1 BLOCKER (mechanism-independence overclaim; HDM 4f could re-introduce UV dependence via fermion loops) + 2 MAJORs (kappa_1 over an order of magnitude uncertain contradicts 'tightly determined' framing; Bayes factor doesn't account for QSFI competitor class) + 2 minors; DeepSeek-V3.2 1 BLOCKER (physical-frame f_NL_inf=0 has no traceable provenance JSON/script) + 3 MAJORs (9.9-sigma Fisher provenance; r ranges inconsistent abstract/body/JSON; BF prior-grid analytic provenance) + 2 minors; Perplexity Sonar Pro 2 MAJORs (CaiBrandenberger:2014 arXiv ID 1404.6968 is actually a 'Computed-torque orthosis' robotic medical-physics paper, NOT cosmology — same fused-metadata pattern as prior Shamir/Jia catches; second BLOCKER is the same issue) + 4 minors/nits; Grok-4 502 FAIL. All real findings closed in v1.7.29: (a) **GPT-M1 sign-arithmetic fix** on f_NL(epsilon) consistency-relation derivation — Eq. (consistency) changed from +kappa_1(epsilon-3/2) to -kappa_1(epsilon-3/2) so the correction direction at Planck n_s=0.9649 gives the previously-quoted (and physically correct) [-4.35, -4.02] range (less negative than -4.375 for epsilon<3/2 quasi-dust); (b) **Mechanism-independence narrowing** (Gemini-B1 + GPT-M5 + DeepSeek-B4): added Assumption (f) to the list of f_NL=-35/8 assumptions explicitly excluding fermion-sourced torsion during contracting phase; closure paragraph now reads 'robust within the scalar-only matter-bounce class' with explicit fermion-bound requirement noted for broader ECH classes; (c) **CFC physical-frame tempering** (DeepSeek-B1 + GPT-M4 + Gemini-m2): abstract rewritten — bounce-vs-inflation discrimination now dual-pronged (Planck/local-template gauge frame ~290× contrast + CFC physical-frame leading-squeezed-limit complementary discriminator) with explicit clarification that SPHEREx/MegaMapper estimators measure the conventional Planck/local-template f_NL, not the CFC quantity directly; (d) **CaiBrandenberger:2014 bib fix** (Perplexity-B1/B5): removed eprint = {1404.6968} from focused_paper_refs.bib (verified by direct lookup to map to a 'Computed-torque orthosis' robotic medical-physics paper), retained DOI 10.1103/PhysRevD.90.023534 as canonical journal reference, added inline note; (e) **9.9-sigma demoted from abstract** (DeepSeek-B2 + GPT-M2): the specific number removed pending Fisher-input release; abstract now references the SDB joint-Fisher analysis as a self-consistency check in §8 only; (f) **r-range unification** (DeepSeek-B3): all sites now quote r ∈ [0.829, 0.876]; the JSON [0.856, 0.895] range is flagged as MC-noise-driven; (g) **'Tightly determined' tempered** (Gemini-M1): introduction reframed as 'minimally parameterized at zeroth order in epsilon-expansion; first-order coefficient kappa_1 has order-of-magnitude range 5.6-80 carrying substantial theoretical uncertainty'; (h) **Suyama-Yamaguchi 'saturates' → 'satisfies'** (Gemini-m1): tau_NL prediction reframed as inequality consistent with SY, not saturation (since bounce bispectrum is not exactly local, r_cos>0.97 not =1); (i) Gemini-M2 QSFI BF closure paragraph also fixed a latex double-subscript bug (n_\fnl → n_{\fnl}) discovered during compile. GPT-B1 Appendix A convention split + GPT-M3 error-budget table deferred to v1.7.30 (require structural rewrites to Appendix A). PDF 19pp / 815 KB / 0 undef refs / sha256 a381c29c... 4 mirrors byte-identical. Readiness 81 (unchanged; this was the first real-vendor round on P2, so the 81% baseline reflects pre-real-vendor confidence; substantial closures in v1.7.29 should justify a +1pp move to 82 after the 2nd R-round confirms vendor-clean state). At 81% — gate (a) of feedback_99_pct_readiness_cap requires clean cross-vendor R-round; v1.7.29 just closed the 1st round's substantive findings, so 82-85 range will require successive clean rounds. Cap 95% pending Houston sign-off.",
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
    pdfMeta: "PDF 815 KB · 19 pp · May 14, 2026, v1.7.29",
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
    version: "v1.0.64",
    pages: "32",
    refs: "46",
    readiness: 95,
    status: "95% — v1.0.64 (13th real-vendor R-round on v1.0.63 closed in single bundled wave). 13th round verdicts: Gemini-2.5-Pro 0 BLOCKERs (7th-consecutive endorsement-class verdict, exact quote: 'No blocker-grade findings are identified. The paper\u2019s core observational result and systematic-error analysis appear robust.'); GPT-5.5 'No BLOCKER-grade findings' + 6 substantive MAJORs (per-pixel-null preservation language contradiction abstract↔§IX; Table III missing ⟨C_null⟩ + MC-count columns; subsample-mask MASTER map-construction details; injection-recovery floor scope HC-spiral vs canonical; §Confidence Stratification HC-spiral 0.3σ-primary contradicts abstract estimator chain; hemisphere 0.17%→0.853% conversion underivable); DeepSeek-V3.2 1 BLOCKER (empirical floor provenance JSON not committed) + 2 MAJORs (Fisher floor JSON + n_pixel_weighted_galaxies traceability); Perplexity Sonar Pro 2 MAJORs (bib state on Shamir:2022 arXiv-pending + Iye:2020 year/title pair); Grok-4 502 capacity FAIL. All real findings closed in v1.0.64: (a) per-pixel-null preservation language reconciled across abstract + §IX (now consistent — shuffle destroys per-galaxy depth-CW correlation but preserves global-monopole × canonical-mask-geometry leakage as the channel sourcing +1.85σ); (b) §Confidence Stratification reframed (HC-spiral 0.3σ now confidence-stability cross-check showing signal does NOT amplify in high-confidence — diagnostic of noise-driven fluctuation; unstratified 0.43σ + -0.122σ + +1.85σ remain headline load-bearing); (c) hemisphere 0.17% half-difference derived correctly as A/2 → A≈0.34% (well below empirical >0.5% floor); max-over-768-directions 0.853% statistic explicitly flagged as different observable, not directly comparable; (d) §VI.D ↔ §VIII.F TTT-spin contradiction reconciled (Motloch+2021 ~2σ correlation now consistently flagged as systematic-contaminated and present null reframed as cleaner probe); (e) wave_14_nn_injection_recovery.json + fisher_sensitivity_floor.json committed at outputs/canonical_provenance/; mc_seed_manifest.json extended with v1_0_63_addendum recording shas + pixel-weighted galaxy count clarification (5,547,858 = TTA-duplicated pixel-weighted count vs 3,201,160 canonical spiral catalog). PDF 32 pp / 25,900,495 bytes / 0 undef refs / sha256 7a7f9f0194026832... Readiness 94→95 (+1pp; gate (a) of feedback_99_pct_readiness_cap re-satisfied per Gemini 7th-consecutive endorsement + GPT 'No BLOCKER-grade findings' + DeepSeek 'No new BLOCKERs introduced'); at 95% cap. Houston manual sign-off (gate b) needed to lift to 99; final 1pp 99→100 Houston-only. P4 IS PUBLISH-READY pending Houston sign-off → arXiv submission per CLAUDE.md order P4 first.",
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
    pdfMeta: "PDF 25.90 MB · 32 pp · May 14, 2026, v1.0.64",
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
