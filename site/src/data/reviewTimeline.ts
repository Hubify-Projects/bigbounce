export type ReviewRoundKind =
  | "external-browser"
  | "internal-api"
  | "internal-cc"
  | "skill-improvement"
  | "closure-wave";

export type PaperId = "P1A" | "P1B" | "P2" | "P3" | "P4" | "P5";

export interface ReviewRoundLink {
  label: string;
  href: string;
}

export interface GapMetric {
  /** Findings only the external tier caught — the internal/external gap. */
  externalOnlyFindings: number;
  note: string;
}

/**
 * One event on the review-activity timeline. ALL strings are ONE-LINE only —
 * long-form round reports live as markdown files under site/public/reviews/
 * and render at /reviews/<reportSlug>.
 */
export interface ReviewRound {
  id: string;
  kind: ReviewRoundKind;
  dateISO: string;
  title: string;
  papers: PaperId[];
  summary: string;
  keyTakeaways: string[];
  gapMetric?: GapMetric;
  links: ReviewRoundLink[];
  /** Slug of a markdown report at /reviews/<slug> (file: public/reviews/<slug>.md). */
  reportSlug?: string;
}

const GH = "https://github.com/Hubify-Projects/bigbounce/blob/main";
const PR = `${GH}/project-context/peer-reviews`;

