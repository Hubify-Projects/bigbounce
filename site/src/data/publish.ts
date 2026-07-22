// Publication Command Center data — drives /publish.
//
// Source of truth: project-context/PUBLICATION_DECISION_BRIEF_2026-07-20.md
// and project-context/SSOT/WAVE1_SUBMISSION_KIT_2026-07-19.md.
//
// Status chips are PLACEHOLDERS driven from this file so a future sync can flip
// a decision's `status` from "pending" to "done" (or a wave's `state`) in one
// edit and the page re-renders. Nothing here is a journal decision; these are
// the author-only decisions and click actions that remain on the critical path.

export type DecisionStatus = "pending" | "done";

export interface PublishDecision {
  /** D1..D5 */
  id: string;
  title: string;
  status: DecisionStatus;
  /** true = the one item that can structurally slip the deadline */
  scheduleRisk?: boolean;
  /** the choice in front of Houston */
  options: string;
  /** the kit/brief recommendation */
  recommendation: string;
  /** what making the decision unblocks */
  unblocks: string;
}

export type WaveState = "ready" | "building" | "queued";

export interface PublishWave {
  id: string;
  label: string;
  /** ordered submission sequence, e.g. ["P1B", "P1A", "P3"] */
  order: string[];
  state: WaveState;
  note: string;
  /** repo-relative kit path if one exists */
  kit?: string;
}

export type BlockerSeverity = "blocker" | "clear";

export interface PublishBlocker {
  title: string;
  severity: BlockerSeverity;
  detail: string;
  decision?: string; // e.g. "D4"
}

export type PaperWave = "wave-1" | "wave-2" | "wave-3";

export interface PaperReadiness {
  code: string; // P1A, P1B, ...
  slug: string;
  title: string;
  version: string;
  readiness: number;
  /** one-liner: the last exact-PDF board + disposition */
  board: string;
  wave: PaperWave;
  /** which D-items still gate this paper's submission */
  remaining: string[];
}

export interface PublishData {
  lastUpdatedDisplay: string;
  deadlineNote: string;
  decisions: PublishDecision[];
  waves: PublishWave[];
  blockers: PublishBlocker[];
  papers: PaperReadiness[];
}

