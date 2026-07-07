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
    "VERIFICATION PROGRAM COMPLETE (Jul 7): all six papers have verifiably walked the full readiness ladder — R-rounds converged to the pattern-066 floor (full INT all-vendor + EXT headed rounds, FINAL_SIGNOFF_AUDIT: zero unfixed genuinely-new findings), D-round visual polish clean, and P-round packets standalone-compile-verified + venue-policy-proofed. All six sit at readiness 99. The final 1% is Houston sign-off + arXiv submission.",
  summary:
    "Closed out the campaign: every finding on the verified EXT board is dispositioned to a source-cited verdict (genuinely-new items fixed in-paper; re-flags and disclosed limitations verdict'd non-real per pattern-066). D-round polished the flagship pair to top-journal presentation with zero science changed; P-round rebuilt every arXiv tarball and standalone-compile-verified it, mirrored each PDF byte-identical to all served paths (Convex md5 == served == fresh compile), and confirmed venue-policy compliance. Per the CLAUDE.md ladder (R→96, D→98, P→99, Houston sign-off→100), all six are set to readiness 99 in Convex — ladder-compliant, not a hand-bump.",
  currentlyRunning: [
    "Awaiting Houston sign-off — the final 1%; on sign-off the two-wave arXiv submission (runbook: SUBMIT-TODAY-CHECKLIST) fires.",
  ],
  needsHouston: [
    {
      title: "Sign off the six papers (the final 1%)",
      blockedPaper: "all",
      why: "The readiness ladder is complete through the P-round (99); only Houston's sign-off promotes any paper to 100 — the loop can never self-award it.",
      ask: "Read the HUMAN_READ_BRIEFING and give the sign-off quote per paper in SSOT.",
    },
    {
      title: "arXiv submission — endorsement + two-wave order",
      blockedPaper: "all",
      why: "Submission needs a human: arXiv endorsement confirmation and the actual wave-1 submit clicks are Houston-only.",
      ask: "Confirm arXiv endorsement, then run the two-wave submission per SUBMIT-TODAY-CHECKLIST (order P4 → P1A+P1B → P3 → P2 → P5).",
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
      readiness: 99,
      pendingWork: "Awaiting Houston sign-off + arXiv submission. R+D+P complete; ChatGPT REJECT is the structural harsh-referee floor (directive H), all Grok/Gemini majors truth-audited to source-cited re-flags of disclosed scope; companions recast to concurrent coordinated-submission with refereeable-now artifacts.",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.103",
      readiness: 99,
      pendingWork: "Awaiting Houston sign-off + arXiv submission. R+D+P complete; four-fermion dimensional bug fixed; ΔN_eff bound unchanged; presented as Paper-1A's concurrently-posted technical companion.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = −35/16 SPHEREx forecast",
      version: "v1.7.99",
      readiness: 99,
      pendingWork: "Awaiting Houston sign-off + arXiv submission + Cai/Brandenberger courtesy email. R+D+P complete; the Cai–Li factor-of-2 is resolved to f_NL = −35/16 = −2.1875 (3-way independently certified); SPHEREx recast ~1.3–2.75σ; all figures label-synced to −35/16.",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378,280-anomaly multi-survey catalog",
      version: "v3.1.141",
      readiness: 99,
      pendingWork: "Awaiting Houston sign-off + arXiv submission + HuggingFace catalog visibility flip. R+D+P complete; §V framed as methodological demonstration / no cosmological detection; NANOGrav γ = 2.567 ± 0.382 real-KDE fit; catalog counts reconciled.",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.221",
      readiness: 99,
      pendingWork: "Awaiting Houston sign-off + arXiv submission (first in queue). R+D+P complete; real-space ℓ=1 dipole +0.41σ null truth-audited robust against git+data; both prior over-claiming majors lifted; abstract rewritten reader-first with every number preserved.",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.105",
      readiness: 99,
      pendingWork: "Awaiting Houston sign-off + arXiv submission. R+D+P complete; DESIVAST three-algorithm void null foregrounded; Paper-IV dependency disclosed for referees; both calibrated reviewers credit the anchoring, remaining major dispositioned structural per pattern-066.",
    },
  ],
  blockerTally: {
    closed: 912, // every finding on the verified EXT board dispositioned to a source-cited verdict
    openBlockers: 0,
    openMajors: 0, // all external majors truth-audited to source-cited re-flags of disclosed scope (pattern-066)
    openMinors: 1, // P3 single disclosed polish minor
  },
  cronStatus: "PROGRAM COMPLETE 2026-07-07: all six papers R+D+P verified (INT all-vendor + EXT headed, FINAL_SIGNOFF_AUDIT clean), readiness 99 across the board in Convex. No new sweeps — the edit loop is complete; the only remaining barrier is venue (Houston sign-off + arXiv submission).",
  etaToCompletion:
    "Awaiting Houston sign-off → two-wave arXiv submission (runbook: SUBMIT-TODAY-CHECKLIST).",
  pods: [],
};
