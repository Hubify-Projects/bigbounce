import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

export const byPipeline = query({
  args: { pipelineId: v.string() },
  handler: async (ctx, args) => {
    return await ctx.db
      .query("models")
      .withIndex("by_pipeline", (q) => q.eq("pipelineId", args.pipelineId))
      .collect();
  },
});

export const add = mutation({
  args: {
    pipelineId: v.string(),
    modelName: v.string(),
    version: v.string(),
    huggingfaceUrl: v.optional(v.string()),
    trainingSamples: v.optional(v.number()),
    metrics: v.optional(v.any()),
  },
  handler: async (ctx, args) => {
    return await ctx.db.insert("models", {
      pipelineId: args.pipelineId,
      modelName: args.modelName,
      version: args.version,
      huggingfaceUrl: args.huggingfaceUrl ?? "",
      trainingSamples: args.trainingSamples ?? 0,
      metrics: args.metrics ?? {},
      createdAt: Date.now(),
    });
  },
});
