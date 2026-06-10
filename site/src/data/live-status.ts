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
  lastUpdatedISO: "2026-06-11T05:30:00Z",
  lastUpdatedDisplay: "June 10, 2026 · 10:30 PM PT",
  headline:
    "Pod session closed the queued recomputes — P4 v1.0.171 · P3 v3.1.84 · P5 v0.1.56 bumped (P1A v1A.0.53 · P1B v1B.0.53 · P2 v1.7.48 unchanged). P3 catalog-grade count corrected to 269,317 (LAMOST-overlap double-removal fixed); P4 + P2 remain SIGN-OFF-READY awaiting Houston.",
  summary:
    "Pod wave: P4 unthresholded injection floors A50=0.36%/A95=0.63% + area-uniform axis curve + threshold-sweep canonical reproduction + T7 confidence quantification (robustness additions; clean-round status unaffected); P3 6-way dedup verified 269,317/269,117 + HEALPix 38,330px unrecoverable confirmed (reproducible rerun 24,049px χ²_ν=15.7) + SMICA preprocessing documented (200/200); P5 stratified Phase-2 LEE p=0.36/0.27 + void-membership null + z-tail no-op. P1B release-pairing MCMC running on pod (ETA 1–2 days).",
  currentlyRunning: [
    "Hourly native-PDF cross-vendor review autoloop on all 6 papers (Claude · GPT · Gemini · Grok · Perplexity + meta-reviewer)",
    "Persistence tracker fingerprinting findings across fires; load-bearing items escalate to Houston decision package",
    "Site + SSOT + Convex sync on every paper version bump",
  ],
  needsHouston: [
    {
      title: "Anthropic API credits exhausted (reviewer leg down)",
      blockedPaper: "all",
      why: "The Claude API reviewer leg is still down on billing 400s; R23conf/R24conf/R25conf ran their Claude legs in-session on subscription as a workaround, but the autoloop needs API credits for R26conf.",
      ask: "Top up API credits at console.anthropic.com → Plans & Billing, then say 'credits topped up' so full 5-vendor rounds restart.",
    },
    {
      title: "External review round on current versions",
      blockedPaper: "all",
      why: "The agent-side review loop has run; the orthogonal external pass is Houston's per his 2026-06-08 plan.",
      ask: "Run your external round on the current PDFs and send back findings for truth-audit.",
    },
    {
      title: "Personal sign-off — P4 + P2 are SIGN-OFF-READY now",
      blockedPaper: "P4, P2",
      why: "P4 completed its 2-of-2 post-retraction clean rounds and P2 came back R25conf-clean — only Houston's read stands between them and arXiv.",
      ask: "Read P4 + P2 end-to-end and reply 'sign off P4'/'sign off P2' or send blocking findings; remaining papers follow after R26conf.",
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
      version: "v1A.0.53",
      readiness: 93,
      pendingWork: "v1A.0.53 — MCS line-of-sight derivation appendix added (App C, closes the last analytic gate; queue #32 CLOSED) → R26conf (new appendix needs review coverage) → Houston sign-off → arXiv",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.53",
      readiness: 92,
      pendingWork: "v1B.0.53 — unchanged this cycle; release-pairing MCMC (#29) running on pod → R26conf → sign-off → arXiv (with P1A)",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.48",
      readiness: 95,
      pendingWork: "v1.7.48 — R25conf ROUND CLEAN (GR-degradation ~15%→~23% c9k-verified, c9l σ_theory marginalization, fig4 'BOUNCE EXCLUDED' regen, envelope relabel) → SIGN-OFF-READY, awaiting Houston → arXiv",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.84",
      readiness: 91,
      pendingWork: "v3.1.84 — catalog-grade count corrected 264,938 → 269,317 (LAMOST-overlap double-removal; 6-way dedup verified); HEALPix + SMICA reproducibility documented → R26conf clean → HF flip → arXiv",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.171",
      readiness: 95,
      pendingWork: "v1.0.171 — pod items closed (injection floors A50=0.36%/A95=0.63%, area-uniform axis curve, threshold sweep, T7 confidence); robustness additions, clean-round status unaffected → still SIGN-OFF-READY, first in submission queue → arXiv",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.56-2026-06-10",
      readiness: 92,
      pendingWork: "v0.1.56 — stratified Phase-2 LEE (p=0.36/0.27) + void-membership null + z-tail no-op (#17–19 CLOSED; #16 randoms missing, documented) → R26conf clean → arXiv (last, after P4)",
    },
  ],
  blockerTally: {
    closed: 678, // 677 through R24conf + 1 substantive R25conf catch (P4 App A field-convention); R25conf otherwise CLEAN×2 (P4+P2), 93 P4 findings audited
    openBlockers: 0,
    openMajors: 0,
    openMinors: 0,
  },
  cronStatus: "autonomous review loop active — hourly fires",
  etaToCompletion:
    "All six papers targeted publishable ~June 12–13, 2026 (per SSOT/PUBLISH_PLAN.md). Gated on Houston external round + sign-off; the final 1% is Houston-only.",
  pods: [],
};
