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
  lastUpdatedISO: "2026-06-13T23:30:00Z",
  lastUpdatedDisplay: "June 13, 2026 · 4:30 PM PT",
  headline:
    "EXT10-MILESTONE: 18/18 MINOR REVISIONS — zero MAJORs across all 6 papers. EXT10-closure-wave addresses every VERIFIED-OPEN item; path to 18/18 ACCEPT = HIGH confidence 1-cycle.",
  summary:
    "EXT10 = 18/18 MINOR (first time in EXT history with zero MAJORs). ChatGPT cleared both remaining MAJORs (P1A Fig 3 caption + P3 Table II). EXT10-closure-wave lands: P1A v1A.0.73 / P1B v1B.0.70 / P2 v1.7.64 / P3 v3.1.107 / P4 v1.0.187 / P5 v0.1.76. P4 Shamir [2] bibchimera fixed (arXiv:2208.00893). P5 V-Web→T-Web rename (235+/181- lines). Tarballs rebuilt to ship state.",
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
      version: "v1A.0.73",
      readiness: 95,
      pendingWork: "v1A.0.73 — EXT10-closure: Sec IV→App B explicit ref + Route 2 sharpener + WKB 10⁻³⁵ eV inlined; EXT10=18/18 MINOR; awaiting Houston sign-off",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.70",
      readiness: 94,
      pendingWork: "v1B.0.70 — EXT10-closure: 6 wording fixes (pairing-swap test note + 40.5 H₀ posterior + phantom-crossing caveats + UV-completion-independent + release-pairing); EXT10=18/18 MINOR; awaiting Houston sign-off",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.64",
      readiness: 94,
      pendingWork: "v1.7.64 — EXT10-closure: 9 wording fixes (CGT M1/M2/M3/M9 stress-test + UV-independence + denominator def + contamination scale + channel hierarchy + UMF universality); EXT10=18/18 MINOR; awaiting Houston sign-off",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.107",
      readiness: 95,
      pendingWork: "v3.1.107 — EXT10-closure: top-1%→S>5 (0.87%) + catalog-grade reinforce in abstract + NANOGrav BF prior-sensitivity table (γ∈[0,5]/[0,7]/[1,6]/[2,5] all decisive); EXT10=18/18 MINOR; awaiting Houston sign-off",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.187",
      readiness: 95,
      pendingWork: "v1.0.187 — EXT10-closure: Shamir [2] bibchimera FIXED (arXiv:2208.00893) + 6 wording; EXT10=18/18 MINOR; awaiting Houston sign-off",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.76-2026-06-13",
      readiness: 95,
      pendingWork: "v0.1.76 — EXT10-closure: V-Web→T-Web rename (235+/181-) + sample-count 783,820 confirmed + frozen-analysis-tree note; EXT10=18/18 MINOR; awaiting Houston sign-off",
    },
  ],
  blockerTally: {
    closed: 818, // +35 EXT10-closure wave — every VERIFIED-OPEN item from EXT10_BATCH_TRUTH_AUDIT.md addressed
    openBlockers: 0,
    openMajors: 0,
    openMinors: 0,
  },
  cronStatus: "autonomous review loop active — EXT11 ready to fire",
  etaToCompletion:
    "EXT10=18/18 MINOR (zero MAJORs — historic milestone). EXT10-closure-wave bundles all 6 papers. Path to 18/18 ACCEPT = HIGH confidence 1-cycle. Gated on Houston sign-off + EXT11.",
  pods: [],
};
