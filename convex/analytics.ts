import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

export const logView = mutation({
  args: {
    path: v.string(),
    referrer: v.optional(v.string()),
    sessionHash: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    return await ctx.db.insert("pageViews", {
      path: args.path,
      referrer: args.referrer,
      sessionHash: args.sessionHash,
      timestamp: Date.now(),
    });
  },
});

export const topPages = query({
  args: { days: v.optional(v.number()) },
  handler: async (ctx, args) => {
    const cutoff = Date.now() - (args.days ?? 7) * 86400000;
    const views = await ctx.db
      .query("pageViews")
      .withIndex("by_timestamp")
      .order("desc")
      .take(10000);

    const filtered = views.filter((v) => v.timestamp > cutoff);
    const counts = new Map<string, number>();
    for (const view of filtered) {
      counts.set(view.path, (counts.get(view.path) ?? 0) + 1);
    }

    return Array.from(counts.entries())
      .map(([path, count]) => ({ path, count }))
      .sort((a, b) => b.count - a.count);
  },
});

export const stats = query({
  args: {},
  handler: async (ctx) => {
    const now = Date.now();
    const dayAgo = now - 86400000;
    const weekAgo = now - 604800000;

    const views = await ctx.db
      .query("pageViews")
      .withIndex("by_timestamp")
      .order("desc")
      .take(10000);

    return {
      totalViews: views.length,
      viewsLast24h: views.filter((v) => v.timestamp > dayAgo).length,
      viewsLast7d: views.filter((v) => v.timestamp > weekAgo).length,
      uniqueSessionsLast7d: new Set(
        views.filter((v) => v.timestamp > weekAgo && v.sessionHash).map((v) => v.sessionHash)
      ).size,
    };
  },
});
