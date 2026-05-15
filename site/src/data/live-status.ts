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
  lastUpdatedISO: "2026-05-15T10:00:00Z",
  lastUpdatedDisplay: "May 15, 2026 · 6:30 AM PT",
  headline:
    "**P4 v1.0.67 -> v1.0.68 -- cycle-3 polish round on Houston-external-4-vendor-review findings; 7 additional text-level closures; readiness 85 -> 87 (+2pp).** **Closed in v1.0.68 single bundled wave**: (a) abstract rewritten ~900 -> ~520 words 4-paragraph structure (Gemini-DR-I-1 / Gemini-I-1); (b) 9.5sigma monopole causal-language softened to working-hypothesis-pending-independent-ground-truth + explicit N_eff caveat (block bootstrap inflates per-pixel variance via 2-point correlation) (ChatGPT-B-3 + ChatGPT-D-5); (c) first-published multi-test overclaim qualified to to our knowledge one of the most extensive (ChatGPT-F-3); (d) multi-survey consensus softened to independent lines of evidence that do not reproduce (ChatGPT-F-4); (e) projected-morphology-vs-3D-spin scope statement added at Introduction + cosmology-transfer-function caveat (ChatGPT-A-4 + Gemini-DR-B-4); (f) bounce-cosmology framing minimized -- four-paper companion footnote removed; §VI.F What does the present null falsify -> What does the present null constrain (ChatGPT-I-7 + Grok-H-1 + Gemini-DR-B-4); (g) Iye photometric-duplication critique added to Shamir-context (ChatGPT-F-4); (h) Sec VI.G redshift-check raw-Catalog-A caveat made explicit (ChatGPT-A-3). **Remaining deferred to v1.0.69+ (compute-bound or external-artifact-bound)**: per-imaging-leg systematics; PSF-ellipticity calibration plot; controlled monopole+mask leakage null simulation (pymaster did not build locally; needs RunPod pod); HF dataset card rewrite (Houston push); HF dataset viewer schema fix; GitHub release tag + Zenodo DOI. **PDF 32pp / 25,887,836 bytes / 0 undef refs / sha256 26989c9e7f40...** (was 33pp / 25,899,597 v1.0.67; -1 page net from abstract shortening + cosmology-framing trim). 6 mirrors byte-identical. **Readiness P4 85 -> 87 (+2pp)** -- modest gain from 7 text-level reviewer-finding closures; compute-bound items still open. Cap 95% pending v1.0.69+ + Houston sign-off. Per-paper: P1A 74 (v1A.0.23), P1B 66 (v1B.0.7), P2 82 (v1.7.30), P3 85 (v3.1.41), **P4 87 (v1.0.68, +2pp)**. Cobaya unchanged 59,832/0.01945.",
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
      version: "v1A.0.23",
      readiness: 74,
      pendingWork:
        "v1A.0.23 (cycle-2 2nd R-round on upgraded model stack closed in single bundled wave; +1pp recovery to 74). 3-vendor convergent BLOCKER on Appendix B M_Pl² volume-integration as by-hand word-salad → reframed as explicit phenomenological ansatz with alternative coupling-rescaling interpretation; GPT-B1 arithmetic ~35 → ~120 orders cosmological-constant hierarchy with N_tot ≈ 94 derived; 2-vendor convergent erasure language \"plausibly\" → \"definitively\" propagated 4 sites with k_SPHEREx × e^N_tot anchor; Gemini-M1 NEW load-bearing physics finding — reheating thermal bath overwrites bounce-era torsion (strengthens B14) added as new paragraph; theorem-overclaim softening 2 sites; Mercuri attribution scope tightened. Visual-formatting QC per feedback_pdf_visual_formatting: paperTimestamp blob shortened, exec-summary table 914pt overflow eliminated. Route 2 dimensional re-derivation deferred to v1A.0.24. PDF 19pp / 807 KB / 0 undef refs / sha c6c1aaeb... 3 mirrors. Readiness 74 (+1pp).",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "ΛCDM+ΔNeff MCMC + NaMaster + ALP companion",
      version: "v1B.0.7",
      readiness: 66,
      pendingWork:
        "v1B.0.7 cycle-2 2nd R-round closed 2 three-vendor BLOCKERs + 5 NEW MAJOR catches in single bundled wave; readiness 64 → 66 (+2pp). 3-vendor BLOCKER on DESI DR2 chain status reported with 3 inconsistent snapshots → single canonical line (59,832/0.01945/22:53 UTC/slow-mode-dominated) propagated 4 sites. 3-vendor BLOCKER on model-comparison Table 2 publishing values it defers → ENTIRE numerical row + Bayes-factor piecewise REMOVED from body (full hard fix, not re-deferral); claims-table updated to Deferred-not-Verified. NEW (\u03c9/H)_0 k=7 vs k=8 scope contradiction (Gemini-M2) closed locally by fixing (\u03c9/H)_0 + \u03a9_k to zero in sampled YAML scope. SH0ES likelihood-label catch (GPT-B1) clarified — Planck NPIPE inverse-variance dominates posterior. C_a\u03b3\u00d7\u03b8_i=3.4\u00b11.1 dimensional inconsistency (GPT-M6) replaced with explicit C_a\u03b3\u00b7\u0394\u03c6/f_a\u224810.3 derivation. Abstract dual H_0; Cai:2009fn cite in \u00a73; cross-paper Table 1 all 5 refreshed + 5\u21924 col compaction (eliminated 600pt overfull); paperTimestamp blob shortened per R1; claims-table 113pt overfull eliminated. Compute-bound: \u0394\u03c7\u00b2/AIC/BIC/lnB recompute + NaMaster MC bias table on-record-deferred to v1B.0.8. PDF 8pp / 663KB / 0 undef / sha 32c4d9d93c94... 3 mirrors. Readiness 66 (+2pp); cap 95% pending v1B.0.8 + clean external R-round + Houston sign-off.",
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
      version: "v1.0.68",
      readiness: 87,
      pendingWork:
        "v1.0.68 cycle-3 polish round on Houston-external-4-vendor-review findings; 7 additional text-level closures + tighter abstract; readiness 85 -> 87 (+2pp). Closed: (a) abstract ~900 -> ~520 words 4-para structure; (b) 9.5sigma monopole causal language softened + N_eff caveat; (c) first-published overclaim qualified; (d) multi-survey consensus -> independent lines of evidence; (e) projected-morphology-vs-3D-spin scope + transfer-function caveat; (f) bounce-cosmology framing minimized (footnote removed + §VI.F rewritten); (g) Iye photometric-duplication critique added; (h) §VI.G raw-Catalog-A redshift-caveat made explicit. Deferred to v1.0.69+ (compute-bound or HF-side): per-leg systematics; PSF plot; monopole+mask null sim (pymaster build failed local); HF card; HF schema; GitHub release tag. PDF 32pp/25.89MB/0 undef/sha 26989c9e... 6 mirrors. Cap 95% pending compute-bound closures + Houston sign-off.",
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
