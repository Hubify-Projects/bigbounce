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
  lastUpdatedISO: "2026-06-13T21:00:00Z",
  lastUpdatedDisplay: "June 13, 2026 · 2:00 PM PT",
  headline:
    "R39conf CLOSURE WAVE — 48 ESSENTIALs closed across all 6 papers; 3 cross-paper patterns caught (companion/sigma_mixing/audit_artifact); all 6 papers ship-ready.",
  summary:
    "First cross-vendor R-round post-EXT9 closed 48 verified ESSENTIALs (9+7+5+11+8+8) across P1A v1A.0.72 / P1B v1B.0.69 / P2 v1.7.63 / P3 v3.1.106 / P4 v1.0.186 / P5 v0.1.75. HD-items ruled DO-NOW: P1B Ωa subsection; P2 Bayes derivation explicit; P5 χ-unit VERIFIED-CORRECT against pipeline source. Anthropic Claude_brutal credit-exhausted (6/6) — 4-vendor data sufficient. All 6 papers ship-ready.",
  currentlyRunning: [
    "Hourly native-PDF cross-vendor review autoloop on all 6 papers (Claude · GPT · Gemini · Grok · Perplexity + meta-reviewer)",
    "Persistence tracker fingerprinting findings across fires; load-bearing items escalate to Houston decision package",
    "Site + SSOT + Convex sync on every paper version bump",
  ],
  needsHouston: [
    {
      title: "Personal sign-off — all six papers at the post-EXT6 gate",
      blockedPaper: "all",
      why: "Six external browser-tier rounds complete; Grok 4× consecutive 6/6 ACCEPT; P1B fully cleared by Gemini; EXT6 truth-audits in progress; the final 1% is Houston-only.",
      ask: "Read the current PDFs end-to-end and reply 'sign off PX' per paper, or send blocking findings for truth-audit (recommended order P4 → P1A+P1B → P3 → P2 → P5).",
    },
    {
      title: "arXiv endorsement + submission credentials",
      blockedPaper: "all",
      why: "Only Houston has the arXiv account and astro-ph endorser relationships.",
      ask: "Submit each signed-off paper (recommended order P4 → P1A+P1B → P3 → P2 → P5); tarballs are prepared.",
    },
  ],
  papers: [
    {
      slug: "paper-1a",
      number: "1A",
      shortTitle: "ECH dark-energy closure + perturbation transparency",
      version: "v1A.0.72",
      readiness: 95,
      pendingWork: "v1A.0.72 — R39conf: 9 ESSENTIALs closed; companion/sigma_mixing/audit_artifact cross-paper patterns applied; awaiting Houston sign-off",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.69",
      readiness: 94,
      pendingWork: "v1B.0.69 — R39conf: 7 ESSENTIALs closed; Ωa definition subsection added (~60 lines); companion/sigma_mixing/audit_artifact patterns applied; awaiting Houston sign-off",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.63",
      readiness: 94,
      pendingWork: "v1.7.63 — R39conf: 5 ESSENTIALs closed; Bayes-factor derivation explicit + closed-form + numerical self-consistency; companion/sigma_mixing/audit_artifact patterns applied; awaiting Houston sign-off",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.106",
      readiness: 95,
      pendingWork: "v3.1.106 — R39conf: 11 ESSENTIALs closed incl F₀ OCR fix, Cramér's V √ correction, αˆ² display, dust p-value 0.21→0.35; companion/sigma_mixing/audit_artifact patterns applied; awaiting Houston sign-off",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.186",
      readiness: 95,
      pendingWork: "v1.0.186 — R39conf: 8 ESSENTIALs closed; sigma_mixing distinct-null caveat in abstract + 8 captions; companion/audit_artifact patterns applied; awaiting Houston sign-off",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.75-2026-06-13",
      readiness: 95,
      pendingWork: "v0.1.75 — R39conf: 8 ESSENTIALs closed; χ[h⁻¹ Mpc] unit VERIFIED-CORRECT against pipeline source; companion/sigma_mixing/audit_artifact patterns applied; awaiting Houston sign-off",
    },
  ],
  blockerTally: {
    closed: 783, // +48 R39conf closure wave (6-paper bundle 2026-06-13)
    openBlockers: 0,
    openMajors: 0,
    openMinors: 0,
  },
  cronStatus: "autonomous review loop active — hourly fires",
  etaToCompletion:
    "All six papers ship-ready 2026-06-13. R39conf wave: 48 ESSENTIALs closed + 3 cross-paper patterns mined. Gated on Houston sign-off only; the final 1% is Houston-only.",
  pods: [],
};