/** Authored newest-first; the page re-sorts by dateISO desc (stable on ties). */
export const reviewRounds: ReviewRound[] = [
  {
    id: "EXT1",
    kind: "external-browser",
    dateISO: "2026-06-10",
    title: "EXT1 — first automated browser-tier external round: 6 papers × 3 frontier web apps, 18 submissions",
    papers: ["P1A", "P1B", "P2", "P3", "P4", "P5"],
    summary: "All six current PDFs (md5-verified against site mirrors) submitted to ChatGPT Pro Extended, Grok Heavy, and Gemini Thinking via the logged-in browser loop; reports harvest into the truth-audit next.",
    keyTakeaways: [
      "18/18 submissions confirmed, with model + effort tier verified in each provider UI before every send",
      "Each chat carries the calibration-armed referee prompt scraped live from this site's per-paper pages",
      "Chat threads are reusable: EXT2 posts revised PDFs + delta-prompts into the SAME threads to keep referee context",
      "Harvest order: Grok + Gemini first, ChatGPT Pro Extended last (30–60+ min per chat), then /peer-review-truth-audit",
    ],
    gapMetric: {
      externalOnlyFindings: 0,
      note: "harvest pending — the internal/external gap for this round is measured after truth-audit",
    },
    links: [
      { label: "P1A · ChatGPT", href: "https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e5e8-96cc-83e8-918f-3b1dd3f96d96" },
      { label: "P1A · Grok", href: "https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=5abdb89c-8b7d-4ec0-8839-c39f5a634f03" },
      { label: "P1A · Gemini", href: "https://gemini.google.com/app/1f57c90ded367b75" },
      { label: "P1B · ChatGPT", href: "https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e620-242c-83e8-80a6-225f2095aded" },
      { label: "P1B · Grok", href: "https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=33f977da-4a3e-44b6-a6e4-599ae00d5c3e" },
      { label: "P1B · Gemini", href: "https://gemini.google.com/app/436b30bedb64f8b6" },
      { label: "P2 · ChatGPT", href: "https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e646-8510-83e8-8999-77b849c6519d" },
      { label: "P2 · Grok", href: "https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=0c4cb7d1-7bc6-4033-a4ac-f4605ec99269" },
      { label: "P2 · Gemini", href: "https://gemini.google.com/app/a08d4fb7ec3bcf99" },
      { label: "P3 · ChatGPT", href: "https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e669-b608-83e8-9c0c-e7f247ff271a" },
      { label: "P3 · Grok", href: "https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=de56f195-4cae-4dc6-bc3e-f9dbf4de9b54" },
      { label: "P3 · Gemini", href: "https://gemini.google.com/app/5f938f572975de0c" },
      { label: "P4 · ChatGPT", href: "https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6c4-0764-83e8-b198-03092b27ba37" },
      { label: "P4 · Grok", href: "https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=411d5219-2864-4196-8d60-da2c97771cc0" },
      { label: "P4 · Gemini", href: "https://gemini.google.com/app/b444fd1d491c74ae" },
      { label: "P5 · ChatGPT", href: "https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6e9-b9a4-83e8-9624-ec9291ae8064" },
      { label: "P5 · Grok", href: "https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=edd1963e-cc7e-4a86-b288-1a7834c9e45a" },
      { label: "P5 · Gemini", href: "https://gemini.google.com/app/3cbe98b65fe83d40" },
      { label: "manifest · GitHub", href: `${PR}/EXT1_BROWSER_MANIFEST.md` },
    ],
    reportSlug: "ext1-browser-manifest",
  },
  {
    id: "SKILL-EXT-LOOP",
    kind: "skill-improvement",
    dateISO: "2026-06-10",
    title: "Internal-skill upgrade — calibration-armed referee prompts + reusable-thread protocol for external rounds",
    papers: ["P1A", "P1B", "P2", "P3", "P4", "P5"],
    summary: "Lessons mined from earlier external reviews hardened into the loop: prompts now pre-empt known false-positive classes and external threads persist across rounds.",
    keyTakeaways: [
      "Referee prompts pre-empt 5 known false-positive classes: future-dated arXiv IDs, deliberate correction notes, placeholder companion cites, labeled conservatism, PDF-extraction artifacts",
      "Prompts are generated per-paper on the live site, so external reviewers always receive the current version + focus areas",
      "/external-review-browser-loop automates submission to logged-in provider web apps with model/effort verification before each send",
    ],
    links: [
      { label: "review-patterns catalog", href: `${GH}/project-context/review-patterns` },
      { label: "findings archive", href: `${PR}/findings-archive` },
    ],
  },
  {
    id: "R23-R26-ROLLUP",
    kind: "closure-wave",
    dateISO: "2026-06-10",
    title: "Internal campaign rollup — R23conf → R26conf: ~700 findings truth-audited, 5 pipeline bugs found + fixed",
    papers: ["P1A", "P1B", "P2", "P3", "P4", "P5"],
    summary: "Four back-to-back full five-vendor confirmation rounds over 2026-06-08..10; every VERIFIED finding closed same-day in bundled hard-fix waves, all version bumps mirrored to this site in the same commit.",
    keyTakeaways: [
      "5 pipeline bugs found + fixed, including the P4 all-CW null-generator selection bug and the P5 ZONEVOID zone-offset join bug",
      "Three of six papers reached the sign-off gate (P4 v1.0.171, P2 v1.7.48, P1B v1B.0.54); the rest carry derivation/recompute residue only",
      "Zero arithmetic errors survived the final wave — every committed number chain-reproduced or corrected in-text",
    ],
    links: [
      { label: "SSOT dashboard", href: `${GH}/project-context/SSOT/index.md` },
      { label: "peer-reviews directory", href: "https://github.com/Hubify-Projects/bigbounce/tree/main/project-context/peer-reviews" },
    ],
  },
  {
    id: "R26conf",
    kind: "internal-api",
    dateISO: "2026-06-10",
    title: "R26conf — five-vendor confirmation round: P1B clean, three of six papers at the sign-off gate",
    papers: ["P1A", "P1B", "P3", "P5"],
    summary: "Zero arithmetic errors across the wave; P1B round clean → sign-off-ready; P1A/P3/P5 carry derivation/recompute residue only and queue for R27conf.",
    keyTakeaways: [
      "P1B v1B.0.54: lone substantive accusation (CPL crossing) falsified by shown arithmetic (z* = +0.39 inside range); every committed number chain-reproduced",
      "P1A v1A.0.56: Cartan factor-2 normalization inconsistency disclosed (single-convention re-derivation queued) + dimensionally inconsistent thermal clause removed",
      "P3 v3.1.87: 12 textual closures — cluster accounting made exact from the dedup artifact; NANOGrav Eq. E1 claim falsified by rederivation",
      "P5 v0.1.60: 9 closures including code-verified tidal-tensor sign documentation",
    ],
    links: [
      { label: "P1B synthesis", href: `${PR}/R26conf_P1B_SYNTHESIS.md` },
      { label: "P1B truth-audit", href: `${PR}/R26conf_P1B_TRUTH_AUDIT.md` },
      { label: "P1A synthesis", href: `${PR}/R26conf_P1A_SYNTHESIS.md` },
      { label: "P3 synthesis", href: `${PR}/R26conf_P3_SYNTHESIS.md` },
    ],
  },
  {
    id: "R25conf",
    kind: "internal-api",
    dateISO: "2026-06-10",
    title: "R25conf — priority round on P2 + P4: both clean, first papers to reach the sign-off gate",
    papers: ["P2", "P4"],
    summary: "P4 completes its 2-of-2 post-retraction clean requirement and P2 comes back clean — both marked READY-FOR-SUBMISSION pending Houston sign-off.",
    keyTakeaways: [
      "P4 v1.0.170: round 2-of-2 clean post-retraction — 93 findings audited; one substantive catch (App A field-convention description) closed same-day, no number changed",
      "P2 v1.7.48: round clean — GR-degradation calibration corrected ~15% → ~23% (c9k-verified); σ_theory continuous-marginalization ranking stable (c9l)",
      "Readiness P4 85 → 95 and P2 92 → 95 under the 99%-cap rule; the final 1% is Houston-only",
    ],
    links: [
      { label: "P4 synthesis", href: `${PR}/R25conf_P4_SYNTHESIS.md` },
      { label: "P4 truth-audit", href: `${PR}/R25conf_P4_TRUTH_AUDIT.md` },
      { label: "P2 synthesis", href: `${PR}/R25conf_P2_SYNTHESIS.md` },
      { label: "P2 truth-audit", href: `${PR}/R25conf_P2_TRUTH_AUDIT.md` },
    ],
  },
  {
    id: "R24conf",
    kind: "internal-api",
    dateISO: "2026-06-10",
    title: "R24conf — full five-vendor confirmation round on all six papers: ~110 verified findings closed",
    papers: ["P1A", "P1B", "P2", "P3", "P4", "P5"],
    summary: "Confirmation round on the R23conf versions; all six papers bumped with 0-error compiles, every closure mirrored to the site same-commit.",
    keyTakeaways: [
      "P5 v0.1.54: ZONEVOID zone-offset join bug found + fixed — GALZONE void counts corrected, conclusion unchanged, earlier-draft disclosure added in §VIII.D",
      "P2 v1.7.47: two substantive physics fixes — QSFI scaling endpoints corrected per Chen–Wang; −35/16 result re-attributed to Li–Quintin–Wang–Cai at 17 sites",
      "P1B v1B.0.53: S8 marginal corrected 0.831 ± 0.018 → 0.827 ± 0.010, chain-recomputed with an in-text correction note",
      "P4 v1.0.169: 7 local recomputes closed — confidence-cut profile z=+4.27 → +0.41 confirms the low-confidence-tail attribution; formal A_dip 95% UL committed",
    ],
    links: [
      { label: "P4 synthesis", href: `${PR}/R24conf_P4_SYNTHESIS.md` },
      { label: "P2 synthesis", href: `${PR}/R24conf_P2_SYNTHESIS.md` },
      { label: "P5 synthesis", href: `${PR}/R24conf_P5_SYNTHESIS.md` },
    ],
  },
  {
    id: "R23conf",
    kind: "internal-api",
    dateISO: "2026-06-09",
    title: "R23conf — first full-coverage five-vendor confirmation round: ~200 findings truth-audited, all six papers bumped",
    papers: ["P1A", "P1B", "P2", "P3", "P4", "P5"],
    summary: "First full-coverage confirmation round on the post-provenance-audit versions — Claude in-session + OpenAI/Gemini/Grok/Perplexity via API + GPT-5-Pro meta; every VERIFIED finding closed same-day.",
    keyTakeaways: [
      "P4 v1.0.168: headline real-space null regenerated from a fixed generator — the committed generator had an all-CW selection bug; verdict unchanged at +0.41σ (p=0.31)",
      "P1B v1B.0.52: §VI ALP provenance rewrite — invented benchmark-config story replaced by the committed chain truth (run1/run2/run3, 9,720 samples)",
      "P2 v1.7.46: irreproducible Table III rebuilt from the committed c9g recompute; Φ/ζ convention mapping proven exactly",
      "P3 v3.1.81: abstract novelty rate arithmetic-anchored 7.9% → 9.4%; gold/silver novelty tiers defined",
    ],
    links: [
      { label: "P4 synthesis", href: `${PR}/R23conf_P4_SYNTHESIS.md` },
      { label: "P1B synthesis", href: `${PR}/R23conf_P1B_SYNTHESIS.md` },
      { label: "P1A truth-audit", href: `${PR}/R23conf_P1A_TRUTH_AUDIT.md` },
    ],
  },
];

export function getReviewRoundByReportSlug(slug: string): ReviewRound | undefined {
  return reviewRounds.find((r) => r.reportSlug === slug);
}

/** Newest-first ordering for the feed (stable on date ties, preserving authored order). */
export function sortedReviewRounds(): ReviewRound[] {
  return [...reviewRounds].sort((a, b) => b.dateISO.localeCompare(a.dateISO));
}
