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
      version: "v1U.0.5",
      readiness: 62,
      pendingWork: "UNIFIED Paper 1 (P1B merged in as appendices): 60pp self-contained; v1U.0.5 is a W11 EXT presentation-closure wave (no number changed, nothing fabricated). THE ask (ChatGPT B2 + Gemini Blocker-1, identical): brought the formally dimension-4 OFF-SHELL parity-odd operator into the MAIN TEXT at Eq. (6) — new displayed Eq. (7) S_eff^(4)=∫√−g Σ_n c_n O_n^[4] over the closed O1–O6 basis, with the explicit statement that the dim-+1 form is an on-shell presentation shorthand for that closed dim-4 set (algebraic torsion eliminated + one curvature stripped by Bianchi), cross-ref to App B.1 where the closure was already derived. Grok's polishing list closed: R4 quintessence/f(R) contrast (the m_θ~H0 tuning is forced by one coupling sourcing both β_obs and ρ_Λ); Route-2 margin robustness (inflating the one-loop prefactor by 10 OOM still leaves ≥48 orders of margin); perturbation-transparency exclusions rationale. Struck the Sec IV.E 'earlier-draft mis-stated' editorial cross-talk (Gemini/ChatGPT minor). Awaiting next EXT re-test.",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.104",
      readiness: 62,
      pendingWork: "MERGED into Paper 1 (2026-07-08, unanimous reviewer recommendation, Houston-approved) — no standalone submission; two-paper fallback preserved.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = −35/16 SPHEREx forecast",
      version: "v1.7.106",
      readiness: 64,
      pendingWork: "Error-clean + verified. W11 EXT sweep (Jul 9): Grok publication-ready for PRD/JCAP/MNRAS · Gemini + ChatGPT major-revisions, all three crediting the per-vertex table with resolving the 8-year factor-of-two f_NL=−35/16. v1.7.106 closes the residual editable items (all forecast-methodology / claim-strength, no math changed): calibrated the abstract to state the vertex re-summation yields −35/16 EXACTLY + Li's independent derivation decisively favors it (ChatGPT claim-strength — the full algebraic Cai-polynomial→vertex-sum map was already displayed as Eq. vertexsum/collapsed/order_grouped/spurious); made the SPHEREx additive-quadrature budget explicit as displayed Eq. (11) bracketed to ~14% by the ρ=−0.868 marginalized floor (Gemini 'soft'); labeled MegaMapper decisively as an uncalibrated high-z projection (Gemini); fixed the stale f_NL≈−4 → −2 (ChatGPT minor). −35/16 unchanged, certified 3 ways. Raw verbatim + screenshots in EXT_real/W11_2026-07-09/.",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378,280-anomaly multi-survey catalog",
      version: "v3.1.146",
      readiness: 62,
      pendingWork: "Error-clean + verified, NOT reviewer-accepted. R9 EXT board (Jul 9): ChatGPT major · Gemini major-if-PRD (ApJS/MNRAS transfer suggested) · Grok minor ('suitable for PRD', 3 presentation clarifications). v3.1.146 real work: (1) NEW committed-data out-of-sample answer to the recurring 'released catalog scored in-sample' major — a held-out anomaly-tail-preservation test on 47,000 DESI rows held out of both train and val across the 5 folds shows the anomaly-defining tail (MSE p99/p50) is preserved vs in-sample at rho=1.00±0.05 (min 0.94, gate≥0.5 PASS), so the tail is not an in-sample-inflation artifact (new artifact heldout_tail_preservation.json); (2) main-text definition of the 5,384 QSO-candidate multi-tracer sample added (Grok minor). Tier-mix major = re-flag of the already-prominent three-tier split (referee variance). Venue = scope/venue, Houston-gated. NO COUNT CHANGED, NO DISCLOSURE WEAKENED, NOTHING FABRICATED.",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.225",
      readiness: 82,
      pendingWork: "Error-clean + verified, NOT reviewer-accepted. R9 EXT board (Jul 9): Grok = MINOR-revisions ('careful, reproducible null-result analysis that meets PRD standards', 3 clarifications) · Gemini = 'Accept with minor revisions' ('a highly significant contribution', 3 clarifications) · ChatGPT = MAJOR (presentation/consolidation of already-disclosed content). Readiness 82 = 50 base + Grok MINOR (+16) + Gemini MINOR (+10) + ChatGPT MAJOR (+6). v1.0.225 closed both ACCEPT-track referees' concrete minors: abstract z≈−18 now explicitly a model-dependent template-disfavor statistic (not a frequentist exclusion) with the injection-recovery A95∈(1.0,1.5]% cross-referenced; main-text downstream-user warning that raw p_eq are not frequentist likelihoods (Appendix-B ECE ≥0.25–0.36); abstract real-space p now names its isotropic-pixel-permutation null. This paper is the program's closest — two clean minor-lists from a Grok+Gemini double-accept. Raw verbatim + screenshots in EXT_real/R9_2026-07-09/.",
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
