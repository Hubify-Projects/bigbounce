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
  lastUpdatedISO: "2026-06-14T19:45:00Z",
  lastUpdatedDisplay: "June 14, 2026 · 12:45 PM PT",
  headline:
    "EXT17 complete — 18/18 ACCEPT across ChatGPT · Grok · Gemini. The 17-round external review campaign closed at universal ACCEPT: publication green light. EXT18 verification round complete — 4/6 papers clean; P1B + P2 had real residual fixes, now closed (v1B.0.73 / v1.7.69). Awaiting Houston's ORCID public flip + coordinated arXiv drop.",
  summary:
    "All six papers cleared EXT17 at universal ACCEPT (EXT16 14/18 → EXT17 18/18). Canonical, tarball-ready: P1A v1A.0.77 · P1B v1B.0.73 · P2 v1.7.69 · P3 v3.1.111 · P4 v1.0.188 (FROZEN) · P5 v0.1.80. EXT18 native-PDF cross-vendor round caught + closed an Ωa relic-arithmetic slip in P1B and 3 consistency fixes in P2; P1A/P3/P4/P5 clean. Tarballs staged for a one-hour coordinated drop (P4 first).",
  currentlyRunning: [
    "EXT18 verification round closed: P1B + P2 residual fixes landed (v1B.0.73 / v1.7.69); P1A/P3/P4/P5 audited clean. 4-vendor round (Anthropic API leg out of credits).",
    "Drop-readiness hold: six tarballs staged, abstracts + Zenodo one-click prepared; release waits only on Houston's two gates.",
  ],
  needsHouston: [
    {
      title: "ORCID public flip (only hard blocker)",
      blockedPaper: "all",
      why: "arXiv submission requires the author ORCID 0009-0008-3617-8729 to resolve publicly; pub.orcid.org currently returns 404, not 200.",
      ask: "At orcid.org set Names/Employment/Education to PUBLIC, then confirm `curl -s -o /dev/null -w '%{http_code}' https://pub.orcid.org/v3.0/0009-0008-3617-8729/person` returns 200.",
    },
    {
      title: "Resolve P5 title galaxy count",
      blockedPaper: "P5",
      why: "P5 title shows '791,635 DR1 Matched Spirals' vs the environment-matched '783,820' — a one-line Houston decision before P5's tarball is final.",
      ask: "Confirm the headline count (recommend 783,820 environment-matched); P5 tarball rebuilds in one command if changed.",
    },
    {
      title: "Authorize the coordinated arXiv drop",
      blockedPaper: "all",
      why: "Only Houston holds the arXiv account + astro-ph endorser relationships; all six tarballs are staged and drop-ready.",
      ask: "Give the go and submit in order P4 → P1A → P1B → P3 → P2 → P5 (P4 first; P5 needs P4's arXiv ID).",
    },
  ],
  papers: [
    {
      slug: "paper-1a",
      number: "1A",
      shortTitle: "ECH dark-energy closure + perturbation transparency",
      version: "v1A.0.77",
      readiness: 99,
      pendingWork: "v1A.0.77 — EXT17 ACCEPT (ChatGPT + Grok + Gemini). Drop-ready; EXT18 verification clean. Final 1% = Houston sign-off + arXiv drop.",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.73",
      readiness: 98,
      pendingWork: "v1B.0.73 — EXT18 corrected Ωa relic-subsection arithmetic (post-freeze slip); EXT17 was 3/3 ACCEPT. Awaiting confirmation, then drop.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.69",
      readiness: 98,
      pendingWork: "v1.7.69 — EXT18 closed 3 internal-consistency fixes; EXT17 was ACCEPT. Awaiting confirmation, then drop.",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.111",
      readiness: 99,
      pendingWork: "v3.1.111 — EXT17 ACCEPT (ChatGPT + Grok + Gemini). Drop-ready; EXT18 verification clean. Final 1% = Houston sign-off + arXiv drop.",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.188",
      readiness: 99,
      pendingWork: "v1.0.188 FROZEN — universal 3/3 ACCEPT across EXT12 + EXT14 + EXT16 + EXT17 (5 rounds; first-ever ChatGPT ACCEPT). Drop-ready; submits first in order.",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.80-2026-06-13",
      readiness: 99,
      pendingWork: "v0.1.80 — EXT17 ACCEPT (first ChatGPT ACCEPT for P5; Grok + Gemini ACCEPT). One open Houston decision: title galaxy count (791,635 vs 783,820).",
    },
  ],
  blockerTally: {
    closed: 864, // EXT17 closure wave — P1A + P2 + P3 + P5 EXT16-MINORs resolved to ACCEPT; P1B + P4 frozen universal ACCEPT
    openBlockers: 0,
    openMajors: 0,
    openMinors: 0,
  },
  cronStatus: "EXT17 CLOSED — 18/18 ACCEPT. Publication green light. EXT18 verification round complete: P1B v1B.0.73 + P2 v1.7.69 closures; P1A/P3/P4/P5 clean.",
  etaToCompletion:
    "Papers + tarballs are drop-ready. Release waits only on Houston's two gates: ORCID public flip (pub.orcid.org → 200) and arXiv drop authorization. Submit order P4 → P1A → P1B → P3 → P2 → P5 in one hour.",
  pods: [],
};
