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
  lastUpdatedISO: "2026-05-06T07:00:00Z",
  lastUpdatedDisplay: "May 5, 2026 · 11:00 PM PT",
  headline:
    "R43 Wave 14-SSS — P1 v2.3.18 PDF recompiled + cobaya warm-restarted with posterior covmat (10× faster sampling)",
  summary:
    "Wave 14-SSS: (1) P1 v2.3.18 PDF recompiled locally (34 pp / 1,239,876 bytes / 0 undef refs) — closes the Wave 14-QQQ 'PENDING pod SSH' item. (2) Cobaya DESI DR2 chain warm-restarted: cold-start diagonal proposal (18.8% acceptance, 95 samples/chain in 8h) replaced by posterior covmat from the April-6 converged quintom chain (same Planck NPIPE CamSpec likelihood). Expected 10× improvement in acceptance rate and mixing. Chain running on pod ijzftpy3klystt (RTX A5000 SECURE, 96 vCPU). **Only P1B has active compute pending; P1A/P2/P3/P4 blocked solely on Houston sign-off + clean external R43 round + arXiv submission.**",
  currentlyRunning: [
    "Cobaya 4-chain MPI run on RTX A5000 pod ijzftpy3klystt — warm-started with posterior covmat from April-6 quintom chain; DESI DR2 + Planck NPIPE + Pantheon+ + DES-Y5; w0-wa CPL PPF; target R̂−1 < 0.01",
    "Autonomous /loop self-pacing every ~25 min — polling pod, will GetDist + update P1B §Structural Tension + recompile when R̂−1 < 0.01",
  ],
  papers: [
    {
      slug: "paper-1a",
      number: "1A",
      shortTitle: "ECH Structural Closure (no-go theorem)",
      version: "v1A.0.1",
      readiness: 99,
      pendingWork:
        "Houston sign-off + clean external R43 peer-review round + arXiv submission (no compute pending)",
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
      version: "v1.7.10",
      readiness: 99,
      pendingWork:
        "Houston sign-off + clean external R43 round + arXiv submission (no compute pending)",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.20",
      readiness: 99,
      pendingWork:
        "HuggingFace dataset visibility flip (Houston manual) + sign-off + R43 round + arXiv submission (no compute pending)",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M galaxy chirality at scale",
      version: "v1.0.30",
      readiness: 99,
      pendingWork:
        "Houston sign-off + clean external R43 round + arXiv submission (no compute pending)",
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
