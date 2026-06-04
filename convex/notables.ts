import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

// ──────────────────────────────────────────────────────────────────────
// papers_notables — per-paper "novelty highlights" bullets surfaced on the
// detail page (Gap #1, closed 2026-06-03).
//
// Distinct from focusAreas (which targets external reviewers); these are
// reader-facing 2-4 bullets like "First systematic no-go classification
// of the ECH Lagrangian space for matter-bounce inflation".
// ──────────────────────────────────────────────────────────────────────

export const list = query({
  args: { paperSlug: v.string() },
  handler: async (ctx, args) => {
    const rows = await ctx.db
      .query("papers_notables")
      .withIndex("by_paper", (q) => q.eq("paperSlug", args.paperSlug))
      .collect();
    rows.sort((a, b) => a.ordinal - b.ordinal);
    return rows;
  },
});

// Returns notables for every paper, keyed by paperSlug. Single round-trip
// for the cross-paper list page or homepage dashboards.
export const listAll = query({
  handler: async (ctx) => {
    const rows = await ctx.db.query("papers_notables").collect();
    const grouped: Record<string, typeof rows> = {};
    for (const row of rows) {
      if (!grouped[row.paperSlug]) grouped[row.paperSlug] = [];
      grouped[row.paperSlug].push(row);
    }
    for (const slug of Object.keys(grouped)) {
      grouped[slug].sort((a, b) => a.ordinal - b.ordinal);
    }
    return grouped;
  },
});

export const add = mutation({
  args: {
    paperSlug: v.string(),
    ordinal: v.number(),
    bullet: v.string(),
    citationKey: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    return await ctx.db.insert("papers_notables", {
      ...args,
      createdAt: Date.now(),
    });
  },
});

// Idempotent upsert by (paperSlug, ordinal). Safe for seed-script re-runs.
export const upsertByOrdinal = mutation({
  args: {
    paperSlug: v.string(),
    ordinal: v.number(),
    bullet: v.string(),
    citationKey: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const existing = await ctx.db
      .query("papers_notables")
      .withIndex("by_paper", (q) =>
        q.eq("paperSlug", args.paperSlug).eq("ordinal", args.ordinal)
      )
      .unique();
    if (existing) {
      await ctx.db.patch(existing._id, {
        bullet: args.bullet,
        citationKey: args.citationKey,
      });
      return existing._id;
    }
    return await ctx.db.insert("papers_notables", {
      ...args,
      createdAt: Date.now(),
    });
  },
});

export const remove = mutation({
  args: { id: v.id("papers_notables") },
  handler: async (ctx, args) => {
    await ctx.db.delete(args.id);
  },
});
