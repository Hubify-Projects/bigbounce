import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const rRound = await client.mutation(api.rRounds.create, {
  paperSlug: "paper-4p",
  paperVersionReviewed: "v4P.0.8",
  roundLabel: "ROUND_2026-09-19-P4P-v4P.0.8-EXACTPDF-e8f1969e-REVERIFY",
  source: "subagent",
  vendors: ["grok-4.3", "gemini-3.1-pro-preview", "claude-opus"],
  promptText:
    "Directive-R2-permitted second consecutive verification round: independently re-review lane L4's own v4P.0.7->v4P.0.8 closures on the exact v4P.0.8 PDF, verdict-blind, not shown the prior closure list or DISPOSITIONS/P4P.md.",
});
console.log("rRounds.create:", rRound);

await client.mutation(api.rRounds.markComplete, { roundId: rRound });
console.log("rRounds.markComplete: done");

const bump = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-4p",
  version: "v4P.0.9",
  datestamp: "2026-09-19",
  texCommit: "pending",
  pdfMd5: "e31da2ee9cc57fbf0344b8d5c3b9a330",
  pdfPages: 14,
  pdfSizeBytes: 1119162,
  sitePdfPath: "/papers/paper4prime_chirality_test_v4P.0.9.pdf",
  arxivTarballPath:
    "project-context/SSOT/arxiv_tarballs/paper4prime_chirality_test_arxiv_v4P.0.9.tar.gz",
  changelog:
    "Exact-v4P.0.8 re-verification board (campaign lane L4b, bb-L4b-p4p-reverify) -- the one directive-R2-permitted consecutive verification round following lane L4's 2026-09-18 confirmation board, independently checking L4's own v4P.0.7->v4P.0.8 closures rather than new content. Grok API grok-4.3 (REJECT, mostly re-flags of already-disclosed content), Gemini API gemini-3.1-pro-preview (accept with minor corrections), Claude opus sub-agent (major-revisions, verdict-blind cold read, explicitly not shown the prior closure list or DISPOSITIONS/P4P.md before writing its report). Found and fixed 6 genuinely-new-real MAJOR, each independently re-derived by the orchestrator from underlying committed artifacts before closure: (1) pixel-injection baseline compared against the wrong monopole sample (catalog-wide vs. HC-selected) and the wrong amplitude convention; (2) 'near-antipodal axis' claim quantitatively false -- recomputed max pairwise separation among four QC-sweep axes is 119.9 degrees, not ~180, and the closest pair (19.3 degrees, the primary_hc-relaxed excess axis vs. the primary channel's own axis) was omitted; (3)+(4) two headline-qualifying Sec. A.1 disclosures (pixel-transfer tension, primary channel's own leg-instability) had zero forward reference from the Abstract/Sec.3/Sec.5/Sec.6/Sec.7, fixed with four targeted pointer sentences (Abstract deliberately untouched, already at the 250-word ApJS cap); (5) 'density-tercile split' is actually a 20/60/20 quintile split per the committed script's own docstring and the paper's own Table 8 counts; (6) a 0.79 correlation figure misattributed to the wrong channel pair, contradicted by the paper's own next sentence. 4 MINOR also closed with real source-verified edits. 6 minors + 6 nits explicitly deferred with documented reason. Directive-G hygiene: paperVersion v4P.0.8->v4P.0.9, paperTimestamp Sept18->Sept19 2026, 4-pass compile 0 undef refs, 14pp unchanged, four-way byte-identical mirror, arXiv tarball rebuilt+standalone-verified. Directive R2: no further consecutive review round on this content without an intervening science/scope decision. Primary null result unchanged.",
});
console.log("paperVersions.bump:", bump);

const reviewRows = [
  {
    reviewerLabel: "Grok API (grok-4.3) -- exact-v4P.0.8 re-verify",
    recommendation: "reject",
    blockerCount: 0,
    majorCount: 4,
    minorCount: 3,
    notes:
      "Mostly re-flags of already-disclosed content (g-bridge, Poplawski qualitative-only, post-hoc DESIVAST test, kappa=0.40 disclosure, 'largest test' framing) -- all dispositioned RE-FLAG-OF-DISCLOSED or FALSIFIED against existing precedent or the manuscript's own text.",
  },
  {
    reviewerLabel: "Gemini API (gemini-3.1-pro-preview) -- exact-v4P.0.8 re-verify",
    recommendation: "minor-revisions",
    blockerCount: 0,
    majorCount: 0,
    minorCount: 1,
    notes:
      "ACCEPT WITH MINOR CORRECTIONS. Sole finding (three URLs with spaces) is a PDF-render column-wrap artifact -- no space in the LaTeX source -- FALSIFIED, same pattern as prior-round Gemini N3.",
  },
  {
    reviewerLabel: "Claude opus INT sub-agent -- exact-v4P.0.8 re-verify (verdict-blind)",
    recommendation: "major-revisions",
    blockerCount: 0,
    majorCount: 6,
    minorCount: 11,
    notes:
      "Cold read, not shown the prior closure list or DISPOSITIONS/P4P.md. 6 MAJOR + 4 of 11 MINOR independently re-derived by the orchestrator and closed in v4P.0.9 (see paperVersions changelog); 7 minors + 7 nits deferred with documented reason.",
  },
];

for (const row of reviewRows) {
  const res = await client.mutation(api.externalReviews.upsertByLabelDate, {
    paperSlug: "paper-4p",
    source: "internal-stage3",
    reviewerLabel: row.reviewerLabel,
    receivedAt: "2026-09-19",
    blockerCount: row.blockerCount,
    majorCount: row.majorCount,
    minorCount: row.minorCount,
    recommendation: row.recommendation,
    rRoundId: rRound,
    paperVersionReviewed: "v4P.0.8",
    notes: row.notes,
  });
  console.log("externalReviews.upsertByLabelDate:", row.reviewerLabel, res);
}

const activity = await client.mutation(api.activityFeed.add, {
  type: "r-round",
  date: "2026-09-19",
  title: "P4′ exact-v4P.0.8 re-verification board closed 6 further genuinely-new-real findings -> v4P.0.9",
  body:
    "Directive-R2-permitted second consecutive verification round (lane L4b) independently re-checked lane L4's own v4P.0.7->v4P.0.8 closures. Grok API REJECT (re-flags of already-disclosed content), Gemini API accept-with-minor-corrections, Claude opus sub-agent major-revisions (verdict-blind, not shown the prior closure list). Found and fixed 6 genuinely-new-real MAJOR + 4 MINOR, every one independently re-derived by the orchestrator from underlying committed artifacts before closure: a mislabeled monopole comparator, a quantitatively-false 'near-antipodal axis' claim, two headline-qualifying disclosures with zero forward reference from the paper's own headline sections, a mislabeled quintile split, and a misattributed correlation figure. Primary null result unchanged. Directive R2: no further consecutive round on this content without a scope decision.",
  tags: [
    { label: "paper-4p", kind: "paper" },
    { label: "v4P.0.9", kind: "version" },
    { label: "campaign-2026-09-18", kind: "campaign" },
  ],
});
console.log("activityFeed.add:", activity);
