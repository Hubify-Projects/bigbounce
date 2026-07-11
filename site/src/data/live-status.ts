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
  lastUpdatedISO: "2026-07-11T16:15:00Z",
  lastUpdatedDisplay: "July 11, 2026 · 9:15 AM PT",
  headline:
    "P3 FR3 (Jul 11) — 1 GENUINELY-NEW correctable finding → P3 clean-wave streak RESET 1→0; P3 is NOT in the exit set. The recompute-verifying Claude INT leg caught a matter-bounce/SMBHB parameter-shift precision inconsistency: the v3.1.154 SMBHB fix moved to full-precision +4.63σ but its matter-bounce partner was left at display-precision +1.13σ in the same clause (committed chain matter_bounce_3p0=1.13543 → +1.14σ). Fixed at all 7 reader-visible sites + F₀ 0.01239→0.01240 (σ=8.14, envelope [3.92,8.98] UNCHANGED) → v3.1.155 (DP3-19), directive-G verified (37pp, 0 undef-refs, served mirrors byte-identical). Every EXT/API MAJOR/REJECT is a canonical DP3 re-flag (PRD-venue, validation-heterogeneity, process-volume, provenance) — referee variance, not new. P3 must post another clean wave to rebuild toward the two-clean-waves bar. Current streaks: P1U 2 · P2 3 · P3 0 · P4 4 · P5 2. Venue/human-referee decision remains Houston-gated.",
  summary:
    "Round H17 (Jul 10) found and FIXED 8 real errors — P4's Shamir factor-of-2 (survived ~17 prior waves), P2's spurious-term sign + 5 stale Bayes columns, P1U's Check-D contradiction + conventions, P5's primary-estimand seam — then converged: two consecutive waves with 0 genuinely-new findings, 49 findings all ledger-matched. New real science shipped: GZ1 confusion matrices stratified by sky-leg, confidence AND void/non-void environment (parity-symmetric errors measured, not assumed). Verdict-gap trend: program average up from ~0.3 (Jul-4 verified-reset era, all REJECT/MAJOR) to ~1.0-1.2 today, driven by real fixes.",
  currentlyRunning: [
    "GEM1-INT adjudicated (Jul 11) — 7TH REVIEWER ONLINE: the first-ever verified Gemini INT verdicts (gemini-3.1-pro-preview, native-PDF) landed across all five papers — P5/P4/P2 MINOR · P1U MAJOR · P3 REJECT. Full source-cited truth-audit: 0 genuinely-new reader-visible editable findings on any paper (every finding → a standing D-id; P3's REJECT is the known catalog-vs-PRD venue class DP3-08/-10/-16). A fresh zero-history reviewer independently reproducing the already-disclosed limitation classes is the honest stress-test of the exit PASSING. (Superseded for P3: FR3 later RESET P3 4→…→0 on a genuinely-new precision finding; current streaks P1U 2 · P2 3 · P3 0 · P4 4 · P5 2.)",
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
      version: "v1U.0.13",
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
      version: "v3.1.155",
      readiness: 62,
      pendingWork: "FR3 (2026-07-11) INT-Claude wave-2 truth-audit surfaced 1 GENUINELY-NEW reader-visible correctable finding → P3 clean-wave streak RESET 1→0; P3 is NOT in the exit set. Closed same-bundle in v3.1.155 (DP3-19): (1) [genuinely-new] matter-bounce parameter-shift precision made consistent with the v3.1.154 SMBHB fix — SMBHB moved to full-precision +4.63σ but its matter-bounce partner was left at display-precision +1.13σ in the same clause; committed chain matter_bounce_3p0=1.13543 → +1.14σ, updated all 7 reader-visible sites; (2) [cosmetic companion] F_0 last-digit 0.01239→0.01240 (downstream 0.01509→0.01510; σ=8.14 and envelope [3.92,8.98] UNCHANGED). Both verified against savage_dickey JSON, no fabrication. INT verdicts openai/grok/gemini/claude = REJECT/MAJOR/REJECT/MINOR; EXT grok/chatgpt = MAJOR/REJECT; every MAJOR/REJECT is a canonical DP3 re-flag (venue PRD-vs-ApJS DP3-16, validation-heterogeneity, process-volume DP3-07, LAMOST bias, eROSITA provenance) — referee variance, not new. directive-G verified (3-way md5, 37pp, 0 undef-refs, 0 overfull). Clock restarts; two clean waves from here. Venue question Houston-gated.",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.236",
      readiness: 74,
      pendingWork: "CROSSED the bar (streak 4) + Grok EXT literal ACCEPT (W1) + Claude INT ACCEPT. Shamir factor-of-2 REAL error fixed this round (A_ref 0.017, z -7.6); stratified confusion matrices measured and integrated. ChatGPT REJECT = documented floor.",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.121-2026-07-11",
      readiness: 80,
      pendingWork: "CROSSED the two-clean-waves bar (streak 2). W4-INT confirm wave (Jul 11): 0 genuinely-new reader-visible findings across INT Claude MINOR / OpenAI MAJOR / Grok MINOR. NEW — OpenAI moved REJECT → MAJOR on P5, its first non-REJECT (native-PDF v0.1.120, INT_v3/ROUND_2026-07-09/API_P5_openai.md). All 8 OpenAI real UNMATCHED = source-cited re-flags (footprint≠selection-mask DP5-06, 2a−1 under-powered void arm DP5-08/-09, duplicate-TARGETID/T-Web DP5-14, fragmented multiplicity DP5-04/-19, abstract-length/Fig-legibility/N_MC DP5-22, DOI-at-acceptance DP5-18/-21); Grok's 2 + Claude's residual all re-flags or parser noise. No bump (v0.1.120 stands, comment-only wave). First EXT ACCEPT of the program (Grok, v0.1.117) + Claude INT ACCEPT.",
    },
  ],
  blockerTally: {
    closed: 920,
    openBlockers: 0,
    openMajors: 6, // latest-per-reviewer verdict words below MINOR: ChatGPT REJECT x5 (documented floor) + OpenAI INT REJECT class -- all ledger-dispositioned re-flags, 0 genuinely-new open
    openMinors: 8, // Grok/Claude MINOR lists -- all ledger re-flags of disclosed limitations
  },
  cronStatus: "FR1 fresh full-board round adjudicated (2026-07-11): INT (openai/grok/gemini/claude) + EXT-Grok on the July-11 restamps (no content change since exit); EXT ChatGPT+Gemini FAILED-dead (rate-limit) → chart GAPs. 4 of 5 papers clean (streaks P1U 2→3, P2 3→4, P4 4→5, P5 2→3, all HOLD past the bar). P3 RESET 4→0: Claude-INT caught a genuinely-new reader-visible mis-round (NANOGrav SMBHB shift +4.61→+4.63σ), fixed same-bundle → v3.1.154 (directive-G verified). MILESTONE: OpenAI-INT returned MAJOR-REVISIONS on P4 — its FIRST non-REJECT on that paper. Oscillations P1U Grok MINOR→REJECT + P5 Claude MINOR→MAJOR = pattern-066 variance on unchanged content, not new findings. No ACCEPT faked, no finding dismissed without a source-cited verdict, no math fabricated. FR1b ChatGPT-retry (2026-07-11) recovered the rate-limit GAP: EXT ChatGPT = P1U REJECT · P2 REJECT · P3 REJECT · P4 REJECT · P5 MAJOR-REVISIONS. 0 genuinely-new reader-visible editable findings on any paper — all source-cited re-flags of the DISPOSITIONS ledger; no streak resets (P1U 3 · P2 4 · P3 0 · P4 5 · P5 3 HOLD). P5's ChatGPT tier-lift REJECT→MAJOR (floor-crack) HOLDS on the restamp → P5 cap 74→80. P3's NANOGrav ChatGPT finding is a scope re-flag; the +4.61→+4.63σ arithmetic was already fixed in v3.1.154 (DP3-18).",
  etaToCompletion:
    "PROGRAM PAST THE CONVERGENCE BAR — wave-1 kit verified. Two independent clocks remain, both external to the loop. arXiv clock: the rebuilt + standalone-verified kit is a set of Houston submission clicks away (minutes) — walk submissions/WAVE1_SUBMIT_WALKTHROUGH.md. Journal clock: human referees (months). No further autonomous editing clears the disclosed venue/scope items.",
  pods: [],
};
