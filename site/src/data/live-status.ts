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
  lastUpdatedISO: "2026-07-12T06:44:23Z",
  lastUpdatedDisplay: "July 11, 2026 · 11:44 PM PT",
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
      version: "v1U.0.17",
      readiness: 62,
      pendingWork: "NJ4 (Jul 12): INT-Claude subscription re-review of v1U.0.16 = MINOR-REVISIONS (0 correctness bugs; conclusion unchanged) → closed same-bundle as v1U.0.17 (presentation-only). (1) Route-1 NJL magnitude leg (B) now explicitly covers the attractive AA channel — worst scanned |G_AA|/G_crit = 2×0.156 = 0.31 (exact factor G_AA/|G_scalar|=2) stated in App. njl_gap + main-text mirror, no longer relying on the PP-only |G_PP|=|G_scalar| equality; (2) added the physical point that AA (Lorentz-violating axial-vector) and PP (parity-breaking) vacua are not the scalar σ-condensate at issue, so leg-(A)'s sign exclusion is already decisive; (3) blanket 'far sub-critical' in abstract + discussion aligned to plain 'sub-critical' to match the tempered appendix worst-case. md5 67127cda, 63 pp; conclusion unchanged. NJ3b (Jul 12): recovered ChatGPT EXT retry (fills the NJ3 dead-GAP) = REJECT on v1U.0.16 — verified verbatim (NJ3b/P1U_chatgpt_NJ3b.md line 1 = 'VERDICT: REJECT'). 12 MAJOR + 1 MINOR all source-cited re-flags (DP1U-03/04/07/08/09/10/11/12/14/17/15/24/02). HIGH-STAKES: ChatGPT's 8π/criticality-ratio-1.07 NJL claim is arithmetically REAL (3·9/8π=1.07) but NOT a defeater — leg (A) sign exclusion G_scalar=−(3/64)κ<0 is convention-independent + decisive (tex L5099-5105, script L149-155); 8π touches only leg (B) magnitude at the unreduced+maximal worst corner; physical Holst-dressed=0.075 / Λ_strong=0.294 stay sub-critical → maps to DP1U-02 + DP1U-05/-26, optional footnote tightening (PROCESS-NIT). ChatGPT engaged app:njl_gap but only leg (B), not leg (A) (same partial-engagement as NJ2). 0 genuinely-new; clean-wave streak HOLDS 1; cap 62 HOLDS (fills GAP, score 0). NJ3 (Jul 12): 0 genuinely-new reader-visible findings on v1U.0.16 — all 5 Grok EXT items re-flag existing dispositions (four-route framing DP1U-06, Sec-X all-orders DP1U-12, 14-barrier tiering DP1U-13, NJL mean-field caveat DP1U-05, length DP1U-18/-24). INT (run.log 08:24Z): openai REJECT / grok REJECT / gemini MAJOR / claude MINOR. Gemini INT flipped MIN(NJ2)→MAJ(NJ3) on content whose only delta is the DP1U-26 leg-A fix — its 3 MAJORs are abstract-length/meta-text/Sec-X-framing (none touching the delta; → DP1U-24/-12), pure presentational-axis referee variance (pattern-066); it still calls the central claim 'robustly supported'. ChatGPT EXT FAILED-dead (NJ3b retry in flight) = chart GAP. clean-wave streak 0→1; cap 62 holds. v1U.0.16 (Jul 12): INT-Claude genuinely-new MINOR closed — the Route-1 NJL sign-exclusion (leg A) is now explicitly scoped to the scalar (SS/χSB) channel; the axial/pseudoscalar channels are attractive by the same Fierz lemma (G_AA=+3/32κ, G_PP=+3/64κ) and are excluded by the magnitude leg (|G_PP|=|G_scalar|, equally sub-critical); 'far'→'comfortably' sub-critical (worst scanned 0.156). Conclusion unchanged; md5 3f43fc81, 63 pp. NJ1 wave (v1U.0.15, Jul 12): INT-Claude caught Holst-dressed NJL factor stated as ∼30× in body; paper's own committed script gives holst_factor=0.0698=γ²/(γ²+1) → 14.3× ≈ ∼14×; corrected at 2 body sites + header comment; NJL-exclusion appendix (app:njl_gap) verified SOUND; conservative direction + conclusion unchanged; EXT Grok MAJOR + ChatGPT REJECT re-flagged old ledger classes without engaging the new appendix; streak reset to 0; md5 3519880a; 63 pp. v1U.0.14 (directive-L): Route-1 vacuum condensate now EXCLUDED by a regulated NJL gap equation (closes DP1U-05/-19). New Appendix app:njl_gap on the paper's own operator -(3/16)κ(J5·J5): (A) Fierz-projecting to scalar condensate channel gives G_scalar=-(3/64)κ<0 = repulsive; (B) |G_eff|/G_crit≈4.3e-2 at Λ=M_Pl (worst case 0.156). Every number verified against the committed njl_gap_equation_route1.py script.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/16 SPHEREx forecast + Cai-Li certification",
      version: "v1.7.115",
      readiness: 74,
      pendingWork: "v1.7.115: INT-Claude found + we closed a genuinely-new MAJOR by RE-COMPUTE — the c15 channel-native Fisher built the GR leg dB/dA_GR WITHOUT the M123 transfer product the f_NL primordial leg carries (GR template in potential space vs f_NL density basis), collapsing F[2,2]~1e-18 and faking rho(f_NL,A_GR)=-0.001 orthogonality. Fixed (Dg *= M123, the same promotion cross_fisher_alpha already used) + re-ran (231s): CORRECTED rho(f_NL,A_GR)=-0.42 (2x2)/-0.49 (3x3) — GR channel MODERATELY correlated with f_NL, not orthogonal; sigma_marg=0.94 -> 2.32sigma. Load-bearing result HOLDS: channel-native floor 2.32sigma still > proxy 1.30sigma floor, proxy stays the conservative quoted endpoint; alpha=0.992 unchanged. Grok EXT MINOR; ChatGPT REJECT = documented floor. -35/16 quadruple-certified, nothing fabricated.",
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
      version: "v0.1.123-2026-07-12",
      readiness: 85,
      pendingWork: "RS2b (Jul 12): recovered ChatGPT EXT retry (fills the RS2 dead-GAP) = MAJOR REVISIONS on the fully-corrected v0.1.123 — verified verbatim (RS2b/P5_chatgpt_RS2b.md line 1 = 'VERDICT: MAJOR REVISIONS'). ChatGPT's REJECT(pre-fix v0.1.122)→MAJOR(corrected v0.1.123) floor-crack HOLDS, and critically it engaged the corrected RSD block and did NOT re-raise the DP5-22 estimand/sign defect it caught in RS1 — the fix landed. 12 MAJOR + 3 MINOR all source-cited re-flags (DP5-06/07/04/11/10/08/09/12/14/19/20/21/22; the 3 low-score UNMATCHED — adjustment-in-lieu→DP5-19, monopole-env-relabeling→DP5-08/09, QSO-in-spirals→DP5-22 — all disclosed). 0 genuinely-new reader-visible editable findings; no bump (v0.1.123 stands); clean-wave streak HOLDS 3. Cap 79→85 (chatgpt reject→major lifts +6: 50 + grok-ACCEPT 16.7 + chatgpt-MAJOR 6 + gemini-MINOR 12 = 84.7; post_verdict.sh same-datestamp tie-break bug corrected via true latest-by-creationTime). RS2 (Jul 12): SECOND Grok EXT ACCEPT — verified char-for-char (RS2/P5_grok_RS2.md line 1 = 'VERDICT: ACCEPT'), and this one is on the fully-corrected v0.1.123. Best-ever INT board same wave (run.log 08:24Z): openai MAJOR / grok MINOR / gemini MINOR / claude MINOR — no INT REJECT. 0 genuinely-new reader-visible findings: all 4 Grok EXT minors are source-cited re-flags (post-hoc DP5-13, 2.1σ sign-flip leakage ~0.001pp already in-paper DP5-14, ≈0.9pp quadrature DP5-11, Paper-IV/DOI submission logistics DP5-21 open-venue). ChatGPT EXT FAILED-dead (RS2b retry in flight) = chart GAP not a zero. No bump (v0.1.123 stands, no edit); clean-wave streak 2→3; cap 74→79 (Grok-EXT-ACCEPT formula recompute). v0.1.123 (Jul 12): INT-Claude + EXT-ChatGPT genuinely-new — the RSD Zel'dovich reconstruction bound is correctly re-scoped to the UNRESTRICTED (secondary) void contrast (no footprint mask), not the primary footprint-restricted estimand, framed as the more conservative larger-sample coherent-outflow probe; honest disclosure that reconstruction reassigns membership substantially (n_void 57,058→42,864, −25%) yet Δf_CW shift stays tiny (0.024pp) because reassigned galaxies are parity-symmetric; sign (−0.069→+0.069pp) + quadrature (√0.898) corrected; null preserved, nothing fabricated; md5 186d985e, 46 pp. v0.1.122 (Jul 12): DP5-12 RSD MAJOR CLOSED-BY-COMPUTE (first-order). The recurring ChatGPT-M4/Grok-M3 'reconstruction deferred' caveat is now a computed consistent first-order Zel'dovich bound — galaxies AND the published DESIVAST holes displaced together by the same coherent void-outflow field (Hamaus, Sutter & Wandelt 2014), exact scripts/26 membership re-run (sample 678,987 vs ref 678,945; n_void 57,058 vs ref 57,081). Primary Δf_CW z-space −0.069pp → reconstructed −0.045pp; RSD systematic |shift|=0.024pp (MC +0.026±0.049pp), ~40× under the ~0.9pp envelope; null preserved (|z| 0.32→0.18). Integrated at §VIII/§XIII/abstract/systematics-budget; honest residual retained (NOT a full nonlinear void-catalog re-derivation). Re-test fired (INT triple + Grok/ChatGPT EXT).",
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
