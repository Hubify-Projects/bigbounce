// Live build status surfaced at the top of every page.
// Updated each cron fire / wave-close commit. Renders into <LiveStatus />.
// Timestamp is baked in at build time — bump on every commit that ships
// research progress so Vercel rebuilds put the new value live.

export interface PaperProgress {
  slug: string;
  number: string;
  shortTitle: string;
  version: string;
  readiness: number; // percent 0-100
  pendingWork: string; // one-line summary of what's still pending for this paper
}

export interface LiveStatus {
  lastUpdatedISO: string; // ISO 8601 UTC, baked at build time
  lastUpdatedDisplay: string; // human-readable PT timestamp for the banner
  headline: string; // one-line current state
  summary: string; // 1-3 sentences, what just shipped
  currentlyRunning: string[]; // bullet list of what is actively running RIGHT NOW
  papers: PaperProgress[]; // 5 papers, sorted by display order
  blockerTally: {
    closed: number;
    openBlockers: number;
    openMajors: number;
    openMinors: number;
  };
  cronStatus: string; // "self-pacing — autonomous loop active"
  etaToCompletion: string; // human-readable ETA to all-papers @ 100%
  pods: Array<{
    name: string;
    state: "active" | "idle" | "queued";
    note: string;
  }>;
}

export const liveStatus: LiveStatus = {
  lastUpdatedISO: "2026-05-19T03:00:00Z",
  lastUpdatedDisplay: "May 18, 2026 · 8:00 PM PT",
  headline:
    "🎯 **P1A v1A.0.33 LANDS THE CASCADED-LOOP EXIT MILESTONE — first paper in the campaign to satisfy AGENT_RULES §4.4.1.** R16 5-vendor cross-vendor returned 0 BLOCKER + 0 MAJOR across ALL 5 of 5 reviewers (DeepSeek-V4-Pro, Gemini-3.1-Pro, GPT-5, Grok-4.3, Perplexity-Sonar-Pro); 9th-consecutive Gemini-cosmology 0-BLOCKER; 2nd-consecutive 5-vendor clean round (R15+R16 both 0/0). External-review-ready, capped at 90% / 99% pending Houston sign-off. P1B v1B.0.20 R16 audit had Grok-only B1+B2 BLOCKERs FALSIFIED via stale-comment direct-file inspection (4 of 5 reviewers 0/0). P3 v3.1.56 closed the 6-round-deferred 9,576-object dedup-shortfall MAJOR via existing on-disk artifact (10,213 = 637 multi-survey + 9,576 intra-survey union-find collapses). P4 v1.0.116 trajectory v1.0.68 → v1.0.116 includes external review wave + 11 internal R-rounds + multi-null battery + cross-spectrum smoking gun + paper-wide +1.85σ → +3.64σ convention. R17/R21 cross-vendor cron blocked on OpenRouter top-up ($500.52/$500 verified). HF dataset README pushed to Hub at v1.0.116 (tick 106). All 4 paper PDFs verified byte-identical Vercel ↔ local at tick 108. Per-paper: P1A 90 (v1A.0.33, loop-exit), P1B 67 (v1B.0.20), P2 82 (v1.7.30), P3 86 (v3.1.56), P4 95 CAP (v1.0.116). Long-form legacy headline preserved for audit trail below.\n\n[Legacy May 15 headline] **P4 v1.0.67 -> v1.0.68 -- cycle-3 polish round on Houston-external-4-vendor-review findings; 7 additional text-level closures; readiness 85 -> 87 (+2pp).** **Closed in v1.0.68 single bundled wave**: (a) abstract rewritten ~900 -> ~520 words 4-paragraph structure (Gemini-DR-I-1 / Gemini-I-1); (b) 9.5sigma monopole causal-language softened to working-hypothesis-pending-independent-ground-truth + explicit N_eff caveat (block bootstrap inflates per-pixel variance via 2-point correlation) (ChatGPT-B-3 + ChatGPT-D-5); (c) first-published multi-test overclaim qualified to to our knowledge one of the most extensive (ChatGPT-F-3); (d) multi-survey consensus softened to independent lines of evidence that do not reproduce (ChatGPT-F-4); (e) projected-morphology-vs-3D-spin scope statement added at Introduction + cosmology-transfer-function caveat (ChatGPT-A-4 + Gemini-DR-B-4); (f) bounce-cosmology framing minimized -- four-paper companion footnote removed; §VI.F What does the present null falsify -> What does the present null constrain (ChatGPT-I-7 + Grok-H-1 + Gemini-DR-B-4); (g) Iye photometric-duplication critique added to Shamir-context (ChatGPT-F-4); (h) Sec VI.G redshift-check raw-Catalog-A caveat made explicit (ChatGPT-A-3). **Remaining deferred to v1.0.69+ (compute-bound or external-artifact-bound)**: per-imaging-leg systematics; PSF-ellipticity calibration plot; controlled monopole+mask leakage null simulation (pymaster did not build locally; needs RunPod pod); HF dataset card rewrite (Houston push); HF dataset viewer schema fix; GitHub release tag + Zenodo DOI. **PDF 32pp / 25,887,836 bytes / 0 undef refs / sha256 26989c9e7f40...** (was 33pp / 25,899,597 v1.0.67; -1 page net from abstract shortening + cosmology-framing trim). 6 mirrors byte-identical. **Readiness P4 85 -> 87 (+2pp)** -- modest gain from 7 text-level reviewer-finding closures; compute-bound items still open. Cap 95% pending v1.0.69+ + Houston sign-off. Per-paper: P1A 74 (v1A.0.23), P1B 66 (v1B.0.7), P2 82 (v1.7.30), P3 85 (v3.1.41), **P4 87 (v1.0.68, +2pp)**. Cobaya unchanged 59,832/0.01945.",
  summary:
    "Wave 14-PPPP launched the R45 multi-agent adversarial peer review on post-OOOO versions of P1A v1A.0.8 / P2 v1.7.15 / P3 v3.1.26 / P4 v1.0.35 (P1B excluded — compute-gated on cobaya R̂−1 < 0.01). 4 parallel Claude general-purpose subagents fetched the latest .tex from GitHub raw and returned 50 findings (6 BLOCKER + 21 MAJOR + 17 MINOR + 6 NIT) — saved at project-context/peer-reviews/2026-05-09_0030pt_R45_CCAI_*.md. The R45 net delta vs R44 (50 findings) is +1 BLOCKER, −2 MAJOR — the loop has NOT yet converged. Several R45 BLOCKERs are issues that the R44-closure waves themselves introduced: (P1A-R45-B1) the new four-route no-go appendix §IV.D Route 4 amplitude bound says ≥8 orders of magnitude but the underlying ρ_θ ≲ 10^{-46} eV^4 vs ρ_Λ ~ 10^{-11} eV^4 ratio is 10^35 (35 orders); (P1A-R45-B2) the new §IV.B Route 2 closure compares a rotation rate β̇ in eV with an angle uncertainty σ(β) in eV — dimensionally inconsistent; (P4-R45-B1) the GZ1 Platt L-BFGS recalibration parameters cited in §IV (A=0.215143, B=−1.581205) are NOT in the on-disk artifact wave_14_fff_gz1_platt_recal.json (which shows placeholder values A=0.21505, B=−1.58, accuracy 0.5194 chance, Brier=NaN). Two R45 BLOCKERs are pre-existing: (P2-R45-B1) abstract \\ref{sec:gr} undefined produces ?? in PDF; (P2-R45-B2) §VII 9.9σ vs 3-5σ headline still semantically conflated; (P3-R45-B1) tier arithmetic 264,938+113,342=378,280 ≠ 378,080 across 23 surfaces. Honest readiness rolled back: P1A 90→78 (−12pp), P1B 75 unchanged (compute-gated), P2 85→73 (−12pp), P3 89→80 (−9pp), P4 89→76 (−13pp). Average 85.6 → 76.4 (−9.2pp). The cycle Houston asked to see is now visible: 11 forward waves over the session added +3.2pp; one R45 round subtracts −9.2pp; the loop continues until per-round delta shrinks to zero. **Wave queue: 14-QQQQ closes P1A R45 BLOCKERs B1+B2 + MAJORs; 14-RRRR closes P2; 14-SSSS closes P3 (B1 tier-arithmetic restate + 5 MAJORs); 14-TTTT closes P4 (B1 re-run GZ1 L-BFGS + 6 MAJORs); 14-UUUU minors+nits sweep; 14-VVVV launches R46.** Cap stays at 95% until BOTH a clean CCAI R-round AND a clean cross-vendor non-Anthropic R-round have passed. Cobaya DESI DR2 chain continues: R̂−1 = 0.076 at May 8 18:27 PT.",
  currentlyRunning: [
    "D4-TTA N=10K holdout job (pid 12509): addresses Houston-flagged 1,558-galaxy statistical-power caveat per cron prompt option (a). Downloading 10,000 DESI Legacy Sky Viewer cutouts at ~0.5 valid/sec (DESI rate-limited, ~24% fail). ETA ~4-5h remaining. Output → outputs/canonical_provenance/d4_tta_holdout_10k_results.json (v1.0.117-d4-tta-holdout-10k-local). On completion will produce a v1.0.117 paper update tightening the statistical-power floor by ~√(10000/1558) ≈ 2.5×.",
    "Autonomous /loop self-pacing across ticks 80-110: ticks 102-108 landed major closures (P1A loop-exit, HF README v1.0.116 push to Hub, P3 9576-dedup closure via artifact, Vercel deploy verification); ticks 103/105/107/110 are SSOT/CLAUDE.md/queue.md/site-data staleness sweeps. Each tick converts at least one stale-doc or pending-recompute item into a closed/refreshed state.",
    "R-round 5-vendor cross-vendor cron BLOCKED at R17/R21: OpenRouter $500 budget exhausted ($500.52/$500 verified via direct API). Will resume immediately when Houston tops up; in the meantime each cron fire continues with non-API-dependent in-repo work.",
    "Cobaya iter2 chain TERMINATED at convergence 2026-05-18 07:53 UTC (R̂−1 = 0.00820 < 0.01 publication target; N = 128,385 across 16 chains). Backed up 3-location: HF (canonical online, bamfai/bigbounce-mcmc), local disk, BackBlaze; GitHub has manifest + posterior summary. Pod ijzftpy3klystt no longer load-bearing.",
  ],
  papers: [
    {
      slug: "paper-1a",
      number: "1A",
      shortTitle: "ECH Structural Closure (no-go theorem)",
      version: "v1A.0.33",
      readiness: 90,
      pendingWork:
        "🎯 v1A.0.33 — FIRST PAPER TO REACH CASCADED-LOOP EXIT (AGENT_RULES §4.4.1 satisfied 2026-05-18 tick 102). R16 5-vendor cross-vendor returned 0 BLOCKER + 0 MAJOR across ALL 5 of 5 reviewers; 9th-consecutive Gemini-cosmology 0-BLOCKER (held since R8); 2nd-consecutive 5-vendor clean (R15+R16). External-review-ready. Cap 99% per feedback_99_pct_readiness_cap pending Houston sign-off. R17 verification blocked on OpenRouter top-up. PDF 20pp / 831KB / 0 undef refs / sha e30e7643. 3 mirrors.",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "ΛCDM+ΔNeff MCMC + NaMaster + ALP companion",
      version: "v1B.0.20",
      readiness: 67,
      pendingWork:
        "v1B.0.20 — R16 audit pass with Grok-only B1+B2 BLOCKERs FALSIFIED via stale-comment direct-file inspection (mirror of v1B.0.18 SH0ES audit falsification pattern). 4 of 5 reviewers returned 0/0 at R16; 9th-consecutive Gemini-cosmology 0-BLOCKER; 2-consec Gemini-clean (R15+R16) → loop-exit ELIGIBLE pending one more full 5-vendor confirmation. R17 verification blocked on OpenRouter top-up. PDF 11pp / 694KB / 0 undef / sha 529f2d8a. 3 mirrors.\n\n[Legacy] v1B.0.7 cycle-2 2nd R-round closed 2 three-vendor BLOCKERs + 5 NEW MAJOR catches in single bundled wave; readiness 64 → 66 (+2pp). 3-vendor BLOCKER on DESI DR2 chain status reported with 3 inconsistent snapshots → single canonical line (59,832/0.01945/22:53 UTC/slow-mode-dominated) propagated 4 sites. 3-vendor BLOCKER on model-comparison Table 2 publishing values it defers → ENTIRE numerical row + Bayes-factor piecewise REMOVED from body (full hard fix, not re-deferral); claims-table updated to Deferred-not-Verified. NEW (\u03c9/H)_0 k=7 vs k=8 scope contradiction (Gemini-M2) closed locally by fixing (\u03c9/H)_0 + \u03a9_k to zero in sampled YAML scope. SH0ES likelihood-label catch (GPT-B1) clarified — Planck NPIPE inverse-variance dominates posterior. C_a\u03b3\u00d7\u03b8_i=3.4\u00b11.1 dimensional inconsistency (GPT-M6) replaced with explicit C_a\u03b3\u00b7\u0394\u03c6/f_a\u224810.3 derivation. Abstract dual H_0; Cai:2009fn cite in \u00a73; cross-paper Table 1 all 5 refreshed + 5\u21924 col compaction (eliminated 600pt overfull); paperTimestamp blob shortened per R1; claims-table 113pt overfull eliminated. Compute-bound: \u0394\u03c7\u00b2/AIC/BIC/lnB recompute + NaMaster MC bias table on-record-deferred to v1B.0.8. PDF 8pp / 663KB / 0 undef / sha 32c4d9d93c94... 3 mirrors. Readiness 66 (+2pp); cap 95% pending v1B.0.8 + clean external R-round + Houston sign-off.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.30",
      readiness: 82,
      pendingWork:
        "v1.7.30 — cycle-2 2nd real cross-vendor R-round on v1.7.29 closed. DBI category error (Gemini-B1), (e)/(f) assumption conflation, 3-vendor convergent r-range propagation [0.821, 0.879] → [0.829, 0.876], (a)-(e) → (a)-(f) propagation 4 sites. Deferred to v1.7.31+ (compute-bound): Appendix A convention, unified Fisher 3-5σ derivation, CFC physical-frame matter-bounce bispectrum, Heinrich σ(f_NL)=0.7 uncertainty propagation. PDF 19pp / 816KB / sha 76108e62.\n\n[Legacy] v1.7.27 (2026-05-13) closes 7/7 BLOCKERs + 19 MAJORs from cross-vendor R-round-3 (51 findings): Eskilt2022b citation reversal, Munchmeyer:2019 kSZ-vs-SPHEREx mistake (now Dore:2014), 9.9σ Fisher provenance disclosure, Heinrich-fiducial-shift disclosure, gauge-frame muddle, mechanism-independence tightening, Cai:2026echoes→Zhu:2026echoes author/title fix, Higuchi misattribution, +Cabass:2022 BOSS. 4 deferred (compute-bound 6-bin SDB Fisher, Heinrich fiducial-shift verification, joint-Fisher post-systematic recompute, Cabass+2024 follow-up). Next: 18 minors + 5 nits sweep; clean cross-vendor R-round-4; Houston sign-off; arXiv submission.",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.56",
      readiness: 86,
      pendingWork:
        "🎯 v3.1.56 — multi-round-deferred 9,576-object DEDUP-SHORTFALL MAJOR CLOSED tick 108 via existing on-disk artifact. pathc_dedup_summary_no_act.json IS the union-find recompute the R3→R16 GRO-B3 deferral was 'pending'; arithmetic decomposition 10,213 total = 637 multi-survey collapses + 9,576 intra-survey duplicate collapses (388,493 → 378,280 unique). Also R16 4-of-5 reviewers 0/0; Grok-only B1 ('σ(f_NL)=8.14 framing as positive claim') FALSIFIED — abstract literally states the <1σ qualifier 3+ times. R15+R16 = 2-consec Gemini-clean. R17 blocked on OpenRouter top-up. PDF 47pp / 28.43MB / sha 37d837cb. 4 mirrors.\n\n[Legacy] v3.1.38 (2026-05-13) closes 6/6 BLOCKERs + 19 MAJORs from cross-vendor R-round-3 (62 findings): Bayes-factor → parameter-shift-likelihood-ratio reframe (with Trotta+Verde refs), §VI bounce-physics cross-paper paragraph, eROSITA western-hemisphere/depth-artifact disclosure, full PTA-companion citation set (Hellings-Downs, EPTA-DR2, PPTA-DR3, Afzal-NewPhysics, Phinney), Liang2023 3-error confab fix, Golden:2026P2 undefined-cite fix, SSOT γ_PTA drift correction (2.567 not 3.20). 4 deferred: proper marginalized (γ,log10A) Savage-Dickey Bayes factor, eROSITA per-tile depth-normalized re-analysis, multi-PTA combination (EPTA+PPTA+IPTA joint), score-stratified novelty quintiles. Next: 22 minors + 9 nits sweep; clean cross-vendor R-round-4; Houston sign-off; arXiv.",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "Environmental dependence of spiral chirality across DESI LSS",
      version: "env-vweb-v0.1-2026-05-19",
      readiness: 30,
      pendingWork:
        "🎯 P5 env-VAC blocker CLOSED tick 116 — Houston-approved Phase 1 MVP V-Web env_finder ran end-to-end in 104s on laptop. Algorithm: V-Web (Hahn+ 2007 / Cautun+ 2014) on 14.6M DESI DR1 spectro galaxies, 256³ grid + 25 Mpc/h Gaussian smoothing + survey-mask-aware overdensity. HEADLINE: galaxy chirality is statistically independent of LSS environment within DESI DR1 at V-Web resolution. Per-env cw_fraction: void 0.4836 (−0.68σ), wall 0.5034 (+0.55σ), filament 0.4980 (−2.6σ), cluster 0.4963 (−4.7σ); range 1.7pp dominated by counting statistics; P4 monopole uniformly distributed across cluster+filament → P4 classifier-bias interpretation confirmed, not environment-dependent chirality. Phase 2 sensitivity sweep + RSD correction + Tempel+2018 cross-validation queued.\n\n[Legacy] P5 brought onto SSOT radar tick 114 after being missed across ticks 102-113. BOOTSTRAP: matched chirality × DESI DR1 catalog landed (1.3 GB / 2,232,212 deduped rows / 791,635 spirals at 1″ primary radius). Headline binomial cw_fraction=0.4972 at −5.0σ from 0.5 (P4-monopole-consistent on DESI-spectro-confirmed sub-sample). 5 of 6 first-pass analyses complete (redshift p=0.372 no z-dep; 5-NN density max_abs_sigma=3.94 pending LEE; HEALPix nside 16/32/64 p=0.61/0.14/0.41 no spatial structure; systematics label-shuffle sanity pass). Cosmic-web headline analysis BLOCKED on DESI environmental VAC missing from repo — the '187 DESI-derived attributes' catalog Houston referenced is exhaustively confirmed not in repo. Three resolution paths: (a) Houston locates the file; (b) wait for DESI DR1 LSS VAC release; (c) run our own cosmic-web finder on DESI DR1 LSS (DBSCAN/DisPerSE sub-project). Paper LaTeX is 9KB scaffold; no compiled PDF yet. R-round campaign has never operated on P5. SSOT: project-context/SSOT/paper-5/status.md. Live tex: pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex.",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M galaxy chirality at scale (3.2M spirals; null detection at sub-percent sensitivity)",
      version: "v1.0.120",
      readiness: 95,
      pendingWork:
        "🎯 v1.0.119 (CAP) — Houston-directed still-carry compute closures (3 of 4 attempted): family-level max-stat null on 15-cell leg×conf grid (OpenAI MAJ-11) finds family-corrected p=0.0086 (~2.4σ) for the DECaLS [0.5,0.6) +4.7σ cell — heavy-tailed null distribution (chi3-distributed dipole amplitude); morphology template ℓ=1 projection (OpenAI MAJ-12 leg-as-proxy) shows ≥25% of the canonical-mask ℓ=1 chirality amplitude is attributable to imaging-leg systematics (DES r_ℓ=1=−0.73, BASS+MzLS r=+0.65); hemisphere LEE Table I row split into MC + Bonferroni rows (OpenAI MAJ-13). MASTER-decoupled monopole-only null × 500 (OpenAI BL4) honestly deferred — pymaster did NOT build locally. PDF 49pp/26.24MB/sha 21eec4cb, 0 overfull/0 undef.\n\nv1.0.118 trajectory: (Grok-heavy + Gemini + OpenAI, 14 BLOCKERs + 12 MAJORs + 4 minors). Title rewritten to drop 'explained by' framing; paper-wide release-tag scrub v1.0.104/v1.0.115/v1.0.116/v1.0.117 → v1.0.118; \\\\artifact{} macro now points at the immutable release tag instead of mutable main; stale +1.85σ JSON renamed; parity-violating sectors → isotropy-breaking axial-vector; 'ruled out' → 'disfavored as a clean dipole-only explanation' for interpretation (i); 'sub-detection-threshold +3.64σ' → 'non-headline, systematics-attributed +3.64σ'; cross-spectrum ℓ=1 over-confirm fix; falsification floor 0.5% → 0.75%; monopole-only N=500 null scoped to PRE-MASTER only. Gemini's 'Table I row (iii) +1.85σ' BLOCKER FALSIFIED via direct file inspection (already +3.64σ since v1.0.115). PDF 49pp/26.23MB/sha 7d2051da, 0 overfull boxes/0 undef refs (cleanest P4 compile of the campaign).\n\nv1.0.117 trajectory: retracted the v1.0.74-v1.0.116 auxiliary claim of a -1.35% Z2-D4 argmax CW-fraction shift after a fresh N=1,988 seed=42 partial-harvest sign-flipped the same statistic to +2.11% at stable mean probability. Mean-per-galaxy-probability (Δp<0.0016 across both holdouts) is now the load-bearing D4-TTA invariance diagnostic. The 9.5σ catalog-level monopole and 21% per-galaxy argmax-flip rate are separately measured and unaffected; Houston-flagged 1,558-galaxy statistical-power caveat closed.\n\nv1.0.116 trajectory v1.0.68 → v1.0.116: external review wave (v1.0.104) + 11 internal R-rounds + GPT5-B3 monopole-subtraction truth-audit (+1.85σ → +3.64σ corrected, paper-wide convention from v1.0.107+) + multi-null battery exploring 3 interpretations + cross-spectrum smoking gun (r_ℓ=2=-0.65 σ=-2.89, r_ℓ=1=-0.49 σ=-1.53 against pixel-density proxy) + bootstrap-tautology audit + abstract trim 1839→600 words + R20 ℓ=1 cross-spectrum closure. Load-bearing scientific result: subsample-mask MASTER-deconvolved -0.12σ null. Canonical-mask +3.64σ is interpretation (ii) coherent depth-correlated systematic, NOT primordial detection. HF dataset README pushed to Hub at v1.0.116 (tick 106). R-round R21 blocked on OpenRouter top-up. PDF 48pp / 26.21MB / sha 273cc6cd. 5 mirrors.\n\n[Legacy] v1.0.68 cycle-3 polish round on Houston-external-4-vendor-review findings; 7 additional text-level closures + tighter abstract; readiness 85 -> 87 (+2pp). Closed: (a) abstract ~900 -> ~520 words 4-para structure; (b) 9.5sigma monopole causal language softened + N_eff caveat; (c) first-published overclaim qualified; (d) multi-survey consensus -> independent lines of evidence; (e) projected-morphology-vs-3D-spin scope + transfer-function caveat; (f) bounce-cosmology framing minimized (footnote removed + §VI.F rewritten); (g) Iye photometric-duplication critique added; (h) §VI.G raw-Catalog-A redshift-caveat made explicit. Deferred to v1.0.69+ (compute-bound or HF-side): per-leg systematics; PSF plot; monopole+mask null sim (pymaster build failed local); HF card; HF schema; GitHub release tag. PDF 32pp/25.89MB/0 undef/sha 26989c9e... 6 mirrors. Cap 95% pending compute-bound closures + Houston sign-off.",
    },
  ],
  blockerTally: {
    closed: 208,
    openBlockers: 0,
    openMajors: 1,
    openMinors: 5,
  },
  cronStatus:
    "/loop self-pacing — autonomous loop active, polling pod every ~25 min",
  etaToCompletion:
    "Compute: cobaya R̂−1 < 0.01 ETA 2-3 days after the 5/11 23:41 UTC iter2-OMP6 fix (16 chains × OMP_NUM_THREADS=6 + GetDist-built posterior covmat; per-chain step rate ~18 sec, total chain throughput 4× iter1); P4 deep-MLP RA/Dec ablation needs an H200 spin-up. Each paper carries a backward step on R45 launch (CCAI multi-agent self-review will open new findings) and a larger backward step on cross-vendor non-Anthropic round (GPT-5/Gemini/Grok/Perplexity). True 99% is gated on BOTH a clean CCAI round AND a clean cross-vendor round AND Houston sign-off; the final 1% is Houston manually triggering arXiv submission.",
  pods: [
    {
      name: "ijzftpy3klystt (cobaya-r43-v2, RTX A5000 SECURE)",
      state: "active",
      note:
        "96 vCPU, 100 GB container disk; **mpirun -n 16 with OMP_NUM_THREADS=6** cobaya-run (iter2-OMP6 since 5/11 23:41 UTC after pre-fix BLAS oversubscription was diagnosed) on Planck NPIPE + DESI DR2 BAO + Pantheon+ + DES-SN5YR in tmux 'chains'. GetDist-built posterior covmat from iter1's 9,503 samples. ~$0.27/hr.",
    },
  ],
};
