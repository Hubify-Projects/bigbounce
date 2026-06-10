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
  lastUpdatedISO: "2026-06-10T19:00:00Z",
  lastUpdatedDisplay: "June 10, 2026 · 12:00 PM PT",
  headline:
    "R24conf wave closed: ~110 verified findings closed across all six papers — including 2 substantive P2 physics fixes (QSFI endpoints, −35/16 attribution) and a P5 join-bug fix — all six bumped (P1A v1A.0.52 · P1B v1B.0.53 · P2 v1.7.47 · P3 v3.1.82 · P4 v1.0.169 · P5 v0.1.54); next gate is R25conf (P2+P4 priority; P4 needs 2 clean) + a pod session for queued recomputes.",
  summary:
    "R24conf closures: P1A 1.06σ recompute fix + Λ_eff curvature-units declared + 10⁻⁵⁸ band relabeled; P1B S8 marginal corrected 0.831±0.018→0.827±0.010 (chain-recomputed) + cosθ-prior robustness + S8/DES-Y3 overlay (2.6σ); P2 QSFI endpoints corrected per Chen–Wang + −35/16 re-attributed to Li–Quintin–Wang–Cai (17 sites) + c9k continuous-GR BF=6.0; P3 eROSITA 0.259 threshold-axis irreproducibility disclosed; P4 7 local recomputes closed (confidence-cut z +4.27→+0.41, A_dip 95% UL 6.8e-3, conditioning 3.17); P5 ZONEVOID zone-offset bug fixed (104,912/74,111 void counts, conclusion unchanged).",
  currentlyRunning: [
    "Hourly native-PDF cross-vendor review autoloop on all 6 papers (Claude · GPT · Gemini · Grok · Perplexity + meta-reviewer)",
    "Persistence tracker fingerprinting findings across fires; load-bearing items escalate to Houston decision package",
    "Site + SSOT + Convex sync on every paper version bump",
  ],
  needsHouston: [
    {
      title: "Anthropic API credits exhausted (reviewer leg down)",
      blockedPaper: "all",
      why: "The Claude API reviewer leg is still down on billing 400s; R23conf/R24conf ran their Claude legs in-session on subscription as a workaround, but the autoloop needs API credits for R25conf.",
      ask: "Top up API credits at console.anthropic.com → Plans & Billing, then say 'credits topped up' so full 5-vendor rounds restart.",
    },
    {
      title: "External review round on current versions",
      blockedPaper: "all",
      why: "The agent-side review loop has run; the orthogonal external pass is Houston's per his 2026-06-08 plan.",
      ask: "Run your external round on the current PDFs and send back findings for truth-audit.",
    },
    {
      title: "Personal sign-off, paper by paper",
      blockedPaper: "all",
      why: "The final 1% of readiness is reserved for Houston's judgment — no agent can award it.",
      ask: "Read each paper end-to-end and reply 'sign off PN' or send blocking findings.",
    },
    {
      title: "arXiv endorsement + submission credentials",
      blockedPaper: "all",
      why: "Only Houston has the arXiv account and astro-ph endorser relationships.",
      ask: "Submit each signed-off paper (recommended order P4 → P1A+P1B → P3 → P2 → P5); tarballs are prepared.",
    },
  ],
  papers: [
    {
      slug: "paper-1a",
      number: "1A",
      shortTitle: "ECH dark-energy closure + perturbation transparency",
      version: "v1A.0.52",
      readiness: 93,
      pendingWork: "v1A.0.52 — R24conf clean-after-closures (1.06σ recompute fix, Λ_eff units, 10⁻⁵⁸ band relabel) → MCS derivation appendix (#32) → Houston external round + sign-off → arXiv",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.53",
      readiness: 92,
      pendingWork: "v1B.0.53 — R24conf clean-after-closures (S8 0.827±0.010 corrected, c10 BB-template, cosθ-prior, DES-Y3 overlay) → release-pairing MCMC (#29, pod) → sign-off → arXiv (with P1A)",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.47",
      readiness: 92,
      pendingWork: "v1.7.47 — R24conf closed 2 substantive fixes (QSFI endpoints per Chen–Wang, −35/16 re-attributed to Li–Quintin–Wang–Cai, c9k BF=6.0) → R25conf must come back clean (priority) → Houston sign-off → arXiv",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.82",
      readiness: 90,
      pendingWork: "v3.1.82 — R24conf closed (eROSITA 0.259 axis irreproducibility disclosed, abstract framing upgrades) → queue #33 production re-derivation → next round clean → HF flip → arXiv",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.169",
      readiness: 85,
      pendingWork: "v1.0.169 — R24conf closed 7 local recomputes (confidence-cut z +4.27→+0.41, A_dip 95% UL 6.8e-3, conditioning 3.17) → pod items (#4/5/9/11–13) → TWO clean rounds R25conf+ (priority) → sign-off → arXiv (first in queue)",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.54-2026-06-10",
      readiness: 90,
      pendingWork: "v0.1.54 — R24conf closed 6 local recomputes + ZONEVOID join-bug fix (104,912/74,111 void counts, σ −0.52/−1.50, conclusion unchanged) → pod field rebuilds (#15–19) → next round clean → arXiv (last, after P4)",
    },
  ],
  blockerTally: {
    closed: 677, // 567 through R23conf + ~110 verified R24conf findings closed 2026-06-10
    openBlockers: 0,
    openMajors: 0,
    openMinors: 0,
  },
  cronStatus: "autonomous review loop active — hourly fires",
  etaToCompletion:
    "All six papers targeted publishable ~June 12–13, 2026 (per SSOT/PUBLISH_PLAN.md). Gated on Houston external round + sign-off; the final 1% is Houston-only.",
  pods: [],
};
