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
      version: "v1A.0.115",
      readiness: 62,
      pendingWork: "Error-clean + verified, NOT reviewer-accepted. FULL8 board (Jul 8): ChatGPT REJECT · Grok MAJOR · Gemini MINOR (improved from MAJOR). v1A.0.115 closed all 4 Gemini MINORs — R4-framing clarifier (amplitude closure applies to R1–R3; R4 is the naturalness route) added unmissably to the abstract; Fierz-lemma scope sentence added to App C (what it establishes vs the operators it does not enumerate); NDA/Immirzi framed as a strict theoretical limitation; §X classical/quantum-anomaly caveat added; App B +1→+4 promotion flagged heuristic. NO NUMBER CHANGED, NO DISCLOSURE WEAKENED. ChatGPT completeness objection dispositioned structural (honestly-scoped, not editable without a full operator-basis proof).",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.104",
      readiness: 62,
      pendingWork: "Error-clean + verified, NOT reviewer-accepted. FULL8 board (Jul 8): ChatGPT MAJOR (off REJECT — first time) · Grok MAJOR · Gemini MAJOR. v1B.0.104 closed every editable item — LiteBIRD 9σ (null-rejection vs β=0) now paired in-sentence with the 0.7σ model-discrimination separation; §III.A ΔNeff sharpened as a leading-parametric-order EFT estimate (O(1)/NJL prefactors dropped, moot at 10⁻⁴⁴); §IV NaMaster caveat made unmissable (foreground-free synthetic E→B only, no real-sky systematic budget); §VI ALP framed as a prior-sensitivity exercise; DOI/data-availability note added. NO NUMBER CHANGED, NO DISCLOSURE WEAKENED. Standalone-scope / merge-into-1A items remain structural (Houston-gated).",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = −35/16 SPHEREx forecast",
      version: "v1.7.103",
      readiness: 74,
      pendingWork: "Error-clean + verified, NOT reviewer-accepted. v1.7.103 (Jul 8) applies the VERIFIED c14 redshift-space (RSD) tree bispectrum Fisher — retires the standing 'independent Fisher is real-space monopole only (~18% offset per Heinrich)' limitation with real computation: Kaiser Z1+SCF99/Sefusatti Z2, growth from the same CAMB Planck2018, orientation-integrated (ℓ=0,2,4 exact). σ(f_NL) tightens to 0.415/0.449 (+34.7% vs real-space 0.687), r_eff≈0.99 persists, f→0 reproduces c13 to 6 sig-figs; unmarginalized −35/16 significance 3.2–3.5σ (real-space floor) → 4.9–5.2σ (RSD), the c12 GR-projection bracket retained EXACTLY. Added Kaiser:1987 + Scoccimarro:1999. NO headline f_NL changed; nothing fabricated.",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378,280-anomaly multi-survey catalog",
      version: "v3.1.144",
      readiness: 62,
      pendingWork: "Error-clean + verified, NOT reviewer-accepted. FULL8 board (Jul 8): ChatGPT REJECT · Grok MAJOR · Gemini MAJOR — all three flagged the title's 'Validated Sources' framing. v3.1.144 decisive fix: title reframed to a Multi-Survey Anomaly-Candidate Catalog of Reconstruction-Outlier Sources (number 268,519 unchanged) so the headline certifies reconstruction-outlier status, not confirmed detections; abstract already leads with the process-volume disclosure + 2,468 science-target benchmark + ≥15σ narrow-line floor; eROSITA/Gaia exclusion made unmissable. NO COUNT CHANGED, NO DISCLOSURE WEAKENED. Gemini 'delete failures' + ChatGPT journal-fit dispositioned OPINION/structural.",
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
