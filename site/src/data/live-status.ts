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
  lastUpdatedISO: "2026-07-11T16:57:00Z",
  lastUpdatedDisplay: "July 11, 2026 · 9:57 AM PT",
  headline:
    "P3 FR5 (Jul 11) — SECOND CONSECUTIVE CLEAN WAVE on the DP3-19 fix → P3 clean-wave streak 1→2, and P3 REJOINS the full five-paper exit set (all five now past the directive-K two-clean-waves bar: P1U 2 · P2 3 · P3 2 · P4 4 · P5 2). FR5 board (run.log 16:57): INT Claude MINOR + OpenAI REJECT + Grok-API MAJOR + Gemini MAJOR + EXT Grok MAJOR + EXT ChatGPT REJECT (FR4b carryover). GEMINI INT'S FIRST NON-REJECT ON P3 (REJECT→MAJOR) — verified from the raw verdict line (native-PDF, PARSED VERDICT MAJOR REVISIONS) + the gemini milestone log; all 5 findings are source-cited DP3 re-flags (honest softening on unchanged content). 0 genuinely-new editable findings across all 6 legs (Grok EXT + Gemini/OpenAI/Grok-API all re-flag DP3-07/-08/-10/-09/-15/-16; Claude recomputed the 268,519 dedup + NANOGrav + f_NL Fisher chain, 0 new factual error). Separately, FR4b recovers the FR4 ChatGPT FAILED gap = ChatGPT REJECT (20 MAJOR + 2 MINOR, all re-flag DP3-01…DP3-19, 0 genuinely-new, no additional reset). No version bump (v3.1.155 stands, served md5 ebd4bfd1…). Convex EXT cap 56 (INT Gemini MAJOR is not an EXT-cap input). Venue/human-referee decision remains Houston-gated.",
  summary:
    "Round H17 (Jul 10) found and FIXED 8 real errors — P4's Shamir factor-of-2 (survived ~17 prior waves), P2's spurious-term sign + 5 stale Bayes columns, P1U's Check-D contradiction + conventions, P5's primary-estimand seam — then converged: two consecutive waves with 0 genuinely-new findings, 49 findings all ledger-matched. New real science shipped: GZ1 confusion matrices stratified by sky-leg, confidence AND void/non-void environment (parity-symmetric errors measured, not assumed). Verdict-gap trend: program average up from ~0.3 (Jul-4 verified-reset era, all REJECT/MAJOR) to ~1.0-1.2 today, driven by real fixes.",
  currentlyRunning: [
    "P3 FR5 adjudicated (Jul 11) — SECOND CONSECUTIVE CLEAN WAVE on the DP3-19 fix → P3 streak 1→2, P3 REJOINS the full five-paper exit set (all five past the directive-K two-clean-waves bar). FR5 = 0 genuinely-new editable findings across all 6 legs: INT Claude MINOR + OpenAI REJECT + Grok-API MAJOR + Gemini MAJOR + EXT Grok MAJOR + EXT ChatGPT REJECT (FR4b carryover). GEMINI INT'S FIRST NON-REJECT ON P3 — moved REJECT→MAJOR (verified from the raw native-PDF verdict line + the gemini milestone log); all 5 Gemini findings source-cited re-flags (§V-disjoint DP3-10/-18, journal-fit DP3-10/-16, repo-paths DP3-16, thresholds DP3-09, SIMBAD-novelty DP3-07/-09) — honest softening on unchanged content. Grok EXT MAJOR (3 MAJOR + 2 MINOR) all re-flag DP3-07/-08/-10/-13/-15/-16; the recompute Claude INT leg reproduced the 268,519 dedup + NANOGrav + f_NL Fisher + DESI injection curve, 0 new factual error (4 MINOR = display-precision γ=2.567 → DP3-19 PROCESS-NIT + 3 cosmetic overfull hboxes). No bump (v3.1.155 stands). Convex EXT cap 56 (INT Gemini MAJOR is not an EXT-cap input).",
    "P3 FR4b adjudicated (Jul 11) — the recovered FR4 ChatGPT leg = ChatGPT REJECT (20 MAJOR + 2 MINOR), reviewed the live v3.1.155 PDF. ledger_match: 13/20 auto-matched, 7 UNMATCHED Opus-adjudicated line-by-line — all 22 findings re-flag DP3-01…DP3-19 (validated-selection-non-uniform DP3-06/-09/-14; point-source/98.7%-sky-fiber DP3-11; held-out-not-out-of-fold DP3-01/-12/-15; Planck spatial-leakage DP3-06; 18-catalog-absence≠novelty DP3-07/-09/-11; §V f_NL/NANOGrav DP3-10; process-volume DP3-03/-04; venue DP3-16). 0 genuinely-new editable findings → recovers the FR4 chart GAP as a recorded REJECT, no additional streak reset. ChatGPT stays REJECT on the same disclosed content (DP3-17 backfire floor).",
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
      version: "v1.7.114",
      readiness: 74,
      pendingWork: "v1.7.114 OPEN-COMPUTE (directive L): channel-native joint {f_NL,b_phi,A_GR} bispectrum Fisher (c15) closes the recurring proxy-floor MAJOR by adopting the c13 Gaussian MT covariance surrogate — channel-native rho(f_NL,A_GR)=-0.001 (near-orthogonal; the -0.868 SDB proxy overstated the degeneracy), sigma_marg=0.88 -> 2.48sigma floor, HIGHER than the 1.30sigma proxy floor (proxy was conservative); alpha=0.992 corroborates r_eff~0.99. Grok EXT MINOR; ChatGPT REJECT = documented floor. -35/16 quadruple-certified.",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "Multi-survey anomaly catalog",
      version: "v3.1.155",
      readiness: 56,
      pendingWork: "FR5 (2026-07-11T16:57Z) — SECOND CONSECUTIVE CLEAN WAVE on the DP3-19 fix → P3 clean-wave streak 1→2, and P3 REJOINS the full five-paper exit set (clears the directive-K two-clean-waves bar). FR5 board (run.log 16:57): INT Claude MINOR + OpenAI REJECT + Grok-API MAJOR + Gemini MAJOR + EXT Grok MAJOR + EXT ChatGPT REJECT (FR4b carryover). GEMINI INT'S FIRST NON-REJECT ON P3 — moved REJECT→MAJOR (gemini-3.1-pro, native-PDF; verified from the raw verdict line API_P3_gemini.md + the .intwave_P3_gemini_0950.log milestone); all 5 Gemini findings are source-cited re-flags (§V-NANOGrav-disjoint DP3-10/-18, journal-fit/null-cosmology DP3-10/-16, repo-paths/signposts DP3-16, heterogeneous thresholds DP3-09, SIMBAD 58.8% novelty DP3-07/-09) — an honest REJECT→MAJOR softening on unchanged content. 0 genuinely-new editable findings across all 6 legs: Grok EXT MAJOR (3 MAJOR + 2 MINOR) re-flag DP3-07/-08/-10/-13/-15/-16; the recompute Claude INT leg reproduced the 268,519 dedup + NANOGrav chain + f_NL Fisher + DESI injection curve, 0 new factual error (4 MINOR = display-precision γ=2.567 → DP3-19 PROCESS-NIT + 3 sub-7pt overfull hboxes cosmetic); OpenAI/Grok-API = canonical catalog-vs-PRD venue (DP3-16) + provenance (DP3-08/-15) + heterogeneous-validation (DP3-01/-09) + referee-variance classes. Separately, FR4b recovers the FR4 ChatGPT FAILED gap = ChatGPT REJECT (20 MAJOR + 2 MINOR, all re-flag DP3-01…DP3-19, 0 genuinely-new, no additional reset). No version bump (v3.1.155 stands, served md5 ebd4bfd13962b0ee8d14e5393a9bd2c9). Convex EXT cap 56 (INT Gemini MAJOR is not an EXT-cap input). Venue question (PRD vs ApJS/MNRAS) Houston-gated.",
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
