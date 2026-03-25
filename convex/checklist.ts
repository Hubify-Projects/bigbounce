import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

export const byPipeline = query({
  args: { pipelineId: v.string() },
  handler: async (ctx, args) => {
    return await ctx.db
      .query("checklistItems")
      .withIndex("by_pipeline", (q) => q.eq("pipelineId", args.pipelineId))
      .collect();
  },
});

export const save = mutation({
  args: {
    pipelineId: v.string(),
    category: v.string(),
    text: v.string(),
    status: v.string(),
    updatedAt: v.optional(v.number()),
  },
  handler: async (ctx, args) => {
    // Find existing by pipelineId + category + text
    const all = await ctx.db
      .query("checklistItems")
      .withIndex("by_pipeline", (q) => q.eq("pipelineId", args.pipelineId))
      .collect();

    const existing = all.find(
      (item) => item.category === args.category && item.text === args.text
    );

    const data = {
      pipelineId: args.pipelineId,
      category: args.category,
      text: args.text,
      status: args.status,
      updatedAt: args.updatedAt ?? Date.now(),
    };

    if (existing) {
      await ctx.db.patch(existing._id, data);
      return existing._id;
    } else {
      return await ctx.db.insert("checklistItems", data);
    }
  },
});

export const updateStatus = mutation({
  args: {
    id: v.id("checklistItems"),
    status: v.string(),
  },
  handler: async (ctx, args) => {
    await ctx.db.patch(args.id, {
      status: args.status,
      updatedAt: Date.now(),
    });
  },
});
