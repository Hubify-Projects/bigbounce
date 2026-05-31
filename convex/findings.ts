import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

export const listForPaper = query({
  args: {
    paperSlug: v.string(),
    status: v.optional(v.union(
      v.literal("open"),
      v.literal("in-progress"),
      v.literal("closed-by-real-action"),
      v.literal("closed-by-truth-audit-falsification"),
      v.literal("closed-by-artifact-verification"),
      v.literal("deferred-genuine")
    )),
  },
  handler: async (ctx, args) => {
    const all = await ctx.db
      .query("findings")
      .withIndex("by_paper", (q) => q.eq("paperSlug", args.paperSlug))
      .collect();
    if (args.status) return all.filter((f) => f.closureStatus === args.status);
    return all;
  },
});

export const listOpen = query({
  handler: async (ctx) => {
    const open = await ctx.db
      .query("findings")
      .withIndex("by_status", (q) => q.eq("closureStatus", "open"))
      .collect();
    const inProgress = await ctx.db
      .query("findings")
      .withIndex("by_status", (q) => q.eq("closureStatus", "in-progress"))
      .collect();
    return [...open, ...inProgress];
  },
});

export const listForRound = query({
  args: { roundId: v.id("r_rounds") },
  handler: async (ctx, args) => {
    return await ctx.db
      .query("findings")
      .withIndex("by_round", (q) => q.eq("roundId", args.roundId))
      .collect();
  },
});

export const create = mutation({
  args: {
    roundId: v.id("r_rounds"),
    paperSlug: v.string(),
    reviewerName: v.string(),
    findingId: v.string(),
    classification: v.union(
      v.literal("BLOCKER"),
      v.literal("MAJOR"),
      v.literal("MINOR"),
      v.literal("NIT")
    ),
    location: v.string(),
    claim: v.string(),
    proposedFix: v.string(),
  },
  handler: async (ctx, args) => {
    return await ctx.db.insert("findings", {
      ...args,
      closureStatus: "open",
    });
  },
});

// Apply truth-audit verdict per feedback_peer_review_truth_audit_protocol.
// MUST run before closure work. The verdict determines whether the next step
// is real-action closure or audit-only closure.
export const truthAudit = mutation({
  args: {
    findingId: v.id("findings"),
    verdict: v.union(
      v.literal("VERIFIED"),
      v.literal("FALSIFIED"),
      v.literal("STALE"),
      v.literal("OUT-OF-SCOPE"),
      v.literal("OPINION")
    ),
    evidence: v.string(),
  },
  handler: async (ctx, args) => {
    await ctx.db.patch(args.findingId, {
      truthAuditVerdict: args.verdict,
      truthAuditEvidence: args.evidence,
      closureStatus: "in-progress",
    });
  },
});

export const close = mutation({
  args: {
    findingId: v.id("findings"),
    closureStatus: v.union(
      v.literal("closed-by-real-action"),
      v.literal("closed-by-truth-audit-falsification"),
      v.literal("closed-by-artifact-verification"),
      v.literal("deferred-genuine")
    ),
    closureCommit: v.optional(v.string()),
    closureArtifact: v.optional(v.string()),
    closureNote: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    await ctx.db.patch(args.findingId, {
      closureStatus: args.closureStatus,
      closureCommit: args.closureCommit,
      closureArtifact: args.closureArtifact,
      closureNote: args.closureNote,
      closedAt: Date.now(),
    });
  },
});
