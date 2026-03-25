import { query } from "./_generated/server";
import { v } from "convex/values";

// Query feedback stored as chatMessages with sessionId prefix "feedback_"
export const recent = query({
  args: { limit: v.optional(v.number()) },
  handler: async (ctx, args) => {
    const messages = await ctx.db
      .query("chatMessages")
      .withIndex("by_timestamp")
      .order("desc")
      .take(args.limit ?? 200);
    return messages.filter((m) => m.sessionId.startsWith("feedback_"));
  },
});

export const summary = query({
  args: {},
  handler: async (ctx) => {
    const messages = await ctx.db
      .query("chatMessages")
      .withIndex("by_timestamp")
      .order("desc")
      .take(5000);
    const feedback = messages.filter((m) => m.sessionId.startsWith("feedback_"));
    const byPage = new Map<string, { up: number; down: number }>();
    for (const f of feedback) {
      const page = f.sessionId.replace("feedback_", "");
      if (!byPage.has(page)) byPage.set(page, { up: 0, down: 0 });
      const entry = byPage.get(page)!;
      if (f.content === "up") entry.up++;
      else if (f.content === "down") entry.down++;
    }
    return Array.from(byPage.entries()).map(([page, counts]) => ({
      page,
      ...counts,
    }));
  },
});
