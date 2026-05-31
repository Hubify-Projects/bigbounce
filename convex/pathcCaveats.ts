import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

export const listForPaper = query({
  args: { paperSlug: v.string() },
  handler: async (ctx, args) => {
    return await ctx.db
      .query("pathc_caveats")
      .withIndex("by_paper", (q) => q.eq("paperSlug", args.paperSlug))
      .collect();
  },
});

export const listOpen = query({
  args: { paperSlug: v.optional(v.string()) },
  handler: async (ctx, args) => {
    const all = args.paperSlug
      ? await ctx.db
          .query("pathc_caveats")
          .withIndex("by_paper", (q) => q.eq("paperSlug", args.paperSlug!))
          .collect()
      : await ctx.db.query("pathc_caveats").collect();
    return all.filter((c) => c.status === "open" || c.status === "deferred");
  },
});

export const upsert = mutation({
  args: {
    paperSlug: v.string(),
    label: v.string(),
    description: v.string(),
    status: v.union(v.literal("open"), v.literal("deferred"), v.literal("closed")),
  },
  handler: async (ctx, args) => {
    const existing = await ctx.db
      .query("pathc_caveats")
      .withIndex("by_paper", (q) => q.eq("paperSlug", args.paperSlug))
      .collect();
    const match = existing.find((c) => c.label === args.label);
    if (match) {
      await ctx.db.patch(match._id, args);
      return match._id;
    }
    return await ctx.db.insert("pathc_caveats", args);
  },
});

export const close = mutation({
  args: {
    paperSlug: v.string(),
    label: v.string(),
    closureMethod: v.union(
      v.literal("real-computation"),
      v.literal("artifact-verification"),
      v.literal("truth-audit-falsification"),
      v.literal("text-only-no-real-action")
    ),
    closureArtifact: v.optional(v.string()),
    closureCommit: v.optional(v.string()),
    closureNote: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const existing = await ctx.db
      .query("pathc_caveats")
      .withIndex("by_paper", (q) => q.eq("paperSlug", args.paperSlug))
      .collect();
    const match = existing.find((c) => c.label === args.label);
    if (!match) {
      throw new Error(`pathc_caveats item not found: ${args.paperSlug} (${args.label})`);
    }
    await ctx.db.patch(match._id, {
      status: "closed",
      closureMethod: args.closureMethod,
      closureArtifact: args.closureArtifact,
      closureCommit: args.closureCommit,
      closureNote: args.closureNote,
      closedAt: Date.now(),
    });
  },
});
