import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

// ──────────────────────────────────────────────────────────────────────
// papers_externalReviews — referee-report metadata (Gap #1, closed
// 2026-06-03).
//
// Distinct from r_rounds (which is the direct-vendor adversarial review
// pipeline). One row per report: Houston-paste from ChatGPT/Gemini/Grok,
// journal referees, arxiv endorser comments, or internal-stage3
// cross-vendor synthesis rollups.
//
// Counts (blocker/major/minor) are POST-TRUTH-AUDIT VERIFIED counts
// per feedback_peer_review_truth_audit_protocol — they reflect what
// actually held after we audited the raw reviewer counts, not the raw
// reviewer assertion.
// ──────────────────────────────────────────────────────────────────────

const sourceValidator = v.union(
  v.literal("journal"),
  v.literal("arxiv"),
  v.literal("houston-paste"),
  v.literal("colleague-private"),
  v.literal("internal-stage3")
);

const recommendationValidator = v.union(
  v.literal("accept"),
  v.literal("minor-revisions"),
  v.literal("major-revisions"),
  v.literal("reject"),
  v.literal("pending")
);

export const list = query({
  args: { paperSlug: v.string() },
  handler: async (ctx, args) => {
    const rows = await ctx.db
      .query("papers_externalReviews")
      .withIndex("by_paper", (q) => q.eq("paperSlug", args.paperSlug))
      .collect();
    rows.sort((a, b) => b.receivedAt.localeCompare(a.receivedAt));
    return rows;
  },
});

// Cross-paper aggregate keyed by slug — for site index pages.
export const listAll = query({
  handler: async (ctx) => {
    const rows = await ctx.db.query("papers_externalReviews").collect();
    const grouped: Record<string, typeof rows> = {};
    for (const row of rows) {
      if (!grouped[row.paperSlug]) grouped[row.paperSlug] = [];
      grouped[row.paperSlug].push(row);
    }
    for (const slug of Object.keys(grouped)) {
      grouped[slug].sort((a, b) => b.receivedAt.localeCompare(a.receivedAt));
    }
    return grouped;
  },
});

export const add = mutation({
  args: {
    paperSlug: v.string(),
    source: sourceValidator,
    reviewerLabel: v.string(),
    receivedAt: v.string(),
    blockerCount: v.number(),
    majorCount: v.number(),
    minorCount: v.number(),
    recommendation: recommendationValidator,
    rRoundId: v.optional(v.id("r_rounds")),
    pdfUrl: v.optional(v.string()),
    notes: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    return await ctx.db.insert("papers_externalReviews", args);
  },
});

// Idempotent upsert keyed by (paperSlug, reviewerLabel, receivedAt).
// Safe for seed-script re-runs.
export const upsertByLabelDate = mutation({
  args: {
    paperSlug: v.string(),
    source: sourceValidator,
    reviewerLabel: v.string(),
    receivedAt: v.string(),
    blockerCount: v.number(),
    majorCount: v.number(),
    minorCount: v.number(),
    recommendation: recommendationValidator,
    rRoundId: v.optional(v.id("r_rounds")),
    pdfUrl: v.optional(v.string()),
    notes: v.optional(v.string()),
    // The exact paper version this leg read. Record it on every new row —
    // publicationStatus:get uses it to prove a board covered the CURRENT PDF.
    paperVersionReviewed: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const rows = await ctx.db
      .query("papers_externalReviews")
      .withIndex("by_paper", (q) => q.eq("paperSlug", args.paperSlug))
      .collect();
    const existing = rows.find(
      (r) =>
        r.reviewerLabel === args.reviewerLabel && r.receivedAt === args.receivedAt
    );
    if (existing) {
      await ctx.db.patch(existing._id, args);
      return existing._id;
    }
    return await ctx.db.insert("papers_externalReviews", args);
  },
});

export const remove = mutation({
  args: { id: v.id("papers_externalReviews") },
  handler: async (ctx, args) => {
    await ctx.db.delete(args.id);
  },
});
