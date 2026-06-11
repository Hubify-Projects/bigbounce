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
    jobs: v.optional(
      v.array(
        v.object({
          name: v.string(),
          paper: v.string(),
          tmuxSession: v.string(),
          status: v.union(
            v.literal("queued"),
            v.literal("running"),
            v.literal("done"),
            v.literal("failed")
          ),
          etaNote: v.string(),
          outputPath: v.optional(v.string()),
        })
      )
    ),
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

/**
 * One-time repair: rewrite the bigbounce-c123-namaster pod startedAt from
 * 2026-06-12T18:46:40 UTC (1781290000000 ms — a 44h double-timezone skew)
 * to the correct 2026-06-10T18:46 PT epoch (= 2026-06-11T01:46:40 UTC,
 * 1781142400000 ms).
 * Safe to run multiple times — row already at correct value is untouched.
 * Call via: npx convex run pods:patchNamasterTimestamp
 */
export const patchNamasterTimestamp = mutation({
  args: {},
  handler: async (ctx) => {
    const BAD_EPOCH_MS = 1781290000000;
    const CORRECT_EPOCH_MS = 1781142400000; // 2026-06-10 18:46 PDT = 2026-06-11 01:46:40 UTC
    const pod = await ctx.db
      .query("pods")
      .withIndex("by_pod_id", (q) => q.eq("podId", "5i2td3deu3hojr"))
      .unique();
    if (!pod) return { status: "not-found" };
    if (pod.startedAt === CORRECT_EPOCH_MS) return { status: "already-correct" };
    if (pod.startedAt !== BAD_EPOCH_MS) return { status: "unexpected-value", startedAt: pod.startedAt };
    await ctx.db.patch(pod._id, { startedAt: CORRECT_EPOCH_MS });
    return { status: "patched", from: BAD_EPOCH_MS, to: CORRECT_EPOCH_MS };
  },
});
