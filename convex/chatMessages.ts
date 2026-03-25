import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

export const log = mutation({
  args: {
    sessionId: v.string(),
    role: v.string(),
    content: v.string(),
    pageContext: v.optional(v.object({
      title: v.optional(v.string()),
      path: v.optional(v.string()),
    })),
    ipHash: v.optional(v.string()),
    timestamp: v.optional(v.number()),
  },
  handler: async (ctx, args) => {
    return await ctx.db.insert("chatMessages", {
      sessionId: args.sessionId,
      role: args.role,
      content: args.content.slice(0, 10000),
      pageContext: args.pageContext,
      ipHash: args.ipHash,
      timestamp: args.timestamp ?? Date.now(),
    });
  },
});

export const recent = query({
  args: {
    limit: v.optional(v.number()),
  },
  handler: async (ctx, args) => {
    const limit = args.limit ?? 100;
    return await ctx.db
      .query("chatMessages")
      .withIndex("by_timestamp")
      .order("desc")
      .take(limit);
  },
});

export const bySession = query({
  args: { sessionId: v.string() },
  handler: async (ctx, args) => {
    return await ctx.db
      .query("chatMessages")
      .withIndex("by_session", (q) => q.eq("sessionId", args.sessionId))
      .collect();
  },
});

export const sessions = query({
  args: {
    limit: v.optional(v.number()),
  },
  handler: async (ctx, args) => {
    const limit = args.limit ?? 50;
    const messages = await ctx.db
      .query("chatMessages")
      .withIndex("by_timestamp")
      .order("desc")
      .take(1000);

    // Group by session, return most recent message per session
    const sessionMap = new Map<string, {
      sessionId: string;
      lastMessage: string;
      lastRole: string;
      messageCount: number;
      lastTimestamp: number;
      firstTimestamp: number;
      pageContext?: { title?: string; path?: string };
    }>();

    for (const msg of messages) {
      const existing = sessionMap.get(msg.sessionId);
      if (!existing) {
        sessionMap.set(msg.sessionId, {
          sessionId: msg.sessionId,
          lastMessage: msg.content.slice(0, 200),
          lastRole: msg.role,
          messageCount: 1,
          lastTimestamp: msg.timestamp,
          firstTimestamp: msg.timestamp,
          pageContext: msg.pageContext,
        });
      } else {
        existing.messageCount++;
        if (msg.timestamp < existing.firstTimestamp) {
          existing.firstTimestamp = msg.timestamp;
        }
      }
    }

    return Array.from(sessionMap.values())
      .sort((a, b) => b.lastTimestamp - a.lastTimestamp)
      .slice(0, limit);
  },
});

export const stats = query({
  args: {},
  handler: async (ctx) => {
    const now = Date.now();
    const dayAgo = now - 86400000;
    const weekAgo = now - 604800000;

    const allRecent = await ctx.db
      .query("chatMessages")
      .withIndex("by_timestamp")
      .order("desc")
      .take(5000);

    const total = allRecent.length;
    const last24h = allRecent.filter((m) => m.timestamp > dayAgo).length;
    const last7d = allRecent.filter((m) => m.timestamp > weekAgo).length;

    const sessions = new Set(allRecent.map((m) => m.sessionId));
    const sessionsToday = new Set(
      allRecent.filter((m) => m.timestamp > dayAgo).map((m) => m.sessionId)
    );

    return {
      totalMessages: total,
      messagesLast24h: last24h,
      messagesLast7d: last7d,
      totalSessions: sessions.size,
      sessionsToday: sessionsToday.size,
    };
  },
});
