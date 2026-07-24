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
  lastUpdatedDisplay: "July 22, 2026 · Los Angeles (PT)",
  deadlineNote:
    "All six manuscripts are science-complete and review-converged. Every exact-PDF referee board is truth-audited; there is no agent-executable science left on the critical path. Four of the five author decisions are DONE (Zenodo, license, Paper-IV plan, ORCID); the single remaining gate is D4 — arXiv endorsement — plus the submission clicks only Houston can perform. The agent loop executes everything else the moment endorsement lands.",

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
        "DONE 2026-07-21 end-to-end: CC-BY-4.0 chosen; ALL THREE deposits PUBLISHED on Houston's explicit go — namaster-proof 0.1.7 software 10.5281/zenodo.21481753, P1A manuscript 10.5281/zenodo.21481838, P1B manuscript 10.5281/zenodo.21481842 (each MD5-verified, records live). DOIs embedded in-paper since v1A.0.125/v2B.0.13, carried in current v1A.0.126/v2B.0.14 (directive-G PASS). Every paper P1A/P1B/P2/P3/P4 now has a published archival DOI; P5's deposit waits only on the Paper-IV back-patch.",
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
        "CHECKED 2026-07-22 in your live session — ENDORSEMENT IS REQUIRED for BOTH archives (the submit flow rejects gr-qc AND astro-ph with 'You are not endorsed for this archive'). All four category codes are generated and emailed to houston@bamf.ai: gr-qc HYEJ7S (P1A) · astro-ph.IM L8TIPN (P1B, P3) · astro-ph.CO LRZHC4 (P2) · astro-ph.GA CLVMAQ (P4, P5). WHAT TO DO: find an endorser and send them the matching code email. Qualification: any author with 4+ astro-ph.* papers (3 months – 5 years old) can endorse ALL THREE astro-ph codes; gr-qc needs 4+ gr-qc papers specifically. ENDORSER SHORTLIST BUILT + eligibility-verified 2026-07-22 (SSOT/ENDORSER_SHORTLIST_2026-07-22.md): Yi-Fu Cai (all 4 codes — P2 re-derives his matter-bounce amplitude) and Hernán E. Noriega (all 4, DESI DR1) can each clear the ENTIRE portfolio solo; Robert Brandenberger (gr-qc+CO+GA) and Lior Shamir (all 3 astro-ph — P4/P5 engage his chirality work directly) are the strong pairings. Forward them the matching code email(s). PARALLEL PATH while endorsement resolves: all six papers already have published Zenodo DOIs (citable now), and journal submissions (CQG, JORS, ApJS, PRD, AJ) do not require arXiv. Draft submission 7859751 is parked at the Start step (agreement accepted, CC BY 4.0 selected) ready to continue the moment endorsement lands.",
      unblocks: "All submissions.",
    },
    {
      id: "D5",
      title: "ORCID",
      status: "done",
      options: "Confirm the correct ORCID iD for all submission metadata.",
      recommendation:
        "DONE 2026-07-22: Houston verified from his signed-in orcid.org record that his actual iD is 0009-0008-5616-5994 — the …3617-8729 iD carried in earlier briefs was WRONG and has been purged from every actionable doc (kits, runbook, preflight checklist, queue; it never entered any manuscript — verified by repo-wide grep). One optional step remains: associate the iD with the arXiv account via arxiv.org/user → 'confirm your ORCID iD' (Houston's OAuth click).",
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
        "P2 v1.7.128 and P4 v1.0.271 PDFs are built, mirrored, and synchronized; the wave-2 kit references the new confirmation-wave tarballs. Submits right after wave 1.",
    },
    {
      id: "wave-3",
      label: "Wave 3 — after P4's arXiv ID",
      order: ["P5"],
      state: "queued",
      note:
        "P5 v0.1.142 is ready and submits once P4 (its Paper IV anchor) has an arXiv ID to back-patch, per decision D3.",
    },
  ],

  blockers: [
    {
      title: "arXiv endorsement risk",
      severity: "blocker",
      decision: "D4",
      detail:
        "CONFIRMED 2026-07-22: endorsement required for BOTH gr-qc and astro-ph. Four codes live (emailed to houston@bamf.ai): HYEJ7S (gr-qc), L8TIPN (astro-ph.IM), LRZHC4 (astro-ph.CO), CLVMAQ (astro-ph.GA). One astro-ph-qualified endorser can clear three of the four. Journal + Zenodo routes remain open in parallel.",
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
      version: "v1A.0.126",
      readiness: 95,
      board:
        "2026-07-22 pre-arXiv confirmation wave: 18 exact-PDF INT legs (Grok+Gemini+Claude) truth-audited; all genuinely-new-real items closed same-day. P1A v1A.0.126 board Grok ACCEPT / Gemini MINOR / Claude MINOR; 3 closures (archival DOI in active availability, Fierz attribution, operator cross-note).",
      wave: "wave-1",
      remaining: ["D2", "D4", "D5"],
    },
    {
      code: "P1B",
      slug: "paper-1b",
      title: "namaster-proof: pseudo-C_ℓ window inference & content-bound validation",
      version: "v2B.0.14",
      readiness: 95,
      board:
        "2026-07-22 pre-arXiv confirmation wave: 18 exact-PDF INT legs (Grok+Gemini+Claude) truth-audited; all genuinely-new-real items closed same-day. P1B v2B.0.14 board all-MINOR; DOI floor CLOSED (software + manuscript DOIs published and cited in-paper); 3 presentation closures.",
      wave: "wave-1",
      remaining: ["D1", "D2", "D4", "D5"],
    },
    {
      code: "P3",
      slug: "paper-3",
      title: "Public-ID Recovery for a Historical DESI DR1 Anomaly List",
      version: "v3.2.0-r13",
      readiness: 95,
      board:
        "2026-07-22 pre-arXiv confirmation wave: 18 exact-PDF INT legs (Grok+Gemini+Claude) truth-audited; all genuinely-new-real items closed same-day. P3 v3.2.0-r13 board Grok ACCEPT / Gemini MAJOR (venue-opinion, dispositioned) / Claude MINOR; 3 closures incl. the annulus-deficit honesty rewrite.",
      wave: "wave-1",
      remaining: ["D1", "D4", "D5"],
    },
    {
      code: "P2",
      slug: "paper-2",
      title: "f_NL forecast — Einstein–Cartan bounce non-Gaussianity",
      version: "v1.7.128",
      readiness: 95,
      board:
        "2026-07-22 pre-arXiv confirmation wave: 18 exact-PDF INT legs (Grok+Gemini+Claude) truth-audited; all genuinely-new-real items closed same-day. P2 v1.7.128 board Grok MAJOR (both majors dispositioned DISCLOSED-RE-FLAG with citations) / Gemini MINOR / Claude MINOR; 5 numeric-transparency closures, −35/16 untouched.",
      wave: "wave-2",
      remaining: ["D1", "D4", "D5"],
    },
    {
      code: "P4",
      slug: "paper-4",
      title: "Galaxy chirality dipole — DESI/GZ1 chirality catalog (Paper IV)",
      version: "v1.0.271",
      readiness: 95,
      board:
        "Last board Grok ACCEPT / Gemini MINOR — the CE-composition sub-conflict adjudicated and the honest-negative integrated, praised by both reviewers. Submits before P5 (it is P5's Paper IV anchor, per D3).",
      wave: "wave-2",
      remaining: ["D1", "D3", "D4", "D5"],
    },
    {
      code: "P5",
      slug: "paper-5",
      title: "DESI void-environment chirality null",
      version: "v0.1.142-2026-07-22",
      readiness: 95,
      board:
        "Exact v0.1.140 board Grok MAJOR / Gemini MINOR / Claude MAJOR (18 findings) → 1 genuinely-new-real closed in v0.1.141 with a real forward-leakage injection. Exact v0.1.141 confirmation pending.",
      wave: "wave-3",
      remaining: ["D1", "D3", "D4", "D5"],
    },
  ],
};
