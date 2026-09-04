import { query } from "./_generated/server";

/**
 * publicationStatus — the directive-P publication surface.
 *
 * WHY THIS EXISTS (2026-07-24). It replaces `readinessMetrics:computeEta`,
 * which computed an "hours to submission-ready" clock against directive K's
 * TWO-CLEAN-WAVES bar. That bar was demoted by directive L ("a CHECKPOINT,
 * not the finish line") and superseded again by directives M / M-AMENDED / P,
 * so the homepage was advertising a countdown to a target the program had
 * abandoned. Worse, it read `readinessMetrics` rows that stopped being written
 * on 2026-07-16 — so it rendered eight-day-old clean-wave streaks (P1A 18,
 * P2 20) as current, silently, while the 2026-07-22 confirmation wave had
 * surfaced genuinely-new-real findings on all six papers. Silent staleness is
 * the failure this module is designed to make impossible.
 *
 * WHAT IT COMPUTES. Nothing is hand-set. Every field is derived from live
 * Convex rows at query time:
 *   - papers / paper_versions  → current version + when it was stamped
 *   - findings / pathc_caveats → open agent-owned work
 *   - papers.houstonSignOff    → directive-P's final 5%
 *   - papers_externalReviews   → the newest automated review board, and
 *                                (via paperVersionReviewed) whether that board
 *                                actually read the CURRENT PDF
 *
 * DRIFT-PROOFING (the load-bearing property). The query returns raw epoch-ms
 * evidence timestamps, never a pre-rendered "N days ago" string. The client
 * computes the age against the viewer's own clock, so a build that froze eight
 * days ago cannot render as current: it renders as eight days stale. If the
 * loop stops writing rows, `evidenceAgeDays` grows on its own and `isStale`
 * flips — no agent has to remember to update anything for the surface to start
 * telling the truth.
 *
 * READINESS IS NOT COMPUTED HERE. The headline % stays owned by
 * `papers:listAllPaperStates` (ceiling = readinessCap, penalties from open
 * findings, 100 only on Houston's sign-off). Duplicating that formula is how
 * home-vs-/paper drift happened before; this module deliberately returns
 * gates, ownership, and freshness only.
 */

// Canonical six submission targets. Retired ids (P1U) and raw store ids that
// linger in older rows must never reach the surface.
// 2026-09-02 portfolio restructure (directive R3): A3M folds the A3
// multi-channel skeleton + P2' exact-amplitude theory into Track A's flagship
// submission candidate, and 4P folds P4+P5 into the Track C1 ApJS candidate.
// Both are live standalone submission targets and must be tracked here or
// their version bumps/review boards never register as evidence, and this
// surface renders permanently stale regardless of how current the loop is.
const CANONICAL: Array<{ slug: string; paperId: string }> = [
  { slug: "paper-1a", paperId: "P1A" },
  { slug: "paper-1b", paperId: "P1B" },
  { slug: "paper-2", paperId: "P2" },
  { slug: "paper-a3m", paperId: "A3M" },
  { slug: "paper-3", paperId: "P3" },
  { slug: "paper-4p", paperId: "4P" },
];

// Beyond this the surface renders as explicitly stale rather than current.
// The review loop's own cadence is sub-daily, so three days without a single
// version bump OR review row on ANY paper means the pipeline stopped.
const STALE_AFTER_DAYS = 3;

const DAY_MS = 86_400_000;

/**
 * paper_versions.datestamp is a human string ("July 22, 2026"); a few older
 * rows are already ISO. Parse defensively and fall back to createdAt, which is
 * always a real epoch-ms write time.
 */
function versionDateISO(datestamp: string | undefined, createdAt: number): string {
  if (datestamp) {
    const iso = /^\d{4}-\d{2}-\d{2}/.exec(datestamp);
    if (iso) return iso[0];
    const t = Date.parse(datestamp);
    if (!Number.isNaN(t)) return new Date(t).toISOString().slice(0, 10);
  }
  return new Date(createdAt).toISOString().slice(0, 10);
}

/** Midday-UTC epoch ms for a YYYY-MM-DD date, so TZ never shifts the day. */
function msFromISO(iso: string): number {
  const t = Date.parse(`${iso}T12:00:00Z`);
  return Number.isNaN(t) ? 0 : t;
}

function receivedAtISO(receivedAt: string): string {
  const iso = /^\d{4}-\d{2}-\d{2}/.exec(receivedAt);
  if (iso) return iso[0];
  const t = Date.parse(receivedAt);
  return Number.isNaN(t) ? "" : new Date(t).toISOString().slice(0, 10);
}

