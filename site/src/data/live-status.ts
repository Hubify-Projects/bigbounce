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
  lastUpdatedISO: "2026-07-11T07:16:00Z",
  lastUpdatedDisplay: "July 11, 2026 · 12:16 AM PT",
  headline:
    "W2 WAVE ADJUDICATED — 4 OF 5 PAPERS PAST THE BAR (Jul 11). P1U crossed the two-clean-waves convergence bar (streak 2) after its W2 Grok MINOR→MAJOR was truth-audited as pattern-066 verdict-word oscillation on unchanged v1U.0.12 — 0 genuinely-new. Only P5 remains below the bar — its wave W3 is now clean (streak 1/2 after the W3-EXT close-out surfaced 0 genuinely-new reader-visible findings; one more clean wave to cross). The program is FIVE papers — P1B merged into the unified Paper 1. Grok EXT has returned literal ACCEPTs on P5 (v0.1.117) and P4 (v1.0.235) — the program's first two external ACCEPTs — while ChatGPT/OpenAI hold their documented REJECT floor (pattern-066).",
  summary:
    "Round H17 (Jul 10) found and FIXED 8 real errors — P4's Shamir factor-of-2 (survived ~17 prior waves), P2's spurious-term sign + 5 stale Bayes columns, P1U's Check-D contradiction + conventions, P5's primary-estimand seam — then converged: two consecutive waves with 0 genuinely-new findings, 49 findings all ledger-matched. New real science shipped: GZ1 confusion matrices stratified by sky-leg, confidence AND void/non-void environment (parity-symmetric errors measured, not assumed). Verdict-gap trend: program average up from ~0.3 (Jul-4 verified-reset era, all REJECT/MAJOR) to ~1.0-1.2 today, driven by real fixes.",
  currentlyRunning: [
    "W3 EXT wave adjudicated (Jul 11) — wave W3 complete on P5: 0 genuinely-new reader-visible findings (Grok MINOR / ChatGPT REJECT both source-cited re-flags of the standing DP5-22 presentation/cross-match D-round class). P5 (v0.1.120) posts its first clean wave (streak 1/2) under the new no-reset-for-process-nits rule. One more clean wave to the two-clean-waves bar, then the wave-1 arXiv kit is handed to Houston.",
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
      pendingWork: "CROSSED the two-clean-waves bar (streak 2, HELD at W2b). W2b EXT: ChatGPT re-sweep of v1U.0.12 = REJECT, 15 MAJOR+2 MINOR, all source-cited re-flags (DP1U-03/-05/-08/-09/-10/-12/-14/-15/-17/-20/-22), 0 genuinely-new — the documented ChatGPT harsh-referee floor. W2 EXT: Grok MINOR→MAJOR was truth-audited as pattern-066 verdict-word oscillation on unchanged v1U.0.12 — all source-cited re-flags, 0 genuinely-new. (W1 INT had caught + fixed the Check-D script/abstract sync in v1U.0.12.)",
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
      version: "v0.1.120-2026-07-10",
      readiness: 68,
      pendingWork: "W3-EXT close-out (Jul 11) — wave W3 complete: 0 genuinely-new reader-visible findings. W3-EXT verdicts: Grok MINOR + ChatGPT REJECT, both source-cited re-flags of the standing DP5-22 presentation/cross-match D-round class (Grok 'overall-presentation length/condensation'; ChatGPT '§III C angular-cross-match/match-radius' — both already disclosed: cross-match §method l.1339-1367 + match-radius row in tab:systematic_budget); 1 parser-noise fragment. No bump (v0.1.120 stands). The W3-INT PROCESS-NIT (missing dedicated v0.1.118/119 changelog block, comment-only) was closed in v0.1.120 and left as-recorded (pre-rule streak reset). P5 posts streak 1/2 — first clean wave under the 2026-07-11 no-reset-for-process-nits rule. First EXT ACCEPT of the program (Grok, v0.1.117) + Claude INT ACCEPT. One more clean wave to the two-clean-waves bar.",
    },
  ],
  blockerTally: {
    closed: 920,
    openBlockers: 0,
    openMajors: 6, // latest-per-reviewer verdict words below MINOR: ChatGPT REJECT x5 (documented floor) + OpenAI INT REJECT class -- all ledger-dispositioned re-flags, 0 genuinely-new open
    openMinors: 8, // Grok/Claude MINOR lists -- all ledger re-flags of disclosed limitations
  },
  cronStatus: "W3-EXT wave adjudicated (2026-07-11): P5 wave W3 complete — 0 genuinely-new reader-visible findings (Grok MINOR / ChatGPT REJECT both source-cited re-flags of the standing DP5-22 presentation/cross-match D-round class). No bump (v0.1.120 stands). The W3-INT PROCESS-NIT changelog block (comment-only) was closed in v0.1.120 and left as-recorded; P5 posts its first clean wave (streak 1) under the 2026-07-11 no-reset-for-process-nits rule. Streaks: P1U 2, P2 3, P3 4, P4 4, P5 1. Loop cadence ~2h/wave with the tooling (ext_submit/ext_harvest/int_wave/ledger_match/directive_g).",
  etaToCompletion:
    "Submission-ready = two consecutive 0-genuinely-new waves per paper (directive K). P1U/P2/P3/P4 are past the bar; only P5 needs one clean wave (~2-4h of loop time, assuming no new findings — a genuinely-new finding resets that paper). Then: Houston's arXiv wave-1 clicks (same day) and human journal referees (months, external). Live ETA on the homepage widget.",
  pods: [],
};
