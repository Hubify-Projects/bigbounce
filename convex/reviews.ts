import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

export const byPipeline = query({
  args: { pipelineId: v.string() },
  handler: async (ctx, args) => {
    return await ctx.db
      .query("reviews")
      .withIndex("by_pipeline", (q) => q.eq("pipelineId", args.pipelineId))
      .collect();
  },
});

export const byObject = query({
  args: { pipelineId: v.string(), objectId: v.string() },
  handler: async (ctx, args) => {
    return await ctx.db
      .query("reviews")
      .withIndex("by_pipeline_object", (q) =>
        q.eq("pipelineId", args.pipelineId).eq("objectId", args.objectId)
      )
      .first();
  },
});

export const save = mutation({
  args: {
    pipelineId: v.string(),
    objectId: v.string(),
    label: v.string(),
    aiLabel: v.optional(v.string()),
    aiReason: v.optional(v.string()),
    humanNotes: v.optional(v.string()),
    reviewerName: v.optional(v.string()),
    reviewedAt: v.optional(v.number()),
    metadata: v.optional(v.any()),
  },
  handler: async (ctx, args) => {
    const existing = await ctx.db
      .query("reviews")
      .withIndex("by_pipeline_object", (q) =>
        q.eq("pipelineId", args.pipelineId).eq("objectId", args.objectId)
      )
      .first();

    const data = {
      pipelineId: args.pipelineId,
      objectId: args.objectId,
      label: args.label,
      aiLabel: args.aiLabel ?? "",
      aiReason: args.aiReason ?? "",
      humanNotes: args.humanNotes ?? "",
      reviewerName: args.reviewerName ?? "Houston",
      reviewedAt: args.reviewedAt ?? Date.now(),
      metadata: args.metadata ?? {},
    };

    if (existing) {
      await ctx.db.patch(existing._id, data);
      return existing._id;
    } else {
      return await ctx.db.insert("reviews", data);
    }
  },
});

export const update = mutation({
  args: {
    pipelineId: v.string(),
    objectId: v.string(),
    label: v.optional(v.string()),
    humanNotes: v.optional(v.string()),
    reviewedAt: v.optional(v.number()),
  },
  handler: async (ctx, args) => {
    const existing = await ctx.db
      .query("reviews")
      .withIndex("by_pipeline_object", (q) =>
        q.eq("pipelineId", args.pipelineId).eq("objectId", args.objectId)
      )
      .first();

    if (!existing) {
      throw new Error(`No review found for ${args.pipelineId}/${args.objectId}`);
    }

    const patch: Record<string, unknown> = {};
    if (args.label !== undefined) patch.label = args.label;
    if (args.humanNotes !== undefined) patch.humanNotes = args.humanNotes;
    patch.reviewedAt = args.reviewedAt ?? Date.now();

    await ctx.db.patch(existing._id, patch);
    return existing._id;
  },
});
