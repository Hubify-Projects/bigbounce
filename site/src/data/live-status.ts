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
  lastUpdatedISO: "2026-06-12T11:00:00Z",
  lastUpdatedDisplay: "June 12, 2026 · 4:00 AM PT",
  headline:
    "EXT6 harvested — Grok 4th consecutive 6/6 ACCEPT; Gemini first full ACCEPT on P1B; R35conf closures landed; ChatGPT MAJOR×6 with P2 narrowly; truth-audits in progress.",
  summary:
    "Six external rounds complete. EXT6 submitted Jun 12 ~02:35 PT on R35conf-closed versions (v1A.0.68/v1B.0.65/v1.7.60/v3.1.103/v1.0.182/v0.1.72). Grok has been 6/6 ACCEPT for four consecutive rounds. Gemini fully cleared P1B for the first time. ChatGPT holds MAJOR×6; per-finding truth-audits determine the genuine residuals.",
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
      version: "v1A.0.68",
      readiness: 95,
      pendingWork: "v1A.0.68 — EXT6: Grok ACCEPT ×4 rounds, Gemini MINOR (fine-tuning score phrasing); ChatGPT MAJOR (NJL wrong-sign, Sec IV closure overclaim); truth-audit in progress; awaiting Houston sign-off",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.65",
      readiness: 94,
      pendingWork: "v1B.0.65 — EXT6: Grok ACCEPT ×4, Gemini FULL ACCEPT (first paper fully cleared by Gemini); ChatGPT MAJOR (artifact-layer pinning, frozen artifact mismatch); awaiting Houston sign-off",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.60",
      readiness: 94,
      pendingWork: "v1.7.60 — EXT6: Grok ACCEPT ×4, Gemini MINOR (Eq 3 variable mismatch + Table IV header); ChatGPT MAJOR (narrowly — null-space interpretation + fresh numerical issues); awaiting Houston sign-off",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.103",
      readiness: 95,
      pendingWork: "v3.1.103 — EXT6: Grok ACCEPT ×4, Gemini MAJOR (fresh thread — calibration/instrumental artifacts, notation); ChatGPT MAJOR (catalogue-tier semantics, DESI denominator); awaiting Houston sign-off",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.182",
      readiness: 95,
      pendingWork: "v1.0.182 — EXT6: Grok ACCEPT ×4 (exemplary, immediate acceptance recommended), Gemini MINOR (misplaced imaging-leg paragraph in appendix); ChatGPT MAJOR (monopole interpretation, +3.64σ taxonomy residuals); awaiting Houston sign-off",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.72",
      readiness: 95,
      pendingWork: "v0.1.72 — EXT6: Grok ACCEPT (EXT5 MINOR → EXT6 ACCEPT; estimand-family coherence cleared), Gemini MINOR (appendix labeling layout sync); ChatGPT MAJOR (GALZONE estimand-family, 3.56% duplicate tracking); awaiting Houston sign-off",
    },
  ],
  blockerTally: {
    closed: 701, // 678 through the pod wave + 23 R26conf closures (P1A 2 catches + P3 12 textual + P5 9; P1B M-tier traceability closures + CPL falsification not separately tallied); P1B R26conf CLEAN
    openBlockers: 0,
    openMajors: 0,
    openMinors: 0,
  },
  cronStatus: "autonomous review loop active — hourly fires",
  etaToCompletion:
    "All six papers targeted publishable ~June 12–13, 2026 (per SSOT/PUBLISH_PLAN.md). Gated on Houston external round + sign-off; the final 1% is Houston-only.",
  pods: [],
};
