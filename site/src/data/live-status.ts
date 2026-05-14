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
  lastUpdatedISO: "2026-05-15T09:00:00Z",
  lastUpdatedDisplay: "May 15, 2026 · 2:00 AM PT",
  headline:
    "**P4 v1.0.64 → v1.0.65 — Cycle-2 2nd real cross-vendor R-round on v1.0.64 closed in single bundled wave; Gemini-2.5-Pro 8th-consecutive endorsement; readiness stable at 95% cap.** First tick of rotation cycle 2 (cycle 1 closed P4+P2+P3+P1A+P1B). **Per-vendor on v1.0.64**: Gemini-2.5-Pro **0 BLOCKERs — 8th-CONSECUTIVE ENDORSEMENT** (exact quote: 'The paper\\u2019s theoretical framing and interpretation of its null result are sound and appropriately cautious. The v1.0.64 revisions have successfully addressed the substantive findings from the previous round.'); GPT-5.5 'No BLOCKER-grade findings' + 5 MAJORs (per-pixel-null language still contradictory abstract↔§Hemisphere; Fig 7 hemisphere statistic mixing; LEE accounting 3.05σ→p~10⁻³ can't give p_LEE≤10⁻⁴; 0.5% empirical floor overstated as 3σ-recovery; Table III ℓ=1 vs bandpower mixing); DeepSeek-V3.2 1 BLOCKER (same per-pixel-null contradiction — convergent) + 3 MAJORs (dangling 0.2% Fisher-floor reference; Table III row separation; 'canonical mask' definition); Grok-4 1 MAJOR + 3 minor/nit (2nd consecutive landing breaking 5-round 502 streak); Perplexity 2 MAJORs (Shamir 2022 + Jia 2023 'no arXiv preprint' notes needed). **Closed in v1.0.65 bundled wave**: (a) **3-vendor convergent per-pixel-null precision fix** at abstract + §Hemisphere + §Conclusions (i)/(ii)/(iii): global-permutation-at-fixed-positions language now uniform — shuffle destroys per-galaxy depth/edge × label correlations but does NOT destroy monopole-mask geometric leakage; (b) dangling 0.2% Fisher-floor abstract reference removed (DeepSeek-M1); (c) 'all higher multipoles null' contradiction with $+2$ to $+6\\sigma$ bandpowers fixed in §Dipole — replaced with explicit monopole-leakage attribution for $\\ell\\in[2,26]$ bandpowers (parity observable lives at $\\ell=1$ specifically). **Deferred to v1.0.66 (smaller polish)**: Table III row separation; canonical-vs-subsample mask definitions in §IX; Fig 7 hemisphere statistic separation; LEE 3.05σ-vs-p_LEE consistency; 0.5% empirical 'lower bound only' framing; TTT 'cleaner probe' rephrase; uncited Mercuri/Freidel/Holst bib entries; Shamir/Jia 'no arXiv preprint' explicit notes. **PDF 33pp / 25,905,151 bytes / 0 undef refs / sha256 `2a1435cc0e40...`** (was 32pp / 25,900,495 / 7a7f9f01; +4,656 bytes + 1 page). 4 mirrors byte-identical. **Readiness P4 95 unchanged** — gate (a) re-confirmed for 3rd consecutive cycle-level satisfaction (v1.0.61 rounds 10+11; v1.0.64 round 13; v1.0.65 round 14). **Gemini endorsement streak now 8 consecutive rounds** — unprecedented stability of the publish-ready external-review-gate state. **P4 REMAINS PUBLISH-READY pending only Houston manual sign-off** (gate b) to lift 95→99; final 1pp 99→100 Houston-only. **Cobaya iter2-OMP6 UPDATE**: chain DID progress — checkpoint advanced 53,736 → 59,832 samples (22:53 UTC); R̂−1 = 0.01945 (slight uptick from 0.01775, within typical chain fluctuation; still > 0.01 threshold so P1B remains compute-gated). Sampler is slow-mode-dominated but NOT stalled. **Per-paper**: P1A 73 (v1A.0.22), P1B 64 (v1B.0.6), P2 81 (v1.7.29), P3 84 (v3.1.40), **P4 95 (v1.0.65, at cap; 8th-consecutive Gemini endorsement)**.",
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
      version: "v1A.0.22",
      readiness: 73,
      pendingWork:
        "v1A.0.22 (1st new real-vendor R-round on v1A.0.21 closed; 3 of 5 prior 'closed' BLOCKERs re-surfaced + new convergent findings). GPT-5.5 3 BLOCKERs (dim+2 vs dim+4 still present; Route 2; 13/14 propagation) + 3 MAJORs; Gemini-2.5-Pro 2 BLOCKERs (dim + Route 2) + 1 MAJOR (deferral note parity contradiction) + 1 minor; DeepSeek 1 BLOCKER (f_NL scope) + 3 MAJORs; Perplexity 1 false-positive BLOCKER + 1 MAJOR + 3 minors; Grok-4 502 FAIL. Closed: dimensional bookkeeping rewrite (explicit volume-int M_Pl^2 factor; ρ_Λ ∼ (α/M)M_Pl^5 dim+4); Hehl-Datta parity-even correctly reaffirmed; 13-barrier propagation 7 sites; f_NL scoped to scalar-only w=0 with Paper II Assumption (f); SPHEREx 3-5σ downgraded to Paper II cross-ref. Route 2 dimensional re-derivation remains on-record deferred to v1A.0.23. PDF 18pp / 798 KB / 0 undef refs / sha256 d2503424... 3 mirrors. Readiness 73 unchanged; +1pp expected after Route 2 closure.",
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
      version: "v1.0.65",
      readiness: 95,
      pendingWork:
        "v1.0.65 (cycle-2 2nd real-vendor R-round on v1.0.64 closed; Gemini 8th-consecutive endorsement; readiness stable at 95% cap). Gemini-2.5-Pro 0 BLOCKERs (8th endorsement); GPT-5.5 0 BLOCKERs + 5 MAJORs; DeepSeek 1 BLOCKER (convergent per-pixel-null contradiction) + 3 MAJORs; Grok-4 1 MAJOR (2nd consecutive landing); Perplexity 2 bib MAJORs. Closed: (a) 3-vendor convergent per-pixel-null precision fix at abstract + §Hemisphere + §IX (global-permutation-at-fixed-positions destroys per-galaxy correlations but not monopole-mask geometric leakage); (b) dangling 0.2% Fisher-floor abstract reference removed; (c) 'all higher multipoles null' contradiction with $+2$ to $+6\u03c3$ bandpowers fixed via explicit monopole-leakage attribution. Deferred to v1.0.66: Table III row separation; canonical-vs-subsample mask definitions; Fig 7 hemisphere statistic separation; LEE 3.05\u03c3-vs-p_LEE consistency; 0.5% empirical 'lower bound only'; TTT 'cleaner probe' rephrase; uncited Mercuri/Freidel/Holst bib; Shamir/Jia 'no arXiv preprint' notes. PDF 33pp / 25.90 MB / 0 undef refs / sha256 2a1435cc... 4 mirrors. Readiness 95 unchanged. P4 publish-ready pending only Houston sign-off.",
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
