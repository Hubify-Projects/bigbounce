import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

export const list = query({
  handler: async (ctx) => {
    return await ctx.db.query("pods").collect();
  },
});

export const listRunning = query({
  handler: async (ctx) => {
    return await ctx.db
      .query("pods")
      .withIndex("by_status", (q) => q.eq("status", "running"))
      .collect();
  },
});

export const upsert = mutation({
  args: {
    podId: v.string(),
    name: v.string(),
    status: v.union(v.literal("running"), v.literal("exited"), v.literal("terminated")),
    gpu: v.string(),
    volumeGb: v.number(),
    containerGb: v.number(),
    hourlyCostUsd: v.number(),
    startedAt: v.number(),
    stoppedAt: v.optional(v.number()),
    totalCostUsd: v.number(),
    purpose: v.string(),
    artifactsBackedUp: v.boolean(),
    backupLocations: v.array(v.string()),
  },
  handler: async (ctx, args) => {
    const existing = await ctx.db
      .query("pods")
      .withIndex("by_pod_id", (q) => q.eq("podId", args.podId))
      .unique();
    const payload = { ...args, lastSyncedAt: Date.now() };
    if (existing) {
      await ctx.db.patch(existing._id, payload);
      return existing._id;
    }
    return await ctx.db.insert("pods", payload);
  },
});
