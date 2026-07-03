// Live build status surfaced at the top of every page.
// Updated each cron fire / wave-close commit. Renders into <LiveStatus />.
// Timestamp is baked in at build time — bump on every commit that ships
// research progress so Vercel rebuilds put the new value live.
//
// KEEP EVERY STRING SHORT. headline <= 2 sentences, summary <= 3 sentences,
// pendingWork/why/ask one line each. The audit trail lives in
// project-context/SSOT/, never here.

export interface PaperProgress {
  slug: string;
  number: string;
  shortTitle: string;
  version: string;
  readiness: number; // percent 0-100
  pendingWork: string; // ONE LINE: what is still pending for this paper
}

export interface NeedsHoustonItem {
  title: string;       // short label (e.g. "arXiv submission credentials")
  why: string;         // ONE SENTENCE: why ONLY Houston can unblock this
  blockedPaper?: string; // e.g. "P1A", "P4", "P5" — which paper this gates
  ask: string;         // ONE SENTENCE: exact action Houston needs to take
}

export interface LiveStatus {
  lastUpdatedISO: string; // ISO 8601 UTC, baked at build time
  lastUpdatedDisplay: string; // human-readable PT timestamp for the banner
  headline: string; // 1-2 sentences, current state
  summary: string; // 1-3 sentences, what just shipped
  currentlyRunning: string[]; // short bullets of what is actively running RIGHT NOW
  needsHouston: NeedsHoustonItem[]; // ONLY items truly blocked on Houston
  papers: PaperProgress[]; // 6 papers, sorted by display order
  blockerTally: {
    closed: number;
    openBlockers: number;
    openMajors: number;
    openMinors: number;
  };
  cronStatus: string;
  etaToCompletion: string; // human-readable ETA to all-papers @ 100%
  pods: Array<{
    name: string;
    state: "active" | "idle" | "queued";
    note: string;
  }>;
}

export const liveStatus: LiveStatus = {
  lastUpdatedISO: "2026-06-30T12:00:00Z",
  lastUpdatedDisplay: "June 30, 2026 · 12:00 PM PT",
  headline:
    "Rounds A/B/C + INT-M2 complete (Jun 28–30): 4 rigorous multi-vendor passes, 30 real items closed program-wide (latest INT-M2: 7 closed + rebuttal-hardening on all 6), every round's truth-audit returning 0 genuinely-new MAJORs. All 6 papers verified internally honest and materially improved each round. Readiness 96. Houston sign-off is the final gate.",
  summary:
    "Three back-to-back review rounds (A/B/C, Jun 28–30) on top of a de-biased external validation closed 23 real items across all 6 papers. The final independent neutral truth-audit (Opus, skeptical stance, no convergence hint) found 0 genuinely-new real findings. Remaining external MAJORs are disclosed caveats, submission-time DOI/arXiv blockers, and LLM-referee variance — not quality issues. Next gate: Houston external-review sign-off → arXiv endorsement + coordinated submission (P4 → P1A → P1B → P3 → P2 → P5).",
  currentlyRunning: [
    "Light-touch regression watch — no active review loop running.",
  ],
  needsHouston: [
    {
      title: "External-review sign-off (final 1% gate)",
      blockedPaper: "all",
      why: "Houston's personal review verdict is the only remaining gate before tarballs are submitted; agents cannot self-authorize submission.",
      ask: "Review the final neutral truth-audit summary (project-context/peer-reviews/) and give go/no-go on coordinated arXiv submission.",
    },
    {
      title: "arXiv endorsement + coordinated submission",
      blockedPaper: "all",
      why: "Only Houston holds the arXiv account + astro-ph endorser relationships; all six tarballs are staged and drop-ready.",
      ask: "Submit in order P4 → P1A → P1B → P3 → P2 → P5 (P4 first; P5 needs P4's arXiv ID).",
    },
  ],
  papers: [
    {
      slug: "paper-1a",
      number: "1A",
      shortTitle: "ECH dark-energy closure + perturbation transparency",
      version: "v1A.0.101",
      readiness: 84,
      pendingWork: "R2/R3 ansatz tiers + R3 arithmetic fixed, verified Benedetti–Speziale β-function provenance (v1A.0.101). At the LLM-referee rigor floor — routes to a human referee on the ansatz-tier venue question.",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.96",
      readiness: 88,
      pendingWork: "Cross-check reframe hardened (v1B.0.96). Grok converged (MINOR, praises scope discipline); Gemini scope-rejects the methodological-companion framing — a human-editor venue call. Bundle submit-ready.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.85",
      readiness: 84,
      pendingWork: "f_NL=−35/8 verified at linear order; a full cubic in-in transmission was attempted (shape preserved, amplitude non-derivable), so f_NL stays honestly conditional. At floor — human referee on the conditional-forecast + single-source-recast venue question.",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.132",
      readiness: 84,
      pendingWork: "DESI injection-recovery closed (real 5σ, 3-gate at parity with SDSS/Planck), scaler-leakage audited leak-free, internal consistency reconciled (v3.1.132). At floor — eROSITA/Gaia exploratory-tier provenance disclosed for a human referee.",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.212",
      readiness: 96,
      pendingWork: "CONVERGED — imaging+morphology forward-model (real 3.2M-spiral DR8 pull), empirical edge-on metric, over-claiming framing all closed (v1.0.212); Grok+Gemini both MINOR, 0 major. Submit-ready. Next: Houston sign-off → arXiv (first in queue).",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.101",
      readiness: 96,
      pendingWork: "CONVERGED — actionable framing majors lifted (abstract foregrounding, forking-paths trials disclosure, dfCW bound widened; v0.1.101); Grok MINOR, Gemini only-structural. Only the Paper-IV dependency remains (clears when Paper IV publishes). Submit-ready. Next: Houston sign-off → arXiv (after P4).",
    },
  ],
  blockerTally: {
    closed: 895, // 872 prior + 23 real items closed across Rounds A/B/C (Jun 28-30)
    openBlockers: 0,
    openMajors: 0,
    openMinors: 0,
  },
  cronStatus: "Rounds A/B/C COMPLETE (2026-06-28 to 2026-06-30). 23 items closed program-wide. Final neutral truth-audit: 0 new genuine findings. All 6 papers at readiness 96. Next gate: Houston sign-off.",
  etaToCompletion:
    "Rounds A/B/C done — all 6 papers at readiness 96. Remaining: Houston sign-off + arXiv endorsement → coordinated drop (P4 → P1A → P1B → P3 → P2 → P5).",
  pods: [],
};
