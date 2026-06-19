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
  lastUpdatedISO: "2026-06-18T12:00:00Z",
  lastUpdatedDisplay: "June 18, 2026 · 12:00 PM PT",
  headline:
    "R40 internal 5-model adversarial round + EXT20 external fresh-referee round complete: all 6 papers ACCEPT, 0 blockers. P1B earns 99 (R40 cosmetic closures confirmed). PDFs updated: P1A v1A.0.78 · P2 v1.7.70 · P3 v3.1.112 · P5 v0.1.82. Drop-ready pending Houston sign-off + ORCID flip.",
  summary:
    "R40 internal 5-model adversarial round (all 6 papers, 3 cosmetic closures P1A/P3/P5, P1B→99) complete 2026-06-18. EXT20 external fresh-referee round (all 6 ACCEPT, 0 blockers, 2 trivial micro-fixes P2/P5) confirmed same day. P1B rises to 99 following R40 clean round. PDFs bumped and mirrored: P1A v1A.0.78 (md5 198cb994), P2 v1.7.70 (md5 99e6426c), P3 v3.1.112 (md5 62d7b294), P5 v0.1.82 (md5 401a73f9). Six tarballs staged for arXiv drop.",
  currentlyRunning: [
    "R40 internal adversarial round complete + EXT20 external ACCEPT × 6 — all papers drop-ready.",
    "Release waits only on Houston's two gates: ORCID public flip + arXiv drop authorization.",
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
      version: "v1A.0.78",
      readiness: 99,
      pendingWork: "v1A.0.78 — R40 + EXT20 ACCEPT (6/6). Drop-ready. Final 1% = Houston sign-off + arXiv drop.",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.74",
      readiness: 99,
      pendingWork: "v1B.0.74 — R40 clean round confirmed → 99. EXT20 ACCEPT. Drop-ready.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.70",
      readiness: 99,
      pendingWork: "v1.7.70 — EXT20 2 trivial micro-fixes closed; ACCEPT. Drop-ready.",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.112",
      readiness: 99,
      pendingWork: "v3.1.112 — R40 + EXT20 ACCEPT (6/6). Drop-ready. Final 1% = Houston sign-off + arXiv drop.",
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
      version: "v0.1.82-2026-06-18",
      readiness: 99,
      pendingWork: "v0.1.82 — EXT20 2 trivial micro-fixes closed; ACCEPT. Drop-ready pending Houston title count decision + arXiv drop.",
    },
  ],
  blockerTally: {
    closed: 864, // EXT17 closure wave — P1A + P2 + P3 + P5 EXT16-MINORs resolved to ACCEPT; P1B + P4 frozen universal ACCEPT
    openBlockers: 0,
    openMajors: 0,
    openMinors: 0,
  },
  cronStatus: "R40 internal adversarial + EXT20 external ACCEPT × 6 complete (2026-06-18). P1B→99. P1A/P2/P3/P5 PDFs bumped and mirrored.",
  etaToCompletion:
    "Papers + tarballs are drop-ready. Release waits only on Houston's two gates: ORCID public flip (pub.orcid.org → 200) and arXiv drop authorization. Submit order P4 → P1A → P1B → P3 → P2 → P5 in one hour.",
  pods: [],
};
