import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

// ──────────────────────────────────────────────────────────────────────
// paper_figures — per-paper figure rows seeded from each paper's
// current .tex \includegraphics + \caption block.
//
// Mirrors the structure of convex/notables.ts: list/listAll for the
// /figures page, upsertByOrdinal for idempotent seed-script re-runs,
// removeByPaper to prune stale rows before a fresh seed.
// ──────────────────────────────────────────────────────────────────────

export const list = query({
  args: { paperSlug: v.string() },
  handler: async (ctx, args) => {
    const rows = await ctx.db
      .query("paper_figures")
      .withIndex("by_paper", (q) => q.eq("paperSlug", args.paperSlug))
      .collect();
    rows.sort((a, b) => a.ordinal - b.ordinal);
    return rows;
  },
});

// Returns figures for every paper, keyed by paperSlug. Single round-trip
// for the /figures gallery page.
export const listAll = query({
  handler: async (ctx) => {
    const rows = await ctx.db.query("paper_figures").collect();
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

// Idempotent upsert by (paperSlug, ordinal). Safe for seed-script re-runs.
export const upsertByOrdinal = mutation({
  args: {
    paperSlug: v.string(),
    ordinal: v.number(),
    src: v.string(),
    alt: v.string(),
    title: v.string(),
    desc: v.string(),
    paperVersion: v.string(),
    citationLabel: v.optional(v.string()),
    status: v.optional(
      v.union(
        v.literal("in-paper"),
        v.literal("candidate"),
        v.literal("retracted"),
      ),
    ),
  },
  handler: async (ctx, args) => {
    const existing = await ctx.db
      .query("paper_figures")
      .withIndex("by_paper_ordinal", (q) =>
        q.eq("paperSlug", args.paperSlug).eq("ordinal", args.ordinal)
      )
      .unique();
    if (existing) {
      await ctx.db.patch(existing._id, {
        src: args.src,
        alt: args.alt,
        title: args.title,
        desc: args.desc,
        paperVersion: args.paperVersion,
        citationLabel: args.citationLabel,
        status: args.status ?? "in-paper",
      });
      return existing._id;
    }
    return await ctx.db.insert("paper_figures", {
      ...args,
      status: args.status ?? "in-paper",
      addedAt: Date.now(),
    });
  },
});

// Delete every figure for a paper. Used by the seed script to prune
// stale rows (figures removed from the current .tex in a revision round)
// before upserting the fresh set.
//
// 2026-06-09: accepts optional status filter so the seed script can
// wipe only "in-paper" rows without touching candidates (which are
// seeded by tools/seed_paper_figure_candidates.mjs from a manual
// manifest, not from the .tex).
export const removeByPaper = mutation({
  args: {
    paperSlug: v.string(),
    status: v.optional(
      v.union(
        v.literal("in-paper"),
        v.literal("candidate"),
        v.literal("retracted"),
      ),
    ),
  },
  handler: async (ctx, args) => {
    const rows = await ctx.db
      .query("paper_figures")
      .withIndex("by_paper", (q) => q.eq("paperSlug", args.paperSlug))
      .collect();
    const targets = args.status
      ? rows.filter((r) => (r.status ?? "in-paper") === args.status)
      : rows;
    for (const row of targets) {
      await ctx.db.delete(row._id);
    }
    return targets.length;
  },
});

export const remove = mutation({
  args: { id: v.id("paper_figures") },
  handler: async (ctx, args) => {
    await ctx.db.delete(args.id);
  },
});
