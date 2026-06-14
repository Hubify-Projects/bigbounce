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
  lastUpdatedISO: "2026-06-13T23:59:00Z",
  lastUpdatedDisplay: "June 13, 2026 · 11:59 PM PT",
  headline:
    "EXT15-closure-wave complete: P1A v1A.0.76 · P2 v1.7.67 · P3 v3.1.110 · P5 v0.1.79 (P1B+P4 FROZEN at universal 3/3 ACCEPT). EXT16 launched — 18 chats submitted. Pattern-052 vindication on P5 (EXT14 flag was false-positive). Target: 18/18 ACCEPT → arXiv coordinated drop.",
  summary:
    "EXT15-closure: P1A v1A.0.76 (3 ChatGPT MINOR + 3 Gemini polish) · P2 v1.7.67 (BF Eq.9 vs Eq.10 mapping + 0.18% typo) · P3 v3.1.110 (Table IX Savage-Dickey KDE values explicit: B_MB/free=3.23; B_MB/SMBHB=7.14e3) · P5 v0.1.79 (pattern-059 sweep: zero residuals, EXT14 flag vindicated as false-positive). P1B v1B.0.72 + P4 v1.0.188 FROZEN — universal 3/3 ACCEPT. EXT16: 18 chats submitted — ChatGPT+Grok in-thread delta; Gemini fresh chats with pattern-058 MNRAS first-line. P1B+P4 courtesy re-confirmation prompts sent. HIGH CONFIDENCE 18/18 ACCEPT.",
  currentlyRunning: [
    "EXT16 harvesting — 18 chats submitted: ChatGPT 6 in-thread · Grok 6 in-thread · Gemini 6 fresh chats (pattern-058 MNRAS first-line). P1B+P4 courtesy re-confirmation prompts included.",
    "Site + SSOT + Convex sync on EXT15-closure-wave bundle",
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
      version: "v1A.0.76",
      readiness: 95,
      pendingWork: "v1A.0.76 — EXT15-closure: 3 ChatGPT MINOR (chirality-flipping + parity-odd amplitude + local-operator-promotion) + 3 Gemini polish. EXT16 submitted. Awaiting harvest (≥30 min).",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.72",
      readiness: 95,
      pendingWork: "v1B.0.72 FROZEN — universal 3/3 ACCEPT at EXT14 (ChatGPT+Grok+Gemini). EXT15+EXT16 courtesy re-confirmation. Queue for arXiv submission.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.67",
      readiness: 95,
      pendingWork: "v1.7.67 — EXT15-closure: BF Eq.9 vs Eq.10 mapping corrected (exact CDF vs large-W approx) + 0.18% arithmetic typo. EXT16 submitted. Awaiting harvest.",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.110",
      readiness: 95,
      pendingWork: "v3.1.110 — EXT15-closure: Table IX Savage-Dickey footnote with explicit KDE values (B_MB/free=3.23; B_MB/SMBHB=7.14e3). EXT16 submitted. Awaiting harvest.",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.188",
      readiness: 95,
      pendingWork: "v1.0.188 FROZEN — universal 3/3 ACCEPT at EXT12+EXT14. EXT15+EXT16 courtesy re-confirmation. Queue for arXiv submission (first in order).",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.79-2026-06-13",
      readiness: 95,
      pendingWork: "v0.1.79 — EXT15-closure: pattern-059 math sweep — ZERO residuals (EXT14 flag was false-positive, pattern-052 vindication). EXT16 submitted. Awaiting harvest.",
    },
  ],
  blockerTally: {
    closed: 856, // +12 EXT15-closure wave — P1A:6 + P2:2 + P3:2 + P5:2 VERIFIED findings closed (P1B+P4 frozen universal ACCEPT)
    openBlockers: 0,
    openMajors: 0,
    openMinors: 0,
  },
  cronStatus: "EXT15-closure-wave COMPLETE: 4 papers bumped (P1B+P4 frozen universal ACCEPT) · EXT16 LAUNCHED: 18 chats submitted · pattern-052 vindication on P5 (false-positive confirmed)",
  etaToCompletion:
    "EXT16 in flight: 18 chats submitted (ChatGPT in-thread · Grok in-thread · Gemini fresh-chat pattern-058 MNRAS first-line; P1B+P4 courtesy re-confirmation). Harvest ETA ≥30 min from last submission. Target: 18/18 ACCEPT → arXiv coordinated drop. Confidence: HIGH.",
  pods: [],
};
