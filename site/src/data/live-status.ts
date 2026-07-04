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
  lastUpdatedISO: "2026-07-03T18:00:00Z",
  lastUpdatedDisplay: "July 3, 2026 · 11:00 AM PT",
  headline:
    "HONEST RESET (Jul 3): first FULLY-VERIFIED external board — all 6 papers × ChatGPT+Grok+Gemini run in the visible browser with the complete raw reviewer text + screenshots + chat URLs saved to git. NONE are converged; every paper draws a real ChatGPT REJECT on substantive grounds. The prior 'converged at 96' was built on unverified, ChatGPT-skipping sweeps and was overstated. Readiness honestly recut to 76–80.",
  summary:
    "Replaced unverifiable label-only EXT sweeps with a fully-verified board (18 raw reviewer responses + screenshots + chat URLs committed under project-context/peer-reviews/EXT_real/). Full-source INT then caught and fixed real issues: a FABRICATED physics claim (P2 Cai/Li factor-of-2, retracted + honestly disclosed), a dimensional bug (P1B four-fermion coefficient, fixed), an overclaim (P3 §V cosmological, reframed to methodological-demonstration/no-detection), while defending one genuinely-robust null with git+data (P4). No fabrication survives. Remaining findings are largely STRUCTURAL — in-prep companion-paper dependencies + hard-conditional physics walls — that route to human editors, not further edits.",
  currentlyRunning: [
    "Verified-finding closure — per-paper full-source INT truth-audits against source; honest fixes / disclosures / dispositions, every verdict evidence-backed.",
  ],
  needsHouston: [
    {
      title: "Publish the in-prep companion papers",
      blockedPaper: "all",
      why: "Multiple papers (P5's Paper-IV catalog, P1A's 4 companions) depend on unpublished same-author companions whose labels/numbers referees cannot vet — the structural driver of the external rejections.",
      ask: "Prioritize completing + publishing the companion papers; that clears the largest class of standing external MAJORs.",
    },
    {
      title: "Route floor papers to human referees",
      blockedPaper: "all",
      why: "Every paper hits the LLM-referee floor (ChatGPT rejects any real manuscript with ansatz-level closures + companion deps); a human referee is needed on the venue/scope + conditional-result questions.",
      ask: "Decide target journals + route P1A/P1B/P2/P3 to human referees on the ansatz-tier / methodological-companion / conditional-forecast questions.",
    },
  ],
  papers: [
    {
      slug: "paper-1a",
      number: "1A",
      shortTitle: "ECH dark-energy closure + perturbation transparency",
      version: "v1A.0.104",
      readiness: 78,
      pendingWork: "VERIFIED EXT: ChatGPT REJECT / Grok MAJOR / Gemini MAJOR. Eq.(1) T² variational concern truth-audited as a misread — first-order variational principle verified SOUND, clarified (v1A.0.104). Remaining: R2/R3 ansatz-tier rigor + 4 in-prep companion deps — structural, human referee.",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.98",
      readiness: 76,
      pendingWork: "VERIFIED EXT: ChatGPT REJECT / Gemini REJECT / Grok gave a favorable free-form read but no format verdict. Four-fermion dimensional bug (κ vs κ²) caught by ChatGPT + FIXED (v1B.0.98); ΔN_eff bound unchanged. Remaining: ECH-scope + methodological-companion venue call.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.86",
      readiness: 78,
      pendingWork: "VERIFIED EXT: ChatGPT REJECT / Grok MAJOR / Gemini MAJOR. INT caught the prior Cai/Li factor-of-2 'resolution' was FABRICATED — retracted; f_NL=−35/8 now carries an explicit unresolved-factor-of-2 disclosure + a real Li −35/16 downward branch (~1.3–2.75σ). Cubic transmission honest-conditional.",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "268K-anomaly multi-survey catalog",
      version: "v3.1.136",
      readiness: 80,
      pendingWork: "VERIFIED EXT: ChatGPT REJECT / Grok MAJOR / Gemini REJECT. §V cosmological (f_NL/NANOGrav) reframed to explicit methodological-demonstration / no cosmological detection (v3.1.136). 268,519 = process-volume candidates (NOT confirmed detections); eROSITA/LAMOST reproducibility dispositioned as re-flags of disclosed content.",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.212",
      readiness: 80,
      pendingWork: "VERIFIED EXT: ChatGPT REJECT / Grok MAJOR / Gemini MINOR. Confidence-cut null truth-audited against git+data: VERIFIED ROBUST (0.6 cut git-pre-specified; low-conf excess is a step-function systematic; pseudo-label-free GZ1 sub-model z=−0.04). Remaining: ~half the ℓ=1 residual unexplained (hard) + pseudo-label under-powering — honestly disclosed.",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.101",
      readiness: 80,
      pendingWork: "VERIFIED EXT: ChatGPT REJECT / Grok MINOR / Gemini MAJOR. Structural dependence on the in-prep same-author Paper-IV classifier catalog (labels referees cannot vet) + RSD/T-Web confounding. Clears when Paper IV publishes — human-editor matter.",
    },
  ],
  blockerTally: {
    closed: 898, // prior + 3 verified findings resolved this reset (P1B bug, P2 fabrication, P3 §V overclaim)
    openBlockers: 2, // structural: companion-paper deps + human-referee routing
    openMajors: 11, // standing verified external MAJORs across the 6 papers (deduplicated)
    openMinors: 6,
  },
  cronStatus: "HONEST RESET 2026-07-03: verified EXT board complete (6 papers, 18 raw legs in git). Real verdicts — every paper a ChatGPT REJECT; P1A/P2 REJECT-MAJOR-MAJOR, P1B/P3 REJECT with a 2nd REJECT, P4 REJECT-MAJOR-MINOR, P5 REJECT-MINOR-MAJOR. NONE converged. 3 real findings caught + fixed (fabrication retracted, dim bug fixed, overclaim reframed). Loop continues on the verified findings; no convergence claimed without external ACCEPT.",
  etaToCompletion:
    "Not converged — the strict gate (ACCEPT from all 3 reviewers, 0 major/minor, all 6 papers) is not met. Fixable findings are being closed against source; the remaining structural blockers (in-prep companion papers, hard-conditional physics, LLM-referee floor) require publishing the companions + human referees, which is Houston-gated.",
  pods: [],
};