export const get = query({
  args: {},
  handler: async (ctx) => {
    const now = Date.now();
    const allPapers = await ctx.db.query("papers").collect();
    const bySlug = new Map(allPapers.map((p) => [p.slug, p]));

    const perPaper = [];
    let newestEvidenceMs = 0;

    for (const { slug, paperId } of CANONICAL) {
      const paper = bySlug.get(slug);
      if (!paper) continue;

      const versions = await ctx.db
        .query("paper_versions")
        .withIndex("by_paper", (q) => q.eq("paperSlug", slug))
        .collect();
      versions.sort((a, b) => b.createdAt - a.createdAt);
      const current = versions[0] ?? null;

      const findings = await ctx.db
        .query("findings")
        .withIndex("by_paper", (q) => q.eq("paperSlug", slug))
        .collect();
      const open = findings.filter(
        (f) => f.closureStatus === "open" || f.closureStatus === "in-progress",
      );
      const openBlockers = open.filter((f) => f.classification === "BLOCKER").length;
      const openMajors = open.filter((f) => f.classification === "MAJOR").length;
      const openMinors = open.filter((f) => f.classification === "MINOR").length;

      const caveats = await ctx.db
        .query("pathc_caveats")
        .withIndex("by_paper", (q) => q.eq("paperSlug", slug))
        .collect();
      const openCaveats = caveats.filter(
        (c) => c.status === "open" || c.status === "deferred",
      ).length;

      // Newest automated review board recorded for this paper. Rows are
      // written one-per-reviewer-leg, so the newest board is the set of rows
      // sharing the newest receivedAt.
      const reviews = await ctx.db
        .query("papers_externalReviews")
        .withIndex("by_paper", (q) => q.eq("paperSlug", slug))
        .collect();
      let boardDateISO = "";
      let boardWrittenMs = 0;
      for (const r of reviews) {
        const iso = receivedAtISO(r.receivedAt);
        if (iso && iso > boardDateISO) boardDateISO = iso;
      }
      const boardRows = reviews.filter(
        (r) => boardDateISO !== "" && receivedAtISO(r.receivedAt) === boardDateISO,
      );
      for (const r of boardRows) {
        boardWrittenMs = Math.max(boardWrittenMs, r._creationTime);
      }
      // Only rows that record WHICH version they read can prove coverage.
      // Historical rows predate the field; absent ⇒ coverage unknown ⇒ not
      // covered. Fail-closed, so the surface can never overstate its evidence.
      const boardVersions = boardRows
        .map((r) => r.paperVersionReviewed)
        .filter((s): s is string => typeof s === "string" && s.length > 0);
      const currentVersionString = current?.version ?? null;
      const boardCoversCurrentVersion =
        currentVersionString !== null && boardVersions.includes(currentVersionString);

      const versionCreatedAtMs = current?.createdAt ?? 0;
      // Freshness is measured against the SEMANTIC dates of the evidence (when
      // the version was stamped, when the board actually reviewed), never
      // against row write-times. Write-times would let a late backfill of old
      // evidence render as "just now" — the same class of lie this module
      // exists to prevent.
      const versionEvidenceMs = current
        ? msFromISO(versionDateISO(current.datestamp, current.createdAt))
        : 0;
      const boardEvidenceMs = boardDateISO ? msFromISO(boardDateISO) : 0;
      const evidenceMs = Math.max(versionEvidenceMs, boardEvidenceMs);
      newestEvidenceMs = Math.max(newestEvidenceMs, evidenceMs);

      // Who owns the next move. Directive P: the four agent gates are
      // science / evidence / convergence / packaging; the last 5% is Houston.
      const agentItems = openBlockers + openMajors + openMinors + openCaveats;
      let owner: "houston" | "agent" | "done";
      let remaining: string;
      if (paper.houstonSignOff) {
        owner = "done";
        remaining = "Signed off — moves to the Publishing phase.";
      } else if (agentItems > 0) {
        owner = "agent";
        const bits: string[] = [];
        if (openBlockers) bits.push(`${openBlockers} blocker`);
        if (openMajors) bits.push(`${openMajors} major`);
        if (openMinors) bits.push(`${openMinors} minor`);
        if (openCaveats) bits.push(`${openCaveats} caveat`);
        remaining = `${bits.join(" · ")} open — agent-owned closure work.`;
      } else if (!boardCoversCurrentVersion) {
        owner = "agent";
        remaining = currentVersionString
          ? `${currentVersionString} has not been read by an automated review board yet — one confirm read, no new science.`
          : "No version recorded — confirm read pending.";
      } else {
        owner = "houston";
        remaining =
          "All four agent gates complete and confirmed on this exact PDF. Waiting on Houston's final personal review — the last 5%.";
      }

      perPaper.push({
        paperId,
        paperSlug: slug,
        shortTitle: paper.shortTitle,
        sitePdfPath: paper.sitePdfPath ?? null,
        currentVersion: currentVersionString,
        versionDateISO: current ? versionDateISO(current.datestamp, current.createdAt) : null,
        versionCreatedAtMs,
        openBlockers,
        openMajors,
        openMinors,
        openCaveats,
        houstonSignOff: paper.houstonSignOff ?? null,
        boardDateISO: boardDateISO || null,
        boardWrittenMs,
        boardVersions,
        boardCoversCurrentVersion,
        evidenceMs,
        owner,
        remaining,
      });
    }

    const papersSignedOff = perPaper.filter((p) => p.owner === "done").length;
    const papersAwaitingHouston = perPaper.filter((p) => p.owner === "houston").length;
    const papersAwaitingAgent = perPaper.filter((p) => p.owner === "agent").length;

    const evidenceAgeDays =
      newestEvidenceMs > 0 ? (now - newestEvidenceMs) / DAY_MS : Number.POSITIVE_INFINITY;

    return {
      // Raw timestamps, deliberately NOT pre-formatted: the client recomputes
      // age against its own clock so a frozen build reads as stale, not current.
      generatedAtMs: now,
      newestEvidenceMs,
      staleAfterDays: STALE_AFTER_DAYS,
      // Server-side view of staleness. The client recomputes and may flip this
      // to true; it can never flip it to false.
      isStaleAtQueryTime: !(evidenceAgeDays <= STALE_AFTER_DAYS),
      papersTotal: perPaper.length,
      papersSignedOff,
      papersAwaitingHouston,
      papersAwaitingAgent,
      perPaper,
      composition:
        "Directive P (2026-07-23): publication readiness = science closure (25) + " +
        "evidence & reproducibility (25) + automated review convergence (25) + " +
        "packaging & PDF hygiene (20) + Houston's final personal review (5). " +
        "arXiv endorsement, venue selection, submission clicks and journal/human " +
        "peer review are the separate Publishing phase and never subtract from readiness.",
    };
  },
});
