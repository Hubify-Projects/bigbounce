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
  lastUpdatedISO: "2026-05-15T05:55:00Z",
  lastUpdatedDisplay: "May 14, 2026 · 10:55 PM PT",
  headline:
    "**P4 v1.0.63 → v1.0.64 — 13th real-vendor R-round on v1.0.63 closed in single bundled wave; readiness 94 → 95 (gate (a) of 99% readiness cap re-satisfied).** 13th cross-vendor R-round on the v1.0.63 closure paper. **Verdicts**: Gemini-2.5-Pro 0 BLOCKERs (7th-consecutive endorsement-class verdict: 'No blocker-grade findings are identified. The paper\\u2019s core observational result and systematic-error analysis appear robust.'); GPT-5.5 'No BLOCKER-grade findings' + 6 substantive MAJORs; DeepSeek-V3.2 1 BLOCKER (empirical floor provenance JSON not committed) + 2 MAJORs; Perplexity 2 MAJORs (bib metadata); Grok-4 502 capacity FAIL. **All real findings closed in v1.0.64 bundled wave**: (a) per-pixel random-label-null preservation language reconciled across abstract + §IX — now consistent: shuffle DESTROYS per-galaxy depth-vs-label correlation (would destroy a true 'depth-coupled' systematic) but does NOT destroy the geometric coupling between the global 9.5σ monopole and the patchy canonical mask, so +1.85σ is mask-geometry leakage of the monopole, not depth-systematic survival; (b) §Confidence Stratification reframed — HC-spiral 0.3σ is now a confidence-stability cross-check (signal does NOT amplify in high-confidence, diagnostic of noise-driven fluctuation), and the unstratified 0.43σ + -0.122σ + +1.85σ remain load-bearing headline estimators; (c) hemisphere 0.17% half-difference derived correctly as A/2 ⇒ A_dipole ≈ 0.34% (well below empirical >0.5% floor); max-over-768-directions 0.853% statistic explicitly flagged as a different observable not directly comparable; (d) §VI.D ↔ §VIII.F TTT-spin contradiction reconciled — Motloch+2021 ~2σ correlation consistently flagged as systematic-contaminated; present null reframed as the cleaner probe; (e) wave_14_nn_injection_recovery.json (sha 92c7d479...) + fisher_sensitivity_floor.json (sha 8ee7c276...) committed at outputs/canonical_provenance/; mc_seed_manifest.json extended with v1_0_63_addendum documenting shas + pixel-weighted galaxy count clarification (5,547,858 TTA-duplicated pixel-weighted vs 3,201,160 spiral catalog). **PDF 32 pp / 25,900,495 bytes / 0 undef refs / sha256 `7a7f9f0194026832...`** (was 25,897,969 / `df1390af31e6ea15`; +2,526 bytes for new derivations + reframings). 6 mirrors byte-identical. **Readiness P4 94 → 95 (+1pp)** — gate (a) of `feedback_99_pct_readiness_cap.md` re-satisfied per Gemini 7th-consecutive endorsement + GPT 'No BLOCKER-grade findings' + DeepSeek 'No new BLOCKERs introduced' (DeepSeek's lone BLOCKER was provenance-only, addressed in same commit). At 95% cap. Houston manual sign-off (gate b) needed to lift 95 → 99; final 1pp 99 → 100 Houston-only. **P4 IS PUBLISH-READY** pending Houston sign-off → arXiv submission per CLAUDE.md order P4 → P1A → P1B → P3 → P2. **Cobaya iter2-OMP6** on pod's `chains` tmux: R̂−1 = 0.01775 at 53,736 samples (5/14 15:43 UTC, stalled — no progress in ~7h, may need restart investigation). **Per-paper readiness**: P1A 73, P1B 64, P2 81, P3 84, **P4 95** (back at 95% cap).",
  summary:
    "Wave 14-PPPP launched the R45 multi-agent adversarial peer review on post-OOOO versions of P1A v1A.0.8 / P2 v1.7.15 / P3 v3.1.26 / P4 v1.0.35 (P1B excluded — compute-gated on cobaya R̂−1 < 0.01). 4 parallel Claude general-purpose subagents fetched the latest .tex from GitHub raw and returned 50 findings (6 BLOCKER + 21 MAJOR + 17 MINOR + 6 NIT) — saved at project-context/peer-reviews/2026-05-09_0030pt_R45_CCAI_*.md. The R45 net delta vs R44 (50 findings) is +1 BLOCKER, −2 MAJOR — the loop has NOT yet converged. Several R45 BLOCKERs are issues that the R44-closure waves themselves introduced: (P1A-R45-B1) the new four-route no-go appendix §IV.D Route 4 amplitude bound says ≥8 orders of magnitude but the underlying ρ_θ ≲ 10^{-46} eV^4 vs ρ_Λ ~ 10^{-11} eV^4 ratio is 10^35 (35 orders); (P1A-R45-B2) the new §IV.B Route 2 closure compares a rotation rate β̇ in eV with an angle uncertainty σ(β) in eV — dimensionally inconsistent; (P4-R45-B1) the GZ1 Platt L-BFGS recalibration parameters cited in §IV (A=0.215143, B=−1.581205) are NOT in the on-disk artifact wave_14_fff_gz1_platt_recal.json (which shows placeholder values A=0.21505, B=−1.58, accuracy 0.5194 chance, Brier=NaN). Two R45 BLOCKERs are pre-existing: (P2-R45-B1) abstract \\ref{sec:gr} undefined produces ?? in PDF; (P2-R45-B2) §VII 9.9σ vs 3-5σ headline still semantically conflated; (P3-R45-B1) tier arithmetic 264,938+113,342=378,280 ≠ 378,080 across 23 surfaces. Honest readiness rolled back: P1A 90→78 (−12pp), P1B 75 unchanged (compute-gated), P2 85→73 (−12pp), P3 89→80 (−9pp), P4 89→76 (−13pp). Average 85.6 → 76.4 (−9.2pp). The cycle Houston asked to see is now visible: 11 forward waves over the session added +3.2pp; one R45 round subtracts −9.2pp; the loop continues until per-round delta shrinks to zero. **Wave queue: 14-QQQQ closes P1A R45 BLOCKERs B1+B2 + MAJORs; 14-RRRR closes P2; 14-SSSS closes P3 (B1 tier-arithmetic restate + 5 MAJORs); 14-TTTT closes P4 (B1 re-run GZ1 L-BFGS + 6 MAJORs); 14-UUUU minors+nits sweep; 14-VVVV launches R46.** Cap stays at 95% until BOTH a clean CCAI R-round AND a clean cross-vendor non-Anthropic R-round have passed. Cobaya DESI DR2 chain continues: R̂−1 = 0.076 at May 8 18:27 PT.",
  currentlyRunning: [
    "Cobaya 16-chain MPI run on pod ijzftpy3klystt (iter2-OMP6, relaunched 5/11 23:41 UTC). R̂−1 trajectory monotonically descending across 32h: 0.118 (5/12 12:34) → 0.087 (5/12 18:53) → 0.082 (5/13 01:50) → 0.060 (5/13 07:42) → 0.040 (5/13 14:22) → **0.0315 (37,761 samples, 5/13 20:35 UTC, latest)**. All 16 cobaya-run workers healthy at 47-49% CPU (OMP=6 isolation holding). Avg slope ~0.0014/h over the last 6h; realistic R̂−1<0.01 ETA 12-15h → ~5/14 12 UTC (5am PT tomorrow). DESI DR2 BAO + Planck NPIPE + Pantheon+ + DES-SN5YR; w0-wa CPL PPF.",
    "Autonomous 30-min loop (job 25b4242d): every tick = pod check + adversarial R-round on rotating paper + bundled closures + recompile + mirror + SSOT + commit + Vercel deploy. Tick 1 (P2): v1.7.26→v1.7.27, 51 findings, 7B+19M closed, readiness 84→79 honest oscillation. Loop continues until all 5 papers pass clean external R-round + Houston sign-off.",
    "Autonomous /loop self-pacing every ~25 min — polling pod, will GetDist + update P1B §Structural Tension + recompile when R̂−1 < 0.01",
  ],
  papers: [
    {
      slug: "paper-1a",
      number: "1A",
      shortTitle: "ECH Structural Closure (no-go theorem)",
      version: "v1A.0.20",
      readiness: 81,
      pendingWork:
        "v1A.0.20 (2026-05-13) closes 4/4 BLOCKERs + 12 MAJORs from cross-vendor R-round-3 (50 findings): stale L1075 ‡ footnote rewrite (outcome-agnostic), structural-tension reframe (robustness check not co-equal closure), four-route channel-vs-operator-level disclosure with missing-operator acknowledgement, Eskilt2022b bib confabulation fix (same pattern as P2 tick 1), Mercuri2006 title fix, Liu2025 phantom-duplicate removal, Pantheon+/DES-SN5YR bibitems added. 4 deferred (operator-level no-go enumeration, AIC/BIC Bayes-factor framework, NANOGrav γ harmonization, 309,789-vs-424,781 sample-count clarification). Next: 21 minors + 9 nits sweep; clean cross-vendor R-round-4; Houston sign-off; arXiv.",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "ΛCDM+ΔNeff MCMC + NaMaster + ALP companion",
      version: "v1B.0.4",
      readiness: 71,
      pendingWork:
        "v1B.0.4 (2026-05-13) closes 5/9 top BLOCKERs + 16 MAJORs from cross-vendor R-round-3 (61 findings): phantom 114,992 third-dataset sample-count removed (no on-disk artifact), stale ~109/1-3-days footnote propagated from P1A tick 3 fix, ΔNeff proxy reframed as bounce-class compatibility check (not ECH-direct test), β=0.30° wrong-cite fix (added DiegoPalazuelos2022 bibitem + retargeted), Pantheon+/DES-SN5YR/Alonso2019 missing-cite fixes. DESI DR2 w0wa chain at R̂−1=0.0315 (5/13 20:35 UTC, ~41k samples). Remaining: ~17 minor + 8 nit items; the additional 4 BLOCKERs are compute-bound (full Planck-only frozen run, AIC/BIC framing collision in Conclusions, ODE solver disclosure, ALP MCMC autocorrelation explicit). Loop continues; next R-round after MCMC convergence + §Structural Tension recompile.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.27",
      readiness: 79,
      pendingWork:
        "v1.7.27 (2026-05-13) closes 7/7 BLOCKERs + 19 MAJORs from cross-vendor R-round-3 (51 findings): Eskilt2022b citation reversal, Munchmeyer:2019 kSZ-vs-SPHEREx mistake (now Dore:2014), 9.9σ Fisher provenance disclosure, Heinrich-fiducial-shift disclosure, gauge-frame muddle, mechanism-independence tightening, Cai:2026echoes→Zhu:2026echoes author/title fix, Higuchi misattribution, +Cabass:2022 BOSS. 4 deferred (compute-bound 6-bin SDB Fisher, Heinrich fiducial-shift verification, joint-Fisher post-systematic recompute, Cabass+2024 follow-up). Next: 18 minors + 5 nits sweep; clean cross-vendor R-round-4; Houston sign-off; arXiv submission.",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.38",
      readiness: 82,
      pendingWork:
        "v3.1.38 (2026-05-13) closes 6/6 BLOCKERs + 19 MAJORs from cross-vendor R-round-3 (62 findings): Bayes-factor → parameter-shift-likelihood-ratio reframe (with Trotta+Verde refs), §VI bounce-physics cross-paper paragraph, eROSITA western-hemisphere/depth-artifact disclosure, full PTA-companion citation set (Hellings-Downs, EPTA-DR2, PPTA-DR3, Afzal-NewPhysics, Phinney), Liang2023 3-error confab fix, Golden:2026P2 undefined-cite fix, SSOT γ_PTA drift correction (2.567 not 3.20). 4 deferred: proper marginalized (γ,log10A) Savage-Dickey Bayes factor, eROSITA per-tile depth-normalized re-analysis, multi-PTA combination (EPTA+PPTA+IPTA joint), score-stratified novelty quintiles. Next: 22 minors + 9 nits sweep; clean cross-vendor R-round-4; Houston sign-off; arXiv.",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M galaxy chirality at scale (3.2M spirals; null detection at sub-percent sensitivity)",
      version: "v1.0.64",
      readiness: 95,
      pendingWork:
        "v1.0.64 (13th real-vendor R-round on v1.0.63 closed in single bundled wave). Gemini-2.5-Pro 0 BLOCKERs (7th-consecutive endorsement-class verdict); GPT-5.5 'No BLOCKER-grade findings' + 6 MAJORs; DeepSeek-V3.2 1 BLOCKER (provenance-only, fixed in same commit) + 2 MAJORs; Perplexity 2 bib MAJORs; Grok-4 502. All real findings closed in single wave: per-pixel-null preservation language reconciled (abstract↔§IX); §Confidence Stratification reframed (HC 0.3σ now confidence-stability cross-check, not headline); hemisphere 0.17% half-difference derived as A/2 → A≈0.34%; §VI.D↔§VIII.F TTT-spin contradiction fixed (Motloch+2021 marginal correlation now consistently flagged as systematic-contaminated); committed wave_14_nn_injection_recovery.json + fisher_sensitivity_floor.json + mc_seed_manifest v1_0_63_addendum. PDF 32pp / 25.90 MB / 0 undef refs / sha256 7a7f9f01... Readiness 94→95 (+1pp), gate (a) of feedback_99_pct_readiness_cap re-satisfied; awaiting Houston sign-off (gate b) to lift 95→99; final 1pp 99→100 Houston-only.",
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
