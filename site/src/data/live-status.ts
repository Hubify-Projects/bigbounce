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
  lastUpdatedISO: "2026-05-09T06:00:00Z",
  lastUpdatedDisplay: "May 8, 2026 · 11:00 PM PT",
  headline:
    "R44 Wave 14-LLLL — P4 v1.0.34 R44 MAJORs M4+M6+M7 shipped (recall asymmetry decomposition: 1.2 pp = ~1% GZ1 prior ⊕ ~0.5% Cat-C residual; MDD N_eff inflation note; morphology-bin flatness disclosed in abstract). P4 readiness 86→88. Forward step. Honest cycle: numbers will roll backward at R45 launch + cross-vendor round.",
  summary:
    "STATUS HONESTY ROLLBACK (Houston directive 2026-05-08 22:00 PT). The site had every paper pegged at 99% across live-status, papers, and SSOT — that was a false positive carried through 6 forward waves this session without any backward step. Rolled to honest numbers. P1A 85% (R44 BLOCKERs + 4-route appendix + cross-paper bibitems shipped; M4 D_inf prefactor + M5 orphan labels open; R45 + cross-vendor + Houston sign-off pending). P1B 75% (compute-gated on cobaya R̂−1 < 0.01, currently 0.076; §Structural Tension MCMC numbers placeholder; not yet through R44 self-review let alone R45 / cross-vendor). P2 78% (R44 BLOCKERs B1+B2 closed Wave 14-HHHH; 4 R44 MAJORs open: Bayes factor 8–17 vs 11 reconciliation, curvaton prior reframing, Heinrich Eq. X normalization, DBI → axion-curvaton/QSFI; Maldacena:2003 cite still undefined). P3 88% (fNL deferral closed Waves 14-VVV/KKKK; R44 BLOCKERs all closed; R44 MAJORs M1+M2+M4+M5+nit1 shipped; R43-M5 anomaly-window-randoms methodology paragraph still open as minor; HuggingFace dataset visibility flip pending Houston manual). P4 86% (R44 MAJORs M1+M2+M3+nit2 shipped Wave 14-GGGG; M4 recall asymmetry decomp + M5 deep-MLP RA/Dec ablation [pod RTX A5000 too slow for 8.47M deep-MLP retrain] + M6 MDD N_eff + M7 morphology-bin flatness disclosure all open). **Workflow rule going forward (saved as feedback memory feedback_readiness_oscillation.md):** readiness numbers oscillate forward (revision wave) → backward (R-round opens findings) → forward (close findings) → backward (next R-round) → ..., until the forward/backward delta per cycle shrinks to zero. Cap is 95% until BOTH a clean CCAI R-round AND a clean cross-vendor non-Anthropic R-round have passed; only then can rise to 99%. Final 1% (99 → 100) is Houston sign-off + arXiv push only. This wave makes no paper-content edits; it's a status-honesty correction. Cobaya DESI DR2 chain continues: R̂−1 = 0.076 at May 8 18:27 PT.",
  currentlyRunning: [
    "Cobaya 4-chain MPI run on RTX A5000 pod ijzftpy3klystt — warm-started with posterior covmat from April-6 quintom chain; DESI DR2 + Planck NPIPE + Pantheon+ + DES-Y5; w0-wa CPL PPF; target R̂−1 < 0.01",
    "Autonomous /loop self-pacing every ~25 min — polling pod, will GetDist + update P1B §Structural Tension + recompile when R̂−1 < 0.01",
  ],
  papers: [
    {
      slug: "paper-1a",
      number: "1A",
      shortTitle: "ECH Structural Closure (no-go theorem)",
      version: "v1A.0.6",
      readiness: 85,
      pendingWork:
        "Houston sign-off + clean external R44 peer-review round (R44 MAJOR M3 four-route no-go appendix shipped Wave 14-IIII; cross-paper companion bibitems Golden2026P{1b,2,3,4} + Eskilt2022b joint Planck+ACT defined Wave 14-JJJJ — all natbib cite warnings cleared) + arXiv submission",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "ΛCDM+ΔNeff MCMC + NaMaster + ALP companion",
      version: "v1B.0.2",
      readiness: 75,
      pendingWork:
        "DESI DR2 w0wa cobaya chain to converge (R̂−1 = 0.076 at 18:27 PT, ~1-3 days) → GetDist → §Structural Tension update → recompile, then Houston sign-off + arXiv. Wave 14-JJJJ refreshed bibitems + version stamp; cross-paper Golden2026P{1a,2,3,4} + Eskilt2022b joint Planck+ACT now defined as proper @article entries.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.13",
      readiness: 78,
      pendingWork:
        "Houston sign-off + clean external R44 round (R44 BLOCKERs B1+B2 shipped Wave 14-HHHH: 9.9σ n_fNL site reframed as joint-Fisher pre-systematic-budget upper bound; convention-reversal halving stated for both 5.25σ→2.6σ optimistic AND 3-5σ→1.5-2.5σ post-systematic in abstract; conclusion-section 1.5-2.5σ unchanged) + arXiv submission",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.25",
      readiness: 88,
      pendingWork:
        "HuggingFace dataset visibility flip (Houston manual) + sign-off + clean external R45 round (R44 MAJORs M1+M2+M4+nit1 shipped Wave 14-FFFF; R44-M5 high-confidence-restricted α re-measurement shipped Wave 14-KKKK: α_GS,jk = +1.83 ± 2.03 on 1,122 Gold+Silver subset, σ(f_NL)_GS = 2.28 ± 7.43, central 74% improvement consistent with no improvement at <1σ; full-sample α_jk = 0.19 ± 0.65 retained as load-bearing headline) + arXiv submission",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M galaxy chirality at scale",
      version: "v1.0.34",
      readiness: 88,
      pendingWork:
        "Houston sign-off + clean external R45 round (Wave 14-GGGG: M1+M2+M3+nit2; Wave 14-LLLL: M4 recall-asymmetry decomposition + M6 MDD N_eff inflation note + M7 morphology-bin flatness in abstract). Open: M5 deep-MLP RA/Dec ablation needs H200 spin-up; R45 self-review + cross-vendor non-Anthropic round + arXiv submission still ahead.",
    },
  ],
  blockerTally: {
    closed: 71,
    openBlockers: 0,
    openMajors: 10,
    openMinors: 17,
  },
  cronStatus:
    "/loop self-pacing — autonomous loop active, polling pod every ~25 min",
  etaToCompletion:
    "Compute: cobaya R̂−1 < 0.01 ETA 1–3 days; P4 deep-MLP RA/Dec ablation needs an H200 spin-up. Each paper carries a backward step on R45 launch (CCAI multi-agent self-review will open new findings) and a larger backward step on cross-vendor non-Anthropic round (GPT-5/Gemini/Grok/Perplexity). True 99% is gated on BOTH a clean CCAI round AND a clean cross-vendor round AND Houston sign-off; the final 1% is Houston manually triggering arXiv submission.",
  pods: [
    {
      name: "ijzftpy3klystt (cobaya-r43-v2, RTX A5000 SECURE)",
      state: "active",
      note:
        "96 vCPU, 100 GB container disk; mpirun -n 4 cobaya-run on Planck NPIPE + DESI DR2 BAO + Pantheon+ + DES-Y5 in tmux 'chains'. ~$0.27/hr.",
    },
  ],
};
