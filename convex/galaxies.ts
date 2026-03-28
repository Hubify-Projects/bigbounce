import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

// Batch import — called by import_to_convex.py
export const importBatch = mutation({
  args: {
    batch: v.array(
      v.object({
        dr8_id: v.string(),
        p_cw: v.float64(),
        p_ccw: v.float64(),
        p_ns: v.float64(),
        classification: v.string(),
        confidence: v.float64(),
      })
    ),
  },
  handler: async (ctx, args) => {
    for (const galaxy of args.batch) {
      await ctx.db.insert("galaxies", galaxy);
    }
    return args.batch.length;
  },
});

// Count total galaxies
export const count = query({
  handler: async (ctx) => {
    const result = await ctx.db.query("galaxies").collect();
    return result.length;
  },
});

// Count by classification
export const countByClass = query({
  handler: async (ctx) => {
    const all = await ctx.db.query("galaxies").collect();
    const cw = all.filter((g) => g.classification === "CW").length;
    const ccw = all.filter((g) => g.classification === "CCW").length;
    const ns = all.filter((g) => g.classification === "NOT_SPIRAL").length;
    return { total: all.length, cw, ccw, ns };
  },
});

// Search by dr8_id
export const getByDr8Id = query({
  args: { dr8_id: v.string() },
  handler: async (ctx, args) => {
    return await ctx.db
      .query("galaxies")
      .withIndex("by_dr8_id", (q) => q.eq("dr8_id", args.dr8_id))
      .first();
  },
});

// Paginated list with optional classification filter
export const list = query({
  args: {
    classification: v.optional(v.string()),
    limit: v.optional(v.number()),
    cursor: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const limit = args.limit ?? 50;
    let q = ctx.db.query("galaxies");

    if (args.classification) {
      q = q.withIndex("by_classification", (idx) =>
        idx.eq("classification", args.classification!)
      );
    }

    const results = await q.take(limit);
    return results;
  },
});

// High confidence galaxies
export const highConfidence = query({
  args: { minConfidence: v.float64(), limit: v.optional(v.number()) },
  handler: async (ctx, args) => {
    const limit = args.limit ?? 100;
    const results = await ctx.db
      .query("galaxies")
      .withIndex("by_confidence")
      .order("desc")
      .take(limit);
    return results.filter((g) => g.confidence >= args.minConfidence);
  },
});
