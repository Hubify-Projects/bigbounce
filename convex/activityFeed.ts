import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

export const list = query({
  args: {
    limit: v.optional(v.number()),
  },
  handler: async (ctx, args) => {
    const limit = args.limit ?? 50;
    return await ctx.db
      .query("activityFeed")
      .withIndex("by_date")
      .order("desc")
      .take(limit);
  },
});

export const add = mutation({
  args: {
    type: v.string(),
    date: v.string(),
    title: v.string(),
    body: v.string(),
    tags: v.array(v.object({
      label: v.string(),
      kind: v.string(),
    })),
  },
  handler: async (ctx, args) => {
    return await ctx.db.insert("activityFeed", {
      type: args.type,
      date: args.date,
      title: args.title,
      body: args.body,
      tags: args.tags,
      createdAt: Date.now(),
    });
  },
});

export const remove = mutation({
  args: { id: v.id("activityFeed") },
  handler: async (ctx, args) => {
    await ctx.db.delete(args.id);
  },
});
