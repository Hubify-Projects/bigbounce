import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  // ── Review System ──
  reviews: defineTable({
    pipelineId: v.string(),
    objectId: v.string(),
    label: v.string(),
    aiLabel: v.string(),
    aiReason: v.string(),
    humanNotes: v.string(),
    reviewerName: v.string(),
    reviewedAt: v.number(),
    metadata: v.any(),
  })
    .index("by_pipeline", ["pipelineId"])
    .index("by_pipeline_object", ["pipelineId", "objectId"]),

  checklistItems: defineTable({
    pipelineId: v.string(),
    category: v.string(),
    text: v.string(),
    status: v.string(),
    updatedAt: v.number(),
  }).index("by_pipeline", ["pipelineId"]),

  pipelineState: defineTable({
    pipelineId: v.string(),
    name: v.string(),
    status: v.string(),
    gatesPassed: v.number(),
    totalGates: v.number(),
    lastUpdated: v.number(),
    summary: v.string(),
  }).index("by_pipeline", ["pipelineId"]),

  models: defineTable({
    pipelineId: v.string(),
    modelName: v.string(),
    version: v.string(),
    huggingfaceUrl: v.string(),
    trainingSamples: v.number(),
    metrics: v.any(),
    createdAt: v.number(),
  }).index("by_pipeline", ["pipelineId"]),

  // ── Chat Logging ──
  chatMessages: defineTable({
    sessionId: v.string(),
    role: v.string(),
    content: v.string(),
    pageContext: v.optional(v.object({
      title: v.optional(v.string()),
      path: v.optional(v.string()),
    })),
    ipHash: v.optional(v.string()),
    timestamp: v.number(),
  })
    .index("by_session", ["sessionId", "timestamp"])
    .index("by_timestamp", ["timestamp"]),

  // ── Activity Feed ──
  activityFeed: defineTable({
    type: v.string(),
    date: v.string(),
    title: v.string(),
    body: v.string(),
    tags: v.array(v.object({
      label: v.string(),
      kind: v.string(),
    })),
    createdAt: v.number(),
  }).index("by_date", ["createdAt"]),

  // ── MCMC Convergence Status ──
  mcmcStatus: defineTable({
    dataset: v.string(),
    rhat: v.any(),
    ess: v.any(),
    drift: v.any(),
    parameterMeans: v.any(),
    converged: v.boolean(),
    timestamp: v.number(),
  })
    .index("by_dataset", ["dataset", "timestamp"]),

  // ── Page Analytics ──
  pageViews: defineTable({
    path: v.string(),
    referrer: v.optional(v.string()),
    sessionHash: v.optional(v.string()),
    timestamp: v.number(),
  }).index("by_path", ["path", "timestamp"])
    .index("by_timestamp", ["timestamp"]),
});
