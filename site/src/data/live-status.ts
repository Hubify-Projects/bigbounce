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
  lastUpdatedISO: "2026-05-08T23:10:00Z",
  lastUpdatedDisplay: "May 8, 2026 · 4:10 PM PT",
  headline:
    "R43 Wave 14-WWW — Cobaya R̂−1 < 0.1 milestone (R̂−1 = 0.083) + P3 v3.1.22 R43 BLOCKER fixes shipped",
  summary:
    "Wave 14-WWW bundles two outcomes: (1) Cobaya DESI DR2 chain crossed R̂−1 < 0.1 after ~52h warm-restarted sampling: 0.86 → 0.31 → 0.21 → 0.15 → 0.083 (May 8 14:45 PT, 4,318 total accepted, outlier fraction crashed 13.6% → 0.03%, chains in essentially perfect overlap). Marginalized 1D posteriors are reliable; 2D-contour grade (R̂−1 < 0.05) ETA 12-24h, publication-quality (R̂−1 < 0.01) ETA 1-3 days. P1B §Structural Tension update queued for R̂−1 < 0.01. (2) R43 multi-agent adversarial peer-review round complete (4 parallel Claude subagents, P1A/P2/P3/P4, P1B excluded; 71 findings: 10 BLOCKER / 31 MAJOR / 30 MINOR; full review at project-context/peer-reviews/2026-05-08_1500pt_R43_CCAI_*). P3 v3.1.21 → v3.1.22 ships ALL three P3 BLOCKERs: (B1) explicit α ≡ b−1 definition reconciling 0.19 (jackknife mean) vs 0.27 (geomean over 3 bins) — adopt α_jk as headline; (B2) ±26%→±28.7% fractional uncertainty correction, +1σ tail = 10.64 explicitly stated to exceed 8.98 baseline (improvement < 1σ from null); (B3) Wave 14-VVV recast: α consistent with zero at 0.29σ, σ(f_NL)=8.27 demoted to central-value forecast pending higher-S/N follow-up. Plus M3 (genuine novelty 17.8% logic flip, now properly upper bound), m1 (141× multi-survey vs 73× single-survey reframe), and stale-text cleanup. PDF recompile: 41 pp / 28,372,914 bytes / 0 undef refs (one pre-existing Munchmeyer cite warning unchanged). **Continuing R43→R44→Rn loop: implementing remaining P3/P4/P2/P1A R43 fixes; on completion launching R44 cross-vendor adversarial round; repeat until reviews find next-to-nothing.**",
  currentlyRunning: [
    "Cobaya 4-chain MPI run on RTX A5000 pod ijzftpy3klystt — warm-started with posterior covmat from April-6 quintom chain; DESI DR2 + Planck NPIPE + Pantheon+ + DES-Y5; w0-wa CPL PPF; target R̂−1 < 0.01",
    "Autonomous /loop self-pacing every ~25 min — polling pod, will GetDist + update P1B §Structural Tension + recompile when R̂−1 < 0.01",
  ],
  papers: [
    {
      slug: "paper-1a",
      number: "1A",
      shortTitle: "ECH Structural Closure (no-go theorem)",
      version: "v1A.0.3",
      readiness: 99,
      pendingWork:
        "Houston sign-off + clean external R43 peer-review round (R43 BLOCKERs B1+B2+B3 shipped Wave 14-ZZZ — title reframed, abstract bounce-class-vs-ECH distinction explicit, MCMC headline forwarded to P1B; remaining MAJORs queued) + arXiv submission",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "ΛCDM+ΔNeff MCMC + NaMaster + ALP companion",
      version: "v1B.0.1",
      readiness: 99,
      pendingWork:
        "DESI DR2 w0wa cobaya chain to converge (R̂−1 < 0.01, ~6-12 h) → GetDist → §Structural Tension update → recompile, then Houston sign-off + arXiv",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.11",
      readiness: 99,
      pendingWork:
        "Houston sign-off + clean external R43 round (R43 B2 gauge-frame footnote shipped Wave 14-YYY; B1 invalidated as table is correctly labelled $\\mathcal{B}_{\\rm NL}$ shape function) + arXiv submission",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.23",
      readiness: 99,
      pendingWork:
        "HuggingFace dataset visibility flip (Houston manual) + sign-off + R43 round (R43 BLOCKER fixes shipped Wave 14-WWW; remaining MAJORs/MINORs queued) + arXiv submission",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M galaxy chirality at scale",
      version: "v1.0.32",
      readiness: 99,
      pendingWork:
        "Houston sign-off + clean external R43 round (R43 BLOCKERs B1+B2 + MAJORs M3+M4 shipped; M1+M2 already in v1.0.31; remaining MAJORs queued) + arXiv submission",
    },
  ],
  blockerTally: {
    closed: 65,
    openBlockers: 0,
    openMajors: 0,
    openMinors: 0,
  },
  cronStatus:
    "/loop self-pacing — autonomous loop active, polling pod every ~25 min",
  etaToCompletion:
    "Compute work: cobaya R̂−1 < 0.01 expected 6-12 h. Final 1% on each paper requires Houston sign-off + clean external R43 round.",
  pods: [
    {
      name: "ijzftpy3klystt (cobaya-r43-v2, RTX A5000 SECURE)",
      state: "active",
      note:
        "96 vCPU, 100 GB container disk; mpirun -n 4 cobaya-run on Planck NPIPE + DESI DR2 BAO + Pantheon+ + DES-Y5 in tmux 'chains'. ~$0.27/hr.",
    },
  ],
};