export const publishData: PublishData = {
  lastUpdatedDisplay: "July 20, 2026 · Los Angeles (PT)",
  deadlineNote:
    "All six manuscripts are science-complete and review-converged. Every exact-PDF referee board is truth-audited; there is no agent-executable science left on the critical path. What remains is five decisions only Houston can make and the submission clicks only Houston can perform — the agent loop executes everything else the moment each decision lands.",

  decisions: [
    {
      id: "D1",
      title: "Zenodo token",
      status: "done",
      options: "Paste a personal-access token with the deposit:write scope.",
      recommendation:
        "DONE 2026-07-20: token provided; DOIs minted + embedded — P2 10.5281/zenodo.21461881, P3 …21461888, P4 …21461899 (receipts in SSOT/zenodo/).",
      unblocks:
        "DOIs for P1B (its only reviewer major), P2, P3, P4, and the dataset archives.",
    },
    {
      id: "D2",
      title: "License for P1A + P1B",
      status: "done",
      options: "arXiv perpetual non-exclusive license, or CC-BY-4.0.",
      recommendation:
        "DONE 2026-07-21: Houston chose CC-BY-4.0 (per recommendation). Authorization recorded via tools/d2_authorize_deposits.py. Same hour: namaster-proof 0.1.7 software DOI PUBLISHED (10.5281/zenodo.21481753 — P1B's software prerequisite, Houston-authorized); P1A and P1B Zenodo drafts uploaded + MD5-verified with prereserved DOIs 10.5281/zenodo.21481838 (P1A) and …21481842 (P1B). Publishing those two paper DOIs is one explicit go from Houston.",
      unblocks: "Deposit staging + arXiv submission for both P1A and P1B (P5's deposit shares the license; its remaining gate is the Paper-IV back-patch).",
    },
    {
      id: "D3",
      title: "Paper IV (P5's anchor)",
      status: "done",
      options:
        "(a) Publish Paper IV as a companion arXiv preprint alongside P5, or (b) fold a minimal validation appendix into P5 and drop the dependency.",
      recommendation:
        "(a) — Paper IV IS the P4 manuscript lineage. Concretely: submit P4 first, then back-patch its arXiv ID into P5. P5's reviewers all asked for the catalog paper public, not perfect.",
      unblocks: "P5 submission (after P4's arXiv ID exists).",
    },
    {
      id: "D4",
      title: "arXiv account + endorsement",
      status: "pending",
      scheduleRisk: true,
      options:
        "Confirm submit privileges for gr-qc (P1A), astro-ph.IM (P1B, P3), and astro-ph.GA (P3 cross-list) at arxiv.org → Submit.",
      recommendation:
        "Check this FIRST today. A first-time gr-qc submission may need an endorsement, which can take 1–2 days — this is the only thing that can structurally slip the deadline. (Checked 2026-07-21: no live arXiv session in the browser — log in at arxiv.org, then the agent can read the endorsement status from your session, or check Submit → 'Start a new submission' yourself: if gr-qc appears in the category list without an endorsement warning, you're clear.)",
      unblocks: "All submissions.",
    },
    {
      id: "D5",
      title: "ORCID",
      status: "pending",
      options: "Confirm 0009-0008-3617-8729 is YOUR ORCID iD (not someone else's or a typo).",
      recommendation:
        "~1 min, concretely: go to orcid.org and sign in (or register free if you never have — takes 2 min). Your iD is shown right under your name on your record page. If it reads 0009-0008-3617-8729, say 'yes that's me'. If it's different — or you had no account — give the real iD and all submission metadata will use that instead. (The public record for …8729 currently shows no public name, so it can't be verified from outside; only you can check it from inside your account.)",
      unblocks: "Metadata correctness everywhere.",
    },
  ],

  waves: [
    {
      id: "wave-1",
      label: "Wave 1 — kit ready",
      order: ["P1B", "P1A", "P3"],
      state: "ready",
      note:
        "Three tarballs standalone-compile clean (0 errors / 0 undef-ref), metadata is paste-ready, and no cross-citation back-patch is needed — each submits independently. ~10 min of clicks each.",
      kit: "project-context/SSOT/WAVE1_SUBMISSION_KIT_2026-07-19.md",
    },
    {
      id: "wave-2",
      label: "Wave 2 — kit building now",
      order: ["P2", "P4"],
      state: "building",
      note:
        "P2 v1.7.125 and P4 v1.0.268 PDFs are built, mirrored, and synchronized. The paste-ready wave-2 kit is being assembled now; submits right after wave 1.",
    },
    {
      id: "wave-3",
      label: "Wave 3 — after P4's arXiv ID",
      order: ["P5"],
      state: "queued",
      note:
        "P5 v0.1.141 is ready and submits once P4 (its Paper IV anchor) has an arXiv ID to back-patch, per decision D3.",
    },
  ],

  blockers: [
    {
      title: "arXiv endorsement risk",
      severity: "blocker",
      decision: "D4",
      detail:
        "A first-time gr-qc (and possibly astro-ph.IM) submission may require an endorsement, which can take 1–2 days to obtain. This is the only item that can structurally slip the deadline — check submit privileges FIRST today.",
    },
    {
      title: "Science & manuscripts",
      severity: "clear",
      detail:
        "All six papers are review-converged; every exact-PDF board is truth-audited with zero genuinely-new-real findings outstanding on the critical path.",
    },
    {
      title: "Tarballs, PDFs & evidence chains",
      severity: "clear",
      detail:
        "Wave-1 tarballs are standalone-verified with proof receipts; all PDFs are built, mirrored byte-identical, and synchronized across surfaces.",
    },
    {
      title: "Datasets & site",
      severity: "clear",
      detail:
        "The HuggingFace catalog release is public (flip-verified at post time), and the site/SSOT/Convex surfaces are current.",
    },
  ],

  papers: [
    {
      code: "P1A",
      slug: "paper-1a",
      title: "Algebraic Cartan Elimination in Minimal Einstein–Cartan–Holst Gravity",
      version: "v1A.0.124",
      readiness: 62,
      board:
        "Exact v1A.0.124 board Grok MINOR / Gemini MINOR / Claude MAJOR (13 findings) → 0 genuinely-new-real. CONVERGED to human gates.",
      wave: "wave-1",
      remaining: ["D2", "D4", "D5"],
    },
    {
      code: "P1B",
      slug: "paper-1b",
      title: "namaster-proof: pseudo-C_ℓ window inference & content-bound validation",
      version: "v2B.0.11",
      readiness: 56,
      board:
        "Exact v2B.0.9 board Grok REJECT / Gemini MINOR / Claude MAJOR → the 'workspace tensor not reproducible' premise FALSIFIED; closed in v2B.0.10/.11.",
      wave: "wave-1",
      remaining: ["D1", "D2", "D4", "D5"],
    },
    {
      code: "P3",
      slug: "paper-3",
      title: "Public-ID Recovery for a Historical DESI DR1 Anomaly List",
      version: "v3.2.0-r10",
      readiness: 56,
      board:
        "Exact v3.2.0-r9 board Grok ACCEPT (its first) / Gemini MINOR / Claude MAJOR → the circularity finding CONFIRMED genuinely-new-real and closed in v3.2.0-r10 with an integrity reframe. License already defaults CC-BY-4.0.",
      wave: "wave-1",
      remaining: ["D1", "D4", "D5"],
    },
    {
      code: "P2",
      slug: "paper-2",
      title: "f_NL forecast — Einstein–Cartan bounce non-Gaussianity",
      version: "v1.7.125",
      readiness: 80,
      board:
        "Prior Claude-leg exact-PDF board v1.7.122 MAJOR (3M/6m) → 0 genuinely-new-real; v1.7.125 lands a real-compute torsion-bound closure. Exact v1.7.125 confirmation pending.",
      wave: "wave-2",
      remaining: ["D1", "D4", "D5"],
    },
    {
      code: "P4",
      slug: "paper-4",
      title: "Galaxy chirality dipole — DESI/GZ1 chirality catalog (Paper IV)",
      version: "v1.0.268",
      readiness: 80,
      board:
        "Last board Grok ACCEPT / Gemini MINOR — the CE-composition sub-conflict adjudicated and the honest-negative integrated, praised by both reviewers. Submits before P5 (it is P5's Paper IV anchor, per D3).",
      wave: "wave-2",
      remaining: ["D1", "D3", "D4", "D5"],
    },
    {
      code: "P5",
      slug: "paper-5",
      title: "DESI void-environment chirality null",
      version: "v0.1.141",
      readiness: 74,
      board:
        "Exact v0.1.140 board Grok MAJOR / Gemini MINOR / Claude MAJOR (18 findings) → 1 genuinely-new-real closed in v0.1.141 with a real forward-leakage injection. Exact v0.1.141 confirmation pending.",
      wave: "wave-3",
      remaining: ["D1", "D3", "D4", "D5"],
    },
  ],
};
