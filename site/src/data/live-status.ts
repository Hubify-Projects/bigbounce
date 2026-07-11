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
  lastUpdatedISO: "2026-07-11T04:30:00Z",
  lastUpdatedDisplay: "July 10, 2026 · 9:30 PM PT",
  headline:
    "W1 WAVE CLEAN ON 4 OF 5 PAPERS (Jul 10-11). The program is now FIVE papers — P1B is merged into the unified Paper 1 (Houston-approved, reviewer-recommended). P2, P3 and P4 have crossed the two-clean-waves convergence bar (directive K); P1U and P5 each need one more clean wave. Grok EXT has returned literal ACCEPTs on P5 (v0.1.117) and P4 (v1.0.235) — the program's first two external ACCEPTs — while ChatGPT/OpenAI hold their documented REJECT floor (pattern-066).",
  summary:
    "Round H17 (Jul 10) found and FIXED 8 real errors — P4's Shamir factor-of-2 (survived ~17 prior waves), P2's spurious-term sign + 5 stale Bayes columns, P1U's Check-D contradiction + conventions, P5's primary-estimand seam — then converged: two consecutive waves with 0 genuinely-new findings, 49 findings all ledger-matched. New real science shipped: GZ1 confusion matrices stratified by sky-leg, confidence AND void/non-void environment (parity-symmetric errors measured, not assumed). Verdict-gap trend: program average up from ~0.3 (Jul-4 verified-reset era, all REJECT/MAJOR) to ~1.0-1.2 today, driven by real fixes.",
  currentlyRunning: [
    "W2 confirm wave queues next: P1U (v1U.0.12, streak 1/2) + P5 (v0.1.118, streak 1/2) — the last two clean waves before the wave-1 arXiv kit is handed to Houston.",
    "Live ETA + verdict-trajectory chart now on this page + /reviews, fed by readinessMetrics on every wave.",
  ],
  needsHouston: [
    {
      title: "Billed Gemini API key",
      blockedPaper: "all",
      why: "Browser Gemini is hard-throttled (silent upload drops); the missing reviewer leg on both remaining waves needs the API.",
      ask: "Provision a billing-enabled Gemini API key and drop it in .env.local as GEMINI_API_KEY.",
    },
    {
      title: "arXiv wave-1 submission clicks",
      blockedPaper: "P4, P3, P2",
      why: "Kit is rebuilt and standalone-verified against the final versions; only Houston holds the arXiv account.",
      ask: "Walk submissions/WAVE1_SUBMIT_WALKTHROUGH.md when the last two clean waves land (site ETA is live).",
    },
    {
      title: "Send the Cai courtesy email",
      blockedPaper: "P2",
      why: "The -35/16 certification note is drafted do-not-send; only Houston sends author correspondence.",
      ask: "Review research/focused_paper_source_integration/CAI_COURTESY_EMAIL_DRAFT.md and send.",
    },
  ],
  papers: [
    {
      slug: "paper-1a",
      number: "1U",
      shortTitle: "Unified Paper 1 — ECH constraints + reproducibility (P1B merged in)",
      version: "v1U.0.12",
      readiness: 62,
      pendingWork: "Streak 1/2 after an honest reset: the W1 INT leg caught the Check-D sign fix un-propagated to the cited script + abstract (fixed v1U.0.12, script re-run PASS). W1 EXT: Grok MAJOR→MINOR, ChatGPT REJECT (all ledger re-flags). One more clean wave to the bar.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/16 SPHEREx forecast + Cai-Li certification",
      version: "v1.7.112",
      readiness: 74,
      pendingWork: "CROSSED the two-clean-waves bar (streak 3). Grok EXT: 'Accept with minor revisions' then MINOR after closures; Claude INT hand-verified every fraction ('no computational error, no fabrication'). ChatGPT REJECT = documented floor. -35/16 quadruple-certified.",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "Multi-survey anomaly catalog",
      version: "v3.1.152",
      readiness: 62,
      pendingWork: "CROSSED the bar (streak 4). W1 EXT: Grok MAJOR→MINOR. Honest three-gate downgrade + provenance reconciliations shipped this round. Venue question (PRD vs ApJS/MNRAS) is Houston-gated, not editable.",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.235",
      readiness: 74,
      pendingWork: "CROSSED the bar (streak 4) + Grok EXT literal ACCEPT (W1) + Claude INT ACCEPT. Shamir factor-of-2 REAL error fixed this round (A_ref 0.017, z -7.6); stratified confusion matrices measured and integrated. ChatGPT REJECT = documented floor.",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.118",
      readiness: 68,
      pendingWork: "Streak 1/2 (reset only because v0.1.118 added NEW content: the void-stratified confusion measurement, void N=933 asymmetry -0.023 +/- CI, p=0.37). First EXT ACCEPT of the program (Grok, v0.1.117) + Claude INT ACCEPT. One more clean wave to the bar.",
    },
  ],
  blockerTally: {
    closed: 920,
    openBlockers: 0,
    openMajors: 6, // latest-per-reviewer verdict words below MINOR: ChatGPT REJECT x5 (documented floor) + OpenAI INT REJECT class -- all ledger-dispositioned re-flags, 0 genuinely-new open
    openMinors: 8, // Grok/Claude MINOR lists -- all ledger re-flags of disclosed limitations
  },
  cronStatus: "W1 wave adjudicated clean (2026-07-11): 0 genuinely-new findings on all 4 audited papers; P4 Grok EXT ACCEPT verified from raw. Streaks: P1U 1, P2 3, P3 4, P4 4, P5 1. Loop cadence ~2h/wave with the new tooling (ext_submit/ext_harvest/int_wave/ledger_match/directive_g).",
  etaToCompletion:
    "Submission-ready = two consecutive 0-genuinely-new waves per paper (directive K). P2/P3/P4 are past the bar; P1U and P5 need one clean wave each (~2-4h of loop time, assuming no new findings — a genuinely-new finding resets that paper). Then: Houston's arXiv wave-1 clicks (same day) and human journal referees (months, external). Live ETA on the homepage widget.",
  pods: [],
};
