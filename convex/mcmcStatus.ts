import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

export const latest = query({
  args: {},
  handler: async (ctx) => {
    const datasets = ["planck_only", "planck_bao", "planck_bao_sn", "full_tension"];
    const results = [];
    for (const dataset of datasets) {
      const row = await ctx.db
        .query("mcmcStatus")
        .withIndex("by_dataset", (q) => q.eq("dataset", dataset))
        .order("desc")
        .first();
      if (row) results.push(row);
    }
    return results;
  },
});

export const byDataset = query({
  args: { dataset: v.string(), limit: v.optional(v.number()) },
  handler: async (ctx, args) => {
    return await ctx.db
      .query("mcmcStatus")
      .withIndex("by_dataset", (q) => q.eq("dataset", args.dataset))
      .order("desc")
      .take(args.limit ?? 20);
  },
});

export const record = mutation({
  args: {
    dataset: v.string(),
    rhat: v.any(),
    ess: v.any(),
    drift: v.any(),
    parameterMeans: v.any(),
    converged: v.boolean(),
    timestamp: v.optional(v.number()),
  },
  handler: async (ctx, args) => {
    return await ctx.db.insert("mcmcStatus", {
      dataset: args.dataset,
      rhat: args.rhat,
      ess: args.ess,
      drift: args.drift,
      parameterMeans: args.parameterMeans,
      converged: args.converged,
      timestamp: args.timestamp ?? Date.now(),
    });
  },
});
