import { mutation, query, internalMutation } from "./_generated/server";
import { v } from "convex/values";

/** Sort paper_versions newest-first. Datestamps are parsed as dates (handles
 * both "July 10, 2026" and ISO); lexicographic localeCompare mis-orders
 * human-format dates ("July 10" < "July 9"), which left stale "current"
 * versions on the site (caught 2026-07-10). Unparseable datestamps fall back
 * to localeCompare. Ties break on createdAt desc. */
function sortVersions<T extends { datestamp: string; createdAt: number }>(vs: T[]): T[] {
  return vs.sort((a, b) => {
    const ta = Date.parse(a.datestamp);
    const tb = Date.parse(b.datestamp);
    if (!Number.isNaN(ta) && !Number.isNaN(tb) && ta !== tb) return tb - ta;
    if (Number.isNaN(ta) || Number.isNaN(tb)) {
      const d = b.datestamp.localeCompare(a.datestamp);
      if (d !== 0) return d;
    }
    return (b.createdAt ?? 0) - (a.createdAt ?? 0);
  });
}

export const listForPaper = query({
  args: { paperSlug: v.string() },
  handler: async (ctx, args) => {
    const versions = await ctx.db
      .query("paper_versions")
      .withIndex("by_paper", (q) => q.eq("paperSlug", args.paperSlug))
      .collect();
    return sortVersions(versions);
  },
});

export const current = query({
  args: { paperSlug: v.string() },
  handler: async (ctx, args) => {
    const versions = await ctx.db
      .query("paper_versions")
      .withIndex("by_paper", (q) => q.eq("paperSlug", args.paperSlug))
      .collect();
    return sortVersions(versions)[0] ?? null;
  },
});

// Atomic version bump — replaces the 4-5 manual file edits per .tex bump.
// Site re-renders on Convex subscription; no more "I forgot to bump
// version on the site after pdflatex compile" drift.
//
// Gap #5 (closed 2026-06-03): accepts an optional `sitePdfPath`. When
// provided, papers.sitePdfPath is patched in the SAME transaction so the
// detail page version chip + PDF link can never disagree. Callers
// (/bigbounce-bump, tools/p*_convex_bump_*.mjs) SHOULD always pass the
// new path; legacy callers that omit it still work (non-breaking).
export const bump = mutation({
  args: {
    paperSlug: v.string(),
    version: v.string(),
    datestamp: v.string(),
    texCommit: v.string(),
    pdfMd5: v.string(),
    pdfPages: v.number(),
    pdfSizeBytes: v.number(),
    changelog: v.string(),
    arxivTarballPath: v.optional(v.string()),
    arxivTarballSizeBytes: v.optional(v.number()),
    sitePdfPath: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const { sitePdfPath, ...versionFields } = args;
    const versionId = await ctx.db.insert("paper_versions", {
      ...versionFields,
      createdAt: Date.now(),
    });
    if (sitePdfPath) {
      const paper = await ctx.db
        .query("papers")
        .withIndex("by_slug", (q) => q.eq("slug", args.paperSlug))
        .unique();
      if (paper && paper.sitePdfPath !== sitePdfPath) {
        await ctx.db.patch(paper._id, { sitePdfPath });
      }
    }
    return versionId;
  },
});

/**
 * One-time repair: rewrite 2026-06-11 / 2026-06-12 datestamps to "2026-06-10"
 * (the correct America/Los_Angeles date at the time those rows were written).
 * Safe to run multiple times — rows already at "2026-06-10" are untouched.
 * Call via: npx convex run paperVersions:patchUtcLeakedDates
 */
export const patchUtcLeakedDates = mutation({
  args: {},
  handler: async (ctx) => {
    const badDates = ["2026-06-11", "2026-06-12"];
    const correctDate = "2026-06-10";
    let patched = 0;
    for (const date of badDates) {
      // Scan all papers for rows with this bad datestamp
      const allVersions = await ctx.db.query("paper_versions").collect();
      for (const row of allVersions) {
        if (row.datestamp === date) {
          await ctx.db.patch(row._id, { datestamp: correctDate });
          patched++;
        }
      }
    }
    return { patched, correctedTo: correctDate };
  },
});
