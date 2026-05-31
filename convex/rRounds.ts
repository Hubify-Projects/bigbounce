import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

export const listForPaper = query({
  args: { paperSlug: v.string() },
  handler: async (ctx, args) => {
    const rounds = await ctx.db
      .query("r_rounds")
      .withIndex("by_paper", (q) => q.eq("paperSlug", args.paperSlug))
      .collect();
    rounds.sort((a, b) => b.dispatchedAt - a.dispatchedAt);
    return rounds;
  },
});

export const getByLabel = query({
  args: { roundLabel: v.string() },
  handler: async (ctx, args) => {
    return await ctx.db
      .query("r_rounds")
      .withIndex("by_label", (q) => q.eq("roundLabel", args.roundLabel))
      .unique();
  },
});

// Create a new R-round row. Called by tools/cross_vendor_review_direct.py
// before dispatch (returns the round ID; findings get written against it).
export const create = mutation({
  args: {
    paperSlug: v.string(),
    paperVersionReviewed: v.string(),
    roundLabel: v.string(),
    source: v.union(
      v.literal("openrouter"),
      v.literal("direct"),
      v.literal("subagent"),
      v.literal("houston-external")
    ),
    vendors: v.array(v.string()),
    promptText: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    return await ctx.db.insert("r_rounds", {
      ...args,
      dispatchedAt: Date.now(),
    });
  },
});

export const markComplete = mutation({
  args: { roundId: v.id("r_rounds") },
  handler: async (ctx, args) => {
    await ctx.db.patch(args.roundId, { completedAt: Date.now() });
  },
});
