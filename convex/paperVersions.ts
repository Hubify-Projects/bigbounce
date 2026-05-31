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
  },
  handler: async (ctx, args) => {
    return await ctx.db.insert("paper_versions", {
      ...args,
      createdAt: Date.now(),
    });
  },
});
