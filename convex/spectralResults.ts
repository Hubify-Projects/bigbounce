import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

export const store = mutation({
  args: {
    pipelineId: v.string(),
    targetId: v.string(),
    ra: v.number(),
    dec: v.number(),
    anomalyScore: v.number(),
    anomalyType: v.string(),
    worstRegion: v.string(),
    regionB: v.number(),
    regionR: v.number(),
    regionZ: v.number(),
    simbadStatus: v.string(),
    batchId: v.string(),
    processedAt: v.number(),
  },
  handler: async (ctx, args) => {
    return await ctx.db.insert("spectralResults", args);
  },
});

export const storeBatch = mutation({
  args: {
    results: v.array(v.object({
      pipelineId: v.string(),
      targetId: v.string(),
      ra: v.number(),
      dec: v.number(),
      anomalyScore: v.number(),
      anomalyType: v.string(),
      worstRegion: v.string(),
      regionB: v.number(),
      regionR: v.number(),
      regionZ: v.number(),
      simbadStatus: v.string(),
      batchId: v.string(),
      processedAt: v.number(),
    })),
  },
  handler: async (ctx, args) => {
    for (const result of args.results) {
      await ctx.db.insert("spectralResults", result);
    }
    return args.results.length;
  },
});

export const getTopAnomalies = query({
  args: {
    pipelineId: v.string(),
    limit: v.optional(v.number()),
  },
  handler: async (ctx, args) => {
    const results = await ctx.db
      .query("spectralResults")
      .withIndex("by_score", (q) => q.eq("pipelineId", args.pipelineId))
      .order("desc")
      .take(args.limit ?? 100);
    return results;
  },
});

export const getByBatch = query({
  args: { batchId: v.string() },
  handler: async (ctx, args) => {
    return await ctx.db
      .query("spectralResults")
      .withIndex("by_batch", (q) => q.eq("batchId", args.batchId))
      .collect();
  },
});

export const getStats = query({
  args: { pipelineId: v.string() },
  handler: async (ctx, args) => {
    const all = await ctx.db
      .query("spectralResults")
      .withIndex("by_pipeline", (q) => q.eq("pipelineId", args.pipelineId))
      .collect();
    return {
      total: all.length,
      novel: all.filter((r) => r.simbadStatus === "NOT_FOUND").length,
      known: all.filter((r) => r.simbadStatus === "KNOWN").length,
      unchecked: all.filter((r) => r.simbadStatus === "UNCHECKED").length,
    };
  },
});
