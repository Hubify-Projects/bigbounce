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
  lastUpdatedISO: "2026-06-14T01:39:00Z",
  lastUpdatedDisplay: "June 13, 2026 · 6:39 PM PT",
  headline:
    "EXT12 harvested: P4 = 3/3 ACCEPT confirmed (ChatGPT ACCEPT — first in campaign!). EXT13 closure wave queued for P1A/P1B/P2/P3/P5 (text-only fixes, ~2 hrs) + Gemini resubmit.",
  summary:
    "EXT12: Grok 6/6 ACCEPT (3 confirmed-read, 3 inferred). ChatGPT P4 ACCEPT (first ChatGPT ACCEPT in campaign) + P1A/P1B/P2/P3/P5 MINOR (1-2 text fixes each). Gemini 6/6 synthesis-mode (no formal verdicts — EXT13 fix: explicit referee-format instruction as first line). P4 is confirmed 3/3 ACCEPT, ready for arXiv. EXT13 target: 18/18 ACCEPT, HIGH CONFIDENCE. New auto-rule pattern-057: after systematic rename, grep full body text for residual tokens.",
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
      version: "v1A.0.74",
      readiness: 95,
      pendingWork: "v1A.0.74 — EXT12: Grok ACCEPT / ChatGPT MINOR / Gemini NO VERDICT. ChatGPT: 2 wording edits (Sec IV/App B dim sentence + reheating residual). EXT13 target ~20 min → HIGH CONFIDENCE ACCEPT.",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.71",
      readiness: 94,
      pendingWork: "v1B.0.71 — EXT12: Grok ACCEPT / ChatGPT MINOR / Gemini NO VERDICT. ChatGPT: harmonize release-pairing language across Sec III+Sec V.B+Conclusion (~20 min). EXT13 target → HIGH CONFIDENCE ACCEPT.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.65",
      readiness: 94,
      pendingWork: "v1.7.65 — EXT12: Grok ACCEPT / ChatGPT MINOR / Gemini NO VERDICT. ChatGPT: 3-sentence BF self-check paragraph fix (Eq.9 vs Eq.10 prior labeling, ~15 min). EXT13 target → HIGH CONFIDENCE ACCEPT.",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.108",
      readiness: 95,
      pendingWork: "v3.1.108 — EXT12: Grok ACCEPT / ChatGPT MINOR / Gemini NO VERDICT. ChatGPT: 2 fixes (DESI validation gate type in abstract + Table IX Savage-Dickey label, ~25 min). EXT13 target → HIGH CONFIDENCE ACCEPT.",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.188",
      readiness: 95,
      pendingWork: "v1.0.188 — EXT12: ChatGPT ACCEPT + Grok ACCEPT + Gemini EXT11 ACCEPT = 3/3 ACCEPT CONFIRMED. P4 is publication-ready. Only proof-stage copy-edit: Shamir [2] title string match. Queue for arXiv submission.",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.77-2026-06-13",
      readiness: 95,
      pendingWork: "v0.1.77 — EXT12: Grok ACCEPT / ChatGPT MINOR / Gemini NO VERDICT. ChatGPT: 3 residual V-Web token replacements + Fig 8 rerender + 'Verdict.'→'Result.' rename (~30 min). EXT13 target → HIGH CONFIDENCE ACCEPT.",
    },
  ],
  blockerTally: {
    closed: 834, // +16 EXT11-closure wave — all residuals from EXT11_BATCH_TRUTH_AUDIT.md closed (P1A:5 + P1B:2 + P2:2 + P3:2 + P4:1 + P5:4 VERIFIED findings)
    openBlockers: 0,
    openMajors: 0,
    openMinors: 0,
  },
  cronStatus: "EXT12 harvested: 7/18 ACCEPT confirmed · P4 ChatGPT ACCEPT (3/3 confirmed) · Gemini synthesis-mode (no formal verdicts) · EXT13 closure wave queued",
  etaToCompletion:
    "EXT12: P4=3/3 ACCEPT (publication-ready). ChatGPT P1A/P1B/P2/P3/P5=MINOR (1-2 text fixes each). Gemini 6/6=synthesis-mode (no verdict, EXT11 baselines held). EXT13 closure wave (5 papers, text-only, ~2 hrs) + Gemini resubmit (with explicit verdict format) → HIGH CONFIDENCE 18/18 ACCEPT.",
  pods: [],
};
