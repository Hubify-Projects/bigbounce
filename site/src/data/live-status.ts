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
  lastUpdatedISO: "2026-07-07T18:00:00Z",
  lastUpdatedDisplay: "July 7, 2026 · 11:00 AM PT",
  headline:
    "VERIFICATION COMPLETE; REVIEW CLOSURE IN PROGRESS (Jul 7). All six papers are error-clean, fully verified, D-round polished, and P-round packets are arXiv-ready — but NOT yet past external review. The verified EXT board is the truth: every paper still draws a real ChatGPT REJECT, with Grok/Gemini MINOR-to-MAJOR. Readiness is verdict-derived, not ladder-derived. The bar is a reviewer ACCEPT, which no paper has yet.",
  summary:
    "Correcting the record: an earlier build read readiness 99 / 'program complete,' which conflated 'verification rounds complete' with 'reviews passed.' They are not the same. Per the POSTPOLISH-2026-07-06 verified round (ChatGPT/Grok/Gemini): P4 REJ/MIN/MAJ · P2 REJ/MIN/MIN · P5 MAJ/MIN/MIN · P3 REJ/MAJ/MAJ · P1B REJ/MAJ/MAJ · P1A REJ/MAJ/MAJ. Readiness = 50 (error-clean/verified base) + per-reviewer points (ACCEPT +16.7, MINOR +12, MAJOR +6, REJECT 0) summed over the 3 EXT reviewers. The loop is now closing the remaining reviewer findings with real science — not declaring victory.",
  currentlyRunning: [
    "Closing remaining reviewer findings with real science: P2 independent Fisher · P1A Fierz-lemma proof attempt · P3 eROSITA reproducibility fix · P1B→P1A merge prep (unanimous reviewer recommendation). ACCEPT is the bar.",
  ],
  needsHouston: [
    {
      title: "Route the review-floor papers to human referees",
      blockedPaper: "all",
      why: "No paper is reviewer-accepted — every one still draws a real ChatGPT REJECT; the remaining barrier is a venue/scope judgment, not an editable defect (pattern-066). Only a human can decide arXiv/journal routing.",
      ask: "Decide the referee route for the review-floor papers while the loop closes the remaining reviewer findings with real science.",
    },
    {
      title: "arXiv submission — endorsement (when a paper clears review)",
      blockedPaper: "all",
      why: "Submission needs a human: arXiv endorsement is Houston-only. Gated behind a paper actually clearing external review — the packets are ready, the reviews are not passed yet.",
      ask: "Confirm arXiv endorsement so a paper can be submitted the moment it earns a reviewer ACCEPT.",
    },
    {
      title: "Send the Cai/Brandenberger courtesy email",
      blockedPaper: "P2",
      why: "The courtesy note about the −35/16 Cai–Li factor-of-2 resolution is drafted do-not-send; only Houston sends outbound author correspondence.",
      ask: "Review the drafted courtesy email and send when ready.",
    },
  ],
  papers: [
    {
      slug: "paper-1a",
      number: "1A",
      shortTitle: "ECH dark-energy closure + perturbation transparency",
      version: "v1A.0.113",
      readiness: 62,
      pendingWork: "Error-clean + verified, NOT reviewer-accepted. Verified EXT board (Jul 6): ChatGPT REJECT · Grok MAJOR · Gemini MAJOR → 50+0+6+6=62. Closing findings with real science: Fierz-lemma proof attempt + P1B→P1A merge prep (unanimous reviewer rec).",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.103",
      readiness: 62,
      pendingWork: "Error-clean + verified, NOT reviewer-accepted. Verified EXT board (Jul 6): ChatGPT REJECT · Grok MAJOR · Gemini MAJOR → 50+0+6+6=62. Four-fermion dimensional bug fixed; being prepped for merge into P1A per unanimous reviewer recommendation.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = −35/16 SPHEREx forecast",
      version: "v1.7.102",
      readiness: 74,
      pendingWork: "Error-clean + verified, NOT reviewer-accepted. FULL8 board (Jul 8): Grok MINOR · Gemini MAJOR (tone) · ChatGPT REJECT. v1.7.102 closed the Gemini tone-regression MAJOR — neutralized rebuttal/defensive prose across §I, §VI, §VII, §VIII, §IX.E, and App A to declarative scientific register; Cai–Li App-A internal-inconsistency (ChatGPT) truth-audited as MISREAD (Li Eq.4.19 ≡ Cai Eq.37 at c_s=1; −35/16 from vertex re-summation) with one clarifying sentence. NO NUMBER CHANGED, NO DISCLOSURE WEAKENED.",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378,280-anomaly multi-survey catalog",
      version: "v3.1.143",
      readiness: 62,
      pendingWork: "Error-clean + verified, NOT reviewer-accepted. v3.1.143 (REALWORK re-test): sharpened Grok's process-volume framing item — the very first prose use of 268,519 now carries the science-target benchmark 2,468 in the SAME sentence (process-volume figure whose like-for-like benchmark is 2,468 DESI clusters, ≈0.92× Liang2023); audited every headline-count use for the pairing. NO COUNT CHANGED. Prior: eROSITA reproducibility fix; §V framed as methodological demonstration, no cosmological detection.",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.223",
      readiness: 80,
      pendingWork: "Error-clean + verified, NOT reviewer-accepted. CW re-test (Jul 8): Grok MINOR · Gemini MINOR · ChatGPT MAJOR — P4 remains the closest to convergence in the program (Grok+Gemini both MINOR, only ChatGPT's structural-floor MAJOR outstanding). Real-space ℓ=1 dipole +0.41σ null robust; every number preserved. Raw verbatim reviewer text + screenshots in EXT_real/CW_2026-07-08/.",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.107",
      readiness: 74,
      pendingWork: "Error-clean + verified, NOT reviewer-accepted. CW re-test (Jul 8): Grok MINOR · Gemini MAJOR · ChatGPT MAJOR — Gemini re-flagged the RSD-in-T-Web classification, radial-selection bias in T-Web void classes, and the unpublished Paper-IV label dependency (all already disclosed); ChatGPT re-flagged the same T-Web/void-membership/Paper-IV items. Central DESIVAST no-environmental-dependence null reasonably supported; every number preserved. Raw verbatim reviewer text + screenshots in EXT_real/CW_2026-07-08/.",
    },
  ],
  blockerTally: {
    closed: 912, // every fixable content error closed; verified board is now reviewer-verdict-limited, not error-limited
    openBlockers: 0,
    openMajors: 5, // POSTPOLISH-2026-07-06 verified EXT board: 1 ChatGPT REJECT/paper (×6) + Grok/Gemini MAJORs on P1A/P1B/P3(×2) and P4/P5(×1) — these are the open reviewer findings the loop is now closing with real science
    openMinors: 6, // Grok/Gemini MINORs on P2/P4/P5
  },
  cronStatus: "VERIFICATION COMPLETE; REVIEW CLOSURE IN PROGRESS (2026-07-07). Papers are error-clean + verified + polished + packet-ready, but the verified EXT board shows NO paper past review (ChatGPT REJECT ×5, Grok/Gemini MINOR-to-MAJOR). Readiness is verdict-derived (avg 68). Driving the remaining reviewer findings to closure with real science — ACCEPT is the bar.",
  etaToCompletion:
    "Driving the remaining reviewer findings to closure with real science; a reviewer ACCEPT is the bar before any paper is submission-eligible.",
  pods: [],
};
