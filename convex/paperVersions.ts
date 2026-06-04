import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

export const listForPaper = query({
  args: { paperSlug: v.string() },
  handler: async (ctx, args) => {
    const versions = await ctx.db
      .query("paper_versions")
      .withIndex("by_paper", (q) => q.eq("paperSlug", args.paperSlug))
      .collect();
    versions.sort((a, b) => b.datestamp.localeCompare(a.datestamp));
    return versions;
  },
});

export const current = query({
  args: { paperSlug: v.string() },
  handler: async (ctx, args) => {
    const versions = await ctx.db
      .query("paper_versions")
      .withIndex("by_paper", (q) => q.eq("paperSlug", args.paperSlug))
      .collect();
    versions.sort((a, b) => b.datestamp.localeCompare(a.datestamp));
    return versions[0] ?? null;
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
