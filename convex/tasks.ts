import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

export const list = query({
  args: {
    status: v.optional(v.union(
      v.literal("pending"),
      v.literal("in-progress"),
      v.literal("blocked"),
      v.literal("done")
    )),
    owner: v.optional(v.union(v.literal("agent"), v.literal("houston"))),
    paperSlug: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    let all = await ctx.db.query("tasks").collect();
    if (args.status) all = all.filter((t) => t.status === args.status);
    if (args.owner) all = all.filter((t) => t.owner === args.owner);
    if (args.paperSlug) all = all.filter((t) => t.paperSlug === args.paperSlug);
    return all;
  },
});

export const create = mutation({
  args: {
    paperSlug: v.optional(v.string()),
    title: v.string(),
    description: v.string(),
    priority: v.union(v.literal("P0"), v.literal("P1"), v.literal("P2")),
    owner: v.union(v.literal("agent"), v.literal("houston")),
  },
  handler: async (ctx, args) => {
    return await ctx.db.insert("tasks", {
      ...args,
      status: "pending",
      createdAt: Date.now(),
    });
  },
});

export const setStatus = mutation({
  args: {
    taskId: v.id("tasks"),
    status: v.union(
      v.literal("pending"),
      v.literal("in-progress"),
      v.literal("blocked"),
      v.literal("done")
    ),
    closureCommit: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const patch: Record<string, unknown> = { status: args.status };
    if (args.status === "done") {
      patch.closedAt = Date.now();
      if (args.closureCommit) patch.closureCommit = args.closureCommit;
    }
    await ctx.db.patch(args.taskId, patch);
  },
});
