import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

export const byPipeline = query({
  args: { pipelineId: v.string() },
  handler: async (ctx, args) => {
    return await ctx.db
      .query("pipelineState")
      .withIndex("by_pipeline", (q) => q.eq("pipelineId", args.pipelineId))
      .first();
  },
});

export const all = query({
  args: {},
  handler: async (ctx) => {
    return await ctx.db.query("pipelineState").collect();
  },
});

export const upsert = mutation({
  args: {
    pipelineId: v.string(),
    name: v.string(),
    status: v.string(),
    gatesPassed: v.number(),
    totalGates: v.number(),
    summary: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const existing = await ctx.db
      .query("pipelineState")
      .withIndex("by_pipeline", (q) => q.eq("pipelineId", args.pipelineId))
      .first();

    const data = {
      pipelineId: args.pipelineId,
      name: args.name,
      status: args.status,
      gatesPassed: args.gatesPassed,
      totalGates: args.totalGates,
      lastUpdated: Date.now(),
      summary: args.summary ?? "",
    };

    if (existing) {
      await ctx.db.patch(existing._id, data);
      return existing._id;
    } else {
      return await ctx.db.insert("pipelineState", data);
    }
  },
});
