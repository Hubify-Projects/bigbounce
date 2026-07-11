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
  lastUpdatedISO: "2026-07-11T08:55:00Z",
  lastUpdatedDisplay: "July 11, 2026 · 1:55 AM PT",
  headline:
    "PROGRAM PAST THE CONVERGENCE BAR — wave-1 kit verified, awaiting Houston submission clicks. All five papers (P1U/P2/P3/P4/P5) are past the directive-K two-clean-waves bar; the edit-loop program has EXITED. Streaks: P1U 2 · P2 3 · P3 4 · P4 4 · P5 2. The wave-1 arXiv kit (P4 → P3 → P2) plus the wave-2 P5 + P1U bundles are rebuilt at the exit versions and standalone-compile-verified (0 errors, 0 undef-refs; each tarball's .tex byte-matches the repo source; P4/P3 unchanged since Jul-10, P2/P5/P1U rebuilt to v1.7.113 / v0.1.120 / v1U.0.12). Grok EXT returned literal ACCEPTs on P5 (v0.1.117) and P4 (v1.0.235) — the program's first two external ACCEPTs; Claude INT ACCEPTed P4 and P5. Remaining work is two Houston-gated clocks: arXiv wave-1 submission clicks (minutes) and human journal referees (months).",
  summary:
    "Round H17 (Jul 10) found and FIXED 8 real errors — P4's Shamir factor-of-2 (survived ~17 prior waves), P2's spurious-term sign + 5 stale Bayes columns, P1U's Check-D contradiction + conventions, P5's primary-estimand seam — then converged: two consecutive waves with 0 genuinely-new findings, 49 findings all ledger-matched. New real science shipped: GZ1 confusion matrices stratified by sky-leg, confidence AND void/non-void environment (parity-symmetric errors measured, not assumed). Verdict-gap trend: program average up from ~0.3 (Jul-4 verified-reset era, all REJECT/MAJOR) to ~1.0-1.2 today, driven by real fixes.",
  currentlyRunning: [
    "GEM1-INT adjudicated (Jul 11) — 7TH REVIEWER ONLINE: the first-ever verified Gemini INT verdicts (gemini-3.1-pro-preview, native-PDF) landed across all five papers — P5/P4/P2 MINOR · P1U MAJOR · P3 REJECT. Full source-cited truth-audit: 0 genuinely-new reader-visible editable findings on any paper (every finding → a standing D-id; P3's REJECT is the known catalog-vs-PRD venue class DP3-08/-10/-16). A fresh zero-history reviewer independently reproducing the already-disclosed limitation classes is the honest stress-test of the exit PASSING. All five clean-wave streaks HOLD (P1U 2 · P2 3 · P3 4 · P4 4 · P5 2); no version bumps.",
    "W4-EXT confirm half adjudicated (Jul 11) — the EXT leg of the exit wave CONFIRMS P5's crossing: Grok EXT MINOR + ChatGPT EXT MAJOR REVISIONS on v0.1.120 surfaced 0 genuinely-new reader-visible findings (2 parser-noise headers + ChatGPT footprint≠selection-mask/covariate-control → DP5-06/DP5-19 + non-rejection-not-independence/Table-XVI-residual → DP5-19/DP5-13, all source-cited re-flags). P5's clean-wave streak HOLDS at 2. ChatGPT EXT moved REJECT → MAJOR — its first non-REJECT EXT verdict on P5.",
    "W4-INT confirm wave adjudicated (Jul 11) — P5 (v0.1.120) posts its SECOND consecutive clean wave (streak 2) and CROSSES the two-clean-waves bar: 0 genuinely-new reader-visible findings across INT Claude MINOR / OpenAI MAJOR / Grok MINOR (13 source-cited re-flags + 4 parser-noise fragments). OpenAI moved REJECT → MAJOR on P5 — its first non-REJECT here. All five papers are now past the bar; the edit-loop program exits and the wave-1 arXiv kit + human-referee handoff are Houston-gated.",
    "Live ETA + verdict-trajectory chart on this page + /reviews, fed by readinessMetrics on every wave.",
  ],
  needsHouston: [
    {
      title: "arXiv wave-1 submission clicks",
      blockedPaper: "P4, P3, P2",
      why: "Kit is rebuilt and standalone-verified against the final versions; all five papers are now past the two-clean-waves bar, so nothing further blocks submission; only Houston holds the arXiv account.",
      ask: "Walk submissions/WAVE1_SUBMIT_WALKTHROUGH.md — all clean waves have landed (site ETA is live).",
    },
    {
      title: "Send the Cai courtesy email",
      blockedPaper: "P2",
      why: "The -35/16 certification note is drafted do-not-send; only Houston sends author correspondence.",
      ask: "Review research/focused_paper_source_integration/CAI_COURTESY_EMAIL_DRAFT.md and send.",
    },
    {
      title: "P3 venue decision — PRD vs ApJS vs MNRAS",
      blockedPaper: "P3",
      why: "Three of five reviewers (Gemini INT, ChatGPT EXT, OpenAI INT) independently converged on 'catalog paper, wrong venue for PRD' — a Houston-gated routing call, not an editable defect.",
      ask: "Read submissions/P3_VENUE_DECISION.md and pick a lane (recommended: ApJS; science + arXiv categories unchanged, ~30-min format conversion if not PRD).",
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
      version: "v1.7.113",
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
      pendingWork: "CROSSED the two-clean-waves bar (streak 2). W4-INT confirm wave (Jul 11): 0 genuinely-new reader-visible findings across INT Claude MINOR / OpenAI MAJOR / Grok MINOR. NEW — OpenAI moved REJECT → MAJOR on P5, its first non-REJECT (native-PDF v0.1.120, INT_v3/ROUND_2026-07-09/API_P5_openai.md). All 8 OpenAI real UNMATCHED = source-cited re-flags (footprint≠selection-mask DP5-06, 2a−1 under-powered void arm DP5-08/-09, duplicate-TARGETID/T-Web DP5-14, fragmented multiplicity DP5-04/-19, abstract-length/Fig-legibility/N_MC DP5-22, DOI-at-acceptance DP5-18/-21); Grok's 2 + Claude's residual all re-flags or parser noise. No bump (v0.1.120 stands, comment-only wave). First EXT ACCEPT of the program (Grok, v0.1.117) + Claude INT ACCEPT.",
    },
  ],
  blockerTally: {
    closed: 920,
    openBlockers: 0,
    openMajors: 6, // latest-per-reviewer verdict words below MINOR: ChatGPT REJECT x5 (documented floor) + OpenAI INT REJECT class -- all ledger-dispositioned re-flags, 0 genuinely-new open
    openMinors: 8, // Grok/Claude MINOR lists -- all ledger re-flags of disclosed limitations
  },
  cronStatus: "W4-INT confirm wave adjudicated (2026-07-11): P5 (v0.1.120) posts its SECOND consecutive clean wave (streak 2) and CROSSES the two-clean-waves bar — 0 genuinely-new reader-visible findings across INT Claude MINOR / OpenAI MAJOR / Grok MINOR (13 source-cited re-flags + 4 parser-noise fragments). OpenAI moved REJECT → MAJOR on P5, its first non-REJECT (native-PDF v0.1.120). No bump (comment-only wave, v0.1.120 stands). Streaks: P1U 2, P2 3, P3 4, P4 4, P5 2 — ALL FIVE PAST THE BAR. The edit-loop program exits; remaining work is Houston-gated.",
  etaToCompletion:
    "PROGRAM PAST THE CONVERGENCE BAR — wave-1 kit verified. Two independent clocks remain, both external to the loop. arXiv clock: the rebuilt + standalone-verified kit is a set of Houston submission clicks away (minutes) — walk submissions/WAVE1_SUBMIT_WALKTHROUGH.md. Journal clock: human referees (months). No further autonomous editing clears the disclosed venue/scope items.",
  pods: [],
};
